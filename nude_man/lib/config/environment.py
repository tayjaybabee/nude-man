import os
from pathlib import Path
from configparser import ConfigParser
from datetime import datetime

env_file = Path(str(env_dir) + '/env.lock')


class EnvironmentError(Exception):
    def __init__(self):
        self.message = 'An error of type "EnvironmentError" has occurred!'


class MalformedEnvironmentError(EnvironmentError):
    def __init__(self):
        super().__init__()
        self.message += f'Was not able to find {env_dir}'


def write_env_file(env):
    with open(env_file, 'w') as fp:
        env.write(fp)


def create_env(args_parser):
    c_parser = ConfigParser()
    env = {
        'ENVIRONMENT': {
            'creation_date': datetime.now(),
            'data_dir': args_parser.data_store
        }
    }

    c_parser.read_dict(env)
    try:
        write_env_file(env)
    except:
        raise

    return c_parser


class Environment(object):
    def __init__(self, args_parser):
        self.current_filepath = os.path.dirname(os.path.realpath(__file__))
        self.conf_dirpath = str(
            self.current_filepath + str('../' * 3 + 'conf'))

        if Path(self.conf_dirpath).resolve().exists():
            if Path(self.current_filepath).resolve().is_file():
                self.load_file
            else:
                self.create()
        else:
            raise MalformedEnvironmentError()

    def load_file():
        pass

    def create():
        c_parser = ConfigParser()
        env = {
            'ENVIRONMENT': {
                'creation_date': datetime.now(),
                'data_dir': args_parser.data_store
            }
        }

        c_parser.read_dict(env)
        try:
            write_env_file(env)
        except:
            raise

        return c_parser


def init_env(args_parser):
    environment =
