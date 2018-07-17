"""
A platform which allows you to get information about new versions.
For more details about this component, please refer to the documentation at
https://github.com/custom-components/sensor.versions
"""
from datetime import timedelta
import voluptuous as vol
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import (PLATFORM_SCHEMA)

__version__ = '0.0.5'

REQUIREMENTS = ['pyhaversion==0.0.2']

CONF_INSTALLATION = 'installation'
CONF_BRANCH = 'branch'
CONF_IMAGE = 'image'

SCAN_INTERVAL = timedelta(seconds=300)

PLATFORM_NAME = 'versions'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_INSTALLATION, default='venv'): cv.string,
    vol.Optional(CONF_BRANCH, default='stable'): cv.string,
    vol.Optional(CONF_IMAGE, default='default'): cv.string,
})

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Create the sensor"""
    installation = config.get(CONF_INSTALLATION)
    branch = config.get(CONF_BRANCH)
    image = config.get(CONF_IMAGE)
    add_devices([HomeAssistantVersion(installation, branch, image)])

class HomeAssistantVersion(Entity):
    """Representation of a Sensor."""

    def __init__(self, installation, branch, image):
        """Initialize the sensor."""
        self._installation = installation
        self._branch = branch
        self._image = image
        self._state = None
        self.update()

    def update(self):
        """Method to update sensor value"""
        from pyhaversion import HAVersion
        ha_version = HAVersion()
        if self._installation == 'venv' or self._installation == 'hassbian':
            source = 'pip'
        else:
            source = self._installation
        if self._branch == 'rc':
            branch = 'beta'
        else:
            branch = self._branch
        version = ha_version.get_version_number(source, branch, self._image)
        self._state = version

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'HA version ' + self._installation + ' ' + self._branch

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return 'mdi:package-up'
