
from adafruit_circuitplayground import cp
import time

# Adjust this threshold based on your movement.
# Higher = requires stronger motion
REP_THRESHOLD = 50



rep_count = 0
in_rep = False

cp.pixels.brightness = 0.2

while True:
    x, y, z = cp.acceleration

    # Detect when movement exceeds threshold
    if z > REP_THRESHOLD and not in_rep:
        in_rep = True
        rep_count += 1
        print("Rep:", rep_count)

        # Flash pixels for feedback
        cp.pixels.fill((0, 255, 0))
        time.sleep(0.2)
        cp.pixels.fill((0, 0, 0))

    # Reset once movement goes back down
    if z < 9:
        in_rep = False

    time.sleep(0.05)
