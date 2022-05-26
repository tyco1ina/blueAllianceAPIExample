import requests

# Our goal is for the code to get information about our team
# Base URL: https://www.thebluealliance.com/api/v3
# Endpoint: /team/{team_key}
# ^ This is one of many endpoints that TBA offers
# Team keys are basically frc{team_key}
# So for us it would be frc5804

# When you request information, you need to specify to the program where you are getting the information from
# This is the base URL that is given on the website
base_url = "https://www.thebluealliance.com/api/v3"
# This is the specific endpoint that will give us information about our team
endpoint = "/team/frc5804"

# Putting together the full string
request_url = base_url + endpoint

# This is the header, where we give information about the request itself
headers = {
    "Accept": "application/json", 
    # When you use the bluealliance api you have to have an authentication key
    # This is to prevent against overloading the company with requests
    "X-TBA-Auth-Key": 'SK8vFkeaQvtgVtdaTgynVKrNIbIMAM7P1HWg0MD1CnT58xX7oSWiNz932RbRMxPI'
}

# This is the line where we make the resposne
# The get method of the requests object takes two parameters:
# 1. The request url
# 2. The headers that we defined earlier
response = requests.get(request_url, headers=headers)

# I don't know what this line does. I just know it has to be there in order for us to treat it like a Python dictionary
response = response.json()

# We can see the data that is returned by the website
print(response)

