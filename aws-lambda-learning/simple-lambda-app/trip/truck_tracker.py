trackers = [
    {"tracker_id": 123, "latitude": 6.4215214, "longitude": -75.254123},
    {"tracker_id": 456, "latitude": 6.32323, "longitude": -75.25413232},
    {"tracker_id": 789, "latitude": 6.42152343, "longitude": -75.253232},
]


def lambda_handler(event, context):
    tracker_id = event.get("pathParameters").get("tracker_id")
    tracker = list(filter(lambda t: t.get("tracker_id") == tracker_id, trackers))
    if not tracker:
        print("Tracker not found")
    body = {
        "latitude": tracker[0].get("latitude"),
        "longitude": tracker[0].get("longitude"),
    }
    print("Latitude: {}".format(body.get("latitude")))
    print("Longitude: {}".format(body.get("longitude")))
