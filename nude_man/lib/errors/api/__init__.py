class APIError(Exception):
    def __init__(self):
        self.api_url = 'https://deepai.org'
        self.message = 'An error of type APIError has occurred'


class KeyMissingError(APIError):
    def __init__(self):
        super().__init__()
        self.message += f'\nThere is no API key from {self.api_url} configured in nude-man.conf.'
        self.message += '\nRun "nude-man configure" or edit nude-man.conf'


class InvalidKeyError(APIError):
    def __init__(self, key):
        super().__init__()
        self.message += '\nInvalid API Key in specified in configuration file!'
        self.message += f'\nCurrently configured key: {key}'
