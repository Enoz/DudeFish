import chess
import math
import copy

piece_values = {
	chess.PAWN: 1,
	chess.BISHOP: 3,
	chess.KNIGHT: 3,
	chess.ROOK: 5,
	chess.QUEEN: 9,
	chess.KING: 20,
}
	

def toend(board):
	res = board.result(claim_draw=True)
	if res == '1-0':
		return math.inf
	elif res == '0-1':
		return -math.inf
	else:
		return 0

def material(board):

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

def _numMoves(board, color):
	board = copy.deepcopy(board)
	if board.turn != color:
		board.push(chess.Move.null())
	return board.legal_moves.count()

def mobility(board):
	tot = 0
	tot += _numMoves(board, chess.WHITE) * 0.01
	tot -= _numMoves(board, chess.BLACK) * 0.01
	return tot

def pawn_push(board):

	total = 0

	for square in chess.SQUARES:
		piece = board.piece_at(square)
		if piece != None and piece.piece_type == chess.PAWN:
			pcolor = piece.color
			#more points for being futher up the board
			rank = chess.square_rank(square)
			total = -0.4 #compensate for pawn scoring 1 by default
			if pcolor == chess.BLACK:
				total -= (7-rank) * 0.1
			else:
				total += rank * 0.1
	return total

class Evaluators:

	@staticmethod
	def dudefish(board):
		if board.is_game_over(claim_draw=True):
			return toend(board)
		tot = 0
		tot += material(board)
		tot += mobility(board)
		tot += pawn_push(board)
		return tot
