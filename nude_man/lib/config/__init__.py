from nude_man import DEFAULT_DATA_DIR, APP_NAME
from nude_man.lib.helpers.debug import format_members
from nude_man.lib.config.environment import check_environment

from configparser import ConfigParser
from logging import getLogger
from pathlib import Path
import os

DEFAULT_CONF_DIR = os.path.expanduser(f"{DEFAULT_DATA_DIR}/conf")
# Default location of the configuration files. Namely example-nude-man.conf & nude-man.conf

DEFAULT_CONF_FILENAME = 'nude-man.conf'
# Default filename of a configuration file that has been intentionally made and will
# be loaded to keep persistence with last sessions settings

DEFAULT_EXAMPLE_FILENAME = 'example-nude-man.conf'
# The name of the example conf file that servers as a template config to load, but also as a template for
# users to fill-in.

log_name = str(f'{APP_NAME}.{__file__}')
log = getLogger(log_name)
debug = log.debug
debug(f'Logger initialized for {log_name}')


class NudeManConfigError(Exception):
    def __init__(self):
        self.message = 'An error of type NudeManConfigError has occurred.'


class InvalidFileLocationError(NudeManConfigError):
    def __init__(self, msg: str = None):
        """__init__ An exception to be raised when the program tries to load an invalid config filepath.

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
    """Add docstrings."""

    def create_data_dir():
        pass

    def load_file(self):
        """load_file Load NudeMans config file from the disk.

        Load the configuration file for NudeMan. This will work whether you're attempting to load an already-in-use
        config file or example-nude-man.conf. In most cases you will not have to call this function directly as it's
        called when the :class:Config class is initialized

        Returns:
            ConfigParser: A ConfigParser object that contains our config loaded from the disk.
        """
        if os.path.exists(self.file_path):
            parser = ConfigParser()
            parser.read(self.file_path)
            return parser
        else:
            raise InvalidFileLocationError(
                msg=f'{self.file_path} is not a valid configuration file location.')

    def __init__(self, file_path=None):

        self.log_name = f'{APP_NAME}.Config'
        self.log = getLogger(log_name)
        debug = self.log.debug

        if not file_path:
            self.dir_path = DEFAULT_DATA_DIR + '/run/conf'
            self.file_name = 'nude-man'
            self.file_ext = 'conf'
            self.file_path = Path(
                self.dir_path + f'/{self.file_name}.{self.file_ext}')
        else:
            self.file_path = Path(file_path)

        debug(f'Determined filepath to load from: {self.file_path}')

        debug(f'Attempting to load file.')
        try:
            self.conf = self.load_file()
        except InvalidFileLocationError as e:
            self.log.error(e)
            exit(1)


debug(f'I introduce the following members: {format_members(dir(), False)}')
