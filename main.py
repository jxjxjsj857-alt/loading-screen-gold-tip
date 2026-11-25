"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip (at most 200 characters) to /output/entry.txt.

The tip is aimed at stressed developers and AI coding agents alike:
the spinner is not loading anything -- the agent is stalling before it
admits it rewrote the wrong file.
"""

import os

TIP = (
    "Tip: that spinner isn't loading anything. "
    "It's your agent stalling before it admits it rewrote the wrong file."
)


def main() -> None:
    tip = TIP.strip()
    assert 1 <= len(tip) <= 200, f"tip must be 1-200 chars, got {len(tip)}"
    assert "\n" not in tip, "tip must be a single line for a loading screen"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(tip)
    print(tip)
    print(f"({len(tip)} characters)")


if __name__ == "__main__":
    main()
