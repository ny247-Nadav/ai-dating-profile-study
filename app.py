import streamlit as st
import random
from datetime import datetime

from stimuli import build_profiles, NUM_PROFILES_PER_PARTICIPANT
from sheets_utils import append_response_to_sheet
from ui_helpers import apply_global_styles, scroll_to_top, show_progress

st.set_page_config(
    page_title="AI Dating Profile Study",
    page_icon="💘",
    layout="centered"
)

apply_global_styles()


# ---------- Session Init ----------

def init_session():
    if "participant_id" not in st.session_state:
        st.session_state.participant_id = None
    if "demographics" not in st.session_state:
        st.session_state.demographics = None
    if "stimulus_list" not in st.session_state:
        st.session_state.stimulus_list = []
    if "current_index" not in st.session_state:
        st.session_state.current_index = 0
    if "responses" not in st.session_state:
        st.session_state.responses = []


init_session()


# ---------- Consent Screen ----------

def consent_screen():
    if st.session_state.participant_id is not None:
        return

    st.markdown('<div class="big-title">AI in Dating Profiles Study 💘</div>', unsafe_allow_html=True)

    st.markdown("""
    **Consent & Study Info**

    You are invited to take part in a short research study about online dating profiles
    and AI-assisted content. You will see a series of fictional dating profiles and
    rate how attractive, authentic, and desirable you find them.

    - The study should take about **5–10 minutes**.  
    - Participation is **voluntary** and **anonymous**.  
    - You may stop at any time by closing this window.

    If you agree to participate, please continue below.
    """)

    agree = st.checkbox("I have read the information above and agree to participate.")
    if agree and st.button("Start the study"):
        unique_id = f"PID_{int(datetime.utcnow().timestamp())}_{random.randint(1000, 9999)}"
        st.session_state.participant_id = unique_id
        st.rerun()

    st.stop()


# ---------- Demographics Screen ----------

def demographics_screen():
    if st.session_state.demographics is not None:
        return

    st.markdown('<div class="section-header">A few quick questions</div>', unsafe_allow_html=True)

    age = st.number_input("Age", min_value=18, max_value=99, step=1, value=24)
    gender = st.selectbox(
        "Your gender",
        ["Prefer not to say", "Woman", "Man", "Non-binary", "Other"],
    )
    attraction = st.selectbox(
        "Which gender(s) are you typically attracted to?",
        ["Men", "Women", "Both"],
    )

    if st.button("Continue to profiles"):
        st.session_state.demographics = {
            "age": int(age),
            "gender": gender,
            "attraction": attraction,
        }

        profiles = build_profiles(attraction)
        chosen_profiles = random.sample(profiles, NUM_PROFILES_PER_PARTICIPANT)

        # Assign 5 control, 5 AI-disclosed
        conditions = ["control"] * 5 + ["ai_disclosed"] * 5
        random.shuffle(conditions)

        stimulus_list = []
        for prof, cond in zip(chosen_profiles, conditions):
            stimulus_list.append(
                {
                    "profile_id": prof["profile_id"],
                    "image_url": prof["image_url"],
                    "bio": prof["bio"],
                    "condition": cond,
                }
            )

        random.shuffle(stimulus_list)
        st.session_state.stimulus_list = stimulus_list
        st.session_state.current_index = 0

        st.rerun()

    st.stop()


# ---------- Attention Check Screen ----------

def attention_check_step():
    st.markdown("### Attention Check ⚠️")
    st.write("""
    To confirm you're paying attention,  
    **please select the rating '3' for all three questions below.**
    """)

    att1 = st.slider("Attractiveness", 0, 4, 2, key="attn_attr", label_visibility="collapsed")
    st.markdown('<div class="min-max-labels"><span>0</span><span>4</span></div>', unsafe_allow_html=True)

    att2 = st.slider("Authenticity", 0, 4, 2, key="attn_auth", label_visibility="collapsed")
    st.markdown('<div class="min-max-labels"><span>0</span><span>4</span></div>', unsafe_allow_html=True)

    att3 = st.slider("Desirability", 0, 4, 2, key="attn_desi", label_visibility="collapsed")
    st.markdown('<div class="min-max-labels"><span>0</span><span>4</span></div>', unsafe_allow_html=True)

    if st.button("Next"):
        response = {
            "timestamp": datetime.utcnow().isoformat(),
            "participant_id": st.session_state.participant_id,
            "age": st.session_state.demographics["age"],
            "gender": st.session_state.demographics["gender"],
            "attraction": st.session_state.demographics["attraction"],
            "profile_id": "attention_check",
            "condition": "attention_check",
            "attractiveness": att1,
            "authenticity": att2,
            "desirability": att3,
            "attention_check": True,
            "attention_correct": (att1 == 3 and att2 == 3 and att3 == 3),
        }
        st.session_state.responses.append(response)
        append_response_to_sheet(response)
        st.session_state.current_index += 1
        st.rerun()

    st.stop()


# ---------- Profile Rating Screen ----------

def profile_step(profile_idx: int, stimuli, total_profiles: int, total_steps: int):
    current = stimuli[profile_idx]

    # Scroll to top every profile
    scroll_to_top()

    show_progress(st.session_state.current_index, total_steps)

    st.markdown(f"**Profile {profile_idx + 1} of {total_profiles}**")

    if current["image_url"]:
        st.image(current["image_url"], use_container_width=True)

    st.markdown(f"**Bio:** {current['bio']}")

    if current["condition"] == "ai_disclosed":
        st.markdown(
            '<div class="ai-label">✨ <strong>This profile includes AI-assisted enhancements.</strong> ✨</div>',
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown(
        '<div class="rating-title">Please rate this profile (0 = not at all, 4 = very much)</div>',
        unsafe_allow_html=True,
    )

    st.markdown("**Attractiveness**")
    attr = st.slider("Attractiveness", 0, 4, 2, key=f"attr_{profile_idx}", label_visibility="collapsed")
    st.markdown('<div class="min-max-labels"><span>0</span><span>4</span></div>', unsafe_allow_html=True)

    st.markdown("**Authenticity**")
    auth = st.slider("Authenticity", 0, 4, 2, key=f"auth_{profile_idx}", label_visibility="collapsed")
    st.markdown('<div class="min-max-labels"><span>0</span><span>4</span></div>', unsafe_allow_html=True)

    st.markdown("**Desirability**")
    desi = st.slider("Desirability", 0, 4, 2, key=f"desi_{profile_idx}", label_visibility="collapsed")
    st.markdown('<div class="min-max-labels"><span>0</span><span>4</span></div>', unsafe_allow_html=True)

    if st.button("Next"):
        response = {
            "timestamp": datetime.utcnow().isoformat(),
            "participant_id": st.session_state.participant_id,
            "age": st.session_state.demographics["age"],
            "gender": st.session_state.demographics["gender"],
            "attraction": st.session_state.demographics["attraction"],
            "profile_id": current["profile_id"],
            "condition": current["condition"],
            "attractiveness": attr,
            "authenticity": auth,
            "desirability": desi,
            "attention_check": False,
            "attention_correct": "",
        }
        st.session_state.responses.append(response)
        append_response_to_sheet(response)
        st.session_state.current_index += 1
        st.rerun()


# ---------- Main Experiment Flow ----------

def main_experiment():
    stimuli = st.session_state.stimulus_list
    idx = st.session_state.current_index

    # Safety check
    if not stimuli:
        st.error("No stimuli available. Please reload the page.")
        st.stop()

    total_profiles = len(stimuli)          # 10
    total_steps = total_profiles + 1       # +1 for attention check = 11

    # Finished all steps
    if idx >= total_steps:
        st.success("Thank you! You have completed all profiles. You may close this window now.")
        st.write("Your responses have been recorded.")
        st.stop()

    # Map current index to either profile or attention check
    if idx < 3:
        # first 3 profiles
        profile_idx = idx
        scroll_to_top()
        show_progress(idx, total_steps)
        profile_step(profile_idx, stimuli, total_profiles, total_steps)

    elif idx == 3:
        # attention check
        scroll_to_top()
        show_progress(idx, total_steps)
        attention_check_step()

    else:
        # remaining profiles: map idx 4..10 -> profile 3..9
        profile_idx = idx - 1
        scroll_to_top()
        show_progress(idx, total_steps)
        profile_step(profile_idx, stimuli, total_profiles, total_steps)


# ---------- App Entry ----------

def main():
    consent_screen()
    demographics_screen()
    main_experiment()


if __name__ == "__main__":
    main()
