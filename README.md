## Prerequisites
1. Create Virtual Environment if needed (for example if Ubuntu OS):
```
python3 -m venv my_project_venv
source my_project_venv/bin/activate
```
2. Install python packages:
```
pip install pytest tesserocr opencv-python pillow
```

## Install aurora_tests package
```
pip install aurora_tests-0.0.2-py3-none-any.whl
```

## System Under Test (SUT)
We uses Android on emulator as SUT, for runing it from the command line:
```
~/Android/Sdk/emulator/emulator -avd Pixel_3a_API_34_extension_level_7_x86_64
```

## Run example tests
See coresponding README.md from desired exmple, for example: [./src/01_find_and_tap_icon/README.md](./src/01_find_and_tap_icon/README.md):
