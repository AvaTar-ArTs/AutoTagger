#!/usr/bin/env python3
import sys
import os
from autotagger import AutoTagger

def main():
    if len(sys.argv) < 2:
        print("Usage: autotag <directory> [prefix]")
        sys.exit(1)
    
    target_dir = sys.argv[1]
    prefix = sys.argv[2] if len(sys.argv) > 2 else os.path.basename(target_dir.rstrip('/'))
    
    tagger = AutoTagger()
    tagger.run(target_dir, prefix)

if __name__ == "__main__":
    main()
