kitapList = []


def ekle():
    secim = 'H'
    while (secim == 'H'):
        kitap = input('Eklenecek kitap adını giriniz: ')
        if kitap != '':
            kitapList.append(kitap)
        while(True):
            secim = input('Bitirelim mi(E/H): ').upper()
            if secim == 'H' or secim == 'E':
                break
            else:
                print('\n!!!Lütfen sadece <E> veya <H> değerlerini giriniz!!!\n')


def sil():
    secim = 'H'
    while(secim == 'H'):
        kitapisim = input('Silinecek kitap adını giriniz: ')
        if kitapisim in kitapList:
            kitapList.remove(kitapisim)
            print(kitapisim, 'kitabı silindi!!')
        else:
            print('\nBöyle bir kitap yok!!\n')

        while(True):
            secim = input('Bitirelim mi(E/H): ').upper()
            if secim == 'H' or secim == 'E':
                break
            else:
                print('\n!!!Lütfen sadece <E> veya <H> değerlerini giriniz!!!\n')


def listele():
    while(True):
        i = 1
        for kitap in kitapList:
            print(i, '-', kitap)
            i += 1

        secim = input('Bitirelim mi(E/H): ').upper()
        if secim == 'H':
            continue
        elif secim == 'E':
            break
        else:
            print('\n!!!Lütfen sadece <E> veya <H> değerlerini giriniz!!!\n')


while (True):
    print('\n***ANA MENÜ***')
    print('1-Kitap ekleme')
    print('2-Kitap silme')
    print('3-Kitap listeleme')
    print('4-Çıkış\n')
    secim = input('Seçiminiz: ')
    if secim == '1':
        ekle()
    elif secim == '2':
        sil()
    elif secim == '3':
        listele()
    elif secim == '4':
        break
    else:
        print('Lütfen Sadece 1..4 arası sayı giriniz!\n')
