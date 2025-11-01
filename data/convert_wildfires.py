import csv
import json

features = []

with open("data/wildfires_global.txt", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(row['longitude']), float(row['latitude'])]
            },
            "properties": {
                "brightness": float(row['bright_ti4']),
                "confidence": row['confidence'],
                "frp": float(row['frp']),
                "acq_date": row['acq_date'],
                "acq_time": row['acq_time'],
                "satellite": row['satellite'],
                "daynight": row['daynight']
            }
        })

geojson = {
    "type": "FeatureCollection",
    "features": features
}

with open('wildfires.geojson', 'w') as f:
    json.dump(geojson, f, indent=2)