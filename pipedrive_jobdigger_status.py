#!/usr/bin/env python3
"""
Pipedrive JobDigger Status Tracker

This script fetches and displays the status of JobDigger deals/contacts from Pipedrive.
It helps track labour market intelligence report requests and their processing status.
"""

import os
import sys
import requests
from datetime import datetime
from typing import Dict, List, Optional
import json


class PipedriveClient:
    """Client for interacting with Pipedrive API"""

    def __init__(self, api_key: str, domain: str):
        """
        Initialize Pipedrive client

        Args:
            api_key: Your Pipedrive API key
            domain: Your Pipedrive domain (e.g., 'acme' from acme.pipedrive.com)
        """
        self.api_key = api_key
        self.base_url = f"https://{domain}.pipedrive.com/api/v1"
        self.session = requests.Session()

    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Make a request to Pipedrive API

        Args:
            endpoint: API endpoint (e.g., '/deals')
            params: Additional query parameters

        Returns:
            API response as dictionary
        """
        if params is None:
            params = {}

        params['api_token'] = self.api_key

        url = f"{self.base_url}{endpoint}"

        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making API request: {e}")
            sys.exit(1)

    def get_deals(self, status: Optional[str] = None, limit: int = 100) -> List[Dict]:
        """
        Fetch deals from Pipedrive

        Args:
            status: Filter by status ('open', 'won', 'lost', or None for all)
            limit: Maximum number of deals to fetch

        Returns:
            List of deals
        """
        params = {'limit': limit}
        if status:
            params['status'] = status

        response = self._make_request('/deals', params)

        if response.get('success'):
            return response.get('data', []) or []
        return []

    def get_deal_fields(self) -> Dict:
        """
        Fetch all deal fields to understand custom fields

        Returns:
            Dictionary of deal fields
        """
        response = self._make_request('/dealFields')

        if response.get('success'):
            return {field['key']: field for field in response.get('data', [])}
        return {}

    def get_persons(self, limit: int = 100) -> List[Dict]:
        """
        Fetch persons (contacts) from Pipedrive

        Args:
            limit: Maximum number of persons to fetch

        Returns:
            List of persons
        """
        params = {'limit': limit}
        response = self._make_request('/persons', params)

        if response.get('success'):
            return response.get('data', []) or []
        return []


def format_currency(value: Optional[float]) -> str:
    """Format currency value"""
    if value is None:
        return "N/A"
    return f"€{value:,.2f}"


def format_date(date_str: Optional[str]) -> str:
    """Format date string"""
    if not date_str:
        return "N/A"
    try:
        date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return date_obj.strftime('%Y-%m-%d %H:%M')
    except:
        return date_str


def display_deals(deals: List[Dict]):
    """
    Display deals in a formatted table

    Args:
        deals: List of deals from Pipedrive
    """
    if not deals:
        print("\nNo deals found.")
        return

    print(f"\n{'='*100}")
    print(f"{'JOBDIGGER DEALS STATUS':^100}")
    print(f"{'='*100}\n")

    print(f"Total Deals: {len(deals)}\n")

    for i, deal in enumerate(deals, 1):
        title = deal.get('title', 'N/A')
        value = format_currency(deal.get('value'))
        status = deal.get('status', 'N/A')
        stage = deal.get('stage_id', 'N/A')
        person = deal.get('person_name', 'N/A')
        org = deal.get('org_name', 'N/A')
        created = format_date(deal.get('add_time'))
        updated = format_date(deal.get('update_time'))

        print(f"{i}. {title}")
        print(f"   Status: {status.upper()} | Value: {value} | Stage: {stage}")
        print(f"   Contact: {person} | Organization: {org}")
        print(f"   Created: {created} | Updated: {updated}")
        print(f"   {'-'*96}")


def display_summary(deals: List[Dict]):
    """
    Display summary statistics

    Args:
        deals: List of deals from Pipedrive
    """
    if not deals:
        return

    total_value = sum(deal.get('value', 0) or 0 for deal in deals)
    open_deals = [d for d in deals if d.get('status') == 'open']
    won_deals = [d for d in deals if d.get('status') == 'won']
    lost_deals = [d for d in deals if d.get('status') == 'lost']

    print(f"\n{'='*100}")
    print(f"{'SUMMARY':^100}")
    print(f"{'='*100}\n")

    print(f"Total Deals:     {len(deals)}")
    print(f"Open Deals:      {len(open_deals)}")
    print(f"Won Deals:       {len(won_deals)}")
    print(f"Lost Deals:      {len(lost_deals)}")
    print(f"Total Value:     {format_currency(total_value)}")

    if won_deals:
        won_value = sum(d.get('value', 0) or 0 for d in won_deals)
        print(f"Won Value:       {format_currency(won_value)}")

    if open_deals:
        open_value = sum(d.get('value', 0) or 0 for d in open_deals)
        print(f"Pipeline Value:  {format_currency(open_value)}")

    print(f"\n{'='*100}\n")


def main():
    """Main execution function"""

    # Get credentials from environment variables
    api_key = os.getenv('PIPEDRIVE_API_KEY')
    domain = os.getenv('PIPEDRIVE_DOMAIN')

    # Validate credentials
    if not api_key or not domain:
        print("\nError: Missing Pipedrive credentials!")
        print("\nPlease set the following environment variables:")
        print("  export PIPEDRIVE_API_KEY='your_api_key_here'")
        print("  export PIPEDRIVE_DOMAIN='yourcompany'")
        print("\nOr create a .env file with these values.\n")
        sys.exit(1)

    if api_key == 'your_api_key_here' or domain == 'yourcompany':
        print("\nError: Please replace the placeholder credentials with actual values!")
        print("\nGet your API key from: Pipedrive Settings > Personal preferences > API")
        print("Your domain is the subdomain of your Pipedrive URL (e.g., 'acme' from acme.pipedrive.com)\n")
        sys.exit(1)

    print(f"\nConnecting to Pipedrive ({domain}.pipedrive.com)...")

    # Initialize client
    client = PipedriveClient(api_key, domain)

    # Fetch deals
    print("Fetching JobDigger deals...")
    deals = client.get_deals()

    # Display results
    display_deals(deals)
    display_summary(deals)

    # Optional: Export to JSON
    export_choice = input("Export to JSON? (y/n): ").strip().lower()
    if export_choice == 'y':
        filename = f"pipedrive_deals_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(deals, f, indent=2)
        print(f"\nExported to {filename}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)
