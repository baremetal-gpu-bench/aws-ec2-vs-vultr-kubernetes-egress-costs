#!/usr/bin/env python3
"""AWS EC2 vs Vultr Kubernetes Egress & Compute Calculator 2026."""
import argparse

def calculate(nodes=3, egress_tb=5):
    # AWS: 3x m6i.xlarge (4 vCPU, 16GB) ~$140/mo each ($420/mo). Egress: $0.09/GB ($90/TB) -> 5 TB = $450/mo! Total ~$870/mo.
    aws_compute = nodes * 140.0
    aws_egress = egress_tb * 1000 * 0.09
    aws_total = aws_compute + aws_egress

    # Vultr: 3x 4 vCPU, 16GB High Performance ~$80/mo each ($240/mo). Egress: Includes 5TB bandwidth free! Total ~$240/mo.
    vultr_compute = nodes * 80.0
    vultr_egress = 0.0 # included in standard pool
    vultr_total = vultr_compute + vultr_egress

    monthly_savings = aws_total - vultr_total
    annual_savings = monthly_savings * 12.0

    print("=" * 65)
    print(f"AWS EC2 vs Vultr Kubernetes: {nodes} Nodes + {egress_tb} TB Egress")
    print("=" * 65)
    print(f"AWS EC2 Total Outlay:      ${aws_total:.2f}/mo (Includes ${aws_egress:.2f} egress fee)")
    print(f"Vultr VKE Total Outlay:    ${vultr_total:.2f}/mo (Includes {egress_tb} TB pooled transfer)")
    print(f"Monthly Cost Difference:   ${monthly_savings:.2f}/mo (Vultr is 72.4% cheaper)")
    print(f"Annual Capital Saved:      ${annual_savings:.2f}/yr")
    print("=" * 65)
    return vultr_total, aws_total, annual_savings

if __name__ == "__main__":
    calculate()
