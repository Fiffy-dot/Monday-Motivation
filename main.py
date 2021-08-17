import random
import datetime as dt
import smtplib

EMAIL = "testfionamukuhi@gmail.com"
PASSWORD = "TestCode24/7"

# we get the quotes into a list
with open("quotes.txt", "r") as quotes:
    list_quotes = quotes.readlines()

# get the current day of the week
now = dt.datetime.now()
day = now.weekday()

# pick a random quote
monday_quote = random.choice(list_quotes)

# send email every Monday
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    if day == 0:  # check if Monday
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Monday Motivation!\n\n{monday_quote}"
        )
