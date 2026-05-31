import json
from urllib.parse import urlencode
from urllib.request import urlopen

from crewai import Agent


class WeatherAgent(Agent):
    latitude: float
    longitude: float

    def respond(self, query: str) -> str:
        temp_c = self._fetch_temperature_c()
        return f"Current temperature: {temp_c} C"

    def _fetch_temperature_c(self) -> float:
        params = urlencode(
            {
                "latitude": self.latitude,
                "longitude": self.longitude,
                "current_weather": "true",
            }
        )
        url = f"https://api.open-meteo.com/v1/forecast?{params}"
        with urlopen(url, timeout=10) as response:
            data = json.load(response)
        return float(data["current_weather"]["temperature"])


def main() -> None:
    agent = WeatherAgent(
        role="WeatherAgent",
        goal="Provide the current temperature.",
        backstory="Fetches real-time weather data for users.",
        latitude=38.7223,
        longitude=-9.1393,
    )
    print(agent.respond(query="temperature"))


if __name__ == "__main__":
    main()
