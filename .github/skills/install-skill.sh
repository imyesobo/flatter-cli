#!/bin/bash
# Quick script to add the flatten-project skill to another project

set -e

if [ -z "$1" ]; then
  echo "Usage: $0 <target-project-path>"
  echo ""
  echo "Example:"
  echo "  $0 ~/Dev/my-project"
  echo ""
  echo "This will copy the flatten-project skill to:"
  echo "  ~/Dev/my-project/.github/skills/flatten-project/"
  exit 1
fi

TARGET_PROJECT="$1"
SKILL_SOURCE="$(dirname "$0")/flatten-project"
SKILL_TARGET="$TARGET_PROJECT/.github/skills/flatten-project"

# Validate
if [ ! -d "$SKILL_SOURCE" ]; then
  echo "❌ Error: Skill not found at $SKILL_SOURCE"
  exit 1
fi

if [ ! -d "$TARGET_PROJECT" ]; then
  echo "❌ Error: Target project not found at $TARGET_PROJECT"
  exit 1
fi

# Create .github/skills if needed
mkdir -p "$TARGET_PROJECT/.github/skills"

# Copy skill
if [ -d "$SKILL_TARGET" ]; then
  echo "⚠️  Skill already exists at $SKILL_TARGET"
  read -p "Overwrite? (y/n) " -n 1 -r
  echo
  if [[ $REPLY =~ ^[Yy]$ ]]; then
    rm -rf "$SKILL_TARGET"
  else
    echo "Cancelled."
    exit 0
  fi
fi

cp -r "$SKILL_SOURCE" "$SKILL_TARGET"

echo "✅ Skill installed to:"
echo "   $SKILL_TARGET"
echo ""
echo "📝 Next steps:"
echo "   1. Update .github/skills/flatten-project/SKILL.md with your project's flatter path"
echo "   2. Commit to git: git add .github/skills/"
echo "   3. Developers can now type '/flatten-project' in Copilot chat"
echo ""
echo "💡 Tip: See .github/skills/flatten-project/references/integration-guide.md"
