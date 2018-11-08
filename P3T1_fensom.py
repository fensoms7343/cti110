#CTI110
#P3T1
#Scott Fensom
#11/6/18

#Determine the area of rectangles
#Input what the length and width of the two rectangles
#Determine which rectangle has a greater area or if they have the same area

#Input the length and width of rectangle 1
#Input the length and width of rectangle 2
#Calculate the area of rectangle 1
#Calculate the area of rectangle 2
#Display which rectangle has a greater area or if they have the same area

#If area1 > area2
    #Display "Rectangle 1 has the greatest area."
#If area2 > area 1
    #Display "Rectangle 2 has the greatest area."
#If area1 = area 2
    #display "Both rectangles have the same area."

#Get the dimensions of rectangle 1
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))

#Get the dimensions of rectangle 2
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))

#Calculate the areas of the rectangles
area1 = length1 * width1
area2 = length2 * width2

#Determine which has the greater area
if area1 > area2:
    print('Rectangle 1 has the greatest area.')
elif area2 > area1:
    print('Rectangle 2 has the greatest area.')
else:
    print('Both rectangles have the same area.')



