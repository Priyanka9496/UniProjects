from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Chat
import json
from django.views.decorators.csrf import csrf_exempt
from .openai_api import ask_openai


@csrf_exempt
def chatbot_ui(request):
    """Render Chatbot UI with previous chat history."""
    chats = Chat.objects.filter(user=request.user).order_by('created_at')
    response = None

    if request.method == 'POST':
        message = request.POST.get('message')
        print("message: ",message)

        # ✅ Validate for empty message
        if not message:
            response = "Message cannot be empty."
        else:
            response = ask_openai(message)
            print("response: ", response)

            # ✅ Save only if message and response are valid
            if message and response:
                Chat.objects.create(
                    user=request.user,
                    message=message,
                    response=response,
                    created_at=timezone.now()
                )

    return render(request, 'chatbot/chatbot.html', {'chats': chats, 'response': response})


@csrf_exempt
def chatbot_api(request):
    """Handle chatbot API responses for AJAX calls."""
    if request.method == 'POST':
        try:
            # Log the raw request body for debugging
            print("Raw Request Body:", request.body)

            # Decode the incoming JSON data
            data = json.loads(request.body)
            message = data.get('message')

            print("Extracted Message:", message)

            if not message:
                return JsonResponse({'error': 'Message cannot be empty.'}, status=400)

            # Mock response for now
            response = ask_openai(message)
            return JsonResponse({'message': message, 'response': response})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)

    return JsonResponse({'error': 'Invalid request.'}, status=400)
