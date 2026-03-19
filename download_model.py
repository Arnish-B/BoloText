#!/usr/bin/env python3
"""
Helper script to download Whisper model with SSL workaround
Run this BEFORE running the main PoC script
"""

import ssl
import urllib.request
import whisper

# Workaround for SSL certificate verification issues on macOS
ssl._create_default_https_context = ssl._create_unverified_context

print("="*60)
print("Downloading Whisper Model (base)")
print("="*60)
print("\nThis may take a few minutes (~150MB download)...")
print()

try:
    model = whisper.load_model("base")
    print("\n✓ Model downloaded successfully!")
    print("You can now run: python poc_voice_to_hinglish.py")
except Exception as e:
    print(f"\n✗ Error downloading model: {e}")
    print("\nTry running this command to fix SSL certificates:")
    print("/Applications/Python\\ 3.*/Install\\ Certificates.command")
