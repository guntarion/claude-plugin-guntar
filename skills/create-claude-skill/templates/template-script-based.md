# Template: Script-Based Skill

Use this template for skills that execute Python scripts or other utilities.

## SKILL.md Template

```markdown
---
name: [skill-name]
description: [Brief description (max 1024 chars). Include WHAT it does AND WHEN to use it. Be specific with trigger keywords.]
---

# [Skill Title]

[One sentence summary of what this skill does]

## Quick Start

```bash
source .venv/bin/activate
python .claude/skills/[skill-name]/[skill-name].py <arguments>
```

**For detailed documentation**, see [reference.md](./reference.md)
**For script details**, see [README.md](./README.md)
```

## reference.md Template

```markdown
# [Skill Name] - Reference Guide

## Table of Contents
1. [When to Use This Skill](#when-to-use-this-skill)
2. [Features](#features)
3. [Usage](#usage)
4. [How It Works](#how-it-works)
5. [Examples](#examples)
6. [What Gets Modified](#what-gets-modified)
7. [What Gets Preserved](#what-gets-preserved)
8. [Limitations](#limitations)
9. [Troubleshooting](#troubleshooting)
10. [Tips](#tips)
11. [Related Skills](#related-skills)
12. [Dependencies](#dependencies)
13. [Performance Notes](#performance-notes)

## When to Use This Skill

Activate this skill when the user requests to:
- [Use case 1]
- [Use case 2]
- [Use case 3]

## Features

- **[Feature 1]:** [Description]
- **[Feature 2]:** [Description]
- **[Feature 3]:** [Description]

## Usage

### Basic Usage

```bash
source .venv/bin/activate
python .claude/skills/[skill-name]/[skill-name].py <input>
```

This creates: `[output description]`

**Example:**
```bash
python .claude/skills/[skill-name]/[skill-name].py ./path/to/file.ext
# Creates: ./path/to/file-processed.ext
```

### Advanced Usage (Optional)

```bash
python .claude/skills/[skill-name]/[skill-name].py <input> <output> [--options]
```

## How It Works

1. **[Step 1]:**
   - [Description]
   - [Details]

2. **[Step 2]:**
   - [Description]
   - [Details]

3. **[Step 3]:**
   - [Description]
   - [Output]

## Examples

### Example 1: [Basic Usage]

User: "[User request]"

```bash
source .venv/bin/activate
python .claude/skills/[skill-name]/[skill-name].py [arguments]
```

### Example 2: [Advanced Usage]

User: "[User request]"

```bash
source .venv/bin/activate
python .claude/skills/[skill-name]/[skill-name].py [arguments] [options]
```

### Example Output

```
Input:  [input file]
Output: [output file]

[Processing message...]

============================================================
✓ Processing complete!
  [Statistics]
  Output saved: [path]
============================================================
```

## What Gets Modified

**[Target 1]:**
- ✓ [Change 1]
- ✓ [Change 2]

**[Target 2]:**
- ✓ [Change 1]
- ✓ [Change 2]

## What Gets Preserved

- **[Preserved 1]:** [Description]
- **[Preserved 2]:** [Description]
- **[Preserved 3]:** [Description]

## Limitations

### Does Not Handle

- **[Limitation 1]:** [Explanation]
- **[Limitation 2]:** [Explanation]

### Workarounds

- **[Limitation 1]:** [Workaround solution]
- **[Limitation 2]:** [Workaround solution]

## Troubleshooting

### [Common Error 1]

```
Error: [error message]
```

**Solution:** [How to fix]

### [Common Error 2]

```
Error: [error message]
```

**Solution:** [How to fix]

### [Common Issue]

If [condition]:
- [Possible cause 1]
- [Possible cause 2]
- [Solution]

## Tips

1. **[Tip 1]:** [Description]
2. **[Tip 2]:** [Description]
3. **[Tip 3]:** [Description]

## Related Skills

- **[skill-name]**: [Brief description of how it relates]
- **[skill-name]**: [Brief description of how it relates]

## Dependencies

- **[dependency-1]**: [Purpose]
- **[dependency-2]**: [Purpose] (built-in)
- Project virtual environment (.venv)

## Performance Notes

- **Speed:** [Typical performance]
- **Example:** [Specific benchmark]
- **Memory:** [Memory usage]
- **Typical:** [Common use case performance]
```

## Folder Structure

```
skill-name/
├── SKILL.md              # Use template above (~18 lines)
├── reference.md          # Use template above (200-300 lines)
├── README.md             # Copy from original script readme
└── skill-name.py         # Copy script, remove numbering
```

## Checklist

- [ ] Skill folder created
- [ ] Script copied without numbering
- [ ] README.md copied
- [ ] SKILL.md created with frontmatter
- [ ] reference.md created with TOC
- [ ] All script paths updated
- [ ] Examples are clear
- [ ] Troubleshooting section complete
- [ ] Links verified
