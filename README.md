# The-Lost-Pirates-game
This is a two-player river crossing game made with Python-Pygame.

Playing arena consists of a river with some partitions in it. 

There are 2 pirates (i.e players) in the game, one at top and 
another at bottom (2 sides of the bank).
The aim is to make players reach the other end of the river.  

A player is safe when it is standing on a partition/slab.
There are two kinds of obstacles, moving and fixed. 

The player starts from the ‘START’ partition and must reach
the ‘END’ position for player 1 and 
the ‘END’ becomes ‘START’, ‘START’ becomes ‘END’ for Player 2. 
The moving obstacles move from left to right. 

The player can move up, down, left and right.
Use arrow keys to move Player1.
Use keypad keys for Player2: 
KP_8: UP, KP_2: DOWN, KP_4: LEFT, KP_6: RIGHT 
 
The score decreases as time passes and score updates on crossing obstacles.
As player crosses moving obstacle successfully, 
he/she gets 10 points and for crossing fixed obstacles 5 points.
The player dies for that round if he/she touches an obstacle
and loses 50 points. 

Only one player plays at a given point of time.
The speed of moving objects increases in the next round for that player
who wins the round. 

After 3 rounds the player who has higher score is declared the winner.
