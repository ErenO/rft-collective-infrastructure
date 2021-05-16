aws ecr get-login-password --region eu-west-2 | sudo docker login --username AWS --password-stdin 880381944355.dkr.ecr.eu-west-2.amazonaws.com
sudo docker build -t delete_tile_info .
sudo docker tag delete_tile_info:latest 880381944355.dkr.ecr.eu-west-2.amazonaws.com/delete_tile_info:latest
sudo docker push 880381944355.dkr.ecr.eu-west-2.amazonaws.com/delete_tile_info:latest
aws lambda update-function-code --region eu-west-2 --function-name deleteTileInfo --image-uri "880381944355.dkr.ecr.eu-west-2.amazonaws.com/delete_tile_info:latest"
