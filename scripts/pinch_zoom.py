import libevdev
import time
import subprocess

# Set up device
from libevdev import Device, InputEvent, EV_ABS, EV_KEY, EV_SYN
import os

def find_touchpad_device():
    for dev_path in os.listdir('/dev/input'):
        if not dev_path.startswith('event'):
            continue
        try:
            d = Device(f"/dev/input/{dev_path}")
            if 'touchpad' in d.name.lower():
                return f"/dev/input/{dev_path}"
        except Exception:
            continue
    return None

dev_path = find_touchpad_device()
if not dev_path:
    print("Touchpad device not found.")
    exit(1)

fd = open(dev_path, 'rb')
d = Device(fd)

print(f"Using device: {d.name}")

# Constants
PINCH_THRESHOLD = 10  # minimal distance delta for zoom
ZOOM_MULTIPLIER = 3   # more = zoom faster
MIN_INTERVAL = 0.05   # 50ms debounce

last_zoom = time.time()

def send_scroll(direction, amount=1):
    subprocess.run(['xdotool', 'keydown', 'ctrl'])
    for _ in range(amount):
        subprocess.run(['xdotool', 'click', '4' if direction == 'down' else '5'])
        time.sleep(0.01)
    subprocess.run(['xdotool', 'keyup', 'ctrl'])

# Main loop
prev_distance = None

for ev in d.events():
    if ev.type == EV_ABS and ev.code in [libevdev.ABS_MT_POSITION_X, libevdev.ABS_MT_POSITION_Y]:
        continue  # skip single finger positions

    if ev.type == EV_ABS and ev.code == libevdev.ABS_MT_SLOT:
        continue

    if ev.type == EV_ABS and ev.code == libevdev.ABS_MT_TOUCH_MAJOR:
        # Detect pinch spread amount — crude but enough
        distance = ev.value
        now = time.time()

        if prev_distance is not None:
            delta = distance - prev_distance

            if abs(delta) > PINCH_THRESHOLD and (now - last_zoom) > MIN_INTERVAL:
                direction = 'up' if delta > 0 else 'down'
                steps = min(int(abs(delta) / PINCH_THRESHOLD) * ZOOM_MULTIPLIER, 10)
                send_scroll(direction, steps)
                last_zoom = now

        prev_distance = distance
