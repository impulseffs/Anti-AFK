import tkinter as tk
import pyautogui
import threading
import time
import ctypes

# Virtual key codes
VK_A = 0x41
VK_D = 0x44
VK_W = 0x57

# Windows API for sending keystrokes
SendInput = ctypes.windll.user32.SendInput

# Key press structures
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

def press_key(key_code):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(key_code, 0x48, 0, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(key_code):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(key_code, 0x48, 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

class AntiAFKApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WoW Anti-AFK")
        self.root.geometry("250x200")
        self.root.resizable(False, False)
        
        # Variables
        self.jump_running = False
        self.rotate_running = False
        self.jump_thread = None
        self.rotate_thread = None
        
        # Create main frame
        self.main_frame = tk.Frame(root, padx=20, pady=20)
        self.main_frame.pack(expand=True, fill='both')
        
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title = tk.Label(
            self.main_frame,
            text="WoW Anti-AFK Tool",
            font=("Helvetica", 14, "bold")
        )
        title.pack(pady=(0, 20))
        
        # Auto Jump Button
        self.jump_button = tk.Button(
            self.main_frame,
            text="Start Auto Jump",
            command=self.toggle_auto_jump,
            width=15,
            relief=tk.RAISED,
            bg='SystemButtonFace'
        )
        self.jump_button.pack(pady=5)
        
        self.jump_status = tk.Label(
            self.main_frame,
            text="Jump: Stopped",
            font=("Helvetica", 9),
            fg="red"
        )
        self.jump_status.pack()
        
        # Auto Rotate Button
        self.rotate_button = tk.Button(
            self.main_frame,
            text="Start Auto Rotate",
            command=self.toggle_auto_rotate,
            width=15,
            relief=tk.RAISED,
            bg='SystemButtonFace'
        )
        self.rotate_button.pack(pady=5)
        
        self.rotate_status = tk.Label(
            self.main_frame,
            text="Rotate: Stopped",
            font=("Helvetica", 9),
            fg="red"
        )
        self.rotate_status.pack()
    
    def toggle_auto_jump(self):
        if not self.jump_running:
            self.jump_running = True
            self.jump_button.config(text="Stop Auto Jump", bg='#ffcccb')
            self.jump_status.config(text="Jump: Running", fg="green")
            
            self.jump_thread = threading.Thread(target=self.auto_jump_loop)
            self.jump_thread.daemon = True
            self.jump_thread.start()
        else:
            self.jump_running = False
            self.jump_button.config(text="Start Auto Jump", bg='SystemButtonFace')
            self.jump_status.config(text="Jump: Stopped", fg="red")
    
    def toggle_auto_rotate(self):
        if not self.rotate_running:
            self.rotate_running = True
            self.rotate_button.config(text="Stop Auto Rotate", bg='#ffcccb')
            self.rotate_status.config(text="Rotate: Running", fg="green")
            
            self.rotate_thread = threading.Thread(target=self.auto_rotate_loop)
            self.rotate_thread.daemon = True
            self.rotate_thread.start()
        else:
            self.rotate_running = False
            self.rotate_button.config(text="Start Auto Rotate", bg='SystemButtonFace')
            self.rotate_status.config(text="Rotate: Stopped", fg="red")
    
    def auto_jump_loop(self):
        jump_counter = 0  # Counter to track when to move forward
        while self.jump_running:
            # Press spacebar twice quickly to ensure jump works even when mounted
            pyautogui.press('space')
            time.sleep(0.1)  # Small delay between presses
            pyautogui.press('space')
            
            # Every 3 jumps, take a small step forward
            jump_counter += 1
            if jump_counter >= 3:
                jump_counter = 0
                press_key(VK_W)
                time.sleep(0.3)  # Very short step forward
                release_key(VK_W)
            
            # Wait 4 seconds before next jump
            time.sleep(4)
    
    def auto_rotate_loop(self):
        move_counter = 0  # Counter to track when to move forward
        while self.rotate_running:
            # Rotate left
            press_key(VK_A)
            time.sleep(1)
            release_key(VK_A)
            
            # Small pause
            time.sleep(0.1)
            
            # Rotate right
            press_key(VK_D)
            time.sleep(1)
            release_key(VK_D)
            
            # Small pause
            time.sleep(0.1)
            
            # Every 5 rotations, take a small step forward
            move_counter += 1
            if move_counter >= 5:
                move_counter = 0
                press_key(VK_W)
                time.sleep(0.3)  # Very short step forward
                release_key(VK_W)
    
    def on_closing(self):
        self.jump_running = False
        self.rotate_running = False
        self.root.destroy()

if __name__ == "__main__":
    # Initialize pyautogui settings
    pyautogui.FAILSAFE = True
    
    # Create and run the application
    root = tk.Tk()
    app = AntiAFKApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
