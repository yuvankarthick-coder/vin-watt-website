import streamlit as st

st.set_page_config(
    page_title="VIN-WATT | Clean Energy",
    page_icon="⚡",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #f5f8f5;
}
h1, h2, h3 {
    color: #14532d;
}
.hero {
    background: linear-gradient(120deg, #052e16, #166534);
    padding: 35px 20px;
    border-radius: 16px;
    color: white;
}
.hero h1, .hero p {
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>VIN-WATT</h1>
    <p>Sustainable Charging Solutions for the Road Ahead.</p>
    <p>Smarter EV Charging. Cleaner Energy. Brighter Future.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

st.header("Our Solutions")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("⚡ EV Charging")
    st.write("Charging solutions for homes, businesses and workplaces.")

with col2:
    st.subheader("☀️ Solar Energy")
    st.write("Explore solar energy solutions for a cleaner future.")

with col3:
    st.subheader("🔋 Charging Infrastructure")
    st.write("Solutions for EV charging installations and businesses.")

st.divider()

st.header("About Vintechnologies")
st.write(
    "We work towards smarter electric mobility "
    "and sustainable energy solutions."
)

st.header("Contact Us")

st.write("**Vintechnologies**")
st.write("374, Pandeeswari Complex,")
st.write("Sarveshwarar Koil Street, Anna Nagar,")
st.write("Madurai - 625020, Tamil Nadu")

st.write("Phone: 9842159555")
st.write("Email: vintechmdu@gmail.com")

with st.form("enquiry_form"):
    name = st.text_input("Your name")
    email = st.text_input("Your email")
    message = st.text_area("How can we help?")
    submitted = st.form_submit_button("Submit enquiry")

    if submitted:
        if name.strip() and email.strip() and message.strip():
            st.success(
                "Thank you! Your form is ready, "
                "but this demo does not send enquiries yet."
            )
        else:
            st.warning("Please fill in all fields.")

