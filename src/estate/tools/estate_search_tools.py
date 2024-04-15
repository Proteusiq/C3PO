import httpx
from crewai_tools import BaseTool, WebsiteSearchTool


def estate_params(params: dict) -> dict:
    # transform params to API specific
    if "postalCode" in params.keys():
        value = params.get("postalCode")
        params["zipCodes"] = value
        del params["postalCode"]
    return params


class BoligaAPIData(BaseTool):
    name: str = "Boliga API Data Fetcher"
    description: str = "Fetches data from an external API using POST request."

    def _run(self, params: dict) -> str:
        # Configuration for the API endpoint and headers
        # example
        # https://api.boliga.dk/api/v2/search/results?pageSize=50&zipCodes=2650&sort=daysForSale-a&includeds=1&includeotw=1
        api_url = "https://api.boliga.dk/api/v2/search/results"
        headers = {"Content-Type": "application/json"}

        params = {
            **estate_params(params),
            "pageSize": 10,
            "sort": "daysForSale-a",
            "includeds": 1,
            "includeotw": 1,
        }

        # Making the GET request
        response = httpx.get(api_url, params=params, headers=headers)

        # Handling the response
        if response.status_code == httpx.codes.OK:
            return response.json()
        else:
            return f"Failed to fetch data: {response.status_code}"


# https://docs.crewai.com/tools/WebsiteSearchTool/#customization-options
boligsiden_tool = WebsiteSearchTool(website="https://www.boligsiden.dk/")

boliga_api_tool = BoligaAPIData()

if __name__ == "__main__":
    # testing
    result = boliga_api_tool.run({"zipCodes": 2650})
    print(result)
