# Prompting Assignment
A lightweight Python project integrating Google Gemini 3 Flash for controlled text generation, exploring parameter tuning (temperature, top_p, max_tokens) across multiple prompting techniques and use this for gettting better optimized output.
## 📌 Project Overview

The project consists of **different prompt experiments**:

1. **Text Generation Experiments with different prompt techniques**
   - Few shot prompt technique
   - Role based prompt technique
   - Context based prompt technique
   - Self consistency prompt technique
   - Chain of thought prompt technique
   - Tree of thought prompt technique

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **LLM:** Google Gemini
- **SDK:** `google-genai`

---

## ⚙️ Installation

1. Clone the repository
    ```bash
        git clone https://github.com/sujeet-crossml/Prompting_Assignment.git
        cd Prompting_Assignment

2. Create and activate a virtual environment (recommended)

    ```bash

        python -m venv venv
        source venv/bin/activate
   
3. Install dependencies

    ```bash
    
        pip install google-genai dotenv
   
4. 🔐 API Key Setup
    Replace API-KEY in the code with your Gemini API key:

    python
      
        client = genai.Client(gemini_api_key="YOUR_API_KEY")

5. ▶️ Usage
  1️⃣ Text Generation Experiment
  
    This script explores how different prompts and parameters affect generated text.

        python main.py


    Prompts Used:
    
      -  All prompt will be find in prompt.py file
      -  Use prompt one by one and analyse the output.
    
    Parameters Tuned:
    
      -  temperature
      
      -  top_p
        
      -  top_k
  
      -  max_output_tokens

  

🧪 Learning Outcomes

  -  Understand the impact of temperature on creativity
  -  Compare top_p vs top_k sampling
  -  Build intuition for prompt engineering
  -  Analyze different Prompting techniques with output.
