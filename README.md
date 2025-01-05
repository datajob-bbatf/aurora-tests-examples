## Intro
This project provides examples of using the AuroraTests - HMI Black Box Testing Framework.


## Envoironment Setup
To set up the environment, follow the "AuroraTests - Quick Start Guide".

## System Under Test (SUT)
This project uses the Android Pixel 3 emulator as the SUT. To launch the emulator from the command line, run:
```
~/Android/Sdk/emulator/emulator -avd Pixel_3a_API_34_extension_level_7_x86_64
```

## How to run HMI Test
To run an HMI test, such as [find_and_tap_icon.py](hmi_tests/src/01_find_and_tap_icon/find_and_tap_icon.py), use the following command from the `hmi_tests` folder:
```
pytest src/01_find_and_tap_icon/find_and_tap_icon.py --config_file config_pixel3.json --res_file res_pixel3_1080_2220/res.json
```

## Debugging in VS Code

The project includes a [launch.json](.vscode/launch.json) file with Visual Studio Code debug configurations. You can use this file to run and debug tests directly in VS Code.