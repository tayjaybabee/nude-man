"""

A module centering around the argument parser for NudeMan from Inspyre Softworks.

"""
import argparse
import os
from pathlib import Path

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

    return parser.parse_args()


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")



args = parse()

print(args)



#

#
# def parser():
#     parser = argparse.ArgumentParser()
#
#     parser.add_argument(
#             "-s",
#             "--start-dir",
#             type=str,
#             action="store",
#             default=None,
#             help="Indicate the directory the program should start its scan in",
#             )
#
#     parser.add_argument('-p',
#                         '--photo-source-dir',
#                         type=str,
#                         action='store',
#                         required=False,
#                         default=Path('~/Photos').resolve(),
#                         help='The root-directory where you want NudeMan to start looking for photos.'
#
#                         )
#     return parser
