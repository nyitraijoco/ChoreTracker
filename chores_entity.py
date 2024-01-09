import logging
import uuid
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

class ChoresCollection(Entity):
    """Representation of a Chores Collection."""

    def __init__(self):
        """Initialize the Chores Collection."""
        self._chores = {}
        # Initialize with some default chores or leave it empty

    @property
    def name(self):
        """Return the name of the entity."""
        return 'Chores Collection'

    @property
    def state(self):
        """Return the state of the entity."""
        return None

    @property
    def device_state_attributes(self):
        """Return the state attributes of the entity."""
        return self._chores

    async def async_update(self, chore_id=None):
        """Update the last done date for a specific chore or all chores."""
        if chore_id:
            if chore_id in self._chores:
                self._chores[chore_id]['last_done'] = datetime.now().strftime('%Y-%m-%d')
            else:
                _LOGGER.warning(f"Chore with ID '{chore_id}' not found.")
        else:
            # Update all chores' last done date
            for chore_id in self._chores:
                self._chores[chore_id]['last_done'] = datetime.now().strftime('%Y-%m-%d')

    async def async_add_chore(self, chore_data):
        """Add a new chore."""
        chore_id = str(uuid.uuid4())[:8]  # Generate a unique ID
        # Validate and set effort within the range of 1 to 5
        effort = chore_data.get('effort', 1)  # Default to 1 if not specified
        effort = max(min(effort, 5), 1)  # Clamp within the range of 1 to 5
        chore_data['id'] = chore_id  # Assign the generated ID to the chore
        chore_data['effort'] = effort  # Update the chore's effort
        self._chores[chore_id] = chore_data

        # Optionally, trigger an update to Home Assistant to reflect the new chore
        await self.async_update_ha_state()

    async def async_remove_chore(self, chore_id):
        """Remove a chore."""
        if chore_id in self._chores:
            del self._chores[chore_id]
        else:
            _LOGGER.warning(f"Chore with ID '{chore_id}' not found.")

        # Optionally, trigger an update to Home Assistant to reflect the removed chore
        await self.async_update_ha_state()
