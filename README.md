# Maths-Revision-Sytem
This is the prototype of my A-Level coursework, it is a mathematics revision system, that has allows students to learn through the integrated game as well as track their progress over time and send this progress to teachers. There is a revision game where students can go through lessons and see topic tips, and then a main game where you have the option to once again see the topic tips, do warmup questions and then a boss battle of sorts where you are tested on the topic, this mode is what tracks the students progress. In both the game and the revision game you see lessons and other attatched windows by walking over to the teachers in the gane and talking to them. 

Libraries used:
- pygame
- PyQt5
- random (randint and shuffle)
- os (path)
- sys
- smtplib
- sqlite3
- PIL (Image)
- Matplotlib //This is not used in the current prototype but it will be used in the final program

Explaination of the three python files:

main.py:

This file contains the main loop which trigers all of the PyQt5 user interfaces, this also contains all of the functions which create the user interface objects and then run the windows. 

programModules.py:

This file contains all of the PyQt5 classes that are not used by the game, for example all of the interfaces in the log on sequence and the main menu system. It also contains some functions that I have creates to improve code efficiency, like a database access function to which I parse an sql query and any arguments and it will return the result from the databse

gameEngine.py:

This file contians all of the pygame classes needed for the game as well as all of the PyQt5 windows that are required for the game

Within this repository there is menu flow diagram for the program labeled 'menuflow.png' as well as some captures of the programs interfaces

Features I need to develop before it is finished:
 - The data tracking system
 - The tracked data system
 - Add more topics instead of just Algebreaic expressions
