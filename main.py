import smtplib

import yaml

with open("data.yml") as yaml_file:
    data = yaml.safe_load(yaml_file)

EMAIL = data["email"]
PASSWORD = data["password"]

connection = smtplib.SMTP("smtp.gmail.com", port=587)
