def simple_interest(p,r):

    return (p * r) / 100
    

principal = float(input("enter the amount of principal: "))
rate = float(input("enter the amt. of interest rate: "))
# time = float(input("enter the amount time period: "))

interest = simple_interest(principal,rate,)
print("simple interest: ",interest)