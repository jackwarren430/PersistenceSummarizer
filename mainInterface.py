import streamlit as st

#Title & Description
st.markdown(f"""
    <div "padding: 0px; border-radius: 5px;">
        <h1 style="color: #7851a9">Terms of Service Translator</h1>
        <p>Welcome to our Hackalytics submission. This project aims to summarize and highlight important sections on terms of service documents so that people actually know what they are signing up for. Simply copy and paste the terms of service into the box below and press enter!</p>
    </div>
""", unsafe_allow_html=True)
st.write("")
st.write("")


#Functions
#Makes API call to LLM with txt as input
def mainAPICall(txt):
	#Add code later
	primaryOutput = ["Placeholder", "Placeholder"]
	return primaryOutput

#Makes API call to LLM with txt as input to return the expansion details
def helperAPICall(txt):
	#add code later
	return "Placeholder"

#Makes API call to LLM for expansion and adds expansionText to expansion box
def expansionText(sectionsArray):
	expansionDetails = []

	for i, section in enumerate(sectionsArray):
		st.write(section)
		if(i == 0):
			st.write("")
			st.write("")
			continue

		with st.expander(f"More on this ({i + 1})"):
			expansionDetails.append(f"{i + 1}. {helperAPICall('')}")
			st.write(expansionDetails[i - 1])

		st.write("")
		st.write("")


mainInput = st.text_area('Enter your terms of service here: ', '', height=500, key="text_area")

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

if(mainInput.strip()):
	st.markdown(f"""
	    <div "padding: 0px; border-radius: 5px;">
	        <h2 style="color: #7851a9">Terms of Service Translator</h2>
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
st.write("Developed by Jack Warren and James Li")

	
