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
                time.sleep(command['recursive_intervall'])
            else:
                testClass.outputValues.append("Call: " + r.url+ " failed")
                status = False

    def execute():
        commands = json.load(open('callstack.json'))
        i = 0
        while i < commands['run_amount']:
            for call in commands["calls"]:
                if call["recursive"]:
                    threading.Thread(target= testClass.runWithThread, args=(call))
                else:
                    r = requests.get(call["location"], params=call["queryStrings"], headers=call["headers"])
                    if r.status_code == 200:
                        testClass.outputValues.append("Call: " + r.url + " succeed")
                    else:
                        testClass.outputValues.append("Call: " + r.url+ " failed")
                time.sleep(commands['wait_time'])

        i = i + 1
        writeResults(commands['output_file'])
        return testClass.outputValues

    def writeResults(filename):
        file = open(filename,”w”)
        for item in outputValues: 
            file.write(str(item)) 




