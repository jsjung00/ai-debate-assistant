from util import global_config
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import nltk
from api import app_router



# Set up fastapi
def setup_fastapi():
    app = FastAPI()
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

def onload():
    nltk.download('punkt')
    global_config.debugger()
    

# Set up app
app = setup_fastapi()
onload()



# Include routers
app.include_router(app_router, prefix="")