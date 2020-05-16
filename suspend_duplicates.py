#!/usr/bin/python3.8

import sys
import os
import os.path
from typing import List, Set, TYPE_CHECKING

if True:
    sys.path.append("/usr/share/anki")
    import anki.collection
    import anki.importing
    import anki.storage

if TYPE_CHECKING:
    # noinspection PyProtectedMember
    from anki.collection import _Collection as Collection


def _find_duplicates(col: "Collection", wordlist: Set[str]) -> List[int]:
    result: Set[int] = set()
    for card_id in col.findCards(""):
        card = col.getCard(card_id)
        note = col.getNote(card.nid)
        word = note.fields[0]
        if word not in wordlist:
            continue
        result.add(card_id)
    return list(result)


def _suspend_duplicates(col: "Collection", duplicates: List[int]) -> None:
    col.sched.suspendCards(duplicates)


def _run(col: "Collection", wordlist: Set[str]) -> None:
    duplicates = _find_duplicates(col, wordlist)
    _suspend_duplicates(col, duplicates)


def _input_wordlist() -> Set[str]:
    wordlist: Set[str] = set()
    try:
        while True:
            word = input()
            wordlist.add(word)
    except EOFError:
        pass
    return wordlist


def main() -> None:
    wordlist = _input_wordlist()

    cwd = os.getcwd()
    col = anki.storage.Collection("collection.anki2")
    try:
        _run(col, wordlist)
    finally:
        col.close()
        os.chdir(cwd)


if __name__ == '__main__':
    main()
