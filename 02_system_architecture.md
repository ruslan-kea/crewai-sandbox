# System Architecture Document for Todo Application with Real-Time Collaboration

---

## 1. Technology Stack Recommendation

### Frontend:
- **Framework:** React.js (with TypeScript)
- **State Management:** Redux Toolkit / Context API
- **Communication:** WebSocket (via native WebSocket API or libraries like Socket.IO)
- **UI Components:** Material-UI or Chakra UI for rapid development
- **Build Tool:** Vite or Webpack
- **Deployment:** Static hosting on AWS S3 + CloudFront or Vercel

### Backend:
- **Framework:** Node.js with TypeScript using NestJS (for scalable, modular architecture)
- **Real-time Communication:** Socket.IO (WS-based WebSocket abstraction)
- **Authentication:** OAuth2 / JWT with Passport.js
- **API Layer:** RESTful APIs for CRUD operations
- **Event Handling & State Synchronization:** Using WebSocket channels
- **Message Broker:** Redis Pub/Sub for event broadcasting among multiple server instances

### Database:
- **Primary Data Store:** PostgreSQL (relational, supports complex queries, ACID compliance)
- **Real-Time Data / Presence Tracking:** Redis (for pub/sub, presence, session info)
- **Optional NoSQL (for flexibility and scale):** Firebase Firestore or MongoDB (if needed for future features)
- **File Storage (e.g., attachments or avatars):** AWS S3

### Hosting & Infrastructure:
- **Cloud Provider:** AWS (or Azure/GCP as alternatives)
- **Containerization:** Docker containers orchestrated via Kubernetes (EKS or GKE)
- **Load Balancing/Scaling:** AWS ALB/ELB or NGINX ingress
- **CI/CD:** GitHub Actions / GitLab CI/CD pipelines
- **Monitoring:** Prometheus + Grafana, AWS CloudWatch
- **Logging:** ELK Stack (Elasticsearch, Logstash, Kibana) or Grafana Loki

---

## 2. System Architecture Diagram & Component Breakdown

```
+--------------------------------------------------------------+
|                       Frontend (React)                       |
|      - REST API + WebSocket Client                             |
+--------------------------------------------------------------+
                |                        |
                | HTTP/WS                | WebSocket (Socket.IO)
                |                        |
+--------------------------------------------------------------+
|                        API Gateway / Load Balancer            |
+--------------------------------------------------------------+
                |                        |
+------------------------------+      +------------------------------+
|       Backend Services         |      |   Backend Services (Scaling)  |
| - Auth Service                |      | (NestJS)                      |
| - Task Management Service     |      | - CRUD APIs                   |
| - Collaboration & Presence    |      | - WebSocket Handlers          |
|   Service                     |      | - Event Management            |
+------------------------------+      +------------------------------+
                |                        |
+--------------------------------------------------------------+
|                       Data Layer                              |
| - PostgreSQL for core data (tasks, users, permissions)      |
| - Redis for pub/sub, presence, and sessions                   |
+--------------------------------------------------------------+
                |
+--------------------------------------------------------------+
|                      Cloud Storage (S3)                        |
+--------------------------------------------------------------+
```

### Components:
- **Frontend:** Connected via HTTPS and WebSockets to backend.
- **API Gateway:** Handles REST API requests, load balancing.
- **Auth Service:** Manages user registration, login, OAuth2, JWT tokens.
- **Task Service:** Handles task CRUD, status updates, sharing, permissions.
- **Collaboration Service:** Manages WebSocket connections, real-time updates, presence.
- **Database Layer:** Postgres for normalized data; Redis for pub/sub and presence.
- **Storage Service:** AWS S3 for assets if necessary.
- **Monitoring:** Prometheus, Grafana for health and metrics.

---

## 3. Database Schema Design

### Users Table:
| Column          | Type             | Constraints             |
|-----------------|------------------|-------------------------|
| id              | UUID             | PRIMARY KEY             |
| email           | VARCHAR(255)     | UNIQUE, NOT NULL        |
| password_hash   | VARCHAR(255)     | NOT NULL                |
| display_name    | VARCHAR(100)     | NOT NULL                |
| created_at      | TIMESTAMP        | DEFAULT now()           |
| updated_at      | TIMESTAMP        | DEFAULT now()           |

### Todo Lists Table:
| Column          | Type             | Constraints                   |
|-----------------|------------------|------------------------------|
| id              | UUID             | PRIMARY KEY                   |
| owner_id        | UUID             | REFERENCES Users(id)          |
| title           | VARCHAR(255)     | NOT NULL                      |
| description     | TEXT             |                              |
| is_shared       | BOOLEAN          | DEFAULT FALSE                 |
| created_at      | TIMESTAMP        | DEFAULT now()                 |
| updated_at      | TIMESTAMP        | DEFAULT now()                 |

### Tasks Table:
| Column          | Type             | Constraints                   |
|-----------------|------------------|------------------------------|
| id              | UUID             | PRIMARY KEY                   |
| list_id         | UUID             | REFERENCES TodoLists(id)      |
| title           | VARCHAR(255)     | NOT NULL                      |
| description     | TEXT             |                              |
| status          | VARCHAR(20)      | 'todo', 'in-progress', 'done'|
| priority        | VARCHAR(20)      |                              |
| due_date        | DATE             |                              |
| assigned_to     | UUID             | REFERENCES Users(id) (nullable) |
| created_at      | TIMESTAMP        | DEFAULT now()                 |
| updated_at      | TIMESTAMP        | DEFAULT now()                 |

### Permissions & Sharing:
- A `collaborators` table for sharing:
| Column          | Type             | Constraints                   |
|-----------------|------------------|------------------------------|
| id              | UUID             | PRIMARY KEY                   |
| list_id         | UUID             | REFERENCES TodoLists(id)      |
| user_id         | UUID             | REFERENCES Users(id)          |
| permission_type | VARCHAR(20)      | 'view', 'edit'               |
| invited_by      | UUID             | REFERENCES Users(id)          |
| status          | VARCHAR(20)      | 'pending', 'accepted'       |
| created_at      | TIMESTAMP        | DEFAULT now()                 |

### Indexes:
- On user email
- On list_id and user_id for fast access
- On task list_id for tasks filtering

---

## 4. API Design and Endpoints Specification

### Authentication:
- `POST /api/auth/signup` – Register user
- `POST /api/auth/login` – Login, return JWT
- `POST /api/auth/logout` – Logout

### User & List Management:
- `GET /api/users/me` – Get current user profile
- `POST /api/lists` – Create new list
- `GET /api/lists/{listId}` – Get list details
- `PUT /api/lists/{listId}` – Update list
- `DELETE /api/lists/{listId}` – Delete list
- `POST /api/lists/{listId}/share` – Invite collaborators

### Tasks:
- `GET /api/lists/{listId}/tasks` – List tasks
- `POST /api/lists/{listId}/tasks` – Create task
- `GET /api/tasks/{taskId}` – Get task
- `PUT /api/tasks/{taskId}` – Update task
- `DELETE /api/tasks/{taskId}` – Delete task

### Real-Time WebSocket Events:
- `connect` – User connects
- `disconnect` – User disconnects
- `task_update` – Broadcast task changes
- `presence_update` – Notify presence
- `list_shared` – Multi-user list sync

---

## 5. Security Considerations and Implementation Strategy

- **Authentication & Authorization:**
  - Employ JWT tokens with expiration, refresh tokens.
  - Role-based access control (owner, collaborator view/edit).
  - OAuth2 support for third-party login (e.g., Google, GitHub).

- **Data Security:**
  - HTTPS for all data in transit.
  - Passwords stored hashed with bcrypt/scrypt.
  - Validate and sanitize all inputs to prevent injection.
  - Least privilege principles for database permissions.

- **WebSocket Security:**
  - Authenticate WebSocket connection via JWT tokens.
  - Validate user permissions before broadcasting tasks or presence updates.

- **Hosting & Network:**
  - WAF (Web Application Firewall) enabled.
  - Regular vulnerability assessments.
  - Rate limiting and DDoS mitigation.

- **Data Privacy & Compliance:**
  - GDPR compliance for user data.
  - Allow users to delete their data.

---

## 6. Deployment & Scaling Strategy

- **Containerized Deployment:** Docker images deployed via Kubernetes for scalability and resilience.
- **Horizontal Scaling:** Deploy multiple instances of backend services behind an AWS ALB/ELB.
- **Database Scaling:**
  - Read replicas for PostgreSQL.
  - Redis clustered mode for pub/sub and session caching.
- **WebSocket Scaling:**
  - Sticky sessions disabled; use Redis Pub/Sub or a message broker to route events across instances.
- **Caching & CDN:**
  - Use CloudFront or similar CDN to cache static assets.
- **CI/CD Pipeline:**
  - Automated testing, building, and deployment through GitHub Actions or GitLab CI.
- **Monitoring & Alerts:**
  - Prometheus + Grafana for system metrics.
  - Error tracking with Sentry or similar.
- **Backup & Recovery:**
  - Regular automated backups of PostgreSQL and Redis.
  - Plan for disaster recovery and data restoration.

---

## Summary

This system architecture combines a responsive React frontend with a scalable, secure backend built on NestJS, communicating via REST APIs and WebSocket for real-time collaboration. The architecture emphasizes modularity, scalability, and security by leveraging container orchestration, pub/sub messaging through Redis, and cloud-native managed services. The database schema is designed for normalization and efficient querying, with an emphasis on user permissions and collaborative features.

This comprehensive design ensures the Todo Application not only supports current MVP requirements but is also extendable for future features, with a focus on high availability, low latency, and maintainability.