import payment

source_secret = "SCWUTKBTSPKETXBAIFOIK6ZY33AJILNDGJTIN7J5QK7JCZBUFDPFCQKS"
dest_account = input("Please, insert the destination account public key: ")
amount = input("How many lumens would you like to send: ")

pay = payment.payment(source_secret, dest_account, amount, "XLM")

print("Sent " + amount + " XLM \nfrom " + pay.source.public_key + "\nto " + dest_account)
