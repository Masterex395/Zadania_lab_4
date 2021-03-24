# # Zad 1
# import sys
# plik = open("zadanie1.txt", "w+")
# import random
# losowo = []
# for x in range(5):
#     losowo.append(random.randint(0, 30))
# print(losowo)
# mnozenie = [x*2 for x in losowo]
# print(mnozenie)
# plik.writelines(str(mnozenie))
# plik.close()

# # Zad 2
# plik = open("zadanie1.txt", "r+")
# wyswietl = plik.readlines()
# print(wyswietl)

# # Zad 3
# with open("zadanie3.txt", "w") as plik:
#     for newLine in range(5) :
#         plik.write("Tu powinien byc napis\n")
# with open("zadanie3.txt", "r") as plik:
#     for line in plik:
#         print(line, end="")

# # Zad 4
# class NaZakupy:
#     nazwa_produktu = ""
#     ilosc = 0
#     jednostka_miary = ""
#     cena_jed = 0
#
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc=ilosc
#         self.jednostka_miary=jednostka_miary
#         self.cena_jed=cena_jed
#     def wyswietl_produkt(self):
#         print(self.ilosc, self.nazwa_produktu, self.jednostka_miary, self.cena_jed)
#     def ile_produktu(self):
#         print(str(self.ilosc)+" "+self.jednostka_miary)
#     def ile_kosztuje(self):
#         cena_koncowa = self.cena_jed*self.ilosc
#         return cena_koncowa
#
# produkt = NaZakupy("Żwir", 15, "T", 50)
# produkt.wyswietl_produkt()
# produkt.ile_produktu()
# print(str(produkt.ile_kosztuje())+(" zł"))
