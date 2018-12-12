#CTI110
#P4HW3-Tuition Increase
#Scott Fensom
#11/29/18

print('The tuition is $8000 per semester.')
print('The tuition increases by 3% each year')

def main():
    tuition = 16000
    rate = 1.03
    new_tuition = tuition 
    for year in range (1,6):
        tuition = 16000
        rate = 1.03
        if year == 1:
            print('The tuition will be:', format(tuition, ',.2f'), 'for year', year)
        else:
            if year > 1:
                new_tuition = new_tuition * rate
                print('The tuition will be:', format(new_tuition, ',.2f'), 'for year', year)


main()
