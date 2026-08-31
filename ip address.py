# coded by N17RO (noob hackers)

import argparse
import requests
import sys
import ipaddress

# arguments and parser
parser = argparse.ArgumentParser(
    description="IP information lookup tool"
)

parser.add_argument(
    "-v",
    help="target/host IP address",
    type=str,
    dest="target",
    required=True
)

args = parser.parse_args()

# colours
red = "\033[31m"
yellow = "\033[93m"
lgreen = "\033[92m"
clear = "\033[0m"
bold = "\033[01m"
cyan = "\033[96m"

# banner
print(red + r"""
██╗██████╗ ██████╗ ██████╗  ██████╗ ███╗   ██╗███████╗
██║██╔══██╗██╔══██╗██╔══██╗██╔═══██╗████╗  ██║██╔════╝
██║██████╔╝██║  ██║██████╔╝██║   ██║██╔██╗ ██║█████╗
██║██╔═══╝ ██║  ██║██╔══██╗██║   ██║██║╚██╗██║██╔══╝
██║██║     ██████╔╝██║  ██║╚██████╔╝██║ ╚████║███████╗
╚═╝╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                      v 1.0
""" + clear)

print(
    lgreen + bold +
    "         <===[[ coded by NOX ]]===>\n" +
    clear
)

print(
    yellow + bold +
    "   <---(( search on youtube uw1.c ))--->\n" +
    clear
)

ip = args.target.strip()

# check IP format
try:
    ip_obj = ipaddress.ip_address(ip)
except ValueError:
    print(red + "[~] Invalid IP address!" + clear)
    sys.exit(1)

# private/local IP check
if ip_obj.is_private:
    print(yellow + "[!] This is a private/local IP address." + clear)
    print(yellow + "[!] Public ISP/location information is not available for it." + clear)
    print(yellow + "[!] Example: 192.168.x.x, 10.x.x.x, 172.16.x.x" + clear)
    sys.exit(0)

api = "http://ip-api.com/json/"

try:
    response = requests.get(
        api + ip,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    # API status check
    if data.get("status") != "success":
        print(
            red +
            "[~] API Error: " +
            str(data.get("message", "Unknown error")) +
            clear
        )
        sys.exit(1)

    a = lgreen + bold + "[$]"
    b = cyan + bold + "[$]"

    print(a, "[Victim]:", data.get("query", "N/A"))
    print(red + "<--------------->" + clear)

    print(b, "[ISP]:", data.get("isp", "N/A"))
    print(red + "<--------------->" + clear)

    print(a, "[Organisation]:", data.get("org", "N/A"))
    print(red + "<--------------->" + clear)

    print(b, "[City]:", data.get("city", "N/A"))
    print(red + "<--------------->" + clear)

    print(a, "[Region]:", data.get("regionName", "N/A"))
    print(red + "<--------------->" + clear)

    print(b, "[Longitude]:", data.get("lon", "N/A"))
    print(red + "<--------------->" + clear)

    print(a, "[Latitude]:", data.get("lat", "N/A"))
    print(red + "<--------------->" + clear)

    print(b, "[Time zone]:", data.get("timezone", "N/A"))
    print(red + "<--------------->" + clear)

    print(a, "[Zip code]:", data.get("zip", "N/A"))
    print(clear)

except requests.exceptions.Timeout:
    print(red + "[~] Request timed out!" + clear)
    sys.exit(1)

except requests.exceptions.ConnectionError:
    print(red + "[~] Check your internet connection!" + clear)
    sys.exit(1)

except requests.exceptions.RequestException as e:
    print(red + "[~] Request error:", str(e) + clear)
    sys.exit(1)

except KeyboardInterrupt:
    print("\n" + yellow + "Terminating, Bye!" + clear)
    sys.exit(0)

except ValueError:
    print(red + "[~] Invalid response from API!" + clear)
    sys.exit(1)