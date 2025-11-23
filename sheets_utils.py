# sheets_utils.py
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

def safe_get_secrets():
    """Return None if secrets are missing (local run)."""
    try:
        return st.secrets["gcp_service_account"]
    except Exception:
        return None


def get_worksheet():
    service_info = safe_get_secrets()
    if service_info is None:
        # Running locally → skip logging
        return None

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
    try:
        ws = get_worksheet()
        if ws is None:
            # Local run → no logging → do nothing
            return
        
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
    except Exception as e:
        # Log error but don't crash the app
        # In production, you might want to log this to a file or monitoring service
        print(f"Error saving to Google Sheets: {e}")
        # Optionally, you could store failed responses in session state for retry
