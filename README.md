# 🌐 Campus Proxy Lite

A lightweight educational Forward Proxy Simulator built using Flask that demonstrates how domain-based filtering, request logging, and policy enforcement work in network security environments.

## 📌 Project Overview

Campus Proxy Lite simulates the behavior of a forward proxy by acting as an intermediary between the user and a website.

Before allowing access to a website, the system:

1. Receives the requested URL.
2. Extracts the domain name.
3. Checks whether the domain exists in the blocked list.
4. Logs the request.
5. Either:

   * Redirects the user to the destination website.
   * Displays an Access Denied page if the domain is blocked.

This project was developed as a hands-on learning exercise to understand Forward Proxies, Domain Filtering, Logging Systems, and Web Security Concepts.

---

## 🚀 Features

### User Features

* Enter any website URL.
* Access allowed websites.
* Receive a custom Access Denied page for blocked domains.

### Admin Features

* View blocked domains.
* Add new blocked domains.
* Remove blocked domains.
* View recent request logs.

### Security Features

* Domain-based filtering.
* Request logging.
* Policy enforcement.
* Administrative control over blocked websites.

---

## 🏗️ Architecture

```text
User
 │
 ▼
Campus Proxy Lite
 │
 ▼
Domain Extraction
 │
 ▼
Policy Check
 │
 ┌───────────────┴───────────────┐
 │                               │
Blocked                       Allowed
 │                               │
 ▼                               ▼
Access Denied              Redirect User
```

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask

### Libraries

* tldextract
* JSON
* Datetime

### Frontend

* HTML5
* CSS3
* Glassmorphism UI
* CSS Animations

### Storage

* JSON File
* Text Log File

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/sahithimeneni06/CampusProxy-lite.git
cd campus-proxy-lite
```

### Install Dependencies

```bash
pip install flask tldextract
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## 📋 How It Works

### Allowed Website

Example:

```text
google.com
```

Workflow:

```text
User Request
      │
      ▼
Check Block List
      │
      ▼
Not Blocked
      │
      ▼
Log Request
      │
      ▼
Redirect to Website
```

---

### Blocked Website

Example:

```text
instagram.com
```

Workflow:

```text
User Request
      │
      ▼
Check Block List
      │
      ▼
Blocked
      │
      ▼
Log Request
      │
      ▼
Access Denied Page
```

---

## 📝 Request Logging

All requests are stored in:

```text
logs.txt
```

Example:

```text
2026-06-14 10:30:15 | google.com | ALLOWED
2026-06-14 10:31:42 | instagram.com | BLOCKED
```

---

## 🎯 Learning Outcomes

This project demonstrates:

* Forward Proxy Concepts
* HTTP Request Flow
* Domain Filtering
* Policy Enforcement
* Traffic Logging
* Flask Web Development
* Network Security Fundamentals

---

## 📚 Educational Purpose

This project is intended for educational purposes to understand how forward proxies perform request inspection and domain-based filtering. It does not intercept, monitor, or control third-party network traffic.

---
