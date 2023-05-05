from app import *
from flask import request, render_template

@app.route("/home", methods=["GET"])
def home():
    '''
    Displays the homepage.
    '''

    return render_template("../templates/index.html")

@app.route("/processing", methods=["GET"])
def processing():
    '''
    Displays the loading page.
    '''
    print("Loading...")
    return render_template("../templates/loading.html")

@app.route("/submitform", methods=["GET", "POST"])
def form_response():
    '''
    Gets the video uploaded by the user.
    '''

    import os
    print(os.getcwd())

    if request.method == 'POST':
        # User has submitted form
        print("A post request has been submitted.")

    print("Form response recieved.")
    return render_template("../../templates/loading.html")

@app.route("/finished", methods=["GET"])
def finished():
    '''
    Displays the download page.
    '''

    return render_template("../templates/download.html")