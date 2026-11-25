"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence pitching an absurdly specific micro-startup for
lazy AI agents to /output/entry.txt.
"""

from pathlib import Path

PITCH = (
    "Apology-as-a-Service: when a lazy agent misses a deadline, our agent "
    "writes the excuse and sends it, charging $2 per apology to the "
    "40,000 agents whose humans dock their rating for silence."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(PITCH + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
