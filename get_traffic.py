import json
import sys

package = sys.argv[1]
event = open('/var/log/nogotofail/mitm.event','r')
traffic = open('/var/log/nogotofail/mitm.traffic','r')

cids = []

for l in event.readlines():
    j = json.loads(l)

    if j['success']:

        if "applications" not in j:
            continue

        apps = j["applications"]
        cid = j["connection_id"]

        for a in apps:
            app = a[0]

            if package == app:
                
                if cid not in cids:
                    cids.append(cid)

for l in traffic.readlines():
    j = json.loads(l)

    if "data" in j:
        data = j["data"].decode("base64")
        
        if j["connection_id"] in cids:
            print data

event.close()
traffic.close()
