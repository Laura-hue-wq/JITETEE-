# importing render and redirect
from django.shortcuts import render, redirect
# importing the openai API
import openai
# import the generated API key from the secret_key file
# from .secret_key import API_KEY
# loading the API key from the secret_key file
openai.api_key = "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"#API_KEY
HARDCODED_RESPONSES = {
    'personal injury': 'You can represent yourself in court in a personal injury case in Kenya, but it is recommended to seek legal advice as these cases can be complex and require extensive knowledge of the law.',
    'land dispute': 'You can represent yourself in court in a land dispute case in Kenya, but it is recommended to seek legal advice as these cases can be complex and require extensive knowledge of the law.',
    'divorce': 'You can represent yourself in court in a divorce case in Kenya, but it is recommended to seek legal advice as these cases can be emotionally challenging and require knowledge of family law.',
    'criminal case': 'Representing yourself in a criminal case in Kenya is not recommended as these cases can be complex and require extensive knowledge of criminal law. It is best to seek legal representation.',
    'contract dispute': 'You can represent yourself in court in a contract dispute case in Kenya, but it is recommended to seek legal advice as these cases can be complex and require knowledge of contract law.',
    'employment law': 'You can represent yourself in court in an employment law case in Kenya, but it is recommended to seek legal advice as these cases can be complex and require knowledge of labor law.',
    'property law': 'You can represent yourself in court in a property law case in Kenya, but it is recommended to seek legal advice as these cases can involve various legal issues such as land ownership, transfer of property, and lease agreements.',
    'tax law': 'Representing yourself in a tax law case in Kenya is not recommended as these cases can be highly technical and require knowledge of tax laws and regulations. It is best to seek legal representation.',
    'intellectual property': 'You can represent yourself in court in an intellectual property case in Kenya, but it is recommended to seek legal advice as these cases can involve complex legal issues such as copyright infringement, trademark disputes, and patent law.',
    'consumer protection': 'You can represent yourself in court in a consumer protection case in Kenya, but it is recommended to seek legal advice as these cases can involve various legal issues related to consumer rights, product safety, and liability.'
}

# this is the home view for handling home page logic
def home(request):
    return render(request, 'law/index.html')

def about(request):
    return render(request, 'law/about.html')

def contact(request):
    return render(request, 'law/contact.html')

def ai(request):
    # the try statement is for sending request to the API and getting back the response
    # formatting it and rendering it in the template
    try:
        # checking if the request method is POST
        if request.method == 'POST':
            # getting prompt data from the form
            userreq = request.POST.get('prompt')
            prompt = "How can I represent myself in court in a civil case relating to "+userreq + "in kenya"
            # making a request to the API 
            response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=1, max_tokens=1000)
            # formatting the response input
            formatted_response = response['choices'][0]['text']
            # bundling everything in the context
            context = {
                'formatted_response': formatted_response,
                'prompt': userreq
            }
            # this will render the results in the home.html template
            return render(request, 'represent/home.html', context)
        # this runs if the request method is GET
        else:
            # this will render when there is no request POST or after every POST request
            return render(request, 'represent/home.html')
    # the except statement will capture any error
    except Exception as e:
        if "You exceeded your current quota, please check your plan and billing details." in str(e):
            # error_message = "Insufficient credits. Please add more credits to your OpenAI account and try again."
            # print(error_message)
            if userreq.lower() in HARDCODED_RESPONSES:
                    formatted_response = HARDCODED_RESPONSES[userreq.lower()]
            else:
                formatted_response = "I'm sorry, I couldn't find a response for your request. Please try again with a different query."

            return render(request, 'represent/home.html', context={'formatted_response': formatted_response, 'prompt':request.POST.get('prompt')})
        else:
            error_message = "An error occurred while processing your request. Please try again later."
            # this will redirect to the error page with the error message
            return render(request, 'represent/404.html')

# this is the view for handling errors
def error_handler(request):
    return render(request, 'represent/404.html')
