import requests
import datetime as dt
import smtplib

mail = "karumanchi304@gmail.com"
password = "ypsh amsp eurv zknc"
MY_LAT = 51.050407
MY_LONG = 13.737262 # Your latitude and longitude

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0,
}

iss_response = requests.get('http://api.open-notify.org/iss-now.json')
iss_response.raise_for_status()  # Ensure we got a successful response

iss_data = iss_response.json()
iss_latitude = float(iss_data['iss_position']['latitude'])
iss_longitude = float(iss_data['iss_position']['longitude'])


sun_response = requests.get('https://api.sunrise-sunset.org/json?', params=parameters)
sun_response.raise_for_status()  # Ensure we got a successful response
sun_data = sun_response.json()
sunrise = sun_data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = sun_data['results']['sunset'].split('T')[1].split(':')[0]

current_time = dt.datetime.now().hour

if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
    if int(sunrise) >= current_time or current_time >= int(sunset):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Make the connection secure, encrypted
            connection.login(user=mail, password=password)
            connection.sendmail(
                from_addr=mail,
                to_addrs=mail,
                msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
            )  # \n\n is used to separate the subject from the body of the email
