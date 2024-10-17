aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 381492315384.dkr.ecr.us-east-1.amazonaws.com
docker build -t sprints-compasso .
docker tag sprints-compasso:latest 381492315384.dkr.ecr.us-east-1.amazonaws.com/sprints-compasso:latest
docker push 381492315384.dkr.ecr.us-east-1.amazonaws.com/sprints-compasso:latest