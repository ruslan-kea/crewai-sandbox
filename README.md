# Software Development Crew 👨‍💻

A multi-agent AI system powered by [CrewAI](https://crewai.com) that simulates a complete software development team. This crew demonstrates how specialized AI agents can collaborate to design, implement, and deploy a full-stack application from requirements to production.

## 🎯 Project Overview

This crew creates a **Todo Application with Real-time Collaboration** by having 6 specialized AI agents work together in a sequential workflow:

1. **📋 Product Manager** - Requirements analysis and user stories
2. **🏗️ Software Architect** - System design and technology stack
3. **⚙️ Backend Developer** - Server-side implementation
4. **🎨 Frontend Developer** - User interface and experience
5. **🔍 QA Engineer** - Testing strategy and quality assurance
6. **🚀 DevOps Engineer** - Deployment and infrastructure

## 🛠️ Technology Stack

The crew designs applications using modern technologies:
- **Backend**: Node.js, Express, TypeScript, PostgreSQL, Socket.io
- **Frontend**: React, TypeScript, WebSocket integration
- **Infrastructure**: Docker, Kubernetes, CI/CD pipelines
- **Real-time**: WebSocket communication for live collaboration

## 📁 Generated Output

Each agent creates a detailed output file:
- `01_requirements_analysis.md` - User stories, acceptance criteria, MVP scope
- `02_system_architecture.md` - Technical specifications and database design
- `03_backend_implementation.md` - API endpoints, server setup, code examples
- `04_frontend_implementation.md` - React components, hooks, state management
- `05_quality_assurance.md` - Testing strategy, automated tests, quality metrics
- `06_deployment_setup.md` - Docker containers, CI/CD, monitoring setup

## 🚀 Installation & Setup

Ensure you have Python >=3.10 <3.14 installed on your system.

1. **Install UV package manager:**
   ```bash
   pip install uv
   ```

2. **Install dependencies:**
   ```bash
   crewai install
   ```

3. **Add your OpenAI API key:**
   Create a `.env` file and add:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## 🎮 Running the Crew

Execute the software development workflow:

```bash
crewai run
```

This command:
- Assembles the 6-agent development team
- Processes the "Todo Application with Real-time Collaboration" project
- Generates comprehensive documentation and implementation details
- Creates individual output files for each development phase

## 📋 Crew Configuration

- **Agents**: Defined in `src/crew_ai_sandbox/config/agents.yaml`
- **Tasks**: Sequential workflow in `src/crew_ai_sandbox/config/tasks.yaml`  
- **Orchestration**: Main crew logic in `src/crew_ai_sandbox/crew.py`
- **Input Parameters**: Project configuration in `src/crew_ai_sandbox/main.py`

## 🎯 Use Cases

This crew demonstrates:
- **Multi-agent collaboration** on complex software projects
- **Sequential workflow** where each agent builds on previous work
- **Realistic development process** from requirements to deployment
- **Comprehensive documentation** generation
- **Modern software architecture** design and implementation

## 🔧 Customization

Modify the project type by editing `main.py`:
```python
inputs = {
    "project_type": "Your Custom Application Type"
}
```

Or customize agents and tasks in the respective YAML configuration files.

## 📚 Learn More

- [CrewAI Documentation](https://docs.crewai.com)
- [CrewAI GitHub](https://github.com/joaomdmoura/crewai)
- [CrewAI Discord Community](https://discord.com/invite/X4JWnZnxPb)

---

*This project showcases the power of multi-agent AI collaboration in software development, demonstrating how specialized agents can work together to create comprehensive, production-ready application designs.*
