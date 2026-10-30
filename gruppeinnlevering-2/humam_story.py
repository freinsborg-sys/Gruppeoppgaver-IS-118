# Interaktiv historie om Erling

poeng = 0

print("Velkommen til hsitorien om Erling")
print("Du skal ta valg som skal påvirke historien videre")

# Første valg - konflikten mellom Silje og Elias 

print("""Det er mandag morgen, og Erling har samlet gruppen til et møte. De skal gå gjennom hvor langt de har kommet med prosjektet, og hva som gjenstår. 

Under møtet begynner Silje og Elias igjen å diskutere hvilken teknologi de skal bruke. Silje mener at forslaget til Elias vil gjøre løsningen mindre brukervennlig. Elias svarer at Siljes forslag blir for dyrt og vanskelig å sikre. 

Diskusjonen blir fort mer personlig. De andre i gruppen sier lite, og stemningen blir dårlig. Erling skjønner at han må gjøre noe før konflikten går enda mer utover samarbeidet.

Han har nå to alternativer.""")

print("""A. Erling bestemmer seg for å ta en prat med Silje og Elias hver for seg. Han vil høre hvordan begge opplever situasjonen, og hvorfor de er så uenige. 

Fordelen med dette er at begge får forklart seg uten å bli avbrutt. Det kan også være lettere å snakke åpent når de ikke sitter i samme rom. 

Ulempen er at dette tar tid. Selv om Erling får en bedre forståelse av problemet, betyr det ikke at Silje og Elias automatisk blir enige. Han må fortsatt følge opp saken etterpå.

I historien vår fører dette til at konflikten roer seg litt. De er fremdeles uenige om teknologien, men klarer å snakke sammen på en bedre måte.""")

print("""B. Erling bestemmer seg for å ta opp problemet i plenum. Han tenker at det kan være lurt å få frem alle meningene, slik at gruppen kan diskutere seg frem til en løsning. 

Fordelen er at alle får mulighet til å si hva de mener. Kanskje noen av de andre har forslag som Silje og Elias ikke har tenkt på.

Problemet er at konflikten allerede har blitt personlig. Begge er frustrerte og har prøvd å få andre med på sin side. Det kan derfor bli vanskelig å ha en rolig diskusjon.

I historien ender møtet med at flere begynner å ta parti. Diskusjonen blir mer opphetet, og stemningen i gruppen blir dårligere.""")

valg1 = input("Velg A eller B: ")

if valg1.upper() == "A":
    poeng += 1
    print("""Erling snakker med silje og Elias hver for seg
    Begge får forklart seg uten å bli avbrutt.
    Konflikten roer seg litt.""")

elif valg1.upper() == "B": 
    print("""Erling tar konflikten opp i plenum. 
    Flere i gruppen begynner å ta parti.
    stemningen blir dårligere.""")

else:
    print("Ugyldig valg.")


# Andre valg - Uenigheten mellom Hamdi og og Hallgeir 

print("""Noen dager senere skal gruppen diskutere hvordan innbyggerne skal kunne delta i digitale folkemøter. 

Hamdi mener at de bør bruke plattformen kommunen allerede har. Han synes dette er den enkleste løsningen, siden kommunen kjenner systemet fra før. 

Hallgeir er ikke enig. Han mener at innbyggerne bør få større frihet til å delta og komme med egne forslag under møtene. 

Diskusjonen fortsetter uten at de kommer noen vei. Erling merker at begge begynner å bli irriterte. Han vil helst unngå at dette utvikler seg til en ny konflikt slik som den mellom Silje og Elias. 

Han må derfor velge hvordan han skal håndtere situasjonen.""")

print("""A. Erling bestemmer seg for å arrangere et eget møte med Hamdi og Hallgeir. Han ønsker å finne ut hva de egentlig er uenige om, og om det finnes en løsning begge kan godta. 

Dette kan være en god måte å løse problemet på før det blir for alvorlig. Begge får forklart hva de mener, og kanskje finner de ut at de egentlig ønsker mye av det samme. 

Ulempen er at møtet tar tid fra arbeidet med prototypen. Det er heller ikke sikkert at de klarer å bli enige. 

I historien vår fungerer møtet bra. Hamdi og Hallgeir blir enige om å se på en løsning som bruker kommunens eksisterende plattform, men som også gjør det mulig for innbyggerne å komme med flere innspill.""")

print("""B. Erling velger å vente og se om Hamdi og Hallgeir klarer å løse problemet på egen hånd. 

Dette kan være positivt fordi de får mer ansvar og mulighet til å bestemme selv. Hvis de klarer å bli enige, slipper Erling å bruke tid på konflikten. 

Men det er også en risiko. Hvis ingen av dem vil gi seg, kan uenigheten fortsette og bli verre. 

I historien klarer de ikke å finne en løsning. Begge fortsetter å jobbe med hvert sitt forslag, og gruppen mister tid som egentlig skulle vært brukt på prototypen. 

Hva skjer videre?""")

valg2 = input("Velg A eller B: ")

if valg2.upper () == "A":
    poeng += 1
    print("""Erling bestemmer seg for å samle gruppen.
    Hamdi og Hallgeir finner etm kompromiss som begge kan leve med.""")

elif valg2.upper () == "B":
    print("""Erling lar dem ordne opp selv
    de klarer ikke å bli enige, og gruppen mister tid.""")

else:
    print("Ugyldig valg.")


#Tredje valg - Motivasjon og fremdrift 

print("""Det er ikke lenge igjen før prototypen skal presenteres. Gruppen har jobbet mye, men konfliktene har tatt både tid og energi. 

Flere begynner å bli slitne, og noen er usikre på om de kommer til å bli ferdige i tide. 

Erling må bestemme hva gruppen skal bruke den siste tiden på. Skal han prøve å forbedre samarbeidet, eller bør alle bare konsentrere seg om å bli ferdige?""")

print("""A. Erling bestemmer seg for å samle gruppen til en felles aktivitet. Han ønsker at de skal få snakket sammen og bli enige om hvordan de skal samarbeide fremover. 

Tanken er at gruppen skal få bedre tillit til hverandre. Hvis stemningen blir bedre, kan det også bli lettere å jobbe sammen om de siste oppgavene. 

Fordelen er at folk kanskje blir mer motiverte og får bedre forståelse for hverandre. Dette kan gjøre at arbeidet går lettere etterpå. 

Ulempen er at de bruker tid som egentlig kunne gått til å utvikle prototypen. Siden fristen nærmer seg, kan dette føre til mer stress. 

I historien vår fører dette valget til at samarbeidet blir bedre. Gruppen får snakket ut om problemene, og flere føler seg mer motiverte til å fullføre prosjektet.""")

print("""B. Erling bestemmer seg for at gruppen må prioritere prototypen. Han fordeler oppgavene og setter klare frister for hva alle skal gjøre. 

Fordelen er at alle vet hva de skal jobbe med. Det kan gjøre det lettere å få gjort mest mulig før fristen. 

Ulempen er at konfliktene ikke nødvendigvis forsvinner. Selv om alle jobber med sine oppgaver, kan den dårlige stemningen fortsatt påvirke samarbeidet. 

I historien fortsetter gruppen arbeidet, men flere er misfornøyde. De føler at Erling bare bryr seg om å bli ferdig, og ikke om problemene som har oppstått.""")

valg3 = input("Velg A eller B: ")

if valg3.upper () == "A": 
    poeng += 1
    print("""Erling samler gruppen.
    De får snakket ut om problemene og samarbeidet blir bedre.""")

elif valg3.upper() == "B":
    print("""Erling fokuserer på fremdrift.
    Arbeidet fortsetter, men flere er misfornøyde.""")

else:
    print("Ugyldig valg.")

# Utfall 

print("\nDin poengsum er:", poeng)

if poeng == 3:
    print("""
UTFALL 1 - POSITIV UTVIKLING

Erling har håndtert konfliktene godt.

Silje og Elias samarbeider bedre.
Hamdi og Hallgeir har funnet en løsning.

Gruppen blir ferdig med prototypen i tide
og er på vei inn i norming-fasen.
""")

elif poeng >= 1:
    print("""
UTFALL 2 - DELVIS POSITIV UTVIKLING

Noen konflikter er løst,
men enkelte utfordringer gjenstår.

Gruppen får gjort mye arbeid,
men prototypen har fortsatt noen mangler.
""")

else:
    print("""
UTFALL 3 - NEGATIV UTVIKLING

Konfliktene har blitt verre.

Gruppen bruker mye tid på uenigheter,
og prototypen blir ikke ferdig innen fristen.

Prosjektet blir forsinket.
""") 






