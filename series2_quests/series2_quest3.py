from stellar_sdk import Keypair, Network, Server, TransactionBuilder, FeeBumpTransaction
import requests

server = Server("https://horizon-testnet.stellar.org")

source_secr = 'your source secret'
source_keypair = Keypair.from_secret(source_secr)
source_acc = server.load_account(source_keypair.public_key)

url = 'https://friendbot.stellar.org'
fee_payer_keypair = Keypair.random()
response = requests.get(url, params={'addr': fee_payer_keypair.public_key})
fee_payer_acc  = server.load_account(fee_payer_keypair.public_key)

payment_transaction = (
    TransactionBuilder(
        source_account = source_acc,
        network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee = 100
    )
    .append_payment_op(
        destination = source_keypair.public_key,
        amount = "1",
        asset_code = "XLM"
    )
    .build()
)

payment_transaction.sign(source_keypair)

fee_bump_transaction = (
    TransactionBuilder.build_fee_bump_transaction(
        fee_source = fee_payer_keypair.public_key,
        base_fee = 100,
        inner_transaction_envelope = payment_transaction
    )
)

fee_bump_transaction.sign(fee_payer_keypair)
response = server.submit_transaction(fee_bump_transaction)
