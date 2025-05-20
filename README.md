# 🚀 Welcome to the Ansible Flask App Deployment Demo!

Hi there! 👋

This project is a hands-on, beginner-friendly guide to deploying a Python Flask web app using Ansible and Docker Compose. You'll get to see how automation can make deploying apps across multiple (simulated) servers a breeze—all on your own machine!

---

## 🗂️ What's Inside?

```plaintext
.
├── control/                 # Ansible control node container
│   ├── dockerfile           # Dockerfile for the control node
│   └── full_app/            # Flask app source code
├── worker/                  # Worker node container (simulates a remote Linux host)
│   └── dockerfile
├── inventory/               # Ansible inventory config
├── playbooks/               # Ansible playbooks (automation scripts)
├── docker-compose.yml       # Orchestrates all containers
└── README.md                # ← Start here!
```

---

## ✨ What Can You Do With This?

- 🚦 Deploy a Flask app to 4 separate (containerized) Linux nodes automatically
- 🛠️ Learn how Ansible works in a real-world scenario
- 🐳 Use Docker Compose to spin up everything with one command
- 🧪 Experiment, break things, and learn—risk free!

---

## 🛠️ What You'll Need

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- That's it! (Everything else is handled inside the containers)

---

## 🚦 Quick Start Guide

1. **Clone this repo**
2. **Start everything up:**

   ```bash
   docker-compose up --build
   ```

3. **Open your browser and visit:**
   - [http://localhost:8551](http://localhost:8551)
   - [http://localhost:8552](http://localhost:8552)
   - [http://localhost:8554](http://localhost:8554)
   - [http://localhost:8555](http://localhost:8555)

Each page is served by a different worker node, running its own copy of the Flask app!

---

## 🤖 How Does It Work?

- **Docker Compose** launches:
  - 1 Ansible control node
  - 4 worker containers (like mini Linux servers)
- The control node runs an Ansible playbook that:
  - Creates a user on each worker
  - Copies the Flask app over
  - Installs Python and dependencies
  - Starts the app in the background (no systemd needed!)
- Each worker exposes its own port on your computer

---

## 📝 Extra Notes

- No need to install Python or Ansible on your own machine—they're inside the containers!
- The Ansible inventory is in `inventory/hosts`
- The main playbook is `playbooks/flask_app.yml`
- This is for learning and experimenting—feel free to poke around and modify things!

---

## 🔒 Security Recommendation

**For your safety:**
- If you use this project beyond local testing, please change any default passwords on the worker hosts.
- Review and update the user creation steps in the Ansible playbooks to use secure, unique passwords for each user.
- Never use demo credentials in production environments!

---

## 🙏 License & Thanks

This project is open for learning and demo purposes. Enjoy, and happy automating! 🎉
