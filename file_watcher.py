"""
File Watcher - Monitors /Inbox and moves new files to /Needs_Action
with timestamp prefix and metadata sidecar.
"""

import os
import sys
import time
import shutil
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
INBOX = SCRIPT_DIR / "Inbox"
NEEDS_ACTION = SCRIPT_DIR / "Needs_Action"
POLL_INTERVAL = 2  # seconds


def ensure_folders():
    INBOX.mkdir(exist_ok=True)
    NEEDS_ACTION.mkdir(exist_ok=True)


def build_metadata(original_name, timestamp, dest_path):
    return f"""---
original_name: "{original_name}"
moved_at: "{timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
source: "Inbox"
status: "needs_action"
---

# {original_name}

## Suggested Actions
- [ ] Review this file
- [ ] Rename or categorize appropriately
- [ ] Process contents and file in the correct folder
- [ ] Delete if no longer needed
"""


def process_file(filepath):
    try:
        now = datetime.now()
        timestamp_prefix = now.strftime("%Y%m%d_%H%M%S")
        original_name = filepath.name
        new_name = f"{timestamp_prefix}_{original_name}"

        dest = NEEDS_ACTION / new_name
        shutil.move(str(filepath), str(dest))

        meta_name = dest.stem + ".md"
        meta_path = NEEDS_ACTION / meta_name
        meta_path.write_text(build_metadata(original_name, now, dest), encoding="utf-8")

        print(f"[{now.strftime('%H:%M:%S')}] Moved: {original_name} -> {new_name}")
        print(f"           Metadata: {meta_name}")
    except Exception as e:
        print(f"[ERROR] Failed to process {filepath.name}: {e}")


def watch():
    ensure_folders()
    print(f"Watching: {INBOX}")
    print(f"Destination: {NEEDS_ACTION}")
    print("Press Ctrl+C to stop.\n")

    seen = set()
    # Seed with files already present so we don't re-process them on start
    for f in INBOX.iterdir():
        if f.is_file():
            seen.add(f.name)

    while True:
        try:
            for f in INBOX.iterdir():
                if f.is_file() and f.name not in seen:
                    seen.add(f.name)
                    process_file(f)
            time.sleep(POLL_INTERVAL)
        except KeyboardInterrupt:
            print("\nStopped.")
            sys.exit(0)
        except Exception as e:
            print(f"[ERROR] {e}")
            time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    watch()
