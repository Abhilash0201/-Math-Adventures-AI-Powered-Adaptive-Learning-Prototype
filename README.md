# 🎯 Math Adventures — AI-Powered Adaptive Learning Prototype (Streamlit)

An **AI-powered adaptive math learning web app** built with **Streamlit**, designed to help kids (ages 5–10) practice math at an appropriate difficulty level that **adapts automatically** based on their performance.

This is the **fixed version** (Streamlit ≥ 1.38 compatible), replacing `st.experimental_rerun()` with `st.rerun()`.

---

## 🚀 Overview

**Math Adventures** dynamically adjusts question difficulty as the learner answers problems.
The goal is to create a fun, real-world–style adaptive learning experience similar to apps like *Khan Academy Kids* or *Prodigy*, but with a lightweight and interpretable backend.

### 🧠 Core Features

* **Dynamic puzzle generation:** Random arithmetic questions (Addition, Subtraction, Multiplication, Division)
* **Adaptive difficulty:** Adjusts between *Easy*, *Medium*, and *Hard* levels
* **Performance tracking:** Logs accuracy, response time, and per-level statistics
* **Simple rule-based adaptive engine** (default) or **optional ML-driven mode**
* **Session summary dashboard:** Displays user performance insights
* **Streamlit web interface:** Ready-to-run interactive learning UI

---

## 📂 Project Structure

```
math-adaptive-prototype-fixed/
├─ README.md
├─ requirements.txt
├─ src/
│  ├─ main.py                # Streamlit app entry point
│  ├─ puzzle_generator.py    # Generates math problems
│  ├─ tracker.py             # Tracks user progress and stats
│  ├─ adaptive_engine.py     # Adaptive difficulty logic
└─ (optional: docs folder if you add tech notes)
```

---

## 🧰 Tech Stack

| Component           | Technology                         |
| ------------------- | ---------------------------------- |
| Frontend            | Streamlit                          |
| Backend Logic       | Python                             |
| Data Handling       | Pandas, Numpy                      |
| ML Model (optional) | Logistic Regression (scikit-learn) |
| Deployment Ready    | Yes — Streamlit Cloud / Localhost  |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone or extract the ZIP

If you downloaded the ZIP:

```bash
unzip math-adaptive-prototype-fixed.zip
cd math-adaptive-prototype-fixed
```

Or if hosted on GitHub:

```bash
git clone https://github.com/yourusername/math-adaptive-prototype.git
cd math-adaptive-prototype
```

---

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application

```bash
streamlit run src/main.py
```

Then open the provided **local URL** in your browser
(e.g., [http://localhost:8501](http://localhost:8501))

---

## 🕹️ How It Works

### Step-by-Step Flow:

1. **Enter your name** and choose an initial difficulty.
2. Click **“Generate Next Puzzle”** to start.
3. Solve the math problem shown.
4. The system measures:

   * Whether the answer was correct
   * How long you took to respond
5. The **adaptive engine** updates your next question’s difficulty level:

   * High accuracy + fast answers → increase difficulty
   * Many errors or slow responses → decrease difficulty
6. Click **“Show Summary”** anytime to review:

   * Total attempts
   * Accuracy %
   * Average response time
   * Stats per difficulty level

---

## 🧩 Adaptive Engine Logic

### 🔹 Rule-Based Mode (Default)

Uses simple transparent heuristics:

* **Increase level** if accuracy ≥ 80% and avg response time < 10s
* **Decrease level** if accuracy ≤ 50% or avg time > 15s
* **Otherwise stay** at current difficulty

### 🔹 ML-Based Mode (Optional)

A small synthetic dataset trains a **Logistic Regression model** to predict whether the next question should go *up*, *down*, or *stay*.
This is purely for demonstration of a data-driven approach — no large dataset required.

---

## 📊 Performance Summary Example

| Metric            | Example |
| ----------------- | ------- |
| Total Attempts    | 15      |
| Correct Answers   | 12      |
| Accuracy          | 80%     |
| Avg Response Time | 8.3s    |
| Easy Accuracy     | 100%    |
| Medium Accuracy   | 75%     |
| Hard Accuracy     | 50%     |

---

## 🖥️ Deployment Options

| Method              | Description                              |
| ------------------- | ---------------------------------------- |
| **Localhost**       | Run via `streamlit run src/main.py`      |
| **Streamlit Cloud** | Upload repository → “Deploy”             |
| **Heroku / Render** | Add `Procfile` and deploy as web service |

---

## 🧩 Future Enhancements

* 🎨 Custom UI theme (cartoon-style for kids)
* 🧑‍🏫 User authentication (to save progress)
* 🧮 Expanded question sets (fractions, word problems)
* 📈 ML-driven personalization using real performance data
* 💾 Local SQLite database for persistent storage

---

## 🏁 Author & Credits

**Developer:** Abhilash
**Based on:** Adaptive Learning Assignment Specification
**Built with:** ❤️ Python, Streamlit, and Scikit-learn

---

## 📜 License

MIT License — free for academic or demonstration use.
