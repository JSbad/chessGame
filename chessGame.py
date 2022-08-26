# use for printing 8x8 matrix
positions=[[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]]

# initialise all white pieces with starting positions
whiteArmy = {'wp1':[6,0],'wp2':[6,1],'wp3':[6,2],'wp4':[6,3],'wp5':[6,4],'wp6':[6,5],'wp7':[6,6],'wp8':[6,7],
              "wr1": [7,0], "wr2": [7,7],"wk1": [7,1], "wk2": [7,6], "wb1": [7,2], "wb2": [7,5], "wking": [7,4], "wqueen": [7,3]}

# initialise all black pieces with starting positions
blackArmy = {'bp1':[1,0],'bp2':[1,1],'bp3':[1,2],'bp4':[1,3],'bp5':[1,4],'bp6':[1,5],'bp7':[1,6],'bp8':[1,7],
              'br1':[0,0],'br2':[0,7], 'bk1':[0,1],'bk2':[0,6], 'bb1':[0,2],'bb2':[0,5], 'bking':[0,4],'bqueen':[0,3]}

# for logic purposes
whitePawns = ['wp1','wp2','wp3','wp4','wp5','wp6','wp7','wp8']
whiteRooks = ['wr1','wr2']
whiteKnights = ['wk1','wk2']
whiteBishops = ['wb1','wb2']
whiteKing = 'wking'
whiteQueen = 'wqueen'
blackPawns = ['bp1','bp2','bp3','bp4','bp5','bp6','bp7','bp8']
blackRooks = ['br1','br2']
blackKnights = ['bk1','bk2']
blackBishops = ['bb1','bb2']
blackKing = 'bking'
blackQueen = 'bqueen'

# get chess piece by value for killing
def get_key(dict, val):
    for key, value in dict.items():
        if val == value:
            return key

# a compact display function
def display():
    for i in range(len(positions)):
        for j in range(8):
            if whiteArmy['wp1'] == [i, j]:
                print("\u2659 1", end='\t')
            elif whiteArmy['wp2'] == [i, j]:
                print('\u2659 2', end='\t')
            elif whiteArmy['wp3'] == [i, j]:
                print('\u2659 3', end='\t')
            elif whiteArmy['wp4'] == [i, j]:
                print('\u2659 4', end='\t')
            elif whiteArmy['wp5'] == [i, j]:
                print('\u2659 5', end='\t')
            elif whiteArmy['wp6'] == [i, j]:
                print('\u2659 6', end='\t')
            elif whiteArmy['wp7'] == [i, j]:
                print('\u2659 7', end='\t')
            elif whiteArmy['wp8'] == [i, j]:
                print('\u2659 8', end='\t')
            elif whiteArmy['wr1'] == [i, j]:
                print('\u2656 1', end='\t')
            elif whiteArmy['wr2'] == [i, j]:
                print('\u2656 2', end='\t')
            elif whiteArmy['wk1'] == [i, j]:
                print('\u2658 1', end='\t')
            elif whiteArmy['wk2'] == [i, j]:
                print('\u2658 2', end='\t')
            elif whiteArmy['wb1'] == [i, j]:
                print('\u2657 1', end='\t')
            elif whiteArmy['wb2'] == [i, j]:
                print('\u2657 2', end='\t')
            elif whiteArmy['wking'] == [i, j]:
                print('  \u2654  ', end='\t')
            elif whiteArmy['wqueen'] == [i, j]:
                print('  \u2655  ', end='\t')
            elif blackArmy['bp1'] == [i, j]:
                print('\u265F 1', end='\t')
            elif blackArmy['bp2'] == [i, j]:
                print('\u265F 2', end='\t')
            elif blackArmy['bp3'] == [i, j]:
                print('\u265F 3', end='\t')
            elif blackArmy['bp4'] == [i, j]:
                print('\u265F 4', end='\t')
            elif blackArmy['bp5'] == [i, j]:
                print('\u265F 5', end='\t')
            elif blackArmy['bp6'] == [i, j]:
                print('\u265F 6', end='\t')
            elif blackArmy['bp7'] == [i, j]:
                print('\u265F 7', end='\t')
            elif blackArmy['bp8'] == [i, j]:
                print('\u265F 8', end='\t')
            elif blackArmy['br1'] == [i, j]:
                print('\u265C 1', end='\t')
            elif blackArmy['br2'] == [i, j]:
                print('\u265C 2', end='\t')
            elif blackArmy['bk1'] == [i, j]:
                print('\u265E 1', end='\t')
            elif blackArmy['bk2'] == [i, j]:
                print('\u265E 2', end='\t')
            elif blackArmy['bb1'] == [i, j]:
                print('\u265D 1', end='\t')
            elif blackArmy['bb2'] == [i, j]:
                print('\u265D 2', end='\t')
            elif blackArmy['bking'] == [i, j]:
                print('  \u265A  ', end='\t')
            elif blackArmy['bqueen'] == [i, j]:
                print('  \u265B  ', end='\t')
            else:
                print('----', end='\t')
        print()

def moveW(ele):
    currentFigure = ele
    # white pawn movement and kills
    if currentFigure in whitePawns:
        checkPos = [whiteArmy[currentFigure][0] - 1, whiteArmy[currentFigure][1]]  # check desired move of the figure
        # check diagonals for kill opportunities
        checkKillLeft = [whiteArmy[currentFigure][0] - 1, whiteArmy[currentFigure][1] - 1]
        checkKillRight = [(whiteArmy[currentFigure][0]) - 1, (whiteArmy[currentFigure][1]) + 1]
        if checkPos[0] >= 0 and checkPos not in whiteArmy.values():  # check if out of bounds or in front of another white piece
            # handle optional killing
            if checkKillRight in blackArmy.values():
                enemy = str(get_key(blackArmy,checkKillRight))  # get key of the enemy that is at the destination
                ch = input(f'you can kill {enemy}, do it? y/n')
                if ch == 'y':
                    #kill and move pawn diagonally
                    whiteArmy[currentFigure] = checkKillRight
                    blackArmy[enemy] = None
                else:
                    whiteArmy[currentFigure][0] -= 1
            elif checkKillLeft in blackArmy.values():
                enemy = str(get_key(blackArmy,checkKillLeft))
                ch = input(f'you can kill {enemy}, do it? y/n')
                if ch == 'y':
                    whiteArmy[currentFigure] = checkKillLeft
                    blackArmy[enemy] = None
                else:
                    whiteArmy[currentFigure][0] -= 1
            else:
                whiteArmy[currentFigure][0] -= 1
        # allow to kill even if in front of enemy, but not move forward
        elif checkPos in blackArmy.values():
            if checkKillRight in blackArmy.values():
                enemy = str(get_key(blackArmy,checkKillRight))
                ch = input(f'you can kill {enemy}, do it? y/n')
                if ch == 'y':
                    whiteArmy[currentFigure] = checkKillRight
                    blackArmy[enemy] = None
                else:
                    print('illegal move')
            elif checkKillLeft in blackArmy.values():
                enemy = str(get_key(blackArmy,checkKillLeft))
                ch = input(f'you can kill {enemy}, do it? y/n')
                if ch == 'y':
                    whiteArmy[currentFigure] = checkKillLeft
                    blackArmy[enemy] = None
                else:
                    print('illegal move')
        else:
            print('illegal move')
    # white rook movement and kills
    elif currentFigure in whiteRooks:
        move = input('choose vertical or horizontal v/h')
        if move == 'v':
            ch = input('up or down? u/d')
            if ch == 'u':
                dist = int(input('enter number of fields'))
                checkPos = [(whiteArmy[currentFigure][0]) - dist,
                            whiteArmy[currentFigure][1]]  # translate appropriate coordinates
                if checkPos in blackArmy.values():
                    enemy = str(get_key(blackArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        #kill and move rook
                        whiteArmy[currentFigure] = checkPos
                        blackArmy[enemy] = None
                        #out of bounds or in front of friendly piece
                elif checkPos in whiteArmy.values() or checkPos[0] < 0:
                    print('illegal move')
                else:
                    whiteArmy[currentFigure] = checkPos
                    print(checkPos)
            elif ch == 'd':
                dist = int(input('enter number of fields'))
                checkPos = [(whiteArmy[currentFigure][0]) + dist, whiteArmy[currentFigure][1]]
                if checkPos in blackArmy.values():
                    enemy = str(get_key(blackArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        whiteArmy[currentFigure] = checkPos
                        blackArmy[enemy] = None
                elif checkPos not in whiteArmy.values() and checkPos[0] <= 7:
                    whiteArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            else:
                print('invalid input')
        elif move == 'h':
            ch = input('right or left r/l')
            if ch == 'r':
                dist = int(input('enter number of moves'))
                checkPos = [whiteArmy[currentFigure][0], (whiteArmy[currentFigure][1]) + dist]
                if checkPos in blackArmy.values():
                    enemy = str(get_key(blackArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        whiteArmy[currentFigure] = checkPos
                        blackArmy[enemy] = None
                elif checkPos not in whiteArmy.values() and checkPos[1] <= 7:
                    whiteArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            elif ch == 'l':
                dist = int(input('enter number of moves'))
                checkPos = [whiteArmy[currentFigure][0], (whiteArmy[currentFigure][1]) - dist]
                if checkPos in blackArmy.values():
                    enemy = str(get_key(blackArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        whiteArmy[currentFigure] = checkPos
                        blackArmy[enemy] = None
                elif checkPos not in whiteArmy.values() and checkPos[1] >= 0:
                    whiteArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            else:
                print('invalid input')
        else:
            print('invalid input')
    elif currentFigure in whiteBishops:
        move = input('choose up or down u/d')
        if move == 'u':
            ch = input('right or left r/l')
            if ch == 'r':
                dist = int(input('enter number of fields'))
                checkPos = [whiteArmy[currentFigure][0] - dist, (whiteArmy[currentFigure][1]) + dist] # diagonal movement shift
                if checkPos in blackArmy.values():
                    enemy = str(get_key(blackArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        whiteArmy[currentFigure] = checkPos
                        blackArmy[enemy] = None
                elif checkPos not in whiteArmy.values() and checkPos[0] >= 0 and checkPos[1] <= 7:
                    whiteArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            elif ch == 'l':
                dist = int(input('enter number of fields'))
                checkPos = [whiteArmy[currentFigure][0] - dist, (whiteArmy[currentFigure][1]) - dist]
                if checkPos in blackArmy.values():
                    enemy = str(get_key(blackArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        whiteArmy[currentFigure] = checkPos
                        blackArmy[enemy] = None
                elif checkPos not in whiteArmy.values() and checkPos[0] >= 0 and checkPos[1] >= 0:
                    whiteArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            else:
                print('invalid input')
        elif move == 'd':
            ch = input('right or left r/l')
            if ch == 'r':
                dist = int(input('enter number of fields'))
                checkPos = [whiteArmy[currentFigure][0] + dist, (whiteArmy[currentFigure][1]) + dist]
                if checkPos in blackArmy.values():
                    enemy = str(get_key(blackArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        whiteArmy[currentFigure] = checkPos
                        blackArmy[enemy] = None
                elif checkPos not in whiteArmy.values() and checkPos[0] <= 7 and checkPos[1] <= 7:
                    whiteArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            elif ch == 'l':
                dist = int(input('enter number of fields'))
                checkPos = [whiteArmy[currentFigure][0] + dist, (whiteArmy[currentFigure][1]) - dist]
                if checkPos in blackArmy.values():
                    enemy = str(get_key(blackArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        whiteArmy[currentFigure] = checkPos
                        blackArmy[enemy] = None
                elif checkPos not in whiteArmy.values() and checkPos[0] <= 7 and checkPos[1] >= 0:
                    whiteArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            else:
                print('invalid input')
        else:
            print('invalid input')
    elif currentFigure in whiteKnights:
        move = int(input('1 Two vertical one horizontal 2 Two horizontal one vertical')) # L-like movement
        if move == 1:
            ch = input('up or down u/d')
            if ch == 'u':
                ch2 = input('left or right l/r')
                if ch2 == 'l':
                    checkPos = [(whiteArmy[currentFigure][0]) - 2, (whiteArmy[currentFigure][1]) - 1]
                    if checkPos in blackArmy.values():
                        enemy = str(get_key(blackArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            whiteArmy[currentFigure] = checkPos
                            blackArmy[enemy] = None
                    elif checkPos not in whiteArmy.values() and checkPos[0] >= 0 and checkPos[1] >= 0:
                        whiteArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                elif ch2 == 'r':
                    checkPos = [(whiteArmy[currentFigure][0]) - 2, (whiteArmy[currentFigure][1]) + 1]
                    if checkPos in blackArmy.values():
                        enemy = str(get_key(blackArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            whiteArmy[currentFigure] = checkPos
                            blackArmy[enemy] = None
                    elif checkPos not in whiteArmy.values() and checkPos[0] >= 0 and checkPos[1] <= 7:
                        whiteArmy[currentFigure] = checkPos
                else:
                    print('invalid input')
            elif ch == 'd':
                if ch2 == 'l':
                    checkPos = [(whiteArmy[currentFigure][0]) + 2, (whiteArmy[currentFigure][1]) - 1]
                    if checkPos in blackArmy.values():
                        enemy = str(get_key(blackArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            whiteArmy[currentFigure] = checkPos
                            blackArmy[enemy] = None
                    elif checkPos not in whiteArmy.values() and checkPos[0] <= 7 and checkPos[1] >= 0:
                        whiteArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                elif ch2 == 'r':
                    checkPos = [(whiteArmy[currentFigure][0]) + 2, (whiteArmy[currentFigure][1]) + 1]
                    if checkPos in blackArmy.values():
                        enemy = str(get_key(blackArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            whiteArmy[currentFigure] = checkPos
                            blackArmy[enemy] = None
                    elif checkPos not in whiteArmy.values() and checkPos[0] <= 7 and checkPos[1] <= 7:
                        whiteArmy[currentFigure] = checkPos
                else:
                    print('invalid input')
            else:
                print('invalid input')
        elif move == '2':
            ch = input('left or right l/r')
            if ch == 'l':
                ch2 = input('up or down u/d')
                if ch2 == 'u':
                    checkPos = [(whiteArmy[currentFigure][0]) - 1, (whiteArmy[currentFigure][1]) - 2]
                    if checkPos in blackArmy.values():
                        enemy = str(get_key(blackArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            whiteArmy[currentFigure] = checkPos
                            blackArmy[enemy] = None
                    elif checkPos not in whiteArmy.values() and checkPos[0] >= 0 and checkPos[1] >= 0:
                        whiteArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                elif ch2 == 'd':
                    checkPos = [(whiteArmy[currentFigure][0]) + 1, (whiteArmy[currentFigure][1]) - 2]
                    if checkPos in blackArmy.values():
                        enemy = str(get_key(blackArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            whiteArmy[currentFigure] = checkPos
                            blackArmy[enemy] = None
                    elif checkPos not in whiteArmy.values() and checkPos[0] <= 7 and checkPos[1] >= 0:
                        whiteArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                else:
                    print('invalid input')
            elif ch == 'r':
                ch2 = input('up or down u/d')
                if ch2 == 'u':
                    checkPos = [(whiteArmy[currentFigure][0]) - 1, (whiteArmy[currentFigure][1]) + 2]
                    if checkPos in blackArmy.values():
                        enemy = str(get_key(blackArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            whiteArmy[currentFigure] = checkPos
                            blackArmy[enemy] = None
                    elif checkPos not in whiteArmy.values() and checkPos[0] >= 0 and checkPos[1] <= 7:
                        whiteArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                elif ch2 == 'd':
                    checkPos = [(whiteArmy[currentFigure][0]) + 1, (whiteArmy[currentFigure][1]) + 2]
                    if checkPos in blackArmy.values():
                        enemy = str(get_key(blackArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            whiteArmy[currentFigure] = checkPos
                            blackArmy[enemy] = None
                    elif checkPos not in whiteArmy.values() and checkPos[0] <= 7 and checkPos[1] <= 7:
                        whiteArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                else:
                    print('invalid input')
            else:
                print('invalid input')
        else:
            print('invalid input')
    elif currentFigure == whiteQueen: # Queen implements all the movements of rook and bishop
        move = input('vertical horizontal or diagonal v/h/d')
        if move == 'v':
            ch = input('up or down u/d')
            if ch == 'u':
                dist = int(input('enter number of fields'))
                checkPos = [(whiteArmy[currentFigure][0]) - dist,
                            whiteArmy[currentFigure][1]]
                if checkPos in blackArmy.values():
                    enemy = str(get_key(blackArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        whiteArmy[currentFigure] = checkPos
                        blackArmy[enemy] = None
                elif checkPos in whiteArmy.values() or checkPos[0] < 0:
                    print('illegal move')
                else:
                    whiteArmy[currentFigure] = checkPos
                    print(checkPos)
            elif ch == 'd':
                dist = int(input('enter number of fields'))
                checkPos = [(whiteArmy[currentFigure][0]) + dist, whiteArmy[currentFigure][1]]
                if checkPos in blackArmy.values():
                    enemy = str(get_key(blackArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        whiteArmy[currentFigure] = checkPos
                        blackArmy[enemy] = None
                elif checkPos not in whiteArmy.values() and checkPos[0] <= 7:
                    whiteArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            else:
                print('invalid input')
        elif move == 'h':
            ch = input('right or left r/l')
            if ch == 'r':
                dist = int(input('enter number of moves'))
                checkPos = [whiteArmy[currentFigure][0], (whiteArmy[currentFigure][1]) + dist]
                if checkPos in blackArmy.values():
                    enemy = str(get_key(blackArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        whiteArmy[currentFigure] = checkPos
                        blackArmy[enemy] = None
                elif checkPos not in whiteArmy.values() and checkPos[1] <= 7:
                    whiteArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            elif ch == 'l':
                dist = int(input('enter number of moves'))
                checkPos = [whiteArmy[currentFigure][0], (whiteArmy[currentFigure][1]) - dist]
                if checkPos in blackArmy.values():
                    enemy = str(get_key(blackArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        whiteArmy[currentFigure] = checkPos
                        blackArmy[enemy] = None
                elif checkPos not in whiteArmy.values() and checkPos[1] >= 0:
                    whiteArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            else:
                print('invalid input')
        elif move == 'd':
            ch = input('choose up or down u/d')
            if ch == 'u':
                ch2 = input('right or left r/l')
                if ch2 == 'r':
                    dist = int(input('enter number of fields'))
                    checkPos = [whiteArmy[currentFigure][0] - dist, (whiteArmy[currentFigure][1]) + dist]
                    if checkPos in blackArmy.values():
                        enemy = str(get_key(blackArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            whiteArmy[currentFigure] = checkPos
                            blackArmy[enemy] = None
                    elif checkPos not in whiteArmy.values() and checkPos[0] >= 0 and checkPos[1] <= 7:
                        whiteArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                elif ch2 == 'l':
                    dist = int(input('enter number of fields'))
                    checkPos = [whiteArmy[currentFigure][0] - dist, (whiteArmy[currentFigure][1]) - dist]
                    if checkPos in blackArmy.values():
                        enemy = str(get_key(blackArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            whiteArmy[currentFigure] = checkPos
                            blackArmy[enemy] = None
                    elif checkPos not in whiteArmy.values() and checkPos[0] >= 0 and checkPos[1] >= 0:
                        whiteArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                else:
                    print('invalid input')
            elif ch == 'd':
                ch = input('right or left r/l')
                if ch == 'r':
                    dist = int(input('enter number of fields'))
                    checkPos = [whiteArmy[currentFigure][0] + dist, (whiteArmy[currentFigure][1]) + dist]
                    if checkPos in blackArmy.values():
                        enemy = str(get_key(blackArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            whiteArmy[currentFigure] = checkPos
                            blackArmy[enemy] = None
                    elif checkPos not in whiteArmy.values() and checkPos[0] <= 7 and checkPos[1] <= 7:
                        whiteArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                elif ch == 'l':
                    dist = int(input('enter number of fields'))
                    checkPos = [whiteArmy[currentFigure][0] + dist, (whiteArmy[currentFigure][1]) - dist]
                    if checkPos in blackArmy.values():
                        enemy = str(get_key(blackArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            whiteArmy[currentFigure] = checkPos
                            blackArmy[enemy] = None
                    elif checkPos not in whiteArmy.values() and checkPos[0] <= 7 and checkPos[1] >= 0:
                        whiteArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                else:
                    print('invalid input')
            else:
                print('invalid input')
        else:
            print('invalid input')
    elif currentFigure == whiteKing: # Same as queen but only 1 field
        move = input('vertical horizontal or diagonal v/h/d')
        if move == 'v':
            ch = input('up or down u/d')
            if ch == 'u':
                checkPos = [(whiteArmy[currentFigure][0]) - 1,
                            whiteArmy[currentFigure][1]] 
                if checkPos in blackArmy.values():
                    enemy = str(get_key(blackArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        whiteArmy[currentFigure] = checkPos
                        blackArmy[enemy] = None
                elif checkPos in whiteArmy.values() or checkPos[0] < 0:
                    print('illegal move')
                else:
                    whiteArmy[currentFigure] = checkPos
                    print(checkPos)
            elif ch == 'd':
                checkPos = [(whiteArmy[currentFigure][0]) + 1, whiteArmy[currentFigure][1]]
                if checkPos in blackArmy.values():
                    enemy = str(get_key(blackArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        whiteArmy[currentFigure] = checkPos
                        blackArmy[enemy] = None
                elif checkPos not in whiteArmy.values() and checkPos[0] <= 7:
                    whiteArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            else:
                print('invalid input')
        elif move == 'h':
            ch = input('right or left r/l')
            if ch == 'r':
                checkPos = [whiteArmy[currentFigure][0], (whiteArmy[currentFigure][1]) + 1]
                if checkPos in blackArmy.values():
                    enemy = str(get_key(blackArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        whiteArmy[currentFigure] = checkPos
                        blackArmy[enemy] = None
                elif checkPos not in whiteArmy.values() and checkPos[1] <= 7:
                    whiteArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            elif ch == 'l':
                checkPos = [whiteArmy[currentFigure][0], (whiteArmy[currentFigure][1]) - 1]
                if checkPos in blackArmy.values():
                    enemy = str(get_key(blackArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        whiteArmy[currentFigure] = checkPos
                        blackArmy[enemy] = None
                elif checkPos not in whiteArmy.values() and checkPos[1] >= 0:
                    whiteArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            else:
                print('invalid input')
        elif move == 'd':
            ch = input('choose up or down u/d')
            if ch == 'u':
                ch2 = input('right or left r/l')
                if ch2 == 'r':
                    checkPos = [whiteArmy[currentFigure][0] - 1, (whiteArmy[currentFigure][1]) + 1]
                    if checkPos in blackArmy.values():
                        enemy = str(get_key(blackArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            whiteArmy[currentFigure] = checkPos
                            blackArmy[enemy] = None
                    elif checkPos not in whiteArmy.values() and checkPos[0] >= 0 and checkPos[1] <= 7:
                        whiteArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                elif ch == 'l':
                    checkPos = [whiteArmy[currentFigure][0] - 1, (whiteArmy[currentFigure][1]) - 1]
                    if checkPos in blackArmy.values():
                        enemy = str(get_key(blackArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            whiteArmy[currentFigure] = checkPos
                            blackArmy[enemy] = None
                    elif checkPos not in whiteArmy.values() and checkPos[0] >= 0 and checkPos[1] >= 0:
                        whiteArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                else:
                    print('invalid output')
            elif ch == 'd':
                ch = input('right or left r/l')
                if ch == 'r':
                    checkPos = [whiteArmy[currentFigure][0] + 1, (whiteArmy[currentFigure][1]) + 1]
                    if checkPos in blackArmy.values():
                        enemy = str(get_key(blackArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            whiteArmy[currentFigure] = checkPos
                            blackArmy[enemy] = None
                    elif checkPos not in whiteArmy.values() and checkPos[0] <= 7 and checkPos[1] <= 7:
                        whiteArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                elif ch == 'l':
                    checkPos = [whiteArmy[currentFigure][0] + 1, (whiteArmy[currentFigure][1]) - 1]
                    if checkPos in blackArmy.values():
                        enemy = str(get_key(blackArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            whiteArmy[currentFigure] = checkPos
                            blackArmy[enemy] = None
                    elif checkPos not in whiteArmy.values() and checkPos[0] <= 7 and checkPos[1] >= 0:
                        whiteArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                else:
                    print('invalid input')
            else:
                print('invalid input')
        else:
            print('invalid input')


def moveB(ele):
    currentFigure = ele
    if currentFigure in blackPawns:
        checkPos = [blackArmy[currentFigure][0]+1,blackArmy[currentFigure][1]]
        checkKillLeft = [blackArmy[currentFigure][0]+1,blackArmy[currentFigure][1]-1]
        checkKillRight = [(blackArmy[currentFigure][0])+1,(blackArmy[currentFigure][1])+1]
        if checkPos[0]>=0 and checkPos not in blackArmy.values():
            if checkKillRight in whiteArmy.values():
                enemy = str(get_key(whiteArmy,checkKillRight))
                ch = input(f'you can kill {enemy}, do it? y/n')
                if ch == 'y':
                    blackArmy[currentFigure] = checkKillRight
                    whiteArmy[enemy] = None
                else:
                    blackArmy[currentFigure][0]+=1
            elif checkKillLeft in whiteArmy.values():
                enemy = str(get_key(whiteArmy,checkKillLeft))
                ch = input(f'you can kill {enemy}, do it? y/n')
                if ch == 'y':
                    blackArmy[currentFigure] = checkKillLeft
                    whiteArmy[enemy] = None
                else:
                    blackArmy[currentFigure][0]+=1
            else:
                blackArmy[currentFigure][0]+=1
        elif checkPos in whiteArmy.values():
            if checkKillRight in whiteArmy.values():
                enemy = str(get_key(whiteArmy,checkKillRight))
                ch = input(f'you can kill {enemy}, do it? y/n')
                if ch == 'y':
                    blackArmy[currentFigure] = checkKillRight
                    whiteArmy[enemy] = None
                else:
                    print('illegal move')
            elif checkKillLeft in whiteArmy.values():
                enemy = str(get_key(whiteArmy,checkKillLeft))
                ch = input(f'you can kill {enemy}, do it? y/n')
                if ch == 'y':
                    blackArmy[currentFigure] = checkKillLeft
                    whiteArmy[enemy] = None
                else:
                    print('illegal move')
        else:
            print('illegal move')
    elif currentFigure in blackRooks:
        move = input('choose vertical or horizontal v/h')
        if move == 'v':
            ch = input('up or down? u/d')
            if ch == 'u':
                dist = int(input('enter number of moves'))
                checkPos = [(blackArmy[currentFigure][0])-dist,blackArmy[currentFigure][1]]
                if checkPos in blackArmy.values():
                    enemy = str(get_key(whiteArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        blackArmy[currentFigure] = checkPos
                        whiteArmy[enemy] = None
                elif checkPos in blackArmy.values() or checkPos[0]<0:
                    print('illegal move')
                else:
                    blackArmy[currentFigure] = checkPos
                    print(checkPos)
            elif ch == 'd':
                dist = int(input('enter number of moves'))
                checkPos = [(blackArmy[currentFigure][0])+dist,blackArmy[currentFigure][1]]
                if checkPos in whiteArmy.values():
                    enemy = str(get_key(whiteArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        blackArmy[currentFigure] = checkPos
                        whiteArmy[enemy] = None
                elif checkPos not in blackArmy.values() and checkPos[0]<=7:
                    blackArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            else:
                print('invalid input')
        elif move == 'h':
            ch = input('right or left r/l')
            if ch == 'r':
                dist = int(input('enter number of moves'))
                checkPos = [blackArmy[currentFigure][0],(blackArmy[currentFigure][1])+dist]
                if checkPos in whiteArmy.values():
                    enemy = str(get_key(whiteArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        blackArmy[currentFigure] = checkPos
                        whiteArmy[enemy] = None
                elif checkPos not in blackArmy.values() and checkPos[0]<=7:
                    blackArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            elif ch == 'l':
                dist = int(input('enter number of moves'))
                checkPos = [blackArmy[currentFigure][0],(blackArmy[currentFigure][1])-dist]
                if checkPos in whiteArmy.values():
                    enemy = str(get_key(whiteArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        blackArmy[currentFigure] = checkPos
                        whiteArmy[enemy] = None
                elif checkPos not in blackArmy.values() and checkPos[0] >= 0 :
                    blackArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            else:
                print('invalid input')
    elif currentFigure in blackBishops:
        move = input('choose up or down u/d')
        if move == 'u':
            ch = input('right or left r/l')
            if ch == 'r':
                dist = int(input('enter number of fields'))
                checkPos = [blackArmy[currentFigure][0]-dist,(blackArmy[currentFigure][1])+dist]
                if checkPos in whiteArmy.values():
                    enemy = str(get_key(whiteArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        blackArmy[currentFigure] = checkPos
                        whiteArmy[enemy] = None
                elif checkPos not in blackArmy.values() and checkPos[0]>=0 and checkPos[1]<=7:
                    blackArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            elif ch == 'l':
                dist = int(input('enter number of fields'))
                checkPos = [blackArmy[currentFigure][0]-dist,(blackArmy[currentFigure][1])-dist]
                if checkPos in whiteArmy.values():
                    enemy = str(get_key(whiteArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        blackArmy[currentFigure] = checkPos
                        whiteArmy[enemy] = None
                elif checkPos not in blackArmy.values() and checkPos[0]>=0 and checkPos[1]>=0:
                    blackArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            else:
                print('invalid input')
        elif move == 'd':
            ch = input('right or left r/l')
            if ch == 'r':
                dist = int(input('enter number of fields'))
                checkPos = [blackArmy[currentFigure][0]+dist,(blackArmy[currentFigure][1])+dist]
                if checkPos in whiteArmy.values():
                    enemy = str(get_key(whiteArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        blackArmy[currentFigure] = checkPos
                        whiteArmy[enemy] = None
                elif checkPos not in blackArmy.values() and checkPos[0]<=7 and checkPos[1]<=7:
                    blackArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            elif ch == 'l':
                dist = int(input('enter number of fields'))
                checkPos = [blackArmy[currentFigure][0]+dist,(blackArmy[currentFigure][1])-dist]
                if checkPos in whiteArmy.values():
                    enemy = str(get_key(whiteArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        blackArmy[currentFigure] = checkPos
                        whiteArmy[enemy] = None
                elif checkPos not in blackArmy.values() and checkPos[0]<=7 and checkPos[1]>=0:
                    blackArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            else:
                print('invalid input')
        else:
            print('invalid input')
    elif currentFigure in blackKnights:
        move = int(input('1 Two vertical one horizontal 2 Two horizontal one vertical'))
        if move == 1:
            ch1 = input('up or down u/d')
            ch2 = input('left or right l/r')
            if ch1 == 'u':
                if ch2 == 'l':
                    checkPos = [(blackArmy[currentFigure][0]) - 2, (blackArmy[currentFigure][1]) - 1]
                    if checkPos in whiteArmy.values():
                        enemy = str(get_key(whiteArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            blackArmy[currentFigure] = checkPos
                            whiteArmy[enemy] = None
                    elif checkPos not in blackArmy.values() and checkPos[0] >= 0 and checkPos[1] >= 0:
                        blackArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                elif ch2 == 'r':
                    checkPos = [(blackArmy[currentFigure][0]) - 2, (blackArmy[currentFigure][1]) + 1]
                    if checkPos in whiteArmy.values():
                        enemy = str(get_key(whiteArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            blackArmy[currentFigure] = checkPos
                            whiteArmy[enemy] = None
                    elif checkPos not in blackArmy.values() and checkPos[0] >= 0 and checkPos[1] <= 7:
                        blackArmy[currentFigure] = checkPos
                else:
                    print('invalid input')
            elif ch1 == 'd':
                if ch2 == 'l':
                    checkPos = [(blackArmy[currentFigure][0]) + 2, (blackArmy[currentFigure][1]) - 1]
                    if checkPos in whiteArmy.values():
                        enemy = str(get_key(whiteArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            blackArmy[currentFigure] = checkPos
                            whiteArmy[enemy] = None
                    elif checkPos not in blackArmy.values() and checkPos[0] <= 7 and checkPos[1] >= 0:
                        blackArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                elif ch2 == 'r':
                    checkPos = [(blackArmy[currentFigure][0]) + 2, (blackArmy[currentFigure][1]) + 1]
                    if checkPos in whiteArmy.values():
                        enemy = str(get_key(whiteArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            blackArmy[currentFigure] = checkPos
                            whiteArmy[enemy] = None
                    elif checkPos not in blackArmy.values() and checkPos[0] <= 7 and checkPos[1] <= 7:
                        blackArmy[currentFigure] = checkPos
                else:
                    print('invalid input')
            else:
                print('invalid input')
        elif move == '2':
            ch = input('left or right l/r')
            if ch == 'l':
                ch2 = input('up or down u/d')
                if ch2 == 'u':
                    checkPos = [(blackArmy[currentFigure][0]) - 1, (blackArmy[currentFigure][1]) - 2]
                    if checkPos in whiteArmy.values():
                        enemy = str(get_key(whiteArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            blackArmy[currentFigure] = checkPos
                            whiteArmy[enemy] = None
                    elif checkPos not in blackArmy.values() and checkPos[0] >= 0 and checkPos[1] >= 0:
                        blackArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                elif ch2 == 'd':
                    checkPos = [(blackArmy[currentFigure][0]) + 1, (blackArmy[currentFigure][1]) - 2]
                    if checkPos in whiteArmy.values():
                        enemy = str(get_key(whiteArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            blackArmy[currentFigure] = checkPos
                            whiteArmy[enemy] = None
                    elif checkPos not in blackArmy.values() and checkPos[0] <= 7 and checkPos[1] >= 0:
                        blackArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                else:
                    print('invalid input')
            elif ch == 'r':
                ch2 = input('up or down u/d')
                if ch2 == 'u':
                    checkPos = [(blackArmy[currentFigure][0]) - 1, (blackArmy[currentFigure][1]) + 2]
                    if checkPos in whiteArmy.values():
                        enemy = str(get_key(whiteArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            blackArmy[currentFigure] = checkPos
                            whiteArmy[enemy] = None
                    elif checkPos not in blackArmy.values() and checkPos[0] >= 0 and checkPos[1] <= 7:
                        blackArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                elif ch2 == 'd':
                    checkPos = [(blackArmy[currentFigure][0]) + 1, (blackArmy[currentFigure][1]) + 2]
                    if checkPos in whiteArmy.values():
                        enemy = str(get_key(whiteArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            blackArmy[currentFigure] = checkPos
                            whiteArmy[enemy] = None
                    elif checkPos not in blackArmy.values() and checkPos[0] <= 7 and checkPos[1] <= 7:
                        blackArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                else:
                    print('invalid input')
            else:
                print('invalid input')
        else:
            print('invalid input')
    elif currentFigure == blackQueen:
        move = input('vertical horizontal or diagonal v/h/d')
        if move == 'v':
            ch == input('up or down u/d')
            if ch == 'u':
                dist = int(input('enter number of fields'))
                checkPos = [(blackArmy[currentFigure][0]) - dist,
                            blackArmy[currentFigure][1]]
                if checkPos in whiteArmy.values():
                    enemy = str(get_key(whiteArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        blackArmy[currentFigure] = checkPos
                        whiteArmy[enemy] = None
                elif checkPos in blackArmy.values() or checkPos[0] < 0:
                    print('illegal move')
                else:
                    blackArmy[currentFigure] = checkPos
                    print(checkPos)
            elif ch == 'd':
                dist = int(input('enter number of fields'))
                checkPos = [(blackArmy[currentFigure][0]) + dist, blackArmy[currentFigure][1]]
                if checkPos in blackArmy.values():
                    enemy = str(get_key(whiteArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        blackArmy[currentFigure] = checkPos
                        whiteArmy[enemy] = None
                elif checkPos not in blackArmy.values() and checkPos[0] <= 7:
                    blackArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            else:
                print('invalid input')
        elif move == 'h':
            ch = input('right or left r/l')
            if ch == 'r':
                dist = int(input('enter number of moves'))
                checkPos = [blackArmy[currentFigure][0], (blackArmy[currentFigure][1]) + dist]
                if checkPos in whiteArmy.values():
                    enemy = str(get_key(whiteArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        blackArmy[currentFigure] = checkPos
                        whiteArmy[enemy] = None
                elif checkPos not in blackArmy.values() and checkPos[1] <= 7:
                    blackArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            elif ch == 'l':
                dist = int(input('enter number of moves'))
                checkPos = [blackArmy[currentFigure][0], (blackArmy[currentFigure][1]) - dist]
                if checkPos in whiteArmy.values():
                    enemy = str(get_key(whiteArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        blackArmy[currentFigure] = checkPos
                        whiteArmy[enemy] = None
                elif checkPos not in blackArmy.values() and checkPos[1] >= 0:
                    blackArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            else:
                print('invalid input')
        elif move == 'd':
            ch = input('choose up or down u/d')
            if ch == 'u':
                ch2 = input('right or left r/l')
                if ch2 == 'r':
                    dist = int(input('enter number of fields'))
                    checkPos = [blackArmy[currentFigure][0] - dist, (blackArmy[currentFigure][1]) + dist]
                    if checkPos in whiteArmy.values():
                        enemy = str(get_key(whiteArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            blackArmy[currentFigure] = checkPos
                            whiteArmy[enemy] = None
                    elif checkPos not in blackArmy.values() and checkPos[0] >= 0 and checkPos[1] <= 7:
                        blackArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                elif ch == 'l':
                    dist = int(input('enter number of fields'))
                    checkPos = [blackArmy[currentFigure][0] - dist, (blackArmy[currentFigure][1]) - dist]
                    if checkPos in whiteArmy.values():
                        enemy = str(get_key(whiteArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            blackArmy[currentFigure] = checkPos
                            whiteArmy[enemy] = None
                    elif checkPos not in blackArmy.values() and checkPos[0] >= 0 and checkPos[1] >= 0:
                        blackArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                else:
                    print('invalid output')
            elif ch == 'd':
                ch = input('right or left r/l')
                if ch == 'r':
                    dist = int(input('enter number of fields'))
                    checkPos = [blackArmy[currentFigure][0] + dist, (blackArmy[currentFigure][1]) + dist]
                    if checkPos in whiteArmy.values():
                        enemy = str(get_key(whiteArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            blackArmy[currentFigure] = checkPos
                            whiteArmy[enemy] = None
                    elif checkPos not in blackArmy.values() and checkPos[0] <= 7 and checkPos[1] <= 7:
                        blackArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                elif ch == 'l':
                    dist = int(input('enter number of fields'))
                    checkPos = [blackArmy[currentFigure][0] + dist, (blackArmy[currentFigure][1]) - dist]
                    if checkPos in whiteArmy.values():
                        enemy = str(get_key(whiteArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            blackArmy[currentFigure] = checkPos
                            whiteArmy[enemy] = None
                    elif checkPos not in blackArmy.values() and checkPos[0] <= 7 and checkPos[1] >= 0:
                        blackArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                else:
                    print('invalid input')
            else:
                print('invalid input')
        else:
            print('invalid input')
    elif currentFigure == blackKing:
        move = input('vertical horizontal or diagonal v/h/d')
        if move == 'v':
            ch == input('up or down u/d')
            if ch == 'u':
                checkPos = [(blackArmy[currentFigure][0]) - 1,
                            blackArmy[currentFigure][1]]
                if checkPos in whiteArmy.values():
                    enemy = str(get_key(whiteArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        blackArmy[currentFigure] = checkPos
                        whiteArmy[enemy] = None
                elif checkPos in blackArmy.values() or checkPos[0] < 0:
                    print('illegal move')
                else:
                    blackArmy[currentFigure] = checkPos
                    print(checkPos)
            elif ch == 'd':
                checkPos = [(blackArmy[currentFigure][0]) + 1, blackArmy[currentFigure][1]]
                if checkPos in whiteArmy.values():
                    enemy = str(get_key(whiteArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        blackArmy[currentFigure] = checkPos
                        whiteArmy[enemy] = None
                elif checkPos not in blackArmy.values() and checkPos[0] <= 7:
                    blackArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            else:
                print('invalid input')
        elif move == 'h':
            ch = input('right or left r/l')
            if ch == 'r':
                checkPos = [blackArmy[currentFigure][0], (blackArmy[currentFigure][1]) + 1]
                if checkPos in whiteArmy.values():
                    enemy = str(get_key(whiteArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        blackArmy[currentFigure] = checkPos
                        whiteArmy[enemy] = None
                elif checkPos not in blackArmy.values() and checkPos[1] <= 7:
                    blackArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            elif ch == 'l':
                checkPos = [blackArmy[currentFigure][0], (blackArmy[currentFigure][1]) - 1]
                if checkPos in whiteArmy.values():
                    enemy = str(get_key(whiteArmy,checkPos))
                    ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                    if ch == 'y':
                        blackArmy[currentFigure] = checkPos
                        whiteArmy[enemy] = None
                elif checkPos not in blackArmy.values() and checkPos[1] >= 0:
                    blackArmy[currentFigure] = checkPos
                else:
                    print('illegal move')
            else:
                print('invalid input')
        elif move == 'd':
            ch = input('choose up or down u/d')
            if ch == 'u':
                ch2 = input('right or left r/l')
                if ch2 == 'r':
                    checkPos = [blackArmy[currentFigure][0] - 1, (blackArmy[currentFigure][1]) + 1]
                    if checkPos in whiteArmy.values():
                        enemy = str(get_key(whiteArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            blackArmy[currentFigure] = checkPos
                            whiteArmy[enemy] = None
                    elif checkPos not in blackArmy.values() and checkPos[0] >= 0 and checkPos[1] <= 7:
                        blackArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                elif ch == 'l':
                    checkPos = [blackArmy[currentFigure][0] - 1, (blackArmy[currentFigure][1]) - 1]
                    if checkPos in whiteArmy.values():
                        enemy = str(get_key(whiteArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            blackArmy[currentFigure] = checkPos
                            whiteArmy[enemy] = None
                    elif checkPos not in blackArmy.values() and checkPos[0] >= 0 and checkPos[1] >= 0:
                        blackArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                else:
                    print('invalid output')
            elif ch == 'd':
                ch = input('right or left r/l')
                if ch == 'r':
                    checkPos = [blackArmy[currentFigure][0] + 1, (blackArmy[currentFigure][1]) + 1]
                    if checkPos in whiteArmy.values():
                        enemy = str(get_key(whiteArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            blackArmy[currentFigure] = checkPos
                            whiteArmy[enemy] = None
                    elif checkPos not in blackArmy.values() and checkPos[0] <= 7 and checkPos[1] <= 7:
                        blackArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                elif ch == 'l':
                    checkPos = [blackArmy[currentFigure][0] + 1, (blackArmy[currentFigure][1]) - 1]
                    if checkPos in whiteArmy.values():
                        enemy = str(get_key(whiteArmy,checkPos))
                        ch = input(f'you can kill {enemy}, do it? y/n (n will cancel the move)')
                        if ch == 'y':
                            blackArmy[currentFigure] = checkPos
                            whiteArmy[enemy] = None
                    elif checkPos not in blackArmy.values() and checkPos[0] <= 7 and checkPos[1] >= 0:
                        blackArmy[currentFigure] = checkPos
                    else:
                        print('illegal move')
                else:
                    print('invalid input')
            else:
                print('invalid input')
        else:
            print('invalid input')




def playGame():
    turn = 0
    while True:
        display()
        # handle player turns
        if (turn % 2 == 0):
            player = 'White'
        else:
            player = 'Black'
        print("------------------------------------------------")
        print("{}'s turn".format(player))
        ele = input('Choose a piece to move: ')
        if (turn % 2 == 0):
            if ele in whitePawns and whiteArmy[ele][0] == 6: # handle first move of pawns
                dist = int(input('Enter how many spaces you want to move (1/2):'))
                if dist == 1:
                    checkPos = [whiteArmy[ele][0] - 1, whiteArmy[ele]]
                    if checkPos not in blackArmy.values():
                        whiteArmy[ele][0] -= 1
                    else:
                        print("You cannot make a move.")
                elif dist == 2:
                    checkPos = [whiteArmy[ele][0] - 2, whiteArmy[ele]]
                    if checkPos not in blackArmy.values():
                        whiteArmy[ele][0] -= 2
                else:
                    print("Invalid input.")
            else:
                moveW(ele)
        else:
            if ele in blackPawns and blackArmy[ele][0] == 1:
                dist = int(input('Enter how many spaces you want to move (1/2):'))
                if dist == 1:
                    checkPos = [blackArmy[ele][0], blackArmy[ele]]
                    if checkPos not in blackArmy.values():
                        blackArmy[ele][0] = blackArmy[ele][0]
                    else:
                        print("You cannot make a move.")
                elif dist == 2:
                    checkPos = [blackArmy[ele][0] + 1, blackArmy[ele]]
                    if checkPos not in blackArmy.values():
                        blackArmy[ele][0] += 1
                else:
                    print("Invalid input.")
            moveB(ele)
        turn += 1
def intro():
    print("Want to be the next Nepomniachtchi?")
    print("-----------------------------------")
    start = int(input("Enter 0 to start"))
    if start == 0:
        print("-----------------------------------")
        print("\n||We really hope you don't expect to become the next Nepomniachtchi, we are only joking.||")
    else:
        print("\nWe said 0, dummy. Anyway, just play already.")
    print("\n--------LIST OF NAMES--------")
    print("\nWHITE PAWN NAMES: wp1 --> wp8")
    print("\nWHITE ROOK NAMES:  wr1 | wr2 ")
    print("\nWHITE BISHOP NAMES:  wb1 | wrb2 ")
    print("\nWHITE KNIGHT NAMES:  wk1 | wk2 ")
    print("\nWHITE QUEEN NAME:  wqueen ")
    print("\nWHITE KING NAME:  wking ")

    print("\nBLACK PAWN NAMES: bp1 --> bp8")
    print("\nBLACK ROOK NAMES:  br1 | br2 ")
    print("\nBLACK BISHOP NAMES:  bb1 | bb2 ")
    print("\nBLACK KNIGHT NAMES:  bk1 | bk2 ")
    print("\nBLACK QUEEN NAME:  bqueen ")
    print("\nBLACK KING NAME:  bking ")
    print("\n\n--->WHITE STARTS<---\n\n")

intro()
playGame()