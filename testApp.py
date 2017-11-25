from flask import Flask, render_template
from tests import testClass

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

if __name__ == "__main__":
    file = open("output.txt","w") 
    file.write(str("results: " + "\n")) 
    app.run(host='localhost',debug=True, port=22222)
