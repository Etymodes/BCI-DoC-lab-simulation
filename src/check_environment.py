import sys
import platform
import importlib.util
from datetime import datetime
from pathlib import Path


def check_package(package_name: str) -> str:
    spec = importlib.util.find_spec(package_name)
    return "OK" if spec is not None else "MISSING"


def main():
    packages = [
        "numpy",
        "scipy",
        "pandas",
        "matplotlib",
        "sklearn",
        "mne",
        "braindecode",
        "moabb",
        "pyriemann",
        "nibabel",
        "nilearn",
        "networkx",
        "jupyterlab",
        "notebook",
    ]

    lines = []
    lines.append("=" * 60)
    lines.append("NeuroBCI Environment Check")
    lines.append("=" * 60)
    lines.append(f"Time: {datetime.now()}")
    lines.append(f"Python executable: {sys.executable}")
    lines.append(f"Python version: {sys.version}")
    lines.append(f"System: {platform.system()}")
    lines.append(f"Machine: {platform.machine()}")
    lines.append(f"Processor: {platform.processor()}")
    lines.append("")
    lines.append("Package status:")

    for package in packages:
        lines.append(f"{package:12s}: {check_package(package)}")

    result_text = "\n".join(lines)
    print(result_text)

    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    output_path = results_dir / "level00_environment_check_from_script.txt"
    output_path.write_text(result_text, encoding="utf-8")


if __name__ == "__main__":
    main()
