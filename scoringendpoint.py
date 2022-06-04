import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "AQvqQUy6eelddWBUYhkNQPVXS7VHPXRoQVTPKKGrdwmi"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": ["f0","f1","f2","f3","f4","f5","f6"], "values": [[8,307,130,3504,12,70,1]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/7fa14f91-d730-4c7e-90a9-8c9c17f5a001/predictions?version=2022-06-02', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
#print(response_scoring.json())
pred=response_scoring.json();
out=pred['predictions'][0]['values'][0][0]
print(out)