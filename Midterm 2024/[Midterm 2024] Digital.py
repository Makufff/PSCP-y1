"""Check digital"""
def check_eligibility(is_thai, has_address, age, annual_income, savings):
    """Check rule"""
    if not (is_thai and has_address):
        return False
    if age < 16:
        return False
    if annual_income > 840000:
        return False
    if savings > 500000:
        return False
    return True

inputs_name = input().strip()
inputs_is_thai = input().strip().lower() in ('yes', 'true')
inputs_has_address = input().strip().lower() in ('yes', 'true')
inputs_age = float(input())
inputs_annual_income = float(input())
inputs_savings = float(input())

if check_eligibility(inputs_is_thai,
                     inputs_has_address,
                     inputs_age,
                     inputs_annual_income,
                     inputs_savings):
    print(f"Congratulations! {inputs_name} is qualified " +
          "to receive a digital wallet amount of 10,000 baht"+
          ", sponsored by all taxpayers in Thailand.")
else:
    print(f"Unfortunately, {inputs_name} is not qualified.")
