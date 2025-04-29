import ollama
def generate_code(idea):
    prompt = f"Generate starter Python code for the following software idea:\n\n{idea}\n\nInclude structure, comments, and placeholders."
    response = ollama.chat(model='codellama', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']
