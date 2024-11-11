# iRacing Configuration Manager

This Python script allows iRacing users to manage and apply custom wheel control configurations across different vehicle setups. Users can select a specific configuration and apply it to one or more vehicles in the iRacing setups directory. Future improvements may include adding a graphical user interface (GUI) for easier navigation.

## Features

- **Configuration Selection**: Scan and list available wheel configuration sets.
- **Vehicle Selection**: Select multiple vehicles to apply a chosen configuration.
- **Configuration Verification**: Ensure required files (`controls.cfg` and `joyCalib.yaml`) are present in each configuration directory.
- **File Copying**: Copy configuration files to each selected vehicle setup, creating directories as needed.

## Requirements

- **Python** 3.10 or newer
- **Permissions**: Ensure read and write access to `Documents\iRacing\setups` and `Documents\iRacing\wheelConfigs`.

## Setup Instructions

### Wheel Configuration Setup

1. **Create the `wheelConfigs` Directory**:
   - Inside your iRacing documents directory (`Documents\iRacing`), create a folder named `wheelConfigs`.

2. **Generate Configuration Files in iRacing**:
   - For each profile you want, generate the configuration files in iRacing by enabling the **Use Custom Controls for this Car** option for a specific vehicle.

3. **Organize Profile Folders**:
   - In the `wheelConfigs` directory, create a subfolder for each profile (e.g., `Profile1`, `Profile2`, etc.).
   - Manually copy the `controls.cfg` and `joyCalib.yaml` files from the vehicle’s setup folder in `Documents\iRacing\setups\[car name]` into the appropriate profile folder in `wheelConfigs`.
   - Each profile folder in `wheelConfigs` must contain a unique pair of `controls.cfg` and `joyCalib.yaml` files to be used by this script.

## Usage

1. **Clone the Repository** (or download the script directly).

2. **Run the Script**:
    ```bash
    python iracing_config_manager.py
    ```

3. **Select Configuration**:
   - The script will list available configuration folders in the `wheelConfigs` directory.
   - Select a configuration by entering its corresponding number.

4. **Select Vehicles**:
   - Choose vehicles from the `setups` folder to apply the configuration.
   - You may select multiple vehicles to apply the configuration to.

5. **Confirm Changes**:
   - Confirm the configuration action to apply settings to all selected vehicles.

## Folder Structure

The script assumes a file structure as follows:
Documents/ └── iRacing/ ├── setups/ │ ├── car1/ │ ├── car2/ │ └── ... └── wheelConfigs/ ├── Profile1/ │ ├── controls.cfg │ └── joyCalib.yaml ├── Profile2/ └── ...

markdown
Copy code

- **setups/**: Folder containing each vehicle setup in iRacing.
- **wheelConfigs/**: Folder containing configuration sets for different control profiles.

## Code Overview

- **`readCars(path)`**: Reads the vehicle setup folder and lists each vehicle.
- **`readConfigs(path)`**: Reads and verifies configuration folders for required files.
- **`verifyConfig(directory)`**: Checks if a configuration folder contains necessary files (`controls.cfg` and `joyCalib.yaml`).
- **`moveConfigFile(configFileDir, destinationCar)`**: Copies configuration files from the selected config directory to a selected vehicle folder.
- **`buildLocations(selectedCars, config)`**: Creates directories for each selected vehicle and applies the configuration files.

## Future Improvements

- **Graphical User Interface (GUI)**: Add a GUI for more user-friendly navigation.
- **Dynamic Directory Selection**: Allow users to set up and select the iRacing directory through the script.
- **Enhanced Error Handling**: Improve handling of missing files and invalid directory paths.

## Author

**Kyle Strycharz**  
Version: 1.0

## License

This project is licensed under the MIT License.