import bil

looping=True
Bmw_svart = bil.Bil("Bmw", "svart", 3)
merca_gul = bil.Bil("Merca", "Gul", 6)
ferrari_röd = bil.Bil("Ferrari", "Röd", 9)
toyota_lila = bil.Bil ("Toyota", "lila", 1)

billista = [Bmw_svart, merca_gul, ferrari_röd, toyota_lila]

print(Bmw_svart.getFabrikat())

while looping:
      
      i = 0

      for bil in billista:
            print(str(i+1) + ". Fabrikat: " + bil.getFabrikat() +", Färg: " + bil.getColour())
            i += 1
    
      bil_nr = input("\n Mata in bilnr för vald bil: ")

      print("\n En " + billista[int(bil_nr)-1].fabrikat + ", Färg: " + billista[int(bil_nr)-1].colour)


      svar_anvandare = input("\n Vill du avsluta programmet? j/n : ")

      if (svar_anvandare == "j"):
            break