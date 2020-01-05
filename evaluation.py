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

def numMoves(board, color):
	board = copy.deepcopy(board)
	if board.turn != color:
		board.push(chess.Move.null())
	return board.legal_moves.count()

class Evaluators:
	
	@staticmethod
	def pure_material(board):
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
		
	@staticmethod
	def mobility(board):
		tot = Evaluators.pure_material(board)
		tot += numMoves(board, chess.WHITE) * 0.01
		tot -= numMoves(board, chess.BLACK) * 0.01
		return tot
	
	@staticmethod
	def pawn_push(board):
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
				#more points for being futher up the board
				rank = chess.square_rank(square)
				if ptype == chess.PAWN:
					if pcolor == chess.BLACK:
						pval += (7-rank) * 0.05
					else:
						pval += rank * 0.05
				if pcolor == chess.BLACK:
					pval = -pval
				total += pval
		return total
