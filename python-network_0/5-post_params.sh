#!/bin/bash
# Sends a POST request with specific email and subject variables
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
