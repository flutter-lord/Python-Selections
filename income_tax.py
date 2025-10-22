filing_status = eval(input("Enter your filing status: "))
taxable_income = eval(input("Enter your taxable income: "))

single_filers, married_filing_jointly, married_filing_separately, \
head_of_household =  0, 1, 2, 3

tax = 0

if filing_status == single_filers: