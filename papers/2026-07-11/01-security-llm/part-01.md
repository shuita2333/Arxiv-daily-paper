# 🔐 大模型安全相关研究 | 2026年07月11日

> 本类共 **10** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Controllability-Aware Adversarial Examples Against LLM-Based Network Traffic Classifiers](https://arxiv.org/abs/2607.07739)

**<font color=#1a73e8>作者：</font>** Zhenpeng Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly explored as network intrusion detection classifiers, but their adversarial robustness under realistic attacker constraints remains unclear. We present a controllability-aware black-box transfer framework for LLM-based network traffic classifiers. The framework partitions flow features into directly controllable (DC), indirectly controllable (IC), and uncontrollable (UC) groups according to network communication semantics, then restricts perturbations to DC features while freezing IC/UC features. Using a shared XGBoost surrogate, we generate finite-difference PGD, greedy coordinate-wise, and NES adversarial examples and transfer them to seven LLM targets and two conventional ML targets across five IDS benchmarks from 1999 to 2022. Across 27 valid LLM configurations and over 500,000 adversarial examples, we find that LLM transfer vulnerability is substantial but dataset- and comparator-dependent. Compared with LightGBM, LLMs are more vulnerable on RT-IoT2022 and CIC-IDS-2018, comparable on NSL-KDD and UNSW-NB15, and less vulnerable on HIKARI-2021; compared with the averaged ML baseline, LLMs show higher ASR on all five datasets. We further observe a consistent cross-architecture transfer hierarchy: gradient- and score-based perturbations transfer more effectively than greedy perturbations across all 27 LLM cells and 9/10 ML cells. Cross-surrogate validation with tree, neural, and linear surrogates yields similar LLM ASR, reducing evidence that the findings are XGBoost-specific. Constraint violation rate is 0\% by construction.

---


### 2. [Forensic Schema for Psychological Manipulation in Cyber Fraud: LLM-Driven Victim Reports Analysis](https://arxiv.org/abs/2607.07751)

**<font color=#1a73e8>作者：</font>** Zikai Alex Wen, Corrazon Ogot, Juan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing cybercrime classification schemas capture contact metadata and financial transactions but omit the psychological manipulation techniques perpetrators employ. We present a forensic schema (four categories, 35 questions) adding 11 manipulation indicators and cryptocurrency evidence fields to established forensic foundations. Applied to 10,994 victim reports via large language model (LLM)-driven annotation and validated against two human annotators (mean LLM-human $\kappa = 0.69$, matching inter-annotator $\kappa = 0.68$), the schema revealed a statistically distinct manipulation profile for each major fraud type (Cramer's $V$ up to $0.790$). A rationale-based evidence audit nonetheless exposed a forensic detail gap: detection of manipulation techniques was reliable, but victim narratives varied widely in the actionable detail supporting each Yes answer, and blockchain-specific identifiers were nearly absent. These findings point to AI-assisted victim intake with schema-informed follow-up questions as the most direct way to close the gap. The tiered annotation strategy also provides a reusable template for LLM-based extraction from other forensic text domains.

---


### 3. [Mechanistic Interpretability of LLM Jailbreaks via Internal Attribution Graphs](https://arxiv.org/abs/2607.07903)

**<font color=#1a73e8>作者：</font>** Anupam Wagle, Ifrat Ikhtear Uddin, Chaowei Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) exhibit remarkable capabilities but remain highly vulnerable to adversarial prompts and jailbreak attacks. Existing approaches primarily analyze these failures through input-output behaviors or attribution methods, offering limited insight into how adversarial perturbations alter the model's internal reasoning. Consequently, the mechanisms underlying unsafe or incorrect behaviors remain poorly understood. We introduce a mechanistic framework for diagnosing LLM vulnerabilities using paired internal computation graphs, which represent prompt-specific inference as structured causal interactions among latent features. By constructing and aligning computation graphs for clean and attacked prompts, we reveal that adversarial attacks induce systematic transformations of internal reasoning, including suppression of safety-relevant components, emergence of attack-specific features, and rerouting of computation paths. Building on this representation, we propose a unified framework that (i) decomposes computation into invariant, suppressed, and emergent structures, (ii) identifies recurring vulnerability motifs associated with failure modes, and (iii) performs causal interventions on nodes, paths, and subgraphs to directly evaluate their contributions to attack success. This enables a transition from descriptive attribution to causal diagnosis of model failures. Experiments across multiple open-source LLMs and diverse adversarial and jailbreak benchmarks demonstrate that structural deviations in internal computation graphs strongly correlate with unsafe behaviors. Furthermore, targeted interventions on identified vulnerability motifs improve model robustness, establishing internal computation graphs as a principled foundation for understanding, diagnosing, and mitigating LLM vulnerabilities.

---


### 4. [Who Broke the System? Failure Localization in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2607.07989)

**<font color=#1a73e8>作者：</font>** Yufei Xia, Anjun Gao, Yueyang Quan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) based multi-agent systems enable complex problem solving through coordinated reasoning and action, but their distributed structure also introduces new challenges in diagnosing system-level failures. When an execution fails, identifying which agent is responsible and at what point the trajectory first becomes irreversibly misdirected is difficult due to long-horizon interactions and tightly coupled agent behaviors. In this paper, we study the problem of failure localization in LLM-based multi-agent systems and present AgentLocate, a framework that attributes failures to both a specific agent and the earliest decisive step. AgentLocate combines an LLM-based judging mechanism with multi-perspective verification by independent evaluators, whose assessments are aggregated using a confidence-aware strategy. The resulting feedback is further used to adapt the judge through lightweight fine-tuning, improving attribution quality. We evaluate AgentLocate on two complementary benchmarks covering diverse tasks, agent configurations, and trajectory lengths. Experimental results show that AgentLocate consistently outperforms existing failure localization methods in identifying both responsible agents and failure steps, while remaining efficient in terms of token usage and running time.

---


### 5. [Beware What You Autocomplete: Forensic Attribution of Backdoored Code Completions](https://arxiv.org/abs/2607.08011)

**<font color=#1a73e8>作者：</font>** Anjun Gao, Yueyang Quan, Zhuqing Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models have enabled powerful code completion systems that assist developers by predicting subsequent lines of code. However, these models remain vulnerable to backdoor attacks, where malicious fine-tuning data covertly implants unsafe behaviors. Despite advances in defensive techniques, adaptive and sophisticated backdoor attacks still evade detection and mitigation. We present CodeTracer, a forensic framework that traces malicious code completions back to the backdoor fine-tuning data responsible for them. Operating under realistic post-deployment constraints, CodeTracer relies solely on the fine-tuning corpus and the reported miscompletion event. It extracts a structured behavioral fingerprint from the compromised output, narrows the search to semantically relevant code samples, and employs LLM-based reasoning to attribute unsafe logic to specific backdoor data. Extensive evaluations across three representative vulnerability cases and ten backdoor attacks, along with sixteen competitive baselines, demonstrate that CodeTracer consistently achieves high forensic accuracy, low false identification rates, and strong robustness against adaptive attacks.

---


### 6. [Out of Sight: Compression-Aware Content Protection against Agentic Crawlers](https://arxiv.org/abs/2607.08180)

**<font color=#1a73e8>作者：</font>** Xuefei Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rise of LLM-based agents with reasoning, summarization, and memory capabilities has created a new threat surface for online content that conventional defenses fail to address. Existing defenses like access controls can be circumvented by agents mimicking ordinary browsers, and injection-based defenses often degrade human readability. In this paper, we revisit the agent pipeline and identify context compression, which agents routinely invoke to fit context budgets, as a critical yet overlooked defense layer. We propose CAPE, a framework that protects high-value textual content by injecting invisible perturbations without changing its human-visible surface form, thereby inducing severe information loss during agent compression. CAPE extracts disruptive seed perturbations from an accessible surrogate compressor, then adapts them to query-only target compressors through prior-guided evolution and preference-calibrated candidate prioritization, achieving effective protection under a low query budget. Experiments on three content types and four compression settings show that CAPE improves information loss by up to 75.8% over the strongest baseline while keeping protected content visually indistinguishable from originals. CAPE also transfers to real-world settings, including the LangGraph agent workflow and GitHub Copilot, highlighting its generality and practical value. This paper aims to reveal context compression as a new defense layer, promoting content protection research in the agent era.

---


### 7. [Simulating the Resident: Generating Executable Smart Home Schedules via LLM Personas](https://arxiv.org/abs/2607.08231)

**<font color=#1a73e8>作者：</font>** Victor Jüttner, Xenia Wagner, Christoph Jahn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smart homes have emerged as an important domain for HCI research, including work on usable security and privacy. Ideally, studies in these areas draw on datasets collected in real homes with real residents, capturing authentic device interactions, network traffic, and daily routines. However, creating such datasets is slow, expensive, and raises significant privacy concerns, as it requires long-term observation of people in their most private spaces. We propose using LLMs to generate diverse resident personas that interact with a simulated smart home, producing behaviorally grounded interaction schedules that can be executed on physical testbeds. We present (1) a design framework configuring simulated households across five socio-technical dimensions, (2) a multi-stage LLM pipeline that produces structured, executable device interaction schedules, and (3) a proof of concept demonstrating feasibility. As a work in progress, we aim to support scalable, privacy-conscious smart-home experimentation without relying on intrusive real-world data collection.

---


### 8. [Multi-Agent Firewall Architecture for Privacy Protection of Sensitive Data in Interactions with Language Models](https://arxiv.org/abs/2607.08282)

**<font color=#1a73e8>作者：</font>** Hugo García Cuesta, Pablo Mateo Torrejón, Alfonso Sánchez-Macián  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) have become essential productivity tools, their integration into workflows without adequate safeguards creates significant risks. This paper proposes an open-source, privacy-focused, user-facing firewall designed to secure both web-based and programmatic LLM interactions. The architecture combines a browser extension and a proxy for total traffic interception across both HTTP(S) and WebSocket communications. At its core, a flexible multi-agent pipeline delivers data leakage prevention through a hybrid approach combining deterministic detectors with LLM-driven semantic analysis, proprietary code leakage prevention, and extensible components designed for future security enhancements such as prompt injection evasion. The framework's layered architecture enables deployment across heterogeneous environments, allowing organizations to balance computational cost, detection depth and latency. Evaluation results demonstrate it achieves F1 scores of up to 94.93% on optimal configurations.

---


### 9. [Token-Flow Firewall: Semantic Runtime Auditing for Persistent AI Agents](https://arxiv.org/abs/2607.08395)

**<font color=#1a73e8>作者：</font>** Puji Wang, Yingchen Zhang, Ruqing Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Persistent AI agents extend large language models (LLMs) beyond single-turn interaction into long-lived software systems. Unlike traditional chat assistants, unsafe content in these agents can propagate through persistent state, reusable skills, and tool-mediated interactions, creating a substantially larger semantic attack surface. We observe that most security-critical interactions in such agents are transmitted through natural-language token flows, including memory updates, tool arguments, retrieved files, and inter-component communications. This observation enables a new security formulation: unsafe behavior can be intercepted as risky semantic flows before reaching privileged runtime sinks. Based on this insight, we propose TokenWall, a runtime defense framework that acts as a semantic firewall over agent token flows. TokenWall performs boundary-aware semantic auditing over these flows, constructing structured source-sink audit records, applying lightweight local inspection before execution, and selectively escalating ambiguous high-risk cases to stronger arbitration modules. Unlike prior approaches that rely on sparse auditing or remote large-model oversight, TokenWall enables full-coverage pre-execution mediation while reducing remote arbitration and latency. Experiments on CIK-Bench show that TokenWall reduces attack success rate to 12.5% while maintaining a 97.4% benign executable pass rate without human confirmation. TokenWall further introduces only 0.69 seconds of additional latency on benign cases, demonstrating that semantic runtime containment can achieve a practical security-utility trade-off for persistent AI agents.

---


### 10. [TRACE: A Two-Channel Robust Attribution Watermark via Complementary Embeddings for LLM-Agent Trajectories](https://arxiv.org/abs/2607.08400)

**<font color=#1a73e8>作者：</font>** Zheng Gao, Xiaoyu Li, Xiaoyan Feng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents reach users through resellers, who may rebrand a developer's agent or substitute a cheaper model. When provenance is disputed, attribution rests on the trajectory log (the record of tool calls, observations, and executed actions, not the model's reasoning), which the reseller stores and processes to meter usage. A watermark must therefore survive an adversary with full read/write access to the very evidence it is detected from; existing agent watermarks do not, as their attribution is read straight off that log. We present TRACE, to our knowledge the first agent watermark that is distortion-free in its action choices, self-synchronizing under deletion, and unconditionally invariant under rewriting. Deletion desynchronizes a position-derived key and rewriting alters content, so a deletion-robust key must come from content and a rewrite-robust key from position, and no single key serves both. A trajectory, however, has room for two watermarks. TRACE superposes a selection channel that sets which action is chosen, keyed on local content with a distortion-free sampler, so the agent's distribution is provably unchanged and detection resynchronizes after deletions, and a tally channel that sets how many records each decision group holds, keyed on the log's skeleton alone, which no rewriting can touch. We prove this behavioral watermark's signal is bought with decision entropy, each decision paying at least half its entropy and deterministic decisions nothing, and that erasing both channels forces the reseller to corrupt the trajectories it resells. On ToolBench and ALFWorld, TRACE matches the unwatermarked agent's success rate while its selection channel reaches detection scores near z = 100 on long-horizon trajectories, stays detectable under 70% step deletion, and keeps a tally channel exactly unchanged under LLM rewriting of any strength.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
