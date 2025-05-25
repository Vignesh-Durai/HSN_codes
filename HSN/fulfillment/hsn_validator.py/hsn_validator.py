import pandas as pd
import pandas as pd
from hsn_validator import validate_hsn_codes

# Load data once globally
df = pd.read_excel(r"C:\Users\vigne\OneDrive\Desktop\HSN\data\HSN_SAC.xlsx")
df.columns = df.columns.str.strip()
df["HSNCode"] = df["HSNCode"].astype(str).str.strip()
df.dropna(subset=["HSNCode", "Description"], inplace=True)

def validate_hsn_codes(codes):
    if isinstance(codes, str):
        codes = [codes]

    result = []

    for code in codes:
        code = str(code).strip()

        if not code.isdigit() or not (2 <= len(code) <= 8):
            result.append(f"❌ {code}: Invalid format (must be 2–8 digit number)")
            continue

        match = df[df["HSNCode"] == code]
        if not match.empty:
            desc = match.iloc[0]["Description"]
            result.append(f"✅ {code}: {desc}")
        else:
            result.append(f"❌ {code}: Not found in master data")
    
    return result

def handler(params):
    codes = params.get("hsn_code", [])
    return { "messages": validate_hsn_codes(codes) }
