#!/bin/bash

# LaTeX CV Compilation Script
# This script compiles the CV with proper bibliography handling

echo "Compiling CV..."

# First pass - generates aux files
xelatex cv.tex

# Process bibliography
bibtex cv

# Second pass - includes bibliography
xelatex cv.tex

# Third pass - resolves all references
xelatex cv.tex

echo "Compilation complete! CV output: cv.pdf"
