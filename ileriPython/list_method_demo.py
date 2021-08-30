names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")
print("Names : ", names)

# 2-  "Sena" değerini listenin başına ekleyiniz.

#names[0] = "Sena"
names.insert(0,"Sena")
print("Names : ",names)

# 3-  "Deniz" ismini listeden siliniz.

#names.remove("Deniz")
names.pop(3)
print("Names : ",names)

# 4-  "Deniz" isminin indeksi nedir ?

names.insert(3,"Deniz")
print("Names : ",names.index("Deniz"))

# 5-  "Ali" listenin bir elemanı mıdır ?

print("Ali" in names)

# 6-  Liste elemanlarını ters çevirin.
names.reverse()
print(names)

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.

names.sort()
print(names)

# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.

years.sort()
print(years)

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia"
anotherStr = str.split(",")
print(anotherStr)

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?

min,max = min(years),max(years)
print("Min : ",min,"Max : ",max)

# 11- years dizisinde kaç tane 1998 değeri vardır ?

print(years.count(1998))

# 12- years dizisinin tüm elemanlarını siliniz.

years.clear()
print(years)

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

marks = []

mark1 = input("Marka : ")
marks.append(mark1)

mark2 = input("Marka : ")
marks.append(mark2)

mark3 = input("Marka : ")
marks.append(mark3)


print(marks)



