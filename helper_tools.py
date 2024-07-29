import requests,json, logging, ui_config
import pandas as pd
from datetime import datetime


logger = logging.getLogger('aol_referral_app')

class animation_other_media():

    def lottie_load_animation():
        with open (ui_config.local_file_locations["lottie_animated_json_file"]) as f:
            lottie_animated_json = json.load(f)
        return lottie_animated_json