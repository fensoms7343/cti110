#CTI110
#P4HW2-Celsius to Farenheit Table
#Scott Fensom
#11/27/18

#Write a program to display a table of celsius temps 0-20 and the farenheit equivalents
#The formula for celsius to farenheit is F=(9/5)C+32

def main():
    celsius = -1
    while celsius < 20:
        celsius = celsius + 1
        farenheit = (9/5)*celsius +32
        print("If Celsius is:",celsius,"Then Farenheit is:",format(farenheit, ',.1f'))

main()
