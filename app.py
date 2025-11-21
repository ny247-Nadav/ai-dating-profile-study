import streamlit as st
import random
import pandas as pd
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

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

BIOS = [
    "Teacher by day, amateur chef by night. I love quiet coffee shops, long walks, and Sunday brunch with friends. Looking for someone kind, grounded, and ready to laugh at bad puns.",
    "Tech worker who escapes screens with books, live music, and weekend hikes. I value honesty, curiosity, and good communication. Let’s see if we can make each other’s playlists better.",
    "NYC transplant who still gets excited about the skyline. Into movies, board games, and exploring new neighborhoods. Looking for a caring partner who enjoys both going out and staying in.",
    "Big fan of cozy dinners, wandering through museums, and talking about everything from podcasts to politics. Friends describe me as thoughtful, reliable, and a good listener.",
    "Fitness is my reset button—runs in the park, yoga classes, and trying new healthy recipes. I’m looking for someone warm, supportive, and open-minded about life and relationships.",
    "I love hosting friends, making way too much pasta, and discovering small local spots. Family and close friendships are a big part of my life. Looking for someone genuine and kind.",
    "Book lover, plant caretaker, and frequent movie re-watcher. I appreciate people who are emotionally mature, honest, and not afraid of real conversations.",
    "Weekdays are busy with work, but I always make time for friends, music, and good food. I’m hoping to meet someone who is thoughtful, affectionate, and looking for something real.",
    "I’m a mix of introvert and extrovert: I love evenings out with friends but also love quiet nights in. Looking for someone respectful, communicative, and emotionally intelligent.",
    "I enjoy traveling when I can, but I’m just as happy discovering new corners of my own city. I value kindness, stability, and a shared sense of humor.",
    "I’m close with my family and deeply value loyalty and support. My ideal evening is cooking together, sharing stories, and finding reasons to laugh about the day.",
    "Curious by nature—I love learning new things, whether it’s a recipe, a podcast topic, or a new neighborhood. Looking for a partner who is kind, patient, and open-hearted.",
    "Concerts, bookstores, and late-night conversations are my favorite kind of weekend. I appreciate people who are sincere, steady, and comfortable being themselves.",
    "I’m pretty grounded: I enjoy my work, take care of my people, and make time for small joys like coffee walks and sunsets. Hoping to meet someone who feels the same.",
    "I like to keep things balanced: staying active, seeing friends, and leaving space to just breathe. Looking for someone caring, thoughtful, and emotionally aware.",
    "I love trying new restaurants, discovering hidden parks, and planning small getaways. My ideal match is empathetic, communicative, and ready to build something meaningful.",
    "Friends would say I’m reliable, easygoing, and quietly funny. I’m happiest when I’m with good company, sharing food, stories, or a show we’re both into.",
    "I’m drawn to people who are honest, kind, and a little playful. I enjoy simple things: walks, coffee dates, and evenings where the conversation just flows.",
    "I like a slow morning, a good playlist, and a day that includes at least one small adventure. Looking for someone who is genuine, caring, and interested in a real connection.",
    "Life is busy but I try to prioritize what matters: relationships, health, and learning. If you’re thoughtful, kind, and ready for something sincere, we might get along well.",
]

# 20 profiles with same image + different bios
PROFILES = [
    {
        "profile_id": f"p{i}",
        "gender": "unspecified",
        "image_url": IMAGE_URL,
        "bio": BIOS[i - 1],
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

# ---------- 3. Google Sheets Helpers ----------

def get_worksheet():
    """Connect to the first worksheet in the Google Sheet using service account secrets."""
    service_info = st.secrets["gcp_service_account"]
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_info(service_info, scopes=scopes)
    client = gspread.authorize(creds)
    sheet_id = service_info["sheet_id"]
    return client.open_by_key(sheet_id).sheet1

def append_response_to_sheet(row_dict):
    """
    Append a single response row to Google Sheets.
    The order here must match the header row in the sheet.
    """
    ws = get_worksheet()
    row = [
        row_dict.get("timestamp", ""),
        row_dict.get("participant_id", ""),
        row_dict.get("age", ""),
        row_dict.get("gender", ""),
        row_dict.get("attraction", ""),
        row_dict.get("profile_id", ""),
        row_dict.get("condition", ""),
        row_dict.get("attractiveness", ""),
        row_dict.get("authenticity", ""),
        row_dict.get("desirability", ""),
        row_dict.get("attention_check", ""),
        row_dict.get("attention_correct", ""),
    ]
    ws.append_row(row, value_input_option="RAW")

# ---------- 4. Consent / Start Screen ----------

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

# ---------- 5. Demographics Screen ----------

if st.session_state.demographics is None:
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

        # ---------- Create Randomized Stimulus List ----------
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

        random.shuffle(stimulus_list)
        st.session_state.stimulus_list = stimulus_list
        st.session_state.current_index = 0

        st.rerun()

    st.stop()

# ---------- 6. Main Rating Loop ----------

stimuli = st.session_state.stimulus_list
idx = st.session_state.current_index

# Safety check
if not stimuli:
    st.error("No stimuli available. Please reload the page.")
    st.stop()

# Finished all stimuli
total_steps = len(stimuli) + 1  # +1 for the attention check

# Finished all steps (10 profiles + 1 attention check)
if idx >= total_steps:
    st.success("Thank you! You have completed all profiles. You may close this window now.")
    st.write("Your responses have been recorded.")
    st.stop()


current = stimuli[idx]

# ---------- Force scroll to top on each profile ----------
st.markdown(
    """
    <script>
        window.scrollTo(0, 0);
    </script>
    """,
    unsafe_allow_html=True,
)

# ---------- Progress Bar ----------

total_steps = len(stimuli) + 1  # 10 profiles + 1 attention check

# Map idx (0..10) to profile index (0..9), skipping idx == 3 for attention check
if idx < 3:
    profile_idx = idx               # show profiles 0,1,2
elif idx == 3:
    profile_idx = None              # attention check, no profile
else:
    profile_idx = idx - 1           # idx 4..10 → profiles 3..9

# ---------- Progress Bar ----------
st.write(f"Progress: {idx + 1} / {total_steps}")
progress = (idx + 1) / total_steps
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

# ---------- Regular Profile Rating ----------

# ---------- Regular Profile Rating ----------

# Only run this block when we're not on the attention check
if profile_idx is not None:
    current = stimuli[profile_idx]

    # Display profile counter out of 10 (profiles only)
    st.markdown(f"**Profile {profile_idx + 1} of {len(stimuli)}**")

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
