# Simple Python App CI with GitHub Actions

🚀 Day 4 of my “Build → Test → Deploy: Daily” challenge!

This repository contains a basic Flask application integrated with a CI workflow using GitHub Actions.

## 🔧 What This Workflow Does

- Checks out the code.
- Sets up Python 3.13.3 with pip cache.
- Installs dependencies from `requirements.txt`.
- Runs unit tests (`test_app.py`).
- Starts the Flask app in the background.
- Performs a `curl` request to ensure the app is responding.
- Stops the Flask app.
- Sends an email notification on build **success** or **failure** using SMTP.

## ⚙️ Requirements

- A Gmail account with App Passwords enabled (for email notifications).
- GitHub repository secrets set:
  - `MAIL_USERNAME`
  - `MAIL_PASSWORD`

## 📬 Email Notifications

The workflow sends a success or failure email to `mohammedadilrehan@gmail.com` using the [dawidd6/action-send-mail](https://github.com/dawidd6/action-send-mail) GitHub Action.

## 🚀 How to Use

1. Clone the repo.
2. Update `requirements.txt`, `app.py`, and `test_app.py` as needed.
3. Push changes to trigger the workflow.

---

Happy Building! 🛠️

