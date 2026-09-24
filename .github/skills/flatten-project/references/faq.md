# Flatter — Frequently Asked Questions

## Installation & Setup

**Q: Do I need to install flatter globally?**
A: No. You can run it directly with `python3 /path/to/flatter.py`. Optional: Add to PATH for convenience.

**Q: Does it work on Windows?**
A: Yes! It's cross-platform Python. Works on Windows, macOS, Linux equally well.

**Q: What Python version is required?**
A: Python 3.6 or higher. Check with `python3 --version`.

---

## Functionality

**Q: What does "flattening" mean?**
A: Converting nested folders into a single flat folder with path-prefixed filenames:
```
src/utils/helpers.py  →  src_utils_helpers.py
```

**Q: Will my original files be deleted?**
A: No. Flattener only **copies** files. Your original directory is untouched.

**Q: Can I flatten a single file?**
A: No, flattener works on directories only. But you can flatten a directory containing one file.

**Q: What if two files have the same name in different folders?**
A: They get unique flattened names with path prefixes:
```
src/utils/helpers.py  →  src_utils_helpers.py
src/core/helpers.py   →  src_core_helpers.py
```

---

## Exclusions & Filtering

**Q: What files are excluded by default?**
A: `.git`, `__pycache__`, `.DS_Store`, `.venv`, `node_modules`, `.env`, and ~15 more. See [full list](../SKILL.md#default-exclusions).

**Q: How do I include `.env` or `.git` files?**
A: Use `--no-defaults` to skip all exclusions:
```bash
python3 flatter.py ~/my-project output/ --no-defaults
```

**Q: How do I exclude more patterns?**
A: Use `--exclude`:
```bash
python3 flatter.py ~/my-project output/ --exclude "*.log" ".env" "temp"
```

**Q: Can I use regex patterns?**
A: No, only simple glob patterns and exact names. Examples: `*.log`, `__pycache__`, `.env`.

---

## Output & Structure Map

**Q: What's in the generated `.md` file?**
A: Two sections:
1. **Original tree** — Visual representation of your folder structure
2. **File mapping table** — List of flattened filename → original path

**Q: Can I customize the structure map?**
A: Not yet. The markdown is auto-generated. You can edit it manually after generation.

**Q: Where does the structure.md file go?**
A: In the output folder, named `{source_folder_name}_structure.md`.

**Q: Can I view the structure.md without flattening again?**
A: Yes, it's in your output folder. Open it with any text editor or markdown viewer.

---

## Common Scenarios

**Q: I want to flatten a git repo but keep `.git` history?**
A: Use `--no-defaults`:
```bash
python3 flatter.py ~/my-repo output/ --no-defaults
```
(Warning: This will copy all `.git` files and can make output very large.)

**Q: How do I upload flattened files to ChatGPT?**
A: 
1. Run: `python3 flatter.py ~/my-project output/`
2. Open ChatGPT and upload files from `output/`
3. Include the `structure.md` first so ChatGPT understands the layout

**Q: Can I flatten a folder inside another folder?**
A: Yes! Just provide the path:
```bash
python3 flatter.py ~/my-project/src output/
# Flattens only the src/ subdirectory
```

**Q: What if the output folder already exists?**
A: Flattener will refuse to overwrite. Use `--force`:
```bash
python3 flatter.py ~/my-project output/ --force
```

---

## Troubleshooting

**Q: I get "No files found to flatten"**
A: All files are probably excluded. Try:
```bash
python3 flatter.py ~/my-project output/ --no-defaults
```

**Q: Permission denied errors**
A: Make the script executable:
```bash
chmod +x /path/to/flatter.py
```

**Q: Output folder shows fewer files than I expected**
A: Some files are being excluded. Check if they match default exclusion patterns. Use `--no-defaults` to include all.

**Q: The flattened filename is too long**
A: Very deep nested paths can create long names. This is by design to preserve structure. Consider `--exclude` patterns to reduce depth.

**Q: I'm on Windows and getting encoding errors**
A: Try running with explicit UTF-8:
```bash
python3 -u flatter.py ~/my-project output/
```

---

## Advanced Usage

**Q: Can I run flattener on a schedule (like with cron)?**
A: Yes! You can use it in shell scripts:
```bash
#!/bin/bash
python3 /path/to/flatter.py ~/my-project ~/flat_output/ --force
tar czf ~/backups/project_$(date +%Y%m%d).tar.gz ~/flat_output/
```

**Q: Can I flatten multiple projects at once?**
A: Not built-in, but you can loop:
```bash
for project in ~/projects/*/; do
  python3 flatter.py "$project" "flat_${project##*/}/"
done
```

**Q: Can I use flattener as a Python library?**
A: Yes! Import and use the `DirectoryFlattener` class:
```python
from flatter import DirectoryFlattener

flattener = DirectoryFlattener("~/my-project", "output/")
flattener.flatten()
```

**Q: How large can a project be?**
A: Flattener handles hundreds of thousands of files. Speed depends on disk I/O and file count.

---

## Misc

**Q: Does flattener modify files (content)?**
A: No. It copies files as-is. Only filenames change (path prefix added).

**Q: Is there a GUI version?**
A: Not yet. Command-line only.

**Q: Can I undo flattening?**
A: The `structure.md` file shows original paths. You'd need to manually recreate folders, but the information is there. Consider keeping your original directory.

**Q: How do I contribute or report bugs?**
A: See the [GitHub repository](https://github.com/yourusername/python-flatter).

**Q: Is flattener open source?**
A: Yes! MIT license. See LICENSE file in repository.
