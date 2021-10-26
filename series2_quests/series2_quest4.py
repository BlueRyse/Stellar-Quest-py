from stellar_sdk import Keypair, Network, Server, TransactionBuilder, ClaimPredicate, Claimant, Asset

server = Server("https://horizon-testnet.stellar.org")

source_secr = 'SCYJGZX26FFGG4UA25VWG6B3T6L7LBA2CPN4X62X5BIRHKE4BUJKJVNG'
source_keypair = Keypair.from_secret(source_secr)
source_acc = server.load_account(source_keypair.public_key)

predicate = ClaimPredicate.predicate_not(ClaimPredicate.predicate_before_relative_time(120))

claimant = Claimant(source_keypair.public_key, predicate)

claimants_list = [claimant]

transaction = (
    TransactionBuilder(
        source_account = source_acc,
        network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee = 100
    )
    .add_text_memo("Create Claimable balance")
    .append_create_claimable_balance_op(
        asset = Asset.native(),
        amount = '100',
        claimants = claimants_list
    )
    .set_timeout(30)
    .build()
)

transaction.sign(source_keypair)
response = server.submit_transaction(transaction)
