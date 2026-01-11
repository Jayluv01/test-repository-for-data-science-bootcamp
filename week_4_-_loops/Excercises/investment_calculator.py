# Ask for initial investment amount
# Ask for annual interest rate (As percentage)
# Ask for number of years
# Calculatge value each year, with compound interest
# Display year-by-year growth
# Show total profit at the end

investment_amount = float(input("Enter inital investment amount: "))
interest_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter number of years: "))

print("\n" + "="*50)
print("INVESTMENT GROWTH PROJECTION")
print("="*50)
print(f"Initial investment: ${investment_amount:,.2f}")
print(f"Interest rate: {interest_rate}%")
print(f"Investment period: {years} years")

current_amount = investment_amount
# Display year-by-year growth
for year in range(1, years + 1):
    #calculate the interest earned for the current year.
    interest_earned = current_amount * (interest_rate / 100)

    #calculate the new amount (investment value) using compound interest
    current_amount = current_amount * (1 + interest_rate / 100)

# Display year-by-year growth200
    print(f"Year {year}: ${current_amount:,.2f} | Interest: ${interest_earned:,.2f}")
total_profit = current_amount - investment_amount
print("")
print(f"Final Amount: ${current_amount:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Return on Investment: {(total_profit/investment_amount)*100:.2f}%")