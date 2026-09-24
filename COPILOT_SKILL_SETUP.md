# Copilot Skill for Flatter — Complete Setup

## ✅ What's Been Created

A complete **GitHub Copilot agent skill** for the flatter tool that other projects can integrate and use.

### Structure

```
.github/skills/flatten-project/
├── SKILL.md                           # Main skill definition
├── README.md                          # Skill documentation
├── references/
│   ├── use-cases.md                   # 10+ real-world scenarios
│   ├── faq.md                         # Frequently asked questions
│   └── integration-guide.md           # How to add to other projects
└── ../install-skill.sh                # One-command installation script
```

## 🚀 How to Use

### For Your Own Projects

#### Option A: Copy via Script (Easiest)

```bash
# Copy skill to your project
/Users/yesobo/Dev/ml-lab/python-flatter/.github/skills/install-skill.sh ~/my-project

# Then commit
cd ~/my-project && git add .github/skills/ && git commit -m "Add flatten-project skill"
```

#### Option B: Copy Manually

```bash
cp -r /Users/yesobo/Dev/ml-lab/python-flatter/.github/skills/flatten-project \
  ~/my-project/.github/skills/
```

#### Option C: Git Submodule

```bash
cd ~/my-project
git submodule add https://github.com/yourusername/python-flatter.git tools/flatter
# Then copy skill files manually
```

### In Copilot Chat

Once installed, developers type:
```
/flatten-project
```

And Copilot shows:
- Step-by-step instructions
- Common use cases
- Command examples
- Troubleshooting help

## 📚 Skill Contents

### SKILL.md (Main)
- **What it does**: Flattens nested directories for upload-restricted systems
- **When to use**: AI assistants, email, web forms, code reviews
- **Prerequisites**: Python 3.6+
- **How-to steps**: 3 easy steps from command to upload

### references/use-cases.md
10+ detailed scenarios:
1. AI Assistant Integration (ChatGPT, Claude)
2. Email Code Review
3. Web Form File Upload
4. Portable Project Bundle
5. Code Generation Context
6. Collaborative Debugging
7. Documentation Snapshots
8. Testing Framework Input
9. Archive & Storage
10. Quick Project Sharing

### references/faq.md
- Installation & Setup (7 Q&A)
- Functionality (7 Q&A)
- Exclusions & Filtering (5 Q&A)
- Common Scenarios (4 Q&A)
- Troubleshooting (5 Q&A)
- Advanced Usage (5 Q&A)
- Misc (7 Q&A)

### references/integration-guide.md
Options for:
1. Reference the skill (recommended)
2. Use as Git submodule
3. Manual installation
4. Global installation (macOS/Linux)
5. Adding to team documentation
6. Publishing as package

## 🔧 Customizing for Your Project

Edit `.github/skills/flatten-project/SKILL.md`:

1. **Update flatter path** in examples:
```yaml
# Change from:
python3 /path/to/python-flatter/flatter.py ~/my-project output/

# To your project's structure:
python3 tools/flatter/flatter.py ~/my-project output/
```

2. **Add team guidelines** to the body
3. **Link to your docs** instead of generic examples
4. **Customize for your tech stack**

## 📦 Distribution Options

### Single Project
```
your-project/.github/skills/flatten-project/
```
→ Developers in your project can use `/flatten-project`

### Organization-Wide
```
.github/  (at org root)
└── skills/
    └── flatten-project/
```
→ All repos access the same skill

### Personal Use
```
~/.copilot/skills/flatten-project/  (on your machine)
```
→ Available in all your personal projects

## 🎯 Common Integration Patterns

### Pattern 1: Project Tool
```bash
# Your project structure
my-project/
├── .github/skills/flatten-project/  ← Skill here
├── tools/flatter/                   ← Flatter script
└── scripts/prepare-share.sh          ← Convenience wrapper
```

Usage: Developers type `/flatten-project` → Get guided help

### Pattern 2: Team Shared
```bash
# Org structure
.github/skills/flatten-project/      ← Org-wide skill
├── skills/
└── repos/
    ├── repo1/ (uses /flatten-project)
    ├── repo2/ (uses /flatten-project)
    └── repo3/ (uses /flatten-project)
```

### Pattern 3: Global Tool
```bash
# ~/.zshrc or ~/.bashrc
alias flatten-project="python3 ~/.flatter/flatter.py"
```

Plus skill in: `~/.copilot/skills/flatten-project/`

## ✨ Key Features

✅ **Progressive loading** — Copilot loads only what's needed  
✅ **Keyword-rich discovery** — Found when relevant  
✅ **Complete documentation** — Uses cases, FAQ, integration guide  
✅ **Easy distribution** — Copy script and integration guide included  
✅ **Team-friendly** — Can be org-wide or per-project  
✅ **Zero dependencies** — Works with flatter.py alone  

## 🚦 Quick Start for Other Projects

**One-command integration:**

```bash
bash /Users/yesobo/Dev/ml-lab/python-flatter/.github/skills/install-skill.sh ~/my-project
```

**Then in that project:**

1. Developers type `/flatten-project` in Copilot chat
2. Get step-by-step guidance
3. Run: `python3 tools/flatter/flatter.py ~/my-app output/`
4. Upload flattened files + structure.md

## 📖 Documentation Files

| File | Purpose |
|------|---------|
| [SKILL.md](.github/skills/flatten-project/SKILL.md) | Main skill definition and procedures |
| [README.md](.github/skills/flatten-project/README.md) | Skill structure and customization |
| [use-cases.md](.github/skills/flatten-project/references/use-cases.md) | 10+ scenarios with examples |
| [faq.md](.github/skills/flatten-project/references/faq.md) | Q&A and troubleshooting |
| [integration-guide.md](.github/skills/flatten-project/references/integration-guide.md) | How to add skill to projects |
| [QUICKSTART.md](./QUICKSTART.md) | Quick reference for flatter itself |
| [README.md](./README.md) | Main project documentation |

## 🔗 Next Steps

1. **Test the skill**:
   ```bash
   mkdir ~/test-skill
   /Users/yesobo/Dev/ml-lab/python-flatter/.github/skills/install-skill.sh ~/test-skill
   # Check that .github/skills/flatten-project/ was created
   ```

2. **Share with your team**:
   - Push to GitHub
   - Add to documentation
   - Announce in team channels

3. **Customize for your workflow**:
   - Edit SKILL.md with your paths
   - Add team guidelines
   - Create convenience scripts

4. **Make it discoverable**:
   - Update description keywords if needed
   - Document in team wiki/docs
   - Show demo to team

---

**That's it!** Your Copilot skill is ready to use. 🎉
