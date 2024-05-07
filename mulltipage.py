import streamlit as st
from streamlit_option_menu import option_menu

# st.set_page_config(
#     page_title="TITLE H BHAY",
# )

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function 
            })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='Pondering',
                options=['Test', 'Account', 'Trending', 'Your Posts'],
                icons=['house-fill','person-circle','trophy-fill'],
                default_index=1,
                )
# import Test
if app== 'Test' :
    Test.app()


#1. as sidebar mwnu
# with st.sidebar:
#     selected = option_menu(
        
#     )

# if selected == "Home":
#     st.title(f" {selected}")
# if selected== "Projects":
#     st.title(f"You have selected {selected}")
# if selected == "Contact":
#     st.title(f"You have selected {selected}")

