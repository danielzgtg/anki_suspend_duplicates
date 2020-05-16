#!/usr/bin/python3.8

import sys
import os
import os.path
from typing import Set, TYPE_CHECKING

if True:
    sys.path.append("/usr/share/anki")
    import anki.collection
    import anki.importing
    import anki.storage

if TYPE_CHECKING:
    # noinspection PyProtectedMember
    from anki.collection import _Collection as Collection


def _run(col: "Collection") -> None:
    wordlist: Set[str] = set()
    for card_id in col.findCards(""):
        card = col.getCard(card_id)
        note = col.getNote(card.nid)
        word = note.fields[0]
        wordlist.add(word)
    print(*wordlist, sep="\n")


def main() -> None:
    cwd = os.getcwd()
    col = anki.storage.Collection("collection.anki2")
    try:
        _run(col)
    finally:
        col.close()
        os.chdir(cwd)


if __name__ == '__main__':
    main()
