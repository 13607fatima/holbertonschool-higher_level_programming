#!/bin/bash
# Sends a GET request with a custom header variable
curl -sH "X-School-User-Id: 98" "$1"
