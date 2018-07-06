# sensor.versions
  
[![Version](https://img.shields.io/badge/version-0.0.4-green.svg?style=for-the-badge)](#) [![mantained](https://img.shields.io/maintenance/yes/2018.svg?style=for-the-badge)](#) [![maintainer](https://img.shields.io/badge/maintainer-Joakim%20Sørensen%20%40ludeeus-blue.svg?style=for-the-badge)](#)   
A sensor platform which allows you to get the newest version number for your install method.
  
To get started put `/custom_components/sensor/versions.py` here:  
`<config directory>/custom_components/sensor/versions.py`  
  
**Example configuration.yaml:**

```yaml
sensor:
  platform: versions
  installation: docker
  branch: beta
  image: default
```

**Configuration variables:**  
key | description  
:--- | :---  
**platform (Required)** | The sensor platform name.  
**installation (Optional)** | Can be 'venv', 'hassbian', 'docker', 'hassio', defaults to 'venv'  
**branch (Optional)** | Can be 'stable', 'rc', 'beta', defaults to 'stable'  
**image (Optional)** | Can be 'default', 'qemux86', 'qemux86-64', 'qemuarm', 'qemuarm-64', 'intel-nuc', 'raspberrypi', 'raspberrypi2', 'raspberrypi3', 'raspberrypi3-64', defaults to 'default'  
  
#### Sample overview
![Sample overview](overview.png)
  
***
Due to how `custom_componentes` are loaded, it is normal to see a `ModuleNotFoundError` error on first boot after adding this, to resolve it, restart Home-Assistant.
