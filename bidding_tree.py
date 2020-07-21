from bidding import biddingIsAllowed 
from bidding_states import *
from uitleg import *

class bidding_tree():   
    def bids(self, current_bidding, points, schoppen, harten, ruiten, klaver):
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

        remove_starting_passes(current_bidding)
        # opening
        if len(current_bidding) == 0:
            if points >= 12:
                if highest_series <= 5 and lowest_series >= 2:
                    if points >= 15 and points <= 17:
                        return '1SA' 
                    
                    if points >= 20 and points <= 22:
                        return '2SA'            
                
                elif points >= 22 or (points >= 15 and highest_series >= 7):
                    return '2♣'                

                elif highest_series >= 5:
                    return '1' + color_hs

                elif highest_series == 4 and color_hs != '♥' and color_hs != '♠': 
                    return '1' + color_hs
    
                else:
                    return '1♣'

            if points < 12:
                if points <= 10:
                    if highest_series >= 6:
                        if highest_series == 6:
                            return '2' + color_hs
                        if highest_series == 7:
                            return '3' + color_hs
                        if highest_series == 8:
                            return '4' + color_hs

                    else: 
                        if biddingIsAllowed(current_bidding, 'pass'): 
                            return 'pass'

                else:
                    return 'pass'
            else: 
                return 'pass'

        # answering
        # answering to 1SA
        if is1SA_Pa(current_bidding):
            if color_hs == '♥' or color_hs == '♠':
                # Jacoby
                if highest_series >= 5:
                    if color_hs == '♥':
                        return '2♦'
                    if color_hs == '♠':
                        return '2♥'
                # Stayman
                if points >= 8:   
                    if highest_series == 4:
                        return '2♣'
            
            elif points == 8 or points == 9:
                return '2SA'

            elif points >= 10:
                return '3SA'

            else: 
                return 'pass'

        # Answering to Jacoby and Stayman
        if isStayman(current_bidding):
            if color_hs == '♥':
                return '2♥'
            if color_hs == '♠':
                return '2♠'
            if color_hs != '♠' and color_hs != '♥':
                return '2♦'
        
        if isOpStayman(current_bidding):
            if points > 10:
                if highest_series == '♣':
                    return 'X'
            return 'pass'

        if isPaJacobyDs(current_bidding):
            return '2♥'
        if isPaJacobyHs(current_bidding):
            return '2♠'

        if isOpJacobyDs(current_bidding):
            if color_hs == '♦':
                if highest_series > 5:
                    return 'X'

        if isOpJacobyHs(current_bidding):
            if color_hs == '♥':
                if highest_series > 5:
                    return 'X'    

        # Answering -X
        if isNX_Ms(current_bidding):
            if color_hs == '♥':
                return 'if you have 4+ ♠, X. Else: pass'

        if isNX_hs(current_bidding):
            if color_hs == '♥':
                return 'X'

        # Answering to random bid partner
        if is2Cs_open(current_bidding):
            if points > 8:
                if highest_series >= 5:
                    return '2' + color_hs
                if points > 10:
                    return '2SA'

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


        return "i'm sorry, BidBud doesn't know this yet, but he keeps learning!"            

