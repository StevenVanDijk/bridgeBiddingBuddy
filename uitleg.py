def uitleg_nl(state):
    uitleg = ''

    if state == 'rondpass':
        uitleg = '''        
        U, en uw tegenstanders, mogen pas openen met 12 punten, er zitten in totaal 40 punten in het spel.
        Dat betekent dat het mogelijk is dat niemand 12 punten heeft, wat betekend dat het mogelijk is dat niemand opent.
        Als dat het geval is spreken we van een rondpas.
        In het geval van een rondpas, is er geen contract, wat betekend dat er niet gespeeld kan worden.
        '''

    if state == '1SA_opening':
        uitleg = '''
        Als uw puntenaantal ligt tussen 15 en 17 denkt u altijd als eerst aan een SA-opening.
        Dit staat voor sans a tout, zonder troef.
        Als u heeft vastgesteld dat uw puntenaantal goed is kunt u kijken of u een sans-verdeling heeft.
        Een sansverdeling is een verdeling waarin geen kleur meer dan 5 kaarten bevat, en geen minder dan 2.
        Als dit het geval is betekend dat dat u 1SA kunt openen.
        '''

    if state == '1SA_opening-NT':
        uitleg = '''
        Als uw puntenaantal ligt tussen 15 en 17 denkt u altijd als eerst aan een SA-opening.
        SA staat voor sans a tout, wat zonder troef betekent in het Frans.
        Als u heeft vastgesteld dat uw puntenaantal goed is kunt u kijken of u een sans-verdeling heeft.
        Een sansverdeling is een verdeling waarin geen kleur meer dan 5 kaarten bevat, en geen minder dan 2.
        Als dit het geval is betekend dat dat u 1SA kunt openen.
        '''

    if state == '2SA_opening':
        uitleg = '''
        Als uw puntenaantal tussen de 20 en 22 ligt denkt u altijd als eerst aan een 2SA-opening.
        SA staat voor sans a tout, wat zonder troef betekent in het Frans.
        Als u heeft vastgeseteld dat uw puntenaantal goed is kunt u kijken of u een sansverdeling heeft.
        Een sansverdeling is een verdeling waarin geen kleur meer dan 5 kaarten bevat, en geen minder dan 2.
        Als dit het geval is betekend dat dat u 2SA kunt openen.
        '''

    if state == '2Cs_opening':
        uitleg = '''
        Een 2♣ opening is manchforcing, dit betekent dat u naar de manch gaat.
        De manch is 3SA, 4♥, 4♠, 5♣ en 5♦.
        Als u en uw partner de manch halen krijgen jullie extra punten, dat heet de manchpremie.
        Om de manch te bereiken heeft u heel wat punten nodig, 25, of 8 vaste slagen.
        Als u 2♣ kunt openen betekent dat dat u en uw parten niet mogen stoppen met bieden totdat 
        jullie de manch hebben bereikt.
        '''

    if state == 'Normal_5card':
        uitleg = '''
        Om te openen heeft u minimaal 12 punten nodig.
        Daarna moet u vaststellen in welke kleur u gaat openen, 
        uw eerste keus is altijd de kleur waarin de meeste kaarten zitten.
        Met 2 vijfkaarten opent u de hoogste, met 2 vierkaarten de laagste, en uiteraard als u een zeskaart heeft gaat dat boven uw vijfkaart en vierkaart.
        Zels als de zeskaart een lage kleur is en de vijfkaart of vierkaart een hoge.
        '''


    if state == 'Normal_4card':
        uitleg = '''
        Om te openen heeft u minimaal 12 punten nodig.
        Daarna moet u vaststellen in welke kleur u gaat openen, 
        uw eerste keus is altijd de kleur waarin de meeste kaarten zitten.
        Met 2 vijfkaarten opent u de hoogste, met 2 vierkaarten de laagste.
        Echter, met de hoge kleuren, ♥ en ♠, mag u pas openen met een vijfkaart.
        '''

    if state == '1Cs_opening':
        uitleg = '''
        Om te openen heeft u minimaal 12 punten nodig.
        Daarna moet u vaststellen in welke kleur u gaat openen, 
        uw eerste keus is altijd de kleur waarin de meeste kaarten zitten.
        Met 2 vijfkaarten opent u de hoogste, met 2 vierkaarten de laagste.

        Echter, met de hoge kleuren, ♥ en ♠, mag u pas openen met een vijfkaart.
        In het geval u dan niet kunt openen, 
        dus u heeft geen vierkaart in de lage kleuren en geen vijfkaart in de hoge, rest er het 1♣ bod.
        Dit kan al vanaf een doubleton in klaveren, onthoud dat dus voor als uw partner dit bied.
        '''

    if state == 'preemtif2':
        uitleg = '''
        Om te openen heeft u minimaal 12 punten nodig, soms heeft u dit niet maar wel een hele lange kaart.
        Dan mag u uw tegenstanders een beetje pesten door hun bieding te saboteren.
        Dit heet preëmptief bieden, bieden met een lange kaart in plaats van met punten, om te slagen heeft u wel een punten minimum van 6.
        Door hoog te bieden met weinig punten neemt u biedruimte weg voor uw tegenstanders, vandaar pesten dus.
        Met een 6 kaart bied u op 2-niveau, hoe langer de kaart hoe hoger u mag bieden en hoe vervelender u mag zijn voor de tegenstanders.
        Onthoud ook dat preëmptief bieden gedefinieerd wordt door de sprong, dus als uw tegenstander, of partner al geboden heeft is preëmptief bieden mogelijk.
        '''

    if state == 'preemtif3':
        uitleg = '''
        Om te openen heeft u minimaal 12 punten nodig, soms heeft u dit niet maar wel een hele lange kaart.
        Dan mag u uw tegenstanders een beetje pesten door hun bieding te saboteren.
        Dit heet preëmptief bieden, bieden met een lange kaart in plaats van met punten, om te slagen heeft u wel een punten minimum van 6.
        Door hoog te bieden met weinig punten neemt u biedruimte weg voor uw tegenstanders, vandaar pesten dus.
        Onthoud ook dat preëmptief bieden gedefinieerd wordt door de sprong, dus als uw tegenstander, of partner al geboden heeft is preëmptief bieden mogelijk.
        Met een 7-kaart bied u op 3-niveau, hoe langer de kaart hoe hoger u mag bieden en hoe vervelender u mag zijn voor de tegenstanders.
        '''

    if state == 'preemtif4':
        uitleg = '''
        Om te openen heeft u minimaal 12 punten nodig, soms heeft u dit niet maar wel een hele lange kaart.
        Dan mag u uw tegenstanders een beetje pesten door hun bieding te saboteren.
        Dit heet preëmptief bieden, bieden met een lange kaart in plaats van met punten, om te slagen heeft u wel een punten minimum van 6.
        Door hoog te bieden met weinig punten neemt u biedruimte weg voor uw tegenstanders, vandaar pesten dus.
        Onthoud ook dat preëmptief bieden gedefinieerd wordt door de sprong, dus als uw tegenstander, of partner al geboden heeft is preëmptief bieden mogelijk.
        Met een 8-kaart bied u op 4-niveau, hoe langer de kaart hoe hoger u mag bieden en hoe vervelender u mag zijn voor de tegenstanders.
        Als u preëmptief biedt op 4-niveau kan het zijn dat u al de manch heeft bereikt, namelijk in de hoge kleuren. Dan spelen jullie dus de manch.
        '''

    if state == 'open_pass':
        uitleg = '''
        Om te openen heeft u minimaal 12 punten nodig, soms heeft u deze gewoon niet en hoe vervelend ook, moet u passen.
        '''

    if state == 'jacoby':
        uitleg = '''
        Uw partner bied 1SA, dit betekend 15-17 punten en een evenwichtige hand.
        U weet ook dat uw partners laagste kaart een doubleton is.
        Samen 8 kaarten heet een fit (met een fit kunt u in die kleur spelen), dus minimaal 2 + 5 is bijna een fit.
        Als jullie een (bijna) fit hebben kunnen jullie beter in die kleur spelen dan het risico van SA te nemen,
        daarom is Jacoby bedacht, en daarom kunt u dit ook al bieden vanaf 0 punten,
        met de voorwaarde van een vijfkaart in een van de hoge kleuren, ♥ en ♠.
        Omdat u liever heeft dat de tegenstanders de minste punten zien, en dus de minste honneurs, heeft u het liefst dat de 1SA openaar speelt,
        daar heeft de heer Jacoby iets op bedacht, als u, met deze hand, de kleur onder de kleur die eigenlijk wilt bieden biedt,
        kan daarna uw partner de kleur bieden die u bedoelde, dit is verplicht, en is het spel in de hand van de openaar.
        '''

    if state == 'jacoby-2sa':
        uitleg = '''
        Uw partner bied 2SA, dit betekend 20-22 punten en een evenwichtige hand.
        U weet ook dat uw partners laagste kaart een doubleton is.
        Samen 8 kaarten heet een fit (met een fit kunt u in die kleur spelen), dus minimaal 2 + 5 is bijna een fit.
        Als jullie een (bijna) fit hebben kunnen jullie beter in die kleur spelen dan het risico van SA te nemen,
        daarom is Jacoby bedacht, en daarom kunt u dit ook al bieden vanaf 0 punten,
        met de voorwaarde van een vijfkaart in een van de hoge kleuren, ♥ en ♠.
        Omdat u liever heeft dat de tegenstanders de minste punten zien, en dus de minste honneurs, heeft u het liefst dat de 2SA openaar speelt,
        daar heeft de heer Jacoby iets op bedacht, als u, met deze hand, de kleur onder de kleur die eigenlijk wilt bieden biedt,
        kan daarna uw partner de kleur bieden die u bedoelde, dit is verplicht, en is het spel in de hand van de openaar. 
        '''

    if state == 'stayman':
        uitleg = '''        
        Uw partner biedt 1SA, dit betekend 15-17 punten en een evenwichtige hand.
        Het liefst speelt u in een hoge kleur, ♥ en ♠. 
        Dus als u een vierkaart in een van de hoge kleur heeft is dit het onderzoeken waard, 
        en aangezien u met 8-9 punten prima 2SA kunt spelen kunt u met dit puntenaantal ook eerst de hoge kleuren onderzoeken.
        U biedt 2♣ om aan uw partner te vragen of hij een vierkaart in een van de hoge kleuren heeft. 
        Onthoud echter wel dat dit alleen zin heeft als u ook een vierkaart in de hoge kleuren heeft.
        '''

    if state == 'stayman-2sa':
        uitleg = '''
        Uw partner biedt 2SA, dit betekend 20-22 punten en een evenwichtige hand.
        Het liefst speelt u in een hoge kleur, ♥ en ♠. 
        Dus als u een vierkaart in een van de hoge kleur heeft is dit het onderzoeken waard.
        Met 5 punten halen jullie al de manch (want 20 + minimaal 5 = minimaal 25) dus er zijn niet veel punten nodig om dit te onderzoeken.
        U biedt 3♣ om aan uw partner te vragen of hij een vierkaart in een van de hoge kleuren heeft.
        '''

    if state == '1SA-2SA':
        uitleg = '''
        Uw partner bied 1SA, dit betekend 15-17 punten en een evenwichtige hand.
        Het liefst speelt u in een hoge kleur, ♥ en ♠, maar als u geen vierkaart in een van deze kleuren heeft is dit het niet waard.
        U weet dat uw partner 15-17 punten heeft, met 8 punten, (8 + 17 = 25) kunnen jullie de manch nog halen,
        om aan uw partner te vragen of hij denkt dat dit nog mogelijk is bied u 2SA, met een maximum bied uw partner de manch.
        '''

    if state == '1SA-3SA':
        uitleg = '''
        Uw partner bied 1SA, dit betekend 15-17 punten en een evenwichtige hand.
        Het liefst speelt u in een hoge kleur, ♥ en ♠, maar als u geen vierkaart in een van deze kleuren heeft is het niet het onderzoeken waard.
        Maar u heeft 10+ punten (10 + 15 = 25) dus u wilt naar de manch, 
        aangezien u al weet dat het geen hoge kleuren manch gaat worden biedt u gewoon de een-na-beste manche, 3SA.
        '''

    if state == '1SA-pass':
        uitleg = '''
        Uw partner bied 1SA, dit betekend 15-17 punten en een evenwichte hand.
        Als u geem vijfkaart heeft in de hoge kleuren en niet meer dan 7 punten, is 1SA gewoon een prima contract.
        '''

    if state == 'answer_to_stayman_colors':
        uitleg = '''
        Uw partner biedt Stayman, hiermee vraagt hij of u een hoge kleur heeft, 
        als u een vierkaart of meer heeft in een van de hoge kleuren moet u dat aan uw partner laten weten.
        '''

    if state == 'answer_to_stayman_nocolors':
        uitleg = '''
        Uw partner biedt Stayman, hiermee vraagt hij of u een hoge kleur heeft, 
        als u een vierkaart of meer heeft in een van de hoge kleuren moet u dat aan uw partner laten weten.
        In dit geval is dat niet zo, ook dat wilt u uw partner laten weten, hier is het bod 2♦ voor.
        U zegt nu dat u geen vierkaart of meer in een van de hoge kleuren heeft.
        '''

    if state == 'answer_to_stayman_multicolor':
        uitleg = '''
        Uw partner biedt Stayman, hiermee vraagt hij of u een hoge kleur heeft, 
        als u een vierkaart of meer heeft in een van de hoge kleuren moet u dat aan uw partner laten weten.
        Maar wat nu als u in beide kleuren  4 of maar kaarten heeft?
        Dan biedt u 2♥, daarna bied uw partner of 2SA, 3SA, 3♥ of 4♥.
        Als uw partner SA bied ontkent hij / zij harten, maar door Stayman te bieden beloofde hij / zij minstens een vierkaart in een van de hoge kleuren.
        Wat betekend dat, in het geval van een SA-bod, u weet dat jullie fit in de schoppen zit, en dan kunt u dan schoppen bieden over uw partners SA.
        Dus ook al laat u uw partner niet meteen weten dat u ook een 4-kaart in de schoppen heeft, kunt u zo wel te weten komen of jullie fit in de harten of schoppen zit.
        '''

    if state == 'OpStayman':
        uitleg = '''
        Uw tegenstanders bieden Stayman en zijn op zoek naar het juiste contract voor wat ze kunnen spelen,
        de kans dat u en uw partner een contract gaan maken is dan erg klein, 
        dat betekent niet dat u geen informatie aan uw partner kunt geven.
        Uw tegenstander heeft Stayman geboden, daarmee geeft hij geen klaveren aan, dus dit is een ideaal moment om er veilig een doublet te bieden, aangezien de 1SA-openaar nooit mag passen, en het doublet dus geen waarde heeft.
        Dus als u een goede kaart klaveren heeft is dit de ideale situatie om dat aan uw partner te laten weten, door te doubleren.
        '''

    if state == 'OpStaymanPass':
        uitleg = '''
        Uw tegenstanders bieden stayman en zijn op zoek naar het juiste contract voor wat ze kunnen spelen,
        de kans dat u en uw partner een contract gaan maken is dan erg klein, 
        dat betekent niet dat u geen informatie aan uw partner kunt geven.
        Uw tegenstander heeft Stayman geboden, daarmee geeft hij geen klaveren aan, dus dit is een ideaal moment om veilig een doublet te bieden, aangezien de 1SA-openaar nooit mag passen, en het doublet dus geen waarde heeft.
        Dus als u een goede kaart klaveren hebt is dit de ideale situatie om dat aan uw partner te laten weten, door te doubleren.
        Echter als u nu doubleert is de kans groot dat uw partner terugkomt met klaveren als dat niet de bedoeling is moet u ook niet doubleren.
        Dus als u geen lange klaverkaart heeft, of niet genoeg honneurs is het soms beter gewoon te passen.
        '''
    
    if state == 'StaymanPa2SAminMulti':
        uitleg = '''
        U heeft zowel een vierkaart harten als een vierkaart schoppen.
        Met Stayman vroeg uw partner naar uw hoge kleuren, daar antwoordde u 2♥ op, omdat u uw partner wilde laten weten dat u mogelijk ook nog een schoppen kaart kon hebben naast de minimaal 4 harten.
        Dus nu uw partner met 2SA aangeeft dat hij / zij geen harten heeft, en dus schoppen, weet u dat jullie een fit hebben in de schoppen.
        En doordat uw partner 2SA heeft geboden weet u dat uw partner 8/9 punten heeft en dus net niet genoeg voor de manch.
        Uw partner vraagt nu aan u of u genoeg heeft om naar de manch te gaan, maar omdat u maar 15 punten heeft is dat net niet genoeg voor de manch.
        Dus u biedt 3♠.
        '''

    if state == 'StaymanPa2SAmaxMulti':
        uitleg = '''
        U heeft zowel een vierkaart harten als een vierkaart schoppen.
        Met Stayman vroeg uw partner naar uw hoge kleuren, waarop u 2♥ antwoordde, omdat u uw partner wilde laten weten dat u mogelijk ook nog een schoppen kaart kon hebben naast de minimaal 4 harten.
        Dus nu uw partner met 2SA aangeeft dat hij / zij geen harten heeft, en dus schoppen, weet u dat jullie een fit hebben in de schoppen.
        En doordat uw partner 2SA heeft geboden weet u dat uw partner 8/9 punten heeft en dus net niet genoeg voor de manch.
        Uw partner vraagt nu aan u of u genoeg heeft om naar de manch te gaan, u heeft genoeg punten om de manch te halen.
        Dus u biedt 4♠.
        '''
    
    if state == 'StaymanPa2SA':
        uitleg = '''
        Uw partner verteld u dat hij / zij een andere vierkaart dan u heeft, want met 2♣ beloofde uw partner een vierkaart hoog, maar hij  / zij ontkent uw vierkaart.
        Wat betekend dat uw partner de andere kleur heeft. Met 2SA verteld uw partner nog iets, namelijk dat hij / zij 8/9 punten bezit.
        En vraagt aan u of u genoeg punten heeft om de manch te halen. Daarom biedt u de manch met een maximale hand en past u met een minimale.
        '''

    if state == 'StaymanPa3SAMulti':
        uitleg = '''
        U heeft zowel een vierkaart harten als een vierkaart schoppen.
        Met Stayman vroeg uw partner naar uw hoge kleuren, waarop u 2♥ antwoordde, omdat u uw partner wilde laten weten dat u mogelijk ook nog een schoppen kaart kon hebben naast de minimaal 4 harten.
        Dus nu uw partner met 3SA aangeeft dat hij / zij geen harten heeft, en dus schoppen, weet u dat jullie een fit hebben. 
        En doordat uw partner 3SA heeft geboden weet u ook dat de manch erin zit.
        Dus u biedt 4♠, want een manch in de hoge kleuren is beter dan een manch in sans.
        '''

    if state == 'OpJacoby':
        uitleg = '''
        Uw tegenstanders bieden Jacoby en zijn op zoek naar het juiste contract voor wat ze kunnen spelen,
        de kans dat u en uw partner een contract gaan maken is dan erg klein, 
        dat betekent niet dat u geen informatie aan uw partner kunt geven.
        Uw tegenstander heeft Jacoby geboden, daarmee geeft hij niet de geboden kleur aan, 
        dus dit is een ideaal moment om veilig een doublet tussen te bieden, 
        aangezien de 1SA-openaar nooit gaat passen, en het doublet dus geen waarde heeft.
        Dus als u een goede kaart in de geboden kleur heeft is dit de ideale situatie om dat aan uw partner te laten weten, 
        door te doubleren.
        '''

   

 if state == 'AnswerJacoby':
        uitleg = '''
        Uw partner weet dat uw laagste kaart een doubleton is, en dat u 15-17 punten heeft.
        Samen 8 kaarten heet een fit (met een fit kunt u in die kleur spelen), dus minimaal 2 + 5 is bijna een fit.
        Als jullie een (bijna) fit hebben kunnen jullie beter in die kleur spelen dan het risico van SA te nemen,
        daarom is Jacoby bedacht, en daarom kan uw partner dit ook al bieden vanaf 0 punten,
        met de voorwaarde van een vijfkaart in een van de hoge kleuren, ♥ en ♠.
        Omdat u liever heeft dat de tegenstanders de minste punten zien, en dus de minste honneurs, 
        heeft u het liefst dat de 1SA openaar speelt,
        daar heeft de heer Jacoby iets op bedacht, als uw partner, de kleur onder de kleur die hij / zij eigenlijk zou willen bieden bied,
        kan u daarna de kleur boven de kleur van uw partner bieden, en is het spel in uw hand, die van de openaar.
        '''

    if state == 'AfterTransferPass':
        uitleg = '''
        Toen u Jacoby bood deed u dat met de intentie om uw partner uw langste kleur te laten weten.
        Als u dat gedaan heeft en niets meer te vertellen heeft aan uw partner kunt u gerust passen.
        '''

    if state == 'AfterTransder2SA':
        uitleg = '''
        Toen u Jacoby bood deed u dat met de intentie om uw partner uw langste kleur te laten weten.
        Maar u heeft 8/9 punten, wat betekend dat er mogelijk nog een manch in zit!
        En als er mogelijk nog een manch in zit mag u dat niet laten varen, 
        dus moet u aan uw partner "overleggen" of hij denkt dat er een manch in zit.
        Dat doet u door 2Sa te bieden.
        '''

    if state == 'AfterTransfer3SA':
        uitleg = '''
        U partner bood als eerste 1SA dat betekent dat hij / zij 15-17 punten heeft. 
        U wilde aan uw partner laten weten dat u een vijfkaart had, wat een goed iets is maar nu moet u ook laten weten hoeveel punten u heeft.
        U heeft 10 punten, en uw partner minimaal 15. 
        10 + 15 = 25
        25 punten is genoeg voor de manch, nu is nog de vraag of u liever een manch in 3SA heeft of in uw kleur.
        Uw partner weet dat u een vijfkaart heeft in die kleur dus het heeft geen zin die kleur nog een keer te bieden.
        Daarom kunt u 3SA bieden, als uw partner wel een driekaart in uw kleur heeft en jullie dus een fit hebben, 
        bied uw partner nog de manch in die kleur.
        Heeft uw partner dit niet, dan past uw partner.
        '''

    if state == 'AfterTransferManchinClr':
        uitleg = '''
        Uw partner opende 1SA, wat betekent dat uw partner 15-17 punten heeft, 
        maar het betekent ook dat uw partners laagste kleur minimaal 2 kaarten bevat.
        Dus als u een zeskaart heeft, heeft u altijd fit, nu heeft u eerst netjes Jacoby geboden om aan te geven dat u een vijfkaart heeft.
        Maar u heeft geen vijfkaart, u heeft een zeskaart, en uw partner weet dat nog niet.
        Uw partner heeft ook 15 punten, wat betekend dat als u meer dan 10 punten heeft, jullie samen 25 punten hebben.
        En 25 is genoeg voor de manch.
        Dus jullie hebben een fit om een kleur in te spelen, en jullie hebben genoeg punten om de manch te spelen.
        Dan kunt u dus gewoon de manch bieden.
        '''

    if state == 'AfterTransferInviteinClr':
        uitleg = '''
        Uw partner opende 1SA, wat betekend dat uw partner 15-17 punten heeft, 
        maar het betekent ook dat uw partners laagste kleur minimaal 2 kaarten bevat.
        Dus als u een zeskaart heeft, heeft u altijd fit, nu heeft u eerst netjes Jacoby geboden om aan te geven dat u een vijfkaart heeft.
        Maar u heeft geen vijfkaart, u heeft een zeskaart, en uw partner weet dat nog niet.
        U heeft 8/9 punten wat betekend dat jullie mogelijk een manch kunnen spelen,
        en u wilt een invite geven om de manch te doen aangezien uw partner weet of jullie de manch gaan doen.
        Dus bied u op 3-niveau uw eigen kleur, als uw partner genoeg punten heeft om naar de manch te gaan biedt uw partner de manch.
        '''

    if state == 'AfterInviteClr':
        uitleg = '''
        Uw partner geeft aan dat hij een zeskaart heeft en net niet genoeg punten om de manch te halen.
        U heeft aangegeven 15-17 punten te halen dat betekent dat er een marge tussen zit. 
        Dus uw partner vraagt nu om, als u sterk bent er de manch van te maken en als u zwak bent te passen.
        '''
        



    if state == 'NXMs':
        uitleg = '''
        Soms biedt een tegenstander tussen en ontneemt u daarmee de kans te bieden wat u wilde bieden,
        daar is het negatief doublet voor bedacht, als de tegenstander een bod doet waardoor u niet meer uw ideale bod kunt doen,
        omdat het bod wat u wilde doen onder het bod van de tegenstander ligt, heeft u de mogelijkheid te doubleren,
        wat betekent dat u het bod wilde doen wat nu niet meer kan. 
        Wegens deze conventie is er nog een mogelijkheid bedacht, in welke u nu zit.
        Als u zowel harten en schoppen bevat krijgt u in dit geval de kans te doubleren 
        waardoor uw partner weet dat u en een 4krt ♥ en ♠ heeft
        '''

    if state == 'NXHs':
        uitleg = '''
        Soms biedt een tegenstander tussen en ontneemt u daarmee de kans te bieden wat u wilde bieden,
        daar is het negatief doublet voor bedacht, als de tegenstander een bod doet waardoor u niet meer uw bod kunt doen,
        omdat het bod wat u wilde doen onder het bod van de tegenstander ligt, heeft u de mogelijkheid te doubleren,
        wat betekent dat u het bod wilde doen wat nu niet meer kan, in dit geval 1♥
        '''

    if state == 'NXSs4':
        uitleg = '''
        Soms biedt een tegenstander tussen en ontneemt u daarmee de kans te bieden wat u wilde bieden,
        daar is het negatief doublet voor bedacht, als de tegenstander een bod doet waardoor u niet meer uw bod kunt doen,
        omdat het bod wat u wilde doen onder het bod van de tegenstander ligt, heeft u de mogelijkheid te doubleren,
        wat betekent dat u het bod wilde doen wat nu niet meer kan, maar doordat die regel bestaat is er nog een regel bedacht.
        Als het biedverloop zo gaat:

        N         O      Z    W
        1♣/♦   P    1♥  ???

        Voldoet het biedverloop aan de regels voor een negatief doublet, dus kunt u hier een negatief doublet doen maar u kunt ook gewoon uw kleur bieden.
        Dus is er bedacht dat als in deze specifieke situatie doubleerd, u precies een vierkaart beloofd, als u 1♠ biedtgeeft u een vijfkaart aan.
        Maar soms heeft u een vijfkaart schoppen maar niet genoeg punten om een normaal antwoord te doen op uw partner dat is de enige situatie waarin u ook mag doubleren in dit geval.
        In dit geval mag u dus doubleren
        '''

    if state == 'NXSs5+':
        uitleg = '''
        Soms biedt een tegenstander tussen en ontneemt u daarmee de kans te bieden wat u wilde bieden,
        daar is het negatief doublet voor bedacht, als de tegenstander een bod doet waardoor u niet meer uw bod kunt doen,
        omdat het bod wat u wilde doen onder het bod van de tegenstander ligt, heeft u de mogelijkheid te doubleren,
        wat betekent dat u het bod wilde doen wat nu niet meer kan, maar doordat die regel bestaat is er nog een regel bedacht.
        Als het biedverloop zo gaat:

        N         O     Z     W
        1♣/♦  P    1♥   ???

        Het biedverloop voldoet aan de regels voor een negatief doublet, dus u kunt hier een negatief doublet doen maar u kunt ook gewoon uw kleur bieden.
        Dus is er bedacht dat als in deze specifieke situatie doubleert, u precies een vierkaart aan geeft, als u 1♠ biedt, geeft u een vijfkaart aan.
        Doordat u nu op een normale plek antwoord heeft u wel een normaal aantal punten nodig, 6+.
        In dit geval bied u dus 1♠
        '''



    if state == '2Cs-2x':
        uitleg = '''
        Uw partner biedt manchforcing, wat betekent dat geen van jullie mag passen totdat jullie de manch hebben bereikt.
        Uw partner kan of 23+ punten hebben met een sans-verdeling, of een lange kaart.
        In elk geval heeft uw partner 8 vaste slagen dat betekent dat hij / zij zonder uw hulp al de manch kan halen maar nu wil hij / zij alleen nog weten wat de gunstigste manch is in combinatie met uw kaart.
        U wilt uw partner laten weten wat u heeft, en dat doet u door uw langste kleur te bieden.
        '''

    if state == '2Cs-2Ds':
        uitleg = '''
        Uw partner biedt manchforcing, wat betekend dat geen van jullie mag passen totdat jullie de manch hebben bereikt.
        Uw partner kan of 23+ punten hebben met een sansverdeling, of een lange kaart.
        In elk geval heeft uw partner 8 vaste slagen.
        Omdat uw partner manchforcing biedt kunt u niet passen, zelfs niet met 0 punten,
        maar met 0 punten wilt u uw partner de ruimte geven, zijn / haar kaart te beschrijven.
        Daarom is er het relay-bod bedacht, het zegt gewoon, partner ik heb niets interessants, wat heeft u?
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
        Met 2SA geeft u aan dat u op punten heeft geboden en niet op een hele lange kaart,
        uw partner weet nu dus dat u 23+ punten heeft en een plausibele sansverdeling
        '''

    if state == '2Cs-2Ds-2x':
        uitleg = '''
        Uw partner heeft aangegeven niet veel te hebben, en heeft het aan u overgelaten te vertellen wat u heeft.
        Dus als u een lange kaart heeft moet u laten weten welke kleur die lange kaart dan zit.
        '''

    if state == '2Cs-2Hs':
        uitleg = '''
        Uw partner heeft harten, nu is het aan u om te laten weten wat u heeft, 
        dan kunnen jullie later vaststellen in welk contract jullie de meeste slagen en punten kunnen halen.
        '''

    if state == 'normal_pass':
        uitleg =  '''
        Soms heeft u gewoon niet genoeg punten, en niet een bijzonder genoeg kaart om te bieden, dan moet u gewoon passen. 
        Vergeet niet dat pas niet betekend dat u niet mee doet in de bieding, met een bod geeft u belangrijke 
        informatie, maar met een pass ook, u verteld uw partner wat u niet heeft. 
        Bijvoorbeeld als u past in plaats van te openen, weet uw partner dat uw punten aantal onder de twaalf zit en u niet een hele lange kaart heeft.
        Bovendien is het belangrijk dat u geen valse informatie naar uw partner stuurt, als u opent alleen maar omdat u wilt openen en niet omdat u twaalf punten heeft 
        weet uw partner niet wat u nu precies heeft. Terwijl als u past u veel meer informatie geeft.
        '''

    if state == 'answering_partnerClr':
        uitleg = '''
        Uw partner heeft een opening, 12 punten, en nu gaan jullie onderzoeken in welk contract jullie de beste kunnen score halen,
        dat gebeurd door de uitwisseling van informatie, dus dat is wat u doet, u verteld uw partner welke kleur u, 
        met de informatie ter beschikking op dat moment het beste lijkt.
        '''

    if state == 'answering_partnerSa':
        uitleg = '''
        Uw partner heeft een opening, 12 punten, en nu gaan jullie onderzoeken in welk contract jullie de beste score kunnen halen,
        Maar er zijn ook een set regels waar u aan moet voldoen, anders raakt uw partner in de war.
        Een van die regels is dat als u op 1-niveau een nieuwe kleur biedt u 6+ punten beloofd, en op 2-niveau 10+ punten. 
        Een andere regel is dat u niet mag passen op uw partners opening met meer dan 6 punten.
        Nog een andere regel is dat u op 1-niveau op uw partner antwoordt, uw partner verwacht dat u een vierkaart heeft.
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
    
    if state == 'answerPaLevel2':
        uitleg = '''
        Uw tegenstanders doen vervelend bij tussenbieden wat betekend dat u uw partner niet meer op 1-niveau kan vertellen wat uw beste kleur is.
        Maar dat betekend niet dat u dat helemaal niet meer kunt doen.
        Met 10 punten of meer mag u namelijk gewoon uw beste kleur op 2-niveau bieden.
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

    if state == 'fitFoundedU2Cs':
        uitleg = '''
        De ideale manch is 4 in de hoge kleuren, maar soms zit dat er niet in en moeten jullie op zoek naar een andere optie, bijvoorbeeld sans of de lage kleuren.
        Als uw partner 1♣ opent betekend dat dat hij of een erg gebalanceerde kaart heeft, of klaveren. 
        Idealiter verteld u eerst uw hoge kleuren maar soms is dat gewoon geen optie dus kunt u als u een vijfkaart heeft of een vierkaart met in de rest van de kleuren een driekaart uw partners klaveren steunen.
        '''

    if state == 'fitFoundedU3Cs':
        uitleg = '''
        Uw partner beloofd met een 1♣ opening minimaal een tweekaart klaveren, als u een zeskaart heeft betekend dat een fit in de klaveren.
        Onthoud wel, een fit in de klaveren is veel minder waard dan een fit in de hoge kleuren. 
        Als uw partner een vijfkaart in een van de hoge kleuren had gehad, had hij / zij die geboden dus dat is niet aan de orde.
        Dat betekend ook dat als u niet een vierkaart in een van de hoge kleuren heeft u die niet hoeft te bieden en ook geen aandacht meer hoeft te geven aan die kleuren.
        Dus kunt u veilig klaveren bieden, door 3♣ te bieden in plaats van 2, geeft u aan dat jullie manch waarde bezitten en een fit in de klaveren.
        Het is dan aan uw partner om te kiezen tussen 3SA en 5♣.
        '''

    if state == 'fitFoundedU2Ds':
        uitleg = '''
        Als u niets te vertellen heeft in de hoge kleuren, dus een vierkaart of zelfs vijfkaart, kunt u net zo goed vertellen wat u wel heeft. 
        Bijvoorbeeld een vierkaart, of vijfkaart, in partners eerstgeboden kleur. 
        Maar u bent niet super sterk, dat is ook informatie voor uw partner. Daarom bied u voorzichtig 2♦.
        '''

    if state == 'fitFoundedU3Ds':
        uitleg = '''
        Als u niets te vertellen heeft in de hoge kleuren, dus een vierkaart of zelfs vijfkaart, kunt u net zo goed vertellen wat u wel heeft. 
        Bijvoorbeeld een vierkaart, of vijfkaart, in partners eerstgeboden kleur. 

        Uw partner beloofd met een 1♦ opening minimaal een vierkaart klaveren, als u een vierkaart heeft betekend dat een fit in de ruiten.
        Onthoud wel, een fit in de lage kleuren is veel minder waard dan een fit in de hoge kleuren. 
        Als uw partner een vijfkaart in een van de hoge kleuren had gehad, had hij / zij die geboden dus dat is niet aan de orde.
        Dat betekend ook dat als u niet een vierkaart in een van de hoge kleuren heeft u die niet hoeft te bieden en ook geen aandacht meer hoeft te geven aan die kleuren.
        Dus kunt u veilig klaveren bieden, door 3♣ te bieden in plaats van 2, geeft u aan dat jullie manch waarde bezitten en een fit in de klaveren.
        Het is dan aan uw partner om te kiezen tussen 3SA en 5♦.
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
        Er is iets gebeurd wat BidBud niet helemaal snapt, of voorzien had.
        Dit kan liggen aan een gebrek aan BidBuds kennis of er is iets niet helemaal goed gegaan in de bieding.
        Als het ligt aan BidBuds kennis hoopt hij bij de volgende verzie u wel van dienst te zijn.
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

    if state == 'X-1SA-tussenbieden':
        uitleg = '''
        Met uw hand wilde u 1SA openen en nu doet uw tegenstander dat, dat is vervelend, en dus moet u een oplossing bedenken.
        U weet dat uw tegenstanders 15+ punten hebben en u weet ook dat u 15 punten heeft, u weet dus ook dat u in het tegenspel erg dwars kan zitten aangezien de snits enzo allemaal bij u zitten.
        Daarom kunt u doubleren, dat verteld uw partner dat u sterk bent en als de partner van de tegenstander niets bied zit u ook nog eens in een fijn contract.
        '''

    if state == 'Clr-1SA-tussenbieden':
        uitleg = '''
        U heeft een lange kaart en wilt uw partner dat graag laten weten, maar uw tegenstanders hebben al 1SA geopend, dat is erg vervelend want nu kunt u helemaal niets meer op 1-niveau openen. 
        Maar omdat uw tegenstanders 1SA hebben geopend weet u ook dat ze niet zomaar een contract op gaan geven, dus kunt u best wel roekeloos bieden.
        Vandaar dat u al met 10 punten en een zeskaart mag tussenbieden na 1SA.
        '''
    
    if state == '3SAtoWeak1SA':
        uitleg = '''
        Uw partner geeft met een 1SA antwoord aan eigenlijk niets te kunnen bieden en dus zwak te zijn.
        Uw partner heeft daarom ook 6-9 punten en geen vierkaart in een van de kleuren die hij / zij nog mogelijk had kunnen bieden.
        Nu is het aan u om te bedenken in welk contract jullie kunnen eindigen.
        U heeft een uitermate sterke hand dus u wilt niet in 1SA eindigen, maar u heeft ook niet een overweldigende kleur die u kunt spelen.
        Dus sans is de goede 'kleur' nu is altijd de volgende vraag, manch?
        U heeft meer dan 19 punten, uw partner 6-9, 19 + 6 = 25, dat zijn genoeg punten om de manch te halen dus het is alleen maar logisch die dan ook te bieden.
        '''

    if state == '2SAtoWeak1SA':
        uitleg = '''
        Uw partner geeft met een 1SA antwoord aan eigenlijk niets te kunnen bieden en dus zwak te zijn.
        Uw partner heeft daarom ook 6-9 punten en geen vierkaart in een van de kleuren die hij / zij nog mogelijk had kunnen bieden.
        Nu is het aan u om te bedenken in welk contract jullie kunnen eindigen.
        U heeft een uitermate sterke hand dus u wilt niet in 1SA eindigen, maar u heeft ook niet een overweldigende kleur die u kunt spelen.
        Dus sans is de goede 'kleur' nu is altijd de volgende vraag, manch?
        U heeft 16-18 punten, 6 + 16 = 22, 9 + 16 = 25, oftewel misschien zit er manch in, misschien niet.
        En degene die weet of er manch in zit is uw partner, die weet namelijk hoeveel punten hij precies heeft, en door het gewoon lief aan uw partner te vragen kunt u erachter komen wat het precies is.
        Dat lief vragen doet u met 2SA.
        '''

    if state == 'passAfterManchPartner':
        uitleg = '''
        U en uw partner hebben de manch bereikt en aangezien het niet meer punten oplevered om hoger te gaan is het alleen maar logisch zo laag moglijk te blijven en te passen.
        
        De manch is:
            3 - SA
            4 - ♥ / ♠
            5 - ♣ / ♦
        '''

    return uitleg
    