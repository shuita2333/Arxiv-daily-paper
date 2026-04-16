# 🔐 大模型安全相关研究 | 2026年04月17日

> 本类共 **4** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

---

### 1. [Can Agents Secure Hardware? Evaluating Agentic LLM-Driven Obfuscation for IP Protection](https://arxiv.org/abs/2604.13298)

**<font color=#1a73e8>作者：</font>** Sujan Ghimire, Parsa Mirfasihi, Muhtasim Alam Chowdhury 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The globalization of integrated circuit (IC) design and manufacturing has increased the exposure of hardware intellectual property (IP) to untrusted stages of the supply chain, raising concerns about reverse engineering, piracy, tampering, and overbuilding. Hardware netlist obfuscation is a promising countermeasure, but automating the generation of functionally correct and security-relevant obfuscated circuits remains challenging, particularly for benchmark-scale designs. This paper presents an agentic, large language model (LLM)-driven framework for automated hardware netlist obfuscation. The proposed framework combines retrieval-grounded planning, structured lock-plan generation, deterministic netlist compilation, functional verification, and SAT-based security evaluation. Rather than a single prompt-to-output generation step, the framework decomposes the task into specialized stages for circuit analysis, synthesis, verification, and attack evaluation. We evaluate the framework on ISCAS-85 benchmarks using functional equivalence checking and SAT-based attacks. Results show that the framework generates correct locked netlists while introducing measurable output corruption under incorrect keys, while SAT attacks remain effective. These findings highlight both the potential and current limitations of agentic LLM-driven obfuscation.

---


### 2. [SafeHarness: Lifecycle-Integrated Security Architecture for LLM-based Agent Deployment](https://arxiv.org/abs/2604.13630)

**<font color=#1a73e8>作者：</font>** Xixun Lin, Yang Liu, Yancheng Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The performance of large language model (LLM) agents depends critically on the execution harness, the system layer that orchestrates tool use, context management, and state persistence. Yet this same architectural centrality makes the harness a high-value attack surface: a single compromise at the harness level can cascade through the entire execution pipeline. We observe that existing security approaches suffer from structural mismatch, leaving them blind to harness-internal state and unable to coordinate across the different phases of agent operation. In this paper, we introduce \safeharness{}, a security architecture in which four proposed defense layers are woven directly into the agent lifecycle to address above significant limitations: adversarial context filtering at input processing, tiered causal verification at decision making, privilege-separated tool control at action execution, and safe rollback with adaptive degradation at state update. The proposed cross-layer mechanisms tie these layers together, escalating verification rigor, triggering rollbacks, and tightening tool privileges whenever sustained anomalies are detected. We evaluate \safeharness{} on benchmark datasets across diverse harness configurations, comparing against four security baselines under five attack scenarios spanning six threat categories. Compared to the unprotected baseline, \safeharness{} achieves an average reduction of approximately 38\% in UBR and 42\% in ASR, substantially lowering both the unsafe behavior rate and the attack success rate while preserving core task utility.

---


### 3. [RealVuln: Benchmarking Rule-Based, General-Purpose LLM, and Security-Specialized Scanners on Real-World Code](https://arxiv.org/abs/2604.13764)

**<font color=#1a73e8>作者：</font>** John Pellew, Faizan Raza  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> How do security scanners perform on real-world code? We present RealVuln, the first open-source benchmark comparing Rule-Based SAST, General-Purpose LLMs, and Security-Specialized scanners on 26 intentionally vulnerable Python repositories (educational and Capture-The-Flag applications) with 796 hand-labeled entries (676 vulnerabilities, 120 false-positive traps). We test 15 scanners (3 Rule-Based SAST, 10 General-Purpose LLM, 2 Security-Specialized) and rank them by F3 score (beta=3, weighting recall 9x over precision). A clear three-tier ranking emerges under all metrics. Under F3, the Security-Specialized scanner this http URL (73.0) leads, followed by the best General-Purpose LLM, Claude Sonnet 4.6 (51.7), which in turn scores nearly 3x higher than the best Rule-Based tool, Semgrep (17.7). Under F1, Sonnet 4.6 leads (60.9) with this http URL at 52.4. Rankings within tiers shift with beta, but the three-tier hierarchy holds across all weightings. All code, ground-truth data, scanner outputs, and scoring scripts are released under an open-source license. An interactive dashboard is at this https URL. RealVuln is a living benchmark: versioned, community-driven, with a roadmap toward multi-language coverage.

---


### 4. [Towards Personalizing Secure Programming Education with LLM-Injected Vulnerabilities](https://arxiv.org/abs/2604.13955)

**<font color=#1a73e8>作者：</font>** Matthew Frazier, Kostadin Damevski  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> According to constructivist theory, students learn software security more effectively when examples are grounded in their own code. Generic examples often fail to connect with students' prior work, limiting engagement and understanding. Advances in LLMs are now making it possible to automatically generate personalized examples by embedding security vulnerabilities directly into student-authored code. This paper introduces a method that uses LLMs to inject instances of specific Common Weakness Enumerations (CWEs) into students' own assignment code, creating individualized instructional materials. We present an agentic AI framework, using autonomous LLM-based agents equipped with task-specific tools to orchestrate injection, evaluation, ranking, and learning outcome generation.
We report the experience of deploying this system in two undergraduate computer science courses (N=71), where students reviewed code samples containing LLM-injected vulnerabilities and completed a post-project survey. We compared responses with a baseline using a widely adopted set of generic security instructional materials. Students qualitatively reported finding CWE injections into their own code more relevant, clearer, and more engaging than the textbook-style examples. However, our quantitative findings revealed limited statistically significant differences, suggesting that while students valued the personalization, further studies and refinement of the approach are needed to establish stronger empirical support.

---


- [返回当日日报目录](./index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
