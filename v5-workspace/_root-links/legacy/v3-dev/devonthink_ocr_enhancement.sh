#!/bin/bash
# DevonThink Alternative - OCR Enhancement Script
# Adds OCR capabilities to make it work like DevonThink for images/PDFs

if [ $# -lt 2 ]; then
    echo "Usage: $0 <directory> <output_prefix>"
    echo "Example: $0 ~/Documents/Scans scans_ocr"
    exit 1
fi

DIRECTORY="$1"
PREFIX="$2"

echo "Adding OCR capabilities to directory: $DIRECTORY"
echo "Output prefix: $PREFIX"

# Check if tesseract is installed
if ! command -v tesseract &> /dev/null; then
    echo "Tesseract OCR not found. Installing..."
    if command -v brew &> /dev/null; then
        brew install tesseract tesseract-lang
    else
        echo "Please install tesseract manually:"
        echo "  macOS: brew install tesseract tesseract-lang"
        echo "  Ubuntu: sudo apt install tesseract-ocr tesseract-ocr-eng"
        exit 1
    fi
fi

# Create temporary directory for OCR results
TEMP_DIR="/tmp/${PREFIX}_ocr_temp"
mkdir -p "$TEMP_DIR"

# Find all image and PDF files
IMAGE_FILES=$(find "$DIRECTORY" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" -o -iname "*.bmp" -o -iname "*.pdf" \))

if [ -z "$IMAGE_FILES" ]; then
    echo "No image/PDF files found in $DIRECTORY"
    exit 0
fi

echo "Processing image/PDF files for OCR..."

# Process each file
while IFS= read -r -d '' file; do
    filename=$(basename "$file")
    name="${filename%.*}"
    ext="${filename##*.}"
    
    echo "Processing: $filename"
    
    if [ "$ext" = "pdf" ]; then
        # For PDFs, extract text directly if possible, or convert to images
        if command -v pdftotext &> /dev/null; then
            pdftotext "$file" "$TEMP_DIR/${name}.txt" 2>/dev/null
        else
            # Convert PDF to images and OCR each page
            convert -density 300 "$file" "$TEMP_DIR/${name}_page_%03d.png" 2>/dev/null
            for page_img in "$TEMP_DIR/${name}_page_"*.png; do
                if [ -f "$page_img" ]; then
                    tesseract "$page_img" "$TEMP_DIR/${name}_$(basename "$page_img" .png)" txt 2>/dev/null
                fi
            done
        fi
    else
        # For images, run OCR directly
        tesseract "$file" "$TEMP_DIR/$name" txt 2>/dev/null
    fi
done < <(find "$DIRECTORY" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" -o -iname "*.bmp" -o -iname "*.pdf" \) -print0)

# Combine all OCR results into a single file for indexing
OUTPUT_FILE="$TEMP_DIR/combined_ocr_results.txt"
cat "$TEMP_DIR"/*.txt > "$OUTPUT_FILE" 2>/dev/null

echo "OCR processing complete!"
echo "Results saved to: $OUTPUT_FILE"
echo "Temporary files in: $TEMP_DIR"

# Optionally, run the multi-format indexer on the OCR results
echo "Running multi-format indexer on OCR results..."
python3 ~/AutoTagger/v3-dev/multi_format_directory_indexer.py "$TEMP_DIR" "${PREFIX}_ocr" "json,csv,md"

echo "DevonThink-like OCR enhancement complete!"
echo "Your images and PDFs have been processed with OCR and indexed."