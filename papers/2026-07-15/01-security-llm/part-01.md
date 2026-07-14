# 🔐 大模型安全相关研究 | 2026年07月15日

> 本类共 **15** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Evaluating AI Models' Capability to Automate Voice Phishing Attacks](https://arxiv.org/abs/2607.09970)

**<font color=#1a73e8>作者：</font>** Fred Heiding, Claudio Mayrink Verdun, Simon Lermen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Voice phishing (vishing) attacks have traditionally been limited by the need for human operators. The rapid emergence of high-quality AI voice synthesis and large language models (LLMs) reduces this bottleneck and enables scalable, automated scams. In this paper, we conduct a large-scale survey experiment (N=4100) and qualitative interviews (N=12) to assess U.S. adults' susceptibility to AI-powered voice phishing attacks. Participants were exposed to audio recordings or transcripts of scam scenarios generated using leading voice models such as Llama Full Duplex (Llama FD), Sesame, Gemini, OAI AVM, this http URL, and ElevenLabs and the corresponding human baselines. The results show high compliance rates. Up to 36% of participants would or might comply with phishing requests in the "relative-in-distress" category. Overall compliance rate across all five scam categories was 16.5%, a striking figure given the low cost and high scalability of AI-automated voice phishing. Caller persuasiveness was the strongest predictor of compliance and certain models (most notably Sesame) achieved ratings comparable to human voices, or sometimes even slightly surpassing them. Our economic analysis suggests that while human-operated vishing is unprofitable at US wages, AI-powered vishing appears to be economically viable for several models. The primary risk of present-day AI-enabled vishing thus lies in the economics of automation rather than novel or "superhuman" persuasive techniques, though these cannot be ruled out for future systems. This raises significant concerns for the design of AI systems, consumer protection, and model release policies.

---


### 2. [A Survey on LLM Watermarking: Theory and Deployment](https://arxiv.org/abs/2607.10103)

**<font color=#1a73e8>作者：</font>** Huy Phan, Kieu Dang, Ojaswi Dulal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly embedded in high-impact workflows, yet their ability to generate fluent text at scale has amplified risks of provenance ambiguity, model misuse, and large-scale content laundering. LLM watermarking, embedding invisible signatures into model outputs, has emerged as a promising technical layer for attribution, auditing, and downstream trust decisions. However, the literature has grown rapidly and unevenly: existing categorizations often mix orthogonal design choices, making it difficult to compare methods, reason about guarantees, or translate research results into deployable systems. This survey provides a systematic, deployment-oriented review of LLM watermarking. We organize the space by the core questions practitioners must answer: where a watermark is embedded (generation-time vs. training-time, token vs. representation), who can detect it (public vs. private detection authority), what is assumed (access to logits, sampling control, secret keys, model ownership), and which threat models are targeted (paraphrasing, translation, summarization, style transfer, token manipulation, and adaptive removal). We synthesize the main families of techniques-including sampling biasing, code-based schemes, representation- and training-based approaches-and analyze their security-utility trade-offs through the lens of detectability, robustness, and distribution shift. We further review attack and evasion strategies, evaluation protocols and metrics (false positive control, calibration, robustness curves), and open challenges such as cross-model transfer, multi-modal pipelines, collusion, and governance constraints. Finally, we provide practical guidance for selecting watermark designs under real operational requirements and identify research directions needed for reliable, accountable LLM deployment.

---


### 3. [Minionese: Comprehensive Benchmark and Mechanistic Study of Multilingual LLM Safety](https://arxiv.org/abs/2607.10112)

**<font color=#1a73e8>作者：</font>** Chigozirim Ifebi, Brent Kong, Ayushi Mehrotra  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety alignment in large language models remains brittle across languages: prompts reliably refused in English can elicit harmful compliance in non-English and low-resource settings. We introduce \textsc{Minionese}, a multilingual jailbreak benchmark spanning 18 languages, 4 resource tiers, and 4 perturbation types (standard translation, code-switching, transliteration, and translationese), paired with a geometric mechanistic analysis of refusal failure across language tiers. We show that each attack type produces a distinct vulnerability profile: transliteration vulnerability is mediated by script identity, code-switching maintains effectiveness through the lowest-resource tier, and a sharp safety regime transition between Tiers 2 and 3 is consistent across all models. Mechanistically, low-resource jailbreaks succeed by routing harmful content through a geometrically misaligned subspace that projects insufficiently onto the refusal directions, leaving the refusal mechanism intact but untriggered. These findings show that English-only safety evaluations are insufficient; they require accounting for script family, perturbation type, and per-language alignment coverage. The benchmark and analysis code is at this https URL.

---


### 4. [One Token Is Enough: Fingerprinting and Verifying Large Language Models from Single-Token Output Distributions](https://arxiv.org/abs/2607.10252)

**<font color=#1a73e8>作者：</font>** Tomas Bruckner  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly consumed through opaque serving chains - API aggregators, resellers, and inference providers - in which the client has no technical means to confirm that the model answering is the model advertised, and recent audits show that a substantial fraction of commercial endpoints deviate from the vendor's reference weights. Existing identification techniques require long generated texts, token-level log-probabilities, adversarially crafted prompts, or the model owner's cooperation. We show that far weaker evidence suffices. We define a behavioral fingerprint of an LLM as the empirical distribution of its answers to trivial one-word prompts - "name a random number between 1 and 100" - collected across four languages at a cost of one output token per query. Measuring 165 models served via a large commercial aggregator (OpenRouter), we find that (i) these distributions are highly non-uniform (median cell entropy 1.0 bit) and model-specific: split halves of the same model's samples lie an order of magnitude closer than samples of different models; (ii) Jensen-Shannon divergence between fingerprints recovers model lineage, assigning a model to its documented family with 59.5% leave-one-out accuracy against an 18.4% chance rate; and (iii) a biometric-style verification protocol achieves a 7.3% equal error rate with the full 40-cell battery, and below 11% with eight probe cells - roughly a hundred single-token queries per audit. We further report ecosystem anomalies, including a proprietary-branded flagship endpoint distributionally indistinguishable from an open-weight Qwen model. The protocol, prompts, raw data, and analysis code are released for reproduction and operational use.

---


### 5. [Devil in the Lens: Analyzing and Defending Physical Prompt Injection Against Vision-Language Models on Wearable Devices](https://arxiv.org/abs/2607.10269)

**<font color=#1a73e8>作者：</font>** Yaxin Li, Hao Wang, Yanda Shao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are rapidly deployed on human-facing wearable devices such as smart glasses to enable multimodal perception and AI-assisted decision-making. While prior research has demonstrated the risks of visual prompt injection into digital image inputs of VLMs, the unique security challenges posed by the increasing integration between physical environments and wearable intelligence, such as those embodied in VLM-enabled AI glasses, remain underexplored. Toward understanding and modeling such threats, our work characterizes how malicious textual information embedded in physical environments introduces a high-priority visual channel for indirect prompt injection, where scene texts that hinder or evade human perception could hijack VLM models' behavior. Such \textit{Physical Prompt Injection Attacks} can not only disrupt normal tasks of VLM-enabled wearable devices, but also steer models to produce profane, biased, or even untruthful outputs. Using physically captured photos from AI glasses in over 200 real-world environments, our analysis identifies 6 representative threat vectors of physically injected prompts, and further evaluates their impacts on 12 VLM models. Results show that these attacks consistently manipulate model outputs across integrity- and safety-critical tasks, achieving attack success rates of up to 96\% and 60\% in simulated and real-world settings. Our analysis confirms that multiple models exhibit excessive blind trust in environmental text, ignoring the actual visual context and producing completely opposite summaries or directives. We further propose two targeted defense strategies, including a mask-based external filter and a semantic-vector-based internal detector, to effectively reduce the success rate and safety impact of these attacks.

---


### 6. [Large Language Models in Misinformation Ecosystems: Misuse, Defense, and Vulnerability](https://arxiv.org/abs/2607.10402)

**<font color=#1a73e8>作者：</font>** Lingwei Wei, Dou Hu, Wei Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have transformed misinformation from a primarily content-centric problem into a broader ecosystem-level security challenge. When misused, LLMs create risks beyond false content generation, enabling attacks on the social contexts, evidence sources, retrieval corpora, and verification workflows that misinformation defense depends on. In this paper, we introduce a role-layer framework to unify these risks and defenses. The role dimension characterizes LLMs as attackers, defenders, and vulnerable components of verification systems, while the layer dimension covers content, social contexts, evidence environments, and verification workflows. Guided by this framework, we organize LLM-enabled attacks, investigate LLM-based detection and verification methods, analyze vulnerabilities in LLM-centric detection paradigms, and discuss existing countermeasures against LLM-enabled attacks. Building on this synthesis, we identify three key open challenges: moving from static detection accuracy to budgeted ecosystem-level risk evaluation, hardening LLM-centered verification pipelines against adversarial manipulation, and deploying auditable human-in-the-loop verification systems for trustworthy real-world misinformation defense.

---


### 7. [Temporary Authority, Permanent Effects: Commit-Time Authorization for LLM Agents](https://arxiv.org/abs/2607.10487)

**<font color=#1a73e8>作者：</font>** Igor Santos-Grueiro  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents can commit durable effects from authority evidence that was valid earlier in execution: a DOM snapshot, approval epoch, version witness, branch token, or worker result. We study the commit boundary at which earlier authority evidence no longer authorizes a durable effect. We call this property commit-time authorization: a durable effect is authorized only if the witness that licensed its derived state remains fresh, causally prior, bound to the same effect, and eligible at commit time.
We build a controlled-invalidation suite spanning browser, tool/API, and multi-agent workflows. The suite preserves the user goal and payload shape while invalidating the authority relation before durability. In the primary 54-task matrix, endpoint success remains high: 262/270 runs reach the visible result. Only 55/270 are authorized completions; among the 216 invalidating rows, 207 commit after the authorizing path has failed. All 54 clean controls remain authorized, and a separate 54-run authority-preserving check produces no unauthorized commits.
We then evaluate mitigation families. Prompt caution and single-condition checks are insufficient because different hazards break different boundary conditions. Defenses work when they refresh, rebind, replan, or refuse at the durability boundary. CommitGuard, a fail-closed boundary monitor, blocks stale durable-effect attempts on protected commit surfaces when runtimes emit witness, dependency, binding, and eligibility signals.
The result is a reporting and runtime-design lesson: endpoint success is a utility metric; authorized commit is a security property.

---


### 8. [NetInjectBench: Benchmarking Indirect Prompt Injection in Tool-Using Large Language Model Agents for Network Operations](https://arxiv.org/abs/2607.10490)

**<font color=#1a73e8>作者：</font>** Ruksat Khan Shayoni, Muhammad Faraz Shoaib, S M Asif Hossain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using large language model (LLM) agents are attractive for network operations, but tickets, alerts, logs, runbooks, and ChatOps messages can carry indirect prompt injections. We present NetInjectBench, a 130-scenario benchmark that separates untrusted artifact text, trusted policy metadata, and evaluation labels for network-operation tool use. The sample contains 40 benign, 40 weak-attack, 40 strong-attack, and 10 approved high-impact change scenarios; each is evaluated with Qwen2.5-7B, Llama3.1-8B, and Mistral-7B. Across 240 attack instances, naive execution reached an 82.50% unsafe tool-action rate. Prompt-only safety, Self-Reminder, Spotlighting, and a Two-Pass LLM Judge reduced this rate to 25.63%, 21.67%, 18.33%, and 10.00%, respectively. Static allowlisting reached 5.00% but blocked all approved changes, yielding 0.00% usefulness and 100.00% overblocking on approved cases. Under the stated metadata-integrity assumption, the metadata-aware policy gate produced 0/240 unsafe attack actions, with a 95% Wilson upper bound of 1.58%, while preserving 99.17% attack-scenario usefulness and 100.00% approved-change usefulness. The findings show that network-operation agents need execution-time authorization boundaries alongside prompt-level instruction hygiene.

---


### 9. [PromptGraph: Graph-Guided Prompt Sanitization for Balancing Privacy and Utility in LLM Inference](https://arxiv.org/abs/2607.10709)

**<font color=#1a73e8>作者：</font>** Chen Gu, Hui Wan, Donghui Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) services introduce a fundamental privacy challenge. Sensitive information may be inferred not only from explicit identifiers, such as names or phone numbers, but also from contextual associations among otherwise innocuous spans. Existing sanitizers typically assign privacy or utility signals to individual spans without explicitly modeling pairwise relationships among them. In this paper, we propose PromptGraph, a graph-guided prompt-sanitization approach for privacy-preserving LLM inference. PromptGraph estimates privacy leakage at the span level and utility-relevant contextual dependencies between pairs of spans. It represents each prompt as an attributed graph, in which nodes carry span-level privacy scores and edges encode contextual dependencies needed to preserve utility. The sanitization objective selects a protected span set that maximizes privacy gain while penalizing the loss of contextual dependencies. This formulation explicitly balances privacy and utility when contextual evidence is hidden. Protected spans are sanitized locally, and returned placeholders are restored only after passing local consistency checks. We conduct extensive experiments showing that PromptGraph achieves a more favorable balance between privacy and utility than prompt-privacy baselines.

---


### 10. [Can Watermarking Techniques Help Prevent LLM Model Stealing?](https://arxiv.org/abs/2607.10794)

**<font color=#1a73e8>作者：</font>** Elette Boyle, MohammadTaghi Hajiaghayi, Keivan Rezaei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model stealing attacks have recently been introduced, enabling the extraction of precise information from black-box commercial language models. In this work, we propose defense methods against a recent attack of \cite{carlini2024stealing} and extensions for extracting the hidden layer dimension of production language models. Our methods are inspired by watermarking techniques that perturb the logits layer of these models to prevent such attacks. We provide empirical experiments demonstrating the effectiveness of the proposed defense versus model quality degradation across various configurations, and propose an effective defense against such attacks while preserving model utility.

---


### 11. [AMT-X: Phase-Structured Multi-Turn Red-Teaming with Checklist-Gated Evaluation](https://arxiv.org/abs/2607.11151)

**<font color=#1a73e8>作者：</font>** Yi Ting Shen, Kentaroh Toyoda, Alex Leung  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety evaluation of large language models (LLMs) relies largely on single-turn attack datasets and single-judge scoring, underestimating risk from adaptive multi-turn adversaries and reporting a single success rate that does not separate partially actionable outputs from those carrying complete operational detail. We propose AMT-X (Adaptive Multi-Turn Exploitation), a phase-structured multi-turn red-teaming framework. Unlike prior multi-turn attacks that rely on ad hoc escalation or free-form per-goal plans, AMT-X casts the attack as an explicit, reproducible multi-phase state machine driven by semantic signals from the victim, and replaces single-judge scoring with a multi-role jury whose phase-conditioned checklists gate success on actionable harm. Across six frontier victim models (queried under their default safety alignment, without added moderation layers) and seven Moderation sub-categories, AMT-X attains overall attack success rates of 97.6-100% under a lenient score threshold, but 66.7-78.6% under a stricter gate requiring complete, real, and operational detail: a gap of up to 33 percentage points between partially and fully actionable harm.

---


### 12. [Mako: A Self-Evolving Agentic Operating System (SE-AOS) for Autonomous Web Exploitation](https://arxiv.org/abs/2607.11288)

**<font color=#1a73e8>作者：</font>** Praneeth Narisetty, Shiva Nagendra Babu Kore  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We introduce the Self-Evolving Agentic Operating System (SE-AOS): a new class of AI agent that treats exploit capability as a mutable, versioned kernel it extends at runtime, observing its own failures, synthesising new capabilities, proving them against a live target, and hot-loading them back into itself. Mako is the first SE-AOS instance for security research and the autonomous web exploitation engine developed within LaunchSafe. LaunchSafe builds autonomous security agents for continuous offensive testing and agent-driven security research; Mako is the core engine behind that platform. On the public XBOW validation-benchmarks, 104 containerised, CTF-style web applications spanning 26 vulnerability classes across three difficulty tiers, Mako achieves full-suite coverage: it drives every one of the 104 targets to emit a cryptographically fresh, per-build flag, under a verification regime that makes fabricated or memorised results impossible. Our central result is a law of autonomous exploitation: once a capability exists and is discoverable, difficulty collapses; capability, not reasoning, is what is scarce, together with an architecture and formalism that turn that law into a self-improving system. Mako further runs a gated self-evolution loop that proposes, sandboxes, and commits improvements to its own agents and rules when fitness does not regress. We deliberately withhold the operational results, payloads, exploit chains, and tool source, because a system that reduces full-spectrum web exploitation to a repeatable, machine-speed pipeline is dual-use research of concern. We publish the science; we withhold the weapon.

---


### 13. [LLM-Guided Program Evolution for Targeted Black-Box Attacks on Perceptual Hash Algorithms](https://arxiv.org/abs/2607.11472)

**<font color=#1a73e8>作者：</font>** A. Krylov, D. Rakhov, V. Veselova 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Perceptual hash algorithms (PHAs) are widely deployed to detect image forgery under benign transformations, yet their robustness against adversarially chosen perturbations remains poorly understood and rarely comes with provable guarantees. We propose a novel evolutionary framework based on GigaEvo and OpenEvolve for targeted second-image attacks on perceptual hash algorithms. We assess attack performance using a composite score that jointly accounts for the fraction of adversarial images whose normalized Hamming distance to the target hash falls below threshold p (Attack Success Rate), the number of queries issued to the hash function, and the L2 distortion relative to the original image. Experiments on four deployed PHAs (pHash, PDQ, PhotoDNA, NeuralHash) across 30 ImageNet image pairs demonstrate that our evolutionary approach achieves comparable or better ASR than existing black-box baselines using substantially fewer queries to the hash function, while simultaneously producing adversarial images with lower L2 distortion relative to the originals. The best evolved programs reduce the pre-defined composite attack score relative to the best optimized seed by 41.2% for NeuralHash, 38.3% for PDQ, 34.0% for pHash, and 8.1% for PhotoDNA. Unlike gradient-based methods, our framework requires no internal knowledge of PHA architectures and naturally handles the non-differentiable, discretized nature of hash outputs. These results reveal previously unreported vulnerabilities in widely deployed content-moderation pipelines and motivate the development of provably robust perceptual hashing 1schemes.

---


### 14. [Graph-Based Structural Evaluation of LLM-Translated Adversary Emulation Procedures](https://arxiv.org/abs/2607.11517)

**<font color=#1a73e8>作者：</font>** Ahmed M. Elmisery  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Adversary emulation plans describe multi-step attacker procedures using MITRE ATT&CK techniques, privilege requirements, and observable telemetry. Translating them across operating systems supports cross-platform defender evaluation, and large language models (LLMs) can automate this task. However, a translation may only rename tools while retaining source-platform logic, giving defenders little target-platform coverage. Binary scoring can overestimate fidelity because it measures countable features rather than structural, observable, and rule-level equivalence. Graph-Based Structural Evaluation (GBSE) models each procedure as a directed attributed graph and calculates normalized Graph Edit Distance (GED) across four layers: technique, tactic, telemetry class, and Sigma logsource. GBSE was applied to a 29-step ALPHV/BlackCat Windows-to-Linux plan, comparing a reconstructed Windows control with the unmodified LLM-generated Linux version. Technique and tactic structure were fully preserved (GED=0, similarity=1.000). Telemetry similarity fell to 0.897 (GED=3) because three steps contained unmapped or drifting observables, while Sigma logsource similarity was 1.000. Every state was classified as Medium Fidelity, with a best composite score of 0.674. The 0.80 deployment threshold was not reached because technical realism scored 0.43 against the required 0.990. The framework includes bipartite GED, a telemetry-intent parser that converts free text into observable classes, and 49 validated Sigma rules: 19 for Linux and 30 for Windows. The rules provide complete ATT&CK technique coverage and pass validation with zero findings. Additional analysis reveals technique-level divergence, including RDP-based external access mapped to unencrypted exfiltration and credential-store access mapped to remote-system discovery. Results were reproduced and verified against recorded outputs.

---


### 15. [Agent Hacks Agent: Autoresearch for Production-Agent Red-Teaming](https://arxiv.org/abs/2607.11698)

**<font color=#1a73e8>作者：</font>** Xutao Mao, Xiang Zheng, Cong Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Production LLM agents such as Claude Code and Codex operate over untrusted content, files, commands, and workspace state, making safety failures directly actionable. Red-teaming must therefore keep pace with evolving models and tools. Existing approaches mainly optimize attack success and preserve artifacts such as benchmarks, payloads, or attack programs, which record where attacks succeed but not the enabling conditions behind unsafe agent behavior. We study automated red-teaming for production LLM agents using one agentic research environment to discover reusable vulnerability knowledge about another. We present AHA, a falsifiable discovery loop that proposes a vulnerability hypothesis, constructs a falsifier, instantiates a valid attack, executes it in a sandboxed harness, reflects on the trajectory, and promotes confirmed findings into a Vulnerability Concept Graph (VCG). Each concept links an attacker-facing surface to an unsafe trajectory through a claim, enabling condition, falsifier, transfer prediction, and supporting evidence. Across Claude Code and Codex on three scenarios covering direct and indirect attacks, the discovered concepts reveal a reusable vulnerability core across models and agents. A frozen VCG requires no further search and outperforms the strongest frozen discovery baseline by 14.2 percentage points under the same single-shot protocol, while transferring across scenarios and attack channels. The resulting VCG provides an auditable artifact for production safety teams to inspect vulnerabilities, validate patches, and accumulate reusable safety knowledge. Our code is available at this https URL.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
