# dit is de betere versie want de vorige deed het niet zo goed 
import math
import sys
g = 9.81
lijst = ['kinetische energie / KE','potentiële_zwaarte_energie / PE','potentiële_elastische_energie / PEE','arbeid / W']
#kinetische energie : formule , printen als v = 0 of m = 0 
def kinetische_energie():
        snelheid = v = float(input('snelheid : '))
        massa = m = float(input('massa : '))
        if v == 0:
            print('er is geen kinetische energie')
            sys.exit
        else : 
              print(m/2*pow(v , 2))


#potentiËle zwaarte energie : formule ,  printen als h = 0 , g = 9,81 (constante)
def potentiële_zwaarte_energie():
        massa = m = float(input('massa : '))
        hoogte = h = float(input('hoogte : '))
        if h == 0:
            print('er is geen potentiele zwaarte energie')
        else:
              print(m*h*g)

#potentiële elastische energie
def potentiële_elastische_energie():
    k = veerconstanten = float(input('wat is de veerconstanten : '))
    l = lengte_verandering = float(input('wat is de lengte_vernandering'))
    if k == 0:
        print('er is geen elastische energie')
    else:
        print(k/2*pow(l , 2))

#arbeid
def arbeid():
    kracht = f = float(input('wat is de kracht die je uitvoert'))
    afstand = x = float(input('wat is de afstand van het begin punt tot het einde : '))
    if x or f == 0:
        print('er is geen arbeid verricht')
    else : 
        print(f*x)

#wrijving
def wrijvings_kracht():
    kracht = f = float(input('wat is de kracht die je uitvoert'))
    afstand = x = float(input('wat is de afstand van het begin punt tot het einde : '))
    if x or f > 0:
         print('er is geen wrijvingskracht')
    else : 
       print(-f*x) 

#rendement
def rendement():
    kinetische_energie  = float(input('wat is de kinetische energie : '))
    potentiële_zwaarte_energie = float(input('wat is de potentiele zwaarte energie : '))
    potentiële_elastische_energie = float(input('wat is de potentiele elastische energie : '))
    Etotaal = kinetische_energie + potentiële_zwaarte_energie + potentiële_elastische_energie
    warmte = Q = kinetische_energie - potentiële_zwaarte_energie
    Enuttig = Etotaal - Q
    rendement = n = Enuttig/Etotaal   
    print(rendement)

#etotaal
def Etotaal():
    kinetische_energie  = float(input('wat is de kinetische energie : '))
    potentiële_zwaarte_energie = float(input('wat is de potentiele zwaarte energie : '))
    potentiële_elastische_energie = float(input('wat is de potentiele elastische energie : '))
    warmte = Q = kinetische_energie - potentiële_zwaarte_energie
    Etotaal1 = int(kinetische_energie + potentiële_elastische_energie + potentiële_zwaarte_energie)
    if kinetische_energie and potentiële_elastische_energie and potentiële_zwaarte_energie == 0:
        print('geen energie waarom probeer je energie te berekenen als je geen energie hebt kieken een kind van vier is slimmer dan u verspil mijn tijd niet alsjeblief dit programma is zo saai ik moet eigenlijk gaan slapen')
    else:
        print(kinetische_energie + potentiële_elastische_energie + potentiële_zwaarte_energie)
      

def Enuttig():
    Etotaal = kinetische_energie + potentiële_elastische_energie + potentiële_zwaarte_energie
    warmte = Q = kinetische_energie - potentiële_zwaarte_energie

    print(Etotaal - Q) 


while True:
     input(f'wat wil je doen {lijst} ? :  ')
     bob = 0
     bob +=1
     if bob == 560:
          break
