import gpxpy
from pathlib import Path

# Resolve the GPX file relative to this script's directory
script_dir = Path(__file__).resolve().parent
gpx_path = script_dir / "flight1.gpx"

if not gpx_path.exists():
    raise FileNotFoundError(f"GPX file not found: {gpx_path}\nRun the script from the project or place the file next to this script.")

with gpx_path.open("r") as f:
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

