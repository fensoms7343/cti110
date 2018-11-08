#CTI110
#P3HW1 - Roman Numerals
#Scott Fensom
#11/8/18

#The user will input a number 1-10 and recieve its Roman numeral
#If the number is outside the range, give the user an error message

#Request a number between 1-10 from the user
simpleNumber = int(input('Enter a number between 1-10: '))

#Store the number as a Roman numeral
romanOne = 1
romanTwo = 2
romanThree = 3
romanFour = 4
romanFive = 5
romanSix = 6
romanSeven = 7
romanEight = 8
romanNine = 9
romanTen = 10

#Give the user a Roman numeral
if simpleNumber == romanOne:
    print('The Roman numeral for 1 is "I"')
else:
    if simpleNumber == romanTwo:
        print('The Roman numeral for 2 is "II"')
    else:
        if simpleNumber == romanThree:
            print('The Roman numeral for 3 is "III"')
        else:
            if simpleNumber == romanFour:
                print('The Roman numeral for 4 is "IV"')
            else:
                if simpleNumber == romanFive:
                    print('The Roman numeral for 5 is "V"')
                else:
                    if simpleNumber == romanSix:
                        print('The Roman numeral for 6 is "VI"')
                    else:
                        if simpleNumber == romanSeven:
                            print('The Roman numeral for 7 is "VII"')
                        else:
                            if simpleNumber == romanEight:
                                print('The Roman numeral for 8 is "VIII"')
                            else:
                                if simpleNumber == romanNine:
                                    print('The Roman numeral for 9 is "IX"')
                                else:
                                    if simpleNumber == romanTen:
                                        print('The Roman numeral for 10 is "X"')
                                    else:
                                        if simpleNumber > romanTen:
                                            print('This number is above the given range.')
                                        else:
                                            if simpleNumber < romanOne:
                                                print('This number is lower than the given range.')
                                                
                                    
            
