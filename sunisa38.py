print("โปรแกรมคำนวณคะแนนรวม")

maths = int(input(" คณิตศาสตร์ "))
thai = int(input(" วิชาภาษาไทย "))
english = int(input(" วิชาภาษาอังกฤษ "))

total_point = (maths + thai + english)
average = total_point /3
if average <60:
    print("ดีเยี่ยม")
elif average <80:
    print("ดีมาก")
elif average <40:
    print("ผ่าน")
print("by toey 4/4")
print("thank you")