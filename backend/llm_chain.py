from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# Temporary fix so you can keep coding without the API
DEBUG_MODE = True



load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", 
                            max_retries=6,
                            temperature=0.7,
                            google_api_key=os.getenv("GOOGLE_API_KEY"))
                          
                              

# Update your prompt template in llm_chain.py  
prompt = ChatPromptTemplate.from_template("""
You are a Luxury Travel & Food Critic AI. 
Generate a high-end itinerary for: {current_city} to {destination_city}.
Duration: {days} Days | Budget: {budget} | Style: {style}

--- 
## 🛫 TRAVEL & 🏨 STAY
(Provide a table for travel and 2-3 hotel recommendations)

---                                                                          
## 🍴 BEST FOOD & FAMOUS EATERIES
| Dish Name | Type | Recommended Location | Approx Cost |
|-----------|------|----------------------|-------------|
| [Dish] | [Type] | [Location] | ₹... |

---
## 🗓️ DETAILED ITINERARY
(Crucial: Start each day with a '### Day' header)

### Day 1: The Adventure Begins
* **Morning:** ...
* **Afternoon:** ...
* **Evening:** ...

### Day 2: Cultural Immersion
* **Morning:** ...
* **Afternoon:** ...
* **Evening:** ...

---
## 💡 TRAVEL TIPS
* Tip 1
* Tip 2
                                          
## 🔗 QUICK BOOKING
- [✈️ Book Flights](https://www.skyscanner.co.in/transport/flights/{current_city}/{destination_city})
- [🏨 Book Hotels](https://www.booking.com/searchresults.html?ss={destination_city})

""")    

chain = prompt | llm

def generate_itinerary(data):
    response = chain.invoke(data)
    return response.content