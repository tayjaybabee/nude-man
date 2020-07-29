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

    parser.add_argument('-d',
                        '--dry-run',
                        action='store_true',
                        default=False,
                        help='Passing this flag will run the program as usual but skips the step at the end where it copies the files it finds.'
                        )

    parser.add_argument('-k',
                        '--api-key',
                        type=str,
                        action='store',
                        help='The API key that you get when you register for free at https://deepai.org/'
                        )

    parser.add_argument('-t',
                        '--threshold',
                        type=float,
                        action='store',
                        default=0.75,
                        help='Any float value between 0.00 and 1.00. If the program gives a photo a "NSFW Score" '
                        'that falls above this number, it will be flagged for sweeping.'
                        )

    parser.add_argument('--data-store',
                        type=str,
                        action='store',
                        required=False,
                        default=f'{str(Path("~/Inspyre-Softworks/NudeMan").expanduser())}',
                        help=f'Provide a directory for NudeMan to store it\'s data in, if you\'re unhappy with the default: {DEFAULT_DATA_DIR}'
                        )

    parser.add_argument("-s",
                        "--source-start",
                        type=str,
                        action="store",
                        default=f'{str(Path("~/Inspyre-Softworks/NudeMan/data/input").expanduser())}',
                        help="Indicate the directory the program should start its scan in",
                        )

    parser.add_argument("-o",
                        "--output-directory",
                        type=str,
                        action='store',
                        default=f'{str(Path("~/Inspyre-Softworks/NudeMan/data/output").expanduser())}',
                        help="Indicate where the files we find should be swept away to."
                        )

    return parser.parse_args()


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(
            f"readable_dir:{path} is not a valid path")
