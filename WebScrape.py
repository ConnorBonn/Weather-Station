import requests
from bs4 import BeautifulSoup
import time as time
import csv

URL = "https://forecast.weather.gov/MapClick.php?lat=39.6127&lon=-105.0162"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
with open("output.csv", "w") as out:
    writer = csv.writer(out)
    writer.writerow(["Date", "High temp", "Low temp", "Current temp"])
    for day in range(2):
        results = soup.find(id="current_conditions-summary")
        results2 = soup.find(id="seven-day-forecast") 

        temp = results.find("p", class_="myforecast-current-lrg")
        high = results2.find("p", class_="temp temp-high")
        low = results2.find("p", class_ ="temp temp-low")
        
        current_date = f"{time.localtime()[1]}/{time.localtime()[2]}/{time.localtime()[0]}"

        for hour in range(24):
            current_time = f"{str(time.localtime()[3]).zfill(2)}:{str(time.localtime()[4]).zfill(2)}"
            writer.writerow([current_date + current_time, high.text.strip(), low.text.strip(), current_time, temp.text.strip()])
            time.sleep(3600) 