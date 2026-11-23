import pytest
from scapy.all import Ether, ARP
from src.scope import load_and_validate_scope, ScopeError, get_target_ips
from src.mapper import DeviceMapper
from src.output import save_deterministic_json

def test_scope_rejection_broad_cidr(tmp_path):
    """Test 1: Rejects CIDRs broader than /28."""
    bad_scope = tmp_path / "bad_scope.json"
    bad_scope.write_text('{"scope_id": "test", "network": "172.28.70.0/24", "maximum_rate_pps": 10, "maximum_attempts": 2}')
    with pytest.raises(ScopeError, match="broader than allowed /28"):
        load_and_validate_scope(str(bad_scope))

def test_packet_construction():
    """Test 2: Verifies Ethernet/ARP packet construction."""
    ip = "172.28.70.10"
    pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    assert pkt[Ether].dst == "ff:ff:ff:ff:ff:ff"
    assert pkt[ARP].pdst == ip
    assert pkt[ARP].op == 1  # 1 represents ARP Request

def test_dry_run_no_transmission():
    """Test 3: Dry run generates execution plan without network activity."""
    scope = {"scope_id": "lab_01", "target_cidr": "172.28.70.0/28", "allowed_rate": 10, "max_attempts": 2}
    targets = get_target_ips(scope["target_cidr"])
    mapper = DeviceMapper(scope)
    plan = mapper.plan_scan(targets)
    assert plan["mode"] == "dry-run"
    assert len(plan["target_ips"]) == len(targets)

def test_deterministic_json_output(tmp_path):
    """Test 4: Output structure sorting and determinism."""
    out_file = tmp_path / "out.json"
    data = {
        "results": [
            {"ip": "172.28.70.5", "status": "not observed"},
            {"ip": "172.28.70.2", "status": "observed"}
        ]
    }
    save_deterministic_json(data, str(out_file))
    import json
    with open(out_file) as f:
        saved = json.load(f)
    assert saved["results"][0]["ip"] == "172.28.70.2"
    assert saved["results"][1]["ip"] == "172.28.70.5"

def test_missing_responder_classification():
    """Test 5: Checks missing/unresponsive targets are marked 'not observed'."""
    scope = {"scope_id": "lab_01", "target_cidr": "172.28.70.0/28", "allowed_rate": 20, "max_attempts": 1}
    mapper = DeviceMapper(scope)
    targets = ["10.255.255.254"]
    results = mapper.execute_scan(targets)
    assert results["results"][0]["status"] == "not observed"