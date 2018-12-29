print("""
Girilen sayıyı girilen sayıyla çarpar.
Multiplies the number entered by itself

""")

sonuç = 1
while True:
    veri = int(input("Bir sayı girin / Enter a number: "))

    sonuç = veri*veri
    print()
    print("Girilen sayının kendiyle çarpımı",
          "Multiplied by the number entered: ",sonuç,sep="\n")
    print("\n"*2)
    

