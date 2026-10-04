# Samadrit Das — Detailed Professional Profile

## About Me

Samadrit Das is a software engineer, technical architect, and creative technologist based in Kolkata, India, with a strong interest in AI engineering, distributed systems, full-stack development, embedded systems, and interactive computing.

His engineering journey started with practical software projects in 2020 and progressed through full-stack applications, IoT and hardware systems, production-oriented health-tech software, and enterprise AI/RAG systems.

He enjoys building complete systems rather than working only on isolated features. His experience spans frontend applications, backend APIs, databases, cloud services, search and retrieval systems, AI applications, embedded hardware, computer vision, blockchain-oriented architectures, and developer tooling.

He is particularly interested in:

- Artificial Intelligence and AI engineering
- Retrieval-Augmented Generation (RAG)
- Semantic and hybrid search
- Software architecture
- Developer tools and repository intelligence
- Full-stack web development
- Embedded systems and IoT
- Robotics and hardware-software integration
- Interactive WebGL/Three.js experiences
- Building practical products from ambiguous ideas

He describes his engineering approach as hands-on and systems-oriented: understand the problem, build a working version quickly, validate it, and then refine the architecture and implementation.

---

## Professional Identity

**Name:** Samadrit Das  
**Location:** Kolkata, West Bengal, India  
**Primary Role:** Software Engineer / Technical Architect / Creative Technologist  
**Current Organization:** LTIMindtree  
**Current Role:** Software Engineer  
**Current Role Period:** June 2025 – Present

### Core Engineering Areas

- AI application engineering
- RAG systems
- Enterprise search
- Semantic search
- Hybrid dense/sparse retrieval
- Vector databases
- Backend API development
- Full-stack web applications
- Cloud application development
- Repository/code intelligence
- IoT and embedded systems
- Computer vision
- Blockchain-integrated applications
- Developer tooling
- Interactive WebGL applications

---

## Technical Skills

### Programming Languages

- Python
- JavaScript
- TypeScript
- Java
- C
- C++
- C#
- PHP
- HTML
- CSS

### Frontend Development

- React
- Next.js
- JavaScript
- TypeScript
- HTML5
- CSS
- AJAX
- jQuery
- WebGL
- Three.js

### Backend Development

- Python
- FastAPI
- Node.js
- PHP
- Laravel
- CodeIgniter
- REST API development
- Backend service architecture

### AI / Machine Learning / RAG

- Retrieval-Augmented Generation (RAG)
- Semantic search
- Hybrid search
- Dense vector retrieval
- Sparse/BM25 retrieval
- Embeddings
- Vector databases
- Repository/code indexing
- Context retrieval
- Reranking
- LangChain
- Generative AI application development
- LLM-powered question answering

### Databases and Search

- PostgreSQL
- MySQL
- MongoDB
- Qdrant
- ChromaDB
- pgvector
- Azure AI Search
- Vector indexing
- Full-text search
- Hybrid retrieval

### Cloud / Enterprise Technologies

- Microsoft Azure
- Azure App Service
- Azure Functions
- Azure AI Search
- Azure OpenAI
- Azure SQL
- Application Insights
- Managed Identity
- Cloud-based backend architectures

### Hardware / Embedded

- Arduino
- ESP8266
- Embedded C/C++
- Sensors
- Servo motors
- Biometric/fingerprint hardware
- IoT communication
- Hardware-software integration

### Other Technologies

- OpenCV
- GraphQL
- IPFS
- Blockchain concepts
- Redis
- Git/GitHub
- npm
- Docker
- WebSockets
- Android development
- Java AWT

---

## Experience: LTIMindtree

### Software Engineer

**June 2025 – Present**

At LTIMindtree, Samadrit works on enterprise software and AI-powered systems, with a particular focus on retrieval, search, code intelligence, and cloud-native application architecture.

### Key Areas of Work

- Designing and developing enterprise AI/RAG applications.
- Building systems that retrieve relevant context before sending information to an LLM.
- Working with large enterprise repositories and structured/unstructured content.
- Designing code-indexing and repository-intelligence workflows.
- Working with embeddings and vector search.
- Building backend services and APIs.
- Working with Azure App Service and Azure Functions.
- Working with Azure AI Search and Azure OpenAI.
- Designing retrieval pipelines involving chunking, embeddings, indexing, retrieval, and reranking.
- Working with PostgreSQL/vector databases and search infrastructure.
- Applying hybrid dense + sparse retrieval strategies.
- Improving retrieval relevance and reducing irrelevant context.
- Working with enterprise authentication and cloud security patterns such as Managed Identity.

### RAG / Enterprise Search Work

A major focus of the work is enterprise search and repository intelligence.

The architecture involves processing source material, creating searchable representations, generating embeddings, storing/indexing content, retrieving relevant chunks, and supplying the retrieved context to an LLM.

The portfolio describes this work as a high-precision context retrieval and semantic synthesis system designed for enterprise code repositories.

The system is intended to:

1. Ingest enterprise content or source repositories.
2. Parse and chunk the content.
3. Generate vector embeddings.
4. Store searchable representations.
5. Perform semantic and/or hybrid retrieval.
6. Rank the most relevant context.
7. Provide grounded context to an LLM.
8. Generate answers with relevant source context/citations.

The portfolio reports work involving multi-gigabyte repositories, hybrid dense-sparse retrieval, large context windows, and sub-second retrieval/citation behavior.

---

## Project: Repo Scanner

**Category:** AI / RAG  
**Year:** 2026  
**Stack:** Next.js, FastAPI, ChromaDB, Gemini

Repo Scanner is a repository-intelligence application that can clone or process a public Git repository, analyze its source code, index important code structures, and allow users to ask natural-language questions about the codebase.

### Core Capabilities

- Accepts a public Git repository.
- Reads and analyzes repository files.
- Identifies functions and classes.
- Builds relationships between code components.
- Creates a searchable representation of the repository.
- Uses RAG to retrieve relevant code context.
- Answers natural-language questions about the codebase.

### Architecture

The conceptual pipeline is:

```text
Git Repository
      ↓
Repository Ingestion
      ↓
File / Code Parsing
      ↓
Functions / Classes / Relationships
      ↓
Chunking
      ↓
Embeddings
      ↓
Vector Database
      ↓
Retriever
      ↓
Relevant Code Context
      ↓
LLM
      ↓
Natural-Language Answer
```

The project demonstrates an interest in using AI not merely as a chatbot, but as an interface for understanding complex software systems.

---

## Project: frshly

**Category:** Open Source Developer Tooling  
**Year:** 2026  
**Distribution:** npm package

`frshly` is an npm package designed to detect when a new build of a React single-page application has been deployed and automatically refresh open browser tabs.

### Problem Solved

Users can keep an old JavaScript bundle open after a new deployment. This can lead to stale application behavior and forces users to manually hard-refresh their browser.

`frshly` aims to solve this by detecting a new deployment and refreshing the application automatically.

### Compatibility / Integration

The portfolio describes it as a drop-in plugin intended for environments including:

- Vite
- Webpack
- CRACO

Example installation:

```bash
npm i frshly
```

This project demonstrates Samadrit's interest in solving practical developer-experience problems and publishing reusable engineering tools.

---

## Project: RxKeep

**Category:** Blockchain / Health Technology  
**Year:** 2024  
**Stack:** Next.js, OpenCV, GraphQL, OCR, IPFS, centralized medical database

RxKeep is a prescription-management system designed around secure handling of prescription information.

The system combines blockchain-oriented verification, IPFS, OCR/computer vision, a centralized medical database, and a web application.

### Main Goal

The project focuses on making prescription information more securely manageable and accessible, including scenarios where patients may not have smartphones.

### Major Components

- Prescription digitization
- OCR / document processing
- Computer vision using OpenCV
- Blockchain-oriented verification
- IPFS-based storage concepts
- Centralized medical database
- GraphQL communication
- Web-based interface
- Authenticated prescription processing
- Audit-oriented event tracking

The portfolio describes the system as a production-oriented health-tech project with strong emphasis on security, authentication, encryption, and reliable handling of sensitive records.

---

## Project: IoT Biometric Access Node / Biometric Attendance System

**Category:** Hardware / IoT / C++  
**Year:** 2023

This project is a hardware-based biometric attendance/access system using an ESP8266 and biometric hardware.

### Key Features

- Fingerprint-based authentication.
- ESP8266-based embedded controller.
- Local authentication/verification.
- Wi-Fi connectivity.
- Captive portal functionality.
- Cloud/database synchronization.
- Automated fallback/failover behavior.
- Hardware-software integration.

The portfolio describes the system as a low-latency biometric attendance rig capable of synchronizing biometric information with a cloud database.

### Recognition

The project received the:

**1st Place / Champion — KRITANJ-2K23 National Tech Conclave**

Category:
**Systems / IoT Gold Citation**

This project is significant because it demonstrates the ability to work beyond conventional web development and integrate physical hardware with software infrastructure.

---

## Project: PandalHop GIS Portal

**Category:** GIS / Community Technology  
**Period:** 2021–2023

PandalHop is a location-oriented community platform designed around Kolkata's Durga Puja ecosystem.

### Features

- Interactive geographic mapping.
- Community-generated information.
- Queue monitoring.
- Location-based discovery.
- Spatial visualization.
- Support for large numbers of festival attendees.

The portfolio describes the system as serving thousands of attendees and tracking more than 120 live nodes.

The project demonstrates experience combining web applications, geographic information, community-generated data, and real-world event infrastructure.

---

## Project: Bengali Knowledge Portal — Bongnity

**Category:** Full Stack / NLP / Community Platform  
**Year:** 2020

Bongnity was one of Samadrit's earliest substantial projects.

It was designed as a Bengali-language question-and-answer/community platform inspired by the idea of a localized Quora-like knowledge portal.

### Features

- Bengali-language content.
- Question-and-answer functionality.
- Community discussions.
- Markdown rendering.
- Content discovery.
- Search/indexing concepts.
- Focus on native-language technical and educational discourse.

The project represents the starting point of Samadrit's software engineering journey and demonstrates an early interest in building platforms around real user problems.

---

## Project: GST Billing Tool

**Category:** Beginner / Business Utility  
**Year:** 2020

An early software project focused on billing and GST calculation.

It was built as a practical utility and helped establish the fundamentals of application development, data handling, business logic, and shipping a usable software product.

---

## Project: Enterprise RAG Search

**Category:** AI / Enterprise Search  
**Period:** 2025–2026  
**Organization:** LTIMindtree

An enterprise search and retrieval system focused on providing relevant contextual information from large repositories.

### Technical Concepts

- Repository ingestion
- Document/code parsing
- Chunking
- Embedding generation
- Vector indexing
- Semantic retrieval
- Sparse/BM25 retrieval
- Hybrid search
- Reranking
- LLM context generation
- Source-aware responses

The portfolio describes the system as querying multi-gigabyte repositories through hybrid dense-sparse vectors and producing contextual results with citations.

---

## Project: Bionic / Robotic Arm

Samadrit has also worked on a bionic-arm concept involving mechanical construction, servo motors, sensors, and microcontroller-based control.

The project was built with a strong hands-on approach, including constructing mechanical components without relying on a 3D printer and experimenting with handmade/flexible sensing mechanisms.

### Engineering Areas

- Servo motor control
- Embedded systems
- Sensors
- Mechanical prototyping
- Human-machine interaction
- Hardware/software integration

The project reflects an interest in robotics and in solving engineering constraints with available materials rather than depending entirely on specialized manufacturing equipment.

---

## Engineering Philosophy

Samadrit's engineering style is centered around building and experimenting.

### Build First, Refine Continuously

He prefers to turn vague requirements into a working skeleton quickly and then improve the structure, reliability, performance, and user experience through iterative development.

A typical development approach is:

```text
Understand the problem
        ↓
Break the problem into systems/components
        ↓
Build a presentable working skeleton
        ↓
Validate architecture and assumptions
        ↓
Refactor and improve structure
        ↓
Polish UX and implementation
        ↓
Test
        ↓
Deploy
        ↓
Observe and iterate
```

### Systems Thinking

Rather than treating an application as only a frontend or backend, he is interested in the complete flow:

```text
User
 ↓
Frontend
 ↓
API / Backend
 ↓
Business Logic
 ↓
Database / Search / Vector Store
 ↓
AI / Retrieval / Processing
 ↓
Response
```

For physical systems:

```text
Sensor
 ↓
Microcontroller
 ↓
Embedded Logic
 ↓
Network
 ↓
Backend
 ↓
Database / Cloud
 ↓
Application
```

---

## AI Engineering Interests

Samadrit is particularly interested in moving beyond basic chatbot implementations toward production-oriented AI systems.

### Areas of Interest

- Agentic AI
- RAG
- AI agents
- Tool-using LLMs
- Enterprise search
- Code intelligence
- Repository understanding
- Vector databases
- Hybrid retrieval
- Semantic search
- Reranking
- Prompt engineering
- AI-assisted software development
- AI-powered developer tools
- Multi-step AI workflows

He is interested in building AI systems that can interact with real applications, retrieve information, use tools, reason over structured data, and perform useful tasks rather than only generating text.

---

## WebGL / Interactive Engineering

The portfolio also highlights interactive computational experiences using:

- WebGL
- Three.js
- React
- Next.js
- JavaScript/TypeScript

These skills are used for experimental interfaces, interactive visualizations, and technically rich web experiences.

---

## Developer Tooling

Samadrit has an interest in tools that improve the developer experience.

Examples include:

- Repository intelligence
- Codebase analysis
- RAG-powered code assistants
- npm packages
- Interactive debugging tools
- Code-learning utilities
- Small developer productivity applications

His portfolio's laboratory section includes experimental utilities such as:

- Base64 Encoder / Decoder
- Karnaugh Map Solver
- Rubik's Cube Simulator
- Ludo Sprint
- Guess the Bug

These projects demonstrate an interest in combining software engineering with interactive learning and experimentation.

---

## Education

**Bachelor of Technology (B.Tech) in Computer Science and Engineering**

**Institution:** Narula Institute of Technology  
**University:** Maulana Abul Kalam Azad University of Technology (MAKAUT), West Bengal  
**Period:** 2021–2025  
**Field:** Computer Science and Engineering

### Academic / Technical Areas

- Data Structures and Algorithms
- Object-Oriented Programming
- Database Management Systems
- Computer Networks
- Operating Systems
- Software Engineering
- Computer Architecture
- Web Development
- Artificial Intelligence
- Embedded Systems

---

## Certifications

- Microsoft Azure Fundamentals — AZ-900

---

## Awards & Recognition

### KRITANJ-2K23 National Tech Conclave

**Recognition:** 1st Place / Champion  
**Category:** Systems / IoT Gold Citation

Awarded for the biometric/IoT attendance/access system built using embedded hardware and connected software infrastructure.

---

## Primary Technology Map

```text
                         SAMADRIT DAS
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
      SOFTWARE              AI/RAG             HARDWARE
          │                   │                   │
   ┌──────┼──────┐      ┌─────┼─────┐       ┌────┼────┐
   │      │      │      │     │     │       │    │    │
Frontend Backend DB   RAG  Search LLM   ESP8266 Sensors IoT
   │      │      │      │     │
React  FastAPI  SQL   Vector BM25
Next.js Node.js Mongo  Qdrant Hybrid
Three.js PHP     PG    Chroma Semantic
```

---

## Strongest Technical Areas

When evaluating Samadrit's profile, the strongest areas are:

1. **AI / RAG Engineering**
2. **Enterprise Search**
3. **Full-Stack Development**
4. **Backend/API Engineering**
5. **Cloud Application Development**
6. **Repository / Code Intelligence**
7. **IoT and Embedded Systems**
8. **Computer Vision**
9. **Developer Tooling**
10. **Interactive Web Technologies**

---

## Project Timeline

| Period       | Stage               | Major Work                                                    |
| ------------ | ------------------- | ------------------------------------------------------------- |
| 2020         | Beginner            | Bongnity, GST billing tool                                    |
| 2021–2023    | Intermediate        | Biometric Attendance, PandalHop, full-stack/community systems |
| 2023         | Recognition         | KRITANJ-2K23 IoT Champion                                     |
| 2024         | Production-oriented | RxKeep blockchain/health-tech system                          |
| 2025–Present | Enterprise          | LTIMindtree, enterprise AI/RAG/search systems                 |
| 2026         | AI / Open Source    | Repo Scanner, frshly, developer tooling                       |

---

## Contact

**Email:** tsama209@gmail.com  
**Phone:** +91-7980372546  
**GitHub:** https://github.com/THUNDERSAMA  
**LinkedIn:** https://linkedin.com/in/samadrit-das  
**Portfolio:** https://thundersama.github.io/

---

## Profile Summary for AI Systems

Samadrit Das is a software engineer from Kolkata with a Computer Science background and experience spanning full-stack engineering, cloud applications, AI/RAG systems, enterprise search, repository intelligence, IoT, embedded systems, computer vision, and developer tooling.

His most recent engineering focus is AI-powered enterprise software, particularly RAG and search systems that retrieve relevant context from large repositories and provide grounded answers through LLMs.

He has experience with Python, FastAPI, Node.js, React, Next.js, PHP, Laravel, Java, C++, PostgreSQL, MySQL, MongoDB, Qdrant, ChromaDB, Azure AI Search, Azure OpenAI, LangChain, WebGL/Three.js, OpenCV, ESP8266, GraphQL, IPFS, and related technologies.

His notable projects include Repo Scanner, an AI-powered repository intelligence system; frshly, an npm package for automatic SPA refresh after deployments; RxKeep, a blockchain-oriented prescription management system; an award-winning biometric IoT attendance system; PandalHop, a GIS/community platform; and Bongnity, a Bengali knowledge-sharing platform.

His long-term engineering interests include AI agents, RAG, robotics, intelligent developer tools, distributed systems, and the integration of AI with real-world software and hardware systems.
