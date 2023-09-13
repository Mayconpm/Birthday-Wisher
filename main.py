##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import os
import smtplib
from random import randint

import pandas as pd
import yaml

os.system("cls")

with open("./data.yml") as yaml_file:
    data = yaml.safe_load(yaml_file)

EMAIL = data["email"]
PASSWORD = data["password"]

NAME_PLACEHOLDER = "[NAME]"

birthdays_df = pd.read_csv("./birthdays.csv", header=0)

now = dt.datetime.now()
month = now.month
day = now.day


if birthdays_df[(birthdays_df.day == day) & (birthdays_df.month == month)].items():
    row = birthdays_df[(birthdays_df.day == day) & (birthdays_df.month == month)]
    receiver_name = row.name[0]
    receiver_email = row.email[0]

    letter_number = randint(1, 3)
    with open(f"./letter_templates/letter_{letter_number}.txt", "r") as letter_file:
        letter = letter_file.read().replace(NAME_PLACEHOLDER, receiver_name)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=receiver_email, msg=letter)
        print("Email Sent.")
