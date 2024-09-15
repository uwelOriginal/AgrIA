# AgrIA

Hecho con Streamlit. Dominio en la liga de abajo:

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://agr-ia.streamlit.app/)

### ¿Cómo correrlo en tu propia máquina?

1. Instalar los requerimientos

   ```
   $ pip install -r requirements.txt
   ```

2. Correr la app

   ```
   $ streamlit run streamlit_app.py
   ```

# Descripción:
AgrIA es una plataforma innovadora que estima la fertilidad de la tierra a través de una imagen. Además, cuenta con un chatbot que brinda asistencia y recomendaciones personalizadas a los usuarios sobre qué cultivos son más adecuados para el tipo de tierra que poseen. Esta solución está diseñada para apoyar tanto a principiantes en jardinería como a expertos en botánica, brindando una herramienta simple y accesible.

## Objetivo:
Facilitar el análisis de la fertilidad del suelo utilizando imágenes y proporcionar recomendaciones sobre cultivos, promoviendo el acceso a información útil para todos los usuarios interesados en la agricultura y botánica.

## Problemática
Determinar la fertilidad de los suelos ha sido un reto significativo para agricultores e investigadores durante años. Según estudios realizados por asociaciones como la FAO (Organización de las Naciones Unidas para la Alimentación y la Agricultura) y la Asociación Internacional de Ciencia del Suelo, la calidad de los suelos está en declive debido a la sobreexplotación y el cambio climático. Esto afecta tanto a pequeños jardineros como a grandes agricultores que dependen de la fertilidad del suelo para obtener buenos rendimientos en sus cultivos.

Un desafío fundamental es la evaluación precisa de la fertilidad sin necesidad de métodos invasivos o costosos. Los análisis tradicionales requieren de muestreos físicos y equipos avanzados que no están al alcance de todos. Esto genera una barrera para quienes desean comenzar a cultivar pero carecen de las herramientas o conocimientos para evaluar adecuadamente la calidad de su suelo.

Los métodos actuales para evaluar la fertilidad en grandes áreas de cultivo son lentos y costosos. Además, no todos los agricultores tienen acceso a tecnologías avanzadas para realizar estos análisis. La falta de acceso a información precisa sobre la fertilidad del suelo puede llevar a decisiones de cultivo erróneas, impactando la producción y generando pérdidas económicas.

## Solución Propuesta
AgrIA ofrece una solución accesible e innovadora para este problema. Utilizando una red neuronal convolucional (CNN) entrenada con imágenes de muestras de tierra, la plataforma clasifica los suelos en cinco tipos: Suelo Negro (Black Soil), Suelo de Ceniza (Cinder Soil), Suelo Laterítico (Laterite Soil), Suelo de Turba (Peat Soil), y Suelo Amarillo (Yellow Soil). A partir de estas clasificaciones, AgrIA evalúa la fertilidad de la tierra y proporciona recomendaciones personalizadas a los usuarios sobre los cultivos más adecuados para su tipo de suelo.

Además, el chatbot integrado apoya a los usuarios brindando información sobre prácticas agrícolas y consejos para optimizar sus cultivos, adaptados a las características específicas de su tierra. Esta tecnología no solo facilita el análisis del suelo a nivel doméstico, sino que también tiene el potencial de expandirse para su uso en grandes áreas agrícolas.

## Implementación tecnológica / Herramientas
CNN (Red Neuronal Convolucional): Se utilizó una CNN para entrenar el modelo de clasificación del suelo en base a las imágenes. Esta arquitectura es clave para identificar patrones en las texturas del suelo y determinar su fertilidad.

Computer Vision (Visión por Computadora): La plataforma emplea técnicas de visión por computadora para analizar las imágenes del suelo, lo que permite que AgrIA extraiga características relevantes y haga predicciones precisas sobre la fertilidad del terreno.

OpenVino: Esta tecnología permite optimizar y acelerar el proceso de inferencia de la red neuronal en dispositivos de bajo consumo, haciendo que el análisis sea rápido y eficiente, incluso en dispositivos móviles.
Redes Degenerativas: Estas redes se utilizan para simular el deterioro del suelo y prever cómo la calidad del mismo podría cambiar con el tiempo, permitiendo a los agricultores tomar decisiones más informadas y preventivas.

## Misión
AgrIA nace como una startup con el objetivo de expandir el análisis de la fertilidad del suelo a nivel agrícola, utilizando imágenes satelitales y análisis espectroscópico en futuras versiones. Aunque el proyecto actual se enfoca en una plataforma accesible para pequeños agricultores y jardineros, este es solo el inicio de una visión más grande para optimizar la productividad de grandes campos de cultivo. Esperamos seguir evolucionando la propuesta para crear una herramienta capaz de analizar hectáreas de tierra con precisión y velocidad, ayudando a mejorar la eficiencia y sostenibilidad en la agricultura global.

## Lo que aprendimos
A lo largo del desarrollo de AgrIA, aprendimos a utilizar tecnologías punteras como OpenVino y técnicas avanzadas de Computer Vision para mejorar el rendimiento del análisis de imágenes. También adquirimos experiencia en el desarrollo de redes neuronales convolucionales y aprendimos a integrar nuestras herramientas en una solución práctica para los usuarios finales.

Uno de los mayores retos fue la generación de la idea inicial y lograr conectar todas las herramientas tecnológicas de manera que funcionaran en conjunto, lo que requirió coordinación y creatividad. Aprendimos también sobre la importancia de la accesibilidad tecnológica y sobre cómo las soluciones más simples pueden generar un impacto positivo en las comunidades.

## Posibles contratiempos / Próximos pasos
### Posibles contratiempos:
Algunas empresas o agricultores podrían resistirse a adoptar nuevas tecnologías como AgrIA, prefiriendo métodos tradicionales de análisis del suelo. Además, la precisión del modelo podría verse afectada si la variedad de suelos no es suficientemente representativa.

### Próximos pasos:
Queremos incorporar técnicas de aprendizaje automático para mejorar la precisión de nuestro modelo, lo que permitirá identificar con mayor exactitud si un suelo es fértil o no. También planeamos expandir la plataforma para proporcionar análisis más detallados y visualizaciones claras que ayuden a los agricultores a comprender mejor sus tierras. Nuestro objetivo es seguir desarrollando esta propuesta hasta convertirla en una herramienta indispensable para la agricultura moderna, fomentando un entorno más saludable y productivo.
