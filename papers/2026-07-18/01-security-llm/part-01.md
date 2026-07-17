# 🔐 大模型安全相关研究 | 2026年07月18日

> 本类共 **7** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Disclosure Divergence: Measuring Privacy Policy and Data Safety Misalignment at Scale](https://arxiv.org/abs/2607.14442)

**<font color=#1a73e8>作者：</font>** Mst Eshita Khatun, Lamine Noureddine, Sideeq Bello 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the rapid growth of mobile applications, user data privacy has become an increasing concern. While privacy policies describe how apps collect and share data, platforms such as Google Play provide Data Safety labels intended to summarize these practices. Because these disclosure channels are declared separately, they may present inconsistent representations of app data practices, creating uncertainty for users and regulators. In this work, we conducted a large-scale empirical study of disclosure consistency across 6,051 Android apps. Using an LLM-based extraction framework and a unified schema over 14 Google Play data categories and two operations (collection and sharing), we measure per-app and per-category consistency and introduce a sensitivity-weighted risk score that emphasizes high-risk data types. We find that misalignment disproportionately affects sensitive categories such as personal information and device identifiers, with sharing disclosures exhibiting lower consistency than collection disclosures. Elevated privac risk is concentrated in app categories associated with persistent monitoring and communication. Overall, our findings highlight structural gaps in current disclosure mechanisms and underscore the need for stronger verification and greater transparency in platform-level privacy reporting.

---


### 2. [Context Contamination in LLM Analysis of Network Security Logs: Poison with Passive Prompt Injection and Mitigation Evaluation](https://arxiv.org/abs/2607.14493)

**<font color=#1a73e8>作者：</font>** Rabimba Karanjai, Yang Lu, Hemanth Hegadehalli Madhavarao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models are increasingly deployed in Security Operations Centers for log analysis tasks including summarization, alert triage, and threat investigation. These systems ingest logs from external-facing services and process network logs as natural language contexts to generate security insights. We demonstrate that this architectural pattern introduces a critical vulnerability: adversaries can embed prompt injection payloads in log-generating fields that persist in storage and are executed when analysts query the LLM, achieving what we term passive prompt injection. We present LogInject, a systematic framework for evaluating these threats. Using LogInject-1.0, a benchmark of 12,847 log entries including 2,569 adversarial samples, we evaluate three production LLMs across four attack objectives: activity concealment, false positive generation, information exfiltration, and output hijacking. Our findings reveal an up to 88.2% attack success rate (83.4% average across models) under the baseline conditions. We introduce Context Stitching, a novel technique that fragments payloads across multiple log entries to evade stateless filters while exploiting LLM long-context reasoning, achieving a 76.4% success rate. As mitigation, we evaluate layered defenses by combining input filtering, prompt hardening, and output validation, demonstrating a 90.4% attack reduction, although 8.4% residual vulnerability persists. Our results establish that LLM-based log analysis creates an inherent confused deputy vulnerability where untrusted data and trusted instructions compete indistinguishably for model attention, requiring defense in-depth architectures and continued human oversight for security-critical decisions.

---


### 3. [Fully Automated End-to-End Adversary Emulation from MITRE ATT\&CK Based Cyber Threat Intelligence Using LLMs](https://arxiv.org/abs/2607.14566)

**<font color=#1a73e8>作者：</font>** Jueon Choi, Seojun Lee, Sanggwon Yun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents a fully automated end-to-end framework for adversary emulation from MITRE ATT&CK-aligned CTI reports using LLMs. Unlike prior work, which either executes prewritten playbooks or partially automates playbook generation, our framework unifies playbook generation, execution, and failure recovery in a single workflow. In particular, although AURORA, the most recent prior study, generates playbooks from CTI reports, it still requires partial manual intervention and does not revise playbooks based on execution failures. Our framework generates Caldera playbooks from CTI reports, executes them automatically, and revises failed Abilities through a failure-type-aware recovery mechanism. Evaluated on 11 CTI reports with Claude Sonnet 4.5, GPT-4o, Gemini 2.5 Pro, and Grok 4 Fast, the framework achieved its best results with Claude Sonnet 4.5: 27.3 Abilities per playbook, 84.22% execution success after revision, and CTI Precision, Recall, and F1 of 73.95%, 52.48%, and 60.50%, respectively. The failure recovery mechanism consistently improved execution success across all evaluated LLM models by 14.59%p to 17.23%p. On the 10 CTI reports selected from AURORA's dataset, this mechanism further increased the final execution success rate, surpassing that of AURORA, which represents the state-of-the-art adversary emulation system.

---


### 4. [Bad Memory: Evaluating Prompt Injection Risks from Memory in Agentic Systems](https://arxiv.org/abs/2607.14611)

**<font color=#1a73e8>作者：</font>** Soham Gadgil, David Alexander, Sai Sunku 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A growing class of agentic systems maintain persistent state across sessions through memory files, behavioral preferences, and knowledge bases. While this makes agents more useful and self-improving, it also creates a new attack surface for prompt injections in which malicious instructions can be embedded within persistent files and influence future behavior. In this work, we study prompt injection attacks in memory-based agentic systems using a sandboxed synthetic workspace. We evaluate two agentic systems, Anthropic Claude Code and OpenAI Codex, across four models: Claude Haiku 4.5, Claude Opus 4.7, GPT-5.2, and GPT-5.5. Our results show that although it is difficult to make an agent overwrite its own memory files using untrusted external content, payloads already planted in those files can successfully attack current and future sessions. Attack success and payload persistence vary substantially across systems, models, adversarial goals, and multi-session attack sequences. These findings show that persistent memory changes the threat model for prompt injection and motivate defenses that protect memory updates without removing useful agent adaptation.

---


### 5. [MemPoison: Uncovering Persistent Memory Threats and Structural Blind Spots in LLM Agents](https://arxiv.org/abs/2607.14651)

**<font color=#1a73e8>作者：</font>** Jifeng Gao, Kang Xia, Yi Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Persistent external memory enhances agent continuity but introduces persistent security vulnerabilities: adversarial content can be injected via standard interaction channels, retained across turns, and later distort downstream behavior. To address this challenge, we propose MemPoison, a comprehensive benchmark and analysis framework featuring 1227 hand-validated cases across four attack types, three injection channels, and three representative memory substrates, evaluated on seven open-weight and three closed-weight model families. We introduce a three-tier taxonomy: (L1) direct single-record corruption, (L2) compositional multi-record corruption and (L3) context-triggered dormant corruption. Our evaluations reveal a distinct defense frontier: while baseline write-time defenses, such as consistency checks, substantially suppress direct L1 attacks, they fail to reliably suppress L2 and L3 attacks. Through mechanistic influence decomposition (MID), we demonstrate structural blind spots in write-time defenses, which admit seemingly benign records that later become harmful through joint retrieval composition or trigger-conditioned activation. Our findings advocate for shifting from static filtering to adaptive, context-sensitive memory defense strategies.

---


### 6. [Is External Database Protection Static in Retrieval-Augmented Generation? Rethinking Privacy Preservation under Dynamic Queries](https://arxiv.org/abs/2607.14811)

**<font color=#1a73e8>作者：</font>** Gang Zhang, Mingyu Tian, Xukun Luan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) enhances large language models via external document retrieval, but retrieved contexts may leak sensitive information. Current privacy protection methods typically rely on a document-level static risk assumption, treating all retrieved documents as having the same privacy leakage risk. However, this assumption overlooks a fundamental characteristic of RAG: the privacy risk of a document is highly dependent on the user's query, making privacy leakage inherently query-driven and dynamic. To address this challenge, we propose a Prompt-Aware Dynamic Hierarchical Differential Privacy framework (PA-HDP) for privacy-preserving RAG. PA-HDP first performs a prompt-aware risk hierarchy to dynamically assess privacy risks under different queries. It then applies adaptive sensitive entity replacement and exponential mechanism-based text selection to provide differentiated privacy protection while preserving semantic utility. By protecting only the content that is truly sensitive under a given query, PA-HDP minimizes unnecessary modifications to the retrieval corpus. Extensive experiments on benchmark datasets demonstrate that PA-HDP significantly reduces privacy leakage while maintaining high retrieval quality, achieving a better privacy-utility trade-off than prior methods.

---


### 7. [DataShield: Uncovering Risky Fine-Tuning Data Across LLMs Through Consensus Subspace Alignment](https://arxiv.org/abs/2607.15081)

**<font color=#1a73e8>作者：</font>** Zefeng Wu, Weiwei Qi, Jielong Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fine-tuning large language models (LLMs) on domain-specific datasets has become a standard paradigm for adapting LLMs to specialized applications. However, recent work has shown that even fine-tuning on benign task-specific data can substantially weaken the safety capabilities of LLMs. While existing efforts have made progress in identifying data responsible for safety degradation, they usually rely on a single mean vector computed over a specific model with its tokenizer to represent the safety direction, which limits both the effectiveness and transferability of their risk assessment measures. To address these limitations, we propose DataShield, a data assessment framework that identifies risky fine-tuning samples and response segments through consensus subspace alignment over joint safety-critical semantic spaces derived from multiple safety-aligned LLMs. Within these spaces, DataShield extracts consensus safe and unsafe subspaces using semantic spectral decomposition over safe and unsafe data representations. The risk of a data sample or segment is then estimated by measuring its relative alignment with the unsafe and safe subspaces, enabling both sample-level filtering and fine-grained segment-level masking. Compared with state-of-the-art filtering and masking baselines, DataShield reduces ASR by 14.6\% with sample filtering and 32.3\% with segment masking, while preserving downstream utility and avoiding target-model-specific risk computation.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
