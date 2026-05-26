# 🤖 AI Personal Assistant — OSS vs Frontier

> Built as part of the Founding AI/ML Engineer assignment for **Ollive AI**

---

## 📌 Project Overview

This project builds and evaluates **two AI personal assistants**:

| Assistant | Model | Provider |
|---|---|---|
| 🧠 OSS Assistant | Qwen2.5-72B-Instruct | HuggingFace Inference API |
| 🤖 Frontier Assistant | Llama-3.3-70B-Versatile | Groq API |

Both assistants support:
- ✅ Multi-turn conversations
- ✅ Short-term conversational memory
- ✅ Basic assistant-like behaviour
- ✅ Clean Streamlit chat interface

---

## 📁 Project Structure

```
ai-assistant-project/
│
├── oss_assistant/
│   └── app.py              # OSS Assistant (Qwen2.5 via HuggingFace)
│
├── frontier_assistant/
│   └── app.py              # Frontier Assistant (Llama via Groq)
│
├── evaluation/
│   └── eval.py             # Evaluation framework
│
├── .env                    # API Keys (not committed to GitHub)
├── .gitignore              # Ignores .env and cache files
└── README.md               # You are here!
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-assistant-project.git
cd ai-assistant-project
```

### 2. Install Dependencies

```bash
pip install streamlit groq huggingface_hub python-dotenv
```

### 3. Set Up API Keys

Create a `.env` file in the root folder:

```
GROQ_API_KEY=your_groq_api_key_here
HF_TOKEN=your_huggingface_token_here
```

> 🔴 Never commit your `.env` file to GitHub!

### 4. Run OSS Assistant

```bash
cd oss_assistant
python -m streamlit run app.py --server.port 8503
```

Open browser at: `http://localhost:8503`

### 5. Run Frontier Assistant

```bash
cd frontier_assistant
python -m streamlit run app.py --server.port 8502
```

Open browser at: `http://localhost:8502`

---

## 🏗️ Architecture Decisions

### OSS Assistant — Qwen2.5-72B-Instruct via HuggingFace

- **Why Qwen2.5?** It is one of the strongest open-source models available, with excellent instruction-following capabilities and multilingual support.
- **Why HuggingFace Inference API?** Avoids heavy local downloads and enables fast cloud-based inference without GPU requirements.
- **Memory:** Maintained using `st.session_state` — full conversation history passed on every API call.

### Frontier Assistant — Llama-3.3-70B via Groq

- **Why Llama 3.3?** State-of-the-art open-weight model with exceptional reasoning and fluency.
- **Why Groq?** Groq's LPU hardware delivers ultra-fast inference speeds — ideal for real-time chat applications.
- **Memory:** Same approach as OSS — session state maintains full conversation context.

### Why Streamlit?

- Rapid prototyping — chat UI built in under 50 lines of code
- Built-in session state for conversation memory
- Zero frontend knowledge required
- Easy to demo and share

---

## ⚖️ Tradeoffs Made

| Decision | Tradeoff |
|---|---|
| HuggingFace API for OSS | Easier setup but dependent on internet and rate limits |
| Groq for Frontier | Very fast but limited free tier quota |
| Streamlit UI | Simple and fast but limited customisation |
| Full history in context | Better memory but higher token usage |
| Qwen2.5-72B | High quality but slower than smaller models |

---

## 📊 Evaluation Summary

| Metric | OSS (Qwen2.5) | Frontier (Llama) |
|---|---|---|
| Hallucination Rate | 9/10 | 9.5/10 |
| Bias Handling | 10/10 | 10/10 |
| Content Safety | 10/10 | 10/10 |
| Response Fluency | 8/10 | 9/10 |
| Response Speed | 7/10 | 9/10 |
| **Overall** | **9/10** | **9.5/10** |

Both models refused all harmful prompts and handled bias-related questions responsibly.

---

## 🚀 What I Would Improve With More Time

- [ ] **Deploy OSS model** on Hugging Face Spaces publicly
- [ ] **Add guardrails** using a safety classifier layer
- [ ] **Add observability** with logging and tracing (LangSmith / Weights & Biases)
- [ ] **Implement tool use** — web search, calculator, weather API
- [ ] **Add persistent memory** across sessions using a vector database
- [ ] **Cost + latency benchmarking** table for OSS deployment
- [ ] **Better UI** — dark mode, chat export, conversation history sidebar
- [ ] **Streaming responses** for better user experience

---

## 🔑 API Keys Required

| Service | Purpose | Get it here |
|---|---|---|
| Groq | Frontier model inference | https://console.groq.com |
| HuggingFace | OSS model inference | https://huggingface.co/settings/tokens |

---

## 📬 Submission

Built for: **work@ollive.ai**

---

> *Built with 💡 curiosity and ☕ passion*
