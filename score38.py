price1 = int(input("คะแนนวิชา 1"))
price2 = int(input("คะแนนวิชา 2"))
price3 = float(input("คะแนนวิชา 3"))
totalpoint  = (price1+price2+price3)
average = totalpoint/3
print("คะแนนรวมของคุณในครั้งนี้คือ /n คือ = , totalpoint")
print("คะแนนเฉลี่ยรวมของตุณในครั้งนี้คือ /n คือ =, totalpoint")
if average < 60:
    print("คะแนนรวมของคุณ =" , totalpoint )
    print("คะแนนรวมเฉลี่ย 3 วิชา = ", average)
    print("ควรปรับปรุง")
elif totalpoint <  80:
    print("ผ่าน")
else:
    print("ยอดเยี่ยม")
