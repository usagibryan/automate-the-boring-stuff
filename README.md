# Zombie Dice Bots

This is my solution to the final practice project from [Chapter 6](https://automatetheboringstuff.com/2e/chapter6/) of Automate the Boring Stuff with Python. You can find the complete rules and the rest of the code at https://github.com/asweigart/zombiedice/.

I met these requirements:

* A bot that, after the first roll, randomly decides if it will continue or stop
* A bot that stops rolling after it has rolled two brains
* A bot that stops rolling after it has rolled two shotguns
* A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns
* A bot that stops rolling after it has rolled more shotguns than brains

But I was having too much fun and decided to experiment and make more bots. I made at least 10 and plan to try more configurations in the future. Other than Alice and Bob they are all named after Walking Dead characters.

<img src="./img/screenshot.png" width="500">

So far Carl and Negan tend to win the most, and therefore they have the best strategy. They roll until they get 2 shot guns (unless they have 0 brains they keep going) and if they have 1 shotgun they keep going unless they have at least 6 (Negan) or 7 (Carl) brains.

Sometimes Maggie has the most wins at at least 5 brais. At the moment Lizzie is the only bot that makes decisions based on the color of the dice.

To run this code you must install the zombiedice module by typing `pip install zombiedice` in the terminal.