# GuessNumbers
Gym Environment for Guessing Multiple Numbers. Inspired by [GoodAI](https://www.goodai.com/badger-architecture) and the Badger architecture. For more information on how the guessing game is used in the Badger architecture, see [the original badger paper](https://arxiv.org/ftp/arxiv/papers/1912/1912.01513.pdf). 

## Installation: 
clone this repository and install the package:<br>
`$git clone https://github.com/jacobbriones1/GuessNumbers`<br>
`$cd GuessNumbers`<br>
`$pip install -e .`<br>

## Running the environment
```
import gym 
import guessing_game

env = gym.make('NumberGuessing-v0')
env.reset(size=5)
```

