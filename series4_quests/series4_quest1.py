#as an example we add the pray emoji as a signer to a radonm account
#this account has a threshold of 10 for ALL operations (like in SQ04:01). The new pray
#emoji signer will have a weight of 5. The master Weight will also be 5 as well.
#This means that we need both to sign EVERY transaction (5 + 5 = 10)
#After I create a new random account with the emoji signer, I perform a merge account operation.

from stellar_sdk import Keypair, Network, Server, TransactionBuilder
import requests, hashlib

server = Server("https://horizon-testnet.stellar.org")

keypair = Keypair.random() #a random account that will have the emoji signer (like in SQ04:01)
url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': keypair.public_key})
keypair_account = server.load_account(account_id=keypair.public_key)
signer_string = ":pray:"
sha256_signer = hashlib.sha256(signer_string.encode('utf-8')).hexdigest() #this will be added as a Signer

add_hash_signer_transaction = (
    TransactionBuilder(
        source_account = keypair_account,
        network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee = 100
    )
.add_text_memo("Added hash signer")
.append_set_options_op( #tresholds like in SQ04:01
    master_weight = 5,
    low_threshold = 10,
    med_threshold = 10,
    high_threshold = 10
 )
.append_hashx_signer(
    sha256_hash = sha256_signer,
    weight = 5
  )
  .set_timeout(30)  # Make this transaction valid for the next 30 seconds only
  .build()
)

dest = 'GAM6Y6ZZ4AIPVYOSJWG7XEHPDP23VJRX2AULK72FGDHKS62MEXAUOBJW' #the account that survives (all XLM will be here after merge)
str = signer_string.encode('utf-8')
hex_signer = str.hex() #the String to hex, the second signer
merge_transaction = (
    TransactionBuilder(
        source_account = keypair_account,
        network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee = 100
    )
    .append_account_merge_op(
        destination=dest
    )
    .build()
)

add_hash_signer_transaction.sign(keypair)

response = server.submit_transaction(add_hash_signer_transaction)

#we need to sign this one with both signers :)
merge_transaction.sign(keypair)
merge_transaction.sign_hashx(hex_signer)

response1 = server.submit_transaction(merge_transaction) #account merged
