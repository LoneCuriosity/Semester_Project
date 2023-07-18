"""
An application for my Semester Project
"""
import toga
import httpx
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class SemesterProject(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        self.label = toga.Label(
            "",
            style=Pack(padding=(0, 5))
        )

        button = toga.Button(
            "Login",
            on_press=self.login,
            style=Pack(padding=5)
        )

        main_box.add(self.label)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def login(self, widget):
        with httpx.Client() as client:
            response = client.get('https://ramongarciajr.tech/api/semesterProject/Pins')

        password = {"id":1,"Pin26":1,"Pin19":0,"Pin13":1,"Pin6":0}

        if(response.json()[0] == password):
            self.label.text = "Welcome!"   
        else:
            self.label.text = "Wrong Password!"
 
def main():
    return SemesterProject()
