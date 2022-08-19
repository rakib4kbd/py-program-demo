import json
import time
import random
import requests

global condition
global con_val
condition = ['DISK', 'CPU', 'Memory']
con_val = ['Too High', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%', 'Crashed']
manager = ['New Relic', 'SOLMAN', 'Splunk']

class CustomAlerts:
    def __init__(self) -> None:
        pass

    def populate_source(self):
        source = []
        i = j = k = l = None
        for i in range(1,8,4):
            for j in range(15,100,50):
                for k in range(2,255,100):
                    for l in range(2,255,100):
                        ip = f"{i}.{j}.{k}.{l}"
                        source.append(ip)

        return source

    def __generate_alert(self):
        source = self.populate_source()

        a = random.choice(condition)
        b = random.choice(con_val)
        c = random.choice(source)
        d = random.choice(manager)
        
        event = {
            "condition"     : f"{a}",
            "source_id"     : f"{c}",
            "manager"       : "SOLMAN",
            "description"   : f"{a} - {b} - {c}",
            "timestamp"     : f"{int(time.time())}",
            "manager"       : f"{d}"
        }
        payload = json.dumps(event, indent=4, sort_keys=True)
        return f"{payload}"

    def send_alerts(self, count=10):

        i = 0
        while i <= count:
            alert = self.__generate_alert()
            head = {
                'Content-Type': 'application/json',
            }
            api_url = 'https://url.here'
            
            #r = requests.post(url=api_url, data=alert, headers=head, auth=('username','password'))
            #print(r.content)
            print(alert)
            i += 1


alert = CustomAlerts()
alert.send_alerts(100)