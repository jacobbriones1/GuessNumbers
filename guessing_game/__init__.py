from gym.envs.registration import register

register(id='NumberGuessing-v0',
         entry_point='guessing_game.envs:GuessingGameEnv')
