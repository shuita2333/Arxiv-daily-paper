# 🔐 大模型安全相关研究 | 2026年05月22日

> 本类共 **7** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Adaptive Probe-based Steering for Robust LLM Jailbreaking](https://arxiv.org/abs/2605.20286)

**<font color=#1a73e8>作者：</font>** Junxi Chen, Junhao Dong, Xiaohua Xie  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent work has demonstrated the potential of contrastive steering for jailbreaking Large Language Models (LLMs). However, existing methods rely on limited and inherently biased contrastive prompts and require laborious manual tuning of steering strength, limiting their robustness and effectiveness. In this paper, we leverage the idea of model extraction to guide the learned steering vectors to approximate the ideal one and propose tuning the steering strength adaptively based on contrastive activations' statistics. Experiments demonstrate that our method notably improves the effectiveness and robustness of probe-based steering, without any extra contrastive prompts or laborious manual tuning. Being an attack paper, this paper focuses on revealing the breakdown of fortified LLMs, raising the average harmfulness score from 6\% to 70\%. Our code is available at this https URL.

---


### 2. [Refusal Evaluation in Coding LLMs and Code Agents: A Systematic Review of Thirteen Malicious-Code Prompt Corpora (2023-2025)](https://arxiv.org/abs/2605.20351)

**<font color=#1a73e8>作者：</font>** Richard J. Young, Gregory D. Moody  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The evaluation of large language model refusal on malicious-coding tasks now spans at least thirteen publicly released prompt corpora (AdvBench, the CyberSecEval family, RMCBench, RedCode, MCGMark, JailbreakBench, CySecBench, MalwareBench, CIRCLE, MOCHA, ASTRA, Scam2Prompt / Innoc2Scam-bench, and JAWS-Bench), each constructed under a different protocol, released under different licensing terms, and validated (or not) against different inter-rater reliability standards. Existing surveys treat code security, jailbreak taxonomy, or vulnerability detection as the central object and mention these corpora only in passing. This paper reverses that framing: it treats the prompt datasets themselves as the unit of analysis. Following a PRISMA-style protocol, we specify a search strategy, screen the recent literature on coding-LLM refusal evaluation, apply a uniform extraction template to each in-scope corpus, and synthesize the resulting catalogue along construction methodology, prompt-construction taxonomy (modality, turn structure, elicitation style), reproducibility and licensing, and malware-category coverage. The synthesis surfaces three recurring methodological gaps: the absence of human-annotator baselines against which LLM-judge labels can be calibrated, the absence of cross-corpus comparability with refusal-rate statistics measuring non-equivalent constructs, and the fragmentation of malware-category taxonomies, with no canonical schema spanning the thirteen in-scope corpora. The review concludes with proposed methodological directions for next-generation corpora, including pre-registration of inclusion criteria, vendor-diverse multi-judge validation, Fleiss' kappa with bootstrap CI as the reliability baseline, and a candidate canonical taxonomy.

---


### 3. [Security Document Classification with a Fine-Tuned Local Large Language Model: Benchmark Data and an Open-Source System](https://arxiv.org/abs/2605.20368)

**<font color=#1a73e8>作者：</font>** Ivan Dobrovolskyi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Organizations that scan documents for sensitive information face a practical problem. Cloud services require data to be sent to external infrastructure, while rule-based tools often miss threats that depend on context. This study presents TorchSight, an open-source local system for security document classification built around a fine-tuned Qwen 3.5 27B model. The model was trained on 78,358 samples from 13 permissively licensed sources and GPT-4 synthetic data covering seven security categories and 51 subcategories. In the main evaluation on 1,000 documents, the model reached 95.0% category-level accuracy (95% confidence interval: 93.5-96.2). The tested commercial models scored 75.4-79.9% under the same prompting protocol. On a separate external set of 500 held-out samples, the model reached 93.8% accuracy, which suggests that performance extends beyond the main benchmark, although the margin depends on dataset composition and difficult boundary cases. The results show that a fine-tuned local model can support accurate security document classification while keeping document processing under local control.

---


### 4. [Latent Geometry as a Structural Monitor: Eigenspace Alignment for Anomaly Detection in Anonymity Networks](https://arxiv.org/abs/2605.20391)

**<font color=#1a73e8>作者：</font>** Vaibhav Chhabra  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Traditional anomaly detection marks events when measured signals cross predefined thresholds. This captures the moment of transition but not the structural pressure that precedes it. We propose treating large behavioral populations as geometric energy landscapes whose deformation can be measured before and during major transitions. The central thesis is that structure precedes geometry: the structural organization of the population is the signal, and geometric metrics are instruments for measuring it. Applied to the Tor anonymity network across 67 consecutive daily observation windows, the dual-observer pipeline identifies a stable nine-dimensional load-bearing subspace invariant across the observation period and validates this structure by Monte Carlo simulation at 16.8 sigma above the noise floor. Primary detection gates achieve 0.0% false positive rate on 24 confirmed stable windows. Forensic analysis of the February 20, 2026 confirmed infrastructure event formally falsifies the relay-departure hypothesis, identifying connectivity degradation without topology change as a detectable network failure mode. The result is a candidate structural-monitoring framework for behavioral populations with sufficient telemetry.

---


### 5. [Trusted Weights, Treacherous Optimizations? Optimization-Triggered Backdoor Attacks on LLMs](https://arxiv.org/abs/2605.20641)

**<font color=#1a73e8>作者：</font>** Yifei Wang, Tianlin Li, Xiaohan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Inference optimization is a vital technique for deploying LLMs at scale. Compilation is the most widely adopted optimization technique for LLMs. While it assumes semantic equivalence between the original and compiled graphs, we first uncover its numerical side effects can be maliciously exploited to implant stealthy backdoors in LLMs. We propose a unified optimization-triggered attack framework comprising two complementary strategies. Without any modification to the compiler or hardware, one strategy flips predictions for specific inputs only when the model is compiled, while the other uses a universal trigger that remains dormant under uncompiled execution but hijacks arbitrary inputs once compilation optimization is applied. Both attacks bypass standard safety evaluations run without compilation. We empirically demonstrate that these optimization-triggered backdoors achieve attack success rates averaging 90% across four mainstream open-source LLMs and four tasks, while clean accuracy is preserved at nearly 100% under all settings. Our findings reveal a novel attack surface at the intersection of optimization and security in the LLM deployment pipeline, and we investigate practical defenses to mitigate this threat.

---


### 6. [An Application-Layer Multi-Modal Covert-Channel Reference Monitor for LLM Agent Egress](https://arxiv.org/abs/2605.20734)

**<font color=#1a73e8>作者：</font>** Alfredo Metere  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A large language model (LLM) agent that sends messages can leak data inside them. Destination allowlists and content scanners do not police whether an otherwise-benign payload is itself a covert channel: a compromised agent encodes bits in zero-width characters, homoglyphs, whitespace, base64, JavaScript Object Notation (JSON) key ordering, message timing or size -- and, in binary egress, in least-significant-bit (LSB) pixel planes, per-image mean luminance, inter-image sequence permutation, ultrasonic tones, or audible-band sonified data. Our egress reference monitor has three contributions. (i) A text pipeline of ten capacity-reducing stages, a per-sink leaky-bucket capacity ledger, and a staged posture that enforces lossless stages from day one. (ii) Two media scramblers (a Fourier-domain audio band-limiter and a red-green-blue (RGB) image bit-depth and mean-luminance bucketer) gated by a boot-time cryptographic legitimacy attestation: an auditor publishes at boot the trusted Ed25519 keys and {kind, data-class} pairs; only payloads with a verifying signature for an authorized class are exempt. The attestation sidesteps the intractable content-based discrimination between real media and data sonified or rasterized as a carrier; unsigned media is suspect by default; a content-addressed canonicalizer closes the inter-image permutation channel. (iii) Residual capacity is the Miller--Madow corrected mutual information between embedded and recovered bits (zero when destroyed), measured by an adversarial ensemble of fifteen working encoders across text, image and audio. The reference implementation drives residual capacity to zero on every destroyable channel and to a stated bound on the one (per-image mean luminance) that cannot be destroyed without ruining the image.

---


### 7. [Rethinking Fraud Safety Evaluation: Multi-Round Attacks Reveal Safety-Utility Tradeoffs in Graph-Context LLM Defenders](https://arxiv.org/abs/2605.20759)

**<font color=#1a73e8>作者：</font>** Laura Jiang, Reza Ryan, Qian Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Single-turn safety evaluation is a poor proxy for real fraud defense, where attackers escalate across multiple rounds. This paper evaluates fraud defenders under replay and adaptive multi-round attacks and measures when a defender refuses, not just whether it eventually refuses. On a frozen multi-round suite built from Fraud-R1, graph-context defenders improve early safe refusal relative to text-only baselines under both replay and adaptive fraud pressure, but they also produce substantially more benign over-refusal. Direct probing of the trained graph encoder, together with paired shuffle-risk ablations on both fraud and benign sides replicated across two seeds on the Qwen-1.5B backbone, localises this cost to how the defender LLM consumes structured context rather than to graph-encoder quality: the encoder cleanly separates fraud from benign, while the LLM responds primarily to the presence of structured graph fields and only secondarily, and asymmetrically, to risk-score magnitude. Temporal graph context is directionally stronger than static and significantly better grounded, but is not yet conclusively superior on the main refusal metrics. The contribution is evaluative and measurement-oriented: robust fraud assessment must be multi-round, must report refusal timing, must account for benign false positives alongside fraud-side safety gains, and must localize observed costs to the graph signal or to how the LLM consumes it.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
