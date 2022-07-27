# print(5**4)
# print(22%4)
# print("P = ",4*125,"S = ",125**2)
# print('c = ',(6**2+7**2)**(1/2))
# ism = 'Ahmad'
# familya = 'Qayum'
# ism_familya = ism+' '+familya
# print('Salom! Mening ismim',"\t",f"{ism} {familya}")
# ism_sharif = f"{ism} {familya}"
# print(ism_sharif.upper())
# print(ism_sharif.lower())
# print(ism_sharif.title())
# meva = " olma "
# text1 = "Men "
# text2 = " yaxshi ko\'raman."
# print(text1+meva.lstrip()+text2) #lstrip matn boshidan bo'shliqni olib tashlaydi
# print(text1+meva.rstrip()+text2) # rstrip matn oxidan bo'shliqni olib tashlaydi
# print(text1+meva.strip()+text2) # strip matn boshi va oxiridan bo'shliqni olib tashlaydi
# ism = input("Ismingiz nima?\n>>>")
# print("Assalom aleykum, "+ ism.capitalize())
# son = int(input("Sonni kiriting:\n>>>"))
# a = str(son**2)
# b = str(son**3)

# print(str(son) + ' ning kvadrati '+ a)
# print(str(son) + ' ning kubi '+ b)
# yoshi = int(input("Yoshingizni kiriting:\n>>>"))
# t_yil = 2022-yoshi
# print('Siz '+str(t_yil)+' da tug\'ilgansiz')
# list = ['olma', 'anor', 'uzum']
# list.append('banan') ro'yxatga element qo'shish (oxiriga)
# list.insert(0,'banan') ro'yxatning istalgan joyiga element qo'shadi
# print(list)

#Ro'yxatdagi elementlarni o'chirish
# del list[0]
# list.remove('uzum')
# print(list)

# mevalar = ['olma', 'uzum', 'banan', 'shaftoli']
# maxsulot = mevalar.pop()
# print('Men ' + maxsulot +' sotib oldim')
# print(mevalar)

# ismlar = ['Abror', 'Alibek', 'Ulugbek']
# print(f"{ismlar[0]} va {ismlar[1]} aka uka")

# sonlar = [1 , -2, 3, 2.25]
# sonlar[0] = 10
# sonlar[0] = sonlar[3]
# sonlar[3] = sonlar[0]+sonlar[1]
# print(sonlar)

# cars = ['bmw', 'Audio', 'tesla', 'Volvo', 'general motors']
# cars.sort()
# cars.sort(reverse=True)
# print(sorted(cars, reverse=True))
# cars.reverse()
# print("Elementlar soni: ", len(cars))

# sonlar = list(range(0,10))
# toq_sonlar = list(range(1, 20, 2))
# juft_sonlar = list(range(0, 20, 2))
# print(toq_sonlar)
# print("Juft sonlar: ", juft_sonlar)

# sonlar = [12000, 25000, 8600, 17000, 1245]
# arzon = min(sonlar)
# qimmat = max(sonlar)
# print(qimmat)

# cars = ['bmw', 'Audio', 'tesla', 'Volvo', 'general motors', 'Audio', 'Porshe', 'Mustang']
# my_cars = cars[0:3]
# my_cars1 = cars[4:]
# print(my_cars1)

# sonlar = [1,2,3,4,5,6,7]
# sonlar2 = sonlar[:]
# sonlar2.append(8)
# sonlar2.append(9)
# print(sonlar)

# tomonlar = (12, 10, 25, 14)
# print(tomonlar[0:3])

# sonlar = [10,2,3,4,5,6,7]
# # print(sorted(sonlar, reverse=True))
# a = sonlar.reverse()
# print(sonlar)

# sonlar = list(range(120,1200,2))
# print(sum(sonlar))
# print(min(sonlar))
# print(max(sonlar))
# print(len(sonlar))

# print(sonlar[:20])
# print(sonlar[-20:])
# print(sonlar)
# print(sonlar[530:550])

# taomlar = ['osh','somsa','norin','shashlik','qozonkabob']
# nonushta = taomlar[:]
# nonushta.remove('shashlik')
# nonushta.remove('osh')
# nonushta.append('choy')
# nonushta.append('non')
# print(nonushta)
# print(taomlar)
# nonushta = ['osh','somsa','norin','shashlik','qozonkabob']
# nonushta[0] = "qaymoq va non"
# nonushta = tuple(nonushta)
# print(nonushta)

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)
# print("Hurmat bilan, Alisher\n")

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(1,11))
# son_kv = []
# for son in sonlar:
#     son_kv.append(son**2)
# print(son_kv)
# print(sonlar)

# dostlar = []
# print("5 ta dostingizni kiriting:")
# for n in range(5):
#     dostlar.append(input(f"{n+1} dostlaringizni kiring: "))
# print(dostlar)

# ismlar = ['Ali', 'Vali', 'Husan', 'Hasan', 'Olim']
# for ism in ismlar:
#     print(ism)
# print("Code", len(ismlar), " marta takrorlandi")

# toq_sonlar = list(range(9,100,2))
# for toq_son in toq_sonlar:
#     print(toq_son**3)

# kinolar = []
# print("Eng yaxshi kinolaringiz qaysi?")
# for n in range(5):
#     kinolar.append(input(f"{n+1} - kino:"))
# print(kinolar)

# persons = []
# p_soni = int(input("Bugun nechta odam bilan gaplashdingiz?>>>"))
# for n in range(p_soni):
#     persons.append(input(f"{n+1} - odam: "))
# print(persons)

# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())

# cars = ['tayota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else: 
#         print(car.upper())

# foydalanuvchi = input("Loginni kiriting: \n>>>")
# if foydalanuvchi.lower() == 'admin':
#     print("Xush kelibsiz, Admin!")
# else:
#     print("Xush kelibsiz", foydalanuvchi)

# son = int(input("Sonni kiriting:"))
# sum = 0
# for digit in str(son):
#     sum += int(digit)
# print(sum)

# sum = 0
# son = int(input("Sonni kiriting:\n>>>"))
# while (son != 0):
#     sum = sum + (son % 10)
#     son = son // 10
#     # print(son)
# print(sum)

# yosh = int(input("yoshingizni nechida? "))
# if yosh < 5:
#     price = 0
# elif yosh < 12:
#     price = 5000
# else:
#     price = 10000
# print(f"Sizga kirish {price} so\'m")

# kun = input("Bugun haftaning qaysi kuni? ")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print('Bugun dam olish kuni')
# else:
#     print('Bugun ish kunis')

# kun = input("Bugun qaysi kun?")
# harorat = float(input("Havo harorati qanday?"))
# if kun.lower() == 'yakshanba' and harorat >= 30:
#     print('Cho\'milishga ketdik')
# elif kun.lower() == 'yakshanba' and harorat < 30:
#     print('Uyda qolamiz!')
# else:
#     print("Ish kuni")

# narx = 15000
# choy = True
# salat = False
# if choy and salat:
#     narx = narx + 10000
# elif choy or salat:
#     narx = narx + 5000
# print(narx)

# narx = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
# if choy:
#     print('Mijoz choy oldi')
#     narx = narx + 2000
# if salat:
#     print('Mijoz salat oldi')
#     narx = narx + 5000
# if non:
#     print('Mijoz non oldi')
#     narx = narx +4000
# if kompot:
#     print('Mijoz kompot oldi')
#     narx = narx + 7000
# if assorti:
#     print('Mijoz assorti oldi')
#     narx = narx + 25000
# print(f"Jami narx {narx} ga teng")

# menu = ['osh', 'shashlik', 'kabob', 'norin', 'somsa']
# ovqat = input("Nima yeysiz?>>>")
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi')
# else:
#     print("Bunday ovqat yo\'q")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Menuda {taom} yoq")
# else:
#     print("Savatchangiz bo\'sh")

# son = int(input("Juft sonni kiriting: "))
# if son % 2 == 0:
#     print("Rahmat")
# else:
#     print("Bu son juft emas")

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <= 4 or yosh >= 60:
#     print('Bepul')
# elif yosh > 4 and yosh < 18:
#     print("10000 sum")
# elif yosh >= 18 and yosh < 60:
#     print("20000 sum")

# son_1 = float(input("Birinchi sonni kiriting: "))
# son_2 = float(input("Ikkinchi sonni kiriting: "))
# if son_1>son_2:
#     print(f"{son_1}>{son_2}")
# elif son_1<son_2:
#     print(f"{son_1}<{son_2}")
# else:
#     print(f"{son_1}={son_2}")

# maxsulotlar = ['non', 'choy', 'guruch', 'olma', 'uzum', 'masla', 'banan', 'pomidor', 'bodring']
# savat = []
# bor_maxsulotlar = []
# mavjud_emas = []
# for n in range(5):
#     savat.append(input(f"{n+1}-maxsulotni kiriting: "))
# for tovar in savat:
#     if tovar in maxsulotlar:
#         bor_maxsulotlar.append(tovar)
#         # print(f"{tovar.title()} do\'konimizda bor")
#         # print(bor_maxsulotlar)
#     else:
#         mavjud_emas.append(tovar)
#         # print(f"{tovar.title()} do\'konimizda yo\'q")

# if mavjud_emas:
#     print("Do\'konimizda quyidagi maxsulotlar mavjud emas")
#     for maxsulot in mavjud_emas:
#         print(maxsulot)
# else:
#     print("Siz tanlagan maxsulotlar bor")

# foydalanuvchilar = ['ali', 'admin', 'shohbek', 'siro']
# login_user = input("Loginni tanlang: ")
# if login_user.lower() in foydalanuvchilar:
#     print(f"Xush kelibsiz {login_user}")
# else:
#     print('Login band, boshqa login tanlang')

son = int(input("Sonni kiriting: "))
bul_son = list(range(2,10))
for n in bul_son:
    if son % n == 0:
        print(f"{son} {n} ga qoldiqsiz bo\'linadi")

# print(bul_son)