QuakeWatch

QuakeWatch is a simple Python Flask application containerized with Docker, deployed with Helm on Kubernetes, and automated via GitHub Actions.

It is part of a DevOps learning project covering containerization, Git workflows, Helm packaging, and CI/CD pipelines.

🚀 Features

Flask API with:

/ → Welcome page

/health → Health check endpoint (for Kubernetes probes)

Dockerized with a multi-stage build

Helm chart for Kubernetes deployment

GitHub Actions CI/CD:

Linting with pylint

Matrix builds (Python 3.10, 3.11, 3.12)

Docker image publishing to GHCR

Helm chart publishing as OCI package

📦 Local Development

Run the Flask app directly:

pip install -r requirements.txt python app.py

Visit http://127.0.0.1:8000 .

🐳 Docker

Build and run locally:

docker build -t quakewatch:local . docker run -p 8000:8000 quakewatch:local

☸️ Helm Deployment

Package and install the Helm chart:

helm package helm/quakewatch --version 0.1.0 -d dist helm push dist/quakewatch-0.1.0.tgz oci://ghcr.io/<your-username>/charts helm upgrade --install quakewatch oci://ghcr.io/<your-username>/charts/quakewatch
--version 0.1.0 -n quakewatch --create-namespace

🔄 Git Workflow

main → production ready

feature/* → new features

release/* → release prep

hotfix/* → urgent fixes

Contributions via Pull Requests are welcome. See CONTRIBUTING.md for details.

🛠️ CI/CD

Every push triggers GitHub Actions:

PRs → lint & test across multiple Python versions

Tags → build & push Docker image + Helm chart

(optional) Deploy automatically to Kubernetes