# SRE Coding Challenge – k3s, Kubernetes & CI/CD

## Overview
This project demonstrates a complete, end-to-end **Site Reliability Engineering (SRE)** workflow.  
The objective was to install a **single-node k3s Kubernetes cluster**, deploy a **Hello World Nginx application**, and automate deployments using a **Git-based CI/CD pipeline**.

The solution focuses on:
- Automation
- Kubernetes fundamentals
- Secure CI/CD practices
- Real-world troubleshooting and reliability considerations

---

## Architecture Summary

- **Infrastructure:** AWS EC2 (Ubuntu)
- **Kubernetes Distribution:** k3s (single-node)
- **Application:** Nginx serving a static “Hello World” page
- **CI/CD:** GitHub Actions
- **Runner:** Self-hosted GitHub Actions runner on the same EC2 instance
- **Exposure:** Kubernetes NodePort service

---

## Repository Structure

sre-k3s-nginx/
├── k8s/
│ ├── configmap.yaml
│ ├── deployment.yaml
│ └── service.yaml
└── .github/
└── workflows/
└── deploy.yml

markdown
Copy code

- `k8s/` contains Kubernetes manifests for the application
- `.github/workflows/` contains the GitHub Actions CI/CD pipeline definition

---

## Step 1: k3s Installation (Python Automation)

- k3s was installed using a **Python automation script**
- The script:
  - Installs required dependencies
  - Installs the latest stable version of k3s
  - Verifies cluster health programmatically

### Cluster Verification
```bash
kubectl get nodes
kubectl get pods -A
Result:

Single-node cluster in Ready state

Core Kubernetes components running successfully

Non-root kubectl access was configured by copying kubeconfig to ~/.kube/config and setting the KUBECONFIG environment variable.

Step 2: Kubernetes Application Deployment
A simple Hello World Nginx application was deployed using native Kubernetes resources.

Kubernetes Resources Used
ConfigMap – Stores static HTML content

Deployment – Runs the Nginx container

Service (NodePort) – Exposes the application externally

Deployment Command
bash
Copy code
kubectl apply -f k8s/
Validation
bash
Copy code
kubectl get pods
kubectl get svc
The application was successfully accessed via:

cpp
http://<EC2-PUBLIC-IP>:30007

Step 3: CI/CD Pipeline with GitHub Actions
A GitHub Actions CI/CD pipeline was implemented to automate deployments.

Key Features
Triggered on every push to the main branch

Secure handling of kubeconfig using GitHub Secrets

Automatic application deployment using kubectl apply

Self-Hosted Runner
Because the k3s cluster runs on a private EC2 instance, a self-hosted GitHub Actions runner was configured on the same machine.
This allows secure, direct access to the Kubernetes API without exposing it publicly.

Workflow Highlights
Checks out the repository

Configures kubectl

Loads kubeconfig securely

Applies Kubernetes manifests

Verifies deployment rollout

Reliability & Troubleshooting Notes
Initial CI/CD runs were slow due to memory constraints on a small EC2 instance.

The issue was resolved by right-sizing the instance, ensuring stable and reliable deployments.

Final Outcome :
✅ k3s installed via Python automation

✅ Hello World Nginx application deployed on Kubernetes

✅ Application accessible externally

✅ Fully automated CI/CD pipeline using GitHub Actions

✅ Secure, production-style setup using a self-hosted runner



Conclusion
This project showcases a practical SRE approach combining automation, Kubernetes, CI/CD, and operational troubleshooting to deliver a reliable deployment pipeline end to end.
