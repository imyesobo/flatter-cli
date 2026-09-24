#!/usr/bin/env python3
"""
Simple test to demonstrate flatter.py in action.
Creates a sample directory structure and flattens it.
"""

import tempfile
import shutil
from pathlib import Path
from flatter import DirectoryFlattener


def create_sample_directory(base_path: Path) -> Path:
    """Create a sample nested directory structure."""
    sample_dir = base_path / "sample_project"
    
    # Create directories
    (sample_dir / "src").mkdir(parents=True)
    (sample_dir / "src" / "utils").mkdir()
    (sample_dir / "tests").mkdir()
    (sample_dir / "docs").mkdir()
    
    # Create files
    files = {
        "README.md": "# Sample Project\n\nThis is a test project.",
        "src/main.py": "def main():\n    print('Hello, World!')\n",
        "src/config.py": "CONFIG = {'debug': True}\n",
        "src/utils/helpers.py": "def helper():\n    pass\n",
        "src/utils/__init__.py": "",
        "tests/test_main.py": "def test_main():\n    assert True\n",
        "docs/guide.md": "# User Guide\n",
        ".env": "SECRET_KEY=test",
    }
    
    for file_path, content in files.items():
        full_path = sample_dir / file_path
        full_path.write_text(content)
    
    return sample_dir


def main():
    """Run the test."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        # Create sample directory
        print("📁 Creating sample directory structure...")
        sample_dir = create_sample_directory(temp_path)
        print(f"✅ Created sample project at: {sample_dir}\n")
        
        # Flatten it
        output_dir = temp_path / "flattened"
        print(f"🔄 Flattening directory...")
        flattener = DirectoryFlattener(str(sample_dir), str(output_dir))
        flattener.flatten()
        
        # Show results
        print(f"\n📊 Results:")
        print(f"  - Flattened files location: {output_dir}")
        
        if output_dir.exists():
            files = list(output_dir.glob("*"))
            print(f"  - Files in output: {len(files)}")
            for f in sorted(files):
                if f.is_file():
                    size = f.stat().st_size
                    print(f"    • {f.name} ({size} bytes)")
        
        # Show the structure markdown
        md_file = output_dir / "sample_project_structure.md"
        if md_file.exists():
            print(f"\n📄 Generated structure map:\n")
            print(md_file.read_text())


if __name__ == "__main__":
    main()
