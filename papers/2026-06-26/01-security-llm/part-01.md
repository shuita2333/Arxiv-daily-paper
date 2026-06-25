# 🔐 大模型安全相关研究 | 2026年06月26日

> 本类共 **7** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Decoupling Reconnaissance and Exploitation: Measuring the Capability Boundaries of LLM-Based Web Penetration Testing](https://arxiv.org/abs/2606.25332)

**<font color=#1a73e8>作者：</font>** Liwei Yu, Shuo Li, Ming Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown promise for automated penetration testing, yet existing end-to-end black-box evaluations are highly susceptible to error cascading: failures in early reconnaissance can mask an agent's actual ability to exploit vulnerabilities. To more accurately characterize these capabilities, we propose a two-stage decoupled evaluation framework that separates exploit execution from reconnaissance. Using ground-truth injection and knowledge-driven ablation across 70 high-fidelity web vulnerability testbeds, our framework isolates exploitation performance from reconnaissance noise. We empirically evaluate five open-source penetration-testing agents, covering multiagent, monolithic, and graph-driven architectures, on a strictly aligned subset of 50 representative vulnerabilities. The results reveal a substantial capability gap. With accurate vulnerability context, agents achieve a functional success rate of up to 90.0%, whereas autonomous reconnaissance, measured by targeted vulnerability recall, plateaus at approximately 50.0%, primarily due to failures in parsing unstructured telemetry. Cross-architectural analysis further reveals distinct capability niches: multi-agent isolation is more effective for long-sequence interactions such as de-serialization, while monolithic and graph-driven designs perform better on short-chain injections and cross-session access-control vulnerabilities, respectively. This decoupled evaluation work provides a fine-grained benchmarking protocol and an empirical basis for designing next-generation automated offensive security agents.

---


### 2. [Representation Matters: An Empirical Study of Program Representations for LLM Vulnerability Reasoning](https://arxiv.org/abs/2606.25356)

**<font color=#1a73e8>作者：</font>** Andrew Stoltman, Johnathan Tang, Haipeng Cai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used for automated vulnerability detection, but it remains unclear how program structure and semantics should be represented for LLM-based reasoning. Most prompting-based approaches provide raw source code, implicitly assuming that more source-level context gives the model better evidence. This paper challenges that assumption through RepBench, an empirical benchmark comparing raw source code with static-analysis-based program representations. RepBench converts real-world C/C++ vulnerability testcases into multiple representations: raw source, Abstract Syntax Trees (ASTs), Control-Flow Graphs (CFGs), Program Dependence Graphs (PDGs), their combinations, and an auxiliary track of enriched PDGs (ePDGs). Using a curated PrimeVul-derived corpus of 107 Joern-based testcases across five CWE categories, we evaluate ten representation variants under a fixed Chain-of-Thought and structured-output protocol, plus 19 additional ePDG cases generated through VulChecker/Hector. Representation choice substantially affects LLM vulnerability reasoning. The strongest variant, AST+PDG, achieves 83.2% accuracy, compared with 53.5% for raw source. At the family level, graph-only prompts outperform both source-only and source-plus-graph prompts while requiring far less prompt overhead. These results reveal a context dilution effect: adding raw source code to compact structural graph evidence can degrade reasoning by making vulnerability-relevant evidence less salient. Overall, our findings show that carefully selected structural representations offer a better accuracy-overhead tradeoff than simply giving LLMs more raw input, and suggest that static analysis can serve as an effective prompt-construction layer for security-focused LLM reasoning.

---


### 3. [Security and Privacy in Retrieval-Augmented Generation: Architectures, Threats, Defenses, and Future Directions for Building Trustworthy Systems](https://arxiv.org/abs/2606.25533)

**<font color=#1a73e8>作者：</font>** Balamurugan Palanisamy, G S S Chalapathi, Vikas Hassija 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has emerged as a dominant paradigm for enhancing large language models with external knowledge. By coupling retrieval mechanisms with generative models, RAG systems improve factual grounding and adaptability across domains. However, integrating retrieval pipelines introduces new security and privacy risks that extend beyond conventional language modeling threats. Sensitive information may be exposed through retrieval indices, query logs, context construction, or federated updates, while adversarial manipulation of knowledge bases can undermine trust in generated outputs. This survey provides a comprehensive examination of privacy and security challenges across RAG systems deployed in centralized, on-device (Micro-RAG), federated, and hybrid paradigms. We present a unified taxonomy of threat surfaces spanning the retrieval, context construction, and generation stages and systematically analyze attack classes, including membership inference, index inference, poisoning, gradient leakage, and collusion. We further review architectural, algorithmic, and cryptographic defenses, highlighting privacy-utility trade-offs and deployment considerations. Finally, we outline open research challenges toward building trustworthy, secure, and resilient RAG systems for real-world applications.

---


### 4. [CrypFormBench: Benchmarking Formal Analysis Capability of Large Language Models for Cryptographic Schemes](https://arxiv.org/abs/2606.25561)

**<font color=#1a73e8>作者：</font>** Zhaoxuan Li, Qionglu Zhang, Hengyuan Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Manual formal analysis of cryptographic schemes is labor-intensive and requires substantial expertise. While model-checking tools (e.g., Scyther and Tamarin) and computational-security tools (e.g., CryptoVerif and EasyCrypt) improve the automation of security proofs, they still rely on experts to abstract schemes and write tool-specific formal descriptions. Large language models (LLMs) are a promising alternative, but their effectiveness in this domain remains unexplored due to the absence of standardized evaluation methodologies. To fill this gap, we introduce CrypFormBench (C.F.B for short), a comprehensive benchmark jointly covering symbolic and computational security to evaluate five core LLM capabilities: interpretation, generation, completion, transformation, and correction. It comprises 700 instances spanning 677 schemes, 7 mainstream formal verifier languages, and 160 security properties. The evaluation of 9 state-of-the-art LLMs reveals that most of them perform well on interpretation and completion, given their code-awareness advantages, but struggle with generation, transformation, and correction. Overall, their performance remains limited, with Claude-3.5 achieving the highest score at 48.7 out of 100. We further provide practical guidance, e.g., few-shot prompting, Pass@K sampling, and lightweight fine-tuning, to mitigate the executability bottleneck and improve tool-usable outputs. Taken together, our benchmark and analyses offer a grounded view of current progress and concrete directions toward reliable LLM-assisted formal cryptographic analysis.

---


### 5. [An Approach for a Supporting Multi-LLM System for Automated Certification Based on the German IT-Grundschutz](https://arxiv.org/abs/2606.25608)

**<font color=#1a73e8>作者：</font>** Lea Roxanne Muth, Marian Margraf  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents a novel approach to perform semi-automated BSI IT-Grundschutz certification using a MultiLarge Language Model system (MLS) with Hybrid RetrievalAugmented Generation (HybridRAG). Facing the challenges of the Network and Information Security Directive 2 (NIS2) directive, a shortage of specialists, and high implementation costs, our MLS architecture aims to increase efficiency, reduce costs, and support certifiers in maintaining the quality of security concepts while meeting the increased demand for certifications of newly affected companies. The system combines Large Language Models (LLMs) and Knowledge Graphs (KGs) to support different phases of the certification process, including protection needs assessment, modeling, IT-Grundschutz check, measure consolidation, and subsequent realization. Our architecture addresses the growing demand for security concepts and offers an approach to handle the digital security challenges introduced by NIS2.

---


### 6. [RAS: Measuring LLM Safety Through Refusal Alignment](https://arxiv.org/abs/2606.25750)

**<font color=#1a73e8>作者：</font>** Chang-Chieh Huang, Yan-Lun Chen, Chia-Mu Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety evaluation of large language models (LLMs) is commonly performed by querying models with unsafe or jailbreak prompts and judging whether their outputs violate a safety policy. Although useful, output-level evaluation is expensive, sensitive to judge choice, and easily tied to fixed question banks. We propose **SafeVec**, a white-box evaluation procedure that measures safety from internal representations rather than generated answers. **SafeVec** first extracts layer-wise refusal directions from a safety-aligned reference model, then selects stable layer windows where safe and unsafe behaviors are separable, and finally scores a target model by measuring whether its hidden states align with these refusal directions under unsafe and jailbreak prompts. The resulting metric, **RAS** (**R**efusal **A**lignment **S**core), maps representation-level refusal alignment to a calibrated 0-100 safety score. Across `Llama`, `Gemma`, and `Qwen` model families, RAS separates aligned models from uncensored and abliterated variants, tracks output-level attack success rate, and is substantially faster than judge-based evaluation. These results suggest that refusal alignment provides a compact and efficient signal for white-box LLM safety evaluation.

---


### 7. [Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries](https://arxiv.org/abs/2606.26021)

**<font color=#1a73e8>作者：</font>** Tânia Carvalho, Maxime Cordy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models are commonly assumed to present limited privacy concerns as they are often pre-trained on large collections of synthetic data. However, these models leverage in-context learning, where sensitive records may be provided directly at inference time as labelled context examples. In this paper, we demonstrate that predictions generated via the attention mechanism leak sufficient information to enable effective Membership Inference Attacks (MIAs). To highlight this vulnerability, we propose AMIA (Attention-based Membership Inference Attack), a shadow-model-free attack that exploits the concentration of transformer attention patterns. Our results show that attention mechanisms reveal strong membership signals, which exceed classical confidence-based attacks, achieving an average gain of 7.7\%, specially in low false-positive regimes. To mitigate this risk, we introduce an inference-time defence inspired by $k$-anonymity principles. This approach reduces the uniqueness of context-key representations without introducing random noise or retraining the model. By targeting only high-risk queries identified through AMIA scores, the defence substantially reduces membership leakage of this attack by an average of 50\% and 25\% against confidence-based attacks, while preserving predictive utility with only 3.9\% performance degradation. Beyond showing that context examples are vulnerable, we further demonstrate that fine-tuning introduces an additional source of privacy risk. In particular, samples whose prediction confidence increases after fine-tuning become more susceptible to MIAs, indicating that fine-tuning can amplify memorisation and expose sensitive training information through confidence shifts.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
