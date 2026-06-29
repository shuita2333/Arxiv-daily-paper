# 🔐 大模型安全相关研究 | 2026年06月30日

> 本类共 **6** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [When the Aggregator Cheats: Data-Free Backdoors in Federated LLM-based QA Systems](https://arxiv.org/abs/2606.27511)

**<font color=#1a73e8>作者：</font>** Chenqing Zhu, Yanbo Dai, Yulong Tian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM)-based question-answering (QA) systems are increasingly deployed in sensitive domains such as healthcare, mental health counseling, and legal consultation. Federated learning (FL) enables collaborative training without sharing raw client data, for which locally trained models are aggregated at a central server (i.e., a cloud service provider) to obtain a global model. In this paper, we explore the potential vulnerability where a malicious aggregator, who may collude with a third-party vendor, stealthily implants advertisement-type backdoors into federated QA models, without ever accessing client data. The attacker's goals are twofold: (1) preserve clean QA fidelity (i.e., the poisoned model behaves like a clean model on non-triggered queries); and (2) generate highly natural, contextually relevant responses with target advertisements when a trigger appears. Achieving these two goals simultaneously is highly challenging, as naive backdoor injection without knowledge about private data may degrade model's clean performance or fail to inject the target. Motivated by this, we propose to leverage clients' uploaded gradients during training, and develop a two-stage framework for data-free and stealthy poisoning: (1) recover representative training samples from client gradients, and (2) construct poisoning datasets utilizing recovered samples and trigger phrases to inject backdoors into the global model. Experiments across representative QA datasets and LLM families under full fine-tuning and LoRA settings demonstrate that, our method achieves nearly 100% Attack Success Rate (ASR) while incurring negligible degradation on clean tasks. Crucially, reconstructing only 5-20% of gradients suffices to mount a reliable attack, exposing a practical blind spot in the pipeline of federated training of QA LLMs.

---


### 2. [Agentic AI-Powered Re-Identification: An Emerging, Scalable Threat to Mobility Microdata Privacy](https://arxiv.org/abs/2606.27936)

**<font color=#1a73e8>作者：</font>** Oscar Thees, Roman Müller, Matthias Templ  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The widespread collection of fine-grained location data by commercial data brokers creates a re-identification risk that is not widely recognised by the public. While prior research has established that mobility traces are highly unique and that individuals can, in principle, be identified from a handful of spatio-temporal points, such attacks have historically required significant manual effort from skilled analysts, limiting their practical scale.
In this feasibility study, we demonstrate in a real world setting that agentic AI fundamentally changes this threat model. We present an end-to-end pipeline in which large language model agents autonomously search the open web, cross-reference public records and social media, and resolve raw coordinate sequences to candidate identities - without human intervention. We evaluate the pipeline on a spatio-temporal dataset containing simulated location points anchored at and around true home and work addresses, focusing on a high-risk disclosure scenario. Our results demonstrate that, from spatio-temporal data and public sources alone, our agentic AI successfully re-identified 18 of the 25 re-identifiable individuals (72%) and 18 of 43 cases overall (41.9%).
We discuss implications for Statistical Disclosure Control (SDC) practice and outline the near-future escalation that data custodians and regulators must anticipate. De facto anonymity - an implicit foundation of SDC practice - is shifting. Agentic AI strengthens the case that re-identification is reasonably likely by any means under the GDPR Recital-26 standard, at costs of minutes-and-dollars per target.

---


### 3. [SHARD: cell-keyed residual splitting for alignment-resistant private dense retrieval](https://arxiv.org/abs/2606.27976)

**<font color=#1a73e8>作者：</font>** Sergey Kurilenko  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Dense embeddings underpin semantic search and RAG, yet a leaked vector store hands much of the underlying text back to whoever holds it. The attacks that make this possible (few-shot alignment, zero-shot inversion, unsupervised cross-space translation) share one weakness: the protected store is a single global geometry that can be aligned to a known one. A secret global rotation, the usual lightweight defence, is no exception: orthogonal Procrustes recovers it once the attacker has about the subspace dimension in known pairs.
We introduce Shard, a retrieval-preserving embedding transform that removes this weak axis. The centred embedding is split into a short public prefix (for stage-1 retrieval) and a private residual sharded into C cells under separate secret keys; the residual is reranked under CKKS, where the keys cancel and leave the inner product exact. A single parameter C runs the design from the global-linear baseline it replaces (C=1) to per-document micro-keys (C=N). Because the rerank is full-dimensional, Shard returns the raw-space nDCG@10 that half-SVD truncation gives up; and because the residual is keyed cell-locally, mapping it back to a common frame under a diffuse known-plaintext leak costs roughly C times more anchors (median 200 to 102,400 at C=256), for a few encrypted queries. The short public prefix leaks far less neighbour structure, and a micro-key limit drives the residual graph to zero with an unlinkable, renewable template. The barrier holds against learned, non-linear and unsupervised aligners, and where a matched-utility noise defence de-anonymises almost every probe, Shard de-anonymises none. We are plain about the limits: within a cell the keys cancel, a targeted attacker needs only about d_priv anchors, and an overlapping reference corpus still leaks through the prefix. Shard is an attack-aware geometric defence, not a cryptographic guarantee.

---


### 4. [AdvancedShelLM: A Stateful Multi-Agent LLM Honeypot for SSH Deception](https://arxiv.org/abs/2606.27990)

**<font color=#1a73e8>作者：</font>** Muris Sladić, Eman Alibalić, Veronica Valeros 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based SSH honeypots can generate believable interactions, but evaluations indicate they remain somewhat identifiable to determined attackers, indicating the need for a better scaffolding. We present a new LLM-based honeypot design that uses a multi-agent, multi-LLM architecture to address the limitations of the previous shelLM LLM honeypot. Our honeypot, called AdvancedShelLM, uses two LLM agents, a Manager and a Worker, that better understand the commands while reducing incorrect responses and increasing deception. It implements an advanced permanent filesystem, allowing many simultaneous attackers to see the same changing files for the first time. It was evaluated with: (i) unit tests for generative capabilities, (ii) an AI attacker (ARACNE) to assess realism and deception, (iii) human attackers to assess its deceptive capability, and (iv) an Internet deployment to evaluate deception in real-world attacks. In unit test results, AdvancedShelLM achieved a pass rate of up to 99.02%. The AI attacker ARACNE had issues making a decision if the system is honeypot or not, but showed slight bias towards saying honeypot, even for a real Ubuntu shell. With human attackers, AdvancedShelLM deceived more humans than Cowrie, but had similar results as shelLM. The Internet deployment showed concrete evidence that the output of AdvancedShelLM can influence the behaviour of real-life attackers.

---


### 5. [ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents](https://arxiv.org/abs/2606.28061)

**<font color=#1a73e8>作者：</font>** Shijing Hu, Liang Liu, Zhu Meng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have increasingly moved from standalone text generation systems to agents that invoke external tools, access environments, and execute multi-step tasks. However, conventional function-calling benchmarks mainly evaluate task completion and API correctness, while privacy evaluation benchmarks typically focus on final responses or privacy judgments. Neither perspective captures purpose-bound information flow across an executed multi-tool trajectory. Motivated by this limitation in current agent evaluation, ToolPrivacyBench audits whether task-private atoms are routed only to authorized tools and downstream sinks, thereby evaluating both task completion and privacy over-disclosure during tool use. The benchmark contains 2,150 cases, including 1,150 fully synthetic privacy-sensitive business workflows and 1,000 cases adapted from existing multi-tool and function-calling benchmarks. Each case is represented by a policy knowledge base. After an agent executes against mock business backends, the evaluator compares recorded tool arguments and backend audit logs with this policy knowledge base. The evaluation covers nine widely used agents to characterize purpose-bound privacy over-disclosure. The results show that successful tool execution does not imply appropriate privacy disclosure: an agent may complete a task while transmitting unnecessary private information through intermediate tool calls. ToolPrivacyBench therefore formalizes a need-to-know disclosure boundary, under which each tool should receive only the information necessary for its stated purpose, and uses trajectory-level auditing to identify privacy over-disclosure in multi-tool workflows.

---


### 6. [Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models](https://arxiv.org/abs/2606.28153)

**<font color=#1a73e8>作者：</font>** Yanchen Yin, Dongqi Han, Linghui Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Jailbreak attacks bypass LLM safety alignment, yet their mechanisms remain poorly understood. We provide evidence that attacks do not comprehensively eliminate safety features, but instead selectively suppress specific attention heads. We identify two functionally differentiated types: Adversarially Compromised Heads (ACHs) concentrated in early layers, which are suppressed under attacks, and Safety-Aligned Heads (SAHs) in mid-layers, which maintain robust activations even when attacks succeed. Ablation studies support the causal role of ACHs and the contribution of SAHs to robust activations: suppressing a small number of ACHs is sufficient to induce jailbreak-like behavior on normally refused inputs, while removing SAHs substantially weakens mid-layer safety activations. Token-level attribution further shows that ACH suppression is driven specifically by attack-template tokens, providing a mechanistic account of why attacks can bypass refusal decisions through ACH suppression while leaving internal safety signals sustained by SAHs -- a phenomenon we term Robust Harmful Features. To validate the practical significance of this robustness, we show that simply reading these persistent activations -- without any training -- yields competitive aggregate detection performance with strong adversarial robustness.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
