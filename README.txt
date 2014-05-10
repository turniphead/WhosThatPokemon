Who's That Pokemon?
A quiz game by Christopher Akatsuka and Dean Wilhelmi

Requires pygame, so download from:
http://www.pygame.org/download.shtml

Requires wxpython:
http://www.wxpython.org/download.php


TO RUN:
python open.py


Files and what they do:
open.py - Game introduction and options to start or quit
game.py - Runs the logic of the game, including the wxpython graphics
background_panel.py - Panel class that makes the pokemon display over the background image correctly
high_score.txt - stores the current high score
Names.txt - provides the base for the dictionaries that we make in the game



************************************************************
Testing EndGame Behavior:
If you want a quick way to get to the end of the game, go to game.py and change the
only_one_pokemon variable to be True (top of the file). This will make the game so that
Bulbasaur is the only pokemon you have to guess.
************************************************************


Cool Items to Note:

open.py:
-Looping music in the background
-Static buttons for starting and quitting


game.py:
-music button
	plays / pauses music
	alternating effect of button label
	music playing interfaces with game-pause
	stops music when you quit the game
-easy mode button:
	alternating label effect
	switches between shadow and color picture
	updates right when you press the button
-text focus
	any button with a method sends the focus back to the textbox after being pressed
-pokemon already answered
	rewrote randomization completey so it could only pick from the pool of pokemon that have not appeared yet
-end screen
	made a screen when you name all pokemon that displays congratuations
	textbox is uneditable until you restart the game
    overwites high score if your score is higher
-next button
	skip to next pokemon
	return focus to textbox
-unclickable button method
	returns focus to textbox, when clicking a button that does nothing. 
	now all buttons return focus to textbox
-hint button
	when activated, shows hint textbox that slowly fills in the name of the pokemon in the hint area
	when deactivated, hides the hint textbox from view
	hint area resets to hidden after each pokemon
-intro sound
	plays the classic "Who's That Pokemon?!" sound clip
-dynamic point calculation
    the more time you take to answer, the lower your score
