#!/bin/bash
# n8n Workflow Setup Script
# =========================

echo "🚀 Setting up n8n AI Agent Workflows"
echo "====================================="

# Check if n8n is running
if ! curl -s http://localhost:5678 > /dev/null; then
    echo "❌ n8n is not running. Please start n8n first:"
    echo "   n8n start"
    exit 1
fi

echo "✅ n8n is running"

# Create workflows directory
mkdir -p ~/.n8n/workflows

# Copy workflow files
echo "📁 Copying workflow files..."
cp *.json ~/.n8n/workflows/

echo "✅ Workflows copied to n8n directory"
echo ""
echo "Next steps:"
echo "1. Open n8n at http://localhost:5678"
echo "2. Go to Settings → Credentials"
echo "3. Add your API credentials"
echo "4. Import the workflows"
echo "5. Configure webhook URLs"
echo ""
echo "🎉 Setup complete!"
