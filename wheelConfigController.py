# Author: Kyle Strycharz
# Version: 1.0
# Description: This script is designed to manage iRacing configuration files, allowing users to select and copy
# custom control configurations to different iRacing vehicle setups.

import os
import shutil

# Set iRacing Documents directory (to be prompted by GUI in future versions)
iRacingDocuments = "C:\\Users\\Kyle\\Documents\\iRacing"

# Define setup and wheel configuration directories
iRacingSetups = os.path.join(iRacingDocuments, "setups")
wheelConfigs = os.path.join(iRacingDocuments, "wheelConfigs")

def displayPath(path):
    """Displays the specified path (may be expanded for dynamic path handling)."""
    return path

def readCars(path):
    """Reads and returns a list of folders in the iRacing setups directory.

    Args:
        path (str): Path to the iRacing setups directory.

    Returns:
        list: List of car folders found in the setups directory.
    """
    carList = os.listdir(path)
    print(f"Cars discovered: {len(carList)}")
    return carList

def readConfigs(path):
    """Reads and verifies wheel configuration directories, only returning those with required files.

    Args:
        path (str): Path to the wheel configurations directory.

    Returns:
        list: List of directories that contain valid configuration files.
    """
    configFiles = os.listdir(path)
    acceptedConfigs = []
    print(f"Configuration Sets Discovered: {len(configFiles)}")

    for configDir in configFiles:
        tempPath = os.path.join(path, configDir)
        if verifyConfig(tempPath):
            print(f"{configDir} contains necessary files")
            acceptedConfigs.append(tempPath)
        else:
            print(f"{configDir} does not contain necessary files")

    return acceptedConfigs

def verifyConfig(directory):
    """Checks if a configuration directory contains required files.

    Args:
        directory (str): Directory path to check.

    Returns:
        bool: True if 'controls.cfg' and 'joyCalib.yaml' are present; False otherwise.
    """
    files = os.listdir(directory)
    if "controls.cfg" in files and "joyCalib.yaml" in files:
        return True
    return False

def moveConfigFile(configFileDir, destinationCar):
    """Copies the control and calibration files from the config directory to a car directory.

    Args:
        configFileDir (str): Directory containing the config files to copy.
        destinationCar (str): Destination car directory to copy the files into.
    """
    controls = os.path.join(configFileDir, "controls.cfg")
    joyCalib = os.path.join(configFileDir, "joyCalib.yaml")
    shutil.copy(controls, destinationCar)
    shutil.copy(joyCalib, destinationCar)

def buildLocations(selectedCars, config):
    """Creates directories for selected cars and copies the config file into each.

    Args:
        selectedCars (list): List of selected car directories.
        config (str): Path to the selected config file.
    """
    for car in selectedCars:
        directory = os.path.join(iRacingSetups, car)
        moveConfigFile(config, directory)

def listItems(items):
    """Prints a numbered list of items.

    Args:
        items (list): List of items to display.
    """
    for idx, item in enumerate(items):
        print(f"{idx}.) {item}")

# Main execution flow
if __name__ == "__main__":
    cars = readCars(iRacingSetups)
    configs = readConfigs(wheelConfigs)
    print()

    # User selects configuration file
    print("SELECT CONFIGURATION FILE OPTIONS")
    listItems(configs)
    while True:
        try:
            print()
            selectConfig = int(input("Select controller configuration: "))
            selectedConfigDir = configs[selectConfig]
            print(f"{selectedConfigDir} selected")
            break
        except (IndexError, ValueError):
            print("Invalid selection. Please enter a valid option.")

    # User selects cars to apply the config to
    listItems(cars)
    print()
    selectedCars = []
    while True:
        try:
            selectedCarNum = int(input("Select Car to move config to: "))
            print()
            selectedCar = cars[selectedCarNum]
            selectedCars.append(selectedCar)
        except (IndexError, ValueError):
            print("Invalid selection. Please enter a valid option.")
            continue

        another = input("Would you like to select another vehicle (y/n): ").lower()
        if another == "n":
            break

    # Confirm action and move configurations
    print()
    confirmation = input("Are you sure you want to apply the selected configuration to the listed cars? This action cannot be undone. (y/n): ")
    if confirmation.lower() == "y":
        buildLocations(selectedCars, selectedConfigDir)
        print()
        print("Configuration files have been successfully applied.")
