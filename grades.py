inpt = True
while inpt == True:  #allowing input to reject values not 0-100
    inpt = False
    grade_percentage = float(input("Enter your grade percentage: ")) # user input

    if grade_percentage > 100 or grade_percentage < 0:
        print("Your percentage was not vaild")
        inpt = True
    elif grade_percentage >= 0 and grade_percentage <= 31:
        print("Grade U – you must work harder")
    elif grade_percentage >= 32 and grade_percentage <= 39:
        print("Grade E – room for improvement")
    elif grade_percentage >= 40 and grade_percentage <= 48:
        print("Grade D – reasonable work")
    elif grade_percentage >= 49 and grade_percentage <= 56:
        print("Grade C – good work")
    elif grade_percentage >= 57 and grade_percentage <= 65:
        print("Grade B – very good work")
    else:
        print("Grade A – excellent work")