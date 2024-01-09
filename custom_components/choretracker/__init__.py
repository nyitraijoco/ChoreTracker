import logging
import uuid
from .chores_entity import ChoresCollection

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'chore_tracker'

async def async_setup_entry(hass, config_entry):
    """Set up the Chores Collection entity."""
    hass.data.setdefault('chores_collection', ChoresCollection())
    return True

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Custom Entity."""
    async_add_entities([ChoresCollection()])


async def async_add_chore(self, chore_data):
    """Add a new chore."""
    chore_id = str(uuid.uuid4())[:8]  # Generate a unique ID
    # Ensure effort falls within the range of 1 to 5
    effort = chore_data.get('effort', 1)  # Default to 1 if not specified
    effort = max(min(effort, 5), 1)  # Clamp within the range of 1 to 5
    chore_data['id'] = chore_id  # Assign the generated ID to the chore
    chore_data['effort'] = effort  # Update the chore's effort
    self._chores[chore_id] = chore_data