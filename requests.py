def request(model, system, rfp, proposal):
    """
    This function makes a request to the OpenAI API and returns the response.

    Parameters:
    model (str): The model to be used for the request. For example, 'gpt-3.5-turbo'.
    system (str): The system message to initialize the conversation.
    master_plan (str): The city's master plan.
    proposal (str): The land developer's proposal.

    Returns:
    str: The message returned by the model. If an error occurs during the request, the function returns None.

    """
    try:
        from openai import OpenAI
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
        return completion.choices[0].message

    except Exception as e:

        print(f"An error occurred: {e}")

        return None