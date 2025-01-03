from typing import Optional
from tkinter import (
    Tk,
    Label,
    Text,
    Button,
    Listbox,
    Frame,
    Menu,
)
from tkinter.constants import *
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk, Image
from pathlib import Path

# Define the default directory for resources
def_dir = Path(__file__).parent


class createTk(Tk):
    """
    A custom Tkinter window class that extends Tk to include utility methods
    for creating widgets and configuring the main window.
    """

    def __init__(self, *args, **kwargs):
        super(createTk, self).__init__(*args, **kwargs)

    def window(
        self,
        title: str = "TkModule Window",
        icon: str = str(def_dir / "defaultImg/default.ico"),
        fullscreen: bool = False,
        minh: int = 456,
        minw: int = 987,
        maxh: Optional[int] = None,
        maxw: Optional[int] = None,
        size: str = "456x456",
    ) -> None:
        """
        Configure the main window.

        :param title: Title of the window
        :param icon: Path to the window icon
        :param fullscreen: Whether the window should start in fullscreen
        :param minh: Minimum height of the window
        :param minw: Minimum width of the window
        :param maxh: Maximum height of the window (optional)
        :param maxw: Maximum width of the window (optional)
        :param size: Initial size of the window (width x height)
        """
        self.geometry(size) if not fullscreen else self.wm_state("zoomed")
        self.title(title)
        self.minsize(minw, minh)
        if maxh and maxw:
            self.maxsize(maxw, maxh)
        self.wm_iconbitmap(icon)

    def label(
        self,
        master: Optional[object] = None,
        side: Optional[str] = None,
        anchor: Optional[str] = None,
        fill: Optional[str] = None,
        padx: Optional[int] = None,
        pady: Optional[int] = None,
        text: Optional[str] = "Default Label",
        **kwargs,
    ) -> Label:
        """
        Create and pack a Label widget.

        :param master: Parent widget (optional)
        :param side: Side to pack the label (optional)
        :param anchor: Anchor position for the label (optional)
        :param fill: Fill behavior (optional)
        :param padx: Padding in the x-direction (optional)
        :param pady: Padding in the y-direction (optional)
        :param text: Text to display in the label
        :return: Configured Label widget
        """
        label_widget = Label(master or self, text=text, **kwargs)
        label_widget.pack(side=side, anchor=anchor, fill=fill, padx=padx, pady=pady)
        return label_widget

    def labelImg(
        self,
        master: Optional[object] = None,
        side: Optional[str] = None,
        anchor: Optional[str] = None,
        fill: Optional[str] = None,
        padx: Optional[int] = None,
        pady: Optional[int] = None,
        image: str = str(def_dir / "defaultImg/default.ico"),
        **kwargs,
    ) -> Label:
        """
        Create and pack a Label widget displaying an image.

        :param master: Parent widget (optional)
        :param side: Side to pack the label (optional)
        :param anchor: Anchor position for the label (optional)
        :param fill: Fill behavior (optional)
        :param padx: Padding in the x-direction (optional)
        :param pady: Padding in the y-direction (optional)
        :param image: Path to the image to display
        :return: Configured Label widget
        """
        img = ImageTk.PhotoImage(Image.open(image))
        label_img_widget = Label(master or self, image=img, **kwargs)
        label_img_widget.image = img  # Keep a reference to avoid garbage collection
        label_img_widget.pack(side=side, anchor=anchor, fill=fill, padx=padx, pady=pady)
        return label_img_widget

    def textarea(
        self,
        master: Optional[object] = None,
        scroll: bool = True,
        side: Optional[str] = None,
        anchor: Optional[str] = None,
        expand: Optional[bool] = None,
        fill: Optional[str] = None,
        padx: Optional[int] = None,
        pady: Optional[int] = None,
        **kwargs,
    ) -> Text:
        """
        Create and pack a Text widget, optionally with a scrollbar.

        :param master: Parent widget (optional)
        :param scroll: Whether to add a scrollbar to the Text widget
        :param side: Side to pack the widget (optional)
        :param anchor: Anchor position for the widget (optional)
        :param expand: Whether the widget should expand to fill space (optional)
        :param fill: Fill behavior (optional)
        :param padx: Padding in the x-direction (optional)
        :param pady: Padding in the y-direction (optional)
        :return: Configured Text widget
        """
        widget_class = ScrolledText if scroll else Text
        text_widget = widget_class(master or self, **kwargs)
        text_widget.pack(side=side, anchor=anchor, expand=expand, fill=fill, padx=padx, pady=pady)
        return text_widget

    def addBtn(
        self,
        master: Optional[object] = None,
        text: str = "Default",
        side: Optional[str] = None,
        anchor: Optional[str] = None,
        expand: Optional[bool] = None,
        fill: Optional[str] = None,
        padx: Optional[int] = None,
        pady: Optional[int] = None,
        **kwargs,
    ) -> Button:
        """
        Create and pack a Button widget.

        :param master: Parent widget (optional)
        :param text: Text to display on the button
        :param side: Side to pack the button (optional)
        :param anchor: Anchor position for the button (optional)
        :param expand: Whether the button should expand to fill space (optional)
        :param fill: Fill behavior (optional)
        :param padx: Padding in the x-direction (optional)
        :param pady: Padding in the y-direction (optional)
        :return: Configured Button widget
        """
        button_widget = Button(master or self, text=text, **kwargs)
        button_widget.pack(side=side, anchor=anchor, expand=expand, fill=fill, padx=padx, pady=pady)
        return button_widget

    def addList(
        self,
        master: Optional[object] = None,
        side: Optional[str] = None,
        expand: Optional[bool] = None,
        anchor: Optional[str] = None,
        fill: Optional[str] = None,
        padx: Optional[int] = None,
        pady: Optional[int] = None,
        **kwargs,
    ) -> Listbox:
        """
        Create and pack a Listbox widget.

        :param master: Parent widget (optional)
        :param side: Side to pack the listbox (optional)
        :param expand: Whether the listbox should expand to fill space (optional)
        :param anchor: Anchor position for the listbox (optional)
        :param fill: Fill behavior (optional)
        :param padx: Padding in the x-direction (optional)
        :param pady: Padding in the y-direction (optional)
        :return: Configured Listbox widget
        """
        listbox_widget = Listbox(master or self, **kwargs)
        listbox_widget.pack(side=side, anchor=anchor, expand=expand, fill=fill, padx=padx, pady=pady)
        return listbox_widget

    def addFrame(
        self,
        master: Optional[object] = None,
        side: Optional[str] = None,
        expand: Optional[bool] = None,
        anchor: Optional[str] = None,
        fill: Optional[str] = None,
        padx: Optional[int] = None,
        pady: Optional[int] = None,
        **kwargs,
    ) -> Frame:
        """
        Create and pack a Frame widget.

        :param master: Parent widget (optional)
        :param side: Side to pack the frame (optional)
        :param expand: Whether the frame should expand to fill space (optional)
        :param anchor: Anchor position for the frame (optional)
        :param fill: Fill behavior (optional)
        :param padx: Padding in the x-direction (optional)
        :param pady: Padding in the y-direction (optional)
        :return: Configured Frame widget
        """
        frame_widget = Frame(master or self, **kwargs)
        frame_widget.pack(side=side, anchor=anchor, expand=expand, fill=fill, padx=padx, pady=pady)
        return frame_widget

    def bindkey(self, keys: str, cmd: callable) -> None:
        """
        Bind a key sequence to a command.

        :param keys: Key sequence to bind
        :param cmd: Command to execute when the key sequence is triggered
        """
        self.bind(keys, cmd)

    def bindkey_ctrl(self, keys: str, cmd: callable) -> None:
        """
        Bind a Control+key sequence to a command.

        :param keys: Key sequence to bind (without Control modifier)
        :param cmd: Command to execute when the key sequence is triggered
        """
        self.bind(f"<Control_L>{keys}", cmd)
        self.bind(f"<Control_R>{keys}", cmd)

    def bindkey_shift(self, keys: str, cmd: callable) -> None:
        """
        Bind a Shift+key sequence to a command.

        :param keys: Key sequence to bind (without Shift modifier)
        :param cmd: Command to execute when the key sequence is triggered
        """
        self.bind(f"<Shift_L>{keys}", cmd)
        self.bind(f"<Shift_R>{keys}", cmd)

    def bindkey_alt(self, keys: str, cmd: callable) -> None:
        """
        Bind an Alt+key sequence to a command.

        :param keys: Key sequence to bind (without Alt modifier)
        :param cmd: Command to execute when the key sequence is triggered
        """
        self.bind(f"<Alt_L>{keys}", cmd)
        self.bind(f"<Alt_R>{keys}", cmd)

    def run(self) -> None:
        """
        Start the Tkinter main loop.
        """
        self.mainloop()

    def quit(self) -> None:
        """
        Quit the application and destroy the window.
        """
        self.destroy()


class Menubars(Menu):
    """
    A custom class for managing menu bars and their items.
    """

    def __init__(self, master: Optional[object] = None, *args, **kwargs):
        """
        Initialize the Menubars instance.

        :param master: The master widget to attach the menu bar to
        """
        super(Menubars, self).__init__(master, *args, **kwargs)

    def createMenu(self, **kwargs) -> Menu:
        """
        Create a new Menu instance.

        :return: Configured Menu widget
        """
        menu_widget = Menu(self, tearoff=0, **kwargs)
        return menu_widget

    def addCmd(self, menu: Menu, **kwargs) -> None:
        """
        Add a command to a menu.

        :param menu: Menu instance to which the command will be added
        """
        menu.add_command(**kwargs)

    def addHead(self, label: str, menu: Menu) -> None:
        """
        Add a menu heading to the menu bar.

        :param label: Label for the menu heading
        :param menu: Menu instance to attach to the heading
        """
        self.add_cascade(label=label, menu=menu)

    def view(self, config: bool = True) -> None:
        """
        Configures the menu for the main tkinter window.

        :param config: Whether to configure the menu for the tkinter window.
                       Defaults to True.
        """
        if config:
            self.master.configure(menu=self)
