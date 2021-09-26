import requests
import time
from datetime import datetime

now = datetime.now()
now = now.strftime("%d/%m/%Y")

print("Today's Date :",now)
dist = [140,141,142,143,144,145,146,147,148,149,150]
date = now[:10]
cnt = 0

for i in dist:
    URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(i, date)

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}


    result = requests.get(URL, headers=header)
    response_json = result.json()
    data = response_json["sessions"]
        
    for each in data:
        if((each["available_capacity"] > 0) and (each["min_age_limit"] == 18)):
            cnt += 1
            print(each["name"])
            print(each["pincode"])
            print(each["district_name"])
            print(each["vaccine"])
            print(each["available_capacity"])
            print(each["fee_type"])
            print("Rs",each["fee"])
            print('\n')
            time.sleep(3)
            
print("\nTotal number of sites :",cnt)            
