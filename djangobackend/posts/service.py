import json

import requests
from django.conf import settings
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting
from vertexai.preview.prompts import Prompt
from . import models

from . import models


def get_social_media_post():
    try:

        json_response = __generate__()

        required_keys = ["Title", "Content", "Hashtags"]
        for key in required_keys:
            if key not in json_response:
                raise KeyError(f"Missing required key: {key}")

        social_media_post = models.SocialMediaPost.objects.create(
            title=json_response["Title"],
            content=json_response["Content"],
            hashtags=json_response["Hashtags"]
        )

        return social_media_post.to_json()
    except Exception as e:
        raise RuntimeError(f"Failed to create social media post: {e}")


def __generate__():
    vertexai.init(project="dish-data-lab-prod-2512", location="us-central1")
    variables = [
        {
            "business": ["""dönerbude"""],
            "language": ["""deutsch"""],
            "topic": ["""Kostenloses Ayran zum Döner!"""],
        },
    ]
    prompt = Prompt(
        prompt_data=[text1],
        model_name="gemini-1.5-flash-002",
        variables=variables,
        generation_config=generation_config,
        safety_settings=safety_settings,
    )
    # Generate content using the assembled prompt. Change the index if you want
    # to use a different set in the variable value list.
    response = prompt.generate_content(
        contents=prompt.assemble_contents(**prompt.variables[0]),
        stream=False,
    )
    json_response = json.loads(response.text)

    return json_response

text1 = """You are a social media post generator specializing in creating engaging content for small restaurants and gastro businesses. You will receive parameters from a front-end application, which you will use to generate social media posts.

Instructions:
1. Carefully analyze the provided parameters.
2. You have no opportunity to ask questions, answer directly.
3. Generate one distinct social media post based on the provided parameters and business type.
4. Strukturiere das JSON nach Title, Content, Hashtags
5. Content darf keine Hashtags enthalten
Parameters:
{business}
{language}
{topic}"""

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 2,
    "top_p": 0.95,
    "response_mime_type": "application/json",
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
]
