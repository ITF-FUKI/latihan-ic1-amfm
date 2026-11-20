def sapa_pengguna():
    nama = input("Masukkan nama kamu: ")
    print(f"\nHalo, {nama}! Selamat datang di program Python pertamamu.\n")

def HelloWorld(s):
    print(s)

def hitung():
    try:
        HelloWorld("Hello World!")
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        
        print("\nPilih operasi:")
        print("1. Tambah (+)")
        print("2. Kurang (-)")
        print("3. Kali (*)")
        print("4. Bagi (/)")
        print("5. Modulo (%)")
        print("6. Floor (//)")
        print("7. Pangkat (**)")
        
        pilihan = input("Masukkan pilihan (1/2/3/4): ")
        
        if pilihan == '1':
            print(f"Hasil: {angka1} + {angka2} = {angka1 + angka2}")
        elif pilihan == '2':
            print(f"Hasil: {angka1} - {angka2} = {angka1 - angka2}")
        elif pilihan == '3':
            pass
        elif pilihan == '4':
            print(f"Hasil: {angka1} * {angka2} = {angka1 * angka2}")
            if angka2 != 0:
                print(f"Hasil: {angka1} / {angka2} = {angka1 / angka2}")
            else:
                print("Error: Tidak bisa membagi dengan angka nol.")
        else:
            print("Pilihan tidak valid.")
            print("TestASKJDHKJSADHASKDBASJKDNBKASJDNLASDHASLDKKLASDJLKASJDLASKJD")
            
    except ValueError:
        print("Error: Harap masukkan angka yang valid.")

if __name__ == "__main__":
    sapa_pengguna()
    hitung()
    print("Xx_AkhtarKAz_xX")
