#!/bin/bash

check_wp_certificate() {
    local domain=$1
    echo -n "Checking $domain... "
    
    # Check if the domain is listening on port 443 (HTTPS) and validate the SSL certificate
    curl -Is https://$domain >/dev/null 2>&1
    https_result=$?

    # Check and print the result
    if [ $https_result -eq 0 ]; then
        echo "HTTPS Certificate: ok"
    else
        echo "HTTPS Certificate: failure"
        exit 1
    fi
}

# input data for script
source data.sh

echo "Testing to see if the WordPress sites have a valid web site certificate for https."
# create loop to test all sub-domains

for domain in $domains; do
    check_wp_certificate $domain
done

