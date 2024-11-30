import requests

# Function to retrieve booking times by patient email
def get_booking_times_from_api(patient_email, api_url):
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error if the request was not successful
        json_data = response.json()  # Parse the JSON response
        
        # Extract appointments and filter by patient email
        appointments = json_data["data"]["appointments"]
        booking_times = [
            appointment["time"] 
            for appointment in appointments 
            if appointment["patient"]["email"] == patient_email
        ]
        return booking_times
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching data from API: {e}"
    except KeyError as e:
        return f"Error parsing data: {e}"

# Example usage
api_url = "https://kalenga.pythonanywhere.com/api/appointments"
patient_email = "mali2@gsumail.gram.edu"
booking_times = get_booking_times_from_api(patient_email, api_url)
print(f"Booking times for {patient_email}: {booking_times}")