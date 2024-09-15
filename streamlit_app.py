import base64
import streamlit as st
from streamlit_option_menu import option_menu

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

main_bg = get_img_as_base64("public/main_bg.webp")
navbar_bg = get_img_as_base64("public/navbar_bg.webp")


# ------- CSS ------- #

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{main_bg}");
background-size: 135%;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{navbar_bg}");
background-size: 100%;
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}

[data-testid="stSidebarCollapsedControl"] {{
background-color: Canvas;
color: CanvasText;
color-scheme: light dark;
}}

[data-testid="stSidebarCollapseButton"] {{
background-color: Canvas;
color: CanvasText;
color-scheme: light dark;
}}

[data-testid="stHeadingWithActionElements"] > h1:first-child {{
padding: 20px;
border-radius: 15px 50px 30px;
text-align: center;
background-color: Canvas;
color: CanvasText;
color-scheme: light dark;
}}

[data-testid="stMarkdownContainer"] > p:first-child {{
border-radius: 30px 50px 15px;
padding: 0px 10px 0px 10px;
background-color: Canvas;
color: CanvasText;
color-scheme: light dark;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu("La Agr.ia", ["Menú", 'Configuración'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    
    st.write("Música")
    st.audio(data="public/playlist/solstice.mp3",loop=True)

if selected == "Menú":
    st.title("Menú")
    
    cam_toggle = st.toggle(label="Cámara",value=True)

    if cam_toggle:
        st.camera_input(label="Tira una foto", key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

elif selected == "Configuración":
    st.title("Configuración")