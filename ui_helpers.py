# ui_helpers.py
import streamlit as st


def apply_global_styles():
    """Inject global CSS for layout and visual styling."""
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


def scroll_to_top():
    """Scroll window to top on each step."""
    st.markdown(
        """
        <script>
            window.scrollTo(0, 0);
        </script>
        """,
        unsafe_allow_html=True,
    )


def show_progress(current_index: int, total_steps: int):
    """Show text + progress bar for study progression."""
    st.write(f"Progress: {current_index + 1} / {total_steps}")
    progress = (current_index + 1) / total_steps
    st.progress(progress)
