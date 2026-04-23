# 🔐 大模型安全相关研究 | 2026年04月24日

> 本类共 **5** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [AgentSOC: A Multi-Layer Agentic AI Framework for Security Operations Automation](https://arxiv.org/abs/2604.20134)

**<font color=#1a73e8>作者：</font>** Joyjit Roy, Samaresh Kumar Singh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security Operations Centers (SOCs) increasingly encounter difficulties in correlating heterogeneous alerts, interpreting multi-stage attack progressions, and selecting safe and effective response actions. This study introduces AgentSOC, a multi-layered agentic AI framework that enhances SOC automation by integrating perception, anticipatory reasoning, and risk-based action planning. The proposed architecture consolidates several layers of abstraction to provide a single operational loop to support normalizing alerts, enriching context, generating hypotheses, validating structural feasibility, and executing policy-compliant responses. Conceptually evaluated within a large enterprise environment, AgentSOC improves triage consistency, anticipates attackers' intentions, and provides recommended containment options that are both operationally feasible and well-balanced between security efficacy and operational impact. The results suggest that hybrid agentic reasoning has the potential to serve as a foundation for developing adaptive, safer SOC automation in large enterprises. Additionally, a minimal Proof-Of-Concept (POC) demonstration using LANL authentication data demonstrated the feasibility of the proposed architecture.

---


### 2. [Taint-Style Vulnerability Detection and Confirmation for Node.js Packages Using LLM Agent Reasoning](https://arxiv.org/abs/2604.20179)

**<font color=#1a73e8>作者：</font>** Ronghao Ni, Mihai Christodorescu, Limin Jia  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapidly evolving Node$.$js ecosystem currently includes millions of packages and is a critical part of modern software supply chains, making vulnerability detection of Node$.$js packages increasingly important. However, traditional program analysis struggles in this setting because of dynamic JavaScript features and the large number of package dependencies. Recent advances in large language models (LLMs) and the emerging paradigm of LLM-based agents offer an alternative to handcrafted program models. This raises the question of whether an LLM-centric, tool-augmented approach can effectively detect and confirm taint-style vulnerabilities (e.g., arbitrary command injection) in Node$.$js packages. We implement LLMVD$.$js, a multi-stage agent pipeline to scan code, propose vulnerabilities, generate proof-of-concept exploits, and validate them through lightweight execution oracles; and systematically evaluate its effectiveness in taint-style vulnerability detection and confirmation in Node$.$js packages without dedicated static/dynamic analysis engines for path derivation. For packages from public benchmarks, LLMVD$.$js confirms 84% of the vulnerabilities, compared to less than 22% for prior program analysis tools. It also outperforms a prior LLM-program-analysis hybrid approach while requiring neither vulnerability annotations nor prior vulnerability reports. When evaluated on a set of 260 recently released packages (without vulnerability groundtruth information), traditional tools produce validated exploits for few ($\leq 2$) packages, while LLMVD$.$js generates validated exploits for 36 packages.

---


### 3. [Text Steganography with Dynamic Codebook and Multimodal Large Language Model](https://arxiv.org/abs/2604.20269)

**<font color=#1a73e8>作者：</font>** Jianxin Gao, Ruohan Lei, Wanli Peng  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the popularity of the large language models (LLMs), text steganography has achieved remarkable performance. However, existing methods still have some issues: (1) For the white-box paradigm, this steganography behavior is prone to exposure due to sharing the off-the-shelf language model between Alice and Bob.(2) For the black-box paradigm, these methods lack flexibility and practicality since Alice and Bob should share the fixed codebook while sharing a specific extracting prompt for each steganographic sentence. In order to improve the security and practicality, we introduce a black-box text steganography with a dynamic codebook and multimodal large language model. Specifically, we first construct a dynamic codebook via some shared session configuration and a multimodal large language model. Then an encrypted steganographic mapping is designed to embed secret messages during the steganographic caption generation. Furthermore, we introduce a feedback optimization mechanism based on reject sampling to ensure accurate extraction of secret messages. Experimental results show that the proposed method outperforms existing white-box text steganography methods in terms of embedding capacity and text quality. Meanwhile, the proposed method has achieved better practicality and flexibility than the existing black-box paradigm in some popular online social networks.

---


### 4. [CyberCertBench: Evaluating LLMs in Cybersecurity Certification Knowledge](https://arxiv.org/abs/2604.20389)

**<font color=#1a73e8>作者：</font>** Gustav Keppler, Ghada Elbez, Veit Hagenmeyer  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid evolution and use of Large Language Models (LLMs) in professional workflows require an evaluation of their domain-specific knowledge against industry standards. We introduceCyberCertBench, a new suite of Multiple Choice Question Answering (MCQA) benchmarks derived from industry recognized certifications. CyberCertBench evaluates LLM domain knowledgeagainst the professional standards of Information Technology cybersecurity and more specializedareas such as Operational Technology and related cybersecurity standards. Concurrently, we propose and validate a novel Proposer-Verifier framework, a methodology to generate interpretable,natural language explanations for model performance. Our evaluation shows that frontier modelsachieve human expert level in general networking and IT security knowledge. However, theiraccuracy declines in questions that require vendor-specific nuances or knowledge in formalstandards, like, e.g., IEC 62443. Analysis of model scaling trend and release date demonstratesremarkable gains in parameter efficiency, while recent larger models show diminishing this http URL and evaluation scripts are available at: this https URL.

---


### 5. [Synthesizing Multi-Agent Harnesses for Vulnerability Discovery](https://arxiv.org/abs/2604.20801)

**<font color=#1a73e8>作者：</font>** Hanzhi Liu, Chaofan Shou, Xiaonan Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents have begun to find real security vulnerabilities that human auditors and automated fuzzers missed for decades, in source-available targets where the analyst can build and instrument the code. In practice the work is split among several agents, wired together by a harness: the program that fixes which roles exist, how they pass information, which tools each may call, and how retries are coordinated. When the language model is held fixed, changing only the harness can still change success rates by several-fold on public agent benchmarks, yet most harnesses are written by hand; recent harness optimizers each search only a narrow slice of the design space and rely on coarse pass/fail feedback that gives no diagnostic signal about why a trial failed. AgentFlow addresses both limitations with a typed graph DSL whose search space jointly covers agent roles, prompts, tools, communication topology, and coordination protocol, paired with a feedback-driven outer loop that reads runtime signals from the target program itself to diagnose which part of the harness caused the failure and rewrite it accordingly. We evaluate AgentFlow on TerminalBench-2 with Claude Opus 4.6 and on Google Chrome with Kimi K2.5. AgentFlow reaches 84.3% on TerminalBench-2, the highest score in the public leaderboard snapshot we evaluate against, and discovers ten previously unknown zero-day vulnerabilities in Google Chrome, including two Critical sandbox-escape vulnerabilities (CVE-2026-5280 and CVE-2026-6297).

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
