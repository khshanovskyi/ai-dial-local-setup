# Practice with DIAL Core, Chat, Themes and Adapter setup

## Project Structure

```
├── core/
│   └── config.json               🚧 TODO: Follow instructions in tasks. DIAL Core configuration with routes, applications, models, and keys
├── settings/
│   └── settings.json             ✅ Complete - Core server settings and identity providers
├── tasks/                        
│   ├── t1/
│   │   └── start.md              🚧 TODO: Follow instructions 
│   ├── t2/
│   │   ├── .env                  ✅ Complete - Environment configuration
│   │   ├── core/
│   │   │   └── config.json       🚧 TODO: Follow instructions
│   │   ├── docker-compose.yml    ✅ Complete - Extended compose with echo service
│   │   ├── echo/
│   │   │   ├── Dockerfile        ✅ Complete - Echo app containerization
│   │   │   ├── app.py            ✅ Complete - Simple echo application
│   │   │   └── requirements.txt  ✅ Complete - Python dependencies
│   │   └── task_2.md             🚧 TODO: Follow instructions
│   ├── t3/
│   │   ├── echo/
│   │   │   ├── app.py            ✅ Complete - Modified echo for local development
│   │   │   └── requirements.txt  ✅ Complete - Updated dependencies
│   │   └── task_3.md             🚧 TODO: Follow instructions 
│   ├── t4/
│   │   └── task_4.md             🚧 TODO: Follow instructions 
│   └── t5/
│       ├── essay_assistant/
│       │   ├── app.py            🚧 TODO: Complete implementation with AsyncDial client
│       │   └── requirements.txt  ✅ Complete - Dependencies for essay assistant
│       └── task_5.md             🚧 TODO: Follow instructions 
└── docker-compose.yml            🚧 TODO: - Main compose file (Add NASA_API_KEY)
```

## Services Architecture

### Core Services
- **themes** (port 3001) - DIAL Chat themes service
- **chat** (port 3000) - Main DIAL Chat interface
- **core** (port 8080) - DIAL Core API gateway
- **redis** (port 6379) - Cache and session storage
- **adapter-dial** - DIAL adapter for upstream model communication

### Development Applications
- **echo** (port 5000/5022) - Simple echo application for testing
- **essay-assistant** (port 5025) - Essay-focused AI assistant

## Configuration Files
- **core/config.json** - Main DIAL configuration with applications, models, and API keys
- **settings/settings.json** - Core server settings and security configuration
- **docker-compose.yml** - Service orchestration and networking

## Learning Path
1. **T1** - Basic DIAL Chat setup
2. **T2** - First Echo application in container
3. **T3** - Local development workflow
4. **T4** - Models and adapter integration
5. **T5** - Advanced application with streaming

## Environment Requirements
- Docker and Docker Compose
- Python 3.11+ for local development
- DIAL API key for model access

---
# <img src="dialx-banner.png">