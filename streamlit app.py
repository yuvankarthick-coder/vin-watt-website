
import streamlit as st
from urllib.parse import quote

# --------------------------------------------------
# VIN-WATT | Premium Clean Energy Website
# Company: Vintechnologies
# No API keys or paid backend required
# --------------------------------------------------

st.set_page_config(
    page_title="VIN-WATT | Sustainable Charging Solutions",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

COMPANY = "Vintechnologies"
BRAND = "VIN-WATT"
PHONE = "9842159555"
WHATSAPP = "919842159555"
EMAIL = "vintechmdu@gmail.com"
ADDRESS = (
    "374, Pandeeswari Complex, Sarveshwarar Koil Street, "
    "Anna Nagar, Madurai - 625020, Tamil Nadu, India"
)
TAGLINE = "Sustainable Charging Solutions for the Road Ahead."

HERO_IMAGE = (
    "https://images.unsplash.com/photo-1593941707882-a5ba14938c7"
    "?auto=format&fit=crop&w=2000&q=85"
)
EV_IMAGE = (
    "https://images.unsplash.com/photo-1593941707882-a5ba14938c7"
    "?auto=format&fit=crop&w=1000&q=85"
)
SOLAR_IMAGE = (
    "https://images.unsplash.com/photo-1509391366360-2e959784a276"
    "?auto=format&fit=crop&w=1000&q=85"
)
ENERGY_IMAGE = (
    "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e"
    "?auto=format&fit=crop&w=1600&q=85"
)

st.markdown(
    """
    <meta name="theme-color" content="#103c30">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

    :root {
        --green: #103c30;
        --green-dark: #09291f;
        --lime: #c6f36b;
        --ink: #14251f;
        --muted: #66756e;
        --paper: #f7f8f4;
        --line: #e5eae3;
    }

    html { scroll-behavior: smooth; }
    .stApp {
        background: var(--paper);
        color: var(--ink);
        font-family: 'DM Sans', sans-serif;
    }
    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stToolbar"] { right: 1rem; }
    .block-container {
        max-width: 1240px;
        padding: 1.4rem 2rem 3rem;
    }
    h1, h2, h3, h4 {
        font-family: 'Manrope', sans-serif !important;
        letter-spacing: -0.045em;
        color: var(--ink);
    }
    p, li { line-height: 1.7; }
    a { text-decoration: none; }

    /* Brand header */
    .brandbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
        padding: 8px 0 22px;
        border-bottom: 1px solid var(--line);
        margin-bottom: 28px;
    }
    .brandmark {
        font-family: 'Manrope', sans-serif;
        font-size: 1.65rem;
        font-weight: 800;
        letter-spacing: -0.06em;
        color: var(--green);
    }
    .brandmark span { color: #76a934; }
    .brandtag {
        color: var(--muted);
        font-size: .76rem;
        letter-spacing: .12em;
        text-transform: uppercase;
        font-weight: 700;
    }
    .navlinks {
        display: flex;
        flex-wrap: wrap;
        gap: 22px;
        justify-content: flex-end;
        font-size: .88rem;
        font-weight: 600;
    }
    .navlinks a { color: var(--ink); }
    .navlinks a:hover { color: #60952d; }

    /* Hero */
    .hero {
        background:
          linear-gradient(90deg, rgba(5,31,23,.96) 0%,
          rgba(5,31,23,.84) 48%, rgba(5,31,23,.12) 100%),
          url("HERO_REPLACE") center / cover no-repeat;
        background-color: var(--green-dark);
        min-height: 490px;
        border-radius: 24px;
        padding: clamp(28px, 5vw, 68px);
        display: flex;
        align-items: center;
        overflow: hidden;
        color: white;
    }
    .hero-content { max-width: 670px; }
    .eyebrow {
        text-transform: uppercase;
        letter-spacing: .18em;
        font-size: .73rem;
        font-weight: 700;
        color: var(--lime);
        margin-bottom: 18px;
    }
    .hero h1 {
        color: white !important;
        font-size: clamp(2.6rem, 5.5vw, 5rem);
        line-height: 1.04;
        margin: 0 0 22px;
        font-weight: 800;
    }
    .hero p {
        color: rgba(255,255,255,.82);
        font-size: 1.05rem;
        max-width: 550px;
        margin-bottom: 28px;
    }
    .hero-cta {
        display: inline-block;
        padding: 14px 21px;
        background: var(--lime);
        color: var(--green-dark) !important;
        border-radius: 8px;
        font-weight: 800;
        font-size: .92rem;
    }
    .hero-cta:hover { background: #d8ff91; }

    /* Sections and cards */
    .section-kicker {
        color: #5b8b35;
        text-transform: uppercase;
        letter-spacing: .15em;
        font-size: .73rem;
        font-weight: 800;
        margin-bottom: 9px;
    }
    .section-heading {
        font-size: clamp(2rem, 3.5vw, 3.1rem);
        line-height: 1.12;
        margin: 0 0 14px;
    }
    .section-copy {
        color: var(--muted);
        max-width: 680px;
        margin-bottom: 24px;
    }
    .product-card {
        background: white;
        border: 1px solid var(--line);
        border-radius: 18px;
        overflow: hidden;
        height: 100%;
    }
    .product-card img {
        width: 100%;
        height: 220px;
        object-fit: cover;
        display: block;
    }
    .product-body { padding: 23px; }
    .product-label {
        color: #5b8b35;
        text-transform: uppercase;
        letter-spacing: .13em;
        font-size: .69rem;
        font-weight: 800;
    }
    .product-body h3 {
        font-size: 1.4rem;
        margin: 10px 0;
    }
    .product-body p {
        color: var(--muted);
        font-size: .94rem;
    }
    .text-link {
        display: inline-block;
        color: var(--green);
        font-weight: 800;
        margin-top: 6px;
    }
    .feature-panel {
        background: var(--green);
        color: white;
        padding: clamp(25px, 4vw, 46px);
        border-radius: 20px;
    }
    .feature-panel h2 { color: white !important; }
    .feature-panel p { color: rgba(255,255,255,.76); }
    .feature-item {
        border-top: 1px solid rgba(255,255,255,.2);
        padding: 16px 0;
    }
    .feature-item strong { color: white; }
    .number {
        font-family: 'Manrope', sans-serif;
        font-size: 1.6rem;
        font-weight: 800;
        color: var(--lime);
        margin-bottom: 5px;
    }
    .contact-panel {
        background: white;
        border: 1px solid var(--line);
        border-radius: 20px;
        padding: clamp(22px, 4vw, 42px);
    }
    .contact-line {
        padding: 13px 0;
        border-bottom: 1px solid var(--line);
        overflow-wrap: anywhere;
    }
    .contact-line:last-child { border-bottom: 0; }
    .contact-line strong {
        display: block;
        margin-bottom: 4px;
    }
    .contact-line span { color: var(--muted); font-size: .92rem; }
    .footer {
        margin-top: 38px;
        border-top: 1px solid var(--line);
        padding: 24px 0 8px;
        color: var(--muted);
        font-size: .82rem;
    }

    /* Streamlit controls */
    div.stButton > button, div.stLinkButton > a,
    div[data-testid="stFormSubmitButton"] > button {
        border-radius: 8px !important;
        min-height: 46px;
        font-weight: 700 !important;
    }
    div.stButton > button[kind="primary"],
    div[data-testid="stFormSubmitButton"] > button[kind="primary"] {
        background: var(--green) !important;
        border-color: var(--green) !important;
        color: white !important;
    }
    div.stLinkButton > a {
        background: var(--green) !important;
        border-color: var(--green) !important;
        color: white !important;
    }
    input, textarea {
        border-radius: 8px !important;
    }
    [data-testid="stForm"] {
        border: 0;
        padding: 0;
    }
    @media (max-width: 700px) {
        .block-container { padding: 1rem 1rem 2rem; }
        .brandbar { align-items: flex-start; flex-direction: column; }
        .navlinks { justify-content: flex-start; gap: 14px; }
        .hero { min-height: 440px; border-radius: 16px; }
        .hero h1 { font-size: 2.65rem; }
        .hero p { font-size: .97rem; }
        .product-card img { height: 190px; }
    }
    </style>
    """.replace("HERO_REPLACE", HERO_IMAGE),
    unsafe_allow_html=True,
)

# Header
st.markdown(
    """
    <div class="brandbar">
      <div>
        <div class="brandmark">VIN<span>•</span>WATT</div>
        <div class="brandtag">A Vintechnologies brand</div>
      </div>
      <div class="navlinks">
        <a href="#solutions">Solutions</a>
        <a href="#about">Why VIN-WATT</a>
        <a href="#contact">Contact</a>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Hero
st.markdown(
    f"""
    <section class="hero">
      <div class="hero-content">
        <div class="eyebrow">Powering a cleaner tomorrow</div>
        <h1>Move forward.<br>Charge smarter.</h1>
        <p>{TAGLINE} Explore EV charging and solar energy solutions
        designed to support a more connected, energy-conscious future.</p>
        <a class="hero-cta" href="#solutions">Explore our solutions&nbsp; ↗</a>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.write("")

# Intro
st.markdown(
    """
    <div id="solutions" class="section-kicker">Our solutions</div>
    <h2 class="section-heading">Clean energy, made practical.</h2>
    <p class="section-copy">
      From electric mobility to solar power, VIN-WATT brings together
      forward-looking energy solutions for homes, businesses and projects.
      Contact our team to discuss the right setup for your requirements.
    </p>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns(2, gap="large")

with left:
    st.markdown(
        f"""
        <div class="product-card">
          <img src="{EV_IMAGE}" alt="Electric vehicle charging solution">
          <div class="product-body">
            <div class="product-label">01 / Electric mobility</div>
            <h3>EV charging solutions</h3>
            <p>Explore charging solutions for residential, commercial
            and workplace requirements. Ask our team about suitable
            charger types and installation needs.</p>
            <a class="text-link" href="#contact">Enquire about EV charging ↗</a>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        f"""
        <div class="product-card">
          <img src="{SOLAR_IMAGE}" alt="Solar energy panels">
          <div class="product-body">
            <div class="product-label">02 / Solar energy</div>
            <h3>Solar power solutions</h3>
            <p>Discuss rooftop solar and clean-energy options for your
            home or business, based on your site and energy requirements.</p>
            <a class="text-link" href="#contact">Enquire about solar ↗</a>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")
st.write("")

# About / benefits
st.markdown(
    """
    <div id="about" class="feature-panel">
      <div class="section-kicker">The VIN-WATT approach</div>
      <h2 class="section-heading">Built around your energy needs.</h2>
      <p>We focus on practical conversations, clear product information
      and solutions aligned with each customer's requirements.</p>
      <div class="feature-item">
        <strong>01 — Understand</strong><br>
        Tell us about your home, business, vehicle or project.
      </div>
      <div class="feature-item">
        <strong>02 — Explore</strong><br>
        Discuss available products and possible configurations with our team.
      </div>
      <div class="feature-item">
        <strong>03 — Connect</strong><br>
        Get in touch directly to discuss the next steps for your enquiry.
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.write("")

# Brand statement
st.markdown(
    f"""
    <div style="
      border-radius:18px;
      padding:32px;
      background:#edf1e8;
      background-image:linear-gradient(90deg,rgba(237,241,232,.97),
      rgba(237,241,232,.86)),url('{ENERGY_IMAGE}');
      background-position:center;
      background-size:cover;">
      <div class="section-kicker">Our purpose</div>
      <h2 class="section-heading" style="max-width:750px;">
        Better energy choices begin with a conversation.
      </h2>
      <p class="section-copy" style="margin-bottom:0;">
        VIN-WATT by Vintechnologies — here to help you explore
        charging and solar solutions for the road ahead.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.write("")

# Contact and enquiry
st.markdown(
    """
    <div id="contact" class="section-kicker">Let's connect</div>
    <h2 class="section-heading">Tell us what you need.</h2>
    <p class="section-copy">
      Share a few details below. Your enquiry will be prepared as a
      WhatsApp message for you to review and send.
    </p>
    """,
    unsafe_allow_html=True,
)

contact_col, form_col = st.columns([0.9, 1.1], gap="large")

with contact_col:
    st.markdown(
        f"""
        <div class="contact-panel">
          <div class="brandmark">VIN<span>•</span>WATT</div>
          <p style="color:#66756e;">{COMPANY}</p>
          <div class="contact-line">
            <strong>Call us</strong>
            <span>{PHONE}</span>
          </div>
          <div class="contact-line">
            <strong>Email</strong>
            <span>{EMAIL}</span>
          </div>
          <div class="contact-line">
            <strong>Visit us</strong>
            <span>{ADDRESS}</span>
          </div>
          <div class="contact-line">
            <strong>Our promise</strong>
            <span>{TAGLINE}</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    st.link_button(
        "Chat with VIN-WATT on WhatsApp",
        f"https://wa.me/{WHATSAPP}?text={quote('Hello VIN-WATT, I would like to know more about your EV charging and solar solutions.')}",
        use_container_width=True,
    )
    st.link_button(
        "Call VIN-WATT",
        f"tel:+91{PHONE}",
        use_container_width=True,
    )
    st.link_button(
        "Email VIN-WATT",
        f"mailto:{EMAIL}",
        use_container_width=True,
    )

with form_col:
    st.markdown('<div class="contact-panel">', unsafe_allow_html=True)
    with st.form("vinwatt_enquiry_form", clear_on_submit=False):
        customer_name = st.text_input(
            "Your name *",
            placeholder="Enter your name",
        )
        customer_phone = st.text_input(
            "Your phone number *",
            placeholder="Enter your contact number",
        )
        enquiry_type = st.selectbox(
            "What are you interested in?",
            [
                "EV charging solution",
                "Solar energy solution",
                "EV charging + solar",
                "Business or dealership enquiry",
                "Other enquiry",
            ],
        )
        customer_location = st.text_input(
            "Your city / location",
            placeholder="e.g. Madurai",
        )
        customer_message = st.text_area(
            "Tell us about your requirement",
            placeholder="Share your project details or questions...",
            height=120,
        )
        submitted = st.form_submit_button(
            "Prepare WhatsApp enquiry ↗",
            use_container_width=True,
            type="primary",
        )

    if submitted:
        if not customer_name.strip() or not customer_phone.strip():
            st.warning("Please enter your name and phone number.")
        else:
            message = (
                "Hello VIN-WATT / Vintechnologies,\n\n"
                "I would like to make an enquiry.\n\n"
                f"Name: {customer_name.strip()}\n"
                f"Phone: {customer_phone.strip()}\n"
                f"Interest: {enquiry_type}\n"
                f"Location: {customer_location.strip() or 'Not provided'}\n"
                f"Requirement: {customer_message.strip() or 'Not provided'}\n\n"
                "Please contact me with more details."
            )
            whatsapp_url = (
                f"https://wa.me/{WHATSAPP}?text={quote(message)}"
            )
            st.success(
                "Your message is ready. Open WhatsApp and press Send "
                "to submit your enquiry."
            )
            st.link_button(
                "Open WhatsApp and review message",
                whatsapp_url,
                use_container_width=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown(
    f"""
    <div class="footer">
      <strong style="color:#103c30;">VIN•WATT</strong> &nbsp;|&nbsp;
      {COMPANY}<br>
      {TAGLINE}<br><br>
      © {2026} Vintechnologies. All rights reserved.
      <br>
      <span style="font-size:.75rem;">
        Product and background images are illustrative.
        Confirm product specifications, availability and installation
        requirements with our team.
      </span>
    </div>
    """,
    unsafe_allow_html=True,
)
