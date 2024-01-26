#!/bin/bash
# Ssends a GET request to the URL provided, and displays the body of the response. A header variable X-School-User-Id must be sent with the value 98
curl -sX GET -H "X-School-User-Id: 98" "$1"
