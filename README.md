# HSN_codes
HSN Code Validation Agent – Google ADK Internship Project
=========================================================

This project is a submission for the Google ADK-based internship + full-time opportunity. It implements a validation agent that checks the validity of HSN (Harmonized System of Nomenclature) codes using a master Excel dataset.

Built using the ADK framework structure, this agent processes user inputs (one or multiple HSN codes), validates them, and returns appropriate responses.

FEATURES
--------

- Input: One or more HSN codes
- Validation:
  - Format Check: Must be 2–8 digit numeric codes
  - Existence Check: Must be found in the master Excel file
- Response:
  - Valid → Return description from dataset
  - Invalid → Return error message

PROJECT STRUCTURE
------------------

HSNValidationAgent/
├── agent.json                          -> Agent configuration
├── intents/
│   └── validate_hsn_code.json          -> Intent for HSN validation
├── entities/
│   └── hsn_code.json                   -> Entity type for HSN codes
├── fulfillment/
│   ├── __init__.py                     -> Makes it a Python module
│   └── hsn_validator.py                -> Python validation logic
├── data/
│   └── HSN_Master_Data.xlsx            -> Master dataset
├── test.py                             -> Script to test the validator
└── README.md                           -> This documentation file

SETUP & EXECUTION
------------------

1. Install Required Libraries

   pip install pandas openpyxl

2. Run the Test Script

   Make sure you are in the project root folder and run:

   python test.py

   This will run the validation logic on sample HSN codes.

SAMPLE OUTPUT
-------------

✅ 0101: LIVE HORSES, ASSES, MULES AND HINNIES.  
✅ 01011010: LIVE HORSES, ASSES, MULES AND HINNIES PURE-BRED BREEDING ANIMALS HORSES  
❌ 999999: Not found in master data  
❌ abc: Invalid format (must be 2–8 digit number)  
✅ 01: LIVE ANIMALS

DATASET DESCRIPTION
--------------------

- File: HSN_Master_Data.xlsx
- Source: Provided Google Sheet
- Columns:
  - HSNCode: Product classification code
  - Description: Name of the goods

DELIVERABLES
------------

- ✅ Working code base
- ✅ Output screenshots
- ✅ Explanation video walkthrough
- ✅ ADK-compatible structure
- ✅ GitHub repository submission

CANDIDATE DETAILS
------------------

- Name: Vignesh Durai
- Role: Internship cum Full-Time Applicant
- Availability: Willing to relocate to Chennai (in-office internship)
- Remarks: Eager to work on ADK-based intelligent agent systems

REFERENCES
-----------

- ADK Docs: https://google.github.io/adk-docs/
- HSN Dataset: https://docs.google.com/spreadsheets/d/1UD4JAAQ6Fgeyc5a1OwBiLV2cPTAK_D2q/edit?usp=sharing
