import random
import streamlit as st

def gamewin (comp, you):
#If two values are equal, declare a tie!
    if comp == you:
        return None

# Check for all possibilities when computer chose s
    elif comp == "stone 🌑":
        if you == "scissor ✂":
            return False 
        elif you == "paper 📃":
            return True

# Check for all possibilities when computer chose w 
    elif comp == "paper 📃":
        if you == "stone 🌑":
            return False 
        elif you == "scissor ✂":
            return True

# Check for all possibilities when computer chose g            
    elif comp == "scissor ✂":
        if you == "paper 📃":
            return False 
        elif you == "stone 🌑":
            return True
        
def main():
    st.title("STONE PAPER SCISSOR")

    compturn = random.randint(1, 3)
    if compturn == 1:
        comp = "stone 🌑"
    elif compturn == 2:
        comp = "paper 📃"
    elif compturn == 3:
        comp = "scissor ✂"
    else:
        comp = None

    your = st.form("Choose Here: stone (st) paper (pa) scissor (sc)")
    you= st.selectbox('your turn',('stone 🌑','paper 📃','scissor ✂'))
    #if your == "st":
        #you = "stone"
    #elif your == "pa":
        #you = "paper"
    #elif your == "sc":
        #you = "scissor"

    st.write(f"Computer chose: {comp}")
    #st.write(f"YOU chose: {you}")

    result = gamewin(comp, you)
    if result == None:
        st.subheader("TIE")
    elif result == True:
        st.subheader("🥳🥳YOU WON")
    else:
        st.subheader("YOU LOST🤣🤣")
    #elif you == "choose between stone, paper, scissor":
        #st.write("Choose between stone, paper, scissor")


if __name__ == "__main__":
    main()

