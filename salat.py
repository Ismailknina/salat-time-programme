import requests

def import_prayer_time(city , country):
    url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=8"

    try:
        response = requests.get(url)
        info = response.json()
        if "data" in info :
            prayers_timing = info["data"]["timings"]
            return prayers_timing
    except requests.exceptions.HTTPError as HTTPError :
        print("Bad Coonection To server :'HTTPError'")
    except requests.exceptions.ConnectionError as ConnectionError :
        print("network problem (DNS failure, refused connection, etc) : 'ConnectionError'")
    except requests.exceptions.Timeout as Timeout :
        print("request times out problem :'Timeout' \n Maybe set up for a retry, or continue in a retry loop")
    except requests.exceptions.TooManyRedirects as TooManyRedirects :
        print("	request exceeds the configured number of maximum redirections : 'TooManyRedirects'")
     

city = input("city: ").strip()
country = input("country: ").strip()

if city and country:
    prayers_with_time = import_prayer_time(city , country)
    for Salat_name , time in prayers_with_time.items() :
        print(f"{Salat_name} : {time}")
else :
    print("Unvalid inputs")