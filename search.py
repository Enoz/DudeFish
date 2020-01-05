import chess
import copy
import math

def minimax(evaluator, board, depth):
	return alphabeta(evaluator, board, depth-1, -math.inf, math.inf)
		
def alphabeta(evaluator, board, depth, a, b):
	if board.is_game_over(claim_draw=True):
		return None, evaluator(board)
		
	if depth == 0:
		return next(board.generate_legal_moves()),evaluator(board)
		
	if board.turn == chess.WHITE:
		value = -math.inf
		best_move = next(board.generate_legal_moves())
		for move in board.legal_moves:
			child = copy.deepcopy(board)
			child.push(move)
			_, n_value = alphabeta(evaluator, child, depth-1, a, b)
			if n_value > value:
				value = n_value
				best_move = move
			a = max(a, value)
			if a >= b:
				break
		return best_move, value
	else:
		value = math.inf
		best_move = next(board.generate_legal_moves())
		for move in board.legal_moves:
			child = copy.deepcopy(board)
			child.push(move)
			_, n_value = alphabeta(evaluator, child, depth-1, a, b)
			if n_value < value:
				value = n_value
				best_move = move
			b = min(b, value)
			if a >= b:
				break
		return best_move, value
