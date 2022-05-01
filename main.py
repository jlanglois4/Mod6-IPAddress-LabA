import re

ip_address_list = ['11.16.211.2', '133.1.1.111', '201.22.3.41', '17.55.23.123', '144.211.32.45']

class_a_regex = r"^([1-9]?\d|1[01]\d|12[0-7])(\.([1-9]?\d|[12]\d\d)){3}$"
class_b_regex = r"^(12[89]|1[3-8]\d|19[01])(\.([1-9]?\d|[12]\d\d)){3}$"
class_c_regex = r"^(19[2-9]|2[01]\d|22[0-3])(\.([1-9]?\d|[12]\d\d)){3}$"

matches = []

for address in ip_address_list:
    match_a = re.match(class_a_regex, address)
    match_b = re.search(class_b_regex, address)
    match_c = re.search(class_c_regex, address)

    if match_a:
        matches.append(match_a.group() + " Class A")
    if match_b:
        matches.append(match_b.group() + " Class B")
    if match_c:
        matches.append(match_c.group() + " Class C")

for item in matches:
    print(item)
