import gpxpy

with open("flight1.gpx", "r") as f:
    gpx = gpxpy.parse(f)

depature = gpx.name[0:4]
arrival = gpx.name[7:11]
track = gpx.tracks[0]
segment = track.segments[0]
points = segment.points

print(f"Depature: {depature}")
print(f"Arrival: {arrival}")
print(f"Total points: {len(points)}")
print(f"Duration: {points[-1].time - points[0].time}")
print(f"First point: {points[0].latitude}, {points[0].longitude}, {points[0].elevation * 3.28084}ft")
print(f"Last point: {points[-1].latitude}, {points[-1].longitude}, {points[-1].elevation * 3.28084}ft")
