print("คำนวนแม่สูตรคูณ2จำนวน")

n = int(input("สูตรคูณเริ่มต้น "))
m = int(input("สูตรคูรสุดท้าย "))

for i in range(n,+m+1 ):
    print(f"\nสูตรคูณของ{i}:")
    for j in range(1,13):
       print(f"{i} x {j} = {i*j}")
print("by ใบเตย 4/4 เลขที่38")