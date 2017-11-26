from flask import Flask, render_template
from tests import testClass
from bottle import Bottle, HTTPResponse

app = Flask(__name__)

def writeResult(filename, entry):
    file = open(filename,"a") 
    file.write(str(entry + "\n")) 


@app.route("/")
def index():
     writeResult("output.txt", "Index route opened")
     return "<form action='/run/tests'><label> Run tests for clicking button check test configuration from callstack.json there is also file where results are displayed</label><br/><input type='submit' value='Run tests'></form>"

@app.route('/run/tests')
def running_tests():
    writeResult("output.txt", "test route opened")   
    values = testClass.execute()
    return str(values) + "<br/>tests runned <br/> <br/><form action='/run/tests'><label> Run tests for clicking button check test configuration from callstack.json there is also file where results are displayed</label><br/><input type='submit' value='Try again'></form>"

@app.route('/volume/<volume>')
def running_tests(volume):
    writeResult("output.txt", "Volume changed to " + volume + "(" + "/volume/<volume>" + ")")  
    return HTTPResponse(status=200) 

    return
@app.route('/get-voice')
def get_voice():
    writeResult("output.txt", "Volume changed to " + volume + "(" + "/volume/<volume>" + ")")  
    return HTTPResponse(status=200, body="mursound.mp3") 


@app.route('/get-name')
def get_name():
    writeResult("output.txt", "getting name of chair (" + "/get-name" + ")")  
    return HTTPResponse(status=200, body="murchair") 

@app.route('/mute/<seconds>')
def mute(seconds):
    writeResult("output.txt", "Chair muted for " + seconds + "(" + "/mute/<seconds>" + ")")  
    return HTTPResponse(status=200) 

@app.route('/set-volume/<volume>/<time>')
def set_volume(volume, time):
    writeResult("output.txt", "Setting volume for  " + time + "(" + "/set-volume/<volume>/<time>" + ")")  
    return HTTPResponse(status=200) 

@app.route('/remote-tickle')
def remote_tickle():
    writeResult("output.txt", "Remote ticking chair" +  "(" + "/remote-tickle" + ")")  
    return HTTPResponse(status=200) 

@app.route('/remote-tickle/<message>')
def remotetickle_param(message):
    writeResult("output.txt", "Remote ticking chair with message " + message +  "(" + "/remote-tickle/<message>" + ")")  
    return HTTPResponse(status=200) 

@app.route('/get-dreams')
def get_dreams():
    writeResult("output.txt", "getting dreams" +  "(" + "/get-dreams" + ")")  
    return HTTPResponse(status=200) 

@app.route('/set-config/<category>/<key>/<value>')
def set_config(category, key, value):
    writeResult("output.txt", "changing chair config" +  "(" + "/set-config/<category>/<key>/<value>" + ")")  
    return HTTPResponse(status=200) 

@app.route('/get-config')
def get_config():
    writeResult("output.txt", "getting chair config" +  "(" + "/get-config/" + ")")  
    return HTTPResponse(status=200, body="chairconfig here") 
@app.route('/reboot/<confirmation>')
def reboot_chair(confirmation):
    writeResult("output.txt", "Rebooting with confirmation " + confirmation +   "(" + "/reboot/<confirmation>" + ")")  
    return HTTPResponse(status=200) 

@app.route('/set-dream/<dream>')
def set_dream(dream):
    writeResult("output.txt", "setting dream to " + dream +   "(" + "/set-dream/<dream>" + ")")  
    return HTTPResponse(status=200) 

@app.route('/get-summary')
def get_summary():
    writeResult("output.txt", "getting summary  " +  "(" + "/get-sumamry" + ")")  
    return HTTPResponse(status=200, body="summary here") 
@app.route('/get-children')
def get_children():
    writeResult("output.txt", "getting children  " +  "(" + "/get-children" + ")")  
    return HTTPResponse(status=200, body="children here") 
@app.route('/register/<host>')
def register_host(host):
    writeResult("output.txt", "registering host to  " + host +   "(" + "/register/<host>" + ")")  
    return HTTPResponse(status=200) 

if __name__ == "__main__":
    file = open("output.txt","w") 
    file.write(str("results: " + "\n")) 
    app.run(host='localhost',debug=True, port=22222)
