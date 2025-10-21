\# QuakeWatch - Kubernetes Deployment



This project contains Kubernetes manifests for deploying the QuakeWatch Flask application.



\## 🚀 Components



\- \*\*Deployment\*\* with 2 replicas

\- \*\*Service\*\* (NodePort) to expose the app

\- \*\*Horizontal Pod Autoscaler (HPA)\*\* based on CPU

\- \*\*ConfigMap\*\* and \*\*Secret\*\* for configuration and sensitive data

\- \*\*Liveness\*\* and \*\*Readiness\*\* probes for health checks

\- \*\*CronJob\*\* for scheduled background task



\## ⚙️ Minikube Setup



```bash

minikube start

\& minikube -p minikube docker-env | Invoke-Expression

docker build -t quakewatch:latest .

kubectl apply -f deployment.yaml

kubectl apply -f service.yaml

minikube service quakewatch-service --url

```



\## 📦 Apply All Resources



```bash

kubectl apply -f configmap.yaml

kubectl apply -f secret.yaml

kubectl apply -f deployment.yaml

kubectl apply -f service.yaml

kubectl apply -f hpa.yaml

kubectl apply -f cronjob.yaml

```



\## 🔄 Restart Deployment (after updates)



```bash

kubectl rollout restart deployment quakewatch-deployment

```



\## 🧪 Check



```bash

kubectl get pods

kubectl get svc

kubectl get hpa

kubectl get cronjob

```



