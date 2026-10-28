# Medborgerportalen - Text Adventure


# Funksjon som kontrollerer spillerens valg
def hent_valg():
    valg = input("Velg 1 eller 2: ")

    while valg != "1" and valg != "2":
        print("Ugyldig valg. Prøv igjen!")
        valg = input("Velg 1 eller 2: ")

    return valg


# Introduksjon til spillet
def introduksjon():
    print("====================================")
    print("          MEDBORGERPORTALEN")
    print("====================================")

    print()
    print("Du spiller som Erling.")
    print("Du er prosjektleder for kommunens nye medborgerportal.")

    print()
    print("Det har gått seks uker siden prosjektet startet.")
    print("I starten var samarbeidet godt, men nå har det oppstått konflikter.")
    print("Silje og Elias er uenige om teknologivalg.")
    print("Hamdi og Hallgeir er også uenige om hvordan innbyggerne skal delta.")

    print()
    print("Den første prototypen skal være ferdig om tre uker.")
    print("Det er nå opp til deg å lede prosjektet!")

    input("Trykk Enter for å starte...")


# Beslutning 1 - Silje og Elias
def beslutning1():
    print()
    print("====================================")
    print("     KAPITTEL 1 - SILJE OG ELIAS")
    print("====================================")

    print()
    print("Under et prosjektmøte begynner Silje og Elias å krangle.")
    print("Silje mener at Elias sitt forslag begrenser brukeropplevelsen.")
    print("Elias mener at Siljes forslag er for dyrt og usikkert.")
    print("Diskusjonen blir personlig, og resten av teamet blir stille.")

    print()
    print("Hva vil du gjøre?")
    print("1. Snakke med Silje og Elias individuelt")
    print("2. Ta konflikten opp i plenum")

    valg = hent_valg()

    if valg == "1":
        print()
        print("Du velger å snakke med dem hver for seg.")
        print("Begge får forklart sine synspunkter.")
        print("Konflikten roer seg, og samarbeidet blir bedre.")
        return 1

    else:
        print()
        print("Du tar konflikten opp foran hele teamet.")
        print("Diskusjonen blir enda mer opphetet.")
        print("Flere gruppemedlemmer begynner å ta parti.")
        print("Stemningen i teamet blir dårligere.")
        return 0


# Beslutning 2 - Hamdi og Hallgeir
def beslutning2(valg1):
    print()
    print("====================================")
    print("    KAPITTEL 2 - HAMDI OG HALLGEIR")
    print("====================================")

    print()

    # Tidligere valg påvirker historien
    if valg1 == 1:
        print("Etter samtalene med Silje og Elias har stemningen blitt bedre.")
        print("Teamet virker mer villig til å samarbeide.")

    else:
        print("Konflikten mellom Silje og Elias påvirker fortsatt teamet.")
        print("Flere gruppemedlemmer er frustrerte.")

    print()
    print("Noen dager senere oppstår en ny uenighet.")
    print("Hamdi ønsker å bruke kommunens eksisterende plattform.")
    print("Hallgeir ønsker en mer åpen løsning med flere muligheter for innspill.")
    print("Erling merker at frustrasjonen mellom dem øker.")

    print()
    print("Hva vil du gjøre?")
    print("1. Arrangere et felles møte")
    print("2. Vente og la dem løse konflikten selv")

    valg = hent_valg()

    if valg == "1":
        print()
        print("Du arrangerer et møte mellom Hamdi og Hallgeir.")
        print("Begge får forklart hva de ønsker.")
        print("Etter en diskusjon finner de et kompromiss.")
        print("De blir enige om en løsning som tar hensyn til begge parter.")
        return 1

    else:
        print()
        print("Du bestemmer deg for å vente.")
        print("Hamdi og Hallgeir klarer ikke å bli enige.")
        print("Frustrasjonen øker, og prosjektet mister verdifull tid.")
        return 0


# Beslutning 3 - Motivasjon og fremdrift
def beslutning3(poeng):
    print()
    print("====================================")
    print("     KAPITTEL 3 - MOTIVASJON")
    print("====================================")

    print()

    # Tidligere valg påvirker situasjonen
    if poeng == 2:
        print("Du har klart å håndtere begge konfliktene.")
        print("Samarbeidet fungerer bedre, men teamet begynner å bli slitent.")

    elif poeng == 1:
        print("Du har klart å løse én av konfliktene.")
        print("Det er fortsatt noen problemer med samarbeidet.")

    else:
        print("Begge konfliktene påvirker fortsatt teamet.")
        print("Stemningen er dårlig, og motivasjonen er lav.")

    print()
    print("Fristen for prototypen nærmer seg.")
    print("Du må bestemme hvordan teamet skal arbeide videre.")

    print()
    print("Hva vil du gjøre?")
    print("1. Prioritere relasjonsbygging")
    print("2. Prioritere fremdrift og leveranser")

    valg = hent_valg()

    if valg == "1":
        print()
        print("Du setter av tid til å forbedre samarbeidet.")
        print("Teamet får mulighet til å snakke sammen.")
        print("Stemningen blir bedre, og motivasjonen øker.")
        print("Samtidig blir det mindre tid til arbeidet med prototypen.")
        return 1

    else:
        print()
        print("Du bestemmer at prototypen må prioriteres.")
        print("Alle får tydelige arbeidsoppgaver og frister.")
        print("Arbeidet fortsetter, men noen konflikter forblir uløste.")
        return 0


# Funksjon som bestemmer avslutningen
def avslutning(poeng):
    print()
    print("====================================")
    print("             RESULTAT")
    print("====================================")

    print()
    print(f"Du fikk {poeng} av 3 poeng!")

    if poeng == 3:
        print()
        print("POSITIVT UTFALL!")
        print()
        print("Du har klart å håndtere konfliktene i teamet.")
        print("Silje og Elias samarbeider bedre.")
        print("Hamdi og Hallgeir har funnet et kompromiss.")
        print("Motivasjonen har økt, og teamet arbeider mot samme mål.")
        print("Prototypen blir ferdig innen fristen.")
        print("Teamet beveger seg mot norming-fasen.")

    elif poeng >= 1:
        print()
        print("DELVIS POSITIVT UTFALL!")
        print()
        print("Du har klart å håndtere noen av utfordringene.")
        print("Samarbeidet fungerer, men enkelte konflikter gjenstår.")
        print("Prototypen blir ferdig, men har noen mangler.")
        print("Du må fortsette å arbeide med samarbeidet i teamet.")

    else:
        print()
        print("NEGATIVT UTFALL!")
        print()
        print("Konfliktene i teamet har blitt verre.")
        print("Flere gruppemedlemmer er frustrerte.")
        print("Motivasjonen er lav, og samarbeidet fungerer dårlig.")
        print("Prototypen blir ikke ferdig innen fristen.")
        print("Prosjektet blir forsinket.")


# Funksjon som kjører hele spillet
def spill():
    poeng = 0

    introduksjon()

    # Beslutning 1
    valg1 = beslutning1()
    poeng += valg1

    # Beslutning 2
    valg2 = beslutning2(valg1)
    poeng += valg2

    # Beslutning 3
    valg3 = beslutning3(poeng)
    poeng += valg3

    # Avslutning
    avslutning(poeng)


# Hovedprogram - Spill på nytt
spill_igjen = "ja"

while spill_igjen == "ja":
    spill()

    print()
    spill_igjen = input("Vil du spille igjen? (ja/nei): ").lower()

    while spill_igjen != "ja" and spill_igjen != "nei":
        print("Ugyldig svar!")
        spill_igjen = input("Skriv ja eller nei: ").lower()

print()
print("Takk for at du spilte Medborgerportalen!")