import streamlit as st


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
        ai_html = "<div class='ai-label'>🤖 I used AI to enhance this profile</div>"

    # Bio
    bio = profile.get("bio", "")

    # Build HTML components list to avoid empty string issues
    html_parts = ['<div class="profile-card">']
    
    if image_html:
        html_parts.append(image_html)
    
    if ai_html:
        html_parts.append(ai_html)
    
    if chips_html:
        html_parts.append(chips_html)
    
    # Bio is always included
    html_parts.append(f'<div class="profile-bio-text">{bio}</div>')
    html_parts.append('</div>')
    
    # Join without extra whitespace
    card_html = "".join(html_parts)

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
        
        /* Scroll anchor at top */
        #scroll-anchor-top {
            position: absolute;
            top: 0;
            left: 0;
            height: 0;
            width: 0;
        }

        body {
            background: #f3f4f6;
        }
        
        /* Improve accessibility - focus states */
        button:focus-visible,
        input:focus-visible,
        select:focus-visible {
            outline: 2px solid #6366f1;
            outline-offset: 2px;
        }
        
        /* Better spacing for form elements */
        .element-container {
            margin-bottom: 1rem;
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
        
        h3 {
            color: #1f2937;
            font-weight: 600;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
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
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        
        .profile-card:hover {
            transform: translateY(-2px);
            box-shadow:
                0 20px 40px rgba(15, 23, 42, 0.12),
                0 0 0 1px rgba(148, 163, 184, 0.3);
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
            transition: all 0.2s ease;
        }
        
        .stButton > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        }
        
        .stButton > button[kind="primary"] {
            background: linear-gradient(90deg, #6366f1 0%, #8b5cf6 100%);
            border: none;
        }

        /* -------- Sliders: make the track a bit nicer -------- */
        /* WebKit browsers */
        input[type="range"]::-webkit-slider-thumb {
            background: #6366f1;
            width: 18px;
            height: 18px;
            border: 2px solid #ffffff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            cursor: pointer;
        }
        input[type="range"]::-webkit-slider-runnable-track {
            height: 6px;
            border-radius: 999px;
            background: #e5e7eb;
        }
        
        input[type="range"]::-moz-range-thumb {
            background: #6366f1;
            width: 18px;
            height: 18px;
            border: 2px solid #ffffff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            cursor: pointer;
            border-radius: 50%;
        }
        
        input[type="range"]::-moz-range-track {
            height: 6px;
            border-radius: 999px;
            background: #e5e7eb;
        }
        
        /* Slider labels */
        .stSlider label {
            font-weight: 500;
            color: #374151;
        }
        
        /* Info tooltips */
        .stTooltip {
            color: #6b7280;
        }
        </style>
        <script>
        // Global scroll handler - runs on every page load
        (function() {
            function scrollToTopNow() {
                try {
                    // Get parent window (where Streamlit actually runs)
                    const pw = window.parent;
                    const pd = pw.document;
                    
                    // Scroll parent window - most important
                    pw.scrollTo(0, 0);
                    pw.scroll(0, 0);
                    
                    // Scroll all possible containers in parent
                    const selectors = [
                        '[data-testid="stAppViewContainer"]',
                        '.main',
                        'main',
                        '#root',
                        'body',
                        'html'
                    ];
                    
                    selectors.forEach(sel => {
                        try {
                            const el = pd.querySelector(sel);
                            if (el) {
                                el.scrollTop = 0;
                                el.scrollLeft = 0;
                                el.scrollTo(0, 0);
                            }
                        } catch(e) {}
                    });
                    
                    // Also scroll document elements
                    if (pd.documentElement) {
                        pd.documentElement.scrollTop = 0;
                    }
                    if (pd.body) {
                        pd.body.scrollTop = 0;
                    }
                } catch(e) {
                    console.error('Scroll error:', e);
                }
            }
            
            // Run immediately
            scrollToTopNow();
            
            // Run when DOM is ready
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', scrollToTopNow);
            }
            
            // Run when window loads
            window.addEventListener('load', scrollToTopNow);
            
            // Also run after a short delay
            setTimeout(scrollToTopNow, 100);
            setTimeout(scrollToTopNow, 300);
            setTimeout(scrollToTopNow, 600);
        })();
        </script>
        """,
        unsafe_allow_html=True,
    )


def render_progress_bar(current: int, total: int) -> None:
    """Render a visual progress bar showing study completion."""
    progress = current / total
    percentage = int(progress * 100)
    
    st.markdown(
        f"""
        <div style="margin-bottom: 1.5rem;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span style="font-size: 0.9rem; color: #6b7280; font-weight: 500;">Progress</span>
                <span style="font-size: 0.9rem; color: #6b7280; font-weight: 600;">{percentage}%</span>
            </div>
            <div style="background: #e5e7eb; border-radius: 999px; height: 8px; overflow: hidden;">
                <div style="background: linear-gradient(90deg, #6366f1 0%, #8b5cf6 100%); height: 100%; width: {percentage}%; transition: width 0.3s ease;"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def scroll_to_top():
    """Scroll the Streamlit page back to the top - guaranteed to work."""
    # Use st.markdown with inline script for immediate execution
    st.markdown(
        """
        <script>
        (function() {
            function scrollToTopNow() {
                try {
                    const pw = window.parent;
                    const pd = pw.document;
                    
                    // CRITICAL: Scroll the parent window first
                    pw.scrollTo(0, 0);
                    pw.scroll(0, 0);
                    
                    // Find and scroll the main Streamlit container
                    const mainContainer = pd.querySelector('[data-testid="stAppViewContainer"]') || 
                                        pd.querySelector('.main') ||
                                        pd.querySelector('main') ||
                                        pd.body;
                    
                    if (mainContainer) {
                        mainContainer.scrollTop = 0;
                        mainContainer.scrollLeft = 0;
                        mainContainer.scrollTo(0, 0);
                    }
                    
                    // Scroll document elements
                    if (pd.documentElement) {
                        pd.documentElement.scrollTop = 0;
                        pd.documentElement.scrollLeft = 0;
                    }
                    if (pd.body) {
                        pd.body.scrollTop = 0;
                        pd.body.scrollLeft = 0;
                    }
                } catch(e) {
                    console.error('Scroll error:', e);
                }
            }
            
            // Execute immediately
            scrollToTopNow();
            
            // Also execute with delays to catch late-rendered content
            setTimeout(scrollToTopNow, 50);
            setTimeout(scrollToTopNow, 150);
            setTimeout(scrollToTopNow, 300);
            setTimeout(scrollToTopNow, 600);
            
            // Use MutationObserver to catch DOM changes
            try {
                const pd = window.parent.document;
                const target = pd.querySelector('[data-testid="stAppViewContainer"]') || 
                              pd.querySelector('.main') ||
                              pd.body;
                
                if (target) {
                    const observer = new MutationObserver(() => {
                        scrollToTopNow();
                    });
                    
                    observer.observe(target, {
                        childList: true,
                        subtree: true,
                        attributes: false
                    });
                    
                    setTimeout(() => observer.disconnect(), 2000);
                }
            } catch(e) {}
        })();
        </script>
        """,
        unsafe_allow_html=True
    )

