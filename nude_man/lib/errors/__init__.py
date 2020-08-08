class ApplicationError(Exception):
    def __init__(self, docs=None, err=None):
        if err is None:
            self.error_type = __class__.__name__
        else:
            self.error_type = err

        self.initial_msg = f'NudeMan has suffered an internal application error of type: {self.error_type}'

        self.message = self.initial_msg + '\n'

        if docs is None:
            self.docs_base = 'https://gitlab.com/tayjaybabee/nude-man'
            self.docs = self.docs_base
        else:
            self.docs = docs



class InvalidArgumentTypeError(ApplicationError):
    def __init__(self, docs=None, msg=None):
        super().__init__(docs=docs, err=__class__.__name__)
        if msg is None:
            self.message = self.message + self.docs
        else:
            self.message = self.message + msg + f'\n{self.docs}'



