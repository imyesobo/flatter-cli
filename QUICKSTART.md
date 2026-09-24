# Quick Start Guide

## 1️⃣ Basic Usage (Simplest)

```bash
cd /Users/yesobo/Dev/ml-lab/python-flatter

# Flatten any directory
python3 flatter.py ~/path/to/my_folder output_folder/
```

This creates:
- `output_folder/` with all files flattened
- `output_folder/my_folder_structure.md` with the original structure

---

## 2️⃣ Executable Wrapper (Recommended for macOS)

Make it easier to use from anywhere:

### Option A: Use the bash wrapper
```bash
cd /Users/yesobo/Dev/ml-lab/python-flatter
./flatter ~/path/to/my_folder output_folder/
```

### Option B: Add to PATH (One-time setup)
```bash
sudo ln -s /Users/yesobo/Dev/ml-lab/python-flatter/flatter.py /usr/local/bin/flatter
# Then use from anywhere:
flatter ~/path/to/my_folder output_folder/
```

---

## 3️⃣ Common Commands

### Flatten with overwrite
```bash
python3 flatter.py ~/Documents/project output/ --force
```

### Exclude additional files
```bash
python3 flatter.py ~/Documents/project output/ --exclude "*.log" ".env"
```

### Flatten EVERYTHING (no exclusions)
```bash
python3 flatter.py ~/Documents/project output/ --no-defaults
```

---

## 4️⃣ Example Workflow

```bash
# Create test directory
mkdir ~/test_project && cd ~/test_project

# Create nested structure
mkdir -p src/utils docs
echo "# My App" > README.md
echo "def main(): pass" > src/main.py
echo "def helper(): pass" > src/utils/helpers.py
echo "# Docs" > docs/guide.md

# Flatten it!
python3 /Users/yesobo/Dev/ml-lab/python-flatter/flatter.py ~/test_project flat_output/

# Check results
ls flat_output/
cat flat_output/test_project_structure.md
```

---

## 5️⃣ Use Cases

- **Upload to ChatGPT/Claude**: Flatten your code, then upload all files + markdown
- **Share project**: No folder restrictions needed
- **Email**: Attach all files as a flat bundle
- **Web forms**: Many don't accept folder uploads

---

## 6️⃣ What Gets Excluded by Default?

```
.git, .gitignore, __pycache__, .DS_Store
.pytest_cache, .venv, venv, node_modules
.egg-info, dist, build, .idea, .vscode
*.pyc, *.pyo, .env, .env.local
```

---

## Output Example

**Input:**
```
my_project/
├── src/
│   ├── main.py
│   └── utils/helpers.py
└── README.md
```

**Output:**
```
flat_output/
├── README.md
├── src_main.py
├── src_utils_helpers.py
└── my_project_structure.md
```

**my_project_structure.md contains:**
- Visual directory tree
- File mapping table (flattened → original)
