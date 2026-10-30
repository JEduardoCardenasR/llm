# Asistente de Escritura Automática

Proyecto 1 de Inteligencia Artificial / LLMs.  
Asistente de escritura en consola que usa la **API de OpenAI** para corregir textos, sugerir continuaciones y generar contenido a partir de un tema.

## Funcionalidades

1. **Corregir gramática y estilo** — pegas un texto y la IA lo mejora.
2. **Sugerir continuación** — das el inicio y la IA escribe el siguiente párrafo.
3. **Generar texto desde un tema** — indicias tema y tono; la IA redacta el texto.

## Requisitos

- Python 3.8+
- Una [API Key de OpenAI](https://platform.openai.com/api-keys)

## Instalación

```bash
cd asistente_escritura
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
# source venv/bin/activate

pip install -r requirements.txt
```

## Uso

```bash
python app.py
```

Ingresa tu API Key cuando se te pida y elige una opción del menú.

## Tecnologías

- Python
- [OpenAI API](https://platform.openai.com/) (`gpt-4o-mini`)
