import spacy


def remove_stopwords(text):
    """
    This function takes a text and returns a version of the text with stopwords removed.

    Parameters:
    text (str): The text from which stopwords should be removed.

    Returns:
    str: The text with stopwords removed.
    """

    # Load the English language model
    nlp = spacy.load('en_core_web_sm')

    # Create a Doc object
    doc = nlp(text)

    # Generate a list of tokens that are not stopwords
    tokens = [token.text for token in doc if not token.is_stop]

    # Join the tokens back into a single string without stopwords
    text_without_stopwords = ' '.join(tokens)

    return text_without_stopwords
