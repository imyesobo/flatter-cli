# Copilot Skill: flatten-project

This folder contains a GitHub Copilot agent skill for the flatter tool.

## What Is This?

A **Copilot skill** is a reusable, task-specific workflow that integrates with GitHub Copilot chat. When developers type `/flatten-project`, Copilot loads this skill and provides:

- ✅ Contextual guidance on when to flatten
- ✅ Step-by-step instructions
- ✅ Real-world use cases
- ✅ Command examples
- ✅ FAQ and troubleshooting

## File Structure

```
flatten-project/
├── SKILL.md                    # Main skill definition (loaded by Copilot)
└── references/
    ├── use-cases.md            # 10+ scenarios for using flatter
    ├── faq.md                  # Frequently asked questions
    └── integration-guide.md    # How to add this skill to your project
```

## How to Use

### In This Project

```bash
cd /Users/yesobo/Dev/ml-lab/python-flatter
python3 flatter.py ~/any-project output/
```

### In Other Projects (Add the Skill)

**Option A: Copy the skill files**
```bash
cp -r /Users/yesobo/Dev/ml-lab/python-flatter/.github/skills/flatten-project \
  YOUR_PROJECT/.github/skills/
```

**Option B: Reference the original location**
Update `SKILL.md` to point to your flatter installation:
```yaml
description: "Use with python3 /path/to/python-flatter/flatter.py"
```

### In Copilot Chat

Type in any project with this skill installed:
```
/flatten-project
```

Copilot will show the skill with full documentation and use cases.

## Progressive Loading

Copilot loads this skill in stages:

1. **Discovery** (~100 tokens)
   - Reads `name` and `description` from SKILL.md frontmatter
   - Decides if skill is relevant to user's request

2. **Full Instructions** (~5000 tokens)
   - Loads entire SKILL.md body if skill is triggered
   - Provides step-by-step procedures

3. **References** (on-demand)
   - Loads `references/*.md` files only when referenced
   - Keeps primary SKILL.md focused and concise

## Key Files Explained

### SKILL.md
- **Frontmatter** (YAML): Name, description, invocation hints
- **Body**: Main procedural guide, examples, reference links
- **Keyword-rich**: Description includes trigger phrases for discovery

### references/use-cases.md
- 10+ real-world scenarios
- When to use flattening
- Quick decision matrix

### references/faq.md
- Common questions and troubleshooting
- Answers for typical issues
- Advanced usage patterns

### references/integration-guide.md
- How to add this skill to your project
- Multiple installation options
- Team workflow integration

## Skill Frontmatter Explained

```yaml
---
name: flatten-project           # Must match folder name
description: 'Use when...'      # Discovery keywords (max 1024 chars)
argument-hint: 'source dir'     # Hint for slash command
user-invocable: true            # Show as /slash command
---
```

**Key**: The `description` field is crucial. It must include keywords like:
- "flatten", "project", "directory", "upload", "folder", "structure"
- Problem statements: "don't support", "folder restrictions"
- Use cases: "AI assistant", "email", "web form"

This helps Copilot's discovery algorithm find the skill when relevant.

## Customizing for Your Project

1. **Update paths** in SKILL.md to match your project structure
2. **Add team guidelines** in `references/` files
3. **Customize examples** to match your tech stack
4. **Add your repo URL** to the integration guide

Example customization:
```markdown
# In your project's flatten-project/SKILL.md

Run flattener from your project:
\`\`\`bash
python3 tools/flatter/flatter.py ~/your-app output/
\`\`\`

See [Integration Guide](./references/integration-guide.md) for setup.
```

## Distributing the Skill

### Option 1: In Your Project Only
```
your-project/
└── .github/
    └── skills/
        └── flatten-project/
```
→ Developers in your project use `/flatten-project`

### Option 2: Org-Wide
```
your-org/.github/
└── skills/
    └── flatten-project/
```
→ All repos in your org share this skill

### Option 3: Personal User Skills
```
~/.copilot/skills/
└── flatten-project/
```
→ Available in all your personal projects

## Related Documentation

- **Main README**: [README.md](../../README.md)
- **Quick Start**: [QUICKSTART.md](../../QUICKSTART.md)
- **Integration Guide**: [integration-guide.md](./references/integration-guide.md)
- **Use Cases**: [use-cases.md](./references/use-cases.md)
- **FAQ**: [faq.md](./references/faq.md)

## Questions?

See the [FAQ](./references/faq.md) or check the main [project repo](https://github.com/yourusername/python-flatter).
