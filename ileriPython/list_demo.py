# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

cars = ["Bmw","Mercedes","Opel","Mazda"]

print(cars)

# 2-  Liste Kaç elemanlıdır ?

print(len(cars))

# 3-  Listenin ilk ve son elemanı nedir ?

print("first member " + cars[0] + "\nlast member " + cars[-1])

# 4-  Mazda değerini Toyota ile değiştirin.

cars[-1] = "Toyota"

print(cars)

# 5-  Mercedes listenin bir elemanı mıdır ?

print("Mercedes" in cars)

# 6-  Listenin -2 indeksindeki değer nedir ?

print(cars[-2])

# 7-  Listenin ilk 3 elemanını alın.

print(cars[0:3])

# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.

cars[-2:] = ["Toyota","Renault"]

print(cars)

# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.

cars = cars + ["Audi","Nissan"]

print(cars)

# 10- Listenin son elemanını silin.

del cars[-1]

print(cars)

# 11- Liste elemanlarını tersten yazdırınız.

print(cars[::-1])

# 12- Aşağıdaki verileri bir liste içinde saklayınız. 

      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90) 

studentA = ["Yiğit","Bilgi",2010,[70,60,70]]

studentB = ["Sena","Turan",1999,[80,80,70]]

studentC = ["Ahmet","Turan",1998,[80,70,90]]


# 13- Liste elemanlarını ekrana yazdırınız.
print("\n")
print(studentA,"\n")
print(studentB,"\n")
print(studentC)
print("\n")
print(f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3:1.3}")
































