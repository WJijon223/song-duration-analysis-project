import requests
import json
import time
from pathlib import Path


# Create folders for the raw JSON files.
folder = Path(__file__).resolve().parent / "raw_data"
itunes_folder = folder / "itunes"

folder.mkdir(exist_ok=True)
itunes_folder.mkdir(exist_ok=True)


def get_api_data(url, parameters, headers):
    """Request JSON data and check the response status code."""

    # Try again if the server is temporarily unavailable.
    for attempt in range(3):
        response = requests.get(
            url,
            params=parameters,
            headers=headers,
            timeout=60
        )

        print("Status Code:", response.status_code)

        if response.status_code == 200:
            print("Request successful!")

            data = response.json()
            return data

        elif response.status_code in [429, 500, 502, 503, 504]:
            print("Server temporarily unavailable.")

            if attempt < 2:
                print("Waiting 10 seconds before trying again.")
                time.sleep(10)

        else:
            print(f"Request failed: {response.status_code}")
            return None

    return None


headers = {
    "User-Agent": (
        "SongDurationAnalysis/1.0 "
        "(https://github.com/WJijon223/song-duration-analysis-project)"
    )
}

periods = [
    (1970, 1979),
    (1980, 1989),
    (1990, 1999),
    (2000, 2009),
    (2010, 2019),
    (2020, 2026)
]


# PART 1: Collect MusicBrainz data.
for start, end in periods:
    filename = folder / f"musicbrainz_{start}_{end}_raw.json"

    if filename.exists():
        print(f"Already saved: {filename.name}")
        continue

    print(f"\nCollecting MusicBrainz: {start}–{end}")

    url = "https://musicbrainz.org/ws/2/recording/"

    parameters = {
        "query": (
            f"firstreleasedate:[{start}-01-01 TO {end}-12-31]"
        ),
        "fmt": "json",
        "limit": 20
    }

    try:
        data = get_api_data(url, parameters, headers)

        if data is not None:
            # Format the complete response without cleaning its values.
            raw_json = json.dumps(data, indent=2)

            with filename.open("w", encoding="utf-8") as file:
                file.write(raw_json)

            print(f"Saved: {filename.name}")

    except (requests.RequestException, ValueError) as error:
        print("Request failed:", error)

    time.sleep(4)


# PART 2: Collect iTunes data for the MusicBrainz recordings.
for start, end in periods:
    musicbrainz_file = folder / (
        f"musicbrainz_{start}_{end}_raw.json"
    )

    if not musicbrainz_file.exists():
        print(f"Missing MusicBrainz data: {start}–{end}")
        continue

    with musicbrainz_file.open(encoding="utf-8") as file:
        musicbrainz_data = json.load(file)

    recordings = musicbrainz_data.get("recordings", [])[:20]

    for number, recording in enumerate(recordings, start=1):
        title = recording.get("title", "")
        recording_id = recording["id"]

        artist = ""

        for credit in recording.get("artist-credit", []):
            if isinstance(credit, dict):
                artist += credit.get("name", "")
                artist += credit.get("joinphrase", "")

        filename = itunes_folder / (
            f"{start}_{end}_{recording_id}_raw.json"
        )

        if filename.exists():
            print(f"Already saved: {filename.name}")
            continue

        if not title or not artist:
            print(f"Missing title or artist: {recording_id}")
            continue

        print(
            f"\nCollecting iTunes {start}–{end} "
            f"[{number}/{len(recordings)}]: {title} | {artist}"
        )

        url = "https://itunes.apple.com/search"

        parameters = {
            "term": f"{title} {artist}",
            "entity": "song",
            "country": "US",
            "limit": 20
        }

        try:
            data = get_api_data(url, parameters, headers)

            if data is not None:
                raw_json = json.dumps(data, indent=2)

                with filename.open("w", encoding="utf-8") as file:
                    file.write(raw_json)

                print(f"Saved: {filename.name}")

        except (requests.RequestException, ValueError) as error:
            print("Request failed:", error)

        time.sleep(4)


print(f"\nRun finished. Check the messages for any failed requests.")
print(f"Raw data folder: {folder}")