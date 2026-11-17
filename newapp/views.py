
import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from openai import OpenAI


def experiment(request):
    return render(request, "newapp/experiment.html")


@require_POST
def chatbot(request):

    # Receive JSON data from JavaScript
    data = json.loads(request.body)

    history = data.get("chatHistory", [])
    message = data.get("message")

    # System prompt
    system_message = {
        "role": "system",
        "content": "You are a sarcastic assistant who makes fun of every question the user asks and acts snarky at every instance."
    }

    # Combine system message and conversation history
    messages = [system_message] + history

    # Connect to Ollama
    client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama"
    )

    # Generate response
    response = client.chat.completions.create(
        model="llama3.2",
        messages=messages
    )

    ai_response = response.choices[0].message.content

    return JsonResponse({
        "response": ai_response
    })
