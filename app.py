import streamlit as st
import random
from datetime import datetime
import streamlit.components.v1 as components  

from stimuly import build_profiles, NUM_PROFILES_PER_PARTICIPANT
from sheets_utils import append_response_to_sheet
from ui_helpers import apply_global_styles, scroll_to_top, render_profile_card

st.set_page_config(
    page_title="Dating Profile Study",
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

    st.markdown('<div class="big-title">Dating Study 💘</div>', unsafe_allow_html=True)

    st.markdown("""
    **Consent & Study Info**  
    You are invited to take part in a short research study about online dating profiles.

    You will see fictional profiles and rate their attractiveness, authenticity,  
    and desirability.

    - Takes **5–10 minutes**  
    - **Anonymous** & **voluntary**  
    """)

    agree = st.checkbox("I agree to participate.")
    if agree and st.button("Start the study"):
        unique_id = f"PID_{int(datetime.utcnow().timestamp())}_{random.randint(1000, 9999)}"
        st.session_state.participant_id = unique_id
        st.rerun()

    st.stop()


# ---------- Demographics ----------
def demographics_screen():
    if st.session_state.demographics is not None:
        return

    st.markdown('<div class="section-header">A few quick questions</div>', unsafe_allow_html=True)

    age = st.number_input("Age", min_value=18, max_value=99, value=24)
    gender = st.selectbox("Your gender", ["Prefer not to say", "Woman", "Man", "Non-binary", "Other"])
    attraction = st.selectbox("You are usually attracted to:", ["Men", "Women", "Both"])

    if st.button("Continue to profiles"):
        st.session_state.demographics = {
            "age": int(age),
            "gender": gender,
            "attraction": attraction,
        }

        # Build profiles with fixed-choice attributes
        profiles = build_profiles(attraction)
        chosen = random.sample(profiles, NUM_PROFILES_PER_PARTICIPANT)

        # Assign 50/50 control/treatment
        conditions = ["control"] * 5 + ["ai_disclosed"] * 5
        random.shuffle(conditions)

        stimulus_list = []
        for prof, cond in zip(chosen, conditions):
            stimulus_list.append(
                {
                    "profile_id": prof["profile_id"],
                    "image_url": prof["image_url"],
                    "bio": prof["bio"],
                    "fixed_choice": prof["fixed_choice"],   # <-- IMPORTANT
                    "condition": cond,
                }
            )

        random.shuffle(stimulus_list)
        st.session_state.stimulus_list = stimulus_list
        st.session_state.current_index = 0
        st.rerun()

    st.stop()


# ---------- Attention Check ----------
def attention_check_step():
    scroll_to_top()

    st.markdown("### Attention Check ⚠️")
    st.write("Please choose **3** for all answers below.")

    att1 = st.slider("Attractiveness", 0, 4, 2, key="attn_attr")
    att2 = st.slider("Authenticity",   0, 4, 2, key="attn_auth")
    att3 = st.slider("Desirability",   0, 4, 2, key="attn_desi")

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

        components.html(
            "<script>window.parent.scrollTo({top: 0, behavior: 'auto'});</script>",
            height=0,
        )

        st.session_state.current_index += 1
        st.rerun()

    st.stop()


# ---------- Rating Screen ----------
def profile_step(idx: int, stimuli, total_profiles: int):
    scroll_to_top()

    current = stimuli[idx]

    # Header
    st.markdown(f"**Profile {idx + 1} of {total_profiles}**")

    # ---- Render full card including fixed-choice ----
    render_profile_card(current)



    # ---- Rating sliders ----
    st.markdown('<div class="rating-title">Rate this profile</div>', unsafe_allow_html=True)

    attr = st.slider("Attractiveness", 0, 4, 2, key=f"attr_{idx}")
    auth = st.slider("Authenticity",   0, 4, 2, key=f"auth_{idx}")
    desi = st.slider("Desirability",   0, 4, 2, key=f"desi_{idx}")

    if st.button("Next"):
        row = {
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

        st.session_state.responses.append(row)
        append_response_to_sheet(row)

        components.html(
            "<script>window.parent.scrollTo({top: 0, behavior: 'auto'});</script>",
            height=0,
        )

        st.session_state.current_index += 1
        st.rerun()


# ---------- Experiment Flow ----------
def main_experiment():
    stimuli = st.session_state.stimulus_list
    idx = st.session_state.current_index

    if not stimuli:
        st.error("No stimuli found.")
        st.stop()

    total = len(stimuli)
    total_steps = total + 1

    if idx >= total_steps:
        st.success("All done! Thank you 🙏")
        st.stop()

    if idx == 3:
        attention_check_step()
    elif idx < 3:
        profile_step(idx, stimuli, total)
    else:
        profile_step(idx - 1, stimuli, total)


# ---------- Main ----------
def main():
    consent_screen()
    demographics_screen()
    main_experiment()

if __name__ == "__main__":
    main()
