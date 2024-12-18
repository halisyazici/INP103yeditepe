preis=float(input("Buchpreis: "))
rabatt=float(input("Rabatt: %"))/100
kargo_1=float(input("Kargo 1.: "))
kargo=float(input("Kargo 2.: "))
zahl=float(input("Zahl "))
#60 kitabın fatura bedelini hesaplayın30

print(((preis-preis*rabatt)*zahl)+(kargo_1+kargo*(zahl-1)))