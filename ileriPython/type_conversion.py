"""

    Daire alanı : πr^2
    Daire çevresi : 2πr

    Yarı çapı verilen bir dairenin alanı ve çevresini hesaplayınız.(π = 3.14)


"""
radius = int(input("radius : "))
pi = 3.14

area = pi * (radius**2)

circumference = 2 * pi * radius

print("Area : ", area)
print("Circumference : ", circumference)
