# Flatter 📂

A command-line tool to flatten directory structures for upload to systems that don't support folder attachments.

## Features

- **Flattens nested directories** into a single flat folder
- **Preserves path information** by prepending relative paths to filenames
- **Generates markdown documentation** showing the original structure
- **File mapping table** for easy reference of flattened ↔ original names
- **Configurable exclusions** (defaults exclude `.git`, `__pycache__`, `.DS_Store`, etc.)
- **macOS optimized** but works on Linux and Windows too

## Installation

### Quick Start (No Installation Required)

Just run the script directly:

```bash
python3 flatter.py <source_directory> <output_directory>
```

### Optional: Make Executable

```bash
chmod +x flatter.py
# Then use it as:
./flatter.py <source_directory> <output_directory>
```

## Usage

### Basic Usage

Flatten a directory into `output_flat/`:

```bash
python3 flatter.py ~/path/to/my_project output_flat/
```

This creates:
- `output_flat/` — folder with all flattened files
- `output_flat/my_project_structure.md` — documentation of original structure

### Overwrite Existing Output

```bash
python3 flatter.py ~/path/to/my_project output_flat/ --force
```

### Custom Exclusions

Add patterns to exclude in addition to defaults:

```bash
python3 flatter.py ~/path/to/my_project output_flat/ --exclude "*.log" "temp"
```

### No Default Exclusions

Flatten everything (no exclusions):

```bash
python3 flatter.py ~/path/to/my_project output_flat/ --no-defaults
```

## Examples

### Example: Flatten a Python Project

```bash
python3 flatter.py ~/Dev/my-app output_flat/
```

**Input structure:**
```
my-app/
├── src/
│   ├── main.py
│   └── utils/
│       └── helpers.py
├── tests/
│   └── test_main.py
└── README.md
```

**Output:**
```
output_flat/
├── README.md
├── src_main.py
├── src_utils_helpers.py
├── tests_test_main.py
└── my-app_structure.md
```

**my-app_structure.md includes:**
- Visual tree of original structure
- Table mapping flattened filenames to original paths

### Default Exclusions

The following are excluded by default:

- `.git`, `.gitignore`
- `__pycache__`, `*.pyc`, `*.pyo`
- `.DS_Store` (macOS)
- `.pytest_cache`
- `.venv`, `venv`, `node_modules`
- `.egg-info`, `dist`, `build`
- `.idea`, `.vscode`
- `.env`, `.env.local`

## Output

### Generated Structure Map

The `*_structure.md` file includes:

1. **Original Directory Tree** — Visual representation of nested structure
2. **File Mapping Table** — Maps each flattened filename to its original path

Example:

```markdown
# Directory Structure Map

**Original Directory:** `my_project`  
**Total Files:** 5

## Original Directory Tree

```
my_project/
├── src/
│   ├── main.py
│   └── utils/
│       └── helpers.py
├── tests/
│   └── test.py
└── README.md
```

## File Mapping

| Flattened Filename | Original Path |
|---|---|
| `README.md` | `README.md` |
| `src_main.py` | `src/main.py` |
| `src_utils_helpers.py` | `src/utils/helpers.py` |
| `tests_test.py` | `tests/test.py` |
```

## Use Cases

- 📧 **Email attachments** — Many systems limit folder uploads
- 🤖 **AI systems** — Upload directory structures to ChatGPT, Claude, etc.
- 🔗 **Cloud services** — Services that don't support folder uploads
- 📦 **File sharing** — Simplify sharing of project structures

## Requirements

- Python 3.6+
- No external dependencies (uses only Python stdlib)

## GitHub Copilot Integration

This tool includes a **Copilot agent skill** that makes it easy to use in your workflows.

### For Your Project

Add this skill to your project's `.github/skills/` folder:

```bash
cp -r .github/skills/flatten-project your-project/.github/skills/
```

Then developers can type `/flatten-project` in Copilot chat for guided help.

### See Also

- [Skill integration guide](./.github/skills/flatten-project/references/integration-guide.md)
- [Use cases](./.github/skills/flatten-project/references/use-cases.md)
- [FAQ](./.github/skills/flatten-project/references/faq.md)

---

## License

MIT

## Contributing

Feel free to submit issues or improvements!
