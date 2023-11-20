import requests
import json
from tkinter import *

#
# # Pushing
# # input_value = "what courses should i take in first year to get into computer science major"
# print("Bot: Welcome to the CLI Science Advicing Chatbot!")
# while True:
#     print("What questions do you have?\n")
#     input_value = input("Question ^^:")
#     print("Thinking!! :))")
#     url = "https://api-v2.agenthub.dev/remote_start_pipeline"
#
#     headers = {
#       "Content-Type": "application/json",
#       "x-auth-key": "xN1WJ1T18BXsmllIEEw8Juq0Zmp1"
#     }
#
#     data = {
#       "user_id": "xN1WJ1T18BXsmllIEEw8Juq0Zmp1",
#       "saved_item_id": "fjcuNfSyPi9E3jaL58nN53",
#       "api_key": "f9ce9031b8024177aa734e357102f078",
#       "pipeline_inputs": [
#             {"input_name": "question", "value": input_value},
#         ]
#     }
#
#     response = requests.post(url, headers=headers, json=data)
#
#     url = response.json()
#
#     run_id = url.split('run_id=')[1]
#
#
#     url = f"https://api-v2.agenthub.dev/plrun?run_id={run_id}"
#     headers = {
#         "x-auth-key": "xN1WJ1T18BXsmllIEEw8Juq0Zmp1"
#     }
#     global sourcedOutput
#
#     while (True):
#         response = requests.get(url, headers=headers)
#         # print(response.json()['state'])
#         if (response.json()['state'] == "FAILED"):
#             # print("FAIL")
#             break
#         if (response.json()['state'] == "DONE"):
#             sourcedOutput = response.json()
#             break
#
#     print("Bot:" + "\n" + sourcedOutput['outputs']['answer2'] + "\n")
#     continueMore = input("Do you have any more questions? (y/n)")
#     if continueMore == "n":
#         break

def returnVal(inputStr):

    input_value = inputStr
    url = "https://api-v2.agenthub.dev/remote_start_pipeline"

    headers = {
        "Content-Type": "application/json",
        "x-auth-key": "xN1WJ1T18BXsmllIEEw8Juq0Zmp1"
    }

    data = {
        "user_id": "xN1WJ1T18BXsmllIEEw8Juq0Zmp1",
        "saved_item_id": "fjcuNfSyPi9E3jaL58nN53",
        "api_key": "f9ce9031b8024177aa734e357102f078",
        "pipeline_inputs": [
            {"input_name": "question", "value": input_value},
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    url = response.json()

    run_id = url.split('run_id=')[1]

    url = f"https://api-v2.agenthub.dev/plrun?run_id={run_id}"
    headers = {
        "x-auth-key": "xN1WJ1T18BXsmllIEEw8Juq0Zmp1"
    }
    global sourcedOutput

    while (True):
        response = requests.get(url, headers=headers)
        # print(response.json()['state'])
        if (response.json()['state'] == "FAILED"):
            # print("FAIL")
            break
        if (response.json()['state'] == "DONE"):
            sourcedOutput = response.json()
            break

    return sourcedOutput['outputs']['answer2']





def main():

    import tkinter as tk
    from tkinter.ttk import Label

    home = tk.Tk()
    home.geometry('540x540')
    home.title('Awesome Science Advising')
    # show a label
    labelGreet = Label(home, text='\n ROBO SCIENCE ADVICING\n ', font = ('Quicksand Light', 35))
    labelGreet.pack()

    labelQuestion = Label(home, text='Enter a question :)')
    labelQuestion.pack()


    inputText = tk.Text(home, width = 100, height = 10)
    inputText.pack()

    global savedText
    savedText = ""

    def getText():
        savedText = inputText.get("1.0",'end-1c')
        global outputWindow
        outputWindow = tk.Tk()
        outputWindow.geometry("480x480")

        strneeded = returnVal(savedText)
        labelAnswerText = Label(outputWindow, text=strneeded)
        labelAnswerText.pack()

    submitButton = tk.Button(home, text="Submit!", command = getText)
    submitButton.pack()

    home.mainloop()


main()

