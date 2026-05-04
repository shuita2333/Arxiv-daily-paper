# 🔐 大模型安全相关研究 | 2026年05月05日

> 本类共 **11** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Symbolic Execution Meets Multi-LLM Orchestration: Detecting Memory Vulnerabilities in Incomplete Rust CVE Snippets](https://arxiv.org/abs/2605.00034)

**<font color=#1a73e8>作者：</font>** Zeyad Abdelrazek, Young Lee  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents a system combining symbolic execution (KLEE) with a 4-agent multi-LLM architecture for detecting memory vulnerabilities in Rust unsafe code. A central challenge we address is the incomplete-code problem: CVE database entries provide only isolated code snippets that lack struct definitions, imports, and Cargo manifests, causing all existing formal verification tools to fail at compilation with zero output. Our system resolves this through four specialized agents -- an Oracle/Validator for strategic planning, a Safety Checker for vulnerability analysis, a Code Specialist for FFI wrapper generation, and a Fast Filter for execution optimization -- that collaboratively synthesize KLEE-compatible harnesses from otherwise uncompilable fragments. KLEE's output is then ingested by this http URL, which constructs a Graph Database linking CVE files, CWE categories, error types, and symbolic execution paths as typed nodes and labelled edges, enabling structured cross-CVE vulnerability queries. We evaluated our system on 31 real-world Rust CVEs spanning 11 CWE categories, achieving 90.3% wrapper compilation success where all state-of-the-art formal verification tools achieve 0%. Our system detected 1,206 critical errors across 26 files (83.9% detection rate), compared to 14 warnings across 11 files for Clippy (35.5%) and generic labels for Miri. The 4-agent architecture reduced wrapper compilation failures from 42% (single-agent baseline) to 9.7% and increased detected errors from 487 to 1,206, confirming that role specialization and structured context passing produce measurably better results than a single general-purpose model. Our replication package is publicly available at this https URL

---


### 2. [Compliance-Aware Agentic Payments on Stablecoin Rails](https://arxiv.org/abs/2605.00071)

**<font color=#1a73e8>作者：</font>** Kenneth See, Xue Wen Tan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic payment systems extend delegated action to financial transfers, but scaling them on stablecoin rails in regulated settings requires safeguards that remain effective when humans are not continuously in the loop. We present a compliance-aware architecture that combines x402-style, signature-based payment authorisation and relayed execution with programmable compliance embedded as an on-chain guardrail via a policy wrapper and policy manager coordinating modular checks. By enforcing compliance at the point of execution, rather than as a separate off-chain workflow, the approach preserves low-friction settlement when conditions are satisfied, records transaction-linked on-chain attestations, and supports structured resolution when requirements are pending.

---


### 3. [XekRung Technical Report](https://arxiv.org/abs/2605.00072)

**<font color=#1a73e8>作者：</font>** Jiutian Zeng, Junjie Li, Chengwei Dai 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present XekRung, a frontier large language model for cybersecurity, designed to provide comprehensive security capabilities. To achieve this, we develop diverse data synthesis pipelines tailored to the cybersecurity domain, enabling the scalable construction of high-quality training data and providing a strong foundation for cybersecurity knowledge and understanding. Building on this foundation, we establish a complete training pipeline spanning continued pre-training (CPT), supervised fine-tuning (SFT), and reinforcement learning (RL) to further extend the model's capabilities. We further introduce a multi-dimensional evaluation system to guide the iterative improvement of both domain-specific and general-purpose abilities. Extensive experiments demonstrate that XekRung achieves state-of-the-art performance on cybersecurity-specific benchmarks among models of the same scale, while maintaining strong performance on general benchmarks.

---


### 4. [Alignment Contracts for Agentic Security Systems](https://arxiv.org/abs/2605.00081)

**<font color=#1a73e8>作者：</font>** Isaac David, Marco Guarnieri, Arthur Gervais  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic security systems increasingly combine LLM planners with tools that can discover, validate, and report vulnerabilities. This creates an asymmetric control problem: the system should retain strong offensive capability inside an authorized engagement, while the same capabilities must be denied outside scope. Existing guardrails provide useful policy controls, but they do not make this boundary a first-class formal contract over observable effects.
We introduce alignment contracts, a framework for specifying and enforcing behavioral constraints over observable effect traces. A contract defines scope, allowed and forbidden effects, resource budgets, and disclosure policies. We give the language finite-trace semantics, characterize satisfaction as a safety property with finite violation witnesses, develop refinement and one-way composition rules for modular contract engineering, and show that admissibility checking is decidable. We instantiate the framework for web-focused agentic security workflows and show how the same structure extends to other effect profiles.
Under an explicit Effect Observability Assumption, where all $\SigmaEff$-effects are mediated, the soundness theorem quantifies over the agent model and gives guarantees for mediated $\SigmaEff$-effects, including enforcement soundness for monitor-realized traces. We also state an assumption-lifted adaptation result and formalize limits through undecidability transfer and observability-boundary theorems. A Lean 4 artifact checks the formal core theorems used by the paper.

---


### 5. [Attention Is Where You Attack](https://arxiv.org/abs/2605.00236)

**<font color=#1a73e8>作者：</font>** Aviral Srivastava, Sourav Panda  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety-aligned large language models rely on RLHF and instruction tuning to refuse harmful requests, yet the internal mechanisms implementing safety behavior remain poorly understood. We introduce the Attention Redistribution Attack (ARA), a white-box adversarial attack that identifies safety-critical attention heads and crafts nonsemantic adversarial tokens that redirect attention away from safety-relevant positions. Unlike prior jailbreak methods operating at the semantic or output-logit level, ARA targets the geometry of softmax attention on the probability simplex using Gumbel-softmax optimization over targeted heads. Across LLaMA-3-8B-Instruct, Mistral-7B-Instruct-v0.1, and Gemma-2-9B-it, ARA bypasses safety alignment with as few as 5 tokens and 500 optimization steps, achieving 36% ASR on Mistral-7B and 30% on LLaMA-3 against 200 HarmBench prompts, while Gemma-2 remains at 1%. Our principal mechanistic finding is a dissociation between ablation and redistribution: zeroing out the top-ranked safety heads produces at most 1 flip among 39 to 50 baseline refusals, while ARA targeting the corresponding safety-heavy layers flips 72/200 prompts on Mistral-7B and 60/200 on LLaMA-3. This suggests that safety is not localized in these heads as removable components, but emerges from the attention routing they perform. Removing a head allows compensation through the residual stream, while redirecting its attention propagates a corrupted signal downstream.

---


### 6. [Trident: Improving Malware Detection with LLMs and Behavioral Features](https://arxiv.org/abs/2605.00297)

**<font color=#1a73e8>作者：</font>** Rebecca Saul, Jingzhi Jiang, Elliott Chia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Traditionally, machine learning methods for PE malware detection have relied on static features like byte histograms, string information, and PE header contents. One barrier to incorporating dynamic analysis features has been the semi-structured nature of sandbox behavior reports. We show that, using the latest generation of large language models with reasoning, it is possible to efficiently process these behavior reports and utilize them as part of a malware detection pipeline. Specifically, we leverage LLMs to generate behavior-based malware detection rules based on a small training set of labeled malware. We find that these detection rules, derived from behavioral features, are much more robust to concept drift than standard static-feature methods, while maintaining practical false positive rates. Finally, we introduce Trident, a system which combines a classic decision tree model over static features, our behavior-based detection rules, and direct LLM analysis of sandbox reports through majority voting. Trident outperforms standard methods using static features, outperforms behavior-based rules alone, and is as resilient to concept drift as active learning methods without requiring retraining.

---


### 7. [Skills as Verifiable Artifacts: A Trust Schema and a Biconditional Correctness Criterion for Human-in-the-Loop Agent Runtimes](https://arxiv.org/abs/2605.00424)

**<font color=#1a73e8>作者：</font>** Alfredo Metere  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills -- structured packages of instructions, scripts, and references that augment a large language model (LLM) without modifying the model itself -- have moved from convenience to first-class deployment artifact. The runtime that loads them inherits the same problem package managers and operating systems have always faced: a piece of content claims a behavior; the runtime must decide whether to believe it. We argue this paper's central thesis up front: a skill is \emph{untrusted code} until it is verified, and the runtime that loads it must enforce that default rather than infer trust from a signature, a clearance, or a registry of origin. Without skill verification, a human-in-the-loop (HITL) gate must fire on every irreversible call -- which is operationally untenable and degrades into rubber-stamping at any non-trivial scale. With skill verification treated as a separate, gated process, HITL fires only for what is unverified, and the system becomes sustainable. We give a trust schema (§\ref{sec:schema}) that includes an explicit verification level on every skill manifest; a capability gate (§\ref{sec:gate}) whose HITL policy is a function of that verification level; a \emph{biconditional} correctness criterion (§\ref{sec:biconditional}) that any candidate verification procedure must satisfy on an adversarial-ensemble exercise (§\ref{sec:eval}); and a portable runtime profile (§\ref{sec:guidelines}) with ten normative guidelines abstracted from a working open-source reference implementation \cite{metere2026enclawed}. The contribution is harness- and model-agnostic; nothing here requires retraining, fine-tuning, or proprietary infrastructure.

---


### 8. [CleanBase: Detecting Malicious Documents in RAG Knowledge Databases](https://arxiv.org/abs/2605.00460)

**<font color=#1a73e8>作者：</font>** Weifei Jin, Xilong Wang, Wei Zou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) is vulnerable to prompt injection attacks, in which an adversary inserts malicious documents containing carefully crafted injected prompts into the knowledge database. When a user issues a question targeted by the attack, the RAG system may retrieve these malicious documents, whose injected prompts mislead it into generating attacker-specified answers, thereby compromising the integrity of the RAG system. In this work, we propose CleanBase, a method to detect malicious documents within a knowledge database. Our key insight is that malicious documents crafted for the same attack-targeted questions often exhibit high semantic similarity, as attackers deliberately make them consistent to improve attack success rates. Accordingly, CleanBase constructs a similarity graph over the knowledge database, where each node represents a document and an edge connects two nodes if their semantic similarity--computed using an embedding model--exceeds a statistically determined threshold. Due to their inherent similarity, malicious documents tend to form cliques within this graph. CleanBase detects such cliques and flags the corresponding documents as malicious. We theoretically derive upper bounds on CleanBase's false positive and false negative rates and empirically validate its effectiveness. Experimental results across multiple datasets and prompt injection attacks demonstrate that CleanBase accurately detects malicious documents and effectively safeguards RAG systems. Our source code is available at this https URL.

---


### 9. [STARE: Step-wise Temporal Alignment and Red-teaming Engine for Multi-modal Toxicity Attack](https://arxiv.org/abs/2605.00699)

**<font color=#1a73e8>作者：</font>** Xutao Mao, Liangjie Zhao, Tao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Red-teaming Vision-Language Models is essential for identifying vulnerabilities where adversarial image-text inputs trigger toxic outputs. Existing approaches treat image generation as a black box, returning only terminal toxicity scores and leaving open the question of when and how toxic semantics emerge during multi-step synthesis. We introduce STARE, a hierarchical reinforcement learning framework that treats the denoising trajectory itself as the attack surface, under a direct white-box T2I and query-only black-box VLM setting. By coupling a high-level prompt editor with low-level T2I fine-tuning via Group Relative Policy Optimization (GRPO), STARE attains a 68\% improvement in Attack Success Rate over state-of-the-art black-box and white-box baselines. More importantly, this trajectory-level view surfaces the Optimization-Induced Phase Alignment phenomenon: vanilla models exhibit diffuse toxicity, whereas adversarial optimization concentrates conceptual harms into early semantic phases and detail-oriented harms into late refinement. Targeted perturbations of either window selectively suppress different toxicity categories, indicating that this temporal structure is a genuine causal handle rather than a side effect of the hierarchical design. The phenomenon turns toxicity formation from a chaotic process into a small set of predictable vulnerability windows, providing both a potent attack engine and a basis for phase-aware safety mechanisms. Content warning: This paper contains examples of toxic content that may be offensive or disturbing.

---


### 10. [Self-Adaptive Multi-Agent LLM-Based Security Pattern Selection for IoT Systems](https://arxiv.org/abs/2605.00741)

**<font color=#1a73e8>作者：</font>** Saeid Jamshidi, Foutse Khomh, Carol Fung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The adoption of Internet of Things (IoT) systems at the network edge of smart architectures is increasing rapidly, intensifying the need for security mechanisms that are both adaptive and resource-efficient. In such environments, runtime defence mechanisms are no longer limited to detection alone but become a resource-constrained task of selecting mitigation actions. Security controls must be carefully selected, combined, and executed under latency, energy, and computational constraints, while preventing unsafe interactions between controls. Existing approaches predominantly rely on static rule sets and learned policies, which provide limited guarantees of feasibility, conflict safety, and execution correctness in resource-constrained edge settings. To address this limitation, we introduce ASPO, a self-adaptive multi-agent security pattern selection that integrates Large Language Model (LLM)-based reasoning with deterministic enforcement within a MAPE-K control loop. ASPO explicitly separates stochastic decision generation from execution: LLM agents propose candidate mitigation portfolios, while a deterministic optimisation core enforces closed-world action integrity, conflict-free composition, and resource feasibility at every decision epoch. We deploy ASPO on a distributed edge-gateway testbed and evaluate it across two workloads, each comprising 500 and 1000 runtime security decisions, using replayed IoT attack traffic. In addition, the results demonstrate invariant safety properties, including 100% conflict-free activation, consistent resource feasibility across workloads, and stable pattern dominance with perfect rank preservation. Importantly, deeper decision exploration reduces extreme-case execution costs, compressing tail latency and energy overheads by 21.9% and 23.1%, respectively, without increasing mean energy consumption.

---


### 11. [When RAG Chatbots Expose Their Backend: An Anonymized Case Study of Privacy and Security Risks in Patient-Facing Medical AI](https://arxiv.org/abs/2605.00796)

**<font color=#1a73e8>作者：</font>** Alfredo Madrid-García, Miguel Rujas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Background: Patient-facing medical chatbots based on retrieval-augmented generation (RAG) are increasingly promoted to deliver accessible, grounded health information. AI-assisted development lowers the barrier to building them, but they still demand rigorous security, privacy, and governance controls. Objective: To report an anonymized, non-destructive security assessment of a publicly accessible patient-facing medical RAG chatbot and identify governance lessons for safe deployment of generative AI in health. Methods: We used a two-stage strategy. First, Claude Opus 4.6 supported exploratory prompt-based testing and structured vulnerability hypotheses. Second, candidate findings were manually verified using Chrome Developer Tools, inspecting browser-visible network traffic, payloads, API schemas, configuration objects, and stored interaction data. Results: The LLM-assisted phase identified a critical vulnerability: sensitive system and RAG configuration appeared exposed through client-server communication rather than restricted server-side. Manual verification confirmed that ordinary browser inspection allowed collection of the system prompt, model and embedding configuration, retrieval parameters, backend endpoints, API schema, document and chunk metadata, knowledge-base content, and the 1,000 most recent patient-chatbot conversations. The deployment also contradicted its privacy assurances: full conversation records, including health-related queries, were retrievable without authentication. Conclusions: Serious privacy and security failures in patient-facing RAG chatbots can be identified with standard browser tools, without specialist skills or authentication; independent review should be a prerequisite for deployment. Commercial LLMs accelerated this assessment, including under a false developer persona; assistance available to auditors is equally available to adversaries.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
