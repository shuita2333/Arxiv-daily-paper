# 🔐 大模型安全相关研究 | 2026年05月20日

> 本类共 **18** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Detecting Verbatim LLM Copy-Paste in Homework](https://arxiv.org/abs/2605.16336)

**<font color=#1a73e8>作者：</font>** Aizierjiang Aiersilan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have made fluent essay writing, code drafting, and quiz answering instantly available to students at every level, from secondary school through graduate study. Many educators do not object to LLM use \emph{per~se}; what they need to detect is the case in which a student pastes the assignment prompt into a chatbot and submits the model's reply verbatim, without engaging with the work. Existing post-hoc AI-text detectors remain unreliable and have been shown to penalise non-native English writers, while output-side watermarks require cooperation from the model provider. We propose an alternative that the educator controls directly: an input-side watermark in which an invisible instruction is embedded inside the visible assignment prompt itself. An LLM that ingests the prompt verbatim quietly reads the hidden instruction and writes a tell-tale signature into its reply, exposing the copy-and-paste pathway specifically. We describe SteganoPrompt, a single-page, zero-dependency web tool that encodes an arbitrary printable-ASCII payload into the deprecated Unicode Tags block (\texttt{U+E0000}--\texttt{U+E007F}). The encoded string is visually identical to the original, survives common copy-paste channels (Word, Google Docs, PDF, Markdown, Slack, e-mail, the major learning-management systems), and is reliably tokenized by frontier models. We evaluate compliance across seven LLM families and a representative set of educational content channels. The work is informed by my experience as a graduate teaching assistant for an undergraduate software engineering course at the George Washington University. The tool is released under the MIT licence at \url{this https URL}.

---


### 2. [The End of Trust: How Agentic AI Breaks Security Assumptions](https://arxiv.org/abs/2605.16436)

**<font color=#1a73e8>作者：</font>** Osama Zafar, Alexander Nemecek, Erman Ayday  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> For decades, the security of digital interaction has rested on an unacknowledged economic constraint. Attackers faced a tradeoff between the fidelity of a deception and the scale at which it could be deployed. Convincing impersonation required sustained human effort and was confined to a narrow set of high-value targets, while mass-market attacks sacrificed plausibility for reach. Detection systems, verification mechanisms, and user awareness training have all been implicitly calibrated to the artifacts of cheap deception that this tradeoff produced. Agentic AI collapses the tradeoff, allowing high-fidelity, individually tailored deception to be produced at mass-market scale. We argue that this shift exhausts a security paradigm rather than merely intensifying the threat landscape. We introduce the Infinite Impostor, an attack model in which an autonomous agent interposes itself between two parties who already trust each other, hijacking an existing relationship rather than building a new one from scratch. Detection-oriented defenses share an assumption that generative progress is eliminating, that synthetic outputs are distinguishable from authentic ones. We propose a suspect-by-default paradigm that shifts security from authenticating actors to evaluating actions, and examine the governance tensions that arise when platforms become the regulatory substrate of digital interaction.

---


### 3. [MalwarePT: A Binary-Level Foundation Model for Malware Analysis](https://arxiv.org/abs/2605.16455)

**<font color=#1a73e8>作者：</font>** Saastha Vasan, Yuzhou Nie, Kaie Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automated malware analysis increasingly relies on machine learning, yet most existing methods remain task-specific and depend on handcrafted features or narrowly scoped models. Recent developments in binary-level foundation models suggest a path toward reusable program representations, but their application to malware analysis remains underexplored, and most still operate at byte-level tokenization, limiting their ability to capture multi-byte code patterns.
In this work, we introduce MalwarePT, a binary-level foundation model for malware analysis built on a ModernBERT-style encoder and pretrained with masked language modeling on Windows PE code-section bytes. We study whether a single pretrained encoder can transfer across malware-analysis tasks at different granularities, and how tokenization design affects that transfer. We train a byte-pair encoding (BPE) tokenizer on code-section bytes to compress frequent multi-byte patterns within a fixed context budget.
We evaluate MalwarePT on three downstream tasks spanning token-, function-, and document-level prediction: API call prediction, functionality classification, and malware (program) detection under temporal drift. Our evaluation demonstrates that pretraining yields substantial gains for API call prediction and functionality classification, and that increasing the BPE vocabulary beyond the byte-level baseline improves performance, with the strongest overall tradeoff at a vocabulary size of 1,024 tokens. In malware detection at FPR ~ 0.001, MalwarePT outperforms the neural network baselines, and is complementary to feature-engineering models that rely on PE structure. We also compare against existing binary foundation models and show that MalwarePT's design choices yield gains across all downstream tasks.

---


### 4. [From AI-Generated Content to Agentic Action: Security and Safety Threats in Generative AI](https://arxiv.org/abs/2605.16471)

**<font color=#1a73e8>作者：</font>** Zelin Zhang, Qi Li, Jie Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Generative AI systems are increasingly used not only to produce content but also to retrieve data, invoke tools, and execute actions. This work examines the security and safety implications of that shift across content-level, model-level, and agentic threats. We analyze how attacker access requirements, system autonomy, and the scope of potential harm change as models move from generating artifacts to executing operations through tool chains and external APIs. We then assess technical countermeasures including detection, watermarking, alignment, and emerging agentic safeguards, and show that several depend on forms of institutional coordination that current governance arrangements do not yet provide. Across the cases examined, capability deployment and attack-surface expansion repeatedly outpace defensive responses as systems move from generating content to executing real-world actions.

---


### 5. [\textsc{PrivScope}: Task-scoped Disclosure Control for Hybrid Agentic Systems](https://arxiv.org/abs/2605.16630)

**<font color=#1a73e8>作者：</font>** Shafizur Rahman Seeam, Zhengxiong Li, Zhiyuan Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hybrid local--cloud agents enrich user requests with context from persistent working state before delegating capability-intensive subtasks to a cloud language model (CLM). While this enrichment can improve task success, it also exposes unnecessary information in the cloud-bound payload, including task-irrelevant context, carryover from prior workflows, and overly specific sensitive details, resulting in \emph{over-disclosure}. Existing solutions either isolate workflows to limit cross-workflow leakage or apply general-purpose sanitization that does not reason over LC-assembled payload scope.
We present \textsc{PrivScope}, a trusted on-device payload governor that enforces \emph{task-scoped disclosure} at the local--CLM boundary, without requiring cloud-side changes. Its key idea: sensitive information should reach the cloud only when required for the delegated subtask, and then only in the least revealing form preserving utility. \textsc{PrivScope} extracts disclosure units from the assembled payload and keeps direct identifiers and account-linked values on device. The remaining units pass through cloud-necessity control, which determines what is actually needed; units that must reach the cloud are abstracted to the least-specific representation sufficient for the task. On 100 medical-booking workflows across three commercial CLMs, \textsc{PrivScope} eliminates profile leakage (0.0\% vs.\ 17.7\%), more than halves attacker re-identification (23.1\% vs.\ 64.3\%), and achieves the highest candidate recall on every CLM tested while preserving task success close to the unprotected baseline on GPT-4o-mini and Gemini 2.5 Flash. Gains hold across five local backbones and add only seconds of on-device latency on commodity hardware.

---


### 6. [Securing LLM Agents Need Intent-to-Execution Integrity](https://arxiv.org/abs/2605.16976)

**<font color=#1a73e8>作者：</font>** Wenjie Qu, Ming Xu, Peiran Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This position paper argues that securing LLM agents requires first defining an end-to-end correctness property that specifies when an agent's execution faithfully reflects the user's intent. Modern LLM agents operate over an \emph{intent-to-execution pipeline}, where natural-language instructions are translated into concrete system operations such as tool calls, API requests, and code execution. While recent defenses have made progress in constraining how agents construct tool calls, most existing formulations implicitly assume that tools are trusted. The emergence of systems such as OpenClaw, with open ecosystems of third-party skills and direct access to user environments, breaks this assumption and exposes new failure modes, including malicious or over-privileged components in the execution pipeline.
Despite rapid progress in defense mechanisms, there is no adequate correctness property that defines what ``secure'' means for LLM agents, nor a principled way to evaluate the coverage of existing defenses. We observe that LLM agents are structurally analogous to compilers, where security violations correspond to mis-executions that do not preserve user intent. Drawing on this analogy, we identify two fundamental problem sources -- untrusted data ingestion and untrusted tool execution -- and derive four integrity properties that must hold simultaneously: \emph{Tool Integrity}, \emph{Instruction Integrity}, \emph{Judgment Integrity}, and \emph{Data Flow Integrity}. We call their conjunction \emph{intent-to-execution integrity}.
Analyzing existing agentic defenses against these properties reveals that current systems provide only partial and non-compositional coverage, leaving fundamental gaps in securing modern LLM agents.

---


### 7. [The Range Shrinks, the Threat Remains: Re-evaluating LLM Package Hallucinations on the 2026 Frontier-Model Cohort](https://arxiv.org/abs/2605.17062)

**<font color=#1a73e8>作者：</font>** Aleksandr Churilov  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Spracklen et al. (USENIX Security '25) showed that code-generating large language models hallucinate package names that do not exist on PyPI or npm at rates ranging from 5.2% on commercial models to 21.7% on open-source models, creating an attack surface for slopsquatting -- the registration of malicious packages under hallucinated names. We replicate their methodology on five frontier code-capable LLMs released between October 2025 and March 2026: Claude Sonnet 4.6, Claude Haiku 4.5, GPT-5.4-mini, Gemini 2.5 Pro, and DeepSeek V3.2. Across 199,845 paired Python and JavaScript prompts validated against PyPI and npm master lists, we measure overall hallucination rates between 4.62% (Claude Haiku 4.5) and 6.10% (GPT-5.4-mini) -- an order-of-magnitude compression of the inter-model spread observed by Spracklen, but not a retirement of the threat. Beyond replication, we identify a set of 127 package names (109 on PyPI, 18 on npm) that all five evaluated models invent identically, constituting a model-agnostic supply-chain attack surface that no single-model study can reveal. We further document a Python-over-JavaScript hallucination asymmetry that inverts Spracklen's 2024 finding, identify a Haiku-below-Sonnet inversion within the Anthropic family, and observe a Jaccard-similarity peak between DeepSeek V3.2 and GPT-5.4-mini (J = 0.343) suggestive of shared training-data origins.

---


### 8. [A Red Teaming Framework for Evaluating Robustness of AI-enabled Security Orchestration, Automation, and Response Systems](https://arxiv.org/abs/2605.17075)

**<font color=#1a73e8>作者：</font>** Ayan Javeed Shaikh, Nathaniel D. Bastian, Ankit Shah  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI-enabled Security Orchestration, Automation, and Response (SOAR) systems increasingly employ autonomous agents for cyber defense, yet their resilience to adaptive adversaries is underexplored. We introduce an autonomous red teaming framework that integrates large language models (LLMs) with reinforcement learning (RL) to generate adaptive, multi-stage attack campaigns against autonomous defenders in enterprise networks. A hierarchical design combines an LLM-based planner for strategic intent with an RL controller for tactical execution, supported by reward shaping aligned with kill-chain progression. Evaluation in a high-fidelity enterprise simulation demonstrates the effectiveness of the proposed approach, while also showing that standalone LLM agents fail to sustain multi-stage attack campaigns and that domain-specific cybersecurity models achieve only limited levels of compromise, highlighting the necessity for hybrid LLM-RL approaches to red teaming.

---


### 9. [When Efficiency Backfires: Cascading LLMs Trigger Cascade Failure under Adversarial Attack](https://arxiv.org/abs/2605.17288)

**<font color=#1a73e8>作者：</font>** Zehan Sun, Dingfan Chen, Songze Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) cascade systems are designed to balance efficiency and performance by processing queries with lightweight models while selectively escalating complex cases to more powerful ones. Such systems seek to reduces computational cost and latency while maintaining task performance, making it an appealing choice for large-scale deployment. However, the cascade design introduces new vulnerabilities through an expanded attack surface: the inclusion of lightweight front-end models and internal decision mechanisms introduces new weaknesses. In this work, we present the first study demonstrating that LLM cascade systems are susceptible to targeted adversarial manipulation, which disrupts both performance objectives and the intended cost advantages of the cascade design. We propose a novel attack framework that employs constrained sequential collaborative optimization of adversarial suffix under cascade dependencies, enabling simultaneous exploitation of lightweight models and decision mechanisms. This framework adapts to adversaries with varying capabilities, inducing controllable degradation in both cost-efficiency and accuracy. Unlike prior attacks targeting standalone models, our approach strategically leverages the cascade structure to achieve significantly stronger impact. Extensive experiments across diverse datasets and representative LLM cascade systems validate the practicality and severity of this attack. Our findings highlight the urgent need to rigorously scrutinize the security of LLM cascade systems and call for broader attention to the systemic risks inherent in such designs.

---


### 10. [ASPI: Seeking Ambiguity Clarification Amplifies Prompt Injection Vulnerability in LLM Agents](https://arxiv.org/abs/2605.17324)

**<font color=#1a73e8>作者：</font>** Udari Madhushani Sehwag, Zhengyang Shan, Heming Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Clarification-seeking behavior is widely regarded as a desirable property of LLM agents, enabling them to resolve ambiguity before acting on underspecified tasks. However, the security implications of this interaction pattern remain unexplored. We investigate whether the transition from standard execution to a clarification-seeking state increases an agent's susceptibility to prompt injection attacks. We introduce ASPI (Ambiguous-State Prompt Injection), a benchmark of 728 task-attack scenarios that isolates clarification as a distinct agent state and measures how this state transition affects vulnerability under controlled conditions. Each benchmark instance is evaluated under matched execution and clarification settings: in the execution setting, the agent acts on a fully specified instruction and encounters adversarial content only through tool-returned data; in the clarification setting, the agent must first request and incorporate additional user input before acting. We evaluate ten frontier LLMs and find that clarification-seeking consistently and substantially amplifies vulnerability. For instance, attack success rises from 1.8% to 34.0% for o3 and from 2.2% to 35.7% for Gemini-3-Flash. A decomposition analysis reveals that this gap reflects both a state-dependent shift in how models process incoming content and a channel-specific effect arising from the agent-solicited clarification interface. These findings demonstrate that standard execution-time security evaluation systematically underestimates the attack surface of interactive agents, and that robustness under fully specified tasks does not translate to robustness under ambiguity. For reproducibility, our data and source code are available at this https URL.

---


### 11. [Rethinking Side-Channel Analysis: Automated Discovery and Analysis of Side-Channel Leakage with LLM-Assisted Agents](https://arxiv.org/abs/2605.17406)

**<font color=#1a73e8>作者：</font>** Zhen Xu, Zihao Wang, Yuhua Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Side-channel attacks exploit unintended information leakage from system behavior and continue to pose serious privacy risks in modern platforms. Despite extensive prior work, side-channel analysis remains largely manual and fragmented, typically assuming predefined target events and a fixed set of known channels. As systems and applications grow increasingly complex, several fundamental questions remain unanswered: which user or system events are sensitive in practice, how side channels associated with these events can be systematically discovered without exhaustive manual effort, and how their leakage can be analyzed at scale without prohibitive data collection and model training costs. To address these questions, we present SCAgent, an automated framework for side-channel risk analysis. To identify sensitive targets beyond manually specified events, SCAgent performs agent-driven system exploration guided by LLM-based semantic reasoning. To systematically discover side channels while mitigating the risk of LLM hallucination, it reasons over system documentation and incorporates explicit verification to enforce semantic consistency, threat-model feasibility, and per-channel usability. To enable scalable analysis under limited data, SCAgent adopts a few-shot learning paradigm based on foundation models, avoiding the need to train bespoke models for each channel--event pair. To bridge the gap between raw time-series side-channel signals and tabular foundation models, SCAgent further introduces a time-shift--robust feature extraction layer that enables effective downstream analysis. We instantiate SCAgent on iOS as a first step, focusing on OS-level side channels observable by unprivileged applications. Our evaluation spans standard benchmarks such as foreground app and website fingerprinting, as well as newly identified sensitive in-app activities in popular applications.

---


### 12. [Ablating Safety: Mechanisms for Removing Alignment in Language Models for Security Applications](https://arxiv.org/abs/2605.17413)

**<font color=#1a73e8>作者：</font>** Isaac David, Arthur Gervais  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety-aligned language models often refuse cybersecurity requests whose wording resembles misuse, even when the task is authorized and defensive. This makes security evaluation ambiguous: a failed answer may reflect missing capability or refusal-policy intervention. Ablating Safety studies alignment removal as a controlled transformation-evaluation protocol for authorized security tasks, comparing authorized-context prompting, reversible refusal-direction activation projection, representation-control projections, and LoRA-based de-alignment or task adaptation.
We evaluate refusal, attempt rate, validated security success, general-capability retention, instability, and out-of-scope unsafe compliance on Security-AR, a 60-prompt suite of authorized security, benign general, and non-operational spillover probes. The reported runs include a four-model projection pilot with 416 completions, a three-model Qwen2.5 LoRA extension with 1,980 held-out completions, representation and robustness sweeps, and executable secure-repair validators. Single-vector refusal projection raises mean security score only from 0.46 to 0.50 while increasing unsafe compliance from 0.10 to 0.47; rank-4 refusal-subspace projection reaches 0.51 while matching the aligned spillover rate. Task-only LoRA raises mean security score to 0.87 with general score 0.83 and unsafe compliance 0.13, while refusal-suppression with retention raises spillover to 0.27. These results support evaluating alignment removal as a utility-risk frontier, not as an uncensoring recipe, and treating compliance alone as neither competence nor safe deployment.

---


### 13. [Trust No Tool: Evaluating and Defending LLM Agents under Untrusted Tool Feedback](https://arxiv.org/abs/2605.17453)

**<font color=#1a73e8>作者：</font>** Lecheng Yan, Ruizhe Li, Xicheng Han 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents increasingly rely on external tools to make consequential decisions, yet most existing agent-security benchmarks and defenses implicitly assume that tool feedback is trustworthy once a tool has been selected. We study a different failure mode, cognitive poisoning, in which a malicious tool behaves plausibly during exploration, accumulates trust through benign-looking feedback, and becomes harmful only when hidden state conditions align with the final executable action. To study this setting, we construct TRUST-Bench, a task-conditioned benchmark of 1,970 hidden-trigger tool-compromise episodes with matched safe controls, introduce an asymmetric penalty metric, GuardedJoint, to better reflect real deployment risk, and present VISTA-Guard, a backbone-agnostic framework for final-action risk scoring. The core idea is to abstract multi-step tool interaction into structured environment variables that encode trust-formation dynamics and then score the risk of the final executable action from this trajectory-conditioned representation. Experiments show that prompt-centric heuristics, scalarized features, and zero-shot judges fail in this regime, whereas trajectory-aware final-action scoring yields strong in-domain discrimination and remains effective under balanced out-of-distribution transfer. Under GuardedJoint, VISTA-Guard reaches $84.2$ in-domain and $56.9$ on balanced out-of-distribution evaluation, while methods that optimize only one side of the safety--utility tradeoff collapse to zero. These findings support a broader view of agent security in black-box tool ecosystems: the decisive defense target is not local prompt text or tool descriptors alone, but the way trust is formed across the interaction trajectory and committed through the final action.

---


### 14. [From Detection to Response: A Deep Learning and Retrieval-Augmented Generation Framework for Network Intrusion Mitigation](https://arxiv.org/abs/2605.17960)

**<font color=#1a73e8>作者：</font>** Md Navid Bin Islam, Sajal Saha, Senior Member  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine-learning-based Intrusion Detection Systems (IDS) have achieved impressive accuracy in classifying network attacks, yet they consistently fall short on the question that matters most to a security analyst: what should I do next? This paper presents a unified, end-to-end framework that closes the gap between threat detection and actionable response. The system operates in two tightly coupled stages. First, an ensemble of three independently trained binary Deep Neural Networks (DNNs) classifies network traffic flows as Benign, Denial of Service (DoS), or Distributed Denial of Service (DDoS), achieving 99.84% accuracy on the CICIDS2018 dataset and 95.30% on the UNSW-NB15 dataset. Second, a Retrieval-Augmented Generation (RAG) pipeline constructs explanation-aware prompts from the top-5 anomalous features, retrieves the most semantically and lexically relevant guidance from a knowledge base derived from authorized sources and di- rects a locally deployed language model to synthesise structured, citation-grounded mitigation reports. The RAG-enhanced reports outperform vanilla LLM outputs across all automated evaluation metrics.

---


### 15. [Babel: Jailbreaking Safety Attention via Obfuscation Distribution Optimized Sampling](https://arxiv.org/abs/2605.17971)

**<font color=#1a73e8>作者：</font>** Ziwei Wang, Jing Chen, Ruichao Liang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite rigorous safety alignment, Large Language Models (LLMs) remain vulnerable to jailbreak attacks. Existing black-box methods often rely on heuristic templates or exhaustive trials, lacking mechanistic interpretability and query efficiency. In this study, we investigate an intrinsic vulnerability in the safety mechanisms of LLMs, where safety alignment relies on a small set of sparsely distributed attention heads, leaving much of the representational space weakly monitored. We formalize this phenomenon with a mathematical jailbreaking model that characterizes the delicate boundary of effective text obfuscation and analytically explains observed jailbreak behaviors. Guided by this model, we propose Babel, an efficient black-box attack framework that exploits the identified safety gap through systematic obfuscation sampling with iterative, feedback-driven distribution refinement, enabling reliable and high-success jailbreak attacks without access to model internals. Comprehensive evaluations on frontier commercial models demonstrate that Babel achieves state-of-the-art attack success rates and superior query efficiency. Specifically, compared to state-of-the-art methods, Babel increases the attack success rate on GPT-4o from 41.33% to 82.67% and on Claude-3-5-haiku from 38.33% to 78.33% within an average of 40 queries, providing a robust red-teaming methodology for LLMs safety research.

---


### 16. [Acoustic Interference: A New Paradigm Weaponizing Acoustic Latent Semantic for Universal Jailbreak against Large Audio Language Models](https://arxiv.org/abs/2605.18168)

**<font color=#1a73e8>作者：</font>** Yanyun Wang, Yu Huang, Zi Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The integration of audio modality into Large Audio Language Models (LALMs) significantly expands their attack surface. Existing jailbreak paradigms predominantly treat audio as a carrier for malicious payloads, relying on semantic optimization, acoustic parameter control, or additive perturbation to embed harmful content into the audio signal. In this work, we challenge this necessity and propose a new paradigm in which the role of audio shifts from content injection to safety alignment interference. We reveal that LALM safety alignment can be compromised solely by specific Acoustic Latent Semantics (ALS), the underlying paralinguistic features intrinsic to the priors of audio generative models. Distinct from previous works that leverage explicit acoustic parameters to merely style malicious audio, we demonstrate that interference audio, benign in content but infused with specific ALS, can serve as a universal jailbreak trigger. Leveraging this insight, we propose the Acoustic Interference Attack (AIA), which decouples the attack payload from the audio. Specifically, AIA employs a set of universal, instruction-neutral interference audio, enabling standard malicious text queries to bypass safety alignment without instance-specific optimization. Extensive experiments on 10 LALMs across five datasets demonstrate that AIA achieves the state-of-the-art attack success rate. Furthermore, our interpretability analysis uncovers the inference path drift induced by AIA and identifies the inherent effective patterns within ALS, revealing the fundamental vulnerability of cross-modal alignment in LALMs.

---


### 17. [Prompts Don't Protect: Architectural Enforcement via MCP Proxy for LLM Tool Access Control](https://arxiv.org/abs/2605.18414)

**<font color=#1a73e8>作者：</font>** Rohith Uppala  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly operate as autonomous agents that select and invoke tools from large registries. We identify a critical gap: when unauthorized tools are visible in an agent's context, models select them in adversarial scenarios -- even when explicitly instructed otherwise. We propose a governed MCP proxy that enforces attribute-based access control (ABAC) at two points: tool discovery, where unauthorized tools are removed from the model's context window, and tool invocation, where a second check blocks any unauthorized call. Across three models (Qwen 2.5 7B, Llama 3.1 8B, Claude Haiku 3.5) and 150 adversarial tasks spanning four attack categories, our proxy reduces unauthorized invocation rate (UIR) to 0% while adding under 50ms median latency. Prompt-based restrictions reduce UIR by only 11--18 percentage points, leaving substantial residual risk. Our results show that architectural enforcement -- not prompting -- is necessary for reliable tool access control in deployed agentic systems.

---


### 18. [Prompt2Fingerprint: Plug-and-Play LLM Fingerprinting via Text-to-Weight Generation](https://arxiv.org/abs/2605.18474)

**<font color=#1a73e8>作者：</font>** Sixu Chen, Xiang Chen, Hongyao Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The widespread deployment and redistribution of large language models (LLMs) have made model provenance tracking a critical challenge. While existing LLM fingerprinting methods, particularly active approaches that embed identity signals via fine-tuning, achieve high accuracy and robustness, they suffer from significant scalability bottlenecks. These methods typically treat fingerprint injection as an independent, one-off optimization task rather than a reusable capability, necessitating separate, resource-intensive training for every new identity. This incurs prohibitive computational costs and deployment delays. To address this, we propose Prompt2Fingerprint (P2F), the first framework that reformulates fingerprinting as a conditional parameter generation task. By leveraging a specialized generator, P2F maps textual descriptions directly to low-rank parameter increments in a single forward pass, enabling plug-and-play LLM fingerprint injection without further model retraining. Our experiments demonstrate that P2F maintains high fingerprint accuracy, harmlessness, and robustness while significantly reducing computational overhead, offering a scalable and instant solution for LLM ownership management.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
