import sys
import argparse
from src.scope import load_and_validate_scope, get_target_ips, ScopeError
from src.mapper import DeviceMapper
from src.output import save_deterministic_json

def main():
    parser = argparse.ArgumentParser(description="WQE7002 Option A Device Mapper")
    parser.add_argument("--scope", required=True, help="Path to scope JSON file")
    parser.add_argument("--output", required=True, help="Path to output result JSON file")
    parser.add_argument("--interface", default="eth0", help="Network interface")
    parser.add_argument("--execute", action="store_true", help="Explicit execution flag (transmits probes)")

    args = parser.parse_args()

    try:
        scope_data = load_and_validate_scope(args.scope)
        target_ips = get_target_ips(scope_data["target_cidr"])
        mapper = DeviceMapper(scope_data, interface=args.interface)

        if not args.execute:
            print("[*] PLAN / DRY-RUN MODE (No packets sent)")
            plan = mapper.plan_scan(target_ips)
            save_deterministic_json(plan, args.output)
            print(f"[+] Dry-run plan saved to {args.output}")
            sys.exit(0)

        print("[*] EXECUTING LIVE ARP DEVICE MAPPER...")
        results = mapper.execute_scan(target_ips)
        save_deterministic_json(results, args.output)
        print(f"[+] Execution completed. Results saved to {args.output}")

    except ScopeError as se:
        print(f"[-] SCOPE ERROR: {se}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[-] UNEXPECTED ERROR: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()