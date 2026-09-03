import requests

API_URL = "http://127.0.0.1:8000/search"


def search_documents(query: str):

    try:

        response = requests.post(
            API_URL,
            json={"query": query},
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.ConnectionError:

        return {
            "error": "Unable to connect to FastAPI server."
        }

    except requests.exceptions.Timeout:

        return {
            "error": "Request timed out."
        }

    except Exception as e:

        return {
            "error": str(e)
        }