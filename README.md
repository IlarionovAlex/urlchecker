# External URL Checker

A simple Python service that checks the status of two external URLs and exposes the results as Prometheus metrics. The service runs a basic HTTP server on port 8000, returning metrics in Prometheus format.

## Features

- Periodically checks:
  - https://httpstat.us/503
  - https://httpstat.us/200
- Exposes Prometheus metrics:
sample_external_url_up{url="https://httpstat.us/503"} = 0 sample_external_url_response_ms{url="https://httpstat.us/503"} = [value] sample_external_url_up{url="https://httpstat.us/200"} = 1 sample_external_url_response_ms{url="https://httpstat.us/200"} = [value]

## markdown

- Containerized with Docker
- Deployable via Kubernetes & Helm
- Uses GitHub Container Registry (GHCR) for image storage

## Setup & Installation

### Clone the Repository

git clone https://github.com/IlarionovAlex/external-url-checker.git cd external-url-checker

### Install Dependencies

Ensure you have Python 3.9+ installed. Then, install required packages:

pip install -r requirements.txt

### Run Locally

python app.py

The service will start on `http://localhost:8000`, and you can access metrics at:

http://localhost:8000/metrics

## Docker Usage

### Build the Docker Image

docker build -t ghcr.io/IlarionovAlex/external-url-checker:latest .

### Log in to GitHub Container Registry (GHCR)

echo "your-github-pat-token" | docker login ghcr.io -u your-github-username --password-stdin

### Push the Image to GHCR

docker push ghcr.io/IlarionovAlex/external-url-checker:latest

## Kubernetes Deployment (via Helm)

### Create a Kubernetes Secret for GHCR

Since GHCR is private by default, create a Kubernetes secret to allow image pulling:

kubectl create secret docker-registry ghcr-secret
--docker-server=ghcr.io
--docker-username=your-github-username
--docker-password=your-github-pat-token

### Deploy with Helm

Ensure Helm is installed, then install the service:

helm install external-url-checker ./helm/external-url-checker-chart

### Verify the Deployment

Check the running pods:

kubectl get pods

Get the service details:

kubectl get svc external-url-checker

### Port-Forward to Access Metrics

To access metrics locally:

kubectl port-forward svc/external-url-checker 8000:8000

Now open:

http://localhost:8000/metrics

### Cleanup & Uninstall

# To remove the Helm deployment:

helm uninstall external-url-checker

# To remove the Kubernetes secret:

kubectl delete secret ghcr-secret