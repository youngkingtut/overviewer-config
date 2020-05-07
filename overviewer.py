URL = "http://www.brohangwangbang.party"
TOWN_MARKER = "TownMarker"
NETHER_GATE_MARKER = "NetherMarker"

TOWN_ICON = f"{URL}/icons/marker_town.png"
NETHER_ICON = f"{URL}/icons/marker_town.png"
DEFAULT_PLAYER_ICON = f"{URL}/icons/marker_location.png"
PLAYER_ICONS = {
    "kylehighclub": f"{URL}/icons/kyle.png",
    "HallsaUsageway": f"{URL}/icons/mike.png",
    "brjns": f"{URL}/icons/levi.png",
    "Bromentum": f"{URL}/icons/bromax.png",
    "IamYourFarter": f"{URL}/icons/matt.png",
    "chucklebug": f"{URL}/icons/chuck.png",
    "tutenkhamun": f"{URL}/icons/tristan.png"
}


def town_filter(poi):
    if (poi["id"] == "Sign" or poi["id"] == "minecraft:sign") and poi["Text1"] == "TownMarker":
        poi["id"] = TOWN_ICON
        return " ".join([poi["Text2"], poi["Text3"], poi["Text4"]])


def nether_filter(poi):
    if (poi["id"] == "Sign" or poi["id"] == "minecraft:sign") and poi["Text1"] == "NetherMarker":
        poi["id"] = NETHER_ICON
        return " ".join([poi["Text2"], poi["Text3"], poi["Text4"]])


def player_filter(poi):
    if poi["id"] == "Player":
        player_name = poi["EntityId"]
        poi["icon"] = PLAYER_ICONS.get(player_name, DEFAULT_PLAYER_ICON)
        return player_name


worlds["BroHangWangBang"] = "/home/tstorz/world"
renders["surface"] = {
    "world": "BroHangWangBang",
    "title": "surface",
    "dimension": "overworld",
    "rendermode": "normal",
    "markers": [
        dict(name="players", filterFunction=player_filter, checked=True),
        dict(name="towns", filterFunction=town_filter, checked=True)
    ]
}
renders["nether"] = {
    "world": "BroHangWangBang",
    "title": "nether",
    "dimension": "nether",
    "rendermode": "nether",
    "markers": [
        dict(name="players", filterFunction=player_filter, checked=True),
        dict(name="gates", filterFunction=nether_filter, checked=True)
    ]
}
outputdir = "/home/tstorz/output"
