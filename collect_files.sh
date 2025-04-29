#!/bin/bash

IN="$1"
OUT="$2"
PAR=""

if [ "$3" = "--max_depth" ] && [ -n "$4" ]; then
  PAR="$4"
fi

python3 collect_files.py "$IN" "$OUT" "$PAR"