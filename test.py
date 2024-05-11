import requests

# Specify the URL of your FastAPI endpoint
url = "http://localhost:8000/doc/"

# Specify the date range you want to query
start_date = "2024-05-11"
end_date = "2024-05-11"

# Make a GET request to the endpoint with the date range parameters
response = requests.get(url, params={"start_date": start_date, "end_date": end_date})

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response JSON data
    print(response.json())
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code} - {response.text}")