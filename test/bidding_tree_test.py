from bidding_tree import bidding_tree

def testYouOpen():
    cb = []
    bt = bidding_tree(cb)
    points = 12
    highest = 5
    color = '♥'
    assert bt.you_open(cb, points, highest, color) == "1♥"

    cb = []
    bt = bidding_tree(cb)
    points = 11
    highest = 6
    color = '♠'
    assert bt.you_open(cb, points, highest, color) == 'pass'

    cb = []
    bt = bidding_tree(cb)
    points = 8
    highest = 7
    color = '♠'
    assert bt.you_open(cb, points, highest, color) == '3♠'

    cb = []
    bt = bidding_tree(cb)
    points = 16
    highest = 5
    lowest = 2
    color = '♠'
    assert bt.you_open(cb, points, highest, lowest, color) == '1SA'

    cb = []
    bt = bidding_tree(cb)
    points = 13
    highest = 4
    color = '♠'
    assert bt.you_open(cb, points, highest, color) == '1♣'

    cb = []
    bt = bidding_tree(cb)
    points = 21
    highest = 5
    lowest = 2
    assert bt.you_open(cb, points, highest, lowest) == '2SA'

    cb = []
    bt = bidding_tree(cb)
    points = 25
    assert bt.you_open(cb, points,) == '2♣'

    cb = []
    bt = bidding_tree(cb)
    points = 16
    highest = 7
    assert bt.you_open(cb, points, highest) == '2♣'

    cb = ['1SA', 'pass']
    bt = bidding_tree(cb)
    points = 0
    highest = 5
    color = '♠'
    assert bt.you_open(cb, points, highest, color) == '2♥'

    cb = ['1SA', 'pass']
    bt = bidding_tree(cb)
    points = 8
    highest = 4
    assert bt.you_open(cb, points, highest) == '2SA'




