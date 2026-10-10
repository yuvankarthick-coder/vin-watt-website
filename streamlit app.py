
import streamlit as st

st.set_page_config(
    page_title="VIN-WATT | EV & Solar Solutions",
    page_icon="⚡",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #f7faf7;
    color: #183b2a;
}
.block-container {
    max-width: 1150px;
    padding-top: 2rem;
}
.hero {
    background: linear-gradient(135deg, #092e1b, #187044);
    padding: 45px 28px;
    border-radius: 22px;
    color: white;
}
.hero h1 {
    color: white;
    font-size: clamp(2.5rem, 6vw, 4.5rem);
    margin-bottom: 8px;
}
.hero p {
    color: #e1f5e8;
    font-size: 1.1rem;
}
.card {
    background: white;
    padding: 24px;
    border: 1px solid #e0ebe2;
    border-radius: 16px;
    min-height: 190px;
}
.eyebrow {
    color: #83d6a0;
    font-weight: 700;
    letter-spacing: 2px;
}
.stButton > button,
.stLinkButton > a {
    background: #17683b;
    color: white;
    border-radius: 9px;
    border: 0;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="hero">
    <div class="eyebrow">CLEAN ENERGY • SMART MOBILITY</div>
    <h1>VIN-WATT</h1>
    <p>Sustainable Charging Solutions for the Road Ahead.</p>
    <p>Smarter EV Charging. Cleaner Energy. Brighter Future.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# Main call to action
left, right = st.columns([2, 1])
with left:
    st.header("Powering a cleaner tomorrow")
    st.write(
        "Explore electric vehicle charging and solar energy "
        "solutions for homes, businesses and charging locations."
    )
with right:
    st.write("")
    st.link_button(
        "Contact Our Team",
        "mailto:vintechmdu@gmail.com"
    )

st.divider()
st.header("Our Solutions")
st.caption("Smart solutions for electric mobility and clean energy.")

a, b, c = st.columns(3)

with a:
    st.markdown("""
    <div class="card">
    <h2>⚡</h2>
    <h3>EV Chargers</h3>
    <p>Charging solutions for homes, workplaces and businesses.</p>
    </div>
    """, unsafe_allow_html=True)

with b:
    st.markdown("""
    <div class="card">
    <h2>☀️</h2>
    <h3>Solar Energy</h3>
    <p>Explore rooftop solar and clean-energy solutions.</p>
    </div>
    """, unsafe_allow_html=True)

with c:
    st.markdown("""
    <div class="card">
    <h2>🔌</h2>
    <h3>Charging Infrastructure</h3>
    <p>Solutions for EV charging installations and locations.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.divider()

st.header("Why VIN-WATT?")
x, y, z = st.columns(3)
x.markdown("### 🌱 Clean Energy\nSolutions for a more sustainable future.")
y.markdown("### 🏢 Business Solutions\nOptions for residential and commercial needs.")
z.markdown("### 🤝 Customer Support\nContact our team to discuss your requirements.")

st.divider()
st.header("About Vintechnologies")
st.write(
    "Vintechnologies focuses on electric mobility and "
    "sustainable energy solutions through the VIN-WATT brand."
)

st.header("Let's Talk About Your Project")
st.write("Contact us for product details, installation enquiries and business discussions.")

st.link_button("📞 Call Vintechnologies", "tel:+919842159555")
st.link_button(
    "✉️ Email Us",
    "mailto:vintechmdu@gmail.com?subject=VIN-WATT%20Enquiry"
)

st.markdown("""
**Vintechnologies**  
374, Pandeeswari Complex, Sarveshwarar Koil Street,  
Anna Nagar, Madurai - 625020, Tamil Nadu, India
""")

st.caption(
    "VIN-WATT | Sustainable Charging Solutions for the Road Ahead."
)
