from fulfillment.hsn_validator import validate_hsn_codes

test_inputs = ["0101", "01011010", "999999", "abc", "01"]

results = validate_hsn_codes(test_inputs)

for res in results:
    print(res)
