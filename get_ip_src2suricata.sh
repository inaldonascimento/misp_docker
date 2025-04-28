#!/bin/bash
api_key=PUT_YOUR_API_KEY_HERE
misp_url=https://andromaca//attributes/restSearch
get="$misp_url/returnFormat:suricata/type:ip-src||ip-dst/org:CIRCL"
curl -k -H 'Accept: application/json' -H 'Content-type: application/json' -H 'Authorization: '$api_key'' -XGET $get 