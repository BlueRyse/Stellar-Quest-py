from stellar_sdk import Keypair, Network, Server, TransactionBuilder, Asset

class payment:
    def __init__(self, source_secr_seed, dest_account_pb, amount, asset, asset_issuer = None, fee = 100):
        if asset == "XLM":
            self.asset = Asset.native()
        else:
            self.asset = Asset(asset, asset_issuer)
        self.fee = fee
        self.server = Server("https://horizon-testnet.stellar.org")
        self.source = Keypair.from_secret(source_secr_seed)
        self.source_account = self.server.load_account(account_id=self.source.public_key)
        self.dest_account = Keypair.from_public_key(dest_account_pb)
        self.amount = amount
        self.__create_transaction()

    def __create_transaction(self):
        self.transaction = (
            TransactionBuilder(
                source_account = self.source_account,
                network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
                base_fee = self.fee
            )
         .add_text_memo("Test_transaction")
         .append_payment_op(
            destination = self.dest_account.public_key,
            asset_code = self.asset.code,
            asset_issuer = self.asset.issuer,
            amount = self.amount
        )
         .set_timeout(30)  # Make this transaction valid for the next 30 seconds only
         .build()
        )
        self.__execute_transaction()

    def __execute_transaction(self):
        self.transaction.sign(self.source)
        self.response = self.server.submit_transaction(self.transaction)
