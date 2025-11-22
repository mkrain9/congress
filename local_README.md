Use preffix: python3 -m congress.run

python3 -m congress.run votes --congress=119

## **Deploy Docker Image to AWS Lambda**

### Create a New Repository

```bash
aws ecr create-repository --repository-name congress-scraper
```

### Build and Push New image

```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 916857935299.dkr.ecr.us-east-1.amazonaws.com
docker build --platform linux/amd64 --provenance=false -t congress-scraper .
docker tag congress-scraper:latest 916857935299.dkr.ecr.us-east-1.amazonaws.com/congress-scraper:latest
docker push 916857935299.dkr.ecr.us-east-1.amazonaws.com/congress-scraper:latest

```
