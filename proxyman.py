# Copied from: https://github.com/ProxymanApp/Proxyman/issues/1220#issuecomment-1249090359
# Usage: https://docs.proxyman.io/debug-devices/python#2.-old-solution-not-recommended
# Proxyman: Certificate -> Export -> Root Certificate as PEM...
# Save that file to certs folder
# Inside venv
# $ python proxyman.py add
# Requests will not proxy through Proxyman
# python proxyman.py remove
# Requests will no longer proxy through Proxyman

try:
    from certifi import where
except ModuleNotFoundError:
    exit('Please run "pip install certifi"')
from re import findall, match
from argparse import ArgumentParser

RE_CERT = r"-----BEGIN\ CERTIFICATE-----\n[A-Za-z0-9\/\+\n=]{1,}-----END\ CERTIFICATE-----\n"

def read_certifi(certifi_path:str) -> str:
    """Returns the content of cacert.pem of certifi"""
    with open(certifi_path, "r") as read:
        certifi_content = read.read()
    return certifi_content

def merge_cert(certifi_path:str, content:str) -> None:
    """Adds the content of Proxyman certificate to cacert.pem"""
    with open(certifi_path, "a") as append:
        # Appends the proxyman cert with "# Proxyman Root Certificate" written over
        # so we can find it back with regex
        append.write(f"\n# Proxyman Root Certificate\n{content}\n")
    print("Proxyman certificate succesfully added.")

def remove_cert(certifi_path:str) -> None:
    """Removes the Proxyman certificate of the cacert.pem"""
    certifi_content = read_certifi(certifi_path=certifi_path)
    proxyman_lines = findall(
        r"\n#\ Proxyman\ Root\ Certificate\n" + RE_CERT,
        certifi_content
    ) # Finds back the content of the previously added proxyman cert with regex
    
    if not proxyman_lines:
        exit("Proxyman certificate have not been added to your python certificates yet.")
    
    new_certifi_content = certifi_content.replace(proxyman_lines[0], "")
    
    # while there's two breakline at the end, we remove the last one
    while new_certifi_content[-2:] == "\n\n":
        new_certifi_content = new_certifi_content[:-1]

    with open(certifi_path, "w") as write:
        write.write(new_certifi_content)
    print("Proxyman certificate removed succesfully.")

def read_proxyman_cert(path: str) -> str:
    """Reads and return in str the content of the input certificate"""
    try:
        print(path)
        with open(path, "r") as read:
            content = read.read()
    except FileNotFoundError:
        exit("Please make sure the path to the exported Proxyman certificate is the right one.")
    return content

def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("action", choices=["add", "remove"], help="choose to add or remove the proxyman certificate from your python certificates")
    action = parser.parse_args().action

    certifi_path = where()
    if action == "add":
        print('Open Proxyman, go to "Certificate" -> "Export" -> "Root Certificate as PEM..." and save it somewhere.')
        proxyman_cert_path = input("Paste the path to the exported Certificate -> ")

        # Steps to verify if the cert is in great format and all to avoid
        # merging a shopping list or idk what to the certificates
        if len(proxyman_cert_path) < 4:
            exit("Invalid path.")

        if proxyman_cert_path.endswith((".pem'", '.pem"')):
            proxyman_cert_path = proxyman_cert_path[1:-1]
        if not proxyman_cert_path.endswith(".pem"):
            exit('The path must be pointing to a ".pem" certificate.')
        proxyman_cert_content = read_proxyman_cert(path=proxyman_cert_path)
        if not match(RE_CERT, proxyman_cert_content):
            exit(f'Invalid ".pem" file content (not matching re"{RE_CERT}").')

        # Checks if the certificate is already present in the certificate list
        if proxyman_cert_content in read_certifi(certifi_path=certifi_path):
            exit("This certificate is already present in certifi certificates.")

        # If it is all good, merge
        merge_cert(certifi_path=certifi_path, content=proxyman_cert_content)

    elif action == "remove":
        remove_cert(certifi_path=certifi_path)

if __name__ == "__main__":
    main()