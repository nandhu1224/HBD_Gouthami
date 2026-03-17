import streamlit as st
import time

# --- CONFIG ---
st.set_page_config(page_title="To My Gothami 🦋", page_icon="🦋", layout="centered")

# --- CSS (Exact Image Style + Butterfly Rain) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #001524;
        color: #E0E1DD;
        font-family: 'sans-serif';
    }
    
    /* Image Header Style */
    .header-text {
        font-size: 52px;
        font-weight: 800;
        color: white;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 22px;
        font-style: italic;
        color: #ff75c3;
        text-align: center;
        margin-top: -10px;
        margin-bottom: 40px;
    }

    /* Butterfly Animation */
    @keyframes butterfly-fall {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    .butterfly {
        position: fixed;
        top: -10%;
        color: #ff75c3;
        font-size: 24px;
        animation: butterfly-fall 10s linear infinite;
    }

    /* The Gift (Letter) Styling */
    .letter-card {
        background: #ffffff;
        color: #1b263b;
        padding: 35px;
        border-radius: 12px;
        border-left: 10px solid #ff75c3;
        line-height: 1.8;
        font-family: 'Georgia', serif;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    /* Button Styling */
    .stButton>button {
        background: #ff75c3;
        color: white;
        border: none;
        border-radius: 50px;
        padding: 15px 40px;
        font-size: 20px;
        font-weight: bold;
        display: block;
        margin: 0 auto;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px #ff75c3;
    }
    
    /* Hide Default UI */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>

    <div class="butterfly" style="left:15%; animation-delay:0s;">🦋</div>
    <div class="butterfly" style="left:45%; animation-delay:3s;">🦋</div>
    <div class="butterfly" style="left:75%; animation-delay:1s;">🦋</div>
    <div class="butterfly" style="left:90%; animation-delay:5s;">🦋</div>
    """, unsafe_allow_html=True)

# --- 1. HEADER (Matches Your Image) ---
st.markdown('<h1 class="header-text">To My Gotham 🦋</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">The girl who stayed, for the girl who deserves my love.</p>', unsafe_allow_html=True)

# --- 2. THE BIG DATE ---
st.markdown("<h2 style='text-align: center; color: white;'>March 18 ✨</h2>", unsafe_allow_html=True)
st.write("##")

# --- 3. THE GIFT BUTTON ---
# This button triggers everything else
if "opened" not in st.session_state:
    st.session_state.opened = False

if not st.session_state.opened:
    if st.button("Open My Heart & Your Gift 🎁"):
        st.session_state.opened = True
        st.rerun()

# --- 4. REVEALED CONTENT ---
if st.session_state.opened:
    st.balloons()
    
    # The Letter
    st.markdown(f"""
    <div class="letter-card">
        <h2 style="color: #1b263b; text-align: center;">💌 A Letter to You</h2>
        <p><b>Dear gundu,</b></p>
        <p>
            They say friends are the family we choose, but with you, it feels like the universe chose us long ago. 
            Looking back from 2022 to now, I realized I’ve been the girl standing beside you through every single season.
        </p>
        <p>
            I’ve watched you grow, heal, and shine. I am so proud that <b>I was the one</b> holding your hand through it all. 
            You aren't just my best friend; you are the keeper of my secrets and the mirror to my soul.
        </p>
        <p>
            On your birthday, <b>March 18</b>, I wish you the kind of peace that never leaves. 
            No matter what situation life throws at us next, <b>I am still that girl</b> who will be standing right there with you.
        </p>
        <p style="text-align: right;"><i>Always & Forever, <br> Your nandhu</i></p>
    </div>
    """, unsafe_allow_html=True)

    st.write("##")
    st.write("---")
    
    # The Timeline
    st.markdown("<h3 style='text-align: center;'>Our Years Together 🥂</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<h4 style='color:#ff75c3; text-align:center;'>2022</h4>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'>Where it all began.</p>", unsafe_allow_html=True)
    with col2:
        st.markdown("<h4 style='color:#ff75c3; text-align:center;'>2023</h4>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'>Stronger than ever.</p>", unsafe_allow_html=True)
    with col3:
        st.markdown("<h4 style='color:#ff75c3; text-align:center;'>2024</h4>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'>To infinity and beyond.</p>", unsafe_allow_html=True)

    st.write("##")
    st.markdown("<h1 style='text-align: center;'>🎂</h1>", unsafe_allow_html=True)