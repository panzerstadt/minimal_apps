"""
based on tutorial : http://www.compjour.org/lessons/flask-single-page/hello-tiny-flask-app/
runs on local test server

made to run as small as possible (in one .py file)
to split python stuff into python and html into html, make a /templates folder
and make a file called home.html
"""

from flask import Flask

# instantiate a Flask app class
app = Flask(__name__)
print("app initiated. name of app is: ", __name__)

@app.route("/")
def homepage():
    print("the print function in python sends stuff into the console!")
    print('like now! hello! running the homepage function!')
    # do the html stuff in here, and return it (or return the string, which flask will interpret as html
    # or, actually, just link it to another html file that you prepare
    # link to html file : https://pythonspot.com/flask-with-static-html-files/
    # python + flask with html : http://pythonhow.com/add-css-to-flask-website/
    return """Hello
    <p>and</p>
    Goodbye World"""

@app.route("/test/")
def homepage_2():
    print("navigated to the address /test/!")
    return 'ooh you know my secret!'

@app.route("/pretty/")
def tutorial_page():
    print("returns the below string, run as html. from the tutorial: http://www.compjour.org/lessons/flask-single-page/serving-simple-html-response/")
    return """
        <!DOCTYPE html>
    <head>
       <title>My title</title>
       <link rel="stylesheet" href="http://stash.compjour.org/assets/css/foundation.css">
    </head>
    <body style="width: 880px; margin: auto;">  
        <h1>Visible stuff goes here</h1>
        <p>here's a paragraph, fwiw</p>
        <p>And here's an image:</p>
        <a href="https://www.flickr.com/photos/zokuga/14615349406/">
            <img src="http://stash.compjour.org/assets/images/sunset.jpg" alt="it's a nice sunset">
        </a>
    </body>
    """

if __name__ == '__main__':
    app.run(debug=True)