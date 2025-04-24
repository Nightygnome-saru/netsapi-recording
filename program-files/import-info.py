import requests
import os
import json

# Import the API key from the environment variable
# DO NOT HARD CODE THE API KEY HERE - SECURITY RISK
api_key = os.environ.get('API_KEY_NETSAP_SB')

# Accept JSON format and input API key for authorization
getHeaders = {
    "accept": "application/json", 
    "Authorization": f"Bearer {api_key}"
}

# URL for Users in Sandbox Domain API endpoint
usersUrl = "https://dev1.ns-api.com/ns-api/v2/domains/noliver.tvcinc.net/users?limit=100&start=0"

# URL for Users in Main TVC Domain API endpoint
#usersUrl ="https://tvc.phoneware.cloud/ns-api/v2/domains/tvc/users?limit=100&start=0"

# Desired fields to extract from users array
#userParams = [
#        "domain",
#        "user",
#        "name-first-name",
#        "name-last-name",
#        "email",
#        "user-scope"
#]

# Get all data of users in domain
domainUsers = requests.get(usersUrl, headers=getHeaders)
usersJson = json.loads(domainUsers.text)
#print(usersJson)

# Print specific info about the users
if(domainUsers.status_code == 200):
    for user in usersJson:
        print("Extension: " + user['user'] + " - " + user['name-first-name'] + " " + user['name-last-name'] + " - " + user['email'])
else:
    print(f"Error: {domainUsers.status_code}")
    exit(1)

# How to determine when/where recordings are available?
# Info in Netsapiens Event Subscriptions
# cdr event subscription - send 1 event at completion of a call - can use to determine which calls had recordings?
# cdr field mapping - call-orig-call-id - Returns SIP Call-ID Header, can use to later retrieve info from specific call?
# Make a new call - May allow to fake a call for testing purposes?
