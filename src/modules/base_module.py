from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseModule(ABC):
    """Base class for all task modules."""
    
    def __init__(self):
        """Initialize the module."""
        self.name = self.__class__.__name__
    
    @abstractmethod
    async def execute(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the module's task.
        
        Args:
            parameters (Dict[str, Any]): Parameters needed for task execution
            
        Returns:
            Dict[str, Any]: Result of the task execution
        """
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        """
        Get a description of what the module does.
        
        Returns:
            str: Module description
        """
        pass
    
    @abstractmethod
    def get_required_parameters(self) -> Dict[str, str]:
        """
        Get the required parameters for this module.
        
        Returns:
            Dict[str, str]: Dictionary of parameter names and their descriptions
        """
        pass
    
    def validate_parameters(self, parameters: Dict[str, Any]) -> bool:
        """
        Validate that all required parameters are present.
        
        Args:
            parameters (Dict[str, Any]): Parameters to validate
            
        Returns:
            bool: True if all required parameters are present, False otherwise
        """
        required = self.get_required_parameters()
        return all(param in parameters for param in required)
    
    def format_error(self, message: str) -> Dict[str, Any]:
        """
        Format an error response.
        
        Args:
            message (str): Error message
            
        Returns:
            Dict[str, Any]: Formatted error response
        """
        return {
            "status": "error",
            "message": message,
            "module": self.name
        }
    
    def format_success(self, data: Any) -> Dict[str, Any]:
        """
        Format a success response.
        
        Args:
            data (Any): The data to return
            
        Returns:
            Dict[str, Any]: Formatted success response
        """
        return {
            "status": "success",
            "data": data,
            "module": self.name
        } 