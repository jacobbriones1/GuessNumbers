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

## The Guessing Game
The goal is to guess a vector of a given size. A vector is initialized randomly, and an agent guesses using `step([...])`. The returned observation is the [Mean Squared Error](https://en.wikipedia.org/wiki/Mean_squared_error) between the actual vector and the guessed vector. A reward of 0 is given for guesses that are not within an MSE of 0.001, and a reward of 1 otherwise.

