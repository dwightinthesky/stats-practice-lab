from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
FILES = ("index.html", "styles.css", "app.js", "questions.js")


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True, exist_ok=True)

    for name in FILES:
        shutil.copy2(ROOT / name, DIST / name)

    print(f"Prepared deployable site in {DIST}")


if __name__ == "__main__":
    main()
