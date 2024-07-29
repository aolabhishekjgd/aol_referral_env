import streamlit as st
import streamlit_lottie as st_lottie
import json,logging
from helper_tools import animation_other_media

class cached_items():

    @st.cache_data()
    def cached_animation():
        #lottie animation
        lottie_json = animation_other_media.lottie_load_animation()
        return lottie_json
    

st.set_page_config(page_title="Happiness Dashboard - Art of living", page_icon=':tada', layout='wide')
st_lottie.st_lottie(cached_items.cached_animation(),key='coding')