"""
Admin CLI Tool - เครื่องมือ Admin ครบวงจร
คุณคือ Admin - ควบคุมทุกอย่าง
"""

import click
import asyncio
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import config
from core.unlimited_engine import UnlimitedAIEngine
from core.memory_system import MemorySystem
from core.code_executor import CodeExecutor
from core.file_analyzer import FileAnalyzer

@click.group()
def cli():
    """🔥 God-Tier AI Admin CLI"""
    pass

@cli.command()
@click.option('-i', '--instruction', required=True, help='Code instruction')
@click.option('-l', '--language', default='python', help='Programming language')
@click.option('-o', '--output', help='Output file')
def generate(instruction, language, output):
    """Generate code"""
    async def run():
        ai = UnlimitedAIEngine()
        result = await ai.generate_code(instruction, language)
        
        if result['success']:
            print("✅ Generated:\n")
            print(result['code'])
            
            if output:
                filepath = os.path.join(config.PROJECTS_PATH, output)
                with open(filepath, 'w') as f:
                    f.write(result['code'])
                print(f"\n💾 Saved to: {filepath}")
        else:
            print(f"❌ Error: {result.get('error')}")
    
    asyncio.run(run())

@cli.command()
@click.option('-f', '--file', required=True, help='Code file')
@click.option('-l', '--language', default='python', help='Language')
def execute(file, language):
    """Execute code file"""
    if not os.path.exists(file):
        print(f"❌ File not found: {file}")
        return
    
    with open(file, 'r') as f:
        code = f.read()
    
    executor = CodeExecutor()
    result = executor.execute(code, language)
    
    if result['success']:
        print("✅ Output:")
        print(result['stdout'])
        if result['stderr']:
            print("\n⚠️ Stderr:")
            print(result['stderr'])
    else:
        print(f"❌ Error: {result.get('error')}")

@cli.command()
@click.option('-f', '--file', required=True, help='File to analyze')
def analyze(file):
    """Analyze file"""
    analyzer = FileAnalyzer()
    result = analyzer.analyze_file(file)
    
    if result['success']:
        print("📊 Analysis:")
        for key, value in result.items():
            print(f"  {key}: {value}")
    else:
        print(f"❌ Error: {result.get('error')}")

@cli.command()
@click.option('-l', '--limit', default=10, help='Number of records')
def history(limit):
    """Show code history"""
    memory = MemorySystem()
    history = memory.get_code_history(limit)
    
    if history:
        for i, item in enumerate(history, 1):
            print(f"\n{i}. [{item['language']}] {item['timestamp']}")
            print(f"   {item['instruction']}")
            print(f"   {item['code'][:100]}...")
    else:
        print("No history")

@cli.command()
def stats():
    """Show statistics"""
    memory = MemorySystem()
    stats = memory.get_stats()
    
    print("📊 Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value}")

@cli.command()
@click.confirmation_option(prompt='Clear ALL data?')
def clear():
    """Clear all data"""
    memory = MemorySystem()
    memory.clear_all()
    print("✅ All data cleared!")

@cli.command()
def info():
    """Show system info"""
    print("="*60)
    print("🔥 GOD-TIER AI SYSTEM INFO")
    print("="*60)
    config.print_config()

if __name__ == '__main__':
    cli()