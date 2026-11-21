from pathlib import Path

JOKE = "I asked my AI agent to fix the demo crash; it deleted the demo, kept the crash, and gave it 100% test coverage."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
