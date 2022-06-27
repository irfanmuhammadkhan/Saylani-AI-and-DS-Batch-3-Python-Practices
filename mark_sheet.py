
name = input("Enter your name: ")
father_name = input("Enter your father name: ")
level = input("Enter your class: ")
roll_number = input("Enter your roll number: ")


urdu = int(input("Enter your urdu marks: "))
english = int(input("Enter your English marks: "))
biology = int(input("Enter your Biology marks: "))
chemistry = int(input("Enter your Chemistry marks: "))
physics = int(input("Enter your Physics marks: "))
math = int(input("Enter your Math marks: "))

total_obtained_marks = urdu + english + biology + chemistry + physics + math

percentage = (total_obtained_marks/600) * 100
percentage = round(percentage, 2)
 
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "Fail"

mark_sheet = f"""
***********************************************

                Mark Sheet
     
Name     : {name}   Father's Name : {father_name}
Class    : {level}  Roll Number   : {roll_number}

Subjects    Total Marks     Obtained Marks  
Urdu            100             {urdu}
English         100             {english}
Biology         100             {biology}
Chemistry       100             {chemistry}
Physics         100             {physics}
Math            100             {math}
______________________________________
Total           600             {total_obtained_marks}
______________________________________

Percentage: {percentage}%
Grade: {grade}

***********************************************
"""
print(mark_sheet)
