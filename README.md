# anki_suspend_duplicates

Suspends duplicate cards from Anki decks.

Unlike the plugin, this project runs outside of the Anki window,
is simpler, and supports arbitrary text files.

## Requirements

- Python 3.8
- The `anki` package installed
- Ubuntu 20.04 LTS (recommended)

## Usage

1. Create the wordlist
2. Suspend the cards

## Wordlist-based Card Suspension

1. Copy the `collection.anki2` file from your Anki profile to the project root
2. Run `cat wordlist.txt | ./suspend_duplicates.py`
3. Make a backup of your Anki profile.
4. Copy the `collection.anki2` in this directory back to your profile, replacing the old one
(but do not overwrite your backup copy)

On Linux, the Anki profile is usually at `~/.local/share/Anki2/User 1/`.

## CJK Text to wordlist

1. Delete `wordlist.txt` if it exists
2. Paste the text into `input.txt`
3. Run `cat input.txt | ./text_to_wordlist.py > wordlist.txt`

Some text that can be used to generate a wordlist can be found at https://forum.duolingo.com/comment/37599030 .
You can just copy and paste the interesting parts with the words.
Non-CJK characters will be filtered out by the script.

## Anki Collection to wordlist

1. Delete `wordlist.txt` if it exists
2. Copy the `collection.anki2` to the project root
3. Run `./collection_to_wordlist.py > wordlist.txt`

You can get the `collection.anki2` by creating a separate profile.
Just create one, import the `.apkg2`s, close Anki, then copy out the `collection.anki2`.

You can also extract the `collection.anki2` database out of a `.apkg` (these are zip files).

## Notes

- **Always make a backup of your Anki collection!**
- Make sure Anki is closed while using this project
- Do not use virtualenv
- The current working directory must be in the root of the Git repo
- Currently only the sort field (which is usually the front of the card) is considered.
This may be a problem if it contains furigana or if alternative definitions are on the back.
