'''
    ogrenciler = {
        '120': {
            'ad': 'Ali',
            'soyad': 'Yılmaz',
            'telefon': '532 000 00 01'
        },
        '125': {
            'ad': 'Can',
            'soyad': 'Korkmaz',
            'telefon': '532 000 00 02'
        },
        '128': {
            'ad': 'Volkan',
            'soyad': 'Yükselen',
            'telefon': '532 000 00 03'
        },
    }
    1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
       dictionary içinde saklayınız.
    2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
'''

students = {}

number = input("School Number : ")
firstName = input("First Name : ")
lastName = input("Last Name : ")
phone = input("Phone : ")

students.update({
    number : {
        "Name":firstName,
        "Surname":lastName,
        "Phone":phone
    }
})

number = input("School Number : ")
firstName = input("First Name : ")
lastName = input("Last Name : ")
phone = input("Phone : ")

students.update({
    number : {
        "Name":firstName,
        "Surname":lastName,
        "Phone":phone
    }
})

number = input("School Number : ")
firstName = input("First Name : ")
lastName = input("Last Name : ")
phone = input("Phone : ")

students.update({
      number : {
        "Name":firstName,
        "Surname":lastName,
        "Phone":phone
    }
})

print(students)

print("-"*10)

student_no = input("Student no : ")


print(f"Aradığınız {student_no} nolu öğrencinin adı: {students[student_no]['Name']} soyadı: {students[student_no]['Surname']} ve telefonu ise {students[student_no]['Phone']}")


































