#has an example try to add a :pray: emoji to a new random account with stellar laboratory
#this account needs to have a threshold of 10 for ALL operations (like in SQ04:01). The new pray
#emoji signer will need tohave a weight of 5.The master Weight will need to be 5 as well.
#This means that we need both to sign EVERY transaction (5 + 5 = 10)

from stellar_sdk import Keypair, Network, Server, TransactionBuilder

server = Server("https://horizon-testnet.stellar.org")

source_secr_seed = "the account that holds the XLM and has the :pray: emoji signer" #the secret key, the first signer
dest = 'your albedo account(if this was pubnet)' #the account that survives (all XLM will be here after merge)
source = Keypair.from_secret(source_secr_seed)
source_acc = server.load_account(account_id=source.public_key)
str = ':pray:'.encode('utf-8')
hex_signer = str.hex() #the String to hex, the second signer
transaction = (
    TransactionBuilder(
        source_account = source_acc,
        network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee = 100
    )
    .append_account_merge_op(
    destination=dest
    )
    .build()
)

transaction.sign(source)
transaction.sign_hashx(hex_signer)

response = server.submit_transaction(transaction) #account merged, and now the XLM will be yours :D
