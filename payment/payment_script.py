import payment

source_secret = "your secret seed"
dest_account = input("Please, insert the destination account public key: ")
amount = input("How many lumens would you like to send: ")
asset = input("What asset you want to send? Type XLM if you want to send lumens")
pay = payment.payment(source_secret, dest_account, amount, asset)

print("Sent " + amount + " XLM \nfrom " + pay.source.public_key + "\nto " + dest_account)
