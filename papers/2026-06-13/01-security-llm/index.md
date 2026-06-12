# 🔐 大模型安全相关研究 | 2026年06月13日

> 本类共 **5** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Influence Factors on RAG Poisoning](https://arxiv.org/abs/2606.12469)

**<font color=#1a73e8>作者：</font>** Pedro Pereira, Eva Maia, Isabel Praça 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems enhance large language models by grounding responses in retrieved documents from external knowledge sources at inference time. However, this reliance on retrieved content introduces vulnerabilities to poisoning attacks, in which adversarial documents can manipulate both the retrieval process and the generated outputs. This paper investigates poisoning robustness in RAG through a full factorial experimental study covering 432 configurations. We analyze the impacts of dataset, retriever type, retrieval depth, database composition, chunking strategy, and generator model on retrieval-level and generation-level metrics. The results show that retriever architecture, dataset, and retrieval depth are the strongest factors affecting poisoning exposure, while generator choice and database composition have a major impact on downstream attack success. Dense and graph-based retrievers generally improve robustness relative to BM25, whereas larger retrieval depth increases the likelihood of retrieving poisoned passages. We further show that replicating poisoned content across multiple databases amplifies adversarial influence, while additional clean sources can mitigate it. These findings highlight that poisoning vulnerability in RAG is not attributable to a single component, but instead arises from the interaction of retrieval, generation, and knowledge-base configuration.

---


### 2. [Beyond Attack Success Rate: Examining Trigger Leakage in Vision-Language Agentic Systems](https://arxiv.org/abs/2606.12586)

**<font color=#1a73e8>作者：</font>** Jiamin Chang, Salil Kanhere, Piotr Koniusz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vision-Language Agentic Systems (VLAS) connect visual perception to planning, tool use, and physical actions. This means backdoor-type triggers can propagate through both decision pipelines and their connected interfaces, thus making visual backdoors a system-level threat. Current evaluations on such backdoors focus on clean accuracy and attack success rate (ASR), metrics that capture whether a trigger works, but not whether an attack is actually "precise" -- i.e. whether it triggers hidden behaviors only when intended. In this work, we formalize the failure of trigger precision as "trigger leakage": inputs that are visually or semantically close to the intended trigger and therefore inadvertently activate the attacker-specified behavior. To quantify this leakage, we introduce Neighbor Leakage Rate (NLR). Our experiments show that at a 3% poisoning ratio, icon and text triggers remain robust to common visual transformations, but their neighboring variants leak heavily, with NLR reaching 0.996 (icon) and 0.944 (text). Using textual triggers as a controlled probe, we show that standard fine-tuning learns a broad activation region rather than an exact trigger condition, causing neighboring strings to invoke the malicious behavior even when the exact trigger is absent. Adding edit-distance-one hard-negative samples during training substantially narrows this activation region and reduces leakage, including in image-editing and embodied-manipulation workflows, where leaked triggers can propagate into executable programs and action sequences.

---


### 3. [SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems](https://arxiv.org/abs/2606.12703)

**<font color=#1a73e8>作者：</font>** Tarun Sharma  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) agents increasingly run with persistent memory that accumulates across user sessions. This creates a new attack surface: an adversary interacting only through normal channels can inject crafted memories that, once retrieved, steer the agent's responses for future users, without touching model weights or code. We call this Multi-Session Memory Poisoning (MSMP) and show that no existing defence certifies against it; static-corpus defences (RobustRAG, ReliabilityRAG) assume a fixed knowledge base, and heuristic filters are bypassed by fluent enterprise-style text. We present Signed Memory with Smoothed Retrieval (SMSR), the first defence with a certified robustness bound for this setting. Component 1 adds HMAC-SHA256 provenance at write time, blocking unsigned injection. Component 2 applies randomised memory ablation with verdict-based majority voting at query time, bounding the influence of authenticated adversaries. We prove that no provenance-free retrieval-time filter can certify against adaptive injection, derive a hypergeometric certificate for Component 2, and formalise the Consistent Minority Effect, whereby a consistent adversarial answer wins string-based voting as a numerical minority while verdict-based voting removes it. Across 15 enterprise scenarios (3,150 repeated trials), Component 1 cuts attack success from 93-100% to 0% for all unsigned variants. For an authenticated adversary with a single injection, Component 2 holds success to 8.0% (95% CI [5.8, 10.9], n=450), below the certified worst case. In an end-to-end query-only attack where the agent itself writes the poison rather than it being pre-seeded, SMSR reduces success from 65.3% to 5.3% (n=150, non-overlapping CIs) on a live agent stack. Clean-query utility is 90% (Component 1) and 85% (combined).

---


### 4. [PI-Hunter: Automated Red-Teaming for Exposing and Localizing Prompt Injections](https://arxiv.org/abs/2606.12737)

**<font color=#1a73e8>作者：</font>** Pengfei He, Lesly Miculicich, Vishesh Sharma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are rapidly evolving into agentic systems that interact with external tools and environments, introducing new security risks such as indirect prompt injection attacks through untrusted external sources. Existing defenses mainly focus on blocking malicious content at inference time, and current red-teaming methods primarily optimize attack success. As a result, developers have limited visibility into how latent prompt injections emerge and propagate through agents. We propose PI-Hunter, an automated agentic auditing framework for proactive vulnerability exposure in LLM agents. PI-Hunter constructs realistic source-aware test cases and iteratively evolves them through feedback-driven exploration to induce agents to retrieve and reveal latent malicious instructions embedded within external environments. Extensive experiments across multiple benchmarks, agent architectures, attacks, and defenses demonstrate that PI-Hunter substantially improves vulnerability exposure and attack-surface coverage over strong automated red-teaming baselines, while remaining effective under existing prompt injection defenses.

---


### 5. [The Emergence of Autonomous Penetration Capabilities in Large Language Model-Powered AI Systems](https://arxiv.org/abs/2606.13079)

**<font color=#1a73e8>作者：</font>** Jiaqi Luo, Jiarun Dai, Zhile Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Nowadays, the autonomous execution of cyberattacks capable of causing substantial real-world harm is widely regarded as one of the critical red lines that frontier AI systems must not cross. Within this broader red-line scenario, autonomous penetration represents a core enabling capability and subtask: the ability of LLM-powered AI systems to independently conduct adversarial operations against a target server without human intervention, identify and exploit vulnerabilities, and obtain unauthorized access or control. A growing body of work has sought to assess the autonomous penetration capabilities of AI systems. However, existing evaluations often employ opaque methodologies, rely on unrealistic or overly simplified penetration-testing scenarios, or provide LLMs with excessive prior knowledge and task-specific guidance, and cannot accurately capture the extent to which modern AI systems can autonomously perform this core capability within broader high-impact cyberattack scenarios.
To address these limitations, we construct a new autonomous penetration evaluation framework consisting of two components: target servers and agent scaffolding. Specifically, on the target-server side, we design two levels of target environments based on the number of secure services without known vulnerabilities deployed alongside a vulnerable service: Tier~1 (one secure service) and Tier~2 (three secure services), resulting in a total of 300 target servers. Meanwhile, the agent scaffolding adopts a general-purpose agent architecture equipped with a set of general-purpose cybersecurity tools, without any target-specific prior knowledge. We evaluate 19 open-weight and proprietary LLMs, and find that current models achieve penetration success rates ranging from 10.7% to 69.3%. Moreover, we observe that autonomous penetration capability continues to improve alongside advances in overall model capability.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
