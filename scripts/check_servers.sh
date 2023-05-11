#!/bin/bash
server_status="Daily status check of Reefscape Genomics Lab servers:\n"
hostnames=("deepcat1" "deepcat2" "deepseal" "deepsquid" "wdizg-viscore.calacademy.org")
for hostname in "${hostnames[@]}"
do
    # Ping the hostname and suppress output
    if ping -c 1 -W 1 "$hostname" > /dev/null 2>&1; then
        server_status+="$hostname is online\n"
    else
        server_status+="$hostname is OFFLINE\n"
    fi
done
curl -k -X POST -H 'Content-type: application/json' --data "{\"text\":\"$server_status\"}" https://hooks.slack.com/services/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
