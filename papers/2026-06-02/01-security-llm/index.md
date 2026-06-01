# 🔐 大模型安全相关研究 | 2026年06月02日

> 本类共 **11** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [The Surface You Test Is Not the Surface That Breaks](https://arxiv.org/abs/2605.30454)

**<font color=#1a73e8>作者：</font>** Shifat E Arman, Syed Nazmus Sakib, Nafiul Haque 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-augmented LLM agents are vulnerable to prompt injection: a third party who controls part of the agent's context can plant instructions that the agent then executes as if they came from the user. Current evaluations report a single attack success rate per model on one channel, the tool output and treat that number as the model's vulnerability. But tool descriptions, which the agent reads at every turn before any tool is called, are themselves an injection surface that the attacker can choose instead. We hold the injection payload byte-identical and deliver it through both surfaces across 13 LLMs from six families and four task suites. The same bytes invert in success rate across models: GPT-4.1 is 96 percent vulnerable on tool outputs but only 4 percent on tool descriptions, while GEMINI-3-FLASH shows the mirror pattern at 20 percent and 98 percent. A variance decomposition over 6,830 attempts attributes 0 percent of the variation in attack outcomes to the surface alone, while the model-surface interaction accounts for 16.7 percent. Vulnerability is a property of the pairing, not the channel. The Adaptive Attack Rate, defined as the per-cell maximum over surfaces, exceeds the strongest fixed-surface baseline by +9.1 percentage points on average. Standard prompt-level defenses inherit the same blindspot, reducing tool-output ASR to 10-18 percent while leaving the description channel above 54 percent. Both attack and defense evaluation must report per-surface vulnerability.

---


### 2. [Strengthening Polymorphic Prompt Assembling: Dynamic Separator Generation Against Emerging Prompt Injection Attacks](https://arxiv.org/abs/2605.30534)

**<font color=#1a73e8>作者：</font>** Nima Dorzhiev, Peng Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Polymorphic Prompt Assembling (PPA) defends LLM agents against prompt injections by randomly selecting separator pairs from a fixed pool to isolate user input from system instructions. Although effective, static pool reuse exposes a blast-radius vulnerability: once a separator leaks, it can be exploited in future requests. We propose a dynamic per-request separator generation using domain-separated SHA-256 digests keyed on the timestamp, session identifier, and cryptographic nonce. Each assembled prompt receives a unique (BEGIN, END) canary pair, thereby limiting leakage exposure to a single request. We evaluated our extension against 16 injection payloads on Llama-3.3-70B-Instruct-Turbo, with cross-model validation on DeepSeek-V4-Flash model. Against the M1 obfuscation payload (leetspeak + urgency), the dynamic mode reduces the Attack Success Rate (ASR) from 0.88 to 0.38, yielding a statistically significant 2.3 x mitigation verified by non-overlapping 95% Wilson confidence intervals. Against format_breakout_salad, static separator leakage (leak_rate = 0.467) is eliminated entirely in the dynamic mode (0.000), confirming the blast-radius reduction in practice. The implementation requires no model fine-tuning, adds 2.7 microseconds prompt-assembly overhead per request, and is backward compatible with the existing PPA SDK.

---


### 3. [An Organization-Scoped LLM Agent Runtime Architecture for Regulated Cybersecurity Operations](https://arxiv.org/abs/2605.30604)

**<font color=#1a73e8>作者：</font>** George Fatouros, Georgios Makridis, George Kousiouris 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Regulated cybersecurity workflows lack a runtime substrate that enforces organization-level scope across retrieval, tool calls, memory, findings, reports, and audit while remaining model-agnostic and locally deployable. Recent large language model (LLM) agent systems report strong results on isolated cybersecurity tasks, yet they do not by themselves define an auditable platform architecture for regulated security operations centre (SOC) and compliance workflows, where a single analyst may trigger actions that bind the organization, and where the runtime must integrate with existing SIEM/XDR stacks as a primary source of context and alert-driven triggers rather than operate as a standalone analytical layer. This paper proposes an organization-scoped LLM agent runtime architecture for financial cybersecurity. The contribution is a typed Security Context that is created at every entry point, including SIEM/XDR notifications ingested as first-class triggers, and enforced at every component boundary, combined with a shared Runtime Core, logical specialist subagents, a governed Tool Adapter Layer exposing SIEM/XDR query, enrichment, and response primitives under uniform policy and audit, structured findings with evidence references, tiered human-in-the-loop (HITL) gates, and append-only audit. Model Context Protocol (MCP), extended telemetry, digital twins for pentesting, graph retrieval, and federated knowledge sharing are treated as optional extension paths rather than mandatory runtime assumptions. We describe an implementable slice as the architecture's testability surface, and we propose a falsifiable evaluation plan with metric-level pass criteria for architecture readiness, security-policy enforcement, evidence traceability, output quality, and operational observability.

---


### 4. [Automatically Attacking Software Reverse Engineering AI Agents](https://arxiv.org/abs/2605.30667)

**<font color=#1a73e8>作者：</font>** Brian Crawford, Justin Phillips, Patrick McClure  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software tools for reverse engineering executable binary files, such as Ghidra, enable malware analysts to safely conduct robust static analysis without having access to original source code. Coupled with the analytic power of large language models (LLM), agentic systems enabled with tools, such as GhidraMCP, can allow analysts to automate a previously human driven process. Although this automation can increase the productivity of a single malware analyst, it also introduces a new area of vulnerability for malware obfuscation. This paper presents an adversarial technique using genetic algorithm-based prompt generation, a modification of an adversarial attack known as AutoDAN, to demonstrate the ability to deceive LLM-powered disassembly and decompilation systems into misinterpreting binary executables, effectively corrupting their analytical output. This proof-of-concept methodology exploits inherent vulnerabilities in how LLMs process and interpret decompiled machine code via prompt injection by using extraneous string variable assignments to pass surreptitious instructions to the LLM while not impacting the functionality of the executable file. We demonstrate this capability through several concise examples. This approach could enable attackers to bypass automated detection systems that rely on LLM-driven analysis pipelines. By studying and understanding this attack, insights can be gained regarding the security implication of integrating LLMs into cybersecurity toolchains and building more robust agentic code analysis systems.

---


### 5. [Differentially Private Preference Data Synthesis for Large Language Model Alignment](https://arxiv.org/abs/2605.30808)

**<font color=#1a73e8>作者：</font>** Fengyu Gao, Jing Yang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Preference alignment is a crucial post-training step for large language models (LLMs) to ensure their outputs align with human values. However, post-training on real human preference data raises privacy concerns, as these datasets often contain sensitive user prompts and human judgments. To address this, we propose DPPrefSyn, a novel algorithm for generating differentially private (DP) synthetic preference data to enable privacy-preserving preference alignment. DPPrefSyn is a principled framework grounded in the Bradley-Terry preference model and the intrinsic geometric structure of pairwise human preference data. It first learns an underlying preference model from private data with formal differential privacy guarantees, and then leverages the learned model together with public prompts to synthesize high-quality preference data. It exploits the shared linear structure of per-cluster reward models to effectively capture heterogeneous human preferences in private datasets, and leverages DP Principal Component Analysis (DP-PCA) to improve learning accuracy. Extensive experimental results demonstrate that DPPrefSyn achieves competitive alignment performance under strong DP guarantees. These findings highlight the potential of synthetic preference data as a practical alternative for privacy-preserving preference alignment across a broad range of applications. To the best of our knowledge, this is the first work to generate DP synthetic preference data for LLM alignment. Our code is available at this https URL.

---


### 6. [LLM Anonymization Against Agentic Re-Identificatio](https://arxiv.org/abs/2605.30848)

**<font color=#1a73e8>作者：</font>** Ziwen Li, Jianing Wen, Tianshi Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic LLMs with web search change the threat model for text anonymization: weak contextual cues can become cross-referenceable evidence for re-identification, yet those same details also carry downstream analytic value of the text. Existing defenses either remove explicit identifiers, perturb text for formal privacy, or test rewritten text against non-web inference models, leaving underexplored the operating region between resistance to agentic web-search re-identification and utility retention. We introduce AURA (\textbf{A}nonymization with \textbf{U}tility-\textbf{R}etention \textbf{A}daptation), an LLM-powered \textit{mask-reconstruct} framework that decouples privacy localization from utility-preserving reconstruction and selects candidates with adversarial privacy and utility-retention checks. We evaluate AURA on real-user interview transcripts using re-identification attacks carried out by web-search agents, along with a utility evaluation based on interviewee-profile facts, codebook facts, and the joint contextual utility grid. Our results show that AURA improves the privacy-utility frontier by using adaptive privacy scope to strengthen resistance to agentic re-identification and using a mask-reconstruct anonymization method to better preserve contextual utility under fixed privacy scope.

---


### 7. [TRACE: Task-Aware Adaptive Self-Evolving Agentic Jailbreaking](https://arxiv.org/abs/2605.30883)

**<font color=#1a73e8>作者：</font>** Churui Zeng, Weiwei Qi, Kedong Xiu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rise of LLM agents introduces a new threat by enabling planning, coding, and even end-to-end execution of expert-level attack workflows. However, this threat remains underexplored and underestimated since (i) safety alignment prevents LLMs from directly generating harmful instructions, and (ii) most existing jailbreak methods cannot consistently induce agents to execute malicious operations. In this paper, we propose TRACE, a practical agentic jailbreaking framework to further reveal the risks of this threat surface. To conceal the malicious intent, TRACE decomposes a malicious task into multiple subtask sequences under different schemes and selects the sequence with the fewest explicitly harmful subtasks. TRACE then disguises the remaining harmful subtasks as benign-looking instructions by embedding them in task-aware scenarios with related roles, environments, directives, and heuristics. The scenarios are iteratively evolved through well-defined transformation actions, which are sampled by a Q-learning-inspired mechanism, for inducing the agent to execute on the harmful subtasks. Extensive evaluations on AgentHarm and AdvCUA show that TRACE consistently outperforms existing jailbreak baselines across multiple advanced LLM agents, achieving up to 100% bypass rate and 0.73 average success score. We also demonstrate the effectiveness of TRACE in controlled cyberattack instances. Our code and demos are available at this https URL.

---


### 8. [From Prompt Injection to Persistent Control: Defending Agentic Harness Against Trojan Backdoors](https://arxiv.org/abs/2605.31042)

**<font color=#1a73e8>作者：</font>** Jiejun Tan, Zhicheng Dou, Xinyu Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents are evolving from conversational chatbots to operational tools in real-world workspaces. In local agentic harnesses, an LLM can read and write files, call tools, and reuse workspace state across sessions. While such capabilities enhance utility, they also expose a new attack surface for attackers. Attackers can embed a prompt injection within a file or tool output. Agents may read this hidden instruction, store it, and execute it later. In this multi-step trojan attack paradigm, no individual step appears malicious on its own, but these steps can collectively turn untrusted text into persistent control content. However, existing defenses often inspect each step in isolation. As a result, they can block a clear harmful action, but fail to detect the earlier write operation that plants the backdoor. To reveal this threat, we introduce ClawTrojan, a benchmark designed to identify multi-step trojan attacks in local agentic harnesses. In an OpenClaw-style simulated workspace with GPT-5.4, ClawTrojan reaches a 95.5% attack success rate (ASR), while existing single-turn prompt-injection attacks produce near-zero ASR on the same model. To address this threat, we propose DASGuard, which scans control-like text in sensitive local files, traces its origin, and removes control content that does not originate from a trusted source. Our results show that DASGuard achieves strong dynamic defense by combining runtime attack blocking with sanitized commits to the workspace.

---


### 9. [R+R: Reassessing Java Security API Misuse in Current LLMs: A Replication on JCA and JSSE APIs with External Security Knowledge](https://arxiv.org/abs/2605.31135)

**<font color=#1a73e8>作者：</font>** Tianhe Lu, Eric Spero, Sakuna Harinda Jayasundara 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The misuse of Java security APIs is a serious security problem in software development. Research in 2024 has shown that this problem is widespread in LLM-generated code. However, it remains unclear whether this phenomenon persists in current models and how external security knowledge affects it. This paper presents a scoped replication and extension of Mousavi et al.'s study on the Java Cryptography Architecture (JCA) and Java Secure Socket Extension (JSSE) APIs. We focus on two complementary settings: GPT-5.5 as a frontier proprietary coding model, and Llama-3.3-70B-Instruct as a strong open-weight model relevant to self-hosted deployment. The results show that although newer LLMs perform better in using Java security APIs, the problem of Java security API misuse has not been eliminated. External security knowledge substantially improves the measured outcome, but its effect is model-dependent. For Llama-3.3-70B-Instruct, secure code examples are the most effective single knowledge type. For GPT-5.5, explicit misuse patterns eliminate all detected security API misuses among valid programs in our benchmark, although some outputs remain invalid due to compilation errors or target-API mismatches. In addition, developer-guide knowledge becomes much more effective, and secure prompting also provides large gains for GPT-5.5. Overall, these findings confirm the Java security API misuse risk identified in the original study and show that the benefits of retrieval-augmented knowledge depend not only on the knowledge itself and retrieval behavior, but also on model capability.

---


### 10. [EvoDefense: Co-Evolving Black-Box Defense with Large Language Models](https://arxiv.org/abs/2605.31140)

**<font color=#1a73e8>作者：</font>** Yu Li, Yuenan Hou, Yingmei Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) remain highly vulnerable to diverse attacks, particularly in black-box settings where the internals of target models are inaccessible. Existing black-box defenses typically rely on pre-defined filtering heuristics, which often fail to generalize to unseen attack types and target model architectures. We introduce EvoDefense, an experience-guided co-evolving black-box defense paradigm. EvoDefense employs a guard LLM to detect malicious queries and an experience memory module to accumulate defense knowledge from previous interactions. At the core of EvoDefense is a continuous attack-defense evolution loop, where an attack generator and the guard model iteratively refine their attack strategies and defense policies through experience-guided optimization. This design enables EvoDefense to generalize across unseen attacks and target models without retraining. Experiments on HarmBench, AdvBench, and AlpacaEval show that EvoDefense achieves consistently strong defense performance across seven popular models and five representative LLM attacks, while preserving competitive general capabilities. On HarmBench, EvoDefense reduces the attack success rate (ASR) of AutoDAN-turbo on Gemini-3-flash and LLaMA-3-8B-Instruct from 29.4% and 43.4% to 8.4% and 6.2%, respectively.

---


### 11. [When Entropy Is Not Enough: Multi-Modal Classification of Encrypted and Compressed Data Fragments](https://arxiv.org/abs/2605.31337)

**<font color=#1a73e8>作者：</font>** Fabio De Gaspari, Dorjan Hitaj, Samuele Salaris 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reliable identification of encrypted data fragments is essential in cybersecurity, with applications to ransomware detection, digital forensics, and large-scale data analysis. Distinguishing encrypted from compressed fragments is particularly challenging, as short fragments lack structural data and exhibit low statistical redundancy. Traditional statistical methods based on byte-level distributions show limited effectiveness on this task. Recent machine learning approaches improve performance by learning subtle patterns from raw bytes, but predominantly rely on single-modal representations, implicitly assuming that a single view of the data is sufficient for accurate classification. This paper shows that this assumption becomes a fundamental limitation in low-information settings, when only small fragments of data are available (512--2048 Bytes). We propose Triumvir, a multi-modal, uncertainty-aware ensemble architecture that integrates statistical, sequential, and spatial representations of raw byte fragments. Extensive experimental analysis demonstrates that Triumvir consistently outperforms state-of-the-art methods with gains of up to +4.5pp in binary and +6.4pp in multiclass classification. Ablation studies confirm that combining modalities is critical, yielding improvements of up to +5pp over partial configurations.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
