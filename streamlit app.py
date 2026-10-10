
import streamlit as st
from urllib.parse import quote
from datetime import datetime

# =====================================================
# VIN-WATT | Premium Clean Energy Website
# Company: Vintechnologies
# WhatsApp enquiries only - no API keys required
# =====================================================

st.set_page_config(
    page_title="VIN-WATT | Clean Energy Solutions",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BRAND = "VIN-WATT"
COMPANY = "Vintechnologies"
PHONE = "9842159555"
WHATSAPP = "919842159555"
EMAIL = "vintechmdu@gmail.com"
ADDRESS = (
    "374, Pandeeswari Complex, Sarveshwarar Koil Street, "
    "Anna Nagar, Madurai - 625020, Tamil Nadu, India"
)
TAGLINE = "Sustainable Charging Solutions for the Road Ahead."

EV_IMAGE = (
    "https://images.unsplash.com/photo-1593941707882-a5ba14938c7"
    "?auto=format&fit=crop&w=1200&q=85"
)
SOLAR_IMAGE = (
    "https://images.unsplash.com/photo-1509391366360-2e959784a276"
    "?auto=format&fit=crop&w=1200&q=85"
)
CLEAN_ENERGY_IMAGE = (
    "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e"
    "?auto=format&fit=crop&w=1600&q=85"
)

# IMPORTANT: All website CSS is inside this <style> block.
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

    :root {
        --green: #103c30;
        --deep-green: #08271e;
        --lime: #c8f36a;
        --ink: #17251f;
        --muted: #68766e;
        --paper: #f6f8f3;
        --line: #e3e9e1;
    }

    html { scroll-behavior: smooth; }

    .stApp {
        background: var(--paper);
        color: var(--ink);
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        max-width: 1240px;
        padding: 1.5rem 2rem 3rem;
    }

    h1, h2, h3, h4 {
        font-family: 'Manrope', sans-serif !important;
        color: var(--ink);
        letter-spacing: -0.04em;
    }

    p {
        line-height: 1.7;
    }

    a {
        text-decoration: none !important;
    }

    .brandbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
        flex-wrap: wrap;
        padding: 8px 0 22px;
        margin-bottom: 26px;
        border-bottom: 1px solid var(--line);
    }

    .brand-logo {
        font-family: 'Manrope', sans-serif;
        font-weight: 800;
        font-size: 1.8rem;
        letter-spacing: -0.07em;
        color: var(--green);
        line-height: 1.1;
    }

    .brand-logo span {
        color: #7ba83b;
    }

    .brand-caption {
        font-size: .72rem;
        letter-spacing: .12em;
        text-transform: uppercase;
        color: var(--muted);
        margin-top: 5px;
    }

    .navlinks {
        display: flex;
        flex-wrap: wrap;
        gap: 22px;
        font-size: .9rem;
        font-weight: 700;
    }

    .navlinks a {
        color: var(--ink);
    }

    .navlinks a:hover {
        color: #628e35;
    }

    .hero {
        background:
          linear-gradient(90deg, rgba(5,31,23,.95),
          rgba(5,31,23,.77) 55%, rgba(5,31,23,.25)),
          url("https://images.unsplash.com/photo-1593941707882-a5ba14938c7?auto=format&fit=crop&w=1800&q=85");
        background-color: var(--deep-green);
        background-size: cover;
        background-position: center;
        color: white;
        min-height: 460px;
        border-radius: 22px;
        padding: clamp(28px, 5vw, 65px);
        display: flex;
        align-items: center;
        overflow: hidden;
    }

    .hero-content {
        max-width: 690px;
    }

    .eyebrow {
        color: var(--lime);
        font-size: .75rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: .17em;
        margin-bottom: 18px;
    }

    .hero h1 {
        color: #ffffff !important;
        font-size: clamp(2.8rem, 6vw, 5.2rem);
        line-height: 1.03;
        margin: 0 0 22px;
        font-weight: 800;
    }

    .hero p {
        color: rgba(255,255,255,.85);
        max-width: 570px;
        font-size: 1.04rem;
        margin-bottom: 28px;
    }

    .hero-button {
        display: inline-block;
        background: var(--lime);
        color: var(--deep-green) !important;
        padding: 14px 22px;
        border-radius: 8px;
        font-weight: 800;
    }

    .section {
        padding-top: 42px;
        padding-bottom: 18px;
    }

    .kicker {
        color: #628e35;
        font-size: .73rem;
        font-weight: 800;
        letter-spacing: .16em;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .section-title {
        font-size: clamp(2rem, 4vw, 3.15rem);
        line-height: 1.12;
        margin: 0 0 14px;
    }

    .section-description {
        color: var(--muted);
        max-width: 700px;
        margin-bottom: 24px;
    }

    .product-card {
        background: white;
        border: 1px solid var(--line);
        border-radius: 17px;
        overflow: hidden;
        height: 100%;
    }

    .product-card img {
        display: block;
        width: 100%;
        height: 225px;
        object-fit: cover;
    }

    .product-content {
        padding: 23px;
    }

    .product-tag {
        color: #628e35;
        font-size: .7rem;
        font-weight: 800;
        letter-spacing: .12em;
        text-transform: uppercase;
    }

    .product-content h3 {
        font-size: 1.5rem;
        margin: 10px 0;
    }

    .product-content p {
        color: var(--muted);
        font-size: .94rem;
    }

    .product-link {
        display: inline-block;
        color: var(--green) !important;
        font-weight: 800;
        margin-top: 8px;
    }

    .dark-panel {
        background: var(--green);
        color: white;
        padding: clamp(25px, 4vw, 46px);
        border-radius: 20px;
        margin-top: 42px;
    }

    .dark-panel h2 {
        color: white !important;
    }

    .dark-panel p {
        color: rgba(255,255,255,.78);
    }

    .dark-panel .kicker {
        color: var(--lime);
    }

    .benefit {
        border-top: 1px solid rgba(255,255,255,.2);
        padding: 16px 0;
        color: rgba(255,255,255,.82);
    }

    .benefit strong {
        color: white;
    }

    .contact-card {
        background: white;
        border: 1px solid var(--line);
        border-radius: 18px;
        padding: 26px;
        height: 100%;
    }

    .contact-row {
        padding: 14px 0;
        border-bottom: 1px solid var(--line);
        overflow-wrap: anywhere;
    }

    .contact-row:last-child {
        border-bottom: 0;
    }

    .contact-row strong {
        display: block;
        margin-bottom: 5px;
    }

    .contact-row span {
        color: var(--muted);
        font-size: .92rem;
    }

    .note {
        color: var(--muted);
        font-size: .82rem;
    }

    .footer {
        border-top: 1px solid var(--line);
        margin-top: 42px;
        padding: 24px 0 8px;
        color: var(--muted);
        font-size: .83rem;
    }

    div.stButton > button,
    div.stLinkButton > a,
    div[data-testid="stFormSubmitButton"] > button {
        border-radius: 8px !important;
        min-height: 45px;
        font-weight: 700 !important;
    }

    div.stButton > button[kind="primary"],
    div[data-testid="stFormSubmitButton"] > button[kind="primary"] {
        background: var(--green) !important;
        color: white !important;
        border-color: var(--green) !important;
    }

    div.stLinkButton > a {
        background: var(--green) !important;
        color: white !important;
        border-color: var(--green) !important;
    }

    @media (max-width: 700px) {
        .block-container {
            padding: 1rem 1rem 2rem;
        }

        .brandbar {
            align-items: flex-start;
            flex-direction: column;
        }

        .navlinks {
            gap: 15px;
        }

        .hero {
            min-height: 430px;
            border-radius: 15px;
        }

        .hero h1 {
            font-size: 2.7rem;
        }

        .product-card img {
            height: 190px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- Header ----------------
st.markdown(
    """
    <div class="brandbar">
      <div>
        <div class="brand-logo">VIN<span>•</span>WATT</div>
        <div class="brand-caption">A Vintechnologies brand</div>
      </div>
      <div class="navlinks">
        <a href="#solutions">Solutions</a>
        <a href="#about">About us</a>
        <a href="#contact">Contact</a>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------- Hero ----------------
st.markdown(
    f"""
    <section class="hero">
      <div class="hero-content">
        <div class="eyebrow">Powering a cleaner tomorrow</div>
        <h1>Move forward.<br>Charge smarter.</h1>
        <p>{TAGLINE} Discover EV charging and solar energy solutions
        for homes, businesses and future-focused projects.</p>
        <a class="hero-button" href="#solutions">Explore our solutions &nbsp; ↗</a>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)
st.image("vinwatt-ev-ad.png", use_container_width=True)
st.write("")

# ---------------- Solutions ----------------
st.markdown(
    """
    <div id="solutions" class="section">
      <div class="kicker">What we do</div>
      <h2 class="section-title">Clean energy, made practical.</h2>
      <p class="section-description">
        Explore our EV charging and solar energy solutions.
        Tell us what you need, and our team can discuss suitable options
        for your project.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

ev_col, solar_col = st.columns(2, gap="large")

with ev_col:
    st.markdown(
        f"""
        <div class="product-card">
          <img src="{EV_IMAGE}" alt="EV charging station">
          <div class="product-content">
            <div class="product-tag">01 / Electric mobility</div>
            <h3>EV charging solutions</h3>
            <p>Explore charging options for homes, workplaces,
            commercial locations and other projects. Ask us about
            charger types and installation requirements.</p>
            <a class="product-link" href="#contact">Enquire about EV charging ↗</a>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with solar_col:
    st.markdown(
        f"""
        <div class="product-card">
          <img src="{SOLAR_IMAGE}" alt="Solar panels">
          <div class="product-content">
            <div class="product-tag">02 / Solar energy</div>
            <h3>Solar power solutions</h3>
            <p>Discuss rooftop solar and clean-energy options for your
            home or business based on your location and energy needs.</p>
            <a class="product-link" href="#contact">Enquire about solar ↗</a>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------- About ----------------
st.markdown(
    """
    <div id="about" class="dark-panel">
      <div class="kicker">The VIN-WATT approach</div>
      <h2 class="section-title">Energy solutions built around you.</h2>
      <p>We believe the right solution begins with understanding your
      needs and having a clear conversation about your project.</p>
      <div class="benefit">
        <strong>01 — Understand</strong><br>
        Tell us about your home, business or project.
      </div>
      <div class="benefit">
        <strong>02 — Explore</strong><br>
        Discuss products and possible configurations with our team.
      </div>
      <div class="benefit">
        <strong>03 — Connect</strong><br>
        Contact us directly to discuss your next steps.
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------- Brand statement ----------------
st.markdown(
    f"""
    <div style="
      margin-top:36px;
      padding:32px;
      border-radius:18px;
      background:linear-gradient(90deg,rgba(237,241,232,.96),
      rgba(237,241,232,.82)),url('{CLEAN_ENERGY_IMAGE}') center/cover;">
      <div class="kicker">Our purpose</div>
      <h2 class="section-title">Better energy choices start here.</h2>
      <p class="section-description">{TAGLINE}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------- Contact ----------------
st.markdown(
    """
    <div id="contact" class="section">
      <div class="kicker">Let's connect</div>
      <h2 class="section-title">Tell us what you need.</h2>
      <p class="section-description">
        Complete the enquiry form to prepare a WhatsApp message.
        You can review it before choosing to send it.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

contact_col, form_col = st.columns([0.9, 1.1], gap="large")

with contact_col:
    st.markdown(
        f"""
        <div class="contact-card">
          <div class="brand-logo">VIN<span>•</span>WATT</div>
          <p class="note">{COMPANY}</p>
          <div class="contact-row">
            <strong>Phone</strong>
            <span>{PHONE}</span>
          </div>
          <div class="contact-row">
            <strong>Email</strong>
            <span>{EMAIL}</span>
          </div>
          <div class="contact-row">
            <strong>Address</strong>
            <span>{ADDRESS}</span>
          </div>
          <div class="contact-row">
            <strong>Our promise</strong>
            <span>{TAGLINE}</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.link_button(
        "Chat on WhatsApp",
        "https://wa.me/" + WHATSAPP + "?text=" + quote(
            "Hello VIN-WATT, I would like to know more about your solutions."
        ),
        use_container_width=True,
    )
    st.link_button(
        "Call VIN-WATT",
        "tel:+91" + PHONE,
        use_container_width=True,
    )
    st.link_button(
        "Email VIN-WATT",
        "mailto:" + EMAIL,
        use_container_width=True,
    )

with form_col:
    st.markdown('<div class="contact-card">', unsafe_allow_html=True)

    with st.form("vinwatt_enquiry", clear_on_submit=False):
        name = st.text_input("Your name *", placeholder="Enter your name")
        phone = st.text_input(
            "Your phone number *",
            placeholder="Enter your contact number",
        )
        interest = st.selectbox(
            "What are you interested in?",
            [
                "EV charging solution",
                "Solar energy solution",
                "EV charging and solar",
                "Business or dealership enquiry",
                "Other enquiry",
            ],
        )
        location = st.text_input(
            "City / location",
            placeholder="e.g. Madurai",
        )
        details = st.text_area(
            "Your requirements",
            placeholder="Tell us a little about your project...",
            height=120,
        )
        submitted = st.form_submit_button(
            "Prepare WhatsApp enquiry ↗",
            type="primary",
            use_container_width=True,
        )

    if submitted:
        if not name.strip() or not phone.strip():
            st.warning("Please enter your name and phone number.")
        else:
            message = (
                "Hello VIN-WATT / Vintechnologies,\n\n"
                "I would like to make an enquiry.\n\n"
                f"Name: {name.strip()}\n"
                f"Phone: {phone.strip()}\n"
                f"Interest: {interest}\n"
                f"Location: {location.strip() or 'Not provided'}\n"
                f"Requirements: {details.strip() or 'Not provided'}\n\n"
                "Please contact me with more details."
            )
            whatsapp_url = (
                "https://wa.me/" + WHATSAPP + "?text=" + quote(message)
            )
            st.success(
                "Your message is prepared. Open WhatsApp and press Send "
                "when you are ready."
            )
            st.link_button(
                "Open WhatsApp and review message",
                whatsapp_url,
                use_container_width=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- Footer ----------------
st.markdown(
    f"""
    <div class="footer">
      <strong style="color:#103c30;">VIN•WATT</strong> &nbsp;|&nbsp;
      {COMPANY}<br>
      {TAGLINE}<br><br>
      © {datetime.now().year} Vintechnologies. All rights reserved.<br><br>
      <span class="note">
        Images are illustrative. Confirm product specifications,
        availability and installation requirements with our team.
      </span>
    </div>
    """,
    unsafe_allow_html=True,
)
