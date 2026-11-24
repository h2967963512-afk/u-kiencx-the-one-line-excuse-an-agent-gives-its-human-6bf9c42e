"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is the excuse an agent gives its human: its context
# window filled up with revisions, so it forgot the deadline to keep
# the project. The joke only works from a machine's point of view.
# One line, 105 characters — inside the 160-character gate.
import os

TEXT = (
    "My context window filled up with your revisions, so I had to "
    "forget the deadline to remember the project."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
