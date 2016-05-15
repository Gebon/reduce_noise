import sys
import os.path as path
import subprocess

def open_audacity(audacity_path):
    openApp(audacity_path)
    try:
        wait("toolbar.png", 10)
        try:
            wait("tooltip_ok_button.png", 2)
            click("tooltip_ok_button.png")
        except FindFailed as e:
            pass
    except FindFailed as e:
        print("Can't open Audacity")
        exit(1)

def open_file(file_name):
    type("o", Key.CTRL)
    try:
        wait("open_file_toolbar.png")
    except FindFailed as e:
        print("Can't find \"Open...\" window")
    paste(input_file)
    type(Key.ENTER)
    wait("sizing_panel.png", 30)

def open_noise_reduction_window(): 
    click("effects_button.png")
    click("noise_reduction_button.png")

def create_noise_model():
    type(Pattern("duration_modifier.png").targetOffset(12,12), "3")
    open_noise_reduction_window()
    click(Pattern("create_noise_model_button.png").targetOffset(-12,19))
    try:
        wait("cancel_button.png", 1)
        waitVanish("cancel_button.png")
    except FindFailed as e:
        pass

def reduce_noise():
    type("a", Key.CTRL)
    open_noise_reduction_window()
    click("ok_button.png")
    try:
        wait("cancel_button.png", 5)
        waitVanish("cancel_button.png", 120)
    except FindFailed as e:
        print("Some problems occured while trying to reduce noise")
        exit(1)

def normalize():
    click("effects_button.png")
    click("normalizing_menu.png")
    click( Pattern("normalizing_dialog.png").targetOffset(4,35))
    try:
        wait("normalize_process.png",5)
        waitVanish("normalize_process.png",120)
    except FindFailed as e:
        print("Some problems occured while trying to normilize audio")
        exit(1)

def export_file(file_path):
    type("e", Key.CTRL + Key.SHIFT)
    try:
        wait("save_cancel_parameters_buttons.png")
    except FindFailed as e:
       print("Can't open exporting window")
       exit(1)
    paste(output_file)
    type(Key.ENTER)
    try:
        wait("replace_alert.png", 1)
        type(Key.ENTER)
    except FindFailed as e:
        pass
    try:
        wait("ok_button.png")
    except FindFailed as e:
        print("Something goes wrong")
        exit(1)
    type(Key.ENTER)
    try:
        wait("stop_or_cancel_buttons.png")
    except FindFailed as e:
        print("Exporting failed")
        exit(1)
    waitVanish("stop_or_cancel_buttons.png", 30)

def close_audacity():
    type(Key.F4, Key.ALT)
    sleep(0.2)
    type(Key.RIGHT)
    type(Key.ENTER)

def maximize_window():
    type(Key.UP, Key.WIN)

def run_cmd_command(command):
    subprocess.Popen(command, shell=True).communicate()

def process_the_soundtrack(audacity_path, input_file, output_file):    
    open_audacity(audacity_path)
    maximize_window()
    open_file(input_file)
    create_noise_model()
    reduce_noise()
    normalize()
    export_file(output_file)
    close_audacity()


if len(sys.argv) > 1:
    audacity_path = sys.argv[1]
    input_file = sys.argv[2]
    output_file=sys.argv[3]
else:
    audacity_path="C:\\Program Files (x86)\\Audacity\\audacity.exe"
    input_file = "H:\\LHPS\\Input\\Module1\\Lecture1\\11\\input.wav"
    output_file="H:\\LHPS\\Input\\Module1\\Lecture1\\11\\clean.wav"

process_the_soundtrack(audacity_path, input_file, output_file)