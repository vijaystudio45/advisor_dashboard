# Create your tests here.
import random
from pprint import pprint

import requests

events = ["scheduleStartAutoServ", "scheduleCompleteAutoServ", "operator", "incomingCall", "escalation", "order",
          "rentStarted", "timeSelected", "linkClicked", "voiceMail"]
url = "https://eu-west-1.aws.webhooks.mongodb-realm.com/api/client/v2.0/app/application-2-febnp/service/LogEvent/incoming_webhook/createEventInSql?agent=BochHonda&eventName={event_name}&phoneNum=+4509090&date=2021-11-30"

count_map = dict()
for event_name in events:
    count = random.randint(5, 15)
    for i in range(count):
        print('logging, ', event_name, ' count - ', i)
        requests.get(url.format(event_name=event_name))
    count_map[event_name] = count

pprint(count_map)
