# Getting Started with the Starter Kit

FIXME

## Running the Game

You start the game by opening *main.py* and running/building the program. It is important that the folders and files stay named the same and are not moved out of their current structure. If you used the installers on the thumbdrive, you can open the main.py file with IDLE and then "Run" the program. You can also install and use PyCharm.



### The game

[The game](the_game.md) is a basic shooter. You are playing against a single opponent. There are modes to play a single player game (against an AI player), and a 2 player mode to play against someone else at Code Camp.

When you load the game you will see a bunch of square objects with an assortment of colors to help you identify them.

*	Green - Your player
*	Red - The opponent
*	Yellow - NPC (Non-Player Character) players, kill them to level up
*	White - Walls, can hide behind, but they get in the way
*	Light Blue - Missiles

There are NPC players you can shoot to level up your player to gain more missile and move mana (ability to move farther and shoot more bullets) as well as abilities to upgrade your missile power, range, and player speed.

Both you and your opponent start with 30 hit points. The default missile deals 0.5 hp of damage (so you have to shoot your opponent 60 times to kill them). You can customize your game to upgrade your missiles to do more damage, but you have to level up your player by shooting NPC players for this to work.

You can customize the game client by changing the colors, shapes, graphics, controls, sound effects, and anything else you can put your mind to. However, you can't give yourself extra bullets, change your's or your opponent's hit-points, make yourself invisible, speed of the bullets, or change the size of the walls, players, NPCs, that would just be unfair.

Have fun with the Rookie Kit. Don't be scared to ask questions or help your neighbors. We want everyone to have a great time at Code Camp.



### The controls

When first running the game, you control the direction the player moves and fires a missile by pushing the UP, DOWN, LEFT, or RIGHT keys. You may notice the player does not move by pushing a direction key. To start the player moving you push the 2 key, and to stop you press 1.

You may change and [customize the controls](client_pygame/control.md) however you want. Below is a list of the default controls.

*	`UP` changes the player's move direction and missile direction to up
*	`DOWN` changes the player's move direction and missile direction to down
*	`LEFT` changes the player's move direction and missile direction to left
*	`RIGHT` changes the player's move direction and missile direction to right
*	`1` stops the player's movement
*	`2` starts the player's movement
*	`q` disables the missile's range
*	`w` sets the missile range to 100 pixels
*	`a` disables the missile's damage (fires blanks)
*	`s` sets missile power to do 0.5 hit-points (hp) damage
*	`SPACE` fires a missile (if the player has enough missile mana)
*	`i` toggles the game info in the status bar (hp, move mana, missile mana, etc)


## The Rookie Kit Files


Below is a description of all folders in the rookie-kit. With links to further documentation. You will do all your customizations in the "client_pygame" folder.


### tps/client

Contains files for the base client system, including controls, display, and other information for allowing your game client to communicate and work with the game. You will not need to edit any files in this folder and don't really need to know how they work so you can probably ignore this folder.

### .

This is where you will do your work. There are four files that you need to know about. You can read about each one by clicking on the appropriate link below

*	[config.py](client_pygame/config.md)
*	[control/control.py](client_pygame/control.md)
*	[display/display.py](client_pygame/display.md)
*	main.py - You will not edit this file. Run this file to start the game.


### tps/common

You will not edit any of the files in this folder, but will want to know what several of them do. They contain methods for the different objects in the game and allow you to get information like its position on the board, its height and width, the direction it is facing on the board and much more.

*	[object.py](common/object.md)
*	[player.py](common/player.md)
*	[missile.py](common/missile.md)
*	[event.py](common/event.md)
*	[npc.py](common/npc.md)
*	[wall.py](common/wall.md)


### tps/engine_client

Contains information about the game engine. You will use this to get an object (player, wall, missile, npc, etc) and get more information about them. You also use this to send requests to update the player and missile direction, set the player's speed, update the missile range, and fire a missile.

*	[game_engine.py](engine_client/game_engine.md)

### tps/engine_server

You can't do much with this files and should not edit the file, but it contains a copy of the server configuration file so that you can see how big objects are, how much health they have, and other information so you can calculate how much xp you need to acquire before upgrading your missile range, missile power, and player's movement.

*	[config.py](engine_server/config.md)
