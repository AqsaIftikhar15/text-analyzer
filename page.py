import streamlit as st

st.set_page_config(
    page_title="Text Analyzer",
    page_icon="🤖",
)

st.title("Text Analyzer")

if 'let' not in st.session_state:
    st.session_state.let = ""
if 'now' not in st.session_state:
    st.session_state.now = ""
if 'mode' not in st.session_state:
    st.session_state.mode = "analyze"


let = st.text_area("Enter the paragraph you want to analyze below:", value=st.session_state.now or st.session_state.let)

if not st.session_state.let and let:
    st.session_state.let = let

but1 = st.button("Analyze Now")
but2 = st.button("Search and Replace")
but3 = st.button("Case Conversion")

if but1: st.session_state.mode = "analyze"
if but2: st.session_state.mode = "replace"
if but3: st.session_state.mode = "case"


if st.session_state.mode == "analyze":
    if let != "":
        word = len(let.split())
        charac = len(let)
        vowels = "AEIOUaeiou"
        vowel_count = sum(1 for char in let if char in vowels)
        
        st.success(f"The total word count for the given text is: {word}")
        st.success(f"The total character count for the given text is: {charac}")
        st.success(f"The total vowel count for the given text is: {vowel_count}")
    else:
        st.error("Enter some text")


elif st.session_state.mode == "replace":
    if let != "":
        with st.form("replace_form"):
            search = st.text_input("Enter word to search:", key="search")
            replace = st.text_input("Enter replacement word:", key="replace")
            submitted = st.form_submit_button("Replace Now")
            
            if submitted:
                if search and replace:
                    st.session_state.now = let.replace(search, replace)
                    st.session_state.let = st.session_state.now  
                    st.success(f"The word {search} replaced with {replace} ✅")
                    st.write(f"Modified text is : {st.session_state.now}")
                else:
                    st.error("Both fields are required!")
    else:
        st.error("Enter some text")


elif st.session_state.mode == "case":
    if let != "":
        with st.form("case_form"):
            case = st.selectbox("Select Case Conversion:", ["Upper Case", "Lower Case"], key="case_select")
            submitted = st.form_submit_button("Convert Now")
            if submitted:
                if case == "Upper Case":
                    st.session_state.now = let.upper()
                else:
                    st.session_state.now = let.lower()
                st.session_state.let = st.session_state.now 
                st.success(f"Text converted to {case}: {st.session_state.now}")
    else:
        st.error("Enter some text")



st.write("---")
st.write("Created by: Aqsa Iftikhar ")
