from bottle import route, run, template, get, request

"""

Server script that uses the BottlePy framework to accept a GET request from a client.

I used this script when I taught web development with Python in my previous job.

Author: Ryan Baclit
Email: gamehelphere@gmail.com

"""

@route('/get_example')
def get_example():

    feelings = request.query["feelings"]
    happy = request.query["happy"]

    webPage = "I am glad you are feeling " + feelings + "!"
    webPage = webPage + " Are you happy? " + happy

    return webPage

run(host='localhost', port=8080)
