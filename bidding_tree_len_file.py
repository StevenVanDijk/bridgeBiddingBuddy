from bidding import biddingIsAllowed 

class bidding_tree():
    _ = False # ✔
    pass_ = False # ✔
    pass_pass_ = False # ✔
    pass_bid_ = False # ❌ 
    pass_1SA_rightOp = False # ✔
    _1SA_rightOp = False # ✔
    pass_1SA_Pa = False # ❌
    PaStayman = False # ✔
    OpStayman = False # ✔
    PaJacobyDs = False # ❌
    PaJacobyHs = False 
    OpJacobyDs = False # ❌
    OpJacobyHs = False 
    _1SA_Pa = False # ✔
    Pa_pass = False # ✔

    def __init__(self, current_bidding):
        #pass
        if len(current_bidding) == 0: 
            self._ = True

        if len(current_bidding) == 1:
            if current_bidding[0] == 'pass': 
                self.pass_ = True

        if len(current_bidding) == 2:   
            if current_bidding[0] == 'pass' and current_bidding[1] == 'pass': 
                self.pass_pass_ = True

        #1SA
        #opponents
        if current_bidding[0] == '1SA':
            if current_bidding[1] == 'pass':
                
        
        if len(current_bidding) == 1:
            if current_bidding[0] == '1SA':
                self._1SA_rightOp = True

        if len(current_bidding) == 2:
            if current_bidding[0] == 'pass' and current_bidding[1] == '1SA':
                self.pass_1SA_rightOp = True
        
        #partner
        if len(current_bidding) >= 1:
            
            if current_bidding[0] == '1SA' and current_bidding[1] == 'pass':
                self._1SA_Pa = True

        #answer to Stayman and Jacoby
        if len(current_bidding) >= 3:
            
            if current_bidding[0] == '1SA':
                if current_bidding[2] == '2♣':
                    if current_bidding[3] == 'pass':
                        self.PaStayman = True
                    else:
                        self.OpStayman = True

                if current_bidding[2] == '2♦' or current_bidding[2] == '2♥':
                    if current_bidding[3] == 'pass':
                        if current_bidding[2] == '2♦':
                            self.PaJacobyDs = True
                        if current_bidding[2] == '2♥':
                            self.PaJacobyHs = True
                    else:
                        if current_bidding[2] == '2♦':
                            self.OpJacobyDs = True
                        if current_bidding[2] == '2♥':
                            self.OpJacobyHs = True
                        
         
        
        #answering partner
        if len(current_bidding) >= 2:
            if current_bidding[0] != 'pass' and current_bidding[1] == 'pass':
                self.Pa_pass = True       


    def bids(self, current_bidding, points, highest_series, lowest_series, color_hs):
        # opening
        if self._ == True or self.pass_ == True or self.pass_pass_ == True:
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
        if self._1SA_Pa:
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
        if self.PaStayman == True:
            if color_hs == '♥':
                return '2♥'
            if color_hs == '♠':
                return '2♠'
            if color_hs != '♠' and color_hs != '♥':
                return '2♦'
        
        if self.OpStayman:
            if points > 10:
                if highest_series == '♣':
                    return 'X'
            return 'pass'

        if self.PaJacobyDs:
            return '2♥'
        if self.PaJacobyHs:
            return '2♠'

        if self.OpJacobyDs:
            if color_hs == '♦':
                if highest_series > 5:
                    return 'X'

        if self.OpJacobyHs:
            if color_hs == '♥':
                if highest_series > 5:
                    return 'X'        

        # Answering to random bid partner
        if self.Pa_pass:
            if points > 5:
                bid = '1' + color_hs
                if biddingIsAllowed(current_bidding, bid):
                    return '1' + color_hs
                else:
                    return '1SA'


        return "i'm sorry, BidBud doesn't know this yet, but he keeps learning!"            
