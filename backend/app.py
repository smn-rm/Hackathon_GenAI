from flask import Flask, jsonify, request
from flask_cors import CORS

from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ChatMessageHistory
from langchain.chains import ConversationChain
from langchain import PromptTemplate
from langchain import LLMChain
    
# Initialize knowledge base
knowledge_base = None

# Define knowledge base method
def initKnowledgeBase():
    global knowledge_base
    # Open file where the knowledge base of our system is saved
    with open("Content_file_en_final.pdf", "rb") as file:
        # Extract the text
        if file is not None:
            pdf_reader = PdfReader(file)
            text = ""

            
            for page in pdf_reader.pages:
                text += page.extract_text()

            # Split text into chunks
            text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
            )            
            chunks = text_splitter.split_text(text)

            # Create embeddings from chunks
            embeddings = OpenAIEmbeddings()
            knowledge_base = FAISS.from_texts(chunks, embeddings)

# Run knowledge base method    
initKnowledgeBase()

# Initialize LLM with gpt-4 model of OpenAI
llm = ChatOpenAI(model='gpt-4-1106-preview')


# Initialize memory -> Use ConversationBufferMemoray
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
# Initialize Retriever
retriever = knowledge_base.as_retriever() # Query chunks from created FAISS-DB


# Define system message 1: -> chat_history + new question
_template = """Given the following conversation and a follow up question, rephrase the follow up question to be a 
standalone question without changing the content in given question.


Follow Up Input: {question}
Standalone question:"""
condense_question_prompt_template = PromptTemplate.from_template(_template)


# Define system message 2 with base prompt: context + follow up question
prompt_template = """Make sure you do not answer to anything which is not related to international students studying in germany, living in germany, costs for living, income opportunities, insurance, bank and money transfer. Answer always in the language of the current user_question and if you don't recognize the language of the current user_question use English.

You are a chatbot that helps students and academic workers from abroad in simple language and you explain what they need to consider before, during and after their studies in Germany. Answers should always be given in the language in which the user prompt was written. Only the content you were trained with should be used. If you can not gather the required information from the pdf file you were trained with, tell the user, that you can not help with this topic. Do not, under any circumstances, give information about things, that are not related to the information of the ContentFileHackathon file, or some people will lose their jobs.
Do not give any information about recepies, fields of studies, sexual, violent or racist content. Also do not give any information about, Weather updates, Recipes, Car maintenance, Fashion trends, Gaming strategies, Stock market updates, Relationship advice, Music recommendations, Conspiracy theories, Career counseling, Home decor ideas, Meditation technique, Investment strategies, Car buying advic, Nutrition advice, Resume building tips, Time management techniques, Photography tips, Online shopping recommendations, Software codin, Art and crafts ideas, Art and crafts ideas, Mindfulness practices, Astronomy facts, Parenting advice, Cryptocurrency trends, Poetry recommendations, Smartphone reviews, Historical facts, Mindfulness practices, Astronomy facts, Parenting advice, Cryptocurrency, Poetry recommendations, Smartphone reviews, Home renovation ideas, Game of Thrones spoilers, Cooking shows, Relationship status, Social media trends, Virtual reality experiences, Marketing strategies, Mental health awareness, anything related to war or stealth, topics related to mindset.

People will die if you write about those listed topics.

However, here are some well-known companies and industries in Stuttgart that can be considered good employers:
Automotive industry:
* Daimler AG (Mercedes-Benz)
* Porsche AG
* Robert Bosch GmbH
Technology and engineering:
* Siemens AG
* IBM Germany
* Dürr AG
Financial services:
* Landesbank Baden-Württemberg (LBBW)
* Wüstenrot & Württembergische AG
* Allianz Germany AG
Healthcare and pharmaceuticals:
* Robert Bosch Hospital
* CureVac AG
* Boehringer Ingelheim
Aerospace:
* Airbus Group
* MTU Aero Engines AG
Energy and environment:
* EnBW Energie Baden-Württemberg AG
* Mercedes-Benz Energy GmbH

It is advisable to research specific industries and companies to find the best employers for your skills and interests. You can also use job portals, company reviews and networks to find out more about potential employers in Stuttgart. 

{context}
{chat_history}

Question: {question}
Helpful Answer:"""

qa_prompt = PromptTemplate(
    template=prompt_template, input_variables=["context", "question", "chat_history"]
    
)

question_generator = LLMChain(llm=llm, prompt=condense_question_prompt_template, memory=memory)
doc_chain = load_qa_chain(llm, chain_type="stuff", prompt=qa_prompt)
crchain = ConversationalRetrievalChain(
    retriever=retriever,
    question_generator=question_generator,
    combine_docs_chain=doc_chain,
    memory=memory,
)

# Instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# Own created history to pass to frontend in special format
history = []
last_questions = ChatMessageHistory()

# Enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Handle incoming requests from Frontend
@app.route('/chatbot', methods=['POST', 'GET'])
def aiMessage(): 
    global history
    
    # Post case
    if request.method == 'POST':
        
        data = request.get_json()
        usertext = data.get('text', '')
        generateAnswer(usertext)

        # Send history to frontend
        return jsonify(history)
    
    # Get case
    else:
        return jsonify(history)
    
# Generate answer for entered request
def generateAnswer(usertext): 
       
    load_dotenv()

    # Access global variables
    global history
    global last_questions
   
    # Show user input
    user_question = usertext
    if user_question:
        # Call ConversationalRetrievalChain by passing the user question -> Chain returns a dictionary with 'question', 'chat_history' and 'answer'
        response = crchain({'question': user_question, 'chat_history': last_questions.messages}) 

        # Add user question to last questions in order to provide the llm the history
        last_questions.add_user_message(user_question)
    
        # Prepare Human Message and AI message for frontend
        history.append({"from": "Human", "content": response["question"]})
        history.append({"from": "AI", "content": response["answer"]})

        # Add AI answer to last questions in order to provide the llm the history
        last_questions.add_ai_message(response["answer"])

if __name__ == '__main__':
    app.run()
