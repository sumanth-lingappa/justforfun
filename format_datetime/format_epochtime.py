from datetime import datetime


def convert_date(timestamp):
    # d = datetime.utcfromtimestamp(timestamp)
    d = datetime.fromtimestamp(timestamp)
    formated_date = d.strftime('%a, %d %b %Y %I:%M:%S %p')
    return formated_date

print(convert_date(float(input("Enter seconds since epoch in seconds: "))))




