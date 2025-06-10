# SpiceflowNavigator-Strategy

**Strategy Agent** for SpiceflowNavigator

## Quick Start

```bash
# Clone with submodules (for agents)
git clone --recursive git@github.com:pa5tabear/SpiceflowNavigator-Strategy.git
cd SpiceflowNavigator-Strategy

# Install dependencies
make install

# Run tests
make test
```

## Agent Responsibilities

- 🎯 **Strategic analysis and goal scoring**
- 📊 **Content relevance evaluation**
- 💡 **Insight generation and ranking**
- 🔍 **Hybrid search and matching**

## Development Commands

```bash
make help          # Show all commands
make test          # Run tests
make install       # Install dependencies  
make dev           # Start development server
make clean         # Clean temporary files
```


## CommonUtils Submodule

This repository includes CommonUtils as a submodule:

```bash
# Update CommonUtils to latest
git submodule update --remote common-utils

# Install CommonUtils in development mode
pip install -e ./common-utils/
```

## Related Repositories

- [Pipeline Agent](git@github.com:pa5tabear/SpiceflowNavigator-Pipeline) - End-to-end orchestration
- [Ingest Agent](git@github.com:pa5tabear/SpiceflowNavigator-Ingest) - RSS + transcription
- [Strategy Agent](git@github.com:pa5tabear/SpiceflowNavigator-Strategy) - Analysis + scoring
- [UI Agent](git@github.com:pa5tabear/SpiceflowNavigator-UI) - User interface
- [CommonUtils](git@github.com:pa5tabear/SpiceflowNavigator-CommonUtils) - Shared utilities

## Architecture

This repository is part of SpiceflowNavigator's **4-Agent Architecture**:

```
Pipeline ←→ Ingest
    ↓         ↓
Strategy ←→ CommonUtils ←→ UI
```

Each agent operates independently while sharing common utilities.

---
*Part of the SpiceflowNavigator 4-Agent Architecture*
