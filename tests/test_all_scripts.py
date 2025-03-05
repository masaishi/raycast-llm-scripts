"""
Simple test script to verify all Raycast scripts can run with dummy arguments.
This helps catch basic syntax errors and import issues.
"""

import os
import subprocess
import sys
from pathlib import Path

# Add parent directory to Python path so we can import scripts
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Unified test text for all scripts
DUMMY_TEXT = "This is a test input to verify the script runs correctly."


def test_script(script_path: str) -> bool:
    """Run a script with test arguments and return True if it executes without error."""
    try:
        print(f"\nTesting {script_path}")

        result = subprocess.run(
            [sys.executable, script_path, DUMMY_TEXT], capture_output=True, text=True
        )

        if result.returncode == 0:
            print("✅ Success")
            if result.stdout:
                print("Output:", result.stdout)
            return True
        else:
            print("❌ Failed")
            print("Error:", result.stderr)
            return False
    except Exception as e:
        print("❌ Failed")
        print(f"Error: {e}")
        return False


def main():
    # Get all .py files in scripts directory (excluding utils and tests)
    scripts_dir = Path(__file__).parent.parent / "scripts"
    script_files = [
        f
        for f in scripts_dir.glob("*.py")
        if f.is_file() and not f.name.startswith("__")
    ]

    results = []

    # Run tests for each script
    for script in script_files:
        success = test_script(str(script))
        results.append((script.name, success))

    # Print summary
    print("\n=== Test Summary ===")
    for script, success in results:
        status = "✅ Pass" if success else "❌ Fail"
        print(f"{status} - {script}")


if __name__ == "__main__":
    main()
