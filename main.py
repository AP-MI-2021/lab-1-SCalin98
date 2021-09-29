'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici
          if n < 2 : return 0
          else :
            for divizor in range (2,int(n/2)+1) :
                if n%divizor == 0 : return 0

            return 1

  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
     produs = 1
     for elemLista in lst :
         produs = produs * elemLista
     return produs
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
  nrMaxim = max(x,y)
  nrMinim = min(x,y)
  for numerePanaLa in range(nrMinim,0,-1):
      if nrMaxim%numerePanaLa==0 and nrMinim%numerePanaLa ==0:
          return numerePanaLa
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  nrMinim = min(x,y)
  nrMaxim = max(x,y)
  while nrMinim:
      rest = nrMaxim % nrMinim
      nrMaxim = nrMinim
      nrMinim = rest
  return nrMaxim

  
def main():
  # interfata de tip consola aici
   print("Introduceti cifra corespunzatoare subprogramului pe care doriti sa-l verificati :")
   print("1.is_prime")
   print("2.get_product")
   print("3.get_cmmdc_v1")
   print("4.get_cmmdc_v2")
   alegereSubprog = int(input())
   if alegereSubprog == 1:
       n = int(input("Introduceti numarul n pentru a determina daca acesta este prim"))
       if is_prime(n) : print("Numarul este prim")
       else : print("Numarul nu este prim")
   elif alegereSubprog == 2 :
       lst = []
       numarElementeLista = int(input("Introduceti numarul de elemente al listei"))
       for indiceLista in range(0,numarElementeLista):
           numarCitit = int(input())
           lst.append(numarCitit)
       print("Produsul elementelor din sir este :")
       print(get_product(lst))
   elif alegereSubprog == 3 or alegereSubprog == 4 :
       print("Introduceti numerele x si y ale caror c.m.m.d.c. va fi calculat")
       x = int(input())
       y = int(input())
       if alegereSubprog == 3 : print(get_cmmdc_v1(x,y))
       elif alegereSubprog == 4 : print(get_cmmdc_v2(x,y))


if __name__ == '__main__':
  main()
