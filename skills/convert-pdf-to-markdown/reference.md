# Convert PDF to Markdown - Reference Documentation

## When to Use This Skill
Activate this skill when the user requests to:
- Convert PDF files to Markdown format
- Extract text from PDF documents
- Transform PDFs to text for LLM processing
- Batch convert PDFs in a folder
- Extract tables from PDF files

## Script Location & Usage
Script: `.claude/skills/convert-pdf-to-markdown/convert-pdf-to-markdown.py`

Always activate the virtual environment:
```bash
source .venv/bin/activate
```

## Conversion Method
Uses **pymupdf4llm** library for fast, accurate conversion:
- Fast C++ backend via PyMuPDF
- Accurate table extraction and preservation
- LLM-optimized Markdown output
- Clean formatting without artifacts
- Preserves document structure

## Three Input Modes

### Mode 1: Single File Conversion
```bash
python .claude/skills/convert-pdf-to-markdown/convert-pdf-to-markdown.py path/to/file.pdf
```
Output: Markdown file saved in same directory as source PDF

### Mode 2: Multiple Files (Comma-Separated)
```bash
python .claude/skills/convert-pdf-to-markdown/convert-pdf-to-markdown.py "file1.pdf,file2.pdf,file3.pdf"
```
Output: Each Markdown file saved in same directory as respective PDF file

### Mode 3: Folder Mode (Test-First Safety)
```bash
python .claude/skills/convert-pdf-to-markdown/convert-pdf-to-markdown.py ./path/to/folder
```

**Workflow**:
1. Scans folder for all `.pdf` files
2. Tests conversion on first file
3. Shows result and prompts for confirmation
4. If user enters `y`, processes all remaining files
5. Shows progress and final summary

## What Gets Converted

### Input Format
- **Extension**: `.pdf` files only
- **Type**: Text-based PDFs (not scanned images)
- **Content**: Text, tables, lists, headings

### Output Format
- **Extension**: `.md` (Markdown)
- **Location**: Same directory as source PDF
- **Encoding**: UTF-8
- **Naming**: Same filename, .md extension

### Extracted Content
- Text content with proper formatting
- Headings and document structure
- Tables (accurately preserved in Markdown)
- Lists and bullet points
- Basic text formatting (bold, italic)
- Optimized for LLM processing

### Limitations
- **Scanned PDFs**: Requires OCR (not included)
- **Images**: Not extracted or embedded
- **Complex layouts**: Multi-column may not preserve exactly
- **Encrypted PDFs**: Not supported
- **Forms**: Interactive elements not converted

## Important Notes
- **Files preserved**: Original PDF files remain unchanged
- **Output location**: Markdown files saved alongside source PDFs
- **Fast conversion**: ~1-3 seconds per typical document
- **Test-first for folders**: Always tests first file before batch
- **User confirmation**: Batch operations require confirmation
- **Accurate tables**: Table structure preserved in Markdown format

## Use Cases

### Extract PDF Content for Analysis
```bash
python .claude/skills/convert-pdf-to-markdown/convert-pdf-to-markdown.py "./reports/quarterly-report.pdf"
```

### Batch Convert Documentation
```bash
python .claude/skills/convert-pdf-to-markdown/convert-pdf-to-markdown.py "./documentation/"
```

### LLM Preprocessing
```bash
python .claude/skills/convert-pdf-to-markdown/convert-pdf-to-markdown.py "./research-papers/"
```

## Troubleshooting

### "No module named 'pymupdf4llm'"
Install: `source .venv/bin/activate && pip install pymupdf4llm`

### "No PDF files found in folder"
- Verify folder path is correct
- Check that `.pdf` files exist
- Use forward slashes

### Conversion fails for specific PDF
- **Encrypted PDF**: Remove password protection first
- **Scanned PDF**: Use OCR software to add text layer
- **Corrupted file**: Try opening in PDF viewer to verify

### Missing content in output
- Check source PDF has text layer (not scanned image)
- Verify PDF is not encrypted or protected

## Advanced Usage

### For Different Folders
```bash
python .claude/skills/convert-pdf-to-markdown/convert-pdf-to-markdown.py "./YOUR-FOLDER-PATH"
```

### Processing Specific Files from Different Folders
```bash
python .claude/skills/convert-pdf-to-markdown/convert-pdf-to-markdown.py "./folder1/doc1.pdf,./folder2/doc2.pdf"
```

## Related Skills
- **pdf-delete-pages**: Delete specific pages from PDF files
- **pdf-split-pages**: Split PDF into multiple parts

## Dependencies
- Python 3.6+
- pymupdf4llm library (via pip)
- Project virtual environment (.venv)

## Performance Notes
- **Speed**: ~1-3 seconds per typical document
- **Small PDFs** (1-10 pages): < 1 second
- **Large PDFs** (50+ pages): 3-10 seconds
- **Memory efficient**: Processes files sequentially
