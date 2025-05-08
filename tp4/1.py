import os
import platform

class Ping:
    def execute(self, ip: str):
        if ip.startswith("192."):
            print(f"[Ping] Ejecutando ping a {ip} con control de dirección:")
            for i in range(10):
                print(f" Intento {i + 1}:")
                os.system(self._get_ping_command(ip))
        else:
            print(f"[Ping] Dirección IP no permitida: {ip}")

    def executefree(self, ip: str):
        print(f"[Ping] Ejecutando ping libre a {ip} (sin control):")
        for i in range(10):
            print(f" Intento {i + 1}:")
            os.system(self._get_ping_command(ip))

    def _get_ping_command(self, ip: str):
        # Usa el comando correcto según el sistema operativo
        if platform.system().lower() == "windows":
            return f"ping -n 1 {ip}"
        else:
            return f"ping -c 1 {ip}"


class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip: str):
        if ip == "192.168.0.254":
            print("[PingProxy] IP especial detectada, reenviando a www.google.com con ping libre.")
            self.ping.executefree("www.google.com")
        else:
            print("[PingProxy] Reenviando a Ping normal.")
            self.ping.execute(ip)


# Ejemplo de uso:
if __name__ == "__main__":
    ip_input = input("Ingresá la dirección IP: ").strip()
    proxy = PingProxy()
    proxy.execute(ip_input)
