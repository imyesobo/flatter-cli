---
name: flatten-project
description: "Flatten a project directory structure into a single folder for upload to systems that don't support folder attachments. Use when: preparing code to share with AI assistants, uploading to systems with folder restrictions, creating portable project bundles, or sharing via email/forms."
argument-hint: "Source directory path (e.g., ~/my-project)"
user-invocable: true
---

# Flatten Project Directory

## When to Use

- 📤 **Upload to AI systems** — Share your project with ChatGPT, Claude, GitHub Copilot without folder restrictions
- 🌐 **Web forms** — Many file-sharing services don't accept folder uploads
- 📧 **Email sharing** — Attach project as flat files instead of zipped folders
- 🔗 **API uploads** — Systems that only accept individual files
- 📦 **Code review bundles** — Send reviewers a self-contained, portable package
- 🤖 **LLM context** — Input entire project structure into prompts

## What It Does

1. **Flattens** all files from nested directories into a single folder
2. **Preserves paths** by prepending relative paths to filenames (`src/utils/helpers.py` → `src_utils_helpers.py`)
3. **Generates documentation** (`.md` file) showing the original directory tree
4. **Creates file mapping** — Table linking flattened filenames to original paths
5. **Excludes automatically** — Skips `.git`, `__pycache__`, `.DS_Store`, and 15+ other patterns by default

## Prerequisites

- Python 3.6+
- Access to the flatter tool: [python-flatter repository](https://github.com/yourusername/python-flatter)

## How to Use

### Step 1: Get the Tool

Clone or download the flatter tool:

```bash
git clone https://github.com/yourusername/python-flatter.git
# or download as ZIP
```

### Step 2: Run Flattening

```bash
# Basic usage
python3 /path/to/python-flatter/flatter.py ~/my-project output_flat/

# With overwrite
python3 /path/to/python-flatter/flatter.py ~/my-project output_flat/ --force

# With custom exclusions
python3 /path/to/python-flatter/flatter.py ~/my-project output_flat/ --exclude "*.log" ".env"
```

### Step 3: Use Flattened Files

All files are now in `output_flat/`:
- **`output_flat/my-project_structure.md`** — Original structure documentation
- **All project files** — Flattened and ready to upload

## Examples

### Example 1: Prepare Python Project for Claude

```bash
# Flatten your Python project
python3 flatter.py ~/Dev/my-app output/

# Upload to Claude:
# 1. Copy all files from output/
# 2. Paste each into Claude's file uploader
# 3. Claude understands the structure from structure.md
```

### Example 2: Share via Email

```bash
# Flatten
python3 flatter.py ~/Documents/project output/

# Create archive
cd output && tar czf project_bundle.tar.gz * && cd ..

# Email project_bundle.tar.gz
# Recipient extracts and reads structure.md to understand layout
```

### Example 3: Web Form Upload

```bash
# Flatten
python3 flatter.py ~/my-website output/ --exclude "*.env" ".git"

# Upload all files from output/ to web form (one by one or zipped)
# The structure.md helps reconstructing the original layout
```

## File Naming Convention

When files are flattened, paths become filenames:

```
Original                          →  Flattened
src/main.py                       →  src_main.py
src/utils/helpers.py              →  src_utils_helpers.py
tests/unit/test_main.py           →  tests_unit_test_main.py
docs/api/endpoints.md             →  docs_api_endpoints.md
```

## Generated Structure Map

The `.md` file includes:

**Tree View** — Visual representation of original structure:
```
my-project/
├── src/
│   ├── main.py
│   └── utils/
│       └── helpers.py
├── tests/
│   └── test_main.py
└── README.md
```

**File Mapping Table** — Links flattened to original:

| Flattened Filename | Original Path |
|---|---|
| `src_main.py` | `src/main.py` |
| `src_utils_helpers.py` | `src/utils/helpers.py` |

## Default Exclusions

The following are automatically excluded:

- Version control: `.git`, `.gitignore`
- Python cache: `__pycache__`, `*.pyc`, `*.pyo`, `.pytest_cache`
- Environment: `.venv`, `venv`, `.env`, `.env.local`
- Dependencies: `node_modules`, `.egg-info`
- IDEs: `.idea`, `.vscode`
- OS files: `.DS_Store`
- Build output: `dist`, `build`

## Command Reference

```bash
# View help
python3 flatter.py --help

# Basic flatten
python3 flatter.py <source> <output>

# Overwrite existing output
python3 flatter.py <source> <output> --force

# Add exclusions
python3 flatter.py <source> <output> --exclude "*.log" ".env"

# No default exclusions (flatten everything)
python3 flatter.py <source> <output> --no-defaults
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `FileNotFoundError` | Source directory doesn't exist — check path |
| `FileExistsError` | Output directory exists — use `--force` to overwrite |
| Files missing | Check if they match exclusion patterns — use `--no-defaults` to include all |
| Permission denied | May need `chmod +x flatter.py` |

## Tips

- **Upload to Claude/ChatGPT**: Include `structure.md` in your first message so the AI understands the project layout
- **Preserve .env files**: Use `--no-defaults` or exclude specifically with care
- **Large projects**: The structure.md helps reviewers understand context without files
- **Batch processing**: Run flattener in a loop for multiple projects

## Related

- [Project repository](https://github.com/yourusername/python-flatter)
- [README with full documentation](./README.md)
- [Quick start guide](./QUICKSTART.md)
