def luas_segitiga():
    print()
    print("Luas segitiga")
    alas = int(input ("masukkan alas: "))
    tinggi = int(input ("masukkan tinggi: "))
    alas = 0.5 * alas * tinggi
    print("Luas segitiga adalah: {}.format(luas)")
    print()

def luas_persegi_panjang():
    print()
    print("Luas persegi panjang")
    panjang = int(input("masukkan panjang: "))
    lebar = int(input("masukkan lebar: "))
    luas = panjang * lebar
    print("Luas persegi panjang adalah: {}.format(luas)")
    print()

def luas_lingkaran():
    print()
    print("Luas lingkaran")
    jarijari = int(input("masukkan jari-jari: " ))
    luas = 3.14 * jarijari * jarijari
    print("Luas lingkaran adalah: {}.format(luas)")
    print()

def luas_jajar_genjang():
    print()
    print("Luas jajar genjang")
    alas = int(input("masukkan jari-jari: " ))
    tinggi = int(input("masukkan tinggi: " ))
    print("Luas jajar genjang adalah: {}.format(luas)")
    print()

if __name__ == "__main__":
    while True:
        print("Menu")
        print("==============")
        print("1. Luas segitiga")
        print("2. Luas persegi panjang")
        print("3. Luas linkaran")
        print("4. Luas jajar genjang")
        print("5. Keluar")
        menu = int(input("pilih menu: "))

        if menu == 5:
            break

        if menu == 1:
            luas_segitiga()
        elif menu == 2:
            luas_persegi_panjang()
        elif menu == 3:
            luas_lingkaran()
        elif menu == 4:
            luas_jajar_genjang()
