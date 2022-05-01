import re

ip_address_list = ['11.16.211.2', '133.1.1.111', '201.22.3.41', '17.55.23.123', '144.211.32.45']

class_a_regex = r"^([1-9]?\d|1[01]\d|12[0-7])(\.([1-9]?\d|[12]\d\d)){3}$"
class_b_regex = r"^(12[89]|1[3-8]\d|19[01])(\.([1-9]?\d|[12]\d\d)){3}$"
class_c_regex = r"^(19[2-9]|2[01]\d|22[0-3])(\.([1-9]?\d|[12]\d\d)){3}$"

matches = []

class_string_a = " Class A "
class_string_b = " Class B "
class_string_c = " Class C "


def get_host(a_match, class_string):
    if class_string == class_string_a:
        final_match = a_match[a_match.find(".") + 1:]

    if class_string == class_string_b:
        final_match = a_match[a_match.find(".", a_match.find(".") + 1) + 1:]

    if class_string == class_string_c:
        final_match = a_match[a_match.rfind(".") + 1:]


    return final_match


def append_matches(match, class_string):
    try:
        match = match.group()
        if match:
            matches.append(match + class_string + get_host(match, class_string))
    except:
        pass



for address in ip_address_list:
    match_a = re.match(class_a_regex, address)
    match_b = re.match(class_b_regex, address)
    match_c = re.match(class_c_regex, address)

    append_matches(match_a, class_string_a)
    append_matches(match_b, class_string_b)
    append_matches(match_c, class_string_c)


for item in matches:
    print(item)
