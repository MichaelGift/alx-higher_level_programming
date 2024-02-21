#!/bin/bash
# Displays the curl request response bbody size
curl -so /dev/null -w '%{size_download}\n' "$1"
