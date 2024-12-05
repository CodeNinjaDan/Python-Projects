import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 0
MY_LONG = 0
MY_EMAIL = ""
PASSWORD = ""
RECEIVER_EMAIL = ""

def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def is_night():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if sunset >= time_now or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        my_email = MY_EMAIL
        password = PASSWORD
        receiver_email = RECEIVER_EMAIL

        if not my_email or not password:
            raise ValueError("Email or password environment variables are not set.")

        subject = "ISS Visible."
        body = "Look up, the ISS is visible!"
        msg = f"Subject:{subject}\n\n{body}"
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()  # Makes the connection secure
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=receiver_email, msg=msg)

        except smtplib.SMTPAuthenticationError:
            print("Failed to login, check your email and password.")

        except Exception as e:
            print(f"An error occurred: {e}")
