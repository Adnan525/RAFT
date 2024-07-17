import os
from dotenv import load_dotenv

from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

from raft_util import get_doc_chunk, generate_qa_pair, generate_cot_answer, process_qa_pair

load_dotenv(".env")
openai_token = os.getenv("openai_api_key")

# openai model
llm = OpenAI(temperature=0, n=1, model="gpt-3.5-turbo", api_key=openai_token)
embed_model = OpenAIEmbedding()

# document chunk
docs = get_doc_chunk("./text/")

# generate questions for each chunk and save the questions in questions.txt
with open("questions.txt", "a") as f:
    for i, chunk in enumerate(docs):
        openai_response = generate_qa_pair(llm, chunk)
        # each chunk will generate 2 questions
        question_list = process_qa_pair(openai_response)
        for j, text in enumerate(question_list):
            f.write(text + "\n")
            if j%2 == 1:
                f.write(str(i) + "\n")
        break

# generate CoT answer for each question
question_file = open("questions.txt", "r")
q_a_i = question_file.readlines()
with open("raft.txt", "a") as raft_file:
    for i, line in enumerate(q_a_i):
        raft_file.write(line)
        # if a question generate CoT
        if i%3 == 0:
            generate_cot_answer(llm, line, int(q_a_i[i+2]))