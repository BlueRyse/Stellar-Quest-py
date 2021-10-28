from stellar_sdk import Keypair, Network, Server, TransactionBuilder, Asset
import requests

server = Server("https://horizon-testnet.stellar.org")

source_secr = 'your source secret'
source_keypair = Keypair.from_secret(source_secr)
source_acc = server.load_account(source_keypair.public_key)

source_acc.increment_sequence_number() #since this transaction is happening in the "future" we need to increment the sequence once

keypair = Keypair.random() #let's pay this account
url = 'https://friendbot.stellar.org'
response = requests.get(url, params={'addr': keypair.public_key})

payment_tx = (
    TransactionBuilder(
        source_account = source_acc, #incremented sequence
        network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee = 100
    )
    .append_payment_op(
        destination = keypair.public_key,
        asset_code = 'XLM',
        amount = '1'
    )
    .set_timeout(30)
    .build()
)

pre_auth_tx_h = payment_tx.hash()

set_options_tx = (
    TransactionBuilder(
        source_account = server.load_account(source_keypair.public_key), #we need the old sequence
        network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee = 100
    )
    .append_pre_auth_tx_signer(
        pre_auth_tx_hash = pre_auth_tx_h,
        weight = 1
    )
    .set_timeout(30)
    .build()
)

set_options_tx.sign(source_keypair)

response = server.submit_transaction(set_options_tx)

response = server.submit_transaction(payment_tx)
