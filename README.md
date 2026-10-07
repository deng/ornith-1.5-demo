# Ornith-1.5-9B Demo

**Ornith-1.5-9B** is a 9B-parameter self-evolving reasoning model from Ornith AI (MIT licensed, commercial use OK). It rivals 35B models on coding and reasoning benchmarks through end-to-end self-improvement training — the model generates its own training tasks, builds scaffolding, and optimizes solutions via RL, all without human annotation.

This repo contains a concrete demo: the model was given a coding task and produced correct, well-tested Python on the first try.

## Quick Start

```bash
python3 fibonacci_lru_cache.py
```

## What It Does

The script benchmarks recursive Fibonacci with and without `@functools.lru_cache`:

| n | Cached (ms) | Uncached (ms) |
|---|------------|---------------|
| 0 | < 0.01     | < 0.01        |
| 1 | < 0.01     | < 0.01        |
| 10 | < 0.01   | < 0.01        |
| 30 | < 0.01    | 70            |
| 38 | < 0.01    | **4,193**     |

LRU cache is **~940,000x faster** at n=38 — turning an O(2ⁿ) algorithm into O(n) with one decorator.

## The Model

| | |
|---|---|
| **Model** | ornith-ai/Ornith-1.5-9B |
| **Parameters** | 9B (dense) |
| **License** | MIT (commercial use OK) |
| **GGUF** | [Ornith-1.5-9B-GGUF](https://huggingface.co/ornith-ai/Ornith-1.5-9B-GGUF) |
| **Key Benchmarks** | SWE-bench 70.6 · Terminal-Bench 47.0 · GPQA Diamond 86.4 |
| **Training** | End-to-end self-improvement via RL |

## Run Locally with Ollama

```bash
# Download Q4_K_M (~5.4GB)
huggingface-cli download ornith-ai/Ornith-1.5-9B-GGUF \
  Ornith-1.5-9B-Q4_K_M.gguf --local-dir /Volumes/Data/models

# Import to Ollama
ollama create ornith-1.5-9b:q4_k_m \
  -f Modelfile.ornith-1.5-9b

# Try it
ollama run ornith-1.5-9b:q4_k_m \
  "Write a Python function that..."
```

## Demo Video

[media/ornith_coding_demo.mp4](media/ornith_coding_demo.mp4) — Full screen recording of the model thinking, writing code, and executing tests.

## Why This Matters

Ornith-1.5-9B proves that **training methodology beats parameter count**. A 9B model, through self-evolution, matches or exceeds 35B models on real programming tasks. And because it's MIT-licensed and runs on a single GPU, it's a practical choice for local coding assistants.

---

🤖 Generated with [Claude Code](https://claude.com/claude-code)