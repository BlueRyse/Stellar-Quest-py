from stellar_sdk import Keypair, Network, Server, TransactionBuilder

server = Server("https://horizon-testnet.stellar.org")

source_secr = 'your source secret'
source_keypair = Keypair.from_secret(source_secr)
source_acc = server.load_account(source_keypair.public_key)

sponsored_public = 'public id of sponsored account'
#sponsored_public = "the public id of the sponsored account"

transaction = (
    TransactionBuilder(
        source_account = source_acc,
        network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee = 100
    )
    .add_text_memo("Revoke Sponsorship")
    .append_revoke_account_sponsorship_op(
        account_id = sponsored_public
    )
    .set_timeout(30)
    .build()
)

transaction.sign(source_keypair)
response = server.submit_transaction(transaction)
