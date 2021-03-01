import re

phoneNumRegex = re.compile(r'(\d\d\d-)?(\d\d\d-)(\d\d\d\d)')
mo = phoneNumRegex.search("My number is 415-555-1234")
print(f'{mo.group(1)}{mo.group(2)}{mo.group(3)}')
mo = phoneNumRegex.search("My number is 555-4321")
print(f'{mo.group()}')

batRegex = re.compile(r'Bat(wo)?man')

mo = batRegex.search("The adventures of Batman")
print(mo.group())
mo = batRegex.search("The adventures of Batwoman")
print(mo.group())

agent_text = 'Agent Alice gave the secret document to Agent Bob.'

namesRegex = re.compile(r'Agent \w+')
namesRegex.findall(agent_text)
print(namesRegex.sub('REDACTED', agent_text))

namesRegex = re.compile(r'Agent (\w)\w*')
namesRegex.findall(agent_text)
print(namesRegex.sub(r'Agent \1****', agent_text))
