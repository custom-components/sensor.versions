# versions
  
![Version](https://img.shields.io/badge/version-0.0.1-green.svg?style=for-the-badge) ![mantained](https://img.shields.io/maintenance/yes/2018.svg?style=for-the-badge)   
A sensor platform which allows you to get information about new versions.
  
To get started put `/custom_components/sensor/versions.py` here:  
`<config directory>/custom_components/sensor/versions.py`  
  
**Example configuration.yaml:**
```yaml
sensor:
  platform: versions
  flavor: docker
```
**Configuration variables:**  
  
key | description  
:--- | :---  
**platform (Required)** | The sensor platform name.  
**flavor (Optional)** | Can be 'venv', 'hassbian', 'docker', 'hassio', defaults to 'venv'  
  
  
  
***
Due to how `custom_componentes` are loaded, it is normal to see a `ModuleNotFoundError` error on first boot after adding this, to resolve it, restart Home-Assistant.