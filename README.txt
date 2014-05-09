Requires pygame, so download from:
http://www.pygame.org/download.shtml

Requires wxpython:
http://www.wxpython.org/download.php


TO RUN:
run the file open.py


Files and what they do:
open.py - displays the opening picuter and choice buttons
game.py - runs the logic of the game, including the wxpython graphics
background_panel.py - Panel class that makes the pokemon display over the background image correctly
high_score.txt - stores the current high score
Names.txt - provides the base for the dictionaries that we make in the game




Cool Items to Note:

music button
	plays / pauses music
	alternating effect of button label
	music playing interfaces with game-pause
	stops music when you quit the game
easy mode button:
	alternating label effect
	switches between shadow and color picture
	updates right when you press the button
text focus
	any button with a method sends the focus back to the textbox afte being pressed
pokemon already answered
	rewrote randomization completey so it could only pick from the pool of pokemon that have not appeared yet
end screen
	made a screen when you name all pokemon that displays congratuations
	textbox is uneditable until you restart the game
next button
	skip to next pokemon
	return focus to textbox
unclickable button method
	returns focus to textbox, when clicking a button that does nothing. 
	now all buttons return focus to textbox
hint button
	when activated, shows hint textbox that slowly fills in the name of the pokemon in the hint area
	when deactivated, hides the hint textbox from view
	hint area resets to hidden after each pokemon
intro sound
	plays the classic "Who's That Pokemon?!" sound clip
	classic
Intro Screen
	Fun picture screen to preface the game
	Buttons do things