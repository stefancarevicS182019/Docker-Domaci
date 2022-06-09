import json
import http.client

connection = http.client.HTTPConnection("localhost:5000")
objectPayload = json.dumps(
  {'ime': 'Stefan',
  'prezime': 'Carevic',
  'username': 'Stefan',
  'smer': 'IT',
  'predmeti':
    [{'ime': 'Administracija i odrzavanje sistema', 'espb': 8},
     {'ime': 'Interakcija covek-racunar', 'espb': 6}
    ]}
)
headers = {
  'Content-Type': 'application/json'
}

connection.request("POST", "/users", objectPayload, headers)
response = connection.getresponse()
dataDisplay = response.read()
print(dataDisplay.decode("utf-8"))