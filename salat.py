import requests

def import_prayer_time(city , country):
    url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=8"

    try:
        response = requests.get(url)
        info = response.json()
        if "data" in info :
            prayers_timing = info["data"]["timings"]
            return prayers_timing
    except Exception :
           return "there is a problem here" 


city = input("city: ").strip()
country = input("country: ").strip()

prayers_with_time = import_prayer_time(city , country)
for Salat_name , time in prayers_with_time.items() :
    print(f"{Salat_name} : {time}")