import random
secret_nunder =random. randint(1,100)
count = 1



while True:
 guess = int(input("ทายตัวเลข"))
 if guess> secret_nunder:
    print("มากไป ลองใหม่อีกครั้ง ")
 elif guess< secret_nunder:
    print("น้อยไป ลองใหม่อีกครั้ง ")
 elif secret_nunder:
    print("ถูกต้อง ลองใหมอีกครั้ง ")