import json
import time
import random
import requests

global condition
global con_val
condition = ['DISK', 'CPU', 'Memory']
con_val = ['Too High', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%',]


class CustomAlerts:
    def __init__(self, count) -> None:
        self.count = count

    def populate_source(self):
        source = []
        i = j = k = l = None
        for i in range(4,5):
            for j in range(10,100,25):
                for k in range(2,255,20):
                    for l in range(2,255,30):
                        ip = f"{i}.{j}.{k}.{l}"
                        source.append(ip)
        return source

    def __generate_alert(self):
        source = self.populate_source()

        a = random.choice(condition)
        b = random.choice(con_val)
        c = random.choice(source)
        
        event = {
            "condition"     : f"{a}",
            "source_id"     : f"{c}",
            "manager"       : "SOLMAN",
            "description"   : f"{a} - {b} - {c}",
            "timestamp": f"{int(time.time())}"
        }
        return f"{event}"

    def send_alerts(self):
        i = 0
        while i <= self.count:
            alert = self.__generate_alert()
            head = {
                'Content-Type': 'application/json',
            }
            api_url = 'https://rakib.free.beeceptor.com/my/api/path'
            
            r = requests.post(url=api_url, data=alert, headers=head)
            print(r.content)
            i += 1


alert = CustomAlerts(10)
alert.send_alerts()