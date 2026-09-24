# Flatter Project — Complete Overview

## 📁 Project Structure

```
python-flatter/
├── Core Files
│   ├── flatter.py                 ← Main script (450+ lines, fully typed)
│   ├── flatter                    ← Executable wrapper (bash)
│   ├── example_test.py            ← Working example/test
│   └── .gitignore                 ← Python project gitignore
│
├── Documentation
│   ├── README.md                  ← Full project documentation
│   ├── QUICKSTART.md              ← Quick reference guide
│   ├── COPILOT_SKILL_SETUP.md    ← Copilot integration guide
│   └── INDEX.md                   ← This file
│
└── Copilot Skill
    └── .github/skills/
        ├── install-skill.sh           ← One-command installer
        └── flatten-project/           ← Skill folder
            ├── SKILL.md               ← Main skill definition
            ├── README.md              ← Skill documentation
            └── references/
                ├── use-cases.md       ← 10+ real-world scenarios
                ├── faq.md             ← Questions & troubleshooting
                └── integration-guide.md ← How to add to projects
```

---

## 🎯 What's Included

### 1. **Core Tool** (`flatter.py`)
- 450+ lines of production-quality Python code
- Zero external dependencies
- Full type hints
- Comprehensive error handling
- Works on macOS, Linux, Windows

**Features:**
- Flattens nested directories into a single folder
- Prepends relative paths to filenames
- Auto-generates markdown structure map
- Configurable file exclusions
- CLI with multiple options

### 2. **Documentation**
- **README.md** — Full feature guide with examples
- **QUICKSTART.md** — Quick reference for common tasks
- **COPILOT_SKILL_SETUP.md** — Integration guide for other projects

### 3. **Copilot Agent Skill**
A complete skill for GitHub Copilot Chat that:
- Provides guided instructions
- Shows 10+ real-world use cases
- Answers 40+ FAQ questions
- Explains integration options
- Progressive loading (efficient context use)

---

## 🚀 Quick Start

### For This Project

```bash
# Flatten any directory
python3 flatter.py ~/path/to/project output_flat/

# View the generated structure map
cat output_flat/project_structure.md
```

### For Other Projects

```bash
# One-command installation
bash .github/skills/install-skill.sh ~/another-project

# Then in that project, developers type:
# /flatten-project
# (in GitHub Copilot chat)
```

---

## 📚 Documentation Map

| Document | Purpose | Audience |
|----------|---------|----------|
| [README.md](./README.md) | Complete feature guide | Everyone |
| [QUICKSTART.md](./QUICKSTART.md) | Quick reference | Users |
| [COPILOT_SKILL_SETUP.md](./COPILOT_SKILL_SETUP.md) | Skill integration | Team leads, DevOps |
| [.github/skills/flatten-project/SKILL.md](./.github/skills/flatten-project/SKILL.md) | Copilot skill definition | Copilot users |
| [.github/skills/flatten-project/references/use-cases.md](./.github/skills/flatten-project/references/use-cases.md) | Real-world scenarios | Planning/evaluation |
| [.github/skills/flatten-project/references/faq.md](./.github/skills/flatten-project/references/faq.md) | FAQ & troubleshooting | Support/debugging |
| [.github/skills/flatten-project/references/integration-guide.md](./.github/skills/flatten-project/references/integration-guide.md) | Team integration | Developers |

---

## 🎯 Use Cases

### Individual Use
```bash
# Share with ChatGPT/Claude
python3 flatter.py ~/my-app output/
# → Upload all files from output/ to ChatGPT
# → Include structure.md first for context
```

### Team Use
```bash
# Add to project
.github/skills/install-skill.sh .

# Team members type in Copilot chat:
/flatten-project
# → Get guided help
```

### Organization Use
```
.github/  (org-wide)
└── skills/
    └── flatten-project/
# → All repos can use /flatten-project
```

---

## ✨ Skill Highlights

### Discovery
The skill's `description` includes keywords like:
- "flatten", "project", "directory", "upload"
- "AI assistant", "email", "web form"
- "folder restrictions", "share code"

→ Copilot finds it when relevant

### Progressive Loading
1. **Discovery** (~100 tokens): Read name + description
2. **Full skill** (~5000 tokens): Load SKILL.md if triggered
3. **References** (on-demand): Load FAQ, use-cases, etc.

→ Efficient context use

### Team-Friendly
- One-command installation
- Works project-wide or org-wide
- Customizable for your workflow
- Easy to update and share

---

## 🔧 Customization

### For Your Project

Edit `.github/skills/flatten-project/SKILL.md`:

```yaml
---
name: flatten-project
description: "Your custom description..."  ← Update keywords
---

# Your custom title

[Add team guidelines, examples, etc.]

# Running Flattener

\`\`\`bash
# Update path to your installation
python3 tools/flatter/flatter.py ~/my-project output/
\`\`\`
```

### For Your Team

Create convenience scripts:

```bash
# scripts/prepare-share.sh
python3 .github/skills/flatten-project/../../flatter.py . output/ --force
echo "✅ Flattened to output/ - ready to share!"
```

---

## 📊 Statistics

| Metric | Value |
|--------|-------|
| **Main script** | 450+ lines |
| **Test example** | Working demo |
| **Documentation** | 5 markdown files |
| **Skill files** | 5 markdown files |
| **External deps** | 0 (pure stdlib) |
| **Python version** | 3.6+ |
| **Platforms** | macOS, Linux, Windows |

---

## 🚦 Getting Started

### New to Flatter?
1. Read [README.md](./README.md)
2. Try [example_test.py](./example_test.py): `python3 example_test.py`
3. Use [QUICKSTART.md](./QUICKSTART.md) for your first flatten

### Want to Add to Your Project?
1. Read [COPILOT_SKILL_SETUP.md](./COPILOT_SKILL_SETUP.md)
2. Run: `bash .github/skills/install-skill.sh ~/my-project`
3. Update paths in the installed SKILL.md

### Want to Distribute to Your Team?
1. Push this repo to your GitHub org
2. Run install script from any project
3. Document in your team wiki

---

## 🔗 File Links

### Main Documentation
- [README.md](./README.md) — Full guide
- [QUICKSTART.md](./QUICKSTART.md) — Quick reference
- [COPILOT_SKILL_SETUP.md](./COPILOT_SKILL_SETUP.md) — Integration guide

### Copilot Skill
- [SKILL.md](./.github/skills/flatten-project/SKILL.md) — Skill definition
- [use-cases.md](./.github/skills/flatten-project/references/use-cases.md) — Scenarios
- [faq.md](./.github/skills/flatten-project/references/faq.md) — Q&A
- [integration-guide.md](./.github/skills/flatten-project/references/integration-guide.md) — Team setup

### Code
- [flatter.py](./flatter.py) — Main implementation
- [example_test.py](./example_test.py) — Working example

---

## 💡 Key Concepts

### Flattening
Converting nested structure → flat structure with path-prefixed names:
```
src/utils/helpers.py  →  src_utils_helpers.py
docs/api/guide.md     →  docs_api_guide.md
```

### Structure Map
Auto-generated `.md` file that shows:
1. **Tree view** of original directory
2. **Mapping table** of flattened → original paths

### Skill
GitHub Copilot agent skill that provides:
- Guided instructions
- Use case scenarios
- FAQ & troubleshooting
- Integration guidance

---

## ❓ Common Questions

**Q: Can I use this without GitHub/Copilot?**
A: Yes! The `flatter.py` script works standalone. The Copilot skill is optional.

**Q: Is this for teams only?**
A: No. Works for individuals (CLI) or teams (with Copilot skill).

**Q: How do I distribute to my team?**
A: Copy the `.github/skills/` folder to your org or projects. See [integration-guide.md](./.github/skills/flatten-project/references/integration-guide.md).

**Q: Can I customize the skill?**
A: Yes! Edit SKILL.md and references/* to match your workflow.

---

## 📞 Support

- **Questions?** See [faq.md](./.github/skills/flatten-project/references/faq.md)
- **Integration help?** See [integration-guide.md](./.github/skills/flatten-project/references/integration-guide.md)
- **Use cases?** See [use-cases.md](./.github/skills/flatten-project/references/use-cases.md)
- **Report issues?** GitHub repo issues

---

**Built with ❤️ for easier project sharing**
