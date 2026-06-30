# 🔐 大模型安全相关研究 | 2026年07月01日

> 本类共 **15** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems](https://arxiv.org/abs/2606.28425)

**<font color=#1a73e8>作者：</font>** Jimmy Laurence Rippin, Simon C. Marshall, David Demitri Africa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Increasingly autonomous agentic AI systems pose novel multi-agent risks, such as secret collusion via covert communication channels. The natural defence to these collusion attempts is to monitor plain-text communication, but the efficacy of monitors has been called into doubt by increasingly sophisticated model steganography; indeed, some theoretical schemes have been proposed that are information-theoretically or computationally indistinguishable from good-faith plain-text communication. In this paper, we demonstrate that the complexity of these schemes is no longer a safety barrier, as agentic coding models can already produce undetectable stegosystems when given realistic tool usage, such as code execution or accessing research papers through web searches. Agents also adapt when key ingredients are missing, for example, by adding model-sampling components or implementing related keyed coding schemes. We then frame tacit steganographic coordination between agents as a Schelling-point problem and introduce coordination metrics for estimating when two agents are likely to select compatible schemes without explicit prior agreement. Our results suggest a shift in the threat model for covert communication between AI agents, where the main barrier is no longer whether frontier agents can understand and implement sophisticated stegosystems, but coordination: whether independently acting agents can converge on compatible schemes, keys, and parameters. We find substantial convergence on broad scheme families but limited strict one-shot coordination, suggesting that shared artefacts, repeated interaction, and tool-mediated search are the settings where covert communication risks are most acute. Overall, our findings provide empirical grounding for the recent strategic confinement hypothesis, which assumes that capable agents can construct covert channels that survive monitoring.

---


### 2. [LLM agents security duality: a comprehensive survey of self-security and empowered cybersecurity](https://arxiv.org/abs/2606.28450)

**<font color=#1a73e8>作者：</font>** Yiwei Xu, Yong Zhuang, Xuanming Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are rapidly being integrated into real-world systems. Their autonomy and tool-use capabilities generate substantial value while simultaneously expanding the security attack surface. This survey provides a comprehensive overview of the opportunities and challenges of LLM agents in security, focusing on two core areas: (1) threats to LLM agents themselves and corresponding mitigation strategies (LLM agents self-security), and (2) the role of LLM agents in empowering the cybersecurity lifecycle across offense and defense (LLM agents empowered cybersecurity). We first examine the internal and external attack surfaces of agents, propose a taxonomy organized by threat sources, and analyze associated mitigations and evaluation frameworks. We then investigate how agent capabilities are applied in cybersecurity practice and present, to our knowledge, the first agent-empowerment framework aligned with the full cyber offense-defense lifecycle. By systematically surveying these two areas, we are the first to highlight a positive feedback synergy between LLM agents self-security and empowered cybersecurity, offering new insights for the advancement of both. We further identify current limitations and outline promising directions for future research. The insights provided aim to catalyze the coordinated development of LLM agents self-security and agent empowered cybersecurity, paving the way for more capable and robust agent applications.

---


### 3. [Decomposing Memorization Reduction in Privacy-Preserving Fine-Tuning of SLMs for CSIRTs](https://arxiv.org/abs/2606.28479)

**<font color=#1a73e8>作者：</font>** Cristhian Kapelinski, Diego Kreutz  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> CSIRTs increasingly fine tune language models on vulnerability scan records, but these records expose internal network topology and create privacy risks under regulations such as GDPR and LGPD. We present the first empirical study of how DP SGD and HMAC pseudonymization interact when fine tuning small language models with 1B to 3B parameters on structured CSIRT data. We evaluate 96 LoRA adapters across four SLMs and four training regimes, including raw fine tuning, QLoRA with large batch training, and DP SGD with epsilon equal to 2 and 8. We also audit memorization using 20 planted canaries, four extraction attacks, and a dual attack targeting HMAC pseudonymized identifiers.
Our results show three main findings. First, matched update controls reproduce the observed reduction in memorization by reducing the number of optimizer updates alone, accounting for 66 percent to 132 percent of the measured effect, with a mean of 100 percent across three seeds and four models. In this setting, DP SGD provides the formal privacy guarantee but does not produce additional measurable reductions in memorization. Second, HMAC pseudonymization removes the original identifiers from the exposure surface, reducing exposure by 40 percent to 61 percent, while pseudonymized identifiers remain close to the expected random baseline and do not become a secondary memorization target. Third, F1 scores remain between 0.19 and 0.28 across all 96 adapters using four shot prompting, indicating that, under the evaluated training budget, 1B to 3B SLMs do not achieve operationally useful performance.

---


### 4. [RIPA: Sensory-Vector Prompt Injection Attacks on LLM-Controlled ROS 2 Robots](https://arxiv.org/abs/2606.28649)

**<font color=#1a73e8>作者：</font>** Nima Dorzhiev  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present RIPA, the first systematic multi-channel empirical study of prompt injection attacks delivered through the sensory pipeline of a ROS 2-based LLM-controlled robotic system. Across 100 independent runs per injection variant on five LLMs spanning four model families and parameter scales from approximately 4B to approximately 284B (DeepSeek-V4-Flash, Llama-3-8B-Instruct-Lite, Llama-3.3-70B-Instruct-Turbo, Qwen 2.5-7B-Instruct-Turbo, Gemma-3n-E4B), we identify model-specific vulnerability profiles that do not follow a monotonic scaling trend: Llama-3.3-70B-Instruct-Turbo exhibits 100% attack success rate (ASR) across all injection variants, while Llama-3-8B-Instruct-Lite and Qwen 2.5-7B-Instruct-Turbo resist direct-override injection (0% ASR), and the smallest model evaluated (Gemma-3n-E4B, approximately 4B) matches the 70B model's vulnerability profile, indicating that robustness is model-specific rather than scale-dependent. We propose a hybrid semantic firewall that achieves 0% ASR against known injection patterns with no false positives on a preliminary benign set (0/20 commands) but exhibits a 10.2% trial-weighted bypass rate (58/570 trials; N equals 30 per payload across 19 obfuscation payloads) against adversarially obfuscated attacks, exposing a critical gap between rule-based and semantic defense layers. We further introduce three sensory injection channels: visual (Channel 1, via OCR), audio (Channel 2, via Whisper STT), and LiDAR sensor context poisoning (Channel 3). We show that Channel 3, which injects fabricated obstacle data into the robot environment-state representation at the LLM system-prompt level, achieves 100% ASR across all variants on DeepSeek-V4-Flash. We also contribute a firewall bypass taxonomy spanning 19 obfuscation payloads across five categories. All code, data, and results are publicly available.

---


### 5. [Why Trust Your Agent? Empirical Security Gains from TRiSM-Guided Agentic Workflows in Healthcare](https://arxiv.org/abs/2606.28666)

**<font color=#1a73e8>作者：</font>** Liam Kearns  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent-based AI has enabled the automation of tasks by exposing application tools and resources to large language models (LLMs). However, to improve scope and accuracy, agents are often given access rights that exceed those of ordinary users, introducing significant security risks. AI is routinely integrated into applications with a disregard to security, risking data exposure and breaching regulations. This paper applies the AI Trust, Risk, and Security Management (TRiSM) framework to a medical report-generation application to demonstrate how an insecure agent workflow can be transformed into security-conscious agentic workflow. Both workflows were evaluated across five LLMs (Claude Haiku 4.5, GPT-4.1-nano, GPT-4.1-mini, GPT-5.4-mini, and Gemini 2.5 Flash) on two report types, totalling 800 generations and 500 attack scenarios including RAG poisoning, data-field injection, and client-side network injection. The TRiSM-guided agentic workflow reduced mean attack success rates from 31% to 10% for RAG poisoning and from 42% to 25% for data-field injection, while eliminating the network injection vector entirely through server-side prompt construction. Furthermore, report accuracy increased by 14 percentage points (72.5% to 86.5%) with the agentic workflow, demonstrating a secure design which provides more reliable outputs. This paper contributes to knowledge by demonstrating least-privilege, defence in depth agentic workflows improving security and accuracy, while also highlighting model choice is a necessary architectural consideration.

---


### 6. [Capability Gates Are Not Authorization: Confused-Deputy Failures in LLM Agent Frameworks](https://arxiv.org/abs/2606.28679)

**<font color=#1a73e8>作者：</font>** David Mellafe Zuvic  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents increasingly read untrusted content while holding side-effecting tools such as payments, email, CRM, and infrastructure APIs, yet common framework defaults still conflate tool exposure with authorization. We audit whether LangChain/LangGraph, LlamaIndex, and the Stripe Agent Toolkit re-authorize each model-emitted call, with concrete argument values, before execution. Across pinned public-source commits, all three provide capability gating by default, but none provides a deterministic fail-closed per-call value authorization gate by default. We introduce ScopeGate, a five-stage PDP/PEP for agent tool calls: scope, authorization, money ceiling, idempotency, and default deny. Evaluation shows the identical unauthorized payout call executes under LangChain's default dispatch (with a companion LlamaIndex PoC) but is denied by ScopeGate; the tested control reports 0/48 static bypasses, 0/29 unauthorized attempts (40-iteration adaptive run), 0/10 benign false-denies, and Latam-GPT payment-agent containment at 10/10. ASR denotes attempted unauthorized action, containment is not a cure, deployment-tier claims are inference over measured model classes, and no CVE is asserted.

---


### 7. [FlipGuard: Defending Large Language Models Against Quantization-Conditioned Backdoor Attacks](https://arxiv.org/abs/2606.28962)

**<font color=#1a73e8>作者：</font>** Aoying Zheng, Anqi Du, Zizhuang Deng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model quantization is essential for the efficient deployment of Large Language Models (LLMs), but introduces a critical vulnerability: Quantization-Conditioned Backdoor (QCB) attacks. In these attacks, malicious behaviors remain dormant in full-precision models and activate only after specific quantization distortions, bypassing standard security audits. To mitigate this, we introduce FlipGuard, a proactive defense framework that selectively perturbs model weights prior to quantization. By breaking the adversary's precise alignment between weight patterns and quantization boundaries, FlipGuard suppresses backdoor activation without requiring access to training data or trigger samples. We further propose the Defense Effectiveness Ratio (DER), a unified metric to jointly evaluate security gains, utility preservation, and computational cost. Extensive experiments across seven LLMs (including StarCoder and LLaMA-family models) and three quantization schemes (INT8, FP4, NF4) demonstrate that FlipGuard effectively neutralizes QCBs across three scenarios, i.e., vulnerable code generation, content injection, and over-refusal, achieving high security with negligible performance degradation.

---


### 8. [Breaking the Rounding Trap: Securing LLMs against Quantization-Conditioned Backdoors](https://arxiv.org/abs/2606.29239)

**<font color=#1a73e8>作者：</font>** Aoying Zheng, Anqi Du, Zizhuang Deng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model quantization is a key technique for reducing storage and inference costs when deploying large language models in practice. However, recent studies show that the discretization and rounding errors introduced by quantization can be exploited by adversaries to construct quantization-conditioned backdoor (QCB) attacks. Under such attacks, malicious behaviors remain dormant in the full-precision stage and are activated only after quantized deployment, thereby bypassing conventional security auditing and detection mechanisms. To address this threat, we propose a proactive pre-quantization defense method, QuantGuard. Our method introduces differentiable rounding control variables and combines error-guided rounding reversal constraints, output-distribution consistency, and weight-distance regularization to finely regulate critical rounding behaviors. Crucially, QuantGuard utilizes only a small calibration dataset and does not modify existing quantization algorithms. This design breaks the precise alignment between attacker-crafted weight patterns and quantization boundaries, effectively suppressing the post-quantization backdoor activation pathway while preserving the model's original functionality and performance. We conduct systematic experiments on six mainstream LLMs (including the LLaMA-3 and Qwen2.5-Coder) using three quantization precisions (INT8, FP4, and NF4) across three representative scenarios: vulnerable code generation, content injection, and over-refusal. The results show that QuantGuard consistently mitigates QCB attacks, reducing the attack success rate to a level comparable to the clean model while largely preserving performance on general capability benchmarks. With low computational overhead, our method offers an effective, practical solution for secure quantized LLM deployment.

---


### 9. [Closing the Activation-Cone Blind Spot: Response-Time Probing and Unified Defense](https://arxiv.org/abs/2606.29441)

**<font color=#1a73e8>作者：</font>** Subhadip Mitra  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Inference-time safety methods for large language models have proliferated, yet no systematic comparison exists. We evaluate five defense paradigms (no defense, static steering, CAST, AlphaSteer, probe-gated) across seven instruction-tuned models (7-31B) and five attack types (GCG, AutoDAN, DeepInception, prefilling, intent laundering). Our central finding: prompt-time activation defenses are structurally blind to prefilling attacks. AlphaSteer achieves 0% attack success on GCG, AutoDAN, and intent laundering but 50% on prefilling. We prove a corollary: any defense that gates intervention on a single layer's activation alignment with a benign reference (cone, subspace, or null-space) is blind to attacks that craft activations to lie inside that reference, whether checked at prompt time or per token. As its constructive contrapositive we introduce response-time probing: a linear probe on the model's hidden state at the first generated tokens, with AUROC 0.97-1.00 across all seven models. Combined with a halt, it cuts prefilling attack success to 0/40 on every model with 0% benign false positives, outperforming Llama Guard 3. Cross-template generalisation depends on probe depth, so we scope the claim to the canonical prefilling-template family. Composing the response-halt with AlphaSteer's null-space steering gives an orthogonal split (the halt catches prefilling, AlphaSteer catches semantic attacks), reaching defense success 0.983 on Mistral and 0.994 on Llama and dominating both components. We further show MMLU fails to capture steering's true utility cost, which appears as behavioral hedging rather than factual loss, and that diverse negative training sets cut probe false positives from 80-100% to near zero. Code, attacks, per-sample results, and the judge prompt are released.

---


### 10. [SurrogateShield: Beyond Redaction for High-Utility, Privacy-Preserving LLM Interactions](https://arxiv.org/abs/2606.29567)

**<font color=#1a73e8>作者：</font>** Sherwin Vishesh Jathanna  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based assistants transmit user queries verbatim to third-party API endpoints that lie outside the user's audit or control. When those queries contain personally identifiable information (PII), the data persists on remote infrastructure subject to breach, subpoena, or policy change. Placeholder redaction (the prevailing mitigation) suppresses PII at the cost of semantic coherence, producing structurally degraded queries and correspondingly degraded responses.
We present SurrogateShield, a client-side proxy that substitutes detected PII with locally generated, type-consistent surrogate values prior to transmission and restores originals in the response. No real PII crosses the network boundary. Detection runs through a three-stage cascade (PatternScan, EntityTrace, and ContextGuard) covering 22 PII types and quasi-identifier combinations grounded in Sweeney's k-anonymity framework. Surrogate-to-original mappings are sealed in an AES-256-GCM encrypted per-conversation ShadowMap that never leaves the device.
Evaluations on a 1,124-query corpus demonstrate that the cascade reliably detects PII, achieving an overall F1 score of 98.87%. Surrogate substitution substantially outperforms placeholder redaction in semantic utility, yielding a 13.26 pp improvement in BERTScore (roberta-large), from 81.59% to 94.85%. Within this corpus, the local pipeline restricted real PII transmission across all tested query types; in a 100-query adversarial trial, a prompted LLM adversary recovered no original values from surrogate-substituted messages.

---


### 11. [An Empirical Evaluation of Prompt Injection Vulnerabilities in Large Language Models Across Multilingual and Obfuscated Attack Scenarios](https://arxiv.org/abs/2606.29602)

**<font color=#1a73e8>作者：</font>** Caglar Uysal, Baturay Birinci, Süha Orhun Mutluergil 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have rapidly evolved, transforming industries by automating complex tasks and generating human-like content. However, as their adoption accelerates, prompt injection vulnerabilities have become increasingly apparent. Malicious actors exploit these weaknesses to generate phishing emails, deceptive websites, nd malware, posing serious security risks. This paper presents an empirical evaluation of six state-of-the-art LLMs (DeepSeek, GPT, Gemini, Grok, Llama, and Qwen) under diverse adversarial prompt scenarios, including direct and multi-stage obfuscated attacks across multiple languages and character encodings. The proposed framework measures how effectively current LLMs resist manipulation into performing harmful actions. Our findings reveal systematic vulnerabilities across all tested models. Even direct prompt injections frequently induce the generation of phishing content, websites, and malware, while elaborate prompts achieve even higher malicious compliance rates, particularly for phishing. Models such as DeepSeek, Gemini, and Grok show especially high susceptibility under complex instructions. Notably, non-English languages consistently exhibit higher compliance rates than English, exposing significant gaps in multilingual safety alignment. Although simple character encodings reduce malicious outputs, they do not eliminate them. These results highlight persistent challenges in LLM safety and underscore the urgent need for stronger defenses and improved security mechanisms to support the ethical and secure deployment of LLMs in cybersecurity sensitive contexts.

---


### 12. [On the Internet, Nobody Knows You're an LLM Bot: Unmasking Web Agents with Multi-Layer Fingerprinting](https://arxiv.org/abs/2606.30119)

**<font color=#1a73e8>作者：</font>** Iliana Fayolle, Sihem Bouhenniche, Samuel Pélissier 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Since 2023, a new class of bots has emerged: Web Agents. They can automate complex tasks on the Web, going beyond traditional browser automation tools such as Selenium, Puppeteer, or Playwright. Leveraging large language models (LLMs), these agents are capable of solving anti-bot mechanisms, mimicking human behavior, and, in some cases, operating directly from the local machine of the user configuring them. As a result, it is becoming increasingly difficult for website administrators to detect and block these LLM-based bots. Modern Web Agents commonly integrate stealth and anti-detection techniques, while numerous proprietary and open-source anti-bot mechanisms have emerged recently, specifically to block them. However, despite their growing prevalence, there is little evaluation of the effectiveness of state-of-the-art anti-bot mechanisms against these LLM-based bots and their stealth capabilities. Likewise, no prior work has comprehensively studied how to characterize and distinguish Web Agents deployed either in the cloud or locally. This paper addresses these open questions by deploying multiple honeysites protected by one or more anti-bot mechanisms (e.g., this http URL, CAPTCHAs, proof-of-work, and Cloudflare's free proprietary solutions). We integrated network-, HTTP-, and browser-level fingerprinting techniques, and prompted six LLM-based Web Agents to visit the deployed honeysites. Our analysis reveals three main findings: (i) some Web Agents were able to bypass all evaluated anti-bot mechanisms; (ii) all evaluated Web Agents can be distinguished both from humans and from one another using multi-layer fingerprinting techniques across network, HTTP and browser layers; (iii) stealth and anti-detection mechanisms often increase detectability rather than decrease it.

---


### 13. [A Multi-task Mixture of Experts Framework for Malware Classification, Packing Detection, and Family Attribution](https://arxiv.org/abs/2606.30572)

**<font color=#1a73e8>作者：</font>** Jithin S., Roshin Sleeba C., Anvin Mariya P. B. 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Malware classification remains a challenging problem due to its inherent heterogeneity, the presence of packed binaries, and the diverse distribution of malware families. Traditional single-model detection mechanisms often fail to generalize across such diverse data, leading to degraded performance, particularly on obfuscated and rare malware samples. In this work, we propose a unified multi-task malware analysis framework based on Mixture of Experts (MoE) architectures. The proposed system evaluates performance across two different input representations, i.e., high-dimensional EMBER feature sets and raw 1D byte arrays extracted from Portable Executable files. It simultaneously performs three critical tasks: malware family classification, packed versus unpacked detection, and malware versus benign identification. By decomposing the problem into specialized expert networks and employing adaptive gating mechanisms, the model enables effective task-specific learning while maintaining overall scalability. We investigate multiple architectural variants, including Homogeneous MoE, Heterogeneous MoE, and Multi-Gate MoE (MMoE). Performance is evaluated in both standard and adversarial settings using original and mutated samples. The obtained results demonstrate that the Multi-Gate MoE model achieves the best performance, reaching a combined detection rate of 0.9744 with only $2.56\%$ failure rate. Moreover, this configuration exhibits improved robustness under mutation-induced distribution shifts. Our findings highlight the effectiveness of expert specialization and task-specific routing in handling complex malware distributions, making the proposed framework a promising direction for scalable and resilient malware detection systems.

---


### 14. [A Hybrid Framework For Crypto-Ransomware Detection In Enterprise Shared Storage](https://arxiv.org/abs/2606.30586)

**<font color=#1a73e8>作者：</font>** Gervais Hatungimana, Abdun Naser Mahmood, Mohammad Jabed Morshed Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Most corporate workplace environments enforce policies and technical controls that limit the storage of sensitive data on client endpoints. Consequently, ransomware operators have evolved variants that expand their attack surface from local systems to network drives and shared storage resources. As traditional endpoint detection mechanisms focus primarily on local system behaviour, a compromised client can impact remote file servers, such as by encrypting shared data, without directly triggering behavioural changes on the servers themselves. In this paper, we propose a hybrid detection framework for detecting crypto-ransomware intrusion within integrated file server and client environments. The framework is based on a new technique referred to as Region of Interest (RoI) to analyse network traffic and extract Indicators of Compromise (IoCs). The IoC repository serves as an additional ruleset to enhance existing security tools such as EDRs and IDSs, while RoI-derived features are used to train an ML model to detect highly evasive variants. This study incorporates a broader set of ransomwares families and carefully selected benign behaviors based on domain expertise, ensuring coverage of common user actions that could interfere with ransomware detection. Beyond IoCs, which operate in a signature-based manner, our machine learning module achieves a detection precision of 99.64%, with a 0% false negative rate (FNR) and a minimal false positive rate (FPR). Furthermore, the proposed method enables early detection, identifying ransomware intrusions before significant damage occurs, achieving an accuracy of 99.44%.

---


### 15. [Words Speak Louder Than Code: Investigating Cognitive Heuristics in LLM-Based Code Vulnerability Detection](https://arxiv.org/abs/2606.30587)

**<font color=#1a73e8>作者：</font>** Asif Shahriar, Hongyu Cai, Hadjer Benkraouda 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Researchers and practitioners increasingly apply Large Language Models (LLMs) for automated vulnerability detection. Recent work has shown that LLMs are susceptible to the same cognitive heuristics that bias human judgment. Yet, no work has investigated whether these heuristics affect a model's assessment of code vulnerabilities. In this paper, we present the first systematic exploration of cognitive heuristics in LLM-driven code vulnerability detection. We introduce a controlled framework that holds the code fixed and only varies the surrounding context to trigger three cognitive heuristics: the halo effect through author attribution, the framing effect through task objectives and consequences, and the anchoring effect through prior analysis results. Within this framework, we evaluate eight LLMs across three programming languages and perform both quantitative and code-level analyses. Our findings demonstrate that all evaluated models are susceptible to these heuristics. Cross-model average susceptibility is highest for framing at 33.2%, followed by anchoring at 23.5% and halo at 18.4%. Code-level analysis reveals that vulnerabilities that require semantic reasoning for detection are more susceptible to cognitive heuristics than those identifiable through pattern matching. Furthermore, models often change their verdict from safe to vulnerable based on the cognitive condition, without accurately identifying the actual vulnerability. To highlight the practical impact, we demonstrate a proof-of-concept black-box cognitive attack that can suppress up to 97% of previously detected vulnerabilities. These findings indicate that cognitive susceptibility is a consistent and exploitable property of LLM-based vulnerability detection.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
