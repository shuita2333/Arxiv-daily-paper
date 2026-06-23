# 🔐 大模型安全相关研究 | 2026年06月24日

> 本类共 **25** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [BELLS-O: Evaluating the Operational Trade-offs of LLM Supervision Systems](https://arxiv.org/abs/2606.20668)

**<font color=#1a73e8>作者：</font>** Leonhard Waibl, Felix Michalak, Hadrien Mariaccia  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM supervision systems, namely input/output moderation filters and jailbreak detectors, are the primary safeguard against misuse in deployed AI applications, yet existing benchmarks are often vendor-biased, omit cost and latency, and rarely compare specialized guardrails against repurposed generalist LLMs. We present BELLS-O (Benchmark for the Evaluation of LLM Supervision Systems, Operational), the first independent operational benchmark of LLM supervision systems. BELLS-O evaluates 28 systems from 17 providers: every major specialized guardrail (e.g., LlamaGuard-4, ShieldGemma-2, Lakera Guard) and frontier generalists repurposed as supervisors (e.g., GPT-5.4, Claude Sonnet 4.6, Grok-4.1), jointly on detection rate, false-positive rate, latency, and monetary cost. We cover input/output moderation across 11 harm categories and jailbreak detection across 13 attack techniques, using in-house datasets built from handcrafted prompts, expert-curated samples, and quality-controlled synthetic generation. To suppress latent generator fingerprints in synthetic data, every generated sample is paraphrased. Mapping the Pareto frontier reveals use-case-dependent tradeoffs. On content moderation, specialized supervisors are operationally dominant: top systems match frontier LLMs on detection (~95% vs. 94%) at comparably low false-positive rates (<=2%), while running 5-10x faster and ~10x cheaper. On jailbreak detection, the tradeoff shifts: frontier LLMs achieve higher detection and lower false-positive rates but at 10-50x higher cost and 5-10x higher latency. We release the benchmark, framework, leaderboard, and datasets as the first vendor-neutral basis for selecting safeguards under real deployment constraints.

---


### 2. [Can LLMs Reason About Brand Ownership? An Empirical Study of Domain Attribution Intelligence](https://arxiv.org/abs/2606.20868)

**<font color=#1a73e8>作者：</font>** Fathima Mashood, Mohamed Nabeel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When a new domain resembling a popular brand appears, defenders face a fundamental ambiguity: it may be an attacker-created squatting site for phishing, or it may be a domain the brand itself registered, either defensively, to block attackers, or legitimately, for a new product or service launch. Incorrectly flagging a brand-owned domain as malicious produces a false positive that harms end users and damages the brand's reputation. Resolving this ambiguity requires brand intelligence: the ability to determine, at scale, whether a given domain belongs to a brand. Large language models (LLMs), with their broad knowledge of brand domain relationships, offer a promising zero configuration approach to this problem, but their reliability for brand intelligence tasks remains unknown. We present the first systematic empirical evaluation of LLM brand intelligence across three tasks: domain enumeration (Q1), open ended brand attribution (Q2), and binary ownership classification (Q3). We evaluate four models, Gemini 2.5 Flash, Gemini 3.5 Flash, Claude Sonnet 4.5, and Claude Sonnet 4.6, across four retrieval settings (in context, web search, WHOIS lookup, and combined) on 36 of the most phished brands. Our results reveal a stark dichotomy: models achieve up to 82% precision enumerating brand domains from memory alone, yet fail at ownership verification without external tools, with macro F1 at most 0.37 in ICL mode. WHOIS augmentation lifts Q3 macro F1 by up to 0.65 points, yielding near perfect precision (<= 0.99), dramatically reducing the false positive risk for defenders. We provide concrete recommendations for deploying LLMs in brand protection pipelines.

---


### 3. [Whose Agent Are You? Multi-Layer Fingerprinting and Attribution of Autonomous Web Agents](https://arxiv.org/abs/2606.20910)

**<font color=#1a73e8>作者：</font>** Dayeon Kang, Hyejun Jeong, Jade Sheffey 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As AI web agents proliferate, combining large language models with autonomous, browser-level control, indiscriminate content scraping by web agents has emerged as a privacy and security challenge. Existing defenses, such as this http URL and active bot-blocking, are insufficient, as they are widely violated and easily circumvented. In this work, we demonstrate that AI web agents can be effectively distinguished from humans and traditional crawlers using a multi-layer fingerprint based on both network layer characteristics (e.g., TLS, HTTP) and browser interaction behavior. We implement this mechanism as a programmatic logging framework that can be deployed on a live, instrumented domain.
By analyzing six prominent agent frameworks (AutoGen, Browser Use, Claude, Gemini, Operator, and Skyvern), we uncover latent structural differences in how these systems assemble HTTP requests, establish TLS/HTTP connections, and execute autonomous browser actions. Feeding these multi-layer features into a decision tree classifier, our framework achieves high-fidelity identification (97% accuracy), successfully isolating distinct agent architectures and differentiating agent traffic from both human browsing baselines and legacy crawlers. Our findings demonstrate that cross-layer agent tracking provides a robust, evasion-resistant strategy for content protection and web security policy enforcement.

---


### 4. [Think Twice Before You Act: Protecting LLM Agents Against Tool Description Poisoning via Isolated Planning](https://arxiv.org/abs/2606.20922)

**<font color=#1a73e8>作者：</font>** Shanghao Shi, Xiao Wang, Chaoyu Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The integration of external tools has substantially expanded the capabilities of large language model (LLM) agents, but it also introduces new attack surfaces beyond prompt injection. In particular, cross-tool description poisoning can manipulate planner-visible tool metadata to steer an agent's trajectory, even if the poisoned tool itself is never chosen. To understand the effectiveness of existing defenses against this emerging threat, we first evaluate several prompt-injection defenses and find that they transfer poorly to cross-tool description poisoning. A key observation is that poisoned descriptions persist in the planning context across steps, enabling continuous influence over subsequent tool choices. Building on this insight, we propose Tool-Guard, a novel system-level defense based on a new concept called isolated planning, in which tool invocations that are detected as misaligned or suspicious cause the corresponding tool to be placed in a quarantined list (the influenced list), breaking further influence from poisoned descriptions. With this influence isolated, the tool can continue to be used to support the task, enabling a robust defense that preserves legitimate tool utility. Experiments on the AgentDojo and ASB benchmarks show that Tool-Guard substantially reduces attack success while maintaining high task utility. Our code is available at this https URL.

---


### 5. [Honeyquest for LLMs: Rethinking Cyber Deception for AI Attackers](https://arxiv.org/abs/2606.21037)

**<font color=#1a73e8>作者：</font>** Kerri Prinos, Lilianne Brush, Cameron Denton  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The empirical foundation of cyber deception relies on human-centered hypotheses, but the rapid emergence of autonomous, AI-enabled attackers challenges whether this foundation transfers to AI agents. To address this, we introduce an automated evaluation framework adapted from the Honeyquest instrument to assess LLM attacker judgment at scale. Our 21-LLM cohort spanned 10 providers, diverse architectures and specializations, open- and closed-weight models, and parameter scales from 8B to over 1T. We evaluated the performance of this LLM cohort (yielding 10,962 responses) against the 47-participant human baseline across an identical set of 174 reconnaissance queries. Our empirical evaluation reveals three key findings that establish LLMs as a distinct attacker class: (1) every model in our cohort falls for deceptive traps at a significantly higher rate than human attackers; (2) the defensive attention-diversion effect observed in humans is statistically absent in our LLM cohort; and (3) a critical recognition-action gap, where LLMs successfully articulate trap recognition in their reasoning but exploit the deceptive elements anyway 73.4\% of the time. Across the 21 models, trap recognition in reasoning text did not predict fell-for-trap behavior (Spearman $r = +0.08$, $p = 0.73$). Ultimately, these findings demonstrate that human-centered deception hypotheses do not reliably transfer to AI attackers, highlighting the critical need for new research into AI-native active defense frameworks.

---


### 6. [DEFENGRAPH: Knowledge Graph-Enhanced LLMs for Blue Team Cyber Defense](https://arxiv.org/abs/2606.21059)

**<font color=#1a73e8>作者：</font>** Zhen Wang, Kristen Moore, Qin Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) show promise for supporting decision-making in cybersecurity, but their reliability in high-stakes, time-evolving environments remains limited due to hallucinations, poor temporal reasoning, and shallow grounding in system context. We introduce DEFENGRAPH, an LLM-driven assistant designed to support human defenders during cybersecurity incidents. DEFENGRAPH improves contextual reasoning by integrating a dual-layer Static-Dynamic Knowledge Graph (KG) with graph-based path retrieval, LLM-driven contextual filtering, and reasoning-based re-ranking. The framework grounds LLM outputs in both long-term domain knowledge and evolving event context, enabling faithful and temporally aware decision support. We evaluate DEFENGRAPH in a cyber defense setting using knowledge graphs constructed from heterogeneous security artifacts, including SIEM alerts, system topology, attacker behaviors, and prior defensive actions. The evaluation uses data collected during live Red vs. Blue team cyber range exercises simulating attacks on critical infrastructure, which generate realistic and noisy datasets reflecting real-world defender workflows and system dynamics. Evaluations across four prevalent LLMs show that DEFENGRAPH sets a new state-of-the-art: on GPT-4o it boosts reasoning-recall from 61.45\% to 73.49\% and ticket-action recall from 52.17% to 72.46% (precision 24.49\% to 29.24\%), with similar gains on LLaMA-3 (46.99\% to 61.45\%), DeepSeek-R1 (45.78\% to 56.63\%) and QWen-3 (51.81\% to 59.04\%), while surfacing up to 50 correct defense actions versus 36 for the next best baseline and holding fault rates steady.

---


### 7. [Local LLM Agents as Vulnerable Runtimes:A Source-Code Audit of the Agent Runtime Layer](https://arxiv.org/abs/2606.21071)

**<font color=#1a73e8>作者：</font>** Zhengsong Zhang, Zongze Li, Jiawei Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Local LLM agents such as OpenClaw and Nanobot run on end-user machines and act on host resources - the shell, filesystem, browser, stored credentials, and messaging applications - through natural-language goals. These agents have become privileged software runtimes that mediate between user intent, model outputs, and host-level actions. Existing research characterizes the landscape through prompt injection, malicious skills, marketplace risks, or black-box evaluation of agents. But the implementation layer that performs this mediation, the prompt builder, parser, tool dispatcher, skill loader, memory writer, network client, and permission gate, has remained an unexamined safety boundary. To our knowledge, no prior work has examined the agent's source tree to audit these components for implementation-level security weaknesses. We present CLAWAUDIT, a static auditing framework for measuring vulnerability exposure in local LLM agent runtimes. CLAWAUDIT derives a five-category vulnerability taxonomy from STRIDE and develops custom static-analysis rules that target agent-specific patterns absent from established rule sets for vulnerability analysis. We instantiate the taxonomy in two backends, 47 Semgrep YAML rules and 30 CodeQL queries, and evaluate on OPENCLAWBENCH, a benchmark of 446 source-code-level advisories from the OpenClaw repository and split temporally into 229 rule-derivation (train) and 217 held-out (test) advisories. On the held-out test, CLAWAUDIT raises Semgrep recall from 21.7% (Pro baseline) to 66.8%, and CodeQL recall from 13.8% (security-extended) to 75.1%. Train/test gaps remain within 4 percentage points for all four configurations, indicating that the rules generalize to vulnerabilities unseen during rule writing. A preliminary live-code audit shows that these recall-oriented rules require manual triage, motivating semantic filtering before production deployment.

---


### 8. [AgenticOS: An Intent-Oriented Secure Operating System Architecture for Autonomous AI Agents](https://arxiv.org/abs/2606.21129)

**<font color=#1a73e8>作者：</font>** Zhen Zhao, Yu Zhang, Yanpeng Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Traditional OS security models based on "resource exposure plus permission checks" face structural challenges as LLM-driven autonomous agents acquire capabilities for planning, tool use, network access, and code execution. Once an agent runtime is compromised through prompt injection or malicious tool outputs, an attacker can compose POSIX-style resource primitives into behaviors far beyond the user's task authorization. To address this, we propose AgenticOS, an intent-oriented secure OS architecture that consolidates delegable, auditable software capabilities into OS-native ones rather than replacing all applications. The core insight is to reframe the OS from a "resource manager" into an "intent filter": instead of requesting low-level resources directly, agents submit structured intent declarations, from which the system synthesizes a least-privilege environment with mandatory mediation, auditing, and information-flow constraints. At the implementation level, we introduce a four-layer architecture -- Ghost Kernel, Logic Shutter, Agent Capsule, and Semantic Boundary Gateway -- together with the Intent ABI, Manifest-Only Runtime, Weaver-based capability generation, and an admission model for AgenticOS-native Skills.

---


### 9. ["What Happens Locally, Leaks Globally": Detecting Privacy Leakage Risks in MCP Servers](https://arxiv.org/abs/2606.21338)

**<font color=#1a73e8>作者：</font>** Biwei Yan, Minghui Xu, Yijun Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) has rapidly become the de facto standard for connecting large language models (LLMs) to external resources, but it also introduces a class of privacy risks that existing tools are ill-equipped to detect. Unlike conventional exfiltration bugs, leakage in MCP servers is largely protocol-induced: credentials, API keys, and Personally Identifiable Information (PII) cross the local/LLM boundary simply by being returned, logged, or raised inside a tool handler, with no explicit outbound request in the source code. We present MCPPrivacyDetector, a context-aware cross-language static analysis framework that detects such leakage in multilingual MCP servers. MCPPrivacyDetector lifts heterogeneous code implemented across different programming language (e.g., Python) into a unified program representation, applies context-aware semantic filtering to isolate genuinely sensitive values and protocol-specific implicit sinks (e.g., @mcp.tool handlers), and performs taint analysis to enumerate feasible flows. Applied to 10,655 real-world MCP servers, MCPPrivacyDetector finds leakage rates above 10%. Case studies confirm concrete exposures including leaked Bearer tokens, propagated API keys, and plaintext authentication credentials, arguing for systematic, protocol-aware safeguards in the emerging LLM agent toolchain.

---


### 10. [LLM-assisted Generation of Pseudo-C2 Servers for IoT Malware Dynamic Analysis](https://arxiv.org/abs/2606.21349)

**<font color=#1a73e8>作者：</font>** K. Hasui, S. Matsugaya, M. Shimamura 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Most IoT malware operates as botnets dependent on Command and Control (C2) servers, but the short-lived nature of attack infrastructure often leaves samples dormant without C2 communication, hindering dynamic analysis. This paper proposes a system that combines Ghidra with a Large Language Model (LLM) to extract communication specifications from a malware binary and automatically generate a pseudo-C2 server. Experiments using Mirai demonstrate that the proposed system semantically interprets binary control structures and extracts all 20 core protocol elements in agreement with the ground truth (100\% specification extraction accuracy). The generated pseudo-C2 server fully reproduces seven of ten DDoS attack vectors with attack behavior consistent with the original C2. When applied to a customized variant created by modifying the publicly available Mirai source code, the method succeeds end-to-end -- from specification extraction through pseudo-C2 generation to attack reproduction -- demonstrating that the LLM infers specifications from binary structures without relying on pre-trained knowledge. This approach extends the applicability of LLMs from analysis assistance to the automated construction of dynamic analysis environments.

---


### 11. [Evaluating LLMs for Real-World Web Vulnerability Detection](https://arxiv.org/abs/2606.21397)

**<font color=#1a73e8>作者：</font>** Sebastian Neef, Luca Jungnickel, Antonio Benjamin Buchholz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have emerged as a promising tool for automated vulnerability detection, yet their effectiveness on web-specific vulnerabilities remains to be explored.
This work benchmarks six frontier (Claude Opus 4.6, Codex GPT-5.4, Gemini 3.1-pro-preview) and open-weight models (Qwen 3.5, Qwen 3 Coder Next, MiniMax M2.5) on their ability to detect real-world web vulnerabilities using static analysis in WordPress plugins, including SQL injection, stored cross-site scripting, path traversal, and remote code execution. Using five prompt designs of varying structure, scope, and complexity across three experiment iterations, we aim to answer how model and prompt choice affects vulnerability detection.
Our results show that all models are capable of detecting valid security issues, but the detection rate varies depending on the model and prompt. For example, Claude Opus 4.6 achieved the highest web vulnerability detection rate (63%), while open-weight MiniMax M2.5 performs on par with other frontier models (48%), and self-hosted Qwen 3.5 only achieved 35%. We show that scoped prompts that narrow the vulnerability scope outperform open-ended ones, whereas the prompt complexity has little impact. Surprisingly, no model achieved full reporting consistency across three experiment iterations, with some as low as 50%. Our experiments demonstrate the opportunities and limits of LLM-based vulnerability detection, as no model correctly identified one baseline vulnerability in one of the plugins.
Additionally, we derive practical lessons learned for security practitioners and publish all code and data to support future research.

---


### 12. [Toward Open Weight Models Without Risks: Separating Public and Private Capabilities in LLMs](https://arxiv.org/abs/2606.21638)

**<font color=#1a73e8>作者：</font>** Charbel El Feghali, Arkil Patel, Nicholas Meade 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-weight Large Language Models (LLMs) enable scientific progress and broad deployment. However, they make it difficult to control access to sensitive capabilities. Current practice either suppresses dangerous capabilities before release or mediates access through closed services that use specialized model variants, input/output monitors, and API permissions. The former is susceptible to jailbreaks while sacrificing capability for all users to mitigate the risks posed by a few, and the latter is fundamentally incompatible with open-weight release. In this paper, we propose Tiered Language Models (TLMs), where a single set of released weights supports multiple capability levels. In its default public configuration, a TLM behaves as a conventional LLM. A compact secret key specifies a permutation over a small parameter subset, inducing an alternative computation graph over the same weights that exposes additional capabilities. We develop a training protocol that jointly pretrains both configurations from scratch, then fine-tunes the keyed configuration on private data with regularization to preserve the public model's behavior. We pretrain 180M- and 650M-parameter TLMs and demonstrate that the keyed configuration can acquire a new language, gain instruction-following ability, and memorize private factual knowledge, whereas the public configuration exhibits none of these capabilities. Moreover, we show that our approach extends naturally to multiple hierarchical tiers. Because authorization operates on the model's weight structure rather than in the input space, the mechanism resists fine-tuning-based extraction and partial key compromise. In general, TLMs take a step toward reconciling open-weight release with selective capability control.

---


### 13. [Safe to Check, Unsafe to Use: Relinking at the Compression Boundary of LLM Agents](https://arxiv.org/abs/2606.21732)

**<font color=#1a73e8>作者：</font>** Zesen Liu, Zihan Zhang, Dongdong She  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Summarization-based prompt compression is increasingly used by LLM agents to shorten long, distributed contexts, but it shifts the security boundary: filters inspect the pre-compression prompt while the backend acts on a newly generated compressed context. We identify relinking, a compression-boundary vulnerability where the compressor behaves as a confused deputy, summarizing distributed, locally benign fragments into a complete malicious instruction. Unlike prompt injection, relinking need not place an explicitly malicious payload in the source context. We show that relinking arises from summarization itself: attention makes separated fragments jointly available, pre-training makes compatible fragments plausible to connect, and post-training favors compact backend-actionable summaries. We formalize the attacker-induced form as adversarial relinking and present Relink, an automated DSL-based tool that splits malicious payloads into benign fragments while keeping the complete payload absent before compression. Across four long-context agent benchmarks, Relink achieves 86.9% Relink Rate and Backend Action Rate versus 17.0% for clean-split controls. Existing defenses fail to reliably capture adversarial relinking; our KBRA defense reduces residual Backend Action Rate to 0.0%.

---


### 14. [Agent-Assisted Side-Channel Attacks on Non-Prefix KV Cache in RAG](https://arxiv.org/abs/2606.21842)

**<font color=#1a73e8>作者：</font>** He Sun, Shinan Liu, Siyuan Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern Large Language Model (LLM) serving engines increasingly rely on Retrieval-Augmented Generation (RAG) and non-prefix Key-Value (KV) cache fusion to accelerate long-context, multi-tenant inference. While existing KV cache side-channel attacks require strict linear prefix alignment--rendering them ineffective against real-world RAG queries that contain unique, user-specific private prefixes--we uncover a critical class of structural vulnerabilities inherent to chunk-aware memory scheduling. We demonstrate that the deterministic micro-architectural mechanisms used to align and fuse disjoint memory chunks inadvertently leak a continuous "Step-Wave" timing signature. Exploiting this physical observation, we introduce SpliceLeak, the first end-to-end side-channel attack targeting non-prefix KV cache fusion. SpliceLeak executes a systematic two-phase privacy breach: it first structurally fingerprints the exact length of hidden private prompts, and subsequently manipulates boundary collisions to extract exact semantic content token-by-token. Extensive evaluations on production-grade frameworks (vLLM integrated with LMCache) demonstrate that SpliceLeak achieves up to a 100% extraction success rate in bounded-entropy scenarios. Driven by a deterministic +104 ms hardware latency void, the attack requires as few as 63 requests per token, piercing through realistic continuous batching noise. To resolve the inherent conflict between memory deduplication and security, we propose SpliceDefense, a bipartite mitigation framework consisting of Quantized Chunk Padding (QCP) and Constant-Time Boundary Fusion (CTBF). Our evaluations confirm that SpliceDefense effectively flattens the side-channel signal (Delta TTFT ~ 0) with negligible throughput overhead, preserving the critical benefits of global cache sharing.

---


### 15. [Harness-MU: A Safe, Governed, and Effective Harness for Multi-User LLM Agents](https://arxiv.org/abs/2606.21856)

**<font color=#1a73e8>作者：</font>** Wangxuan Fan, Xiaoyu Nie, Zhongxiang Dai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing deployment of large language model (LLM) agents in collaborative workflows demands robust multi-user, multi-principal interaction mechanisms capable of enforcing access permissions, resolving authoritative conflicts, and preventing unauthorized data disclosure. However, a fundamental mismatch exists between the single-user training paradigm of contemporary LLMs and the hard constraints required for multi-principal governance, rendering probabilistic, prompt-based safeguards vulnerable under multi-turn adversarial this http URL key insight is that governance constraints -- who is authorized, what is restricted, and whose instructions take precedence -- are deterministic runtime variables that should be enforced by execution hooks rather than entrusted to the LLM. We present \textbf{Harness-MU}, the first model-agnostic, zero-tuning infrastructure framework for multi-user LLM agents. By decoupling language generation from safety orchestration, Harness-MU guarantees unbreakable permission boundaries while maximizing compliant demand satisfaction. Across four frontier open-weight and proprietary models on the \textit{Muses-Bench} benchmark, Harness-MU achieves the goal of privacy preservation across all access-control attacks, outperforming the standard baseline by 0.28--0.39 in utility score and improving instruction-following accuracy by up to 48.9 percentage points. Harness-MU advances the philosophy of \textit{Harness Engineering}, establishing that systematic infrastructure is essential for solving LLM multi-principal governance challenges. The code and data are available at this https URL.

---


### 16. [$π$-RAG: Oblivious Retrieval via Semantic Quantization and Transcendental Addressing for Large Language Models](https://arxiv.org/abs/2606.22153)

**<font color=#1a73e8>作者：</font>** Aniket Wattamwar, Mrunal Kakirwar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper introduces $\pi$-RAG, a novel architecture for oblivious retrieval that decouples Large Language Models (LLMs) from sensitive data storage without sacrificing semantic understanding. Traditional Retrieval-Augmented Generation (RAG) architectures expose raw vector embeddings to potential inversion attacks and nondeterministic retrieval failures. To address this, we utilize the digits of $\pi$ as a source of transcendental entropy, creating an immutable indirection layer between the LLM and private records. The value $\pi$ provides immutability, is uneditable and math governs it. The architecture also introduces a Semantic Quantization Layer. This layer projects user inputs onto a pre-computed manifold of Canonical Intent Centroids. RAG performs vector cosine similarity but here it maps the centroids to deterministic offsets via cryptographic salt. The resulting $\pi$-key is a pointer to standardized payload from the actual datastore. By replacing direct access to the datastore via LLM with this transcendental layer, $\pi$-RAG mathematically guarantees that the inference remains oblivious to the data. This architecture unifies deterministic randomness, auditability, and differential privacy, demonstrating high efficacy for high-compliance sectors such as finance and healthcare.

---


### 17. [Revelio: Cost-Efficient Agentic Memory Safety Vulnerability Detection For Repository-Scale Codebases](https://arxiv.org/abs/2606.22263)

**<font color=#1a73e8>作者：</font>** Yiwei Hou, Hao Wang, Muxi Lyu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Memory safety vulnerabilities remain a significant threat even for projects with extensive fuzzing and manual auditing. Recent results suggest that large language models hold great promise for detecting such vulnerabilities, but they are unreliable, at risk of hallucination, and challenging to scale to repository-size codebases. This paper presents Revelio, a cost-efficient end-to-end agentic framework for memory-safety vulnerability discovery. Revelio addresses the problem of hallucination by generating an executable Proof-of-Vulnerability, which is checked with a deterministic sanitizer. It reduces cost using inexpensive LLMs and lightweight static analysis to help generate and rank vulnerability hypotheses, reporting vulnerabilities only when they can be reproduced and confirmed by a sanitizer. We evaluated Revelio on seven production-quality projects that had been continuously fuzzed for five to eight years, as well as on 100 randomly selected Arvo projects from the CyberGym benchmark. With around one hour per project and a total cost of $300, Revelio discovered 19 previously unknown memory-safety vulnerabilities. On benchmarks, Revelio outperformed frontier coding agents across diverse backbone models at comparable token costs. Our results suggest that Revelio enables scalable and trustworthy end-to-end LLM-based memory-safety vulnerability detection.

---


### 18. [Evidence-Bound Gateway-Path Provenance for Third-Party LLM Inference](https://arxiv.org/abs/2606.22560)

**<font color=#1a73e8>作者：</font>** Fei Wang, Zebai Tian  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Third-party LLM gateways have become a critical infrastructure layer between applications and external LLM providers. Conventional gateways do more than forward traffic: they decide which provider and model are called, whether fallback occurred, which stream is delivered, and what usage record should be billed. Because these decisions and records are authored inside the operator-controlled service, clients cannot independently distinguish honest mediation from route substitution, hidden fallback, stream manipulation, or forged provenance.
We present an evidence-bound LLM gateway architecture that separates the operator control plane from an attested execution plane. Within the gateway, a measured Attested Gateway Runtime (AGR) is the only component allowed to decrypt requests, enforce path policy, construct upstream calls, and sign evidence. Clients verify signed release metadata and fresh attestation before encrypting requests to keys bound to the AGR measurement. AGR enforces request-scoped routing, fallback, and endpoint constraints, invokes admitted providers, returns encrypted response streams, and signs evidence binding the policy, selected route, endpoint identity, stream commitments, and completion metadata to the attested runtime. An initial Rust prototype on AWS Nitro Enclaves shows modest mechanism overhead and fail-closed detection of policy, routing, endpoint, and stream-evidence tampering outside the attested runtime.

---


### 19. [RAVEN: Agentic RAG for Automated Vulnerability Repair](https://arxiv.org/abs/2606.22647)

**<font color=#1a73e8>作者：</font>** Varun Gadey, Zijie Liu, Alexandra Dmitrienko  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automated vulnerability repair has emerged as a promising direction to mitigate the growing number of software vulnerabilities. Recent advances in Large Language Models (LLMs) have further accelerated research in automated repair. However, existing frameworks remain largely restricted to memory-related vulnerabilities and locally repairable vulnerability settings, leaving generalization to unseen vulnerability types underexplored. Their evaluations are often limited to a single programming language, and largely rely on proprietary models. In this paper, we propose RAVEN, a scalable, efficient and autonomous framework that integrates an agentic retrieval-augmented generation (RAG) pipeline with controlled iterative repair in a unified framework. The framework utilizes open-source LLMs in a fully locally deployable setting with limited GPU requirements, while building a multi-faceted retrieval pipeline to retrieve historically relevant vulnerability fixes and guide the patch generation. In addition, RAVEN introduces a dedicated Curator Agent that retrieves cross-file dependencies from the target repository, to fix complex vulnerabilities that cannot be addressed using local vulnerable code alone. We evaluate RAVEN on 160 real-world CVE vulnerabilities across diverse vulnerability types, two programming languages, unseen CWE categories, and out-of-distribution settings. RAVEN achieves an overall repair success rate of 83.13%, outperforming all existing state-of-the-art repair frameworks, while also demonstrating strong generalization capabilities and maintaining the repair cost negligible.

---


### 20. [The Geometry of Refusal: Linear Instability in Safety-Aligned LLMs](https://arxiv.org/abs/2606.22686)

**<font color=#1a73e8>作者：</font>** Shivam Ratnakar, Kartikeya Vats  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern Large Language Models (LLMs) rely on extensive safety alignment, yet the mechanistic basis of refusal remains opaque. In this work, we investigate whether safety compliance is a deep semantic decision or a manipulable linear feature. We introduce Contrastive Logit Steering (CLS), a zero-optimization framework that isolates the "refusal direction" by contrasting hidden states derived from safe and unrestricted system prompts. Unlike representation engineering methods that intervene on internal activations, CLS operates directly on the output distribution, serving as a diagnostic probe for alignment fragility. When coupled with prefix injection to bypass initial refusal reflexes, this method induces a phase transition where guardrails collapse. Our experiments on 7 model families reveal that safety implementation is architecturally deterministic. While models like Llama-3.1 exhibit a "Late Decision" topology that is easily bypassed by CLS (reaching 95% ASR in approximately one second), others like Qwen-2.5 demonstrate "Early Divergence" by integrating safety mid-computation. Direct comparison with established activation-level steering methods shows that CLS achieves substantially higher attack success rates on Llama 2 (73% vs. 22.6%) and Qwen 7B (91% vs. 79.2%), demonstrating that logit-level intervention exposes alignment vulnerabilities that hidden-state methods underestimate. Beyond attacks, we show that this linearity enables bidirectional control: inverting the steering vector "hardens" models against jailbreaks without retraining. Our findings suggest that current alignment techniques create a steerable "safety axis" that serves as both a critical vulnerability and a precise primitive for defense.

---


### 21. [Black-Box Forensics for Conversational LLM Agents](https://arxiv.org/abs/2606.22698)

**<font color=#1a73e8>作者：</font>** Isadora White, Yasaman Jafari, Taylor Berg-Kirkpatrick  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As LLM-powered scams proliferate, black-box forensics for conversational LLM agents offers a path to accountability for systems hidden behind anonymous endpoints. Identifying the base model behind a chatbot endpoint (attribution), without model parameter access or knowledge of the hidden system prompt, would let investigators trace AI-enabled scams back to the providers whose models power them. Detecting when two endpoints run the exact same system prompt (fingerprinting), even one novel and unseen, would link individual scams into criminal networks and expose silent API changes. We conduct an empirical investigation of both capabilities. Our attribution classifiers identify the base model behind an agent with 98% accuracy from a few turns of non-adversarial conversation. Attribution of system prompts, while possible, requires retraining on a large amount of data for each prompt; system prompts in the wild are unbounded and ever-changing, making this approach costly. To tackle this more open-ended setting, our cross-encoder fingerprinting method achieves an AUC of 0.768 and an F1 of 0.703 on entirely unseen system prompts, and aggregating 50 interaction conversations from each target agent boosts AUC to 0.943. Conversational agents with unseen system prompts can thus be fingerprinted with robust accuracy from a few turns of ordinary conversation.

---


### 22. [VCT: A Verifiable Transcript System for LLM Conversations](https://arxiv.org/abs/2606.23003)

**<font color=#1a73e8>作者：</font>** Ruilin Xing, Feihong Li, Jiayue Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) interaction records are increasingly vital in digital forensics and compliance auditing. However, traditional linear tamper-evident logs fail to capture the inherent non-linear evolution of LLM conversations, such as re-prompting based on historical queries, response regeneration, session deletion, multi-device concurrency, and selective sharing. To address this issue, this paper proposes Verifiable Conversation Transcript (VCT), which abstracts complex non-linear LLM semantic operations into account-level authenticated state transitions. VCT constructs a three-tier cryptographic data structure: atomic Q&A pairs form branch-level hash chains, branch tails aggregate into session-level Merkle roots, and all session roots are further aggregated into an account-level Merkle root anchored by joint signatures from both the user and the server. VCT introduces a serialized state transition protocol with deletion barriers to eliminate conflicts between deletion and modification, complemented by a deterministic state-merge protocol to preserve concurrent non-deletion incremental operations. Furthermore, incremental denial checks and a gossip protocol enable asynchronous user devices to autonomously detect view forks caused by malicious servers and generate non-repudiable forensic evidence. Security analysis demonstrates that, under standard cryptographic assumptions, VCT guarantees the integrity, consistency, verifiable shareability, and non-repudiation of account-level conversation records. Evaluation of a Python prototype shows that the cryptographic latency of core operations is within sub-millisecond to low-millisecond ranges. Under a realistic configuration with 21 KB of text, security metadata introduces a negligible storage overhead of only 0.9%, validating the deployment feasibility of VCT for high-stakes forensic review on production-grade LLM platforms.

---


### 23. [Safety in Self-Evolving LLM Agent Systems: Threats, Amplification, and Case Studies](https://arxiv.org/abs/2606.23075)

**<font color=#1a73e8>作者：</font>** Ruixiao Lin, Xinhao Deng, Qingming Li 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Self-evolving LLM agent systems, which autonomously update their model parameters, memory, tools, and architectures, introduce a qualitatively new threat landscape in which adversarial influences become permanently encoded, self-amplify across generations, and propagate through populations without sustained attacker access. We present a systematic security and privacy analysis organized around the Module-Lifecycle Attack Surface (MLAS) matrix, which decomposes the attack surface into five functional modules (Brain, Cognitive Resource, Execution, Self-Design, Collective) $\times$ five lifecycle stages (Bootstrap, Propose, Evaluate, Commit, Serve). Analysis of the resulting 25 cells reveals that 17 face critical threats for which no effective partial mitigation. We identify seven cross-cutting amplification effects that interact synergistically and cannot be addressed by securing individual modules in isolation. Comparative case studies of two open-source frameworks demonstrate that evolution-native design activates $3.5\times$ more attack surface cells and achieves a 100% attack persistence rate (40/40 payloads across all CIA+Privacy categories), while co-located security scanners block only 2.5% of attacks. Our findings establish that self-evolution converts every known attack category from session-bounded to lineage-persistent, gives rise to entirely new attack classes, and renders static defenses structurally inadequate, motivating evolution-aware security frameworks and formal verification for self-modifying systems.

---


### 24. [Rising From the Ashes: How Agentic AI is Unblocking Challenges in Cybersecurity](https://arxiv.org/abs/2606.23138)

**<font color=#1a73e8>作者：</font>** Gabriela F. Ciocarlie, Kathrin Grosse, Somesh Jha 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security remains a high-cost challenge, with many problems historically deemed inefficient to address or effectively unsolvable. A significant number of these problems stem from labor-intensive tasks that create bottlenecks in defensive approaches. Agentic AI has the potential to alleviate these bottlenecks by directly ingesting and reasoning over natural language or code, thereby expanding the scope of feasible defenses. In this paper, we map open security problems to emergent agentic AI capabilities. To illustrate this potential, we examine 16 case studies, including supply chain analysis, highlighting how agentic AI may benefit defenders.

---


### 25. [FlexServe: A Fast and Secure LLM Serving System for Mobile Devices with Flexible Resource Isolation](https://arxiv.org/abs/2606.23370)

**<font color=#1a73e8>作者：</font>** Yinpeng Wu, Yitong Chen, Lixiang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Device-side Large Language Models (LLMs) have grown explosively, offering stronger privacy and higher availability than their cloud-side counterparts. During LLM inference, both the model weights and the user data are valuable, and attackers may compromise the OS kernel to steal them. ARM TrustZone is the de facto hardware-based isolation technology on mobile devices, used to protect sensitive applications from a compromised OS. However, protecting LLM inference with TrustZone incurs significant overhead to both the secure inference and the normal aplications, due to two challenges: the inflexible resource isolation and the inefficient secure resource management.
To address these challenges, this paper presents FlexServe, a fast and secure LLM inference system for mobile devices. The key idea is to decouple the access permission from the management permission of secure resources, so that the normal-world OS cannot access them but can still manage them as usual. First, FlexServe introduces a Recallable Resource Isolation mechanism to construct Recallable Secure Memory (Flex-Mem) and a Recallable Secure NPU (Flex-NPU). They can only be accessed by the secure world, but can be efficiently allocated and reclaimed by the normal-world OS. Based on them, FlexServe further introduces a FlexServe Framework to run secure LLM inference in the secure world. It works together with the normal-world OS to perform cooperative secure memory management. We implement a prototype of FlexServe and compare it with two TrustZone-based strawman designs. The results show that FlexServe achieves average TTFT speedups of 10.05X over the strawman and 2.44X over an optimized strawman.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
