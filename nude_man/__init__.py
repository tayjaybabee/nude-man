from nude_man.lib.helpers.debug import format_members

from logging import getLogger

__version__ = '0.1.0'

DEFAULT_DATA_DIR = '~/Inspyre-Softworks/NudeMan'
APP_NAME = 'NudeMan'

log_name = str(f'{APP_NAME}.Main')
log = getLogger(log_name)
debug = log.debug
debug(f'Imported {__file__}!')


def safe_exit(exit_reason: str, code: int):
    log.info('Received call for a safe exit')
    if code:
        log.error(
            'This exit is due to a program exception. Please see program logs')
        exit(1)
    else:
        log.info('Program is exiting expectedly, no errors detected.')


debug(f'I introduce the following members: {format_members(dir(), False)}')
