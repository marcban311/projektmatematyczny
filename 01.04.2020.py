import math
import numpy as np

masa= int(input("Podaj masę ciała w kilogramach znajdującego się na pochylni "))

while (True):
    a1=int(input("Podaj kąt w stopniach jaki tworzy pochylnia z podłożem w przedziale od 0 do 90 stopni"))
    if (a1 < 90) and (a1 > 0):
        break;

a2= a1*math.pi/180
calfa = math.cos(a2)

while (True):
    wsp=float(input("Podaj współczynnik w przedziale od 0 do 1"))
    if (wsp < 1.0) and (wsp > 0.0): 
        break;
        
i=int(input("Podaj jak dokładny ma być wynik siły tarcia podająć ilość miejsc po przecinku."))
g=9.80665
g1 = round(g,i)     
ft=(calfa*masa*g1*wsp)
ft1= round(ft,i)

print(ft1)