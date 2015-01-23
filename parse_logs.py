import json

event = open('/var/log/nogotofail/mitm.event', 'r')

total = 0
success = 0

packages = {}
hostnames = {}
handlers = {}

package_handler = {}

for l in event.readlines():
    j = json.loads(l)

    total += 1

    if j["success"]:
        
        success += 1

        if "hostname" in j:
            h = j["hostname"]

            if h in hostnames:
                hostnames[h] += 1
            else:
                hostnames[h] = 1

        if "handler" in j:
            h = j["handler"]

            if h in handlers:
                handlers[h] += 1
            else:
                handlers[h] = 1

        if "applications" in j:
            apps = j["applications"]

            for a in apps:

                if a[0] in packages:
                    packages[a[0]] += 1
                else:
                    packages[a[0]] = 1

        if "handler" in j and "applications" in j:
            h = j["handler"]
            apps = j["applications"]

            for a in apps:

                if a[0] in package_handler:
                    l = package_handler[a[0]]

                    if h not in l:
                        l.append(h)
                        package_handler[a[0]] = l

                else:
                    l = []

                    l.append(h)
                    package_handler[a[0]] = l


            

event.close()

print total
print success

for k,v in packages.iteritems():
    print k, v

for k,v in handlers.iteritems():
    print k, v

for k,v in hostnames.iteritems():
    print k, v

for k,v in package_handler.iteritems():
    print k, v
