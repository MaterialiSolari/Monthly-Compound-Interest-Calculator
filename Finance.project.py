def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):   
    monthlyInterest = monthlyInterestRate / 100 / 12
    numberOfMonths = years * 12    
    futureInvestmentValue = investmentAmount * (1 + monthlyInterest) ** numberOfMonths

    return futureInvestmentValue

investmentAmount = float(input('Enter your principal amount: $'))
monthlyInterestRate = float(input('Enter the annual interest rate (as a percentage): '))
    

print(f"{'Year':<5}{'Future Value':<15}")
print(f'-' * 20)

for year in range(1, 21):
    product = futureInvestmentValue(investmentAmount, monthlyInterestRate, year)
    print(f"{year:<3}: ${product:.2f}")