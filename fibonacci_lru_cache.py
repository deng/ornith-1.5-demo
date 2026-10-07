#!/usr/bin/env python3
"""
Ornith-1.5-9B Demo — LRU-Cached Fibonacci

This script was generated in real-time by Ornith-1.5-9B (MIT-licensed, self-evolving 9B model)
and is reproduced here for you to run locally.

Model: ornith-ai/Ornith-1.5-9B (GGUF Q4_K_M)
"""

import functools
import time
import sys


@functools.lru_cache(maxsize=None)
def fibonacci_cached(n: int) -> int:
    """Recursive Fibonacci with LRU cache — O(n) after warm-up."""
    if n < 2:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


def fibonacci_uncached(n: int) -> int:
    """Plain recursive Fibonacci — O(2^n), exponential."""
    if n < 2:
        return n
    return fibonacci_uncached(n - 1) + fibonacci_uncached(n - 2)


def time_function(func, *args):
    start = time.perf_counter()
    result = func(*args)
    elapsed = (time.perf_counter() - start) * 1000
    return result, elapsed


def main():
    print("Ornith-1.5-9B Demo — Fibonacci LRU Cache Benchmark\n")
    print("Model:  ornith-ai/Ornith-1.5-9B (9B params, Q4_K_M)")
    print("Task:   Recursive Fibonacci — with vs without @lru_cache\n")

    # n=40 uncached takes ~30s, n=45 takes ~5min. Cap at 38 for reasonable demo.
    test_values = [0, 1, 10, 30, 38]

    print(f"{'n':>4} | {'cached result':>15} | {'uncached result':>15}")
    print("-" * 52)

    for n in test_values:
        cached_result, cached_time = time_function(fibonacci_cached, n)

        # n >= 35 is very slow uncached, show a progress note
        if n >= 35:
            sys.stdout.write(f"{n:>4} | computing cached...\r")
            sys.stdout.flush()

        uncached_result, uncached_time = time_function(fibonacci_uncached, n)

        print(f"{n:>4} | {cached_result:>15} | {uncached_result:>15}")
        print(f"     cached: {cached_time:>8.3f} ms   uncached: {uncached_time:>9.1f} ms")

        if uncached_time > 1000:
            speedup = uncached_time / max(cached_time, 0.001)
            print(f"     ⚡ LRU cache is {speedup:,.0f}x faster for n={n}")

    # Verify correctness
    print()
    all_match = all(
        fibonacci_cached(n) == fibonacci_uncached(n)
        for n in test_values
    )
    print(f"  All results match: {all_match}")

    # Summary
    print(f"\n{'='*52}")
    print(f"  Summary: @lru_cache makes recursive Fibonacci practical")
    print(f"  Model:   Ornith-1.5-9B (MIT open-source, commercial use OK)")
    print(f"  Repo:    https://github.com/deng/ornith-1.5-demo")
    print(f"{'='*52}")


if __name__ == "__main__":
    main()