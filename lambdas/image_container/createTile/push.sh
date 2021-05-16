aws ecr get-login-password --region eu-west-2 | sudo docker login --username AWS --password-stdin 880381944355.dkr.ecr.eu-west-2.amazonaws.com
sudo docker build -t create_tile .
sudo docker tag create_tile:latest 880381944355.dkr.ecr.eu-west-2.amazonaws.com/create_tile:latest
sudo docker push 880381944355.dkr.ecr.eu-west-2.amazonaws.com/create_tile:latest
# aws lambda update-function-code --region eu-west-2 --function-name create_tile --image-uri "880381944355.dkr.ecr.eu-west-2.amazonaws.com/create_tile:latest"
