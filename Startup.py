import Functions as f


scripts = ["Clone"]
print("Here is a list of possible answers: ", scripts)
print("Gee, Brain. What are we going to do tonight?")
ui = input("> ")
if f.egg_chk(ui):
    f.egg()
else:
    f.run_script(ui)
