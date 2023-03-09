# hello-vault-python

# install hvac - "pip install hvac"

# install vault -> "brew install vault"

# Run command "vault" -> Output should appear

# Start a dev environment -> "vault server -dev"

# Copy and save the UNSEAL KEY and the ROOT TOKEN

# You should see something like this -> UNSEAL KEY : PInUpGJZtuYYtxFXGSl1iL6l0CwbKiGJe4KQjnqw4E=

# ROOT TOKEN : hvs.8yrdbFLQI5CTd0Qr7XGD1sA4

# Keep the dev environment running

# Initisalise a second terminal and set environment variables ->

# export VAULT_ADDR="http://127.0.0.1:8200"

# export VAULT_TOKEN="hvs.8yrdbFLQI5CTd0Qr7XGD1sA4"

# Check vault status - "vault status"

# You should get something like this :

Key Value

---

Seal Type shamir
Initialized true
Sealed false
Total Shares 1
Threshold 1
Version 1.13.0
Build Date 2023-03-01T14:58:13Z
Storage Type inmem
Cluster Name vault-cluster-b6c0037e
Cluster ID b5b68f9d-2eb6-f7c0-8aeb-b7098a841337
HA Enabled false

# Create a secret - `vault kv put secret/hello-vault-python password=Hashi123

# Read the secret to verify - "vault kv get secret/hello-vault-python
