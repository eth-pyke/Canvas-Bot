# Canvas-Bot

## Decription
This bot works with the Discord and Canvas API's to provide students and teachers with options to
view upcoming activities and assignments through Discord. It allows users to optin on scheduling
reminders and to be aware of what is coming up.

## canvas.py
`canvas.py` holds functionalities to talk to the Canvas API to retrieve student's course and planned office hour or section information.

## bot.py
`bot.py` is the mainframe of the Canvas bot. `bot.py` implements functionalities for setting reminders for upcoming office hours, showing current courses, and showing upcoming events listed on the the Canvas calendar. In order to store the necessary data about the users (their user id, the server id, opt in status) and servers, the user of the bot should run `create-tables.sql` to create the tables in the sqlite3 database.

## Usage

Before running the bot, the user must do 2 things; create a Canvas API Key, and create the database. To create a Canvas API key, the user must head to https://canvas.uw.edu/profile/settings to create a new access token and then add it to the .env file under `API_KEY`. Then, in order to create the database, run the following commands:

``` bash
sqlite3 canvasbot.db
-> .read create-tables.sql
-> .exit
```

Finally, to run the bot, do the following:
```bash
python bot.py
```

