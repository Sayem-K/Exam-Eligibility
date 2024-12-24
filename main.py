print("Please enter you medical condition:")
medical_condition = str(input("Enter Y for good medical condition and enter N for bad medical condition. "))
if medical_condition == 'Y':
    print("You are eligible for the exam.")
else:
    attendance = int(input("Enter your attendance with anumber from 1 - 100: "))
    if attendance > 75:
        print("You are eligible for the exam.")
    else:
        print("You cannot take the exam.")


