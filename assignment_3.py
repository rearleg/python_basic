# 👇🏻 YOUR CODE 👇🏻:
def get_yearly_revenue(monthly_revenue):
    return monthly_revenue * 12 

def get_yearly_expenses(monthly_expenses):
    return monthly_expenses * 12

def get_tax_amount(profit):
    if profit > 100_000:
        tax = profit * 0.25
    else:
        tax = profit * 0.15
    return tax

def apply_tax_credits(tax_amount, tax_credits):
    return tax_amount * tax_credits


# /YOUR CODE

# BLUEPRINT | DONT EDIT

monthly_revenue = 5_500_000
monthly_expenses = 2_700_000
tax_credits = 0.01

yearly_revenue = get_yearly_revenue(monthly_revenue)
yearly_expenses = get_yearly_expenses(monthly_expenses)

profit = yearly_revenue - yearly_expenses

tax_amount = get_tax_amount(profit)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")

# /BLUEPRINT