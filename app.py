from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

import json
from datetime import datetime
import tldextract

app = Flask(__name__)

def load_blocked_domains():
    with open("blocked_domains.json", "r") as file:
        return json.load(file)
def get_domain(url):

    extracted = tldextract.extract(url)

    if extracted.suffix:
        return f"{extracted.domain}.{extracted.suffix}"

    return extracted.domain

def log_request(domain, status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = (f"{timestamp} | {domain} | {status}\n")
    with open("logs.txt", "a") as f:
        f.write(log_entry)

def save_blocked_domains(domains):
    with open("blocked_domains.json", "w") as f:
        json.dump(domains, f, indent=4)
def load_logs():
    try:
        with open("logs.txt", "r") as f:
            return f.readlines()[::-1]
    except:
        return []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/proxy", methods=["POST"])
def proxy():

    url = request.form.get("url")

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    domain = get_domain(url)

    blocked_domains = load_blocked_domains()

    if domain in blocked_domains:

        log_request(
            domain,
            "BLOCKED"
        )

        return render_template(
            "blocked.html",
            domain=domain
        )

    log_request(
        domain,
        "ALLOWED"
    )

    return redirect(url)


@app.route("/admin")
def admin():
    domains = load_blocked_domains()
    logs = load_logs()
    return render_template("admin.html", domains=domains, logs = logs)

@app.route("/add-domain", methods=["POST"])
def add_admin():
    domain = request.form.get("domain").lower()
    domains = load_blocked_domains()
    if domain not in domains:
        domains.append(domain)
        save_blocked_domains(domains)
    return redirect("/admin")

@app.route("/remove-domain/<domain>")
def remove_domain(domain):
    domains = load_blocked_domains()
    if domain in domains:
        domains.remove(domain)
        save_blocked_domains(domains)
    return redirect("/admin")



if __name__=="__main__":
    app.run(debug=True)