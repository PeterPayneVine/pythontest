def calculate_mortgage_details(loan_amount, annual_interest_rate, loan_term_years):
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    loan_term_months = loan_term_years * 12

    # Calculate monthly payment using the formula for mortgage payment
    monthly_payment = (loan_amount * monthly_interest_rate) / \
                      (1 - (1 + monthly_interest_rate) ** -loan_term_months)

    principle_values = []
    outstanding_loans = []

    remaining_loan = loan_amount
    for month in range(1, loan_term_months + 1):
        interest_payment = remaining_loan * monthly_interest_rate
        principle_payment = monthly_payment - interest_payment
        remaining_loan -= principle_payment

        principle_values.append(principle_payment)
        outstanding_loans.append(remaining_loan)

    return principle_values, outstanding_loans

# Input parameters
loan_amount = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (%): "))
loan_term_years = int(input("Enter the loan term (years): "))

# Calculate and display principle value and outstanding loan for each month
principles, outstandings = calculate_mortgage_details(loan_amount, annual_interest_rate, loan_term_years)
print("\nMonth\tPrinciple Value\tOutstanding Loan")
for month, (principle, outstanding) in enumerate(zip(principles, outstandings), start=1):
    print(f"{month}\t{principle:.2f}\t\t{outstanding:.2f}")