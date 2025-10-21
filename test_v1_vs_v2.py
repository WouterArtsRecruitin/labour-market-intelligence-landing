#!/usr/bin/env python3
"""Test Pipedrive API v1 vs v2 endpoints"""

import os
import requests

api_key = os.getenv('PIPEDRIVE_API_KEY')
domain = os.getenv('PIPEDRIVE_DOMAIN')

print(f"Testing API v1 vs v2")
print(f"Domain: {domain}.pipedrive.com")
print(f"API Key: {api_key[:10]}...")
print("=" * 70)

headers = {
    'x-api-token': api_key,
    'Accept': 'application/json'
}

# Test v1 endpoints
print("\n=== API v1 Endpoints ===")
v1_endpoints = [
    '/api/v1/users/me',
    '/api/v1/deals',
    '/api/v1/persons'
]

for endpoint in v1_endpoints:
    url = f"https://{domain}.pipedrive.com{endpoint}"
    response = requests.get(url, headers=headers, timeout=10)
    print(f"\n{endpoint}")
    print(f"  Status: {response.status_code}")
    print(f"  Response: {response.text[:100]}")

# Test v2 endpoints (if available)
print("\n\n=== API v2 Endpoints ===")
v2_endpoints = [
    '/api/v2/deals',
    '/api/v2/persons'
]

for endpoint in v2_endpoints:
    url = f"https://{domain}.pipedrive.com{endpoint}"
    response = requests.get(url, headers=headers, timeout=10)
    print(f"\n{endpoint}")
    print(f"  Status: {response.status_code}")
    print(f"  Response: {response.text[:100]}")

print("\n" + "=" * 70)
print("\nNOTE: If v1 fails but v2 works, use v2 endpoints.")
print("If both fail with 403, the 'Use API' permission is not enabled.")
