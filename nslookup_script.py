import subprocess

print("""
  
      ฅ^•ﻌ•^ฅ
      Script de busca de ips de vários
      domínios usando nslookup
      By Evs
  
  Esta ferramenta tem como output apenas os ips encontrados.

""")
# Get user input
input_domains = input("Coloque os domínios separados por vírgula: ")
domains = [d.strip() for d in input_domains.split(',') if d.strip()]

print("\n================ IPS ENCONTRADOS ================\n")

for idx, domain in enumerate(domains, 1):
    print(f"[{idx}] Domain: \033[1;34m{domain}\033[0m")
    print("-" * 50)
    try:
        result = subprocess.run(["nslookup", domain], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            in_answer = False
            addresses = []
            for line in result.stdout.splitlines():
                if line.strip().startswith("Non-authoritative answer:"):
                    in_answer = True
                    continue
                if in_answer:
                    if line.strip() == '':
                        break  # End of answer section
                    if line.strip().startswith("Address:"):
                        # Extract only the value after 'Address:'
                        addr = line.strip().split("Address:", 1)[1].strip()
                        addresses.append(addr)
            if addresses:
                for addr in addresses:
                    print(f"\033[1;32m{addr}\033[0m")
            else:
                print("\033[1;33mNenhum IP encontrado.\033[0m")
        else:
            print(f"\033[1;31mErro no domínio: {domain}\033[0m")
    except Exception as e:
        print(f"\033[1;31mException: {e}\033[0m")
    print("\n" + "=" * 50 + "\n") 
    