import payment
from stellar_sdk import Keypair

source_secret = "your source secret seed"
dest_account = input("Please, insert the destination account: ")
amount = input("How many lumens would you like to send: ")

pay = payment.payment(source_secret, dest_account, amount, "XLM")

print("Sent " + amount + " XLM \nfrom " + pay.source.public_key + "\nto " + dest_account)
