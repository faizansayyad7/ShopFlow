# 🛒 ShopFlow

### E-Commerce Application with a DevOps-Ready Architecture

ShopFlow is a modern e-commerce web application built with **Python and Flask**.

The project is being developed as a practical **Cloud & DevOps learning project**, with a focus on application development, automated testing, containerization, CI/CD, cloud deployment, and monitoring.

The application currently includes product management, product details, shopping cart functionality, quantity handling, SQLite database integration, and automated testing.

---

## 🚀 Project Overview

ShopFlow simulates a simple online shopping platform where users can:

- Browse products
- View product details
- Add products to the shopping cart
- Increase product quantities
- Calculate item subtotals
- Calculate the total cart value
- Proceed to checkout
- Interact with a responsive e-commerce interface

The application is being developed progressively toward a complete DevOps workflow:

```text
Developer
    ↓
Git
    ↓
GitHub
    ↓
Jenkins
    ↓
Automated Tests
    ↓
Docker
    ↓
AWS ECR
    ↓
Kubernetes / AWS EKS
    ↓
Monitoring
    ↓
Prometheus + Grafana
```

---

# ✨ Current Features

## 🛍️ E-Commerce Features

- Modern e-commerce homepage
- Product listing
- Product detail pages
- Product descriptions
- Product pricing
- Shopping cart
- Cart quantity management
- Item subtotal calculation
- Total cart calculation
- Checkout page
- Responsive UI

## 🗄️ Database

ShopFlow currently uses **SQLite** for product data.

Database responsibilities include:

- Creating the products table
- Storing product information
- Retrieving all products
- Retrieving individual products
- Seeding initial product data

---

## 🧪 Automated Testing

The project uses **Pytest** for automated application testing.

Current tests cover:

- Home page
- Products page
- Product details
- Invalid product handling
- Add-to-cart request
- Cart page
- Checkout page

Run tests using:

```bash
pytest
```

Expected result:

```text
7 passed
```

---

# 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| Web Framework | Flask |
| Frontend | HTML5, CSS3 |
| Database | SQLite |
| Testing | Pytest |
| Version Control | Git |
| Repository | GitHub |
| Containerization | Docker |
| CI/CD | Jenkins |
| Cloud | AWS |
| Container Registry | AWS ECR |
| Orchestration | Kubernetes / AWS EKS |
| Infrastructure as Code | Terraform |
| Monitoring | Prometheus |
| Visualization | Grafana |

> Docker, Jenkins, AWS, Kubernetes, Terraform, Prometheus and Grafana are part of the planned DevOps implementation roadmap and will be integrated progressively.

---

# 🏗️ Current Architecture

```text
                    ┌───────────────┐
                    │     User      │
                    └───────┬───────┘
                            │
                            ↓
                    ┌───────────────┐
                    │ Flask Web App │
                    └───────┬───────┘
                            │
                  ┌─────────┴─────────┐
                  ↓                   ↓
           ┌─────────────┐     ┌─────────────┐
           │   Routes    │     │   Sessions  │
           └──────┬──────┘     └─────────────┘
                  │
                  ↓
           ┌─────────────┐
           │   Models    │
           └──────┬──────┘
                  │
                  ↓
           ┌─────────────┐
           │   SQLite    │
           │  Database   │
           └─────────────┘

                  +
                  
             ┌─────────┐
             │ Pytest  │
             └─────────┘
```

---

# 📁 Project Structure

```text
ShopFlow/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   │
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   │
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── products.html
│       ├── product.html
│       ├── cart.html
│       └── checkout.html
│
├── tests/
│   └── test_app.py
│
├── .gitignore
├── requirements.txt
├── run.py
└── README.md
```

---

# ⚙️ Local Setup

## 1. Clone the repository

```bash
git clone https://github.com/faizansayyad7/ShopFlow.git
```

Move into the project:

```bash
cd ShopFlow
```

---

## 2. Create a virtual environment

### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the application

```bash
python run.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

# 🧪 Run Tests

From the project root:

```bash
pytest
```

Example:

```text
============================= test session starts =============================
collected 7 items

tests/test_app.py .......                                             [100%]

============================== 7 passed ==============================
```

---

# 🔄 Development Workflow

The project follows a simple Git workflow:

```text
Make Changes
     ↓
Test Application
     ↓
Run Pytest
     ↓
git status
     ↓
git add .
     ↓
git commit
     ↓
git push
     ↓
GitHub
```

Example:

```bash
git status

git add .

git commit -m "Improve shopping cart"

git push
```

---

# 🗺️ DevOps Roadmap

ShopFlow is being developed progressively toward a production-style DevOps workflow.

### Phase 1 — Application

- [x] Flask application
- [x] E-commerce UI
- [x] Product pages
- [x] Shopping cart
- [x] Quantity management
- [x] SQLite database
- [x] Checkout page

### Phase 2 — Version Control

- [x] Git
- [x] GitHub repository
- [x] Git workflow
- [ ] Feature branches
- [ ] Pull request workflow

### Phase 3 — CI

- [x] Pytest
- [ ] Jenkins installation
- [ ] Jenkins pipeline
- [ ] Automated test execution
- [ ] GitHub webhook

### Phase 4 — Containerization

- [ ] Dockerfile
- [ ] Docker image
- [ ] Docker Compose
- [ ] Container testing

### Phase 5 — AWS

- [ ] AWS ECR
- [ ] IAM configuration
- [ ] VPC
- [ ] Cloud deployment

### Phase 6 — Kubernetes

- [ ] Kubernetes manifests
- [ ] Deployment
- [ ] Service
- [ ] ConfigMap
- [ ] Secrets
- [ ] AWS EKS deployment

### Phase 7 — Infrastructure as Code

- [ ] Terraform
- [ ] AWS infrastructure automation
- [ ] Reusable infrastructure configuration

### Phase 8 — Monitoring

- [ ] Prometheus
- [ ] Grafana
- [ ] Application metrics
- [ ] Infrastructure monitoring
- [ ] Alerts

---

# 🔐 Future Security / DevSecOps

Security will be added progressively as the project evolves.

Planned improvements include:

- Secure environment variables
- Secrets management
- IAM least-privilege configuration
- Container image scanning
- Dependency vulnerability scanning
- Secure Docker configuration
- Kubernetes security practices
- CI/CD security checks

The long-term goal is to evolve the project toward a **Cloud + DevOps + DevSecOps** workflow.

---

# 🎯 Learning Objectives

This project is being developed to gain practical experience with:

- Python Flask application development
- Git and GitHub
- Automated testing
- CI/CD pipelines
- Docker
- AWS
- Container registries
- Kubernetes
- Terraform
- Monitoring
- DevSecOps practices

---

# 📸 Screenshots

Screenshots of the application will be added here as the project progresses.

### Homepage

> Add homepage screenshot here.

### Products

> Add products page screenshot here.

### Shopping Cart

> Add cart screenshot here.

### Checkout

> Add checkout screenshot here.

---

# 👨‍💻 Author

**Faizan Sayyad**

Cloud & DevOps Engineering Learner  
Interested in Cloud Infrastructure, DevOps Automation and DevSecOps.

---

## ⭐ Project Status

**Current Status:** Active Development 🚧

ShopFlow is being developed step-by-step as a practical Cloud & DevOps portfolio project.

The project will progressively evolve from a Flask application into a containerized, CI/CD-enabled, cloud-deployed and monitored application.

---

## 📄 License

This project is created for educational and portfolio purposes.
