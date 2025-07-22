# Automated Code Documentation Assistant - Mermaid Diagrams

## System Architecture Diagram

```mermaid
graph TB
    subgraph "External Systems"
        GIT[Git Repository]
        GITHUB[GitHub API]
        WEBHOOK[Webhook Events]
    end
    
    subgraph "API Gateway"
        FASTAPI[FastAPI Server]
        AUTH[Authentication]
        RATE[Rate Limiting]
    end
    
    subgraph "Agent Orchestration Layer"
        LANGGRAPH[LangGraph Workflow]
        COORDINATOR[Agent Coordinator]
        ROUTER[Workflow Router]
    end
    
    subgraph "AI Agents"
        MONITOR[Repository Monitor Agent]
        ANALYZER[Code Analysis Agent]
        DOCGEN[Documentation Generator Agent]
        NOTIFY[Notification Agent]
    end
    
    subgraph "Core Services"
        LLM[OpenAI GPT-4]
        AST[AST Parser]
        GITHANDLER[Git Handler]
        VECTORDB[Vector Database]
    end
    
    subgraph "Data Layer"
        MONGODB[MongoDB]
        FAISS[FAISS Vector Store]
        REDIS[Redis Cache]
    end
    
    subgraph "Infrastructure"
        DOCKER[Docker Containers]
        LANGSMITH[LangSmith Observability]
        LOGGER[Logging System]
    end
    
    subgraph "User Interface"
        STREAMLIT[Streamlit Dashboard]
        API_DOCS[API Documentation]
        ALERTS[Alert System]
    end
    
    %% Connections
    GIT --> WEBHOOK
    GITHUB --> FASTAPI
    WEBHOOK --> FASTAPI
    
    FASTAPI --> AUTH
    AUTH --> LANGGRAPH
    FASTAPI --> RATE
    
    LANGGRAPH --> COORDINATOR
    COORDINATOR --> ROUTER
    ROUTER --> MONITOR
    ROUTER --> ANALYZER
    ROUTER --> DOCGEN
    ROUTER --> NOTIFY
    
    MONITOR --> GITHANDLER
    ANALYZER --> AST
    ANALYZER --> LLM
    DOCGEN --> LLM
    DOCGEN --> VECTORDB
    
    GITHANDLER --> GIT
    LLM --> FAISS
    VECTORDB --> FAISS
    
    MONITOR --> MONGODB
    ANALYZER --> MONGODB
    DOCGEN --> MONGODB
    NOTIFY --> MONGODB
    
    LANGSMITH --> LANGGRAPH
    LOGGER --> DOCKER
    
    STREAMLIT --> FASTAPI
    API_DOCS --> FASTAPI
    ALERTS --> NOTIFY

    style GIT fill:#f9f,stroke:#333,stroke-width:2px
    style FASTAPI fill:#bbf,stroke:#333,stroke-width:2px
    style LANGGRAPH fill:#bfb,stroke:#333,stroke-width:2px
    style LLM fill:#fbf,stroke:#333,stroke-width:2px
    style MONGODB fill:#ffb,stroke:#333,stroke-width:2px
```

## Agent Workflow Diagram

```mermaid
sequenceDiagram
    participant U as User/Webhook
    participant API as FastAPI Gateway
    participant LG as LangGraph Orchestrator
    participant RM as Repository Monitor Agent
    participant CA as Code Analysis Agent
    participant DG as Documentation Generator Agent
    participant NA as Notification Agent
    participant DB as MongoDB
    participant VS as Vector Store
    participant LLM as OpenAI GPT-4

    U->>API: Repository Change Event
    API->>LG: Process Documentation Request
    
    LG->>RM: Monitor Repository Changes
    RM->>DB: Fetch Repository State
    RM->>RM: Detect Code Changes
    RM->>LG: Return Changed Files
    
    LG->>CA: Analyze Code Changes
    CA->>CA: Parse AST
    CA->>CA: Extract Function Signatures
    CA->>CA: Identify Documentation Gaps
    CA->>LLM: Generate Code Summaries
    LLM->>CA: Return Summaries
    CA->>VS: Store Code Embeddings
    CA->>LG: Return Analysis Results
    
    LG->>DG: Generate Documentation
    DG->>VS: Retrieve Similar Documentation
    DG->>LLM: Generate Documentation Content
    LLM->>DG: Return Generated Docs
    DG->>DB: Store Documentation
    DG->>LG: Return Documentation Results
    
    LG->>NA: Send Notifications
    NA->>DB: Log Notification
    NA->>U: Send Alert/Email
    
    LG->>API: Return Processing Results
    API->>U: Response with Status
```

## Data Flow Diagram

```mermaid
flowchart TD
    A[Git Repository] --> B[Webhook Trigger]
    B --> C[FastAPI Endpoint]
    C --> D{Authentication?}
    D -->|Valid| E[LangGraph Workflow]
    D -->|Invalid| F[Error Response]
    
    E --> G[Repository Monitor Agent]
    G --> H[Git Handler]
    H --> I[Fetch Repository Changes]
    I --> J[Parse Commit Messages]
    J --> K[Identify Changed Files]
    
    K --> L[Code Analysis Agent]
    L --> M[AST Parser]
    M --> N[Extract Functions/Classes]
    N --> O[Generate Code Embeddings]
    O --> P[Store in Vector Database]
    
    P --> Q[Documentation Generator Agent]
    Q --> R[Retrieve Similar Docs]
    R --> S[LLM Processing]
    S --> T[Generate Documentation]
    T --> U[Update Documentation Store]
    
    U --> V[Notification Agent]
    V --> W[Generate Alerts]
    W --> X[Send Notifications]
    
    X --> Y[Update MongoDB]
    Y --> Z[Return Results]
    
    subgraph "Monitoring & Observability"
        AA[LangSmith Tracing]
        BB[Logging System]
        CC[Performance Metrics]
    end
    
    E --> AA
    G --> BB
    L --> BB
    Q --> BB
    V --> CC
```

## Agent State Machine Diagram

```mermaid
stateDiagram-v2
    [*] --> Idle
    
    Idle --> Monitoring: Repository Event
    Monitoring --> Analyzing: Changes Detected
    Analyzing --> Generating: Analysis Complete
    Generating --> Notifying: Documentation Ready
    Notifying --> Storing: Notifications Sent
    Storing --> Idle: Process Complete
    
    Monitoring --> Idle: No Changes
    Analyzing --> Failed: Analysis Error
    Generating --> Failed: Generation Error
    Notifying --> Failed: Notification Error
    
    Failed --> Retry: Retry Logic
    Retry --> Monitoring: Retry Attempt
    Retry --> [*]: Max Retries Exceeded
    
    state Monitoring {
        [*] --> CheckingRepo
        CheckingRepo --> ParsingCommits
        ParsingCommits --> IdentifyingChanges
        IdentifyingChanges --> [*]
    }
    
    state Analyzing {
        [*] --> ParsingAST
        ParsingAST --> ExtractingStructure
        ExtractingStructure --> GeneratingEmbeddings
        GeneratingEmbeddings --> [*]
    }
    
    state Generating {
        [*] --> RetrievingContext
        RetrievingContext --> CallingLLM
        CallingLLM --> ProcessingResponse
        ProcessingResponse --> [*]
    }
```

## Technology Stack Diagram

```mermaid
graph TB
    subgraph "Frontend Layer"
        ST[Streamlit UI]
        API_UI[API Documentation]
        DASH[Dashboard]
    end
    
    subgraph "API Layer"
        FASTAPI_LAYER[FastAPI]
        AUTH_LAYER[Authentication]
        VALIDATE[Validation]
    end
    
    subgraph "Agent Framework"
        LANGCHAIN[LangChain]
        LANGGRAPH_LAYER[LangGraph]
        AGENTS_LAYER[AI Agents]
    end
    
    subgraph "AI/ML Stack"
        OPENAI[OpenAI GPT-4]
        EMBEDDINGS[Text Embeddings]
        RAG[RAG Pipeline]
    end
    
    subgraph "Data Processing"
        AST_PROCESSING[AST Processing]
        GIT_PROCESSING[Git Processing]
        NLP[NLP Processing]
    end
    
    subgraph "Storage Layer"
        MONGO[MongoDB]
        VECTOR[FAISS Vector DB]
        CACHE[Redis Cache]
    end
    
    subgraph "DevOps & Monitoring"
        DOCKER_STACK[Docker]
        LANGSMITH_STACK[LangSmith]
        LOGGING[Logging]
    end
    
    subgraph "External Integrations"
        GIT_EXT[Git Repositories]
        GITHUB_EXT[GitHub API]
        WEBHOOKS[Webhooks]
    end
    
    ST --> FASTAPI_LAYER
    API_UI --> FASTAPI_LAYER
    DASH --> FASTAPI_LAYER
    
    FASTAPI_LAYER --> AUTH_LAYER
    AUTH_LAYER --> VALIDATE
    VALIDATE --> LANGCHAIN
    
    LANGCHAIN --> LANGGRAPH_LAYER
    LANGGRAPH_LAYER --> AGENTS_LAYER
    
    AGENTS_LAYER --> OPENAI
    AGENTS_LAYER --> EMBEDDINGS
    EMBEDDINGS --> RAG
    
    AGENTS_LAYER --> AST_PROCESSING
    AGENTS_LAYER --> GIT_PROCESSING
    AGENTS_LAYER --> NLP
    
    AST_PROCESSING --> MONGO
    GIT_PROCESSING --> MONGO
    NLP --> VECTOR
    RAG --> VECTOR
    
    AGENTS_LAYER --> CACHE
    
    LANGSMITH_STACK --> LANGGRAPH_LAYER
    LOGGING --> DOCKER_STACK
    
    GIT_PROCESSING --> GIT_EXT
    FASTAPI_LAYER --> GITHUB_EXT
    FASTAPI_LAYER --> WEBHOOKS

    style OPENAI fill:#ff9999
    style LANGCHAIN fill:#99ff99
    style MONGO fill:#99ccff
    style FASTAPI_LAYER fill:#ffcc99
```

## Deployment Architecture

```mermaid
graph TB
    subgraph "Load Balancer"
        LB[Nginx/Traefik]
    end
    
    subgraph "Application Tier"
        API1[FastAPI Instance 1]
        API2[FastAPI Instance 2]
        API3[FastAPI Instance 3]
    end
    
    subgraph "Agent Processing Tier"
        AGENT1[Agent Worker 1]
        AGENT2[Agent Worker 2]
        AGENT3[Agent Worker 3]
    end
    
    subgraph "Data Tier"
        MONGO_PRIMARY[MongoDB Primary]
        MONGO_SECONDARY[MongoDB Secondary]
        REDIS_MASTER[Redis Master]
        REDIS_SLAVE[Redis Slave]
        VECTOR_DB[Vector Database]
    end
    
    subgraph "External Services"
        OPENAI_API[OpenAI API]
        GITHUB_API[GitHub API]
        LANGSMITH_API[LangSmith API]
    end
    
    subgraph "Monitoring"
        PROMETHEUS[Prometheus]
        GRAFANA[Grafana]
        LANGSMITH_DASH[LangSmith Dashboard]
    end
    
    LB --> API1
    LB --> API2
    LB --> API3
    
    API1 --> AGENT1
    API2 --> AGENT2
    API3 --> AGENT3
    
    AGENT1 --> MONGO_PRIMARY
    AGENT2 --> MONGO_PRIMARY
    AGENT3 --> MONGO_PRIMARY
    
    MONGO_PRIMARY --> MONGO_SECONDARY
    REDIS_MASTER --> REDIS_SLAVE
    
    AGENT1 --> REDIS_MASTER
    AGENT2 --> REDIS_MASTER
    AGENT3 --> REDIS_MASTER
    
    AGENT1 --> VECTOR_DB
    AGENT2 --> VECTOR_DB
    AGENT3 --> VECTOR_DB
    
    AGENT1 --> OPENAI_API
    AGENT2 --> OPENAI_API
    AGENT3 --> OPENAI_API
    
    API1 --> GITHUB_API
    API2 --> GITHUB_API
    API3 --> GITHUB_API
    
    AGENT1 --> LANGSMITH_API
    AGENT2 --> LANGSMITH_API
    AGENT3 --> LANGSMITH_API
    
    PROMETHEUS --> API1
    PROMETHEUS --> API2
    PROMETHEUS --> API3
    
    GRAFANA --> PROMETHEUS
    LANGSMITH_DASH --> LANGSMITH_API
```