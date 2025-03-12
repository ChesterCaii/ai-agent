import asyncio
import time
from datetime import datetime, timedelta
from rich.console import Console
from rich.table import Table
from ..agent import Agent

async def run_benchmark(agent: Agent, commands: list[str]) -> dict:
    """
    Run performance benchmarks on a set of commands.
    
    Args:
        agent (Agent): The agent instance to benchmark
        commands (list[str]): List of commands to test
        
    Returns:
        dict: Benchmark results
    """
    results = {
        "total_time": 0,
        "successful_commands": 0,
        "failed_commands": 0,
        "average_response_time": 0,
        "response_times": []
    }
    
    for command in commands:
        start_time = time.time()
        response = await agent.process_command(command)
        end_time = time.time()
        
        response_time = end_time - start_time
        results["response_times"].append(response_time)
        
        if response["status"] == "success":
            results["successful_commands"] += 1
        else:
            results["failed_commands"] += 1
    
    results["total_time"] = sum(results["response_times"])
    results["average_response_time"] = results["total_time"] / len(commands)
    
    return results

def display_results(results: dict):
    """
    Display benchmark results in a formatted table.
    
    Args:
        results (dict): Benchmark results to display
    """
    console = Console()
    
    table = Table(title="Benchmark Results")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")
    
    table.add_row("Total Time", f"{results['total_time']:.2f}s")
    table.add_row("Average Response Time", f"{results['average_response_time']:.2f}s")
    table.add_row("Successful Commands", str(results["successful_commands"]))
    table.add_row("Failed Commands", str(results["failed_commands"]))
    table.add_row(
        "Success Rate",
        f"{(results['successful_commands'] / (results['successful_commands'] + results['failed_commands'])) * 100:.1f}%"
    )
    
    console.print(table)

async def main():
    """Run the benchmark suite."""
    # Sample commands for benchmarking
    test_commands = [
        "Remind me to call John tomorrow at 2pm",
        "Set a reminder for team meeting in 30 minutes",
        "Invalid command with no clear intent",
        "Remind me to check email in 5 minutes",
        "Set an alarm for yesterday",  # Should fail
    ]
    
    agent = Agent()
    console = Console()
    
    console.print("[bold blue]Running benchmarks...[/bold blue]")
    results = await run_benchmark(agent, test_commands)
    display_results(results)

if __name__ == "__main__":
    asyncio.run(main()) 