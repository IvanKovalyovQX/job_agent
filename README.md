# Job Agent 🤖💼

An automated AI-powered job search agent designed to parse job feeds (DOU, Djinni), evaluate relevant opportunities using OpenAI, generate customized cover letters, and send instant notifications via Telegram.

---

## ✨ Features

- **Automated RSS Job Monitoring**: Fetches job listings from target platforms (DOU, Djinni) for QA Automation, SDET, and QA Lead positions.
- **AI-Powered Evaluation**: Analyzes job descriptions using OpenAI to determine relevance, assign match scores, and structure findings.
- **Cover Letter Generation**: Automatically drafts customized English cover letters for matching vacancies.
- **Telegram Notifications**: Delivers matching job alerts directly to your Telegram chat.
- **Daily Scheduled Execution**: Automated via GitHub Actions cron job every day at 06:00 UTC (with manual trigger support).

---

## 🛠️ Requirements

- **Python 3.11+**
- **OpenAI API Key**
- **Telegram Bot Token** and **Chat ID**

---

## 🚀 Quick Start (Local Setup)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/jobagent.git
   cd jobagent
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```env
   BOT_TOKEN="your_telegram_bot_token"
   OPENAI_API_KEY="your_openai_api_key"
   MY_TELEGRAM_CHAT_ID="your_telegram_chat_id"
   ```

5. **Run the bot**:
   ```bash
   python bot.py
   ```

---

## ⏰ Automated Workflow (GitHub Actions)

The repository includes a GitHub Actions workflow (`.github/workflows/daily_run.yml`) configured to run automatically every day at **06:00 AM UTC**.

### Setting up GitHub Secrets

To enable the automated workflow:
1. Navigate to your repository on GitHub.
2. Go to **Settings** > **Secrets and variables** > **Actions**.
3. Add the following **Repository Secrets**:
   - `BOT_TOKEN`
   - `OPENAI_API_KEY`
   - `MY_TELEGRAM_CHAT_ID`

---

## 📦 Project Structure

```
jobagent/
├── .github/
│   └── workflows/
│       └── daily_run.yml     # Daily GitHub Actions cron workflow
├── bot.py                     # Main application logic
├── requirements.txt           # Project dependencies
├── .env                       # Local environment variables (ignored by git)
└── README.md                  # Project documentation
```
