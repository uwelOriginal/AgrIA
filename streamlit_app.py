import base64
import streamlit as st
from streamlit_option_menu import option_menu
import Preprocesamiento.agria_model as model

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
background-size: 150%;
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

[data-testid="stHeadingWithActionElements"] > h2:first-child {{
padding: 20px;
border-radius: 15px 50px 30px;
text-align: center;
background-color: Canvas;
color: CanvasText;
color-scheme: light dark;
}}

[data-testid="stWidgetLabel"] > div {{
border-radius: 15px 15px 15px;
padding: 0px 10px 0px 10px;
background-color: Canvas;
color: CanvasText;
color-scheme: light dark;
}}

[data-testid="stMarkdown"] > div {{
border-radius: 15px 15px 15px;
padding: 0px 10px 0px 10px;
background-color: Canvas;
color: CanvasText;
color-scheme: light dark;
}}

</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

with st.sidebar:
    st.write("Para que tu vida no sea...")

    selected = option_menu("AgrIA", ["Menú", "Términos y Condiciones", "Política de Privacidad"], 
        icons=['house', 'list-task', 'list-task'], menu_icon="cast", default_index=1)
    
    st.write("Música")
    st.audio(data="public/playlist/solstice.mp3",loop=True)

if selected == "Menú":
    st.title(selected)
    
    cam_toggle = st.toggle(label="Cámara",value=True)

    if cam_toggle:
        picture = st.camera_input(label="-", key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
        
        if picture:
            result = model.run(picture)
            st.balloons()
            st.header(result)

elif selected == "Términos y Condiciones":
    st.title(selected)
    st.divider()
    st.write('''
            Términos y Condiciones de Uso de la Aplicación "AgrIA".
             
Fecha de última actualización: 15-9-2024

Estos Términos y Condiciones rigen el uso de la aplicación AgrIA (la “Aplicación”), impulsada por inteligencia artificial (IA) y diseñada por Attack on Python (la "Empresa") para tomar fotos y analizar la calidad del suelo. Al descargar, instalar o utilizar la Aplicación, usted acepta cumplir con estos Términos y Condiciones. Si no está de acuerdo con ellos, no debe utilizar la Aplicación.

1. Descripción del Servicio
AgrIA es una aplicación que permite a los usuarios tomar fotos de diferentes tipos de suelo para analizar su calidad utilizando técnicas avanzadas de inteligencia artificial. Los análisis proporcionan información basada en los datos visuales obtenidos a través de la fotografía, pero no constituyen un diagnóstico profesional o una recomendación definitiva sobre la viabilidad del suelo para fines agrícolas u otros usos.

2. Uso Aceptable
El uso de la Aplicación está limitado a fines personales o profesionales relacionados con la evaluación de suelos. Usted acepta no utilizar la Aplicación para:
Recopilar, almacenar o compartir datos de suelos para actividades ilegales.
Alterar, hackear o descompilar la Aplicación o intentar acceder a su código fuente.
Distribuir análisis falsos o malintencionados que puedan causar daño a terceros.

3. Propiedad Intelectual
Todos los derechos, títulos e intereses de la Aplicación, incluyendo pero no limitándose a sus algoritmos de inteligencia artificial, software, diseños, interfaces, gráficos, y cualquier contenido asociado, son propiedad exclusiva de la empresa o sus licenciantes. El uso de la Aplicación no le otorga ningún derecho sobre la propiedad intelectual, excepto por el uso limitado conforme a estos Términos y Condiciones.

4. Privacidad y Datos Personales
El uso de la Aplicación implica el procesamiento de imágenes y datos de suelos. La información recopilada se utilizará únicamente para fines de análisis de suelo. La privacidad del usuario es de suma importancia para nosotros, y nos comprometemos a manejar sus datos de acuerdo con nuestra Política de Privacidad, la cual debe leerse conjuntamente con estos Términos y Condiciones.

5. Limitaciones de Responsabilidad
La aplicación proporciona análisis basados en algoritmos de IA, pero no garantiza la exactitud, precisión o adecuación de los resultados para un propósito específico. Los análisis generados son estimaciones y no deben considerarse como asesoramiento profesional. La empresa no se hace responsable de:

Cualquier pérdida o daño causado por el uso incorrecto de los datos proporcionados.
Fallos técnicos, errores, o indisponibilidad del servicio.
             
6. Modificaciones de la Aplicación y los Términos
Nos reservamos el derecho de modificar o descontinuar la Aplicación en cualquier momento sin previo aviso. También podemos modificar estos Términos y Condiciones periódicamente. El uso continuado de la Aplicación después de tales cambios constituirá su aceptación de los nuevos términos.

7. Cancelación de la Cuenta
Usted puede dejar de usar la Aplicación en cualquier momento. Nos reservamos el derecho de suspender o cancelar su acceso a la Aplicación si viola estos Términos y Condiciones.

8. Jurisdicción y Ley Aplicable
Estos Términos y Condiciones se regirán por las leyes de los Estados Unidos Mexicanos. Cualquier disputa derivada del uso de la Aplicación será resuelta exclusivamente en los tribunales de los Estados Unidos Mexicanos.

9. Contacto
Para preguntas, inquietudes o comentarios sobre estos Términos y Condiciones, puede comunicarse con nosotros en a00835693@tec.mx.

Al utilizar la Aplicación, usted declara que ha leído, comprendido y acepta estos Términos y Condiciones.
            ''')

elif selected == "Política de Privacidad":
    st.title(selected)
    st.divider()
    st.write('''
            
             Política de Privacidad de la Aplicación "AgrIA"

Fecha de última actualización: 15-9-2024
             
En AgrIA (la "Aplicación"), impulsada por inteligencia artificial (IA), nos comprometemos a proteger y respetar su privacidad. Esta Política de Privacidad explica cómo recopilamos, utilizamos, divulgamos y protegemos la información personal cuando usted utiliza la Aplicación para tomar fotos y analizar la calidad del suelo.

Al utilizar la Aplicación, usted acepta la recopilación y el uso de su información según lo descrito en esta Política de Privacidad. Si no está de acuerdo con esta política, no utilice la Aplicación.

1. Información que Recopilamos:
             
    La aplicación recopila información personal y no personal de los usuarios con el fin de mejorar la funcionalidad de la Aplicación y proporcionar análisis de suelos más precisos.

    Información de Identificación Personal (IIP): Recopilamos ciertos datos que pueden identificarlo, como su nombre, dirección de correo electrónico, y ubicación geográfica aproximada, si usted elige proporcionarlos.

    Datos de Imágenes: Cuando toma fotos a través de la Aplicación para el análisis del suelo, las imágenes se procesan localmente en su dispositivo o, en algunos casos, se pueden enviar a nuestros servidores para un análisis más profundo. Estas imágenes pueden incluir metadatos asociados (como ubicación geográfica, hora y fecha).

    Datos de Uso: Recopilamos información sobre su interacción con la Aplicación, como la frecuencia de uso, características utilizadas, tiempo de uso y errores o fallos del sistema.

2. Cómo Utilizamos su Información
    
    La información recopilada se utiliza para los siguientes propósitos:
Proporcionar y mejorar los análisis de suelos a través de la IA.
Optimizar la experiencia del usuario y mejorar el rendimiento de la Aplicación.
Monitorear el uso de la Aplicación y resolver problemas técnicos.
Cumplir con obligaciones legales o responder a solicitudes de autoridades reguladoras.
No vendemos, alquilamos ni compartimos su información personal con terceros para fines comerciales sin su consentimiento explícito.

3. Retención de Datos
    
    Mantendremos su información personal y los datos recopilados por la Aplicación únicamente durante el tiempo necesario para cumplir con los fines establecidos en esta Política de Privacidad, a menos que la ley exija o permita un período de retención más largo.

4. Protección de sus Datos

    Implementamos medidas técnicas y organizativas adecuadas para proteger su información contra accesos no autorizados, alteraciones, divulgación o destrucción. Esto incluye el cifrado de datos cuando sea necesario, controles de acceso, y procedimientos de seguridad para garantizar la protección de su información.

5. Divulgación de Información
    
    Podemos compartir su información con terceros en los siguientes casos:
             
        Proveedores de servicios: Podemos compartir información con proveedores de servicios de terceros que nos ayuden a operar y mantener la Aplicación, siempre que estén sujetos a obligaciones de confidencialidad.

       Cumplimiento de la ley: Podemos divulgar su información si así lo requiere la ley, para cumplir con un proceso legal o para proteger nuestros derechos legales.

6. Cookies y Tecnologías Similares

    La Aplicación no utiliza cookies en sí misma. Sin embargo, si accede a contenido o servicios web asociados con la Aplicación, estos pueden utilizar cookies para recopilar datos y mejorar la experiencia del usuario.

7. Derechos del Usuario
    
    Usted tiene derecho a acceder, corregir, actualizar o eliminar la información personal que recopilemos. Puede ejercer estos derechos poniéndose en contacto con nosotros a través de [correo electrónico de soporte]. Si solicita la eliminación de sus datos, podríamos necesitar retener cierta información para cumplir con nuestras obligaciones legales o de seguridad.

8. Transferencias Internacionales de Información
    
    La información recopilada puede ser transferida a, y mantenida en, servidores ubicados fuera de su país de residencia. Tomamos todas las medidas razonables para garantizar que sus datos personales sean tratados de manera segura y de acuerdo con esta Política de Privacidad.

9. Privacidad de los Menores
    
    La Aplicación no está dirigida a menores de 13 años. No recopilamos deliberadamente información personal de menores. Si descubriéramos que hemos recopilado información de un menor, tomaremos medidas para eliminarla de nuestros registros.

10. Actualizaciones a esta Política
    
    Nos reservamos el derecho de actualizar esta Política de Privacidad en cualquier momento. Las modificaciones se publicarán en esta página con la fecha de la última actualización. El uso continuo de la Aplicación después de cualquier cambio en la Política constituye su aceptación de los términos revisados.

11. Contacto

    Si tiene preguntas o inquietudes sobre esta Política de Privacidad o sobre el tratamiento de su información, puede contactarnos en [correo electrónico de soporte].

Al utilizar la Aplicación, usted confirma que ha leído y comprendido esta Política de Privacidad y acepta la forma en que manejamos su información.
            ''')