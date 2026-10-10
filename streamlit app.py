
import html
from urllib.parse import quote

import streamlit as st

# ============================================================
# VIN-WATT | VINTECHNOLOGIES
# No API keys. WhatsApp enquiries only.
# Customers must press Send in WhatsApp themselves.
# ============================================================

st.set_page_config(
    page_title="VIN-WATT | EV & Solar Solutions",
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
SLOGAN = "Sustainable Charging Solutions for the Road Ahead."

WA_BASE = f"https://wa.me/{WHATSAPP}"
WA_GENERAL = WA_BASE + "?text=" + quote(
    "Hello VIN-WATT! I would like to know more about your EV charging and solar solutions."
)
CALL_LINK = f"tel:+91{PHONE}"
EMAIL_LINK = f"mailto:{EMAIL}?subject={quote('VIN-WATT Enquiry')}"

# Illustrative stock images. Replace with your own product photos later.
HERO_IMAGE = (
    "https://images.unsplash.com/photo-1593941707882-a5bba14938c7"
    "?auto=format&fit=crop&w=1800&q=85"
)
EV_IMAGE = (
    "https://images.unsplash.com/photo-1593941707882-a5bba14938c7"
    "?auto=format&fit=crop&w=900&q=80"
)
SOLAR_IMAGE = (
    "https://images.unsplash.com/photo-1509391366360-2e959784a276"
    "?auto=format&fit=crop&w=900&q=80"
)
INFRA_IMAGE = (
    "https://images.unsplash.com/photo-1497435334941-8c899ee9e8e9"
    "?auto=format&fit=crop&w=900&q=80"
)

# ---------------------- DESIGN ------------------------------

st.markdown(
    f"""
    <style>
    .stApp {{
        background: #f6faf7;
        color: #153c29;
    }}
    [data-testid="stHeader"] {{
        background: rgba(246,250,247,0.94);
    }}
    .block-container {{
        max-width: 1180px;
        padding-top: 1.3rem;
        padding-bottom: 3rem;
    }}
    h1, h2, h3 {{
        color: #0b3520;
        letter-spacing: -0.025em;
    }}
    .brandbar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 1rem;
        padding-bottom: 1.2rem;
    }}
    .brand {{
        font-size: 1.8rem;
        font-weight: 900;
        color: #082b1b;
        letter-spacing: .04em;
    }}
    .brand span {{
        color: #239455;
    }}
    .brand-sub {{
        color: #587262;
        font-size: .9rem;
        text-align: right;
    }}
    .hero {{
        border-radius: 24px;
        overflow: hidden;
        min-height: 370px;
        padding: clamp(1.6rem, 5vw, 4rem);
        display: flex;
        align-items: center;
        background-color: #082b1b;
        background-image:
            linear-gradient(90deg,
                rgba(4, 34, 19, .97) 0%,
                rgba(4, 34, 19, .84) 52%,
                rgba(4, 34, 19, .25) 100%),
            url("{HERO_IMAGE}");
        background-size: cover;
        background-position: center;
    }}
    .hero-kicker {{
        color: #b7edc8;
        font-size: .78rem;
        font-weight: 800;
        letter-spacing: .15em;
        text-transform: uppercase;
    }}
    .hero h1 {{
        color: white;
        font-size: clamp(2.8rem, 7vw, 5.2rem);
        line-height: 1.05;
        margin: .6rem 0 1rem;
    }}
    .hero p {{
        color: #f0fff4;
        font-size: clamp(1rem, 2vw, 1.2rem);
        max-width: 620px;
        line-height: 1.7;
    }}
    .section-kicker {{
        color: #21834b;
        font-size: .76rem;
        font-weight: 800;
        letter-spacing: .13em;
        text-transform: uppercase;
        margin-bottom: .3rem;
    }}
    .intro {{
        color: #607469;
        line-height: 1.8;
    }}
    .product-card {{
        background: white;
        border: 1px solid #dce8df;
        border-radius: 18px;
        overflow: hidden;
        box-shadow: 0 6px 22px rgba(8,43,27,.05);
    }}
    .product-card img {{
        display: block;
        width: 100%;
        height: 205px;
        object-fit: cover;
    }}
    .product-body {{
        padding: 1.2rem;
        min-height: 155px;
    }}
    .product-label {{
        display: inline-block;
        background: #e8f4ec;
        color: #14532d;
        padding: .3rem .65rem;
        border-radius: 30px;
        font-size: .72rem;
        font-weight: 800;
        margin-bottom: .5rem;
    }}
    .product-body h3 {{
        font-size: 1.15rem;
        margin: .2rem 0 .5rem;
    }}
    .product-body p {{
        color: #607469;
        font-size: .92rem;
        line-height: 1.6;
    }}
    .benefit {{
        background: white;
        border: 1px solid #dce8df;
        border-radius: 16px;
        padding: 1.2rem;
        height: 100%;
    }}
    .benefit h3 {{
        font-size: 1.05rem;
    }}
    .benefit p {{
        color: #607469;
        font-size: .9rem;
    }}
    .contact-panel {{
        background: linear-gradient(120deg, #082b1b, #17623a);
        border-radius: 22px;
        padding: clamp(1.5rem, 4vw, 2.5rem);
        color: white;
    }}
    .contact-panel h2, .contact-panel p {{
        color: white;
    }}
    .contact-panel .muted {{
        color: #d7eddf;
    }}
    .footer {{
        border-top: 1px solid #dce8df;
        margin-top: 2rem;
        padding-top: 1.2rem;
        color: #607469;
        font-size: .85rem;
        line-height: 1.8;
    }}
    div.stLinkButton > a,
    div.stFormSubmitButton > button {{
        border-radius: 10px;
        font-weight: 700;
        min-height: 2.7rem;
    }}
    div.stFormSubmitButton > button[kind="primary"] {{
        background: #1f7a49;
        border-color: #1f7a49;
    }}
    @media (max-width: 700px) {{
        .block-container {{
            padding-left: 1rem;
            padding-right: 1rem;
        }}
        .brandbar {{
            align-items: flex-start;
            flex-direction: column;
        }}
        .brand-sub {{
            text-align: left;
        }}
        .hero {{
            min-height: 330px;
            border-radius: 18px;
            padding: 1.5rem;
        }}
        .product-card img {{
            height: 180px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------- HEADER -----------------------------

st.markdown(
    f"""
    <div class="brandbar">
        <div class="brand">⚡ {BRAND}<span>.</span></div>
        <div class="brand-sub">
            EV Charging &nbsp;·&nbsp; Solar Energy &nbsp;·&nbsp; Smart Mobility
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------- HERO --------------------------------

st.markdown(
    f"""
    <section class="hero">
        <div>
            <div class="hero-kicker">Clean energy · Smarter journeys</div>
            <h1>{BRAND}</h1>
            <p><strong>{SLOGAN}</strong></p>
            <p>
                EV charging and solar solutions for homes,
                businesses and charging locations.
            </p>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.write("")
intro_col, action_col = st.columns([1.3, 1], gap="large")

with intro_col:
    st.subheader("Powering a cleaner tomorrow")
    st.markdown(
        '<p class="intro">Discover electric mobility and clean-energy '
        'solutions from Vintechnologies. Contact our team to discuss your '
        'project, product options and quotation.</p>',
        unsafe_allow_html=True,
    )

with action_col:
    st.write("")
    st.link_button(
        "💬 WhatsApp VIN-WATT",
        WA_GENERAL,
        type="primary",
        use_container_width=True,
    )
    st.link_button(
        "✉️ Email VIN-WATT",
        EMAIL_LINK,
        use_container_width=True,
    )

# ---------------------- PRODUCTS ----------------------------

st.write("")
st.markdown(
    '<div class="section-kicker">OUR SOLUTIONS</div>',
    unsafe_allow_html=True,
)
st.header("Solutions for a smarter, cleaner future")
st.markdown(
    '<p class="intro">Explore our main solution categories. '
    'Contact us for current product availability and specifications.</p>',
    unsafe_allow_html=True,
)

products = [
    {
        "label": "E-MOBILITY",
        "title": "EV Charging Solutions",
        "description": (
            "Charging options for homes, offices, commercial sites "
            "and selected public charging locations."
        ),
        "image": EV_IMAGE,
        "alt": "Electric vehicle charging equipment",
        "message": "Hello VIN-WATT, I am interested in EV charging solutions.",
    },
    {
        "label": "SOLAR ENERGY",
        "title": "Solar Energy Solutions",
        "description": (
            "Explore rooftop solar options for residential and "
            "commercial energy requirements."
        ),
        "image": SOLAR_IMAGE,
        "alt": "Solar panels under sunlight",
        "message": "Hello VIN-WATT, I am interested in solar energy solutions.",
    },
    {
        "label": "INFRASTRUCTURE",
        "title": "Charging Infrastructure",
        "description": (
            "Discuss site requirements and installation planning "
            "for your EV charging project."
        ),
        "image": INFRA_IMAGE,
        "alt": "Modern energy infrastructure",
        "message": "Hello VIN-WATT, I want to discuss EV charging infrastructure.",
    },
]

cols = st.columns(3, gap="medium")

for col, product in zip(cols, products):
    with col:
        st.markdown(
            f"""
            <div class="product-card">
                <img src="{product['image']}"
                     alt="{html.escape(product['alt'])}"
                     loading="lazy">
                <div class="product-body">
                    <span class="product-label">{product['label']}</span>
                    <h3>{product['title']}</h3>
                    <p>{product['description']}</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        st.link_button(
            "Enquire on WhatsApp",
            WA_BASE + "?text=" + quote(product["message"]),
            use_container_width=True,
        )

# ---------------------- BENEFITS ----------------------------

st.write("")
st.markdown(
    '<div class="section-kicker">WHY VIN-WATT</div>',
    unsafe_allow_html=True,
)
st.header("A customer-first clean-energy approach")

benefits = [
    (
        "🌱",
        "Sustainability-minded",
        "Explore options for electric mobility and cleaner energy.",
    ),
    (
        "🏢",
        "Homes and businesses",
        "Discuss requirements for residential and commercial projects.",
    ),
    (
        "🤝",
        "Personal enquiry",
        "Talk to our team about product options and quotations.",
    ),
]

cols = st.columns(3, gap="medium")
for col, (icon, title, description) in zip(cols, benefits):
    with col:
        st.markdown(
            f"""
            <div class="benefit">
                <div style="font-size:1.7rem">{icon}</div>
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ---------------------- CONTACT -----------------------------

st.write("")
st.markdown(
    '<div class="section-kicker">ABOUT US</div>',
    unsafe_allow_html=True,
)
st.header(COMPANY)
st.markdown(
    '<p class="intro">VIN-WATT by Vintechnologies focuses on electric '
    'mobility and sustainable energy solutions. Contact us to discuss '
    'your requirements and confirm technical specifications and availability.</p>',
    unsafe_allow_html=True,
)

st.write("")
st.markdown(
    f"""
    <section class="contact-panel">
        <div class="section-kicker" style="color:#b7edc8">GET IN TOUCH</div>
        <h2>Let's talk about your project.</h2>
        <p class="muted">Contact our team to start a conversation.</p>
        <p><strong>{COMPANY}</strong><br>{html.escape(ADDRESS)}</p>
        <p>Phone: +91 {PHONE}<br>Email: {EMAIL}</p>
    </section>
    """,
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)
with c1:
    st.link_button(
        "📞 Call Us",
        CALL_LINK,
        use_container_width=True,
    )
with c2:
    st.link_button(
        "✉️ Email Us",
        EMAIL_LINK,
        use_container_width=True,
    )
with c3:
    st.link_button(
        "💬 WhatsApp Us",
        WA_GENERAL,
        type="primary",
        use_container_width=True,
    )

# ---------------------- WHATSAPP FORM -----------------------

st.write("")
st.divider()
st.header("Send an enquiry on WhatsApp")
st.write(
    "Fill in the form, then click **Prepare WhatsApp message**. "
    "WhatsApp will open with your enquiry filled in. Review the message "
    "and press **Send** in WhatsApp. This website does not send it automatically."
)

with st.form("vinwatt_whatsapp_enquiry"):
    name = st.text_input("Your name *", max_chars=100)
    customer_phone = st.text_input(
        "Your phone number (optional)",
        max_chars=30,
    )
    interest = st.selectbox(
        "What are you interested in? *",
        [
            "EV chargers",
            "Solar energy",
            "Charging infrastructure",
            "Other",
        ],
    )
    details = st.text_area(
        "Tell us about your requirement *",
        max_chars=2000,
    )
    prepare = st.form_submit_button(
        "Prepare WhatsApp message",
        type="primary",
        use_container_width=True,
    )

if prepare:
    if not name.strip() or not details.strip():
        st.error("Please enter your name and describe your requirement.")
    else:
        message = (
            "Hello VIN-WATT / Vintechnologies!\n\n"
            f"Name: {name.strip()}\n"
            f"Phone: {customer_phone.strip() or 'Not provided'}\n"
            f"Interested in: {interest}\n\n"
            f"Requirement: {details.strip()}\n\n"
            "Please share more information and a quotation."
        )
        wa_url = WA_BASE + "?text=" + quote(message)

        st.success(
            "Your enquiry message is ready. Open WhatsApp and press Send."
        )
        st.link_button(
            "Open WhatsApp to Send Enquiry",
            wa_url,
            type="primary",
            use_container_width=True,
        )

st.caption(
    "Privacy: the form does not store or submit your details. "
    "Your message is prepared for WhatsApp, and you decide whether to send it."
)

# ---------------------- FOOTER -----------------------------

st.markdown(
    f"""
    <div class="footer">
        <strong>{BRAND}</strong> · {COMPANY}<br>
        {html.escape(ADDRESS)}<br>
        {SLOGAN}<br><br>
        Product photographs are illustrative. Please confirm product
        availability and specifications with our team.
    </div>
    """,
    unsafe_allow_html=True,
)
