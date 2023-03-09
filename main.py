import hvac
import sys
import json

# AUTHENTICATE


def init_server():
    client = hvac.Client(url='http://localhost:8200')
    print(f" Is client authenticated: {client.is_authenticated()}")


# WRITE


def create_secret():
    client = hvac.Client(url='http://localhost:8200')
    create_response = client.secrets.kv.v2.create_or_update_secret(
        path='hello-vault-python', secret=dict(password="Hashi123"))
    print(json.dumps(create_response, indent=4, sort_keys=True))


# READ


def read_secret():
    client = hvac.Client(url='http://localhost:8200')
    read_response = client.secrets.kv.v2.read_secret_version(
        path='hello-vault-python')
    print(json.dumps(read_response, indent=4, sort_keys=True))


def main():
    init_server()
    create_secret()
    read_secret()


if __name__ == "__main__":
    main()
