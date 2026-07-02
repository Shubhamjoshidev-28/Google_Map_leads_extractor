# Google Maps Business Extractor

> A modular Python-based Google Maps Business Data Extraction pipeline
> powered by **SerpAPI**.

Extract business listings from Google Maps, process them into a clean
dataset, and export them to Google Sheets or JSON for lead generation,
analytics, CRM import, or cold-email workflows.

------------------------------------------------------------------------

## Features

-   Google Maps search using SerpAPI
-   Automatic pagination
-   Raw JSON storage
-   Required field extraction
-   Google Sheets export
-   Modular architecture
-   Easy to extend with new addons

------------------------------------------------------------------------

## Project Structure

``` text
project/
│
├── data/
│   ├── raw_data.json
│   └── business.json
│
├── venv/
│
├── extract.py
├── required_data_extractor.py
├── json_file_manager.py
├── google_sheet_writer.py
├── run.py
│
├── credentials.json
├── .env
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

## Project Flow

``` text
User Input
    │
    ▼
extract.py
    │
    ▼
raw_data.json
    │
    ▼
required_data_extractor.py
    │
    ▼
business.json
    │
    ▼
google_sheet_writer.py
    │
    ▼
Google Sheets
```

------------------------------------------------------------------------

## Module Responsibilities

  ----------------------------------------------------------------------------
  Module                         Responsibility
  ------------------------------ ---------------------------------------------
  `extract.py`                   Fetch business data from SerpAPI and save
                                 `raw_data.json`.

  `required_data_extractor.py`   Extract only required fields and generate
                                 `business.json`.

  `json_file_manager.py`         Read, write, append, deduplicate and manage
                                 JSON files.

  `google_sheet_writer.py`       Upload processed data to Google Sheets.

  `run.py`                       Orchestrates the execution order only.
  ----------------------------------------------------------------------------

------------------------------------------------------------------------

## Installation

### 1. Clone Repository

``` bash
git clone <repository-url>
cd <repository-name>
```

### 2. Create Virtual Environment

``` bash
python -m venv venv
```

Windows

``` bash
venv\Scripts\activate
```

Linux/macOS

``` bash
source venv/bin/activate
```

### 3. Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## Environment Variables

Create a `.env` file.

``` env
SERP_API_KEY=YOUR_SERPAPI_KEY
GOOGLE_SHEET_NAME=Business Leads
```

Never hardcode secrets.

------------------------------------------------------------------------

# Google Sheets Setup

## Step 1

Create a Google Cloud project.

https://console.cloud.google.com/

## Step 2

Enable:

-   Google Sheets API
-   Google Drive API

## Step 3

Go to:

``` text
APIs & Services
    ↓
Credentials
    ↓
Create Credentials
    ↓
Service Account
```

## Step 4

Open the service account.

``` text
Keys
    ↓
Add Key
    ↓
Create New Key
    ↓
JSON
```

Download the file and rename it to:

``` text
credentials.json
```

Place it in the project root.

``` text
project/
├── credentials.json
├── .env
├── run.py
```

## Step 5

Open your Google Sheet.

Click **Share**.

Open `credentials.json` and copy the value of:

``` json
client_email
```

Share the spreadsheet with that email as an **Editor**.

------------------------------------------------------------------------

## Run

``` bash
python run.py
```

Execution pipeline:

``` text
extract.py
    ↓
required_data_extractor.py
    ↓
google_sheet_writer.py
```

------------------------------------------------------------------------

## Coding Standards

-   Single Responsibility Principle
-   No hardcoded paths
-   No API keys in code
-   Small focused functions
-   Prefer type hints
-   Proper exception handling
-   Use logging instead of print

------------------------------------------------------------------------

## Adding New Addons

Example:

``` text
addons/
├── email_extractor.py
├── website_scraper.py
├── linkedin_scraper.py
```

Rules:

-   Read from `business.json`
-   Update `business.json`
-   Do not modify existing extraction logic
-   Register the addon inside `run.py`

Pipeline example:

``` text
extract.py
    ↓
required_data_extractor.py
    ↓
email_extractor.py
    ↓
google_sheet_writer.py
```

------------------------------------------------------------------------

## Suggested Future Addons

-   Email Extractor
-   Website Scraper
-   LinkedIn Scraper
-   Instagram Scraper
-   Facebook Scraper
-   Email Validator
-   Phone Validator
-   CSV Exporter
-   Excel Exporter
-   Airtable Exporter
-   HubSpot Exporter
-   Duplicate Checker
-   AI Industry Classifier

------------------------------------------------------------------------

## Troubleshooting

### `credentials.json` not found

Place the file in the project root.

### Permission Error

Share the spreadsheet with the Service Account email.

### Spreadsheet Not Found

Verify the spreadsheet name or ID and ensure it has been shared.

------------------------------------------------------------------------

## Security

Never commit:

``` text
credentials.json
.env
data/
```

Example `.gitignore`

``` gitignore
venv/
__pycache__/
.env
credentials.json
data/
*.pyc
```

------------------------------------------------------------------------

## Version Roadmap

  Version   Features
  --------- ------------------------
  v1.0      Google Maps Extraction
  v1.1      Email Extraction
  v1.2      Website Scraping
  v1.3      CRM Export
  v2.0      Desktop GUI

------------------------------------------------------------------------

## License

MIT License

Copyright (c) 2026
