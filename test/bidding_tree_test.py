from bidding_tree import bidding_tree

def testYouOpen():
    cb = []
    bt = bidding_tree(cb)
    points = 12
    highest = 5
    lowest = 0 
    color = '♥'
    assert bt.you_open(cb, points, highest, lowest, color) == "1♥"

def testYouOpenPass():
    cb = []
    bt = bidding_tree(cb)
    points = 11
    highest = 6
    lowest = 0
    color = '♠'
    assert bt.you_open(cb, points, highest, lowest, color) == 'pass'

def testYouOpenPreemtif():
    cb = []
    bt = bidding_tree(cb)
    points = 8
    highest = 7
    lowest = 0
    color = '♠'
    assert bt.you_open(cb, points, highest, lowest, color) == '3♠'

def testYouOpen1SA():
    cb = []
    bt = bidding_tree(cb)
    points = 16
    highest = 5
    lowest = 2
    color = '♠'
    assert bt.you_open(cb, points, highest, lowest, color) == '1SA'

def testYouOpen1clubs():
    cb = []
    bt = bidding_tree(cb)
    points = 13
    highest = 4
    lowest = 0
    color = '♠'
    assert bt.you_open(cb, points, highest, lowest, color) == '1♣'

def testYouOpen2SA():
    cb = []
    bt = bidding_tree(cb)
    points = 21
    highest = 5
    lowest = 2
    color = '♥'
    assert bt.you_open(cb, points, highest, lowest, color) == '2SA'

def testYouOpen2clubsWithPoints():
    cb = []
    bt = bidding_tree(cb)
    points = 25
    highest = 0
    lowest = 0
    color = '♥'
    assert bt.you_open(cb, points, highest, lowest, color) == '2♣'

def testYouOpen2clubs():
    cb = []
    bt = bidding_tree(cb)
    points = 16
    highest = 7
    lowest = 0
    color = '♥'
    assert bt.you_open(cb, points, highest, lowest, color) == '2♣'

def testYouOpen2hearts():
    cb = ['1SA', 'pass']
    bt = bidding_tree(cb)
    points = 0
    highest = 5
    lowest = 0
    color = '♠'
    assert bt.you_open(cb, points, highest, lowest, color) == '2♥'

def testYouOpen2SA():
    cb = ['1SA', 'pass']
    bt = bidding_tree(cb)
    points = 8
    highest = 4
    lowest = 0
    color = '♥'
    assert bt.you_open(cb, points, highest, lowest, color) == '2SA'
    