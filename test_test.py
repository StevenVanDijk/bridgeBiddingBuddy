count_pass = 0

def passes_are_back(current_bidding):
    while count_pass > 0:
        current_bidding.append('pass')
        count_pass -= 1

def remove_starting_passes(current_bidding):
    current_biddingNP = current_bidding
    done = False
    while not done:
        if len(current_biddingNP) >= 1:
            if current_biddingNP[0] == 'pass':
                current_biddingNP.remove('pass')
                count_pass += 1
                if len(current_biddingNP) == 0:
                    done = True
            else:
                done = True
        else: 
            done = True
    return current_biddingNP

current_bidding = ['pass', 'pass', '1♣', 'pass']

remove_starting_passes(current_bidding)