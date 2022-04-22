import tkinter as tk
from view import View
from model import Model

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:

            # save the model
            self.model.email = email
            self.model.save()

            # show a success message
            self.view.show_success(f'The email {email} saved!')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)

class App(tk.Tk):
    def __init__(self, master):
        super().__init__(master)

        self.title("Tkinter MVC Demo")
        self.geometry("300x100")

        self.model = Model()
        view = View(self.master)
        model = Model(view.)

if __name__ == '__main__':
    pass