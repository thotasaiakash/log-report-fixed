The file /app/access.log contains an Apache combined-format access log. Parse it and
write a JSON report to /app/report.json containing exactly these three keys:

  "total_requests"  - integer, total number of log lines
  "unique_ips"      - integer, number of distinct client IP addresses
  "top_path"        - string, the URL path with the most requests

The report must be a single JSON object with no extra keys. If two paths tie for most
requests, return either one.

Success criteria:
1. /app/report.json exists.
2. /app/report.json contains valid JSON.
3. "total_requests" is the correct integer count of log lines.
4. "unique_ips" is the correct integer count of distinct client IPs.
5. "top_path" is the correct string for the most-requested path.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
