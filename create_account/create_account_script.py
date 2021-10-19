import create_account
from stellar_sdk.server import Server

server = Server("https://horizon-testnet.stellar.org")
genesis_account = "your_genesis"
new_account_public_ID = input("Please enter the new account Public ID: ")
balance = input("Please enter new account starting balance: ")

account = create_account.create_account(server,genesis_account,new_account_public_ID,balance)

print(f"Transaction hash: {account.response['hash']}")
print(
    f"Account created: \n\taccount id: {new_account_public_ID}"
)
