#!/usr/bin/env python3
"""Advanced Pipedrive API diagnostics - test multiple endpoints"""

import os
import requests
import json

api_key = os.getenv('PIPEDRIVE_API_KEY')
domain = os.getenv('PIPEDRIVE_DOMAIN')

print(f"Pipedrive API Diagnostics")
print(f"Domain: {domain}.pipedrive.com")
print(f"API Key: {api_key[:10]}..." if api_key else "No API key")
print("=" * 70)

headers = {
    'x-api-token': api_key,
    'Accept': 'application/json'
}

# Test different endpoints to see which ones work/fail
endpoints = [
    '/users/me',           # Current user info
    '/users',              # All users
    '/permissionSets',     # Permission sets
    '/deals',              # Deals
    '/persons',            # Persons
    '/activities',         # Activities
    '/organizations',      # Organizations
]

results = []

for endpoint in endpoints:
    url = f"https://{domain}.pipedrive.com/api/v1{endpoint}"

    try:
        response = requests.get(url, headers=headers, timeout=10)

        status = response.status_code

        # Try to parse JSON response
        try:
            data = response.json()
            error_msg = data.get('error', data.get('errorCode', 'N/A'))
            success = data.get('success', False)
        except:
            error_msg = response.text[:100]
            success = False

        results.append({
            'endpoint': endpoint,
            'status': status,
            'success': success,
            'error': error_msg,
            'response_preview': response.text[:150]
        })

        print(f"\n{endpoint}")
        print(f"  Status: {status}")
        print(f"  Success: {success}")
        if not success:
            print(f"  Error: {error_msg}")
            print(f"  Response: {response.text[:150]}")

    except Exception as e:
        print(f"\n{endpoint}")
        print(f"  Exception: {str(e)}")
        results.append({
            'endpoint': endpoint,
            'status': 'ERROR',
            'error': str(e)
        })

# Summary
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

working = [r for r in results if r.get('success') == True]
forbidden = [r for r in results if r.get('status') == 403]
other_errors = [r for r in results if r.get('status') not in [200, 403] and r.get('status') != 'ERROR']

print(f"\nWorking endpoints: {len(working)}")
print(f"403 Forbidden: {len(forbidden)}")
print(f"Other errors: {len(other_errors)}")

if len(working) > 0:
    print("\n✓ Some endpoints are working!")
    print("Working endpoints:")
    for r in working:
        print(f"  - {r['endpoint']}")
elif len(forbidden) == len(results):
    print("\n✗ ALL endpoints return 403 Forbidden")
    print("\nThis confirms the API token lacks permissions.")
    print("\nACTION REQUIRED:")
    print("  1. Go to: https://recruitinbv.pipedrive.com/settings/users/permissions")
    print("  2. Find your permission set")
    print("  3. Enable 'Use API' checkbox")
    print("  4. Save changes")
    print("  5. Regenerate your API token at:")
    print("     https://recruitinbv.pipedrive.com/settings/api")
else:
    print("\n⚠ Mixed results - some specific permissions issue")
    print("Check which endpoints work vs don't work above")
