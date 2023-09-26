#!/bin/bash

check_wp_site() {
    local domain=$1
    echo -n "Checking $domain... "
    
    # Check if the domain is listening on port 80 (HTTP)
    curl -Is http://$domain >/dev/null 2>&1
    http_result=$?

    # Check if the domain is listening on port 443 (HTTPS)
    curl -Is https://$domain >/dev/null 2>&1
    https_result=$?

    # Check and print the results
    if [ $http_result -eq 0 ]; then
        echo -n "Port 80: ok, "
    else
        echo -n "Port 80: failure, "
        exit 1
    fi

    if [ $https_result -eq 0 ]; then
        echo -n "Port 443: ok"
    else
        echo -n "Port 443: failure"
        exit 1
    fi

    echo ""
}

# input data for script
source data.sh

echo "Testing to see if the WordPress sites have a web site listening on ports 80 and 443."
# create loop to test all sub-domains

for domain in $domains; do
    check_wp_site $domain
done

