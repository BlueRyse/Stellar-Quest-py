from stellar_sdk import Keypair, Network, Server, TransactionBuilder

server = Server("https://horizon-testnet.stellar.org")
asset_iss = 'SCWUTKBTSPKETXBAIFOIK6ZY33AJILNDGJTIN7J5QK7JCZBUFDPFCQKS'
asset_cd = 'ser2Quest2'
source_secret = 'SCYJGZX26FFGG4UA25VWG6B3T6L7LBA2CPN4X62X5BIRHKE4BUJKJVNG'
lim = '100'

source_keypair = Keypair.from_secret(source_secret)
asset_issuer_keypair = Keypair.from_secret(asset_iss)
source_acc = server.load_account(account_id = source_keypair.public_key)

transaction = (
    TransactionBuilder(
        source_account = source_acc,
        network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee = 100
    )
    .add_text_memo("Series 2 quest 2")
    .append_change_trust_op(
        asset_issuer = asset_issuer_keypair.public_key,
        asset_code = asset_cd,
        limit = lim
    )
    .append_payment_op(
        destination = source_keypair.public_key,
        asset_code = asset_cd,
        asset_issuer = asset_issuer_keypair.public_key,
        amount = "1",
        source = asset_issuer_keypair.public_key
    )
    .set_timeout(30)
    .build()
)

transaction.sign(source_keypair)
transaction.sign(asset_issuer_keypair)

response = server.submit_transaction(transaction)
