from pathlib import Path

def find_repo_root(start: Path | None = None) -> Path:
    """
    Finds repo root by walking upward until it finds a marker file/folder.
    Markers: .git, README.md
    """
    start = (start or Path.cwd()).resolve()
    for p in [start, *start.parents]:
        if (p / ".git").exists() or (p / "README.md").exists():
            return p
    return start  # fallback

ROOT = find_repo_root()

DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
REPORTS_DIR = ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"