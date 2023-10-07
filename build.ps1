rmdir build -Recurse -Force
rmdir dist -Recurse -Force
pip install pyinstaller
pyinstaller client/TriggerNotation.py --onefile --windowed