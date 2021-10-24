import payment

source_secret = input("Please, insert your source secret seed: ")
dest_account = input("Please, insert the destination account public key: ")
asset = input("What asset do you want to send? Type XLM if you want to send lumens: ")
if asset != "XLM":
    asset_issuer = input("Insert the asset issuer public key: ")
    amount = input("How many " + asset + " would you like to send: ")
    pay = payment.payment(source_secret, dest_account, amount, asset, asset_issuer)
else:
    amount = input("How many " + asset + " would you like to send: ")
    pay = payment.payment(source_secret, dest_account, amount, asset)

print("Sent " + amount + " " + asset + "\nfrom " + pay.source.public_key + "\nto " + dest_account)
