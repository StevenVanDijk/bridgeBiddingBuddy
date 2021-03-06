from difflib import SequenceMatcher

def passes_are_back(current_bidding):
    count_pass = 0
    for elem in current_bidding:
        if elem == 'pass':
            count_pass += 1
        else: 
            break
    while count_pass > 0:
        current_bidding.append('pass')
        count_pass -= 1

def remove_starting_passes(current_bidding):
    done = False
    while not done:
        if len(current_bidding) >= 1:
            if current_bidding[0] == 'pass':
                current_bidding.remove('pass')
                if len(current_bidding) == 0:
                    done = True
            else:
                done = True
        else: 
            done = True
    return current_bidding

def similar(x, y):
    return SequenceMatcher(None, x, y).ratio()
    
def levelofbid(bid):
    if '1' in bid:
        return '1'
    if '2' in bid:
        return '2'
    if '3' in bid:
        return '3'
    if '4' in bid:
        return '4'
    if '5' in bid:
        return '5'
    if '6' in bid:
        return '6'
    if '7' in bid:
        return '7'   
    
def lastBidIsOps(current_bidding):
    remove_starting_passes(current_bidding)
    if current_bidding[-1] != 'pass': return True
    else:
        if current_bidding[-2] != 'pass': return False
        if current_bidding[-3] != 'pass': return True

#############################################################################

def isStayman(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) >= 3:
        if current_bidding[0] == '1SA':
            if current_bidding[2] == '2♣':
                if current_bidding[3] == 'pass':
                    return True
    return False


def is1SA_NH_Op(current_bidding):
    remove_starting_passes(current_bidding)
    if current_bidding[0] == '1SA':    
        if len(current_bidding) == 1:
            return True
        if len(current_bidding) == 3:
            if current_bidding[1] == 'pass' and current_bidding[2] == 'pass':
                return True
    return False

def isNX_hs(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 2:
            if current_bidding[0] == '1♣' or current_bidding[0] == '1♦':
                if current_bidding[1] == '1♥' or current_bidding[1] == '1♠':
                    return True
    return False

def isNX_Ms(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 2:
            if current_bidding[0] == '1♣' or current_bidding[0] == '1♦':
                if current_bidding[1] == '1♦':
                    return True
    return False


def is1SA_Pa(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 2:
            if current_bidding[0] == '1SA' and current_bidding[1] == 'pass':
                return True
    return False


def isPaStayman(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) >= 3:
        if current_bidding[0] == '1SA':
            if current_bidding[2] == '2♣':
                if current_bidding[3] == 'pass':
                    return True
    return False

def isOpStayman(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 3:
            if current_bidding[0] == '1SA':
                if current_bidding[2] == '2♣':
                    return True
    return False

def isPaJacobyDs(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 4:
        if current_bidding[0] == '1SA':
            if current_bidding[3] == 'pass':
                if current_bidding[2] == '2♦':
                    return True
    return False

def isPaJacobyHs(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 4:
        if current_bidding[0] == '1SA':
            if current_bidding[3] == 'pass':
                if current_bidding[2] == '2♥':
                    return True
    return False

def isOpJacobyDs(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 3:
        if current_bidding[0] == '1SA':
            if current_bidding[2] == '2♦':
                return True
    return False

def isOpJacobyHs(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 3:
        if current_bidding[0] == '1SA':
            if current_bidding[2] == '2♥':
                return True
    return False

def is2Cs_open(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 2:
        if current_bidding[0] == '2♣':
            if current_bidding[1] == 'pass':
                return True
    return False

def is2Cs_pass_2Ds_pass(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 4:
        if current_bidding[0] == '2♣' and current_bidding[2] == '2♦':
            if current_bidding[1]  == 'pass' and current_bidding[3] == 'pass':
                return True
    return False

def is2Cs_pass_2Hs_pass(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 4:
        if current_bidding[0] == '2♣' and current_bidding[2] == '2♥':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass':
                return True
    return False

def is2Cs_pass_2Ss_pass(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) > 4:
        if current_bidding[0] == '2♣' and current_bidding[2] == '2♠':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass':
                return True
    return False

def is2Cs_pass_2SA_pass(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 4:
        if current_bidding[0] == '2♣' and current_bidding[2] == '2SA':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass':
                return True
    return False

def isAnswerPa(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 2:
        if current_bidding[0] != 'pass' and current_bidding[1] == 'pass':
            return True
    return False


def is1x_pass_1x_pass(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 4:
        if levelofbid(current_bidding[0]) == '1':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass':
                if levelofbid(current_bidding[2]) == '1':
                    return True
    return False


def is1x_pass_1x_pass(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 4:
        if levelofbid(current_bidding[0]) == '1':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass':
                if levelofbid(current_bidding[2]) == '1':
                    return True
    return False


def is1x_pass_2x_pass(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 4:
        if similar(current_bidding[0], current_bidding[2]) == 0.5:
            return False
        if levelofbid(current_bidding[0]) == '1':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass':
                if levelofbid(current_bidding[2]) == '2':
                    return True
    return False


def is1x_pass_3x_pass(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 4:
        if similar(current_bidding[0], current_bidding[2]) == 0.5:
            return False
        if levelofbid(current_bidding[0]) == '1':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass':
                if levelofbid(current_bidding[2]) == '3':
                    return True
    return False


def is1x_pass_4x_pass(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 4:
        if similar(current_bidding[0], current_bidding[2]) == 0.5:
            return False
        if levelofbid(current_bidding[0]) == '1':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass':
                if levelofbid(current_bidding[2]) == '4':
                    return True
    return False

    

def is1x_pass_1SA_pass(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 4:
        if levelofbid(current_bidding[0]) == '1':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass':
                if current_bidding[2] == '1SA':
                    return True
    return False

def is1x_pass_1SA_pass_3SA_p(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 6:
        if levelofbid(current_bidding[0]) == '1':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass' and current_bidding[5] == 'pass':
                if current_bidding[2] == '1SA':
                    if current_bidding[4] == '3SA':
                        return True
    return False    

def is1x_pass_1SA_pass_2SA_p(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 4:
        if levelofbid(current_bidding[0]) == '1':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass' and current_bidding[5] == 'pass':
                if current_bidding[2] == '1SA':
                    if current_bidding[4] == '2SA':
                        return True
    return False

def is1x_pass_2x_pass_same(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 4:
        if levelofbid(current_bidding[0]) == '1':
            if levelofbid(current_bidding[2]) == '2':
                if similar(current_bidding[0], current_bidding[2]) == 0.5:
                    return True
    return False

def is1x_pass_3x_pass_same(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 4:
        if levelofbid(current_bidding[0]) == '1':
            if levelofbid(current_bidding[2]) == '3':
                if similar(current_bidding[0], current_bidding[2]) == 0.5:
                    return True
    return False

def is1x_pass_4x_pass_same(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 4:
        if levelofbid(current_bidding[0]) == '1':
            if levelofbid(current_bidding[2]) == '4':
                if similar(current_bidding[0], current_bidding[2]) == 0.5:
                    return True 
    return False

def is2SA_openingPa(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 2:
        if current_bidding[0] == '2SA':
            if current_bidding[1] == 'pass':
                return True
    return False

def is1x(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 1:
        if current_bidding[0] != 'pass':
            return True
    return False

def isAnsweringJacoby(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 6:
        if current_bidding[0] == '1SA':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass' and current_bidding[5] == 'pass':
                if current_bidding[2] == '2♦' or current_bidding[2] == '2♥':
                    return True
    return False

def isPotentielRondPass(current_bidding):
    if len(current_bidding) >= 3:
        if current_bidding[0] == 'pass':
            if current_bidding[1] == 'pass':
                if current_bidding[2] == 'pass':
                    return True
    return False

def isAfterJacoby(current_bidding): # You bidded Jacoby, and partner responded
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 6:
        if current_bidding[0] == '1SA':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass' and current_bidding[5] == 'pass':
                if current_bidding[2] == '2♦':
                    if current_bidding[4] == '2♥':
                        return True
                if current_bidding[2] == '2♥':
                    if current_bidding[4] == '2♠':
                        return True
    return False

def isAfterJacobyInviteSA(current_bidding): #Your partner bidded Jacoby and invited to the manch, SA
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 6:
        if current_bidding[0] == '1SA':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass':
                if current_bidding[5] == 'pass' and current_bidding[7] == 'pass':
                    
                    if current_bidding[2] == '2♦':
                        if current_bidding[4] == '2♥':
                            if current_bidding[6] == '2SA':
                                return True
                            
                    if current_bidding[2] == '2♥':
                        if current_bidding[4] == '2♠':
                            if current_bidding[6] == '2SA':
                                return True
    return False

def isAfterJacobyInviteClrHs(current_bidding): #Your partner bidded Jacoby and invited to the manch, ♥
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 6:
        if current_bidding[0] == '1SA':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass':
                if current_bidding[5] == 'pass' and current_bidding[7] == 'pass':
                    
                    if current_bidding[2] == '2♦':
                        if current_bidding[4] == '2♥':
                            if current_bidding[6] == '3♥':
                                return True
                            
                    if current_bidding[2] == '2♥':
                        if current_bidding[4] == '2♠':
                            if current_bidding[6] == '3♠':
                                return False
    return False

def isAfterJacobyInviteClrSs(current_bidding): #Your partner bidded Jacoby and invited to the manch, ♠
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 6:
        if current_bidding[0] == '1SA':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass':
                if current_bidding[5] == 'pass' and current_bidding[7] == 'pass':
                    
                    if current_bidding[2] == '2♦':
                        if current_bidding[4] == '2♥':
                            if current_bidding[6] == '3♥':
                                return False
                            
                    if current_bidding[2] == '2♥':
                        if current_bidding[4] == '2♠':
                            if current_bidding[6] == '3♠':
                                return True
    return False

def isStayman2SAHs(current_bidding): # Partner bidded Stayman and after that 3SA, you bidded 3♥
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 8:
        if current_bidding[0] == '1SA':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass':
                if current_bidding[5] == 'pass' and current_bidding[7] == 'pass':
                    if current_bidding[2] == '2♣':
                        if current_bidding[4] == '2♥':
                            if current_bidding[6] == '2SA':
                                return True
    return False


def isStayman2SASs(current_bidding): # Partner bidded Stayman and after that 3SA, you bidded 2♠
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 8:
        if current_bidding[0] == '1SA':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass':
                if current_bidding[5] == 'pass' and current_bidding[7] == 'pass':
                    if current_bidding[2] == '2♣':
                        if current_bidding[4] == '2♠':
                            if current_bidding[6] == '2SA':
                                return True
    return False

def isStayman2SA(current_bidding): # Partner bidded Stayman and after that 2SA
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 8:
        if current_bidding[0] == '1SA':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass':
                if current_bidding[5] == 'pass' and current_bidding[7] == 'pass':
                    if current_bidding[2] == '2♣':
                        if currrent_bidding[4] == '2♥' or current_bidding[4] == '2♠':
                            if current_bidding[6] == '2SA':
                                return True
    return False

def isStayman3SAHs(current_bidding): # Partner bidded Stayman and after that 3SA, you bidded 3♥
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 8:
        if current_bidding[0] == '1SA':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass':
                if current_bidding[5] == 'pass' and current_bidding[7] == 'pass':
                    if current_bidding[2] == '2♣':
                        if current_bidding[4] == '2♥':
                            if current_bidding[6] == '3SA':
                                return True
    return False

def isStayman3SASs(current_bidding): # Partner bidded Stayman and after that 3SA, you bidded 3♠
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 8:
        if current_bidding[0] == '1SA':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass':
                if current_bidding[5] == 'pass' and current_bidding[7] == 'pass':
                    if current_bidding[2] == '2♣':
                        if current_bidding[4] == '2♠':
                            if current_bidding[6] == '3SA':
                                return True
    return False

def isStayman3SA(current_bidding): # Partner bidded Stayman and after that 3SA
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 8:
        if current_bidding[0] == '1SA':
            if current_bidding[1] == 'pass' and current_bidding[3] == 'pass':
                if current_bidding[5] == 'pass' and current_bidding[7] == 'pass':
                    if current_bidding[2] == '2♣':
                        if current_bidding[4] == '2♥' or current_bidding[4] == '2♠':
                            if current_bidding[6] == '3SA':
                                return True
    return False


def isInfoXPaNoIn(current_bidding): # Information Xdoublet of Partner No Interference
    if isNX_Ms(current_bidding) or isNX_Ms(current_bidding): return False
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 3:
        if current_bidding[0] != 'pass':
            if current_bidding[1] == 'X':
                if current_bidding[2] == 'pass' or current_bidding[2] == 'XX':
                    return True
    return False

def isInfoXPaIn(current_bidding): # Information Xdoublet of Partner, Interfered
    if isNX_Ms(current_bidding) or isNX_Ms(current_bidding): return False
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 3:
        if current_bidding[0] != 'pass':
            if current_bidding[1] == 'X':
                if current_bidding[2] != 'pass' and current_bidding[2] != 'XX':
                    return True
    return False

def isOpInL1(current_bidding): # Oppenents Interference Level1
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 2:
        if current_bidding[0] != 'pass':
            if current_bidding[1] != 'pass' and levelofbid(current_bidding[1]) == '1':
                return True
    return False

def isOpInL1PaP(current_bidding):  # Oppenents Interference Level1 Partner Pass
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 4:
        if current_bidding[0] != 'pass':
            if current_bidding[1] != 'pass' and current_bidding[3] == 'pass':
                if current_bidding[2] == 'pass': 
                    return True 
            if current_bidding[1] == 'pass' and current_bidding[3] != 'pass':
                if current_bidding[2] == 'pass': 
                    return True
    return False

def isOpinL2M(current_bidding):  # Oppenents Interference Level2 or More
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 2:
        if current_bidding[0] != 'pass' and levelofbid(current_bidding[0]) == '1':
            if current_bidding[1] != 'pass' and levelofbid(current_bidding[1]) != '1':
                return True
    return False

def isOpInL2MPaP(current_bidding):  # Oppenents Interference Level1 or More Partner Pass
    remove_starting_passes(current_bidding)
    if len(current_bidding) == 4:
        if current_bidding[0] != 'pass' and levelofbid(current_bidding[0]) == '1':
            if current_bidding[1] != 'pass' and current_bidding[3] == 'pass':
                if levelofbid(current_bidding[1]) != '1':
                    if current_bidding[2] == 'pass': return True 
            if current_bidding[1] == 'pass' and current_bidding[3] != 'pass':
                if levelofbid(current_bidding[3]) != '1':
                    if current_bidding[2] == 'pass': return True
    return False

def levelManch(current_bidding):
    for bid in current_bidding:
        if 'SA' in bid and levelofbid(current_bidding) == '3':
            return '3'
        if '♥' in bid or '♠' in bid and levelofbid(current_bidding) == '4':
            return '4'
        if '♦' in bid or '♣' in bid and levelofbid(current_bidding) == '5':
            return '5'
    return False



def isManchByPartner(current_bidding):
    if current_bidding[-1] != 'pass': return False
    if current_bidding[-2] != 'pass' and levelManch(current_bidding) in ('3', '4', '5'): return True
    return False

        
    