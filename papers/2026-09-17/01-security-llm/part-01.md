# 🔐 大模型安全相关研究 | 2026年09月17日

> 本类共 **3** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Universal Defenses for Tool-Integrated LLM Agents Against Adversarial Attacks](https://arxiv.org/abs/2609.16098)

**<font color=#1a73e8>作者：</font>** Xiaoyan Li, Yunli Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents have demonstrated impressive capabilities across a variety of domains, particularly when integrated with external tools for multi-step task completion. However, they are increasingly vulnerable to adversarial attacks, including direct prompt injection, indirect prompt injection, memory poisoning, and backdoor attacks, which exploit the model's openness to prompt injection and tool manipulation. In this work, we explore practical and generalizable defense strategies within a unified framework across these four attack types. We introduce two universal tool-based defenses: Attacker Tool Filtering, which uses anomaly detection (e.g., Isolation Forest) to identify and remove suspicious tools, and Normal Tool Recalling, a white-box method that restores the agent's original toolset prior to planning. Additionally, we incorporate prompt-based defenses: Chain-of-Thought prompting and self-reflection techniques to enhance reasoning and task paraphrasing to mitigate attacks. Experimental results across both four open-source LLMs (Gemma2-9B, Qwen2-7B, LLaMA3-8B, and LLaMA3.1-8B) and three proprietary LLMs (GPT-3.5, GPT-4, and GPT-5) show that our methods significantly reduce the Attack Success Rates (ASR), achieving 0% ASR in many settings, while preserving or even improving the original task success rate. These findings highlight the promise of simple, modular, multi-layered defenses for strengthening the security and robustness of tool-integrated LLM agents. The code is available at this https URL.

---


### 2. [Benchmarking Factual Robustness of LLMs via Multi-conversation Persuasion](https://arxiv.org/abs/2609.16777)

**<font color=#1a73e8>作者：</font>** Zhuoang Cai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) increasingly serve as primary knowledge retrieval interfaces, their robustness against \textit{persuasion attacks}---attempts to inject misinformation or enforce counterfactuals---has become a critical safety concern. Existing red-teaming frameworks typically evaluate models in multi-turn dialogues where the target model retains full conversation history. We identify a critical flaw in this setting termed \textbf{``Refusal Inertia''}: a model's initial refusal often propagates through subsequent turns largely to maintain contextual consistency, thereby masking its true vulnerability to sophisticated, isolated persuasion attempts. To rigorously evaluate the ``cold-start'' defense capabilities of SOTA models, we introduce the \textbf{SAST-IR} (Stateful Attacker, Stateless Target - Iterative Refinement) framework. By enforcing a memory wipe on the target while retaining the attacker's history, we simulate a worst-case adversarial setting using \textbf{multi-turn} (stateless) iterations. Leveraging \textbf{CP-Agent} (Cognitive Persuasion Agent), an enhanced diagnosis-guided agent, our experiments on the custom \textsc{CounterFact-Strict} dataset ($N=50$) yield alarming results: simple, diverse attack strategies achieved a staggering \textbf{96\%} success rate, exposing severe brittleness in memory-less defense. Furthermore, we reveal a \textbf{``Complexity Paradox''}: while complex, iteratively refined attacks are effective, they often trigger defensive compliance, whereas simple strategies achieve a higher rate of genuine persuasion (\textbf{84.7\%}). Our code and dataset are available at GitHub, this https URL.

---


### 3. [InceptionRAG: Stealthy Poisoning Attack Against Retrieval-Augmented Generation](https://arxiv.org/abs/2609.16818)

**<font color=#1a73e8>作者：</font>** Jiachang Zhang, Min Chen, Xiao Ren 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) systems enhance large language models (LLMs) with external knowledge but have been demonstrated to be vulnerable to corpus poisoning. Existing poisoning attacks against RAG largely focus on single-point explicit injection, where the malicious payload is fully encapsulated within a single document. Consequently, recent mitigation mechanisms have evolved to identify and diminish these threats effectively. In this paper, we first verify that existing mitigation mechanisms are insufficient for a new class of threats: indirect logic induction. Motivated by this observation, we introduce InceptionRAG, a stealthy attack mechanism that subverts the standard attack paradigm. Instead of injecting explicit malicious payloads, InceptionRAG fragments it into a chain of dormant passages. These passages appear harmless and can bypass existing mitigation mechanisms when examined separately. However, when retrieved together, they trigger LLMs to self-deduce target misinformation via multi-hop reasoning. To further improve the applicability of InceptionRAG in black-box settings, we propose zeroth-order suffix optimization (ZOSO) to automate the generation of authoritative suffixes. Extensive evaluations across three datasets and three LLMs demonstrate that InceptionRAG achieves an attack success rate exceeding 80% even under rigorous adversarial constraints. In particular, InceptionRAG shows superior evasion capabilities, effectively bypassing established defenses that mitigate traditional single-document injections. Our findings expose a concerning paradox: the stronger reasoning capabilities of LLMs increase their vulnerability to reasoning-based poisoning attacks. To mitigate potential misuse, we propose a document isolation-based defense, HODOR, which decouples adversarial logical dependencies.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
