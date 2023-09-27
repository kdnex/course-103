#!/bin/bash

check_domain() {
    local domain=$1
    echo -n "Checking $domain... "
    
    # Use dig to query the DNS and capture the result in a variable
    ip_address=$(dig +short $domain)

    # Check if the result is not empty (i.e., an IPv4 address exists)
    if [ -n "$ip_address" ]; then
        echo "ok"
    else
        echo "failure"
        exit 1
    fi
}

# input data for script
source data.sh

# create loop to test all sub-domains

for domain in $domains; do
    check_domain $domain
done

