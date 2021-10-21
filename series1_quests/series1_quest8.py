from stellar_sdk import Keypair, Network, Server, TransactionBuilder, Asset

server = Server("https://horizon-testnet.stellar.org")

source_secret = "SDI6W7JR2R4DBWUXSB3CPQTGNYT5IIRKJ757RMD2QDXLJF7BMHWIHPOI"
source_keypair = Keypair.from_secret(source_secret)
account = server.load_account(account_id=source_keypair.public_key)

path_list=[]

transaction = (
    TransactionBuilder(
        source_account = account,
        network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee = 100
    )
    .add_text_memo("Channel transaction")
    .append_path_payment_strict_send_op(
    destination = source_keypair.public_key, #we are sending a payment to the same account that pays the fees
    send_code = "XLM",
    send_issuer = Asset.native().issuer,
    send_amount = "1",
    dest_code = "SRT",
    dest_issuer = "GCDNJUBQSX7AJWLJACMJ7I4BC3Z47BQUTMHEICZLE6MU4KQBRYG5JY6B",
    dest_min = "1",
    path = path_list
    )
    .set_timeout(30)
    .build()
)

#we need to sign with both accounts
transaction.sign(source_keypair)

response = server.submit_transaction(transaction)
