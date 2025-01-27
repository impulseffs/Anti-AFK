# Anti-AFK
![Image](https://github.com/user-attachments/assets/a47f4725-f311-402b-882b-c20af37e5433)

# WoW Anti-AFK Tool

Created by Impulseffs  
Download: [https://github.com/impulseffs/Anti-AFK](https://github.com/impulseffs/Anti-AFK)

A sophisticated Anti-AFK (Away From Keyboard) tool designed specifically for World of Warcraft (WotLK 3.5.5), with a focus on the Warmane private server. This tool helps prevent automatic disconnections due to inactivity by simulating periodic character movements.

## Features

### 1. Auto Jump
- Automatically makes your character jump every 4 seconds
- Works with both mounted and unmounted characters
- Includes occasional forward movement every 3 jumps to enhance anti-AFK effectiveness
- Double-press jump mechanism ensures compatibility with mounted characters

### 2. Auto Rotate
- Smoothly rotates your character left and right
- Creates a natural-looking movement pattern
- Includes periodic forward movement every 5 rotations
- Uses direct Windows API calls for reliable key simulation

### 3. User Interface
- Clean and intuitive graphical interface
- Independent controls for Auto Jump and Auto Rotate features
- Real-time status indicators with color coding
- Ability to run both features simultaneously or independently

## Requirements

### System Requirements
- Operating System: Windows (tested on Windows 10)
- Python 3.8 or higher
- Administrative privileges (required for key simulation)
- Minimum 100MB free disk space
- 2GB RAM recommended

### Game Requirements
- World of Warcraft (WotLK 3.5.5)
- Game must be running in windowed or windowed fullscreen mode
- Character should be in a safe location before activating the tool

## Installation

1. **Install Python**:
   - Download Python from [python.org](https://www.python.org/downloads/)
   - During installation, **IMPORTANT**: Check "Add Python to PATH"
   - Complete the Python installation

2. **Download the Tool**:
   - Clone this repository or download the files:
     - `anti_afk.py`
     - `requirements.txt`

3. **Install Dependencies**:
   - Open Command Prompt as Administrator
   - Navigate to the tool's directory:
     ```
     cd path/to/Anti-AFK
     ```
   - Install required packages:
     ```
     pip install -r requirements.txt
     ```

## Usage

1. **Starting the Tool**:
   - Double-click `anti_afk.py` or run from command prompt:
     ```
     python anti_afk.py
     ```
   - The tool's interface will appear

2. **Using Auto Jump**:
   - Click "Start Auto Jump" to begin automatic jumping
   - Your character will:
     - Jump every 4 seconds
     - Take a small step forward every 3 jumps
   - Click "Stop Auto Jump" to stop

3. **Using Auto Rotate**:
   - Click "Start Auto Rotate" to begin rotation
   - Your character will:
     - Rotate left and right in a smooth pattern
     - Take a small step forward every 5 rotations
   - Click "Stop Auto Rotate" to stop

4. **Emergency Stop**:
   - Move your mouse to any corner of the screen to trigger the failsafe
   - Close the program window to stop all activities
   - Both features have independent stop buttons

## Safety Features

1. **PyAutoGUI Failsafe**:
   - Moving the mouse to any screen corner will stop all automation
   - Prevents loss of control over your character

2. **Independent Controls**:
   - Each feature can be stopped independently
   - Clean shutdown on program close

3. **Smooth Movement Patterns**:
   - Natural-looking movements to avoid detection
   - Random timing elements to prevent pattern recognition

## Troubleshooting

1. **Program Won't Start**:
   - Verify Python is installed and in PATH
   - Run Command Prompt as Administrator
   - Install dependencies using pip

2. **Keys Not Working**:
   - Ensure WoW is in focus
   - Run the program as Administrator
   - Check if other programs are blocking key simulation

3. **Movement Issues**:
   - Verify character isn't in a blocked position
   - Check if character has enough space to move
   - Ensure no movement-blocking effects are active

## Legal Notice

This tool is provided for educational purposes only. Using automation tools may violate the World of Warcraft Terms of Service. Use at your own risk. The developers are not responsible for any consequences of using this tool.

## Technical Details

The tool uses several sophisticated mechanisms to ensure reliable operation:

- Direct Windows API calls for key simulation
- Threading for simultaneous feature operation
- Tkinter for the graphical interface
- Failsafe mechanisms to prevent loss of control

## Contributing

Feel free to submit issues and enhancement requests. For major changes:

1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request

## Version History

- 1.0.0: Initial release
  - Basic Auto Jump and Auto Rotate features
- 1.1.0: Enhanced movement
  - Added forward movement to both features
  - Improved key simulation reliability

## Support

For support, please open an issue in the repository or contact the maintainers.
