#CTI110
#P4T2 Bug Collector
#Scott Fensom
#11/15/18

#Write a program to keep a running total of the number of bugs collected in a five day period
#Ask for the umber of bugs collected for each day
#Display the total number of bugs collected

def main():
    
    go_again = 'y'
    while go_again == 'y':

        total = 0

        #Get the number of bugs collectd each day
        for day in range(1,8):
            print('How many bugs were collected on day', day)
            bugs = int(input())
            total += bugs

        #Display the total number of bugs collected
        print('You collected', total, 'bugs')
        go_again = input('Count for another week? y/n ')

    print('You have finished counting bugs.')

#call main() to start program
main()
