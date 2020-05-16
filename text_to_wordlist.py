#!/usr/bin/python3.8

import unicodedata
from typing import Iterable


def _get_words(line: str) -> Iterable[str]:
    """Gets desired words such as Japanese ones, excluding undesired ones such as English ones."""
    if not line:
        return
    last_idx = -1
    idx = 0
    for idx in range(len(line)):
        char = line[idx]
        if unicodedata.category(char) != "Lo":
            # The enclosing conditional ends the word upon seeing non-Lo characters such as:
            # - Spaces and commas
            # - Latin letters
            # "Lo" (Letter other) isn't really CJK, but it's good enough
            if last_idx + 1 < idx:
                yield line[last_idx + 1:idx]
            last_idx = idx
    if last_idx < idx:
        yield line[last_idx + 1:]


def main() -> None:
    try:
        while True:
            line = input()
            wordlist = list(_get_words(line))
            if not wordlist:
                continue
            print(*wordlist, sep="\n")
    except EOFError:
        pass


if __name__ == '__main__':
    main()
