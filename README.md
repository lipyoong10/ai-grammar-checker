# ai-grammar-checker
A simple web application that corrects your grammar with GPT-3

To run this application:
1. Make sure to install the latest Python on your computer (https://www.python.org/downloads/)
2. Open "aigrammarchecker.py", and edit the following:
    a. openai.api_key - Get your key by creating an account and generating an API key (https://platform.openai.com/account/api-keys)
3. Run the script, and access it via localhost:7860

Do note that the default username and password is "username":"password". Do update this! 

Current live site: https://aigrammarchecker.lippykong.site/

The following is the AWS reference architecture for how this website is being hosted.

![alt text](https://github.com/lipyoong10/ai-grammar-checker/blob/main/aigrammarchecker.drawio.png)

Note: This does not adhere to AWS best practices as it's meant for author's learning purposes in self-hosting a web application, and testing out with OpenAI APIs
