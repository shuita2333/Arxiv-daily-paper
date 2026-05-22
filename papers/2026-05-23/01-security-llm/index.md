# 🔐 大模型安全相关研究 | 2026年05月23日

> 本类共 **9** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Autonomous LLM Agents & CTFs: A Second Look](https://arxiv.org/abs/2605.21497)

**<font color=#1a73e8>作者：</font>** Youness Bouchari, Matteo Boffa, Marco Mellia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents are increasingly proposed to automate offensive security tasks, with recent studies reporting near human-level success rates in Capture-the-Flag (CTF) challenges. We here revisit these results, providing a second look at these claims. We engineer different agent architectures of increasing complexity and modularity on 30 web-based CTFs challenges spanning 14 vulnerability classes. We instantiate these agents with multiple LLM backbones, and compare them with claude-code, a general-purpose agent that automatically determines its internal architecture. Our evaluation yields three main findings. First, claude-code achieves performance comparable to the engineered architectures (19/30 solved tasks), suggesting that general-purpose agents are strong baselines for offensive security tasks. Second, both our architectures and claude-code struggle in the same challenge categories, revealing persistent barriers that keep current agents below human-level capability. Third, by leveraging our manually designed architectures we can systematically measure the impact of additional components, finding that structured orchestration of specialized roles outperforms monolithic designs, improving run-to-run consistency, and reducing execution costs.

---


### 2. [Frequency-Domain Regularized Adversarial Alignment for Transferable Attacks against Closed-Source MLLMs](https://arxiv.org/abs/2605.21541)

**<font color=#1a73e8>作者：</font>** Leitao Yuan, Qinghua Mao, Daizong Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) remain vulnerable to transfer-based targeted attacks, where perturbations optimized on open-source surrogate encoders can generalize to closed-source MLLMs. A key challenge for improving adversarial transferability is to effectively capture the intrinsic visual focus shared across different models, such that perturbations align with transferable semantic cues rather than surrogate-specific behaviors. However, existing methods suffer from spatial-domain feature redundancy and surrogate-specific gradient signals, thereby hindering cross-model transferability. In this paper, we propose FRA-Attack, which addresses both challenges from a unified frequency-domain regularization perspective. For feature alignment, a high-pass DCT objective on patch features suppresses redundant global structures and concentrates the loss on the high-frequency band that carries the MLLMs' intrinsic visual focus. For gradient optimization, we introduce Frequency-domain Gradient Regularization (FGR), a \textit{model-agnostic} low-pass regularizer that modulates the surrogate gradient using only the geometric frequency coordinate, \textit{i.e.}, no surrogate-derived statistic is involved, so that FGR is model-agnostic by construction, removing surrogate-specific high-frequency artifacts while preserving transferable low-frequency directions. Together, the two components form a unified frequency-domain treatment of transferability. Extensive experiments on $15$ flagship MLLMs across $7$ vendors show that FRA-Attack achieves superior cross-model transferability, particularly with state-of-the-art performance on GPT-5.4, Claude-Opus-4.6 and Gemini-3-flash.

---


### 3. [ASSEMBLAGE-DEEPHISTORY: A Cross-Build Binary Dataset with Temporal Coverage](https://arxiv.org/abs/2605.21615)

**<font color=#1a73e8>作者：</font>** Chang Liu, Noah Fleischmann, Nicolò Altamura 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing binary corpora typically capture only one or two axes of binary variation: they either provide cross-compiler builds without a temporal axis, or CVE labels for single-build binaries. None combine cross-build diversity, cross-version history, and CVE labels into a queryable structure. We present ASSEMBLAGE-DEEPHISTORY, which consolidates these dimensions into a unified framework where every binary's compilation context, source code, vulnerable functions, and package version are stored as first-class metadata.
ASSEMBLAGE-DEEPHISTORY comprises 73,610 binaries spanning 248 open-source projects, compiled across GCC, Clang, and MSVC at multiple optimization levels on Linux and Windows, with multi-year historical builds. Each binary is indexed in a database that links it to its source code, functions, debug info, variant builds, historical versions, and vulnerable functions. Three analyses demonstrate this structure's value: (1) a three-stage LLM benchmark (recognition, strategy-guided detection, and cross-build transfer) to test whether LLMs reason about binary vulnerabilities or pattern-match on build-specific artifacts; (2) a comparison of MalConv embeddings, jTrans function embeddings, and TLSH fuzzy hashes quantifying how same-package versions cluster in each space; and (3) a Bayesian regression decomposing binary similarity into contributions from temporal distance, file changes, and commits.

---


### 4. [Adversarial Reframing: A Framework for Targeted Generation in Language Models](https://arxiv.org/abs/2605.21674)

**<font color=#1a73e8>作者：</font>** Shahnewaz Karim Sakib, Swati Kar, Anindya Bijoy Das  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are widely deployed in diverse real-world settings, yet remain vulnerable to jailbreaking, where prompt-based attacks bypass safety filters. We present THREAT (Targeted Harmful generation via Reframing and Exploitation of Adversarial Tactics), a reasoning-driven framework that coordinates multiple LLMs in an iterative search loop to find textual jailbreak prompts. We formulate prompt discovery as a nonconvex optimization problem and provide an efficient solution that lowers runtime and improves attack effectiveness. Across diverse datasets and model architectures, THREAT delivers higher attack success rates with lower computational cost than prior methods. The crafted prompts were flagged as harmful in fewer than 1% of cases, compared with about 50% refusals for the corresponding unmodified prompts. These findings reveal previously undetected vulnerabilities in aligned LLMs and position THREAT as a practical tool for proactively strengthening the safety of foundation models.

---


### 5. [HIDBench: Benchmarking Large Language Models for Host-Based Intrusion Detection](https://arxiv.org/abs/2605.21773)

**<font color=#1a73e8>作者：</font>** Danyu Sun, Jinghuai Zhang, Yuan Tian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent benchmark efforts have advanced the evaluation of large language models (LLMs) in cybersecurity, including tasks such as penetration testing and vulnerability identification. However, a critical cybersecurity task, namely intrusion detection from system logs, remains unexplored. In this work, we present a new benchmark to assess LLMs' capabilities in supporting host-based intrusion detection systems (HIDS). This task requires fine-grained reasoning over large-scale, noisy, and highly imbalanced system logs, where complex interactions between benign and malicious activities make reliable detection challenging. Our benchmark unifies three public system log datasets, DARPA-E3, DARPA-E5, and NodLink, and introduces a data construction pipeline that transforms raw host telemetry into LLM-compatible inputs, enabling systematic evaluation under realistic intrusion detection settings. Our evaluation of frontier LLMs reveals substantial performance gaps across datasets. While many models achieve high precision (often above 0.8) on simpler datasets, their performance degrades significantly as system logs become noisier and more complex, with MCC frequently dropping below 0.5 and false positive rates increasing sharply. We further analyze model behavior and identify distinct regimes, including conservative detectors with low false positive rates and over-sensitive models that generate excessive alerts. Overall, our results highlight that while LLMs show strong potential for HIDS, their effectiveness is highly sensitive to data complexity, and robust system design is essential for reliable deployment.

---


### 6. [FuzzingBrain V2: A Multi-Agent LLM System for Automated Vulnerability Discovery and Reproduction](https://arxiv.org/abs/2605.21779)

**<font color=#1a73e8>作者：</font>** Ze Sheng, Zhicheng Chen, Qingxiao Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software vulnerabilities pose critical security threats, with nearly 50,000 CVEs reported in 2025. While Large Language Models (LLMs) show promise for automated vulnerability detection, three key challenges remain. First, LLM-generated vulnerability reports suffer from high false positive rates and lack
reproducible verification. Second, existing LLM-based approaches use suboptimal granularities for vulnerability localization: function-level analysis overlooks bugs when context becomes extensive, while line-level analysis lacks sufficient context. Third, existing approaches have difficulty reasoning about
vulnerabilities with complex cross-function dependencies and triggering conditions.
We present FuzzingBrain V2, a multi-agent system that addresses these gaps through four key contributions: (1) fully automated vulnerability analysis built on Google's OSS-Fuzz, ensuring all reported vulnerabilities are fuzzer-reproducible; (2) Suspicious Point, a novel control-flow-based abstraction for precise
vulnerability localization at the optimal granularity; (3) logic-driven hierarchical function analysis with dual-layer fuzzing enhancing function coverage under resource constraints; (4) MCP-based static and dynamic analysis tools with context engineering enhancing complex vulnerability reasoning.
On the AIxCC 2025 Final Competition C/C++ dataset, FuzzingBrain V2 achieved 90% detection rate (36 of 40 vulnerabilities). In real-world deployment, FuzzingBrain V2 discovered 29 zero-day vulnerabilities across 12 open-source projects, all confirmed and fixed by maintainers, with 2 assigned CVE IDs.

---


### 7. [A Large Language Model Approach to Generating Bypass Rules for Malware Evasion in Analysis Sandbox](https://arxiv.org/abs/2605.21821)

**<font color=#1a73e8>作者：</font>** Zhiyong Sui, Lamine Noureddine, Mst Eshita Khatun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sandbox evasion remains a critical challenge for automated malware analysis, as modern malware employs environment checks to detect analysis platforms and suppress malicious behavior. Existing approaches rely on manually crafted bypass rules that require deep reverse engineering of each evasion mechanism -an approach that cannot scale against rapidly evolving evasion techniques. In this paper, we leverage large language models (LLMs) to automatically generate YARA rules that bypass evasion checks in sandbox environments. We propose ABLE, which analyzes execution traces from malware terminated due to potentially evasive behavior and employs multiple reasoning strategies to generate targeted bypass rules. To address syntactic errors and improve the efficacy of the bypass rules in the LLM outputs, we introduce an auto-sanitization pipeline and feedback-driven iterative refinement. We evaluate ABLE on 334 real-world malware samples across four open-weight LLMs. ABLE achieves a 79% bypass success rate, with iterative refinement contributing 29.5% of successful cases. Compared to existing analysis platforms, ABLE identifies 47% more malware family classifications and exposes previously hidden behaviors.

---


### 8. [Blind Spots in the Guard: How Domain-Camouflaged Injection Attacks Evade Detection in Multi-Agent LLM Systems](https://arxiv.org/abs/2605.22001)

**<font color=#1a73e8>作者：</font>** Aaditya Pai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Injection detectors deployed to protect LLM agents are calibrated on static, template-based payloads that announce themselves as override directives. We identify a systematic blind spot: when payloads are generated to mimic the domain vocabulary and authority structures of the target document, what we call domain camouflaged injection, standard detectors fail to flag them, with detection rates dropping from 93.8% to 9.7% on Llama 3.1 8B and from 100% to 55.6% on Gemini 2.0 Flash. We formalize this as the Camouflage Detection Gap (CDG), the difference in injection detection rate between static and camouflaged payloads. Across 45 tasks spanning three domains and two model families, CDG is large and statistically significant (chi^2 = 38.03, p < 0.001 for Llama; chi^2 = 17.05, p < 0.001 for Gemini), with zero reverse discordant pairs in either case. We additionally evaluate Llama Guard 3, a production safety classifier, which detects zero camouflage payloads (IDRcamouflage = 0.000), confirming that the blind spot extends beyond few-shot detectors to dedicated safety classifiers. We further show that multi-agent debate architectures amplify static injection attacks by up to 9.9x on smaller models, while stronger models show collective resistance. Targeted detector augmentation provides only partial remediation (10.2% improvement on Llama, 78.7% on Gemini), suggesting the vulnerability is architectural rather than incidental for weaker models. Our framework, task bank, and payload generator are released publicly.

---


### 9. [RADAR: Defending RAG Dynamically against Retrieval Corruption](https://arxiv.org/abs/2605.22041)

**<font color=#1a73e8>作者：</font>** Ziyuan Chen, Yueming Lyu, Yi Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While RAG systems are increasingly deployed in dynamic web search, temporal volatility amplifies their vulnerability to adversarial attacks. Existing static-oriented defenses struggle to handle evolving threats and incur prohibitive storage costs in dynamic settings. We propose RADAR, a framework that models reliable context selection as a graph-based energy minimization problem, solved exactly via Max-Flow Min-Cut. By incorporating a Bayesian memory node, RADAR recursively updates a belief state instead of archiving raw historical documents, effectively balancing stability against attacks with adaptability to genuine knowledge shifts. Experiments on a novel dynamic dataset show that RADAR achieves superior robustness and response quality with minimal storage overhead compared to the baselines.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
