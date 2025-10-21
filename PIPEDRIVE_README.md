# Pipedrive JobDigger Status Tracker

This tool helps you track and monitor Labour Market Intelligence report requests through Pipedrive CRM.

## Features

- Fetch and display all deals from Pipedrive
- View deal status (open, won, lost)
- Show contact and organization information
- Display summary statistics
- Export data to JSON format

## Setup

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get Your Pipedrive Credentials

#### API Key
1. Log in to your Pipedrive account
2. Go to Settings > Personal preferences > API
3. Copy your API token

#### Domain
Your domain is the subdomain of your Pipedrive URL.
- Example: If your Pipedrive URL is `acme.pipedrive.com`, your domain is `acme`

### 3. Set Environment Variables

You can set credentials in two ways:

#### Option A: Environment Variables (Recommended)

```bash
export PIPEDRIVE_API_KEY='your_api_key_here'
export PIPEDRIVE_DOMAIN='yourcompany'
```

#### Option B: .env File

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your credentials:

```env
PIPEDRIVE_API_KEY=your_actual_api_key
PIPEDRIVE_DOMAIN=yourcompany
```

Then install python-dotenv if not already installed:

```bash
pip install python-dotenv
```

And modify the script to load from .env (add at the top of main()):

```python
from dotenv import load_dotenv
load_dotenv()
```

## Usage

### Run the Script

```bash
python pipedrive_jobdigger_status.py
```

### Sample Output

```
Connecting to Pipedrive (yourcompany.pipedrive.com)...
Fetching JobDigger deals...

====================================================================================================
                                        JOBDIGGER DEALS STATUS
====================================================================================================

Total Deals: 15

1. Labour Market Analysis - Tech Sector
   Status: OPEN | Value: €59.00 | Stage: 1
   Contact: John Doe | Organization: Tech Corp
   Created: 2025-10-15 10:30 | Updated: 2025-10-20 14:22
   ------------------------------------------------------------------------------------------------

====================================================================================================
                                              SUMMARY
====================================================================================================

Total Deals:     15
Open Deals:      8
Won Deals:       5
Lost Deals:      2
Total Value:     €885.00
Won Value:       €295.00
Pipeline Value:  €472.00

====================================================================================================

Export to JSON? (y/n):
```

## Features Explained

### Deal Information Displayed

- **Title**: Name of the deal
- **Status**: Current status (open/won/lost)
- **Value**: Deal value in euros
- **Stage**: Current pipeline stage
- **Contact**: Associated person
- **Organization**: Associated company
- **Timestamps**: Creation and last update times

### Summary Statistics

- Total number of deals
- Breakdown by status
- Total pipeline value
- Won deals value

### JSON Export

Export all deal data to a timestamped JSON file for further analysis or record-keeping.

## Troubleshooting

### Error: Missing Pipedrive credentials

Make sure you've set the environment variables or created a .env file with your credentials.

### Error: Invalid API key

Verify that:
1. Your API key is correct
2. You have API access enabled in Pipedrive
3. Your API key hasn't expired

### Error: Connection failed

Check that:
1. Your domain is correct
2. You have internet connectivity
3. Pipedrive services are operational

## Integration with Labour Market Intelligence

This script helps you track:
- Report requests from the landing page
- Customer pipeline status
- Revenue metrics
- Conversion rates

## Security

- Never commit your `.env` file or API keys to version control
- The `.env` file is already listed in `.gitignore`
- Keep your API key confidential
- Rotate API keys periodically for security

## Support

For issues or questions:
- Email: info@recruitin.com
- Website: https://recruitin.com

---

**Labour Market Intelligence - WouterArts Recruitin**
