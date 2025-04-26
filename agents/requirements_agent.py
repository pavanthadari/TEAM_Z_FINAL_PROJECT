import ollama

def generate_requirements(idea):
    prompt = f"Generate both functional and non-functional requirements for the following software idea:\n\n{idea}"
    response = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']
