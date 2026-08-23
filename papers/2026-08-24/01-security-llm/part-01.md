# 🔐 大模型安全相关研究 | 2026年08月24日

> 本类共 **5** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Enforcing LLM Safety through DMD-based Classification of Prompt-Response Embedding Dynamics](https://arxiv.org/abs/2608.19579)

**<font color=#1a73e8>作者：</font>** Mohamed Akrout, Olivera Kotevska, Dan Wilson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed in high-stakes applications, yet their tendency to generate toxic, harmful, or policy-violating content poses significant risks. Detecting these unsafe outputs efficiently in a black-box manner remains an open challenge. In this paper, we extend a recently proposed dynamical systems framework designed for hallucination detection to LLM safety classification. By projecting both prompts and responses into high-dimensional embedding spaces and fitting separate Koopman-based predictive models for safe and unsafe regimes, we classify new outputs using a new differential residual score that compares prediction errors of the safe and unsafe regimes. A key contribution is the incorporation of the prompt and response embedding dynamics, yielding fitted Koopman operators that capture crucial interaction patterns. We evaluate our black-box method across three safety benchmarks using three embedding models. Our results show that incorporating prompt embeddings yields consistent improvements, particularly for interaction-dependent violations when paired with causal decoders (e.g., in Llama-3), while response-only violations benefit more from dense semantic embedding representations. These findings opens the door for using dynamical systems to analyze AI systems rather than the dominant paradigm of using AI to model dynamical systems.

---


### 2. [SafeBranch: Branch-Pair Safety Alignment for Embodied Agents](https://arxiv.org/abs/2608.19729)

**<font color=#1a73e8>作者：</font>** Hyunse Lee, Jiwoo Jeong, Haneul Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language-model-based embodied agents can complete instructed tasks but often violate safety constraints in the process, a problem recently framed as interactive safety. Training such agents to act safely is difficult, since safety and task success are distinct objectives, and safety arises only at a small number of safety-critical steps within a trajectory. Standard supervision is insufficient: imitating safe trajectories teaches behavior without explaining why it is safe, and contrasting arbitrary safe and unsafe trajectories mixes the safety signal with unrelated differences. We propose SafeBranch, a framework that aligns an embodied actor on safety through branch pairs constructed from the actor's own unsafe rollouts via environment rollback. SafeBranch rolls each unsafe rollout back to the safety-critical step that caused the violation, queries the actor for a safe alternative, and pairs the original action with the alternative so that the two branches differ only at that step. The trained actor acts safely at deployment with no critic in the loop. On IS-Bench, SafetyALFRED, and out-of-distribution variants with unseen tasks and objects, it handles safety reliably without sacrificing task success, achieving roughly ten times more safe successes than the untrained baseline on the unseen-object variant.

---


### 3. [TempJail: Temporal Jailbreak Attack against Large Vision-Language Models via Subtitle Scheduling](https://arxiv.org/abs/2608.19737)

**<font color=#1a73e8>作者：</font>** Ling Zhou, Yihao Huang, Jingling Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) have achieved remarkable progress in video understanding and reasoning. Despite extensive studies on text- and image-based jailbreaks, video jailbreaks against LVLMs remain largely unexplored. Existing video jailbreak methods mainly manipulate textual content embedded in videos, while overlooking how such information is organized over time. Our analysis reveals that jailbreak effectiveness depends not only on the semantics of textual information but also on its temporal presentation, including duration and timing-slot allocation. Motivated by this finding, we use subtitles, which are common in real-world videos and allow semantic content to be presented under precise temporal control without appearing visually intrusive, as a natural attack medium. Based on this insight, we propose TempJail, a black-box video-based jailbreak framework that constructs query-aligned dialogue-style subtitle sequences and optimizes their temporal scheduling to exploit temporal vulnerabilities in LVLMs and elicit responses that satisfy the harmful intent of the source query. Extensive experiments on four representative LVLMs and two datasets demonstrate that TempJail achieves the highest attack success rate across all evaluated model--dataset settings, outperforming the strongest baseline by 53 and 18 percentage points in dataset-averaged ASR on GPT-5 and Gemini 3.5-Flash, respectively.

---


### 4. [COPA: Continual Preference Optimization for Adaptive Prompt Injection Defense](https://arxiv.org/abs/2608.19982)

**<font color=#1a73e8>作者：</font>** Roshan Sood, Onat Gungor, Tajana Rosing  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLMs remain vulnerable to prompt injection attacks, where adversarial instructions embedded in user inputs or external content manipulate model behavior and bypass safeguards. Existing defenses are predominantly static, relying on fixed alignment objectives or attack-specific filtering mechanisms that require redesign as new attack strategies emerge. While recent lifelong alignment methods address shifting user preferences, they do not account for adaptive adversaries that continually evolve to exploit weaknesses in previously learned defenses. This limitation is particularly important in real-world deployments, where evolving attack distributions necessitate continual adaptation without sacrificing robustness to previously encountered threats. We present COPA, a continual preference optimization framework that treats prompt-injection defense as a lifelong learning problem. Instead of one-time alignment, COPA incrementally incorporates feedback from newly observed attacks via GRPO-based optimization and uses margin-weighted experience replay to retain defenses against prior attack classes. This enables continuous adaptation to emerging threats while mitigating catastrophic forgetting and preserving general-purpose model capabilities. Across lifelong prompt injection attack streams, COPA reduces attack success rate by up to 6.3x and 4.4x on average compared to state-of-the-art defenses. These results highlight continual preference optimization as an effective paradigm for defending LLMs against adaptive adversaries.

---


### 5. [Auditing Cross-Lingual Fairness in Language Model Watermarking](https://arxiv.org/abs/2608.20047)

**<font color=#1a73e8>作者：</font>** Alexander Nemecek, Osama Zafar, Debargha Ganguly 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Watermarking schemes for large language model output are evaluated almost exclusively on English text using each scheme's detection threshold and a narrow set of quality measurements. Multilingual deployment exposes evaluation-design choices that are inconsequential on English but determine conclusions cross-lingually. We propose an evaluation framework with four components: detection thresholds calibrated empirically per deployment context, a threshold-independent companion measurement that distinguishes calibration failures from detection failures, three disjoint quality measurement paradigms (distributional, paired-semantic, and reference-perplexity), and a generalized-entropy decomposition of cross-language disparity over a typological family partition. Applied to six watermarking schemes, three open-weight generators, eleven languages spanning four scripts and eight typological families, and both base and instruction-tuned regimes, the framework reveals failure modes that single-language single-paradigm evaluation cannot surface. Across detection and quality, observed disparity is predominantly between-family on the typological partition, indicating that cross-lingual fairness gaps in watermarking are structural to language properties rather than idiosyncratic to particular languages.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
