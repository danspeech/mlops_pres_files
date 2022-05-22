# mlops_pres_files

docker build . -t alvenir/my_api:0.0.1
docker run -p 5001:5001 --name "my_machine_learning_api" --rm alvenir/my_api:0.0.1
 
docker tag alvenir/my_api:0.0.1 eu.gcr.io/mlopspres/alvenir/my_api:0.0.1 && docker push eu.gcr.io/mlopspres/alvenir/my_api:0.0.1

gcloud run deploy my-api-model-service --memory 2G --region europe-west4 --image --allow-unauthenticated eu.gcr.io/mlopspres/alvenir/my_api:0.0.1
