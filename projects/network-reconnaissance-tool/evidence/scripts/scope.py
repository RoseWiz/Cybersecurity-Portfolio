import json
import ipaddress
from typing import Dict, Any, List

class ScopeError(Exception):
    """Custom exception for invalid or out-of-scope parameters."""
    pass

def load_and_validate_scope(scope_path: str) -> Dict[str, Any]:
    try:
        with open(scope_path, "r") as f:
            data = json.load(f)
    except Exception as e:
        raise ScopeError(f"Failed to read scope file: {e}")

    # Check required fields from the actual lab manifest schema
    required_keys = ["scope_id", "network", "maximum_rate_pps", "maximum_attempts"]
    for key in required_keys:
        if key not in data:
            raise ScopeError(f"Missing required field in scope: {key}")

    # Validate Network CIDR
    try:
        net = ipaddress.ip_network(data["network"], strict=False)
    except ValueError as e:
        raise ScopeError(f"Invalid CIDR notation: {e}")

    # Reject networks broader than /28 (e.g. /24, /16)
    if net.prefixlen < 28:
        raise ScopeError(f"Scope network {data['network']} is broader than allowed /28 maximum.")

    # Rate and Attempt safety checks
    if data.get("maximum_rate_pps", 0) > 20:
        raise ScopeError("Rate limit exceeds maximum allowed 20 probes per second.")
    if data.get("maximum_attempts", 0) > 2:
        raise ScopeError("Max attempts exceeds limit of 2.")

    # Normalize internal dictionary key names for the mapper tool
    return {
        "scope_id": data["scope_id"],
        "target_cidr": str(net),
        "allowed_rate": data["maximum_rate_pps"],
        "max_attempts": data["maximum_attempts"],
        "interface": data.get("interface", "eth0"),
        "raw_manifest": data
    }

def get_target_ips(cidr_str: str) -> List[str]:
    net = ipaddress.ip_network(cidr_str, strict=False)
    # Return all usable host IP addresses in the /28 block
    return [str(ip) for ip in net.hosts()]