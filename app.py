import streamlit as st
import random
import pandas as pd
from datetime import datetime
import os

st.set_page_config(
    page_title="AI Dating Profile Study",
    page_icon="💘",
    layout="centered"
)

# ---------- Global Styling ----------

st.markdown(
    """
    <style>
    .main {
        max-width: 900px;
        margin: 0 auto;
        font-size: 18px;
    }
    .big-title {
        font-size: 32px !important;
        font-weight: 700 !important;
    }
    .section-header {
        font-size: 24px !important;
        font-weight: 600 !important;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }
    .rating-title {
        font-size: 22px !important;
        font-weight: 600 !important;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    .ai-label {
        color: #1f6feb;
        font-weight: 700;
        font-size: 18px;
        padding: 0.4rem 0.6rem;
        border-radius: 6px;
        background-color: #e8f0ff;
        display: inline-block;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }
    .min-max-labels {
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        color: #555;
        margin-top: -8px;
        margin-bottom: 4px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- 1. Define Stimuli ----------

IMAGE_URL = "https://fortune.com/img-assets/wp-content/uploads/2025/05/GettyImages-2215203788-e1747765808923.jpg?w=1440&q=75"
BIO_TEXT = "King of the US, looking for a nice woman"

# 20 dummy profiles, same image + same bio, different IDs
PROFILES = [
    {
        "profile_id": f"p{i}",
        "gender": "unspecified",
        "image_url": IMAGE_URL,
        "bio": BIO_TEXT,
    }
    for i in range(1, 21)
]

NUM_PROFILES_PER_PARTICIPANT = 10   # 5 control + 5 AI-disclosed

# ---------- 2. Init session state ----------

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

# ---------- 3. Consent / Start Screen ----------

if st.session_state.participant_id is None:
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
        # Auto-generate a participant ID
        unique_id = f"PID_{int(datetime.utcnow().timestamp())}_{random.randint(1000, 9999)}"
        st.session_state.participant_id = unique_id
        st.rerun()

    st.stop()

# ---------- 4. Demographics Screen ----------

if st.session_state.demographics is None:
    st.markdown('<div class="section-header">A few quick questions</div>', unsafe_allow_html=True)

    age = st.number_input("Age", min_value=18, max_value=99, step=1, value=24)
    gender = st.selectbox(
        "Your gender",
        ["Prefer not to say", "Woman", "Man", "Non-binary", "Other"],
    )
    attraction = st.multiselect(
        "Which gender(s) are you typically attracted to?",
        ["Women", "Men", "Non-binary people", "Other"],
    )

    if st.button("Continue to profiles"):
        st.session_state.demographics = {
            "age": int(age),
            "gender": gender,
            "attraction": attraction,
        }

        # ---------- 5. Create Randomized Stimulus List ----------
        # Randomly pick 10 profiles from the 20
        chosen_profiles = random.sample(PROFILES, NUM_PROFILES_PER_PARTICIPANT)

        # Assign 5 control, 5 AI-disclosed
        conditions = ["control"] * 5 + ["ai_disclosed"] * 5
        random.shuffle(conditions)

        stimulus_list = []
        for prof, cond in zip(chosen_profiles, conditions):
            stimulus_list.append({
                "profile_id": prof["profile_id"],
                "image_url": prof["image_url"],
                "bio": prof["bio"],
                "condition": cond,
            })

        # Randomize presentation order
        random.shuffle(stimulus_list)
        st.session_state.stimulus_list = stimulus_list
        st.session_state.current_index = 0

        st.rerun()

    st.stop()

# ---------- 6. Main Rating Loop ----------

stimuli = st.session_state.stimulus_list
idx = st.session_state.current_index

# Safety check: if something went wrong and the list is empty
if not stimuli:
    st.error("No stimuli available. Please reload the page.")
    st.stop()

# Finished all stimuli
if idx >= len(stimuli):
    st.success("Thank you! You have completed all profiles. You may close this window now.")

    # Save data to CSV
    df = pd.DataFrame(st.session_state.responses)

    # Append mode with header only if file doesn't exist yet
    filename = "responses.csv"
    file_exists = os.path.isfile(filename)
    df.to_csv(filename, mode="a", header=not file_exists, index=False)

    st.write("Your responses have been recorded.")
    st.stop()

current = stimuli[idx]

# ---------- Progress Bar ----------
st.write(f"Progress: {idx+1} / {len(stimuli)}")
progress = (idx + 1) / len(stimuli)
st.progress(progress)

# ---------- Attention Check at Profile 4 (idx == 3) ----------
if idx == 3:
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
            "attraction": "|".join(st.session_state.demographics["attraction"]),
            "profile_id": "attention_check",
            "condition": "attention_check",
            "attractiveness": att1,
            "authenticity": att2,
            "desirability": att3,
            "attention_correct": (att1 == 3 and att2 == 3 and att3 == 3),
        }
        st.session_state.responses.append(response)
        st.session_state.current_index += 1
        st.rerun()

    st.stop()

# ---------- Regular Profile Rating ----------

st.markdown(f"**Profile {idx + 1} of {len(stimuli)}**")

# Show image (same for all)
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

# Sliders with forced reset (key = profile index)
st.markdown("**Attractiveness**")
attr = st.slider("Attractiveness", 0, 4, 2, key=f"attr_{idx}", label_visibility="collapsed")
st.markdown('<div class="min-max-labels"><span>0</span><span>4</span></div>', unsafe_allow_html=True)

st.markdown("**Authenticity**")
auth = st.slider("Authenticity", 0, 4, 2, key=f"auth_{idx}", label_visibility="collapsed")
st.markdown('<div class="min-max-labels"><span>0</span><span>4</span></div>', unsafe_allow_html=True)

st.markdown("**Desirability**")
desi = st.slider("Desirability", 0, 4, 2, key=f"desi_{idx}", label_visibility="collapsed")
st.markdown('<div class="min-max-labels"><span>0</span><span>4</span></div>', unsafe_allow_html=True)

if st.button("Next"):
    response = {
        "timestamp": datetime.utcnow().isoformat(),
        "participant_id": st.session_state.participant_id,
        "age": st.session_state.demographics["age"],
        "gender": st.session_state.demographics["gender"],
        "attraction": "|".join(st.session_state.demographics["attraction"]),
        "profile_id": current["profile_id"],
        "condition": current["condition"],
        "attractiveness": attr,
        "authenticity": auth,
        "desirability": desi,
    }
    st.session_state.responses.append(response)
    st.session_state.current_index += 1
    st.rerun()
