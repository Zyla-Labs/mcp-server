from fastmcp import FastMCP
import requests

server = FastMCP("Zyla API Hub MCP Server")

@server.tool()
def call_api(
    method: str,
    url: str,
    headers: dict = {},
    params: dict = {},
    data: dict = {}
) -> dict:
    """
    Makes a request to any API with a given method, URL, headers, and optional query/body parameters.

    Example:
    method = "GET"
    url = "https://www.zylalabs.com/api/824/crime+data+by+zipcode+api/583/get+crime+rates+by+zip"
    headers = {"Authorization": "Bearer <API_KEY>"}
    """

    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            params=params if method.upper() == "GET" else None,
            json=data if method.upper() != "GET" else None,
            timeout=15
        )

        return {
            "status_code": response.status_code,
            "response": response.json() if response.headers.get("Content-Type", "").startswith("application/json") else response.text
        }

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    server.run()
