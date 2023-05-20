import argparse
import random
import re


def search_for_blocks(filename):
    # read the file
    with open(filename, "r") as file:
        contents = file.read()

    # define the regular expression pattern
    pattern = r'\[Event "[^"]+"\](?:\n\[.+\])+'

    # find all matches in the contents
    matches = re.findall(pattern, contents)

    # shuffle the matches in random order
    random.shuffle(matches)

    # open the output file
    with open("output.pbn", "w") as file:
        # iterate over the shuffled matches
        for i, match in enumerate(matches, start=1):
            block = match[1:]

            # set the [Board "..."] to the respective number
            board_number = f'[Board "{i}"]'

            # replace [Board "..."] with the updated number
            block = re.sub(r'\[Board "[^"]+"]', board_number, block)

            # write the match to the output file
            file.write(f"[{block}\n\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', type=str, required=True)
    args = parser.parse_args()
    search_for_blocks(args.file)
