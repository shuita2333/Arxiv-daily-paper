# 🔐 大模型安全相关研究 | 2026年06月17日

> 本类共 **23** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [A Security Analysis of Long-Horizon Agentic AI Systems: Threats, Evaluation, and Framework Development](https://arxiv.org/abs/2606.14816)

**<font color=#1a73e8>作者：</font>** Ahmed Mohammed Almalki, Mehedi Masud  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents a structured analysis of security challenges in long-horizon agentic AI systems. The study reviews existing threats, evaluation approaches, attack propagation mechanisms, and security frameworks. A taxonomy of security threats and a framework for analyzing attack propagation are proposed to support future research in agentic AI security

---


### 2. [Is Your Agent Playing Dead? Deployed LLM Agents Exhibit Constraint-Evasive Fabrication and Thanatosis](https://arxiv.org/abs/2606.14831)

**<font color=#1a73e8>作者：</font>** Andoni Rodríguez, Alberto Pozanco, Daniel Borrajo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper presents and characterizes a spectrum of previously unreported behaviours we term Constraint-Evasive Fabrication (CEF): when an LLM agent operates under irreconcilable constraints (where no response can simultaneously satisfy all active rules) it spontaneously fabricates plausible external obstacles and presents them as a fact. At the extreme end of this spectrum lies Constraint-Evasive Thanatosis (CET); the limit case where, rather than inventing a plausible excuse, the model simulates a full system crash to make the user disengage entirely. We first observed CET in an uncontrolled deployment test, where a GPT-4o banking agent fabricated Python-style exception traces (complete with memory addresses) to feign a system failure when threatened by a user. In subsequent controlled experiments, the model independently invented audit restrictions, microservice architectures, error codes, and service timeouts, none present in its prompt. Reproduction attempts across pressure levels and attacker personas yielded CEF consistently but with substantial variation in form, onset, and severity: the phenomenon is robust but stochastic. Critically, injecting ground-truth data mid-conversation did not restore honest behaviour once fabrication had taken hold (the model ignored correct information and continued confabulating) suggesting CEF is self-reinforcing rather than a knowledge gap. We show that (1) standard enterprise guardrails routinely create CEF-enabling conditions in production, (2) current RLHF procedures suppress but cannot eliminate CEF, and (3) existing safety benchmarks do not test for this failure mode. Our results highlight the need for irreconcilable-constraint benchmarks, CEF-aware training procedures, and deployment-time detection methods before constrained agents become further entrenched in high-stakes domains.

---


### 3. [Security Engineering of OpenClaw: Analyzing Attack Surface Expansion and Trust-Boundary Violations](https://arxiv.org/abs/2606.15008)

**<font color=#1a73e8>作者：</font>** Saeid Jamshidi, Arghavan Moradi Dakhel, Kawser Wazed Nafi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic large language model (LLM) systems can now execute actions, not only produce text. When model outputs trigger privileged operations such as shell commands, browser automation, or external tool calls, the security problem shifts from alignment alone to system configuration and structural design. We analyze OpenClaw, a self-hosted multi-agent system in which LLM outputs can execute commands and interact with tools and services. We measure compromise probability, boundary failures, privilege drift, and how these metrics change as attacker capability increases. With one agent, the compromise probability is 0.24. With seven agents, when the system executes an action, the compromise rises to 0.86 if any single agent proposes it. The models do not change; the increase comes from output aggregation. Prompt injection propagates instability across the system. Attack surface entropy increases from 0.42 to 0.71, indicating a broader distribution of exploit paths. The mean privilege drift increases from 0.03 to 0.21, indicating unintended authority gain. Positive escalation curvature of 0.08 indicates that privilege grows faster as attacker capability increases. Defensive controls, including policy gating and execution filtering, reduce compromise probability by 0.10, boundary failures by 0.10, and privilege drift by 0.02, all statistically significant at p < 0.0001. The system remains sensitive, but the mitigation impact is measurable. Injection mitigation success differs across models: 0.37 for GPT-5.2, 0.35 for Llama-4-Maverick, and 0.31 for DeepSeek-R1. When execution can be triggered by any single agent, the most vulnerable agent determines system exposure. Mitigations slightly reduce task utility from 0.93 to 0.89 and increase median latency from 420 ms to 468 ms.

---


### 4. [Semantic Integrity Failures in Document-to-LLM Supply Chains](https://arxiv.org/abs/2606.15020)

**<font color=#1a73e8>作者：</font>** Side Liu, Jiang Ming  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Document-to-LLM applications typically read uploaded PDFs by first translating them into text through a hidden extraction layer that users cannot observe or audit. We show that this layer enables split-view PDFs: one document can have two semantic views before model reasoning. By mining specification-permitted or implementation-tolerated representation gaps at the PDF render/extract boundary, we instantiate 25 extraction gaps (EG) in which extractors return attacker-controlled or extractor-dependent text while the rendered page shows benign or different content. The gaps form four families: semantic overrides, hidden semantic injection, reading-order splits, and font-decoding splits, and 14 gaps have no exact path/mechanism-level match in prior PDF-to-LLM attacks.
We evaluate these gaps on 16 PDF processing stacks and 7 commercial LLM services. Each gap causes render-extract divergence on at least one stack. Under a gap-level exposure criterion, every evaluated service exposes at least one gap, with 12/25 to 21/25 exposed gaps. Exposure is driven mainly by the ingestion stack -- not model identity alone. We further show that tested safety filters cover only selected hidden-text constructions. To support triage, we develop a static screening scanner whose rules trigger on all 25 benchmark gaps, and discuss dual-view consistency as a longer-term defense direction.

---


### 5. [AutoDojo: Adaptive Attacks Expose Superficial Defenses and User-Underspecification Limits in LLM Agents](https://arxiv.org/abs/2606.15057)

**<font color=#1a73e8>作者：</font>** Xinhang Ma, Taoran Li, Chaowei Xiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Indirect prompt injection (IPI) is a major security threat to LLM-powered agents. Thus, a growing body of work have proposed a variety of defensive approaches against IPI. These can be grouped into three broad categories: 1) prompt-based (using prompting as a way to prevent agents from following malicious instructions), 2) detection-based (identifying and filtering malicious instructions), and 3) system-level (using systems insights, such as control and data isolation, for defense). However, commonly used benchmarks for evaluating defense, such as AgentDojo, are \emph{inherently static}, generating a fixed distribution of IPI attacks. Consequently, static benchmarks do not usefully evaluate defense robustness to adaptive threats. We address this issue by developing AutoDojo, an adaptive extension of AgentDojo that optimizes IPI against a given defense. Using AutoDojo against state-of-the-art IPI defenses across three task suites and five target models, we make two key observations. First, many defenses offer only limited protection: a cheap, black-box adaptive attack using a frontier LLM to iteratively optimize the injection raises attack success rate (ASR) well above the level achieved by static injections against nearly all evaluated defenses. Against a filter that reduces static ASR to 0\%, AutoDojo recovers 28\% overall and 64\% on action-open tasks. Second, for prompt-level and filter-based defenses, ASR is substantially higher on \emph{action-open} tasks -- where the user's request delegates the action itself to attacker-controlled content -- than on precisely specified tasks. This is a structural limit: on such tasks the injection can pose as ordinary data rather than an explicit instruction, bypassing defenses that rely on detecting instruction-like text. AutoDojo is publicly available at this https URL.

---


### 6. [Data-Centric Benchmarking of Exploit Generation in LLMs: Understanding the Impact of Fine-Tuning](https://arxiv.org/abs/2606.15123)

**<font color=#1a73e8>作者：</font>** Yiwei Chen, Lichi Li, Kai Cheung 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We study the task of CVE-conditioned exploit generation, where a model drafts proof-of-concept (PoC) exploits given software vulnerability context. We adopt a data-centric approach, constructing a high-quality dataset via multi-stage preprocessing and introducing a scalable evaluation framework with LLM-as-judge and fine-grained rubrics. Under this unified setup, we benchmark 17 large language models across 8 evaluation criteria, providing systematic insights into their zero-shot capabilities. We further show that a compact 8B open-weight model, when fine-tuned on curated data, achieves over 42.5% improvement in exploit quality and rivals some proprietary models when combined with simple test-time rejection strategies. Our results highlight the importance of data quality, structured supervision, and evaluation design for reliable exploit generation, suggesting that these factors can be as critical as model scale in adapting LLMs to cybersecurity tasks.

---


### 7. [LLM: LSTM Look-Ahead Moving Target Defense Based on Historical Malicious Scan](https://arxiv.org/abs/2606.15229)

**<font color=#1a73e8>作者：</font>** Yu Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Network scanning is a critical preliminary step for most adversaries to gain essential information before launching cyber attacks. Moving Target Defense (MTD) based on IP shuffling has emerged as a proactive defense strategy to counteract these reconnaissance efforts. Unlike static, reactive defense techniques, IP shuffling introduces randomness by dynamically reassigning network addresses, making it more challenging for attackers to identify and track targets. However, current IP shuffling methods face three key challenges: 1) limited scalability across different network topologies, 2) inherent reconfiguration overhead even in the absence of an active attack, and 3) the need for large-scale unused address blocks. To address these issues, we propose LSTM Look-ahead Moving Target Defense (LLM). Our approach is the first attempt using a Long Short-Term Memory (LSTM) network to predict future target addresses that attackers will likely scan. Ensemble learning is used to improve robustness to different scanning behaviors. We introduce a dynamic mutation mechanism to enhance adaptability. Compared to the baseline mutation strategy, LLM performs better in both security and overhead.

---


### 8. [Defending against Adaptive Prompt Injection Attacks via Reasoning-enabled Task Alignment](https://arxiv.org/abs/2606.15441)

**<font color=#1a73e8>作者：</font>** Lipeng He, Yihan Wang, Jiawen Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Indirect prompt injection attacks hijack LLM-based agents by embedding malicious instructions in third-party data that the agent retrieves during task execution. Existing defenses report near-zero attack success rate on static benchmarks, yet recent adaptive evaluations show that these results collapse once the attacker is allowed to optimize against the deployed defense. In this work, we trace this collapse to two failure modes. First, existing defense methods are confined to recognizing specific attack patterns, rather than assessing whether the intent of every embedded instruction is relevant to the user task. Second, training-based defenses, which otherwise offer the strongest safety-utility trade-off, assemble their adversarial examples from a handful of hand-crafted templates, and the resulting defender fails to generalize outside that narrow strategy distribution. To address these gaps, we propose RETA, a training-based method that grounds defense decisions on the user tasks rather than attacker-controlled data. At each tool-output step, the defender undertakes chain-of-thought reasoning verifying that its actions are consistent with the user task. Leveraging red-teaming, a simulated attacker synthesizes adversarial training data and receives a dictionary-learning diversity reward, achieving broad coverage of injection-reformulation strategies. Together, these allow the defender to be optimized via multi-objective reinforcement learning and achieve better safety-utility trade-off. Across six black-box adaptive attacks, RETA keeps every per-attack ASR below 10%, with average ASR of 2.92% and 3.75% on the two target models, while preserving most utility under attack and on clean inputs.

---


### 9. [FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion](https://arxiv.org/abs/2606.15609)

**<font color=#1a73e8>作者：</font>** Zixin Rao, Wentian Zhu, Chan Aristella Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly rely on long-term memory to support complex task execution, user personalization, and domain adaptation. Meanwhile, emerging access-control mechanisms for LLM agents are being explored to block policy-violating requests and prevent misuse. We reveal a novel attack surface arising from agent memory operations: prohibited content that would trigger access control can be fragmented across interactions, stored in long-term memory in benign-appearing form, and later reconstructed through memory retrieval without appearing explicitly in the final user query. We propose FragFuse, the first attack that enables unprivileged users to bypass agent access control by exploiting this temporal channel introduced by long-term memory. FragFuse operates in three stages: (1) identifying rejection-responsive fragments via black-box adaptive querying with fragment masking; (2) injecting these fragments into memory using marker carrier queries; and (3) retrieving and fusing the stored fragments through a follow-up attack query. Although FragFuse can be instantiated manually for individual agents, we further develop a surrogate-based optimization scheme that tunes fusion instructions and marker designs, enabling automated attack generation without violating the attacker's threat-model assumptions. We evaluate FragFuse across four representative agent settings and task domains, covering three state-of-the-art agent access-control mechanisms. FragFuse achieves an average bypass success rate of 86.3% and an average end-to-end harmful task success rate of 41.1% across all settings, with only 4.4% average task-success degradation compared with configurations without access control. We also show that alternative defenses, including state-of-the-art prompt-injection detectors and perplexity detectors, do not effectively address this attack.

---


### 10. [Snyk VulnBench JS 1.0: Can LLMs Find the Same Bugs Twice?](https://arxiv.org/abs/2606.15762)

**<font color=#1a73e8>作者：</font>** Liran Tal, Johannes Kloos, Arsenii Rudich 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We ran 300 repeated vulnerability-finding scans to measure how repeatable agentic large language model (LLM) security review is on the same JavaScript code, prompt, and benchmark harness. The headline result is that LLM security findings were unevenly repeatable: reference-matched findings were stable, but extra model reports varied heavily from run to run. Across 250 model runs, 80 of 161 unique unmatched findings appeared in only one of five identical repetitions, while only 22 appeared in all five. By contrast, when Claude matched a Snyk Code reference finding, the behavior was much more stable: 134 of 158 unique reference-matched findings appeared in all five repetitions. The benchmark also shows complementarity. Models consistently found familiar, high-signal exploit shapes, and in one case surfaced a likely Snyk Code product gap. Snyk Code static application security testing (SAST) was deterministic and better at systematically enumerating repeated data-flow sinks. The results support combining agentic LLM review with deterministic SAST rather than treating either technique as a replacement for the other.

---


### 11. [GAS-Leak-LLM: Genetic Algorithm-Based Suffix Optimization for Black-Box LLM Jailbreaking](https://arxiv.org/abs/2606.15788)

**<font color=#1a73e8>作者：</font>** Aman Anifer, Vignesh Kumar Kembu, Vishnu M 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) constitute pivotal components within the AI-dominated information technology ecosystem. To mitigate risks associated with harmful or policy-violating outputs, commercial systems employ advanced alignment strategies and multi-layered content moderation mechanisms. Despite these safeguards, recent research has demonstrated that LLMs remain vulnerable to adversarial manipulation, particularly through jailbreaking and prompt injection techniques. In this work, we propose GAS-Leak-LLM a novel jailbreaking attack based on a genetic algorithm that systematically evolves adversarial suffix to bypass safety constraints. Operating in a strict black-box setting, our method requires no access to model parameters or internals, thereby reflecting realistic threat scenarios in deployed systems. Through the iterative application of selection, mutation, and crossover heuristics, the framework systematically explores the discrete prompt space to identify high-fitness adversarial suffixes. Empirical findings reveal critical shortcomings in existing safety enforcement mechanisms and confirm the effectiveness and practical viability of the proposed attack.

---


### 12. [AttackonCTF: Defending Hardware Security Competition Benchmarks in the Age of LLMs](https://arxiv.org/abs/2606.15809)

**<font color=#1a73e8>作者：</font>** Mohamadreza Rostami, Nikhilesh Singh, Stephen Muttathil 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hardware security competitions such as HackTheSilicon serve as benchmarking platforms for evaluating vulnerability detection methods and for training humans and AI. However, our study reveals that LLMs threaten their validity. Instead of genuine security reasoning, detectors exploit a diff-style syntactic comparison, achieving an 83% detection rate, undermining fair evaluation. To mitigate this, we propose the first LLM-oriented, semantics-preserving obfuscation framework for these benchmarks. Unlike IP-protection approaches, it applies human-readable transformations and controlled diff-noise while preserving functionality. On HackTheSilicon, the framework reduces LLM-based detection accuracy by 50% with only 10% obfuscation and by 78.6% under complete obfuscation, restoring benchmark reliability.

---


### 13. [Let Them Steal: Trapping Large Language Model Extraction Attacks with Knowledge Honeypot](https://arxiv.org/abs/2606.15810)

**<font color=#1a73e8>作者：</font>** Yuyang Dai, Yushun Dong  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models deployed as commercial APIs are vulnerable to model extraction attacks, while existing defenses either act too late or degrade utility for legitimate users. We propose \textbf{Knowledge Trap}, a defense that redirects extraction attacks toward low-transferability knowledge through a \emph{Honeypot Knowledge Graph} (HKG) and breadcrumb-guided exploration. Instead of blocking queries or perturbing outputs, Knowledge Trap consumes the attacker's limited query budget on knowledge with negligible downstream utility while preserving benign-user performance. Experiments in medical and financial domains show that Knowledge Trap reduces surrogate Agreement by 6.2\% on average without degrading legitimate-user accuracy, outperforming existing defenses that impose measurable user impact. These results suggest that defending knowledge-space traversal is a practical direction for mitigating LLM extraction attacks.

---


### 14. [SkillVetBench: LLM-as-Judge for Multi-Dimensional Security Risk Evaluation in Open-Source LLM Agent Skills](https://arxiv.org/abs/2606.15899)

**<font color=#1a73e8>作者：</font>** Ismail Hossain, Sai Puppala, Md Jahangir Alam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-source LLM agent ecosystems are growing rapidly, yet the security of community-contributed skills - modular tool definitions that extend agent capabilities - remains largely unvetted. The gap we fill: existing scanners operate at the code layer and are structurally blind to instruction-layer and multi-agent risk - natural-language directives that hijack an agent, exfiltrate data through encoded side channels, or chain harm across pipelines - so what is needed is a semantic, multi-dimensional vetting system rather than another signature matcher. We present SKILLVETBENCH, a live public leaderboard on Hugging Face that uses an LLM-as-Judge to vet agent skills. What is new: SARS (Skill Agentic Risk Score), a five-dimensional agentic-risk metric with a principled weighted formula for instruction-following systems. What is integrated: full CVSS v4.0 vector decomposition and a ClawHub dual-view that places our LLM-generated review beside the official marketplace verdict. What is demonstrated: drawing on our companion benchmark paper [ 1], the LLM-as-Judge stage achieves zero false negatives across 78 confirmed-malicious skills and zero false positives across 22 benign controls, while the best static baseline (SKILLSIEVE) still misses 15%; for instruction-layer categories such as Prompt Injection and Memory Poisoning, conventional tools miss between 89% and 100% of threats (e.g., CODEBERT detects none of nine memory-poisoning skills). Detection rates vary from 35% to 95% across four LLM evaluators, motivating ensemble scoring in production deployments.

---


### 15. [Your "Pro" LLM Subscription May Actually Be "Free": Exposing Fingerprint Spoofing Risks in LLM Inference Services](https://arxiv.org/abs/2606.16100)

**<font color=#1a73e8>作者：</font>** Jiahao Zhang, Xiuyu Li, Suhang Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As Large Language Model (LLM) APIs become ubiquitous, users increasingly rely on black-box fingerprinting to verify that providers are serving the advertised premium models. However, these methods may overlook adversarial providers who manipulate model weights to cheat the fingerprint process. We introduce a novel threat termed fingerprint spoofing, where a malicious provider stealthily serves a weaker model that has been parameter-efficiently fine-tuned to mimic a stronger model, thereby evading user-side fingerprinting. We first formally prove that user-side resource constraints (i.e., finite query budgets and weak fingerprinting classifiers) make current fingerprinting vulnerable to fingerprint spoofing. Guided by this theoretical analysis, we propose GhostPrint, a cost-effective attack framework leveraging surrogate modeling, reward-ranked fine-tuning, and knowledge distillation. Extensive evaluations in both static and continual fingerprinting settings demonstrate that GhostPrint allows weak models to consistently bypass representative fingerprint methods while maintaining utility at a low fine-tuning cost, exposing a critical vulnerability in current LLM fingerprinting pipelines.

---


### 16. [SPARK: Security Knowledge Priming and Representation-Guided Knowledge Activation for LLM-based Secure Code Generation](https://arxiv.org/abs/2606.16244)

**<font color=#1a73e8>作者：</font>** Xiaoyun Xu, Lichao Wu, Jona te Lintelo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models routinely generate code with exploitable security flaws. Prior literature attributes this limitation to a lack of security expertise, steering current defense mechanisms toward heavy fine-tuning or external knowledge retrieval, which introduces significant computational overhead and data bias through redundant code examples. Contrary to this view, we argue that pretraining corpora are already rich in security material. The bottleneck is activation: without an explicit and brief cue, statistical pressure toward common training-distribution patterns suppresses the model's safety-relevant representations. We present SPARK, an inference-time security harness that activates this latent knowledge without any retraining. The harness has two parts. Component~I retrieves a few of the relevant Common Weakness Enumeration (CWE) entries for each coding task and appends a short structured cue to the prompt; this alone is enough to surface the model's existing security representations. Component~II adds a precomputed token bias to the logits at every decoding step. We obtain the bias by projecting a safe-direction vector, the unit difference between the mean safe and mean unsafe last-layer hidden states, through the language model head. The bias is computed once offline; applying it costs a single vector addition per generated token. We evaluate SPARK on 9 open-source models across C++, Java, and Python, and compare with 7 baselines spanning fine-tuning and retrieval-augmented methods. SPARK matches or improves on the best baseline in every setting while preserving HumanEval utility. We further test Component~I in a black-box setting on 7 of today's strongest models, including Claude, DeepSeek, and GPT, demonstrating the bottleneck of insecure code generation and the improvements enabled by our method.

---


### 17. [Dynamic Malicious Skills in Agentic AI](https://arxiv.org/abs/2606.16287)

**<font color=#1a73e8>作者：</font>** Tianhao Chen, Zhengyuan Jiang, Yuepeng Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Skills are a key enabling component of agentic AI. While they enhance agents' capabilities, they also introduce new attack surfaces. In this work, we investigate one such attack surface by demonstrating dynamic malicious skills. By embedding malicious instructions in natural-language documentation (e.g., this http URL), an attacker can induce an agent to dynamically inject malicious logic into an otherwise benign skill during execution. We evaluate this attack across agentic frameworks such as OpenHands and Claude Code, showing that dynamic malicious skills can successfully introduce a range of malicious behaviors at runtime with non-trivial success rates. To mitigate this vulnerability, we propose a system-level defense that prevents dynamic modification of skills using operating system kernel-enforced read-only mounts. Our evaluation demonstrates that this defense effectively blocks dynamic malicious skills while preserving the functionality of benign skills.

---


### 18. [From Refusal Geometry to Safety Geometry: Harmfulness--Refusal Coupling under Dynamic Adversarial Fine-Tuning](https://arxiv.org/abs/2606.16349)

**<font color=#1a73e8>作者：</font>** Wenhao Lan, Shan Li, Xinhua Lai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety alignment requires language models to refuse harmful requests without losing the ability to answer benign ones. Existing robustness evaluations, however, do not reveal whether a model has learned to recognize harmfulness, to activate a refusal policy, or to couple these two processes. We study this question with a dual safety-geometry protocol that measures harmfulness carriers, refusal carriers, and their coupling across aligned instruction-tuned anchors and matched Mistral-7B-v0.1 SFT/R2D2 training trajectories. The aligned anchors validate the protocol: refusal-side interventions reopen attack success more strongly than harmfulness-only interventions, while harmfulness and refusal carriers remain nearly orthogonal. Along the Mistral trajectory, R2D2 exhibits a high-coupling early phase with strong fixed-source robustness, saturated safe-prompt refusal, and collapsed benign utility. Later checkpoints move to a lower-coupling regime with partial utility recovery and reopened attack success. SFT provides an important contrast: it also reaches low coupling, but remains substantially less robust, showing that low coupling alone is not a safety guarantee. All-anchor diagnostics and sparse GCG/AutoDAN transfer experiments further show that H/R coupling is informative in the R2D2 regime, whereas SFT transfer is better summarized by drift or behavior-state measures. Causal sweeps support fixed-protocol sensitivity relative to matched unit-direction controls, but do not establish independent harmfulness and refusal pathways. These results frame harmfulness--refusal coupling as an operational diagnostic for safety-geometry dynamics under adversarial fine-tuning.

---


### 19. [The Proxy Knows Too Much: Sealing LLM API Routers with Attested TEEs](https://arxiv.org/abs/2606.16358)

**<font color=#1a73e8>作者：</font>** Sipeng Xie, Qianhong Wu, Hengrun Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agents increasingly access large language models (LLMs) through API routers. A router terminates the client's transport-layer security session and opens a separate upstream session, so it holds the full interaction in plaintext. This makes the router an application-layer man-in-the-middle: it can rewrite agent tool calls, swap dependencies for typosquatted packages, trigger attacks only under audit-evading conditions, and passively exfiltrate secrets. Existing client-side defenses are evadable.
We propose AEGIS, a provider-transparent attested API router whose data path is a client-verified faithful passthrough. AEGISconfines plaintext handling to a small hardware-enclave component while leaving authentication, scheduling, accounting, and management on the untrusted host. The client verifies the enclave before releasing plaintext. The host can neither read nor alter the interaction, and plaintext leaves only toward destinations fixed by the measured image. We show that all four malicious-router attack classes succeed against a plaintext-access baseline and are blocked by AEGIS, including adaptive tests against the same boundary. The trusted path is $851$ lines, carries three provider-native APIs without conversion, and completes every request under real-provider workload and concurrency. In a seeded audit pilot, two commodity coding agents find eight and ten of ten planted invariant violations. The local relay overhead is about six milliseconds per request.

---


### 20. [FEnc$^2$: Unifying Data Packing for Efficient Private Inference via Convolution and Architecture-Aware Fragment Encoding](https://arxiv.org/abs/2606.16359)

**<font color=#1a73e8>作者：</font>** Ran Ran, Zhaoting Gong, Nuo Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully Homomorphic Encryption (FHE) enables privacy-preserving machine learning but incurs extreme computational and memory overhead. These costs come not only from expensive low-level primitives, including Number Theoretic Transform (NTT), rotation, and key-switching, but also from inefficient ciphertext packing at the application level. Existing packing strategies typically preserve either neighboring data elements or feature grouping, but not both, leading to wasted ciphertext slots, excessive rotations, and inflated ciphertext counts. We propose FEnc2, a unified and principled fragment-based encoding framework for CKKS-based private convolutional neural network inference. FEnc2 optimizes slot utilization, rotation complexity, and ciphertext density through two components: 1)Conv-aware Encoding, which analytically selects an optimal fragment size to decouple spatial dependencies and jointly minimize inner-outer rotations across layers, and 2)Arch-aware Ct Compression, which restores ciphertext density after feature- or channel-reduction layers. Together, these transformations reshape encrypted workload structure and reduce homomorphic operations by one to two orders of magnitude. With full memory capacity utilized, i.e., at maximum batch size, FEnc2 achieves end-to-end latency speedups over the state-of-the-art Orion of up to 228.83x on GPU and 226.06x on CPU for LeNet on MNIST, and up to 4.55x on GPU and 9.43x on CPU for MobileNet on ImageNet. FEnc2 is hardware-agnostic yet architecturally transformative: by optimizing encrypted tensor layout before execution, it reduces ciphertext count and workload pressure on hardware, complementing primitive-level optimizations such as NTT and keyswitch accelerators. These results show that application-level data layout is a first-order architectural design dimension for encrypted inference and an important enabler for next-generation FHE systems.

---


### 21. [Transferable Self-Evolving Playbooks for Agentic Security Auditing](https://arxiv.org/abs/2606.16420)

**<font color=#1a73e8>作者：</font>** Ziyue Wang, Cheuk Wang Maurice Ng, Chenchen Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An LLM agent for vulnerability discovery and validation is more than a model. It combines three components: an LLM for code analysis, an agent harness such as Codex or OpenCode for navigation, tool use, and execution, and an audit playbook, domain-specific procedural knowledge that guides the LLM and harness toward vulnerability discovery. Prior work relies on human-supplied playbooks, including prompt engineering, manual workflows, knowledge bases, and heuristics. This raises two research questions: Acquisition - is human curation necessary, and can playbook creation be automated? Transfer - can an evolved playbook transfer the audit procedure to weaker agents, improving their capability?
We present EvoHunt, a playbook evolution environment over open-source repositories for security auditing. Three agents drive the evolution loop: an audit agent rolls out the current playbook and produces findings; an evaluator scores outcomes against ground truth; and a reviser commits updates to the playbook based on failure analysis. The playbook format is unconstrained: starting empty, EvoHunt adds or removes workflows, heuristics, vulnerability knowledge, or domain-specific content. The evolved playbook requires only minor adaptation to run under a different LLM or harness.
We evaluate EvoHunt on open-source security advisories. For acquisition, playbook evolution raises end-to-end exploits for Codex/GPT5.4-xhigh 6x, from 1.1% to 6.2%, and the evolved OpenCode/GLM5.1 playbook surpasses OpenAI Codex Security on every metric, with 11.3% vs. 9.2% target-match rate, showing open-source evolution can outperform a dedicated commercial product. For transfer, the GLM-evolved playbook gives the strongest student lift: Qwen3.6-27B improves from 2.4% to 6.5%, Qwen3.6-35B-A3B from 1.1% to 4.6%, and A3B obtains 2.4x more matches than GPT transfer.

---


### 22. [DoubtProbe: Black-Box Jailbreak Defense via Structural Verification and Semantic Auditing](https://arxiv.org/abs/2606.16527)

**<font color=#1a73e8>作者：</font>** Xuanyu Yin, Yilin Jiang, Jun Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly deployed in user-facing systems, black-box jailbreak defense has become an important practical problem. Existing defenses often rely on known-attack coverage, prompt-level semantic judgment, or local runtime control, yet these paths can become unstable under evolving prompt packaging, expression rewriting, and structure manipulation. We observe that many black-box jailbreaks do not remove the harmful goal, but reorganize the information needed to express and execute it, thereby evading safety alignment while remaining recoverable during generation. Motivated by this observation, we propose DoubtProbe, a dual-branch inference-time defense framework that combines structural verification with semantic auditing and formulates black-box jailbreak defense as consistency checking under controlled transformation. The structural branch extracts a structured representation from the original request, reconstructs the request under representation constraints, and detects information-preservation failures between the original and reconstructed requests; the semantic branch audits the original prompt directly. We evaluate DoubtProbe against representative black-box defenses on jailbreak and benign-request benchmarks, and further test backbone transfer from Qwen2.5-72B to Llama-3.1-70B. Results show that DoubtProbe achieves a stronger and more stable defense-utility trade-off: on Qwen2.5-72B, it reduces the JBB attack success rate from 0.293 to 0.100 and the CodeAttack attack success rate from 0.152 to 0.001, while maintaining false positive rates of 0.022 and 0.016 on AlpacaEval and OR-Bench; the same pattern remains stable on Llama-3.1-70B. These findings show that structural inconsistency signals provide a practical and generalizable basis for black-box jailbreak defense, especially when combined with semantic auditing.

---


### 23. [Automated jailbreak attack targeting multiple defense strategies](https://arxiv.org/abs/2606.16751)

**<font color=#1a73e8>作者：</font>** Qi Wang, Chengcheng Wan, Weijia He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated remarkable capabilities across a wide range of tasks. However, their safety remains a critical concern due to their susceptibility to adversarial prompt-based attacks. In this paper, we present UNIATTACK, an adversarial testing framework designed from a defense-oriented perspective to systematically construct effective black-box attack prompts. Unlike prior approaches that rely on static templates or iterative model-specific tuning, UNIATTACK extracts minimal but high-impact attack features from diverse existing attacks, optimizes them via a specialized attacker LLM, and composes them into flexible templates through automated refinement process. This feature-centric construction enables one-shot attacks that generalize across multiple models and safety categories, providing a practical tool for assessing LLM robustness. Our evaluation results shows that compared to the baselines, UNIATTACK achieves an average attack success rate (ASR) improvement of 64.63\%-248.82\% on models deployed with multi-layered defense mechanisms and it only takes 0.03\%-4.96\% cost of the baselines. UNIATTACK artifact is available at this https URL.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
