import os

def save_output(filename, content):
    os.makedirs("outputs", exist_ok=True)
    with open(f"outputs/{filename}", "w") as f:
        f.write(content)
