import os, sys, glob
import numpy as np
import torch
import cv2
from sam2.build_sam import build_sam2_video_predictor

BASE = r"C:\Users\Admin\quest\media\الدوري السعودي\raw"
FRAMES_DIR = os.path.join(BASE, "frames_work4")
OUT_DIR = os.path.join(BASE, "frames_masked_full")
os.makedirs(OUT_DIR, exist_ok=True)

ckpt = r"C:\Users\Admin\sam2_checkpoints\sam2.1_hiera_small.pt"
cfg = "configs/sam2.1/sam2.1_hiera_s.yaml"

predictor = build_sam2_video_predictor(cfg, ckpt, device="cuda")
state = predictor.init_state(video_path=FRAMES_DIR)

ANCHOR_IDX = 0  # frame 00001.jpg; confirmed via forward-propagation validation to converge
# with the known-correct position at frame 204 (centroid 408,292 vs confirmed 407,293)
POINT = np.array([[380, 230]], dtype=np.float32)
LABEL = np.array([1], dtype=np.int32)

_, out_obj_ids, out_mask_logits = predictor.add_new_points_or_box(
    inference_state=state, frame_idx=ANCHOR_IDX, obj_id=1,
    points=POINT, labels=LABEL)

masks = {}
CUTOFF = 485  # stop before GOAL graphic transition

print("propagating forward...")
for frame_idx, obj_ids, mask_logits in predictor.propagate_in_video(state, start_frame_idx=ANCHOR_IDX, reverse=False):
    m = (mask_logits[0] > 0.0).cpu().numpy()[0]
    masks[frame_idx] = m
    if frame_idx >= CUTOFF:
        break
print("forward done, frames covered:", len(masks))

def imread_unicode(path):
    data = np.fromfile(path, dtype=np.uint8)
    return cv2.imdecode(data, cv2.IMREAD_COLOR)

def imwrite_unicode(path, img):
    ext = os.path.splitext(path)[1]
    ok, buf = cv2.imencode(ext, img, [cv2.IMWRITE_JPEG_QUALITY, 95])
    buf.tofile(path)

frame_files = sorted(glob.glob(os.path.join(FRAMES_DIR, "*.jpg")))
print("total source frames:", len(frame_files))

areas = {}
for i in sorted(masks.keys()):
    areas[i] = int(masks[i].sum())
with open(os.path.join(BASE, "mask_areas_full.txt"), "w") as f:
    for i in sorted(areas.keys()):
        f.write(f"{i}\t{areas[i]}\n")

for i, fpath in enumerate(frame_files):
    if i > CUTOFF:
        break
    img = imread_unicode(fpath)
    if i in masks:
        m = masks[i]
        if m.shape[:2] != img.shape[:2]:
            m = cv2.resize(m.astype(np.uint8), (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST).astype(bool)
        img[m] = (255, 255, 255)
    out_path = os.path.join(OUT_DIR, os.path.basename(fpath))
    imwrite_unicode(out_path, img)

print("MASKING DONE")

# Lesson: a first attempt anchored mid-clip (near the kick) and propagated
# BACKWARD into the deep buildup; backward tracking degraded almost immediately
# (drifted onto empty grass within single-digit frames of the anchor) even
# though FORWARD tracking from that same anchor was fully reliable through the
# kick and aftermath. Don't trust long backward propagation on a wide/distant
# shot with lookalike players.
#
# Fix: anchor at frame 0 instead and propagate forward only. To find the right
# player at frame 0 (hard to tell by eye in a wide shot with several similar
# yellow shirts), validate candidates empirically: run a SHORT forward
# propagation from a candidate frame-0 point out to a frame where the correct
# player's position is already known (e.g. from a previous successful anchor),
# and check whether the resulting mask centroid converges to that known
# position. A correct candidate converges almost exactly (within a couple of
# pixels here); a wrong one drifts or lands on the wrong player. This is much
# cheaper than guessing and re-running the full clip blind.
