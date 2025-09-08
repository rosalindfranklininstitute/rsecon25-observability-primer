#!/bin/sh

# Generate some dice rolls using curl (for Mac/Linux/WSL)
while true; do curl localhost:9000; printf " "; sleep $((RANDOM % 10)); done
