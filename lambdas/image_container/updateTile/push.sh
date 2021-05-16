aws ecr get-login-password --region eu-west-2 | sudo docker login --username AWS --password-stdin 880381944355.dkr.ecr.eu-west-2.amazonaws.com
sudo docker build -t update_tile .
sudo docker tag update_tile:latest 880381944355.dkr.ecr.eu-west-2.amazonaws.com/update_tile:latest
sudo docker push 880381944355.dkr.ecr.eu-west-2.amazonaws.com/update_tile:latest
# aws lambda update-function-code --region eu-west-2 --function-name update_tile --image-uri "880381944355.dkr.ecr.eu-west-2.amazonaws.com/update_tile:latest"
