from requests import request
from pdfhandler import load_pdf
from remove_stopwords import remove_stopwords
from summarizer_func import summarize_text


if __name__ == "__main__":
    def main(request_for_proposals, proposal, mode_switch=None):
        # Load PDF for city plan and proposal
        plan_page_count, request_text = load_pdf(request_for_proposals)
        proposal_page_count, proposal_text = load_pdf(proposal)

        if mode_switch == 'stopwords':
            # test option, removal of stopwords to reduce tokens
            plan_text = remove_stopwords(request_text)
            proposal_text = remove_stopwords(proposal_text)
            return plan_text, proposal_text

        if mode_switch == 'summarize':
            # Summarize the master plan and proposal
            plan_text = summarize_text(request_text)
            proposal_text = summarize_text(proposal_text)
            return plan_text, proposal_text

        print(proposal_text)
        # # Make a request to the OpenAI API
        # response = request('gpt-3.5-turbo',
        #                    'Compare the proposal to the master plan.',
        #                    request_for_proposals,
        #                    proposal_text)


main('PDFs/State_Street_Campus_Garage_RFP.pdf',
     'PDFs/Greystar_response.pdf')

