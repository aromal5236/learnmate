import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from groq import Groq
from django.shortcuts import render

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')

        if not user_message:
            return JsonResponse({'error': 'Message is required.'}, status=400)

        # Groq API setup
        client = Groq(api_key="API_KEY")
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "you are a helpful assistant."},
                {"role": "user", "content": user_message},
            ],
            model="llama3-8b-8192",
        )
        response_content = chat_completion.choices[0].message.content
        return JsonResponse({'response': response_content})

    return JsonResponse({'error': 'Invalid request method.'}, status=405)



def home(request):
    return render(request, 'index.html')
