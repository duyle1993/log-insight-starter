log_file = "sample.log"
ip_counts = {}
total_failed_attempts = 0

with open(log_file, "r") as file:
    logs = file.readlines()

for line in logs:
    if "Failed password" in line:
        total_failed_attempts += 1
        parts = line.split("from ")
        if len(parts) > 1:
            ip_address = parts[1].split()[0]

            if ip_address in ip_counts:
                ip_counts[ip_address] += 1
            else:
                ip_counts[ip_address] = 1

print("=" * 50)
print("        LOG INSIGHT STARTER REPORT")
print("=" * 50)
print(f"Total Failed Login Attempts: {total_failed_attempts}")
print(f"Unique Suspicious IPs: {len(ip_counts)}")
print("-" * 50)

for ip, count in ip_counts.items():
    if count >= 2:
        risk = "High Risk"
    else:
        risk = "Low Risk"

    print(f"IP Address: {ip}")
    print(f"Failed Attempts: {count}")
    print(f"Risk Level: {risk}")
    print("-" * 50)