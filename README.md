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


### About the Deployment
1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2


## create ECR repository in AWS to store the docker image 
 - Save the URI: 975049934025.dkr.ecr.us-east-1.amazonaws.com/chatbot

## Create IAM User
    # Add policies
   - AWSEC2FullAccess
   - AmazonEC2ContainerRegistryFullAccess

## Create EC2 instance

## Open EC2 and install docker in EC2 machine

    # Optional

   - sudo apt-get update -y

   - sudo apt-get upgrade

    # Required

   - curl -fsSL https://get.docker.com -o get-docker.sh

   - sudo sh get-docker.sh

   - sudo usermod -aG docker ubuntu

   - newgrp docker
     
## Check wheter docker installed in your EC2 machine
 - docker --version

## Configure EC2 as self-hosted runner
- In GitHub, go to 
     Settings ---> Actions ---> Click on Runner ----> Create a 'self hosted runner' ---> Choose OS ---> Execute commands in your EC2 machine

## Set-up GitHub secrets
    - PINECONE_API_KEY
    - OPENAI_API_KEY
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - AWS_DEFAULT_REGION
    - ECR_REPO: <only repository_name>

