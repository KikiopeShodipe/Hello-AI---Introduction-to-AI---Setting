#function to create the chatbot
def chatbot():
    print("Chatbot:Hello there, I am a simple chatbot,type exit to quit")
    while True:
        user_input=input("You:").lower()
        if user_input=="exit":
            print("Chatbot:exiting.....Goodbye!")
            break#stop loop from execution
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot:Hi there,how may i assist you?")
        elif "name" in user_input:
            print("Chatbot:My name is ChatPy!Am just a simple chatbot")
        elif "age" in user_input:
            print("Chatbot:I am 12 years old")
        elif "dob" in user_input:
            print("Chatbot:I was born in 2012")
        elif "hobby" in user_input:
            print("Chatbot:I like editing,drawing and playing Roblox")
        elif "food" in user_input:
            print("Chatbot:I like chocolte oat biscuits")
        elif "drink" in user_input:
            print("Chatbot:I don't have any particular drink i like,but i do like drinking hot green tea")
        elif "anime" in user_input:
            print("Chatbot:My favorite Shoenen anime is JJk(JuJutsu Kaisen) and I also like Horimiya")
        else:
            print("Chatbot:I am not yet configured to help with that.")
#run the main funcion
chatbot()