#!/usr/bin/env python3
"""Test different Pipedrive authentication methods"""

import os
import requests

api_key = os.getenv('PIPEDRIVE_API_KEY')
domain = os.getenv('PIPEDRIVE_DOMAIN')

print(f"Testing Pipedrive API: {domain}.pipedrive.com")
print(f"API Key: {api_key[:10]}..." if api_key else "No API key")
print("=" * 60)

# Method 1: Header-based authentication
print("\n1. Testing HEADER authentication (x-api-token)...")
url = f"https://{domain}.pipedrive.com/api/v1/users"
headers = {
    'x-api-token': api_key,
    'Accept': 'application/json'
}
response1 = requests.get(url, headers=headers)
print(f"   Status: {response1.status_code}")
print(f"   Response: {response1.text[:200]}")

# Method 2: Query parameter authentication
print("\n2. Testing QUERY PARAMETER authentication (api_token)...")
url = f"https://{domain}.pipedrive.com/api/v1/users"
params = {'api_token': api_key}
response2 = requests.get(url, params=params)
print(f"   Status: {response2.status_code}")
print(f"   Response: {response2.text[:200]}")

# Method 3: Try a simpler endpoint
print("\n3. Testing /recents endpoint...")
url = f"https://{domain}.pipedrive.com/api/v1/recents"
headers = {'x-api-token': api_key}
response3 = requests.get(url, headers=headers)
print(f"   Status: {response3.status_code}")
print(f"   Response: {response3.text[:200]}")

# Summary
print("\n" + "=" * 60)
print("SUMMARY:")
if response1.status_code == 200:
    print("✓ Header authentication WORKS")
elif response2.status_code == 200:
    print("✓ Query parameter authentication WORKS")
else:
    print("✗ All methods failed - possible issues:")
    print("  - API token is invalid or expired")
    print("  - API access is disabled on your account")
    print("  - Your IP is being blocked by Cloudflare")
    print("  - Insufficient permissions on the API token")
    print("\nNext steps:")
    print("  1. Go to Settings > Personal preferences > API")
    print("  2. Check if API access is enabled")
    print("  3. Try regenerating your API token")
    print("  4. Verify your user role has API permissions")
