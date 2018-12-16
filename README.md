# Simple Flask API Wrapper for fitPLS

The endpoint /fitPLS expects a POST request, _Content-Type_ set to _application/json_ and for the body of the request to contain the training dataset as it formatted in the example file `training_dataset.json`.

To see if the service is running you can hit the index `/` and expect the message "Greetings! Nothing to see here though."

## Run Locally

Navigate to the folder containing these files and set the environment variable to the `real_tech_api.py` script, and then run the service.
```
export FLASK_APP=real_tech_api.py
flask run
```

You can expect the service to run port 5000


## Run in AWS ElasticBeanstalk

1. Create a new ElasticBeanstalk environment
2. Select 'Web server environment'
3. Under 'Base configuration', select 'Docker' for _Platform_
4. Under 'Base configuration', choose 'Upload your code' and upload the `RealTech_Docker_for_AWS.zip` located in this repo
5. Click 'Create environment' button
6. When the environment is running you can use swagger to hit the `/fitPLS` endpoint