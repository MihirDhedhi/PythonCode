hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"

websites = [
    "www.facebook.com",
    "facebook.com",
    "www.youtube.com",
    "youtube.com"
]

with open(hosts_path, 'r+') as file:
    content = file.read()
    for site in websites:
        if site not in content:
            file.write(f"{redirect} {site}\n")
            print(f"Blocked: {site}")
        else:
            print(f"Already blocked: {site}")

print("Website blocking complete ✅")
