# vyska, polomer vpisanej, opisanej, uhly, taznice, obvod, obsah, druhy trojuholnika
import math
a = int(input("Zadaj stranu a: "))
b = int(input("Zadaj stranu b: "))
c = int(input("Zadaj stranu c: "))
if a + b > c and a + c > b and b + c > a:
    print("Trojuholnik existuje")
    if  a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
        print("Trojuholnik je pravouhly")
        #ci je pravouhly
        if a==b==c:
            print("Trojuholník je rovnostranný")
            #ci je rovnostranny
            if a==b and a==c or a==c and b==c or b==c and a==c:
                print("Trojuholník je rovnoramenný")
                #ci je rovnoramenny
    o  = a+b+c
    po=o/2
    s= (po*(po-a)*(po-b)*(po-c))**0.5
    va= (2*s)/a
    vb= (2*s)/b
    vc= (2*s)/c
    polomer_vpisanej= (2*s)/o
    polomer_opisanej1= (a*b*c)/(4*s)
    #uhly
    alfa= round(math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c))),2)
    beta= round(math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c))),2)
    gamma= round(math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b))),2)

print("Obsah je :",s)
print("Výška na stranu a je :",va)
print("Výška na stranu b je :",vb)
print("Výška na stranu c je :",vc)  
print("Polomer vpisanej kruznice je :",polomer_vpisanej)
print("Polomer opisanej kruznice je :",polomer_opisanej1)
print("Uhol alfa je :",alfa)
print("Uhol beta je :",beta)
print("Uhol gamma je :",gamma)
print("Obvod je :",o)

