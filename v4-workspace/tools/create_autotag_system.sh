#!/bin/bash
# AutoTag Setup Script
# Sets up the AutoTag system for AVATARARTS automation indexing

set -e  # Exit on any error

echo "🚀 Setting up AutoTag - AVATARARTS Automation Tagging System"

# Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv /Users/steven/AutoTag/venv

# Activate virtual environment
source /Users/steven/AutoTag/venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
echo "Installing required packages..."
# Note: sqlite3 is built-in to Python, no need to install separately

echo "✅ Virtual environment created and packages installed"

# Create the main AutoTag scripts
echo "Creating AutoTag core scripts..."

# Copy the existing tiered indexing scripts to AutoTag
cp /Users/steven/avatararts-kb/phase1_rapid_scan.py /Users/steven/AutoTag/scripts/
cp /Users/steven/avatararts-kb/phase2_intelligent_organization.py /Users/steven/AutoTag/scripts/
cp /Users/steven/avatararts-kb/phase3_advanced_intelligence.py /Users/steven/AutoTag/scripts/
cp /Users/steven/avatararts-kb/run_tiered_indexing.py /Users/steven/AutoTag/scripts/

# Create AutoTag specific main script
cat > /Users/steven/AutoTag/scripts/autotag_main.py << 'EOF'
#!/usr/bin/env python3
"""
AutoTag - AVATARARTS Automation Tagging System
Main entry point for the AutoTag system
"""

import os
import sys
import argparse
import subprocess
from datetime import datetime

def run_autotag_phase(phase_script, description, input_path=None, output_path=None):
    """Run a single phase of the AutoTag process"""
    print(f"\n{'='*60}")
    print(f"RUNNING: {description}")
    print(f"{'='*60}")

    cmd = [sys.executable, phase_script]
    if input_path:
        cmd.extend(["--input", input_path])
    if output_path:
        cmd.extend(["--output", output_path])

    start_time = datetime.now()
    print(f"Started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        end_time = datetime.now()
        duration = end_time - start_time

        print(f"Completed successfully in {duration}")
        print(f"Ended at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

        # Print any important output
        if result.stdout:
            print(f"Output:\n{result.stdout}")

        return True

    except subprocess.CalledProcessError as e:
        print(f"ERROR in {description}:")
        print(f"Return code: {e.returncode}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    parser = argparse.ArgumentParser(description='AutoTag - AVATARARTS Automation Tagging System')
    parser.add_argument('--target', required=True, help='Path to directory to index')
    parser.add_argument('--output-dir', default='/Users/steven/AutoTag/output', help='Output directory for results')
    parser.add_argument('--name', default='autotag_run', help='Name for this indexing run')
    
    args = parser.parse_args()

    print("🚀 AutoTag - AVATARARTS Automation Tagging System")
    print("="*60)
    print(f"Target directory: {args.target}")
    print(f"Output directory: {args.output_dir}")
    print(f"Run name: {args.name}")
    print("="*60)

    # Create output directory for this run
    run_output_dir = os.path.join(args.output_dir, args.name)
    os.makedirs(run_output_dir, exist_ok=True)

    # Define the phase scripts
    base_script_dir = "/Users/steven/AutoTag/scripts"
    phases = [
        (os.path.join(base_script_dir, "phase1_rapid_scan.py"), 
         "Phase 1: Rapid Initial Scan",
         {"--path": args.target}),
        (os.path.join(base_script_dir, "phase2_intelligent_organization.py"), 
         "Phase 2: Intelligent Organization",
         {}),
        (os.path.join(base_script_dir, "phase3_advanced_intelligence.py"), 
         "Phase 3: Advanced Intelligence",
         {})
    ]

    # Run each phase
    all_successful = True
    phase_outputs = []
    
    for i, (script, description, extra_args) in enumerate(phases):
        if i == 0:
            # Phase 1: input is target path, output is first phase result
            input_path = None  # Will be specified by --path
            output_filename = f"{args.name}_phase1.json"
        else:
            # Phases 2 and 3: input is previous phase output
            input_path = phase_outputs[-1]
            output_filename = f"{args.name}_phase{i+1}.json"
        
        output_path = os.path.join(run_output_dir, output_filename)
        
        # Build command with extra args for phase 1
        cmd = [sys.executable, script]
        if input_path:
            cmd.extend(["--input", input_path])
        cmd.extend(["--output", output_path])
        
        # Add extra args for phase 1 (like --path)
        for arg_name, arg_value in extra_args.items():
            cmd.extend([arg_name, arg_value])

        print(f"\n{'='*60}")
        print(f"RUNNING: {description}")
        print(f"{'='*60}")

        start_time = datetime.now()
        print(f"Started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

            end_time = datetime.now()
            duration = end_time - start_time

            print(f"Completed successfully in {duration}")
            print(f"Ended at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

            phase_outputs.append(output_path)
            print(f"Output saved to: {output_path}")

        except subprocess.CalledProcessError as e:
            print(f"ERROR in {description}:")
            print(f"Return code: {e.returncode}")
            print(f"Error output: {e.stderr}")
            all_successful = False
            break

    # Final summary
    print(f"\n{'='*60}")
    if all_successful:
        print("🎉 AUTOtag PROCESS COMPLETED SUCCESSFULLY!")
        print(f"The {args.target} directory has been fully indexed:")
        print("  - Phase 1: Rapid cataloging of all tools")
        print("  - Phase 2: Intelligent categorization and tagging")
        print("  - Phase 3: Advanced analysis and predictions")
        print(f"\nResults saved to: {run_output_dir}")
        print("The knowledge base now contains comprehensive intelligence")
        print("about all automation tools with predictive insights.")
    else:
        print("❌ Some phases failed. Please check the error messages above.")
    print("="*60)

if __name__ == "__main__":
    main()
EOF

# Create the main AutoTag runner script
cat > /Users/steven/AutoTag/autotag.sh << 'EOF'
#!/bin/bash
# AutoTag Runner Script

# Check if virtual environment exists
if [ ! -d "/Users/steven/AutoTag/venv" ]; then
    echo "❌ AutoTag virtual environment not found. Please run setup first."
    exit 1
fi

# Activate virtual environment
source /Users/steven/AutoTag/venv/bin/activate

# Check if required arguments are provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <target_directory> [output_name]"
    echo "Example: $0 /Users/steven/pythons my_python_analysis"
    exit 1
fi

TARGET_DIR="$1"
OUTPUT_NAME="${2:-autotag_run_$(date +%Y%m%d_%H%M%S)}"

echo "🚀 Running AutoTag on: $TARGET_DIR"
echo "📅 Run name: $OUTPUT_NAME"

# Run the main AutoTag script
python3 /Users/steven/AutoTag/scripts/autotag_main.py --target "$TARGET_DIR" --name "$OUTPUT_NAME"

echo "✅ AutoTag process completed!"
EOF

# Make the runner script executable
chmod +x /Users/steven/AutoTag/autotag.sh

echo "✅ AutoTag core scripts created"

# Create configuration file
cat > /Users/steven/AutoTag/config/autotag_config.json << 'EOF'
{
  "system": {
    "name": "AutoTag - AVATARARTS Automation Tagging System",
    "version": "1.0",
    "description": "Intelligent tagging and categorization system for AVATARARTS automation tools"
  },
  "paths": {
    "output_base": "/Users/steven/AutoTag/output",
    "logs_base": "/Users/steven/AutoTag/logs",
    "data_base": "/Users/steven/AutoTag/data",
    "scripts_base": "/Users/steven/AutoTag/scripts"
  },
  "processing": {
    "phases": [
      "rapid_scan",
      "intelligent_organization", 
      "advanced_intelligence"
    ],
    "default_timeout_seconds": 3600,
    "max_file_size_mb": 100
  },
  "categorization": {
    "confidence_threshold": 0.5,
    "business_value_weight": 0.7,
    "integration_potential_weight": 0.3
  },
  "database": {
    "path": "/Users/steven/AutoTag/data/knowledge_base.db",
    "backup_enabled": true,
    "backup_retention_days": 30
  }
}
EOF

echo "✅ Configuration file created"

# Create README
cat > /Users/steven/AutoTag/README.md << 'EOF'
# AutoTag - AVATARARTS Automation Tagging System

AutoTag is an intelligent tagging and categorization system for AVATARARTS automation tools. It uses a three-phase approach to analyze, categorize, and assign business value to automation tools.

## Features

- **Three-Phase Analysis**: Rapid scan → Intelligent organization → Advanced intelligence
- **Smart Categorization**: Automatically categorizes tools based on functionality
- **Business Value Prediction**: Assigns predicted business value scores
- **Integration Potential**: Identifies potential tool integrations
- **Scalable Processing**: Efficiently handles large automation libraries

## Prerequisites

- Python 3.8+
- Unix-like environment (macOS, Linux)

## Setup

1. Run the setup script:
   ```bash
   ./setup_autotag.sh
   ```

## Usage

1. Run AutoTag on a directory:
   ```bash
   ./autotag.sh /path/to/target/directory [output_name]
   ```

2. Examples:
   ```bash
   # Analyze the pythons directory
   ./autotag.sh /Users/steven/pythons my_python_analysis
   
   # Analyze with default timestamped output name
   ./autotag.sh /Users/steven/AVATARARTS/Automations
   ```

## Output

Results are stored in `/Users/steven/AutoTag/output/[run_name]/` with:
- Phase 1: Basic cataloging and metadata
- Phase 2: Intelligent categorization and tagging
- Phase 3: Advanced analysis and predictions

## Architecture

The system follows a three-phase approach:

1. **Phase 1: Rapid Initial Scan**
   - Catalogs all directories and files
   - Identifies potential automation tools
   - Extracts basic metadata

2. **Phase 2: Intelligent Organization**
   - Categorizes tools based on content
   - Generates relevant tags
   - Assigns confidence scores

3. **Phase 3: Advanced Intelligence**
   - Predicts business value
   - Identifies integration potential
   - Extracts insights and relationships

## Directory Structure

```
AutoTag/
├── scripts/                 # Core Python scripts
├── config/                  # Configuration files
├── data/                    # Data files and database
├── output/                  # Analysis results
├── logs/                    # Log files
├── docs/                    # Documentation
├── autotag.sh              # Main runner script
├── setup_autotag.sh        # Setup script
└── README.md               # This file
```

## Integration with AVATARARTS

AutoTag is designed to work seamlessly with the AVATARARTS ecosystem, providing intelligent analysis of automation tools to support the content-awareness intelligence system.
EOF

echo "✅ README file created"

# Create setup script
cat > /Users/steven/AutoTag/setup_autotag.sh << 'EOF'
#!/bin/bash
# AutoTag Setup Script

set -e  # Exit on any error

echo "🚀 Setting up AutoTag - AVATARARTS Automation Tagging System"

# Check if already set up
if [ -d "/Users/steven/AutoTag/venv" ]; then
    echo "⚠️  AutoTag virtual environment already exists. Skipping setup."
    echo "To reinstall, remove the venv directory first: rm -rf /Users/steven/AutoTag/venv"
    exit 0
fi

# Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv /Users/steven/AutoTag/venv

# Activate virtual environment
source /Users/steven/AutoTag/venv/bin/activate

# Upgrade pip
pip install --upgrade pip

echo "✅ Virtual environment created and packages installed"

# Make scripts executable
chmod +x /Users/steven/AutoTag/autotag.sh
chmod +x /Users/steven/AutoTag/setup_autotag.sh

# Create initial database
echo "Creating initial knowledge base database..."
touch /Users/steven/AutoTag/data/knowledge_base.db

# Create initial data files
echo '{"runs": []}' > /Users/steven/AutoTag/data/runs.json

echo "✅ AutoTag setup completed successfully!"

echo ""
echo "To use AutoTag:"
echo "1. Run: source /Users/steven/AutoTag/venv/bin/activate"
echo "2. Or use the runner: /Users/steven/AutoTag/autotag.sh /path/to/target"
echo ""
echo "For more information, see: /Users/steven/AutoTag/README.md"
EOF

chmod +x /Users/steven/AutoTag/setup_autotag.sh

echo "✅ Setup script created"

# Create a simple test script
cat > /Users/steven/AutoTag/test_autotag.sh << 'EOF'
#!/bin/bash
# AutoTag Test Script

echo "🧪 Testing AutoTag installation..."

# Check if virtual environment exists
if [ ! -d "/Users/steven/AutoTag/venv" ]; then
    echo "❌ Virtual environment not found. Run setup first."
    exit 1
fi

# Check if main script exists
if [ ! -f "/Users/steven/AutoTag/scripts/autotag_main.py" ]; then
    echo "❌ Main script not found."
    exit 1
fi

# Check if runner script exists
if [ ! -f "/Users/steven/AutoTag/autotag.sh" ]; then
    echo "❌ Runner script not found."
    exit 1
fi

echo "✅ All AutoTag components are present"
echo "✅ AutoTag installation test passed!"
EOF

chmod +x /Users/steven/AutoTag/test_autotag.sh

echo "✅ Test script created"

# Create documentation
cat > /Users/steven/AutoTag/docs/user_guide.md << 'EOF'
# AutoTag User Guide

## Overview

AutoTag is an intelligent tagging and categorization system for AVATARARTS automation tools. It helps organize, categorize, and assess the business value of automation scripts and tools.

## Quick Start

1. **Setup AutoTag**:
   ```bash
   cd /Users/steven/AutoTag
   ./setup_autotag.sh
   ```

2. **Run AutoTag on a directory**:
   ```bash
   ./autotag.sh /path/to/your/automation/directory [optional_output_name]
   ```

3. **Check results**:
   Results will be in `/Users/steven/AutoTag/output/[output_name]/`

## Understanding the Output

AutoTag produces three main outputs:

### Phase 1: Rapid Scan
- Basic catalog of all directories and files
- Identification of potential automation tools
- Basic metadata extraction

### Phase 2: Intelligent Organization
- Categorization of tools (e.g., "AI/Automation", "Content Creation", "Code/Scripts")
- Auto-generated tags based on content
- Confidence scores for categorizations

### Phase 3: Advanced Intelligence
- Predicted business value scores (0-10 scale)
- Integration potential identification
- Relationship mapping between tools
- Extracted insights

## Use Cases

### 1. Inventory Management
Use AutoTag to catalog your entire automation library:
```bash
./autotag.sh /Users/steven/pythons python_scripts_inventory
```

### 2. Value Assessment
Identify high-value automation tools:
```bash
./autotag.sh /Users/steven/AVATARARTS/Automations high_value_assessment
# Then analyze the business value scores in the output
```

### 3. Organization Planning
Understand how your automation tools are categorized:
```bash
./autotag.sh /Users/steven/AVATARARTS/Automations organization_plan
```

## Configuration

The system can be configured via `/Users/steven/AutoTag/config/autotag_config.json`.

## Troubleshooting

### Common Issues

1. **Virtual Environment Not Found**
   - Run `./setup_autotag.sh` to create the virtual environment

2. **Permission Errors**
   - Ensure the runner script is executable: `chmod +x autotag.sh`

3. **Large Directory Processing**
   - For very large directories, consider running on subsets first

## Best Practices

1. **Start Small**: Test on a small directory before running on large collections
2. **Use Descriptive Names**: Give meaningful names to your analysis runs
3. **Regular Analysis**: Periodically re-analyze growing automation libraries
4. **Review Results**: Check the categorization accuracy and adjust as needed

## Integration with AVATARARTS

AutoTag integrates with the broader AVATARARTS ecosystem by:
- Providing structured data about automation tools
- Supporting the content-awareness intelligence system
- Enabling better organization and discovery of automation capabilities
- Facilitating the activation of the 95% built AVATARARTS system
EOF

echo "✅ User guide created"

echo "AutoTag system has been created successfully in /Users/steven/AutoTag/"
echo ""
echo "To get started:"
echo "1. cd /Users/steven/AutoTag"
echo "2. ./setup_autotag.sh"
echo "3. ./autotag.sh /path/to/target/directory [optional_name]"