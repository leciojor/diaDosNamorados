# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('IMG_0615-2.jpg', '.'), ('D85095D8-.jpg', '.'), ('90DD7B9E--2.jpg', '.'), ('298B6100--2.jpg', '.'), ('549A4F07--2.jpg', '.'), ('IMG_0624-2.jpg', '.'), ('IMG_0615.jpg', '.'), ('The Avengers Theme (Good Part Loop).mp3', '.'), ('cute-level-up-3-189853.mp3', '.'), ('level-passed-143039.mp3', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
