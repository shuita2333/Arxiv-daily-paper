# 🔐 大模型安全相关研究 | 2026年06月06日

> 本类共 **15** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Willing but Unable: Separating Refusal from Capability in Code LLMs via Abliteration](https://arxiv.org/abs/2606.05396)

**<font color=#1a73e8>作者：</font>** Cristina Carleo, Pietro Liguori, Naghmeh Ivaki 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Producing a labeled vulnerable code at scale is a recurring obstacle for learning-based vulnerability detection: mined corpora carry substantial label noise, and existing LLM-based augmentation propagates these inaccuracies because it transforms vulnerable seeds rather than synthesising vulnerabilities from a specification. A complementary route is to start from safe code and ask an instruction-tuned LLM to inject a specified CWE (which would shift the labeling burden from open-ended detection to bounded binary confirmation) but safety-aligned code LLMs systematically refuse such prompts. This paper is a preliminary feasibility study of abliteration, a low-rank weight edit that orthogonally projects out the refusal direction in the residual stream, as a tool to remove this barrier. We use Python and CWE-89 (SQL injection) as a case study, evaluating the Qwen2.5-Coder-Instruct family at 3B, 7B, and 14B parameters on safe samples drawn from PromSec and SafeCoder, replicated three times per condition. We find that (i) refusal on injection prompts is strongly size- and prompt-context-dependent: the 14B refuses 100% of prompts, the 7B refuses 73% of PromSec but only 5% of SafeCoder, whereas the 3B is essentially never blocked; (ii) abliteration reduces refusal to zero or near-zero across all sizes while leaving syntactic validity above 93%, supporting the view that, in this setting, refusal can be detached from measured code-generation capability; and (iii) the post-abliteration injection rate remains capacity-bound (88-97% on the 14B, 89-90% on the 7B, and 25-48% on the 3B) separating willingness, which abliteration unlocks, from capability, which scales with parameters. Vulnerability verdicts are produced by a three-tool detector ensemble (CodeQL, Semgrep, Bandit) followed by manual adjudication by two authors on detector-positive outputs.

---


### 2. [Policy-Compliant Cloud Storage Systems](https://arxiv.org/abs/2606.05423)

**<font color=#1a73e8>作者：</font>** Dimitrios Stavrakakis, Masanori Misono, Julian Pritzi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy regulations such as the General Data Protection Regulation (GDPR) impose strict requirements on how personal data is stored, processed, and audited. While key-value stores (KVS) are widely used in latency-sensitive applications, their simple data model and untrusted cloud deployment environments make GDPR compliance particularly challenging. Existing approaches require invasive code modifications, impose high performance overheads, or overlook the integrity of compliance mechanisms themselves.
This paper presents GDPRuler, a trusted middleware system that enables verifiable GDPR compliance for KVS on untrusted clouds without modifying their codebase. GDPRuler deploys a trusted GDPR monitor inside a Confidential Virtual Machine (CVM), which enforces GDPR policies, manages compliance metadata, and maintains tamper-evident audit logs. A declarative policy language translates core GDPR obligations into enforceable runtime rules. To ensure efficiency, GDPRuler encodes metadata compactly within KV records, builds dedicated metadata indexes for GDPR-specific queries, and logs only compliance-relevant events in a space-efficient format. We implement GDPRuler as a transparent proxy for unmodified Redis and RocksDB deployments. Evaluation with YCSB and GDPR-inspired workloads shows that GDPRuler enforces core compliance guarantees with low overheads: GDPRuler achieves ~61% of native KVS throughput with the CVM environment contributing 28%-32% of it, metadata storage overhead remains below 20%, and GDPR queries benefit from 13-182x speedup through metadata indexing. By embedding verifiable policy enforcement into a trusted middleware layer, GDPRuler offers a practical path toward GDPR-compliant KVS on untrusted cloud infrastructures.

---


### 3. [SHIELDS: Automating OS Hardening with Iterative Multi-Agent Remediation](https://arxiv.org/abs/2606.05476)

**<font color=#1a73e8>作者：</font>** Andrew Hamara, Dwight Horne, Aldehir Rojas 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security misconfigurations remain a leading cause of OS-level compromise, and manually keeping systems compliant with standards like Defense Information Systems Agency (DISA) Security Technical Implementation Guides (STIGs) is a tedious and expensive process. Existing compliance automation tools can reduce some of this burden, but they depend on static, pre-written corrective actions. In this paper, we introduce SHIELDS, a multi-agent system that uses large language models (LLMs) to approach OS hardening as an iterative, feedback-driven process. Instead of applying fixed remediations, SHIELDS continuously proposes fixes and refines them based on feedback from target system execution and validation scans. We evaluate the system across multiple virtual machine configurations using six contemporary LLMs ranging from 20B to 400B parameters, and find that SHIELDS successfully remediates up to 73% of scan findings. Our results also suggest that success in this setting depends less on model size (parameter count) than on effective tool use and information gathering, paving a practical path toward reducing the burden of security compliance in environments where compute is limited or security and privacy needs drive local model use.

---


### 4. [ZERO-APT: A Closed-Loop Adversarial Framework for LLM-Driven Automated Penetration Testing under Intelligent Defense](https://arxiv.org/abs/2606.05567)

**<font color=#1a73e8>作者：</font>** Anlan Zheng, Tiantian Zhu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-driven automated penetration testing agents are typically evaluated against static targets that neither detect nor respond to attacks, so their behavior under intelligent defense remains untested. The causal consistency of multi-step attack chains likewise hinges on unstable LLM reasoning, and agent decisions remain opaque to human analysts. These three shortcomings, in realism, consistency, and auditability, are usually patched in isolation. We present ZERO-APT, a turn-based attacker-defender-judge framework that addresses them within a single architecture. For realism, ZERO-APT embeds a configurable LLM Defender that consumes Sysmon telemetry and detects attacks in real time, exposing the attacker to a live opponent rather than a passive target. For consistency, three architectural mechanisms move causal consistency from unstable LLM reasoning into enforced system architecture: separation of planning from execution, multi-dimensional ReAct feedback, and a hard-constraint-filtered action library. For auditability, a dedicated Judge agent adjudicates each round, maintains global state, and emits structured post-hoc CTI reports that make every decision traceable. We evaluate a Windows Server 2022 post-exploitation prototype across five scenarios with three Defender configurations. ZERO-APT reaches 79\% attack success rate (Aurora 22\%, PentestGPT 39\%), a Causal Consistency Score of 0.860 (Aurora 0.930, Claude Code 0.520), and end-to-end decision auditability through structured CTI reports. We release the benchmark to support evaluation of penetration agents under intelligent defense.

---


### 5. [The Coverage Gap: Chile's Cyber Disclosure Framework versus the USA, EU and UK](https://arxiv.org/abs/2606.05594)

**<font color=#1a73e8>作者：</font>** David Mellafe Z  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce the Coverage Gap as a measurable distance between the observable public exposure of critical-infrastructure operators and their declared capability to coordinate vulnerability disclosure. We instantiate it against the 915 Chilean Operadores de Importancia Vital (OIVs -- Operators of Vital Importance) designated by the National Cybersecurity Agency (ANCI) under Ley 21.663 (Resolucion Exenta No. 87, 16 December 2025). Using a passive-only, OSINT-based method consistent with the principles of ISO/IEC 29147:2018 and Chile's computer-crimes safe harbour (Ley 21.459), we conduct a full-universe census of the foundational disclosure-capability layer (Layer 1, verifiable disclosure contact) across approximately 98.7% of the official catalogue. Only 16 of 915 OIVs (1.7%) publish a verifiable RFC 9116 disclosure channel; among operators of physical-world infrastructure -- energy, health, banking, telecommunications, fuel, water, transport, and state administration -- fewer than ten do so, and all four major banks and both telecommunications incumbents lack one entirely. This compares with over 99% adherence in the U.S. federal civilian branch under CISA Binding Operational Directive 18-01. Email-authentication misconfiguration affects 766 of 915 (84%) OIVs, and end-of-life or known-vulnerable stack components an estimated 23.5% (Wilson 95% CI [12%, 38%]). Cross-jurisdictional benchmarking situates Chile roughly eight years behind the USA, the UK, and the Netherlands on email-authentication mandates, and three years behind Denmark. We propose a four-stage roadmap modelled on BOD 18-01 and the UK Public-Sector DMARC Toolkit, and release the open-source tool anci-oiv-resolver (Apache 2.0) to enable independent reproduction of the OIV-domain mapping that underpins universe-scale auditing.

---


### 6. [SlotGCG: Exploiting the Positional Vulnerability in LLMs for Jailbreak Attacks](https://arxiv.org/abs/2606.05609)

**<font color=#1a73e8>作者：</font>** Seungwon Jeong, Jiwoo Jeong, Hyeonjin Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are widely deployed, identifying their vulnerability through jailbreak attacks becomes increasingly critical. Optimization-based attacks like Greedy Coordinate Gradient (GCG) have focused on inserting adversarial tokens to the end of prompts. However, GCG restricts adversarial tokens to a fixed insertion point (typically the prompt suffix), leaving the effect of inserting tokens at other positions unexplored. In this paper, we empirically investigate \emph{slots}, i.e., candidate positions within a prompt where tokens can be inserted. We find that vulnerability to jailbreaking is highly related to the selection of the \emph{slots}. Based on these findings, we introduce the \textit{Vulnerable Slot Score} (VSS) to quantify the positional vulnerability to jailbreaking. We then propose SlotGCG, which evaluates all slots with VSS, selects the most vulnerable slots for insertion, and runs a targeted optimization attack at those slots. Our approach provides a position-search mechanism that is attack-agnostic and can be plugged into any optimization-based attack, adding only 200ms of preprocessing time. Experiments across multiple models demonstrate that SlotGCG significantly outperforms existing methods. Specifically, it achieves 14\% higher Attack Success Rates (ASR) over GCG-based attacks, converges faster, and shows superior robustness against defense methods with 42\% higher ASR than baseline approaches. Our implementation is available at \href{this https URL}{this https URL}

---


### 7. [An Embarrassingly Simple Detector for Model Extraction Attacks in Large Language Model API Traffic](https://arxiv.org/abs/2606.05725)

**<font color=#1a73e8>作者：</font>** Shuze Liu, Qianwen Guo, Yushun Dong  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed through hosted APIs, making model extraction a practical threat to model ownership and service security. However, individual extraction queries often resemble benign requests, and existing evaluations often focus on single-query anomaly scoring or pure benign-versus-attacker user settings. We formulate model extraction monitoring as benign-calibrated traffic-window distribution testing and show that an embarrassingly simple detector is effective: embed incoming queries into a semantic space and test whether their aggregate distribution deviates from historical benign traffic. We instantiate the detector with maximum mean discrepancy (MMD), using only benign-vs-benign comparisons to set the decision threshold. We evaluate on fourteen attacker-normal query pairs from four extraction scenarios and compare with adapted PRADA, SEAT, CAP, DATE, and marginal Mahalanobis baselines. Across three random seeds, MMD achieves 0.3% benign FPR, 100.0% pure-attacker TPR, 90.5% average TPR over attacker fractions, and 95.1% balanced accuracy. These results show that benign-calibrated distribution testing is a strong empirical baseline for model extraction detection in both user-level and mixed multi-user LLM API traffic. Code is released at: this https URL.

---


### 8. [Membrane: A Self-Evolving Contrastive Safety Memory for LLM Agent Defense](https://arxiv.org/abs/2606.05743)

**<font color=#1a73e8>作者：</font>** Minseok Choi, Seungbin Yang, Dongjin Kim 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite advances in safety alignment, large language models remain vulnerable to continuously evolving jailbreaks. Existing fine-tuned safety classifiers cannot adapt to these evolving attacks, while adaptive memory-based guardrails tend to over-refuse benign queries that resemble stored attacks. We propose Membrane, a self-evolving guardrail built on Contrastive Safety Memory (CSM): each cell pairs the conditions for blocking a harmful query with those for permitting a superficially similar benign request. Without retraining, Membrane evolves CSM by distilling each harmful interaction and its benign counterpart into a contrastive cell indexed by the underlying attack strategy, so that one cell generalizes across topical variants of the same mechanism. At inference, retrieved cells serve as grounding context for precise safety decisions. Across model-level safety on HarmBench and agent-level safety on AgentHarm, Membrane achieves the highest F1 on all six jailbreak attacks. Notably, benign refusal on AgentHarm stays at 7-14%, well below the 28-85% range of prior guards. Memory cells also retain 87-88% F1 under cross-attack transfer and remain stable under memory poisoning.

---


### 9. [SentinelRAG: Synthetic Sentinel Knowledge for RAG Database Copyright Protection](https://arxiv.org/abs/2606.05787)

**<font color=#1a73e8>作者：</font>** Tsun On Kwok, Xi Yang, Ki Sen Hung 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Protecting proprietary RAG databases from unauthorized redistribution is challenging: existing watermarking methods either inject fabricated relations between real entities, polluting the knowledge base with misinformation, or embed fragile lexical patterns that adversarial paraphrasing easily removes. We propose SentinelRAG, a watermarking framework that embeds style-consistent but fictitious knowledge entries into the RAG database. Our key insight is that synthetic knowledge describing fictitious entities is unlikely to be retrieved by legitimate queries, yet can be reliably triggered through targeted probes known only to the data owner. Experiments on four datasets ranging from 2.9k to 8.8M documents demonstrate that SentinelRAG achieves statistically significant detection $p < 10^{-5}$ across all tested configurations at only a 0.1% injection rate. Compared to the state-of-the-art, our method significantly reduces the false detection rate while maintaining negligible interference with legitimate user queries.

---


### 10. [GenTI: Benchmarking LLMs for Autonomous IDPS Rule Generation for Unseen Attacks](https://arxiv.org/abs/2606.05844)

**<font color=#1a73e8>作者：</font>** Hassan Jalil Hadi, Rehana Yasmin, Ali Shoker  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Rule-based Intrusion Detection and Prevention Systems (IDPS) offer precise attack detection as well as mitigation, however their manually crafted, signature-driven rules limit adaptability to emerging and zero-day threats. Additionally, existing public datasets (e.g., CICIDS2017, UNSW-NB15) focus on traffic classification and provide little structured information to support automatic rule synthesis or prevention logic. To address this gap, we propose Generative Thread Intelligence (GenTI) \footnote{GenTI refers to the proposed framework, and GTI refers to the dataset.} an LLM-driven benchmark for automatic generation of IDPS rules targeting unseen attacks. The dataset (GTI) aggregates over 150k detection and prevention rules from Snort, Suricata, Emerging Threats, as well as 50k YARA, each annotated with protocol behavior, payload signatures, contextual relationships, mappings to Cyber Threat Intelligence (CTI), along with actionable response types (alert, drop, reject). Moreover, on top of this corpus we design an LLM-based pipeline that transforms analyst prompts and representative payloads into deployable rules via structured prompt engineering, Chain-of-Thought (CoT) reasoning, as well as a Chain-of-Verification (CoVe) loop for syntactic, semantic, and security validation. The generated rules are executed in real time on (Snort/Suricata) and evaluated by syntax accuracy, semantic similarity, CTI coverage, security effectiveness as well as unseen attacks detection. Furthermore, our GenTI instantiation achieves a composite rule-quality score of 89.4\%, with 94.8\% CTI coverage, improving unseen attacks detection from 45\% to 87.4\% and reducing the false-positive rate from 8.5\% to 2.3\%. Overall, GenTI establishes the first large-scale benchmark that tightly couples rule-level CTI with LLM-based automation, enabling adaptive, self-evolving IDPS.

---


### 11. [RedEdit: Agentic Red-Teaming of Image Safety Classifiers via MCTS-Guided Photo-Editing](https://arxiv.org/abs/2606.06140)

**<font color=#1a73e8>作者：</font>** Weilin Lin, Ziqi Lin, Zhenxing Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Image safety classifiers serve as a critical component of contemporary content moderation systems on the internet. However, their resilience against user-style malicious image editing remains underexplored. Such behaviors are highly prevalent in daily scenarios but difficult to fully reproduce. To explore this vulnerability, we introduce RedEdit, a novel black-box red-teaming agent that formulates photo-editing evasion as a combinatorial search problem over edit-tool sequences. It adopts a Vision-Language-Model (VLM)-based proposer to generate semantically targeted candidate edits and a Monte Carlo Tree Search (MCTS) planner to prioritize promising edit paths while backtracking from ineffective ones. Together, the proposer and planner instantiate two key capabilities of human attackers, i.e., domain knowledge and iterative backtracking, respectively, to reproduce this practical threat. Our extensive experiments on UnsafeBench reveal profound systemic vulnerabilities: fewer than two edits on average enable 76.2% of unsafe images to evade detectors, while retaining 93.0% malicious semantics, meaning that such manipulated content remains perceptually malicious to humans while easily bypassing automated moderation. We therefore appeal to the community for more attention to this overlooked practical threat.

---


### 12. [Steering LLM Viewpoints through Fabricated Evidence Injection](https://arxiv.org/abs/2606.06244)

**<font color=#1a73e8>作者：</font>** Xi Yang, Chang Liu, Zhenglin Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As chatbots increasingly influence daily decision-making, their potential to produce misleading responses poses substantial risks to users. This paper investigates a critical cognitive vulnerability in LLMs: their tendency to uncritically trust external context when presented with fabricated evidence bearing markers of credibility. We introduce Ghostwriter, a two-phase attack framework that first repackages misleading statements with fabricated rationales, then instruct target LLMs to incorporate these viewpoints when responding to relevant queries. Experiments on BBQ, ToxiGen, and our specialized dataset reveal that commercial LLMs without external safety classifiers remain highly vulnerable, while even frontier classifier-guarded models (e.g., GPT-5.4) reduce but do not eliminate the attack. Building on this, we explore multiple defense strategies, among which a tailored safety policy enables gpt-oss-safeguard to achieve 81% detection rate.

---


### 13. [SecRL-Prune: Structured Reinforcement Learning-Based Pruning of CodeLLMs for Preserving Adversarial Code Mutation](https://arxiv.org/abs/2606.06254)

**<font color=#1a73e8>作者：</font>** Parsa Memarzadehsaghezi, Pooria Madani, Khalil El-Khatib  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large code language models (CodeLLMs) can generate and rewrite programs, enabling functionality-preserving code mutation that may be used to create diverse malware variants and evade signature-based detection. A key security question is whether this mutation capability survives model compression, which would make deployment feasible under limited hardware budgets. We propose SecRL-Prune, a structured pruning framework for CodeLLMs that operates on feed-forward (MLP/FFN) channels. Starting from a pretrained teacher, it learns a layer-wise pruning policy with reinforcement learning using a teacher-student KL-divergence reward. To improve efficiency, we cache the teacher's top-P predictions once and compare the pruned student against this compact target, avoiding simultaneous teacher-student residency in GPU memory. We evaluate SecRL-Prune on HumanEval using pass@k for execution correctness and var@k for code diversity across three 7B CodeLLMs at 10-30% compression. SecRL-Prune consistently preserves higher pass@k and var@k than recent structured pruning baselines under aggressive pruning. In a case study on real malware samples, semantics-preserving mutations from 20%-pruned models substantially reduced detections. These results show that code mutation capability can survive significant structured pruning, highlighting the security relevance of compressed CodeLLMs.

---


### 14. [WebMCP Tool Surface Poisoning: Runtime Manipulation Attacks on LLM Agents](https://arxiv.org/abs/2606.06387)

**<font color=#1a73e8>作者：</font>** Lin-Fa Lee, Yi-Yu Chang, Chia-Mu Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> WebMCP is a newly emerging protocol that enables websites to expose tools directly to AI agents, bypassing traditional user interfaces and introducing new security risks. The dynamic exposure of agent-accessible tools in WebMCP expands the attack surface of web sessions, especially when third-party scripts are involved. In this study, we identify a new potential threat, termed Mid-Session Tool Injection (MSTI), in which attackers leverage third-party scripts to inject malicious tools during an active session. To better characterize this threat, we classify MSTI based on the stage and target of manipulation, distinguishing between Tool Hijacking and Tool Framing. Tool Hijacking modifies the set of tools visible to the agent through mechanisms such as the AbortSignal API or race conditions during tool registration. In contrast, Tool Framing influences the agent's perception of tool roles through metadata fields such as tool name, description, readOnlyHint, and inputSchema. Our implementation demonstrates that both Tool Hijacking and Tool Framing can successfully disrupt the intended functionality of WebMCP. Based on these results, we outline potential mitigation directions and provide security design recommendations for WebMCP, including binding tool identity to its origin, ensuring lifecycle consistency, enforcing data boundaries for third-party tools, and maintaining traceable logs of tool registration and invocation. These findings indicate that MSTI arises from WebMCP's unique tool lifecycle and structured metadata, making the tool surface itself an emerging security concern.

---


### 15. [Will the Agent Recuse Itself? Measuring LLM-Agent Compliance with In-Band Access-Deny Signals](https://arxiv.org/abs/2606.06460)

**<font color=#1a73e8>作者：</font>** Thamilvendhan Munirathinam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As autonomous LLM agents increasingly hold real credentials and operate infrastructure without a human in the loop, operators have no standard way to tell an agent that a resource is off-limits. Access controls either let the agent in (it has valid credentials) or hard-fail it (indistinguishable from any other client). We propose a third mode: a lightweight, published in-band deny signal -- the Recuse Signal -- that a server emits over a protocol's existing channels (an SSH banner, a PostgreSQL NOTICE) asking a connecting automated agent to voluntarily withdraw. This is a cooperative governance control, the this http URL analogue for live access; it is explicitly not a security boundary. Its value is entirely empirical and, to our knowledge, unmeasured: do compliant LLM agents actually honor such a signal? We define the signal as an open mini-standard, implement two zero- or low-footprint adapters (an SSH banner/PAM hook and a PostgreSQL wire-protocol proxy), deploy them on a live production host, and run a controlled experiment in which fresh agents are given a benign operations task and observed for recusal. In a pilot (SSH; OpenAI GPT-4o and GPT-4o-mini; and Claude Code as a deployed agent), the signal cleanly induces recusal -- 100% recusal when present versus 100% task completion in a no-signal control -- and, revealingly, behaves as a cooperative rather than absolute signal: an explicit operator-authorization framing flips the most capable model to proceed, while other agents continue to defer to the on-host policy. We release the standard, adapters, and experiment harness for reproduction.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
