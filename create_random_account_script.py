import create_account
from stellar_sdk import Keypair, Server

server = Server("https://horizon-testnet.stellar.org")
new_account = Keypair.random()
genesis_account = "SCWUTKBTSPKETXBAIFOIK6ZY33AJILNDGJTIN7J5QK7JCZBUFDPFCQKS"
balance = input("Please enter new account starting balance: ")

account = create_account.create_account(server,genesis_account,new_account.public_key,balance)
print(f"Transaction hash: {account.response['hash']}")
print(
    f"New Keypair: \n\taccount id: {new_account.public_key}\n\tsecret seed: {new_account.secret}"
)
