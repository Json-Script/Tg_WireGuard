import secrets

def generate_wireguard_uri():
    private_key = secrets.token_urlsafe(32)
    public_key = secrets.token_urlsafe(32)  # Placeholder; replace with real public key if needed
    address = "client.cloudflare.com"
    port = 2408
    allowed_ips = "0.0.0.0/0,::/0"

    uri = (
        f"wireguard://{private_key}@{address}:{port}"
        f"?allowed-ips={allowed_ips}&public-key={public_key}"
    )
    return uri
