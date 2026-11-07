"""依次运行本系列所有代码文件，检查是否全部正常执行。用法：python run_all.py"""
import pathlib, subprocess, sys

here = pathlib.Path(__file__).parent
files = sorted(here.glob("ep*.py"))
failed = []
for f in files:
    r = subprocess.run([sys.executable, f.name], cwd=here, capture_output=True, text=True)
    status = "OK " if r.returncode == 0 else "ERR"
    print(f"[{status}] {f.name}")
    if r.returncode:
        failed.append(f.name); print(r.stderr)
print(f"\n共 {len(files)} 个文件，失败 {len(failed)} 个")
