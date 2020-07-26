from difflib import SequenceMatcher

def remove_starting_passes(current_bidding):
    count_pass = 0
    done = False
    while not done:
        if len(current_bidding) >= 1:
            if current_bidding[0] == 'pass':
                current_bidding.remove('pass')
                count_pass += 1
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
    if len(current_bidding) >= 3:
        if current_bidding[1] == 'pass':
            if current_bidding[2] != 'pass':
                return False

    if len(current_bidding) == 1:
        if current_bidding[0] == '2♣':
            if current_bidding[1] == 'pass':
                return True
    return False

def is2Cs_pass_2Ds_pass(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) > 4:
        if current_bidding[0] == '2♣':
            if current_bidding[1] == 'pass':
                if current_bidding[2] == '2♦':
                    return True
    return False

def is2Cs_pass_2Hs_pass(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) > 4:
        if current_bidding[0] == '2♣':
            if current_bidding[1] == 'pass':
                if current_bidding[2] == '2♥':
                    return True
    return False

def is2Cs_pass_2Ss_pass(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) > 4:
        if current_bidding[0] == '2♣':
            if current_bidding[1] == 'pass':
                if current_bidding[2] == '2♠':
                    return True
    return False

def is2Cs_pass_2SA_pass(current_bidding):
    remove_starting_passes(current_bidding)
    if len(current_bidding) > 4:
        if current_bidding[0] == '2♣':
            if current_bidding[1] == 'pass':
                if current_bidding[2] == '2SA':
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
        if current_bidding[0] == '2SA' and current_bidding[1] == 'pass':
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
    if len(current_bidding) == 3:
        if current_bidding[0] == 'pass':
            if current_bidding[1] == 'pass':
                if current_bidding[2] == 'pass':
                    return True
    return False
