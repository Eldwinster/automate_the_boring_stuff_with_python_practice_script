#!/usr/bin/env python3
import sys, time

# TODO test with différentes board
# TODO add main function

test_this_chess_board = {'1h': 'bking',
                         '6c': 'wqueen',
                         '7c': 'wqueen',
                         '2g': 'bbishop',
                         '5h': 'bqueen',
                         '3e': 'wking'}

CHESS_PIECES = ['king',
                'queen',
                'bishop',
                'knight',
                'rook',
                'pawn']

CHESS_BOARD = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
               'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
               'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
               'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
               'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
               'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
               'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
               'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8',
               ]

CHESS_PIECES_COUNT_PER_PLAYER = {'king': 1,
                                 'queen': 1,
                                 'bishop': 2,
                                 'knight': 2,
                                 'rook': 2,
                                 'pawn': 8}

# Add color to chess pieces
# I forgot why I create this..
# Si ! il faut que je check si les couleurs sont bonnes. gnere si chaque key commence bien par soit 'w', soit 'b'.
# def colorChessPieces(color):
#     for index, item in enumerate(CHESS_PIECES):
#         coloredItem = color + item
#         CHESS_PIECES[index] = coloredItem
#     return CHESS_PIECES

# Remove color from a player piece
def removeColorChessPiece(string):
    colorless = string[1:]
    return colorless

# Remove pieces from key name in dictionary
# def removeColorChessPieces(dictionary):
#     colorless_dictionary = {}
#     for key in dictionary.keys():
#         colorless = removeColorChessPiece(key)
#         colorless_dictionary

# Count how many pieces each player have on the board
def chessPiecesToCount(boardToTest):
    whitePiecesCount = {}
    blackPiecesCount = {}
    for value in boardToTest.values():
        blackOrWhite = value[0]
        if blackOrWhite == 'w':
            value = removeColorChessPiece(value)
            whitePiecesCount.setdefault(value, 0)
            whitePiecesCount[value] = whitePiecesCount[value] + 1
        elif blackOrWhite == 'b':
            value = removeColorChessPiece(value)
            blackPiecesCount.setdefault(value, 0)
            blackPiecesCount[value] = blackPiecesCount[value] + 1
        else:
            print(value)
    return whitePiecesCount, blackPiecesCount

def extractBoardFromTuple(tupleToFragrement):
    for item in tupleToFragrement:
        return item

transformedBoard = extractBoardFromTuple(chessPiecesToCount(test_this_chess_board))

# Check correct name used
def checkCorrectPiecesName(boardToTest):
    boardToTest = transformedBoard
    for key in boardToTest.keys():
        if key in CHESS_PIECES_COUNT_PER_PLAYER.keys():
            continue
        else:
            print(f"Error: Incorrect name used for a piece -> {key}")
    print("Chess pieces name OK.")

# Check correct number of pieces is present on the board
def checkCorrectPiecesNumber(boardToTest):
    boardToTest = transformedBoard
    for key in CHESS_PIECES_COUNT_PER_PLAYER.keys():
        if key in CHESS_PIECES_COUNT_PER_PLAYER.keys():
            testValue = boardToTest.get(key)
            compaValue = CHESS_PIECES_COUNT_PER_PLAYER.get(key)
            # Otherwise I get the following error:
            # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
            # solved thanks to:
            # https://stackoverflow.com/questions/3930188/how-to-convert-nonetype-to-int-or-string
            if int(testValue or 0) <= int(compaValue or 0):
                continue
            else:
                print(f"Error: Incorrect number of pieces detected -> {testValue} {key}")
    print("Chess pieces number OK.")

# Check pieces position on the board
def checkPiecesPosition(boardToTest):
    for key in boardToTest.keys():
        result = any(key in CHESS_BOARD for key in CHESS_BOARD)
        # print(str(bool(result)))
        if result:
            continue
        else:
            print(f"Error: Incorrect piece position -> {key}")
    print("Chess pieces all inbound.")

COUNTING = chessPiecesToCount(test_this_chess_board)
checkCorrectPiecesName(COUNTING)
checkCorrectPiecesNumber(COUNTING)
checkPiecesPosition(test_this_chess_board)
