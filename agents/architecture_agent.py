import ollama

def generate_architecture(idea):
    prompt = f"Generate a high-level system architecture for this idea:\n\n{idea}\n\nInclude components and interactions."
    response = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']
