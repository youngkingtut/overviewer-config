def town_filter(poi):
    if (poi["id"] == "Sign" or poi["id"] == "minecraft:sign") and poi["Text1"] == "TownMarker":
        poi["id"] = "http://www.brohangwangbang.party/icons/marker_town.png"
        return " ".join([poi["Text2"], poi["Text3"], poi["Text4"]])


def nether_filter(poi):
    if (poi["id"] == "Sign" or poi["id"] == "minecraft:sign") and poi["Text1"] == "NetherMarker":
        poi["id"] = "http://www.brohangwangbang.party/icons/marker_town.png"
        return " ".join([poi["Text2"], poi["Text3"], poi["Text4"]])


def player_filter(poi):
    if poi["id"] == "Player":
        player_name = poi["EntityId"]
        poi["icon"] = {
            "kylehighclub": f"http://www.brohangwangbang.party/icons/kyle.png",
            "HallsaUsageway": f"http://www.brohangwangbang.party/icons/mike.png",
            "brjns": f"http://www.brohangwangbang.party/icons/levi.png",
            "Bromentum": f"http://www.brohangwangbang.party/icons/bromax.png",
            "IamYourFarter": f"http://www.brohangwangbang.party/icons/matt.png",
            "chucklebug": f"http://www.brohangwangbang.party/icons/chuck.png",
            "tutenkhamun": f"http://www.brohangwangbang.party/icons/tristan.png"
        }.get(player_name, "http://www.brohangwangbang.party/icons/marker_location.png")
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
    ],
    "showspawn": False
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
