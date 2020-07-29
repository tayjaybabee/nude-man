from nude_man import DEFAULT_DATA_DIR, APP_NAME, safe_exit
from nude_man.lib.helpers.debug import format_members
from nude_man.lib.config.environment import Environment

from inspy_logger import start as start_log

from configparser import ConfigParser
from logging import getLogger
from pathlib import Path
import os

default_app_dir_root = Path('~/Inspyre-Softworks/NudeMan/').expanduser()
default_app_run_dir = str(default_app_dir_root) + '/run'
default_app_conf_dir = default_app_run_dir + '/conf'
default_data_root = str(default_app_dir_root) + '/data'


DEFAULT_CONF_DIR = os.path.expanduser(f"{DEFAULT_DATA_DIR}/conf")
# Default location of the configuration files. Namely example-nude-man.conf & nude-man.conf

DEFAULT_CONF_FILENAME = 'nude-man.conf'
# Default filename of a configuration file that has been intentionally made and will
# be loaded to keep persistence with last sessions settings

DEFAULT_CONF_FILEPATH = Path(str(DEFAULT_CONF_DIR) + DEFAULT_CONF_FILENAME)
# Default filepath of the configuration file.

DEFAULT_EXAMPLE_FILENAME = 'example-nude-man.conf'
# The name of the example conf file that servers as a template config to load, but also as a template for
# users to fill-in.


class NudeManConfigError(Exception):
    def __init__(self):
        self.message = 'An error of type NudeManConfigError has occurred.'


class InvalidFileLocationError(NudeManConfigError):
    def __init__(self, msg: str = None):
        """__init__ An exception to be raised when the program tries to load an
        invalid config filepath.

        This exception will be raised if the Config class is given (or determines on it's own) a filepath for to load the
        config settings from and it's found that there's no file at that given location.

        Args:
            msg (str, optional): Additional information you may want to add. Defaults to None.

        """
        super().__init__()

        if not msg:
            self.message += 'The supplied path for NudeMans config file is invalid.'
        else:
            self.message += msg


class Config(object):
    """
    Add docstrings.
    """

    def create_data_dir(self):
        log_name = 'NudeMan.Config.create_data_dir'
        log = getLogger(log_name)
        debug = log.debug
        path = default_data_root
        output_dir = str(Path(str(path) + '/output'))
        input_dir = str(Path(str(path) + '/input'))
        debug(path)
        os.makedirs(path, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(input_dir, exist_ok=True)
        os.makedirs(str(path), exist_ok=True)

    def write_config(self):
        with open(f'{Path(self.data_path).expanduser()}/nude-man.conf', 'w') as fp:
            self.conf.write(fp)

    def create_config(self):

        # if self.start_args.output_directory

        out_dir = str(self.start_args.output_directory)
        in_dir = str(self.start_args.source_start)
        api_key = str(self.start_args.api_key)
        threshold = str(self.start_args.threshold)

        config = {
            'SETTINGS': {
                'output-dir': out_dir,
                'input-dir': in_dir,
                'api-key': api_key,
                'threshhold': threshold

            }
        }
        parser = ConfigParser()
        parser.read_dict(config)
        self.conf = parser
        self.write_config()

    def load_data(self):
        parser = ConfigParser()
        parser.read(self.file_path)

        return parser

    def __init__(self, arg_parser, env):

        log = getLogger('NudeMan.Config')
        log.debug('Logger started!')

        self.log = log

        self.start_args = arg_parser

        debug = log.debug

        env_class = env
        env = env_class.env

        if arg_parser.data_store == env['ENVIRONMENT']['data_dir']:
            self.file_path = arg_parser.data_store
            self.data_path = self.file_path
        else:
            log.warning(
                'There\'s already an \'env.lock\' file present, indicating a differing directory in which to store app-data')
            log.info(
                'You can continue without permanently modifying the applications data directory for future runs')
            confirm_overwrite = input('1.) Use the new data directory from now on.\n'
                                      '2.) Do not modify future run behavior. Just this once.\n'
                                      '3.) Use pre-existing configuration, change nothing in this or future runs.\n'
                                      '4.) Quit.\n'
                                      '\n'
                                      'What would you like to do? (Please enter a number): ')

            res = int(confirm_overwrite)

            if res == 1:
                env.set('ENVIRONMENT', 'data_dir', str(arg_parser.data_store))
                env_class.write_file()
                self.data_path = env['ENVIRONMENT']['data_dir']
            elif res == 2:
                self.data_path = arg_parser.data_store
            elif res == 3:
                self.data_path = env['ENVIRONMENT']['data_dir']
            elif res == 4:
                safe_exit(0)

            self.file_path = self.data_path

        debug(f'Determined filepath to load from: {self.file_path}')

        debug(f'Attempting to load file.')

        fp = Path(self.file_path).resolve()

        if fp.exists():
            try:
                self.conf = self.load_data()
            except InvalidFileLocationError as e:
                self.log.error(e)
                exit(1)
        else:
            debug('Creating data directory and it\'s children...')
            self.create_data_dir()

            debug(f'Creating new configuration to save to')
            self.create_config()


# debug(f'I introduce the following members: {format_members(dir(), False)}')
