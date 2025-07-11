

 # 1. KVADRATNI PARAMETRINI TOPISH UCHUN

 side = float (input("Parametr topish uchun Kvadrat tomonini kiriting :"))
 parametr = 4*side
 print(" Kvadratning parametri :",parametr)



 # KVADRATNI YUZASINI TOPISH UCHUN



side = float (input("Yuzani topish uchun Kvadrat tomonini kiriting :"))
area = side ** 2
print(" Kvadratning parametri :",area)


# 2. DOIRANI DIAMETRINI TOPISH 


sircle = float (input("Doirani Diametrini kiriting : "))
radius = sircle / 2
parametr = 2 * 3.14 * radius
print(" Kvadratning parametri :",parametr)




#  3. A VA B NI O'RTACHA QIYMATINI TOPISH 

a = float (input(" A ni kititng :"))
b = float (input(" B ni kititng :"))
mean = (a+b)/2
print(" O'rtacha qiymat :",mean)



# 4. A VA B NI YIGINDI , KO'PAYTMA VA KVADRATI


a = int (input(" A ni kititng :"))
b = int (input(" B ni kititng :"))
yigindi = a+b
kopaytma = a*b
kvadrat1 = a**2
kvadrat2 = b**2

print (" A va B ni yigindisi :",yigindi)
print (" A va B ni ko'paytmasi :",kopaytma)
print (" A ni kvadrati :",kvadrat1)
print (" B ni kvadrati :", kvadrat2)

