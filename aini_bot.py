from data import PRODUCT_DATA
from memory import update_memory, get_memory, add_to_history
from score import calculate_best_site
from ai_layer import ask_groq,check_satisfaction,detect_upgrade_intent,classify_product_request



EXIT_WORDS = ["exit", "quit", "bye"]

current_product = None
awaiting_confirmation = False



def detect_greeting(text):
    greetings = ["hi", "hello", "hey", "hii", "heyy"]
    return text.lower().strip() in greetings


def detect_product(text):
    text = text.lower().strip()

    supported_products = ["laptop", "smartphone", "headphones", "smartwatch"]

    words = text.split()

    for product in supported_products:
        if product in words or product + "s" in words:
            return product

    return None


print("🤖 AINI: Hey! What electronics are you looking for?")
print("Supported: laptop, smartphone, headphones, smartwatch")
print("Type 'exit' anytime to quit.\n")


while True:
    try:
        user_input = input("You: ").strip()
        lower_input = user_input.lower()
        add_to_history(user_input)
        # 1 GREETING
        if detect_greeting(lower_input):
            print("🤖 AINI: Heyyy 😄 What electronics are you looking for today?\n")
            continue

         # 2 EXIT
        if lower_input in EXIT_WORDS:
            print("👋 AINI: Bye! Happy shopping 🛍️")
            break

        # 3 HANDLE SATISFACTION 
        if awaiting_confirmation:
            result = check_satisfaction(user_input,current_product)

            if result == "SATISFIED":
                print("🤖 AINI: I'm glad it helped 😄 Want to check another product?\n")
                awaiting_confirmation = False
                continue

            elif result == "UPGRADE":
                print("🤖 AINI: So you want something more powerful 😎 Let me suggest premium options...\n")
                awaiting_confirmation = False
                continue

            elif result == "UNSATISFIED":
                print("🤖 AINI: Ohh tell me what didn’t match your expectation 💛\n")
                awaiting_confirmation = False
                continue

            elif result == "CONFUSED":
                print("🤖 AINI: No worries 😊 Are you unsure about price, performance, or brand?\n")
                awaiting_confirmation = False
                continue

            else:
                print("🤖 AINI: Got it 👍 Tell me how you'd like it improved.\n")
                awaiting_confirmation = False
                continue


    # 4 Upgrade intent detection
        if detect_upgrade_intent(lower_input):

            last_product = get_memory("last_product")

            if last_product:
               print(f"🤖 AINI: Got it 😎 Showing better {last_product.upper()} options...\n")

               current_product = last_product

               results = PRODUCT_DATA[current_product]

               for site, data in results.items():
                    print(f"{site.capitalize()} → ₹{data['price']} | ⭐ {data['rating']} | 📝 {data['reviews']} reviews")

               best_site = calculate_best_site(results)
               best = results[best_site]

               print("\n✅ AINI Recommendation:")
               print(f"Buy from {best_site.upper()} — Rating {best['rating']}⭐, "
            f"{best['reviews']} reviews, Price ₹{best['price']}.\n"
        )

               print("🤖 AINI: How does this improved option look? 😊\n")

               awaiting_confirmation = True
               continue


     # 5 classify_product
         
        classification = classify_product_request(user_input)
        add_to_history(user_input)

        if classification == "UNSUPPORTED":
            print("🤖 AINI: Sorry,I currently support only laptops, smartphones, headphones, and smartwatches.\n")
            continue

        elif classification == "OTHER":
             ai_reply = ask_groq(user_input, get_memory("history"))
             print("🤖 AINI:", ai_reply, "\n")
             continue


        

        
        current_product =detect_product(lower_input)
        update_memory("last_product", current_product)


# 6  PRODUCT DETECTION
        current_product = detect_product(lower_input)

        if current_product:
            update_memory("last_product", current_product)


            print(f"\n🔍 Comparing {current_product.upper()}...\n")

            results = PRODUCT_DATA[current_product]

            for site, data in results.items():
                print(f"{site.capitalize()} → ₹{data['price']} | ⭐ {data['rating']} | 📝 {data['reviews']} reviews")

                best_site = calculate_best_site(results)
                best = results[best_site]

            print("\n✅ AINI Recommendation:")
            print(
                f"Buy from {best_site.upper()} — Rating {best['rating']}⭐, "
                f"{best['reviews']} reviews, Price ₹{best['price']}.\n"
            )

            print("🤖 AINI: How does that look? 😊\n")

            awaiting_confirmation = True
            continue

        # 6 AI Layer fallback
        ai_reply = ask_groq(user_input, get_memory("history"))
        print("🤖 AINI:", ai_reply, "\n")

    except Exception as e:
        print("ERROR:", e)
        break