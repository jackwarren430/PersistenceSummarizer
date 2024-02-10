import streamlit as st
from pdfminer.high_level import extract_text
import io

#Title & Description
st.markdown("""
    <div style="padding: 0px; border-radius: 5px;">
        <h1 style="color: #7851a9; font-size: 60px;">Terms of Service Translator</h1>
        <p>Welcome to our Hackalytics submission. This project aims to summarize and highlight important sections on terms of service documents so that people actually know what they are signing up for. Simply copy and paste the terms of service into the box below and press enter!</p>
        <hr> <!---->
    </div>
""", unsafe_allow_html=True)

#Functions
#Makes API call to LLM with txt as input
def mainAPICall(txt):
	#Add code later
	primaryOutput = [["Summary", ''], ["Section1", "Expansion1"], ["Section2", "Expansion2"], ["Section3", "Expansion3"]]
	#primaryOutput.append(["New", 'lol'])
	return primaryOutput

#Makes API call to LLM for expansion and adds expansionText to expansion box
def expansionText(sectionsArray):
	expansionDetails = []

	for i, section in enumerate(sectionsArray):
		st.write(section[0])
		if(i == 0):
			st.write("")
			st.write("")
			continue

		with st.expander(f"More on this section ({i})"):
			expansionDetails.append(f"{i}. {section[1]}")
			st.write(expansionDetails[i - 1])

		st.write("")
		st.write("")


mainInput = st.text_area('Enter your terms of service here: ', '', height=500, key="text_area")

# Upload PDF file
pdf_file = st.file_uploader("Or upload a PDF version here:", type=["pdf"])
pdf_text = ""
pdf_success = False
if pdf_file is not None:
    # Convert to bytes
    bytes_data = pdf_file.getvalue()

    # Use bytes data to create a BytesIO object
    pdf_bio = io.BytesIO(bytes_data)

    # Extract text from PDF
    try:
        pdf_text = extract_text(pdf_bio)
        pdf_success = True
        #APIoutput = mainAPICall(pdf_text)

    except Exception as e:
        pdf_text = (f"An error occurred while processing the PDF file. {e}")
        pdf_success = False

if(mainInput.strip() and not pdf_success):
	st.write("")
	st.write("")
	st.write("")
	st.write("")
	st.write("")
	st.markdown(f"""
	    <div "padding: 0px; border-radius: 5px;">
	        <h2 style="color: #7851a9">TOS Translated</h2>
	    </div>
	""", unsafe_allow_html=True)
	APIoutput = mainAPICall(mainInput) #Location of main API call
	if(len(APIoutput) == 1):
		st.write("The following is a summary of the Terms of Service")
	else:
		st.write("The following is a summary of the Terms of Service and its notable sections: ")
	st.write("")
	expansionText(APIoutput)
	st.write("")
	st.write("")
	st.write("")
	st.write("")
	st.write("")
elif(pdf_success):
	st.write("")
	st.write("")
	st.write("")
	st.write("")
	st.write("")
	st.markdown(f"""
	    <div "padding: 0px; border-radius: 5px;">
	        <h2 style="color: #7851a9">TOS Translated</h2>
	    </div>
	""", unsafe_allow_html=True)
	APIoutput = mainAPICall(pdf_text) #Location of main API call
	if(len(APIoutput) == 1):
		st.write("The following is a summary of the Terms of Service")
	else:
		st.write("The following is a summary of the Terms of Service and its notable sections: ")
	st.write("")
	expansionText(APIoutput)
	st.write("")
	st.write("")
	st.write("")
	st.write("")
	st.write("")

st.markdown(f"""
	    <div "padding: 0px; border-radius: 5px;">
	        <hr><!---->
	    </div>
	""", unsafe_allow_html=True)
st.write("Developed by Jack Warren and James Li")

	
