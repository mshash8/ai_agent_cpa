# ai_agent_cpa
This repo is for the hackathon to build an AI Agent CPA


## Create Virtual environment
```
python -m venv c:\path\to\myenv
```
### Activate virtual environment
```
source {env_name}/bin/activate
```

### Deactivate virtual environment
```
source deactivate
```

## To download requirements:
```
pip install -r requirements.txt
```

## To run the api:
```
uvicorn cpa:app --reload
```
Follow the outout from the terminal after that.


## API request

Method: POST
route: retrain
body: raw/json
```
# Modelus-Api
This api is made for re-training the ml model for modelus application. The retrain route will be called with the bellow mentioned parameters, to retrain the model.

## API work
1. Retrain the model with new Test images (and labels)
2. Update 'updates_at' for project's model.
3. Update/Add 'predicted_label' for each test image.

## Create Virtual environment
```
python -m venv c:\path\to\myenv
```
### Activate virtual environment
```
source {env_name}/bin/activate
```

### Deactivate virtual environment
```
source deactivate
```

## To download requirements:
```
pip install -r requirements.txt
```

## To run the api:
```
uvicorn retrain-model:app --reload
```
Follow the outout from the terminal after that.




## API request

Method: POST
route: retrain
body: raw/json
```
{
    "projectId": "your_project_id",
    "userId": "your_user_id"
}
```

