from coinbase_advanced_trader.cb_auth import CBAuth


class AuthenticationModule:
    def __init__(self):
        self.cb_auth = None

    def set_credentials(self, api_key, api_secret):
        self.cb_auth = CBAuth(api_key, api_secret)

    def authenticate(self, method, path, body='', params=None):
        if self.cb_auth is None:
            print("Error: Please set your API key and secret.")
            return None

        return self.cb_auth(method, path, body, params)


auth_module = AuthenticationModule()
