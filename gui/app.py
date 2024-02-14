from appJar import gui

app = gui("My first GUI", "200x150")

def rate():
   match app.getRadioButton("rating"):
       case "1":
         app.setLabel("rating", "Ouch")
       case "2":
         app.setLabel("rating", "Ooh...")
       case "3":
         app.setLabel("rating", "Thats fair")
       case "4":
         app.setLabel("rating", "Better than I expected")
       case "5":
         app.setLabel("rating", "Hell yeah!!")

app.addLabel("title", "How do you rate this application?")

for i in ["1", "2", "3", "4", "5"]:
    app.addRadioButton("rating", i)

app.setRadioButtonChangeFunction("rating", rate)

app.addLabel("rating", "")

app.go()