from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Constants
API_URL = "https://api-ssl.bitly.com/v4/shorten"
API_KEY = os.getenv("BITLY_ACCESS_TOKEN")  # Retrieves the API key from environment variables

def shorten_url(long_url):
    """Shorten a given long URL using Bitly."""
    if not API_KEY:
        print("API key not found. Make sure to set it in your environment variables.")
        return None

    if not long_url.startswith(('http://', 'https://')):
        print("Invalid URL format. Make sure the URL starts with 'http://' or 'https://'.")
        return None

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "long_url": long_url
    }
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        link = response.json().get("link")
        return link
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response Content: {response.content.decode()}")
    except requests.exceptions.RequestException as e:
        print(f"Error shortening URL: {e}")
    return None

def main():
    print("URL Shortener Script")
    long_url = input("Enter the URL to shorten: ").strip()
    if not long_url:
        print("Please enter a valid URL.")
        return

    shortened = shorten_url(long_url)
    if shortened:
        print(f"Shortened URL: {shortened}")
    else:
        print("Failed to shorten the URL.")

if __name__ == "__main__":
    main()
