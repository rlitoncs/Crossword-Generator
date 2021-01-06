#Ralph Liton
blank = ' '
board = [[blank] * 20 for i in range(20)]


def printboard(board):
    for i in range(21):  # the numbers 0-9 above border
        if i == 0:
            print(' ', end='')
        else:
            print((i - 1) % 10, end='')
    print()

    for i in range(22):
        if i == 0 or i == 21:
            print(' ', end='')  # the underscores for top border
        else:
            print('_', end='')
    print()

    for i in range(20):
        for j in range(22):
            if j == 0 or j == 21:
                print('|', end='')  # vertical lines for side border

            else:
                print(board[i][j - 1], end='')

        print(i)  # number on the side of border

    for i in range(22):
        if i == 0 or i == 21:  # the underscores at the bottom
            print(' ', end='')
        else:
            print('_', end='')
    print()

    for i in range(21):
        if i == 0:
            print(' ', end='')  # the numbers 0-9 above border
        else:
            print((i - 1) % 10, end='')

    print()

def addFirstWord(board, word):
    midWord = (len(word)) // 2
    index = 0
    if len(word) > 20:
        print('Error:', '"' + word + "'", 'reaches outside of grid')            # if the length of the word is less than 20; reaches out of grid
        return False

    elif len(word) % 2 == 1:
        for i in range(10 - midWord - 1, 10 + midWord):
            board[10][i] = word[index]
            index+= 1
    elif len(word) % 2 == 0:
        for i in range(10 - midWord, 10 + midWord):
            board[10][i] = word[index]
            index += 1
    return True

def checkVertical(board, word, row, col):
    blank = ' '
    length_ofVertical = len(word)
    can_word_be_added = False

    if length_ofVertical > 20 - row:
        return can_word_be_added

    for x in range(len(word)):
        if word[x] == board[row + x][col]:
            can_word_be_added= True

        if board[row + x][col] == blank:
            if board[row + x][col - 1] != blank or board[row + x][col + 1] != blank or board[row + x][col] != blank:
                return can_word_be_added
            else:
                continue

        elif word[x] != board[row + x][col]:
            return can_word_be_added
    return can_word_be_added


def checkHorizontal(board,word,row,col):
    blank = ' '
    length_ofHorizontal = len(word)
    can_word_be_added = False

    if length_ofHorizontal > 20 - col:
        return can_word_be_added


    for x in range(len(word)):
        if word[x] == board[row][col + x]:
            can_word_be_added= True

        if board[row][col + x] == blank:
            if board[row - 1][col + x] != blank or board[row + 1][col + x] != blank or board[row][col + x] != blank:
                return can_word_be_added
            else:
                continue

        elif word[x] != board[row][col + x]:
            return can_word_be_added
    return can_word_be_added

def addVertical(board, word):
    find_lettermatch = 0
    for row in range(len(board) - 1):
        for col in range(len(board) - 1):
            if checkVertical(board, word, row, col):
                find_lettermatch +=1                            #Checks how many times a letter matches with a word

    if find_lettermatch == 0:                                   # If find_lettermatch == 0, if the len(word) > 20 then it will reach out of grid
        if len(word) > 20 :                                     # else if the len(word) < 20, then it has no matching letter
            print(word, 'reaches outside of grid')
        else:
            print(word, 'has no matching letter')
        return


    for row in range(len(board) - 1):
        for col in range(len(board) - 1):
            if checkVertical(board,word,row,col):
                for x in range(len(word)):
                    for x in range(len(word)):
                        if board[row + x][col - 1] == ' ' and board[row + x][col + 1] == ' ' and board[row + x][col] == ' ':
                            checkagain = True

                        elif board[row + x][col] == word[x]:
                            checkagain = True

                        else:
                            checkagain = False
                            print(word, 'has illegal adjacencies')
                            return checkagain

                    if checkagain:
                        for x in range(len(word)):
                            if board[row + x][col - 1] == ' ' and board[row + x][col + 1] == ' ' and board[row + x][col] == ' ':
                                board[row + x][col] = word[x]

                            elif board[row + x][col] == word[x]:
                                board[row + x][col] = word[x]

                    return checkagain



def addHorizontal(board, word):
    find_lettermatch = 0
    for row in range(len(board) -1 ):
        for col in range(len(board) - 1):
            if checkHorizontal(board, word, row, col):
                find_lettermatch +=1                       # Checks how many times a letter matches with a word

    if find_lettermatch == 0:                             # If find_lettermatch == 0, if the len(word) > 20 then it will reach out of grid
        if len(word) > 20:                                # else if the len(word) < 20, then it has no matching letters
            print(word, 'reaches outside of grid.')
        else:
            print(word, 'has no matching letter')
        return

    for row in range(len(board) - 1):
        for col in range(len(board) - 1):
            if checkHorizontal(board, word, row, col):
                for x in range(len(word)):
                    if board[row - 1][col + x] == ' ' and board[row + 1][col + x] == ' ' and board[row][col + x] == ' ':
                        checkagain = True


                    elif board[row][col + x] == word[x]:
                        checkagain = True

                    else:
                        checkagain = False
                        print(word, 'has illegal adjacencies')
                        return checkagain

                if checkagain:
                    for x in range(len(word)):
                        if board[row - 1][col + x] == ' ' and board[row + 1][col + x] == ' ' and board[row][col + x] == ' ':
                            board[row][col + x] = word[x]

                        elif board[row][col + x] == word[x]:
                            board[row][col + x] = word[x]
                return checkagain



def crossword(L):
    for i in range(len(L)):
        if L[0] == L[i]:
            addFirstWord(board, L[i])

        elif i % 2 == 1:
            addVertical(board, L[i])

        else:
            addHorizontal(board, L[i])


    print()
L1 = ['hippopotamus', 'playing', 'adjacent', 'everyday', 'everything', 'boal', 'but', 'nick', 'kink', 'going', 'over'] #All words are added
L2 = ['hippopotamus', 'playing', 'zoo', 'everyday', 'everything', 'boal', 'but', 'nick', 'kink', 'going', 'over']   #illegal adjacencies & no matching letter
L3 = ['hippopotamus', 'playing', 'adjacent', 'everyday', 'everything', 'boal', 'but', 'nick', 'kink', 'going', 'over', 'qwewqiwqjeiwqjiscjiaicwi'] #reaches outside of grid
L4 = ['spectacular', 'furniture', 'crumble', 'timothy', 'yawn', 'yellow', 'electron', 'supercalifrag', 'blue']

crossword(L1)
printboard(board)




