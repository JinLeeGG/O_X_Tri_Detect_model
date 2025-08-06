# Circle, X, Triangle detection model and showcase with Gradio

## How to start
- clone repository
- create venv 
> pip install -r requirements.txt

### In cmd and virtual enviornment
> python shape.classifier
    - This enables to train AI
> uvicorn shape_server:app --reload
    - starting backend 
> python shape.client
    - shows web url (ctrl + click)