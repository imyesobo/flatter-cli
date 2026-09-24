# Flatten Project — Use Cases

## 1. AI Assistant Integration

### Problem
You want to share your entire project with ChatGPT/Claude/Copilot, but these systems have limitations:
- Can't directly attach folders
- Require uploading individual files
- Struggle to understand nested context

### Solution
1. Flatten your project: `python3 flatter.py ~/my-app output/`
2. Upload `output/my-app_structure.md` first (gives context)
3. Upload all source files from `output/`
4. AI understands original structure and can help with the full codebase

### Example
```
Chat prompt:
"I've flattened my Python project (structure in my-app_structure.md). 
All files are listed below. Please review the architecture and suggest improvements."

[User then shares all flattened files]
```

---

## 2. Email Code Review

### Problem
You need to share code with a colleague, but:
- Email limits attachment sizes/quantities
- Folder structures get lost
- Recipient has to reconstruct context

### Solution
1. Flatten: `python3 flatter.py ~/project output/`
2. Zip the output: `cd output && zip -r project.zip *`
3. Email `project.zip` (single file)
4. Recipient extracts and reads `.md` to understand structure

---

## 3. Web Form File Upload

### Problem
A service (bug tracker, survey form, web IDE) accepts files but not folders.

### Solution
```bash
# Flatten
python3 flatter.py ~/my-site output/

# Recipient either:
# A) Uploads files individually to the web form
# B) Reads structure.md to manually reconstruct locally
```

---

## 4. Portable Project Bundle

### Problem
You want to share a snapshot of your project that's self-contained and reconstructible.

### Solution
```bash
# Flatten
python3 flatter.py ~/project output/

# Create archive with metadata
cd output
tar czf project_snapshot.tar.gz *
cd ..

# Share project_snapshot.tar.gz
# Recipient can:
# 1. Extract and see all files
# 2. Read .md to understand original layout
# 3. Reconstruct folder structure manually if needed
```

---

## 5. Code Generation Context

### Problem
An LLM or code generator needs to understand your project structure but can only process flat file lists.

### Solution
```bash
python3 flatter.py ~/my-project output/
# Use the flattened files + structure.md as context
```

**Example prompt:**
```
Here's my project structure (my_project_structure.md):
[paste content]

Here are my project files:
[paste all flattened files]

Generate a new feature that integrates with this codebase...
```

---

## 6. Collaborative Debugging

### Problem
You need to get a teammate or external expert to review your entire project quickly.

### Solution
1. Flatten: `python3 flatter.py ~/buggy-app output/`
2. Create a gist or paste bin with all files + structure.md
3. Share single link instead of multiple file shares
4. Colleague can quickly understand context

---

## 7. Documentation Snapshots

### Problem
You want to include a "snapshot" of a project structure in documentation.

### Solution
```bash
# Flatten
python3 flatter.py ~/example-project output/

# Copy the structure.md content into your docs
# Readers see exactly what files are where
```

---

## 8. Testing Framework Input

### Problem
A testing/analysis tool needs individual files and a structure manifest.

### Solution
```bash
# Flatten with custom exclusions for test data
python3 flatter.py ~/my-project output/ --exclude "*.log" "test_data"

# Feed output/ files to your testing framework
# Include structure.md for context about original layout
```

---

## 9. Archive & Storage

### Problem
You want to preserve a project in a format that's:
- Easy to backup
- Browseable without recreating folders
- Shareable as a flat structure

### Solution
```bash
# Flatten
python3 flatter.py ~/project_v1 output/

# Archive
tar czf project_v1_archive.tar.gz output/

# Store indefinitely
# If needed later, extract and use structure.md to reconstruct
```

---

## 10. Quick Project Sharing (No Setup)

### Problem
You want to share code with someone but don't want to deal with git, zips, or folder structures.

### Solution
```bash
# One command
python3 flatter.py ~/my-code output/

# Share single flat folder (via cloud storage, email, messaging)
# Recipient sees all files + structure.md immediately
# No extraction, no folder recreation needed
```

---

## Quick Decision Matrix

| Scenario | Best Approach |
|----------|---------------|
| Share with AI assistant | Flatten + upload structure.md + files |
| Email to colleague | Flatten + zip + email |
| Web form upload | Flatten + upload individually or zip |
| Git repository | Flatten + create branch with flat structure |
| Documentation | Flatten + include structure.md in docs |
| Code review tool | Flatten + create gist with files + map |
| Backup/Archive | Flatten + tar.gz for storage |
| Quick sharing | Flatten + share output/ folder via cloud |
