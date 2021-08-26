websitesi = "http://www.sadıkturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#   1-'course' karakter dizisinde kaç karakter bulunmaktadır.

print("1. soru : ", len(course))

#    2-'websitesi' içinden www karakterlerini alın.

print(websitesi[7:10])

letterW = ""
for s in websitesi:
    if s == "w":
        letterW += s
print("2.soru : ", letterW)

#    3-'websitesi' içinde com karakterini alın.

print(websitesi[22:25])
print(websitesi[len(websitesi) - 3:len(websitesi)])

letterCom = ""
for s in websitesi:
    if s == "c":
        letterCom += s
    if s == "o":
        letterCom += s
    if s == "m":
        letterCom += s
print("3.soru : ", letterCom)

#    4-'course' içinden ilk 15 ve son 15 karakterini alın

print("4.soru :\nfirst 15th character of website : " + websitesi[0:15] +
      "\n-----------------\n"
      " last 15th character of website : " + websitesi[15:])

#    5-'course' ifadesindeki karakterleri tersten yazdırın

print(course[::-1])

temp = ""

for i in course[len(course):0:-1]:
    temp += i

print("5.soru : ", temp)
"""

    - Aşağıda verilen değişkenlerle ekrana aşağıdaki ifadeyi yazdırın.
        'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'

    - 'hello world' ifadesindeki 'w' harfini 'W' ile değiştirin.

    - 'abc' ifadesini yan yana 3 defa yazdırın.

"""

name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"

print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.")

statement = "hello world"

print(statement.replace("w", "W"))

print("abc " * 3)

# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

message = ' Hello World '
print(message.strip())

#result = websitesi.lstrip('/:pth')
#print(result)

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

print('www.sadikturan.com'.strip('w.com'))

# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

print(course.lower())
print(course.title())

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))

print(websitesi.count('a'))

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?

print(websitesi.startswith("www"))
print(websitesi.endswith("com"))

# 6-  'website' içinde '.com' ifadesi var mı?

print(websitesi.find(".com"))

print(websitesi.index(".com"))

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

print(course.isalpha())
print("hello".isalpha())

print(course.isdigit())
print("1213".isdigit())

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

print('Contents'.center(50, "-"))
print('Contents'.ljust(50, "-"))
print('Contents'.rjust(50, "-"))

# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.

print(course.replace(" ", "-"))

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin

print("Hello World".replace("World", "There!"))

# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.

print(course.split(" "))
