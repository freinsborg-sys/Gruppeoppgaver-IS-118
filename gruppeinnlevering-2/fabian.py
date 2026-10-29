# IS-118 Gruppeoppgave 2, del 2
# Interaktiv historie: Erling og storming-fasen i prosjektteamet


def hent_valg(sporsmal):
    """Spør helt til brukeren svarer A eller B. Returnerer 'A' eller 'B'."""
    while True:
        svar = input(sporsmal).strip().upper()
        if svar in ("A", "B"):
            return svar
        # Ugyldig input: forklar og spør på nytt, så historien ikke krasjer
        print("Ugyldig valg. Skriv A eller B.\n")


def spill():
    # Variabler som lagrer valgene underveis
    valg1 = ""
    valg2 = ""
    valg3 = ""
    poeng = 0  # Hvert "gode" valg gir ett poeng (0-3 til sammen)

    # ---------- Introduksjon ----------
    print("=" * 60)
    print("PROSJEKT MEDBORGERPORTAL: seks uker inn")
    print("=" * 60)
    print("Du er Erling, prosjektleder. Starten var full av energi,")
    print("men nå har teamet havnet i storming-fasen.")
    print("- Silje (UX) og Elias (IT) krangler om teknologi og design.")
    print("- Hamdi og Hallgeir er uenige om digitale folkemøter.")
    print("Første prototype skal være klar om tre uker.\n")

    # ---------- Beslutningspunkt 1: Silje og Elias ----------
    print("--- BESLUTNING 1: Konflikten mellom Silje og Elias ---")
    print("A) Ta individuelle samtaler med begge for å dempe temperaturen")
    print("B) Ta konflikten opp i plenum for å skape åpenhet")
    valg1 = hent_valg("Ditt valg (A/B): ")

    if valg1 == "A":
        poeng += 1
        print("\nSilje og Elias føler seg hørt hver for seg og roer seg ned.")
        print("Hamdi og Hallgeir merker likevel at teamet er stille.\n")
    elif valg1 == "B":
        print("\nMøtet blir opphetet og begge trekker støtte fra sine allierte.")
        print("Konflikten er åpen, men alle kjenner nå saken.")
        print("Hamdi og Hallgeir sitter tause og irriterte.\n")

    # ---------- Beslutningspunkt 2: Hamdi og Hallgeir ----------
    print("--- BESLUTNING 2: Hamdi og Hallgeir ---")
    print("A) Ta initiativ til et felles møte for å avklare uenigheten")
    print("B) Avvente og håpe at de finner en løsning selv")
    valg2 = hent_valg("Ditt valg (A/B): ")

    if valg2 == "A":
        poeng += 1
        print("\nHamdi og Hallgeir blir enige om en kombinert løsning:")
        print("kommunens plattform med en åpen innspillsdel.\n")
    elif valg2 == "B":
        print("\nUenigheten ulmer videre. Hallgeir føler seg overhørt,")
        print("og Hamdi trekker seg tilbake fra diskusjonene.\n")

    # ---------- Beslutningspunkt 3: Motivasjon ----------
    print("--- BESLUTNING 3: Motivasjonen i teamet ---")
    print("Prototypen skal leveres om bare noen dager.")
    print("A) Sett av tid til relasjonsbygging og sosiale aktiviteter")
    print("B) Prioriter fremdrift og leveranser")
    valg3 = hent_valg("Ditt valg (A/B): ")

    if valg3 == "A":
        poeng += 1
        print("\nEn felles lunsj og en uformell workshop gjenoppretter tilliten.\n")
    elif valg3 == "B":
        print("\nFremdriften holdes, men stemningen er fortsatt anstrengt.\n")

    # ---------- Avslutning: utfall basert på poeng ----------
    print("=" * 60)
    print("UTFALL")
    print("=" * 60)
    if poeng == 3:
        print("Teamet gjenoppretter tillit og går videre til norming-fasen.")
        print("Prototypen leveres i tide, og samarbeidet er sterkere enn før.")
    elif poeng == 2:
        print("Konflikten løses delvis, men relasjonene er fortsatt sårbare.")
        print("Prototypen leveres, men teamet må jobbe videre med tilliten.")
    else:
        print("Prosjektet mister samhold og forsinkes.")
        print("Teamet blir værende i storming-fasen, og prototypen er ikke klar.")

    # Oppsummering av valgene som ble lagret underveis
    print("\nDine valg: " + valg1 + " - " + valg2 + " - " + valg3)
    print("Poeng: " + str(poeng) + " av 3")


# ---------- Hovedprogram ----------
while True:
    spill()
    igjen = input("\nVil du spille igjen? (j/n): ").strip().lower()
    if igjen != "j":
        print("Takk for at du spilte!")
        break
    print()