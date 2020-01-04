import chess
import berserk
from game import Game

with open('./lichess.token') as f:
	token = f.read().replace('\n', '')

session = berserk.TokenSession(token)
client = berserk.Client(session)
botid = client.account.get()['id']

games = []

for event in client.bots.stream_incoming_events():
	if event['type'] == 'challenge':
		client.bots.accept_challenge(event['challenge']['id'])
	elif event['type'] == 'gameStart':
		game = Game(client, event['game']['id'])
		game.start()
		games.append(game)
