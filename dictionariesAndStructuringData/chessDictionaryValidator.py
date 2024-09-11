#!/usr/bin/env python3

import sys, time

test_this_chess_board = {'1h': 'bking',
                         '6c': 'wqueen',
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

# TODO effectue la verification que les pièces sont bien sur l'échéquié

CHESS_PIECES_COUNT_PER_PLAYER = {'king_count': 1,
                                 'queen_count': 1,
                                 'bishop_count': 2,
                                 'knight_count': 2,
                                 'rook_count': 2,
                                 'pawn_count': 8}

# Add color to chess pieces
def colorChessPieces(color):
    for index, item in enumerate(CHESS_PIECES):
        coloredItem = color + item
        CHESS_PIECES[index] = coloredItem
    return CHESS_PIECES

def removeColorChessPieces(string):
    colorless = string[1:]
    return colorless

# Count how many pieces each player have on the board
def chessPiecesCount(boardToTest):
    whitePiecesCount = {}
    blackPiecesCount = {}
    for value in boardToTest.values():
        blackOrWhite = value[0]
        if blackOrWhite == 'w':
            whitePiecesCount.setdefault(value, 0)
            whitePiecesCount[value] = whitePiecesCount[value] + 1
        elif blackOrWhite == 'b':
            blackPiecesCount.setdefault(value, 0)
            blackPiecesCount[value] = blackPiecesCount[value] + 1
        else:
            print(value)
    return whitePiecesCount, blackPiecesCount

COUNTING = chessPiecesCount(test_this_chess_board)

# TODO Ajoute une fonction qui vérifie que le compte est bon pour chaque joueurs

print(COUNTING)
