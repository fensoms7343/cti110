#CTI110
#P3HW2-Shipping Charges
#Scott Fensom
#11/8/18


#The user will input the weight of a package and recieve the shipping charges
#The weight shouldn't be equal or less than 0

#Ask for the weight of the package
packageWeight = float(input('what is the weight of the package in pounds? ' ))

#What is the package rate to ship per pound
rateOne = 1.50
rateTwo = 3.00
rateThree = 4.00
rateFour = 4.75

#Multiply weight by shipping rate
if packageWeight<= 2:
    cost = packageWeight * rateOne
else:
    if packageWeight <= 6:
        cost = packageWeight * rateTwo
    else:
        if packageWeight <= 10:
            cost = packageWeight * rateThree
        else:
            if packageWeight > 10:
                cost = packageWeight * rateFour

#Print shipping cost
if packageWeight <= 0:
    print('Not a valid weight')
else:
    if packageWeight <= 2:
        print('The cost to ship this package will be $',format(cost, ',.2f'))
    else:
        if packageWeight <= 6:
            print('The cost to ship this package will be $',format(cost, ',.2f'))
        else:
            if packageWeight <= 10:
                print('The cost to ship this package will be $',format(cost, ',.2f'))
            else:
                if packageWeight > 10:
                    print('The cost to ship this package will be $',format(cost, ',.2f'))
