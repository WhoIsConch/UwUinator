import argparse
from uwuinator import UwUinator
import os
import sys
import asyncio

arg_parser = argparse.ArgumentParser(
    prog = "uwuinator",
    description = "The UwUinator",
    usage = "uwuinator [options]",
    )

arg_parser.add_argument(
    'path',
    type = str,
    help = "The path to the directory to UwUinate."
)

arg_parser.add_argument(
    '-f',
    '--file',
    type = str,
    help = "The file to make the UwUinator copy.",
    required=False
)

arg_parser.add_argument(
    '-a',
    '--amount',
    type = int,
    help = "The amount of storage, in megabytes, to UwUinate.",
    required=False
)

args = arg_parser.parse_args()

if not os.path.exists(args.path):
    print(f"The specified path, \"{args.path}\", does not exist.")
    sys.exit(1)

if args.file and not os.path.exists(args.file):
    print(f"The specified file, \"{args.file}\", does not exist.")
    sys.exit(1)

if args.amount and args.amount < 1:
    print("The amount of storage must be greater than 0.")
    sys.exit(1)


asyncio.run(UwUinator.start(**vars(args)))
