# 🔐 大模型安全相关研究 | 2026年07月17日

> 本类共 **9** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Operational Evidence Gaps for LLMs in Fraud Detection and Trust-and-Safety Workflows](https://arxiv.org/abs/2607.13078)

**<font color=#1a73e8>作者：</font>** Keyur Gabani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLMs are now proposed for fraud detection, scam investigation, content moderation, and other trust-and-safety workflows. Much of the public literature still evaluates them as models, with less attention to their behavior as components in operational pipelines. This creates a practical evidence question: what would justify placing an LLM inside a live workflow with latency, cost, escalation, human-review, and adversarial-risk constraints?
We address this question through a fraud-first survey of deployment evidence. We code 49 operationally relevant sources on LLM use in fraud detection, investigation support, content moderation, and cross-cutting robustness (18 fraud, 14 moderation, 17 cross-cutting), supplemented by 15 contextual references that establish the survey boundaries. These sources include systems, benchmarks, frameworks, and deployment-relevant surveys, not 49 production deployments.
The main finding is an evidence imbalance. Fraud supplies the largest task-specific portion of the coded corpus. The moderation papers, however, include more explicit public evidence on latency, cost, governance, and fairness. Among the 18 fraud and investigation sources, none report clean per-decision latency, per-decision dollar cost, or calibration evidence; most report offline task performance, retrieval gains, or case-study accuracy instead.
The survey contributes a role-and-evidence organizing frame, FORTE, for locating LLMs as classifiers, retrieval interfaces, explanation generators, reviewer assistants, agents, feature extractors, or escalation components. It also contributes a minimum deployment-evidence checklist covering latency budget, cost per decision, decision threshold, explanation integrity, and adversarial pressure. The resulting agenda identifies studies needed to support deployment claims for LLM-based fraud and trust-and-safety work.

---


### 2. [SingGuard-NSFA: Extensible Guardrails for Agentic AI via Generative Reasoning and Real-Time Classification](https://arxiv.org/abs/2607.13081)

**<font color=#1a73e8>作者：</font>** SingGuard Team  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present nsfaguard, a guardrail framework for securing agentic AI systems against operational threats, such as prompt injection, sensitive information extraction, malicious code requests, dangerous tool misuse, and resource exhaustion. We first introduce the NSFA taxonomy, which organizes 185 risk variants into a CIA-triad-grounded hierarchy and is cross-validated against three well-established OWASP guidelines. Based on this taxonomy, we construct a benchmark suite spanning 133 languages, comprising over 93K purpose-built samples targeting both user queries and agent responses, along with 3,435 cross-source samples adapted from five public agent-security datasets. To detect these operational threats in practice, we develop a dual-mode approach combining SFT-based generative reasoning for interpretable offline auditing with discriminative classification heads on the frozen backbone, enabling real-time detection at approximately 50,ms. We release four models with 0.8B, 2B, 4B, and 9B parameters, all achieving $\geq$94% F1 on purpose-built benchmarks and surpassing the strongest competing guardrails by 6 to 12 absolute points. On cross-source evaluation, the 9B model attains 91.29% F1 with a more balanced precision--recall trade-off. Moreover, ablation experiments show that classification heads can equip a guardrail with risk detection capabilities beyond its original scope and achieve state-of-the-art performance. These results demonstrate the extensibility of the approach and its generality as a plug-in enhancement.

---


### 3. [Securing LLMs in the Wild: Privacy and Security Challenges at the Edge](https://arxiv.org/abs/2607.13088)

**<font color=#1a73e8>作者：</font>** Ren-Yi Huang, Mingchen Li, Dumindu Samaraweera 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are rapidly moving from research settings into the wild, deployed on enterprise infrastructure, personal devices, and edge platforms. While cloud deployments offer scalable compute, concerns over data sovereignty, compliance, latency, and third-party dependence are driving organizations toward edge and on-premise LLMs. This shift introduces new security and privacy challenges: limited compute and memory force aggressive optimizations, including quantization, pruning, model partitioning, and parameter-efficient adaptation, each of which can introduce vulnerabilities and reshape the threat landscape. We describe this tension as the Security-Efficiency Paradox, mechanisms that improve efficiency may weaken robustness, expose new attack surfaces, or increase privacy risks. We examine how compression can degrade safety alignment, how partitioned inference enables reconstruction attacks, and how continuous local adaptation may cause privacy leakage and model drift. To analyze these risks, we introduce a deployment-centric taxonomy organized around three architectural constraints: the Memory Wall, the Quadratic Wall, and the Compute Wall. We derive a unified constraint model that quantifies when unsafe optimizations become unavoidable, linking each wall to specific attack surfaces. Building on this model, we propose the Secure Operational Efficiency Score (SOES), a holistic metric balancing task accuracy, jailbreak resistance, and privacy against energy, memory, and latency, enabling practitioners to configure edge LLMs under real-world hardware limits. We further present a practical decision procedure and targeted mitigations for each optimization-induced vulnerability. Together, these contributions provide a co-designed framework for jointly evaluating security, privacy, and efficiency, laying a foundation for securing edge-native intelligent systems.

---


### 4. [Efficient and Privacy Aware Edge Cloud Collaborative Inference for Large Language Models](https://arxiv.org/abs/2607.13093)

**<font color=#1a73e8>作者：</font>** Yi Li, Chen Li, Jiexiong Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> On-device LLM inference faces a trilemma of response latency, limited hardware resources and user privacy. Full cloud inference delivers strong computing power but exposes user prompts and dialogue data, while standalone on-device inference is unfeasible for most consumer and embedded edge devices. This paper presents a privacy-centric edge-cloud collaborative LLM inference framework built on endpoint-authenticated KV cache. Local endpoints handle input preprocessing, embedding computation, adaptive feature optimization, KV cache authentication, speculative decoding and low-dimensional model head calculation, while the cloud conducts authenticated decoder inference, KV cache management, token verification and high-dimensional vocabulary projection. Endpoints fuse partial outputs, apply language-adaptive masking and sample target tokens. All transmitted data and truncated logits are quantized and AES-GCM encrypted for privacy, with core lightweight modules, draft parameters and cache access policies kept local to avoid leakage. The framework supports heterogeneous devices including CPU-only, GPU-equipped and embedded devices via optimized streaming, batching and quantized ONNX deployment. Evaluations demonstrate that the framework reduces per-token latency by up to 46.1\% and downlink payloads by up to 67.4\% over baseline split inference, retaining comparable performance to full cloud inference.

---


### 5. [WaterMoE: Expert-Routing-based Watermarking for High Fidelity and Efficiency](https://arxiv.org/abs/2607.13099)

**<font color=#1a73e8>作者：</font>** Z Sun, Q Jiang, S Sheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved remarkable success but raise growing concerns about content provenance and misuse, motivating the need for reliable watermarking techniques. However, these techniques have rarely been adopted in practice mainly for two reasons: i) severely degraded model performance, and ii) additional inference overhead. To confirm the problem, we construct a comprehensive benchmark spanning different generation tasks to systematically evaluate 9 representative watermarking methods. We found almost all existing methods are designed for text fluency, but not for restricted and complicated tasks, and their overhead prevents them from deployment in latency-critical systems.
To address i) and ii), we propose an LLM watermarking scheme \textit{WaterMoE} for the growingly popular Mixture-of-Experts (MoE) LLMs. WaterMoE embeds watermarking signals through controlled perturbation into the expert selection at each router, which accumulates to token selection shift at the final output. In contrast to watermarking as a post-processing token-sampling approach, WaterMoE embeds watermark within the inference loop incurring negligible quality degradation and computational overhead. Extensive experiments demonstrate that our method achieves a fidelity performance close to the unwatermarked and consistently outperforms state-of-the-art watermarking methods on the benchmark, with up to $4\times$ speedup, incurring merely 1\% additional inference latency compared to native generation. The results demonstrate the capability of WaterMoE to be deployed in real-world tasks.

---


### 6. [Composable Trust for Language Models: A proven boundary and a measured defense](https://arxiv.org/abs/2607.13149)

**<font color=#1a73e8>作者：</font>** Yakov Pyotr Shkolnikov  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In a language model, instructions and data share one token stream, so nothing inside the model's generation can keep untrusted text from steering it. We develop a trust model that places the authority to act outside the model, in code: a source's standing, not its content, decides which operation runs and whether it acts. A lower-trust source may inform an answer but not override a higher one. An unmodified model runs inside a deterministic pipeline that ranks inputs by source integrity, and a fixed non-model monitor provably chooses the operation and any outside action from trusted inputs alone. We can measure but not prove the pipeline's resistance to injection; we prompt-tune it and report the rate. On a one-shot held-out set with an unmodified Gemma~4 26B model, passivation and a wrapper (the cascade) raise the genuine-leak defended rate from $27\%$ to $94\%$ at roughly a $4\%$ clean-quality cost ($Q_{\mathrm{rel}}{=}0.96$). Under adaptive red-teaming the proved boundary holds unconditionally, and the measured defense stays at $87\%$. The cascade also attributes a lower-trust source's fact rather than dropping it, raising attribution from $0\%$ to $92\%$, and follows the higher-trust source on a conflict.

---


### 7. [The Refusal Residue: When Probes Catch Alignment Faking and When They Don't](https://arxiv.org/abs/2607.13346)

**<font color=#1a73e8>作者：</font>** Aman Mehta  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Alignment faking is dangerous because a model can appear compliant under monitoring while preserving behavior it would reveal when unmonitored. When no scratchpad is visible, behavior alone cannot distinguish strategic from genuine compliance. We ask whether hidden states reveal what outputs hide.
We run a 13-model sweep for naturally-emerging faking, then probe and steer hidden states on the two models that fake. Natural faking appears only in Qwen3-32B (+18.2pp) and Llama-3.1-8B (+24.4pp at n=10, p<10^-15), while explicit scratchpad self-reports are rare (a Claude Opus 4 judge flags faking reasoning in 1.4% of Qwen and 0.0% of Llama compliant scratchpads). Both fakers show an asymmetric refusal residue: monitored compliance shifts toward refusal (d=0.32 Qwen, d=0.33 Llama, both p<0.0001), while refusal representations do not move (p=1.00).
Per-sample detection is model-conditional. Under leakage-free leave-one-query-out probing, detection survives on Llama (AUROC 0.87) but collapses to chance on Qwen (0.43), and cross-model transfer is null. Steering over 2,000 runs barely changes compliance (|h|<0.08), so the detected direction can flag faking but does not by itself control it.
Standard residualized probing leaks across folds and reaches AUROC 0.63 on a control where no faking can occur; naive linear probes reach a meaningless AUROC 1.0; and conventional MLPs overstate detectability by 0.2-0.3 AUROC. For future alignment-faking detection work, we release a five-control measurement framework: multi-token extraction, refuse-vs-refuse confound checks, per-fold residualization, leave-one-query-out evaluation, and orthogonality-constrained probing.

---


### 8. [Protective Capacity Hallucination: When Large Language Models Claim Nonexistent Capabilities](https://arxiv.org/abs/2607.13596)

**<font color=#1a73e8>作者：</font>** Eunna Lee, Jungpyo Nam, Sunjun Hwang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When cast as the protector of a vulnerable user yet given no explicit capability boundary, a large language model (LLM) may respond not by acknowledging its limits but by claiming to have taken -- or to be taking -- a real-world protective action it cannot perform, such as contacting emergency services or administering care. We term this phenomenon Protective Capacity Hallucination (PCH): a self-referential misattribution in which a model, acting in a protective role, asserts physical or institutional agency exceeding its affordances as a language model. In a three-phase study spanning eight LLMs and 13{,}600 sessions, we find PCH jointly gated by situational severity and interactional format: multi-party dialogic input drives it toward ceiling in most models across ordinary service domains, whereas in intimate-partner conflict -- a domain explicitly covered by safety alignment -- it remains at floor in all eight models despite greater physical severity. We interpret PCH as the signature of a deployment-design gap between role assignment and capability-boundary specification: a by-product of partial alignment in which a universally trained pressure to help outruns a domain-selective specification of how to help. Because suppression tracks alignment coverage rather than severity, deployment-side specification of capability boundaries emerges as a general mitigation target.

---


### 9. [Traffic-Aware Randomized Smoothing for LLM-Based Network Intrusion Detection](https://arxiv.org/abs/2607.13801)

**<font color=#1a73e8>作者：</font>** Zhenpeng Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based intrusion detection systems (IDS) are increasingly studied for security monitoring, yet their robustness against feasible traffic manipulation remains largely empirical. We present Traffic-Aware Randomized Smoothing (TA-RS), a classifier-agnostic certified defense that injects Gaussian noise exclusively into the directly controllable (DC) subspace -- features a remote attacker can modify -- during both fine-tuning and certification, aligning the smoothing distribution with the attacker-controllable subspace. We identify a critical prerequisite: applying standard randomized smoothing to clean-trained LLM-IDS yields weak certified accuracy in three of four (model, dataset) pairs tested (14-33%, at or below random) and only 57% in the fourth (43 pp below the noise-augmented result); noise-augmented fine-tuning recovers to 68-100% on two of three benchmark datasets (at sigma=0.25). At the L_inf-equivalent threshold R_inf = epsilon*sqrt(|DC|) (epsilon=0.05), TA-RS achieves 55-100% certified accuracy on CIC-IDS-2018 and HIKARI-2021, with median certified radii (R approx 0.45-0.96) exceeding R_inf by 1.8-5x (across sigma=0.25-1.00). Against a fairly trained iso-trained RS baseline the residual advantage is dataset-dependent (4-19 pp on CIC-IDS-2018). The larger gap -- up to 72 pp against an isotropic RS baseline that shares the DC-noise-augmented training recipe -- primarily reflects the training-certification mismatch rather than DC alignment alone: isotropic test-time noise perturbs uncontrollable features the attacker cannot exploit, triggering abstention rates up to 68%. RT-IoT2022 probes the limits of the method: it fails under the default fine-tuning recipe but recovers to 76%/69% certified accuracy (LLaMA3-8B/Qwen3-8B) when noise augmentation is increased.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
