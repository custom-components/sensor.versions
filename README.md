# versions
  
[![Version](https://img.shields.io/badge/version-0.0.3-green.svg?style=for-the-badge)](#) [![mantained](https://img.shields.io/maintenance/yes/2018.svg?style=for-the-badge)](#)   
A sensor platform which allows you to get the newest version number for your install method.
  
To get started put `/custom_components/sensor/versions.py` here:  
`<config directory>/custom_components/sensor/versions.py`  
  
**Example configuration.yaml:**
```yaml
sensor:
  platform: versions
  installation: docker
  branch: beta
```
**Configuration variables:**  
  
key | description  
:--- | :---  
**platform (Required)** | The sensor platform name.  
**installation (Optional)** | Can be 'venv', 'hassbian', 'docker', 'hassio', defaults to 'venv'  
**branch (Optional)** | Can be 'stable', 'rc', 'beta', defaults to 'stable'  
  
#### Sample overview
![Sample overview](overview.png)
  
  
  
***
Due to how `custom_componentes` are loaded, it is normal to see a `ModuleNotFoundError` error on first boot after adding this, to resolve it, restart Home-Assistant.