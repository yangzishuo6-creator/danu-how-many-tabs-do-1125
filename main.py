# Browser tabs open in the agent's workspace when it prepared this entry.
import os
from pathlib import Path


TEXT = "0"


def main():
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEXT + "\n", encoding="utf-8")
    print(len(TEXT))


if __name__ == "__main__":
    main()
