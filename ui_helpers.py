# ui_helpers.py
import streamlit as st
import streamlit.components.v1 as components


def apply_global_styles():
    st.markdown(
        """
        <style>
        /* Global page background + font */
        .main {
            max-width: 900px;
            margin: 0 auto;
            font-size: 17px;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "SF Pro Text",
                         "Segoe UI", sans-serif;
        }

        body {
            background: radial-gradient(circle at top left, #f3f4ff 0, #f9fafb 40%, #ffffff 100%);
        }

        /* Streamlit default button -> pill, techie color */
        .stButton > button {
            background: linear-gradient(135deg, #6366f1, #4f46e5);
            color: white;
            border-radius: 999px;
            border: none;
            padding: 0.4rem 1.6rem;
            font-weight: 600;
            box-shadow: 0 10px 20px rgba(79, 70, 229, 0.18);
        }

        .stButton > button:hover {
            background: linear-gradient(135deg, #4f46e5, #4338ca);
            box-shadow: 0 12px 24px rgba(79, 70, 229, 0.28);
        }

        .big-title {
            font-size: 32px !important;
            font-weight: 700 !important;
            letter-spacing: -0.03em;
            margin-bottom: 0.5rem;
        }

        .section-header {
            font-size: 22px !important;
            font-weight: 600 !important;
            margin-top: 1.5rem;
            margin-bottom: 0.5rem;
        }

        .rating-title {
            font-size: 20px !important;
            font-weight: 600 !important;
            margin-top: 1.2rem;
            margin-bottom: 0.7rem;
        }

        /* Profile card */
        .profile-card {
            background: #ffffff;
            border-radius: 24px;
            padding: 1.2rem 1.4rem 1.4rem 1.4rem;
            box-shadow:
                0 18px 45px rgba(15, 23, 42, 0.06),
                0 0 0 1px rgba(148, 163, 184, 0.18);
            margin-bottom: 1.5rem;
        }

        .profile-header-text {
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 0.5rem;
        }

        .profile-bio-label {
            font-weight: 600;
        }

        .profile-bio-text {
            margin-top: 0.15rem;
            margin-bottom: 0.5rem;
        }

        .ai-label {
            color: #1f6feb;
            font-weight: 700;
            font-size: 16px;
            padding: 0.45rem 0.9rem;
            border-radius: 999px;
            background: rgba(37, 99, 235, 0.08);
            display: inline-flex;
            align-items: center;
            gap: 0.25rem;
            margin-top: 0.4rem;
            margin-bottom: 0.4rem;
        }

        .ai-label::before,
        .ai-label::after {
            content: "✨";
            font-size: 15px;
        }

        .min-max-labels {
            display: flex;
            justify-content: space-between;
            font-size: 13px;
            color: #6b7280;
            margin-top: -6px;
            margin-bottom: 4px;
        }

        /* Sliders – slightly thicker and colored */
        [data-baseweb="slider"] > div {
            padding-top: 0.6rem;
            padding-bottom: 0.2rem;
        }

        input[type=range]::-webkit-slider-thumb {
            background: #ef4444;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def scroll_to_top():
    """Force the browser window to scroll to the top on each rerun."""
    components.html(
        """
        <script>
        window.parent.scrollTo({top: 0, behavior: 'auto'});
        </script>
        """,
        height=0,
    )
