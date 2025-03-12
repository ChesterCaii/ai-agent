import asyncio
from rich.console import Console
from rich.prompt import Prompt
from agent import Agent

async def main():
    """Main entry point for the AI Task Assistant."""
    console = Console()
    agent = Agent()
    
    # Display welcome message
    console.print("[bold blue]Welcome to the AI Task Assistant![/bold blue]")
    console.print("Type your commands in natural language. Type 'exit' to quit.\n")
    
    while True:
        try:
            # Get user input
            command = Prompt.ask("[bold green]Command[/bold green]")
            
            if command.lower() == 'exit':
                console.print("\n[bold blue]Goodbye![/bold blue]")
                break
            
            # Process the command
            response = await agent.process_command(command)
            
            # Display the response
            agent.display_response(response)
            
        except KeyboardInterrupt:
            console.print("\n[bold blue]Goodbye![/bold blue]")
            break
        except Exception as e:
            console.print(f"[red]Error: {str(e)}[/red]")

if __name__ == "__main__":
    asyncio.run(main()) 