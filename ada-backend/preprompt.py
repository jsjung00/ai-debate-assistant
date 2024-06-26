import openai
# import fitz  # PyMuPDF
import os


from dotenv import load_dotenv

load_dotenv()
# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Extract text from PDFs
def extract_text_from_pdfs(folder_path):
    text_data = {}
    # for filename in os.listdir(folder_path):
    #     if filename.endswith(".pdf"):
    #         file_path = os.path.join(folder_path, filename)
    #         pdf_document = fitz.open(file_path)
    #         text = ""
    #         for page_num in range(len(pdf_document)):
    #             page = pdf_document.load_page(page_num)
    #             text += page.get_text()
    #         text_data[filename] = text
    return text_data

# Find key points related to the prompt
def find_key_points(text, prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Find key points in the following text that relate to the prompt."},
            {"role": "user", "content": f"Prompt: {prompt}\n\nText: {text}"}
        ],
        max_tokens=200
    )
    return response.choices[0].message['content']

def generate_counter_arg(prompt, preprompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": preprompt},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message['content']

def generate_counter_arg_update_w_keypoints(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Use these keypoints to make this counter argument better."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message['content']

# Generate argument

def process_speech( speech ):
    folder_path = 'ragfiles'
    pdf_texts = extract_text_from_pdfs(folder_path)
    #print(pdf_texts)
    preprompt = "DO NOT GIVE A FURTHERMORE, ADDITIONALLY, IN CONCLUSION. YOU MUST Provide a Observation 1 for Contention 1 and its Subpoint A, Contention 2 make a Subpoint A, B and C. You are a champion competitive debator, this is the debating speech your competitior has given. Based on your inference of the specific debate format that they have followed, respond to it. Respond to it and win!To construct an effective counter-argument, immerse yourself deeply in the topic, seeking out and understanding numerous examples, and read extensively on both sides of the issue. Identify key authors and familiarize yourself with their works. After thorough immersion, brainstorm the foundational values and criteria that link these values to the topic. YOU MUST Provide a Observation 1 for Contention 1 and its Subpoint A, Contention 2 make a Subpoint A, B and C against each brainstormed item to prepare for potential clashes. This preparation will enable you to contest predictable arguments and develop a strong platform for your case. Divide roles into affirmative and negative debaters to craft cases that incorporate your style, evidence, clear organization, and direct incorporation of the topic wording. Establish a value premise, the ultimate value to uphold in the debate (e.g., Justice, Morality, Social Welfare), ensuring all arguments relate to this value. Next, decide on a criterion, the mechanism to achieve and weigh the value premise (e.g., the social contract, protection of individual rights). Finally, develop two or three main contentions, each supported by at least one quote, to form the core of your case. This comprehensive approach ensures a robust and coherent counter-argument that effectively engages with the core assertions of the prompt. YOU MUST Provide a Observation 1 for Contention 1 and its Subpoint A, Contention 2 make a Subpoint A, B and C."
    prompt = "Make a counter argument speech to this speech: ${speech}"
    key_points = {filename: find_key_points(text, prompt) for filename, text in pdf_texts.items()}
    #print(key_points)
    response = generate_counter_arg(prompt, preprompt)
    print(response)
    updated_response = generate_counter_arg_update_w_keypoints(response)
    print(updated_response)
    return updated_response



sample_speech = "I affirm the resolution that a just society ought not use the death penalty as a form of punishment. My value today is Justice. Justice is defined simply and traditionally as giving each their due. Justice within the context of today’s debate can be seen as solely retributive insofar as we are discussing the just response to wrongdoing. The central question of the resolution is whether a just society ought to implement death punishments, thus justice must be the overarching value premise. My criterion today is the happiness principle. Utilitarian in practice, the happiness principle provides a clear mechanism to weigh different paths and their consequences within the context of the same end state or goal, Justice. In addition, the happiness principle is the most appropriate criterion for this debate topic. Jeremy Bentham explains the immediate principal end of punishment is to control action, i.e., the conduct of those who are liable to a punishment if they violate the law as well as the conduct of those who are undergoing punishment after having been sentenced for a violation. Bentham further clarifies that the goal of punishment ought to be general prevention, an end that will be achieved if and only if adequate control is attained. But both of these ends are penultimate. The ultimate end of penal laws is one shared with all legislation, to positively augment the total happiness of the community. Thus, in his theory, the only rational or justifiable punishments for a society to adopt are punishments that most efficiently produce the greatest happiness.  Observation 1: Resolutional Analysis  The resolution asks us to evaluate the nature of the death penalty as just or otherwise. We must first look at how theoretical ideas are properly used in discussing real world occurrences. Concepts of justice and morality exist within a vacuum but when practically applied to actions must be contextualized as existing among alternatives. In other words, the morality of genocide is neutral unless it’s considered within the span of less offensive and egregious forms of combat. With this view, it’s seen that both sides of this debate must argue the death penalty’s morality or just nature as it compares to a comparable alternative, namely life imprisonment.  Contention 1: The death penalty consumes costly resources.  Subpoint A: From purely a financial perspective, the death penalty wastes financial resources that could be used more effectively and efficiently elsewhere. A New Jersey Policy Perspectives report concluded that the state's death penalty has cost taxpayers $253 million since 1983, a figure that is over and above the costs that would have been incurred had the state utilized a sentence of life without parole instead of death. The study examined the costs of death penalty cases to prosecutor offices, public defender offices, courts, and correctional facilities. The report concluded that from a strictly financial perspective, it is hard to reach a conclusion other than this: New Jersey taxpayers over the last 23 years have paid more than a quarter billion dollars on a capital punishment system that has executed no one. Furthermore, this is not a phenomenon for New Jersey. According to a report released by the National Bureau of Economic Research, counties across the US manage the high costs associated with the death penalty by decreasing funding for highways and police and by increasing taxes. The report estimates that between 1982-1997 the extra cost of capital trials was $1.6 billion. This evidence has two implications. First, the death penalty is using vast financial resources while rarely actually being used, i.e., killing people. This speaks not only to its wastefulness but also its decreasing ability to deter future capital crimes. Second, the money that is wasted in death penalty cases could be spent in numerous other areas to increase the overall happiness of any given community. Using the happiness principle, it’s clear that a just society trying to increase its community’s happiness wouldn’t use the death penalty as a form of punishment.  Contention 2: The death penalty is not just.  Subpoint A: There is no way to correct the erroneous infliction of the death penalty. Imprisonment, however, can be abruptly ended as soon as there is reason to conclude that an innocent person is being punished. Furthermore, there is no way to compensate the wrongly executed person; the wrongly imprisoned person can be awarded a compensatory sum. Insofar as the happiness principle applies to all sentient beings that are able to feel happiness, imprisonment allows the greatest ability for corrective action toward greater happiness. This characteristic of imprisonment will always leave it a small amount more just and consequently yield an affirmative ballot.  Subpoint B: The execution of an individual hinders the ability of the criminal justice system to effectively administer justice. Extending Bentham’s critique, Hugo Bedau explains that executing a convicted criminal destroys one source of testimonial proof concerning other crimes, committed by the offender or by other criminals. That same criminal, however, if confined to prison, may well be persuaded to divulge such information and thereby aid the cause of justice. In utilitarian terms, the usefulness of the convict to the administration of criminal justice is frustrated by the death penalty, at least by comparison with prolonged imprisonment. The implication of this evidence is overall total possible social happiness is lessened than it otherwise would be. This violates the happiness principle and warrants an affirmative ballot.  Subpoint C: The death penalty is applied at random. Politics, quality of legal counsel, and the jurisdiction where a crime is committed are more often the determining factors in a death penalty case than the facts of the crime itself. The death penalty is a lethal lottery: of the 22,000 homicides committed every year, approximately 150 people are sentenced to death. Such a divide in convictions and death sentences violates the equitable nature of the happiness principle by unevenly affecting the happiness of certain criminals as opposed to others. Such an application is unjust and should be rejected."

'''
Example response:

I negate the resolution that a just society ought not use the death penalty as a form of punishment. My value today is Retribution. Retribution is an essential aspect of justice and plays a crucial role in maintaining societal order and reinforcing the consequences of criminal actions. The central question of this debate is whether the death penalty serves as a just response to heinous crimes, and retribution must be the primary value premise to consider in this context.

My criterion for evaluating the use of the death penalty is Legal Justice. Legal justice refers to the appropriate application of laws and punishment within a legal system. It is crucial to ensure that criminals are held accountable for their actions and that the severity of punishment is commensurate with the severity of the crime committed. The death penalty, when applied judiciously and in accordance with due process, can serve as a just form of retribution for the most egregious offenses.

Observation 1: Resolutional Analysis
While it is important to consider alternative forms of punishment, such as life imprisonment, it is essential to recognize that not all crimes can be adequately punished through incarceration alone. Some crimes, such as mass murder or acts of terrorism, may be so heinous that they warrant the ultimate punishment of death. In such cases, the death penalty serves as a deterrent to potential offenders and sends a powerful message about the consequences of committing such atrocities.

Contention 1: The Death Penalty is a Just Response to Heinous Crimes
Subpoint A: The death penalty serves as a deterrent to potential offenders and helps prevent future crimes. Studies have shown that the threat of execution can dissuade individuals from committing violent crimes, thereby protecting society from dangerous criminals. By imposing the death penalty for the most severe crimes, society sends a clear message that such actions will not be tolerated, ultimately contributing to a safer and more just society.

Subpoint B: The death penalty provides closure and justice for victims and their families. For the loved ones of victims of heinous crimes, seeing the perpetrators face the ultimate consequence of their actions can provide a sense of closure and vindication. The death penalty allows society to uphold the rights and dignity of victims, ensuring that justice is served and that the memory of those who have been wronged is honored.

Subpoint C: The death penalty can be applied in a fair and just manner through reforms to the legal system. While concerns about arbitrary application and disparities in sentencing are valid, reforms can be implemented to ensure that the death penalty is reserved for the most serious and heinous crimes. By addressing issues such as bias, inadequate legal representation, and procedural errors, the death penalty can be applied more equitably and in accordance with principles of legal justice.

In conclusion, the death penalty, when applied justly and in accordance with legal principles, serves as a necessary and appropriate form of punishment for the most heinous crimes. By upholding retribution and legal justice, society can ensure that criminals are held accountable for their actions and that justice is served for victims and their families. The death penalty, as a tool of justice, plays a crucial role in maintaining societal order and deterring future crimes, making it a just and necessary form of punishment in a fair and equitable legal system.
'''
