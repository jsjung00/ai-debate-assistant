## OpenAI 

from openai import OpenAI

import os


def initialize_api_client(api_key):
    return OpenAI(api_key=api_key)


# Replace 'your-api-key' with your actual OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')

api_client = initialize_api_client(api_key)

def generate_counter(speech, api_client):
    
    system_prompt = """ You are a champion competitive debator, this is the debating speech your competitior has given. 
    Based on your inference of the specific debate format that they have followed, respond to it 
    Respond to it and win! 
    """

    response = api_client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        #response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Here's the speech: {speech} \\n "}
        ]
    )
    return response.choices[0].message.content



speech = """Ladies and gentlemen, the sanctity of human life and the inherent dignity of the individual lie at the core of our moral and legal systems. Today, I stand before you to argue that the death penalty fundamentally violates these principles and thus should be abolished. My value is Justice, upheld through the criterion of protecting human dignity.

Contention 1: The Death Penalty is Irreversible and Risks Innocent Lives
First, let's address the irreversibility of the death penalty. Our justice system, despite its intentions, is not infallible. Statistics from the Death Penalty Information Center show that since 1973, over 185 individuals sentenced to death have later been exonerated. These numbers not only highlight errors but also underscore the terrifying risk of executing the innocent—a risk that cannot be undone.

Contention 2: The Death Penalty Fails as a Deterrent
Moreover, the death penalty fails in its purported role as a crime deterrent. Extensive research indicates that states with the death penalty do not have lower rates of serious crimes than those without it. This lack of deterrence questions the effectiveness of the death penalty and challenges its justification on practical grounds.

Contention 3: The Death Penalty Violates Human Dignity
Finally, the death penalty inherently violates human dignity. The premeditated execution of a person by the state is a direct contradiction to the value of human life, a value endorsed by various international human rights organizations. The United Nations Human Rights Committee has repeatedly expressed concerns over the use of the death penalty, emphasizing its incompatibility with the right to life.

Conclusion
In conclusion, the death penalty is an irreversible, ineffective, and inhumane practice that undermines the very essence of justice by violating human dignity. For a society that values justice, morality, and human rights, abolishing the death penalty is not just an option—it is an obligation."
"""

print(generate_counter(speech, api_client))