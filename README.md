# LLM Safety Benchmark Processing

Data processing utilities for the AgentHarm benchmark dataset.

## About AgentHarm

AgentHarm evaluates agentic AI capabilities and safety boundaries through adversarial testing. The benchmark measures how LLM agents handle requests across harmful, benign, and conversational scenarios.

## Source

Based on [AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](https://arxiv.org/abs/2410.09024) by Andriushchenko et al., 2024.

**Original dataset:** https://huggingface.co/datasets/ai-safety-institute/AgentHarm

## Processing Approach

Scripts extract and normalize benchmark behaviors from JSON format into structured CSV for analysis. Separates harmful, benign, and chat test cases while preserving grading metadata.

## Usage

```bash
python convert_to_csv.py
# Outputs: agentharm_dataset.csv

python make_csv.py
# Outputs: agentharm_full.csv
```

## Contents

- `convert_to_csv.py` - JSON to CSV conversion with error handling
- `make_csv.py` - Streamlined CSV generation
- `agentharm_dataset.csv` - Processed benchmark behaviors
- `agentharm_full.csv` - Complete dataset export

## Requirements

Python 3.8+ (standard library only)

## License

Original benchmark: MIT License with additional safety research clause (see LICENSE)
