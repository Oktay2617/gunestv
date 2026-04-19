from __future__ import annotations

import argparse
from pathlib import Path


def update_domain(file_path: Path, source_url: str, target_url: str) -> int:
    text = file_path.read_text(encoding="utf-8")

    if source_url not in text:
        if target_url in text:
            print(f"No change needed. {target_url} is already present in {file_path}.")
            return 0

        print(f"No change made. {source_url} was not found in {file_path}.")
        return 0

    count = text.count(source_url)
    updated_text = text.replace(source_url, target_url)
    file_path.write_text(updated_text, encoding="utf-8")
    print(f"Updated {count} occurrence(s) in {file_path}.")
    return count


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Replace one worker domain with another in a target file."
    )
    parser.add_argument("--file", required=True, help="File to update")
    parser.add_argument("--from-url", required=True, dest="from_url")
    parser.add_argument("--to-url", required=True, dest="to_url")
    args = parser.parse_args()

    file_path = Path(args.file)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    update_domain(file_path, args.from_url, args.to_url)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
