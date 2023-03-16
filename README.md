# ai-grammar-checker
A simple web application that corrects your grammar with GPT-3<br>
The <b>application prompt is prepared to receive any text and perform grammar checking for all languages</b>

<h1>Installing, Setup, and Configuration steps:</h1>
To run this application:
<ol type="1">
   <li>Make sure to install the latest Python on your computer (https://www.python.org/downloads/)</li>
   <li>Open "aigrammarchecker.py", and edit the following:<br>
    <i>openai.api_key</i> - Get your key by creating an account and generating an API key (https://platform.openai.com/account/api-keys)</li>
   <li>Run the script, and access it via localhost:7860</li>
</ol>

Do note that the default username and password is "username":"password". Do update this! 

<h1>Live Demo Site</h1>
Current live site: https://aigrammarchecker.lippykong.site/ <br>
<s><i>Authentication restricted - Screenshot of Interface below</i></s>
<i>Authentication temporarily removed</i>

<h1>Solution Architecture</h1>
The following is the AWS reference architecture for how this website is being hosted.<br>

![AI Grammar Checker Cloud Architecture](https://github.com/lipyoong10/ai-grammar-checker/blob/main/aigrammarchecker.drawio.png)

<b>Note: This does not adhere to AWS best practices as it's meant for author's learning purposes in self-hosting a web application, and testing out with OpenAI APIs</b>


<h1>Web Interface & Demo</h1>
The user interface below is what the user will see after successful authentication.<br>

![Web User Interface](https://github.com/lipyoong10/ai-grammar-checker/blob/main/FunctionalPage.png)
