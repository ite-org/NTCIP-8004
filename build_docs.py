import os
import re
import subprocess
import shutil
import tempfile

def extract_and_convert_mermaid():
    """Extract Mermaid code blocks, convert to SVG, and replace with image refs."""
    docs_dir = "docs"
    output_dir = os.path.join(docs_dir, "assets", "mermaid")
    os.makedirs(output_dir, exist_ok=True)
    
    # Create temporary directory and copy entire docs directory
    temp_dir = tempfile.mkdtemp()
    temp_docs_dir = os.path.join(temp_dir, "docs")
    shutil.copytree(docs_dir, temp_docs_dir)
    
    mermaid_count = 0  # Counter for unique SVG filenames
    
    for root, _, files in os.walk(temp_docs_dir):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Find all Mermaid code blocks
                mermaid_blocks = re.findall(r"```mermaid\n(.*?)\n```", content, re.DOTALL)
                if not mermaid_blocks:
                    continue
                
                new_content = content
                
                # Convert each Mermaid block to SVG
                for block in mermaid_blocks:
                    mermaid_count += 1
                    # Write Mermaid code to temporary file
                    temp_mmd = os.path.join(temp_dir, f"temp_{mermaid_count}.mmd")
                    with open(temp_mmd, "w", encoding="utf-8") as f:
                        f.write(block.strip())
                    
                    # Convert to SVG
                    svg_filename = f"mermaid-diagram-{mermaid_count}.svg"
                    svg_filepath = os.path.join(output_dir, svg_filename)
                    subprocess.run([
                        "mmdc",
                        "-i", temp_mmd,
                        "-o", svg_filepath,
                        "--outputFormat", "svg"
                    ], check=True)
                    
                    # Replace Mermaid block with image reference
                    img_ref = f"![Diagram {mermaid_count}](assets/mermaid/{svg_filename})"
                    new_content = new_content.replace(f"```mermaid\n{block}\n```", img_ref, 1)
                
                # Write modified content to temp file
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
    
    return temp_dir

def run_mkdocs_with_pdf(temp_dir):
    """Run mkdocs build with with-pdf using temporary Markdown files."""
    print("Generating PDF...")
    env = os.environ.copy()
    env["EXPORT_PDF"] = "1"
    
    # Temporarily replace docs directory
    orig_docs = "docs"
    shutil.move(orig_docs, "docs_orig")
    shutil.move(os.path.join(temp_dir, "docs"), orig_docs)
    
    try:
        subprocess.run(["mkdocs", "build", "--clean"], env=env, check=True)
    finally:
        # Restore original docs directory
        shutil.move(orig_docs, os.path.join(temp_dir, "docs"))
        shutil.move("docs_orig", orig_docs)
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    print("Converting Mermaid diagrams to images...")
    temp_dir = extract_and_convert_mermaid()
    run_mkdocs_with_pdf(temp_dir)
    print("PDF generated at pdf/document.pdf")