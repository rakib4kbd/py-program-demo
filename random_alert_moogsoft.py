import json
import time
import random
import http.client

global condition
global con_val
condition = ['DISK', 'CPU', 'Memory']
con_val = ['Too High', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%', 'Crashed']
manager = ['New Relic', 'SOLMAN', 'Splunk']
event_type = ['DATABASE', 'SYSTEM', 'JVM HEAP']
vsad = ['DUM1', 'DUM2']

class CustomAlerts:
    def __init__(self) -> None:
        pass

    def populate_source(self):
        source = []
        i = j = k = l = None
        for i in range(1,8,4):
            for j in range(15,100,50):
                for k in range(2,255,39):
                    for l in range(2,255,3):
                        ip = f"{i}.{j}.{k}.{l}"
                        source.append(ip)
        return source
    
    def severityGen(self):
        severity = []
        for i in range (0,6):
            severity.append(i)
        return severity

    def __generate_alert(self):
        source = self.populate_source()
        severity = self.severityGen()

        a = random.choice(condition)
        b = random.choice(con_val)
        c = random.choice(source)
        d = random.choice(manager)
        e = random.choice(severity)
        f = random.choice(event_type)
        g = random.choice(vsad)
        
        event = {
            "condition"     : f"{a}",
            "source"     : f"{c}",
            "manager"       : "SOLMAN",
            "description"   : f"{a} - {b} - {c}",
            "timestamp"     : int(time.time()),
            #manager"       : f"{d}",
            "severity"      : e,
            "type"          : f"{f}",
            "vsad"          : f"{g}",
            }

# severity, manager, agent_time, description, external_id, type, priority, vsad, category, class

        payload = json.dumps(event, indent=4, sort_keys=True)
        return f"{payload}"

    def send_alerts(self, count=10):

        i = 0
        while i <= count:
            i+=1
            alert = self.__generate_alert()
            head = {
                'Content-Type': 'application/json',
            }
            api_url = 'rakib.free.beeceptor.com'
            
            conn = http.client.HTTPSConnection(api_url)
            conn.request('POST', '/my/api/path', body=alert, headers=head)
            res = conn.getresponse()
            output = res.read().decode()
            print(output)


alert = CustomAlerts()
alert.send_alerts(10)