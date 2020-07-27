"""

A module centering around the argument parser for NudeMan from Inspyre Softworks.

"""
import argparse
import os
from pathlib import Path
from nude_man.lib.config import DEFAULT_DATA_DIR


def parse():
    parser = argparse.ArgumentParser('nude-man', description="Automatically sort through your pictures and quickly/easily "
                                     "get them moved to a more suitable location; should help prevent "
                                     "accidental indecent exposure, but I make no guarantees.")

    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        required=False,
        default=False,
        help='Enable verbose output to the console.'
    )

    parser.add_argument("-s",
                        "--source-start",
                        type=str,
                        action="store",
                        help="Indicate the directory the program should start its scan in",
                        )

    parser.add_argument("-o",
                        "--output-directory",
                        type=dir_path,
                        action='store',
                        help="Indicate where the files we find should be swept away to."
                        )

    parser.add_argument('-k',
                        '--api-key',
                        type=str,
                        action='store',
                        help='The API key that you get when you register for free at https://deepai.org/')

    parser.add_argument('-d',
                        '--data-store',
                        type=str,
                        action='store',
                        required=False,
                        default=f'{Path("~/Inspyre-Softworks/NudeMan").expanduser()}',
                        help=f'Provide a directory for NudeMan to store it\'s data in, if you\'re unhappy with the default: {DEFAULT_DATA_DIR}')

    return parser.parse_args()


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(
            f"readable_dir:{path} is not a valid path")
