import time
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional
from scapy.all import Ether, ARP, srp, conf

class DeviceMapper:
    def __init__(self, scope_config: Dict[str, Any], interface: Optional[str] = None):
        self.scope_id = scope_config["scope_id"]
        self.cidr = scope_config.get("target_cidr") or scope_config.get("network", "172.28.70.0/28")
        self.rate_limit = min(scope_config.get("allowed_rate", scope_config.get("maximum_rate_pps", 20)), 20)
        self.max_attempts = min(scope_config.get("max_attempts", scope_config.get("maximum_attempts", 2)), 2)
        # Use provided interface, fallback to scope interface, or fallback to Scapy default interface on host
        self.interface = interface or scope_config.get("interface")

    def plan_scan(self, target_ips: List[str]) -> Dict[str, Any]:
        """Dry-run execution planner (does not transmit packets)."""
        return {
            "mode": "dry-run",
            "scope_id": self.scope_id,
            "target_cidr": self.cidr,
            "total_targets": len(target_ips),
            "target_ips": target_ips,
            "estimated_duration_sec": round(len(target_ips) * self.max_attempts * (1.0 / self.rate_limit if self.rate_limit > 0 else 0.05), 2),
            "rate_limit_pps": self.rate_limit,
            "max_attempts": self.max_attempts
        }

    def execute_scan(self, target_ips: List[str]) -> Dict[str, Any]:
        """Constructs ARP probes, transmits with bounded rate, deduplicates responses."""
        utc_start = datetime.now(timezone.utc).isoformat()
        observations: Dict[str, Dict[str, Any]] = {}
        interval = 1.0 / self.rate_limit if self.rate_limit > 0 else 0.05

        # Determine effective interface safely for Windows vs Linux host
        kwargs = {}
        if self.interface:
            try:
                conf.ifaces.dev_from_name(self.interface)
                kwargs["iface"] = self.interface
            except ValueError:
                # Interface string (e.g. eth0) not found on Windows host; use Scapy default interface
                pass

        for attempt in range(1, self.max_attempts + 1):
            for ip in target_ips:
                packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
                
                ans, _ = srp(packet, timeout=0.5, verbose=False, **kwargs)
                send_time = datetime.now(timezone.utc).isoformat()

                for sent, rcv in ans:
                    src_ip = rcv.psrc
                    src_mac = rcv.hwsrc
                    
                    if src_ip not in observations:
                        observations[src_ip] = {
                            "status": "observed",
                            "mac_address": src_mac,
                            "observation_count": 1,
                            "first_seen": send_time,
                            "last_seen": send_time
                        }
                    else:
                        observations[src_ip]["observation_count"] += 1
                        observations[src_ip]["last_seen"] = send_time

                time.sleep(interval)

        results = []
        for ip in target_ips:
            if ip in observations:
                results.append({"ip": ip, **observations[ip]})
            else:
                results.append({
                    "ip": ip,
                    "status": "not observed",
                    "mac_address": None,
                    "observation_count": 0,
                    "first_seen": None,
                    "last_seen": None
                })

        utc_end = datetime.now(timezone.utc).isoformat()

        return {
            "metadata": {
                "tool_version": "1.0.0",
                "option": "Option A: Device Mapper",
                "scope_id": self.scope_id,
                "target_cidr": self.cidr,
                "utc_window": {"start": utc_start, "end": utc_end},
                "parameters": {
                    "rate_limit_pps": self.rate_limit,
                    "max_attempts": self.max_attempts,
                    "interface": self.interface or str(conf.iface)
                }
            },
            "results": results
        }