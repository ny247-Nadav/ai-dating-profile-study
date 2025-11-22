# sheets_utils.py
import streamlit as st
from streamlit.errors import StreamlitSecretNotFoundError
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

SPREADSHEET_NAME = "AI Dating Study Responses"  # your sheet name


def get_worksheet():
    """Return a gspread worksheet, or None if secrets are not available (e.g., local run)."""
    try:
        service_info = st.secrets["gcp_service_account"]
    except (KeyError, StreamlitSecretNotFoundError):
        # Running locally without secrets -> just skip Google Sheets
        print("[sheets_utils] No secrets found, skipping Google Sheets logging.")
        return None

    creds = Credentials.from_service_account_info(service_info, scopes=SCOPE)
    client = gspread.authorize(creds)
    spreadsheet = client.open(SPREADSHEET_NAME)
    # Use first worksheet or a named one if you prefer
    ws = spreadsheet.sheet1
    return ws


def append_response_to_sheet(response_dict: dict):
    """
    Append one response to Google Sheets.
    If no secrets / worksheet (e.g., local dev), silently skip.
    """
    ws = get_worksheet()
    if ws is None:
        # Local dev: don't crash, just print and return
        print("[sheets_utils] Worksheet is None, response not saved (local run).")
        return

    # Adjust order/fields to match your header row
    row = [
        response_dict.get("timestamp"),
        response_dict.get("participant_id"),
        response_dict.get("age"),
        response_dict.get("gender"),
        response_dict.get("attraction"),
        response_dict.get("profile_id"),
        response_dict.get("condition"),
        response_dict.get("attractiveness"),
        response_dict.get("authenticity"),
        response_dict.get("desirability"),
        response_dict.get("attention_check"),
        response_dict.get("attention_correct"),
    ]
    ws.append_row(row)
