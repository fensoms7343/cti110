#CTI110
#P4HW1-Budget Expenses
#Scott Fensom
#11/27/18

#Write a program that asks for a monthly budget
#Ask the user for their expenses for that month
#Take the expenses and display if the user is over or under budget




def main():
    totalExpense = 0
    #ask the user for their monthly budget
    budget = int(input('What is your monthly budget? '))

    go_again = 'y'
    while go_again == 'y':

        expense = float(input('What is the expense? '))

        #get the total expenses for the month
        totalExpense = totalExpense + expense

        go_again = input('Is there another expense? y/n ')
        finalResult = budget - totalExpense
        if totalExpense < budget:
            print('You are',finalResult,'under budget')
        elif totalExpense > budget:
            print('You are',finalResult,'over budget')
        elif totalExpense == budget:
            print('You have met your monthly budget')

main()
