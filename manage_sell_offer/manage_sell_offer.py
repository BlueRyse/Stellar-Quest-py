from stellar_sdk import Keypair, Network, Server, TransactionBuilder, Asset

class manage_sell_offer:

    def __init__(self, source_secr_seed, selling_code, selling_issuer, amount, price, fee = 100):
        self.fee = fee
        self.server = Server("https://horizon-testnet.stellar.org")
        self.source = Keypair.from_secret(source_secr_seed)
        self.source_account = self.server.load_account(account_id=self.source.public_key)
        self.selling_asset = Asset(selling_code, selling_issuer)
        self.buying_asset = Asset.native()
        self.selling_issuer = selling_issuer #public key
        self.amount = amount
        self.price = price
        self.__create_transaction()

    def __create_transaction(self):
        self.transaction = (
            TransactionBuilder(
                source_account = self.source_account,
                network_passphrase = Network.TESTNET_NETWORK_PASSPHRASE,
                base_fee = self.fee
            )
            .append_manage_sell_offer_op(
                selling_code = self.selling_asset.code,
                selling_issuer = self.selling_asset.issuer,
                buying_code = self.buying_asset.code,
                buying_issuer = self.buying_asset.issuer,
                amount = self.amount,
                price = self.price,
                offer_id = 0
            )
            .build()
        )
        self.__execute_transaction()

    def __execute_transaction(self):
        self.transaction.sign(self.source)
        self.response = self.server.submit_transaction(self.transaction)
