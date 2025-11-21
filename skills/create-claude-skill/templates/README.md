# Skill Templates

This folder contains templates for creating new Claude Code skills.

## Available Templates

### 1. template-script-based.md

Use this template for skills that execute Python scripts or other utilities.

**Includes:**
- SKILL.md structure (~18 lines)
- reference.md structure with TOC
- Folder organization guide
- Checklist

**Examples:** convert-docx-to-pdf, msword-format-table, sanitize-filenames

### 2. template-ai-only.md

Use this template for skills that provide guidance without executing scripts.

**Includes:**
- SKILL.md structure (~25-40 lines)
- reference.md structure with TOC
- Guidelines organization
- Workflow structure
- Checklist

**Examples:** sop-editing-content, sop-deep-editing, narrate-business-process

## How to Use Templates

1. **Choose appropriate template:**
   - Script-based: If skill executes code/scripts
   - AI-only: If skill provides guidance/rules

2. **Copy template content:**
   - Create new skill folder
   - Copy template sections
   - Fill in placeholders

3. **Customize:**
   - Replace `[skill-name]` with actual name
   - Replace `[placeholders]` with real content
   - Adjust sections as needed

4. **Verify:**
   - Use checklist at bottom of template
   - Ensure all sections complete
   - Test links and examples

## Template Conventions

**Placeholders:**
- `[skill-name]` - Lowercase with hyphens
- `[Skill Title]` - Title case
- `[Description]` - Replace with actual text
- `[arguments]` - Replace with actual arguments

**Sections marked (Optional):**
- Include if relevant to your skill
- Remove if not needed

**Examples:**
- Always include at least 3 real examples
- Show actual command syntax
- Include expected output

## Quick Start

**For script-based skill:**
```bash
# 1. Create folder
mkdir -p .claude/skills/my-new-skill

# 2. Copy template
cp templates/template-script-based.md temp.md

# 3. Create SKILL.md from template's SKILL.md section
# 4. Create reference.md from template's reference.md section
# 5. Copy your script
# 6. Update all paths
```

**For AI-only skill:**
```bash
# 1. Create folder
mkdir -p .claude/skills/my-new-skill

# 2. Copy template
cp templates/template-ai-only.md temp.md

# 3. Create SKILL.md from template's SKILL.md section
# 4. Create reference.md from template's reference.md section
```

## Best Practices

1. **Keep SKILL.md concise** - ~50 tokens
2. **Use table of contents** - For reference.md >100 lines
3. **Include real examples** - Not just syntax
4. **Update all paths** - No old script references
5. **Test before finalizing** - Verify all links work

## Need Help?

- See [../reference.md](../reference.md) for comprehensive guide
- See [../examples.md](../examples.md) for real skill examples
- Check existing skills for patterns
