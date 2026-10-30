# Funksjon som kontrollerer spillerens valg
def hent_valg():
    # Ber spilleren velge mellom 1 og 2
    valg = input("Velg 1 eller 2: ")

    # Sjekker om valget er gyldig
    if valg == "1" or valg == "2":
        return valg
    else:
        # Hvis valget er feil, blir valg 2 valgt automatisk
        print("Ugyldig valg. Du får automatisk valg 2.")
        return "2"


# Introduksjon til spillet
def introduksjon():
    # Viser tittelen på spillet
    print("====================================")
    print("          Konfliktløseren")
    print("====================================")

    print()
    print("Velkommen Erling.")

    print()
    print("Det har gått seks uker siden prosjektet startet.")
    print("I starten var samarbeidet godt, men nå har det oppstått konflikter.")
    print("Silje og Elias er uenige om teknologivalg.")
    print("Hamdi og Hallgeir er også uenige om hvordan innbyggerne skal delta.")

    print()
    print("Den første prototypen skal være ferdig om tre uker.")
    print("Det er nå opp til deg å lede prosjektet!")

    # Venter på at spilleren trykker Enter
    input("Trykk Enter for å starte...")


# Beslutning 1 - Silje og Elias
def beslutning1():
    print()
    print("====================================")
    print("     BESLUTNING 1 - SILJE OG ELIAS")
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

    # Henter valget fra spilleren
    valg = hent_valg()

    # Sjekker hvilket valg spilleren tok
    if valg == "1":
        print()
        print("Du velger å snakke med dem hver for seg.")
        print("Begge får forklart sine synspunkter.")
        print("Konflikten roer seg, og samarbeidet blir bedre.")

        # Gir 1 poeng for et positivt valg
        return 1
    else:
        print()
        print("Du tar konflikten opp foran hele teamet.")
        print("Diskusjonen blir enda mer opphetet.")
        print("Flere gruppemedlemmer begynner å ta parti.")
        print("Stemningen i teamet blir dårligere.")

        # Gir 0 poeng for negativt valg
        return 0


# Beslutning 2 - Hamdi og Hallgeir
# Tar med resultatet fra beslutning 1
def beslutning2(valg1):
    print()
    print("====================================")
    print("    BESLUTNING 2 - HAMDI OG HALLGEIR")
    print("====================================")

    print()

    # Viser hvordan det første valget påvirket teamet
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
    print("Frustrasjonen mellom dem øker.")

    print()
    print("Hva vil du gjøre?")
    print("1. Arrangere et felles møte")
    print("2. Vente og la dem løse konflikten selv")

    # Henter et nytt valg fra spilleren
    valg = hent_valg()

    if valg == "1":
        print()
        print("Du arrangerer et møte mellom Hamdi og Hallgeir.")
        print("Begge får forklart hva de ønsker.")
        print("Etter en diskusjon finner de et kompromiss.")
        print("De blir enige om en løsning som tar hensyn til begge parter.")

        # Returnerer 1 poeng
        return 1
    else:
        print()
        print("Du bestemmer deg for å vente.")
        print("Hamdi og Hallgeir klarer ikke å bli enige.")
        print("Frustrasjonen øker, og prosjektet mister verdifull tid.")

        # Returnerer 0 poeng
        return 0


# Beslutning 3 - Motivasjon og fremdrift
# Bruker poengene fra de to første valgene
def beslutning3(poeng):
    print()
    print("====================================")
    print("     BESTLUTNING 3 - MOTIVASJON")
    print("====================================")

    print()

    # Sjekker hvor mange poeng spilleren har så langt
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

    # Henter spillerens siste valg
    valg = hent_valg()

    if valg == "1":
        print()
        print("Du setter av tid til å forbedre samarbeidet.")
        print("Teamet får mulighet til å snakke sammen.")
        print("Stemningen blir bedre, og motivasjonen øker.")
        print("Samtidig blir det mindre tid til arbeidet med prototypen.")

        # Gir 1 poeng
        return 1
    else:
        print()
        print("Du bestemmer at prototypen må prioriteres.")
        print("Alle får tydelige arbeidsoppgaver og frister.")
        print("Arbeidet fortsetter, men noen konflikter forblir uløste.")

        # Gir 0 poeng
        return 0


# Funksjon som bestemmer avslutningen
def avslutning(poeng):
    print()
    print("====================================")
    print("             RESULTAT")
    print("====================================")

    print()
    # Viser hvor mange poeng spilleren fikk
    print(f"Du fikk {poeng} av 3 poeng!")

    # Sjekker poengsummen og velger riktig avslutning
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
    # Starter med 0 poeng
    poeng = 0

    # Starter med introduksjonen
    introduksjon()

    # Kjører første beslutning og legger til poengene
    valg1 = beslutning1()
    poeng += valg1

    # Sender resultatet fra første beslutning videre
    valg2 = beslutning2(valg1)
    poeng += valg2

    # Sender den totale poengsummen til siste beslutning
    valg3 = beslutning3(poeng)
    poeng += valg3

    # Viser avslutningen basert på poengsummen
    avslutning(poeng)



# Starter spillet
spill()

print()

# Spør om spilleren vil starte spillet på nytt
spill_igjen = input("Vil du spille igjen? (ja/nei): ").lower()

# Starter spillet på nytt hvis spilleren svarer ja
if spill_igjen == "ja":
    spill()
else:
    # Avslutter spillet
    print()
    print("Takk for at du spilte Konfliktløseren!")