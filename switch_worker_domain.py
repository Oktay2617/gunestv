from __future__ import annotations

import argparse
from pathlib import Path


def update_domain(file_path: Path, source_url: str, target_url: str) -> int:
    text = file_path.read_text(encoding="utf-8")
    original_text = text

    # 1. Normal replacement
    if source_url in text:
        count = text.count(source_url)
        text = text.replace(source_url, target_url)
        print(f"✅ Updated {count} occurrence(s): {source_url} → {target_url}")
    
    # 2. Zaten hedef URL varsa değişiklik yapma
    elif target_url in text:
        print(f"ℹ️  No change needed. Already using target URL: {target_url}")
        return 0
    
    # 3. Hiçbiri yoksa uyarı ver
    else:
        print(f"⚠️  WARNING: Neither source nor target URL found in {file_path}")
        print(f"   Looking for: {source_url}")
        print(f"   Target was : {target_url}")
        # Debug için mevcut domainleri göster
        if "oktay2617" in text:
            print("\nFound oktay2617 domains in file:")
            for line in text.splitlines():
                if "oktay2617" in line:
                    print("   ", line.strip()[:120])
        return 0

    # Değişiklik varsa kaydet
    if text != original_text:
        file_path.write_text(text, encoding="utf-8")
        print(f"💾 File saved: {file_path}")
        return text.count(target_url)
    
    return 0


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
