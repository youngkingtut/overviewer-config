from datetime import date
import json


PLAYER_NAME_TO_UUID = {
    "chucklebug": "5be02612-c19d-40fc-bd46-cb280ae1342f",
    "tutenkhamun": "772ee789-2598-4d80-a3ef-71daee97b09a",
    "CharlesBronson0": "b841af9d-6911-466f-8d58-37e1af1570f7",
    "kylehighclub": "c33f0781-9fd3-4dca-9807-e0a279e27e42",
    "HallsaUsageway": "e07deaea-89bd-4093-9c40-9199513c9232",
    "IamYourFarter": "f75f9e1c-3a0a-4931-82bb-12a0591d9ce9",
    "Bromentum": "f4865c5b-8117-4bf8-b680-f7a6b4164b0c",
    "brjns": "f0097790-369f-4f4d-ba5f-e9a429fb7605"
}

CSV_HEADER = [
    "chucklebug",
    "tutenkhamun",
    "CharlesBronson0",
    "kylehighclub",
    "HallsaUsageway",
    "IamYourFarter",
    "Bromentum",
    "brjns"
]

PATH_TO_STATS = "/home/tstorz/world/stats/"
PATH_TO_PLAYTIME = "/home/tstorz/playtime.csv"

if __name__ == "__main__":
    print("Fetching play time stats")
    play_times = []
    for name in CSV_HEADER:
        with open(f"{PATH_TO_STATS}{PLAYER_NAME_TO_UUID[name]}.json", "r") as stat_file:
            play_times.append(str(json.load(stat_file)["stats"]["minecraft:custom"]["minecraft:play_one_minute"]/20))

    print(f"Writing the following play times to {PATH_TO_PLAYTIME}: {play_times}")
    with open(PATH_TO_PLAYTIME, "a") as output_csv:
        output_csv.writelines(f"{date.today()}" + "," + ",".join(play_times) + '\n')
