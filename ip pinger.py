import subprocess
import ipaddress
import threading
import colorama
from pystyle import Colors, Colorate, Center
def ping_host(ip):
    """Esegue un ping su un host IP e determina se è attivo o no."""
    try:
        response = subprocess.run(["ping", "-n", "1", str(ip)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if response.returncode == 0:
            print(f"{ip} è attivo.")
        else:
            print(f"{ip} non è raggiungibile.")
    except Exception as e:
        print(f"Errore durante il ping di {ip}: {e}")

def scan_ip_range(network):
    """Scansiona un range di indirizzi IP in una rete."""
    try:
        net = ipaddress.ip_network(network, strict=False)
        
        for ip in net.hosts():
            threading.Thread(target=ping_host, args=(ip,)).start()
    except ValueError as e:
        print(f"Errore nella rete specificata: {e}")

if __name__ == "__main__":
    network = input("Inserisci la rete da scansionare (es. 192.168.1.0/24): ")
    scan_ip_range(network)
    print(Colorate.Horizontal(Colors.purple_to_blue, f"Press enter to return..."))    
    input()  