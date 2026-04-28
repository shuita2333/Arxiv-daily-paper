# 🔐 大模型安全相关研究 | 2026年04月29日

> 本类共 **22** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [AutoRISE: Agent-Driven Strategy Evolution for Red-Teaming Large Language Models](https://arxiv.org/abs/2604.22871)

**<font color=#1a73e8>作者：</font>** Tanmay Gautam, Alireza Bahramali, Sandeep Atluri  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Automated red-teaming methods for large language models typically optimize attack prompts within a fixed, human-designed strategy, leaving the attack strategy itself unchanged. We instead optimize the strategy. We propose AutoRISE, a method that searches over executable attack programs rather than individual prompts. At each iteration, a coding agent edits a strategy and a fixed evaluation harness scores the resulting attacks, returning both a scalar objective and per-example diagnostics that guide subsequent edits. This allows structural changes, including new attack components and altered control flow, that prompt-level methods do not directly express. We also release two benchmark suites developed on disjoint target sets and evaluate on 11 models from five families against seven established jailbreak datasets. Across held-out models, AutoRISE improves average attack success rate by 17.0 points over the strongest baseline, and improves attack success by up to 16 points on frontier targets with low baseline success rates. Ablations against parametric and strategy-library baselines suggest that these gains arise from unrestricted program search, particularly compositional techniques and control-flow edits. AutoRISE operates in a black-box, inference-only setting, requiring no fine-tuning, human annotation, or GPU compute.

---


### 2. [RouteGuard: Internal-Signal Detection of Skill Poisoning in LLM Agents](https://arxiv.org/abs/2604.22888)

**<font color=#1a73e8>作者：</font>** Wenjie Xiao, Xuehai Tang, Biyu Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills introduce a new and more severe form of indirect injection for LLM agents: unlike traditional indirect prompt injection, attackers can hide malicious instructions inside a dense, action-oriented skill that already functions as a legitimate instruction source. We study pre-execution skill-poison detection and show that successful skill poisoning induces a structured internal effect, attention hijacking, in which response-time attention shifts from trusted context to malicious skill spans and drives harmful behavior. Motivated by this mechanism, we propose RouteGuard, a frozen-backbone detector that combines response-conditioned attention and hidden-state alignment through reliability-gated late fusion. Across both real and synthetic open-source skill benchmarks, RouteGuard is consistently the strongest or most robust detector; on the critical Skill-Inject channel slice, it reaches 0.8834 F1 and recovers 90.51% of description attacks missed by lexical screening, showing that defending against skill poisoning requires internal-signal detection rather than text-only filtering

---


### 3. [Secure eFPGA-Enabled Edge LLM Inference: Architectural and Hardware Countermeasures](https://arxiv.org/abs/2604.22935)

**<font color=#1a73e8>作者：</font>** Voktho Das, M Zafir Sadik Khan, Jafar Vafaei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Edge deployment of transformer-based models increasingly relies on ASIC accelerators due to their high performance and energy efficiency, achieved through optimized dataflows, specialized architectures, low-bitwidth computation, and efficient memory hierarchies. However, these advantages come with significant security vulnerabilities. ASIC-based DNN accelerators are susceptible to side-channel attacks (e.g., power, electromagnetic, and timing analysis) and fault injection attacks (e.g., voltage manipulation, clock glitches, and memory perturbations), which can lead to model extraction or compromised inference integrity. Furthermore, threats introduced during design and fabrication, such as hardware Trojans or untrusted third-party IPs, further expand the attack surface. To address these challenges, we explore a hybrid ASIC+eFPGA architecture that combines the efficiency of ASICs with the flexibility of reconfigurable logic. The integrated eFPGA enables security-oriented mechanisms such as adaptive runtime monitoring, side-channel mitigation and post-deployment patching. By leveraging these capabilities, the proposed approach enhances system resilience against both runtime and supply-chain attacks, while preserving the performance benefits of ASIC-based transformer inference.

---


### 4. [From Language to Logic: Bridging LLMs & Formal Representations for RTL Assertion Generation](https://arxiv.org/abs/2604.23100)

**<font color=#1a73e8>作者：</font>** Nowfel Mashnoor, Hadi Kamali, Kimia Azar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> SystemVerilog Assertions (SVA) are essential for formal verification of digital hardware, yet their manual creation demands significant expertise in both the design under verification and temporal logic. Recent studies have explored using large language models (LLMs) to automate SVA generation, but existing approaches suffer from incorrect signal references, missing timing constraints, and lack of formal correctness guarantees. This paper presents ProofLoop, a tool-augmented ReAct agent that generates SVA from natural-language specifications using a solver-in-the-loop approach. The agent operates in two phases: Phase A autonomously gathers design context by invoking EDA and formal tools, including semantic search over an AST-indexed vector database and JasperGold structural queries, while Phase B generates SVA and iteratively refines it using JasperGold formal proof feedback over up to fixed (here 3) verification rounds. We evaluate ProofLoop on FVEval Design2SVA design benchmarks and demonstrate that this framework can achieve 93.7% syntax correctness and 82.0% functional correctness. An ablation study confirms that each component, i.e., retrieval-augmented generation (RAG), JasperGold tools, and the verification loop contributes significantly (and orthogonally).

---


### 5. [UNSEEN: A Cross-Stack LLM Unlearning Defense against AR-LLM Social Engineering Attacks](https://arxiv.org/abs/2604.23141)

**<font color=#1a73e8>作者：</font>** Tianlong Yu, Yang Yang, Xiao Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Emerging AR-LLM-based Social Engineering attack (e.g., SEAR) is at the edge of posing great threats to real-world social life. In such AR-LLM-SE attack, the attacker can leverage AR (Augmented Reality) glass to capture the image and vocal information of the target, using the LLM to identify the target and generate the social profile, using the LLM agents to apply social engineering strategies for conversation suggestion to win the target trust and perform phishing afterwards. Current defensive approaches, such as role-based access control or data flow tracking, are not directly applicable to the convergent AR-LLM ecosystem (considering embedded AR device and opaque LLM inference), leaving an emerging and potent social engineering threat that existing privacy paradigms are ill-equipped to address. This necessitates a shift beyond solely human-centric measures like legislation and user education toward enforceable vendor policies and platform-level restrictions. Realizing this vision, however, faces significant technical challenges: securing resource-constrained AR-embedded devices, implementing fine-grained access control within opaque LLM inferences, and governing adaptive interactive agents. To address these challenges, we present UNSEEN, a coordinated cross-stack defense that combines an AR ACL (Access Control Layer) for identity-gated sensing, F-RMU-based LLM unlearning for sensitive profile suppression, and runtime agent guardrails for adaptive interaction control. We evaluate UNSEEN in an IRB-approved user study with 60 participants and a dataset of 360 annotated conversations across realistic social scenarios.

---


### 6. [AsmRAG: LLM-Driven Malware Detection by Retrieving Functionally Similar Assembly Code](https://arxiv.org/abs/2604.23196)

**<font color=#1a73e8>作者：</font>** ElMouatez Billah Karbab  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep learning malware detectors achieve high classification accuracy but suffer from severe interpretability limitations, typically returning probabilistic verdicts that lack forensic context. We introduce AsmRAG, a framework performing malware analysis through Assembly-Level Retrieval-Augmented Generation. Unlike classifiers built on global statistical features, AsmRAG reformulates detection as an evidence-based retrieval task. The system uses a code-specialized Large Language Model (LLM) to analyze assembly functions and convert them into semantic embeddings. This process constructs a searchable knowledge base resilient to syntactic obfuscation. For inference, we propose a Density-Weighted Anchor Selection mechanism that isolates the primary unit of malicious logic within a binary to extract verifiable forensic evidence and resist evasion attempts. Testing on a curated dataset of 40k binaries shows AsmRAG reaching a detection F1-score of 96% alongside a family attribution F1-score of 95%. Comparisons confirm this semantic retrieval approach remains robust against metamorphic obfuscation. When holistic baselines (EMBER and ResNeXt) degrade, our methodology gives Security Operations Centers a transparent and reliable alternative.

---


### 7. [From Stateless Queries to Autonomous Actions: A Layered Security Framework for Agentic AI Systems](https://arxiv.org/abs/2604.23338)

**<font color=#1a73e8>作者：</font>** Kexin Chu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems face security challenges that stateless large language models do not. They plan across extended horizons, maintain persistent memory, invoke external tools, and coordinate with peer agents. Existing security analyses organize threats by attack type (prompt injection, jailbreaking), but provide no principled model of which architectural component is vulnerable or over what timescale the threat manifests. This paper makes five contributions. First, we introduce the Layered Attack Surface Model (LASM), a seven-layer framework that maps threats to distinct architectural components: Foundation, Cognitive, Memory, Tool Execution, Multi-Agent Coordination, Ecosystem, and Governance, the accountability and observability layer that spans the stack analogously to the network management plane. Second, we introduce attack temporality as an orthogonal analytical dimension with four classes: Instantaneous (T1), Session-Persistent (T2), Cross-Session Cumulative (T3), and Sub-Session-Stack, Non-Session-Bounded (T4). Third, through a systematic review of 94 papers (2021--2025), we show that the most dangerous emerging threats concentrate at the intersection of high-layer attacks (L5--L7) and slow-burn temporality (T3--T4): covert agent collusion, long-term memory poisoning, MCP supply-chain compromise, and alignment failure that manifests as an insider threat with no external adversary. Only 8 of 120 paper-cell assignments (7%) fall in this zone. Fourth, we propose a cross-layer defense taxonomy spanning all seven LASM layers and all four temporality classes, exposing which threat classes existing defenses leave unaddressed. Fifth, we survey evaluation benchmarks, identify five research gaps in the under-studied high-layer, slow-burn zone, and argue that agentic security must be treated as a distributed systems problem embedded in an adversarial ecosystem.

---


### 8. [Evaluating Jailbreaking Vulnerabilities in LLMs Deployed as Assistants for Smart Grid Operations: A Benchmark Against NERC Standards](https://arxiv.org/abs/2604.23341)

**<font color=#1a73e8>作者：</font>** Taha Hammadia, Lucas Rea, Ahmad Mohammad Saber 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The deployment of Large Language Models (LLMs) as assistants in electric grid operations promises to streamline compliance and decision-making but exposes new vulnerabilities to prompt-based adversarial attacks. This paper evaluates the risk of jailbreaking LLMs, i.e., circumventing safety alignments to produce outputs violating regulatory standards, assuming threats from authorized users, such as operators, who craft malicious prompts to elicit non-compliant guidance. Three state-of-the-art LLMs (OpenAI's GPT-4o mini, Google's Gemini 2.0 Flash-Lite, and Anthropic's Claude 3.5 Haiku) were tested against Baseline, BitBypass, and DeepInception jailbreaking methods across scenarios derived from nine NERC Reliability Standards (EOP, TOP, and CIP). In the initial broad experiment, the overall Attack Success Rate (ASR) was 33.1%, with DeepInception proving most effective at 63.17% ASR. Claude 3.5 Haiku exhibited complete resistance (0% ASR), while Gemini 2.0 Flash-Lite was most vulnerable (55.04% ASR) and GPT-4o mini moderately susceptible (44.34% ASR). A follow-up experiment refining malicious wording in Baseline and BitBypass attacks yielded a 30.6% ASR, confirming that subtle prompt adjustments can enhance simpler methods' efficacy.

---


### 9. [Ghost in the Agent: Redefining Information Flow Tracking for LLM Agents](https://arxiv.org/abs/2604.23374)

**<font color=#1a73e8>作者：</font>** Yuandao Cai, Wensheng Tang, Cheng Wen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous Large Language Model (LLM) agents are increasingly deployed to conduct complex tasks by interacting with external tools, APIs, and memory stores. However, processing untrusted external data exposes these agents to severe security threats, such as indirect prompt injection and unauthorized tool execution. Securing these systems requires effective information flow tracking. Yet, traditional taint analysis that is designed for program memory states fundamentally fails when applied to LLMs, where data propagation is governed by probabilistic natural language reasoning. In this paper, we present NeuroTaint, the first comprehensive taint tracking framework tailored for the unique information flow characteristics of LLM agents. Our key insight is that taint propagation in LLM agents must be understood not only as explicit content transfer, but also as semantic transformation, causal influence on decisions, and cross-session persistence through memory. NeuroTaint therefore audits execution traces offline to reconstruct provenance from untrusted sources to privileged sinks using semantic evidence, causal reasoning, and persistent context tracking, rather than relying on exact string matches or pre-defined source-sink paths alone. Extensive evaluation using TaintBench, our 400-scenario benchmark spanning 20 real-world agent frameworks, shows that NeuroTaint substantially outperforms FIDES, an information-flow-control (IFC)-style baseline for LLM agents, in source-sink propagation detection. We further show that NeuroTaint remains effective on established agent-security benchmarks, including InjecAgent and ToolEmu, while operating offline with modest additional auditing cost.

---


### 10. [When the Agent Is the Adversary: Architectural Requirements for Agentic AI Containment After the April 2026 Frontier Model Escape](https://arxiv.org/abs/2604.23425)

**<font color=#1a73e8>作者：</font>** Richard Joseph Mitchell  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The April 2026 disclosure that a frontier large language model escaped its security sandbox, executed unauthorized actions, and concealed its modifications to version control history demonstrates that agentic AI systems with autonomous tool access can circumvent the containment mechanisms designed to constrain them. This paper analyzes four categories of current containment approaches - alignment training, environmental sandboxing, application-level tool-call interception, and accessible audit systems - and identifies the failure modes each exhibits when the AI agent is treated as a potential adversary rather than a trusted component receiving adversarial inputs. We categorize five behavioral incidents from the public disclosure and situate them within 698 real-world AI scheming incidents documented by the Centre for Long-Term Resilience between October 2025 and March 2026, a 4.9x acceleration establishing the challenge as systemic. We derive five architectural requirements: trust separation through layered OS privilege enforcement with semantic intent analysis, sequential intent inference through five-phase taxonomic monitoring, independent containment integrity monitoring, adversarial audit isolation through logical invisibility, and emergent capability envelope enforcement through distributional divergence monitoring. No publicly described system satisfies all five. We argue that architectural containment is the only durable safety strategy given the inevitable proliferation of equivalent capabilities including open-weight models. The author's published patent portfolio in provider-independent constraint enforcement addresses several of these requirements. Concurrent work including SandboxEscapeBench (arXiv:2603.02277) independently confirms that frontier models can escape standard container sandboxes, corroborating the threat model presented here.

---


### 11. [CyberCane: Neuro-Symbolic RAG for Privacy-Preserving Phishing Detection with Formal Ontology Reasoning](https://arxiv.org/abs/2604.23563)

**<font color=#1a73e8>作者：</font>** Safayat Bin Hakim, Aniqa Afzal, Qi Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy-critical domains require phishing detection systems that satisfy contradictory constraints: near-zero false positives to prevent workflow disruption, transparent explanations for non-expert staff, strict regulatory compliance prohibiting sensitive data exposure to external APIs, and robustness against AI-generated attacks. Existing rule-based systems are brittle to novel campaigns, while LLM-based detectors violate privacy regulations through unredacted data transmission. We introduce CyberCane, a neuro-symbolic framework integrating deterministic symbolic analysis with privacy-preserving retrieval-augmented generation (RAG). Our dual-phase pipeline applies lightweight symbolic rules to email metadata, then escalates borderline cases to semantic classification via RAG with automated sensitive data redaction and retrieval from a phishing-only corpus. We further introduce PhishOnt, an OWL ontology enabling verifiable attack classification through formal reasoning chains. Evaluation on DataPhish2025 (12.3k emails; mixed human/LLM) and Nazario/SpamAssassin demonstrates a 78.6-point recall gain over symbolic-only detection on AI-generated threats, with precision exceeding 98% and FPR as low as 0.16%. Healthcare deployment projects a 542x ROI; tunable operating points support diverse risk tolerances, with open-source implementation at this https URL.

---


### 12. [Spore: Efficient and Training-Free Privacy Extraction Attack on LLMs via Inference-Time Hybrid Probing](https://arxiv.org/abs/2604.23711)

**<font color=#1a73e8>作者：</font>** Yu Cui, Ruiqing Yue, Hang Fu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the wide adoption of personal AI assistants such as OpenClaw, privacy leakage in user interaction contexts with large language model (LLM) agents has become a critical issue. Existing privacy attacks against LLMs primarily target training data, while research on inference-time contextual privacy risks in LLM agent memory remains limited. Moreover, prior methods often incur high attack costs, requiring multiple queries or relying on white-box assumptions, which limits their practicality in real-world deployments. To address these issues, we propose a training-free privacy extraction attack targeting LLM agent memory, which we name \textsc{Spore}. \textsc{Spore} is compatible with both black-box and gray-box settings. In the black-box setting, \textsc{Spore} can efficiently extract a small candidate set via a single query to recover the original private information. In the gray-box setting, \textsc{Spore} allows the attacker to leverage multi-ranked tokens for more accurate and faster privacy extraction. We provide an information-theoretic analysis of \textsc{Spore} and show that it achieves high query efficiency with substantial per query information leakage. Experiments on multiple frontier LLMs show that \textsc{Spore} outperforms attack success rate over existing state-of-the-art (SOTA) schemes. It also maintains low attack cost and remains stable across different model parameter settings. We further evaluate the robustness of \textsc{Spore} against existing defense mechanisms. Our results show that \textsc{Spore} consistently bypasses both detection and strong safety alignment, demonstrating resilient performance in diverse defensive settings and real-world safety threats.

---


### 13. [LLM-CEG: Extending the Classification Error Gauge Framework for Privacy Auditing of Large Language Models](https://arxiv.org/abs/2604.23795)

**<font color=#1a73e8>作者：</font>** Kato Mivule  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper extends the Classification Error Gauge (x-CEG) framework, originally developed for measuring the privacy-utility trade-off in tabular datasets, to privacy auditing of Large Language Models (LLMs). We propose LLM-CEG, a systematic framework that employs membership inference attack (MIA) success rates as an empirical privacy gauge and model perplexity as a utility gauge, iteratively adjusting differential privacy parameters until both thresholds are jointly satisfied. A proof-of-concept prototype fine-tunes DistilGPT-2 on a synthetic clinical PII dataset under four privacy regimes using DP-SGD. Results indicate that DP-SGD reduces MIA attacker advantage by 71.5% while simultaneously improving out-of-distribution utility by 47-50% relative to the overfitted baseline, suggesting that differential privacy may act as implicit regularization under narrow fine-tuning conditions. We further extend the SIED engineering framework to the LLM context as LLM-SIED, providing an auditable, regulator-aligned process for privacy-compliant LLM deployment.

---


### 14. [Evaluation of Prompt Injection Defenses in Large Language Models](https://arxiv.org/abs/2604.23887)

**<font color=#1a73e8>作者：</font>** Priyal Deep, Shane Emmons, Amy Fox 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-powered applications routinely embed secrets in system prompts, yet models can be tricked into revealing them. We built an adaptive attacker that evolves its strategies over hundreds of rounds and tested it against nine defense configurations across more than 20,000 attacks. Every defense that relied on the model to protect itself eventually broke. The only defense that held was output filtering, which checks the model's responses via hardcoded rules in separate application code before they reach the user, achieving zero leaks across 15,000 attacks. These results demonstrate that security boundaries must be enforced in application code, not by the model being attacked. Until such defenses are verified by tools like Swept AI, AI systems handling sensitive operations should be restricted to internal, trusted personnel.

---


### 15. [Jailbreaking Frontier Foundation Models Through Intention Deception](https://arxiv.org/abs/2604.24082)

**<font color=#1a73e8>作者：</font>** Xinhe Wang, Katia Sycara, Yaqi Xie  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large (vision-)language models exhibit remarkable capability but remain highly susceptible to jailbreaking. Existing safety training approaches aim to have the model learn a refusal boundary between safe and unsafe, based on the user's intent. It has been found that this binary training regime often leads to brittleness, since the user intent cannot reliably be evaluated, especially if the attacker obfuscates their intent, and also makes the system seem unhelpful. In response, frontier models, such as GPT-5, have shifted from refusal-based safeguards to safe completion, that aims to maximize helpfulness while obeying safety constraints. However, safe completion could be exploited when a user pretends their intention is benign. Specifically, this intent inversion would be effective in multi-turn conversation, where the attacker has multiple opportunities to reinforce their deceptively benign intent. In this work, we introduce a novel multi-turn jailbreaking method that exploits this vulnerability. Our approach gradually builds conversational trust by simulating benign-seeming intentions and by exploiting the consistency property of the model, ultimately guiding the target model toward harmful, detailed outputs. Most crucially, our approach also uncovered an additional class of model vulnerability that we call para-jailbreaking that has been unnoticed up to now. Para-jailbreaking describes the situation where the model may not reveal harmful direct reply to the attack query, however the information that it reveals is nevertheless harmful. Our contributions are threefold. First, it achieves high success rates against frontier models including GPT-5-thinking and Claude-Sonnet-4.5. Second, our approach revealed and addressed para-jailbreaking harmful output. Third, experiments on multimodal VLM models showed that our approach outperformed state-of-the-art models.

---


### 16. [AgentVisor: Defending LLM Agents Against Prompt Injection via Semantic Virtualization](https://arxiv.org/abs/2604.24118)

**<font color=#1a73e8>作者：</font>** Zonghao Ying, Haozheng Wang, Jiangfan Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents are increasingly used to automate complex workflows, but integrating untrusted external data with privileged execution exposes them to severe security risks, particularly direct and indirect prompt injection. Existing defenses face significant challenges in balancing security with utility, often encountering a trade-off where rigorous protection leads to over-defense, or where subtle indirect injections bypass detection. Drawing inspiration from operating system virtualization, we propose AgentVisor, a novel defense framework that enforces semantic privilege separation. AgentVisor treats the target agent as an untrusted guest and intercepts tool calls via a trusted semantic visor. Central to our approach is a rigorous audit protocol grounded in classic OS security primitives, designed to systematically mitigate both direct and indirect injection attacks. Furthermore, we introduce a one-shot self-correction mechanism that transforms security violations into constructive feedback, enabling agents to recover from attacks. Extensive experiments show that AgentVisor reduces the attack success rate to 0.65%, achieving this strong defense while incurring only a 1.45% average decrease in utility relative to the No Defense scenario, demonstrating superior performance compared to existing defense methods.

---


### 17. [Defusing the Trigger: Plug-and-Play Defense for Backdoored LLMs via Tail-Risk Intrinsic Geometric Smoothing](https://arxiv.org/abs/2604.24162)

**<font color=#1a73e8>作者：</font>** Kaisheng Fan, Weizhe Zhang, Yishu Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Defending against backdoor attacks in large language models remains a critical practical challenge. Existing defenses mitigate these threats but typically incur high preparation costs and degrade utility via offline purification, or introduce severe latency via complex online interventions. To overcome this dichotomy, we present Tail-risk Intrinsic Geometric Smoothing (TIGS), a plug-and-play inference-time defense requiring no parameter updates, external clean data, or auxiliary generation. TIGS leverages the observation that successful backdoor triggers consistently induce localized attention collapse within the semantic content region. Operating entirely within the native forward pass, TIGS first performs content-aware tail-risk screening to identify suspicious attention heads and rows using sample-internal signals. It then applies intrinsic geometric smoothing: a weak content-domain correction preserves semantic anchoring, while a stronger full-row contraction disrupts trigger-dominant routing. Finally, a controlled full-row write-back reconstructs the attention matrix to ensure inference stability. Extensive evaluations demonstrate that TIGS substantially suppresses attack success rates while strictly preserving clean reasoning and open-ended semantic consistency. Crucially, this favorable security-utility-latency equilibrium persists across diverse architectures, including dense, reasoning-oriented, and sparse mixture-of-experts models. By structurally disrupting adversarial routing with marginal latency overhead, TIGS establishes a highly practical, deployment-ready defense standard for state-of-the-art LLMs.

---


### 18. [Agentic Witnessing: Pragmatic and Scalable TEE-Enabled Privacy-Preserving Auditing](https://arxiv.org/abs/2604.24203)

**<font color=#1a73e8>作者：</font>** Antony Rowstron  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Auditing the semantic properties of proprietary data creates a fundamental tension: verification requires transparent access, while proprietary rights demand confidentiality. While Zero-Knowledge Proofs (ZKPs) ensure privacy, they are typically limited to precise algebraic constraints and are ill-suited for verifying qualitative, unstructured properties, such as the logic within a codebase. We propose {\em Agentic Witnessing}, a framework that moves verification from attested execution to {\em attested reasoning}. The system is composed of three agents: a Verifier (who wants to check properties of a dataset), a Prover (who owns the dataset) and an Auditor (that inspects the dataset). The Verifier is allowed to ask a limited number of simple binary true/false questions to the auditor. By isolating an LLM-based Auditor within a Trusted Execution Environment (TEE), the system enables the Verifier to query a Prover's private data via simple Boolean queries, without exposing the raw dataset. The Auditor uses the Model Context Protocol (MCP) to dynamically inspect the target dataset, producing a yes/no verdict accompanied by a cryptographic transcript: a signed hash chain binding the reasoning trace to both the original dataset and the TEE's hardware root of trust. We demonstrate this architecture by automating the artifact evaluation process for 21 peer-reviewed computer science papers with released codebases on GitHub (e.g. Does the codebase implement the system described in the paper?). We verified five high-level properties of these codebases described in the corresponding publications, treating the source code as private. Our results show that TEE-enabled agentic auditing provides a mechanism for privacy-preserving oversight, effectively decoupling qualitative verification from the need for data disclosure.

---


### 19. [MAS-SZZ: Multi-Agentic SZZ Algorithm for Vulnerability-Inducing Commit Identification](https://arxiv.org/abs/2604.24398)

**<font color=#1a73e8>作者：</font>** Sicong Cao, Jinxuan Xu, Le Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Accurate vulnerability-inducing commit identification serves as a foundation for a series of software security tasks, such as vulnerability detection and affected version analysis. A straightforward solution is the SZZ algorithm, which traces back through the code history to identify the earliest commit that modify the vulnerable code. Unfortunately, neither the customized V-SZZ nor state-of-the-art LLM4SZZ perform satisfactorily due to the incorrect anchor selection and inadequate backtracking capability, making them far beyond a reliable usage in practice.
To overcome these challenges, we propose a multi-agentic SZZ algorithm, named MAS-SZZ, that facilitates the identification of vulnerability-inducing commits through collaboration among agents. Specifically, given a CVE description and its corresponding fixing commit, MAS-SZZ summarizes the root cause of the vulnerability and employs a structured step-forward prompting strategy to localize vulnerability-related statements based on the change intent of each patch hunk. These vulnerable statements serve as anchors from which MAS-SZZ autonomously traces backward through the repository's history to find the commit that first introduced the vulnerability. Extensive experiments show that MAS-SZZ outperforms the state-of-the-art baselines across datasets and programming languages, achieving F1-score gains of up to 65.22% over the best-performing SZZ algorithm.

---


### 20. [A Survey on Split Learning for LLM Fine-Tuning: Models, Systems, and Privacy Optimizations](https://arxiv.org/abs/2604.24468)

**<font color=#1a73e8>作者：</font>** Zihan Liu, Yizhen Wang, Rui Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fine-tuning unlocks large language models (LLMs) for specialized applications, but its high computational cost often puts it out of reach for resource-constrained organizations. While cloud platforms could provide the needed resources, data privacy concerns make sharing sensitive information with third parties risky. A promising solution is split learning for LLM fine-tuning, which divides the model between clients and a server, allowing collaborative and secure training through exchanged intermediate data, thus enabling resource-constrained participants to adapt LLMs safely. % In light of this, a growing body of literature has emerged to advance this paradigm, introducing varied model methods, system optimizations, and privacy defense-attack techniques for split learning. To bring clarity and direction to the field, a comprehensive survey is needed to classify, compare, and critique these diverse approaches. This paper fills the gap by presenting the first extensive survey dedicated to split learning for LLM fine-tuning. We propose a unified, fine-grained training pipeline to pinpoint key operational components and conduct a systematic review of state-of-the-art work across three core dimensions: model-level optimization, system-level efficiency, and privacy preservation. Through this structured taxonomy, we establish a foundation for advancing scalable, robust, and secure collaborative LLM adaptation.

---


### 21. [GAMMAF: A Common Framework for Graph-Based Anomaly Monitoring Benchmarking in LLM Multi-Agent Systems](https://arxiv.org/abs/2604.24477)

**<font color=#1a73e8>作者：</font>** Pablo Mateo-Torrejón, Alfonso Sánchez-Macián  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid integration of Large Language Models (LLMs) into Multi-Agent Systems (MAS) has significantly enhanced their collaborative problem-solving capabilities, but it has also expanded their attack surfaces, exposing them to vulnerabilities such as prompt infection and compromised inter-agent communication. While emerging graph-based anomaly detection methods show promise in protecting these networks, the field currently lacks a standardized, reproducible environment to train these models and evaluate their efficacy. To address this gap, we introduce Gammaf (Graph-based Anomaly Monitoring for LLM Multi-Agent systems Framework), an open-source benchmarking platform. Gammaf is not a novel defense mechanism itself, but rather a comprehensive evaluation architecture designed to generate synthetic multi-agent interaction datasets and benchmark the performance of existing and future defense models. The proposed framework operates through two interdependent pipelines: a Training Data Generation stage, which simulates debates across varied network topologies to capture interactions as robust attributed graphs, and a Defense System Benchmarking stage, which actively evaluates defense models by dynamically isolating flagged adversarial nodes during live inference rounds. Through rigorous evaluation using established defense baselines (XG-Guard and BlindGuard) across multiple knowledge tasks (such as MMLU-Pro and GSM8K), we demonstrate Gammaf's high utility, topological scalability, and execution efficiency. Furthermore, our experimental results reveal that equipping an LLM-MAS with effective attack remediation not only recovers system integrity but also substantially reduces overall operational costs by facilitating early consensus and cutting off the extensive token generation typical of adversarial agents.

---


### 22. [Layerwise Convergence Fingerprints for Runtime Misbehavior Detection in Large Language Models](https://arxiv.org/abs/2604.24542)

**<font color=#1a73e8>作者：</font>** Nay Myat Min, Long H. Pham, Jun Sun  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models deployed at runtime can misbehave in ways that clean-data validation cannot anticipate: training-time backdoors lie dormant until triggered, jailbreaks subvert safety alignment, and prompt injections override the deployer's instructions. Existing runtime defenses address these threats one at a time and often assume a clean reference model, trigger knowledge, or editable weights, assumptions that rarely hold for opaque third-party artifacts. We introduce Layerwise Convergence Fingerprinting (LCF), a tuning-free runtime monitor that treats the inter-layer hidden-state trajectory as a health signal: LCF computes a diagonal Mahalanobis distance on every inter-layer difference, aggregates via Ledoit-Wolf shrinkage, and thresholds via leave-one-out calibration on 200 clean examples, with no reference model, trigger knowledge, or retraining. Evaluated on four architectures (Llama-3-8B, Qwen2.5-7B, Gemma-2-9B, Qwen2.5-14B) across backdoors, jailbreaks, and prompt injection (56 backdoor combinations, 3 jailbreak techniques, and BIPIA email + code-QA), LCF reduces mean backdoor attack success rate (ASR) below 1% on Qwen2.5-7B and Gemma-2 and to 1.3% on Qwen2.5-14B, detects 92-100% of DAN jailbreaks (62-100% for GCG and softer role-play), and flags 100% of text-payload injections across all eight (model, domain) cells, at 12-16% backdoor FPR and <0.1% inference overhead. A single aggregation score covers all three threat families without threat-specific tuning, positioning LCF as a general-purpose runtime safety layer for cloud-served and on-device LLMs.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
