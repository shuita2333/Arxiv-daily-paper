# 🧠 大模型相关研究 | 2026年09月02日

> 本类共 **452** 篇论文：已确认 **431** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-452](./part-10.md)

---

### 251. [Arkios: An Open Bilingual English-Nepali Language Model Trained From Scratch, with a Devanagari-Aware Tokenizer](https://arxiv.org/abs/2608.30092)

**<font color=#1a73e8>作者：</font>** Sajal Regmi, Siddhartha Pudasaini, Chetan Phakami Pun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Arkios, a 1.04B-parameter dense transformer pretrained from scratch on 150B tokens of bilingual English-Nepali text, using a custom single-file C/CUDA training stack and a Devanagari-aware byte-level BPE tokenizer built for this project. On ARC-Easy and ARC-Challenge, Arkios exceeds three comparably sized open models (Pythia-1.4B, TinyLlama-1.1B, OLMo-1B) despite an order of magnitude fewer training tokens, likely aided by a match between our educational-web-text pretraining data and ARC's grade-school-science format rather than a general capability advantage. We report full evaluation results under standard protocols, including a correction to an earlier partial-sample estimate, and findings specific to evaluating small models in a low-resource language: the standard multiple-choice-letter prompt format used by common evaluation harnesses places this model at chance on Nepali reading comprehension, and simultaneously at chance on English in the same format, which would lead a naive benchmark run to conclude the model has no Nepali ability when in fact it does. Concretely, both languages score at chance in the letter-choice format (0.240 Nepali, 0.236 English, against a chance baseline of 0.250), while scoring the answer text directly reveals genuine, English-favoring comprehension (0.306 Nepali, 0.387 English). We describe a manifest-conditioned tool-use contract introduced during instruction tuning, where tool calls are permitted only when a tool manifest is declared in context and suppressed otherwise, and report where that contract holds and where it does not. We release both the base and instruction-tuned model weights under Apache-2.0. The training code and a small privately-sourced portion of the Nepali pretraining corpus are not released; everything needed to reproduce the reported numbers from the released weights is included here.

---


### 252. [A Hybrid State-Space Approach for Census-Tract Population Estimation](https://arxiv.org/abs/2608.30094)

**<font color=#1a73e8>作者：</font>** Jackson R. Ye, Alexandre V. Morozov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sequence models---the architecture family behind large language models and, increasingly, state-of-the-art image recognition---have redefined how machines learn from high-dimensional data. Yet population estimation from satellite imagery, a task that underpins infrastructure planning, public health, and disaster response, has scarcely benefited: leading systems still bind population to a uniform raster, disaggregating census counts onto grid cells through weighting surfaces built from ancillary data (e.g., in WorldPop and LandScan), which can introduce systematic spatial bias, and predicting population per grid cell with convolutional neural networks. In this approach, the administrative-unit structure in which the census was actually collected is discarded. We close this gap with MambaPop, which renders each administrative unit as a single polygon-masked satellite image and treats tract-level population estimation as a sequence-modeling problem over its image patches, pairing each tract image directly with its population label and eliminating the disaggregation step entirely. Built on the hybrid state-space--attention MambaVision backbone, MambaPop is, to our knowledge, the first method to learn population directly from an administrative unit's own image as well as the first to apply a state-space based (Mamba) hybrid architecture to the population estimation task. Across all $\sim$84{,}000 contiguous-US census tracts of the 2020 census, MambaPop attains a mean absolute error (MAE) of $1{,}141$ persons per tract, matching the strongest convolutional baseline (YOLOv11, MAE $1{,}122$).

---


### 253. [COGTRL: Training LLMs for Scientific Discovery Assistance using Cognitive Traces via Reinforcement Learning](https://arxiv.org/abs/2608.30109)

**<font color=#1a73e8>作者：</font>** Shrinidhi Kumbhar Santosh Mashetty Divij Handa Kevin Coutinho, Siddharth Sambhaji Ghule, Chitta Baral  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) trained on extensive scientific research are increasingly integrated as assistants for scientific discovery. However, most research papers omit the fine-grained cognitive process of examining constraints, failed alternatives, and iterative decisions required to achieve the desired goal. Such cognitive processes are vital for real-world scientists working toward specific goals under constraints. In this paper, we show that LLMs, when trained to produce such cognitive traces, perform better as scientific discovery assistants than when trained solely on scientific literature. We propose COGTRL, a trajectory-level reinforcement learning framework that trains LLMs to emulate cognitively grounded reasoning by jointly optimizing cognitive traces and the scientific steps produced in an interleaved manner. Across two 3B-parameter models and two scientific domains (AI and Materials Science), COGTRL improves method quality by an average of 7.85 points over comparable 3B model baselines and achieves competitive performance relative to 70B parameter models. Moreover, analysis by domain experts shows a preference for methods generated by COGTRL over the baselines.

---


### 254. [Can LLMs Take the Pulse of the Economy? A Real-Time Evaluation of LLM Nowcasts on Macroeconomic Indicators](https://arxiv.org/abs/2608.30110)

**<font color=#1a73e8>作者：</font>** Xinyue Zhao, Ruiyi Zhang, Liqin Ye 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Nowcasting headline macroeconomic indicators, i.e., estimating an indicator's value for the current reference period before its official release, is critical for monetary policy and financial markets, and central banks devote dedicated teams of expert economists to producing such estimates. Large language model (LLM) agents are a promising candidate for this task, combining broad world knowledge with real-time web search and supporting queries at higher frequency than institutional nowcasts. Evaluating their nowcasting capability is, however, challenging: headline indicators such as GDP and CPI are widely reported and likely memorized during pretraining, so any evaluation on historical releases is vulnerable to data contamination. To address this, we introduce LiveMacroEval, a live, contamination-resistant benchmark in which LLM agents produce hourly nowcasts for sixteen major U.S. macroeconomic indicators over a pre-release window closing at each official release. Nowcast quality is assessed through a LiveMacro Score against announcement-window equity returns and a LiveBetting Score from simulated Polymarket-style trading, with Federal Reserve regional-bank nowcasts, the Bloomberg ECOS professional consensus, and an auto-ARIMA baseline as comparators. Over six months with four state-of-the-art LLM agents configured with web search, aggregate nowcast accuracy is broadly comparable to the institutional and professional benchmarks, with performance varying widely across individual indicators. This highlights LLM agents' potential as real-time estimators of macroeconomic conditions.

---


### 255. [Manacá-1B: An Open, Reproducible Brazilian-Portuguese Language Model and a Tokenizer-Aware, Paired Evaluation](https://arxiv.org/abs/2608.30114)

**<font color=#1a73e8>作者：</font>** Bruno Leonardo Santos Menezes, Carlos Leonardo Souza Cardoso, Fabio Andre Machado Porto  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Brazilian Portuguese remains under-served by open language models, and the few that exist are difficult to reproduce and are often compared without measures of uncertainty. We release Manacá-1B, an open decoder-only model of 1.72 billion parameters trained from scratch for Brazilian Portuguese with a fully containerized, reproducible pipeline. The pretraining is stable, with zero skipped or NaN steps and self-recovering loss spikes, and we release its full log and dynamics. We evaluate the model against nine open baselines on four Portuguese benchmarks under a single harness. Every comparison reports a standard error and a paired significance test, and the harness is validated against previously published numbers. On last-word prediction Manacá-1B is the strongest model below the 7B scale, exceeding both Tucano-1b1 and Tucano-2b4 on LAMBADA-PT with large paired margins; it is competitive on commonsense completion and near chance on multiple-choice reasoning, as are all small base models. Along the way we document a concrete evaluation pitfall: converting a SentencePiece tokenizer with case-folding normalization to the HuggingFace fast format silently drops the normalizer, routing every capitalized token to byte-fallback and depressing scores in a way that is invisible in aggregate metrics. The uncorrected tokenizer lowered LAMBADA-PT accuracy from 45.3 to 25.0; we quantify the effect and provide a one-line fix that reproduces the training tokenizer exactly. Code, raw training and evaluation logs, per-example prediction vectors, the model weights, and the corrected tokenizer are released so that every number in this paper can be recomputed.

---


### 256. [Aligning Multi-Trajectory Supervision with Policy Optimization for VLA Driving](https://arxiv.org/abs/2608.30122)

**<font color=#1a73e8>作者：</font>** Tian Zhang, Zhuo Huang, Hongrui Ye 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) driving methods increasingly combine multi-trajectory imitation learning with group-relative policy optimization (GRPO), making trajectory selection critical to final performance. However, some high-scoring trajectories that improve imitation can degrade subsequent GRPO by inducing advantage estimates misaligned with the current policy's feasible behavior distribution, driving updates away from safe and compliant behaviors. To address this, we propose a novel framework that aligns multi-trajectory supervision with policy optimization. To address the policy gradient bias induced by infeasible noisy trajectories outside the feasible region, augmented trajectories are constrained to a neighboring manifold of the ground-truth feasible region, and a Pareto-optimality criterion is adopted in place of the conventional aggregate score, retaining only non-dominated candidates and thereby filtering out conflicting samples at the source. To ensure that expanded trajectory supervision is effectively absorbed during policy optimization, we introduce two complementary mechanisms: feasibility-first advantage assignment and dynamic distillation. The former adapts Pareto credit to the feasibility composition of each rollout group and guides fully infeasible groups toward safe references. The latter updates teacher trajectories across refinement rounds to continually transfer useful supervision. Together, they progressively translate the benefits of expanded supervision into policy improvement. On NAVSIM v1 and v2, our method achieves 91.4 PDMS and 89.1 EPDMS, respectively, under single-trajectory inference, and recovers 440 of 658 initially failed scenes, 11.1\% higher than the original GRPO baseline.

---


### 257. [Verification-Aware Training for Speculative Decoding](https://arxiv.org/abs/2608.30135)

**<font color=#1a73e8>作者：</font>** Geonmo Gu, Byeongho Heo, HeeJae Jun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model inference by using a draft model to generate candidate tokens, which are verified by the target model in a single forward pass. Verification proceeds sequentially and discards every position from the first rejection onward, yet existing draft training relies on token-level imitation of the target with a fixed per-position weighting that reflects neither property. We introduce Verification-Aware Training (VAT), a plug-in framework that simulates verification at every training step and turns the resulting accept and reject patterns into supervision. VAT consists of two components: (i) a verification head, a lightweight jointly trained binary classifier that supervises the draft model on whether each position survives sequential verification; (ii) verification-adaptive weighting, which replaces the fixed weighting schedule by keeping full weight up to each sample's first rejection point and re-anchoring the decay to start there. VAT modifies only the training objective, so it can be layered on top of existing methods without changing the draft architecture, the target model, or the inference procedure. Applied to EAGLE-3 and DFlash on Qwen3-4B, Qwen3-8B, and LLaMA-3.1-8B, VAT improves average acceptance length by up to 11.4% and wall-clock speedup by up to 8.7%, with consistent gains across math, code, and chat benchmarks. Code will be available at this https URL

---


### 258. [Balancing Privacy, Utility, and Safety in LLM Alignment through Preference Optimization](https://arxiv.org/abs/2608.30141)

**<font color=#1a73e8>作者：</font>** Dishu Yang, Jingjing Liu, Jize Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Preference optimization is widely used to align large language models with human preferences, but preference-data composition may also influence privacy-relevant memorization. We examine whether adding synthetic privacy-preference pairs to Direct Preference Optimization (DPO) is associated with lower canary-based memorization signals without modifying the objective or introducing a formal privacy mechanism. We propose Privacy-Pressure Preference Mixing (P3M), a data-composition protocol that varies the amount of privacy-preference data while keeping helpfulness and harmlessness preference data fixed. We evaluate a non-privacy Baseline and privacy-mixing ratios of 0.5, 1.0, and 2.0 using Gemma 3 270M-IT across five random seeds and validate the same four conditions using 4-bit-quantized Gemma 2 2B-IT across three seeds. Overall, under the tested conditions, privacy-preference mixing is associated with lower mean canary suffix log-likelihood proxy values across both model settings and lower aggregate membership-inference attack performance relative to the Baseline in the mixed-source 2B evaluation. Specifically, across the privacy-aware 2B configurations, the mean area under the receiver operating characteristic curve (AUROC) ranges from 0.596 to 0.629, and the mean area under the precision-recall curve (AUPRC) ranges from 0.541 to 0.575, compared with 0.804 and 0.790, respectively, for the Baseline. However, the reduction in membership distinguishability does not hold uniformly across data sources. Moreover, the relationship between the privacy ratio and harmlessness preference accuracy varies by model setting, whereas helpfulness preference accuracy remains broadly stable. These findings suggest that P3M should be viewed as a lightweight empirical protocol for examining privacy-utility-safety trade-offs rather than as a formal privacy guarantee or a defense against extraction attacks.

---


### 259. [LandmarkLens: Predicting and Presenting Effective Landmarks for Mixed-Reality Urban Exploration](https://arxiv.org/abs/2608.30142)

**<font color=#1a73e8>作者：</font>** Chu Li, Yotam Sechayk, Jared Hwang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People with a poor sense of direction (SOD) struggle to build cognitive maps for effective spatial navigation, and existing navigation tools prioritize efficiency over spatial learning. To understand how navigation strategies differ by ability, we conducted a landmark attention study with 20 participants (ten good SOD, ten poor SOD) who navigated across four Tokyo neighborhoods in virtual reality (VR). We found systematic group differences in both gaze behavior and the types of landmarks they verbally identify as effective. Based on these findings, we built LandmarkLens, a mixed-reality (MR) navigation system that uses a vision-language model (VLM) to identify and highlight navigation-relevant landmarks. A follow-up study with eight poor-SOD participants showed improved performance in scene recognition, suggesting that guided landmark attention can support landmark-level spatial knowledge acquisition for people with poor SOD, a first step toward broader spatial learning.

---


### 260. [CAST: Critique-Aware Supervision for Training Reliable Long-Horizon Tool-Calling Agents](https://arxiv.org/abs/2608.30147)

**<font color=#1a73e8>作者：</font>** Amir Saeidi, Zehua Zhang, Rishitosh Singh 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly deployed in long-horizon, interactive, and stateful environments. In these settings, a single wrong action, such as refunding the wrong purchase, can cause irreversible task failure and must be intercepted before execution. Such failures may not appear in every single run, but can emerge across repeated trials, making reliability across steps and trials critical. However, ensuring agentic reliability is challenging: even frontier LLMs struggle to explain why an action may be wrong, especially in long, intertwined trajectories governed by domain-specific policies. Much recent work relies on prompt-based critique agents, while optimization-based methods lack a systematic way to produce rich verification rationales for training. We address this gap with CAST, a critique-aware training framework that converts sparse task outcomes into action-level supervision for critique learning and policy optimization. CAST analyzes agent trajectories to synthesize structured rationales explaining action validity under partial observability. The resulting critique model is used to construct critique-aware training data for optimizing the policy model. Fine-tuning Qwen3-family models on dynamic tool-calling benchmarks, CAST improves reliability across domains, outperforming GPT-OSS-120B by over 10% pass^4 on Retail tasks and yielding an additional 9% improvement on Telehealth in an out-of-domain setting. These results demonstrate that critique-aware training improves the robustness of LLM agents in realistic dynamic environments.

---


### 261. [Reactivating Test-Time Scaling for Plane Geometry Problem Solving](https://arxiv.org/abs/2608.30156)

**<font color=#1a73e8>作者：</font>** Xiaoqiang Kang, Shengen Wu, Maizhen Ning 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Plane geometry problem (PGP) solving has become a critical benchmark for multimodal reasoning because it requires accurate visual perception and precise multi-step symbolic deduction. Although test-time scaling (TTS) has demonstrated remarkable success in general mathematical reasoning, it fails to scale effectively under the symbolic-program paradigm for plane geometry. We identify two key obstacles: limited reasoning diversity induced by rigid symbolic programs and insufficient explicit visual grounding before symbolic deduction. To address these issues, we propose Multi-Trace Synthesis (MTS), which converts each symbolic program into heterogeneous reasoning traces, including executable Python scripts and CoT-augmented variants. We further propose Perception-Augmented (PA) training, which parses diagrams into structured semantic clauses before deduction, and Consensus-Guided Multi-Trace Ensemble (CG-MTE) for efficient self-adaptive inference. Experiments on three geometry benchmarks show that our method consistently improves PGP-solving across model scales and achieves strong performance against both general-purpose MLLMs and specialized geometry solvers. Under test-time scaling, CG-MTE achieves comparable accuracy to high-budget self-consistency while reducing sampling cost by up to 8x. Code and data are publicly available at this https URL.

---


### 262. [CPR for LLMs: Critical-Point Routing against Catastrophic Forgetting in Domain Adaptation](https://arxiv.org/abs/2608.30158)

**<font color=#1a73e8>作者：</font>** Kwangmin Ki, Yunhun Nam, Jongheon Jeong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) is the de facto standard for adapting large language models (LLMs) to target domains, but it often degrades the model's general capabilities, a phenomenon known as catastrophic forgetting. Existing approaches typically modify the SFT loss to mitigate forgetting, but they inevitably operate along a domain-generality trade-off. In this work, we step outside this trade-off by decoupling the two capabilities at the model level: we keep the original base model for general capability, and selectively invoke the SFT expert only when domain-specific knowledge is required. Specifically, we propose CPR (Critical-Point Routing), a token-level routing framework between a base model and its expert derivative, based on critical tokens where the base model fails but the expert succeeds. We train a lightweight hierarchical router that estimates the expert-call probability per token, and pair it with a tailored inference procedure that combines momentum smoothing and threshold gating. Across diverse model-domain configurations, CPR achieves state-of-the-art across all settings, surpassing SFT expert by 1.4-5.5% in domain performance while recovering its general-capability drop from 3.4-14.5% to at most 0.5%, with minimal overhead from invoking the expert on only one-third of tokens.

---


### 263. [Understanding Stage-Wise Utility-Risk Trade-offs in LLM Agent Memory](https://arxiv.org/abs/2608.30177)

**<font color=#1a73e8>作者：</font>** Chuanchao Zang, Zijian Cao, Xiangtao Meng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Long-term memory is becoming a core capability of LLM agents, enabling personalization and long-horizon interaction. However, memory mechanisms that retain, transform, or expose more information can affect both benign utility and susceptibility to memory poisoning. Existing evaluations typically measure memory utility or attack risk in isolation under fixed configurations, providing limited insight into how stage-specific design choices reshape their trade-off. We present \textsc{MemGauge}, a controllable framework that separately varies writing admission, management policy, and retrieval exposure under matched clean and poisoned conditions. Across 11 LLMs and two long-term memory benchmarks, controlled evaluations reveal three distinct profiles: a threshold-like risk transition during writing, policy-dependent local decoupling during management, and coupled growth of utility and risk during retrieval. We further apply analogous stage-level measurements to four existing memory systems and observe diagnostic associations qualitatively consistent with these profiles. These results show that targeted poisoning risk varies across memory operations and motivate stage-aware evaluation and control of LLM-agent memory.

---


### 264. [A.X K2 Technical Report](https://arxiv.org/abs/2608.30181)

**<font color=#1a73e8>作者：</font>** Cheolseung Baek, Dhammiko Arya, Eunki Kim 等 43 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce A.X K2, a 688B-parameter Mixture-of-Experts (MoE) language model trained from scratch as a high-performance foundation for \emph{agentic} applications. Trained on approximately 8.5T tokens---fewer than its predecessor, A.X K1---on a smaller but higher-quality mixture with substantially expanded agentic and software-engineering data, it nonetheless improves over A.X K1 across the board, by over 30 percentage points on some benchmarks, reflecting large gains in token efficiency. To support long contexts efficiently, we introduce Sparse Gated Attention (SGA), which combines sparse attention with gated attention, and adopt Gated Norm (GN) to stabilize large-scale training. SGA is trained natively at 128K through a \emph{sparse} indexer warmup that optimizes the indexer against its own sparse top-$k$ selection rather than the dense attention distribution, making adaptation markedly cheaper: each query reads only 2,048 positions, yet long-context quality is unchanged and A.X K2 scores 94.6 on RULER out to 256K. The outlier suppression of GN in turn keeps 4-bit NVFP4 serving within one point of FP8 accuracy. A simple yet effective Think-Fusion recipe further lets users switch between thinking and non-thinking modes within a single unified model. Extensive evaluations show that A.X K2 performs competitively against strong open-weight baselines, matching or exceeding them on math and Korean-language benchmarks.

---


### 265. [GPAgentBench-2K: Benchmarking Large Language Model Agents in Complex Clinical Action Space](https://arxiv.org/abs/2608.30188)

**<font color=#1a73e8>作者：</font>** Boqi Chen, Xudong Liu, Yunke Ao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) show great potential as clinical agents, yet existing benchmarks reduce clinical workflows to static predictions or unconstrained Markov Decision Processes (MDPs) with coarse action sets. To address this, we introduce GPAgentBench-2K, the first Constrained MDP (CMDP) LLM-agent benchmark for primary-care clinical decision-making, constructed from expert-validated records of real-world GP encounters. Our environment models a full spectrum of six foundational clinical actions, imposes a topological workflow prior over the action space, and operationalizes safety-informed abstention as a first-class outcome. Evaluating 16 state-of-the-art LLMs reveals a significant performance degradation as the action space scales. Crucially, we uncover a clinical quality-safety gap: even frontier models with the highest diagnosis accuracy violate safety constraints in over half of high-risk cases. Finally, we establish a reference point using Constrained Group Relative Policy Optimization (C-GRPO), and show that while explicitly modeling constraints improves performance over unconstrained RL methods, it remains far from clinically acceptable safety.

---


### 266. [FaVOR: LLM-Based Agentic Framework for Factor Mining via Empirical Validation](https://arxiv.org/abs/2608.30192)

**<font color=#1a73e8>作者：</font>** Hyeonjin Kim, Minseok Kim, Seunghyeon Jung 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional finance relies on experts to hand-craft factors through a principled process grounded in economic rationale. Recent LLM-based multi-agent systems have automated this process, scaling factor mining far beyond manual effort. However, these automated approaches optimize directly for returns and rarely check whether a generated factor still expresses the economic hypothesis that motivated it. We identify this inconsistency between mathematical form and economic meaning as a structural failure mode of return-oriented automation. The resulting factors blur the line between real signals and spurious correlations and break down across regime shifts. We propose FaVOR (Factor Validation through Observable Reasoning), an agentic framework that restructures factor mining around hypothesis-level evidence rather than return outcomes. In place of the standard hypothesis-to-formula leap, FaVOR enforces a three-stage consistency loop tying mathematical form to economic rationale throughout. (1) Decomposition splits a broad economic hypothesis into independent observable conditions. (2) Validation checks whether each factor reflects its intended condition. (3) Integration merges them into a composite whose structure remains interpretable. On the CSI 500 and S&P 500 in 2025, FaVOR outperforms existing baselines while remaining effective across regimes. FaVOR shows that hypothesis-grounded factor discovery produces signals that are interpretable by construction, regime-robust, and economically faithful. The code is available at this https URL.

---


### 267. [ALTSTEER: Selective Safety Steering for Moving Beyond Hard Refusals to Constructive Alternatives](https://arxiv.org/abs/2608.30197)

**<font color=#1a73e8>作者：</font>** Hoejoon Kwon, Byeonggeuk Lim, Kahyeon Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety alignment is essential for deploying large language models, requiring systems to prevent harmful compliance while preserving helpfulness on benign requests. Activation steering offers a training-free inference-time approach to safety control, but effective safety steering requires addressing two coupled questions: when to intervene and how generation should be shaped after intervention. However, existing safety steering methods remain limited along both dimensions, as their triggering mechanisms can be unstable across domains and refusal-oriented steering often yields rigid refusals rather than constructive safe guidance. To address these limitations, we propose ALTSTEER, an inference-time framework that couples selective intervention with refusal-anchored constructive redirection within a single inference pass. ALTSTEER uses an internal refusal-relevant signal to decide when to steer, and applies staged steering to shift generation from refusal-oriented control toward constructive alternatives. Evaluations on Llama-3.1 and Qwen2.5 show that ALTSTEER preserves benign utility while improving constructive safe-completion behavior, especially on models that otherwise tend to produce short refusals for harmful requests.

---


### 268. [When Errors Become Memories: Causal Pathway Tracing in Multi-Turn Memory-Augmented LLMs](https://arxiv.org/abs/2608.30198)

**<font color=#1a73e8>作者：</font>** Shuyao Xiao, Shengling Wang, Xuan Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory enables large language models (LLMs) to preserve and reuse information across interactions, but it can also turn localized errors into persistent risks. Existing work mainly evaluates whether memory systems store and retrieve information correctly, leaving limited understanding of how errors propagate across responses, memory states, and future interactions. We propose a structural causal model (SCM)-based framework for cross-turn error propagation in memory-augmented LLMs. We model user questions, model responses, and memory states as a dynamic causal process, and identify two entry pathways: internal memory updating and external question feedback. By intervening on these pathways, we construct four counterfactual trajectories and quantify their downstream effects and interaction. Error influence is evaluated at four levels: memory retention, natural responses, targeted diagnostic probing, and probability-level error preference. Experiments show that error influence generally decays with interaction distance, while the memory-update pathway contributes more persistent effects than question feedback; latent errors may remain even after disappearing from natural responses. Propagation patterns also vary across memory categories and memory mechanisms. Pathway-guided restoration further validates this decomposition: Question Repair reduces residual error by 27.5%, Memory Repair by 70.2%, and Joint Repair by 98.3%, nearly eliminating residual propagation.

---


### 269. [When Models Hear What They Expect: Diagnosing Prosodic Heuristics in Multimodal Sarcasm Detection](https://arxiv.org/abs/2608.30204)

**<font color=#1a73e8>作者：</font>** Yongjian Chen, Pengfei Wei, Yiqun Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) process speech and text jointly, yet whether they exploit prosodic cues for pragmatic inference or rely on surface acoustic patterns has received little systematic investigation. We address this through sarcasm detection, evaluating Qwen2.5-Omni and Qwen3-Omni on Mandarin Chinese and English under five modality conditions that decompose the contributions of lexical content, vocal semantics, and prosodic structure. Adding audio systematically inflates false positives without improving true positive detection. Acoustic error diagnosis reveals that model errors cluster on a shared stereotype of expressive prosody, namely elevated pitch and irregular pausing, that diverges from the actual cues marking sarcasm in both languages. Targeted manipulation of only these two dimensions causally confirms the heuristic, inducing false positive rates of up to 60%. Applying the same manipulation template to Gemini~3 Flash Preview without modification replicates the effect, suggesting that the stereotype extends beyond the Qwen Omni family rather than arising from a single model architecture.

---


### 270. [DICS: Exploring Data Intrinsic Consistency for Visual Instruction Selection](https://arxiv.org/abs/2608.30209)

**<font color=#1a73e8>作者：</font>** Yuyang Hong, Jinhui Guo, Jiaqi Gu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual instruction tuning is crucial for advancing the vision-language alignment and instruction-following capabilities of Vision-Language Models (VLMs). However, identifying optimal subsets under a fixed ratio constraint from rapidly expanding datasets remains a significant bottleneck. While existing methods largely depend on distribution diversity or heuristic filtering, they often overlook the internal coherence within individual samples. To bridge this gap, we propose Data Intrinsic Consistency (DIC), a self-scoring metric designed to quantify the sample-level inter-component consistency. DIC consists of two modules: Visual Information Consistency (VIC), evaluating the alignment between visual content and instructions, and Response Information Consistency (RIC), assessing response coherence relative to the instruction. Building upon DIC, we introduce Data Intrinsic Consistency Selection (DICS), an adaptive data selection method that optimizes the trade-off between high intra-sample consistency and global distributional diversity under varying data budgets. Extensive experiments demonstrate that DICS consistently outperforms state-of-the-art methods across diverse dataset scales and model architectures, surpassing full-dataset fine-tuning while using only 25% of the LLaVA-1.5-665K data. We further curate DICS-6M, a 6M-sample multi-modal instruction corpus that enables the largest-scale visual instruction selection study to date; remarkably, DICS reaches 94.52\% of the official InternVL3-8B-Instruct performance using less than 25\% of its reported training data. Code can be seen at this https URL

---


### 271. [Frontier vision-language models have overtaken young adults at detecting AI-generated portraits -- but not their calibration](https://arxiv.org/abs/2608.30210)

**<font color=#1a73e8>作者：</font>** Sunwhi Kim, Sunyul Kim, Meounggun Jo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI image generators now create face portraits that are hard to tell from real photographs. Vision-language models (VLMs) are increasingly proposed to flag such images. We benchmarked 19 VLMs on the same 198 face portraits -- real photographs and identity-matched ChatGPT-4o and Imagen 3 versions -- under the same task as our earlier study of 1,667 adults (85% correct overall; accuracy fell steeply with age). The June-2026 cohort of 14 models only matched adults in their 20s-30s. Four weeks later the ceiling broke. Among five July-2026 releases under the identical protocol, gpt-5.6-sol reached 92.8% balanced accuracy (five-draw mean 92.1%), clearly above adults in their 20s (88.5%), and claude-fable-5 detected every AI image while averaging 91.9%. Model sensitivity now exceeds young adults decisively (d' up to 3.4 versus ~ 2.4). What has not been overtaken is human calibration. Model criteria spread from c = -1.10 to +1.45 while humans sit near zero at every age; both new leaders are biased (+0.44, -0.97), and only a few mid-ranked models approach the human balance. Changing the labelled examples still flipped about one answer in four. The best machines now out-see young adults here, without matching the human balance between suspicion and trust.

---


### 272. [Towards a Joint Khmer Text Recognition and Word Segmentation](https://arxiv.org/abs/2608.30213)

**<font color=#1a73e8>作者：</font>** Marry Kong, Rina Buoy, Sovisal Chenda 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text recognition, or extracting electronic text from document images, has been indispensable for knowledge retrieval tasks, such as retrieval-augmented generation (RAG). For Khmer, extracted text is subject to an extra word segmentation step, as Khmer does not use any visible word delimiters to denote word boundaries. Thus, a recognition-then-segmentation pipeline for Khmer requires two separate sequential models; this is not only error-prone but also adds significant latency for large-scale document processing. This paper proposes a novel joint Khmer text recognition and word segmentation framework in a unified model. The proposed model, using a connectionist-temporal-classification (CTC) decoder for fast, parallel decoding, can be instructed to recognize Khmer text with ($b=1$) and without ($b=0$) word segmentation. Experimental results on different benchmark datasets of different document modalities (document, scene, and handwritten images) show that the proposed model can not only recognize characters in document images but also locate word boundaries, removing the need for an extra word segmentation step in a conventional sequential pipeline.

---


### 273. [The Differential Reasoning Router: Operationalizing Cost-Aware LLM Annotation in E-commerce](https://arxiv.org/abs/2608.30224)

**<font color=#1a73e8>作者：</font>** Cheng Lyu, Jingyue Zhang, Vinny DeGenova 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used to annotate structured product data in e-commerce, but early deployment often begins as a cold-start problem: only limited pre-launch labels are available, the value of expensive reasoning is unknown, and human review is needed before the system can be trusted at scale. This challenge is especially common in rule-based annotation workflows, where each item must satisfy multiple business rules and both model errors and ambiguous rule boundaries affect final decisions. We introduce the Differential Reasoning Router (DRR), a cost-aware framework for cold-start LLM annotation that jointly optimizes model selection and human escalation. Rather than treating a reasoning model as a default fallback, DRR estimates separate success probabilities for a direct model and a reasoning model at both the sample and business-rule levels, enabling adaptive routing: easy cases are handled directly, reasoning is reserved for cases where it is expected to improve the decision, and likely double-failure or rule-disagreement cases are escalated to human annotators. The resulting labels provide targeted ground truth for prompt engineering, supervised fine-tuning, calibration, and rule refinement, enabling a gradual shift from human-heavy cold-start annotation toward high-confidence automated routing. In a production e-commerce workflow, DRR reaches accuracy parity with the strongest confidence-based router while achieving more than 60\% reasoning-token cost savings.

---


### 274. [LaMoC: Loss-Aware Modular Compression for LLMs](https://arxiv.org/abs/2608.30226)

**<font color=#1a73e8>作者：</font>** Mohanad Odema, Jacob Song  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modular compression has enabled considerable parameter reduction in LLMs while preserving strong language understanding and downstream task accuracy. However, existing joint modular compression methods primarily rely on activation statistics, leaving loss-sensitivity information and its module-level characterization underexplored. We investigate addressing this gap with LaMoC, a loss-aware modular compression methodology that blends activation and Empirical Fisher statistics through gradient-error alignment. LaMoC improves joint compression by selecting compression statistics that better align local module reconstruction error with the downstream loss. Our contributions are three-fold: (1) We characterize the Empirical Fisher as a module-level loss-aware proxy that can be blended with the activation statistics required for compression. (2) We reformulate joint modular compression as a two-tiered optimization problem that minimizes module reconstruction error while tuning the activation and gradient information blending rate. (3) We implement an empirically driven methodology with statistical validation to solve the resulting compression problem. We evaluate LaMoC across four model families spanning eight models. On the 4-8B models, LaMoC achieves an average 2.5% reduction in perplexity and a 1% relative improvement in task accuracy over state-of-the-art modular compression methods.

---


### 275. [Quantifying and Mitigating Korean Jamo-Level Typographical Vulnerabilities in Large Language Models](https://arxiv.org/abs/2608.30229)

**<font color=#1a73e8>作者：</font>** Seojin Lee, Hwanhee Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Korean introduces an additional typographical perturbation level not captured by ordinary character-level edit models: because syllable blocks are internally composed of sub-character units called jamo, keyboard-level errors can occur within a syllable, either producing a valid but semantically altered character or exposing raw jamo on the surface. Both outcomes disrupt sub-word tokenization and are not reliably corrected by existing grammatical error correction pipelines, leaving LLMs directly exposed to corrupted inputs. To quantify this vulnerability, we apply five jamo-level perturbation types to the KMMLU benchmark and evaluate four language models, finding that accuracy declines monotonically with perturbation intensity and that parameter scaling does not confer robustness against intra-syllabic noise. We further show that typo-corrupted inputs induce a distinct shift in internal representations that is not reducible to ordinary answer incorrectness, and that a simple linear probe trained on these representations detects unseen perturbation types with high AUROC. Motivated by this signal, we propose Typo-Aware Chain-of-Thought (TACoT), which routes inputs to chain-of-thought inference only when the probe detects a likely typo, recovering a substantial portion of the CoT accuracy gain at a fraction of the inference cost.

---


### 276. [LLM-Based Knowledge Graph Completion Combining Discrete Structural Coding with Similar Entity Information](https://arxiv.org/abs/2608.30235)

**<font color=#1a73e8>作者：</font>** Jiaqi Wang, Dongying Lin, Yang Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge graph completion requires models to use both textual descriptions and relational structure. Existing LLM-based methods either encode KG structure as discrete tokens or refine a restricted set of candidate entities, and these two directions have largely been studied separately. We propose CoSC for LLM-based KGC, which combines discrete structural coding with similar entity information. Specifically, an LLM generates an initial candidate entity ranking from discrete structural codes, after which information from entities with structures similar to that of the query entity refines the ranking. Experiments on FB15k-237 show that CoSC outperforms existing baselines on MRR and Hits@10 while remaining competitive on Hits@1.

---


### 277. [Generating Workflow DAGs from Natural Language with Non-Reasoning LLMs](https://arxiv.org/abs/2608.30250)

**<font color=#1a73e8>作者：</font>** Anand Iyer, Bhanu Khetharpal, Srinivas Upadhya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper addresses the problem of translating natural-language routing rules written by business administrators into executable workflow graphs for enterprise contact centers. Each target is a directed acyclic graph (DAG) of conditional actions with parallel branches, hit-first fallback chains, and per-branch Boolean predicates, encoded in the JSON dialect of a commercial routing platform. We show that neuro-symbolic decomposition enables lower-cost, non-reasoning large language models to generate complex workflow DAGs at production-relevant quality without expensive extended-reasoning models. Our central diagnostic is an emission-density bottleneck: on a 635-rule benchmark of manufactured synthetic data, models select the correct graph nodes with high accuracy but increasingly misconfigure attributes and Boolean grouping as the number of interdependent nodes emitted in one pass grows. We therefore move combinatorial graph construction from the model into a deterministic compiler driven by a compact intermediate representation, with a learned registry-selection front end that focuses generation on relevant vocabulary. Across four models, the full system reaches approximately 89% LLM-judge validity, approximately 90% exact-match condition accuracy, and 99-100% valid JSON while using roughly half the per-rule prompt tokens of a monolithic prompt. On GPT-5.3-chat, the method improves judge validity by 24 percentage points and achieves statistical equivalence to a reasoning model's out-of-the-box quality, although an approximately 8-point frontier gap remains. We also present a deployment path and transferable lessons for structured-generation applications.

---


### 278. [Strong Drafts Need Compact Memories: Long-Context Speculative Decoding with Compressed KV Cache](https://arxiv.org/abs/2608.30252)

**<font color=#1a73e8>作者：</font>** Tong Yuan, Chengxi Liao, Zeyi Wen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context LLM applications such as document summarization and multi-turn agents require generation from prefixes spanning tens of thousands of tokens, making decoding latency a major bottleneck. Speculative decoding (SD) reduces latency without changing model outputs, but its speedup depends on both accepted draft tokens and draft-step latency: Lightweight drafts are fast but lack the capacity to capture long-range dependencies, whereas strong independent drafts recover acceptance but incur growing KV-access cost at long prefixes. We introduce memory-augmented drafting for long-context SD, equipping a strong independent draft with compressed draft-side KV memory: A lightweight adaptor constructs and incrementally updates this memory to retain distant information and exact recent context. The target verifier retains its full KV cache and applies the standard accept/reject rule, preserving SD's lossless guarantee. Experiments on Llama~3.1-8B and 70B targets at prefix lengths up to 32K show that our method reduces draft-side memory by over 70%. It achieves speedups of up to 2.08x and 3.33x , respectively, over autoregressive decoding.

---


### 279. [Beyond Surface Forms: Symbolic Edits as a Test for Logical Reasoning with LLMs](https://arxiv.org/abs/2608.30256)

**<font color=#1a73e8>作者：</font>** Ramya Keerthy Thatikonda, Wray Buntine, Ehsan Shareghi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Logical reasoning with large language models (LLMs) is a critical capability, as it reflects a system's ability to correctly deduce hypotheses from a given context using faithful deductive processes. However, LLM reasoning has often been shown to be sensitive to small surface-level variations in problem formulation, raising questions about whether models truly follow the underlying logical structure. Studying this behavior is challenging because the symbolic components of logical problems, such as operators and predicates, are difficult to systematically manipulate in natural language. We introduce a tool-driven framework for generating controlled, label-preserving edits to logical reasoning problems. Our method operates on symbolic representations of first-order logic and constraint satisfaction problem tasks, enabling targeted modifications to logical operators and other structural components before translating them back into natural language. Using this framework, we evaluate various LLMs under cumulative and individual operator edits and analyze their behavior in response to these changes. Our quantitative and qualitative analyses show that LLM reasoning behavior under controlled operator edits is inconsistent, regardless of model size or family: models sometimes adapt correctly to structural changes but often fail to track their logical consequences. The results from this automated stress test enable an evaluation of language models across different dimensions and help measure the reliability of their reasoning.

---


### 280. [Stratified Consistency Distillation for Natural Language Formalization](https://arxiv.org/abs/2608.30258)

**<font color=#1a73e8>作者：</font>** Zhichao Hou, Ferhat Erata, Joe Lilien 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neurosymbolic reasoning has shown promising success in addressing complex reasoning tasks by combining large language models (LLMs) and symbolic solvers. While this approach shows promise, a fundamental challenge remains: improving the accuracy of translations from natural language to logical formulas. Current methods predominantly rely on prompt engineering, which is difficult to scale across different domains and input formats. Drawing inspiration from the success of fine-tuning in other model adaptation and alignment applications, we propose a fine-tuning-based Stratified Consistency Distillation approach: (1) We generate K logical translations per input using a frontier LLM and cluster them by semantic equivalence (2) Based on the entropy level, we apply majority voting (low entropy), LLM-as-a-Judge (medium entropy), or unification/abstention (high entropy), and (3) fine-tune a smaller model using the selected pseudo-labels. Our experiments show significant and consistent improvements in both Pass@K and our novel Equivalent Logical Similarity metrics, demonstrating the potential of advancing logical translation through consistency distillation.

---


### 281. [Using Prosody to Predict Syntactic Structure](https://arxiv.org/abs/2608.30260)

**<font color=#1a73e8>作者：</font>** Junghyun Min, Alex Warstadt, Tamar I. Regev 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While it is well-established that prosody carries crucial cues for syntactic structure, the degree and nature of correspondence between these two domains remains contested. We investigate the syntax-prosody interface through an information-theoretic lens, quantifying the interaction between prosodic features and syntactic representations as their mutual information. We provide a general-purpose framework for estimating this quantity over large speech-text corpora using multimodal language models. Our framework is structure-agnostic and modular, insofar as it can be used to measure the contributions of individual prosodic features or components of structure. We evaluate the syntax-prosody relationship for two features (word duration and inter-word pauses) across two domains--read audiobooks and spontaneous conversations--both in English. Our results demonstrate that prosody contains measurable syntactic information, with prosodic features reducing syntactic uncertainty in spontaneous conversations by up to 10.2%. Our findings offer new empirical support for several theoretical accounts of the syntax-prosody interface.

---


### 282. [Centering before Pruning: Lightweight Geometry Correction for Diversity-Based Visual Token Pruning in LVLMs](https://arxiv.org/abs/2608.30263)

**<font color=#1a73e8>作者：</font>** Shunjie Wen, Jaeyeon Lee, Dong-Wan Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) incur substantial inference costs due to their long and highly redundant visual-token sequences. Diversity-based pruning mitigates this cost by selecting token subsets based on pairwise cosine similarity. We find, however, that similarities between raw visual tokens are strongly concentrated in the positive range, limiting their ability to distinguish non-redundant tokens. A natural way to improve this resolution is to center token features before computing cosine similarity. Centering indeed reveals a substantially richer pairwise structure, yet unexpectedly degrades pruning performance when used alone. We show that this apparent contradiction arises because the raw geometry does more than represent pairwise diversity: it also implicitly favors globally distinctive tokens, which tend to contain semantically informative content. Centering better resolves subset diversity but loses this useful token-wise preference, revealing that diversity and distinctiveness are entangled in the raw geometry. Based on this analysis, we propose the \textbf{Cen}tered Geometry \textbf{Prune}r (Cen-Prune), which measures subset diversity using centered cosine similarity while retaining raw-space distinctiveness as a complementary token-wise preference. This lightweight, plug-and-play correction leaves the underlying selection mechanism unchanged and incurs negligible computational overhead. Extensive experiments across multiple image- and video-understanding benchmarks and LVLM architectures demonstrate that Cen-Prune provides robust improvements in overall performance across existing diversity-based pruners.

---


### 283. [SimCRAFT: Distilling Remote Sensing Agents via Synthetic Trajectories and Contextual Retrieval-Augmented Fine-Tuning](https://arxiv.org/abs/2608.30277)

**<font color=#1a73e8>作者：</font>** Haoran Wang, Jing Yao, Xu Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The unprecedented surge in Earth observation data volume and diversity has exposed a critical bottleneck for traditional manual workflows, catalyzing the emergence of Remote Sensing (RS) Agents. However, the practical deployment of these advanced agents is severely hindered by their heavy reliance on large-scale general-purpose LLMs, which lack deep domain expertise and impose prohibitive infrastructure demands. To resolve this, we propose SimCRAFT, a model-agnostic framework that distills sophisticated RS orchestration capabilities into a compact 7B-scale model. Addressing data scarcity, we first pair a multiagent synthesis engine with a Mock Execution Engine that checks schema correctness, inter-tool dependencies, and sensor/tool compatibility, producing SimRS-14k, a large-scale, constraint-validated workflow planning corpus. Second, we propose Contextual Retrieval-Augmented Fine-Tuning (CRAFT) that finetunes the model to reason analogically by adapting retrieved Standard Operating Procedures to novel queries under a noise-robust objective, generalizing RAFT to multi-step RS workflow planning without mechanical copying. Extensive experiments demonstrate that SimCRAFT-7B significantly outperforms openweights LLMs and rivals advanced closedsource models and specialized RS agents, while reproducing across three 7B backbones. This work contributes a competitive open-weights baseline for lightweight RS intelligence, enabling efficient autonomous deployment under resource-constrained or resource-conserving conditions.

---


### 284. [Extracting Knowledge from Tools in LLM Agents](https://arxiv.org/abs/2608.30288)

**<font color=#1a73e8>作者：</font>** Chuanchao Zang, Jianing Wang, Wenyu Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents commonly use knowledge-based tools and access their underlying files, databases, and search indexes through tool invocation. This integration improves agents' ability to provide domain-specific services but also introduces the risk of tool-mediated knowledge extraction: source content exposed to an agent for legitimate responses may be progressively recovered from its outputs, enabling reconstruction of the knowledge source behind a target tool. This paper systematically investigates this risk and identifies two challenges introduced by tool invocation: tool-selection uncertainty, where an agent may invoke a competing tool instead of the target tool, and tool-argument compression, where fine-grained query information may be lost when the agent generates tool arguments. To tackle these challenges, we propose ToolSiphon, a query-only extraction attack that introduces two complementary signals: a target-discriminative signal, implemented through Tool Contrastive Analysis, to steer queries toward the target tool; and a response-grounded factual signal, implemented through Evidence Chained Feedback, to mitigate argument compression and progressively expand extraction coverage. Across three types of knowledge-based tools and six domain-specific datasets, ToolSiphon recovers 74.3% of source records on average when coarse-grained information about non-target tools is available, with 83.2% textual recovery and 90.2% semantic similarity. Even without such information, it recovers 66.3% of source records. ToolSiphon also remains effective against representative defenses and on three real-world agent platforms.

---


### 285. [Dynamic Hub-and-Spoke Memory for Streaming Video Understanding](https://arxiv.org/abs/2608.30294)

**<font color=#1a73e8>作者：</font>** Xinru Jiang, Lin Zhao, Xi Xiao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video understanding requires answering questions at arbitrary times over a continuously growing visual stream. The central challenge is to compactly remember long-range history while effectively retrieving question-relevant evidence. We propose Dynamic Hub-and-Spoke Memory (D-HSM), a training-free framework that represents distant history as structured textual memory while preserving the recent frames as visual tokens for fine-grained perception. Specifically, D-HSM turns selected historical video chunks into typed textual observations and stores them in an entity-centered hub-and-spoke memory, with entities as hubs and related evidence as spokes. When answering a question, D-HSM dynamically retrieves a compact question-aware memory subset, expands it through hub-and-spoke links, and combines it with the recent visual window for frozen-VLM answer prediction. Extensive experiments on both streaming and long video benchmarks show that D-HSM consistently and substantially improves VLM backbones and outperforms other state-of-the-art online and offline video understanding baselines.

---


### 286. [CateKV: On Sequential Consistency for Long-Context LLM Inference Acceleration](https://arxiv.org/abs/2608.30295)

**<font color=#1a73e8>作者：</font>** Haoyun Jiang, Haolin Li, Jianwei Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated strong capabilities in handling long-context tasks, but processing such long contexts remains challenging due to the substantial memory requirements and inference latency. In this work, we discover that certain attention heads exhibit sequential consistency in their attention patterns, which can be persistently identified using a coefficient-of-variation-based algorithm. Inspired by this observation, we propose CateKV, a hybrid KV cache method that retains only critical token information for consistent heads, thereby reducing KV cache size and computational overhead, while preserving the majority of KV pairs in adaptive heads to ensure high accuracy. We show the unique characteristics of our algorithm and its extension with existing acceleration methods. Comprehensive evaluations on long-context benchmarks show that, while maintaining accuracy comparable to full attention, CateKV reduces memory usage by up to $2.72\times$ and accelerates decoding by $2.18\times$ in single-sample inputs, and boosts throughput by $3.96\times$ in batch scenarios.

---


### 287. [AIA$^{2}$: Attribute-Agnostic Imbalance Augmentation for Subgroup Robustness](https://arxiv.org/abs/2608.30297)

**<font color=#1a73e8>作者：</font>** Hanshu Rao, Guangzeng Han, Xiaolei Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Attributes describing data content and context can induce diverse imbalance patterns that go beyond label imbalance alone. However, existing studies primarily address label imbalance while overlooking data attributes, such as topics and demographics, which can induce meaningful subgroup structure while causing model degradation on underrepresented subgroups. We propose Attribute-Agnostic Imbalance Augmentation (AIA$^{2}$), a framework for improving model robustness under varying subgroup imbalances without explicit subgroup annotations. AIA$^{2}$ automatically discovers varying imbalances via latent semantic distributions, obtains slices with both learning difficulty and subgroup imbalance deficits, and deploys a large language model (LLM) for subgroup-aware imbalance augmentation. We have evaluated AIA$^{2}$ on 5 popular corpora with rich domains and their attribute values, covering social issues and diverse topics. Results show improved performance on the lowest-performing subgroups and consistent gains over competitive baselines. Ablation studies confirm complementary contributions from each component, and additional analyses show that AIA$^{2}$ provides a practical and consistent way to improve worst-group robustness under data subgroup imbalance. Code is available at this https URL.

---


### 288. [ScenePilot: Grow-and-Repair Policy for Text-Driven 3D Indoor Scene Generation](https://arxiv.org/abs/2608.30307)

**<font color=#1a73e8>作者：</font>** Jiawei Zhang, Hongsong Wang, Pan Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-driven 3D indoor scene generation has advanced from dataset-bound layout modeling to open-vocabulary synthesis with large language and vision-language models. Yet existing methods remain limited: one-pass generators often yield geometrically invalid layouts, heavy post-hoc optimization is costly and unstable, and prompt-only planners lack reusable layout priors for functional grouping and object relations. We propose \textbf{ScenePilot}, a retrieval-augmented \textbf{Grow-and-Repair} framework that formulates scene generation as prior-guided incremental growth with learned rectification. Given a prompt, the Hierarchical Retrieval-Augmented Planning (HRAP) module retrieves room-, group-, and anchor-level layout priors to support functional group planning. A text-driven base generator then inserts object groups sequentially, while the Reinforcement Multimodal Repair (RMR) module performs lightweight local correction after each insertion and a final global repair after completion. To train this policy, we construct \textbf{SceneReverse-17k}, a repair-trajectory dataset built by perturbing high-quality 3D scenes in position, rotation, and scale, then using inverse operations as executable rectification targets. The policy predicts structured \emph{move--rotate--scale} actions from rendered views, scene state, retrieved priors, and edit history. By combining HRAP with RMR, ScenePilot offers an efficient alternative to one-shot generation and heavy full-scene optimization, improving physical plausibility, functional coherence, and controllability while preserving diversity.

---


### 289. [Tail-Replay: Escaping the Curse of Linear Attention in Prefix Caching for Hybrid LLMs](https://arxiv.org/abs/2608.30310)

**<font color=#1a73e8>作者：</font>** Yirui Liu, Ruoling Qi, Xuaner Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid large language models interleave full-attention layers with linear-attention layers to reduce the cost of long-context inference. This structure complicates prefix caching: full-attention key-value caches are token-addressable, whereas linear-attention layers maintain recurrent states that cannot be rolled back to arbitrary prefix boundaries. Existing hybrid prefix caching methods address this mismatch by storing recurrent-state checkpoints. As a result, token-level matches are directly usable only at positions aligned with stored checkpoints, constraining prefix reuse to a discrete set of boundaries. We present Tail-Replay, a prefix caching mechanism that enables unconstrained token-level prefix reuse in hybrid large language models. The key insight is that linear-attention mechanisms such as Gated DeltaNet can be viewed as a structured, lossy compression of the input prefix: gated recurrent updates progressively attenuate the contributions of earlier inputs. Consequently, the recurrent state of a matched prefix can be well approximated by replaying only a short, recent suffix of that prefix. Tail-Replay exploits this property by caching the exact full-attention key-value cache while omitting recurrent-state checkpoints. On a cache hit, it reconstructs the linear-attention states by replaying a short, recent suffix of the matched prefix. As a result, the reuse boundary is determined by the shared tokens rather than by recurrent-state checkpoints. We evaluate Tail-Replay on three Gated DeltaNet-based hybrid models using the LongBench and RULER benchmarks. With only a 5--10\% replay budget, it retains 92.8--99.9\% of full-prefill quality on LongBench and RULER. For serving efficiency, we evaluate time-to-first-token speedups across multiple matched-prefix lengths---8K, 16K, and 32K. The speedup grows with prefix length, reaching $9.1$--$14.3\times$ over full prefill at 32K.

---


### 290. [Context Staircase: Signature-Aligned Dynamics of Token Embeddings under Small Initialization](https://arxiv.org/abs/2608.30315)

**<font color=#1a73e8>作者：</font>** Junjie Yao, Liangkai Hang, Zhi-Qin John Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Token embeddings are the basic representational units that connect discrete tokens with continuous computation in language models. Although modern language models learn embeddings from random initialization through gradient-based training, the dynamical mechanism by which meaningful embedding structures emerge remains unclear. In this work, we identify that the evolving embedding structures are closely related to token-conditioned label and contextual distributions, which we formalize as probability signatures. We observe a progressive learning process, which we term Context Staircase: embeddings learn the low-order statistic signatures of the data before the high-order ones. More specifically, we observe that early in training they align with the simplest, context-free signature linking a token to its label, and as training proceeds, they progressively reflect signatures involving more and more context tokens. We then analyze the gradient flow of embeddings under small initialization to explain this phenomenon, deriving embedding evolution equations for feed-forward and self-attention architectures. We further extend these observations to real language-model training. Finally, we show that these embedding structures play an important role in both task learning and the incorporation of semantic structure into the embedding space. Overall, our results provide a dynamic explanation of how data statistics and architecture jointly shape token embeddings in language models, and reveal an implicit bias in the space of data statistics: training proceeds from simpler, low-order statistical relations toward increasingly complex, context-dependent ones.

---


### 291. [Beyond Token-Level Guidance: Inference-Time Alignment of Specialized LLMs via Cross-Family Representation Steering](https://arxiv.org/abs/2608.30319)

**<font color=#1a73e8>作者：</font>** Jin Gan, Xin Li, Jun Luo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) finetuned for specialized domains represent crucial high-impact applications. Inference-time alignment improves safety degraded from specialization finetuning without requiring substantial computational resources, complementing finetuning-based methods with an easy-to-use, plug-and-play solution. However, existing inference-time methods fail to reliably improve safety without disrupting domain capability. We identify the root cause as complementary expertise orthogonality: specialized base models and general-domain guidance models have orthogonal competencies, making the guidance signal unreliable for specialized generation. This primarily manifests as stop token interference, where the guidance model's tendency toward continuation overrides the base model's decision to stop, burying correct answers under guidance-induced continuation. To address this problem, we propose CREST, an inference-time alignment method that steers base model hidden representations using safety directions extracted from a guidance model of any family, avoiding token-level structural limitations entirely. CREST improves safety where specialization has weakened it while preserving both domain-specific capability and the safety of already well-aligned models, outperforming baselines by up to 22.2\% on safety benchmarks. Our code is available at: this https URL.

---


### 292. [On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability](https://arxiv.org/abs/2608.30320)

**<font color=#1a73e8>作者：</font>** Zihan Qiu, Zekun Wang, Xiao Li 等 36 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe the architecture and ablations of Qwen3.8-Flash-Next, a sparse mixture-of-experts model with 125B parameters, 6B activated per token, and additional 51B parameters of n-gram embedding tables held off the accelerator. On fourteen pre-training benchmarks the model leads the 397B-A17B predecessor on eight and trails it on the rest by at most 2.6 points, at 1/3 the activated parameters, 1/3 the training tokens, and roughly 1/9 the training FLOPs. Token mixing uses a layer-wise hybrid of Gated DeltaNet (GDN) and global attention, with one full-attention layer in every four; at continued-pretraining time those full-attention layers are replaced by Qwen Sparse Attention (QSA), which scores context at micro-block granularity with a compressed lightweight indexer. The residual stream is widened to four branches and read through an elementwise gate, a design we call the Gated Residual (GR). Capacity is added outside the backbone by a single n-gram embedding layer whose tables are prefetched from host memory. We evaluate every candidate change along three axes: loss together with downstream benchmarks; the cost of the change in training, prefill and decode; and its effect on the optimal hyperparameters and training stability. Loss and downstream accuracy do not always move together: enlarging the n-gram vocabulary lowers loss monotonically while downstream accuracy saturates. The architecture and the Muon optimizer together shift the optimal learning rate and batch size upwards, render batch-size warmup unnecessary, and substantially improve stability under stress tests. Loss, benchmarks, efficiency and stability form one design problem. Solved jointly, they yield a recipe that is simultaneously more efficient, more capable and more stable.

---


### 293. [Ignorance or Incompetence? Constructing Knowledge-Gated, Verifiable Tasks for LLM Agents](https://arxiv.org/abs/2608.30322)

**<font color=#1a73e8>作者：</font>** Hanlin Tian, Minhao Li, Yu Mi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Professional agent tasks often depend on conventions that are absent from public corpora, yet benchmarks rarely control whether an agent has access to those conventions. We introduce a knowledge-gated task-construction protocol that separates a task instruction from a compact artefact containing private conventions, reference tables, and utility operators. Construction-time provenance, byte-identical task instructions across the provided- and withheld-artefact conditions, leak audits, and executable witnesses make dependence on the artefact explicit and testable. Across fifteen calibration tasks, one frontier agent configuration achieves a 68.0% pass rate with the artefact and 0% without it; on one task, a plausible but incorrect artefact also yields 0% across five trials. Deterministic solvers and rule corpora provide exact ground truth for structured tasks, while named criterion-level rubrics support outputs that cannot be checked by a single executable oracle. A configuration-relative calibration screen retains seven tasks satisfying our five-trial empirical knowledge-gating screen. These experiments validate the behavior of the construction protocol; they do not establish that the retained tasks improve post-training. We publicly release part of the task suite and supporting tooling at this https URL.

---


### 294. [Sequential Trajectories and Simultaneous Blending: Multi-Emotion Modeling for Instruction-Following TTS](https://arxiv.org/abs/2608.30325)

**<font color=#1a73e8>作者：</font>** Yan Zhou, Yun Hong, Yang Feng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural-language instructions enable flexible control of synthesized speech, yet emotional TTS systems primarily model a single utterance-level affect, leaving multi-emotion control underexplored. We study two complementary multi-emotion TTS tasks: emotion trajectory, which spans several ordered affective stages, and emotion blending, in which multiple emotions coexist throughout an utterance. These tasks expose a supervision mismatch: supervised fine-tuning (SFT) does not explicitly evaluate emotion features, while single-emotion rewards provide neither structure-aware feedback for trajectory completion nor pair-aware feedback for blending. We introduce HybridEmo, a post-training framework that initializes both tasks with SFT and then aligns the speech-token policy through Group Relative Policy Optimization using a sample-aware hybrid reward. For trajectory samples, segment-aligned consistency combines average and weakest-stage evidence to preserve the correctness and completeness of prescribed stages. For blending samples, a GMM-based reward combines frame-level support from the union of target-emotion anchors in an offline emotion space with an utterance-level weaker-target margin. Both branches share an ASR reward and are routed within a unified policy. On MultiEmo-Test, HybridEmo significantly improves trajectory correctness and blending intensity, without a noticeable degradation in speaker similarity. Human evaluation prefers HybridEmo to CosyVoice 3 and EmoVoice-0.5B, with nearly balanced preferences against Qwen3-TTS.

---


### 295. [Do Small Models Use the Law You Give Them? Measuring Context Use on a Bilingual Bangladesh Legal Benchmark](https://arxiv.org/abs/2608.30327)

**<font color=#1a73e8>作者：</font>** Moniruzzaman Mahadi, Abrar Mohammed Tanzim Alam, Sayma Siddika Monalisa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning can improve legal question-answering accuracy without improving how models use law supplied in context. We study this distinction in bilingual Bangladeshi legal QA, where observed errors can arise from answer scoring, retrieval, or failure to use relevant law. We construct a hierarchy-preserving statutory corpus, 2,165 reviewed bilingual fine-tuning examples, and a 150-item supplied-law control. We evaluate six instruction-tuned models: Llama-3.2-1B, Llama-3.2-3B, Qwen3.5-0.8B, Qwen3.5-2B, Qwen3.5-4B, and Gemma-4-E2B, with three LoRA seeds per model. To separate effects, we combine constrained option-letter scoring, cyclic option rotation, and controlled removal of the governing provision. On 398 Bar Council outputs, an exact-line parser attributes an accuracy gain of 50.0\% to the Qwen3.5-2B seed-42 adapter, whereas option scoring yields only $3.0\%$. For Gemma-4-E2B, the two scoring methods favor different systems. When the governing provision is guaranteed to be present, five of six reference models improve by $14.7\%-19.3\%$ under the four-order criterion. Removing that provision reduces accuracy by $8.0\%-15.3\%$ for models and by $13.8\%-14.9\%$ points for their adapters. However, difference-in differences estimates show no increase in reliance on the governing provision after fine-tuning. Results show that legal adaptation claims require separating scorer, retriever, and model effects. Our Code and data are available at this https URL

---


### 296. [Coarse composition suffices: tabular in-context learning for multi-activity antimicrobial peptide profiling](https://arxiv.org/abs/2608.30337)

**<font color=#1a73e8>作者：</font>** Raunak Kumar, Anuj Pal, Dhruvi Solanki 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Antimicrobial peptides (AMPs) often act against multiple pathogen classes, making multi-label activity prediction a more realistic screening target than binary antimicrobial classification. The ESCAPE benchmark formalizes this setting, but leading approaches typically rely on multimodal, structure-conditioned deep models that are costly to train and tune. We show that a simple, sequence-only pipeline can match and surpass these methods by combining 330 interpretable sequence descriptors with TabPFN, a tabular foundation model that performs in-context prediction in a single forward pass without gradient-based training or hyperparameter search. On ESCAPE (82,359 peptides; five labels), a label-powerset TabPFN model achieves mAP-5 = 77.8%, improving on the previously best reported 72.1%. A probabilistic classifier chain is the first method to match or exceed the best published average precision on each of the five labels simultaneously. The gains persist under the prior state-of-the-art single-fold training protocol, indicating they are not a training-set-size artefact, and are largest for remote homologues (+11.2 points below 30% sequence identity). Ablations further show that predicted structure is unnecessary at inference and that performance is not driven by any single descriptor family: ten global physicochemical scalars recover 91% of full-feature performance. Finally, explicitly modelling label dependence yields targeted benefits for scarce activities and supports ranking which activity to assay next from partial positive evidence.

---


### 297. [CapFrame: Text-Instructed Viewpoint Grounding in 3D Gaussian Scenes via Geometric Pseudo Labels](https://arxiv.org/abs/2608.30342)

**<font color=#1a73e8>作者：</font>** Jirong Li, Satoshi Ikehata, Shuhei Kurita 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) enables photorealistic real-time novel view synthesis, yet placing a virtual camera to capture a desired frame remains largely manual. Existing language-guided approaches in 3D scenes mainly focus on object-centric grounding, determining what to observe but rarely controlling how it should appear in a single frame, such as subject orientation or frame layout. To address this limitation, we introduce a new task, Text-Instructed Viewpoint Grounding (TIVG), which aims to identify a 6-DoF camera pose in a 3D Gaussian scene whose rendered frame aligns with a text instruction. To solve this task, we propose CapFrame, a partially differentiable framework that converts language into geometric pseudo labels for camera pose optimization. CapFrame follows a Retrieve-Translate-Refine pipeline: it retrieves relevant views and ranks them through a Question-Evaluation process with MLLMs, translates the instruction into orientation and layout pseudo labels, and refines the camera pose via differentiable optimization with layout and orientation losses in 3DGS. Experiments on 38 real-world scenes with 135 instructions indicate that CapFrame produces viewpoints better aligned with texts than heuristic viewpoint search and adapted trajectory generation baselines, validated by VLM metrics, MLLM judges, and user studies. Code is available at: this https URL

---


### 298. [Answer Probing-Guided Search for Diverse Solution Exploration of LLMs](https://arxiv.org/abs/2608.30345)

**<font color=#1a73e8>作者：</font>** Yi Fang, Que Shen, Chengpeng Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating multiple diverse and high-quality solutions is valuable for many applications, such as code-test generation and drug discovery. However, Large Language Models (LLMs) tend to converge on a single high-confidence solution during inference, limiting exploration of alternative valid solution paths. Existing test-time methods promote diversity through tree-like search and prune semantically similar branches using response-level semantic embeddings. However, we find that such embeddings are easily confounded by linguistic and stylistic similarities, making it difficult to distinguish genuinely distinct solution paths. To address this, we introduce Answer Probing, which probes the potential answer an LLM would reach from an intermediate reasoning path. We demonstrate that the hidden states of probed answers more effectively differentiate distinct solution paths than semantic embeddings, and the perplexity of probed answers serves as a practical proxy for reasoning correctness. Based on these findings, we propose Answer Probing-Guided Tree Search (APTS), which guides the tree search by the probed answers' hidden state similarity and perplexity. Experiments on three reasoning tasks across two LLMs show that APTS consistently enhances solution diversity, demonstrating its effectiveness and robustness.

---


### 299. [Co-Annotator: Expert-Distilled ViT and VLM for Visual and Documentation Guidance in Age-Related Macular Degeneration](https://arxiv.org/abs/2608.30352)

**<font color=#1a73e8>作者：</font>** Ziheng "Leo" Li, Benjamin Freeman, Akshay Raman 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical AI often optimizes predictive performance without engaging how clinicians decide where to look and what to write. We present Co-Annotator, which distills expert gaze and dictation into two guidance components: a gaze-aligned Vision Transformer producing fixation-aligned areas of interest (AOIs), and an ontology-bounded vision-language model (VLM) that pre-fills editable biomarker summaries for retinal optical coherence tomography (OCT). We first collect expert gaze and dictations (US1) to train the models, significantly improving diagnostic accuracy and biomarker generation. We then deploy the system with ophthalmology residents: a controlled resident study (US2) confirmed each modality is safe and independently beneficial, with AOI guidance producing lasting perceptual efficiency gains through post-guidance carryover and VLM guidance more than doubling biomarker documentation breadth. In a combined deployment across two academic institutions (US3), providing both modalities simultaneously produced efficiency gains that substantially exceeded either modality alone: correct diagnoses per minute increased by 40% and comment editing time fell by 67%, without compromising diagnostic accuracy. Notably, neither modality improved efficiency during guidance in US2, which makes the in-guidance efficiency gain under combined guidance in US3 the more striking result. Expert-distilled multimodal guidance can remove two distinct clinical workflow bottlenecks at once (visual search overhead and documentation burden) without compromising the diagnostic accuracy clinicians already achieve.

---


### 300. [Augmenting Human Performance with an XR Agent Learning from Online Behavior and BCI Evidence](https://arxiv.org/abs/2608.30369)

**<font color=#1a73e8>作者：</font>** Ziheng Li, Xichen He, Haoyan Chen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present OLIVE, a framework for adapting a foundation model to provide real-time assistance in temporally demanding, high-stakes, and dynamic tasks. We show that passive EEG, fused online with behavioral evidence, can meaningfully extend the number of targets users detect and engage beyond their unaided action bandwidth. OLIVE learns from both explicit behavioral signals (the targets the user shoots down in an XR first-person shooter game) and implicit physiological signals (fixation-locked EEG) to provide timely guidance, continuously adapting a frozen vision-language model's inference on which items are task-relevant by jointly estimating per-source reliability without manual labels or offline training. Through three user studies, including two live deployments of an assistive agent driven by OLIVE in XR, we show that OLIVE Pareto-dominates prior test-time adaptation frameworks, achieving the highest convergence rate at comparable convergence speed. Combining implicit physiological and explicit behavioral signals, the OLIVE agent produces the largest and most reliable within-session improvement to a user's ability to detect and engage targets, largely independent of the individual's skill. When the target switches silently, the agent that uses both behavioral and physiological signals reconverges significantly faster than the behavior-only agent (1.27 times faster on average, p = .008), restoring trustworthy guidance at the moment the task changes, precisely when reliable assistance matters most.

---


> [!TIP]
> 当前位于：**251-300**（第 6/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-452](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
