from stellar_sdk import Keypair, Network, Server, TransactionBuilder

server = Server("https://horizon-testnet.stellar.org")

source_secr = 'SD25HQTII44UXZDMBCUKTNBLVYV45RBY635YWP25RFGVCEWM7Z77W26Z'
source_keypair = Keypair.from_secret(source_secr)
source_acc = server.load_account(source_keypair.public_key)

tx_builder = TransactionBuilder(
    source_account = source_acc,
    network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
    base_fee = 100
)


for i in range(100):
    tx_builder.append_bump_sequence_op(
        bump_to = source_acc.sequence + i
    )

tx_builder.set_timeout(30)

tx = tx_builder.build()

tx.sign(source_keypair)
response = server.submit_transaction(tx)
