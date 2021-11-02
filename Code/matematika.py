# tahap pengembangan ~

def kaidah_pencacahan():
    txt = input("Nilai (ex : 1 2 3 4...) = ")
    x = txt.replace(' ', '*')
    print(f'Hasil Pencacahan = {eval(x)}')
    print('\n')

    back = input('Coba lagi [Y/N] ? ').upper()
    if back == 'Y':
        print('\n')
        return kaidah_pencacahan()
    else:
        menucal()

def filling_slot():
    import os

    os.system('cls')
    print('Code created by @xcl')
    print(120*"=")
    print("a. Angka boleh Berulang")
    print("b. Angka tidak boleh Berulang\n")
    c = input("Masukkan pilihan a/b > ").lower()
    if c == 'a':
        x = input("Masukkan angka > ").split(' ')
        y = input('Jumlah digit > ')
        z = len(x)
        out = int(z)**int(y)
        print(f'Hasil = {out} cara\n')
        back = input('Coba lagi [Y/N] ? ').upper()
        if back == 'Y':
            print('\n')
            return filling_slot()
        else:
            menucal()
    elif c == 'b':
        x = input("Masukkan angka > ").split(' ')
        y = input('Jumlah digit (max 10)> ')
        z = len(x)
        out1 = int(z)
        out2 = int(z)*int(z-1)
        out3 = int(z)*int(z-1)*int(z-2)
        out4 = int(z)*int(z-1)*int(z-2)*int(z-3)
        out5 = int(z)*int(z-1)*int(z-2)*int(z-3)*int(z-4)
        out6 = int(z)*int(z-1)*int(z-2)*int(z-3)*int(z-4)*int(z-5)
        out7 = int(z)*int(z-1)*int(z-2)*int(z-3)*int(z-4)*int(z-5)*int(z-6)
        out8 = int(z)*int(z-1)*int(z-2)*int(z-3)*int(z-4)*int(z-5)*int(z-6)*int(z-7)
        out9 = int(z)*int(z-1)*int(z-2)*int(z-3)*int(z-4)*int(z-5)*int(z-6)*int(z-7)*int(z-8)
        out10 = int(z)*int(z-1)*int(z-2)*int(z-3)*int(z-4)*int(z-5)*int(z-6)*int(z-7)*int(z-8)*int(z-9)
        print(f'Banyak Digit 1 > {out1}')
        print(f'Banyak Digit 2 > {out2}')
        print(f'Banyak Digit 3 > {out3}')
        print(f'Banyak Digit 4 > {out4}')
        print(f'Banyak Digit 5 > {out5}')
        print(f'Banyak Digit 6 > {out6}')
        print(f'Banyak Digit 7 > {out7}')
        print(f'Banyak Digit 8 > {out8}')
        print(f'Banyak Digit 9 > {out9}')
        print(f'Banyak Digit 10 > {out10}\n')
        if z == int(y):
            print(f'Banyak Digit {y} > 1\n')
        else:
            pass

    back = input('Coba lagi [Y/N] ? ').upper()
    if back == 'Y':
        print('\n')
        return filling_slot()
    else:
        menucal()

def notasi_faktorial():
    import math

    print(120*'=')
    n = int(input('Masukkan nilai faktorial > '))
    fak = math.factorial(n)
    print(f'\nNilai {n}! adalah {fak}')
    
    back = input('\nCoba lagi [Y/N] ? ').upper()
    if back == 'Y':
        print('\n')
        return notasi_faktorial()
    else:
        menucal()

def permutasi_unsur_berbeda():
    import math
    print(120*'=')
    print('Index nilai = "nPr"')
    n = int(input('Masukkan nilai n > '))
    r = int(input('Masukkan nilai r > '))
    z = (n-r)
    n_fac = math.factorial(n)
    z_fac = math.factorial(z)
    out = n_fac/z_fac
    print(f'\nHasil = {int(out)} Cara ')

    back = input('\nCoba lagi [Y/N] ? ').upper()
    if back == 'Y':
        print('\n')
        return permutasi_unsur_berbeda()
    else:
        menucal()

def permutasi_unsur_sama():
    pass

def permutasi_siklis():
    pass

def kombinasi():
    pass

def ruang_sampel():
    pass

def peluang_kejadian():
    pass

def frekuensi_harapan():
    pass

def peluang_kejadian_saling_lepas():
    pass

def peluang_kejadian_saling_bebas():
    pass

def statistika():
    pass

def ukuran_pemusatan_data_tunggal():
    pass

def menucal():
    import os
    import time
    from Code import menu as m

    os.system('cls')
    os.system('color 9')
    print('Code created by @xcl')
    print(120*"=")
    print('0. Exit')
    print('1. Kaidah pencacahan')
    print('2. Filling slot')
    print('3. Notasi faktorial')
    print('4. Permutasi unsur berbeda')
    print('5. Permutasi unsur sama')
    print('6. Permutasi Siklis')
    print('7. Kombinasi')
    print('8. Ruang Sampel')
    print('9. Peluang kejadian')
    print('10. Frekuensi harapan')
    print('11. Peluang kejadian saling lepas')
    print('12. Peluang kejadian saling bebas')
    print('13. Statistika')
    print('14. Ukuran pemusatan data tunggal')
    print(120*"=")
    i = input("Code Program > ")
    print('\n')
    
    if i=='1':
        kaidah_pencacahan()
        os.system('cls')
        print('Code created by @xcl')
    
    elif i=='2':
        filling_slot()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='3':
        notasi_faktorial()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='4':
        permutasi_unsur_berbeda()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='5':
        permutasi_unsur_sama()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='6':
        permutasi_siklis()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='7':
        kombinasi()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='8':
        ruang_sampel()
        os.system('cls')
        print('Code created by @xcl')
    
    elif i=='9':
        peluang_kejadian()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='10':
        frekuensi_harapan()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='11':
        peluang_kejadian_saling_lepas()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='12':
        peluang_kejadian_saling_bebas()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='13':
        statistika()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='14':
        ukuran_pemusatan_data_tunggal()
        os.system('cls')
        print('Code created by @xcl')

    elif i=='0':
        os.system('cls')
        print('Code created by @xcl')
        m.show_menu()
        
    else:
        os.system('cls')
        os.system('color 4')
        print("Code salah !")
        time.sleep(0.2)
        os.system('cls')
        print('Code created by @xcl')
        return menucal()