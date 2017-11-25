import requests
import json
from threading import Thread
import time

class testClass:

    def runWithThread(command, commands):
        status = True
        testClass.writeResult(commands['output_file'], "Call: " + "starting recursion")
        while status:
            r = requests.get(command["location"], params=command["queryStrings"], headers=command["headers"])
            if r.status_code == 200:
                testClass.writeResult(commands['output_file'], "Call: " + r.url + " succeed (thread)" )
                status = True
                time.sleep(command['recursive_intervall'])
            else:
                testClass.writeResult(commands['output_file'], "Call: " + r.url + " failed (thread)" )
                status = False

    def execute():
        commands = json.load(open('callstack.json'))
        i = 0
        while i < commands['run_amount']:
            for call in commands["calls"]:
                if call["recursive"]:
                    testClass.writeResult(commands['output_file'], "call was recursive")
                    t = Thread(target= testClass.runWithThread, args=(call, commands))
                    t.start()

                else:
                    r = requests.get(call["location"], params=call["queryStrings"], headers=call["headers"])
                    if r.status_code == 200:
                        testClass.writeResult(commands['output_file'], "Call: " + r.url + " succeed" )
                    else:
                        testClass.writeResult(commands['output_file'], "Call: " + r.url + " failed" )
                time.sleep(commands['wait_time'])
            i = i + 1
        
    def writeResult(filename, entry):
        file = open(filename,"a") 
        file.write(str(entry + "\n")) 




