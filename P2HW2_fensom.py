#CTI110
#P2HW2
#Scott Fensom
#11/1/18

#Get the total number of students
student_total= int(input('Enter the total number of students in the class: '))

#Get the total number of female students
student_female= int(input('How many students are female?: '))

#Get the total number of male students
student_male= int(input('How many students are male?: '))

#Calculate the percentage of females students in the class
female_ratio= student_female/student_total

#Calculate the percentage of male students in the class
male_ratio= student_male/student_total

#Display male/female student ratios
print('The percentage of females in the class is', female_ratio, 'percent')
print('The percentage of males in the class is', male_ratio, 'percent')
