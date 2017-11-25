import requests
import json
import threading
import time

class testClass:
    outputValues = []
    
    def runWithThread(command):
        status = True
        while status:
            r = requests.get(command["location"], params=command["queryStrings"], headers=command["headers"])
            if r.status_code == 200:
                testClass.outputValues.append("Call: " + r.url + " succeed")
                status = True
                time.sleep(command.recursive_intervall)
            else:
                testClass.outputValues.append("Call: " + r.url+ " failed")
                status = False

    def execute():
        commands = json.load(open('callstack.json'))
        for call in commands["calls"]:
            if call["recursive"]:
                threading.Thread(target= testClass.runWithThread, args=(call))
            else:
                r = requests.get(call["location"], params=call["queryStrings"], headers=call["headers"])
                if r.status_code == 200:
                    testClass.outputValues.append("Call: " + r.url + " succeed")
                else:
                    testClass.outputValues.append("Call: " + r.url+ " failed")



