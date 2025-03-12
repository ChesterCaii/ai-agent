import os
import sys
from typing import Dict, Any, List
from openai import AsyncOpenAI
import traceback
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

# Load environment variables
load_dotenv()

# Configure OpenAI
api_key = os.getenv("OPENAI_API_KEY")

class Agent:
    def __init__(self):
        """Initialize the AI Task Assistant agent."""
        self.console = Console()
        self.modules = {}
        self._load_modules()
        
        # Verify API key is set
        if not api_key:
            raise ValueError("OpenAI API key is not set. Please check your .env file.")
        self.console.print(f"[green]API key loaded: {api_key[:6]}...{api_key[-4:]}[/green]")
        
        # Initialize OpenAI client
        self.client = AsyncOpenAI(api_key=api_key)

    def _load_modules(self):
        """Load all available task modules."""
        # TODO: Implement dynamic module loading
        pass

    async def process_command(self, command: str) -> Dict[str, Any]:
        """
        Process a natural language command and execute the appropriate action.
        
        Args:
            command (str): The natural language command from the user
            
        Returns:
            Dict[str, Any]: Response containing the action taken and any relevant data
        """
        try:
            # Parse the command using the LLM
            response = await self._analyze_command(command)
            
            # Execute the appropriate module based on the command analysis
            result = await self._execute_task(response)
            
            return result
        except Exception as e:
            error_msg = f"Error: {str(e)}\n{traceback.format_exc()}"
            self.console.print(f"[red]{error_msg}[/red]")
            return {"status": "error", "message": error_msg}

    async def _analyze_command(self, command: str) -> Dict[str, Any]:
        """
        Analyze the command using the LLM to determine intent and extract parameters.
        
        Args:
            command (str): The natural language command
            
        Returns:
            Dict[str, Any]: Parsed command with intent and parameters
        """
        try:
            self.console.print("[yellow]Sending request to OpenAI...[/yellow]")
            
            messages = [
                {"role": "system", "content": "You are an AI assistant that analyzes user commands and extracts structured information. Respond with JSON containing 'intent' and 'parameters'."},
                {"role": "user", "content": command}
            ]
            
            # Print debug information
            self.console.print(f"[blue]Using API key: {api_key[:6]}...{api_key[-4:]}[/blue]")
            self.console.print(f"[blue]Messages: {messages}[/blue]")
            
            response = await self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.1
            )
            
            self.console.print("[green]Received response from OpenAI[/green]")
            
            if not response or not response.choices:
                raise ValueError("Invalid response from OpenAI API")
            
            # Get the assistant's response
            assistant_message = response.choices[0].message.content
            self.console.print(f"[blue]Assistant response: {assistant_message}[/blue]")
            
            # For now, return a basic response until we implement proper parsing
            return {
                "intent": "echo",
                "parameters": {
                    "message": assistant_message
                }
            }
            
        except Exception as e:
            raise Exception(f"Error processing command: {str(e)}\n{traceback.format_exc()}")

    async def _execute_task(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the appropriate task based on the analyzed command.
        
        Args:
            task_data (Dict[str, Any]): The analyzed command data
            
        Returns:
            Dict[str, Any]: Result of the task execution
        """
        intent = task_data.get("intent")
        if intent in self.modules:
            return await self.modules[intent].execute(task_data["parameters"])
        else:
            # For now, just echo back the message for testing
            if intent == "echo":
                return {
                    "status": "success",
                    "message": task_data["parameters"]["message"]
                }
            return {
                "status": "error",
                "message": f"No module found for intent: {intent}"
            }

    def display_response(self, response: Dict[str, Any]):
        """
        Display the response to the user in a formatted way.
        
        Args:
            response (Dict[str, Any]): The response data to display
        """
        status = response.get("status", "unknown")
        message = response.get("message", "No message provided")
        
        if status == "success":
            self.console.print(Panel(message, title="Success", style="green"))
        else:
            self.console.print(Panel(message, title="Error", style="red"))

    def benchmark(self) -> Dict[str, Any]:
        """
        Run performance benchmarks on the agent.
        
        Returns:
            Dict[str, Any]: Benchmark results
        """
        # TODO: Implement benchmarking
        return {
            "status": "not_implemented",
            "message": "Benchmarking not yet implemented"
        } 