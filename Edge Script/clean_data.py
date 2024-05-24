import requests
import json

# Define the URL of your FastAPI server
FASTAPI_SERVER_URL = "http://localhost:8000/data/"

# Define the URL of the destination server
DESTINATION_SERVER_URL = "http://destination-server-url/data/"


def get_all_data():
    response = requests.get(FASTAPI_SERVER_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get data. Status code: {response.status_code}")
        return []


def check_for_null_values(data):
    non_null_data = []
    for entry in data:
        if all(value is not None for value in entry.values()):
            non_null_data.append(entry)
    return non_null_data


def send_data_to_another_server(data):
    headers = {"Content-Type": "application/json"}
    for entry in data:
        response = requests.post(DESTINATION_SERVER_URL, data=json.dumps(entry), headers=headers)
        if response.status_code == 200:
            print(f"Data sent successfully: {entry}")
        else:
            print(f"Failed to send data: {entry}. Status code: {response.status_code}")


def main():
    # Get all data from the FastAPI server
    data = get_all_data()

    # Check for null values and filter out entries with null values
    non_null_data = check_for_null_values(data)

    # Send the non-null data to another server
    send_data_to_another_server(non_null_data)


if __name__ == "__main__":
    main()
