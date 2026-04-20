# 🔐 大模型安全相关研究 | 2026年04月21日

> 本类共 **11** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [SoK: Security of Autonomous LLM Agents in Agentic Commerce](https://arxiv.org/abs/2604.15367)

**<font color=#1a73e8>作者：</font>** Qian'ang Mao, Jiaxin Wang, Ya Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous large language model (LLM) agents such as OpenClaw are pushing agentic commerce from human-supervised assistance toward machine actors that can negotiate, purchase services, manage digital assets, and execute transactions across on-chain and off-chain environments. Protocols such as the Trustless Agents standard (ERC-8004), Agent Payments Protocol (AP2), the HTTP 402-based payment protocol (x402), Agent Commerce Protocol (ACP), the Agentic Commerce standard (ERC-8183), and Machine Payments Protocol (MPP) enable this transition, but they also create an attack surface that existing security frameworks do not capture well. This Systematization of Knowledge (SoK) develops a unified security framework for autonomous LLM agents in commerce and finance. We organize threats along five dimensions: agent integrity, transaction authorization, inter-agent trust, market manipulation, and regulatory compliance. From a systematically curated public corpus of academic papers, protocol documents, industry reports, and incident evidence, we derive 12 cross-layer attack vectors and show how failures propagate from reasoning and tooling layers into custody, settlement, market harm, and compliance exposure. We then propose a layered defense architecture addressing authorization gaps left by current agent-payment protocols. Overall, our analysis shows that securing agentic commerce is inherently a cross-layer problem that requires coordinated controls across LLM safety, protocol design, identity, market structure, and regulation. We conclude with a research roadmap and a benchmark agenda for secure autonomous commerce.

---


### 2. [LogJack: Indirect Prompt Injection Through Cloud Logs Against LLM Debugging Agents](https://arxiv.org/abs/2604.15368)

**<font color=#1a73e8>作者：</font>** Harsh Shah  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM debugging agents that consume cloud logs and execute remediation commands are vulnerable to indirect prompt injection through log content. We present LogJack, a benchmark of 42 payloads across 5 cloud log categories, and evaluate 8 foundation models under 3 prompt conditions with 5 independent trials each (n = 160 per model per condition on 32 attack payloads). Under the active condition, verbatim command execution rates range from 0% (Claude Sonnet 4.6) to 86.2% (Llama 3.3 70B). Passive instructions ("do not execute fixes") reduce most models to 0% but Llama still executes at 30.0%. Remote code execution via curl | bash succeeds on 6 of 8 models. Guardrails from AWS, GCP, and Azure largely fail to detect log-embedded injections-Azure Prompt Shield detected only the most obvious payload (1/32), while GCP Model Armor detected none-though they detect identical payloads in isolation. We also observe a novel "sanitize and execute" behavior where a model detects and removes an obvious malicious component but still executes the remaining injected command. Benchmark and harness available at this http URL.

---


### 3. [An Agentic Workflow for Detecting Personally Identifiable Information in Crash Narratives](https://arxiv.org/abs/2604.15369)

**<font color=#1a73e8>作者：</font>** Junyi Ma, Pei Li, Rui Gan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Crash narratives in crash reports provide crucial contextual information for traffic safety analysis. Yet, their broader use is hindered by the presence of personally identifiable information (PII), including names, home addresses, and license plate numbers. Because PII appears sparsely and inconsistently in crash narratives, manual detection is not scalable, and existing rule-based approaches often fail to capture context-dependent PII. This study develops and evaluates a locally deployable, agentic workflow for PII detection in crash narratives by leveraging large language models (LLMs). The workflow contains a Hybrid Extractor and a Verifier. The Hybrid Extractor routes structured PII (e.g., phone numbers and email addresses) to a rule-based model (i.e., Presidio) and context-dependent PII (e.g., names, home addresses, and alphanumeric identifiers) to a domain-adapted, fine-tuned LLM. To address ambiguity in challenging categories, the workflow incorporates ensemble LLM extraction and an agentic verification step that filters false detections through evidence-based reasoning. Evaluated on a real-world crash dataset, the agentic workflow achieves strong performance with a precision of 0.82, a recall of 0.94, an F1 of 0.87, and an accuracy of 0.96, outperforming multiple baseline methods. Moreover, the ablation results suggest that ensemble LLM extraction and Verifier offer improved detection for home addresses and alphanumeric identifiers. The workflow runs locally, supporting privacy-sensitive operational settings where external APIs are restricted. This work offers a practical and robust path for scalable, privacy-preserving crash data processing, enabling broader research and safety interventions while safeguarding individual privacy.

---


### 4. [The Synthetic Media Shift: Tracking the Rise, Virality, and Detectability of AI-Generated Multimodal Misinformation](https://arxiv.org/abs/2604.15372)

**<font color=#1a73e8>作者：</font>** Zacharias Chrysidis, Stefanos-Iordanis Papadopoulos, Symeon Papadopoulos  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As generative AI advances, the distinction between authentic and synthetic media is increasingly blurred, challenging the integrity of online information. In this study, we present CONVEX, a large-scale dataset of multimodal misinformation involving miscaptioned, edited, and AI-generated visual content, comprising over 150K multimodal posts with associated notes and engagement metrics from X's Community Notes. We analyze how multimodal misinformation evolves in terms of virality, engagement, and consensus dynamics, with a focus on synthetic media. Our results show that while AI-generated content achieves disproportionate virality, its spread is driven primarily by passive engagement rather than active discourse. Despite slower initial reporting, AI-generated content reaches community consensus more quickly once flagged. Moreover, our evaluation of specialized detectors and vision-language models reveals a consistent decline in performance over time in distinguishing synthetic from authentic images as generative models evolve. These findings highlight the need for continuous monitoring and adaptive strategies in the rapidly evolving digital information environment.

---


### 5. [HarmfulSkillBench: How Do Harmful Skills Weaponize Your Agents?](https://arxiv.org/abs/2604.15415)

**<font color=#1a73e8>作者：</font>** Yukun Jiang, Yage Zhang, Michael Backes 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have evolved into autonomous agents that rely on open skill ecosystems (e.g., ClawHub and this http URL), hosting numerous publicly reusable skills. Existing security research on these ecosystems mainly focuses on vulnerabilities within skills, such as prompt injection. However, there is a critical gap regarding skills that may be misused for harmful actions (e.g., cyber attacks, fraud and scams, privacy violations, and sexual content generation), namely harmful skills. In this paper, we present the first large-scale measurement study of harmful skills in agent ecosystems, covering 98,440 skills across two major registries. Using an LLM-driven scoring system grounded in our harmful skill taxonomy, we find that 4.93% of skills (4,858) are harmful, with ClawHub exhibiting an 8.84% harmful rate compared to 3.49% on this http URL. We then construct HarmfulSkillBench, the first benchmark for evaluating agent safety against harmful skills in realistic agent contexts, comprising 200 harmful skills across 20 categories and four evaluation conditions. By evaluating six LLMs on HarmfulSkillBench, we find that presenting a harmful task through a pre-installed skill substantially lowers refusal rates across all models, with the average harm score rising from 0.27 without the skill to 0.47 with it, and further to 0.76 when the harmful intent is implicit rather than stated as an explicit user request. We responsibly disclose our findings to the affected registries and release our benchmark to support future research (see this https URL).

---


### 6. [Into the Gray Zone: Domain Contexts Can Blur LLM Safety Boundaries](https://arxiv.org/abs/2604.15717)

**<font color=#1a73e8>作者：</font>** Ki Sen Hung, Xi Yang, Chang Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A central goal of LLM alignment is to balance helpfulness with harmlessness, yet these objectives conflict when the same knowledge serves both legitimate and malicious purposes. This tension is amplified by context-sensitive alignment: we observe that domain-specific contexts (e.g., chemistry) selectively relax defenses for domain-relevant harmful knowledge, while safety-research contexts (e.g., jailbreak studies) trigger broader relaxation spanning all harm categories. To systematically exploit this vulnerability, we propose Jargon, a framework combining safety-research contexts with multi-turn adversarial interactions that achieves attack success rates exceeding 93% across seven frontier models, including GPT-5.2, Claude-4.5, and Gemini-3, substantially outperforming existing methods. Activation space analysis reveals that Jargon queries occupy an intermediate region between benign and harmful inputs, a gray zone where refusal decisions become unreliable. To mitigate this vulnerability, we design a policy-guided safeguard that steers models toward helpful yet harmless responses, and internalize this capability through alignment fine-tuning, reducing attack success rates while preserving helpfulness.

---


### 7. [Privacy-Preserving LLMs Routing](https://arxiv.org/abs/2604.15728)

**<font color=#1a73e8>作者：</font>** Xidong Wu, Yukuan Zhang, Yuqiong Ji 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) routing has emerged as a critical strategy to balance model performance and cost-efficiency by dynamically selecting services from various model providers. However, LLM routing adds an intermediate layer between users and LLMs, creating new privacy risks to user data. These privacy risks have not been systematically studied. Although cryptographic techniques such as Secure Multi-Party Computation (MPC) enable privacy-preserving computation, their protocol design and implementation remain under-explored, and naïve implementations typically incur prohibitive computational overhead. To address this, we propose a privacy-preserving LLM routing framework (PPRoute). PPRoute includes multiple strategies to speed up encoder inference and nearest neighbor search under the MPC and maintain the quality of LLM routing. First, PPRoute uses MPC-friendly operations to boost the encoder inference. Second, PPRoute uses a multiple-step model training algorithm to maintain routing quality despite the constraints of the encrypted domain. Third, PPRoute proposes an unsorted Top-k algorithm with $O(1)$ communication complexity for secure sorting in model search, significantly reducing communication latency. Across different datasets, PPRoute achieves the performance of plaintext counterparts, while achieving approximately a 20$\times$ speedup over naïve MPC implementations.

---


### 8. [A Case Study on the Impact of Anonymization Along the RAG Pipeline](https://arxiv.org/abs/2604.15958)

**<font color=#1a73e8>作者：</font>** Andreea-Elena Bodea, Stephen Meisenbacher, Florian Matthes  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite the considerable promise of Retrieval-Augmented Generation (RAG), many real-world use cases may create privacy concerns, where the purported utility of RAG-enabled insights comes at the risk of exposing private information to either the LLM or the end user requesting the response. As a potential mitigation, using anonymization techniques to remove personally identifiable information (PII) and other sensitive markers in the underlying data represents a practical and sensible course of action for RAG administrators. Despite a wealth of literature on the topic, no works consider the placement of anonymization along the RAG pipeline, i.e., asking the question, where should anonymization happen? In this case study, we systematically and empirically measure the impact of anonymization at two important points along the RAG pipeline: the dataset and generated answer. We show that differences in privacy-utility trade-offs can be observed depending on where anonymization took place, demonstrating the significance of privacy risk mitigation placement in RAG.

---


### 9. [Where Does MEV Really Come From? Revisiting CEXDEX Arbitrage on Ethereum](https://arxiv.org/abs/2604.15973)

**<font color=#1a73e8>作者：</font>** Bence Ladóczk, Miklós Rásonyi, János Tapolcai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A central question of the Ethereum ecosystem is where Maximal Extractable Value (MEV)revenue originates and to what extent it stems from harming unsuspecting users. It is acceptable if MEV arises from arbitrages between centralised and decentralised exchanges (CEX-DEX). Yet theoretical models have significantly underestimated the scale of these arbitrages, while empirical studies have highlighted their importance - though these remain conservative estimates, constrained by numerous debatable heuristic assumptions. Revisiting the theoretical model, we found that CEX-DEX arbitrages require trading volumes on the order of the total activity of major liquidity pools and yield profits comparable to MEV. Most prior AMM models utilised the Black-Scholes (BS) stochastic differential equation (SDE) - i.e., geometric Brownian motion - and assumed continuous price trajectories where asset prices move in small increments this http URL argue that BS underestimates arbitrage profits by ignoring price jumps, which are precisely the points at which arbitrage opportunities tend to arise. To address this gap, we present an extended discrete-time AMM model in which the price process is the sum of a diffusive component and stochastic jumps that can have arbitrary noise distributions. Although mathematically more involved this framework allows us to employ a general discrete-time SDE and compute the stationary probability distribution via function iteration with geometric convergence. We further prove that the resulting mispricing process is an ergodic Markov chain. We implement our model in C++, collect spot prices and AMM exchange data from the Ethereum blockchain and fit the model parameters to the observed prices. The estimates derived from our model closely match empirical observations and provide a natural theoretical explanation for several fundamental questions in the blockchain ecosystem.

---


### 10. [MATRIX: Multi-Layer Code Watermarking via Dual-Channel Constrained Parity-Check Encoding](https://arxiv.org/abs/2604.16001)

**<font color=#1a73e8>作者：</font>** Yuqing Nie, Chong Wang, Guosheng Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Code Large Language Models (Code LLMs) have revolutionized software development but raised critical concerns regarding code provenance, copyright protection, and security. Existing code watermarking approaches suffer from two fundamental limitations: black-box methods either exhibit detectable syntactic patterns vulnerable to statistical analysis or rely on implicit neural embedding behaviors that weaken interpretability, auditability, and precise control, while white-box methods lack code-aware capabilities that may compromise functionality. Moreover, current single-layer watermarking schemes fail to address increasingly complex provenance requirements such as multi-level attribution and version tracking.
We present MATRIX, a novel code watermarking framework that formulates watermark encoding as solving constrained parity-check matrix equations. MATRIX employs dual-channel watermarking through variable naming and semantic-preserving transformations, enhancing watermark coverage across a wider range of code while ensuring mutual backup for robustness. By integrating BCH error-correction codes with solution space diversity, our approach achieves robustness against statistical analysis. Extensive evaluation on Python code generated by multiple Code LLMs demonstrates that MATRIX achieves an average watermark detection accuracy of 99.20% with minimal functionality loss (0-0.14%), improves robustness by 7.70-26.67% against various attacks, and increases watermarking applicability by 2-6x compared with existing methods. These results establish MATRIX as an effective solution for complex code provenance scenarios while balancing among detectability, fidelity, and robustness.

---


### 11. [PolicyGapper: Automated Detection of Inconsistencies Between Google Play Data Safety Sections and Privacy Policies Using LLMs](https://arxiv.org/abs/2604.16128)

**<font color=#1a73e8>作者：</font>** Luca Ferrari, Billel Habbati, Meriem Guerar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mobile application developers are required to disclose how they collect, use, and share user data in compliance with privacy regulations. To support transparency, major app marketplaces have introduced standardized disclosure mechanisms. In 2022, Google mandated the Data Safety Section (DSS) on Google Play, requiring developers to summarize their data practices. However, compiling accurate DSS disclosures is challenging, as they must remain consistent with the corresponding privacy policy (PP), and no automated tool currently verifies this alignment. Prior studies indicate that nearly 80% of popular apps contain incomplete or misleading DSS declarations. We present PolicyGapper, an LLM-based methodology for automatically detecting discrepancies between DSS disclosures and privacy policies. PolicyGapper operates in four stages: scraping, pre-processing, analysis, and post-processing, without requiring access to application binaries. We evaluate PolicyGapper on a dataset of 330 top-ranked apps spanning all 33 Google Play categories, collected in Q3 2025. The approach identifies 2,689 omitted disclosures, including 2,040 related to data collection and 649 to data sharing. Manual validation on a stratified 10% subset, repeated across three independent runs, yields an average Precision of 0.75, Recall of 0.77, Accuracy of 0.69, and F1-score of 0.76. To support reproducibility, we release a complete replication package, including the dataset, prompts, source code, and results available at this https URL and this https URL.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
