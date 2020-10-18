# Canvas-Bot

## canvas.py
Canvas.py holds functionalities to talk to the Canvas API to retrieve student's course and planned office hour or section information. 

## bot.py
bot.py is the mainframe of the Canvas bot. bot.py implements functionalities for setting reminders for upcoming office hours, showing current courses, and showing upcoming events listed on the the Canvas calendar. In order to store the necessary data about the users (their user id, the server id, opt in status) and servers, the user of the bot should run `create-tables.sql` to create the tables in the sqlite3 database. 

## How to use the bot
To use the bot, the user should create a Canvas API key by heading to https://canvas.uw.edu/profile/settings to create a new access token and then add it to the .env file. 

