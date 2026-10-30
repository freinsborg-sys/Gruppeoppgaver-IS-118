score = 0

print(r"""
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
                VELKOMMEN TIL ERLINGS KONFLIKTHÅNDTERINGSPILL!
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
prøv å ta de riktige valgene for å håndtere konfliktene i erlings prosjekt.
""")


choice = input("er du klar til å starte? (ja/nei):")
if choice.lower() == "ja":
    print("flott! la oss starte!")
else:
    print("ok, vi starter uansett!")

print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
print("problemsituasjon 1: Hvordan håndtere konflikten mellom Silje og Elias?")
print("hva gjør du?")
print("1. snakk med dem hver for seg?")
print("2. ta konflikten foran hele gruppen?")

choice = input("hva velger du? (1 eller 2): ")
if choice == "1":
        print("stemningen i gruppa blir bedre til neste møte")
        print("du får 1 poeng" \
        "")
        score += 1
elif choice == "2":
        print("stemningen forblir dårlig til neste møte")
        print("du får 0 poeng")
else:
        print("svaret ditt er ugyldig. du får 0 poeng")
print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")


print("problemsituasjon 2: Hvordan forhindre at konflikten mellom Hamdi og Hallgeir blusser opp?")
print("hva gjør du?")
print("1. samle dem til et møte?")
print("2. la dem ordne opp i det selv?")

choice = input("hva velger du? (1 eller 2): ")
if choice == "1":
        print("du får 1 poeng")
        score += 1
elif choice == "2":
        print("feil valg! du får 0 poeng")
else:
        print("svaret ditt er ugyldig. du får 0 poeng")
        score += 0

print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
print("problemsituasjon 3: Hvordan skal Erling beholde motivasjon i teamet som helhet?")
print("hva gjør du?")
print("1. samle gruppen for en felles aktivitet og bruke tid på samarbeidet?")
print("2. fokus på å fullføre prototypen og bli ferdig?")

choice = input("hva velger du? (1 eller 2): ")
if choice == "1":
        print("samerbeided til gruppen forbedres og de klarer å fullføre prosjektet.")
        print("tid som kunne blit brukt på å fullføre prosjektet blir brukt på å bygge samhold i gruppen, men i dette tilfellet er det viktigere å forbedre samarbeidet.")
        print("du får 1 poeng")
        score += 1
elif choice == "2":
        print("teamet har mer tid å bruke på prototypen.")
        print("stemningen blir verre og gruppen tenker erling bare bryr seg om å fullføre prototypen.")
        print("du får 0 poeng")
else:
        print("svaret ditt er ugyldig. du får 0 poeng")
        score += 0
print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
print(f"du fikk {score} poeng")
if score == 3:
       print("gratulerer! du fikk alt riktig, Erling og teamet kom seg over konfliktene og går videre til norming-fasen.")
elif score == 1 or score == 2:
       print(" du fikk noen riktige valg. Erling og teamet har klart å løse noen av konfliktene, stemningen har roet seg ned, men det er noen som sliter å arbeide sammen.")
elif score == 0:
       print("du hadde ingen riktige valg. Konfliktene har eskalert, teamet klarer ikke å få fullført prtorypen i tide.")
else:
       score += 99
       print("Jeg er usikker hvordan du fikk en annen poengsum, gratulerer du klarte å ødelegge koden min her får du noen ekstra poeng.")
