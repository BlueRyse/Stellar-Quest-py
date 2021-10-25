from stellar_sdk import Keypair

secret = input("Insert the secret seed: ")
keypair = Keypair.from_secret(secret)

print(keypair.public_key)
