import random
import smtplib
import pandas
import datetime as dt
import os 



MY_EMAIL = os.environ['EMAIL']
EMAIL_PASSWORD = os.environ['PASSWORD']

birthdays_data = pandas.read_csv('birthdays.csv')

now = dt.datetime.now()

year = now.year
month = now.month
day = now.day

today_tuple = (month, day)

birthdays_data_dict = {(data_row['month'], data_row['day']):data_row for(index, data_row) in birthdays_data.iterrows()}

if today_tuple in birthdays_data_dict:
    birthday_person = birthdays_data_dict[today_tuple]
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthday_person['name']).replace('[AGE]', str(year-birthday_person['year']))
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person['email'], msg=f'Subject:Happy Birthday!\n\n{contents}')
        print('Email was sent successfully')




