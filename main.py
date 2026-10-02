"""Fullscreen image slideshow.

Usage:
	python3 main.py --seconds 8 --shuffle

Press Escape or Q to quit, Space to pause/resume, and the arrow keys to
move between images.
"""

from __future__ import annotations

import argparse
import signal
import sys
from datetime import date, datetime
from pathlib import Path

try:
	import tkinter as tk
except ModuleNotFoundError:
	raise SystemExit(
		"Tkinter is required. On Debian/Ubuntu, install it with: sudo apt install python3-tk"
	) from None

try:
	from PIL import Image, ImageFile, ImageOps, ImageTk
except ImportError as error:
	raise SystemExit(
		"Pillow's ImageTk support is required. On Debian/Ubuntu, install it with: "
		"sudo apt install python3-pil.imagetk"
	) from error

# Self defined from here

from config import AUDIO_CONFIG, SLIDES_CONFIG # loads environment as well

from slideshow import Slideshow
ImageFile.LOAD_TRUNCATED_IMAGES = True

def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description="Display a folder of images like a screensaver.")
	parser.add_argument("--seconds", type=float, default=8.0, help="Seconds per image (default: 8)")
	parser.add_argument("--shuffle", action="store_true", help="Show images in random order")
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	folder = Path(SLIDES_CONFIG["slides_folder"]).resolve()
	if not folder.is_dir():
		raise SystemExit(f"Not a folder: {folder}")
	if args.seconds <= 0:
		raise SystemExit("--seconds must be greater than zero")

	root = tk.Tk()
	slideshow = Slideshow(root, args.seconds, args.shuffle)
	slideshow.start()
	signal.signal(signal.SIGINT, lambda _signum, _frame: slideshow.close())
	root.mainloop()


if __name__ == "__main__":
	main()

