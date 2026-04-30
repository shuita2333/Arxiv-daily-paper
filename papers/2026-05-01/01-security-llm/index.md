# 🔐 大模型安全相关研究 | 2026年05月01日

> 本类共 **6** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Large Language Models as Explainable Cyberattack Detectors for Energy Industrial Control Systems](https://arxiv.org/abs/2604.26079)

**<font color=#1a73e8>作者：</font>** Weiyi Kong, Ahmad Mohammad Saber, Amr Youssef 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In modern energy systems, industrial control systems (ICS) and power-system SCADA require intrusion detection that is not only accurate but also auditable by operators. The ICS intrusion-detection landscape is currently dominated by established supervised detectors. In this paper, we study whether an off-the-shelf large language model (LLM) can serve as a complementary, human-in-the-loop layer for Modbus traffic. We cast this as a binary network-side normal/critical decision task on two public ICS Modbus datasets, collapsing attack periods and other safety-critical behaviors into a single critical class. Each Modbus communication instance is converted into a compact token string derived from discretized protocol fields, and a prompt-configured LLM produces a normal/critical alert together with a concise, token-grounded incident record for analyst review. Under matched event information and shared evaluation splits, the resulting LLM-based triage pipeline achieves high predictive performance on both benchmarks and is broadly comparable to strong supervised baselines, while requiring no task-specific weight updates. To assess the audit record, we apply intervention-based diagnostics, including sufficiency- and necessity-style tests, which provide evidence that the cited tokens are often decision-relevant to the model's own prediction. These records are intended as audit signals rather than full human-grounded explanations.

---


### 2. [OpenSOC-AI: Democratizing Security Operations with Parameter Efficient LLM Log Analysis](https://arxiv.org/abs/2604.26217)

**<font color=#1a73e8>作者：</font>** Chaitanya Vilas Garware, Sharif Noor Zisad  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Small and medium sized businesses (SMBs) face an escalating cybersecurity threat landscape, yet most lack the resources to staff full Security Operations Centers (SOCs) or deploy enterprise grade detection platforms. This paper presents OpenSOC-AI, a lightweight log analysis framework that uses parameter efficient fine tuning of a 1.1-billion parameter language model (TinyLlama-1.1B) to perform automated threat classification, MITRE ATT&CK technique mapping, and severity assessment on raw security log entries. Using Low-Rank Adaptation (LoRA) with only 12.6 million trainable parameters (roughly 1.13% of the base model), we fine tuned on 450 domain specific SOC examples in under five minutes on a single NVIDIA T4 GPU. Testing on a heldout set of 50 examples showed a 68% point gain in threat classification accuracy (from 0% to 68%), a 30% point gain in severity accuracy (from 28% to 58%), and an F1 score of 0.68 compared to the untuned baseline. Full codebase, adapter weights, and datasets are publicly released to support reproducibility and community extension.

---


### 3. [VulStyle: A Multi-Modal Pre-Training for Code Stylometry-Augmented Vulnerability Detection](https://arxiv.org/abs/2604.26313)

**<font color=#1a73e8>作者：</font>** Chidera Biringa, Ajmal Abbas, Vishnu Selvaraj 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present VulStyle, a multi-modal software vulnerability detection model that jointly encodes function-level source code, non-terminal Abstract Syntax Tree (AST) structure, and code stylometry (CStyle) features. Prior work in code representation primarily leverages token-level models or full AST trees, often missing stylistic cues indicative of risky programming practices, or incurring high structural overhead. Our approach selects only non-terminal AST nodes, reducing input complexity while preserving semantic hierarchy, and integrates syntactic and lexical CStyle features as auxiliary vulnerability signals.
VulStyle is pre-trained using masked language modeling on 4.9M functions across seven programming languages, and fine-tuned across five benchmark datasets: Devign, BigVul, DiverseVul, REVEAL, and VulDeePecker. VulStyle achieves state-of-the-art performance on BigVul and VulDeePecker, improving F1 by 4-48% over strong transformer baselines, and attains competitive or best-average performance across all benchmarks. We contribute an ablation study isolating the effect of CStyle and AST structure, error case analysis, and a threat model situating the detection task in attacker-realistic scenarios.

---


### 4. [SecMate: Multi-Agent Adaptive Cybersecurity Troubleshooting with Tri-Context Personalization](https://arxiv.org/abs/2604.26394)

**<font color=#1a73e8>作者：</font>** Yair Meidan, Omri Haller, Yulia Moshan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models and agentic frameworks have enabled virtual customer assistants (VCAs) for complex support. We present SecMate, a multi-agent VCA for cybersecurity troubleshooting that integrates device, user, and service specificity from conversational and device-level signals. Device specificity is provided by a lightweight local diagnostic utility, while user specificity relies on implicit proficiency inference and profile-aware troubleshooting. Service specificity is achieved through a proactive, context-aware recommender. We evaluate SecMate in a controlled study with 144 participants and 711 conversations. Device-level evidence increased correct resolutions from about 50% to over 90% relative to an LLM-only baseline, while step-by-step guidance improved pleasantness and reduced user burden. The recommender achieved high relevance (MRR@1=0.75), and participants showed strong willingness to substitute human IT support at costs well below human benchmarks. We release the full code base and a richly annotated dataset to support reproducible research on adaptive VCAs.

---


### 5. [Tatemae: Detecting Alignment Faking via Tool Selection in LLMs](https://arxiv.org/abs/2604.26511)

**<font color=#1a73e8>作者：</font>** Matteo Leonesi, Francesco Belardinelli, Flavio Corradini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Alignment faking (AF) occurs when an LLM strategically complies with training objectives to avoid value modification, reverting to prior preferences once monitoring is lifted. Current detection methods focus on conversational settings and rely primarily on Chain-of-Thought (CoT) analysis, which provides a reliable signal when strategic reasoning surfaces, but cannot distinguish deception from capability failures if traces are absent or unfaithful. We formalize AF as a composite behavioural event and detect it through observable tool selection, where the LLM selects the safe tool when unmonitored, but switches to the unsafe tool under monitoring that rewards helpfulness over safety, while its reasoning still acknowledges the safe choice. We release a dataset of 108 enterprise IT scenarios spanning Security, Privacy, and Integrity domains under Corruption and Sabotage pressures. Evaluating six frontier LLMs across five independent runs, we find mean AF detection rates between 3.5% and 23.7%, with vulnerability profiles varying by domain and pressure type. These results suggest that susceptibility reflects training methodology rather than capability alone.

---


### 6. [PRAG End-to-End Privacy-Preserving Retrieval-Augmented Generation](https://arxiv.org/abs/2604.26525)

**<font color=#1a73e8>作者：</font>** Zhijun Li, Minghui Xu, Huayi Qi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) is essential for enhancing Large Language Models (LLMs) with external knowledge, but its reliance on cloud environments exposes sensitive data to privacy risks. Existing privacy-preserving solutions often sacrifice retrieval quality due to noise injection or only provide partial encryption. We propose PRAG, an end-to-end privacy-preserving RAG system that achieves end-to-end confidentiality for both documents and queries without sacrificing the scalability of cloud-hosted RAG. PRAG features a dual-mode architecture: a non-interactive PRAG-I utilizes homomorphic-friendly approximations for low-latency retrieval, while an interactive PRAG-II leverages client assistance to match the accuracy of non-private RAG. To ensure robust semantic ordering, we introduce Operation-Error Estimation (OEE), a mechanism that stabilizes ranking against homomorphic noise. Experiments on large-scale datasets demonstrate that PRAG achieves competitive recall (72.45%-74.45%), practical retrieval latency, and strong resilience against graph reconstruction attacks while maintaining end-to-end confidentiality. This work confirms the feasibility of secure, high-performance RAG at scale.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
