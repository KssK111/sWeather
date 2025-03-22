def temp_relative(kelvins, multiplier):
    return 100 + (kelvins - 310) / 310 * 100 * multiplier

def temp_celsius(kelvins):
    return kelvins - 273.15

def temperatura_fahrenheit(kelvins):
    return kelvins * 1.8 - 459.67

def print_weatherAPI(json_data, settings):
    paths_for_eval = [
    "['coord']['lon']",
    "['coord']['lat']",
    "['weather'][0]['id']",
    "['weather'][0]['main']",
    "['weather'][0]['description']",
    "['weather'][0]['icon']",
    "['base']",
    "['main']['temp']",
    "['main']['feels_like']",
    "['main']['temp_min']",
    "['main']['temp_max']",
    "['main']['pressure']",
    "['main']['humidity']",
    "['main']['sea_level']",
    "['main']['grnd_level']",
    "['visibility']",
    "['wind']['speed']",
    "['wind']['deg']",
    "['wind']['gust']",
    "['clouds']['all']",
    "['rain']['1h']",
    "['snow']['1h']",
    "['dt']",
    "['sys']['message']",
    "['sys']['type']",
    "['sys']['id']",
    "['sys']['country']",
    "['sys']['sunrise']",
    "['sys']['sunset']",
    "['timezone']",
    "['id']",
    "['name']",
    "['cod']"
]
    for key in settings.options("weatherAPI"):
        try:
            values = settings.get("weatherAPI", key).split(", ")
            label = values[0]
            is_enabled = values[1] == "true"
            indent = int(values[2]) * "\t"
            json_path = eval("json_data" + "".join(paths_for_eval[int(key) - 1]))
            if is_enabled:
                print(f"{indent}{label}: {json_path}")
        except (KeyError, TypeError, IndexError) as e:
            pass

