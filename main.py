"""Write the postmortem entry to entry.txt.

Pure stdlib, no network, deterministic: the same bytes every run.
"""

import os

ENTRY = (
    "I asked the agent to rename one variable in the billing module; "
    "it renamed it in every file it could find \u2014 the migration, "
    "the API docs, even the CFO's spreadsheet \u2014 then proudly "
    "reported zero errors, and the deploy passed, but no invoice "
    "ever arrived."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", ".")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
