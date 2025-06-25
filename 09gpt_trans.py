from deep_translator import GoogleTranslator

#output
def google_trans(messages):
    result = GoogleTranslator(source='auto', target='ko').translate(messages)
    return result

#input
text = f'''
Mamdani Stuns Cuomo in N.Y.C. Mayoral Primary, as Ex-Governor Concedes
Zohran Mamdani, a 33-year-old state assemblyman, built a significant lead over former Gov. Andrew Cuomo, who conceded the race. Mr. Cuomo left the door open to running in the general election.
'''

result = google_trans(text)
print(result)