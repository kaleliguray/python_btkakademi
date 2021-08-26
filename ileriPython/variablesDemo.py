# -*- coding: utf-8 -*-
"""
    1- Bir müşterinin aşağıdaki bilgileri içeren değişken oluşturunuz

    adı,soyadı,ad + soyad, cinsiyet,tc kimlik, doğum yılı, adres bilgisi, yaşı


"""

customerName = "Guray"
customerSurname = "Kaleli"

customer = customerName + " " + customerSurname

customerGender = True # Male => true Female => false
customerTcNo = "12883729492"
customerBirthYear = 1992
customerAdress = "Istanbu/TURKEY"
customerAge = 2021 - customerBirthYear
print(customerAge)


"""

    2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız

    siparis 1 : 110 tl
    siparis 2 : 1100.5 tl
    siparis 3 : 356.95 tl

"""

order1 = 110
order2 = 1100.5
order3 = 356.95

total = order1 + order2 + order3

print("Total : ",total)






