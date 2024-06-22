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

        try:
            java_version = r.json()["javaVersion"]["majorVersion"]
        except KeyError:
            java_version = None

        downloads_db.append(
            {
                version["id"]: {
                    "downloads": r.json()["downloads"],
                    "java_version": java_version,
                }
            }
        )

    with open("data/json/versions.json", "w") as f:
        json.dump(downloads_db, f, indent=4)


if __name__ == "__main__":
    main()
