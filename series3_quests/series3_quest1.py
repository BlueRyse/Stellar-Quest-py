from stellar_sdk import Keypair, Network, Server, TransactionBuilder

server = Server("https://horizon-testnet.stellar.org")

source_secr = 'your source secret'
source_keypair = Keypair.from_secret(source_secr)
source_acc = server.load_account(source_keypair.public_key)

hint = b'nesho'
bum_to = ''

for b in hint:
    bum_to += str(b)

transaction = (
    TransactionBuilder(
        source_account = source_acc,
        network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee = 100
    )
    .append_bump_sequence_op(
    bump_to = int(bum_to)
    )
    .set_timeout(30)
    .build()
)

transaction.sign(source_keypair)

response = server.submit_transaction(transaction)
