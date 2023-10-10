# imports
import random
import pyjokes
import yr_weather

# create a Textforecast client (wip)
my_client = yr_weather.Textforecast()

# fetch the list of available areas
areas = my_client.get_areas("area")

# create a dictionary to map area names to IDs
area_dict = {area["areaDesc"].lower(): area["id"] for area in areas["area"]}


# bot responses
def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == "help":
        return "`Available commands: !help !roll !jokes and hello`"

    if p_message == "hello":
        return "Hello there!"

    if p_message == "roll":
        return str(random.randint(1, 100))

    if p_message == "joke":
        return pyjokes.get_joke()

    if p_message.startswith("weather"):
        # Split the message into command and location
        _, location = p_message.split(maxsplit=1)

        # Check if the location is in the list of available areas
        if location in area_dict:
            # Fetch the forecast for the location
            land_overview = my_client.get_forecasts("landoverview")
            newest_forecast = land_overview["time"][0]["forecasttype"]

            # Search for the forecast for the specified location
            for loc in newest_forecast["location"]:
                if loc["id"] == area_dict[location]:
                    forecast_text = loc["text"]
                    return f"Weather in {location}: {forecast_text}"

        return f"Sorry, I don't have a forecast for {location}"

    else:
        return None
