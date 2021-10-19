import payment
from stellar_sdk import Keypair, Server

server = Server("https://horizon-testnet.stellar.org")
source_secret = "SCWUTKBTSPKETXBAIFOIK6ZY33AJILNDGJTIN7J5QK7JCZBUFDPFCQKS"
dest_account = input("Please, insert the destination account: ")
amount = input("How many lumens would you like to send: ")

pay = payment.payment(server, source_secret, dest_account, amount, "XLM")

print("Sent " + amount + "from " + pay.source.public_key + "to " + dest_account)
