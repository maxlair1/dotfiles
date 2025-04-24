#!/usr/bin/env bash

# Kill all running polybar instances
killall -q polybar

# Wait until they're all gone
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch Polybar
polybar top &
