# UdacityAdventureGame
Created an adventure game for my nano degree - introduction to programming.

To run adventure_game.py open a console, navigate to the directory where adventure_game.py was saved and type "python3 adventure_game.py".

Instructions:
In this project, you'll make a simple version of an old-fashioned text-based adventure game. You can find an example in the workspace below. Try it out to get a feeling for how the game works!

As you can see, this is only a very short game with a couple of choices available to the player. We did that on purpose, to keep it simple. If we were making a complete game, we would expand it a great deal, and probably give the player a whole world to explore. But for this project, the idea is to focus on some key things that we need if want to make a working game:

The game gives players a description of what's happening, and then asks them to make a choice.
Something different happens depending on the choice the player made.
The game also includes some random factors, so that it's a little different each time.
The game has conditions for winning and losing.
When the game is over, it asks if the player wants to play again.


Code Review:
The descriptions are printed to the console for the player to see.

The game uses the following functions:

The time.sleep function is used to create delays between messages so that they aren't all printed at once.
The random.choice or random.randint function is used to influence the game so that each game is different in some way.
The game uses the input function in combination with conditional statements (e.g., if and while) to create an interactive program.

The input function is used to ask the player what they would like to do.
The player's choices affect what happens in the game, including:
Whether the player wins or loses.
Whether to restart or exit after the game is over.
The game uses a conditional loop to handle invalid input. If the player enters a choice that is not valid, the game gives them the chance to retry until they enter a valid option. The game does not crash and does not treat invalid input as a valid choice.
The program's code is refactored by defining and calling functions. The code includes at least four-function definitions that are used to improve the code in some way, such as by:

Reducing repetition
Reducing complexity
Improving the readability or organization of the code
Each function should have a single purpose and a name that describes that purpose.

The code written follows the standard Python Style Guide, such that pycodestyle tool reports zero errors and zero warnings.
The program is a playable game, and runs from start to finish without crashing or displaying errors.
