from bidding import biddingIsAllowed 
from bidding_states import *
from uitleg import *

def bids(current_bidding, points, schoppen, harten, ruiten, klaver):
    colors = [schoppen, harten, ruiten, klaver]
    highest_series = 0
    secondhighest_series = 0
    thirththighest_series = 0
    lowest_series = 0
    color_hs = None

    for color in colors:
        if color > highest_series:
            highest_series = color        
            if color == colors[3]: 
                color_hs = '♣'
            if color == colors[2]: 
                color_hs = '♦'
            if color == colors[1]: 
                color_hs = '♥'
            if color == colors[0]: 
                color_hs = '♠'

    colors.sort()
    lowest_series = colors[0]
    thirththighest_series = colors[1]
    secondhighest_series = colors[2]

    if len(current_bidding) >= 3 and current_bidding[0] == 'pass' and current_bidding[1] == 'pass' and current_bidding[2] == 'pass':
        if points < 12:
            return ('pass', 'rondpass')

    remove_starting_passes(current_bidding)
    # opening
    if len(current_bidding) == 0:
        if points >= 12:
            if highest_series <= 5 and lowest_series >= 2:
                if points >= 15 and points <= 17:
                    return ('1SA', '1SA_opening')
                
                if points >= 20 and points <= 22:
                    return ('2SA', '2SA_opening')     
            
            elif points >= 22 or (points >= 15 and highest_series >= 7):
                return ('2♣', '2Cs_opening')            

            elif highest_series >= 5:
                return ('1' + color_hs, 'Normal_5card')

            elif highest_series == 4 and color_hs != '♥' and color_hs != '♠': 
                return ('1' + color_hs, 'Normal_4card')

            else:
                return ('1♣', '1Cs_opening')

        if points < 12:
            if points <= 10:
                if highest_series >= 6:
                    if highest_series == 6:
                        return ('2' + color_hs, 'preemtif2')
                    if highest_series == 7:
                        return ('3' + color_hs, 'preemtif3')
                    if highest_series == 8:
                        return ('4' + color_hs, 'preemtif4')

                else: 
                    if biddingIsAllowed(current_bidding, 'pass'): 
                        return ('pass', 'open_pass')

            else:
                return ('pass', 'open_pass')
        else: 
            return ('pass', 'open_pass')

    # answering
    # answering to 1SA
    if is1SA_Pa(current_bidding) or is2SA_openingPa(current_bidding):
        if color_hs == '♥' or color_hs == '♠':
            # Jacoby
            if highest_series >= 5:
                if color_hs == '♥':
                    if is1SA_Pa:    
                        return ('2♦', 'jacoby')
                    if is2SA_openingPa:
                        return ('3♦', 'jacoby-2sa')
                if color_hs == '♠':
                    if is1SA_Pa:
                        return ('2♥', 'jacoby')
                    if is2SA_openingPa:
                        return ('3♥', 'jacoby-2sa')
            # Stayman
            if points >= 8:   
                if highest_series == 4:
                    return ('2♣', 'stayman')
        
        elif points == 8 or points == 9:
            return ('2SA', '1SA-2SA')

        elif points >= 10:
            return ('3SA', '1SA-2SA')

        else: 
            return ('pass', '1SA-pass')

    # Answering to Jacoby and Stayman
    if isStayman(current_bidding):
        if color_hs == '♥':
            return ('2♥', 'answer_to_stayman_colors')
        if color_hs == '♠':
            return ('2♠', 'answer_to_stayman_colors')
        if color_hs != '♠' and color_hs != '♥':
            return ('2♦', 'answer_to_stayman_nocolors')

    if isOpStayman(current_bidding):
        if points > 10:
            if highest_series == '♣':
                return ('X', 'OpStayman')
        return ('pass', 'OpStaymanPass')

    if isPaJacobyDs(current_bidding):
        return ('2♥', 'AnswerJacoby')
    if isPaJacobyHs(current_bidding):
        return ('2♠', 'AnswerJacoby')

    if isOpJacobyDs(current_bidding):
        if color_hs == '♦':
            if highest_series > 5:
                return ('X', 'OpJacoby')

    if isOpJacobyHs(current_bidding):
        if color_hs == '♥':
            if highest_series > 5:
                return ('X', 'OpJacoby')    

    # Answering -X
    if isNX_Ms(current_bidding):
        if harten >= 4:
            if schoppen >= 4:
                return ('X', 'NXMs')
            else:
                return 'pass'

    if isNX_hs(current_bidding):
        if harten >= 4:
            return ('X', 'NXHs')

    # Answering to random bid partner
    if is2Cs_open(current_bidding):
        if points > 8:
            if highest_series >= 5:
                return ('2' + color_hs, '2Cs-2x')
            if points > 10:
                return '2SA'
        else:
            return ('2♦', '2Cs-2Ds')

    if is2Cs_pass_2Ds_pass(current_bidding):
        if points >= 22:
            return '2SA'
        else:
            return '2' + color_hs

    if is2Cs_pass_2Hs_pass(current_bidding):
        if color_hs == '♠':
            pass

    if isAnswerPa(current_bidding):
        if points > 5:
            bid = '1' + color_hs
            if biddingIsAllowed(current_bidding, bid):
                return '1' + color_hs
            else:
                return '1SA'

    if is1x_pass_1x_pass(current_bidding):
        if points <= 14:
            return '1SA'
        else: 
            return '2' + secondhighest_series

    if is1x_pass_1SA_pass(current_bidding):
        if points < 14:
            return 'pass'
        return '2' + secondhighest_series

    if is1x_pass_2x_pass_same(current_bidding):
        if points < 14:
            return 'pass'
        elif points > 14 and points < 18:
            return '2' + color_hs
        else:
            return '4' + color_hs

    if is1x_pass_3x_pass_same(current_bidding):
        if points <= 13:
            return 'pass'
        if points > 14:
            return '4' + color_hs 

    if is1x_pass_4x_pass_same(current_bidding):
        return 'pass'   

    if is1x(current_bidding):
        if points > 4:
            bid = '1' + highest_series

            if biddingIsAllowed(current_bidding, bid):
                return bid

            elif secondhighest_series >= 4:  
                bid2 = '1' + secondhighest_series
                if biddingIsAllowed(current_bidding, bid2):
                    return bid2

            else:
                return '1SA'


                
            
        


    return "i'm sorry, BidBud doesn't know this yet, but he keeps learning!, i reccomend pass"            

