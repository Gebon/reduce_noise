import sys
import os.path as path
import subprocess
source_folder = input("File path:") # sys.argv[2]
audacity_path = input("Audacity executable path:") # sys.argv[1]

def open_audacity(audacity_path):
    openApp(audacity_path)
    try:
        wait("toolbar.png", 10)
        try:
            wait("tooltip_ok_button.png")
            click("tooltip_ok_button.png")
        except FindFailed as e:
            pass
    except FindFailed as e:
        print("Can't open Audacity")
        exit(1)

def open_file(file_name):
    type("o", Key.CTRL)
    wait("open_file_toolbar.png")
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
    export_file(output_file)
    close_audacity()

for root, _, files in os.walk(source_folder):
    for file in files:
        if file != "face.mp4":
            continue
        input_file = path.join(root, "source.mp3")
        output_file = path.join(root, "cleaned.wav")
        result_file = path.join(root, "cleaned.mp3")
        run_cmd_command(r"ffmpeg -i %s -vn -ar 44100 -ac 2 -ab 320k -f mp3 %s" % (path.join(root, file), input_file))
        process_the_soundtrack(audacity_path, input_file, output_file)
        run_cmd_command('ffmpeg -i %s -vn -ar 44100 -ac 2 -ab 320k -f mp3 %s' % (output_file, result_file))
        run_cmd_command('del %s' % input_file)
        run_cmd_command('del %s' % output_file)
