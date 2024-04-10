if __name__ == "__main__":
    from requests import request
    from pdfhandler import load_pdf

def main(city_plan, proposal):
    plan_page_count, plan_text = load_pdf(city_plan)
    proposal_page_count, proposal_text = load_pdf(proposal)


    response = request('gpt-3.5-turbo','Consider some text',plan_text)

    return response

