# n8n Automation Environment

This directory contains your n8n automation setup with intelligent workflows and configurations.

## Quick Start

```bash
# Start n8n
n8n-start

# Start with tunnel (for external access)
n8n-dev

# Stop n8n
n8n-stop

# Check status
n8n-status

# View logs
n8n-logs
```

## Available Workflows

1. **AI Content Generator** - Generate content using AI
2. **File Processor** - Intelligent file analysis and processing
3. **AI Sites Deployer** - Automated deployment for ai-sites projects

## Configuration

- Config file: `/Users/steven/.n8n/config.json`
- Environment: `/Users/steven/.env.d/n8n.env`
- Workflows: `/Users/steven/.n8n/workflows/`
- Logs: `/Users/steven/.n8n/n8n.log`

## Web Interface

Access n8n at: http://localhost:5678

## API Endpoints

- Webhook: http://localhost:5678/webhook/
- REST API: http://localhost:5678/api/
- Swagger UI: http://localhost:5678/api-docs/

## Service Management

```bash
# Start as service
/Users/steven/.n8n/service.sh start

# Stop service
/Users/steven/.n8n/service.sh stop

# Check status
/Users/steven/.n8n/service.sh status

# Restart service
/Users/steven/.n8n/service.sh restart
```
