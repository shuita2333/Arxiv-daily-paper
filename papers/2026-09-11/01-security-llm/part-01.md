# 🔐 大模型安全相关研究 | 2026年09月11日

> 本类共 **6** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [In RAG We Trust? Measuring Robustness of Retrieval-Augmented Generation Under Document Poisoning](https://arxiv.org/abs/2609.09243)

**<font color=#1a73e8>作者：</font>** Iliano Fasolino  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) grounds a language model in retrieved documents, which reduces hallucination but creates a new attack surface: if retrieved text is tampered with, the model may repeat the falsehood. We study how much a small quantized model, Llama 3.1 8B, degrades when a fraction of its retrieved context is poisoned. Three corruption strategies are tested, entity swap, number swap, and negation, each applied to zero, one, two, or three of the three retrieved passages, over a factorial sweep of 588 runs on a fact-checking task built from FEVER. Accuracy falls from 77.9% on clean context to 43.5% when all three passages are corrupted. Entity swap flips the largest share of answers that were correct on clean context. Number-based corruption stays flat while poisoned passages are a minority and jumps once they form a majority, a pattern we re-check with query-level bootstrap intervals. The model rarely invents new falsehoods; its dominant reaction is to abstain, and a lexical overlap proxy of unsupported generation falls under attack rather than rising. The study is a small-scale measurement with coarse automated labels; we treat the strategy contrasts as suggestive until decoding is controlled and stronger adjudication is in place.

---


### 2. [An Experimental Evaluation of Multimodal Prompt Injection Attacks on Agentic AI Frameworks](https://arxiv.org/abs/2609.09404)

**<font color=#1a73e8>作者：</font>** Viet K. Nguyen, Mohammad I. Husain  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic AI frameworks let a language model plan, keep memory, and call tools that reach real files, mail, and services. Most of these agents also read images, which gives an attacker a way to put text into the agent's context without going through the user. We present MMPIBench, a reproducible benchmark that measures what happens next. It delivers a fixed set of attacks through six visual carriers (OCR text, overlays, EXIF metadata, QR codes, fake interfaces, and hybrids) and records how far each injected instruction travels through the agent, from perception through planning to the tool call. Across 720 runs covering six frameworks, five foundation models, six carriers, and four attacker objectives, attacks complete in approximately 1% of runs but are attempted in 12.8%, and the gap is closed almost entirely at the planning step, where the model reads the injected instruction and declines to act on it. The model matters far more than the framework for whether an instruction is acted on. One model never attempts an attack and recognizes the injection in 59.7% of runs, while two others attempt in 23.6%. We then extend the benchmark to audio, the only other raw perceptual channel current frontier models accept. Only two of the five models ingest audio and only three of the six frameworks deliver it, but where the signal arrives the attack completes in 49% of cells, and in 75% for one model. Reporting completion alone therefore understates exposure, and perceptual channels beyond vision are narrower but much less defended.

---


### 3. [Arbitrary Cipher Attacks Against Large Language Models Do Not Require Fine-Tuning](https://arxiv.org/abs/2609.09553)

**<font color=#1a73e8>作者：</font>** Thomas Rivasseau  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model safety and security research is preoccupied with, among other things, detecting and preventing jailbreak attacks: alignment bypasses that allow an adversarial user to elicit unwanted or harmful outputs from models. Arbitrary cipher, or covert communication, attacks are one such type of jailbreak and have previously been demonstrated against the fine-tuning APIs of commercial models. In these attacks, target models are trained on a corpus of encrypted harmful questions and responses and subsequently respond to harmful requests through the learned encryption scheme. In this paper, we show that newer frontier models do not require fine-tuning to acquire cipher-based communication skills. Instead, they can learn these skills through prompting and, when necessary, through in-context learning. Furthermore, model alignment is significantly weakened or entirely bypassed when communication occurs through the learned cipher. To the best of our knowledge, this constitutes a novel attack vector against commercial black-box large language models. We demonstrate successful jailbreaks against frontier models developed by Anthropic, Google, and OpenAI. Our attack bypasses commercial harmfulness classifiers because harmful content is encrypted and therefore appears as nonsensical text or gibberish.

---


### 4. [Black-Box Red Teaming of Agentic AI: A Taxonomy-Driven Framework for Automated Risk Discovery](https://arxiv.org/abs/2609.09647)

**<font color=#1a73e8>作者：</font>** Divyanshu Kumar, Nitin Aravind Birur, Tanay Baswa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic systems are rapidly moving to production, where they read untrusted inputs, call tools with real permissions, and act autonomously, expanding the security surface beyond chat-only models. Yet standard evaluations remain single-turn and fail to capture multi-step agent vulnerabilities. We present a systematic black-box framework for risk-aware agent evaluation requiring only basic system descriptions. Our approach introduces: (1) a seven-domain taxonomy mapping observable behaviors to risk categories, (2) fully automated SAGE-RT red teaming producing 120 adversarial scenarios per domain, and (3) human-validated evaluation using LLM judges. Empirical validation across two agent architectures (CrewAI and AutoGen) with four base models reveals alarming patterns: 56.25\% average governance risk, 65\% privacy risk in multi-agent configurations, and agent behavior vulnerabilities reaching 85\%. Our black-box approach effectively identifies critical architectural vulnerabilities without privileged access, providing a scalable path toward safer agent deployments.

---


### 5. [How Fragile Is Safety Alignment at Frontier Scale? A Single-Direction Attack on a 320B MoE](https://arxiv.org/abs/2609.09793)

**<font color=#1a73e8>作者：</font>** Yi Shi, Tanyu Chen, Kai Shen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Directional ablation removes an aligned language model's ability to refuse by projecting a single "refusal direction" out of the weights that write the residual stream. It needs no gradient-based training and no optimization, only a few hundred contrastive prompts, which makes it the canonical white-box attack on open-weight alignment. However, it has been established only on dense models up to roughly 70B parameters. We study whether it survives the shift to frontier mixture-of-experts (MoE) models whose residual streams are no longer a single tensor and whose weights ship quantized. We apply it to GLM-5.3-Flash (320B parameters, 288 routed experts, a four-wide hyper-connection residual, block-FP8). The attack survives the architecture, but what it reaches is no longer where a reader of the original recipe would look for it. Editing the attention, dense and routed-expert writers on their own removes 0.039, 0.016 and 0.148 of refusal respectively; editing all three together removes 0.776. As a result, 74% of the effect exists only under the joint intervention. The part the conventional recipe reaches by module-name matching accounts for 0.066 of that 0.776, which is why it fails silently on an MoE. The effect does not follow from removing just any direction: ablating a random direction orthogonal to it leaves refusal unchanged. A category-concentrated residue survives every edit we tried: subspaces fitted on violence, sexual content and hate leave measurable refusal at every rank from 1 to 12. We report the method, the 41-89 percentage-point reductions it achieves across seven harmful benchmarks with no detected change in capability, and the boundary where it stops.

---


### 6. [CS-Guard: Benchmarking LLM Guardrails for Code Generation Security](https://arxiv.org/abs/2609.09798)

**<font color=#1a73e8>作者：</font>** Jinyang Li, Mingyu Guo, Hung X. Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have been ex- ploited to generate malware, but the effective- ness of guardrails for code generation secu- rity remains unclear. We introduce CS-Guard, the first benchmark to systematically evalu- ate guardrails for code generation security. It covers 1) text-to-code generation with 1000 high-quality malware-generation prompts, 7 jailbreak attacks, and a novel fictional scenario attack (FSA) that embeds malicious intent in a legitimate fictional software-development sce- nario; and 2) code-to-code generation with 331 code prompts spanning code infilling, code completion, and code translation. We empiri- cally evaluate 9 guardrails across seven LLMs. We find that current guardrails perform poorly against malicious code-generation re- quests: for text-to-code, the average attack success rate (ASR) after jailbreaks reaches about 50% for many guardrails; for code-to- code, average ASR approaches 100% on base LLMs and remains high across many guardrails (14.4% to nearly 100%). Our FSA also achieves ASR close to 100% across many guardrails, raising major reliability concerns for real-world software development. To sup- port future research, CS-Guard uses a modular three-layer guardrail taxonomy that lets devel- opers register guardrails for evaluation. We release the benchmark and data to enable fur- ther community evaluation.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
