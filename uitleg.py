def uitleg_nl(state):
    uitleg = ''

    if state == 'rondpass':
        uitleg = '''
        U, en uw tegenstanders, mogen pas openen met 12 punten, er zitten in totaal 40 punten in het spel.
        Dat betekend dat het mogelijk is dat niemand 12 punten heeft, wat betekend dat het mogelijk is dat niemand opent.
        Als dat het geval is spreken we van een rondpass.
        In het geval van een rondpass, is er geen contract, wat betekend dat er niet gespeeld kan worden.
        '''

    if state == 'regelVanTwintig':
        uitleg = '''
        Soms heeft u net niet genoeg om te openen maar is uw hand zo mooi dat u denkt, 
        maar potverdorie hier moet toch wel iets mee te doen zijn?
        Als u zo'n hand heeft kunt u kijken of uw hand voldoet aan de regel van 20.
        De regel luid: als uw punten + de lengte van uw twee langste kaarten samen 20 is, mag u openen.
        Deze regel is erop gebaseerd dat de lengte in uw kaarten het gebrek aan punten goed maken.
        Onthoud dat deze regel heel strikt is, met minder dan 20 punten kunt u niet openen, zelfs niet met 19.
        En u mag geen punten bijtellen voor een singleton of doubleton of renonce, die punten worden automatisch meegeteld doordat het gebrek in die kleur ergens anders weer erbij moet komen.
        '''

    if state == '1SA_opening':
        uitleg = '''
        Als uw puntenaantal ligt tussen 15 en 17 denkt u altijd als eerst aan een SA-opening.
        Dit staat voor sans a tout, zonder troef.
        Als u heeft vastgesteld dat uw puntenaantal goed is kunt u kijken of u een sans-verdeling heeft.
        Een sansverdeling is een verdeling waarin geen kleur meer dan 5 kaarten bevat, en geen minder dan 2.
        Als dit het geval is betekent dat dat u 1SA kunt openen
        '''

    if state == '2SA_opening':
        uitleg = '''
        Als uw puntenaantal ligt tussen 20 en 22 denkt u altijd als eerst aan een SA-opening.
        Dit staat voor sans a tout, zonder troef.
        Als u heeft vastgeseteld dat uw puntenaantal goed is kunt u kijken of u een sansverdeling heeft.
        Een sansverdeling is een verdeling waarin geen kleur meer dan 5 kaarten bevat en geen minder dan 2.
        Als dit het geval is betekent dat dat u 2SA kunt openen.
        '''

    if state == '2Cs_opening':
        uitleg = '''
        Een 2♣ opening is manchforcing, dit betekent dat u naar de manch gaat.
        Om de manch te bereiken heeft u heel wat punten nodig, 25, of 8 vaste slagen.
        Als u 2♣ kunt openen betekent dat, dat u en uw parten niet mogen stoppen met bieden totdat 
        jullie de manch hebben bereikt.
        '''

    if state == 'Normal_5card':
        uitleg = '''
        Om te openen heeft u minimaal 12 punten nodig.
        Daarna moet u vastellen in welke kleur u gaat openen, 
        uw eerste keus is altijd de kleur waarin de meeste kaarten zitten.
        Met 2 vijfkaarten opent u de hoogste, met 2 vierkaarten de laagste.
        '''

    if state == 'Normal_4card':
        uitleg = '''
        Om te openen heeft u minimaal 12 punten nodig.
        Daarna moet u vastellen in welke kleur u gaat openen, 
        uw eerste keus is altijd de kleur waarin de meeste kaarten zitten.
        Met 2 vijfkaarten opent u de hoogste, met 2 vierkaarten de laagste.
        Echter, met de hoge kleuren, ♥ en ♠, mag u pas openen met een vijfkaart.
        '''

    if state == '1Cs_opening':
        uitleg = '''
        Om te openen heeft u minimaal 12 punten nodig.
        Daarna moet u vastellen in welke kleur u gaat openen, 
        uw eerste keus is altijd de kleur waarin de meeste kaarten zitten.
        Met 2 vijfkaarten opent u de hoogste, met 2 vierkaarten de laagste.

        Echter, met de hoge kleuren, ♥ en ♠, mag u pas openen met een vijfkaart.
        In het geval u dan niet kunt openen, 
        dus u heeft geen vierkaart in de lage kleuren en geen vijfkaart in de hoge,rest er het 1♣ bod.
        Dit kan al vanaf een tweekaart in klaveren, onthoud dat dus voor als uw partner dit bied.
        '''

    if state == 'preemtif2':
        uitleg = '''
        Om te openen heeft u minimaal 12 punten nodig, soms heeft u dit niet maar wel een hele lange kaart.
        Dan mag u uw tegenstanders een beetje pesten door hun bieding te saboteren.
        Dit heet preemtif bieden, bieden met een lange kaart in plaats van met punten, om te slagen heeft u wel een punten minimum van 6.
        Door hoog te bieden met weinig punten neemt u biedruimte weg voor uw tegenstanders, vandaar pesten dus.
        Met een 6 kaart bied u op 2-niveau, hoe langer de kaart hoe hoger u mag bieden en hoe vervelender u mag zijn voor de tegenstanders.
        Onthoud ook dat preemtief bieden gedefineerd wordt door de sprong, dus als uw tegenstander, of partner al geboden heeft is preemtief bieden mogelijk.
        '''

    if state == 'preemtif3':
        uitleg = '''
        Om te openen heeft u minimaal 12 punten nodig, soms heeft u dit niet maar wel een hele lange kaart.
        Dan mag u uw tegenstanders een beetje pesten door hun bieding te saboteren.
        Dit heet preemtif bieden, bieden met een lange kaart in plaats van met punten, om te slagen heeft u wel een punten minimum van 6.
        Door hoog te bieden met weinig punten neemt u biedruimte weg voor uw tegenstanders, vandaar pesten dus.
        Onthoud ook dat preemtief bieden gedefineerd wordt door de sprong, dus als uw tegenstander, of partner al geboden heeft is preemtief bieden mogelijk.
        Met een 7 kaart bied u op 3-niveau, hoe langer de kaart hoe hoger u mag bieden en hoe vervelender u mag zijn voor de tegenstanders.
        '''

    if state == 'preemtif4':
        uitleg = '''
        Om te openen heeft u minimaal 12 punten nodig, soms heeft u dit niet maar wel een hele lange kaart.
        Dan mag u uw tegenstanders een beetje pesten door hun bieding te saboteren.
        Dit heet preemtif bieden, bieden met een lange kaart in plaats van met punten, om te slagen heeft u wel een punten minimum van 6.
        Door hoog te bieden met weinig punten neemt u biedruimte weg voor uw tegenstanders, vandaar pesten dus.
        Onthoud ook dat preemtief bieden gedefineerd wordt door de sprong, dus als uw tegenstander, of partner al geboden heeft is preemtief bieden mogelijk.
        Met een 8 kaart bied u op 4-niveau, hoe langer de kaart hoe hoger u mag bieden en hoe vervelender u mag zijn voor de tegenstanders.
        '''

    if state == 'open_pass':
        uitleg = '''
        Om te openen heeft u minmaal 12 punten nodig, soms heeft u deze gewoon niet en hoe vervelend ook, moet u passen.
        '''

    if state == 'jacoby':
        uitleg = '''
        Uw partner bied 1SA, dit betekend 15-17 punten en een evenwichtige hand.
        U weet ook dat uw partners laagste kaart een tweekaart is.
        Samen 8 kaarten heet een fit (met een fit kun je in die kleur spelen), dus min2 + 5 is bijna een fit.
        Als jullie een (bijna) fit hebben kunnen jullie beter in die kleur spelen dan het risico van SA te nemen,
        vandaar is Jacoby bedacht, en vandaar kunt u dit ook al bieden vanaf 0 punten,
        met de voorwaarde van een vijfkaart in een van de hoge kleuren, ♥ en ♠.
        Omdat u liever heeft dat de tegenstanders de minste punten zien, en dus de minste mineurs, heeft u het liefst dat de 1SA openaar speelt,
        daar heeft meneer Jacoby iets op bedacht, als u, met deze hand, de kleur onder de kleur die eigenlijk wilt bieden bied,
        kan daarna uw partner verplicht de kleur bieden die u bedoelde, en is het spel in de hand van de openaar.
        '''

    if state == 'jacoby-2sa':
        uitleg = '''
        Uw partner bied 2SA, dit betekend 20-22 punten en een evenwichtige hand.
        U weet ook dat uw partners laagste kaart een tweekaart is.
        Samen 8 kaarten heet een fit (met een fit kun je in die kleur spelen), dus min2 + 5 is bijna een fit.
        Als jullie een (bijna) fit hebben kunnen jullie beter in die kleur spelen dan het risico van SA te nemen,
        vandaar is Jacoby bedacht, en vandaar kunt u dit ook al bieden vanaf 0 punten,
        met de voorwaarde van een vijfkaart in een van de hoge kleuren, ♥ en ♠.
        Omdat u liever heeft dat de tegenstanders de minste punten zien, en dus de minste mineurs, heeft u het liefst dat de 2SA openaar speelt,
        daar heeft meneer Jacoby iets op bedacht, als u, met deze hand, de kleur onder de kleur die eigenlijk wilt bieden bied,
        kan daarna uw partner verplicht de kleur bieden die u bedoelde, en is het spel in de hand van de openaar.
        '''

    if state == 'stayman':
        uitleg = '''
        Uw partner bied 1SA, dit betekend 15-17 punten en een evenwichte hand.
        Het liefst speelt u in een hoge kleur, ♥ en ♠. 
        Dus als u een vierkaart in een van de hoge kleur heeft is dit het onderzoeken waard, 
        en aangezien u met 8-9 punten prima 2SA kunt spelen kunt u met dit puntenaantal ook eerst de hoge kleuren onderzoeken.
        U biedt 2♣ om aan uw partner te vragen of hij een vierkaart in een van de hoge kleuren heeft.
        '''

    if state == '1SA-2SA':
        uitleg = '''
        Uw partner bied 1SA, dit betekend 15-17 punten en een evenwichte hand.
        Het liefst speelt u in een hoge kleur, ♥ en ♠, maar als u geen vierkaart in een van deze kleuren heeft is dit het niet waard.
        U weet dat uw partner 15-17 punten heeft, met 8 punten, (8 + 17 = 25) kunnen jullie de manch nog halen,
        om aan uw partner te vragen of hij denkt dat dit nog mogelijk is bied u 2SA, met een maximum bied uw partner de manch
        '''

    if state == '1SA-3SA':
        uitleg = '''
        Uw partner bied 1SA, dit betekend 15-17 punten en een evenwichte hand.
        Het liefst speelt u in een hoge kleur, ♥ en ♠, maar als u geen vierkaart in een van deze kleuren heeft is dit het niet waard.
        Maar u heeft 10+ punten (10 + 15 = 25) dus u wilt naar de manch, 
        aangezien u al weet dat het geen kleurenmanch gaat worden bied u maar gewoon de een-na-beste manche, 3SA
        '''

    if state == '1SA-pass':
        uitleg = '''
        Uw partner bied 1SA, dit betekend 15-17 punten en een evenwichte hand.
        Als u geem vijfkaart heeft in de hoge kleuren en niet meer dan 7 punten, is 1SA gewoon een prima contract.
        '''

    if state == 'answer_to_stayman_colors':
        uitleg = '''
        Uw partner bied Stayman, hiermee vraagt hij of u een hoge kleur heeft, 
        als u een vierkaart of meer heeft in een van de hoge kleuren moet u dat aan uw partner laten weten.
        '''

    if state == 'answer_to_stayman_nocolors':
        uitleg = '''
        Uw partner bied Stayman, hiermee vraagt hij of u een hoge kleur heeft, 
        als u een vierkaart of meer heeft in een van de hoge kleuren moet u dat aan uw partner laten weten.
        In dit geval is dat niet zo, ook dat wilt u uw partner laten weten, hier is het bod 2♦ voor.
        U zegt nu dat u geen vierkaart of meer in een van de hoge kleuren heeft.
        '''

    if state == 'OpStayman':
        uitleg = '''
        Uw tegenstanders bieden Stayman en zijn op zoek naar het juiste contract voor wat ze kunnen spelen,
        de kans dat u en uw partner een contract gaan maken is dan erg klein, 
        dat betekent niet dat u geen informatie aan uw partner kunt geven.
        Uw tegenstander heeft Stayman geboden, daarmee geeft hij geen klaveren aan, dus dit is een ideaal moment om er veilig een doubletje 
        tussen te doen, aangezien de 1SA-openaar nooit gaat passen, en het doublet dus geen waarde heeft.
        Dus als u een goede kaart klaveren hebt is dit de ideale situatie om dat aan uw partner te laten weten, door te doubleren.
        '''

    if state == 'OpStaymanPass':
        uitleg = '''
        Uw tegenstanders bieden stayman en zijn op zoek naar het juiste contract voor wat ze kunnen spelen,
        de kans dat u en uw partner een contract gaan maken is dan erg klein, 
        dat betekent niet dat u geen informatie aan uw partner kunt geven.
        Uw tegenstander heeft Stayman geboden, daarmee geeft hij geen klaveren aan, dus dit is een ideaal moment om er veilig een doubletje 
        tussen te doen, aangezien de 1SA-openaar nooit gaat passen, en het doublet dus geen waarde heeft.
        Dus als u een goede kaart klaveren hebt is dit de ideale situatie om dat aan uw partner te laten weten, door te doubleren.
        Echter als u nu doubleerd is de kans groot dat uw partner terugkomt met klaveren als dat niet gewenst is moet u ook niet doubleren.
        Dus als u geen lange klaverkaart heeft, of niet genoeg honeurs is het soms beter gewoon te passen.
        '''
    
    if state == 'OpJacoby':
        uitleg = '''
        Uw tegenstanders bieden Jacoby en zijn op zoek naar het juiste contract voor wat ze kunnen spelen,
        de kans dat u en uw partner een contract gaan maken is dan erg klein, 
        dat betekent niet dat u geen informatie aan uw partner kunt geven.
        Uw tegenstander heeft Jacoby geboden, daarmee geeft hij niet de geboden kleur aan, 
        dus dit is een ideaal moment om er veilig een doubletje tussen te doen, 
        aangezien de 1SA-openaar nooit gaat passen, en het doublet dus geen waarde heeft.
        Dus als u een goede kaart in de geboden kleur heeft is dit de ideale situatie om dat aan uw partner te laten weten, 
        door te doubleren.
        '''

    if state == 'AnswerJacoby':
        uitleg = '''
        Uw partner weet dat uw laagste kaart een tweekaart is, en dat u 15-17 punten heeft.
        Samen 8 kaarten heet een fit (met een fit kun je in die kleur spelen), dus min2 + 5 is bijna een fit.
        Als jullie een (bijna) fit hebben kunnen jullie beter in die kleur spelen dan het risico van SA te nemen,
        vandaar is Jacoby bedacht, en vandaar kan uw partner dit ook al bieden vanaf 0 punten,
        met de voorwaarde van een vijfkaart in een van de hoge kleuren, ♥ en ♠.
        Omdat u liever heeft dat de tegenstanders de minste punten zien, en dus de minste mineurs, heeft u het liefst dat de 1SA openaar speelt,
        daar heeft meneer Jacoby iets op bedacht, als uw partner, de kleur onder de kleur die eigenlijk wilt bieden bied,
        kan u daarna de kleur boven de kleur van uw patner bieden, en is het spel in uw hand, die van de openaar.
        '''

    if state == 'NXMs':
        uitleg = '''
        Soms bied een tegenstander tussen en ontneemt u daarmee de kans te bieden wat u wilde bieden,
        daar is het negatief doublet voor bedacht, als de tegenstander een bod doet waardoor u niet meer uw bod kunt doen,
        omdat het bod wat u wilde doen onder het bod van de tegenstander ligt, heeft u de mogelijkheid te doubleren,
        wat betekent dat u het bod wilde doen wat nu niet meer kan. 
        Wegens deze conventie is er nog een mogelijkheid bedacht, in welke u nu zit.
        Als u zowel harten en schoppen bevat krijgt u in dit geval de kans te doubleren waardoor uw partner weet dat u en een 4krt ♥ en ♠ heeft
        '''

    if state == 'NXHs':
        uitleg = '''
        Soms bied een tegenstander tussen en ontneemt u daarmee de kans te bieden wat u wilde bieden,
        daar is het negatief doublet voor bedacht, als de tegenstander een bod doet waardoor u niet meer uw bod kunt doen,
        omdat het bod wat u wilde doen onder het bod van de tegenstander ligt, heeft u de mogelijkheid te doubleren,
        wat betekent dat u het bod wilde doen wat nu niet meer kan, in dit geval 1♥
        '''

    if state == '2Cs-2x':
        uitleg = '''
        Uw partner biedt manchforcing, wat betekend dat geen van jullie mag passen totdat jullie de manch hebben bereikt.
        Uw partner kan of 23+ punten hebben met een sansverdeling, of een lange kaart.
        In elk geval heeft uw partner 8 vaste slagen.
        U wilt uw partner laten weten dat u wat heeft, en dat doet u door uw langste kleur te bieden.
        '''

    if state == '2Cs-2Ds':
        uitleg = '''
        Uw partner biedt manchforcing, wat betekend dat geen van jullie mag passen totdat jullie de manch hebben bereikt.
        Uw partner kan of 23+ punten hebben met een sansverdeling, of een lange kaart.
        In elk geval heeft uw partner 8 vaste slagen.
        Omdat uw partner manchforcing biedt kunt u niet passen, zelfs niet met 0 punten,
        maar met 0 punten wilt u uw partner de ruimte geven, zijn / haar kaart te beschrijven.
        Daarom is er het relay-bod bedacht, het zegt gewoon, partner ik heb niets interresants, wat heeft u?
        '''

    if state == '2Cs-2SA':
        uitleg = '''
        Uw partner biedt manchforcing, wat betekend dat geen van jullie mag passen totdat jullie de manch hebben bereikt.
        Uw partner kan of 23+ punten hebben met een sansverdeling, of een lange kaart.
        In elk geval heeft uw partner 8 vaste slagen.
        Omdat uw partner manchforcing biedt kunt u niet passen, zelfs niet met 0 punten,
        maar als u heel veel punten heeft, wilt u dat uw partner zeker laten weten.
        Daar is het 2SA bod voor bedacht hierna, het betekend dat u 10 punten of meer heeft.
        '''

    if state == '2Cs-2Ds-2SA':
        uitleg = '''
        Uw partner heeft aangegeven niet veel te hebben, en heeft het aan u overgelaten te vertellen wat u heeft.
        Met 2SA geeft u aan dat u op punten heeft gebonden en niet op een hele lange kaart,
        uw partner weet nu dus dat u 23+ punten heeft en een plausibele sansverdeling
        '''

    if state == '2Cs-2Ds-2x':
        uitleg = '''
        Uw partner heeft aangegeven niet veel te hebben, en heeft het aan u overgelaten te vertellen wat u heeft.
        Dus als u een lange kaart heeft moet u dat zeker laten weten
        '''

    if state == '2Cs-2Hs':
        uitleg = '''
        Uw partner heeft harten, nu is het aan u om te laten weten wat u heeft, 
        dan kunnen jullie later vaststellen in welk contract jullie horen te zitten
        '''

    if state == 'normal_pass':
        uitleg =  '''
        Soms heeft u gewoon niet genoeg punten, en niet een bijzonder genoege kaart om te bieden, dan moet u gewoon passen
        '''

    if state == 'answering_partnerClr':
        uitleg = '''
        Uw partner heeft een opening, 12 punten, en nu gaan jullie onderzoeken in welk contract jullie de beste kunnen score halen,
        dat gebeurd door de uitwisseling van informatie, dus dat is wat u doet, u verteld uw partner in welke kleur u, 
        met de informatie ter uw beschikking op dat moment, het beste uitkomt.
        '''

    if state == 'answering_partnerSa':
        uitleg = '''
        Uw partner heeft een opening, 12 punten, en nu gaan jullie onderzoeken in welk contract jullie de beste score kunnen halen,
        Maar er zijn ook een set regels waar u aan moet voldoen, anders raakt uw partner in de war.
        Een van die regels is dat als u op 1-niveau een nieuwe kleur biedt u 6+ punten beloofd, en op 2-niveau 10+ punten. 
        Een andere regel is dat u niet mag passen op uw partners opening met meer dan 6 punten.
        En nog een andere is dat u als u antwoord op uw partner minimaal een vierkaar 
        Maar soms kunt u dus niets bieden, omdat u dan of niet voldoet aan de punten regel of de vierkaart regel.
        Dan zit u vast, dan is er nog maar een optie en dat is 1SA bieden, waarmee u aangeeft dat u minimaal bent en niets kunt bieden.
        '''
        
    if state == 'answering_partner_min':
        uitleg = '''
        Uw partner heeft aangegeven een kleur te hebben maar niet dezelfde kleur als u.
        U wilt niet meer punten, en kaartwaarde aangeven dan u heeft dus soms is de enige optie, 1SA te bieden.
        Daarmee geeft 12-14 punten aan en niet overwaarde ergens in, kortom een minimale hand.
        '''

    if state == '6krt_herhalen':
        uitleg = '''
        Door op een niveau te openen beloofd u, in het geval van ♣ en ♦, een vierkaart, in het geval van ♥ en ♠ een vijfkaart.
        Als u een 6 kaart heeft dan weet uw partner dat nog niet en is dat dus belangrijke informatie om te bepalen welk contract jullie gaan spelen.
        Daarom kunt u die kleur herbieden.
        '''

    if state == 'answerLevel2':
        uitleg = '''
        Soms heeft u meer dan een goede kleur.
        U laat vanzelfsprekend eerst de beste kaart horen maar het kan van belang zijn voor uw partner om meer informatie te hebben.
        Zoals of u een tweede kaart hebt, of te wel een kaart die minder goed is dan de kaart die als eerst heeft laten weten maar wel van belang is.        
        '''

    if state == 'fitFoundedNoPoints':
        uitleg = '''
        U heeft uw fit gevonden wat betekend dat de volgende vraag is of jullie voldoende punten hebben om naar de manch te gaan.
        Om de manch te spelen heeft u ruwweg 25 punten nodig, en als u die niet heeft is het ook niet nodig om hoger te gaan en is er dus wijsheid in passen.
        '''

    if state == 'fitFoundedInvite':
        uitleg = '''
        U heeft uw fit gevonden wat betekend dat de volgende vraag is of jullie voldoende punten hebben om naar de manch te gaan.
        Om de manch te spelen heeft u ruwweg 25 punten nodig.
        Uw partner beloofd met zijn bod op 2-niveau 6-9, als u tussen de 14 en 18 punten heeft is er nog kans op de manch.
        Maar de manch is niet gegarandeerd, dus moet u eerst aan uw partner vragen of hij / zij genoeg heeft om naar de manch te gaan.
        Dat doet u met een bid op 3-niveau, een invite.
        '''

    if state == 'fitFoundedInviteU2':
        uitleg = '''
        De ideale manch is 4 in de hoge kleuren wat betekend dat als u een fit heeft gevonden in de hoge kleuren u daar op handeld.
        Dus als u weet dat uw partner een vijfkaart hoog heeft, doordat hij dat heeft geopend, en u heeft een driekaart of meer in die kleur weet u dat als er een potentiele manch in zit dat in die kleur gaat zijn.
        Dus als u nog een vijfkaart in een andere kleur heeft is dat minder belangrijk dan uw partner laten weten dat jullie een fit hebben in de hoge kleuren.
        Ok, u heeft uw fit gevonden wat betekend dat de volgende vraag is of jullie voldoende punten hebben om naar de manch te gaan.
        Om de manch te spelen heeft u ruwweg 25 punten nodig.
        U heeft 6-9 punten, als uw partner meer dan 18 punten heeft is er nog kans op de manch.
        Maar de manch is niet gegarandeerd, dus moet u eerst aan uw partner vragen of hij / zij genoeg heeft om naar de manch te gaan.
        Dat doet u met een bid op 2-niveau, een invite.
        '''

    if state == 'fitFoundedInviteU3':
        uitleg = '''
        De ideale manch is 4 in de hoge kleuren wat betekend dat als u een fit heeft gevonden in de hoge kleuren u daar op handeld.
        Dus als u weet dat uw partner een vijfkaart hoog heeft, doordat hij dat heeft geopend, en u heeft een driekaart of meer in die kleur weet u dat als er een potentiele manch in zit dat in die kleur gaat zijn.
        Dus als u nog een vijfkaart in een andere kleur heeft is dat minder belangrijk dan uw partner laten weten dat jullie een fit hebben in de hoge kleuren.
        Ok, u heeft uw fit gevonden wat betekend dat de volgende vraag is of jullie voldoende punten hebben om naar de manch te gaan.
        Om de manch te spelen heeft u ruwweg 25 punten nodig.
        U heeft 10/11 punten, als uw partner 14/15 punten heeft is er nog kans op de manch.
        Maar de manch is niet gegarandeerd, dus moet u eerst aan uw partner vragen of hij / zij genoeg heeft om naar de manch te gaan.
        Dat doet u met een bid op 3-niveau, een invite.
        '''

    if state == 'fitFoundedManchU':
        uitleg = '''
        De ideale manch is 4 in de hoge kleuren wat betekend dat als u een fit heeft gevonden in de hoge kleuren u daar op handeld.
        Dus als u weet dat uw partner een vijfkaart hoog heeft, doordat hij dat heeft geopend, en u heeft een driekaart of meer in die kleur weet u dat als er een potentiele manch in zit dat in die kleur gaat zijn.
        Dus als u nog een vijfkaart in een andere kleur heeft is dat minder belangrijk dan uw partner laten weten dat jullie een fit hebben in de hoge kleuren.
        Ok, u heeft uw fit gevonden wat betekend dat de volgende vraag is of jullie voldoende punten hebben om naar de manch te gaan.
        Om de manch te spelen heeft u ruwweg 25 punten nodig.
        U heeft net als uw partner, een opening, dat betekend dat jullie sowieso genoeg punten hebben om naar de manch te gaan.
        Als u een hoge kleur heeft gevonden waarin jullie de manch kunnen spelen en u weet dat er genoeg punten bij jullie zitten om naar de manch te gaan is het logisch het gewoon te bieden.
        '''

    if state == 'fitFoundedManch':
        uitleg = '''
        U heeft uw fit gevonden wat betekend dat de volgende vraag is of jullie voldoende punten hebben om naar de manch te gaan.
        Om de manch te spelen heeft u ruwweg 25 punten nodig.
        Uw partner beloofd met zijn bod op 2-niveau 6-9, dus als u meer dan 18 punten hebt is de manch haast gegarandeerd en is het dus ook logisch die te bieden.
        '''

    if state == 'answerInvite':
        uitleg = '''
        Uw partner weet dat u meer dan 12 punten heeft, en met zijn / haar bod op 3-niveau geeft uw partner aan dat hij / zij 10-11 punten heeft.
        Uw partner wilt weten of de manch er in zit, en dat is nu aan u om te bepalen.
        Als u meer dan 14 punten heeft samen met de 10-11 punten van uw partner is dat meestal genoeg voor de manch
        '''

    if state == 'unknown':
        uitleg = '''
        BidBud weet niet alles, dit lijkt iets te zijn wat hij nog niet weet.
        In de volgende versie hoopt BidBud hier een antwoord op te weten.
        Probeer met de kennis die u heeft een antwoord te verzinnen op dit biedprobleem, en soms is het beste wat u kunt doen passen.
        Vriendelijke groeten, BidBud
        '''
    
    if state == 'tussenbieden':
        uitleg = '''
        Als de tegenstanders openen betekend dat niet meteen dat u en uw partner helemaal niet meer mee mogen doen.
        En omdat als uw tegenstanders veel punten hebben, ze toch niet stoppen met bieden, met relatief weinig punten u al veilig bemoeien met de bieding.
        Dat is een reden om tussen te bieden maar de voornaamste reden is informatie.
        Het hele biedingproces gaat erom, zoveel mogelijk informatie naar uw partner te krijgen en dit is een perfecte situatie om informatie naar uw partner te krijgen over uw hand.
        En ookal wordt het niets weet uw partner wel tijdens het spelen waar u sterk in bent.
        '''

    if state == 'infoX':
        uitleg = '''
        Soms heeft u een opening maar is uw tegenstander u voor en weet u niet goed wat u nu moet doen.
        U heeft veel punten en wilt dat dus op een zo'n effictiefste manier aan uw partner laten weten.
        Daar is het informatie doublet voor, u doubleert op de opening van de tegenstanders en uw partner weet dat u een opening heeft.
        '''

    if state == 'answeringJacoby6Crd':
        uitleg = '''
        U heeft Jacoby gedaan om uw partner te laten weten dat u een vijfkaart in die kleur heeft, net niet genoeg voor een fit.
        Maar als u overwaarde heeft, een zeskaart dus, hebben jullie ineens wel een fit in die kleur en kunt u aan nadenken of er een manch in zit.
        Dus als u meer dan 10 punten heeft en een zeskaart in die hoge kleur is het meestal een goed idee om eerst Jacoby te doen en dan nadat uw partner de transfer heeft beantwoord, de manch te bieden.
        '''

    if state == 'Jacoby-3SA':
        uitleg = '''
        U heeft Jacoby geboden om uw partner te vertellen dat u een vijfkaart in een van de hoge kleuren heeft.
        Uw partner weet niet hoe sterk u bent, wat uw partner betreft kunt u 0 punten hebben, dus is het misschien een goed idee om uw partner ongelijk te bewijzen.
        Maar dat is ook een andere goede reden voor waarom Jacoby zo handig is, doordat u precies weet wat uw partner gaat antwoorden kunt u met 20 punten bij wijze van spreken nog Jacoby doen.
        U krijgt als het ware 2 beurten achter elkaar en dat is een goede kans om uw partner goed te vertellen wat u in uw handen hebt.
        U weet heel precies wat uw partner heeft en kunt dat goed gebruiken om te bepalen in welk contract jullie gaan zitten, u weet dat uw partner meer dan 15 punten heeft bijvoorbeeld.
        Als u dus meer dan 10 punten heeft weet u dat er een manch in gaat zitten, u weet ook dat dat of 3SA of 4♥/♠ gaat zijn.
        Welke het wordt hangt af van of jullie een fit hebben in de hoge kleuren, en dat hangt weer af van of uw partner een tweekaart of meer heeft.
        Door 3SA te bieden vraagt u aan uw partner welk contract hem beter uitkomt, 3SA of 4 in de hoge kleuren.
        '''

    if state == 'Jacoby-2SA':
        uitleg = '''
        U heeft Jacoby geboden om uw partner te vertellen dat u een vijfkaart in een van de hoge kleuren heeft.
        Uw partner weet niet hoe sterk u bent, wat uw partner betreft kunt u 0 punten hebben, dus is het misschien een goed idee om uw partner ongelijk te bewijzen.
        Maar dat is ook een andere goede reden voor waarom Jacoby zo handig is, doordat u precies weet wat uw partner gaat antwoorden kunt u met 20 punten bij wijze van spreken nog Jacoby doen.
        U krijgt als het ware 2 beurten achter elkaar en dat is een goede kans om uw partner goed te vertellen wat u in uw handen hebt.
        U weet heel precies wat uw partner heeft en kunt dat goed gebruiken om te bepalen in welk contract jullie gaan zitten, u weet dat uw partner meer dan 15 punten heeft bijvoorbeeld.
        U weet dus ook dat als er een manch in zit dat 3SA of 4♥/♠ gaat zijn.
        Met 8/9 punten is het mogelijk dat er nog een manch in zit, wat betekend dat u niet kunt passen, u wilt eerst van uw partner weten of er een manch in zit. 
        Welke het wordt hangt af van of jullie een fit hebben in de hoge kleuren, en dat hangt weer af van of uw partner een tweekaart of meer heeft.
        Door 2SA te bieden vraagt u aan uw partner of hij/zij maximaal is of minimaal en welk contract hem beter uitkomt, 3SA of 4 in de hoge kleuren.
        '''

    if state == 'answeringJacoby5Crd':
        uitleg = '''
        U heeft Jacoby gedaan om uw partner te laten weten dat u een vijfkaart in die kleur heeft, net niet genoeg voor een fit.
        Maar als u overwaarde heeft, een zeskaart dus, hebben jullie ineens wel een fit in die kleur en kunt u aan nadenken of er een manch in zit.
        Dus als u meer dan 10 punten heeft en een zeskaart in die hoge kleur is het meestal een goed idee om eerst Jacoby te doen en dan nadat uw partner de transfer heeft beantwoord, de manch te bieden.
        Maar soms heeft u niet meer dan 10 punten en heeft u mogelijke manch waarde en wilt u dat aan uw partner laten weten.
        U wilt laten weten hoeveel punten u heeft en dat u een zeskaart heeft in die kleur, daarom herhaald u uw langste kleur
        '''
    
    

    
    
    return uitleg
    
        



        