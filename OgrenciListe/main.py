ogrenciler = {}


def ekle():
    secim = 'e'
    while (secim == 'e'):
        no = input('\nÖğrenci no giriniz: ')
        sinif = input('Öğrenci sınıfı giriniz: ')
        isim = input('Öğrenci adını ve soyadını giriniz: ')
        if no == '':
            continue
        ogrenciler[no] = {'sinif': sinif, 'isim': isim}
        while(True):
            secim = input('Devam edelim mi (e/h): ').lower()
            if secim == 'e' or secim == 'h':
                break
            else:
                print('\n!!!Lütfen sadece <e> veya <h> değerlerini giriniz!!!\n')


def ara():
    no = input('\nAranacak öğrenci numarası: ')
    if no in ogrenciler.keys():
        ogr = ogrenciler[no]
        print()
        print("{:<5} {:<7} {:<12}".format('No', 'Sınıf', 'Adı Soyadı'))
        print("{:<5} {:<7} {:<12}".format('--', '-----', '----------'))
        print("{:<5} {:<7} {:<12}".format(no, ogr['sinif'], ogr['isim']))


def listele():
    print()
    print("{:<5} {:<7} {:<12}".format('No', 'Sınıf', 'Adı Soyadı'))
    print("{:<5} {:<7} {:<12}".format('--', '-----', '----------'))
    for no, ogr in ogrenciler.items():
        print("{:<5} {:<7} {:<12}".format(no, ogr['sinif'], ogr['isim']))


while (True):
    print('\n*-------------MENU-------------*')
    print('1-Öğrenci ekleme')
    print('2-Öğrenci arama (Öğrenci no ile)')
    print('3-Sınıf Listesi')
    print('4-Çıkış')
    print('*------------------------------*')
    secim = input('Seçiminiz (1-2-3-4): ')
    if secim == '1':
        ekle()
    elif secim == '2':
        ara()
    elif secim == '3':
        listele()
    elif secim == '4':
        break
    else:
        print('\nYanlış seçim yaptınız')
