from stellar_sdk import Keypair, Network, Server, TransactionBuilder

server = Server("https://horizon-testnet.stellar.org")

source_secr = 'your source'
source_keypair = Keypair.from_secret(source_secr)
source_acc = server.load_account(source_keypair.public_key)

new_sponsored_account = Keypair.random()

transaction = (
    TransactionBuilder(
        source_account = source_acc,
        network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee = 100
    )
    .add_text_memo("Begin Sponsoring")
    .append_begin_sponsoring_future_reserves_op(
        sponsored_id = new_sponsored_account.public_key
    )
    .append_create_account_op(new_sponsored_account.public_key, "1")
    .append_end_sponsoring_future_reserves_op(
        source = new_sponsored_account.public_key
    )
    .set_timeout(30)
    .build()
)

transaction.sign(source_keypair)
transaction.sign(new_sponsored_account)
response = server.submit_transaction(transaction)
