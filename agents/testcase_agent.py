import ollama

def generate_testcases(idea):
    prompt = f"Generate Python unit test cases for key components of this software idea:\n\n{idea}"
    response = ollama.chat(model='codellama', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']
