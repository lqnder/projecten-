# dit is de betere versie want de vorige deed het niet zo goed 
import math
import sys
g = 9.81
lijst = ['kinetische energie / KE','potentiële_zwaarte_energie / PE','potentiële_elastische_energie / PEE','arbeid / W']
#kinetische energie : formule , printen als v = 0 of m = 0 
def kinetische_energie():
        snelheid = v = float(input('snelheid : '))
        massa = m = float(input('massa : '))
        kinetische_energie = m/2*pow(v, 2)
        if v == 0:
            print('er is geen kinetische energie')
            sys.exit
        else : 
              print(f'de kinetische_energie bedraagt {kinetische_energie}')


#potentiËle zwaarte energie : formule ,  printen als h = 0 , g = 9,81 (constante)
def potentiële_zwaarte_energie():
        g = 9.81
        massa = m = int(input('massa : '))
        hoogte = h = int(input('hoogte : '))
        potentiële_zwaarte_energie = m*h*g
        if h == 0:
            print('er is geen potentiele zwaarte energie')
        else:
              print(f'de potentiele zwaarte energie bedraagt {potentiële_zwaarte_energie}')

#potentiële elastische energie
def potentiële_elastische_energie():
    k = veerconstanten = int(input('wat is de veerconstanten : '))
    l = lengte_verandering = int(input('wat is de lengte_vernandering'))
    potentiële_elastische_energie = k/2*pow(l , 2)
    if k == 0:
        print('er is geen elastische energie')
    else:
        print(f'de potentiele elastische energie bedraagt {potentiële_elastische_energie}')

def arbeid():
    kracht = f = float(input('wat is de kracht die je uitvoert  : '))
    afstand = x = float(input('wat is de afstand van het begin punt tot het einde : '))
    arbeid = f*x
    print(f'je hebt {arbeid:.>} arbeid verricht ')

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
