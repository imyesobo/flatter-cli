# Using Flatter in Your Project

## Option 1: Reference the Skill (Recommended)

If you want other developers on your team to use the flatten tool via Copilot, add a `.github/prompts/` configuration that references the flatter skill.

### For Your Project

1. Copy this skill into your project:

```bash
# Clone/copy the flatter tool to your project
git submodule add https://github.com/yourusername/python-flatter.git tools/flatter
# OR copy the files manually into your project
```

2. Create `.github/skills/flatten-project/` → copy all files from python-flatter

3. Update paths in your SKILL.md to match your project structure

4. Developers can now type `/flatten-project` in Copilot chat

### Example Project Structure

```
my-project/
├── .github/
│   └── skills/
│       └── flatten-project/
│           ├── SKILL.md
│           └── references/
│               ├── use-cases.md
│               └── faq.md
├── tools/
│   └── flatter/
│       ├── flatter.py
│       └── README.md
└── src/
    ├── main.py
    └── ...
```

---

## Option 2: Use as Git Submodule

Add flatter as a development dependency:

```bash
cd my-project
git submodule add https://github.com/yourusername/python-flatter.git tools/flatter

# Create a wrapper or script that calls it
echo '#!/bin/bash
python3 tools/flatter/flatter.py "$@"' > ./scripts/flatten.sh
chmod +x ./scripts/flatten.sh
```

Developers use: `./scripts/flatten.sh ~/my-project output/`

---

## Option 3: Manual Installation

1. Download [flatter.py](https://github.com/yourusername/python-flatter/blob/main/flatter.py)
2. Place in `tools/` or `scripts/` directory
3. Run: `python3 tools/flatter.py ~/my-project output/`

---

## Option 4: Global Installation (macOS/Linux)

```bash
# Clone the repo
git clone https://github.com/yourusername/python-flatter.git ~/.flatter

# Add to PATH
echo 'export PATH="$PATH:$HOME/.flatter"' >> ~/.zshrc

# Make executable
chmod +x ~/.flatter/flatter.py

# Use globally
flatter ~/my-project output/
```

---

## Adding Flatter to Your Team

### Step 1: Include in Documentation

Add to your `CONTRIBUTING.md` or `README.md`:

```markdown
## Sharing Code

To share this project with AI assistants or external reviewers:

\`\`\`bash
python3 tools/flatter/flatter.py . output/
\`\`\`

This creates a flat bundle with all project files and a structure map.
```

### Step 2: Create a Convenience Script

Create `scripts/prepare-share.sh`:

```bash
#!/bin/bash
# Prepare project for sharing

OUTPUT_DIR="${1:-.flatten_output}"

python3 tools/flatter/flatter.py . "$OUTPUT_DIR" \
  --exclude "*.log" ".git" ".github"

echo "✅ Project flattened to: $OUTPUT_DIR"
echo "📄 Structure map: $OUTPUT_DIR/$(basename $(pwd))_structure.md"
```

Usage:
```bash
./scripts/prepare-share.sh
# or
./scripts/prepare-share.sh my_output_folder/
```

### Step 3: Add to Makefile (Optional)

```makefile
.PHONY: flatten
flatten:
	python3 tools/flatter/flatter.py . flatten_output/ --force
	@echo "✅ Project flattened to flatten_output/"
```

Usage: `make flatten`

---

## Copilot Skill Integration

### For Your Project's Developers

Add a custom Copilot agent instruction (`.github/copilot-instructions.md`):

```markdown
# Using Flatter in This Project

The flatter tool is available to flatten our project structure for sharing.

## Common Tasks

1. **Share with ChatGPT/Claude:**
   ```bash
   ./scripts/prepare-share.sh
   ```
   Then upload all files from the output folder.

2. **Email code review:**
   ```bash
   ./scripts/prepare-share.sh
   cd flatten_output && tar czf ../project.tar.gz * && cd ..
   ```

3. **Get help from Copilot:**
   Type `/flatten-project` in Copilot chat for detailed guidance.
```

---

## Distributing the Skill to Others

### Publish as Package

1. Create a Python package:
```bash
pip install python-flatter
```

2. Use from anywhere:
```bash
python3 -m flatter ~/my-project output/
```

### Share via Organization

Add to your org's `.github/skills/` so all repos access it:

```
.github/
└── skills/
    └── flatten-project/  ← Shared across org
```

Every repo can reference this central skill.

---

## Next Steps

- 🔗 **Link to flatter repo** in your docs
- 📝 **Document** when your team should flatten
- 🎯 **Create convenience scripts** for common use cases
- 🤖 **Enable Copilot** to suggest flattening when appropriate
