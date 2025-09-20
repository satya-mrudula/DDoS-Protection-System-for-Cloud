class Mitigation:
    def __init__(self):
        self.blocked_ips = set()

    def block_ip(self, ip):
        self.blocked_ips.add(ip)
