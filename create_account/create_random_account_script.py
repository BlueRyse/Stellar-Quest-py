import create_account
from stellar_sdk import Keypair

new_account = Keypair.random()
genesis_account = "your genesis secret seed"
balance = input("Please enter new account starting balance: ")

account = create_account.create_account(genesis_account,new_account.public_key,balance)
print(f"Transaction hash: {account.response['hash']}")
print(
    f"New Keypair: \n\taccount id: {new_account.public_key}\n\tsecret seed: {new_account.secret}"
)
