from stellar_sdk import Keypair, Network, Server, TransactionBuilder

class change_trust:
    def __init__(self, asset_issuer, asset_code, source, limit, fee = 100):
        self.server = Server("https://horizon-testnet.stellar.org")
        self.asset_issuer = asset_issuer
        self.asset_code = asset_code
        self.source = Keypair.from_secret(source)
        self.source_account = self.server.load_account(account_id=self.source.public_key)
        self.limit = limit
        self.fee = fee
        self.__create_transaction()

    def __create_transaction(self):
        self.transaction = (
            TransactionBuilder(
                source_account = self.source_account,
                network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
                base_fee = self.fee
            )
         .add_text_memo("Change trust")
         .append_change_trust_op(
            asset_issuer = self.asset_issuer,
            asset_code = self.asset_code,
            limit = self.limit
        )
         .set_timeout(30)  # Make this transaction valid for the next 30 seconds only
         .build()
        )
        self.__execute_transaction()

    def __execute_transaction(self):
        self.transaction.sign(self.source)
        self.response = self.server.submit_transaction(self.transaction)
