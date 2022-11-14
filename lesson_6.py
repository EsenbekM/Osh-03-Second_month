import re

# Regular Expression \ RegExp

text = 'AV Analytics Vidhya AV'

# result = re.match(r'AV', text)
# print(result)
#
# result = re.search(r'Analytics', text)
# print(result)
#
#
# result = re.findall(r'AV', text)
# print(result)
#
#
# result = re.split(r'Analytics', text)
# print(result)
#
# result = re.sub(r' ', r'_', text)
# print(result)
#
# result = re.sub(r'a', r'o', text)
# print(result)

with open("test_regs.txt", "r", encoding='utf-8') as file:
    content = file.read()
    # print(content)
    beeline_number_list = re.findall(r"\+996 (?:77\d|22\d) [\d ]{8}", content)
    print(len(beeline_number_list))
    print(beeline_number_list)

    megacom_number_list = re.findall(r"\+996 (?:55\d|99\d|755) [\d ]{8}", content)
    print(len(megacom_number_list))
    print(megacom_number_list)

    nur_telecom_number_list = re.findall(r"\+996 (?:50\d|70\d) [\d ]{8}", content)
    print(len(nur_telecom_number_list))
    print(nur_telecom_number_list)

