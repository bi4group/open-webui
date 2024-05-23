import json

from config import FIREFLIES_API_TOKEN
from fastapi import APIRouter, HTTPException, status

import requests

router = APIRouter()
API_URL = 'https://api.fireflies.ai/graphql'


@router.get("")
async def get_meetings():
    auth_header = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {FIREFLIES_API_TOKEN}'
    }

    # data = ('{"query": "query Transcripts($userId: String) { transcripts(user_id: $userId) { title id dateString '
    #         'duration summary { action_items overview shorthand_bullet  } participants } }"}')
    #
    # response = requests.post(API_URL, headers=auth_header, data=data)
    #
    # return response.json()

    return {
    "data": {
        "transcripts": [
            {
                "title": "Review estimate AWWG v1.0",
                "id": "3qxjW7OI2KJaPxGg",
                "dateString": "2024-05-20T07:15:00.000Z",
                "duration": 21,
                "summary": {
                    "action_items": "",
                    "overview": "**Rubén Trujillo Fernández** organiza una reunión con **Andrea Sorroche Reverón**, **Jose Requena Martínez**, **Julio Sanchez Miron**, y **Adrián Sánchez Cerrillo** para planificar la implementación de un proyecto. Se discuten tareas como la infraestructura, entrenamiento de modelos, pruebas de carga y el desarrollo de distintos modelos para recomendar eventos y ropa por separado. Se destaca la importancia de pruebas exhaustivas con usuarios simulados y la integración de WhatsApp para evitar pérdida de mensajes en caso de fallos en el sistema.\n\nSe menciona la flexibilidad de las estimaciones para ajustarse según los avances, subrayando la colaboración entre el equipo para revisar progresos y asignar tareas. Se acuerda mantener una comunicación constante para posibles mejoras o nuevos requisitos a medida que avance el proyecto. Rubén enfatiza la bienvenida a modificaciones o adiciones a las actividades propuestas para fomentar la participación activa de todo el equipo en la planificación detallada del proyecto.\n\nLa reunión concluye con disposición al trabajo conjunto y apertura a futuras actualizaciones en función de los resultados obtenidos durante la ejecución del proyecto.",
                    "shorthand_bullet": "- 🔍 **Análisis de Reunión con Producto Visual Fabric:**\n    - **Rubén Trujillo Fernández** menciona que la reunión con el producto Visual Fabric está casi terminada.\n    - Se discute la necesidad de determinar los tiempos y costos para llevar el proyecto a una versión cero.\n\n- 📋 **Planificación de Tareas para el Proyecto:**\n    - Se detallan tareas como montar infraestructura, configurar monitorización y entrenar con documentos sobre eventos.\n    - **Rubén Trujillo Fernández** hace una estimación de las horas dedicadas a diferentes aspectos del proyecto.\n\n- 🗂️ **Modelo de Agentes Expertos:**\n    - **Julio Sanchez Miron** sugiere implementar agentes expertos en recomendación de eventos y ropa.\n    - Se plantea la importancia de mejorar la gestión de peticiones en caso de caída del sistema.\n\n- 📊 **Refinamiento del Modelo y la API:**\n    - **Rubén Trujillo Fernández** propone dedicar horas al refinamiento del modelo y la API para la versión cero del proyecto.\n    - **Se discute la relevancia de incluir en la estimación el tiempo invertido en la investigación y entrenamiento del modelo.**\n\n- 📝 **Revisión y Comentarios Finales:**\n    - **Rubén Trujillo Fernández** revisa la propuesta con Maggi y Jorge, destacando la importancia de añadir tareas necesarias.\n    - **Se plantea la realización de pruebas de carga tanto en la API como en el entorno del cliente.**"
                },
                "participants": [
                    "ruben.trujillo@nucleoo.com,adrian.sanchez@nucleoo.com,andrea.sorroche@nucleoo.com,jose.requena@nucleoo.com",
                    "julio.sanchez@nucleoo.com",
                    "adrian.sanchez@nucleoo.com",
                    "andrea.sorroche@nucleoo.com",
                    "jose.requena@nucleoo.com"
                ]
            },
            {
                "title": "AWWG Catch-up",
                "id": "Wsx1e36Y3TEX4NMq",
                "dateString": "2024-05-17T09:45:00.000Z",
                "duration": 58,
                "summary": {
                    "action_items": "",
                    "overview": "",
                    "shorthand_bullet": ""
                },
                "participants": [
                    "mayi.echeveste@nucleoo.com,adrian.sanchez@nucleoo.com",
                    "julio.sanchez@nucleoo.com",
                    "mayi.echeveste@nucleoo.com"
                ]
            },
            {
                "title": "AIAIAI Chat & Agent PoC's",
                "id": "Fqm4HFbH30RcTtas",
                "dateString": "2024-05-16T11:00:00.000Z",
                "duration": 31,
                "summary": {
                    "action_items": "",
                    "overview": "La reunión comenzó con **Luis Rosado Garrido** presentando la integración de Stabilis con un modelo para responder preguntas automáticamente, destacando la eficacia en consultas actuales y el tiempo de respuesta. **Rubén Trujillo Fernández** propuso avanzar en la integración de funcionalidades dentro del chat, incluyendo el uso de una API como Tabili. Se discutieron planes futuros para implementar esta solución y cómo facilitaría a los usuarios acceder a respuestas relevantes. Se exploraron ideas de configurar agentes personalizados en chats adaptados al usuario y sus necesidades, permitiendo respuestas contextualizadas y eficiencia operativa.\n\nPosteriormente, se mencionó la posibilidad de integrar la solución en un chat del proyecto Open Web Ui y se planteó la integración de agentes personalizados en chats basados en documentos almacenados localmente o en plataformas como Google Drive y Sharepoint. También se discutió sobre cómo generar documentos basados en plantillas predefinidas y habilitar chats especializados por dominios documentales específicos. En conjunto, los avances presentados por **Jorge Gonzalez Diaz de Leon** señalaron pasos importantes hacia una aplicación más versátil y centrada en las necesidades individuales de los usuarios dentro del proyecto Open Web Ui.",
                    "shorthand_bullet": "⚙️ **Integración de Stabilis con el chat de Open Web Ui**\n**Luis Rosado Garrido** trabajó en integrar Stabilis con el modelo existente para detectar y responder automáticamente a preguntas fuera del contexto temporal.\n**Rubén Trujillo Fernández** expresó interés en probar la integración en la solución de chat en desarrollo.\nSe discutió la posibilidad de usar modelos desplegados localmente para mejorar la funcionalidad."
                },
                "participants": [
                    "ruben.trujillo@nucleoo.com,jorge.gonzalez@nucleoo.com,adrian.sanchez@nucleoo.com,luis.rosado@nucleoo.com,francisco.dominguez@nucleoo.com",
                    "ruben.trujillo@nucleoo.com",
                    "julio.sanchez@nucleoo.com",
                    "adrian.sanchez@nucleoo.com",
                    "luis.rosado@nucleoo.com",
                    "francisco.dominguez@nucleoo.com"
                ]
            },
            {
                "title": "Julio fireflies",
                "id": "HjgIRwd5KGGYvskw",
                "dateString": "2024-05-16T10:00:00.000Z",
                "duration": 10,
                "summary": {
                    "action_items": "",
                    "overview": "",
                    "shorthand_bullet": ""
                },
                "participants": [
                    "adrian.sanchez@nucleoo.com",
                    "julio.sanchez@nucleoo.com"
                ]
            },
            {
                "title": "Modelo AWWG",
                "id": "BKCQO9T5KglFQirS",
                "dateString": "2024-05-10T10:30:00.000Z",
                "duration": 74,
                "summary": {
                    "action_items": "\n**Mayi Echeveste Schredelseker**\nIdentify and document the next steps from the meeting transcript for future actions (49:28)\n",
                    "overview": "The meeting involved discussions on business operations and customer engagement, with participants like **Mayi Echeveste Schredelseker**, **Andrea Sorroche Reverón**, and **Julio Sanchez Miron** actively sharing insights. They explored strategies for utilizing platforms such as WhatsApp for customer interaction, product recommendations, and video content creation. Key points included considerations for enhancing customer relationships through personalized interactions, efficient communication channels, and strategic use of video content. Julio emphasized the importance of integrating chat functionality within customer experiences.\n\nParticipants discussed implementing solutions to improve user engagement while maintaining a competitive edge. They also touched upon aspects like color coordination in product recommendations and optimizing social media presence. The significance of continuous improvement in approaches towards customer service and leveraging technology tools effectively was highlighted. Plans for further collaboration on refining strategies to enhance business performance through innovative marketing techniques were made, tailored to meet evolving consumer preferences.",
                    "shorthand_bullet": "📊 **Recommendations for WhatsApp Integration**\n- **Mayi** suggested using saber sake for example recommend.\n- **Andrea** discussed the importance of moving forward with recommendations.\n- **Julio** mentioned implementing interactive features like a pokemon button.\n\n📹 **Video Content Strategy**\n- **Mayi** emphasized the need for video content related to customer responses and competition.\n- **Julio** talked about the importance of video recording and note-taking during discussions.\n\n📱 **Utilizing Emojis in Communication**\n- **Adrián** highlighted the use of emojis in video content for customer engagement.\n- **Mayi** and **Julio** discussed the significance of incorporating emojis in chat interactions.\n\n🛠️ **Next Steps**\n- **Mayi** and **Julio** outlined the plan for the next steps in the project.\n- **Mayi** emphasized the need for an open-ended approach to certain tasks."
                },
                "participants": [
                    "mayi.echeveste@nucleoo.com,adrian.sanchez@nucleoo.com,andrea.sorroche@nucleoo.com",
                    "julio.sanchez@nucleoo.com",
                    "adrian.sanchez@nucleoo.com",
                    "andrea.sorroche@nucleoo.com"
                ]
            },
            {
                "title": "AIAIAI Chat & Agent PoC's",
                "id": "A6Xef576WqBPDVna",
                "dateString": "2024-05-10T10:00:00.000Z",
                "duration": 41,
                "summary": {
                    "action_items": "\n**Rubén Trujillo Fernández**\nExplain the strategies in place to improve water quality (25:05)\n",
                    "overview": "**Julio Sanchez Miron**, **Rubén Trujillo Fernández**, **Luis Rosado Garrido**, and **Jorge Gonzalez Diaz de Leon** discussed solutions, customer relationships, project proportions, documentations, language models, and improvement strategies. They emphasized implementing recommendations, integrating various platforms, addressing COVID's economic impacts in transportation, and enhancing water quality with open source tools. Budget considerations in New York City and Microsoft Teams training for effective communication were also covered.\n\nThe focus switched to creating user stories and automating documentation based on historical data. Ethical considerations in implementations and effectively integrating algorithms, such as Graphia, were explored for better outcomes. Technical aspects like solution design templates and clear communication within teams, considering historical data patterns for improved decision-making processes, were significant areas of discussion.\n\nThe group delved into demonstrating solutions, customer relationships, project proportions, and documentation, among other topics. They discussed integrating recommendations, platforms, addressing COVID's economic impact in transportation, improving water quality using open source tools, and budget considerations in New York City. Emphasis was put on training related to Microsoft Teams for effective communication.\n\nExplorations continued about user stories creation, automatic documentation generation, ethical considerations, and integrating algorithms effectively for better outcomes. Technical aspects like solution design templates and the importance of clear communication within teams considering historical data patterns for decision-making processes concluded the discussion.",
                    "shorthand_bullet": "🔍 **Reviewing Solutions for Customer Ethical Issues**\n- **Julio Sanchez Miron** discusses implementing recommendations aligned with the brand.\n- **Rubén Trujillo Fernández** mentions demonstrating solutions during the day to showcase importance.\n\n📊 **Discussion on Project Implementation**\n- **Rubén Trujillo Fernández** emphasizes the importance of clear project proposals.\n- **Jorge Gonzalez Diaz de Leon** mentions the implementation concept and MVP.\n\n📚 **Document Organization and Implementation**\n- **Rubén Trujillo Fernández** talks about organizing documents and the need for clear structures.\n- **Luis Rosado Garrido** and **Rubén Trujillo Fernández** discuss document management and implementation challenges.\n\n🌍 **Strategies for Water Quality Improvement**\n- **Rubén Trujillo Fernández** inquires about strategies to enhance water quality.\n- **Rubén Trujillo Fernández** mentions the use of open-source solutions for analysis.\n\n🚇 **Economic Impact of COVID on Transportation**\n- **Rubén Trujillo Fernández** raises questions about the economic impact of COVID on transportation.\n- **Rubén Trujillo Fernández** queries about budget-friendly Mosfet options in New York City.\n\n📝 **Effective Communication and Collaboration**\n- **Jorge Gonzalez Diaz de Leon** discusses the importance of automated document creation for user stories.\n- **Rubén Trujillo Fernández** highlights the need for ethical implementation and algorithmic considerations."
                },
                "participants": [
                    "ruben.trujillo@nucleoo.com,jorge.gonzalez@nucleoo.com,adrian.sanchez@nucleoo.com,luis.rosado@nucleoo.com,francisco.dominguez@nucleoo.com",
                    "ruben.trujillo@nucleoo.com",
                    "julio.sanchez@nucleoo.com",
                    "adrian.sanchez@nucleoo.com",
                    "luis.rosado@nucleoo.com",
                    "francisco.dominguez@nucleoo.com"
                ]
            },
            {
                "title": "AIAIAI Chat & Agent PoC's",
                "id": "SEe7ciNLC2K4qhFB",
                "dateString": "2024-05-02T11:00:00.000Z",
                "duration": 35,
                "summary": {
                    "action_items": "\n**unassigned**\nFollow up on implementing the proposed solutions discussed during the meeting (15:59)\n",
                    "overview": "En la reunión participaron **Rubén Trujillo Fernández**, **Jorge Gonzalez Diaz de Leon**, **Julio Sanchez Miron**, y **Adrián Sánchez Cerrillo**. Se abordaron desafíos con la toma de notas, actualizaciones en varios asuntos, temas relacionados con video, soluciones de software, implementación de protocolos, modelos de IA, y modelos de código abierto como OpenAI. Se discutieron configuraciones de internet y herramientas para análisis. Hubo conversaciones sobre sistemas de gestión de documentos enfocados en procesamiento de texto e integración multimedia. Se destacó la importancia de mantener claridad en la comunicación, la estructura de la información y la consistencia de formatos.\n\nSe mencionaron términos técnicos como middleware y herramientas de análisis de contenido. Se abordaron aplicaciones de inteligencia artificial y técnicas de web scraping para extracción de datos. Se intercambiaron puntos de vista sobre métodos de identificación y modelos operativos, explorando enfoques para manejar estructuras de datos complejas. Se enfatizó la necesidad de estándares precisos de documentación para garantizar colaboración fluida dentro del equipo. Se compartieron ideas sobre funcionalidades de software, implementaciones de algoritmos para tareas específicas, y ejemplos prácticos relacionados con la carga de modelos desde fuentes externas.\n\nLa discusión resaltó la importancia del aprendizaje continuo para adaptarse a nuevas tecnologías y asegurar prácticas eficientes de gestión del flujo de trabajo alineadas con los objetivos del proyecto.",
                    "shorthand_bullet": "🔍 **Data Integration Strategy**\n- **Rubén Trujillo Fernández** emphasized the importance of a comprehensive data integration strategy.\n- Mentioned the need for reliable data sources and efficient integration methods.\n- **Julio Sanchez Miron** discussed the challenges faced in data integration.\n\n📊 **Multimodal Integration Approach**\n- **Adrián Sánchez Cerrillo** highlighted the significance of a multimodal integration approach.\n- Discussed the protocol implementation and architectural aspects.\n- Mentioned the need for a robust solution for seamless integration.\n\n🔄 **Middleware Implementation**\n- **Jorge Gonzalez Diaz de Leon** and **Julio Sanchez Miron** touched upon the middleware implementation process.\n- Highlighted the importance of middleware for smooth integration across different systems.\n\n🔒 **Data Security Measures**\n- **Rubén Trujillo Fernández** emphasized the need for robust data security measures.\n- Discussed the importance of safeguarding data during integration processes.\n- Mentioned considerations for secure data transmission.\n\n🚀 **AI Integration**\n- **Adrián Sánchez Cerrillo** mentioned the integration of AI models.\n- Highlighted the use of open-source AI tools for data processing.\n- Discussed the role of AI in enhancing integration capabilities.\n\n📝 **Documentation and Reporting**\n- **Rubén Trujillo Fernández** discussed the importance of thorough documentation.\n- Mentioned the need for detailed reporting on integration processes.\n- Emphasized maintaining clear records for future reference.\n\n📲 **Mobile Integration Strategy**\n- **Adrián Sánchez Cerrillo** and **Rubén Trujillo Fernández** discussed strategies for mobile integration.\n- Highlighted the significance of adapting integration processes for mobile platforms.\n- Mentioned considerations for seamless mobile data integration."
                },
                "participants": [
                    "ruben.trujillo@nucleoo.com,jorge.gonzalez@nucleoo.com,adrian.sanchez@nucleoo.com,luis.rosado@nucleoo.com,francisco.dominguez@nucleoo.com",
                    "ruben.trujillo@nucleoo.com",
                    "julio.sanchez@nucleoo.com",
                    "adrian.sanchez@nucleoo.com",
                    "luis.rosado@nucleoo.com",
                    "francisco.dominguez@nucleoo.com"
                ]
            },
            {
                "title": "Debrif & Next Steps",
                "id": "SowT6092wpe6Y2HJ",
                "dateString": "2024-04-30T09:00:00.000Z",
                "duration": 16,
                "summary": {
                    "action_items": "\n**Mayi Echeveste Schredelseker**\nFollow up on the marketing strategies discussed in the meeting and implement the proposed changes to enhance workshop quality and Alitar. Ensure the Ladonian prescription is prioritized and the Via de los Catenamos palette training is effectively implemented (03:22)\n",
                    "overview": "The meeting commenced with **Jose Requena Martínez**, **Mayi Echeveste Schredelseker**, and **Jaime Frías Funes** discussing the significance of workshops, transcription quality, and personality analysis. They explored new strategies to enhance their investigative processes, emphasizing the maintenance of high standards and thorough analyses for improved outcomes, while also considering potential challenges.\n\n**Mayi** stressed the importance of upholding high-quality transcription standards and conducting in-depth analyses. Factors such as timelines, potential hurdles in their work, and the essence of promoting key qualities were deliberated upon. Encouraging collaboration among team members to attain desired results was a focal point, underlining the necessity for feedback mechanisms like questionnaires and continuous evaluations.\n\nThe group collectively agreed on prioritizing quality and efficiency, valuing diverse perspectives and ideas. They aligned on fostering a culture of excellence, where teamwork and shared insights were instrumental in achieving their goals. This shared vision aimed at harmonizing efforts towards enhancing performance through a blend of innovation and feedback mechanisms, reinforcing the importance of collaboration and continual evolution.\n\nIn conclusion, the team's alignment on quality and efficiency underscored their commitment to excellence in tasks. By recognizing the significance of varied viewpoints and collaborative endeavors, they aimed to elevate performance standards through ongoing feedback and evaluation processes. The meeting laid the groundwork for a unified approach focused on quality outcomes while embracing diverse perspectives within their operations.",
                    "shorthand_bullet": "🔑 **Meeting Summary**\n- **Discussion on transcription analysis and workshops led by Mayi Echeveste Schredelseker\n- **Importance of transcription accuracy highlighted by Jaime Frías Funes\n- **Plans for future workshops and analysis shared by Mayi Echeveste Schredelseker\n- **Focus on quality commentaries and promotion emphasized by Jose Requena Martínez\n- **Potential timeline for upcoming activities mentioned by Mayi Echeveste Schredelseker and Jaime Frías Funes"
                },
                "participants": [
                    "mayi.echeveste@nucleoo.com,jose.requena@nucleoo.com,andrea.sorroche@nucleoo.com,jaime.frias@nucleoo.com",
                    "jose.requena@nucleoo.com",
                    "andrea.sorroche@nucleoo.com",
                    "jaime.frias@nucleoo.com",
                    "julio.sanchez@nucleoo.com"
                ]
            },
            {
                "title": "AI-First Plan | G14",
                "id": "X6hAVK1seukO4cdg",
                "dateString": "2024-04-25T13:30:00.000Z",
                "duration": 54,
                "summary": {
                    "action_items": "**Jaime Frías Funes**\nAutomatizar el proceso de imputar horas (03:53)\nMejorar la búsqueda de documentación para facilitar el acceso a la información relevante (08:18)\nProbar la herramienta Find con GPT4 para mejorar las búsquedas en la documentación (21:29)\nSolicitar una licencia ChatGPT Club para obtener funcionalidades adicionales como búsqueda en internet (22:24)\nExplorar opciones de licencia y herramientas para investigaciones y tareas específicas (49:14)\n\n**Sandra Rodríguez García**\nEvaluar soluciones más fiables que ChatGPT 3.5 para diseño e investigación inicial, considerando GPT4 u otras versiones nuevas (41:27)\nCompartir feedback sobre problemas y soluciones identificados durante las reuniones de trabajo (52:01)",
                    "overview": "**En la reunión**, se discutió sobre la optimización de tareas diarias y procesos, identificando puntos de mejora. Se alentó a **los participantes** a compartir aspectos considerados una pérdida de tiempo, proponiendo soluciones colectivas y creativas. Se mencionaron iniciativas previas, como usar **ChatGPT**, y la importancia de evaluar nuevas tecnologías para obtener resultados eficaces.\n\nSe destacó la importancia de identificar problemas en actividades diarias, como imputación horaria y el onboarding de nuevos miembros. Se sugirió usar herramientas como **ChatGPT**. Se enfatizó evaluar nuevas tecnologías. Hablaron sobre facilitar el acceso a licencias y herramientas actualizadas, para una mejor gestión de tareas complejas e investigación más efectiva.\n\nSe planea recopilar ideas, priorizar soluciones viables e implementar medidas para mejorar el rendimiento operativo del equipo. Se instó a **los participantes** a proporcionar feedback constante sobre sus experiencias laborales. Resumiendo, se buscó identificar áreas problemáticas en rutinas diarias, proponer soluciones colaborativas y fomentar un ambiente productivo mediante mejoras continuas.",
                    "shorthand_bullet": "🎯 **Proceso de Onboarding**\n- **Contextualizar a nuevas personas en la empresa**\n- **Necesidad de sacar información de la cabeza de pocas personas y centralizarla**\n- Propuesta de utilizar repositorios como Confluence para documentación\n\n🚀 **Mejora en Demostraciones de Producto**\n- **Simplificar las demostraciones para que cumplan el objetivo de mostrar la solución final de forma eficiente**\n- Reflexión sobre la cantidad de demostraciones necesarias y su duración\n- Importancia de adaptar el proceso de demostración al potencial de venta\n\n📚 **Gestión de Documentación y Herramientas de Apoyo**\n- Implementación de chatbots para consultas de documentación\n- Utilización de herramientas como ChatGPT para documentación y apoyo\n- Necesidad de best practices para el uso efectivo de herramientas\n\n📊 **Medición de Impacto**\n- Importancia de medir el impacto de herramientas y mejoras en la empresa\n- Identificación y medición de los \"pain points\" para evaluar mejoras\n- Consideración de medidas cualitativas para evaluar la eficacia de las herramientas\n\n📝 **Seguimiento de Acciones**\n- Iniciar acciones inmediatas como la aprobación de licencias\n- Apertura para recibir feedback adicional y sugerencias de mejora"
                },
                "participants": [
                    "bi4group.com_3437393538313737373630@resource.calendar.google.com,carlos.ariza@nucleoo.com,alejandro.martin@nucleoo.com,jaime.frias@nucleoo.com,julio.sanchez@nucleoo.com,sandra.rodriguez@nucleoo.com,angel.polo@nucleoo.com,rodrigo.diaz@nucleoo.com,andrea.sorroche@nucleoo.com,jose.requena@nucleoo.com",
                    "bi4group.com_3437393538313737373630@resource.calendar.google.com",
                    "carlos.ariza@nucleoo.com",
                    "alejandro.martin@nucleoo.com",
                    "jaime.frias@nucleoo.com",
                    "julio.sanchez@nucleoo.com",
                    "sandra.rodriguez@nucleoo.com",
                    "angel.polo@nucleoo.com",
                    "rodrigo.diaz@nucleoo.com",
                    "andrea.sorroche@nucleoo.com",
                    "jose.requena@nucleoo.com"
                ]
            }
        ]
    }
}
