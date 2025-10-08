#!/bin/bash
# Extract patient IDs from the first column and count unique values
# Expected tools: cut, sort, uniq, wc
# Output format: Single number (e.g., "10000")
# Save to: output/part1_patient_count.txt
cd /
wc -l health.data.csv
cut -d',' -f1 health.data.csv|tail -n +2|sort|uniq -c 

