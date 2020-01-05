import chess
import math

piece_values = {
	chess.PAWN: 1,
	chess.BISHOP: 3,
	chess.KNIGHT: 3,
	chess.ROOK: 5,
	chess.QUEEN: 9,
	chess.KING: 20,
}

def evaluator(board):
	if board.is_game_over(claim_draw=True):
		res = board.result(claim_draw=True)
		if res == '1-0':
			return math.inf
		elif res == '0-1':
			return -math.inf
		else:
			return 0
	
	total = 0
			
	for square in chess.SQUARES:
		piece = board.piece_at(square)
		if piece != None:
			pcolor = piece.color
			ptype = piece.piece_type
			pval = piece_values[ptype]
			if pcolor == chess.BLACK:
				pval = -pval
			total += pval
	return total
