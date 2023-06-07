import random
import pyjokes
import yr_weather


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'help':
        return '`Available commands: !help !roll !jokes and hello`'

    if p_message == 'hello':
        return 'Hello there!'

    if p_message == 'roll':
        return str(random.randint(1, 100))

    if p_message == 'joke':
        return pyjokes.get_joke()
    
    if p_message.startswith('!weather'):
        location = p_message.replace('!weather', '').strip()
        weather_data = yr_weather.get_weather(location)
        if weather_data:
            # Extract relevant weather information from the weather_data object
            temperature = weather_data.temperature()
            wind_speed = weather_data.wind_speed()
            return f"Weather in {location}: Temperature {temperature}°C, Wind Speed {wind_speed} m/s"
        else:
            return f"Unable to fetch weather information for {location}"
    else:
        return None
