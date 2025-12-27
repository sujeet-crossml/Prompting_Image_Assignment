from google.genai import types

from client import client
from constant import *
from prompt import system_instruction

# Defining functions for the text generation 

def text_generation(prompt:str, image)->str:
    """
    Summary:
        Generate text from a multimodal model using an image and a text prompt.

    Args:
        prompt (str): Text prompt guiding the generation.
        image: Image input provided to the model for multimodal understanding.

    Returns:
        str: Generated
    """
    # Defining config for the model
    config = types.GenerateContentConfig(
        system_instruction= system_instruction,
        temperature=DEFAULT_PARAMS.get("temperature"), # For randomness and creative response
        top_p=DEFAULT_PARAMS.get("top_p"), # selects a fixed number of the most probable words
        top_k=DEFAULT_PARAMS.get("top_k"), # selects the smallest set of words whose cumulative probability exceeds a threshold 
        max_output_tokens=DEFAULT_PARAMS.get("max_tokens"), # max output token allowed for the response get.
    )
    # creating response form client
    response  = client.models.generate_content(
        model=MODEL_ID,
        contents=[image, prompt],
        config=config,
    )

    # returning text 
    return response.text