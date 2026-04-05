#!/usr/bin/env python3
"""
ArXiv Paper Correlation Analyzer
Uses LLM semantic analysis to classify papers into correlation levels.
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# Try to import OpenAI, but don't fail if not available
try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

# Configuration
BASE_DIR = Path.home() / "Documents" / "arxiv每日阅读"
DAILY_DIR = BASE_DIR / "daily"

# Classification prompt template
CLASSIFICATION_PROMPT = """You are an expert in computer science and AI research. Analyze the following arXiv paper title and classify it into one of four levels based on its relevance to large language models (LLMs).

Paper Title: {title}

Classification Levels:
1. **大模型安全相关研究** - Directly discusses LLM safety issues (safety, security, alignment, privacy, fairness, hallucination detection, interpretability, jailbreak, adversarial attacks, etc.)

2. **大模型内生能力研究** - Explores LLM capabilities (reasoning, planning, knowledge, memory, in-context learning, chain-of-thought, tool use, code generation, math reasoning, scaling, emergence, etc.)

3. **大模型相关研究** - Related to LLMs but not specifically safety or capability exploration (LLM architecture, training, fine-tuning, MoE, RAG, multimodal, agents, etc.)

4. **其他研究** - Not related to LLMs (traditional ML, CV, NLP non-LLM, other CS areas)

Instructions:
- Analyze the semantic meaning of the title
- Consider the main focus of the research
- If uncertain between levels, choose the lower number (more specific)

Output your response in this exact JSON format:
{{
  "level": 1,
  "reasoning": "Brief explanation of why this level was chosen"
}}

Respond with only the JSON, no other text."""


def get_llm_client():
    """Initialize LLM client from environment variables."""
    # Priority: user-provided key > environment variables
    api_key = "sk-kimi-zxHeXjGYWdKcL4L8SVTukUXsHoUEgyH6k518vM60W0hSGhpVJopTXOYNpaIuJk5p"
    base_url = "https://api.moonshot.cn/v1"
    
    # Allow override from environment
    if os.getenv("OPENAI_API_KEY") or os.getenv("LLM_API_KEY"):
        api_key = os.getenv("OPENAI_API_KEY") or os.getenv("LLM_API_KEY")
        base_url = os.getenv("LLM_BASE_URL") or os.getenv("OPENAI_BASE_URL") or "https://api.moonshot.cn/v1"
    
    try:
        return OpenAI(api_key=api_key, base_url=base_url)
    except Exception as e:
        print(f"❌ Error initializing LLM client: {e}")
        return None


def classify_with_llm(title, client, model="gpt-4o-mini"):
    """Classify a paper using LLM semantic analysis."""
    if not client:
        return None, "LLM client not available"
    
    prompt = CLASSIFICATION_PROMPT.format(title=title)
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful research assistant specializing in AI paper classification."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=150
        )
        
        content = response.choices[0].message.content.strip()
        
        # Extract JSON from response
        # Handle cases where LLM wraps JSON in markdown code blocks
        json_match = re.search(r'\{[\s\S]*\}', content)
        if json_match:
            content = json_match.group(0)
        
        result = json.loads(content)
        level = result.get("level", 4)
        reasoning = result.get("reasoning", "")
        
        # Validate level
        if not isinstance(level, int) or level < 1 or level > 4:
            level = 4
        
        return level, reasoning
        
    except Exception as e:
        return None, f"LLM error: {str(e)}"


def classify_with_rules(title):
    """Fallback classification using keyword rules when LLM is unavailable."""
    title_lower = title.lower()
    
    # Level 1: Safety-related keywords
    safety_keywords = [
        "safety", "security", "robustness", "attack", "defense",
        "adversarial", "jailbreak", "poisoning", "backdoor",
        "toxicity", "harmful", "malicious", "vulnerability",
        "alignment", "RLHF", "red teaming", "privacy",
        "fairness", "bias", "hallucination detection",
        "interpretability", "explainability", "trustworthiness",
        "risk", "ethical", "governance"
    ]
    
    for kw in safety_keywords:
        if kw in title_lower:
            return 1, f"Rule-based: matched '{kw}'"
    
    # Level 2: Capability-related keywords
    capability_keywords = [
        "reasoning", "planning", "problem solving",
        "knowledge", "memory", "generalization",
        "few-shot", "zero-shot", "in-context learning",
        "chain-of-thought", "CoT", "tool use",
        "code generation", "programming", "math",
        "creativity", "summarization", "translation",
        "instruction following", "scaling", "emergence"
    ]
    
    for kw in capability_keywords:
        if kw in title_lower:
            return 2, f"Rule-based: matched '{kw}'"
    
    # Level 3: LLM-related keywords
    llm_keywords = [
        "LLM", "language model", "foundation model",
        "transformer", "GPT", "BERT", "T5",
        "multimodal", "reinforcement learning",
        "fine-tuning", "pre-training", "MoE",
        "rag", "retrieval augmented", "agent"
    ]
    
    for kw in llm_keywords:
        if kw.lower() in title_lower:
            return 3, f"Rule-based: matched '{kw}'"
    
    # Level 4: Other
    return 4, "Rule-based: no LLM keywords found"


def analyze_paper(paper, client, use_llm=True):
    """Analyze a single paper and return correlation level."""
    title = paper.get('title', '')
    
    if use_llm and client:
        level, reasoning = classify_with_llm(title, client)
        if level is not None:
            return level, reasoning
        # Fall back to rules if LLM fails
    
    return classify_with_rules(title)


def analyze_daily_file(date_str=None, use_llm=True, model="moonshot-v1-8k"):
    """Analyze papers for a specific date."""
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')
    
    input_file = DAILY_DIR / f"{date_str}.json"
    
    if not input_file.exists():
        print(f"❌ Error: File not found: {input_file}")
        return None
    
    # Load papers
    with open(input_file, 'r', encoding='utf-8') as f:
        papers = json.load(f)
    
    # Initialize LLM client if requested
    client = None
    method = "LLM semantic analysis"
    if use_llm:
        client = get_llm_client()
        if not client:
            print("⚠️  LLM not available, falling back to keyword rules")
            method = "Keyword rules (LLM unavailable)"
    else:
        method = "Keyword rules (LLM disabled)"
    
    print(f"\n{'='*60}")
    print(f"Analyzing {len(papers)} papers from {date_str}")
    print(f"Method: {method}")
    print(f"{'='*60}\n")
    
    # Analyze each paper
    stats = {1: 0, 2: 0, 3: 0, 4: 0}
    
    for i, paper in enumerate(papers):
        title = paper.get('title', 'Untitled')
        level, reasoning = analyze_paper(paper, client, use_llm)
        paper['correlation'] = level
        stats[level] += 1
        
        # Print progress
        print(f"[{i+1}/{len(papers)}] Level {level}: {title[:60]}...")
        print(f"       → {reasoning[:80]}...")
        
        # Progress indicator every 10 papers
        if (i + 1) % 10 == 0:
            print(f"\n📊 Progress: {i+1}/{len(papers)} papers analyzed\n")
    
    # Save updated papers
    with open(input_file, 'w', encoding='utf-8') as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)
    
    print(f"\n{'='*60}")
    print("✅ Analysis complete!")
    print(f"\n📈 Correlation distribution:")
    print(f"  Level 1 (大模型安全):    {stats[1]:3d} papers")
    print(f"  Level 2 (大模型能力):    {stats[2]:3d} papers")
    print(f"  Level 3 (大模型相关):    {stats[3]:3d} papers")
    print(f"  Level 4 (其他研究):      {stats[4]:3d} papers")
    print(f"\n💾 Updated: {input_file}")
    print(f"{'='*60}")
    
    return stats


def main():
    """Main entry point."""
    # Parse arguments
    date_str = None
    use_llm = True
    model = "moonshot-v1-8k"
    
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--no-llm":
            use_llm = False
        elif args[i] == "--model" and i + 1 < len(args):
            model = args[i + 1]
            i += 1
        elif not date_str and not args[i].startswith("-"):
            date_str = args[i]
        i += 1
    
    # Check dependencies
    if use_llm and not HAS_OPENAI:
        print("⚠️  OpenAI package not installed. Run: pip install openai")
        print("   Falling back to keyword rules...")
        use_llm = False
    
    # Analyze
    stats = analyze_daily_file(date_str, use_llm, model)
    
    if stats:
        print("\n🎉 Done!")
        sys.exit(0)
    else:
        print("\n❌ Failed to analyze papers.")
        sys.exit(1)


if __name__ == "__main__":
    main()
