import requests
import json

url = 'https://burnertickets.com/BurnerTicketing/API/index.php'
apiKey = 'KEY'
eventId = 'ID'


def getResponseForMethod(payload):
	 r = requests.post(url, data = payload)
	 response = r.json()
	 return response['message']

payload = (('method', 'GetUsersWithTicketsEventId'), ('apiKey', apiKey), ('eventId', eventId))
allBorderlings = getResponseForMethod(payload);

for borderling in allBorderlings:
	userId = borderling['UserId']
	name = borderling['FirstName'] + " " + borderling['LastName']
	email = borderling['EmailAddress']
	payload = (('method', 'GrabUsersCustomEventInfo'), ('apiKey', apiKey), ('userId', userId), ('eventId', eventId))
	response = getResponseForMethod(payload);
	for item in response:
		if item['meta_key'] == '15_CivicRoles':
			print(userId + "," + name + "," + email + "," + item['meta_value'])