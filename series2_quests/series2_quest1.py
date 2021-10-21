import create_account, hashlib, requests
from stellar_sdk import Keypair, Server, Network,TransactionBuilder


server = Server("https://horizon-testnet.stellar.org")

account_pb = "you account public key"
string = "Stellar Quest Series 2"
hash = hashlib.sha256(string.encode('utf-8')).hexdigest()

source=Keypair.random() #account that funds the new one
url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': source.public_key})
source_account = server.load_account(account_id = source.public_key)

transaction = (
    TransactionBuilder(
        source_account = source_account,
        network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee = 100
    )
    .add_hash_memo(hash)
    .append_create_account_op(
        destination=account_pb,
        starting_balance = "5000"
    )
    .build()
)

transaction.sign(source)
response = server.submit_transaction(transaction)

print(f"Transaction hash: {response['hash']}")
