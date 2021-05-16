aws ecr get-login-password --region eu-west-2 | sudo docker login --username AWS --password-stdin 880381944355.dkr.ecr.eu-west-2.amazonaws.com
sudo docker build -t get_tiles .
sudo docker tag get_tiles:latest 880381944355.dkr.ecr.eu-west-2.amazonaws.com/get_tiles:latest
sudo docker push 880381944355.dkr.ecr.eu-west-2.amazonaws.com/get_tiles:latest
aws lambda update-function-code --region eu-west-2 --function-name get_tiles --image-uri "880381944355.dkr.ecr.eu-west-2.amazonaws.com/get_tiles:latest"
