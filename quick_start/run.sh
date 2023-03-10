#!/bin/bash
echo "###################################################################"
echo "STARTING VAULT DEV SERVER..."
container_id=$(docker run --rm --detach -p 8200:8200 -e 'VAULT_DEV_ROOT_TOKEN_ID=dev-only-token' vault:1.1.0)

echo "###################################################################"
echo "RUNNING QUICKSTART EXAMPLE..."
python main.py

echo "###################################################################"
echo "STOPPING VAULT DEV SERVER..."
docker stop "${container_id}" > /dev/null

echo "###################################################################"
echo "VAULT SERVER STOPPED.."