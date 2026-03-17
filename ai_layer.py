from groq import Groq


client = Groq(api_key="")



def ask_groq(user_input, history=None):

    system_prompt = """
You are AINI, a smart shopping assistant.

STRICT RULES:
- Reply in MAXIMUM 1 sentence.
- Maximum 15 words.
- You only support these products : Laptop,Smartphone,Headphone,Smartwatch
- If user asks anything outside thsese, reply EXACTLY like: " I currently support only electronics devices like Laptop, Smartphone, Headphone, and Smartwatch. Other categories wiill be supported soon. " 
- Never give medical advice.
- Do not suggest clothes, shoes, dresses or other products
- Never give health tips.
- Never give long explanations.
- Stay casual, friendly, human.
- Focus on shopping and emotions.
- If user is sad → comfort briefly.
- If user is happy → respond positively.
- If unrelated topic → gently bring back to shopping.

Bad example ❌:
"Drink water, rest well, consult doctor..."

Good example ✅:
"I'm here for you 💛 Want to explore some cool gadgets?"

Keep responses VERY SHORT.
"""

    messages = [{"role": "system", "content": system_prompt}]

    if history:
        for msg in history[-3:]:
            messages.append({"role": "user", "content": msg})

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.2,
        max_tokens=30   # HARD LIMIT
    )

    reply = response.choices[0].message.content.strip()

    # Safety limiter (extra protection)
    reply = reply.split("\n")[0]
    if len(reply.split()) > 15:
        reply = "I’m here to help 💛 Want to explore another product?"

    return reply
# -----------------------------
# Satisfaction classifier
# -----------------------------
def check_satisfaction(user_input, current_product=None):

    prompt = f"""
You are a classifier for a shopping assistant.
Rules:
- Alaways reply short (max 1-2 lines)
- Be friendly and human like
- Do not give medical,health or unrelated advice
- stay focused on shopping and user feelings
- If user is sad comfort briefly
- If user is happy, respond positively 
- if unrelated topic, gently bring back to shopping
- Never exceed two sentencees 

Product recommended: {current_product}

Classify user reaction:

SATISFIED → likes it
UNSATISFIED → dislikes it
UPGRADE → wants better options
CONFUSED → unsure
GENERAL → unrelated

Examples:

bad → UNSATISFIED
not good → UNSATISFIED
don't like → UNSATISFIED
good → SATISFIED
nice → SATISFIED
better options → UPGRADE
reply should consist of 1-2 lines

Return ONLY ONE WORD.

User input: {user_input}
"""

    result = ask_groq(prompt)

    return result.strip().upper()


def classify_product_request(user_input):

    prompt = f"""
You are a strict product classifier for an electronics shopping assistant called AINI.

Your job is to classify the user's request into ONLY ONE of these three labels:

SUPPORTED → ONLY if the user is asking about these exact products:
- laptop
- smartphone
- headphones
- smartwatch

UNSUPPORTED → if the user is asking about:
- accessories (charger, case, cover, cable, adapter, battery, etc.)
- any other electronics not in supported list
- clothes, shoes, furniture, or anything else

OTHER → if the user is greeting, chatting, saying ok, thanks, or general conversation

IMPORTANT RULES:
- "laptop charger" → UNSUPPORTED
- "smartphone case" → UNSUPPORTED
- "buy laptop" → SUPPORTED
- "hello" → OTHER
- "ok" → OTHER

Return ONLY one word:
SUPPORTED
UNSUPPORTED
OTHER

User input: {user_input}
"""

    result = ask_groq(prompt)

    return result.strip().upper()

# intent detect
def detect_upgrade_intent(user_input):
    upgrade_words = [
        "better",
        "upgrade",
        "more advanced",
        "premium",
        "higher",
        "best",
        "improve",
        "not good",
        "don't like",
        "bad"
    ]

    user_input = user_input.lower()

    for word in upgrade_words:
        if word in user_input:
            return True

    return False