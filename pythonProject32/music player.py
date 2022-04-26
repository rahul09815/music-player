from playsound import playsound
playsound("C:\\Users\\rt098\\Downloads\\free fire.mp3")
print("no of available songs\n1.free fire.\n2.believer\n3.grateful")
order =input("enter the music you want youn play")
if "free fire" in order:
    playsound("C:\\Users\\rt098\\Downloads\\free fire.mp3")
elif"believer" in order:
    playsound("C:\\Users\\rt098\\Downloads\\believer.mp3")
elif"greatful" in order:
    playsound("C:\\Users\\rt098\\Downloads\\greatful.mp3")

