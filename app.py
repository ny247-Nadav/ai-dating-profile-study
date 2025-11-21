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
    st.title("AI in Dating Profiles Study 💘")

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
    if agree:
        pid = st.text_input(
            "Please create a simple participant ID (e.g., your initials + 3 digits):"
        )

        if pid:
            st.session_state.participant_id = pid.strip()
            st.rerun()

    st.stop()

# ---------- 4. Demographics Screen ----------

if st.session_state.demographics is None:
    st.header("A few quick questions")

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

st.write(f"Profile {idx + 1} of {len(stimuli)}")

# Show image (same for all)
if current["image_url"]:
    st.image(current["image_url"], use_column_width=True)

st.markdown(f"**Bio:** {current['bio']}")

if current["condition"] == "ai_disclosed":
    st.markdown("> 🔍 *This profile includes AI-assisted enhancements.*")

st.markdown("---")
st.subheader("Please rate this profile")

attr = st.slider("Attractiveness (0 = not at all, 4 = very much)", 0, 4, 2)
auth = st.slider("Authenticity (0–4)", 0, 4, 2)
desi = st.slider("Desirability (0–4)", 0, 4, 2)

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
