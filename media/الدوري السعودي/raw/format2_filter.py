import os, glob
import numpy as np
import cv2

# Format 2 standard treatment (human-approved, 2026-10-21):
#   1. A light grayscale blur over the WHOLE frame -- strong enough to destroy
#      fine kit pattern (stripes/hoops) and jersey numbers, but light enough
#      that players/ball stay clearly visible as sharp, trackable shapes.
#   2. A separate, much harder blur over just the scoreboard's fixed box --
#      the light blur above is nowhere near strong enough to make broadcast
#      scoreboard text illegible, so it needs its own, far stronger pass.
# This replaced an earlier per-player silhouette approach (too slow/fragile)
# and an earlier crowd-wide adaptive blur (also hid the stands/any fan flags,
# but the human decided the light whole-frame blur is enough and only the
# scoreboard needs hard treatment -- see CLAUDE.md "Hiding the teams" for the
# current standard; the adaptive crowd-detection code is still a good trick
# to reach for if a specific banner/flag/graphic turns out to need covering).

BASE = r"C:\Users\Admin\quest\media\الدوري السعودي\raw"
FRAMES_DIR = os.path.join(BASE, "frames_color_f2")      # extract with ffmpeg first, fps/scale matched to the clip
OUT_DIR = os.path.join(BASE, "frames_filtered")
os.makedirs(OUT_DIR, exist_ok=True)

WHOLE_FRAME_SIGMA = 3.0          # tune per-source: enough to blur kit pattern/numbers, not enough to blur player shape
SCOREBOARD_SIGMA = 25            # hard blur -- must make all text fully illegible
SCOREBOARD_BOX = (5, 10, 235, 95)  # x0, y0, x1, y1 -- measured for alnassr_h264.mp4's broadcast overlay (960x540)

def imread_unicode(path):
    data = np.fromfile(path, dtype=np.uint8)
    return cv2.imdecode(data, cv2.IMREAD_COLOR)

def imwrite_unicode(path, img):
    ext = os.path.splitext(path)[1]
    ok, buf = cv2.imencode(ext, img)
    buf.tofile(path)

x0, y0, x1, y1 = SCOREBOARD_BOX
frame_files = sorted(glob.glob(os.path.join(FRAMES_DIR, "*.png")))
print("total frames:", len(frame_files))

for i, fpath in enumerate(frame_files):
    img = imread_unicode(fpath)
    img = cv2.GaussianBlur(img, (0, 0), sigmaX=WHOLE_FRAME_SIGMA)
    region = img[y0:y1, x0:x1]
    img[y0:y1, x0:x1] = cv2.GaussianBlur(region, (0, 0), sigmaX=SCOREBOARD_SIGMA)
    imwrite_unicode(os.path.join(OUT_DIR, os.path.basename(fpath)), img)
    if i % 30 == 0:
        print("done", i)

print("DONE -- remember: grayscale (hue=s=0) is applied at the final ffmpeg encode step, not here.")
