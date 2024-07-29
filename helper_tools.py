import requests,json, logging, ui_config,re
import pandas as pd
from datetime import datetime


logger = logging.getLogger('aol_referral_app')

class animation_other_media():

    def lottie_load_animation():
        with open (ui_config.local_file_locations["lottie_animated_json_file"]) as f:
            lottie_animated_json = json.load(f)
        return lottie_animated_json
    
class validate_inputs(object):
    def __init__(self, input_text):
        self.input_text = input_text

    def validate_phone_number(self):
        if str(self.input_text).isdigit() and bool(re.search("^[6-9]\d{9}$",self.input_text)):
            return True
        else:
            return False

