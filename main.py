import requests, time, smtplib
from datetime import datetime

MY_LAT = 49.839684 # Your latitude
MY_LONG = 24.029716 # Your longitude
HOST_EMAIL = 'dz.danylo@gmail.com'
HOST_PASS = 'sahu imqp pdui ikos'


def notify():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = round(float(data["iss_position"]["latitude"]))

    if sunrise >= hour_now >= sunset:
        if iss_latitude <= MY_LAT + 5 or iss_latitude >= MY_LAT - 5:
            time.sleep(30)

            with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
                connection.starttls()
                connection.login(user=HOST_EMAIL, password=HOST_PASS)
                connection.sendmail(
                    from_addr=HOST_EMAIL,
                    to_addrs=HOST_EMAIL,
                    msg=f'Subject:Look up!\n\nLook up!')

            notify()


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = round(float(data["iss_position"]["latitude"]))
iss_longitude = round(float(data["iss_position"]["longitude"]))

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

hour_now = datetime.now().time().hour

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

# if sunrise >= hour_now >= sunset:
#     if iss_latitude <= MY_LAT + 5 or iss_latitude >= MY_LAT - 5:

notify()
