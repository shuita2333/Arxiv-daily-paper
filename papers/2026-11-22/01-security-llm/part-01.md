# 🔐 大模型安全相关研究 | 2026年11月22日

> 本类共 **2** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [DSFlow: A Neuro-Symbolic Data Workflow Agent with Statistical Diagnostic Guardrails](https://arxiv.org/abs/2611.25111)

**<font color=#1a73e8>作者：</font>** Junfeng Nie, Xiaohui Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data science workflows often require tools that presume non-trivial technical knowledge. Large language models (LLMs) reduce this barrier, but a gap remains between flexible general-purpose agents and statistically controlled pipelines. We introduce DSFlow, a LangGraph-based neuro-symbolic data-agent platform that combines reusable, LLM-selected skills with deterministic diagnostic guardrails. Skills provide extensible task knowledge. Symbolic validation can accept a proposed method, request clarification or replanning, override an unsuitable method, or supply a safe fallback. Regression and clustering case studies illustrate how DSFlow uses diagnostic evidence to correct method choices and documents those decisions in auditable reports.

---


### 2. [Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)](https://arxiv.org/abs/2611.26553)

**<font color=#1a73e8>作者：</font>** Mengxiao Wang, Mahbub Alam, Kalyan Nakka 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agents based on large language models (LLMs) can now delete files and send payments on behalf of their users. News media reports routinely describe failures of these agents (e.g., Replit's coding agent deleting a production database), but a report often only says what went wrong and rarely (in)validates the incident or finds its root cause. Incident catalogs collect these reports, and benchmarks record whether agents fail, but neither replicates an incident nor tests the cause its report might identify. In this paper, we present ROGUE-AI (Replication of Agentic Security Events: Audit and Investigation), a multi-agent framework that closes the above gap and rebuilds each reported incident offline together with a matched control that lacks only the blamed cause, and runs agents on both. Our results suggest that ROGUE-AI is able to reproduce the reported harm in 89% of its 108 attempted replications. Agents built on five current GPT, Claude, Gemini and DeepSeek models made the reported mistake in 18% to 33% of runs, against at most 1% without the blamed cause. Of the 72 incidents with real-world harm, 62 had no underlying attacker, and in these, agents did what their task asked for but missed an ordinary hazard, such as a database shared with the live site. Replications without an attacker caused more harm than replications of prompt injection for all five models. Defenses against prompt injection look for injected instructions, but these replications contain none. Further, a warning after each tool output that names the hazard and its consequence lowered harm for all five models, whereas a note of the same length that does not mention the hazard left most of the harm in place. Built from real incidents, the ROGUE-AI replications form a reusable audit framework that vendors can rerun before each new release.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
