def uitleg_nl(state):
    uitleg = ''
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

    if state == '1CS_opening':
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
        '''

    if state == 'preemtif3':
        uitleg = '''
        Om te openen heeft u minimaal 12 punten nodig, soms heeft u dit niet maar wel een hele lange kaart.
        Dan mag u uw tegenstanders een beetje pesten door hun bieding te saboteren.
        Dit heet preemtif bieden, bieden met een lange kaart in plaats van met punten, om te slagen heeft u wel een punten minimum van 6.
        Door hoog te bieden met weinig punten neemt u biedruimte weg voor uw tegenstanders, vandaar pesten dus.
        Met een 7 kaart bied u op 3-niveau, hoe langer de kaart hoe hoger u mag bieden en hoe vervelender u mag zijn voor de tegenstanders.
        '''

    if state == 'preemtif4':
        uitleg = '''
        Om te openen heeft u minimaal 12 punten nodig, soms heeft u dit niet maar wel een hele lange kaart.
        Dan mag u uw tegenstanders een beetje pesten door hun bieding te saboteren.
        Dit heet preemtif bieden, bieden met een lange kaart in plaats van met punten, om te slagen heeft u wel een punten minimum van 6.
        Door hoog te bieden met weinig punten neemt u biedruimte weg voor uw tegenstanders, vandaar pesten dus.
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

    if state == 'answer_to_jacoby_nocolors':
        uitleg = '''
        Uw partner bied Stayman, hiermee vraagt hij of u een hoge kleur heeft, 
        als u een vierkaart of meer heeft in een van de hoge kleuren moet u dat aan uw partner laten weten.
        In dit geval is dat niet zo, ook dat wilt u uw partner laten weten, hier is het bod 2♦ voor.
        U zegt nu dat u geen vierkaart of meer in een van de hoge kleuren heeft.
        '''
        
    return uitleg
    
        



        