print("คำนวณBMIและแปลผลสุขภาพ")


kilogram = int(input("น้ำหนัก "))
heinght= int(input("ส่วนสูง "))


BMI = kilogram/ (heinght * heinght)
total = BMI


print(" /n หาค่าเฉลี่ย BMI = ", total)


if BMI <18.5:
    print("น้ำหนักน้อย")
elif BMI >18.5-22.9:
    print("ปกติ")
elif BMI >23-24.9:
    print("น้ำหนักเกิน")
elif  BMI >25:
    print ("อ้วน")                    