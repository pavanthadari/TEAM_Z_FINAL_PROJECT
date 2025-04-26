import ollama

def generate_uml(idea):
    prompt = f"Generate a PlantUML-style sequence diagram (in text) for this system:\n\n{idea}"
    response = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']
