#!/usr/bin/env python3

import os
import sys
import shutil

src = sys.argv[1]
dst = sys.argv[2]
depth = None


def ensure(dir_path):
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)


if len(sys.argv) >= 5 and sys.argv[3] == "--max_depth":
	try:
		depth = int(sys.argv[4])
	except:
		depth = None

ensure(dst)

for root, dirs, files in os.walk(src):
	rel = os.path.relpath(root, src)
	parts = [] if rel == "." else rel.split(os.sep)

	if depth is not None and len(parts) > depth:
		parts = parts[-depth:]

	target_dir = os.path.join(dst, *parts) if parts else dst
	ensure(target_dir)

	for fname in files:
		src_file = os.path.join(root, fname)
		new_name = fname
		dest_file = os.path.join(target_dir, new_name)

		count = 1
		while os.path.exists(dest_file):
			if "." in fname:
				base, ext = fname.rsplit(".", 1)
				new_name = f"{base}{count}.{ext}"
			else:
				new_name = f"{fname}{count}"
			dest_file = os.path.join(target_dir, new_name)
			count += 1

		shutil.copy2(src_file, dest_file)
