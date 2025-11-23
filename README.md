# AI Dating Profile Study

A Streamlit-based research study application for assessing attractiveness, authenticity, and desirability in online dating profiles with AI disclosure conditions.

## Features

- **User-friendly interface** with modern, clean design
- **Progress tracking** with visual progress bar
- **Attention check** to ensure data quality
- **Demographics collection** (age, gender, attraction preference)
- **Profile rating system** (attractiveness, authenticity, desirability)
- **Condition randomization** (control vs. AI-disclosed profiles)
- **Google Sheets integration** for data collection
- **Error handling** and validation
- **Responsive design** with smooth animations

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure Google Sheets (optional, for production):
   - Create a Google Cloud service account
   - Add credentials to Streamlit secrets as `gcp_service_account`
   - The app will work locally without Sheets integration

3. Run the app:
```bash
streamlit run app.py
```

## Study Flow

1. **Consent Screen**: Participants read study information and provide consent
2. **Demographics**: Age, gender, and attraction preference are collected
3. **Profile Rating**: Participants rate 10 profiles on three dimensions
4. **Attention Check**: Quality check after 3 profiles
5. **Completion**: Thank you screen with completion time

## Project Structure

- `app.py` - Main application logic and flow control
- `ui_helpers.py` - UI components, styling, and helper functions
- `stimuly.py` - Profile generation and stimulus management
- `sheets_utils.py` - Google Sheets integration for data logging
- `requirements.txt` - Python dependencies

## Improvements Made

- ✅ Fixed code quality issues (duplicate imports, typos, unused code)
- ✅ Added visual progress bar
- ✅ Enhanced error handling and validation
- ✅ Improved completion screen with timing information
- ✅ Added loading states and user feedback
- ✅ Enhanced UI styling with hover effects and animations
- ✅ Better accessibility (focus states, tooltips)
- ✅ Improved attention check with validation
- ✅ Better button styling and user guidance

## Data Collection

Responses are automatically logged to Google Sheets (when configured) with the following fields:
- Timestamp
- Participant ID
- Demographics (age, gender, attraction)
- Profile ID and condition
- Ratings (attractiveness, authenticity, desirability)
- Attention check results

## Notes

- The app works locally without Google Sheets (responses stored in session state)
- All participant data is anonymous
- Study takes approximately 5-10 minutes to complete
