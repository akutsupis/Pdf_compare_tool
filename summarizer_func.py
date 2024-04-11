from summarizer import Summarizer


def summarize_text(text):
    """
    This function takes a text and returns a summarized version of the text.

    Parameters:
    text (str): The text to be summarized.

    Returns:
    str: The summarized text.
    """

    # Initialize the BERT summarizer
    summarizer = Summarizer()

    # Summarize the text
    summarized_text = summarizer(text)

    return summarized_text