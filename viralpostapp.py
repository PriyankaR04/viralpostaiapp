import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="AI Viral Post Generator",
    page_icon="🌐",
    layout="centered",

)

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception as e:
    st.error("API key error...Please check your api key")


st.title("AI Viral Post Generator")
st.markdown("----------------")

st.write("Enter your topic and get a viral post")
topic = st.text_area("What is your post about?", placeholder="Ex: My first day learning AI with python")
language = st.selectbox("Select language", ["English","Tamil","Hindi"])

col1, col2, col3 = st.columns([1,2,1])

with col2:
    generate_btn = st.button("Generate viral post",type="primary",use_container_width=True)

if generate_btn:
    if not topic.strip():
        st.warning("Please enter a topic")
    else:
        with st.spinner("AI is thinking..."):

            prompt = f"""
            Act as a professional social media influencer
            write an engaging,viral linkedin/instagram post about : `{topic}`
            
            STRICT REQUIREMENT: Write the post in **{language}**
            
            Rules:
            1. Start with a catchy Hook/Headline
            3. Include relevant emojis
            4. End with a question to audience
            5. Add 5 trending hashtags
"""
            try:
                chat_completion= client.chat.completions.create(
                    messages=[
                        {"role":"user","content": prompt}
                    ],
                    model = "llama-3.3-70b-versatile"
                )

                ai_response = chat_completion.choices[0].message.content

                st.balloons()
                st.success("Your viral post is ready")
                st.markdown(ai_response)
                st.info("Tip: copy this and post it on your linkedin/instagram")

            except Exception as e:
                st.error(f"Error: {e}")

