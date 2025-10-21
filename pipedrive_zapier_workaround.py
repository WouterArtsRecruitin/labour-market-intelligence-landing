#!/usr/bin/env python3
"""
Pipedrive JobDigger Status via Zapier + Google Sheets

This script reads Pipedrive deal data from Google Sheets that is
populated by Zapier. Works around direct API access issues.

Setup:
1. Create a Zap: Pipedrive → Google Sheets
2. Install: pip install gspread oauth2client
3. Set up Google Sheets API credentials
4. Run this script to view deals
"""

import json
import os
from datetime import datetime
from typing import List, Dict

# Check if Google Sheets libraries are available
try:
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    GSPREAD_AVAILABLE = True
except ImportError:
    GSPREAD_AVAILABLE = False
    print("⚠️  Google Sheets libraries not installed.")
    print("   Run: pip install gspread oauth2client")


def read_from_csv(csv_file: str) -> List[Dict]:
    """Read deals from CSV file (exported from Google Sheets)"""
    import csv

    deals = []
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                deals.append(row)
        return deals
    except FileNotFoundError:
        print(f"❌ File not found: {csv_file}")
        return []
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return []


def read_from_google_sheets(sheet_name: str, credentials_file: str) -> List[Dict]:
    """Read deals from Google Sheets"""
    if not GSPREAD_AVAILABLE:
        print("❌ gspread library not available")
        return []

    try:
        # Define the scope
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']

        # Add credentials
        creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
        client = gspread.authorize(creds)

        # Open the spreadsheet
        sheet = client.open(sheet_name).sheet1

        # Get all records
        records = sheet.get_all_records()

        return records
    except Exception as e:
        print(f"❌ Error reading Google Sheets: {e}")
        return []


def format_currency(value) -> str:
    """Format currency value"""
    try:
        val = float(value)
        return f"€{val:,.2f}"
    except:
        return "€0.00"


def display_deals(deals: List[Dict]):
    """Display deals in formatted output"""
    if not deals:
        print("\n❌ No deals found.")
        print("\nMake sure:")
        print("  1. Your Zapier zap is running")
        print("  2. Data has been sent to Google Sheets")
        print("  3. You've downloaded the CSV or set up API credentials")
        return

    print(f"\n{'='*100}")
    print(f"{'PIPEDRIVE DEALS (VIA ZAPIER)':^100}")
    print(f"{'='*100}\n")

    print(f"Total Deals: {len(deals)}\n")

    for i, deal in enumerate(deals, 1):
        title = deal.get('title', deal.get('Title', 'N/A'))
        value = format_currency(deal.get('value', deal.get('Value', 0)))
        status = deal.get('status', deal.get('Status', 'N/A'))
        person = deal.get('person_name', deal.get('Person', 'N/A'))
        org = deal.get('org_name', deal.get('Organization', 'N/A'))

        print(f"{i}. {title}")
        print(f"   Status: {status} | Value: {value}")
        print(f"   Contact: {person} | Organization: {org}")
        print(f"   {'-'*96}")


def display_summary(deals: List[Dict]):
    """Display summary statistics"""
    if not deals:
        return

    total_value = 0
    open_count = 0
    won_count = 0
    lost_count = 0

    for deal in deals:
        # Get value
        try:
            val = float(deal.get('value', deal.get('Value', 0)))
            total_value += val
        except:
            pass

        # Get status
        status = str(deal.get('status', deal.get('Status', ''))).lower()
        if 'open' in status:
            open_count += 1
        elif 'won' in status:
            won_count += 1
        elif 'lost' in status:
            lost_count += 1

    print(f"\n{'='*100}")
    print(f"{'SUMMARY':^100}")
    print(f"{'='*100}\n")

    print(f"Total Deals:     {len(deals)}")
    print(f"Open Deals:      {open_count}")
    print(f"Won Deals:       {won_count}")
    print(f"Lost Deals:      {lost_count}")
    print(f"Total Value:     {format_currency(total_value)}")

    print(f"\n{'='*100}\n")


def main():
    """Main execution"""

    print("\n🔄 Pipedrive JobDigger Status (Zapier Workaround)")
    print("="*60)

    # Method 1: Try reading from CSV (simplest)
    csv_file = 'pipedrive_deals.csv'

    print(f"\nAttempting to read from: {csv_file}")
    print("(Export from Google Sheets as CSV with this name)")

    deals = read_from_csv(csv_file)

    if deals:
        print(f"✅ Found {len(deals)} deals in CSV file")
        display_deals(deals)
        display_summary(deals)
    else:
        print("\n📋 CSV file not found. Here's how to set up:")
        print("\n" + "="*60)
        print("SETUP INSTRUCTIONS")
        print("="*60)
        print("\n1. Create a Zap in Zapier:")
        print("   - Trigger: Schedule (Daily)")
        print("   - Action 1: Pipedrive - Find Deals")
        print("   - Action 2: Google Sheets - Create/Update Rows")
        print("")
        print("2. In Google Sheets, create columns:")
        print("   - Title")
        print("   - Status")
        print("   - Value")
        print("   - Person")
        print("   - Organization")
        print("   - Stage")
        print("")
        print("3. Map Pipedrive fields to Google Sheets columns")
        print("")
        print("4. Download the Google Sheet as CSV:")
        print("   - File → Download → CSV")
        print("   - Save as: pipedrive_deals.csv")
        print("   - Place in same folder as this script")
        print("")
        print("5. Run this script again:")
        print("   python pipedrive_zapier_workaround.py")
        print("\n" + "="*60)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Cancelled by user.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
