# ASCII Video Player

Convert and play videos or GIFs as ASCII art in your terminal with proper frame timing and synchronization.

## Features

- **Video to ASCII Conversion**: Transform video frames into ASCII art using brightness-based character mapping
- **Terminal-Optimized Display**: Automatically adapts to your terminal size for proper aspect ratio
- **Frame-Accurate Timing**: Maintains original video playback speed in the terminal
- **Multi-Format Support**: Compatible with GIFs and video formats supported by OpenCV
- **Real-Time Processing**: Processes and displays frames with minimal latency

## Requirements

- Python 3.7+
- OpenCV (`cv2`)
- Pillow (PIL)

## Installation

1. Clone or download this repository
2. Install dependencies:

```bash
pip install opencv-python pillow
```

3. Place your video/GIF file in the project directory (update the filename in `main.py` if needed)

## Usage

1. Update the video filename in `main.py`:

```python
video = cv2.VideoCapture("your_video.gif")  # or .mp4, .avi, etc.
```

2. Run the script:

```bash
python main.py
```

The video will display as ASCII art in your terminal with the following character mapping based on brightness:

- `@` - Very bright
- `#` - Bright
- `%` - Medium-bright
- `*` - Medium
- `+` - Medium-dark
- `:` - Dark
- `.` - Very dark
- ` ` - Black

## How It Works

1. **Video Loading**: Opens the specified video/GIF file using OpenCV
2. **Frame Extraction**: Reads video frames and converts them to RGB color space
3. **Resizing**: Scales frames to match terminal dimensions
4. **ASCII Conversion**: Maps pixel brightness to ASCII characters
5. **Display**: Renders frames in the terminal with accurate timing based on the original video's FPS
6. **Playback**: Loops through frames at the correct speed, clearing and redrawing for smooth animation

## Example

```bash
python main.py
# Output: ASCII animation of your video/GIF in the terminal
```

## Notes

- Ensure your terminal has enough space for the ASCII display (minimum recommended: 80x24 characters)
- Larger terminal sizes will produce higher-quality ASCII art
- Very long videos may require significant memory
- Video playback speed depends on terminal rendering performance

## License

MIT

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.
