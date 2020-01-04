import threading

class Game(threading.Thread):
	def __init__(self, client, game_id, **kwargs):
		super().__init__(**kwargs)
		self.game_id = game_id
		self.client = client
		self.stream = client.bots.stream_game_state(game_id)
		self.current_state = next(self.stream)
 	
	def run(self):
		for event in self.stream:
			if event['type'] == 'gameState':
				self.handle_statea_change(event)
	
	def handle_state_change(self, game_state):
		print(game_state)
