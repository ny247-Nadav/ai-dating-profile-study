# sheets_utils.py
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials


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
