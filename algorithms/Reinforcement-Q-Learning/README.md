# Reinforcement Learning

Think of pac-man game as an example of reinforcement learning.

To run the given example, first install gym (used to setup test cases for reinforcement learning)
```
pip install gym
```

## Q-Learning

A specific implementation of Reinforcement learning.

It maintains a set of actions a and states s. 

Starts with a Q value of 0. Explore the space. If bad things happen after a given state/action, reduce its Q. If rewards happen after a given state/action, increase the Q.

**Markov Decision Processes (MDP)** : (a fancy way to name the exploration algorithm used in Q learning) It provides a mathematical framework for modeling decision making in situations where outcomes are partly random and partly under the control of a decision maker.


## References

https://pymdptoolbox.readthedocs.io/en/latest/api/mdp.html

https://github.com/ramit21/machine-learning-python/tree/master/data

https://github.com/studywolf/blog/tree/master/RL/Cat%20vs%20Mouse%20exploration


