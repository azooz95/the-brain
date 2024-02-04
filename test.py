

# huggingFaceAPI = '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'

# import os
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = huggingFaceAPI


# from langchain import HuggingFaceHub
# from getpass import getpass
# from langchain.llms import CTransformers
# from langchain import PromptTemplate, LLMChain

# repo_id = "TheBloke/llama-2-7b.ggmlv3.q4_1"
 
# # llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature":0, "max_length":64})
# llm = CTransformers(model="TheBloke/Llama-2-7B-GGML", model_file='llama-2-7b.ggmlv3.q4_1.bin', model_kwargs={"temperature":0.0, "max_length":256})
# template = """{question}"""
# prompt = PromptTemplate(template=template, input_variables=["question"])
# llm_chain = LLMChain(prompt=prompt, llm=llm)

# question = "Extract name and phone from following sentance and rewrite it as json: 0536568169 abdulaziz salman"
# print('The answer is: ',llm_chain.run(question))

# from transformers import XLNetTokenizer, XLNetModel

# tokenizer = XLNetTokenizer.from_pretrained('xlnet-base-cased')
# model = XLNetModel.from_pretrained('xlnet-base-cased')

# inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")
# outputs = model(**inputs)

# last_hidden_states = outputs.last_hidden_state
test_variable = '''

Problem solving
Teamwork
Leadership
Communication
S O F T S K I L L S
A research assistant of sound localization systems via AI contemporary
methods. I have a strong urge to prepare, analyze data, and construct models
to assist organizations achieving their objectives, which resulted acquiring
experiences of building various machine learning projects. I am a fast learner,
and a problem solver, with high adaptability and ability to manoeuvre difficult
tasks under high pressure. I am looking forward to having an honor to be a part
of your community.
MAINTENANCE INTERN ENGINEER
Top Glove Company | Aug 2020 - Oct 2020
Investigated and found the root causes of hole on glove pouch
Investigated the root causes of wrinkled wrappers and designed two
mechanical systems as proposed solutions
Digitized the usage of papers by built an android app with Google
sheet monitor
Investigated on root causes of weak seal, wrinkled seal and seal
allowance of glove pouch
Investigated and examined of the effectiveness of ionizers on
electrostatic cloud
C/C++, Python, Matlab, JavaScript,
Dart, HTML, CSS, SQL
AutoCAD,Catia, Solidworks (CAD)
Computer Numerical Control
Machine (CNC)
Machine learning (ML)
Mobile Development | Flutter
PLC
Circuit Design | NI Multisim & Proteus
Microsoft Office
PowerBi
T E C H N I C A L
S K I L L S
ABDULAZIZ SALMAN
M E C H A T R O N I C S E N G I N E E R
W O R K E X P E R I E N C E
P: +966582733605
E: aziz.alhaj25@gmail.com
Linkedin: https://bit.ly/3Eiad3w
Google Scholar: https://bit.ly/3JJtdZT
GitHub: https://bit.ly/3vyN6xB
Anwar P.P. Abdul Majeed, PhD CEng
MIMechE MIET SMIEEE
Associate Professor-School of
Robotics - Xi’an Jiaotong-Liverpool
University
Address: 111 Ren’ai Rd., Dushu Lake
Science & Education Innovation
Town- Suzhou Industrial Park, P.R.
China.
Phone: +60164378902
R E F E R E N C E
Arabic
English
L A N G U A G E S
The Institution Of Engineers,
Malaysia | Student Member
A F F I L I A T I O N
& M E M B E R S H I P S
A B O U T
RESEARCH ASSISTANT
Universiti Putra Malaysia| Oct 2021 - Current | Full-time
Research assistant in sound localization and AI
Co-supervised final year students for their final year projects
A Lab assistant for two lab sessions, navigation and electric labs
Supervised and assisted students for their study case project
AI ENGINEER
Aruvii Pte Ltd | July 2022 - Current
Pose Estimation and action recognition
Products dimension measurements and sent them through MQTT
server through ROS
Checking and counting rods diameter
The Diagnosis Of Diabetic Retinopathy By Means Of Transfer Learning And
Fine-Tuned Dense Layer Pipeline | https://bit.ly/3roJ21m | 2020
The Diagnostics of Osteoarthritis: A Fine-Tuned Transfer Learning Approach |
https://bit.ly/3BXM9SZ | 2022
P U B L I C A T I O N S

'''
# def template(word):
#     return f'Question: what is {word}?'

# from transformers import pipeline

# question_answerer = pipeline(task="question-answering", model="deepset/deberta-v3-large-squad2")

# for i in ['job name','the onwer\'s application name is a humnan', 'phone numbr']: 
#     q = template(i)
#     print(q)
#     preds = question_answerer(
#         question=q,
#         context=test_variable,
#     )
#     print(preds)
#     print(
#         f"score: {round(preds['score'], 4)}, start: {preds['start']}, end: {preds['end']}, answer: {preds['answer']}"
#     )


# import spacy
# from spacy import displacy

# nlp = spacy.load("en_core_web_trf")
# doc = nlp(test_variable)

# for ent in doc.ents:
#     print(ent.text, ent.start_char, ent.end_char, ent.label_)

# displacy.serve(doc, style="ent")
