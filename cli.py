import functions as fc
from dbmodels import Domain, Credential


def start() -> None:
    try:
        print("\nWelcome to 3P!\n")
        while True:
            print("Enter a command (type 'help' for list): ", end="")
            user_input = input().strip().lower()

            if user_input == "help":
                print(
                    "\nAvailable commands:\n"
                    "  add           - add a domain and login/password\n"
                    "  delete        - delete a domain's login/password\n"
                    "  delete-domain - delete a domain\n"
                    "  show          - show logins/passwords for a domain\n"
                    "  show-domains  - show all domains\n"
                    "  help          - help\n"
                    "  exit          - exit\n"
                )

            elif user_input == "add":
                print("\nEnter domain: ", end="")
                domain = input().strip()
                print("Enter login: ", end="")
                login = input().strip()
                print("Enter password: ", end="")
                password = input().strip()
                fc.add(domain=domain, login=login, password=password)
                print("✅ Data added successfully!\n")

            elif user_input == "delete":
                show_creds()
                print("\nEnter credential ID to delete: ", end="")
                id_cred = input().strip()
                try:
                    fc.delete(id_cred=int(id_cred))
                    print("✅ Deleted!\n")
                except ValueError:
                    print("❌ Invalid ID!\n")

            elif user_input == "delete-domain":
                print("\nEnter domain to delete: ", end="")
                domain_name = input().strip()
                fc.delete_domain(domain_name=domain_name)
                print("✅ Domain deleted!\n")

            elif user_input == "show":
                show_creds()

            elif user_input == "show-domains":
                print("\nDomain list:")
                fc.show_domains()
                print()

            elif user_input == "exit":
                print("👋 Goodbye!")
                break

            else:
                print("❓ Unknown command. Type 'help' for help.\n")
    except KeyboardInterrupt:
        print("\n👋 Shutting down.")


def show_creds():
    print("\nEnter domain: ", end="")
    domain = input().strip()
    creds = fc.search(domain_name=domain)
    if creds is None:
        print("❌ Domain not found.\n")
    elif creds:
        print(f"\nCredentials for domain '{domain}':")
        for cred in creds:
            print(f"  ID: {cred.id} | Login: {cred.login} | Password: {cred.password}")
        print()
    else:
        print(f"❌ No credentials stored for '{domain}'.\n")
