from openai import OpenAI
import os
from dotenv import load_dotenv


def request(model, system, rfp, proposal):
    """
    This function makes a request to the OpenAI API and returns the response.

    Parameters:
    model (str): The model to be used for the request. For example, 'gpt-3.5-turbo'.
    system (str): The system message to initialize the conversation.
    rfp (str): The city's request for proposal.
    proposal (str): The land developer's proposal.

    Returns:
    str: The message returned by the model. If an error occurs during the request, the function returns None.

    """
    load_dotenv()  # take environment variables from .env.

    # Code of your application, which uses environment variables (e.g. from `os.environ` or
    # `os.getenv`) as if they came from the actual environment.

    API_KEY = os.getenv('OPENAI_API_KEY')
    if not API_KEY:
        print("Error: The OPENAI_API_KEY environment variable is not set.")
        return None
    try:
        # Initialize the OpenAI client with the base URL and API key
        client = OpenAI(base_url="https://openai.vocareum.com/v1", api_key=API_KEY)

        # Create a chat completion with the specified model and messages
        completion = client.chat.completions.create(
         model=model,
         messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": rfp},
            {"role": "user", "content": proposal}
          ]

         )

        # Return the message from the first choice in the completion
        return (completion)

    except Exception as e:

        return f"An error occurred: {e}"