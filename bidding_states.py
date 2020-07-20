def isStayman(current_bidding):
    if len(current_bidding) >= 3:
        if current_bidding[0] == '1SA':
            if current_bidding[2] == '2♣':
                if current_bidding[3] == 'pass':
                    if len(current_bidding) >= 6:
                        return isAnswerStayman(current_bidding)
                    return True
    return False