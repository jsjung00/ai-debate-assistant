## OpenAI 
import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = ''

prompt = "ONLY construct a cogent counter-argument that engages the following prompt's core assertions while adhering to these guidelines: Clearly delineate your foundational value premise and criteria for evaluating the resolution. Directly refute at least one key claim from the initial prompt by challenging its validity and implications. Ground your refutation in philosophical concepts and ethical frameworks from notable thinkers. Provide contrasting examples or perspectives that undermine the prompt's arguments. Weigh the real-world impacts and broader implications of both positions. If the prompt prioritizes certain values, articulate an alternate value hierarchy. Finally, craft a concise yet substantive response within a prescribed length, modeling the time constraints of a speech. Your counter-argument should coherently refute the prompt's central points, root your position in philosophical rigor, and adjudicate the competing perspectives through impact analysis and value judgments."

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message['content']

# Example usage
prompt = "The death penalty should be abolished."
response = generate_response(prompt)
print(response)
