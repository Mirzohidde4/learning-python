# cars = ["Audi", "gm", "mustang", "nissan", "bmw"]
# for car in cars:
#     if car == "gm":
#         print(car.upper())
#     else:
#         if car == "bmw":
#             print(car.upper())
#         else:
#             print(car.title())


# cars = ["Audi", "Gm", "mustang", "nissan", "bmw"]
# for car in cars:
#     if car.lower() != "bmw":
#         if car.lower() != "gm":
#             print(car.title())
#         else:
#             print(car.upper())
#     else:
#         print(car.upper())


# login = input("Login kiriting : ")
# if login.title() == "Admin":
#     print(f"Xush kelibsiz {login.title()}.Foydalanuvchilar ro'yxatini ko'rasizmi ?")
# else:
#     print(f"Xush kelibsiz, {login.title()} ")


# a = int(input("1-son = "))
# b = int(input("2-son = "))
# if a == b:
#     print("Ikki son teng")
# else:
#     if a > b:
#         print(f"{a} katta")
#     else:
#         print(f"{b} katta")


# n = int(input("Son kiriting = "))
# if n == 0:
#     print("Oraliq")
# else:
#     if n > 0:
#         print("Musbat")
#     else:
#         print("Manfiy")


# son=int(input('Juft son kiriting : \n>>>'))
# if son%2==0:
#     print("Raxmat")
# else:
#     print("Bu son juft emas!")


# yosh=int(input("Yoshingizni kiriting:\n "))
# if yosh<=4 or yosh>=60:
#     narx=0
# elif yosh<18:
#     narx=10000
# elif yosh>18:
#     narx=20000
# print(f"Chipta narxi {narx} so'm")


# a = int(input("1-son = "))
# b = int(input("2-son = "))
# if a == b:
#     print(f"{a}={b}")
# else:
#     if a > b:
#         print(f"{a}>{b}")
#     else:
#         print(f"{a}<{b}")


# mahsulotlar=["Olma",'Uzum','Pamidor',"Banan","Kivi",'Piyoz',"Bodring","Kartoshka",'Sabzi',"Limon"]
# Savat=[]
# bor_mahsulotlar=[]
# mavjud_emas=[]
# print("Kamida 5 ta mahsulot ayting?")
# Savat.append(input("1-"))
# Savat.append(input("2-"))
# Savat.append(input("3-"))
# Savat.append(input("4-"))
# Savat.append(input("5-"))
# for mahsulot in Savat:
#     if mahsulot.title() in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print(f"Quidagi mahsulotlar do'konimizda yo'q\n{mavjud_emas}")
# else:
#     print(f"Siz so'ragan barcha mahsulotlar do'konimizda bor")


# foydalanuvchilar=["Messi",'Ronaldo',"Neymar","xavi",'Zidan']
# login=input("Login kiriting:\n")
# if login in foydalanuvchilar:
#     print("login band")
# else:
#     print(f"Xush kelibsiz {login}")


son = int(input("Son kiriting= "))
for i in range(2, 11):
    if son % i == 0:
        print(f"{son} {i} ga qoldiqsiz bo'linadi")
