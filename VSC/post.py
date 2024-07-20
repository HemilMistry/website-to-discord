import concurrent.futures
import subprocess

def run_first_script():
    subprocess.run(['python', 'app.py'])

def run_second_script():
    subprocess.run(['python', 'bot.py'])

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.submit(run_first_script)
    executor.submit(run_second_script)