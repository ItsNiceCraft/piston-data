import requests
import json


def main():

    downloads_db = []

    r = requests.get("https://piston-meta.mojang.com/mc/game/version_manifest_v2.json")
    if r.status_code != 200:
        exit(1)
    version_manifest = r.json()
    print(f"Processing {len(version_manifest['versions'])} versions...")
    for version in version_manifest["versions"]:

        r = requests.get(version["url"])

        downloads_db.append({version["id"]: r.json()["downloads"]})

    with open("data/json/all_urls.json", "w") as f:
        json.dump(downloads_db, f, indent=4)


if __name__ == "__main__":
    main()
