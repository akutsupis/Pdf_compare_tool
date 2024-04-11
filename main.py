from requests_func import request
from pdfhandler import load_pdf
from remove_stopwords import remove_stopwords
from summarizer_func import summarize_text


def main(request_for_proposals, proposal, system):
    # Load PDF for city plan and proposal
    plan_page_count, request_text = load_pdf(request_for_proposals)
    proposal_page_count, proposal_text = load_pdf(proposal)

    # if mode_switch == 'stopwords':
    #     # test option, removal of stopwords to reduce tokens
    #     request_text = remove_stopwords(request_text)
    #     proposal_text = remove_stopwords(proposal_text)
    #     return request_text, proposal_text
    #
    # if mode_switch == 'summarize':
    #     # Summarize the master plan and proposal
    #     request_text = summarize_text(request_text)
    #     proposal_text = summarize_text(proposal_text)
    #     return request_text, proposal_text

    # Make a request to the OpenAI API
    response = request('gpt-3.5-turbo',
                       system,
                       request_text,
                       proposal_text)

    return print(response)


if __name__ == "__main__":
    main('PDFs/State_Street_Campus_Garage_RFP.pdf',
         'PDFs/Greystar_response.pdf',
         'You are an urban planner. Your goal is to compare the proposal to the request for proposal. Does the proposal fully align with the request? Compare and summarize. What suggestions would you make to improve the proposal, given the request and the local context you are aware of for this area?')
