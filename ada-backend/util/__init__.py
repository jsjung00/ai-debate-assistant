import os
from dotenv import load_dotenv
import debugpy

load_dotenv()



class GlobalConfig:
    
    def __init__(self):
        # set up environment
        self.debug_mode="True"
    
    def debugger(self):
        if self.debug_mode=="True":
            debugpy.listen(("0.0.0.0", 5678))


global_config = GlobalConfig()
__all__ = ["global_config"]