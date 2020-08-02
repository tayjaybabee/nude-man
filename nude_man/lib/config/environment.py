import os
from pathlib import Path
from configparser import ConfigParser
from datetime import datetime


class EnvironmentError(Exception):
    def __init__(self):
        """__init__ An exception to be raised upon the program's discovery of
        an environment error.

        An exception of this type will nearly always have a child type.

        """
        self.message = 'An error of type "EnvironmentError" has occurred!'


class MissingEnvLockError(EnvironmentError):
    def __init__(self):
        super().__init__()
        self.message += '\nWas not able to find environment directory'


class InvalidEnvLockError(EnvironmentError):
    def __init__(self):
        super().__init__()
        self.message += '\nWas able to find env.lock, but it\'s malformed!'
        self.message += "\nIt might be helpful to run NudeMan's configure command again:"
        self.message += '\n    nude-man configure <options>'
        self.message += '\n\nNOTE:\nRunning the above command will wipe your current configuration!'
        self.message += '\n' + str('---->Back it up!<----' * 3)


class Environment(object):
    def __init__(self, arg_parser):
        self.current_filepath = os.path.dirname(os.path.realpath(__file__))
        self.conf_dirpath = str(
            self.current_filepath + str('../' * 3 + 'conf'))
        self.conf_filepath = self.conf_dirpath + '/env.lock'
        self.existing = False

        if Path(self.conf_dirpath).resolve().exists():

            if Path(self.conf_filepath).resolve().is_file():
                self.env = self.load_file()
                self.existing = True
            else:
                self.env = self.create(arg_parser)
        else:
            raise MissingEnvLockError()

    def write_file(self):
        with open(Path(self.conf_filepath).resolve(), 'w') as fp:
            self.env.write(fp)

    def load_file(self):
        fp = Path(self.conf_filepath).resolve()
        c_parser = ConfigParser()
        c_parser.read(fp)
        c_parser.sections()
        if not 'environment'.upper() in c_parser.sections():
            raise InvalidEnvLockError()
        else:
            return c_parser

    def create(self, arg_parser):
        c_parser = ConfigParser()
        env = {
            'ENVIRONMENT': {
                'creation_date': datetime.now(),
                'data_dir': arg_parser.data_store
            }
        }

        c_parser.read_dict(env)
        print(c_parser)

        self.env = c_parser

        try:
            self.write_file()
        except:
            raise

        return c_parser
