import requests
import os
import sys


def get_api_key():
    return os.getenv("API_FOOTBALL_KEY")


def fetch_match_data(api_key):
    url = "https://v3.football.api-sports.io/fixtures?team=86&last=3"
    headers = {
        "x-apisports-key": api_key
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def process_matches(data, num_matches=3):
    matches = data['response'][:num_matches]
    results = []
    if not matches:
        return ["No recent matches found for Real Madrid."]
    for match in matches:
        home_team = match['teams']['home']['name']
        away_team = match['teams']['away']['name']
        score = match['goals']
        results.append(
            f"{home_team} {score['home']} - {score['away']} {away_team}")
    return results


def motivational_quote():
    return "Dream big!"


if __name__ == "__main__":
    api_key = get_api_key()
    if not api_key:
        print("Error: API key not found. Please make sure ENV var is set.")
        sys.exit(1)
    else:
        try:
            data = fetch_match_data(api_key)
            matches = process_matches(data)
            print("Recent Real Madrid Matches:")
            if not matches:
                print("No matches found.")
            for match in matches:
                print(match)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching match data: {e}")
            sys.exit(1)
    print(motivational_quote())
