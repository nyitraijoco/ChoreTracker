import logging
import uuid
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'chore_tracker'


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Custom Entity."""
    async_add_entities([ChoresCollection()])


class ChoresCollection(Entity):
    """Representation of a Chores Collection."""

    def __init__(self):
        """Initialize the Chores Collection."""

    @property
    def name(self):
        """Return the name of the entity."""
        return 'Chores Collection'

    @property
    def state(self):
        """Return the state of the entity."""
        # For a group entity, the state might not be meaningful
        return None

    @property
    def device_state_attributes(self):
        """Return the state attributes of the entity."""
        return self._chores

    async def async_update(self, chore_id=None):
        """Update the entity or specific chore's last done date."""
        if chore_id:
            if chore_id in self._chores:
                self._chores[chore_id]['last_done'] = datetime.now().strftime('%Y-%m-%d')
            else:
                _LOGGER.warning(f"Chore with ID '{chore_id}' not found.")

async def async_add_chore(self, chore_data):
    """Add a new chore."""
    chore_id = str(uuid.uuid4())[:8]  # Generate a unique ID
    # Ensure effort falls within the range of 1 to 5
    effort = chore_data.get('effort', 1)  # Default to 1 if not specified
    effort = max(min(effort, 5), 1)  # Clamp within the range of 1 to 5
    chore_data['id'] = chore_id  # Assign the generated ID to the chore
    chore_data['effort'] = effort  # Update the chore's effort
    self._chores[chore_id] = chore_data
