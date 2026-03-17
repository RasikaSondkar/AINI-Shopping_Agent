import streamlit as st
from data import PRODUCT_DATA
from score import calculate_best_site
from memory import update_memory, get_memory
from ai_layer import ask_groq, classify_product_request
from utils import detect_product
from route import route_query
from logger import log_query

# -------------------------------------------------
# Page Config
# -------------------------------------------------

st.set_page_config(
    page_title="AINI Smart Shopping",
    page_icon="🤖"
)

st.title("🤖 AINI - Smart Shopping Assistant")
st.caption("Ask me about laptops, smartphones, headphones, smartwatches")

# -------------------------------------------------
# Session Memory
# -------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------------------------
# Display Chat History
# -------------------------------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------------------------------
# User Input
# -------------------------------------------------

user_input = st.chat_input("Type your message...")

if user_input:

    # ---------------------------------------------
    # Show User Message
    # ---------------------------------------------

    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # ---------------------------------------------
    # Pre-processing
    # ---------------------------------------------

    lower_input = user_input.lower()

    product = None
    response = ""

    # detect product
    product = detect_product(user_input)

    # ---------------------------------------------
    # Router System (Multi-model decision)
    # ---------------------------------------------

    route = route_query(user_input)

    # ---------------------------------------------
    # Assistant Response
    # ---------------------------------------------

    with st.chat_message("assistant"):

        # -----------------------------------------
        # PRODUCT ROUTE
        # -----------------------------------------

        if route == "PRODUCT":

            if product:

                update_memory("last_product", product)

                response += f"🔍 Comparing **{product.upper()}** options:\n\n"

                results = PRODUCT_DATA[product]

                for site, data in results.items():

                    response += (
                        f"**{site.capitalize()}** → "
                        f"₹{data['price']} | "
                        f"⭐ {data['rating']} | "
                        f"{data['reviews']} reviews\n\n"
                    )

                best_site = calculate_best_site(results)
                best = results[best_site]

                response += (
                    f"✅ **AINI Recommendation:**\n"
                    f"Buy from **{best_site.upper()}** "
                    f"— Price ₹{best['price']} | "
                    f"Rating {best['rating']} ⭐ | "
                    f"{best['reviews']} reviews."
                )

            else:

                response = "😅 I couldn't detect the product. Try asking about laptops, smartphones, headphones, or smartwatches."

        # -----------------------------------------
        # AI ROUTE (Groq reasoning)
        # -----------------------------------------

        else:

            classification = classify_product_request(user_input)

            if classification == "UNSUPPORTED":

                response = (
                    "😅 I currently support only **laptops, smartphones, "
                    "headphones, and smartwatches.**"
                )

            elif classification == "OTHER":

                response = ask_groq(user_input, get_memory("history"))

            else:

                response = ask_groq(user_input, get_memory("history"))

        # -----------------------------------------
        # Display Assistant Response
        # -----------------------------------------

        st.markdown(response)

        # -----------------------------------------
        # Store Chat Memory
        # -----------------------------------------

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        # -----------------------------------------
        # Logging System
        # -----------------------------------------

        log_query(user_input, response)

        # -----------------------------------------
        # Confidence Score
        # -----------------------------------------

        confidence = 0.90

        if route == "PRODUCT":
            confidence = 0.95

        st.caption(f"Confidence Score: {confidence}")