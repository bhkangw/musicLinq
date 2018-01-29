## Synopsis
MusicLinq is place where friends can share music with each other.

## Motivation
I realized that between friends, we send a lot of music to each other, but the links would always get lost amongst the jumble of texts, Facebook chats, and other apps. To solve this I built MusicLinq to create a centralized place where we can share music with each other. Friends can login and post new songs, favorite songs shared by others, and monitor their profile. It’s become our go-to place for new music! Built with Python/Django, using OOP, ORM, SQLite, REST, AWS.

## Features
- Handles opening links into Spotify app and/or dashboard effortlessly for the user.

- Login app has full validations on all essential form fields.

- Users' passwords encypted using bcrypt.

- Each user has a page displaying their contributed songs.

- Connected to backend database using django SQLite for all Songs and User data.

- Utilizes a many to many model relationship in order to display a user's favorited songs separately from the default list.

- Used Twitter Bootstrap for styling.

## Skills/Concepts Practiced
- OOP / ORMs
- Client/Server Communication
- Django
- Models/Migration/Relationships
- Password Hashing
- Backend Database connections
- SQL Queries
- RESTful Routing
- Deployment through AWS
