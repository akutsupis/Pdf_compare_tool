import openai.types
from openai import OpenAI
from key import API_KEY


def request(model, system, message):
    """
    This function makes a request to the OpenAI API and returns the response.

    Parameters:
    model (str): The model to be used for the request. For example, 'gpt-3.5-turbo'.
    system (str): The system message to initialize the conversation.
    message (str): The user message to be processed by the model.

    Returns:
    str: The message returned by the model. If an error occurs during the request, the function returns None.

    """
    try:
        # Initialize the OpenAI client with the base URL and API key
        client = OpenAI(base_url="https://openai.vocareum.com/v1", api_key=API_KEY)

        # Create a chat completion with the specified model and messages
        completion = client.chat.completions.create(
         model=model,
         messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": message}
          ]

         )

        # Return the message from the first choice in the completion
        return completion.choices[0].message

    except OpenAI.Error as e:
        # If an error occurs during the request, print the error and return None
        print(f"An error occurred: {e}")
        return None