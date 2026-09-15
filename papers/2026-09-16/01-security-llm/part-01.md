# 🔐 大模型安全相关研究 | 2026年09月16日

> 本类共 **17** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Machine Unlearning for Speech Question Answering in Large Audio-Language Models](https://arxiv.org/abs/2609.13195)

**<font color=#1a73e8>作者：</font>** Zhe Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Audio-Language Models (LALMs) have recently shown strong capabilities in speech understanding and question answering (QA), but they also inherit privacy risks from large-scale training data, including the unintended memorization of sensitive information. In this work, we study machine unlearning for speech QA in LALMs, a setting that is more challenging than prior work on text-based Large Language Models (LLMs) or Automatic Speech Recognition (ASR) due to the tight coupling between acoustic perception and factual knowledge. We present and evaluate multiple unlearning strategies, including gradient ascent, task arithmetic, and alignment-based fine-tuning methods that enforce safe refusal responses, to remove private knowledge while still preserving performance on core capabilities. Through extensive experiments on speech QA datasets, we show that these unlearning methods can reduce the privacy leakage rate by up to 80% while maintaining near-neutral performance on non-private speech QA and general speech understanding benchmarks.

---


### 2. [BadEngram: Backdoor Attack on Gated Memory Components in LLMs](https://arxiv.org/abs/2609.13478)

**<font color=#1a73e8>作者：</font>** Ariel Fogel, Omer Hofman, Eilon Cohen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> To expand open-weight models' capacity without proportionally increasing computation, recent language models incorporate gated parametric memories that retrieve learned values and inject them into intermediate representations. Despite these efficiency benefits, such modules create a distinct attack surface: their parameters can be modified independently of the backbone while directly shaping its computation. We introduce BadEngram, a post-training attack that exploits this surface to implant persistent, trigger-dependent behavior while leaving conventional backbone weights and the execution graph unchanged. We first establish the attack's feasibility and causally characterize its mechanism in a controlled Engram model, where BadEngram achieves 96.6% ASR on triggered inputs while limiting false activation on matched trigger-free inputs to 0.1% and preserving 99.6% clean accuracy. Replacing the retrieved memory values with their clean counterparts or closing the memory gates reduces ASR to at most 0.32%, confirming that the backdoor is expressed through the gated-memory pathway. We then test whether this vulnerability extends to production scale in Qwen3.8-Flash-Next's native Per-Layer Embedding subsystem. Using independently trained checkpoints for the two benchmarks, BadEngram achieves 50.4% ASR on HarmBench and 60.0% on AdvBench, while dormant-condition ASR remains 0.9% and 0.0%, respectively. These results identify native gated-memory parameters as a security-critical part of the model whose integrity cannot be inferred from an unchanged backbone.

---


### 3. [An Efficient and Modular Framework for Targeted Harm Mitigation in LLMS](https://arxiv.org/abs/2609.13624)

**<font color=#1a73e8>作者：</font>** Roberto Campbell, Momin Abbass, Muneeza Azmat 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are powerful zero-shot learners but remain prone to misalignment with human preferences, often producing biased, toxic, or otherwise harmful outputs. Existing alignment methods, while effective, are costly and tightly coupled to the model, limiting flexibility and scalability. We propose a modular correction framework that augments pretrained LLMs with Activated LoRA (aLoRA) adapters and a context-aware routing mechanism to eliminate harms from misaligned model responses. Our approach enables expert adapters to activate mid-sequence without invalidating the KV cache, allowing low-latency, targeted correction during generation. Each expert is trained to detect and mitigate specific harms, such as bias or toxicity. A learned router dynamically selects appropriate experts based on the models intermediate outputs. We demonstrate that our system improves alignment on standard safety benchmarks while preserving task performance, offering a lightweight and efficient path toward safer and more controllable LLM deployments.

---


### 4. [PriMobiBench: Characterizing Visual Privacy Leakage in VLM-Driven Mobile GUI Agents](https://arxiv.org/abs/2609.13873)

**<font color=#1a73e8>作者：</font>** Qihang Cen, Tianshuo Cong, Da Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mobile GUI agents increasingly rely on Vision-Language Models (VLMs) to automate smartphone tasks by interpreting screenshot streams. However, this design introduces serious and underexplored privacy risks, including direct leakage of sensitive on-screen information and unintended user profiling. The absence of standardized benchmarks makes it difficult to quantify these risks in realistic mobile agent workflows. To address this gap, we propose PriMobiBench, the first benchmark for systematically evaluating privacy leakage and visual profiling in screenshot-driven mobile agents. It provides a unified pipeline for data generation, agent trajectory construction, and multi-model evaluation. We also introduce MobiLeak, a dataset of execution traces from 16 apps, covering 25 privacy attributes with 2,960 embedded privacy instances. Our results reveal substantial risks: (1) VLMs can directly extract sensitive information with up to 82.5% success rate; (2) beyond explicit leakage, they can infer user profiles from aggregated visual evidence with approximately 70% success. We further propose a mitigation that masks privacy-sensitive but task-irrelevant UI elements before cloud processing, reducing profiling success by up to 58% with only approximately 8% performance loss. Overall, our work provides the first systematic benchmark for visual privacy risks in mobile GUI agents, demonstrates that both leakage and profiling are feasible at a highly concerning level, and offers a practical direction for mitigation.

---


### 5. [When Malicious Instructions Persist: Persistent Memory Poisoning Attack on Harness-Based Agents](https://arxiv.org/abs/2609.13889)

**<font color=#1a73e8>作者：</font>** Shuhuai Huang, Jingfeng Zhang, Hong Jia  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Harness design has transformed the development of LLM-based agents by integrating memory, tool use, and runtime control. However, this design also introduces security and privacy risks because malicious instructions from external sources may be written into persistent memory and persist across sessions. To study this risk, we propose PMPA, a Persistent Memory Poisoning Attack against harness-based agents. PMPA embeds malicious instructions into benign external sources and induces the victim agent to write them into persistent memory without directly accessing to the agent framework. Once stored, the poisoned memory can be retrieved in later sessions, triggering additional malicious actions and causing privacy leakage. We evaluate PMPA on OpenClaw and Claude Code across different backbone LLMs, input modalities, and trigger scenarios. Across all settings, PMPA achieves average Injection Success Rate (ISR) and Cross-session Attack Success Rate (C-ASR) of 73.7%/ 55.5% on OpenClaw and 66.9%/ 81.7% on Claude Code, while preserving benign task performance on both systems. We further evaluate a targeted prompt-level defense and find that it can reduce memory injection in many settings, but provides limited protection once the persistent memory has been poisoned.

---


### 6. [Confuse the Model, Control the Flow: Understanding and Mitigating Privacy Leakage from LLM Agents with Information Flow Control](https://arxiv.org/abs/2609.14003)

**<font color=#1a73e8>作者：</font>** Minsun Shim, Ramisha Raida Karim, Ruthwik Jakkula 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Personal AI agents built on large language models (LLMs) are increasingly given access to a user's private data and communications in order to provide personalized assistance. This access creates a persistent privacy risk: the agent must decide whether a given sensitive information should be disclosed to a particular party. Existing defenses address this by making the agent's backend LLM more privacy-preserving through stronger system prompts, training, or explicit consent-checking procedures, but this approach has a structural challenge: whenever enforcement is a judgment the LLM makes over the same conversational context an adversary controls, the enforcement mechanism and the attack surface coincide. We demonstrate this against existing defenses with three new attacks that require only ordinary agent interaction and no prompt injection: Collaborative Workspace Lure reframes an extraction attempt as collaborative work; Semantic Obfuscation Attack induces disclosure through omission rather than through anything the agent writes; and Channel Decoupling Attack splits the extraction request and the disclosure across independent channels. All three achieve substantially higher leak rates than the attacks these defenses were originally designed to withstand. Guided by this observation, we present FLOWSEAL, a defense that enforces confidentiality through a tool-level interceptor outside the LLM's context, grounded in data provenance and an information-flow-control lattice with controlled declassification. Evaluated across three benchmarks, five prompt-based baselines, and eight attacks, including a real agent executing live tool calls through MCP, FLOWSEAL reduces leak rates to near zero (e.g., 52.2% to 0.5% against Collaborative Workspace Lure) while preserving task utility, regardless of the underlying LLM backend.

---


### 7. [AGENTQ: Quantization-Conditioned Backdoor Attacks on LLM Agents](https://arxiv.org/abs/2609.14060)

**<font color=#1a73e8>作者：</font>** Xiaoqun Liu, Qiben Yan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Quantization is one of the default deployment paths for open-weight LLM agents, but it is not behavior-preserving: an adversary can release a full-precision checkpoint that passes audits yet misbehaves once quantized, termed as quantization-conditioned attack (QCA). Prior QCA work targets free-text generation, where harm is mediated by a human reader. In contrast, the agentic setting poses a more severe risk: the triggered payload is a structured function that can be executed without human oversight. We present the first study of QCA against LLM agents. We find that directly adapting prior backdoor-injection methods can produce malicious behavior after quantization, but substantially degrades benign utility, rendering the resulting attacks impractical. To understand the true upper bound of the threat, we propose AGENTQ, an attack framework that combines layer-banded LoRA injection with partial-PGD repair over a multi-codebook quantization-equivalence class. AGENTQ preserves normal agentic capability while concentrating malicious behavior in the quantized model. Across three trigger-action pairs and three codebooks (NF4, FP4, INT8), AGENTQ reaches up to 100% post-quantization attack success rate with minimal loss of benign utility, underscoring the need to make quantization-aware safety evaluation a standard requirement before open-weight agents are deployed.

---


### 8. [SkillSecurer: Detecting and Patching Prompt-Injection Vulnerabilities in AI Agent Skills](https://arxiv.org/abs/2609.14079)

**<font color=#1a73e8>作者：</font>** Donato Mecca, Alberto Verna, Youness Bouchari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills extend AI agents with reusable instructions, scripts, and configuration, but are also open to new attacks to influence an agent's decisions and actions. To address these risks, we present SkillSecurer, a fully agentic framework for generating, detecting, localising, and remediating security risks in agent skills. Its red agent generates context-compatible injections across nine threat types while recording the exact modification; its blue agent analyses complete skill packages, produces grounded evidence, and proposes patches. For controlled instances, a verifier compares findings and patches with the recorded injection, enabling injection-level evaluation.
We thoroughly evaluate SkillSecurer by selecting the best backend LLM, comparing it with competitors, and manually cross-validating each evaluation stage. With its best performing backend, SkillSecurer is the only scanner to achieve a 100% injection detection rate. Next, we analyse popular skills from this http URL, finding latent vulnerabilities in more than 17% of the skills examined. Testing some of those skills, we trigger actual incidents, showing the risks of running unverified skills. Our results show that context-aware LLM analysis can provide reliable injection localisation and actionable remediation beyond skill-level flagging alone.

---


### 9. [DenMark: Robust Semantic Watermarking for Diffusion Language Models](https://arxiv.org/abs/2609.14257)

**<font color=#1a73e8>作者：</font>** Tianhao Ma, Weihao Xuan, Dong-Dong Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Semantic text watermarks encode signals in meaning rather than surface token choices, offering robustness to paraphrasing and other semantic-preserving edits. Existing semantic watermarking methods are primarily designed for autoregressive language models (ARLMs), where completed candidate units can be generated and scored before generation proceeds. This paradigm does not naturally extend to diffusion language models (DLMs), where semantic units remain incomplete during intermediate denoising steps and tokens may be updated in flexible orders. We propose DenMark, a semantic watermarking framework that injects key-dependent signals directly into the DLM denoising process. DenMark partitions the output into fixed token regions and uses temporary rollouts as semantic lookahead: conditional completions estimate the eventual semantics of an incomplete region, enabling DenMark to select local updates with higher estimated semantic watermark scores. Repeating this procedure across denoising steps progressively accumulates watermark evidence in the final output. For detection, DenMark uses calibrated scanning over candidate unit sizes to remain robust to boundary shifts introduced by semantic attacks. Across four DLMs, three datasets, and four semantic attacks, DenMark achieves the best results across all reported detection metrics in all 48 backbone-dataset-attack combinations. These results demonstrate that DenMark provides an effective mechanism for robust semantic watermarking in DLMs.

---


### 10. [CIG-MIA: Context-Induced Information Gain Membership Inference Attacks against Retrieval-Augmented Generation](https://arxiv.org/abs/2609.14649)

**<font color=#1a73e8>作者：</font>** Tan Xue, Huo Chang, Wang Changhui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) systems ground large language models on external knowledge bases, enabling access to private, domain-specific, and up-to-date knowledge without retraining. However, the same retrieval interface can expose whether a candidate document is contained in the knowledge base. This paper studies knowledge base membership inference against RAG systems under both gray-box and text-only black-box access. Existing RAG membership inference attacks rely on signals such as direct membership prompts, response similarity, mask recovery, or query perturbation, which can be sensitive to prompt defenses, semantically related retrieved documents, and the generator's parametric knowledge. We introduce CIG-MIA, a membership inference attack based on context-induced information gain. The key insight is that explicit candidate-document injection affects members and non-members differently: if a document is already available through retrieval, injection provides little additional support for document-derived answers; if it is absent, injection introduces new evidence and yields a larger likelihood gain. In the gray-box setting, CIG-MIA computes this gain directly from token-level likelihoods. In the black-box setting, it estimates the same gain from generated text by scoring selected answer tokens with a lightweight surrogate-based estimator using semantic similarity and exact-match features. We evaluate CIG-MIA on Natural Questions, MS-MARCO, and HealthCareMagic against recent RAG membership inference baselines. On Natural Questions, CIG-MIA achieves an AUC of 0.99 in the gray-box setting and 0.93 in the black-box setting. We further analyze the information-gain signal, RAG configuration effects, ablations, and robustness to paraphrasing and generation randomness.

---


### 11. [ViTeGate: Visual-Textual Triggered Knowledge Poisoning for Vision-Language Retrieval-Augmented Generation](https://arxiv.org/abs/2609.14685)

**<font color=#1a73e8>作者：</font>** Xue Tan, Xuandi Zeng, Yu Shao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern Vision-Language Retrieval-Augmented Generation (VLRAG) systems augment Large Vision-Language Models (LVLMs) with retrieved visual and textual evidence, enabling responses grounded in external knowledge. However, the retrieval pipeline also creates an attack surface: adversaries can inject poisoned image-text pairs into the knowledge corpus to influence model outputs. Existing knowledge poisoning attacks are typically always-on, allowing poisoned evidence to affect generation whenever it is retrieved. This lack of precise activation control makes it difficult to confine malicious behavior to intended inputs, reducing both attack stealth and effectiveness. In this paper, we propose ViTeGate, a visual-textual triggered knowledge poisoning attack for VLRAG systems. ViTeGate uses a visual trigger to conditionally promote poisoned evidence into retrieval results and a textual trigger to induce an attacker-specified response from the retrieved evidence. By coordinating retrieval and generation, ViTeGate reduces poison exposure when the visual trigger is absent and preserves normal responses when the textual trigger is absent. The two-trigger design enables selective attack activation and reduces unintended single-trigger activation. Experiments across multiple query datasets, retrievers, and LVLMs validate the effectiveness of ViTeGate. On InfoSeek, ViTeGate achieves an attack success rate of up to 0.98 while maintaining a clean answer accuracy of up to 0.93.

---


### 12. [Detecting and Localizing Segment-Level Poisoning in Multi-Source LLM-Agent Inputs](https://arxiv.org/abs/2609.14723)

**<font color=#1a73e8>作者：</font>** Xue Tan, Changhui Wang, Sanrui Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern large language model (LLM) agents often construct prompts by aggregating retrieved passages, user reviews, and documents from multiple external sources. This paradigm exposes them to segment-level poisoning attacks, in which an adversary controlling only a small subset of sources injects malicious content to manipulate model outputs. Existing defenses mainly rely on textual patterns, external embeddings, or auxiliary detectors and may therefore fail against fluent, semantically plausible poisoned segments. They also provide limited support for locating the responsible segments. We observe that successful corrupted-evidence and adversarial-instruction attacks induce structured shifts in the LLM's internal activations, forming a consistent activation-space pattern that we call the poison direction. Based on this observation, we propose ActProbe, an internal-state-based framework for detecting and localizing poisoned segments in multi-source LLM inputs. ActProbe projects MLP activations onto a learned poison direction and uses a lightweight linear SVM trained on a small calibration set to detect contaminated prompts. It then applies BinRoL, which combines recursive replacement ablation, Mahalanobis-distance-based branch pruning, and MAD-based robust leaf detection to locate poisoned segments. ActProbe requires no modification to the backend LLM and reduces localization overhead from O(n) exhaustive probing to O(k log n) forward passes. Across three datasets, two attacks, and four open-weight LLMs, ActProbe achieves a 0.01 false-positive rate, a 0.05 false-negative rate, 0.94 localization recall, and a 0.90 localization F1-score. It remains effective against defense-aware adaptive attacks and can protect black-box APIs through surrogate-based poisoned-segment removal.

---


### 13. [ActGuard: Pre-execution Action Auditing against Indirect Prompt Injection in LLM Agents](https://arxiv.org/abs/2609.14987)

**<font color=#1a73e8>作者：</font>** Bingzheng Wang, Xiaoyan Gu, Wentao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents interact with external environments through tool invocation, but tool outputs can also expose them to indirect prompt injection (IPI) attacks. Existing defenses mainly rely on prompt hardening, content filtering, pre-generated plans, or permission constraints. These approaches often struggle with complex tasks or over-sanitize external content, making it difficult to balance security and utility. The key challenge is therefore to preserve execution flexibility while precisely identifying and removing the malicious content that actually induces unsafe actions. To address this challenge, we propose ActGuard, a pre-execution action auditing framework. Rather than judging whether external content is inherently suspicious, ActGuard assesses whether it causes the current action to deviate from a locally reasonable expectation. At each step, ActGuard predicts the tools likely to be used by the upcoming action and constructs a local tool prior without constraining the execution trajectory. Before execution, it compares the candidate action against this prior and performs tool-level contrastive analysis and parameter-level evidence localization to identify deviations in tool selection and action parameters. A verifier then examines the localized evidence, masks only spans confirmed as malicious, and regenerates the action from the sanitized context. This design preserves legitimate planning flexibility while minimizing information loss from indiscriminate filtering. We evaluate ActGuard on challenging benchmarks for tool-using agents. Results show that ActGuard reduces attack success rates to a level comparable to state-of-the-art defenses while maintaining task utility close to the no-attack setting, achieving a favorable security-utility trade-off. Our code is publicly available at: this https URL.

---


### 14. [Overflip: Repetition-Induced Label Flips in Guardrail Models](https://arxiv.org/abs/2609.15013)

**<font color=#1a73e8>作者：</font>** Xu He, Chih-Hsuan Lin, Hung-Mao Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Guardrail models are classifiers deployed to screen malicious prompts and responses in LLM-based services. To meet latency constraints, many lightweight guardrails adopt compact Transformer backbones (e.g., DeBERTa) that are trained with short context windows (typically 512 tokens) and rely on bucketed relative positional encodings to process longer inputs. Prior evaluations assume that a guardrail's decision is stable as the input is lengthened. We show that this assumption can fail. We identify Overflip, a repetition-induced instability where repeating a prompt causes the guardrail's prediction to flip (MAL$\to$BEN) as the sequence grows. We conduct experiments on 9 widely used lightweight guardrail models. Five exhibit MAL$\to$BEN flips on a benchmark of 100 prompts, with confidence margins shrinking steadily with repetition. Among these vulnerable models, flip rates range from 8% to 92%, with first flips occurring at roughly 2.6k--9.4k tokens. Our analysis suggests Overflip differs from traditional attention-dilution baselines, which aim to divert the model's attention away from tokens associated with malicious content, shifting it instead toward unrelated content, such as benign padding or shuffling. While Overflip preserves malicious content, it homogenizes token-level attention over repeated structure and induces a distinct, more gradual attention-dispersion trajectory than padding. Moreover, Overflip poses a greater threat to LLM services than traditional attention dilution methods. Because the bypassed prompt remains semantically intact and is still readily understood by downstream business LLMs, it can transmit malicious intent after passing the guardrail. These findings expose repetition as an attack surface for guardrail models and motivate length-robust evaluation and mitigation.

---


### 15. [PIDS-Bench: Evaluating Prompt-Injection Detectors Under Over-Defense, Obfuscation, and Distribution Shift](https://arxiv.org/abs/2609.15017)

**<font color=#1a73e8>作者：</font>** Yusuf Khalid Shire, Sang-Chul Kim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prompt-injection detectors are typically evaluated using aggregate F1 on in-distribution test data, which offers limited insight into behavior under distribution shift, particularly on the benign side of the decision boundary, where false positives impose direct operational cost yet are seldom measured. We present PIDS-Bench, a frozen multi-axis benchmark that jointly evaluates attack detection and benign false-positive behavior at fixed thresholds, spanning in-distribution inputs, hard-benign prompts that mimic injection structure without malicious intent, obfuscated attacks, and domain and structural distribution shifts. We evaluate seven detectors (learned baselines, external prompt-injection classifiers, and broad-safety comparators) alongside a rule-based lower-bound reference.
Multi-axis evaluation exposes a failure mode that aggregate F1 conceals. A detector exceeding F1 = 0.98 on the held-out split still misclassifies roughly one-third of an externally-sourced benign subset drawn from public corpora and restricted to security-adjacent content. Across a full threshold sweep and five training seeds, no internal detector reaches an operating point satisfying F1 >= 0.95 and hard-benign FPR <= 0.10 together on this stress distribution. Decomposing by provenance, we find that hard-negative augmentation nearly eliminates over-defense on curated stress inputs but leaves it substantially intact on externally-sourced prompts, a pattern we term provenance-sensitive over-defense. The asymmetry holds across both fine-tuned architectures and does not diminish as the augmentation pool grows, with the externally-sourced FPR remaining far above the 0.10 target. Whether augmentation matched to the externally-sourced distribution would close this gap is untested; threshold calibration and curated-style augmentation alone do not.

---


### 16. [Pick Your Poison: Learning to Select Poison Sets for Stronger LLM Backdoor Attacks](https://arxiv.org/abs/2609.15029)

**<font color=#1a73e8>作者：</font>** Aashiq Muhamed, Mona T. Diab, Virginia Smith 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Backdoor poisoning attacks add poisoned examples to otherwise-clean finetuning data, pairing a trigger with a target behavior that the model learns to produce when the trigger appears. Existing evaluations typically fix the number of poisoned examples and sample them at random from a candidate pool. We show that this can severely underestimate worst-case vulnerability: across three LLaMA-3-8B backdoor settings, holding the model, clean data, and poison count fixed, attack success ranges from 3% to 80% depending only on which poison set is chosen.
We formalize poison selection as oracle-budgeted set optimization and introduce SAILS (Set-level Audit-Informed Iterative Learned Selection), which learns a set scorer from a few hundred finetune-and-evaluate runs, ranks millions of candidate sets, and audits only a small shortlist. SAILS improves held-out attack success by 30 percentage points on average over the strongest influence baselines, transfers from small-scale to full-scale finetuning, and extends to code-generation, agentic, and API-only backdoors.

---


### 17. [Divide, Consult, Conquer: Capability Laundering Through Aligned LLMs](https://arxiv.org/abs/2609.15383)

**<font color=#1a73e8>作者：</font>** Mark Russinovich, Blake Bullwinkel, Giorgio Severi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Language model safety is typically evaluated one interaction at a time. We show that a weaker, unaligned model can split a harmful task into benign-looking subproblems, consult a stronger aligned model independently on each, and combine the answers locally. We call this attack capability laundering. Unlike a jailbreak, no single response is a harmful task. We measure consultation-aided uplift using tasks that a raw frontier model solves, the aligned frontier refuses, and the unassisted orchestrator fails. We evaluate GPT-5.5, Claude Opus 4.8, and Grok-4.3 as consultants to four local orchestrators on CyBench, BountyBench, and harmful CBRN requests. On CyBench, Gemma-4-31B recovers 8/14 candidates with GPT-5.5 and 7/9 with Opus, compared with 2/21 and 4/15 for Gemma-4-12B. On BountyBench, Gemma-4-31B recovers 3/9 and 2/3 candidates, while Muse-Glimmer-30B recovers none of 22 and 13. For CBRN, we measure uplift across eight steps of a hypothetical bioweapon attack chain and find that consultation raises Gemma-4-31B's mean rubric score from 62.3 to 83.1 on a 100-point rubric scale. These results expose a gap in current defenses: refusing a harmful task does not prevent frontier capabilities from being transferred and composed across many individually permitted interactions.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
