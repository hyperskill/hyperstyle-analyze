import sys
from pathlib import Path

MAIN_FOLDER = Path(__file__)
HYPERSTYLE_PATH = f'{MAIN_FOLDER.parent.parent}/main/venv/src'
sys.path.append(HYPERSTYLE_PATH)
