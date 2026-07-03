import streamlit as st
import re
import random
import string

st.set_page_config(page_title="Password Security Checker", page_icon="🔐", layout="centered")

# ---------------------- CSS ----------------------
st.markdown("""
<style>
.stApp{
    background: linear-gradient(135deg, #1E3C72, #2A5298);
}

.title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:white;
}

.sub{
    text-align:center;
    color:#d9d9d9;
    font-size:18px;
}

.box{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 0px 10px gray;
}

.result{
    font-size:20px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------------- Functions ----------------------
def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character.")

    weak_patterns = [
        "password",
        "123456",
        "qwerty",
        "admin",
        "welcome",
        "abc123"
    ]

    if password.lower() in weak_patterns:
        feedback.append("⚠ Common password detected.")
        score = 0

    if score == 5:
        strength = "🟢 Very Strong"
    elif score == 4:
        strength = "🟡 Strong"
    elif score == 3:
        strength = "🟠 Medium"
    elif score == 2:
        strength = "🔴 Weak"
    else:
        strength = "❌ Very Weak"

    return strength, feedback


def generate_password(length=12):
    characters = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*()"
    )

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# ---------------------- UI ----------------------
st.markdown("<div class='title'>🔐 Password Security Checker</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>Check your password strength and generate secure passwords.</div>", unsafe_allow_html=True)

st.write("")

password = st.text_input("Enter Password", type="password")

col1, col2 = st.columns(2)

with col1:
    check = st.button("Check Strength")

with col2:
    generate = st.button("Generate Password")

st.write("")

if check:
    if password == "":
        st.warning("Please enter a password.")
    else:
        strength, feedback = check_password(password)

        st.markdown(
    f"""
    <h3 style="color:orange;">
        Strength: {strength}
    </h3>
    """,
    unsafe_allow_html=True
)

if check:
    if password == "":
        st.warning("Please enter a password.")
    else:
        strength, feedback = check_password(password)

        st.markdown(
            f"""
            <h3 style="color:orange;">
                Strength: {strength}
            </h3>
            """,
            unsafe_allow_html=True
        )

        if feedback:
            st.markdown(
                """
                <h3 style="color:orange;">
                    Suggestions
                </h3>
                """,
                unsafe_allow_html=True
            )

            for item in feedback:
                st.markdown(
                    f"""
                    <p style="color:orange; font-size:18px;">
                        {item}
                    </p>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.success("✅ Excellent! Your password is secure.")

if generate:
    # Generate a secure password
    new_password = generate_password()

    # Pink heading
    st.markdown(
        """
        <h3 style="color:#FF1493; text-align:center;">
            🎉 Secure Password Generated
        </h3>
        """,
        unsafe_allow_html=True
    )

    # Display generated password
    st.code(new_password)

    # Pink message
    st.markdown(
        """
        <p style="color:#FF1493; font-size:18px; text-align:center; font-weight:bold;">
            📋 Copy this password and use it for your accounts.
        </p>
        """,
        unsafe_allow_html=True
    )