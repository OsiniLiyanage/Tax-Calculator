# ============================================
# SRI LANKAN TAX CALCULATOR PROJECT
# Session 04: Functions, Lambdas & Functional Programming
# ============================================
# Name: _____________________________
# Date: _____________________________

# ============================================
# SRI LANKA TAX BRACKETS (Effective April 1, 2025)
# ============================================
# Annual Income (LKR):
#   Up to 1,800,000: 0% (Tax-free!)
#   1,800,001 - 2,800,000: 6%
#   2,800,001 - 3,300,000: 18%
#   3,300,001 - 3,800,000: 24%
#   3,800,001 - 4,300,000: 30%
#   Greater than 4,300,000: 36%
# ============================================


def calculate_income_tax(annual_income):
    tax =0.0
    taxable =annual_income

    if taxable<=1800000:
        return 0.0
    
    taxable-= 1800000

    if taxable>1000000:
        tax+=1000000*0.06
        taxable -=1000000
    else:
        tax+= taxable*0.06
        return tax 
    
    if taxable>500000:
        tax+=500000*0.18
        taxable -= 500000
    else:
        tax+= taxable*0.18
        return tax
    
    if taxable>500000:
        tax+=500000*0.24
        taxable -= 500000
    else:
        tax+= taxable*0.24
        return tax
    
    if taxable>500000:
        tax+=500000*0.30
        taxable -= 500000
    else:
        tax+= taxable*0.30
        return tax
    
    tax += taxable*0.30
    return tax
    
     

def calculate_effective_tax_rate(annual_income):
  if annual_income ==0:
      return 0.0
  
  tax= calculate_income_tax(annual_income)
  rate=(tax/annual_income)*100
  return rate



def calculate_take_home(annual_income):
   tax=calculate_income_tax(annual_income)
   return annual_income-tax


# ============================================
# HELPER FUNCTIONS FOR DISPLAY (PROVIDED)
# ============================================

def print_taxpayer_details(income):
    """Print detailed tax information for a single taxpayer"""
    tax = calculate_income_tax(income)
    effective_rate = calculate_effective_tax_rate(income)
    take_home = calculate_take_home(income)
    monthly_take_home = take_home / 12

    print(f"\nAnnual Income: Rs. {income:,.2f}")
    print(f"  Income Tax: Rs. {tax:,.2f} ({effective_rate:.2f}%)")
    print(f"  Take-Home (Annual): Rs. {take_home:,.2f}")
    print(f"  Take-Home (Monthly): Rs. {monthly_take_home:,.2f}")
    print("-" * 60)


def print_ranking(sorted_income_tax_pairs):
    """Print ranked list of taxpayers by tax paid"""
    for rank, (income, tax) in enumerate(sorted_income_tax_pairs, start=1):
        print(f"{rank}. Rs. {income:,.2f} - Tax Paid: Rs. {tax:,.2f}")


def print_high_earners(high_earner_incomes):
    """Print details for high earners (>= Rs. 4,300,000)"""
    for income in high_earner_incomes:
        tax = calculate_income_tax(income)
        print(f"Income: Rs. {income:,.2f} - Tax: Rs. {tax:,.2f}")


# ============================================
# MAIN PROGRAM
# ============================================

def main():
    """Main program to demonstrate tax calculations"""

    # Test data: Multiple taxpayer incomes (in LKR)
    incomes = [2500000, 4000000, 5000000, 1500000, 3500000]

    print("=" * 60)
    print("SRI LANKAN TAX CALCULATOR (April 2025 Tax Reforms)")
    print("=" * 60)

    # ========================================
    # TODO 1: Calculate taxes for all incomes using map()
    # ========================================
    # Use map() to calculate income tax for each income

    taxes = list(map(calculate_income_tax,incomes))


    # ========================================
    # TODO 2: Filter high earners using filter()
    # ========================================
    # Find all incomes >= Rs. 4,300,000 (highest tax bracket)

    high_earners = list(filter(lambda i:i>=4300000,incomes))


    # ========================================
    # TODO 3: Create (income, tax) pairs and sort
    # ========================================
    # 1. Use zip() to pair incomes with taxes
    # 2. Use sorted() to rank by tax amount (highest first)

    sorted_incomes_taxes = sorted(zip(incomes,taxes), key=lambda i:i[1], reverse=True)


    # ========================================
    # Display Results (Provided - No need to modify)
    # ========================================

    # Display detailed tax reports
    print("\n" + "=" * 60)
    print("DETAILED TAX REPORTS")
    print("=" * 60)
    for income in incomes:
        print_taxpayer_details(income)

    # Display top taxpayers ranking
    print("\n" + "=" * 60)
    print("TOP TAXPAYERS (Ranked by Tax Paid)")
    print("=" * 60)
    print_ranking(sorted_incomes_taxes)

    # Display high earners
    print("\n" + "=" * 60)
    print("HIGH EARNERS (>= Rs. 4,300,000 - Top Tax Bracket)")
    print("=" * 60)
    print_high_earners(high_earners)

    # ========================================
    # BONUS: Calculate summary statistics
    # ========================================
    print("\n" + "=" * 60)
    print("SUMMARY STATISTICS")
    print("=" * 60)

    # YOUR CODE HERE (BONUS)
    # Calculate and print:
    # - Total tax revenue: sum(taxes)
    # - Average effective tax rate
    # - Highest and lowest tax amounts: max(taxes), min(taxes)
    # - Average monthly take-home


# Run the program
if __name__ == "__main__":
    main()
