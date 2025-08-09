import requests

LIST_MAILS_URL = "https://myapis.tr.ht/api.php?action=get-mail"
CHECK_MAIL_URL = "https://myapis.tr.ht/api.php?action=check-mail&token="

def list_emails():
    response = requests.get(LIST_MAILS_URL)
    data = response.json()

    if "emails" not in data:
        print("No email data found.")
        return []

    emails = data["emails"]
    print(f"\n{data.get('message', 'Available emails:')}\n")
    for idx, email in enumerate(emails):
        print(f"{idx + 1}. {email['email']}")

    return emails

def select_email(emails):
    while True:
        try:
            choice = int(input("\nSelect an email number: "))
            if 1 <= choice <= len(emails):
                return emails[choice - 1]
            else:
                print("Invalid choice.")
        except ValueError:
            print("Enter a valid number.")

def check_mail(token):
    url = CHECK_MAIL_URL + token
    response = requests.get(url)
    data = response.json()

    print("\n📬 Mail Details:")
    print(f"From   : {data.get('from', 'N/A')}")
    print(f"Subject: {data.get('subject', 'N/A')}")
    print(f"Body   :\n{data.get('body', 'No content.')}\n")

def main():
    emails = list_emails()
    if not emails:
        return

    selected = select_email(emails)
    print(f"\nSelected: {selected['email']}")
    check_mail(selected['token'])

if __name__ == "__main__":
    main()
