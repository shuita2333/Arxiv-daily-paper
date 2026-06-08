# 🔐 大模型安全相关研究 | 2026年06月09日

> 本类共 **7** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Subtle Injection for Ground-truth Inference of LLM Training Data](https://arxiv.org/abs/2606.06502)

**<font color=#1a73e8>作者：</font>** Abraham Itzhak Weinberg  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly trained on scraped web corpora without authorisation, content owners require forensic methods to prove that their documents were included in a model's training set. We propose \textbf{SIGIL} (\textbf{S}ubtle \textbf{I}njection for \textbf{G}round-truth \textbf{I}nference of \textbf{L}LM training data), a framework that embeds imperceptible \emph{canary sequences} into protected text and code such that any LLM trained on those documents exhibits statistically detectable behavioural signatures when probed with targeted queries.
SIGIL defines five canary strategies -- lexical-rare, lexical-phrase, syntactic, semantic, and code-pattern -- and a \emph{Membership Inference Score} (MIS) grounded in the Neyman-Pearson hypothesis testing framework with formal false-positive rate (FPR) control. Simulator parameters are calibrated against the empirical membership inference literature, yielding realistic heterogeneous results across $36{,}000$ trials: overall AUC $= 0.892$, rising from $0.831$ at $0.1\%$ injection to $0.947$ at $10\%$. Detection rates range from $33\%$ to $78\%$ across model-size and injection-rate conditions. Code Pattern canaries achieve the highest AUC ($0.903$, Cohen's $d = 1.84$); Syntactic Structure the lowest ($0.875$, $d = 1.63$). All four experimental factors -- injection rate, model size, canary strategy, and mixture ratio -- have significant independent effects on MIS ($p < 0.001$). SIGIL maintains AUC $> 0.86$ even under $100\%$ paraphrasing ($\text{AUC} = 0.864$), confirming robustness through semantic leakage that survives surface-level rewriting.

---


### 2. [What Your Posts Reveal: A Benchmark and Agentic Framework for User-Level Privacy Leakage on Social Media](https://arxiv.org/abs/2606.06784)

**<font color=#1a73e8>作者：</font>** Zifan Peng, Yini Huang, Aiwen Lu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Public social media posts can reveal private information through weak cues scattered across text, images, or metadata. Such leakage is often cumulative and cross-post: cues that appear harmless in isolation may jointly expose a user's home, workplace, or routine. However, current research lacks a unified benchmark for user-level multimodal privacy leakage and an evaluation metric that captures exposure severity beyond binary accuracy.
To address these gaps, we propose SopriBench, a synthetic benchmark guided by leakage patterns abstracted from a private reference corpus of Rednote and Instagram accounts, covering 50 user profiles and 1,569 images with attributes, contextual sensitivity, granularity, leakage type, inference difficulty, and supporting evidence. We further introduce the Privacy Exposure Score (PES), which weights value granularity by contextual sensitivity. Inspired by abductive reasoning, we introduce Argus, a training-free agentic framework for cumulative leakage inference. Argus forms hypotheses from accumulated evidence, verifies supporting evidence, and aggregates cross-post cues into privacy profiles, achieving 0.55 PES, a 25% improvement over the strongest baseline, with the largest gain on cross-post leakage.

---


### 3. [DPAgent-in-the-Middle: Agentic Defense and Repair Against AI-Groomed Deceptive Patterns](https://arxiv.org/abs/2606.06914)

**<font color=#1a73e8>作者：</font>** Zewei Shi, Ruoxi Sun, Haoyang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy deceptive patterns in web interfaces systematically manipulate users into disclosing personal data, yet existing defenses are fragmented, static, and increasingly vulnerable to manipulation by large language models. Moreover, data voids, areas of information scarcity within the web ecosystem, create fertile ground for adversaries to inject misleading content that can be scraped and learned by AI systems, thereby amplifying both deceptive design and model misbehavior. In this paper, we formalize a new threat model, AI grooming, where attackers exploit data voids to seed benign-looking but malicious samples that corrupt model reasoning and normalize deceptive practices. To address this threat in privacy deceptive patterns, we present DPAgent, an agentic and reasoning-aware framework that orchestrates four specialized agents to mitigate the AI Grooming threat via a proactive defense that combines latent space purification with defensive prompting and operates directly in live web environments to proactively explore, detect, and repair privacy deceptive user interfaces before they reach end users. Extensive evaluations show that DPAgent detects 90.98% of groomed samples, achieves state-of-the-art privacy deceptive pattern detection with a micro F1 of 0.816, explores over 80% of pattern types while visiting only about 10% of the pages required by baselines, and successfully repairs 77% of detected deceptive interfaces. A large-scale study of 485 websites in the wild reveals that up to 98% contain at least one privacy deceptive pattern, over 90% of which can be mitigated by DPAgent. User studies further confirm that DPAgent effectively reduces privacy risks while preserving browsing experience. Our results demonstrate the promise of agent-in-the-middle defenses for securing the web UI supply chain against deceptive design and emerging AI threats rooted in data void exploitation.

---


### 4. [MalSkillBench: A Runtime-Verified Benchmark of Malicious Agent Skills](https://arxiv.org/abs/2606.07131)

**<font color=#1a73e8>作者：</font>** Wenbo Guo, Wei Zeng, Chengwei Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI coding agents such as Claude Code and Gemini CLI increasingly extend themselves with third-party skills: markdown packages bundling natural-language instructions, executable scripts, and tool permissions. Because a skill is at once code and agent-facing instruction, it introduces a supply chain dependency whose risk is neither pure code nor pure prompt. Detection tools have never been measured against verified ground truth spanning this hybrid space, leaving their effectiveness unknown and wild-only evaluations biased.
We present MalSkillBench, the first runtime-verified benchmark of malicious agent skills: 3,944 malicious skills labeled along a three-dimensional taxonomy of 108 cells. Of these, 3,214 come from a closed-loop Generate-Verify-Feedback pipeline admitting only samples whose malicious behavior fires inside a Docker sandbox under system-call monitoring and an LLM judge; we add 703 in-the-wild and 4,000 matched benign skills. Our measurements are consistent: code injection reaches 94.5% verification yield but prompt injection only 75.8%, the same fragility that later makes it hard to detect; the wild sample is narrow, dominated by one cryptocurrency-theft campaign (86.6% one behavior, 81% from two accounts) with a small but architecturally new tail attacking the agent control plane; the strongest skill-specific detector reaches 98.4% recall on code injection yet collapses on prompt-injection and agent-control attacks, and wild-only scoring swings the ranking by up to 66 recall points; supply-chain scanners and prompt-injection defenses each see only half of a skill, and no combination recovers the code-instruction relationship. Detecting malicious skills therefore requires reasoning jointly over task intent, code, and instructions. We release the dataset, pipeline, baselines, and results.

---


### 5. [Authorized and Verifiable Searchable Encryption Based on Public Key Equality Test for Cloud Storage](https://arxiv.org/abs/2606.07319)

**<font color=#1a73e8>作者：</font>** Xiuping Li, Kaiwen Wang, Xiaolin Chang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud storage revolutionizes data management but raises conflicts between functionality and privacy. Public Key Encryption with Equality Test (PKEET), an advanced cryptographic technique, can enable multi-user searchable encryption (SE) through cross-key ciphertext comparison without shared keys. However, existing PKEET-based SE schemes lack ciphertext-file-level authorization, public verifiability, or SE-level support. This paper first proposes a novel PKEET scheme, AVPKEET (Authorized and Verifiable PKEET). It enables non-transferable and non-replayable authorization of ciphertext files, while supporting public verifiability, all without the need for trusted third parties. Then we propose an AVPKEET-based SE scheme, denoted as AVSE (Authorized and Verifiable SE), featuring one-time non-transferable tokens bound to users and nonces, batch operations, and fine-grained access control (ALL, PARTIAL, SINGLE). We prove OW-CCA2 security, token unforgeability, and verification soundness under standard assumptions. Experiment results demonstrate that AVSE achieves the most compact token size (168 bytes) while uniquely providing both ciphertext-file-level authorization and public verification, with acceptable overhead for cloud storage deployment.

---


### 6. [Defending Jailbreak Attacks on Large Language Models via Manifold Trajectory Kinetics](https://arxiv.org/abs/2606.07335)

**<font color=#1a73e8>作者：</font>** Hangtao Zhang, Yucheng Zhao, Sishun Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Jailbreak prompts can bypass alignment guardrails in large language models (LLMs) and elicit unsafe outputs, making reliable deployment-time detection critical. Prior detection approaches largely rely on a fixed metric space, e.g., raw inputs, gradients, or hidden features, in which benign and jailbreak prompts are linearly separable. We show this assumption breaks under (i) pseudo-malicious prompts that are benign by intent but contain safety-related keywords, and (ii) adaptive attacks that explicitly optimize against the deployed detector. To overcome this limitation, we shift our focus from identifying a universal metric space to analyzing the more robust neighborhood structure of the underlying data manifold. We present Manifold Trajectory Kinetics (MTK), which treats an LLM as a kinetic system transforming inputs into outputs and detects jailbreaks by tracking how a prompt's neighborhood structure evolves across layers. Benign prompts remain close to benign neighborhoods throughout inference, whereas jailbreak prompts exhibit a characteristic trajectory that begins near malicious seeds and later strategically shifts toward benign neighborhoods to evade this http URL four LLMs and ten jailbreak attacks, MTK achieves strong robustness to both failure modes: on pseudo-malicious prompts, it attains a jailbreak true positive rate of 95% at a false positive rate of 5% on benign prompts and 2% on pseudo-malicious prompts, and under adaptive attacks, it maintains a true positive rate of 85%. We further demonstrate the superior performance of MTK for jailbreak detection in vision-language models. Our code is available at this https URL.

---


### 7. [Empirical Evaluation of Large Language Models for Migration of Code Fragments to Post-Quantum Cryptography](https://arxiv.org/abs/2606.07341)

**<font color=#1a73e8>作者：</font>** Javier Pallarés de Bonrostro, Ana I. González-Tablas, María Isabel González Vasco  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The transition to post-quantum cryptography (PQC) requires not only replacing vulnerable cryptographic primitives, but also refactoring the surrounding software logic. While existing PQC migration frameworks provide organizational guidance, practical code-level remediation remains largely manual and error-prone. This paper evaluates whether large language models (LLMs) can be trained to assist in the migration of pre-quantum cryptographic code fragments to post-quantum counterparts while preserving functional correctness. To this end, we introduce a reproducible experimental framework built around a synthetic dataset of 800 paired Python code fragments covering six cryptographic families and combined multi-primitive cases. Each pair is validated through category-specific functional tests, enabling both dataset quality control and objective evaluation of model-generated migrations. Four models are assessed: GPT-4.1 in a zero-shot setting, and fine-tuned versions of GPT-3.5-turbo, GPT-4.1-mini, and CodeLlama-7B-Instruct. The results show that domain-specific fine-tuning is essential for reliable cryptographic migration. The fine-tuned GPT-4.1-mini model achieves the best overall performance, with a mean static similarity of 0.9072 and a dynamic functional correctness rate of 92.5%, substantially outperforming the zero-shot baseline. A complementary validation on six open-source repositories further shows that the approach can produce useful migrations in localized cryptographic modules, while also revealing limitations in larger projects with complex dependencies and cross-module interactions. These findings suggest that fine-tuned LLMs can serve as practical components in future crypto-agile migration pipelines, provided they are coupled with automated verification and dependency-aware validation.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
