from pathlib import Path
import os

# Base directory of the project (2 levels up from this file)
ROOT_DIR = Path(__file__).resolve().parents[2]

# Core directories
DATA_DIR = ROOT_DIR / "data"
ASSETS_DIR = ROOT_DIR / "assets"
SERVICES_DIR = DATA_DIR / "services"

# Default service name (can be overridden via environment variable)
DEFAULT_SERVICE = os.getenv("AURAOPS_SERVICE", "ssp_sp")

# Path to active service data
ACTIVE_SERVICE_DIR = SERVICES_DIR / DEFAULT_SERVICE