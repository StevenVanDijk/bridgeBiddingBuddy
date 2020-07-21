    _ = False # ✔
    pass_ = False # ✔
    pass_pass_ = False # ✔
    pass_1SA_rightOp = False # ✔
    _1SA_rightOp = False # ✔
    pass_1SA_Pa = False # ❌
    PaStayman = False # ✔
    OpStayman = False # ✔
    PaJacobyDs = False # ✔
    PaJacobyHs = False # ✔
    OpJacobyDs = False # ✔
    OpJacobyHs = False # ✔
    _1SA_Pa = False # ✔
    Pa_pass = False # ✔
    _1x_pass_1SA_pass = False 
    _1x_pass_1x_pass = False # ❌
    _1x_pass_2x_pass = False # ❌
    _1x_pass_3x_pass = False # ❌
    _1x_pass_2x_pass_same = False
    _1x_pass_3x_pass_same = False
    _1x_pass_4x_pass_same = False
    # negatief doublet
    NX_hs = False
    NX_Ms = False 
    _2Cs = False
    _2Cs_pass_2Ds_pass = False
    _2Cs_pass_2Hs_pass = False
    _2Cs_pass_2Ss_pass = False
    _2Cs_pass_2SA_pass = False 
    answerPaStayman = False
    answerPaJAcoby = False

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
                
        count_pass = 0
        done = False

        while not done:
            if len(current_bidding) >= 1:
                if current_bidding[0] == 'pass':
                    current_bidding.remove('pass')
                    count_pass += 1
                    if len(current_bidding) == 0:
                        while count_pass != 0:
                            current_bidding.insert(0, 'pass')
                            count_pass -= 1
                            if count_pass == 0:
                                done = True
                else:
                    done = True
            else: 
                done = True

        #1SA
        #opponents
        if len(current_bidding) >= 2:
            if current_bidding[0] == '1♣' or current_bidding[0] == '1♦':
                if current_bidding[1] == '1♦':
                    self.NX_Ms = True
                if current_bidding[1] == '1♥' or current_bidding[1] == '1♠':
                    self.NX_hs = True                             

        
        if len(current_bidding) == 1:
            if current_bidding[0] == '1SA':
                self._1SA_rightOp = True

        if len(current_bidding) == 2:
            if current_bidding[0] == 'pass' and current_bidding[1] == '1SA':
                self.pass_1SA_rightOp = True
        
        #partner
        if len(current_bidding) == 2:
            if current_bidding[0] == '1SA' and current_bidding[1] == 'pass':
                self._1SA_Pa = True

        #answer to Stayman and Jacoby
        if len(current_bidding) >= 3:
            if current_bidding[0] == '1SA':
                if current_bidding[2] == '2♣':
                    if current_bidding[3] == 'pass':
                        if len(current_bidding) >= 6:
                            self.answerPaStayman
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

        return               
        if current_bidding[0] == '2♣':
            self._2Cs = True
            if len(current_bidding) > 4:
                if current_bidding[1] == 'pass':
                    self._2Cs = False
                    if current_bidding[2] == '2♦':
                        self._2Cs_pass_2Ds_pass = True                        
                    elif current_bidding[2] == '2♥':
                        self._2Cs_pass_2Hs_pass = True
                    elif current_bidding[2] == '2♠':
                        self._2Cs_pass_2Ss_pass = True
                    elif current_bidding[2] == '2SA':
                        self._2Cs_pass_2SA_pass = True
                    else:
                        self._2Cs = True                                          
        
        #answering partner
        if len(current_bidding) >= 2:
            if current_bidding[0] != 'pass' and current_bidding[1] == 'pass':
                self.Pa_pass = True    

        #let's go to the manch!
        if len(current_bidding) >= 4:
            if current_bidding[0] == '1♣' or current_bidding[0] == '1♦' or current_bidding[0] == '1♥' or current_bidding[0] == '1♠' or current_bidding[0] == '1SA':
                if current_bidding[1] == 'pass' and current_bidding[3] == 'pass':
                    if current_bidding[2] == '1SA':
                        self._1x_pass_1SA_pass = True
                    if current_bidding[2] == '1♣' or current_bidding[2] == '1♦' or current_bidding[2] == '1♥' or current_bidding[2] == '1♠':                        
                        self._1x_pass_1x_pass = True
                    if current_bidding[2] == '2♣' or current_bidding[2] == '2♦' or current_bidding[2] == '2♥' or current_bidding[2] == '2♠':
                        self._1x_pass_2x_pass = True
                    if current_bidding[2] == '3♣' or current_bidding[2] == '3♦' or current_bidding[2] == '3♥' or current_bidding[2] == '3♠':
                        self._1x_pass_3x_pass = True      
                               


