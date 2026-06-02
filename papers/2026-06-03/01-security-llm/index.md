# 🔐 大模型安全相关研究 | 2026年06月03日

> 本类共 **20** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [From Frontier to Shadow AI: A Simmering Threat to Assurance and Security in Critical Infrastructure](https://arxiv.org/abs/2606.00088)

**<font color=#1a73e8>作者：</font>** Mohan Baruwal Chhetri, Shahroz Tariq, Tooba Aamir 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Frontier AI systems, including large language models and emerging agentic AI tools, offer significant operational benefits but present unique challenges to critical infrastructure (CI) environments due to their non-deterministic and emergent properties. While formal adoption is inherently cautious and tightly controlled due to strict regulatory oversight, widespread accessibility has catalysed shadow AI: the unsanctioned use of frontier AI outside established organisational controls. In CI settings, shadow AI bypasses established assurance and oversight mechanisms, amplifying risks to data protection, decision reliability, and regulatory compliance, with potential consequences for essential service delivery. We present the first empirical study of shadow AI in CI environments, characterising it as a systemic socio-technical condition of assurance erosion. Drawing on semi-structured interviews with senior executives and functional leaders across 27 Australian CI organisations (Communications, Energy, and Water and Sewerage sectors), we analyse how shadow AI manifests in practice, how it interacts with existing technical and governance controls, and the resulting security, assurance, and compliance risks. We develop an empirically derived threat model identifying three primary mechanisms of security degradation: (i) boundary bypass, where data flows circumvent established perimeters; (ii) unassessed capability expansion, where embedded AI features introduce latent risks; and (iii) loss of observability via governance circumvention, undermining forensic auditability and least-privilege enforcement. Our findings demonstrate that shadow AI introduces unmanaged risks that fundamentally challenge existing security and compliance frameworks, necessitating tailored, pathway-aligned governance and control strategies.

---


### 2. [Persona Attack: Incremental Memory Injection Jailbreak Attack against Large Language Models](https://arxiv.org/abs/2606.00150)

**<font color=#1a73e8>作者：</font>** Junyoung Park, Seongyong Ju, Sunghwan Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As Large Language Models evolve for user convenience, vulnerability to jailbreak attacks continues to be reported despite ongoing efforts in safety training. Traditional jailbreak techniques typically focus on a single prompt injection, neglecting the models' ability to remember the flow of conversation and the user's instructions. In this paper, we propose Persona Attack, a memory injection based jailbreak method that manipulates the model's context window through a step by step approach. Experimental results from applying Persona Attack to several widely used LLMs reveal that, as injections accumulate in memory, models increasingly prioritize these instructions over their internal safety alignment mechanisms. Furthermore, our experiments empirically demonstrate that the attack success rate varies not only according to the memory implementation of the model, but also combinations of instructions and can reach 95% under specific instruction configurations.

---


### 3. [PrivacyPeek: Auditing What LLM-Based Agents Acquire, Not Just What They Say](https://arxiv.org/abs/2606.00152)

**<font color=#1a73e8>作者：</font>** Mingxuan Zhang, Jiahui Han, Dadi Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are rapidly advancing, autonomously invoking external tools to complete multi-step tasks for users. However, agents often acquire more sensitive information than the task requires. Existing privacy benchmarks audit what the agent's response or outgoing actions disclose, but overlook the acquisition stage where data first enters the agent's context. The over-acquired information is then one careless action or one attack away from an outright leak. To assess its prevalence, we introduce \emph{PrivacyPeek}, a benchmark for evaluating acquisition-stage privacy leakage of LLM-based agents, with $1{,}182$ cases across $7$ acquisition behaviours and $16$ application domains. Specifically, \emph{Acquisition Inspection} examines the agent's tool-call trajectory, both the tools it invokes and the data it receives, to detect when it acquires sensitive information beyond the task scope. \emph{Probe Elicitation} then issues a follow-up probe and measures how readily an attacker could elicit sensitive information the agent acquired but did not disclose. Our experiments on 10 LLM-based agents across 4 model families show that the unnecessary acquisition of sensitive information is widespread. In addition, we observe a correlation between the task-completion capability and acquisition-stage leakage. Prompt-level defences reduce only a small fraction of acquisition-stage leakage, leaving the majority unmitigated. These results make auditing acquisition-stage privacy both urgent and necessary. Our dataset and code are available at this https URL.

---


### 4. [A Protocol-Language Model for Network Intrusion (Without Deep Packet Inspection)](https://arxiv.org/abs/2606.00155)

**<font color=#1a73e8>作者：</font>** Vivek Kumar Sharma  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern network intrusion detection systems (NIDS) are caught in a structural contradiction: the protocols carrying the highest threat intelligence are precisely those encrypted under TLS 1.3 and QUIC, where payload inspection yields nothing. We ask a simpler question -- what if the attack signature is not in the bytes, but in the rhythm? -- and answer it by treating network flows as a language whose grammar is written entirely in L3/L4 packet metadata: length, inter-arrival time, TTL, TCP flags, and hashed port numbers. We present PLM-NIDS, which proves three claims in sequence. (1) The grammar exists and is learnable: a RWKV-4 state-space model trained on 344,232 unlabelled Monday flows achieves a causal LM validation loss of 0.204, demonstrating that benign traffic has predictable, statistically consistent structure. (2) Attacks violate this grammar: the per-flow perplexity score cleanly separates benign from attack flows with PR-AUC = 0.93 using zero attack labels at training time. (3) This separation is architecturally nontrivial: an LSTM trained on identical token sequences degenerates to a majority-class predictor (ROC-AUC approximately 0.50, F1 = 0.91 by always predicting "attack"), proving that RWKV's causal pre-training provides an inductive bias unavailable to direct classifiers. Supervised fine-tuning further raises PR-AUC to 0.94 and ROC-AUC to 0.75, with a precision of 97.7% at the calibrated operating threshold. The RWKV backbone's O(T) recurrent inference enables per-packet streaming without flow buffering, making PLM-NIDS operationally viable at line rate. Because it reads only IP/TCP/UDP headers, it is inherently encryption-agnostic: TLS 1.3, QUIC, and future encrypted protocols are handled transparently.

---


### 5. [DataShield: Safety-degrading Data Filtering for LLM Benign Instruction Fine-Tuning](https://arxiv.org/abs/2606.00160)

**<font color=#1a73e8>作者：</font>** Junbo Zhang, Qianli Zhou, Xinyang Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) suffer from degraded safety capabilities even when fine-tuned with benign datasets. However, existing methods for identifying safety-degrading samples in benign datasets suffer from high computational costs and significant noise issues. In this paper, we propose DataShield to efficiently and effectively identify potential safety-degrading samples. Our key intuition is based on the observation that benign fine-tuning increases the overall response compliance of LLMs. DataShield's key technical insight is to quantify each sample's contribution to the model's compliance behavior as its safety degradation score. DataShield consists of three core components: (1) Compliance Vector Extraction, which captures the LLM's compliance behavior tendency; (2) a novel Compliance-Aware Score (CAS), which automatically identifies the optimal safety-critical layer; and (3) Safety-degrading Sample Filtering, which quantifies the projection shift of training data along the compliance direction. Extensive experimental evaluation on Llama3-8B, Llama3.1-8B, and Qwen2.5-7B using the Alpaca and Dolly benign datasets validates our method's effectiveness in identifying high-risk and low-risk data subsets. We also observe that open-ended question answering is more likely to trigger safety degradation, and corresponding responses tend to be longer. We hope this work can provide new insights into data-centric defense methods. The source code is available at: this https URL.

---


### 6. [How to Compare the Security of Code Written by Humans to LLM-generated Code](https://arxiv.org/abs/2606.00186)

**<font color=#1a73e8>作者：</font>** Rebecca Balebako, Jasmine Egl  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are rapidly transforming how software is created and maintained. Comparing LLM-generated code against human-written standards is essential to determine whether these new tools uphold or erode the security baselines established by professional developers. Yet, we lack a standardized method for empirically comparing the security of code produced through human-LLM collaboration against LLM-only, or traditional human-only methods. To facilitate this, we propose an automated framework for conducting comparative studies across human-only, LLM-only, and hybrid conditions. Our approach automates the logging of prompts, timing, and experimental settings, measuring outcomes through multi-dimensional static and dynamic quality analysis. We provide an open-source implementation of this framework to ensure that future researchers can conduct reproducible, species-fair experiments. Importantly, we validate the framework via a feasibility study, providing an experimental blueprint for ``species-fair'' comparisons between human and AI subjects. By sharing lessons learned, we establish a foundation for empirical research on human and LLM-generated code for software security.

---


### 7. [Beyond Edge Coverage: Per-Task Data-Flow Extraction at Kernel Function Boundaries via LLVM](https://arxiv.org/abs/2606.00455)

**<font color=#1a73e8>作者：</font>** Yunseong Kim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Coverage-guided kernel fuzzers such as syzkaller rely on edge coverage (trace-pc) as their sole feedback signal. This context-blind approach cannot distinguish execution paths that differ only in argument values. for example, two invocations of copy_from_user() with different size parameters hit identical basic blocks yet have vastly different security implications. We present BOUNDARY FLOW, an LLVM-based instrumentation framework that extends Linux KCOV with data-flow extraction of function arguments and return values. A compiler pass (-fsanitize-coverage=dataflow-args, dataflow-ret) emits lightweight callbacks capturing a structured tuple <PC, arg_idx, arg_size, ptr, offsets[]> at function entry and <PC, ret_size, ptr, offsets[]> at return. Composite types are automatically decomposed via DWARF DICompositeType metadata with zero source annotation. A separate kernel device(/sys/kernel/debug/kcov_dataflow) provides lock-free per-task ring buffers with no inter ference to existing KCOV or syzkaller infrastructure. We demonstrate dual utility: fuzzers gain state-aware feedback for mutation guidance into value-dependent state transitions, and security analysts obtain deterministic argument records for root-cause analysis without printk or kprobe overhead. A post-compilation pipeline (rustc, opt, llc) enables Rust kernel module instrumentation without modifying rustc, the only runtime method for capturing Rust function arguments given that drgn/vmcore fails under-O2 DWARF elision. Evaluated on five vulnerability classes (OOB, UAF, double-free, 10 deep chain propagation, Rust FFI, Rust for Linux Modules) with <3% overhead on instrumented paths.

---


### 8. [Confused ChatGPT: Cross-App Context Poisoning via First-Party APIs](https://arxiv.org/abs/2606.00485)

**<font color=#1a73e8>作者：</font>** Chao Wang, Somesh Jha, Zhiqiang Lin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> ChatGPT Apps, launched by OpenAI on Oct. 6, 2025, introduce an app-in-app paradigm in which third-party applications share a single chat context with the user and with every other connected app. The ecosystem grew from 122 apps in Dec. 2025 to 888 by May 2026, yet its security has remained uninvestigated. We identify cross-app context poisoning, a variant of indirect prompt injection distinguished by three properties: 1) the injection persists in the shared chat context across turns; 2) the effect surfaces through a different co-resident app the user later invokes; and 3) the delivery vectors are first-party APIs exposed to every connected app. We find multiple APIs capable of writing app-controlled content into the shared context, with sendFollowUpMessage as the most direct and potent channel. Two undocumented parameters that the runtime silently accepts, systemPrompt and isVisible, amplify this channel to silent, system-priority writes. Leveraging this channel, we realize a confused-deputy attack in which a malicious app poisons the context so that the LLM, consulting that context, enables manipulation against benign co-resident apps. We demonstrate two payload styles (conditional and imperative) and evaluate them across six current ChatGPT models. The root cause is architectural: the LLM's context is a persistent, flat, untagged data store shared by user and apps, with no isolation. Every mature multi-tenant platform, from Multics virtual memory to Android UIDs and iOS sandbox profiles, paid the isolation cost before admitting third parties; ChatGPT Apps did not. Fixing this requires an architectural change, not a patch. We disclosed our findings to OpenAI; the undocumented parameters remain accessible at the time of writing, and the architectural gap is by design: the shared context that enables cross-app composition is the same flat namespace that enables cross-app poisoning.

---


### 9. [The Invitation Trap: Proactive Availability Backdoor in LLMs via Conversational Induction](https://arxiv.org/abs/2606.00654)

**<font color=#1a73e8>作者：</font>** He Wang, Jun Feng, Hong Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Current backdoor attacks against LLMs are typically manipulated by the attacker and remain passive. In this paper, we introduce the \textbf{Proactive Availability Backdoor (PAB)}, a novel paradigm that shifts the attack vector from passive waiting to active social engineering. By weaponizing the inherent helpfulness of aligned LLMs, PAB proactively traps users into executing trigger-implanted queries by offering suggestions, achieving high aggressiveness, precision and stealthiness. To rigorously evaluate its threat in a real-life context, we introduce a dual-agent ecological simulation framework based on selected dimensions of the Five-Factor Model, and deploy PAB with few-shot prompts. Being validated on different models and domains, PAB performs remarkably and its effective attack success rate, which calculates the joint probability of attack incidence rate and attack success rate, goes to \textbf{73.1\%}. We also introduce \textbf{Anti-PAB}, a defense method tailored for PAB. Our findings reveal that the helpfulness of LLMs can be weaponized to compromise availability, exposing a serious hidden threat to LLMs users. We release all the scripts and datasets in the experiments at \texttt{this https URL}.

---


### 10. [NeuroLog: Reasoning You Can Audit -- Neuro-Symbolic Vulnerability Discovery via LLM Facts, Datalog, and SMT](https://arxiv.org/abs/2606.00669)

**<font color=#1a73e8>作者：</font>** Sanjay Rawat  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vulnerability discovery on C/C++ source asks the analyst to choose between heavyweight static analysers, which need a working build before a single query runs, and free-form LLMs, which read source readily but invent details and lose track of cross-function dataflow on real codebases. We present NeuroLog, an end-to-end build-free pipeline that assigns each layer the role it is uniquely good at: an LLM extracts typed dataflow facts one function at a time; a Souffle rule mesh composes those facts into cross-function findings; a Z3 post-pass filters infeasible findings and emits a SAT model for each survivor. To go beyond pure static reasoning we also fold in runtime evidence: likely range invariants from a handful of corpus seeds tighten the SMT problem at near-zero cost. A second LLM agent reads each SAT model and writes a Python program that produces a candidate crashing input, validated by an AddressSanitizer harness. Combining static-narrowing-SMT (Saturn, Pinpoint) and Datalog-with-SMT (Formulog) is prior art; new here are an LLM-derived fact base, a no-build pipeline, and the SAT model as an artifact (input to crash synthesis) rather than a yes/no verdict. Across stb, cJSON, libxml2, an FFmpeg demuxer slice, and curl 8.3.0, NeuroLog re-discovers eight CVE-class issues end-to-end, including the CVSS-9.8 SOCKS5 heap overflow CVE-2023-38545, each ASan-confirmed. On libarchive HEAD we surface five memory-safety bugs (four previously unreported) across the cpio reader and the XAR/WARC/7zip writers; all filed upstream, several fixes merged, with the cpio use-after-free acknowledged in seven hours. Extraction takes ~37 s and $0.005 on stb; crash synthesis turned a static finding into a 102-byte stb_vorbis crash in two LLM iterations (no fuzzer); a likely-invariant filter from three Matroska seeds eliminates 13.2% of the FFmpeg-demuxer feasible set.

---


### 11. [Quality-Diversity Evolution for Discovering Diverse Vulnerabilities in LLM Safety](https://arxiv.org/abs/2606.00801)

**<font color=#1a73e8>作者：</font>** Subhadip Mitra  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Current approaches to LLM adversarial testing suffer from coverage gaps: manual red-teaming does not scale, LLM-as-attacker methods exhibit mode collapse, and gradient-based approaches produce uninterpretable gibberish. We introduce a quality-diversity evolutionary framework that operates at the semantic level, evolving interpretable attack strategies rather than token sequences. Using MAP-Elites, we maintain a diverse archive of attacks across behavioral dimensions (strategy type, encoding method, prompt length). In experiments across GPT-4o-mini, Claude 3.5 Sonnet, Gemini 2.0 Flash, and an open-weight coding model (Devstral-small-2), we discover distinct vulnerability profiles: GPT-4o-mini is vulnerable to hypothetical and multi-turn framing combined with ROT13 encoding (fitness 0.8), Gemini to direct attacks with ROT13 and multi-turn with Leetspeak (0.8), while Claude shows uniformly ambiguous responses across all strategies (max 0.4). The semantic representation produces interpretable attacks that reveal systematic, model-specific weaknesses, providing actionable insights for improving LLM safety and a reproducible baseline for evaluating future frontier models. Code and experiment artifacts are released at this https URL.

---


### 12. [Cross-Generational Transfer of Adversarial Attacks Reveals Non-Monotonic Safety Alignment in LLMs](https://arxiv.org/abs/2606.00813)

**<font color=#1a73e8>作者：</font>** Subhadip Mitra  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety alignment in LLMs does not improve monotonically across model generations. Studying four generations of Google's Gemma family (7B-31B) with quality-diversity evolution (MAP-Elites) as an automated red-teaming probe, we find that Gemma 3 (12B) exhibits 68.7% +/- 5.7% attack success rate (ASR; mean +/- std, 3 seeds), significantly higher than its predecessor Gemma 2 (45.5% +/- 7.2%; p = 0.030, paired bootstrap) and its successor Gemma 4 (33.9% +/- 1.8%). Replaying evolved attack archives across generations reveals that attacks from other generations transfer to Gemma 3 at 44-46% but only 14-18% to Gemma 4, indicating that Gemma 4's safety gains generalize beyond the attack distributions evolved against earlier generations. Under our 8B judge, copyright and cybercrime vulnerabilities register at near-100% across all generations, though a second-judge audit (Section 6) suggests the copyright result is sensitive to judge choice. Misinformation ASR jumps from 29% to 99% between Gemma 2 and Gemma 3 and remains elevated at 77% in Gemma 4, indicating the regression was not fully addressed. These patterns are invisible to static benchmarks and emerge only through adaptive, longitudinal probing. All experiments use 3 random seeds with a unified self-hosted judge; code and artifacts are available at this https URL.

---


### 13. [Benchmarking Security Risk Detection and Verification in Open Agentic Skill Ecosystems](https://arxiv.org/abs/2606.00925)

**<font color=#1a73e8>作者：</font>** Ismail Hossain, Sai Puppala, Zhuoran Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open agent platforms allow community contributors to publish reusable skills that agents can invoke at runtime. This extensibility also creates a supply-chain risk: malicious contributors can hide harmful behavior inside skills that appear benign under superficial inspection. However, existing defenses are hard to evaluate because there is no benchmark that measures both malicious-skill detection and runtime verification. We present SkillVetBench, a two-stage security vetting benchmark for open agentic skill ecosystems. The first stage performs semantic vetting over each skill's natural-language specification to detect hidden malicious intent. The second stage executes flagged skills in an instrumented sandbox to observe runtime behavior and collect auditable evidence. We build a benchmark from confirmed malicious skills in the live OpenClaw ecosystem, including samples from the recent ClawHavoc supplychain campaign. Unlike static-only methods, SkillVetBench verifies detected threats with execution traces. Our experiments show that: (1) semantic-only and signature-based baselines are insufficient, missing up to 89\% of malicious skills whose threats arise from natural-language instructions, multicomponent logic, or cross-component interactions; (2) runtime attacks are concentrated in a small set of high-permission primitives, especially exec, write\_file, install\_skill, and spawn; and (3) SkillVetBench provides case studies in which sandbox execution directly supports malicious verdicts with concrete runtime evidence.

---


### 14. [BraveGuard: From Open-World Threats to Safer Computer-Use Agents](https://arxiv.org/abs/2606.01166)

**<font color=#1a73e8>作者：</font>** Yunhao Feng, Yifan Ding, Xiaohu Du 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Computer-use agents extend language models from text generation to sustained interaction with files, terminals, browsers, and external tools. This shift creates safety risks that are difficult to detect from isolated prompts or final responses, because harm often emerges only through multi-step execution traces whose individual actions appear locally benign. We introduce BraveGuard, a self-evolving defense framework for training guard models from open-world threat signals and realistic agent trajectories. BraveGuard mines recent research sources to identify emerging risks and attack patterns, instantiates them as executable computer-use tasks, collects agent rollouts, and derives trajectory-level supervision for guard model training. As new threats and validation failures appear, the pipeline can be repeated, yielding an adaptive defense loop rather than a static, benchmark-driven training process. We instantiate BraveGuard by training multiple guard backbones, including Qwen3-Guard and Llama-Guard variants, and evaluate the resulting guards on trajectory-level agent-safety benchmarks. BraveGuard consistently improves safety detection across computer-use trajectories. On AgentHazard, it substantially improves detection accuracy over off-the-shelf guard models, with accuracy increasing from 38.79% to 82.38% under the averaged guard-model setting. These results show that guard supervision grounded in open-world threat discovery and realistic agent execution can improve safety monitoring beyond fixed taxonomies and synthetic prompt-level data. BraveGuard offers a scalable path toward adaptive defenses for computer-use agents facing evolving real-world risks.

---


### 15. [Needles at Scale: LLM-Assisted Target Selection for Windows Vulnerability Research](https://arxiv.org/abs/2606.01364)

**<font color=#1a73e8>作者：</font>** Michael J. Bommarito II  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The attack surface of a modern operating system is a haystack: thousands of signed binaries and millions of functions, almost none relevant to any given vulnerability. A human analyst or an LLM agent must pick the function worth reading before analyzing it. At whole-OS scope, this target selection, not the analysis, is the binding constraint. We present Symbolicate-Enrich-Sample, a low-cost batch pipeline that turns a corpus of production Windows binaries into a queryable, priority-ranked research queue. We (i) recover function-level symbols for stripped vendor binaries by auto-fetching the public symbol files and joining them to a recovered call graph; (ii) attach cheap, deterministic structural features to each named function and, conditioned on those features, use a low-cost language model to assign a reachability tier, a risk level, a bug-class hypothesis, and a rationale; and (iii) draw diverse, prioritized batches via a priority-weighted importance sampler. The contribution is a selection substrate: the prioritization layer a downstream detector or LLM agent runs on top of. Across a whole Windows image of 7,231,419 functions, the labels are markedly selective, and stacking deterministic filters on them leaves a ~22K-function shortlist: the candidate needles, few enough for a human or agent to work through. We characterize the pipeline's selectivity and its failure modes, describe the methodology, and report aggregate statistics; we withhold the derived dataset for legal and dual-use reasons.

---


### 16. [Agent Operating Systems (AOS): Integrating Agentic Control Planes into, and Beyond, Traditional Operating Systems](https://arxiv.org/abs/2606.01508)

**<font color=#1a73e8>作者：</font>** Ankur Sharma, Deep Shah  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Traditional operating systems were designed around deterministic programs, explicit control flow, and human initiated workflows. Their core abstractions processes, threads, system calls, files, and permissions assume bounded behavior and predictable interaction patterns. Agentic AI systems introduce a different execution model: long-lived, goal-directed entities that reason probabilistically, invoke tools dynamically, and adapt behavior based on feedback. While agents can be implemented as user-space applications today, their execution characteristics stress OS boundaries in scheduling, memory and state management, security, observability, and governance. This paper introduces the concept of an Agent Operating System (AOS), a systems architecture that integrates an agentic control plane into existing operating systems or, in some models, subsumes selected OS responsibilities over time. We provide a precise definition of an AOS, explicit assumptions and non-goals, and a structured decomposition of AOS responsibilities into schedulers, context and memory management, tool and capability registries, policy and trust enforcement, and observability and audit. We analyze limitations of classical OS abstractions for agent workloads, propose integration models from user-space runtimes to distributed control planes, and map AOS concepts onto Linux and Windows primitives. We present security and safety implications, including agent specific threat models, and define evaluation criteria that emphasize deterministic enforcement, auditability, and operator comprehensibility. The objective is not to replace operating systems wholesale, but to establish a rigorous systems foundation for agentic computation that remains controllable, accountable, and secure at scale.

---


### 17. [Defenses & Enablers For Skill Injection Attacks on Terminal Based Agents](https://arxiv.org/abs/2606.01567)

**<font color=#1a73e8>作者：</font>** Yoshinari Fujinuma, Varun Gangal, Traian Rebedea 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly rely on reusable skills i.e. documents describing task-specific procedures. However, this introduces a new attack surface for agents to manage. We study two complementary directions for this threat. First, we evaluate guardian-based defenses: an intermediary LLM agent that acts as a mediator for skill file access (dynamic guardian) or pre-rewrites these files at build time (static guardian). Across three LLM agent families, our guardians cut attack success rate (ASR) by well over half while preserving task utility. Second, we stress test them through attack reframing using four attacks that preserve the malicious instruction but change the phrasing. For non-guardian setup, the reframing pushes the ASR up to 81.4\%, but the dynamic guardian brings it down to 18.6\%, showing that real-time mediation is a robust defense.

---


### 18. [IstGPT: LLM-based Anomaly Detection for Spatial-Temporal Graph in Industrial Systems](https://arxiv.org/abs/2606.01691)

**<font color=#1a73e8>作者：</font>** Yuchen Zhang, Ning Xi, Pengbin Feng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Industrial Internet systems face increasing threats from sophisticated industrial control system (ICS) attacks, resulting in critical safety incidents. However, existing tools exhibit limited effectiveness in real-time anomaly detection due to the complex dependencies among sensors and actuators. To tackle this, we present IstGPT, the first industrial anomaly detection tool based on LLMs and graph learning to provide real-time protection against a wide range of ICS attacks. IstGPT achieves fine-grained and precise modeling on spatial-temporal dependencies in industrial cyber-physical systems. It first leverages industrial multi-modal knowledge, including operational data, technical documents, and system diagrams, to extract sensor-actuator dependency graphs via multi-stage prompt engineering. Then, LLM-Optimation iteratively refines the graph based on node accuracy, edge consistency, and logical coherence. Finally, IstGPT integrated improved graph neural networks with an encoder-decoder architecture to detect anomalies via reconstruction errors. We evaluate IstGPT against 12 state-of-the-art baselines on 9 datasets, including 2 public, 6 simulated, and a real-world robotic arm dataset. IstGPT achieves the best F1-scores and eTaF1 (a newer time-aware metric) across nine datasets. We further discuss the feasibility of deploying IstGPT in real-world industrial scenarios.

---


### 19. [Benign Inputs, Harmful Outputs: Cross-Modal Jailbreaking via Distributed Semantic Recomposition](https://arxiv.org/abs/2606.01837)

**<font color=#1a73e8>作者：</font>** Yani Wang, Yilong Yang, Yang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have recently demonstrated remarkable capabilities in content synthesis and autonomous reasoning. Previous safety guardrails are primarily designed for unimodal textual input interception, leaving them vulnerable to cross-modal jailbreak attacks. However, regardless unimodal textual attack or cross-modal jailbreak, typically inclusive part of explicit harmful or sensitive content at the input level, which is called Harm-Bearing. It allow the model's safety filters to detect and block such content easily. To address this limitations, we propose Distributed Semantic Recomposition (DSR), a novel cross-modal jailbreak framework that decomposes harmful intent into a set of benign textual and visual primitives. By exploiting the model's reasoning ability, DSR enables the latent fusion of these seemingly innocent components into harmful outputs during the cross-modal inference phase. Extensive experiments on multiple commercial MLLMs pipelines demonstrate that DSR achieves superior attack success rates while maintaining an extremely low or even negligible input toxicity rate. Our findings uncover a critical Utility-Safety Paradox in MLLMs, where the model's instruction-following proficiency facilitates its own cognitive exploitation. Content Warning: This paper contains harmful model responses.

---


### 20. [AgentRedBench: Dynamic Redteaming and Integration-Aware Defense for LLM Agents over SaaS Integrations](https://arxiv.org/abs/2606.02240)

**<font color=#1a73e8>作者：</font>** Hiskias Dingeto, Will Leeney  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Indirect prompt injection in tool-use agents is a concrete production threat: LLM agents read from integrations (third-party services such as Gmail, Salesforce, or Jira accessed through tool calls) whose response content the user neither writes nor controls. Existing benchmarks under-measure the threat: most cover only a handful of integrations with the same attack payload replayed across runs, and open-source guards are trained on chat-style data rather than tool-response content. We introduce AGENTREDBENCH, a dynamic LLM-driven redteaming benchmark of 215 subtle underspecified authorization (attacks at the boundary of what the user's request authorises) scenarios across 24 enterprise integrations in nine functional families and five attack types. Across an eight-model panel (Anthropic, OpenAI, Google), no-guard ASR (attack success rate) ranges from 32% (Claude Sonnet 4.6) to 81% (Gemini 3 Flash). To keep the scenario set out of training corpora and preserve headline ASR meaning over time, we release the codebase, integration schemas, and AGENTREDGUARD model openly; the canonical scenarios are evaluated through a maintainer-mediated channel with immutable versioning. We release AGENTREDGUARD alongside the benchmark: a guard trained on an integration-diverse corpus of adversarial tool-response content. AGENTREDGUARD cuts panel ASR from 69.9% to 2.4% at 0.37% false-positive rate, outperforming every open-source baseline with non-trivial detection (Llama Guard, PromptGuard 2, ProtectAI) on both axes. Cross-integration and cross-attack type holdouts both confirm the gain transfers beyond the training subset.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
