"""
Benchmark System - วัดความฉลาดของ AI
ทดสอบก่อนและหลังฝึก เพื่อเปรียบเทียบ
"""

import asyncio
import json
import os
from datetime import datetime
from typing import Dict, List
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import config
from core.unlimited_engine import UnlimitedAIEngine
from core.code_executor import CodeExecutor

class AIBenchmark:
    def __init__(self):
        self.ai = UnlimitedAIEngine()
        self.executor = CodeExecutor()
        self.results_path = os.path.join(config.DATA_PATH, 'benchmarks')
        os.makedirs(self.results_path, exist_ok=True)
        
        # Test cases (ตายตัว เพื่อเทียบได้)
        self.test_cases = [
            {
                'id': 1,
                'difficulty': 'easy',
                'instruction': 'create a function that adds two numbers',
                'test_input': 'result = add(5, 3)',
                'expected_output': '8'
            },
            {
                'id': 2,
                'difficulty': 'easy',
                'instruction': 'create a function that reverses a string',
                'test_input': 'result = reverse("hello")',
                'expected_output': 'olleh'
            },
            {
                'id': 3,
                'difficulty': 'medium',
                'instruction': 'create a function that checks if a number is prime',
                'test_input': 'result = is_prime(17)',
                'expected_output': 'True'
            },
            {
                'id': 4,
                'difficulty': 'medium',
                'instruction': 'create a function that finds fibonacci number at position n',
                'test_input': 'result = fibonacci(7)',
                'expected_output': '13'
            },
            {
                'id': 5,
                'difficulty': 'hard',
                'instruction': 'create a function that sorts a list using bubble sort',
                'test_input': 'result = bubble_sort([5,2,8,1,9])',
                'expected_output': '[1, 2, 5, 8, 9]'
            },
        ]
    
    async def run_benchmark(self, name: str = "benchmark") -> Dict:
        """
        รัน benchmark test
        
        Returns:
            Dict with scores and details
        """
        print("="*60)
        print(f"🧪 Running Benchmark: {name}")
        print("="*60)
        
        results = {
            'name': name,
            'timestamp': datetime.now().isoformat(),
            'total_tests': len(self.test_cases),
            'passed': 0,
            'failed': 0,
            'scores': {
                'easy': {'total': 0, 'passed': 0},
                'medium': {'total': 0, 'passed': 0},
                'hard': {'total': 0, 'passed': 0},
            },
            'details': []
        }
        
        for test in self.test_cases:
            print(f"\n📝 Test {test['id']}: [{test['difficulty'].upper()}] {test['instruction'][:50]}...")
            
            # Generate code
            gen_result = await self.ai.generate_code(
                instruction=test['instruction'],
                language='python'
            )
            
            if not gen_result['success']:
                print("❌ Failed to generate")
                results['failed'] += 1
                results['scores'][test['difficulty']]['total'] += 1
                continue
            
            code = gen_result['code']
            
            # Test code
            test_code = code + '\n' + test['test_input'] + '\nprint(result)'
            
            exec_result = self.executor.execute(test_code, 'python')
            
            if exec_result['success']:
                output = exec_result['stdout'].strip()
                expected = test['expected_output']
                
                if output == expected or output in expected or expected in output:
                    print(f"✅ PASS (output: {output})")
                    results['passed'] += 1
                    results['scores'][test['difficulty']]['passed'] += 1
                    status = 'pass'
                else:
                    print(f"❌ FAIL (expected: {expected}, got: {output})")
                    results['failed'] += 1
                    status = 'fail'
            else:
                print(f"❌ ERROR: {exec_result.get('stderr', 'Unknown')[:50]}")
                results['failed'] += 1
                status = 'error'
            
            results['scores'][test['difficulty']]['total'] += 1
            
            results['details'].append({
                'test_id': test['id'],
                'difficulty': test['difficulty'],
                'instruction': test['instruction'],
                'status': status,
                'code': code[:200] + '...' if len(code) > 200 else code
            })
        
        # Calculate final score
        results['score'] = round((results['passed'] / results['total_tests']) * 100, 1)
        
        # Print summary
        self._print_summary(results)
        
        # Save results
        self._save_results(results)
        
        return results
    
    def _print_summary(self, results: Dict):
        """พิมพ์สรุปผล"""
        print("\n" + "="*60)
        print("📊 BENCHMARK RESULTS")
        print("="*60)
        print(f"Name: {results['name']}")
        print(f"Time: {results['timestamp']}")
        print(f"\nTotal Tests: {results['total_tests']}")
        print(f"✅ Passed: {results['passed']}")
        print(f"❌ Failed: {results['failed']}")
        print(f"\n🏆 SCORE: {results['score']}/100")
        print()
        
        for diff in ['easy', 'medium', 'hard']:
            s = results['scores'][diff]
            if s['total'] > 0:
                pct = (s['passed'] / s['total']) * 100
                print(f"  {diff.upper():8} - {s['passed']}/{s['total']} ({pct:.0f}%)")
        
        print("="*60)
    
    def _save_results(self, results: Dict):
        """บันทึกผล"""
        filename = f"benchmark_{results['name']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(self.results_path, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Results saved: {filepath}")
    
    def compare_benchmarks(self, before_file: str, after_file: str):
        """เปรียบเทียบ 2 benchmarks"""
        
        with open(before_file, 'r', encoding='utf-8') as f:
            before = json.load(f)
        
        with open(after_file, 'r', encoding='utf-8') as f:
            after = json.load(f)
        
        print("="*60)
        print("📈 BENCHMARK COMPARISON")
        print("="*60)
        print(f"Before: {before['name']} - Score: {before['score']}/100")
        print(f"After:  {after['name']} - Score: {after['score']}/100")
        print()
        
        improvement = after['score'] - before['score']
        
        if improvement > 0:
            print(f"🎉 IMPROVED: +{improvement} points!")
        elif improvement < 0:
            print(f"⚠️ WORSE: {improvement} points")
        else:
            print("➖ NO CHANGE")
        
        print()
        print("Details by difficulty:")
        for diff in ['easy', 'medium', 'hard']:
            b = before['scores'][diff]
            a = after['scores'][diff]
            
            if b['total'] > 0:
                before_pct = (b['passed'] / b['total']) * 100
                after_pct = (a['passed'] / a['total']) * 100
                change = after_pct - before_pct
                
                symbol = "📈" if change > 0 else "📉" if change < 0 else "➖"
                print(f"  {diff.upper():8} - {before_pct:.0f}% → {after_pct:.0f}% ({symbol} {change:+.0f}%)")
        
        print("="*60)

# ========== วิธีใช้งาน ==========
if __name__ == "__main__":
    async def main():
        benchmark = AIBenchmark()
        
        print("🎯 AI Benchmark Tool")
        print()
        print("1. Run benchmark (before training)")
        print("2. Run benchmark (after training)")
        print("3. Compare two benchmarks")
        print()
        
        choice = input("Choose (1/2/3): ").strip()
        
        if choice == '1':
            await benchmark.run_benchmark(name="before_training")
        
        elif choice == '2':
            await benchmark.run_benchmark(name="after_training")
        
        elif choice == '3':
            print("\nAvailable benchmarks:")
            benchmarks_path = os.path.join(config.DATA_PATH, 'benchmarks')
            files = [f for f in os.listdir(benchmarks_path) if f.endswith('.json')]
            
            if len(files) < 2:
                print("❌ Need at least 2 benchmark files to compare")
                return
            
            for i, f in enumerate(files, 1):
                print(f"  {i}. {f}")
            
            b1 = int(input("\nBefore (number): ")) - 1
            b2 = int(input("After (number): ")) - 1
            
            file1 = os.path.join(benchmarks_path, files[b1])
            file2 = os.path.join(benchmarks_path, files[b2])
            
            benchmark.compare_benchmarks(file1, file2)
    
    asyncio.run(main())