import pytest
from datetime import datetime, timedelta
from ..modules.reminder_module import ReminderModule

@pytest.fixture
def reminder_module():
    """Create a ReminderModule instance for testing."""
    return ReminderModule()

@pytest.mark.asyncio
async def test_reminder_creation(reminder_module):
    """Test creating a new reminder."""
    # Set up test data
    future_time = datetime.now() + timedelta(minutes=5)
    parameters = {
        "task": "Test reminder",
        "time": future_time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Execute the reminder creation
    result = await reminder_module.execute(parameters)
    
    # Verify the result
    assert result["status"] == "success"
    assert "Test reminder" in result["data"]["task"]
    assert len(reminder_module.reminders) == 1

@pytest.mark.asyncio
async def test_invalid_time(reminder_module):
    """Test creating a reminder with past time."""
    # Set up test data with past time
    past_time = datetime.now() - timedelta(minutes=5)
    parameters = {
        "task": "Test reminder",
        "time": past_time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Execute the reminder creation
    result = await reminder_module.execute(parameters)
    
    # Verify the result
    assert result["status"] == "error"
    assert "must be in the future" in result["message"]
    assert len(reminder_module.reminders) == 0

@pytest.mark.asyncio
async def test_missing_parameters(reminder_module):
    """Test creating a reminder with missing parameters."""
    # Set up test data with missing time
    parameters = {
        "task": "Test reminder"
    }
    
    # Execute the reminder creation
    result = await reminder_module.execute(parameters)
    
    # Verify the result
    assert result["status"] == "error"
    assert "Missing required parameters" in result["message"]
    assert len(reminder_module.reminders) == 0 