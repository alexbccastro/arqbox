import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["tkinter", "tkinter.font", "tkinter.ttk"],
                     "include_files": ["arqbox_icon_2e2e2e_100px.png",
                                       "arqbox_icon_2e2e2e_glossary.png",
                                       "arqbox_icon_545454_48px.ico",
                                       "arqbox_logo_txt_2e2e2e_100px.png"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="ARQBOX",
      version="1.0",
      description="ARQBOX",
      options={"build_exe": build_exe_options},
      executables=[Executable("arqbox.py",
                              base=base,
                              icon="arqbox_icon_545454_48px.ico")])

# Para salvar o código em exe, abra o terminal da pasta e digite "python setup.py build"
