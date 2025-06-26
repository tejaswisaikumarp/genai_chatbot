# Chatbot

# How to implement

###  Steps:

Clone the repository
```bash
Project repo: https://github.com/
```

### Step-1: Create a conda environment after cloning the repository
```bash
conda cretae -n chatbot_genai python=3.10 -y
```

### Activate the conda environment
```bash
conda activate chatbot_genai
```

### Step-2: Install the requirements.txt
```bash
pip install requirements.txt
```



### Create a `.env` file in the root directory and add the api_keys(Pinecone, OpenAI):
```ini
PINECONE_API_KEY="*********************************************"
OPENAI_API_KEY="************************************************"
```

```bash
# Run the following command to store the embeddings in  pinecone
python store_index.py
```

```bash
# Finally, Run the app.py
python app.py
```