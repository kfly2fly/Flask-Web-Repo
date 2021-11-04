# Welcome to my Website repo

I originally built this website in Winter 2020.
I made this repo as part of an effort to revamp the
site and align it with standard coding practices.

The first time around it was held together with duck tape :D

I want to credit Corey Schafer and Tech with Tim who taught me a lot about Flask and web design. I have used some of their code snippets
but have tried to make this website my own as much as possible

-- Change Log --
10/8/21:
    Updated to Python 3.10
    Added Python to the PATH
    Set up Python virtual environment
    Learned Git, created github account
    Installed Terminus in Sublime to run the terminal

10/14/21:
    Set up this github repo
    Initial commit/push of flaskblog.py, README.md
    Created new dedicated local file path to store website files

10/15/21:
    Got acquainted with my old code today.
    Added bootstrap and css

10/16/21:
    Created forms for user input. Created buttons and login fields.
    Added a database to track users using SQLAlchemy. I'm pretty familiar with sql but this was new to me. Its a Object Oriented database so it was interesting to get my hands on.

10/17/21:
    Today I followed a tutorial that brings my application up to industry standards.
    Before this I used a module structure where I had 1 main python file that ran my application. I got rid of this in favor of a python package.
    The application now runs from a __inti__.py file and this will allow for a better division of files and tasks. This particularly helps out
    the SQLAlchemy stuff because I was having to deal with a circular import.

10/19/21:
    Connecting SQLAlchemy database to user login system. Storing passwords using Bcrypts hashing function. Made email login case insensitive.
    Created a new account route, which requires users to be logged in to access. Register page now validates uniqueness for username and email.
    Added functionality to change account information. Profile pictures will now be saved to a database.

10/22/21:
    Fleshed out the post section today. This will allow users to create, update, and delete posts. To delete posts I implemented a modal.
    The tutorial that I'm following uses Bootstrap 4, so I've had to do some trouble shooting to get it to work in Bootstrap 5.
    I also implemented Pagination today. I don't have many posts up yet, but once there are more than 5, they will be split up into several
    different pages. This comes with a feature where you can click on someones name and be taken to a page where jsut their posts show up. I had
    to create a custom anchor tag <!-- <a class="article-title"> --> because the previous look was ugly

10/29/21:
    It's been a while since my last update. I've been following some tutorials by Corey Schafer. I've added blueprints and also a password reset
    mechanism that will send users an email. I hope to adapt this functionality into a form where a user can enter their email and have my
    resume sent to them.

10/29/21:
    Application factory, flask blueprints, allow for a version that we can test with and a production version
