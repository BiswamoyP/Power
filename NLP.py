from nltk.chat.util import Chat, reflections



pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
     [
        r"what is your name ?",
        ["My name is Chatty and I'm a chatbot ?",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
        
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) created ?",
        ["Biswamoy created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Bhubaneswar, Odisha',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
[
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
    
    
]
def chatty():
        print("Hi, I'm Chatty and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start
        chat = Chat(pairs, reflections)
        #chat = Chat(pairs, my_dummy_reflections)
        chat.converse()

#if __name__ == "__main__":
def Dext():
    from firebase import firebase
    txt = input("Hey I'm a friend of Chatty, you wanna know something about your house I'm here. Press 1 for status of the house, Press 2 to give orders.")
    if(txt=="1"):
        firebase = firebase.FirebaseApplication('https://temperature-3c6bd.firebaseio.com/', None)
        result = firebase.get('/user',None)
        print(result)
    if(txt=="2"):
        w = input("Enter your name")
        x = input("Enter the ID")
        y = input("Enter the action")
        firebase = firebase.FirebaseApplication('https://rpi-trial.firebaseio.com/', None)  
        data =  { 'Name': w,  
                  'ID No': x,  
                  'Action': y  
                }  
        result = firebase.post('/rpi-trial/',data)  
        print("The data has been updated and actions are being taken") 


    


rt = input("Hey There! Who do you wanna talk to? Chatty is your friend who will listen to you and Chatter will obey your commands\n")
if(rt == "Chatty"):
        chatty()
if(rt == "Chatter"):
        i = 1
        while(i>0):
            i = i+1
            Dext()        
