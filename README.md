# kinghenrybot2

This interactive Discord bot interfaces both with users and with the ESPN api to enhance my fantasy football group's experience. 

What initially started out as a basic bot that responded to keywords in the Discord chat ("hello, hi", etc.) turned into a personal project in which I learned a considerable amount about Python modules and interacting with a real API (in this case, ESPN).

Current highlights of the bot functionality are:

!starters command: using live data of a person's roster, the user types their name and a position into Discord and the bot chooses a random player who should be started that week

!goober command: (my favorite) The user types their name and an NFL week number and the bot calculates what the user's score would have been if they started the highest scoring lineup that week. The difference in potential score and actual score serves as the "goober index". 

!injuries command: after typing a user name, the bot finds and shares the current injured or questionable players (might or miht not play) on the user's roster

!points command: after typing an NFL player's name, displays the total and average points that player scored

!scoring command: after typing a user's name, displays the average points their team has scored and the average points their opponent has scored and also calculates the point differential. Could be used as somewhat of a luck index


Future direction: For the 2022 NFL season, these are some of my tentative plans:

1. Include a trades command of some sort which allows players to propose trades. The bot will use information from an external site to determine if the trade is fair.
2. Refactor some of the code, particularly the code that reads JSONs of user rosters/data and converts it to a Python-usable format. The time complexity of some of my code is inefficient and means that some operations (such as the !goober command) take longer than needed. 
Rewriting the code to use more efficient data structures will allow for a better user experience.
3. Refactor the code into more classes. I wrote much of this code while I was still relatively early in my Python learning career, so some files/functions aren't as organized as they should be. Using my current knowledge of OOP and Python will allow me to refactor the bot into a more readable and efficient form.
