"""
Run every Python program of the book "Lecture Notes for Numerical Analysis with Python".

For each program  code/chNN/name.py  the printed output is written to
code/chNN/name.out  (the same output that is printed in the book).
Figures are saved in the folder  figures/ .

Usage:
    python run_all.py            # run everything
    python run_all.py ch04       # run only Chapter 4
"""
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.join(ROOT, "code")
FIGS = os.path.join(ROOT, "figures")


def main():
    only = sys.argv[1:]
    os.makedirs(FIGS, exist_ok=True)
    env = dict(os.environ, MPLBACKEND="Agg", PYTHONIOENCODING="utf-8")
    failures = []
    t0 = time.time()
    for chap in sorted(os.listdir(CODE)):
        if only and chap not in only:
            continue
        cdir = os.path.join(CODE, chap)
        if not os.path.isdir(cdir):
            continue
        for fname in sorted(os.listdir(cdir)):
            if not fname.endswith(".py"):
                continue
            path = os.path.join(cdir, fname)
            res = subprocess.run([sys.executable, path], cwd=FIGS, env=env,
                                 capture_output=True, text=True, timeout=300)
            out = res.stdout.replace("\r\n", "\n").rstrip() + "\n"
            with open(path[:-3] + ".out", "w", encoding="utf-8") as fh:
                fh.write(out)
            status = "ok " if res.returncode == 0 else "ERR"
            print(f"[{status}] {chap}/{fname}")
            if res.returncode != 0:
                failures.append(f"{chap}/{fname}")
                print(res.stderr)
    print(f"\n{len(failures)} failure(s) in {time.time() - t0:.1f}s")
    for f in failures:
        print("   ", f)
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
