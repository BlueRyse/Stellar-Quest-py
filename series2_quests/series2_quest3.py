from stellar_sdk import Keypair, Network, Server, TransactionBuilder
import requests

server = Server("https://horizon-testnet.stellar.org")

source_secr = 'SCYJGZX26FFGG4UA25VWG6B3T6L7LBA2CPN4X62X5BIRHKE4BUJKJVNG'
source_keypair = Keypair.from_secret(source_secr)

url = 'https://friendbot.stellar.org'
fee_channel_keypair = Keypair.random()
response = requests.get(url, params={'addr': fee_channel_keypair.public_key})
source_acc  = server.load_account(fee_channel_keypair.public_key)

transaction = (
    TransactionBuilder(
        source_account = source_acc,
        network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee = 100
    )
    .add_text_memo("Bump sequence operation")
    .append_bump_sequence_op(
        bump_to = source_acc.sequence + 1,
        source = source_keypair.public_key
    )
    .set_timeout(30)
    .build()
)

transaction.sign(source_keypair)
transaction.sign(fee_channel_keypair)

repsonse = server.submit_transaction(transaction)