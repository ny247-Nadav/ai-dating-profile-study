import streamlit as st
import streamlit.components.v1 as components


def render_profile_card(profile: dict) -> None:
    """
    Corrected version — ensures Streamlit does NOT escape HTML for control profiles.
    """

    fc = profile.get("fixed_choice", {}) or {}
    age = fc.get("age")
    race = fc.get("race")
    activities = fc.get("activities", []) or []

    # Chips
    tags = [age, race] + activities
    tags = [t for t in tags if t]

    chips_html = ""
    if tags:
        chips_html = "<div class='profile-chips'>" + "".join(
            f"<span class='profile-chip'>{t}</span>"
            for t in tags
        ) + "</div>"

    # Image
    image_html = ""
    if profile.get("image_url"):
        image_html = f"<img src='{profile['image_url']}' class='profile-photo' />"

    # AI disclosure
    ai_html = ""
    if profile.get("condition") == "ai_disclosed":
        ai_html = "<div class='ai-label'>🤖 Profile includes AI enhancements</div>"
    elif profile.get("condition") == "control":
        ai_html = "<div class='ai-label'></div>"
        ai_html = "<div></div>"


    # Bio
    bio = profile.get("bio", "")

    # *** CRITICAL FIX ***
    # NO newline before <div ...>
    # NO indentation anywhere in the HTML block
    card_html = f"""<div class="profile-card">
    {image_html}
    {ai_html}
    {chips_html}
    <div class="profile-bio-text">{bio}</div>
    </div>"""

    # Render safely
    st.markdown(card_html, unsafe_allow_html=True)





def apply_global_styles() -> None:
    """
    Global CSS for the study UI:
    - clean light theme
    - card, chips, typography
    - slider min/max labels
    - AI label pill
    """
    st.markdown(
        """
        <style>
        /* -------- Layout & Typography -------- */
        .main {
            max-width: 900px;
            margin: 0 auto;
            font-family: system-ui, -apple-system, BlinkMacSystemFont,
                         "SF Pro Text", "Segoe UI", Roboto, sans-serif;
        }

        body {
            background: #f3f4f6;
        }

        .big-title {
            font-size: 32px;
            font-weight: 700;
            letter-spacing: -0.03em;
            margin-bottom: 0.5rem;
        }

        .section-header {
            font-size: 22px;
            font-weight: 600;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
        }

        .rating-title {
            font-size: 18px;
            font-weight: 600;
            margin-top: 1.4rem;
            margin-bottom: 0.75rem;
        }

        /* -------- Profile Card -------- */
        .profile-card {
            background: #ffffff;
            border-radius: 22px;
            padding: 1.2rem 1.5rem 1.4rem 1.5rem;
            box-shadow:
                0 14px 30px rgba(15, 23, 42, 0.08),
                0 0 0 1px rgba(148, 163, 184, 0.25);
            margin-bottom: 1.5rem;
        }

        .profile-photo {
            width: 100%;
            border-radius: 18px;
            object-fit: cover;
            margin-bottom: 0.85rem;
            max-height: 420px;
        }

        .profile-chips {
            display: flex;
            flex-wrap: wrap;
            margin-top: 0.1rem;
            margin-bottom: 0.6rem;
            gap: 0.3rem;
        }

        .profile-chip {
            padding: 0.25rem 0.75rem;
            border-radius: 999px;
            font-size: 0.8rem;
            background: #f3f4f6;
            border: 1px solid #e5e7eb;
            color: #111827;
        }

        .profile-bio-label {
            font-weight: 600;
            font-size: 0.95rem;
            margin-bottom: 0.1rem;
            color: #4b5563;
        }

        .profile-bio-text {
            font-size: 0.95rem;
            line-height: 1.6;
            color: #111827;
        }

        /* -------- AI label pill -------- */
        .ai-label {
            color: #1d4ed8;
            font-weight: 600;
            font-size: 0.9rem;
            padding: 0.35rem 0.85rem;
            border-radius: 999px;
            background: #e0ecff;
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
            margin-top: 0.4rem;
            margin-bottom: 0.4rem;
        }

        /* -------- Slider labels 0 / 4 -------- */
        .min-max-labels {
            display: flex;
            justify-content: space-between;
            font-size: 0.8rem;
            color: #6b7280;
            margin-top: -4px;
            margin-bottom: 8px;
        }

        /* -------- Buttons -------- */
        .stButton > button {
            border-radius: 999px;
            padding: 0.45rem 1.6rem;
            font-weight: 600;
        }

        /* -------- Sliders: make the track a bit nicer -------- */
        /* WebKit browsers */
        input[type="range"]::-webkit-slider-thumb {
            background: #6366f1;
        }
        input[type="range"]::-webkit-slider-runnable-track {
            height: 6px;
            border-radius: 999px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


import streamlit.components.v1 as components

def scroll_to_top():
    """Scroll the Streamlit page back to the top."""
    components.html(
        """
        <script>
        // Try both html and body (different browsers use one or the other)
        const d = window.parent.document;
        if (d) {
            d.documentElement.scrollTop = 0;
            d.body.scrollTop = 0;
        }
        </script>
        """,
        height=0,
    )

