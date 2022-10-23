# Create a virtual environment using "python3 -m venv web_server" from outside the 'web_server' directory
# Then put all you static files (html, css, js) in the 'web_server' directory that was just created
# then run "pip install Flask" to install flask if not already installed
# THIS MAIN FLASK APP FILE SHOULD NOT BE CALLED 'flask.py' TO PREVENT CONFLICTS WITH FLASK ITSELF

# TO RUN THE APP: "flask --app server run" or "python -m flask --app server run"
# RUN APP IN DEBUGGER MODE FOR IT TO DYNAMICALLY REFLECT CODE CHANGES HERE: "flask --app server --debug run" or "python -m flask --app server --debug run"
# THE APP WILL RUN IN LOCALHOST (http://127.0.0.1:5000/) BY DEFAULT AT PORT 5000


# A minimal Flask Application
from flask import Flask, render_template, url_for # Flask for the app object, render_template to render HTML files, url_for to create static asset url

# create an instance of a Flask App 
app = Flask(__name__) # __name__ = '__main__' - The name of the app is set to '__main__' essentially
# print(__name__)

# ROUTES AND HANDLERS
# IN FLASK, WHEN THE SAME ROUTE IS DECLARED TWICE, THE FIRST DECLARATION TAKES PRECEDENCE.

# Decorator app.route is used to define functions that take care of the content to retun for each route of the app
@app.route("/")
def hello_world():
    # Render the index.html file at this route
    return render_template('index.html') 
    # Flask automaticlaly looks for HTML template of the given name in a 'templates' sub-directory 
    # in the current directory of this script


# Create a '/blog' route
@app.route("/blog")
def blog(): # You cannot have two route-handlers with the same name - It will break the app
    return "<p>These are my thoughts on blogs</p>"

# Create sub-route paths for the '/blog' route
@app.route("/blog/2020/dogs")
def blog2():
    return "<p>This is my dog!</p>"


# You can also add html file names in the route
@app.route("/about.html")
def about():
    return render_template('about.html') # render the 'about.html' from the 'templates' dir in the current dir


# In the Flask Framework, CSS and JS files are served as static files.
# A media type (also known as a Multipurpose Internet Mail Extensions or MIME type) indicates the nature and 
# format of a document, file, or assortment of bytes. Flash sends this content type information for the static
# files that are served and therefore the text content of these different static assets are process differently.
# STATIC FILES LIKE CSS AND JS FILES ARE STORED IN A 'static' SUB-DIRECTORY IN THE SAME DIRECTORY WHERE THIS SCRIPT RESIDES
# FOR ALL THE HTML FILES IN THE 'templates' SUB-DIR, THE STYLESHEET AND SCRIPT LINKS MUST NOW BE 'static/<stylesheet>.css'
# OR 'static/<script>.js' FOR PROPER LINKING OF THE STATIC FILES WITH THE HTML TEMPLATES

# ADDING A FAVICON IMAGE TO THE WEBSITE THAT ALL BROWSERS REQUEST FOR
# A Favicon is a 16 x 16 pixels ICO file and is a de-facto standard supported by all relevant browsers. It can be
# included by putting it in the 'static' sub-dir with the name 'favicon.ico'. This ico file will then be linked
# to the HTML using a link tag with attribute 'rel="shortcut icon"'


# ADDING VARIABLE NAMES TO THE URL THAT ARE ACCESSIBLE WITHIN THE ROUTE HANDLERS
# BY DEFAULT, THESE URL VARIABLES ARE OF TYPE STRING, BUT YOU CAN SPECIFY THEIR TYPES FOR EXAMPLE LIKE: <int:username>
@app.route("/<username>")
def greetings(username=None): # route-handler with arguments that use the variable names from the query URL
    return render_template('dynamic.html', name=username) # Pass variables to the template for dynamic content


@app.route("/<username>/<int:post_id>")
def multivar(username=None, post_id=None): # route-handler with arguments that use the variable names from the query URL
    return render_template('dynamic2.html', name=username, post_id=post_id) 