from tkinter import *
root = Tk()
root.title("Chatbot")


def notify_responses():
    global name, chatbot, responses, email
    responses = {
        'quit': {
            'keyword': ['end', 'bye', 'quit', 'leave', 'exit'],
            'response': "Visit us for detailed health evaluation " + name
        },
        'my_name': {
            'keyword': ['my name', 'i am', 'my self'],
            'response': f"Hi {name}, nice to meet you"
        },
        'your_name': {
            'keyword': ['your name', 'who are you'],
            'response': f"My name is {chatbot} and Please Enter your name and email"
        },
        'your_email': {
            'keyword': ['my email', '@', '.com', 'number', 'whatsapp'],
            'response': f"We have noted your details and will save it for the time you visit us."
        },
        'hello': {
            'keyword': ['hi', 'hello', 'good morning', 'good evening', 'good afternoon', 'hola', 'namaste', 'pranam', 'namaskar', 'ram ram', 'jai hind'],
            'response': "Hello " + name + ", what can I help you with?"
        },
        'treatments': {
            'keyword': ['treatments', 'treatment', 'dental', 'optical', 'eye', 'chest', 'surgery', 'cancer', 'typhoid', 'dengue', 'malaria', 'diabetis', 'cholestrol', 'heart', 'kidney', 'cold', 'covid', 'corona', 'flu', 'cholera', 'chikenpox', 'depression', 'anxiety', 'pneumonia', 'tb'],
            'response': f"We have this treatment available, you can book an appointment for it. "
        },
        'rates': {
            'keyword': ['rates', 'charges', 'charge', 'rate', 'price', 'cost', 'money', 'payment'],
            'response': f"For routine checkup we charge 100 Rs and for a full body checkup we cost 500 Rs."
        },
        'symptoms': {
            'keyword': ['symptoms', 'cough', 'headache', 'fever', 'pain', 'sore', 'inflammation', 'acidity', 'temperature', 'stress', 'sneezing', 'vomiting'],
            'response': f"We have noted your symptomes, when you visit us, we will send this information to doctor."
        },
        'medicines': {
            'keyword': ['medicines', 'paracetamol', 'cetirizine', 'dolo', 'nise', 'numesulide', 'azithromcin', 'ibuprofen'],
            'response': f'You can show the medicine slip to the medical store. He will help you out.'

        },
        'Quit': {
            'keyword': ['Quit'],
            'response': f'Please do visit us again and i hope you are satisfied'
        }
    }
global query
query = ""

def set_query(x):
    global query
    query = x

def keyword_find(keyword):
    return any(x in query for x in responses[keyword]['keyword'])


def get_response(keyword):
    return responses[keyword]['response']


def converse(query: str):
    global name, chatbot, ticket, responses, email

    if keyword_find('quit'):
        res = get_response('quit')

    elif keyword_find('my_name'):
        name = query.split(' ')[-1].capitalize()
        notify_responses()
        res = get_response('my_name')
    elif keyword_find('your_name'):
        res = get_response('your_name')

    elif keyword_find('your_email'):
        res = get_response('your_email')

    elif keyword_find('hello'):
        res = get_response('hello')
    elif keyword_find('treatments'):
        res = get_response('treatments')
    elif keyword_find('rates'):
        res = get_response('rates')
    elif keyword_find('symptoms'):
        res = get_response('symptoms')
    elif keyword_find('medicines'):
        res = get_response('medicines')
    elif keyword_find('Quit'):
        res = get_response('Quit')
    else:
        res = "Sorry, we can not help you online.\nPlease do visit nearest A* hospital."
    return res


global name, chatbot, ticket, responses
name = ''
chatbot = 'Aliza'
ticket = ''
notify_responses()

def func(query):
    return converse(str(query))
    # while not keyword_find('quit'):
    #     print(converse(query))
    #     print()
    #     query = str(input('> ')).lower()
    #     if query in ['quit', 'Quit', 'buy']:
    #         print("Glad I could help you. Have a nice day! ")
    #         break
    

# query = str(
#     input('\nWelcome to A* Multispeciality Hospital.\n> ')).lower()
# while not keyword_find('quit'):
#     print(converse(query))
#     print()
#     query = str(input('> ')).lower()
#     if query in ['quit', 'Quit', 'buy']:
#         print("Glad I could help you. Have a nice day! ")
#         break





def send():
    # query = str(
    #     input('\nWelcome to A* Multispeciality Hospital.\n> ')).lower()
    # while not keyword_find('quit'):
    #     print(converse(query))
    #     print()
    #     query = str(input('> ')).lower()
    #     if query in ['quit', 'Quit', 'buy']:
    #         print("Glad I could help you. Have a nice day! ")
    #         break
    
    
    
    # send = "You -> "+e.get()
    # txt.insert(END, "n"+send)
    # user = e.get().lower()
    
    # txt.insert(END, '\nWelcome to A* Multispeciality Hospital.\n> ')
    a = e.get()
    send = "You -> "+a
    txt.insert(END, "\n"+send)
    set_query(a)
    txt.insert(END, "\nBot -> " + func(a))
    
    
    # if(user == "hello"):
    #     txt.insert(END, "n" + "Bot -> Hi")
    # elif(user == "hi" or user == "hii" or user == "hiiii"):
    #     txt.insert(END, "n" + "Bot -> Hello")
    # elif(e.get() == "how are you"):
    #     txt.insert(END, "n" + "Bot -> fine! and you")
    # elif(user == "fine" or user == "i am good" or user == "i am doing good"):
    #     txt.insert(END, "n" + "Bot -> Great! how can I help you.")
    # else:
    #     txt.insert(END, "n" + "Bot -> Sorry! I dind't got you")
    # e.delete(0, END)



txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
e.grid(row=1, column=0)
send = Button(root, text="Send", command=send).grid(row=1, column=1)
root.mainloop()