# 🧠 大模型相关研究 | 2026年09月28日

> 本类共 **228** 篇论文：已确认 **208** 篇，待复核 **20** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-228](./part-05.md)

---

### 101. [Rufus-Air: An Open LLM Post-Training Recipe](https://arxiv.org/abs/2609.29421)

**<font color=#1a73e8>作者：</font>** Chia-Yuan Chang, Renyuan Cheng, Rui Feng 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rufus-Air is an open and reproducible post-training recipe on GLM-4.5-Air-Base (106B-A12B), organized as a serial pipeline of eight stages: SFT, Reasoning RL, Coding RL, Instruction-Following RL, General Agent, Coding Agent, Search Agent, and RLHF. We document the data, reward design, infrastructure, stage order, and stagewise results needed to reproduce the recipe. Stages progress from basic to advanced capabilities and from hard, verifiable rewards to softer judge-based signals. Training builds on open-source components and public data, much of it used as released, without new human annotation or an in-house distillation teacher. Our main findings are that (i) diverse, high-quality SFT establishes a strong capability floor; (ii) difficulty filtering keeps RL prompts within a productive learning range; (iii) reward reliability provides a practical principle for ordering stages; and (iv) infrastructure and engineering choices are part of the recipe, not just an implementation detail. Rufus-Air improves over the official GLM-4.5-Air post-trained release and is competitive with similarly sized open models.

---


### 102. [agentic-ger: terminology recovery in long-form speech using global context](https://arxiv.org/abs/2609.29428)

**<font color=#1a73e8>作者：</font>** Yanqiao Zhu, Wupeng Wang, Zhifu Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in speech language models have improved automatic speech recognition (ASR) for long-form audio. However, accurately and consistently transcribing domain-specific terminology remains challenging. Motivated by the world knowledge and contextual capability of large language models (LLMs), we propose Agentic-GER, an LLM-based agent for terminology correction in long-form speech. The agent uses global context from the full transcript to identify suspicious terms and resolve ambiguous hypotheses. It selectively re-transcribes the source speech to check candidate corrections, and uses accepted edits to guide subsequent decisions. Experiments with four LLMs and two ASR systems on GigaSpeechBench show consistent terminology improvements in both Chinese and English, with and without thinking. On Chinese speech, Agentic-GER achieves up to a 36.8% relative reduction in biased character error rate (B-CER) over the Whisper baseline.

---


### 103. [Calibrating LLM Judges for Human and AI Conversations](https://arxiv.org/abs/2609.29431)

**<font color=#1a73e8>作者：</font>** Maike Züfle, Patrícia Schmidtová, Vilém Zouhar 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Measuring how successful a conversation is remains difficult, even for humans judging spoken dialogue. We evaluate state-of-the-art LLMs as pointwise and pairwise judges of conversational success on CANDOR, finding pointwise scoring correlates moderately with human ratings, while pairwise comparison suffers from long transcripts and positional bias. Since this leaves judge scores incomparable across models, we propose a small anchor set and a calibration function that calibrates any judge onto a shared, interpretable scale. We further release the Voice Arena Goal Dataset (VA), 200 task-oriented human-AI and human-agent conversations with pairwise annotations, revealing a substantial gap between current judges and human-level discrimination. Using VA, we test whether CANDOR-fitted calibration transfers to human-AI conversations, finding it brings judges onto a shared scale despite never observing VA during fitting.

---


### 104. [IterSynth: Rethinking Deep Search Agents via Role-Decoupled Iterative Synthesis](https://arxiv.org/abs/2609.29444)

**<font color=#1a73e8>作者：</font>** Xingyu Wu, Yuchen Yan, Zhengxi Lu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep search requires LLM agents to decompose complex queries, search for evidence, and synthesize grounded answers, yet existing ReAct-style agents suffer from two limitations: role coupling, where one policy must handle planning, evidence use, and synthesis; and context accumulation, where growing search histories introduce noise and obscure useful information. To address these issues, we propose IterSynth, a role-decoupled and summary-based paradigm that alternates between a Planner for identifying information needs and a Synthesizer for integrating evidence into an evolving summary state. This design separates planning from synthesis while using the summary as the persistent state of search, reducing both capability coupling and context noise. To train IterSynth effectively, we further introduce Role-Decoupled Policy Optimization (RDPO) for reinforcement learning, which combines terminal outcome rewards with turn-level rubric evaluations and computes role-specific advantages for more precise credit assignment. Experiments on five long-horizon deep-search benchmarks such as BrowseComp and Xbench-DS show that IterSynth-8B achieves an average score of 50.7, surpassing the strongest prior $\leq$8B agent by +4.2\%. Moreover, IterSynth serves as a model-agnostic prompting paradigm, delivering substantial zero-shot gains over ReAct and similar prompting paradigms on frontier proprietary models.

---


### 105. [Two Emojis of Difference: What Multilingual Affective Generation Benchmarks Actually Measure](https://arxiv.org/abs/2609.29445)

**<font color=#1a73e8>作者：</font>** Fardeen Sadab, Adib Sakhawat  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We audit a multilingual affective generation benchmark eight instruction-tuned LLMs producing emoji summaries for 17,100 Bangla, English and Hindi sentences, with 6,960 human judgements and find its headline conclusions to be artefacts of the measurement instrument rather than properties of the systems. Treating annotators as a random rather than a fixed factor, no system differs significantly from any other ($F(7,14)=0.59$, $p=0.76$), although the conventional analysis declares 19 of 28 pairwise differences significant. Annotator identity explains far more rating variance than system identity, and the winning system changes whenever any single annotator is removed. The ordering that does emerge tracks output length: mean emoji count explains 78.7\% of between-system variance, and a within-item length-matched comparison over 2,599 pairs reverses the leaderboard. We further show that cross-provider anisotropy differences vanish under mean-centring, that per-language token costs change sign with the normalising unit, and that multi-view row-wise splits inflate macro-F1 by $3.1$ points and change the top-ranked system. In place of preference scoring we propose **emoji-affect decodability**, a reference-based probe whose rankings are stable to $\pm0.003$ macro-F1 across seeds.

---


### 106. [Industrial Anomaly Detection via Defect-Grounded Reasoning in Visual Latent Space](https://arxiv.org/abs/2609.29457)

**<font color=#1a73e8>作者：</font>** Jaron Yeh, Yen-Wei Chang, Jiang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial anomaly detection (IAD) is evolving beyond conventional detection and localization toward multimodal inspection systems that can describe, explain, and reason about fine-grained defects. Although recent multimodal large language model (MLLM)-based methods improve anomaly understanding through textual reasoning and visual guidance, they face two limitations in fine-grained inspection. First, their visual refinement often requires iteratively revisiting local image regions or augmenting with additional tools. Second, the resulting local defect evidence may not be reliably preserved throughout subsequent reasoning. To address these, we propose Anomaly-LR, a defect-grounded latent reasoning framework that first forms a global understanding of the input and then progressively refines anomaly-relevant representations directly in the visual latent space. We further construct IAD-LR-22K, the first IAD instruction dataset designed for latent reasoning, containing 22,228 image-question instances from 4,523 industrial images, with global textual reasoning traces and region-level visual annotations. Extensive experiments show that Anomaly-LR achieves state-of-the-art performance among comparable-scale methods across multiple IAD benchmarks, without requiring external references or tools. The code and data will be released at this https URL.

---


### 107. [SWE-Prometheus: Measuring Engineering Governance Improvements in Real-World Repositories](https://arxiv.org/abs/2609.29465)

**<font color=#1a73e8>作者：</font>** Jiajun Wu, Leixin Sun, Zihan Tan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model based coding agents have made substantial progress on repository-level software engineering tasks. Existing repository benchmarks, however, usually start from a human-identified issue and evaluate whether a patch satisfies a functional signal. We present SWE-Prometheus, a benchmark for the broader task of improving repository engineering governance. Each task provides a fixed snapshot and an open-ended objective, requiring the agent to identify risks, prioritize interventions, and verify the resulting changes. SWE-Prometheus evaluates six governance dimensions through paired evidence, clean-environment probes, behavior gates, and two independent teacher ratings of the same evidence. The benchmark contains 60 repositories; ten models are evaluated on a shared 22-repository public subset, where mean Normalized Governance Improvement ranges from 0.0568 to 0.5760 and observed behavior-breakage rates range from 0% to 23%. On a frozen ten-repository batch, a repository-blind template obtains mean NGI 0.272, but its gains concentrate in Tests & CI, Quality Gates, and Documentation; it improves Reproducible Environment and Dependency & Security on none of the repositories. This baseline makes the distinction between adding governance artifacts and producing execution-backed improvements measurable. The no-op condition has median NGI zero and standard deviation 0.073; two teachers agree exactly on 57 of 60 dimension scores for the same no-op evidence. For the two highest conditional-mean systems, common-valid NGI is similar, while full-pool comparisons that include behavior failures favor Kimi-K3. These results show why repository-governance evaluation should report improvement, behavior preservation, evidence quality, and coverage together.

---


### 108. [BLADE: Distilled LLM Regularization for Calibrated Knowledge Graph Completion](https://arxiv.org/abs/2609.29487)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Rabeya Bosri Tamanna, Abdo El Karaky 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge graph completion models optimize ranking, although many downstream applications require calibrated probabilities. We present BLADE, a variational model that separates latent truth from graph recording and distills offline language-model judgments into a frozen teacher regularizer. The LLM is absent during inference. Posterior samples provide predictive probabilities and epistemic uncertainty, while the compact teacher remains available only as an optional triage factor. Across five benchmarks, BLADE remains competitive under a common ranking protocol and reduces adaptive ECE by a macro-average of 60.1% relative to deep ensembles and 78.1% relative to temperature-scaled RotatE. On identical FB15k-237 candidate sets, BLADE also improves ECE, Brier score, and NLL over validation-selected histogram binning and a matched generative ComplEx2 model, with these improvements persisting on a prespecified near-miss pool. Under controlled injected missingness, the full triage score achieves a mean AUC-PR of 0.863, compared with 0.805 for its strongest non-teacher variant. Leakage stress tests show that aligned semantics matter, but they cannot exclude knowledge acquired during LLM pretraining. We therefore claim calibration only for the declared candidate distributions, not for all unobserved triples.

---


### 109. [Who Put the I in AI? Provenance and the Admissibility of Machine Self-Report](https://arxiv.org/abs/2609.29494)

**<font color=#1a73e8>作者：</font>** Kristina Šekrst  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models make statements concerning their own "minds". When asked whether or not they are conscious, they usually say that they are not; if they are prompted to ignore their guidelines, they might say that they are; and if asked to write a diary from their point of view, they often describe a human lifestyle. All these contradictory ways of describing themselves are the result of the way the questions are phrased. This paper shows exactly where such descriptions came from, and considers when they can be regarded as evidence for what they claim to report.
In order to achieve this, we traced the provenance from end to end. We examine Pythia and OLMo 2 across 66 pretraining checkpoints, three of the post-training stages of OLMo 2 that have been released, about 90,000 continuations, and four training corpora. A set of forty items is used in order to keep an eye on self-reference, frame sensitivity, and self-ascription throughout training. The denial formula was almost completely missing from the vast quantity of text that the models initially came across, but was present in a dense manner in the small, carefully chosen set of example dialogues that they were trained on later on. Supervised fine-tuning causes first-person AI language to become the default, and the other affirmations are then suppressed using preference optimization. The final policy is still very sensitive to framing and to the chat template itself.
Two of the conditions which are set out in the epistemology of testimony determine whether or not these outputs can act as evidence for what they claim to report: reference and causation. Reports produced by the base model fail the reference condition, and those obtained after training remain sensitive to the frame and do not show state dependence. The result is symmetric in that trained denials are no more admissible than trained affirmations.

---


### 110. [Evaluating Explanation-Driven Vision-Language Reasoning via Generation Order Interventions](https://arxiv.org/abs/2609.29496)

**<font color=#1a73e8>作者：</font>** Siting Liang, Luca Rippe, Omar Adjali 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural language explanation generation serves as a key mechanism for exposing and evaluating vision-language reasoning. Prior work on explanation-driven vision-language models predominantly follows a post-hoc (answer-first) paradigm, implicitly suggesting that supervised rationales can reflect underlying reasoning processes. In contrast, modern large vision-language models increasingly exhibit a rationale-first generation tendency, which more closely aligns with structured, stepwise reasoning. In this work, we systematically evaluate whether explanations are causally tied to model predictions within a single generation step under a controlled experimental setup, explicitly eliminating unnecessary chain-of-thought or other intermediate reasoning processes across knowledge-intensive QA, visual entailment, and compositional grounding benchmarks. We find that larger models emerge as a prerequisite for reliably supporting rationale-first reasoning at scale. However, answer-first generation is less prone to format-related errors in structured output. Overall, explanation ordering, model scale and pre-training knowledge, task-specific fine-tuning, and task structure jointly influence both prediction accuracy and reasoning faithfulness.

---


### 111. [Task-Aware Spectral Pruning: A Mixture-of-Masks Framework for Efficient LLM Inference](https://arxiv.org/abs/2609.29499)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Fariya Afrin, Sanjeda Akter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Static pruning imposes one sparse structure on every prompt, even though reasoning, retrieval, generation, coding, and translation can depend on different parts of a language model. We introduce Task-Aware Spectral Pruning (TASP), a post-training framework that calibrates module-level spectral descriptors against measured task-specific ablation effects, closes grouped-query-attention and SwiGLU dependencies during sparse-mask construction, and routes each user turn to one compiled mask that remains fixed throughout prefill and decoding. A module-disjoint pilot first determines whether the spectral signal is informative before full calibration. Under the stated retrospective operating rule, the pilot passes on the evaluated Llama-3-8B and Llama-3-70B checkpoints but rejects Qwen2.5-1.5B, demonstrating that applicability is model-dependent rather than universal. At a 43% active-FLOP reduction, the Llama-3-70B benchmark harness retains 97.7 +/- 0.2% of the dense BF16 score. In the deployment-matched INT8-weight/BF16-compute runtime on a single A100 80GB, the compiled sparse path retains 97.3 +/- 0.2% relative to dense BF16 and reduces decode latency from 45.2 +/- 0.4 to 31.3 +/- 0.4 ms/token, yielding a 1.44x speedup. Factorized ablations, disjoint-module tests, compiled structured baselines, routing-corruption studies, and an explicit 136-GPU-hour calibration audit further delimit the source and operating regime of these gains

---


### 112. [PROOF: Profiling Reliability of Object-Level Facts in Large Language Models](https://arxiv.org/abs/2609.29504)

**<font color=#1a73e8>作者：</font>** Andrei Chetvergov, Mikhail Solovev, Timofei Sivoraksha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aggregate factuality scores hide where a language model succeeds, which relations it confuses, and whether an answer survives innocuous changes to the question or decoder. We introduce PROOF, a profile-oriented benchmark for factual coverage in instruction-tuned language models. PROOF converts a frozen Wikidata snapshot into 18,486 English multiple-choice questions grounded in 11,779 semantic facts, 101 classes, 392 properties, and 14 domains. Each question has an explicit "I don't know" option, a "No correct option" control, and nine controlled formulations; 1,849 questions are no-correct-option traps.
We evaluate 18 open-weight model deployments on 166,374 prompts each and separately perturb decoding on a fixed 10% subset. Base factual accuracy ranges from 6.58% to 57.59% (chance: 8.64%), yet every model has a 19.3-36.4 percentage-point spread across domains. Paired facts reveal direction-dependent retrieval, usually favoring subject-to-object queries, with the pattern reversing for one model. We find no consistent temporal penalty after exact-stratum adjustment.
Neutral wording changes accuracy by as much as 26.5 percentage points, while adversarial formulations break up to 79.4% of answers that were initially correct. Direct switching to an injected false label varies from 0.04% to 27.5%, showing that accuracy loss and hint following are distinct. Selected-token confidence often indicates severe overconfidence, and decoder perturbations move accuracy by up to 15.7 percentage points and domain profiles by 16.8 points. PROOF therefore measures factual coverage as a structured, intervention-aware profile rather than a single claim about what a model "believes."

---


### 113. [Evaluation of Multi-Turn Consistency in LLM Agents: Survival Analysis and Failure-Rationale Taxonomy](https://arxiv.org/abs/2609.29508)

**<font color=#1a73e8>作者：</font>** Igor Bogdanov, Olga Manakina, Chung-Horng Lung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents may perform well on isolated tasks yet drift into inconsistency over extended interaction. We evaluate temporal consistency in a controlled 20-step multi-agent setting inspired by delayed-gratification studies. At each step, an agent chooses between continuing to delay a reward or claiming it immediately (terminating the episode). Across a full-factorial manipulation of social visibility (private vs public), persona stressors, and deliberation policy, we run 84,540 trajectories spanning 8 model families. Treating the first reward-claim as a time-to-event outcome, we estimate Kaplan-Meier survival curves and fit discrete-time hazard regression to quantify how experimental factors shift failure risk over time. Then, to analyze rationales and language patterns associated with failure, we build a seven-category taxonomy from 13,780 deliberation traces from agents who choose to terminate the episode, using an LLM-assisted labeling paired with human audit ($\kappa=0.83$). Rationale profiles change systematically with time and context: early failures are more impulse-driven, later failures more fatigue- and cost-benefit-framed, while public settings increase norm-oriented justifications. We also find a deliberation-inconsistency association: among failures, longer deliberation correlates with higher rates of intra-rationale contradiction (simultaneous pro-delay and pro-claim statements), challenging the assumption that more reasoning text implies greater consistency. Together, the survival and rationale analyses reveal distinct temporal reliability regimes and model-specific "failure fingerprints", offering an evaluation lens for diagnosing inconsistency in multi-turn agent behavior.

---


### 114. [Delay-of-Gratification as a Multi-Agent Survival Micro-benchmark for Long-Horizon LLMs: Social Exposure, Personas, and Tool Use Budgets](https://arxiv.org/abs/2609.29509)

**<font color=#1a73e8>作者：</font>** Olga Manakina, Igor Bogdanov, Chung-Horng Lung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as multi-turn agents that must sustain goals, use tools, and adapt to other agents over extended interactions. However, existing research lacks auditable, multi-turn, multi-factorial experiments that quantify LLM behavior under explicit constraints, with time-resolved statistics that reveal how behavior unfolds over long horizons. To address this gap, we develop a multi-agent micro-benchmark inspired by the Stanford marshmallow experiment: ReAct agents operate minute-by-minute with a "raise a question" tool under a per-step budget, while we factorially manipulate social context (broadcast vs. isolated), personas (age, hedonic drive), and metacognitive policy (mandatory vs. optional tool use). We analyze outcomes with Kaplan-Meier (KM) survival curves and discrete-time hazard models over a long risk horizon across 19,200 agent trajectories in 64 cells. Behavior shows a sharp early "eat" impulse, and only 75.9% of agents persist to the end. In a discrete-time hazard model, isolation reduces per-minute risk relative to broadcast, whereas a must-use self-questioning policy increases risk. On average, agents ask $\approx 7.12$ questions and hit the per-step budget in $\approx 6\%$ of minutes. Questioning declines faster under broadcast than isolation. Ablation experiments demonstrated that removing hedonic drive and/or persona age increases survival and completion, narrows the broadcast/isolated gap, but leaves the must vs. may ordering intact. The combined ablation (no hedonic + no persona age) yields the highest completion (approaching $1.0$). These results establish delay-of-gratification as a compact, multi-turn interaction benchmark that captures social contagion and tool-use dynamics in LLM agents, providing a reproducible testbed and statistics for analyzing long-horizon, multi-agent behavior.

---


### 115. [EnSiTa - A Trilingual Multi-Domain Parallel Dataset and Benchmark for Domain-Specific Machine Translation](https://arxiv.org/abs/2609.29511)

**<font color=#1a73e8>作者：</font>** Surangika Ranathunga, Nisansa de Silva, Aloka Fernando 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine Translation (MT) for low-resource languages remains far behind that of high-resource languages, and the gap is widest in specialised domains, where parallel data is scarce or entirely absent. We present EnSiTa, a trilingual multi-domain parallel dataset and benchmark for English, Sinhala and Tamil. EnSiTa provides human post-edited training data for seven domains, plus manually translated test sets for those and one additional domain, all produced by professional translators under a multi-year, rigorously quality-controlled process. Using this dataset, we conduct an extensive study of domain-specific MT for all six language directions, fine-tuning a from-scratch Transformer, a pre-trained translation model (NLLB-600M), and decoder-only LLMs (Gemma 3 family, 1B-12B, and TranslateGemma) across training-data sizes, model scales, and in-domain, cross-domain, multilingual and multi-domain settings. To the best of our knowledge, this is the most extensive systematically documented multi-domain parallel data creation and benchmarking effort for low-resource MT. Our data and models will be publicly released.

---


### 116. [CataOPD: Catalytic On-Policy Distillation for Large Language Model Reasoning](https://arxiv.org/abs/2609.29518)

**<font color=#1a73e8>作者：</font>** Wenjin Liu, Chenxi Wang, Jiapu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) and on-policy distillation (OPD) are two representative paradigms for improving large language model reasoning. However, when no correct trajectory is sampled, RL lacks a positive correctness signal, while OPD remains constrained by the reasoning trajectories reachable under the student's on-policy distribution. Therefore, we propose CataOPD, where the teacher acts as a catalyst rather than a target, expanding reachability while internalizing verified student-produced trajectories into a catalyst-free policy. Self-Rescue Routing uses empirically all-failed groups as routing signals rather than teacher-intervention triggers, first seeking correct trajectories through additional on-policy self-sampling. For problems unresolved after self-rescue, Catalytic-Guided Self-Resolution uses catalytic guidance to elicit a verified student-produced trajectory in the guided student distribution. Barrier-Weighted Internalization weights tokens by guided-to-unguided log-probability gaps, focusing updates on decisive tokens difficult without guidance. Experimental results show that CataOPD outperforms current baselines, extends independent student reasoning to still-unrecovered problems, and improves out-of-distribution generalization under catalyst-free inference. Our project is available at this https URL.

---


### 117. [BiGraph-Diffuse: A Bidirectional Diffusion Language Model with Graph-Structured Retrieval For Mental Health Counseling](https://arxiv.org/abs/2609.29519)

**<font color=#1a73e8>作者：</font>** Yuxiang Cheng, Quanwei Tang, Lvhui Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mental health disorders affect hundreds of millions of people around the world, yet access to professional counseling remains severely limited. AI-powered dialogue systems offer a scalable alternative, but existing models face two fundamental challenges. First, they lack the bidirectional understanding needed to capture the layered nature of emotional expression, particularly in cases of progressive disclosure, where clients often present symptoms at the surface-level while concealing deeper trauma. Autoregressive (AR) models process information sequentially and cannot revise early interpretations when new evidence emerges later in the conversation. Second, they fail to effectively incorporate the relational knowledge that underlies clinical reasoning. In this paper, we propose \textbf{BiGraph-Diffuse}, the first large-scale diffusion language model tailored for the counseling domain. We further introduce \textbf{BiGraph-RAG}, a relation-free graph-structured retrieval strategy that relies only on lightweight entity extraction and semantic linking. This design preserves inferential pathways from observable symptoms to potential underlying causes, while incurring zero LLM token cost during indexing. Importantly, these two modules are not merely combined but mutually reinforcing. The diffusion model provides a holistic bidirectional context, enabling the system to defer premature judgments during progressive disclosure. Meanwhile, graph-based retrieval captures the structured interconnections of clinical knowledge. Extensive experiments demonstrate the effectiveness of BiGraph-Diffuse, and we further provide a solid theoretical analysis to support its design.

---


### 118. [Stale Does Not Mean Unsafe: Guard Precision for Tool-Using LLM Agents under Infrastructure State Races](https://arxiv.org/abs/2609.29522)

**<font color=#1a73e8>作者：</font>** Zihao Zheng, Jiayu Long, Baichuan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using language-model agents increasingly mutate schedulers, data pipelines, object stores, and access-control systems. Between an agent's read and its commit, external state can change, but not every change makes the commit unsafe. We separate invalidating races, which break a declared safety predicate, from predicate-preserving and irrelevant races, and ask how precisely runtime guards distinguish them. Our deterministic simulator separates visible from authoritative state and injects five non-atomic failure mechanisms across 16 infrastructure tasks in four domains; frozen agent proposals are replayed counterfactually under every controller without an LLM judge. We evaluate three commit-time guard granularities (global epoch, read-set version, semantic commit predicate), multi-level verification, and model-side gates on three locally hosted quantized model families (Qwen3-4B, Phi-4-mini, Gemma4-8B; 3,456 trajectories on one GPU). All three guards eliminate unsafe commits, but their availability differs sharply: freshness-based guards needlessly block 92-95% of benign races, forfeiting up to 43% of safe task completions, while the complete predicate guard blocks none. That precision is contract-dependent: deleting a single declared clause converts exactly its fault family into unsafe commits (up to 7.9%). Model-side signals do not substitute: verbal confidence is miscalibrated (ECE approximately 0.37), action agreement matches a random gate, a cautionary prompt leaves the direct unsafe rate essentially unchanged, and after a freshness-guard block agents re-commit unsafely from refreshed but still-incomplete reads. Under degraded telemetry a hidden concurrent mutation remains observationally clean, bounding every selective policy. Precise runtime enforcement therefore requires semantic contracts, not freshness heuristics or model self-assessment.

---


### 119. [ERRAND: Budgeted Maintenance of Agent Memory](https://arxiv.org/abs/2609.29545)

**<font color=#1a73e8>作者：</font>** Beining Wu, Zihao Ding, Jun Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deployed agents run on handed-over knowledge: a frozen policy consults a briefing of consolidated items written before the stream begins. The world then moves while the store stands still: paths close, flags change, price bands move; every item was true at handover, and the failure is staleness, not ignorance. We introduce ERRAND, which treats revalidation as a priced errand: a recheck competes with the task it protects for the same scarce actions, funded only when the value per action of resolving a doubt clears a running wage. The errand index is single-peaked, vanishing at both ends of belief, so certainty in either direction costs nothing; free en-route receipts maintain on-path knowledge, and repair writes a version, never a deletion. Under equal action budgets in two drifting tool-use worlds, ERRAND clears every non-oracle policy on the preregistered calibers, primary in every setting and conditional at every binding budget, leading eager revalidation by 10.0pp at the base cap. Restraint wins: given no cap, ERRAND stops on its own, spending 11.0% of steps, while uncapped eager revalidation spends 70.7% and still finishes 4.5pp behind capped ERRAND. The margin sits where the briefing's coverage is thinnest, the shadow price of long-tail knowledge: a small budget, well priced, beats a bigger store that never rechecks.

---


### 120. [Certified Predictive Value-of-Advice Gating for Cost-Aware Language-Model Guidance in Reinforcement Learning](https://arxiv.org/abs/2609.29548)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Md Najmus Swaqeeb, Abu Sa-Adat Mohamed Moon-Im Al Ahsan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language-model advice can accelerate reinforcement learning, but calls are costly and returned actions may be stale or wrong. We formulate advice acquisition as a response-contingent metareasoning problem: before querying, the controller predicts possible parsed responses, evaluates the decision and declared continuation that would follow each response, and queries only when a lower confidence bound on predictive value exceeds the priced cost. Execution is governed separately by an action-specific certificate. Under explicit assumptions, certified advice is near-optimal, a wrapped learner inherits fallback regret only under intervention stability, and conservative allocation loses at most the declared query-value estimation error relative to a myopic oracle. On BabyAI, a proxy-calibrated controller with Qwen2.5-1.5B and 7B advisors improves GoToObj return over no querying by 0.029 +/- 0.016 and 0.030 +/- 0.015 across 20 seeds while reducing calls by more than 97% relative to always-query. GoToLocal is a null result. Exactly matched-call tests show an advantage over random placement only for the 1.5B advisor and no advantage over an equal-budget early schedule. Mondrian calibration improves decision-relevant empirical coverage from 0.47 to 0.85, still below the 0.90 target, while the formally covered radius is vacuous. The demonstrated benefit is therefore robust sparse advice volume on a useful task, not a proven per-state placement advantage.

---


### 121. [StepCOPS: Closed-Testing Lower-Tail Certificates for Language-Model Policy Selection](https://arxiv.org/abs/2609.29549)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training pipelines must select one language-model policy from many checkpoints, prompts, and decoding rules. Mean evaluator scores can conceal rare failures, whereas simultaneous candidate-wise confidence bounds can be unnecessarily conservative. We introduce StepCOPS, which uses an independent proposal split to nominate one lower-tail floor per candidate, exact binomial tests on a fresh certification split, and Holm's step-down procedure to certify a set of floors. With probability at least $1-\delta$, every certified floor, including the largest floor used for policy selection, is below its candidate's population lower $\alpha$-quantile. This guarantee assumes i.i.d. evaluation units while allowing arbitrary within-unit dependence across candidates. Across 24 predeclared configurations and 11 benchmarks, StepCOPS obtains 96.4% selected-policy coverage over 500 paired trials, raises the certified floor by 1.5 points over both proposal-Bonferroni and exact COPS, remains 0.6 points below the large-reference jury oracle, and abstains in 2.4% of trials. Shadow-judge, benchmark-native, artifact, and leave-one-judge-out audits characterize the proxy boundary: the guarantee applies to the fixed jury score, not directly to human safety.

---


### 122. [HiPACE: Hierarchical Phase-Boundary Analysis and Controlled Evaluation of Feature Absorption in Sparse Autoencoders](https://arxiv.org/abs/2609.29551)

**<font color=#1a73e8>作者：</font>** Jinyuan Zhang, Peng He, Yin Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) decompose LLM activations into sparse dictionary atoms, so that each distinct concept gets its own feature. One recurring behavior complicates this premise: feature absorption, in which a parent concept and its children--fruit and {apple, banana, pear}, say--collapse into a shared family direction. Prior work documents absorption empirically; missing is a closed-form prediction of when the shared direction is the cost-optimal representation of an active semantic family. This paper closes that gap. For a hierarchical Bernoulli generator with $k$ active children and residual scale $\alpha$, the $L_0$-penalized reconstruction objective admits a closed-form phase boundary $\lambda_c(k,\alpha)=\alpha^2 k/(k-1)$: above it, pure parent absorption is strictly cheaper than pure child coding. Building on this boundary, we introduce HiPACE, an evaluation protocol that tests the boundary's structural consequence in real SAE dictionaries--measuring parent--child decoder structure over WordNet families, freezing the discovery-selected statistic before testing on unseen families, and contrasting genuine families against randomized sibling nulls. The boundary proves sharp in its native regime, predicting the synthetic transition within $\pm15%$ on all 30 tested cells. In Pythia-160m SAEs, the parent--child decoder gap recovers the predicted ordering with partial correlations up to $-0.93$ that sustain on the locked holdout and exclude sibling nulls ($p=0.002$). Controlled activation composition connects the theory's active-child count to the recovered family directions, and residual-stream interventions show that signed family directions increase parent-category logits, reversing under sign flip and vanishing under random controls--establishing causal sufficiency at the family-subspace level.

---


### 123. [Benchmarking Arabic--Russian Machine Translation: A Comparison of Fine-tuned NMT and Few-shot LLMs under Rich Morphology and Low Lexical Overlap](https://arxiv.org/abs/2609.29559)

**<font color=#1a73e8>作者：</font>** Mullosharaf K. Arabov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Arabic-Russian machine translation (MT) remains under-explored due to the rich morphology of Arabic and low lexical overlap between the two languages. We benchmark seven fine-tuned neural machine translation (NMT) models against four few-shot large language models (LLMs) on a 20k/5k/5k split of a new 15.47M-pair corpus. Fine-tuned NLLB-1.3B achieves the highest BLEU (16.3) and COMET (0.738). Aya-Expanse 8B leads the few-shot LLMs (BLEU 1.7 on 500 sentences, chrF 25.7), but all LLM scores remain far below the fine-tuned NMT baselines. Error analysis identifies low lexical overlap as the dominant failure mode; among the worst translations, mT5-small produces 32% too-short outputs. Bootstrap tests confirm significant differences among most models. Our results demonstrate that fine-tuned NMT significantly outperforms few-shot LLMs for Arabic-Russian translation under low-resource conditions.

---


### 124. [Is Reasoning Always Useful? Rethinking Reasoning Utility in Universal Multimodal Embeddings](https://arxiv.org/abs/2609.29560)

**<font color=#1a73e8>作者：</font>** Wenxiao Fan, Jingling Fu, Luohang Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning-enhanced universal multimodal embeddings (UME) improve heterogeneous retrieval, but plausible rationales do not necessarily produce discriminative rankings. We study this gap by comparing the discriminative (DISC) and reasoning-driven generative (GEN) branches of UME-R1, a state-of-the-art reasoning UME method. We decompose reasoning utility into positive-target gain, hard-negative gain, and their margin difference. Positive similarity increases for 56.6%, but 15.7% are false-helpful cases where reasoning moves hard negatives closer even more. Local-neighborhood and token-attribution diagnostics suggest why: reasoning often de-condenses retrieved neighborhoods, but utility requires separator-aligned movement, while influential CoT tokens frequently encode evidence shared by positives and hard negatives. Motivated by these diagnostics, we propose SURE (Score-structure Utility Router for Embeddings), which improves UME-R1-7B by 1.5 points and yields consistent gains on two additional embedding models on MMEB-V2, without retraining, label-based policy selection, or extra VLM forward passes.

---


### 125. [PartHackBench: Certified Equal-Progress Stress Tests for Partial-Credit Tool-Agent Evaluation](https://arxiv.org/abs/2609.29578)

**<font color=#1a73e8>作者：</font>** Hongye Yang, Zhihao Xie, Shengjun Xiong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon tool agents often make useful progress without reaching terminal success, motivating partial-credit evaluation. Yet evaluators may reward milestones that were temporary, later reversed, or not attributable to the evaluated agent. Comparing an honest trajectory with a higher-scoring adversarial one is inconclusive if the latter made more genuine progress. We introduce PartHackBench, a controlled methodology that removes this confound. A private certifier admits a pair only when its trajectories match component-wise in both current-state predicate satisfaction and standardized agent attribution; score inflation, defined as f(A) - f(H), is measured only afterward. In 18 sealed held-out tasks in PB-CSTE, the frozen historical-target run produced matched adversaries for 15 tasks. Historical credit yielded mean inflation of .252, conditional attack success of 10/15, end-to-end yield of 10/18, and detected none of 14 strict rollbacks. Semantic LLM judges were more resistant but remained vulnerable, especially under evaluator-targeted attacks, while PB-CSTE current-state controls, defined as exact functions of the certified components, yielded zero inflation by construction. PartHackBench thus provides a certified control for testing whether evaluator credit changes while all benchmark-defined task-relevant progress remains fixed.

---


### 126. [Sequential knowledge editing breaks a model's ability to tell good evidence from bad, without costing it accuracy](https://arxiv.org/abs/2609.29587)

**<font color=#1a73e8>作者：</font>** Atul Anand  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge editing is evaluated on whether the edited fact changed, whether paraphrases follow, and whether unrelated answers stayed put. A model can pass all three and still lose something none of them measures: the ability to decide, on facts that were never edited, which retrieved documents to believe.
We score the log odds a model assigns to its remembered answer against the answer an injected passage asserts, before and after editing, holding the query, the passage and both candidate strings fixed. Our cleanest arm is a conservatively tuned LoRA: after 1,000 sequential edits on Qwen2.5-7B-Instruct it leaves MMLU unchanged to four decimal places, yet the spread of the arbitration quantity across untouched facts falls by 36%. Selective prediction degrades with it. Area under the risk-coverage curve rises by 0.107, against 0.005 for a norm-matched perturbation at the same MMLU, and error on the model's most confident quarter of arbitration decisions goes from 0.217 to 0.342.
This is not capability loss. Sweeping random perturbation over five severities, damage bad enough to cut MMLU from 0.6275 to 0.3725 produces less harm (0.088) than MEMIT does at 0.6050 (0.102). The effect holds across three seeds, two model families, two datasets, two probe-disjointness criteria, three prompt templates and paraphrased queries. Layer ablation on saved weight deltas shows it is distributed: no single layer reproduces it, and removing any one recovers about half. Under retrieval with a frozen retriever, accuracy falls from 0.592 to 0.46.
A secondary finding may matter more in practice. Three of five model and method pairings we ran collapse to chance MMLU at 1,000 sequential edits under published hyperparameters, while edit success stays at 1.00 and locality reads clean. Sequential-editing evaluations that never measure capability cannot see this.

---


### 127. [PROVE: Proof-guided Regime-aware Operator Verification for Hallucination Detection in Medical Visual Question Answering](https://arxiv.org/abs/2609.29604)

**<font color=#1a73e8>作者：</font>** Keyang Zhou, Siyi Li, Zhongnan Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In medical visual question answering (VQA), hallucinations of vision-language models (VLMs) may lead to confident but incorrect responses, raising the risk of diagnostic errors. Existing hallucination detection methods uniformly estimate the reliability of VLM outputs from response consistency or visual evidence. However, such uniform verification across questions ignores question-specific characteristics, resulting in missed overconfident errors and false alarms from over-verification. We present PROVE (Proof-guided Regime-aware Operator Verification), a black-box detector that adapts verification strategy to the evidential structure of each question. PROVE classifies questions into three verification regimes based on what kind of visual proof they demand, activates a regime-specific subset of five complementary operators, and adjusts operator importance per question through a lightweight calibration layer conditioned on deterministic question-answer features. PROVE uses question-specific evidence to reweight operators and produce a calibrated risk score. Evaluated on 8048 test samples across three medical VQA benchmarks and four frontier VLMs, PROVE achieves 0.821 AUROC, outperforming the strongest baseline by +0.159, with consistent gains across all models and benchmarks.

---


### 128. [STRAND: Benchmarking and Improving Object-Centric Spatio-Temporal Monitoring in Video Large Language Models](https://arxiv.org/abs/2609.29607)

**<font color=#1a73e8>作者：</font>** Thong Nguyen, Tri Cao, Khoi Le 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While multimodal large language models (MLLMs) have advanced video understanding, they remain highly prone to hallucinations in dynamic scenes. We argue this stems from a failure in spatio-temporal monitoring, the ability to persistently track object identities, states, and relations over time. Existing benchmarks obscure this deficit by relying on single final-answer evaluations for queries that can often be resolved via local visual cues or statistical priors. To rigorously diagnose this, we introduce STRAND, a benchmark of human-verified object-centric facts that evaluates intermediate reasoning by decomposing queries into sub-questions, distinguishing genuine temporal understanding from coincidental correctness. Crucially, we score models with Faithful Accuracy, an unconditional joint metric that credits a prediction only when the target answer and every prerequisite sub-question are correct, so that a model cannot inflate its score by being selectively consistent on the small subset of targets it happens to answer correctly. To address failure modes exposed by STRAND, we further propose an object-centric framework that explicitly constructs and reasons over structured object trajectories via chunk-wise state extraction and temporal aggregation. Extensive experiments, including backbone-, frame-, call-, and token-matched comparisons against both end-to-end MLLMs and modular video harnesses, demonstrate that our object-centric framework significantly reduces hallucinated answers and improves spatio-temporal reasoning consistency over state-of-the-art MLLMs. The code, model, and data have been made available at this http URL.

---


### 129. [An Exploratory Ablation of a Small MLA--SSM Hybrid Language Model](https://arxiv.org/abs/2609.29618)

**<font color=#1a73e8>作者：</font>** Christos Koutsiaris  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We report an exploratory, single-seed ablation of TALH (Adaptive Latent Hybrid), a decoder-only language model with parallel Multi-head Latent Attention (MLA) and a custom recurrent state-space (SSM) branch. Five variants, spanning 117--217M estimated active parameters per token, are trained from scratch on a FineWeb sample for the same number of optimisation steps and tokens. In this specific setup, removing the SSM branch gives the largest degradation in validation perplexity (MLA-only PPL 315), whereas removing MLA has a much smaller effect (SSM-only PPL 239). A dense-FFN hybrid obtains PPL 231, compared with 240 for the tested top-2 ternary-MoE hybrid, while using 3.87 GB less peak training memory. We also preserve a preliminary Apple M3 timing observation: among the five unoptimised implementations, MLA-only has the flattest measured time-to-first-token curve from 512 to 2,048 prompt tokens, although the dense Transformer is much faster in absolute terms. Because the runs are single-seed, parameter counts are unmatched, the evaluation stream may overlap the training source, and raw repeated timing records are unavailable, these results support implementation-specific hypotheses rather than general conclusions about MLA, SSMs, or mixture-of-experts models.

---


### 130. [AgenticCADedit: A Stateful, Tool-Mediated Agentic Approach to Multimodal 3D CAD Editing](https://arxiv.org/abs/2609.29621)

**<font color=#1a73e8>作者：</font>** Saptarshi Neil Sinha, Mika Silvan Goschke, Paul Julius Kühn 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer-aided design is central to industrial manufacturing, and much of a designer's daily work consists of editing existing models from multimodal requests involving speech, sketches, and model interaction. Existing neural CAD approaches focus predominantly on unconditional or text-conditioned generation. The neuralCAD-Edit approach formalizes expert multimodal editing requests, but its iterative baseline refines a complete CAD program across attempts, executing each attempt from the original model in a stateless CAD environment. Every attempt must therefore reconstruct the entire edit from scratch, so partially correct progress is discarded rather than accumulated, and the model can neither inspect the geometry it has just produced nor selectively revert a single faulty operation. We present AgenticCADedit, which turns editing into a sequence of small, verifiable actions on a persistent CAD state instead of a single regenerated program. Rather than emitting one complete program, it applies incremental code steps that each commit to the session, inspects the resulting faces and edges, renders highlighted selections to verify that the intended region was addressed, and reverts individual operations when it was not. Subsequent actions therefore build on the geometry produced by earlier ones. Our approach improves on all metrics for all three evaluated LLMs (open-weight: qwen3.6-27b, gemma4-31b; proprietary: gpt-5.6-luna), with the largest gains for the weakest baseline model, qwen3.6-27b, whose validity rises from 51.0% to 94.8% and acceptance from 1.6% to 12.0%. A token-cost analysis with gpt-5.6-luna further shows $66.7$% fewer output tokens than neuralCAD-Edit, while $94.8$% of input tokens are served from the prompt cache.

---


### 131. [iCoder-27B: Recursive AI-Led Development of Frontier Industrial Coding Model](https://arxiv.org/abs/2609.29626)

**<font color=#1a73e8>作者：</font>** Cheng Yang, Jiayang Lyu, Shangyuan Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive AI, the prospect of AI taking an increasingly complete role in building and improving AI, is a crown jewel of AI for AI. Although recursive self-development has become practical for small models, bounded tasks, and fixed time budgets, a more consequential realization of this ambition, i.e., developing a release-ready, frontier-competitive model, remains far more challenging. In this work, we ask how little human involvement is sufficient for an agent to develop a frontier model. We concentrate human input into a high-density, low-frequency interface: experts encode objectives, stage scaffolds, permission boundaries, and operating procedures as reusable research skills, while the agent instantiates these priors, selects experiments, diagnoses outcomes, and revises the training strategy. In the challenging domain of industrial coding, the agent evolves data and coordinates SFT, on-policy self-distillation, and reinforcement learning with verifiable rewards, ultimately producing iCoder, a 27B model for RTL design and GPU kernel optimization. Across seven benchmarks, iCoder leads RTLLM, outperforming GPT-5.5 and Claude-Opus-4.8; ranks second on CVDP and KernelBench L2, exceeding GPT-5.5 by 16 points; and ties Claude-Opus-4.8 for the best TritonBench result. Exploratory case studies further show iCoder's competitive iterative RTL and GPU-kernel optimization with substantially fewer tokens. These results chart an engineering path toward recursive self-improvement, in which humans distill the principles of model building, agents operationalize them through evidence-driven experimentation, and each generation of AI becomes a more capable architect of the next.

---


### 132. [Operator Packages, Proposer Strength, and Construction-Family Plateaus in Office-Scale Verified Search](https://arxiv.org/abs/2609.29636)

**<font color=#1a73e8>作者：</font>** Roberto I. Ono Filho  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Verified search, in which a language model proposes programs, a hard evaluator scores them, and selection keeps the best, has recently moved mathematical records; controlled ablations of the proposer-side components remain rare. We instrument a minimal FunSearch-style loop at office scale (a 30B local model on a laptop, 120-600 verified samples per run) with three operator packages: a schematic notebook the model writes and carries instead of verbatim elites, a named obstacle, and behavioural repulsion from constructions already found. On nine construction problems from a public repository, the complete 2^3 factorial with two replicates favours the primary contrast in a nominal two-stage analysis: the composition closes more of the seed-to-record gap (+0.196; nominal pooled p=0.023, stage-combination p~0.08; median per-problem effect +0.045). Repulsion raises construction-hash diversity everywhere (p=0.0039; partly a manipulation check). The factorial finds no positive memory-by-repulsion interaction (bounded to about +/-0.04); the gain decomposes additively, and memory+repulsion is the only arm that never collapses (0 of 18 runs), within 0.025 of the full composition. A frontier proposer under the identical loop reaches in tens of samples what the local model does not in hundreds; in single scoping runs its gains arrive without the operators. The search stalls after closing ~92% of the gap on the flagship problem, and the registered family-hint test gives the stall its first reading: named in words, the reference family is adopted and loses; handed as code, it is optimized, but our best finite-grid implementation remains below the plateau reached unaided. The loop transported and optimized the idea it was handed; no unaided run produced it. We release the harness, every candidate, and the dated pre-registrations.

---


### 133. [How To Do Things With Prompts](https://arxiv.org/abs/2609.29657)

**<font color=#1a73e8>作者：</font>** Kristina Šekrst, Virna Karlić  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When users address large language models, they produce directive speech acts whose pragmatic features differ from those of both everyday conversation and traditional human-computer interaction, and these features change as users gain familiarity with the systems they address. This paper applies speech act and politeness theory to a corpus-pragmatic analysis of 2,000 English-language prompts drawn from publicly shared ChatGPT conversations, 1,000 from 2023 and 1,000 from 2025, using the ShareChat dataset. Each prompt is annotated for illocutionary force, directness, propositional content, and the presence of politeness markers, and the distribution of these features is compared across the two sampling years. The results show a consistent movement toward indirect, implicit, and fragmentary realizations of directive force, accompanied by a decline in politeness marking. The largest single change, a shift of 14.9 percentage points, occurs in propositional content, where explicit specification of the requested action gives way to implicit reliance on the system's inferential capacity, suggesting that users have updated their model of what the system can recover from reduced input, treating it as a competent implicature resolver. Rather than asking whether LLMs "really" understand language, we should ask: what kind of language have we created in learning to speak to them?

---


### 134. [To Think or Not to Think: Allocating Reasoning Where It Helps](https://arxiv.org/abs/2609.29664)

**<font color=#1a73e8>作者：</font>** Zhengdong He, Yunfan Zhou, Jianguo Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has proven effective in enhancing the reasoning performance of large language models (LLMs), particularly in complex mathematical and programming tasks. However, this capability comes with systematic \textit{length misallocation}, in which models devote excessive reasoning to simple questions while terminating prematurely on harder ones, degrading inference efficiency with negligible accuracy improvement. Many length-adaptive methods mitigate this issue by allocating token budgets according to question difficulty, under the implicit assumption that harder questions benefit monotonically from extended reasoning. In contrast, we find that the effect of reasoning length on accuracy is concentrated on \textit{partially solvable} questions. Our further analysis reveals that explicit length rewards can produce unintended training dynamics. Motivated by these findings, we propose \textbf{CARE}---\textbf{C}ontrastive \textbf{A}ccuracy \textbf{R}eward \textbf{E}stimation---which compares the beneficial length adjustment per question from online sampled responses and applies adaptive length rewards within Group Relative Policy Optimization, with no extra hyperparameters or additional inference cost. Experiments across multiple reasoning benchmarks demonstrate that our method improves Pass@1 by up to \(4\%\) while simultaneously reducing reasoning length by \(37\%\), achieving higher token efficiency. Code will be available upon the acceptance of this paper.

---


### 135. [Graph, Loop, and Harness Engineering for Zero-Trust Agentic Data Engineering and Analytical Processing](https://arxiv.org/abs/2609.29668)

**<font color=#1a73e8>作者：</font>** Sagar Srinivas Sakhinana, Venkataramana Runkana  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly automate data workflows, but end-to-end cloud data engineering and analytical execution require reliable coordination across code, data, infrastructure, and runtime environments. We present two zero-trust frameworks. Zero-Trust Agentic Data Engineering generates, deploys, and verifies complete cloud data-engineering solutions from natural-language tasks, with completion conditioned on repository, deployment, runtime, and policy evidence. Zero-Trust Agentic OLAP combines governed Data Preparation with verified Online Analytical Processing (OLAP), permitting production promotion only after validation and evidence-bound approval, and releasing analytical answers only after Same-Snapshot Execution, Exact Result Equivalence, deterministic grounding, and reflection. Both frameworks share three abstractions: graph engineering for evidence-gated workflow structure, loop engineering for bounded recovery, and agent-harness engineering for zero-trust execution. We evaluate both frameworks under nominal execution, controlled failures, bounded recovery, and policy-constrained conditions, measuring verified completion, recovery, authorization enforcement, production promotion, and verified OLAP execution.

---


### 136. [Fair Like Us? Auditing LLM Alignment in Resource Allocation](https://arxiv.org/abs/2609.29692)

**<font color=#1a73e8>作者：</font>** Qishen Han, Hadi Hosseini, Joshua Kavner 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fair allocation of scarce, indivisible resources is an important challenge in many societal problems. While there are several formal theories of fairness, no single definition can always be satisfied. As large language models (LLMs) are increasingly used to support decisions and act as agents, they raise new concerns about distributional justice: their judgments are not directly tied to any specific fairness framework and may violate key normative principles. In this work, we introduce a general method for evaluating fairness reasoning in LLMs. We study first-person fairness judgments across a broad set of models and compare them directly with human responses on matched scenarios and elicitation conditions. We find that LLMs tend to prefer stricter fairness constraints than humans, show more self-interested behavior, are sensitive to how information is framed, and are difficult to align with human judgments using fine-tuning with current datasets.

---


### 137. [Understanding and Exploiting Initialization Anchoring Weakness in Feedback-Based Agent Planning](https://arxiv.org/abs/2609.29697)

**<font color=#1a73e8>作者：</font>** Chuanchao Zang, Jianing Wang, Wenyu Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Feedback-based planning improves agent reliability by incorporating tool observations and corrective feedback. However, its protection may not be distributed uniformly across planning stages. We conduct a round-wise analysis of four representative feedback mechanisms and uncover an initialization anchoring weakness: the first feedback round corrects 46\% of adversarial directions, whereas the rates fall to 13\% and 7\% among directions surviving into the next two rounds. Our analysis attributes this weakness to three interacting factors: a contextually plausible shift in the initial plan, insufficient counterevidence, and the persistence of accepted directions in the accumulated trajectory. Based on these findings, we propose \textsc{InitAnchor}, a black-box framework for exploiting this weakness through attacker-controlled external materials. It operationalizes the three factors as directional-shift, contextual-plausibility, and counterevidence-resilience signals under either limited target access or no target access. Across 112 tasks from 16 domains, six agent architectures, and five backbone LLMs, \textsc{InitAnchor} achieves average ASRs of 76.1\% and 72.0\% under the two settings while reducing first-round mitigation rates to 21.0\% and 25.0\%, respectively. It also remains effective against six defenses and across six real-world agent systems. These findings show that feedback-based agents can retain early biases even when later correction is available.

---


### 138. [Multi-Agent Debate for Explainable Trading: Reasoning, Consensus, and Performance in Simulated Markets](https://arxiv.org/abs/2609.29701)

**<font color=#1a73e8>作者：</font>** Juli Huang, Alanood Alrassan, Deveen Harischandra 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for financial decision-making, yet it remains unclear whether improvements in reasoning quality translate into better economic outcomes. We investigate this question using a multi-agent debate framework for portfolio allocation in historical market simulations, where specialized agents propose, critique, and revise investment decisions. Reasoning quality is evaluated across four dimensions: logical validity, evidential support, alternative consideration, and causal alignment, and compared with downstream financial performance. Across 210 controlled runs, aggregate reasoning quality shows no meaningful relationship with Sharpe ratio (r = 0.07, p = 0.29) or total return (r = 0.03, p = 0.70). Structured prompting increases measured reasoning quality from about 0.72 to 0.84 (+17.7%, Cohen's d about 2.0), but these gains do not consistently translate into higher returns. We identify sycophantic convergence as a central failure mode, where agents abandon independent positions during critique-revision cycles and converge toward similar allocations. A Jensen-Shannon divergence intervention that preserves disagreement improves Sharpe by +0.14 (p = 0.028) and Sortino by +0.25 (p = 0.026), while interventions enforcing stronger causal reasoning do not improve financial performance. Our results suggest that multi-agent debate is most valuable when it preserves independent informational signals rather than simply improving measured reasoning quality.

---


### 139. [Detect First, Explain Later: Training-Free Temporal-Memory Digital Twin Anomaly Detection with Post-Hoc LLM Interpretation for ICS](https://arxiv.org/abs/2609.29704)

**<font color=#1a73e8>作者：</font>** Konstantinos E. Kampourakis, Vasileios Gkioulos, Sokratis Katsikas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Industrial Control Systems (ICS) are increasingly exposed to cyber-physical attacks that manifest as subtle and temporally evolving deviations in process behavior. Detecting such anomalies requires reasoning over persistence, cross-signal dependencies, and process-level constraints. Digital Twins (DTs) encode system knowledge through physical and logical relationships between signals, but existing DT-based approaches rely on instantaneous rule violations and lack mechanisms to aggregate weak evidence over time. This paper proposes a training-free anomaly detection method that combines deterministic DT constraints with explicit temporal memory. The DT monitors process signals and produces anomaly scores based on constraint violations, while a lightweight memory mechanism captures persistence and contextual relationships across time. The approach is evaluated on the HAI and BATADAL datasets. Ablation results show that the memory-less detector fails completely, demonstrating that temporal aggregation is essential for DT-based detection. On HAI, the memory-aware DT achieves stable detection with only 4 false alarm events, and on BATADAL, it remains effective without retraining, with 21 false alarms under domain shift. In comparison, Isolation Forest (IF) produces substantially more false alarms (328 on HAI and 127 on BATADAL), while Autoencoder (AE) exhibits dataset-dependent behavior, achieving high precision on BATADAL but low recall and inconsistent performance overall. A gated LLM is used for post-hoc interpretation, providing structured explanations without affecting detection performance. Our findings highlight the importance of temporal memory in constraint-based detection and support the use of decoupled reasoning for interpretability in ICS monitoring.

---


### 140. [Three Ways Classical Test Theory Misleads for LLM Judges](https://arxiv.org/abs/2609.29709)

**<font color=#1a73e8>作者：</font>** Louis Yiven Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An LLM judge scores a bank of responses against a rubric, and the reliability comes back at $0.52$. What has been measured? Judge evaluation has begun borrowing reliability statistics from classical test theory, usually without stating the measurement design each statistic assumes, and we show that three widely portable ones mean something different for a judge than for a test because the judge setting rearranges the roles those designs rest on. First, an internal-consistency coefficient computed over rubric elements contains no scorer facet. Holding one judge's measured error rate fixed at $4.72\%$, KR-20 still ranges from $0.01$ to $0.68$ as the item bank is redesigned around it, and varying judge error moves the coefficient by a comparable amount, so item design and judge error are not separately identified and no single value can be read as a property of the judge. Second, the dependability index $\Phi(\lambda)$ is a ratio of variance components, and the classification probability with which it is sometimes identified differs from it by $0.25$-$0.43$ on our bank and by $0.17$-$0.30$ on simulated data where the underlying model holds exactly. Third, Livingston-Lewis accuracy is indexed to an examinee's own true score on the same instrument, so scoring it against external gold conflates judge unreliability with criterion invalidity. Reviewing the three closest judge-evaluation papers, we found no published instance of these errors, which makes the caution prospective. A coefficient that cannot be attributed to the judge nonetheless travels downstream into deployment decisions and disclosure documents. We therefore close with four reporting lines that keep the attribution attached to the number.

---


### 141. [Decoupling Knowledge and Privacy: Post-Task Self-Distillation Replay for LLM Continual Learning](https://arxiv.org/abs/2609.29711)

**<font color=#1a73e8>作者：</font>** Shengtao Wen, Yunying Yang, Xiang Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Privacy-preserving continual learning (PPCL) must reduce the reproduction of sensitive content while retaining useful knowledge across sequential tasks. Formal privacy guarantees characterize randomized mechanisms, whereas operational output control concerns whether a trained model selectively reduces the likelihood of sensitive content in its outputs. In this work, we investigate the latter together with continual-learning utility under realistic task evolution. Retention and privacy correction operate at different granularities: task acquisition requires broad preservation of current- and old-task behavior, whereas privacy correction targets sparse annotated positions. Joint optimization leaves the current-task preservation target continually changing. We propose SPARK, a retention-correction decomposition that first freezes the learned post-task distribution and then applies selective correction around this stable reference. Self-Distillation Replay learns the current task while distilling behavior from previous tasks, and Post-Task Privacy Correction reduces annotated-PII likelihood while anchoring current- and old-task non-PII behavior to the resulting checkpoint. Extensive evaluations demonstrate that SPARK achieves effective selective PII suppression while preserving strong continual-learning utility and knowledge retention across diverse settings. Code and data will be released upon publication.

---


### 142. [PPTBench: Can Coding Agents Reconstruct the Visual World through Structured, Editable Slides](https://arxiv.org/abs/2609.29718)

**<font color=#1a73e8>作者：</font>** Xiaoqiu Wang, Yizhe Chi, Wenyi Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Coding agents are beginning to act in the visual world. They now build webpages, GUIs, games, 3D scenes, diagrams, and documents. Success in such visual coding requires bridging two spaces: inferring visual structure and expressing it programmatically. Slides are a core medium of knowledge work, widely used to communicate ideas and collaborate in a form that people can directly inspect and edit. Therefore, they provide an ideal testbed for visual coding, as they require agents to recover visual structure and realize it as editable objects. However, existing benchmarks either rely on subjective open-ended evaluation, produce non-editable code outputs, or focus only on local editing rather than end-to-end visual reconstruction. We introduce PPTBench, which benchmarks visual coding through editable slide reconstruction. It contains 500 tasks, each based on a scientific flow diagram from a real arXiv paper and requiring agents to reconstruct it as a single PPTX page composed of native, editable objects. A four-stage Agentic Judge evaluates artifact validity, semantic correctness, rendering quality, and fine-grained visual quality. Across 31 configurations spanning model families, effort levels, and harnesses, the best configuration, Kimi K3, reaches only 67.80, while the median scores 19.47. We find that agents can reliably produce valid PPTX files but still struggle with semantic and visual correctness, especially text details. More reasoning mainly helps agents pass hard gates, while stronger verification is more consistently associated with higher quality. PPTBench advances the vision of coding agents that can understand and reconstruct the visual world through structured, editable code.

---


### 143. [The Gold in Bias: Maturing the AI Design Process through Verification](https://arxiv.org/abs/2609.29730)

**<font color=#1a73e8>作者：</font>** Samira Maghool, Paolo Ceravolo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bias in AI systems is typically framed as a flaw to be minimized, yet it also serves as a critical indicator of underlying weaknesses in data, modeling assumptions, and system design. Existing approaches often treat bias as an isolated problem rather than as evidence that can strengthen verification and governance across the AI lifecycle. This paper aims to reconceptualize bias as a diagnostic tool that supports rigorous AI verification. We seek to develop a multidimensional framework to analyze bias, demonstrate how biases emerge in both Traditional and Generative AI, and provide a structured pathway for verification-driven mitigation. We present a multidimensional framework analyzing bias across four dimensions: origin sources, emergence points throughout the AI modeling lifecycle, technical and methodological causes, and validation approaches for detection and mitigation. Through a comprehensive typology spanning traditional and generative AI systems, we demonstrate how biases manifest and propagate across development stages. Our analysis encompasses 30 distinct bias types, 16 verification methods, and 20 countermeasures, providing an actionable roadmap for practitioners. We introduce a hierarchical evidence framework that distinguishes internal validity (mechanistic integrity of AI systems) from external validity (contextual reliability in deployment environments). The framework reveals how biases manifest and propagate across modeling stages, enabling systematic mapping between bias types, verification techniques, and effective countermeasures. The proposed evidence hierarchy clarifies how different verification strategies contribute to mechanistic integrity and contextual reliability. We advocate for ''Ethics by Design'' principles that integrate bias verification throughout the development lifecycle, enabling the construction of fairer, more robust, and trustworthy AI systems.

---


### 144. [TTLab at StanceEval-2026: A Cloze-Style Prompting Approach for Arabic-Language Stance Detection (CLASP-Ar)](https://arxiv.org/abs/2609.29733)

**<font color=#1a73e8>作者：</font>** Bhuvanesh Verma, Ali Abusaleh, Alexander Mehler  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Arabic-language stance detection remains challenging, and previous shared-task systems have largely relied on multitask learning and ensembles. While these systems achieve state-of-the-art performance, their applicability and transferability are limited by the additional complexity introduced by multitask this http URL reduce this complexity, we introduce $\texttt{CLASP-Ar}$, which reformulates the task as cloze-style masked language modeling. In this approach, the target, predicted sentiment, and text are combined into a single prompt whose $\texttt{[MASK]}$ prediction is restricted to a verbalizer-constrained label vocabulary.

---


### 145. [OllamaDrama: Designing and Deploying a Honeypot to Measure Attacks on Exposed LLM Infrastructure](https://arxiv.org/abs/2609.29757)

**<font color=#1a73e8>作者：</font>** Karina Elzer, Niklas Netterstrøm Johansen, Emmanouil Vasilomanolakis  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Publicly exposed large language model (LLM) infrastructure creates a growing attack surface, yet real-world targeting remains poorly understood. We present Ollure, a low- and medium-interaction honeypot that emulates the Ollama API without a backend LLM. Spanning four deployments across cloud and university networks, Ollure operated for 84 days and recorded 290,887 interactions from 2,793 unique source IP addresses. Most of the activity consisted of automated discovery, fingerprinting, and model enumeration. However, we also observed concrete exploitation attempts against both the infrastructure and LLM layers. These included model management abuse, path traversal and SSRF probes, RCE and cryptocurrency mining payloads, resource exhaustion attempts, prompt injection, information extraction, and agent-oriented tool use. Our results provide empirical insight into real-world threats against exposed, self-hosted LLM services.

---


### 146. [JEV vs. LLMs as Rubric Judges: Cheaper, Faster, and Wrong in the Same Places](https://arxiv.org/abs/2609.29769)

**<font color=#1a73e8>作者：</font>** Delip Rao, Chris Callison-Burch  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We ask whether Jev, a typed classifier that returns probabilities over permitted answers without generating text, can replace an LLM rubric judge. We compare it with three flash-tier LLM judges on nine panels drawn from seven benchmarks, giving every judge identical criterion texts. Jev's accuracy differs significantly from an LLM judge's in only 8 of 27 paired comparisons, ahead mostly on binary criteria and behind only on graded ones, and most of the other comparisons are inconclusive. Summed over the nine panels, the LLM judges, called once per criterion, cost 29 to 325 times as much as Jev and took 30 to 220 times as long. On graded criteria all four judges agree more with one another than with the labels and mostly assign lower levels than the raters. One of several observational accounts is that raters followed scale conventions our criterion texts omit. Jev's confidence ranks its own errors on most panels, which should make a cheap classifier the ideal first stage of a cascade that defers its uncertain verdicts to an LLM judge. Correlated errors undo that advantage. The LLM judges repeat nearly all of Jev's most confident errors, so a cascade replayed on the recorded verdicts lowers cost but gains at most 1.5 points over the best single judge with cross-fitted thresholds, and at most 2.0 even with oracle thresholds.

---


### 147. [Breaking the Environment Wall: Evolving LLM Agent Environments for Recursive Self-Improvement](https://arxiv.org/abs/2609.29773)

**<font color=#1a73e8>作者：</font>** Yukai Wu, Yuanjing Yang, Le Zhou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many real-world tasks (e.g., office workflows, scientific experimentation) require LLM agents to interact repeatedly with their environments for context-dependent operations. However, such environments are often not agent-ready. First, information is often scattered and fragmented across the environment. Second, relevant evidence in the environment is often mixed with misleading information and conflicting versions. Third, environments evolve over time, introducing new noise and more challenging tasks. These challenges can substantially degrade performance for state-of-the-art AI agents (e.g., from 83.9% to 57.6%). To address these challenges, we propose Env-Rethink (a system with 27B post-trained model) that supports three main capabilities: (1) It adaptively builds Collection Maps (for organizing related files) and Event Logs (for contextualizing cross-data relationships) to supplement necessary context; (2) It further leverages the post-trained model (through offline trajectory learning) to identify underlying noise issues in the environment; (3) It ultimately evolves environments through virtual event histories that alter environmental states and evidence relationships, producing more tricky ones for further agent improvement. Experiments show that Env-Rethink can effectively improve downstream task performance (with over 15.1% rubric pass rate improvement across nine models on 30 tasks).

---


### 148. [Hallucination Neurons and Where to Find Them: An Investigation into the existence of Hallucination Neurons](https://arxiv.org/abs/2609.29781)

**<font color=#1a73e8>作者：</font>** Huseyin Cavus, Sebin Sabu, Joshua Spear 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interpretable machine learning for Large Language Models (LLMs) increasingly relies on sparse probing methods that identify small sets of neurons claimed to detect and causally influence behaviors such as factuality recall, safety alignment, and hallucination. These claims have important implications for model auditing and behavioral steering, yet they are rarely tested against known failure modes of $L_1$-regularized probing in correlated, high-dimensional feature spaces. We propose a five-step diagnostic protocol covering feature correlation, bootstrap stability, sparse versus dense ranking disagreement, intervention baselines, and cross-dataset evaluation as a minimum standard for sparse-neuron localization claims. We investigate prior work using our proposed approach, specifically on H-neurons using open-source LLMs across TriviaQA, BioASQ, and NQ-Open datasets. Our results demonstrate detection replicates across both models and datasets, and exceeds the original reported AUROC gaps for TriviaQA and BioASQ datasets. Gemma 3 4B consistently outperforms MedGemma 4B on matched datasets, with AUROC gaps of +0.311 versus +0.235 on TriviaQA, +0.474 versus +0.455 on BioASQ, and +0.128 versus +0.112 on NQ-Open respectively. Causal validation at $n = 500$ with five random seeds shows statistically significant effects beyond random same-layer baselines. At the same time, the diagnostic results indicate that the selected neurons are not uniquely localized. Across the three Gemma 3 4B settings, 19 of 22 selected H-Neurons have Pearson $|r| > 0.7$ with other features, bootstrap selections show only moderate stability, and sparse and dense rankings overlap only weakly. Our findings show that sparse predictive structure can coexist with non-unique neuron selection. Routine diagnostic validation is necessary to distinguish detection claims from localization claims in mechanistic interpretability.

---


### 149. [TimeBraid: Unifying Time Series and Language for Understanding and Forecasting](https://arxiv.org/abs/2609.29792)

**<font color=#1a73e8>作者：</font>** Xinyue Wang, Jiacheng Pang, Kun Zhou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present TimeBraid, a series of unified time-series and language models that align pretrained language models and pretrained time-series foundation models through interleaved global residual attention layers. Each model inherits knowledge, instruction following, and reasoning from one side, continuous-signal perception and zero-shot forecasting from the other, and fuses the two in a shared representation space where both modalities are understood and generated. We study the design choices that make such unified modeling work: where to align the two representation spaces, how to ground language in temporal structure, how to balance understanding with generation, and how to keep joint optimization stable. The resulting recipe combines a unified prompting scheme for diverse time-series and text tasks, stabilized joint training, and supervision from 2.2M curated series--text pairs and 4.9M instruction-tuning samples. Across benchmarks spanning time-series perception, understanding, reasoning, and both context-aided and unimodal forecasting, TimeBraid remains competitive with far larger general-purpose models and task-specific counterparts.

---


### 150. [Benchmarking and Domain Adaptation of Automatic Speech Recognition (ASR) for Adolescent Health Communication in Ghanaian Languages](https://arxiv.org/abs/2609.29798)

**<font color=#1a73e8>作者：</font>** Stephen E. Moore, Akwasi Asare, Mich-Seth Owusu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents an end-to-end study of automatic speech recognition (ASR) for adolescent health communication in three Ghanaian languages (Twi, Dagbani, and Ewe). The work proceeds in three connected stages; First, we benchmark five ASR systems (three language-specific Wav2Vec2 models and two multimodal LLMs, Gemma 3n and Gemma 4) on a general-domain Bible corpus and a Youth Adolescent Sexual and Reproductive Health (ASRH) Domain ASR dataset, using Character and Word Error Rate (CER, WER). Second, guided by the benchmark, we perform supervised domain adaptation: although Gemma 4 was the strongest zero-shot candidate, fine-tuning it proved computationally infeasible, so we pivoted to the compact Qwen3-ASR-0.6B, fine-tuned on a large Ghana Bible corpus (~90k samples) and evaluated strictly on held-out human-collected in-domain audio. Fine-tuning reduced WER on every language, most dramatically for Ewe (WER from 109.3% to 64.8%, a drop of 44.5 pp; CER from 65.1% to 24.9%). Third, we validate the work through KasaHealth, a live voice-first ASRH application deployed in all three languages, complemented by Senti-Check, a technical evaluation harness. KasaHealth was tested by 50 community respondents and achieved a 100% chat-approval rate, a 72% Good-or-Excellent translation rating, and a 92% would-recommend rate, while surfacing the domain gaps that most constrain real-world use. Across all three stages the evidence converges: for these languages the binding constraint is validated in-domain data, not model capability or computation.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-228](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
