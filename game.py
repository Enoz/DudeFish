import threading
import chess
import search
from evaluation import Evaluators

evaluator = Evaluators.mobility
search_depth = 3

class Game(threading.Thread):
	def __init__(self, client, game_id, **kwargs):
		super().__init__(**kwargs)
		self.game_id = game_id
		self.client = client
		self.stream = client.bots.stream_game_state(game_id)
		self.current_state = next(self.stream)
		self.color = chess.BLACK
		if self.current_state['white']['id'] == client.account.get()['id']:
			self.color = chess.WHITE
		
	def create_board(self, state):
		board = chess.Board()
		if state['moves'] != '':
			for move in state['moves'].split(' '):
				board.push_uci(move)
		return board
 	
	def run(self):
		#perform first move if necessary
		self.handle_state_change(self.current_state['state'])
		for event in self.stream:
			if event['type'] == 'gameState':
				self.handle_state_change(event)
	
	def handle_state_change(self, game_state):
		board = self.create_board(game_state)
		if board.turn == self.color:
			mv, val = search.minimax(evaluator, board, search_depth)
			if mv != None:
				self.client.bots.make_move(self.game_id, mv)
