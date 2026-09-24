#!/usr/bin/env python3
"""
Flatter: A utility to flatten directory structures for upload to systems 
that don't support folder attachments.

Flattens all files from nested directories into a single folder and generates
a markdown file documenting the original structure.
"""

import os
import shutil
import argparse
from pathlib import Path
from typing import List, Dict, Tuple
import sys


class DirectoryFlattener:
    """Flattens directory structures and creates structure documentation."""
    
    DEFAULT_EXCLUDE_PATTERNS = {
        '.git', '.gitignore', '__pycache__', '.DS_Store',
        '.pytest_cache', '.venv', 'venv', 'node_modules',
        '.egg-info', 'dist', 'build', '.idea', '.vscode',
        '*.pyc', '*.pyo', '.env', '.env.local'
    }
    
    def __init__(self, source_dir: str, output_dir: str, exclude_patterns: set = None):
        """
        Initialize the flattener.
        
        Args:
            source_dir: Path to the directory to flatten
            output_dir: Path where flattened files and structure map will be saved
            exclude_patterns: Set of patterns to exclude (uses defaults if None)
        """
        self.source_dir = Path(source_dir).resolve()
        self.output_dir = Path(output_dir).resolve()
        self.exclude_patterns = exclude_patterns or self.DEFAULT_EXCLUDE_PATTERNS.copy()
        self.file_mapping: Dict[str, str] = {}  # flattened_name -> original_path
        
        # Validate source directory
        if not self.source_dir.exists():
            raise FileNotFoundError(f"Source directory does not exist: {self.source_dir}")
        if not self.source_dir.is_dir():
            raise NotADirectoryError(f"Source path is not a directory: {self.source_dir}")
    
    def _should_exclude(self, path: Path) -> bool:
        """Check if a path should be excluded based on patterns."""
        name = path.name
        
        for pattern in self.exclude_patterns:
            # Handle exact matches
            if name == pattern:
                return True
            # Handle wildcard patterns
            if pattern.startswith('*.') and name.endswith(pattern[1:]):
                return True
            # Handle directory names
            if pattern in path.parts:
                return True
        
        return False
    
    def _get_flattened_name(self, file_path: Path) -> str:
        """
        Generate flattened filename by prepending relative path.
        
        Example: 
            src/utils/helpers.py -> src_utils_helpers.py
        """
        try:
            relative_path = file_path.relative_to(self.source_dir)
        except ValueError:
            relative_path = file_path
        
        # Convert path to string and replace separators
        path_str = str(relative_path).replace(os.sep, '_')
        return path_str
    
    def _collect_files(self) -> List[Tuple[Path, str]]:
        """
        Recursively collect all files to flatten.
        
        Returns:
            List of (original_path, flattened_name) tuples
        """
        files = []
        
        for root, dirs, filenames in os.walk(self.source_dir):
            # Filter out excluded directories
            dirs[:] = [d for d in dirs if not self._should_exclude(Path(root) / d)]
            
            # Process files
            for filename in filenames:
                file_path = Path(root) / filename
                
                if not self._should_exclude(file_path):
                    flattened_name = self._get_flattened_name(file_path)
                    files.append((file_path, flattened_name))
        
        return files
    
    def _build_tree_structure(self) -> str:
        """Build a tree representation of the original directory structure."""
        def get_tree(path: Path, prefix: str = "", is_last: bool = True) -> str:
            """Recursively build tree string."""
            tree_str = ""
            connector = "└── " if is_last else "├── "
            tree_str += prefix + connector + path.name + "\n"
            
            new_prefix = prefix + ("    " if is_last else "│   ")
            
            if path.is_dir():
                try:
                    entries = sorted([p for p in path.iterdir() if not self._should_exclude(p)])
                except PermissionError:
                    return tree_str
                
                for i, entry in enumerate(entries):
                    is_last_entry = i == len(entries) - 1
                    tree_str += get_tree(entry, new_prefix, is_last_entry)
            
            return tree_str
        
        # Start tree without root prefix
        tree_str = self.source_dir.name + "/\n"
        try:
            entries = sorted([p for p in self.source_dir.iterdir() if not self._should_exclude(p)])
        except PermissionError:
            return tree_str
        
        for i, entry in enumerate(entries):
            is_last = i == len(entries) - 1
            tree_str += get_tree(entry, "", is_last)
        
        return tree_str
    
    def _build_file_mapping_table(self) -> str:
        """Build a markdown table of flattened filenames and original paths."""
        if not self.file_mapping:
            return ""
        
        table = "| Flattened Filename | Original Path |\n"
        table += "|---|---|\n"
        
        for flattened_name in sorted(self.file_mapping.keys()):
            original_path = self.file_mapping[flattened_name]
            table += f"| `{flattened_name}` | `{original_path}` |\n"
        
        return table
    
    def _generate_structure_md(self) -> str:
        """Generate the markdown documentation file."""
        md_content = f"""# Directory Structure Map

**Original Directory:** `{self.source_dir.name}`  
**Generated:** Flattened structure documentation  
**Total Files:** {len(self.file_mapping)}

## Original Directory Tree

```
{self._build_tree_structure()}```

## File Mapping (Flattened → Original)

{self._build_file_mapping_table()}

---
*Generated by flatter.py*
"""
        return md_content
    
    def flatten(self, force: bool = False) -> None:
        """
        Flatten the directory structure.
        
        Args:
            force: If True, overwrite existing output directory
        
        Raises:
            FileExistsError: If output directory exists and force=False
        """
        # Check output directory
        if self.output_dir.exists() and not force:
            raise FileExistsError(
                f"Output directory already exists: {self.output_dir}\n"
                f"Use --force to overwrite."
            )
        
        # Create or clean output directory
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Collect files
        files = self._collect_files()
        
        if not files:
            print("⚠️  No files found to flatten (all excluded or directory is empty)")
            return
        
        # Copy files
        print(f"📂 Flattening {len(files)} files...")
        for original_path, flattened_name in files:
            output_path = self.output_dir / flattened_name
            
            # Create subdirectories if needed (shouldn't be needed for flat structure)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy file
            shutil.copy2(original_path, output_path)
            
            # Store mapping (relative path for readability)
            try:
                rel_original = original_path.relative_to(self.source_dir)
            except ValueError:
                rel_original = original_path
            self.file_mapping[flattened_name] = str(rel_original)
        
        # Generate structure markdown
        md_path = self.output_dir / f"{self.source_dir.name}_structure.md"
        md_content = self._generate_structure_md()
        md_path.write_text(md_content)
        
        print(f"✅ Done! Files flattened to: {self.output_dir}")
        print(f"📄 Structure map: {md_path.name}")


def main():
    """Command-line interface."""
    parser = argparse.ArgumentParser(
        description="Flatten directory structure for upload to systems that don't support folders.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Flatten a directory
  python flatter.py ~/Documents/my_project output_flat/
  
  # Flatten and overwrite existing output
  python flatter.py ~/Documents/my_project output_flat/ --force
  
  # Flatten with custom exclusions
  python flatter.py ~/Documents/my_project output_flat/ --exclude ".git" "*.pyc" "node_modules"
        """
    )
    
    parser.add_argument(
        "source",
        help="Path to the source directory to flatten"
    )
    parser.add_argument(
        "output",
        help="Path to the output directory where flattened files will be saved"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite output directory if it exists"
    )
    parser.add_argument(
        "--exclude",
        nargs="+",
        help="Additional patterns to exclude (in addition to defaults)"
    )
    parser.add_argument(
        "--no-defaults",
        action="store_true",
        help="Don't use default exclusion patterns"
    )
    
    args = parser.parse_args()
    
    # Build exclude patterns
    exclude_patterns = set() if args.no_defaults else DirectoryFlattener.DEFAULT_EXCLUDE_PATTERNS.copy()
    if args.exclude:
        exclude_patterns.update(args.exclude)
    
    try:
        flattener = DirectoryFlattener(args.source, args.output, exclude_patterns)
        flattener.flatten(force=args.force)
    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
