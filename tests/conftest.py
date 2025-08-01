"""
pytest configuration file to set up the Python path for testing.
"""

import sys
import os
from pathlib import Path

# Add the project root directory to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
