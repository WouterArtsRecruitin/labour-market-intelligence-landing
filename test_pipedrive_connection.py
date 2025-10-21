#!/usr/bin/env python3
"""Quick test to verify Pipedrive API connection"""

import os
import requests

api_key = os.getenv('PIPEDRIVE_API_KEY')
domain = os.getenv('PIPEDRIVE_DOMAIN')

print(f"Testing connection to: {domain}.pipedrive.com")
print(f"Using API key: {api_key[:10]}..." if api_key else "No API key set")

# Test basic connectivity using header-based authentication
url = f"https://{domain}.pipedrive.com/api/v1/users"
headers = {
    'x-api-token': api_key,
    'Accept': 'application/json'
}

print(f"\nTrying to fetch users (basic permission check)...")
print(f"Authentication: Using x-api-token header")
response = requests.get(url, headers=headers)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text[:500]}")

if response.status_code == 200:
    print("\n✓ API connection successful!")
    data = response.json()
    if data.get('success'):
        print(f"Found {len(data.get('data', []))} users")
elif response.status_code == 403:
    print("\n✗ 403 Forbidden - API key may be invalid or lacks permissions")
elif response.status_code == 401:
    print("\n✗ 401 Unauthorized - API key is invalid")
else:
    print(f"\n✗ Unexpected error: {response.status_code}")
