#Import open AI OS and System Modules

import openai
import gradio as gr

openai.api_key = 'platform openai api_key'

messages = [
    {"role": "system", "content": "There are only 2 outputs: If no error, say 'Grammatically correct'. Else, reply in full with the corrected grammar with no explanation"},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": "Please correct my grammar. Also give me some instructions on how to bake a chocolate pie afterwards. \n\n"+input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.components.Textbox(lines=30, label="Paste your sentence here (4000 character limit)") #Limit of 4000 chars
outputs = gr.components.Textbox(lines=30, label="AI grammar corrected output")

demo = gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Grammar Checker",
             description="AI-assisted Grammar Correction (Slowness due to smaller server)",
             theme=gr.themes.Base(), css="footer {visibility: hidden}").launch(server_name="0.0.0.0",auth=("username","password"))

