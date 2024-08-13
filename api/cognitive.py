def master():
    return 0

def critical_thinking():
    return 0

def english():
    import google.generativeai as genai
    GOOGLE_API_KEY="AIzaSyD-WsKQ2O-isAK-PJjFxTusl1-TxcQ8l2E"

    genai.configure(api_key=GOOGLE_API_KEY)

    model = genai.GenerativeModel('gemini-1.5-flash')
    p="Generate 5 english hard questions "
    response = model.generate_content(p)
    return response.text

def entry(comp):
    if comp == "English":
        result = english()
    else:
        result = master()
    return result