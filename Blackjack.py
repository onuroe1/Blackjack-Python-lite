'''
Author: Onur Ökten
Datum : 19.03.2026
'''
### Imports ###

import random

### Variablen ###

lSpielDeck = [2,3,4,5,6,7,8,9,10,10,10,10,11]*4 # Blackjack Spieldeck

### Funktionen ###

def ZieheKarte():
    karte = random.choice(lSpielDeck)
    return karte

# Berechnet Punkte und wandelt Asse (11) in 1 um wenn man über 21 kommt   
def PunkteBerechnen(hand):
    punkte = sum(hand)
    while punkte > 21 and 11 in hand:
        punkte -= 10
        hand.remove(11)
        hand.append(1)
    return punkte

# Schleife damit man das Spiel immer wiederholen kann
while True:
    spielerhand = []
    spielerhand.append(ZieheKarte())
    spielerhand.append(ZieheKarte())

    dealerhand = []
    dealerhand.append(ZieheKarte())
    dealerhand.append(ZieheKarte())

    print(f"Deine Karten: {spielerhand}")
    print(f"Deine Punkte: {PunkteBerechnen(spielerhand)}")

# Spieler zieht Karten
    while PunkteBerechnen(spielerhand) < 21:
        eingabe = input("Möchtest du noch eine Karte ziehen? j/n: ")
        if eingabe == "j":
            spielerhand.append(ZieheKarte())
            print(f"Deine Karten: {spielerhand}")
            print(f"Deine Punkte: {PunkteBerechnen(spielerhand)}")
        else:
            break
# Dealer Zug
    if PunkteBerechnen(spielerhand) > 21:
        print("Bust! Du hast über 21 und verloren.")
    else:
        print("Der Dealer ist nun dran...")
        while PunkteBerechnen(dealerhand) < 17: # Dealer muss ziehen bis er min. 17 Punkte hat
            dealerhand.append(ZieheKarte())
        
        print(f"Dealer-Karten: {dealerhand}, Punkte: {PunkteBerechnen(dealerhand)}")
        
# Gewinner ermitteln

        sPunkteSpieler = PunkteBerechnen(spielerhand)
        sPunkteDealer  = PunkteBerechnen(dealerhand)

        if sPunkteDealer > 21:
            print("Du hast gewonnen!")
        elif sPunkteDealer == sPunkteSpieler:
            print("Oh, Unentschieden")
        elif sPunkteSpieler > sPunkteDealer:
            print("Du hast gewonnen!")
        else:
            print("Du hast verloren.")

# Neustart Abfrage

    nochmal = input("Willst du noch eine Runde (j/n): ")
    if nochmal == "n":
        print("Danke fürs Spielen! Bis zum nächsten Mal.")
        break
        

        
    
                        
              

    
    
    
    
    

