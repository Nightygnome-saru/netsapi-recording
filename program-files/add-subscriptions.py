import requests
import os
import json

api_key = os.environ.get('API_KEY_NETSAP_SB')

# Add CDR event subscription to notify when a call is completed
# Will use to check if call was recorded and store the call_ID if it was

eventsUrl = "https://dev1.ns-api.com/ns-api/v2/subscriptions"

cdrPayload = {
    "subscription-geo-support": "yes",
    "domain": "noliver.tvcinc.net",
    "user": "*",
    "model": "cdr",
    "post-url": "https://hook.us2.make.com/lbkrnvcpadhh6hc2ma4ghwy113dvri86"
}
eventHeaders = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Bearer {api_key}"
}

response = requests.post(eventsUrl, json=cdrPayload, headers=eventHeaders)

print(response.text)
