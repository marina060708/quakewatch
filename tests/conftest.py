# tests/conftest.py
# Ensure project root is on sys.path so `import app` works in CI runners.
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
