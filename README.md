 # DudeFish
DudeFish is an AI chess engine that runs on [Lichess](https://lichess.org) out of the box.
The goal of the engine is to gradually progress in to a winning position by strategically choosing game branches.
## Implementation
At it's core, the engine uses the [Minimax](https://en.wikipedia.org/wiki/Minimax) algorithm with [Alpha-Beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning), and evaluates leaves at shallow depths with an evaluation function.
The engine can only see, on average, 3 moves ahead.
## Deployment
To deploy on **Lichess**

 1. you must be in possession of a [Lichess BOT Account](https://lichess.org/api#operation/botAccountUpgrade). Create a new file, `lichess.token`. The contents of this file should be your Lichess *api key*.
 2. *Optional*, create a new python venv with `python -m venv venv` and activate it with `source venv/bin/activate`
 3. Install the python dependencies with `pip install -r requirements.txt`
 4. Start the bot with `python bot.py` and confirm that the bot is online and responds to challenge requests
   


