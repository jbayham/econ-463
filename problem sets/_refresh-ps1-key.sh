#!/bin/sh
# The private renderer is present only in the instructor's checkout.
key_renderer=../dev/answer-keys/ps1/render_key.py
if [ -f "$key_renderer" ] && printf '%s\n' "$QUARTO_PROJECT_OUTPUT_FILES" | grep -Fxq 'problem-set-01.pdf'; then
  exec python3 "$key_renderer"
fi
