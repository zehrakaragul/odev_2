# 1. Asal Sayı Kontrolü
def asal_mi(sayi):
    if sayi < 2:
        return f"{sayi} bir asal sayı değildir."

    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return f"{sayi} bir asal sayı değildir."

    return f"{sayi} bir asal sayıdır."


# Kullanıcıdan sayı alma
sayi = int(input("Bir sayı girin: "))

# Asal sayı kontrolü
print(asal_mi(sayi))
#
#
#


#2. Basit Hesap Makinesi
def hesap_makinesi(sayi1, sayi2, islem):
    if islem == '+':
        return f"{sayi1} + {sayi2} = {sayi1 + sayi2}"
    elif islem == '-':
        return f"{sayi1} - {sayi2} = {sayi1 - sayi2}"
    elif islem == '*':
        return f"{sayi1} * {sayi2} = {sayi1 * sayi2}"
    elif islem == '/':
        if sayi2 == 0:
            return "Bölme işlemi için ikinci sayı 0 olamaz!"
        return f"{sayi1} / {sayi2} = {sayi1 / sayi2}"
    else:
        return "Geçersiz işlem türü!"

# Kullanıcıdan iki sayı ve işlem türü alma
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
islem = input("İşlem türünü (+, -, *, /) girin: ")

# Hesap makinesi fonksiyonunu çağırma
print(hesap_makinesi(sayi1, sayi2, islem))