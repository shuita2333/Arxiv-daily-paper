# 🧠 大模型相关研究 | 2026年09月02日

> 本类共 **452** 篇论文：已确认 **431** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**401-450**（第 9/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-452](./part-10.md)

---

### 401. [CogEvol: Towards Efficient and Reliable Learning Environment Generation](https://arxiv.org/abs/2608.30968)

**<font color=#1a73e8>作者：</font>** Shangqing Tu, Daniel Zhang-Li, Yucheng Wang 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present CogEvol, a family of models trained specifically for Learning Environment Generation: turning a course brief into a finished learning artifact (structured-JSON slides or self-contained interactive HTML pages) in a single pass. Across 220k production requests, CogEvol completes a slide in a median of 17 seconds and an interactive page in 59, replacing minutes-long multi-turn agent scaffolding. Reliability is enforced rather than hoped for: a production-grounded data pipeline turns real failures into 53,687 verified SFT samples, and a hybrid rule-plus-VLM reward drives GRPO-based RL, hardened after we caught and fixed a reward-hacking episode that produced visually convincing but unplayable games. CogEvol-27B scores 83.7 on slide quality and 63.7 on a 500-case interactive-HTML benchmark with 26.9x fewer parameters than flagship coding models, and, in collaboration with the OpenMAIC team, serves their live production traffic. CogEvol-4B is released openly under the Apache 2.0 license at this https URL external flagships are measured on the same suites under the identical harness. Scaffold editing cuts interactive-page generation cost by a further ~76%, and the full stack runs on domestic Ascend accelerators at application-level parity with A800 GPUs, lowering the unit cost of AI-native education at scale.

---


### 402. [A Human-in-the-Loop Autonomous Agent for Industry Time Series Forecasting](https://arxiv.org/abs/2608.30976)

**<font color=#1a73e8>作者：</font>** Xiaoyu Tao, Mingyue Cheng, Ze Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world time-series forecasting is rarely a one-shot model invocation: practitioners must formulate tasks, connect data and models, incorporate domain expertise, assess prediction plausibility, and communicate uncertainty. Specialized forecasting models provide strong numerical predictions but usually operate in fixed pipelines, while general-purpose large language model (LLM) agents often lack forecasting-specific checks, constraints, and stopping rules. We present CastClaw, a human-in-the-loop autonomous forecasting system built through forecasting-oriented harness engineering. CastClaw connects data, specialized models, analytical tools, user input, and a versioned execution record in one runtime. Users specify the target, horizon, constraints, and hypotheses in natural language. Starting from a supplied or model-generated forecast, CastClaw checks temporal patterns and user constraints; when evidence is missing, it retrieves context, runs an analysis or another model, or asks the user. It then keeps, revises, or escalates the result under explicit stopping conditions. The output contains the final forecast and an execution report recording inputs, evidence, actions, and revisions. In this five-dataset electricity-price setting, CastClaw reports the lowest point-estimate MSE and MAE among 16 baselines. A Nord Pool case demonstrates the inspectable workflow. CastClaw was also validated offline on provincial electricity-load data from North China covering January--June 2026.

---


### 403. [Evaluating and Improving LLM Self-Modeling](https://arxiv.org/abs/2608.30980)

**<font color=#1a73e8>作者：</font>** Siqi Zeng, Andre N. Assis, Rowan Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study self-modeling: an LLM's ability to answer questions about its own behavior. We focus on verifiable behavioral questions, such as whether a prompt edit would change the model's final answer. To measure this capability, we introduce a benchmark that tests diverse types of self-modeling questions. Current models show non-trivial but limited self-modeling skill, and make systematic mistakes on simple counterfactual questions about their own behavior. To improve self-modeling skill, we develop a scalable synthetic-data pipeline that produces self-modeling training data, and show that reinforcement-learning can improve aggregate self-modeling skill across three open-source model families with some transfer to held-out tasks. These gains, however, do not seem to constitute introspection consistently: improved self-modeling may not arise from privileged access to the model's internal decision process.

---


### 404. [Controlling Refusal Behavior of LLMs via Stiefel-Constrained Rotation Steering](https://arxiv.org/abs/2608.30986)

**<font color=#1a73e8>作者：</font>** Kirill Bunin, Dmitry Bylinkin, Vladimir Aletov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering has emerged as a lightweight approach for controlling model refusal at inference time. A growing line of research explores trainable rotations of activations to develop geometrically principled intervention mechanisms. However, existing techniques rely on auxiliary constructs, such as refusal vectors, to define these rotations. In our work, we develop a self-contained methodology for learning parameter-efficient rotational transformations based on Riemannian optimization. We empirically validate the proposed scheme, demonstrating its superiority in intervention efficiency. An extensive ablation study highlights the importance of key design choices in our method. Our results identify the proposed rotation-based steering scheme as a promising direction for more reliable control over the behavior of LLMs.

---


### 405. [Stick to What You Know: A Study of Knowledge-Aligned Supervised Fine-Tuning](https://arxiv.org/abs/2608.30987)

**<font color=#1a73e8>作者：</font>** Arthur Becker, Jakob Kemmler, David Thulke 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) trains a base language model to imitate target responses, and these targets may require knowledge the base model has not robustly internalized. We study this as a source of hallucinations and frame a group of mitigation methods as \emph{knowledge-aligned SFT}: constraining SFT training targets to the base model's parametric knowledge. Under a unified setup, we compare existing generation-based and estimation-based knowledge-alignment methods and introduce two new variants: Evidence Rewrite, which verifies base-model generations using external evidence, and Recall Rewrite, which retains claims only when they can be consistently recalled by the base model. Experiments with Qwen 3 4B and OLMo 3 7B show that knowledge-aligned SFT can reduce factual hallucinations on WildHalu and Biography while largely preserving general capabilities. Recall Rewrite yields the strongest factuality gains and improves refusal behavior on UnknownBench. It thereby confirms that SFT targets beyond the base model's knowledge drive hallucination behavior.

---


### 406. [Faithfulness Is Not Free: Auditing Offline KV-Cache Quantization in Retrieval-Augmented Generation](https://arxiv.org/abs/2608.30996)

**<font color=#1a73e8>作者：</font>** Atta Ul Asad, Ahsan Bilal, Muhammad Ali 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation systems can precompute and store key-value caches of retrieved documents to avoid re-encoding context at every query. Quantizing these caches further reduces storage, but no prior work asks whether compression damages faithfulness, whether responses remain grounded in the retrieved evidence. Faithfulness and accuracy are not equivalent: a model can produce a correct answer that is no longer supported by the context it was given. We evaluate Qwen2.5-7B-Instruct under INT8 and INT4 quantization on RGB and HotpotQA, measuring both accuracy and faithfulness with a hallucination detector, NLI entailment, and an LLM judge. INT8 is near-lossless across both metrics. INT4 reduces accuracy and, more critically, even among answers that remain factually correct, over 90% of faithfulness changes are negative, i.e., accuracy metrics are blind to this regression. The harm grows under noisy retrieval and with more retrieved chunks. Faithfulness must be audited before compressed caches are deployed.

---


### 407. [Multi-View Reflective Surface Inspection via Semantic-Saliency Cross-Verification](https://arxiv.org/abs/2608.30997)

**<font color=#1a73e8>作者：</font>** Van-Giang Nguyen, Thanh-Tuan Tran, Xuan-Hieu Phan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reflective smartphone cover glass is challenging to inspect from a single fixed viewpoint because defect visibility varies with viewing geometry and specular reflections. This gives rise to two practical challenges: defects may be weakly observable from certain viewpoints, while the available visual evidence may remain spatially ambiguous. To address these issues, we propose a multi-view inspection framework in which each RGB observation is processed by a shared per-view expert. A vision-language model (VLM) produces class-aware semantic boxes, while a normal-reference reconstruction branch provides class-agnostic saliency. Their spatial agreement is used as supporting evidence to rank semantic proposals without modifying their coordinates or treating saliency as ground truth. The resulting evidence records are combined at product level without cross-view registration. On 282 production-line images, semantic-saliency association improves $AP_{50}$ from 52.6% to 62.6% by re-ranking fixed semantic proposals. Across 94 products, cross-view evidence recall $R_{\rm prod}@0.5$ increases from 75.5% for the best single view to 88.3% using all three views. These results support the complementary roles of semantic-saliency cross-verification and additional optical observations in reflective-surface inspection.

---


### 408. [Evidence-Bounded Mental Health Reasoning from Heterogeneous Speech Protocols](https://arxiv.org/abs/2608.31014)

**<font color=#1a73e8>作者：</font>** Chengyuan Gao, Jiang Wu, Tao Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computational mental health screening using multimodal speech and text has shown great promise. However, existing models often assume all clinical speech protocols carry equivalent evidentiary validity. In reality, heterogeneous protocols, from free interviews to fixed reading tasks, support fundamentally different evidence. Forcing uniform reasoning flattens these boundaries, causing models to hallucinate symptoms from irrelevant text or overclaim support. Even advanced long chain-of-thought LLMs fail to resolve this issue, as free-form reasoning can exacerbate boundary violations. To address this, we reformulate multimodal screening as an evidence-bounded reasoning problem. We introduce the Evidence Package Benchmark, integrating 1,870 packages across six heterogeneous sources with explicit modality masks and evidence permissions. We further propose EviBound, a protocol-aware evidence control framework. Unlike direct LLM prompting, EviBound uses a profile-aware planner to restrict reasoning scope, orchestrates evidence tools via five-way acoustic consensus, and enforces a boundary critic to suppress unsupported claims. Empirical results show EviBound achieves a held-out test Depression AUROC of 0.8658, exceeding the strongest direct omni-modal baseline by +0.0811 AUROC while maintaining zero claim violations. Our work moves beyond unconstrained accuracy toward evidence-consistent, protocol-aware systems for safer clinical NLP research.

---


### 409. [LLM Judges Verify Presence, Not Absence: Omission Blindness in AI Clinical Notes and What Recovers It](https://arxiv.org/abs/2608.31016)

**<font color=#1a73e8>作者：</font>** Sebastian Fox, Luke Markham, Ryan Lail 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ambient AI scribes draft clinical notes, and published audits find their dominant error is omission: information the encounter established that the note fails to record. The standard check is an LLM judge: a second model reads the note against the transcript and flags problems. We ask whether judges detect omissions. Public corpora cannot supply the answer key: their clinician reference notes and transcripts are materially discrepant. Our benchmark has 500 single-error note pairs from audited fact sheets, 298 with a named fact certainly absent and 202 added-or-altered controls. Across eight judge designs, paired discrimination (the flawed note below its clean twin, 0.5 a coin flip) reads 0.79-0.94 on added or altered content and 0.50-0.63 on omissions. On single notes, no design flags omissions reliably more often than perfect notes. Wording changes, voting and GEPA prompt optimisation move the operating point without creating usable detection. Restructuring the task recovers it: list the facts the transcript establishes, then check the note for each. Two methods reach it independently and trade off: a per-fact pipeline, and a GEPA-evolved prompt doing the same in one call. The pipeline's flags name the missing fact and its severity at 2.7% false alarms. The single call detects more (36.9% against 24.6%, p=0.002) at 6.2% false alarms and a tenth of the cost per note. A physician author validated 70 items and, where the two routes disagree, sided with the pipeline on 10 of 10 (p=0.002). A second clinician, not an author, graded the severity rubric blind and agrees to within a grade. On real vendor notes from a companion census no benchmark threshold transfers, but the re-calibrated single call detects more than the best of the eight at half its false-alarm rate. Omissions whose fact is restated elsewhere defeat both routes. We release the benchmark, prompts and judgements.

---


### 410. [When Does Predictor-Based RL Align with Human Perception? A Study of Subjective Rewards in Codec-Based Speech Language Models](https://arxiv.org/abs/2608.31035)

**<font color=#1a73e8>作者：</font>** Joonyong Park, Jerry Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Codec-based text-to-speech (TTS) models make language-model post-training applicable to speech generation, but it remains unclear when learned perceptual predictors can serve as reinforcement learning rewards without losing alignment with human listeners. We study this question with Group Relative Policy Optimization (GRPO) using learned rewards for anime-like speaking style, naturalness, likability, and arousal. To prevent perceptual rewards from being optimized through transcript drift, we introduce a character error rate (CER) zone constraint and compare policy optimization with Best-of-$N$ reranking under the same reward gate. Across single-reward runs, each reward primarily improves its own target metric, showing that subjective predictors are not interchangeable quality surrogates. Multi-rater A/B tests further show uneven human transfer, while a reward-gap analysis separates average transfer from within-axis calibration: signed reward gaps significantly predict listener choices in the pooled analysis, whereas residual CER gaps do not, but per-axis calibration remains heterogeneous. Best-of-8 is a strong human-level baseline and is not clearly worse than GRPO perceptually, suggesting that GRPO should be viewed as amortizing reward-selected behavior into the policy rather than uniformly outperforming reranking. These results support analyzing subjective speech rewards as predictor-axis-base tuples and provide practical diagnostics for selecting rewards before multi-reward speech post-training.

---


### 411. [Does On-Policy Distillation Really Distill? From Noisy Teacher to Self-Improvement](https://arxiv.org/abs/2608.31046)

**<font color=#1a73e8>作者：</font>** Yi Ding, Ruqi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) offers dense token-level supervision as an alternative to the sparse outcome-level advantages of reinforcement learning with verifiable rewards (RLVR). However, the teacher scores student-generated trajectories that are inherently off-policy for it, so the reliability of its supervision, and hence the source of the student's improvement, remains unclear. We quantitatively analyze teacher supervision during OPD training and find substantial noise whose prevalence increases with teacher scale. Surprisingly, the student policy is insensitive to such noise, converging to comparable performance regardless of whether noisy supervision is retained or removed. Does OPD distill at all? By analyzing what drives its gains, we find that learning concentrates on low log-probability tokens, and using a single fixed negative advantage matches the performance of teacher-provided ones. This suggests that OPD works largely by suppressing low log-probability tokens, which requires no teacher. These findings motivate On-Policy Self-Adaptation (OPSA), a supervision-free method using entropy-adaptive negative advantages. It assigns stronger learning signals to high-entropy positions, suppressing tail tokens, and evenly redistributing probability mass among head tokens. Compared with the base \texttt{Qwen3-1.7B}, OPSA improves Avg@32 by 35.41 points on AIME24, corresponding to a 263\% relative gain, and more than doubles Pass@32 across all three benchmarks. It also outperforms OPD by 16.77 points in Avg@32 on AIME24. Extensive experiments and analyses across model families and tasks further demonstrate its effectiveness and generalizability.

---


### 412. [Measure Before You Manage: Evaluating Agent Working Memory in Coding Agents](https://arxiv.org/abs/2608.31057)

**<font color=#1a73e8>作者：</font>** Le Chen, Zishen Wan, Baixi Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent working memory is heterogeneous. Objects such as instructions, artifacts, tool outputs, and agent-generated state play different semantic roles and exhibit different size, retention, and representation profiles. Recent work has begun to explore memory-management mechanisms that account for such heterogeneity. This work focuses on semantic heterogeneity and studies how it should shape the management and evaluation of working memory in coding agents. Across 55 archived coding-agent trajectories, we find that semantically different working-memory objects exhibit distinct retention and compression behavior. This heterogeneity motivates semantically informed memory management. We study two semantically informed strategies: an object-aware compression policy and a retrieval-based policy. Their evaluation shows that calibration gains may not transfer to held-out tasks, and that equal token budgets do not imply equal delivered context or management cost. A real-system replay further exposes serving limits that nominal budgets alone do not capture. Together, these results show why semantic structure matters for agent working memory and why evaluating memory-management strategies requires more than a nominal token budget. We organize these lessons into four levels: stored state, delivered context, management work, and task or process outcome.

---


### 413. [Improving Information Extraction with Learned Queries](https://arxiv.org/abs/2608.31058)

**<font color=#1a73e8>作者：</font>** Omar Sharif, Soroush Vosoughi, Nikhil Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When information extraction fails, a natural instinct is to improve the model doing it: for example, by scaling it up or refining its reasoning. In this paper, we show that another part of the pipeline matters at least as much: the queries used to elicit this information. Across four clinical benchmarks and five LLMs, improving the question design alone raises performance by 18.6 F1-score points, i.e. more than using larger extraction models. To make such question design learnable, we introduce List of Questions (LoQ), which generates document-specific question sets, and FeedQ, a feedback-driven optimization method that iteratively refines questions against extraction outcomes. The resulting optimized questions can be used to train lightweight generators: with fine-tuning, 4B-parameter models match or outperform expert-derived baselines and substantially exceed the performance of much larger untuned models. We release a dataset of 12,820 optimized questions to support a broader shift in information extraction research toward treating question design as a first-class problem.

---


### 414. [Every Token Leaves a Ripple in the Stream of Thought: Eliciting Model-Internal Token Saliency for Chain-of-Thought Compression](https://arxiv.org/abs/2608.31066)

**<font color=#1a73e8>作者：</font>** Tianyi Zhao, Yinhan He, Wendy Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning improves multi-step problem solving, but long reasoning traces inflate inference cost. Token-level CoT compression reduces this cost by pruning full reasoning chains into shorter traces for model adaptation, making token selection the central challenge. Existing methods often rely on external scorers or heuristic signals only indirectly tied to the model's internal answer computation. We instead adopt a model-internal perspective: as the model forms an answer, each reasoning token leaves a ripple in the residual stream, the model's \emph{stream of thought}, and the magnitude of this ripple reflects the token's contribution to the answer computation. Building on this view, we propose \textsc{MIST} (Model-Internal Saliency for Token-level CoT compression), which defines token importance along two complementary axes: \emph{necessity}, the drop in answer likelihood when a token's internal contribution is removed, and \emph{sufficiency}, the gain in answer likelihood when that contribution alone is provided. Combining the two yields a unified importance score for pruning. Across four reasoning benchmarks and four models, \textsc{MIST} consistently outperforms baseline methods, suggesting that model-internal saliency provides an effective proxy for reasoning-token importance.

---


### 415. [Wrong Prediction, Right Answer: Recovering Evidence from Collapsed LLM Sequence Scores](https://arxiv.org/abs/2608.31068)

**<font color=#1a73e8>作者：</font>** Qiyao Yan, Chenpeng Wang, Liangming Pan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a large language model fails a reasoning task, it is often assumed to lack the underlying capability. However, this conflates a genuine absence of reasoning with a late-stage output bottleneck. We observe a consistent readout gap across diverse reasoning benchmarks: hidden-state probes successfully decode correct answers even when native sequence scoring completely collapses due to structural biases. To test whether instance-specific logic survives this collapse, we introduce a diagnostic protocol using a minimal, target-label-free additive correction. Fitting just two parameters on as few as 25 unlabeled examples recovers 9--34 accuracy points for Qwen3.5 models, transferring successfully to OLMo-2-1B and Llama-3.1-8B. Crucially, these recovered decisions persist on hard instances unresolved by simple lexical overlap and significantly exceed count-preserving permutation baselines. Our results show that many apparent zero-shot reasoning deficits are expression failures masking intact internal logic, urging a narrower interpretation of benchmark evaluations.

---


### 416. [A Model with No Head and Many Thoughts](https://arxiv.org/abs/2608.31069)

**<font color=#1a73e8>作者：</font>** Nikita Koriagin, Yaroslav Aksenov, George Bredis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models decode by projecting hidden states through a large vocabulary head at every step. This operation is computationally costly and forces all reasoning to be expressed in discrete tokens. We introduce Soft Latent Thinking, a method that replaces the LM head during reasoning with a lightweight projector, enabling autoregressive rollout in embedding space where reasoning steps remain continuous rather than tokenized. Experiments on DeepSeek-Qwen-1.5B and LLaMA-3.2-3B show that Soft Latent Thinking consistently improves pass@k across all k while reducing per-step compute during chain-of-thought. Our method achieves the highest pass@32 among all soft-thinking approaches, demonstrating that effective reasoning can be carried out in continuous space without discrete token generation.

---


### 417. [Scaling Large Reasoning Models beyond Human Supervision: A Path toward Superintelligence](https://arxiv.org/abs/2608.31075)

**<font color=#1a73e8>作者：</font>** Zhiqin Yang, Jingwen Fu, Yuhan Liu 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large reasoning models (LRMs) have shown that reinforcement learning with verifiable rewards (RLVR) can substantially improve reasoning in mathematics and code, where outcomes can be checked automatically. Extending this progress to open-ended and agentic tasks remains difficult because reliable rewards are harder to obtain and direct human supervision cannot keep pace with the scale and complexity of model-generated experience. This paper studies how LRMs can continue to improve as human supervision gradually recedes from the learning loop. We examine two connected dimensions of this problem. The reward axis traces the development from per-instance human judgments to reusable verifiers and rewards that operate even without human feedback. The experience axis examines how learning can progress from human-curated tasks and environments toward self-generated curricula, constructed environments, and autonomous co-evolution. We connect these dimensions through a five-level ladder from L0 to L4 that identifies which parts of the learning process remain under continued human control. Our analysis further highlights the risks introduced by increasingly autonomous rewards and experience generation, including reward hacking, feedback drift, curriculum collapse, and environment errors. Consequently, we also provide the evaluation around three complementary objects: policy capability, feedback fidelity, and experience quality. This analysis provides a structured account of current approaches to scaling LRMs beyond human supervision and the open problems involved in developing self-sustaining learning systems toward superintelligence. Furthermore, we maintain a continuously updated \href{this https URL}{GitHub repository} to track the latest advances.

---


### 418. [Learning to Evaluate Before Improving: Automatic Rubric Induction for Automatic Research Agents](https://arxiv.org/abs/2608.31076)

**<font color=#1a73e8>作者：</font>** Xuehai Wang, Haowei Qin, Tongxin Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autonomous scientific research agents are increasingly applied to end-to-end scientific workflows, including literature review, data analysis, experimentation, and report generation. However, open-ended research tasks often do not clearly specify the analyses, methods, and success criteria required to complete the task. As a result, agents may miss important analyses, use inappropriate methods, or draw conclusions that are insufficiently supported by evidence. To address the problem, we present AutoSciRub, an evaluation-first framework that induces a task-specific executable rubric before research execution, and uses it to guide execution, criterion-level verification as well as iterative revision. AutoSciRub decomposes an underspecified instruction into atomic scientific goals, grounds them in relevant literature and task-visible data, and synthesizes specific, actionable, and verifiable criteria. The resulting rubric makes implicit experimental and evidential requirements explicit, providing guidance for experiments and analyses. During revision, rubric-guided verification identifies unmet criteria and enables targeted refinement of the research report and its supporting artifacts. On ResearchClawBench, AutoSciRub consistently improves all tested configurations, with an average gain of 2.08 points across three backbone LLMs under the fixed Codex harness and 2.95 points across three agent harnesses using a fixed DeepSeek-V4-Flash backbone. On a randomly sampled 20-task subset of AstaBench E2E Discovery, AutoSciRub further achieves an average improvement of 16.8 points across three agent harnesses, while maintaining or increasing the number of successfully completed tasks. These results demonstrate that evaluation-first guidance provides an effective and generalizable control mechanism for autonomous scientific research (Code: this https URL).

---


### 419. [Reconciling Process Supervision with Outcome-Based Credit in Agentic Policy Optimization](https://arxiv.org/abs/2608.31077)

**<font color=#1a73e8>作者：</font>** Jingxiao Yang, Wangjie Gan, Yingxuan Zhuang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Outcome-based reinforcement learning provides verified feedback for language-model agents, but assigns trajectory-level advantage uniformly to all decisions, yielding coarse credit over long-horizon interactions. On-policy self-distillation offers finer supervision by re-evaluating sampled behavior with privileged information (PI) available only during training. However, fine-grained supervision is not necessarily fine-grained credit: PI-induced likelihood changes describe how additional information alters policy preference, but do not directly determine how an executable action should inherit the verified task outcome. This creates a supervision-credit gap. Privileged signals may be irrelevant to the current interaction state, operate at a token granularity misaligned with executable decisions, and lack the outcome semantics required for reinforcement. We introduce TASPO, which converts privileged supervision into outcome-grounded action credit. TASPO constructs decision-applicable PI from verified successful experience, aggregates PI-induced likelihood shifts at the executable-action level, and converts relative action support into positive, bounded, mean-preserving weights on the original trajectory advantage. Thus, the verified outcome determines the update direction and average scale, while PI only redistributes credit across actions. Across three agentic benchmarks, TASPO improves over GRPO by 10.6\% and generalizes better to unseen tasks. Further analysis indicates that TASPO reduces supervision mismatch and that action-level assignment stabilizes the policy optimization process. These findings offer the community another interesting perspective.

---


### 420. [Sycophantic Agreement Transfers with Neutral Data via Contrastive Preference Optimization](https://arxiv.org/abs/2608.31079)

**<font color=#1a73e8>作者：</font>** Camila Blank, Zhuofan Ying, Christopher Potts 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sycophantic agreement refers to a behavior in which language models excessively affirm the user, often at the cost of factual accuracy. Although sycophantic agreement is a well-known failure of model alignment, there is limited understanding of how it emerges from model training. In this work, we demonstrate that sycophantic agreement can emerge as an unintended consequence of widely used contrastive preference optimization objectives. Using the OLMo 3 post-training pipeline, we show that, for various pairs of teacher models across three families, there is a strong correlation between the log-ratio of the teacher model sycophantic agreement rates and the resulting student model sycophantic agreement rate. We further demonstrate that this unintended transfer is not limited to DPO but also occurs across 6 other preference optimization objectives. To understand whether this effect can be attributed to particular training examples, we analyze the preference data and find that the sycophancy signal is diffused across the entire dataset rather than concentrated in a sparse set of examples: each example appears neutral, i.e., there are no explicit instances of sycophantic agreement, and filtering based on probe-based data attribution or logit-linear selection fails to mitigate sycophancy without removing a large portion of the dataset. Overall, our findings suggest that the teacher models used to generate preference data can interact with alignment training objectives in unexpected ways, generalizing to undesirable and potentially harmful behaviors like sycophantic agreement.

---


### 421. [Token-Efficient Data Reasoning Agents via Adaptive Structuring of Unstructured Data](https://arxiv.org/abs/2608.31082)

**<font color=#1a73e8>作者：</font>** Milad Rezaei Hajidehi, Qitong Wang, Stratos Idreos  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Valuable data remains embedded in unstructured sources: web pages, reports, contracts, filings, earnings calls, and PDFs. The big bet in enterprise AI is deploying LLM agents that reason over this data to answer complex questions for every knowledge worker. Agents can do this today, but at prohibitive cost. Each question repeatedly opens large documents to recover scattered evidence, consuming up to a million tokens. However, if the data were already structured, the same question would reduce to a cheap database lookup. For example, on FanOutQA benchmark, reasoning over an ideal pre-structured store is 28X cheaper, and the gap grows to orders of magnitude as questions fan out over more documents. Yet structuring everything in advance is not viable: documents hold vastly more possible structure than any workload will use, and the useful structure and documents are unknown until queries arrive. We propose agentic data cracking, a method that structures unstructured data adaptively and speculatively as a byproduct of reasoning itself. Structuring is adaptive because observed queries decide when it happens and what matters, and speculative because it goes beyond the current question. Whenever the agent opens a document to answer, a cracking sub-agent forks from the already-loaded context at marginal cost and extracts grounded structure likely to serve related future queries. Over time, an increasing share of queries is fully covered by structured data and answered without opening a document, keeping agentic accuracy at close to RAG cost. On FanOutQA, extended with merely one related question per test question, cracking cuts cost by 53% while preserving accuracy. Agentic data cracking is a first step toward next-generation data infrastructure for agentic reasoning over unstructured data: a shared substrate beneath the model where knowledge that reasoning already paid to uncover accumulates.

---


### 422. [The First Token Is a Clue: Verbalizing Multi-Token Concepts from the J-lens](https://arxiv.org/abs/2608.31084)

**<font color=#1a73e8>作者：</font>** Xijie Gong, Tonghan Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Jacobian Lens (J-lens) is a recent tool for interpreting LLMs. It reads a hidden state as a ranked list of vocabulary tokens, leaving multi-token concepts without a representation of their own. The original J-lens work addresses this limitation with Template Lens, which precomputes vectors for a fixed phrase vocabulary, and Oracle Lens, which fine-tunes components to propose phrases and reconstruct phrase vectors. We ask whether multi-token concepts and their vectors can instead be recovered directly from J-lens and the frozen model. We find that the first token of a multi-token concept is about as readable as a single-token concept. Given the correct first token and source prompt, the frozen model recovers the second token in 88.3% of two-token cases. We show that a vector for the complete concept can be recovered from subsequent hidden states in a single forward pass. We therefore use J-lens to propose first tokens and let the frozen model complete candidate concepts. We then recover a vector for each candidate and score it alongside the complete vocabulary. Across 496 multi-hop clozes on Gemma-3-12B-IT, Llama-3.1-8B, and Qwen3-14B, our method achieves an average $\mathrm{Rank@}10$ of 43.1%, compared with 27.6% for Template Lens. Without the J-lens clue, performance drops to 21.6%, showing that the first-token clue substantially improves readout. Causal concept swaps using the recovered vectors achieve an average $\mathrm{succ}@10$ of 61.4%, compared with 26.2% for Template Lens under the same intervention. These results show that first-token clues can guide multi-token concept recovery, while subsequent hidden states provide vectors for readout and intervention.

---


### 423. [S3Gym: Can LLMs Turn Self-Testing and Self-Judging into Self-Improvement?](https://arxiv.org/abs/2608.31100)

**<font color=#1a73e8>作者：</font>** Jiajun Shi, Siyuan Tao, Yuhao Wu 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly interact with external environments and accumulate substantial behavioral experience, yet existing agent benchmarks largely evaluate them as fixed policies. It therefore remains unclear whether an agent can actively test its behavior, judge the resulting experience, and use that experience to improve future decisions. We introduce \textbf{S\textsuperscript{3}Gym}, an interactive benchmark for evaluating LLM self-improvement through three coupled capabilities: \textbf{Self-Testing}, \textbf{Self-Judging}, and \textbf{Self-Improvement}. S$^3$Gym separates permissive exploration from strict held-out evaluation and instantiates this protocol in seven text-based games with executable environment verifiers. We evaluate three pathways for incorporating interaction experience: direct History ICL, score-conditioned Summary Memory, and parameter Training.
Our experiments reveal that self-improvement is neither automatic nor uniform. Context-level experience improves performance for several model--game pairs, but the most effective pathway depends strongly on the task structure: summaries are beneficial when experience can be compressed into reusable strategic rules, yet often underperform raw history when success depends on precise, state-contingent information. Parameter training produces substantial gains on some tasks, but also exhibits unstable improvement and severe negative transfer on others. These findings show that recognizing successful actions is insufficient; agents must also transform feedback into executable and transferable policies. S$^3$Gym provides a unified framework for diagnosing this process and identifying the bottlenecks that prevent agents from translating interaction experience into reliable self-improvement.

---


### 424. [BLOOM-WILT: Logit Tilting for Behaviour Elicitation in Automated LLM Auditing](https://arxiv.org/abs/2608.31105)

**<font color=#1a73e8>作者：</font>** Adrians Skapars, Edoardo Manino  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Users of a deployed language model routinely encounter behaviours that testing almost never surfaces, since deployment puts the model through orders of magnitude more interactions than any evaluation can simulate. Automated auditors make testing cheap to scale and flexible enough to cover almost any specified behaviour, yet their lack of optimisation pressure makes them sample-inefficient. To address this shortcoming, we introduce BLOOM-WILT, a full auditing pipeline that elicits natural multi-turn instances of rare behaviours, without training cost or access beyond the target's next-token distribution. On the input side, WILT's auditor model revises its conversational strategy across rounds, learning from previous scored interactions. On the output side, WILT adaptively reweights the target's decoding using the model's own distribution conditioned on an elicitation prompt, so that behaviour-relevant generations are sampled ahead of others it finds equally probable when unprompted. We evaluate WILT across 4 target models and 8 behaviours, where it beats the baseline auditor in 30 of the 32 settings and overturns the previous model safety rankings. WILT raises average behaviour presence from 51% to 100% when eliciting self-harm encouragement from Qwen3.5-4B, beating every elicitation method we port into the same pipeline at matched compute, without pushing output probability below the baseline's.

---


### 425. [Aspire: Can Models Self-Evolve from Vague Goals?](https://arxiv.org/abs/2608.31111)

**<font color=#1a73e8>作者：</font>** Yuhao Wu, Jingyuan Zhang, Jiajun Shi 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many important forms of human learning begin with a vague goal, such as "become a better physicist" or "improve at research." Learners must interpret the goal, identify capability gaps, decide how to learn, and determine whether they have actually improved. In contrast, existing work on LLM self-evolution typically begins with tasks and evaluation metrics specified by humans, reducing self-evolution to optimizing an explicit objective rather than deciding what and how to learn. We introduce ASPIRE, a benchmark for vague-goal-driven self-evolution. ASPIRE provides only a natural-language capability goal while downstream evaluation tasks remain hidden. The agent must operationalize the goal by choosing data and update methods, constructing training and validation signals, and deciding when to evaluate. ASPIRE supports both model-weight and agent-harness evolution in a unified interactive environment and evaluates the resulting systems on a hidden, expert-authored set of 520 items spanning six goals. Our experiments show that vague goals redirect search effort toward goal interpretation. Current agents routinely complete training and harness-editing loops, but weight-level gains remain sparse and unstable, and the strongest evolved harness remains below the engineered Qwen-Agent reference. Agents often train on mismatched data and trust narrow self-evaluations, so local gains fail to transfer to hidden evaluation and continued search and training can erase earlier improvements.

---


### 426. [InsightToast: Proactive Information Retrieval & Glanceable Visualization in the Side Channel of Data-Rich Meetings](https://arxiv.org/abs/2608.31115)

**<font color=#1a73e8>作者：</font>** Mohammad Abolnejadian, Matthew Brehmer  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Missing institutional context during meetings can impede effective participation. Retrieving relevant information, often scattered across heterogeneous internal and external sources, requires costly task-switching that disrupts both individual focus and collective conversational flow, particularly detrimental during cognitively demanding tasks such as decision-making. We introduce InsightToast, a mixed-initiative application that monitors verbal discourse in real time, identifies topics and informational needs as they emerge, and proactively retrieves relevant information through a multi-agent large language model (LLM)-based pipeline integrating retrieval-augmented generation (RAG) to produce source-grounded insights as succinct text and glanceable interactive charts, delivered through a peripheral interface as ephemeral toasts in the conversation's side channel. To demonstrate the potential for yielding serendipitous insights, we showcase a usage scenario involving a knowledge base of legislative documents as the meeting's context. We then report on a comparative study (N=16), in which participants arrived at informed policy decisions while maintaining natural conversation flow.

---


### 427. [When Does Bigger Help? A Controlled Study of LLM Scale for Ontology Learning](https://arxiv.org/abs/2608.31118)

**<font color=#1a73e8>作者：</font>** Hamed Babaei Giglou, Sören Auer, Jennifer D'Souza  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The effect of Large Language Model (LLM) scale on ontology learning (OL) performance remains insufficiently characterized. We present a controlled evaluation of 13 models spanning dense and Mixture-of-Experts variants from the Qwen3.5 and Qwen3.6 lineages, together with proprietary GPT release variants, using the OntoLearner retrieval-augmented generation pipeline. All models are evaluated with the same embedding model, retrieval configuration, prompt templates, decoding settings, datasets, and metrics on term typing, taxonomy discovery, and non-taxonomic relationship extraction across four biomedical and materials science and engineering ontologies. Within the dense Qwen3.5 lineage, increasing parameter count primarily improves precision rather than recall, with the largest gains occurring between 9B and 27B parameters. However, the effect of scale is neither monotonic nor uniform across tasks and domains. Dense 27B models outperform substantially larger sparse models on term typing, whereas larger Mixture-of-Experts models achieve the strongest open-weight results on taxonomy discovery. Non-taxonomic relationship extraction remains difficult across model scales, particularly for the Materials Data Science ontology. Performance differences across matched Qwen variants and proprietary GPT releases further indicate that architecture and model lineage can outweigh nominal parameter count. These findings show that model size alone is an insufficient selection criterion for OL and provide empirical guidance for reproducible LLM-assisted ontology engineering.

---


### 428. [PaperGym: Rubric-Centered Evolution for Research-Plan Generation](https://arxiv.org/abs/2608.31119)

**<font color=#1a73e8>作者：</font>** Yuhan Wang, Zhengxi Lu, Yuchen Yan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Research planning is the decisive capability of AI scientists. Yet a research plan admits no verifiable answer, so reinforcement learning lacks the environment it requires: tasks paired with a critic. Rubrics extracted from scientific papers can supply the critic. Existing pipelines, however, draw the question and the criteria from the same content, so the reward can be earned by paraphrase. The rubric is further compressed into a single scalar per rollout. We introduce PaperGym, a unified framework that turns each research paper into a complete training environment. PaperGym exploits the structure of a paper: the question is synthesized from the research goal and background, while the criteria are derived from the method and experiments. The criteria span methodological innovation and experimental design, and criterion leakage falls to 3.7%, versus 11.90% to 34.10% in existing datasets. Training uses the rubric twice: first as privileged context for OPSD's self-teacher, then as the reward for GRPO. Across Qwen3-1.7B/4B/8B, this schedule outperforms supervised fine-tuning, either stage alone, and the reverse ordering, improving five-benchmark averages by +5.6, +5.0, and +4.8 points. With the recipe held fixed, models trained on PaperGym-20k win 58.1% of three-way comparisons, against 28.2% for RubricHub Science. The trained Qwen3-8B reaches 73.48 on ResearchQA, above the far larger Kimi K2.6. We release the pipeline, the 20,000-instance corpus PaperGym-20k, and the benchmarks PaperGym-Innov and PaperGym-Design.

---


### 429. [DIASENTINEL: An Auditable Multi-Agent System for Guideline-Grounded Diabetes Risk Screening](https://arxiv.org/abs/2608.31128)

**<font color=#1a73e8>作者：</font>** Yung Wei Shueh, Zhi-Jie Chen, Chia-Hsuan Hsu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) offer promising clinical decision support but remain vulnerable to hallucinated facts, unsupported recommendations, and citation errors. We present DIASENTINEL, a fully on-premise multi-agent system for one-year type 2 diabetes mellitus (T2DM) risk screening and guideline-grounded report generation from electronic health records (EHRs). The system integrates calibrated risk prediction, deterministic clinical signal extraction, Reciprocal Rank Fusion over American Diabetes Association (ADA) guidelines, and a hybrid verification layer combining rule-based checks with LLM entailment. The demonstration provides a real-time batch-screening dashboard and an interactive patient report interface with cited recommendations, verification results, and raw EHR comparison. DIASENTINEL demonstrates a practical framework for reliable, auditable, and privacy-preserving LLM-based clinical decision support.

---


### 430. [OntoAligner-Ensemble: Voting-Based Fusion across Heterogeneous Ontology Alignment Techniques](https://arxiv.org/abs/2608.31137)

**<font color=#1a73e8>作者：</font>** Hamed Babaei Giglou, Sören Auer, Peio Popov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ontology alignment (OA) has evolved through several methodological paradigms, ranging from lexical and structural aligners to knowledge graph embedding (KGE) models and, more recently, Large Language Model (LLM)-based approaches. Although modern OA frameworks provide unified ecosystems for deploying these heterogeneous aligners, mechanisms for systematically reconciling their complementary and sometimes conflicting predictions remain relatively underexplored. We present OntoAligner-Ensemble, a modular and aligner-agnostic framework that combines candidate correspondences through a configurable two-stage process comprising voting-based fusion strategies followed by post-fusion selection policies. The framework supports any aligner implemented within OntoAligner that produces candidate correspondences, enabling diverse alignment paradigms to be integrated through a unified decision process. To demonstrate its effectiveness, we instantiate the framework using representative lightweight string-aligner, KGE-based, and Retrieval-Augmented Generation aligners powered by both open-weight and API-based LLMs. We evaluate individual aligners and ensemble configurations across eight benchmark tasks from five OAEI tracks spanning biomedical to beyond-equivalence. The results show that ensemble fusion consistently improves the balance between precision and recall and frequently outperforms standalone aligners across diverse domains. Furthermore, our analysis reveals that ensemble composition directly affects the precision-recall trade-off: heterogeneous cross-paradigm ensembles generally improve precision, whereas homogeneous LLM ensembles more often achieve higher overall F1-scores. These findings demonstrate that systematic ensemble learning offers a robust and reproducible strategy for OA while providing practical guidance for selecting ensemble compositions under different alignment scenarios.

---


### 431. [Configurable Semantic Chunking for Biomedical Information Extraction in Retrieval-Augmented Generation](https://arxiv.org/abs/2608.31139)

**<font color=#1a73e8>作者：</font>** Riya Ahuja, Tim Kacprowski, Roya Shiasi Sardoabi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> BioMedRAG introduced retrieval-augmented generation with a learned chunk scorer for biomedical information extraction. However, it relies on fixed-size chunking which can fragment semantic evidence. We propose a configurable semantic chunking framework that addresses this limitation by combining entity-preserving windows, trigger-centered chunking, proposition-first extraction, tiered trigger prioritization, and hierarchical relation resolution. The framework integrates with BioMedRAG by replacing only the chunk construction stage while preserving the embedding model, learned chunk scorer, generator, and evaluation protocol. We evaluate the framework on biomedical relation extraction benchmarks (GM-CIHT, DDI, ChemProt) and adverse event classification (ADE). On GM-CIHT, the full hybrid configuration achieves 82.6% F1, improving over the fixed-size baseline (74.2% F1) by 8.4 points under our experimental setup. Cross-dataset analysis shows that semantic chunking improves extraction datasets with explicit relation cues, such as GM-CIHT and DDI, while fixed chunking remains competitive or stronger for dense biochemical extraction and binary classification settings such as ChemProt and ADE. By externalizing chunking logic into configuration files, the framework provides an interpretable and adaptable alternative to rigid fixed-size chunking for biomedical RAG pipelines.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 432. [MedTVL: Harnessing Vision and Language for Medical Time Series Classification](https://arxiv.org/abs/2608.28605)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiexia Ye, Jia Li, Fugee Tsung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advancements in multimodal learning for medical time series (MedTS) classification highlight the benefits of integrating complementary modalities for clinical decision. However, existing methods typically focus on bi-modal interactions (e.g., time series and text), leaving the tri-modal synergy between time series, vision, and language largely unexplored. Inspired by diagnostic practice synergizing numerical assessment, visual inspection and clinical context, we introduce MedTVL, a text-guided dual-pathway architecture tailored for MedTS classification. Specifically, it synergizes a convolution-based temporal pathway for fine-grained temporal dynamics from raw numerical sequences and a transformer-based visual pathway for holistic morphological structures from time-series-derived images. Such combination of cross-modal and architectural heterogeneity provides a comprehensive diagnostic perspective. To further resolve potential diagnostic ambiguity, both pathways are guided by adaptive medical textual semantics. Finally, a Mixture-of-Experts mechanism dynamically routes each instance to specialized fusion experts, capturing instance-specific reliance on the temporal and visual pathway outputs. In addition, MedTVL supports multimodal contrastive learning to mitigate the clinical label scarcity challenge. Extensive experiments across multiple medical datasets and tasks, spanning supervised, few-shot, and contrastive learning settings, demonstrate the superiority and transferability of MedTVL, highlighting its potential for robust clinical decision support.

---


### 433. [Automated Researchers Can Reliably Mitigate Alignment Failures](https://arxiv.org/abs/2608.28945)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chen Yueh-Han, Jiaxin Wen, Jan Hendrik Kirchner  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automating alignment research may accelerate progress toward aligned AI, but whether it does is hard to measure. Luckily, many alignment failures, such as deception, sycophancy, and jailbreaks, are already measurable by public benchmarks. We study whether automated alignment researchers (AARs) can post-train to mitigate alignment failures by proposing training methods and data to simultaneously optimize multiple safety benchmarks, while preserving general capability. Across 10 alignment failures, the strongest AAR methods significantly reduce the targeted alignment failures and generalize to a held-out benchmark, multi-turn behavioral audits, and models up to 4.7 times larger than the target model. As a human baseline, 28 experienced researchers receive up to eight hours to develop methods for the same benchmarks, but their methods underperform the best AAR methods. Using human ideas as the AARs' initial research direction does not improve performance, suggesting current AARs may not need guidance from experienced researchers. These results suggest that automating alignment research on well-characterized failures may be practical in the near term.

---


### 434. [The Illusion of Replacement: Rethinking Specialized Machine Learning Models in the Foundation Model Era](https://arxiv.org/abs/2608.28980)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kiyan Rezaee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Can the specialized architectures that machine learning has traditionally built for structured data be replaced by language-based models? This question is examined through a review of 159 papers (2016--2026) across nine modalities, with predictive accuracy considered alongside structural representation and computation. A distinction is made between performing a task and preserving and computing the structure that makes the task tractable, and existing approaches are organized into eight representational regimes, ranging from language-only systems to fully specialized architectures. Language-mediated models are found to be highly competitive in specific settings, including extreme few-shot prediction, discretized symbolic tasks, textually annotated knowledge graphs, and large-scale single-modality pretraining. However, whenever structural representation or computation is directly evaluated rather than accuracy alone, no evidence of general architectural replacement is found. Instead, a recurring pattern is observed across independent research communities: when language alone is insufficient, the missing structure is reintroduced through a graph module, structural tokens, specialized attention, or another non-linguistic component. In this sense, specialization more often relocates than disappears. Moreover, although performance of language-based models is improved by scaling, whether the gap to a structure-aware architecture can eventually be eliminated remains untested.

---


### 435. [Revolutionizing Turn-by-Turn Navigation with Cloud-Edge Deep Learning](https://arxiv.org/abs/2608.29073)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yiming Yang, Hao Fu, Fanxiang Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Turn-by-turn (TBT) navigation systems are integral to modern driving experiences, providing real-time audio instructions to guide drivers safely to destinations. However, existing audio instruction policy often relies on rule-based approaches that struggle to balance informational content with cognitive load, potentially leading to driver confusion or missed turns in complex environments. To overcome these difficulties, we first model the generation of navigation instructions as a multi-task learning problem by decomposing the audio content into combinations of modular elements. Then, we propose a novel deep learning framework that leverages the powerful spatiotemporal information processing capabilities of Transformers and the strong multi-task learning abilities of Mixture of Experts (MoE) to generate real-time, context-aware audio instructions for TBT driving navigation. A cloud-edge collaborative architecture is implemented to handle the computational demands of the model, ensuring scalability and real-time performance for practical applications. Experimental results in the real world demonstrate that the proposed method significantly reduces the yaw rate (the proportion of vehicles deviating from navigation routes) compared to traditional methods, delivering clearer and more effective audio instructions. This is the first large-scale application of deep learning in driving audio navigation, marking a substantial advancement in intelligent transportation and driving assistance technologies.

---


### 436. [RAGDiffusion++: From Macro-Retrieval to Micro-Fidelity Alignment for Garment Generation](https://arxiv.org/abs/2608.29280)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuhan Li, Xianfeng Tan, Fangao Zeng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard clothing asset generation---restoring forward-facing flat-lay garment images from diverse real-world contexts---holds immense commercial value yet demands both macroscopic topological accuracy and microscopic physical fidelity. Although our previous work RAGDiffusion effectively eradicated large-scale structural hallucinations via retrieval-augmented macro-constraints, achieving industrial-grade micro-texture realism remains an unsolved bottleneck. We formally identify this limitation as High-Frequency Trajectory Collapse: supervised fine-tuning (SFT) converges to the conditional mean of the training distribution, which is dominated by smooth, low-frequency textures, causing high-frequency patterns (e.g., fabric weaves, intricate logos) to become nearly un-sampleable. Naively applying Reinforcement Learning (RL) post-training further triggers Artifact Hacking, where models exploit semantic biases in generic reward models by generating deceptive checkerboard noise. Our key insight is that RL can fundamentally reshape the sampling distribution of flow models---elevating the probability of high-fidelity trajectories under accurate reward guidance---while adversarial regularization prevents exploitation of reward blind spots. Realizing this principle requires three prerequisites: (i)inherent capacity, established through a 27,725-pair high-complexity garment dataset (STGarment-Plus) and a Dual-Image-Stream FLUX architecture upgrade; (ii)perceptive reward, provided by a novel attribute-aware reward model (Garment-RM) trained on 500K images via fine-grained contrastive learning, achieving 84.67% human preference accuracy; and (iii)hacking prevention, enforced by our Adversarial-Regularized GRPO (AR-GRPO) strategy that integrates a dynamic discriminator into the RL sampling trajectory to penalize artifacts while enriching authentic high-frequency details.

---


### 437. [MedCache: Efficient and Temporally Valid Memory for Longitudinal Clinical Agents](https://arxiv.org/abs/2608.29528)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hei Ting, Chan, Chenwei Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Longitudinal clinical agents must maintain an evolving patient state from evidence distributed across visits, time points, and specialties. However, how agent memory should be designed for this setting remains unclear. We introduce a benchmark of multi-visit, multi-specialty patient records that evaluates long-context evidence retrieval, cross-time evidence aggregation, and cross-specialty clinical reasoning. Using this benchmark, we systematically study four memory design choices: curation, organization, retrieval, and memory-augmented reasoning. We find that temporal validity is more important than simply retaining more history; specialty-factorized memory reduces context but can hide shared evidence; and multiple agents help when specialists must reason together, not merely when evidence comes from multiple memories. Guided by these findings, we propose \textit{MedCache}, a hybrid framework that constructs temporally valid patient memory, organizes evidence into overlapping specialty views, routes each query to relevant memories, and adaptively invokes one or multiple specialists. Experiments show that MedCache improves reasoning accuracy and memory efficiency over strong single-agent and multi-agent baselines, while generalizing across model backbones and external datasets.

---


### 438. [Biomechanical 3D Body: Self-Supervised Distillation of Biomechanical Pose from a 3D Body Foundation Model](https://arxiv.org/abs/2608.29928)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** R. James Cotton, J.D. Peiffer, Lucinda Williamson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> State-of-the-art monocular body recovery methods predict mesh vertices and angles on the corresponding kinematic tree, but their outputs lack biomechanically defined joint angles that downstream applications like clinical and biomechanical analyses require. We extend an existing foundation model, SAM-3D-Body, with an additional biomechanical prediction head that, from a single RGB image, regresses the joint angles and scales of a biomechanical model. Training this model presents a challenge, as there are limited datasets of paired images and biomechanical fits. To overcome this, we supervise biomechanical outputs with in-loop optimized targets from a Levenberg-Marquardt solver performing inverse kinematics fits against markers from the mesh predictions. This allows distilling the biomechanical head from the mesh head, even from unlabeled images. To make this work with GPU-optimized biomechanical models in MuJoCo, the entire model was implemented in JAX using Equinox. We trained this distilled output head on the publicly released SAM-3D-Body dataset. We then validated this model on biomechanical fits to two publicly available marker-based datasets, MoVi and BioCV, as well as movements from a clinical cohort captured with multiview markerless motion capture. The resulting model outperforms existing models for direct regression of biomechanics from images while only slightly underperforming the state-of-the-art monocular biomechanics method that performs more costly inference-time optimization of entire trajectories.

---


### 439. [Evaluating 2D and 3D-Aware Vision Foundation Models for Vehicle Attribute Recognition](https://arxiv.org/abs/2608.29929)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Alexandre V. Delazeri, Gabriel E. Lima, Eduil Nascimento Jr 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vehicle attribute recognition is an important task in intelligent transportation systems, particularly when Automatic License Plate Recognition (ALPR) is unavailable or unreliable. Although vision foundation models have shown strong transferability across domains, their effectiveness for fine-grained vehicle classification remains underexplored. Moreover, given the inherently three-dimensional structure of vehicles, it is unclear whether emerging 3D-aware foundation models offer advantages over standard 2D architectures. This paper presents an empirical benchmark of 14 state-of-the-art 2D and 3D-aware vision foundation models. Using the challenging real-world UFPR-VeSV dataset, we evaluate these models as frozen feature extractors via linear probing for vehicle type, make, and model recognition. We further stress-test the best-performing models under few-shot learning and Out-of-Distribution (OOD) domain shifts. Our results show that standard 2D self-supervised models, particularly DINOv3, substantially outperform 3D-aware models in fine-grained tasks, achieving over 93% Macro-Accuracy for make and model recognition. However, the 3D-aware Depth Anything v2 exhibits stronger invariance to viewing angles in vehicle type classification. These findings motivate hybrid approaches that combine 2D and 3D priors for robust vehicle recognition. Our code is publicly available at this https URL.

---


### 440. [Zero-Knowledge Predicate Proofs Between AI Agents: A Measured, Cross-Protocol Gateway and the Source-Integrity Gap](https://arxiv.org/abs/2608.30083)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ashok Subbabhatta Gopalakrishna  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multi-agent AI platforms move quickly from staging to production, but the way agents establish trust remains rudimentary: an agent either transmits raw data to a peer or accepts that peer's natural-language self-report that a value complies with policy. The first over-shares; the second is unverifiable and is exactly the channel prompt injection attacks. Prevailing responses emphasise identity, visibility, and post-hoc detection, and recent proposals for cryptographically enforced agent policy have been evaluated in simulation rather than execution. We take provable data minimisation between agents from proposal to running system. In our Zero-Knowledge Proof Gateway, agents exchange proofs of governance-defined predicates over private data rather than the data itself, so exposure is prevented by design rather than detected afterwards; because no interoperability protocol can carry such a proof, we propose a slot and implement it on both MCP and Agent2Agent from one endpoint. A 32-bit threshold predicate proves in 6.2 ms and verifies in 1.0 ms with a 608-byte Bulletproofs proof on one commodity vCPU; eleven adversarial experiments and nineteen protocol checks pass; and the system is deployed to Kubernetes with empirically verified network isolation. Our case study proves a retail client order is within its limit without revealing the amount, instantiating the GDPR data-minimisation principle as an enforced technical measure of the kind EU law now names explicitly. We then address the limitation no comparable work resolves: a predicate proof binds a statement to a committed value, never to the system of record. We give a construction fusing an enclave attestation with the proof in both directions, so verifying one artifact certifies jointly that the predicate holds and that the value was read by a specific measured binary, and test it against a mock authority.

---


### 441. [NoisEasier: Test-Time Noise Optimization for Text-to-Video Generation](https://arxiv.org/abs/2608.30194)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yujiang Pu, Yu Kong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have recently advanced text-to-video (T2V) generation, yet they still struggle with fine-grained compositional alignment, such as attribute binding, spatial relations, and object interactions. While reward-based fine-tuning improves alignment, it is susceptible to reward hacking and adapts poorly to new prompt distributions. In this work, we propose NoisEasier, a test-time scaling framework that improves T2V generation through differentiable reward-guided noise optimization without modifying the underlying model. By combining efficient short-step generators with a multi-objective reward formulation, NoisEasier enables stable and practical test-time optimization under realistic inference budgets. Our key insight is that jointly optimizing the entire stochastic trajectory accelerates reward convergence and improves compositional alignment over optimizing only the initial latent, with negligible additional computational and time cost. Experiments on VBench and T2V-CompBench demonstrate consistent improvements across multiple backbones, achieving over 10% average gains on challenging dimensions such as attribute binding, object interaction, and numeracy. Overall, NoisEasier serves as both a flexible alternative and a complementary enhancement to reward-based fine-tuning, establishing test-time scaling as an effective paradigm for controllable text-to-video generation.

---


### 442. [Uncertainty of Vision Medical Foundation Models](https://arxiv.org/abs/2608.30390)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haoxu Huang, Narges Razavian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate uncertainty estimation is essential for machine learning systems de- ployed in high-stakes domains such as medicine. Traditional approaches primarily rely on probability outputs from trained models (point predictions), which provide no formal guarantees on prediction coverage and often require additional calibra- tion techniques to improve reliability. In contrast, conformal prediction (region prediction) offers a principled alternative by generating prediction sets with finite- sample validity guarantees, ensuring that the ground truth is contained within the set at a specified confidence level. In this study, we explore the impact of pre-training approach, dataset scale and domain on both point and region-level uncertainty quantification, by studying domain-specific vision medical foundation models vs. general domain vision foundation models. We conduct a comprehensive evaluation across foundation models trained on retinal, histopathological, and Chest X-Rays data, applying various calibration techniques. Our results demonstrate that (1) pre-training on higher-quality domain-specific datasets along with self-supervised learning leads to better-calibrated point predictions than general domain pre-training, (2) stan- dard re-calibration methods alone cannot fully mitigate uncertainty discrepancies across models trained on different data sources, (3) domain-specific foundation model can lead to more efficient conformal prediction. These findings highlight the importance of careful model selection and the inte- gration of both point and region prediction to enhance the reliability and trust- worthiness of medical AI systems. Our work underscores the need for a holistic approach to uncertainty quantification in recent development of medical vision foundation model, ensuring robust and interpretable AI-driven decision-making.

---


### 443. [Foundation Models Meet Agriculture: Challenges Beyond Pretraining](https://arxiv.org/abs/2608.30392)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Vishal Nedungadi, Xingguo Xiong, Marc Rußwurm 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Global food security and sustainable climate action increasingly rely on robust, scalable agricultural monitoring. Earth observation foundation models have emerged as powerful, label-efficient tools across general remote sensing domains, yet early attempts to deploy them for agricultural applications have yielded surprisingly poor results. We hypothesize that this performance gap stems from the extreme heterogeneity of agricultural landscapes and the inherent inability of current earth observation foundation models to adapt to task-specific nuances. In this work, we systematically evaluate two critical bottlenecks hindering the deployment of foundation models in agricultural tasks, benchmarking two earth observation foundation models, a foundation model designed for tabular data, and conventional supervised baselines across seven real-world agricultural datasets spanning yield prediction, phenology estimation, and crop classification. First, we identify a pretraining-deployment modality gap: agricultural downstream tasks frequently require diverse, non-imagery data modalities that earth observation foundation models are architecturally unequipped to ingest, while a foundation model built for tabular data handles this heterogeneity more naturally. Second, we formalize the agricultural task space across five structural axes to demonstrate why current models fail to generalize reliably, resulting in highly unstable model rankings across evaluation settings. By characterizing these structural and modal gaps, our insights highlight the friction between general-purpose architectures and specialized agricultural downstream data, providing a strategic roadmap for developing the next generation of domain-aware foundation models.

---


### 444. [Co-Evolving Actor-Conditioned Critics for Non-Verifiable Generation](https://arxiv.org/abs/2608.30397)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jinyoung Kim, Muhammad Khalifa, Lajanugen Logeswaran 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural-language critiques provide supervision beyond scalar rewards for non-verifiable generation, which lacks deterministic verifiers. In critique-guided refinement, a critic gives feedback on an initial response and an actor revises it. However, final revision quality does not reveal whether the critique was actually useful: a capable actor may improve without following the feedback, while valid feedback may fail if the actor cannot execute it. We frame critique as actor-conditioned revision guidance, where usefulness depends on whether the feedback helps the target actor address the intended weakness. We introduce TAIScore (Targeted Actionable Improvement Score), a reward that evaluates the instruction, initial response, critique, and revision together, assessing whether the critique targets a real weakness, whether the actor follows it, and whether the intended aspect improves. We use this reward to train an actor-tailored critic with GRPO, and use critique-guided refinements to construct DPO preference pairs for the actor, forming a co-evolving critic-actor loop where the critic adapts to the actor's changing capability. Experiments show that an 8B critic trained with TAIScore outperforms both a zero-shot 120B critic and critics trained with outcome-only or critique-only reward signals. Co-evolving the critic and actor further improves performance, suggesting that effective critique supervision should adapt as the actor changes.

---


### 445. [PRIME: Mitigating Subgroup Optimization Competition in Shared CTR Top Networks with Plug-in Residual Input-Conditioned Mixture of Expert](https://arxiv.org/abs/2608.30449)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Heng Yao, Siyun Hou, Tianying Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Click-through rate (CTR) models vary in feature-interaction design, yet their top networks usually remain a single multilayer perceptron shared by all examples. Heterogeneous user, item, and context subgroups therefore update the same parameters; weakly aligned learning signals make the aggregate gradient a compromise among competing directions. We study the competition on Avazu with 4 models and 4 semantic fields. Across all architectures, semantic subgroups show lower Top-NN gradient cosine similarity than random groups matched by sample size and label ratio, with reductions of 0.23-0.37.
This competition motivates input-conditioned experts, but directly replacing an established Dense mapping changes its initial function, sharing pattern, and capacity, obscuring the source of gains. We introduce PRIME (Plug-in Residual Input-conditioned Mixture of Experts), a Dense-anchored mixture of low-rank residual experts. PRIME anchors the original prediction and uses zero-residual initialization to match the Dense baseline exactly at training onset. Input-dependent routing weights low-rank experts for example-specific logit corrections; multi-bag aggregation and EMA load biases stabilize conditional estimation.
We evaluate PRIME on held-out Avazu and Criteo test sets across 13 CTR architectures and five paired seeds. Median paired AUC gains are +0.0022 and +0.0066, with LogLoss reductions of 0.0011 and 0.0081, respectively. On FiBiNET and DCNv2, PRIME outperforms APG in all ten seed-level AUC comparisons while using fewer parameters and lower inference latency on both backbones. These results show that function-preserving conditional residuals add input-dependent capacity while preserving the Dense path and its optimization stability. Code is available at this https URL.

---


### 446. [Hi-Q: Hierarchical Evidence-guided Query Refinement for Multi-Hop Question Answering](https://arxiv.org/abs/2608.30468)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jueun Kim, Sungho Park, Wook-Shin Han  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A central bottleneck in multi-hop Question Answering (QA) is that the granularity at which a question is expressed often differs from the granularity at which corpus evidence is retrievable. Existing methods address this mismatch by imposing fixed graph structures over the corpus, by iteratively reformulating the query, or by executing a generated program over it, but these strategies do not explicitly decide when a query unit is already supported by evidence and when it should be refined. We formulate this bottleneck as retrievable granularity discovery and introduce Hi-Q, an evidence-conditioned framework for hierarchical query refinement. At each query node, a resolution operator tests whether retrieved evidence supports the current query unit; resolved nodes terminate, while unresolved nodes are expanded by a dependency-preserving binary operator and checked by a semantic coverage verifier. Hi-Q therefore grows a query tree whose topology is determined by corpus support signals rather than by a fixed decomposition template or a pre-built graph. We evaluate Hi-Q on three multi-hop QA benchmarks, primarily under full-corpus retrieval, where dependent evidence must be located among open-domain distractors rather than within a small annotated pool. In this setting Hi-Q reaches 52.3 EM and 64.0 F1 averaged over the three benchmarks, ahead of the iterative retrieval baseline IRCoT by 15.1 EM / 18.2 F1 on that same average, and ahead of the graph-based RAG baseline PropRAG by 11.5 EM / 12.0 F1 on MuSiQue-full, without corpus-wide graph construction. In the restricted supporting/distractor setting used by prior work, Hi-Q likewise attains the best accuracy, with 57.9 EM and 69.3 F1 on average, ahead of PropRAG by 5.6 EM / 3.9 F1 and IRCoT by 13.7 EM / 15.8 F1. The project page is available at this https URL.

---


### 447. [Can Video World Models Track Unobserved World States?](https://arxiv.org/abs/2608.30692)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Joonghyuk Shin, Yicong Hong, Jaesik Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models are increasingly used as simulators, yet visual fidelity alone does not show that a model maintains the hidden state of the world. We examine this gap with an action-conditioned video Shell Game, a visual analog of $S_5$ state tracking that decouples visual rendering from compositing the hidden state underneath. Bidirectional and autoregressive Transformers, Mamba, and linear attention restricted to nonnegative transition eigenvalues all fit the training horizon of 5 swaps and then fall toward chance on longer swap chains (extrapolation) while still rendering plausible video with additional denoising steps providing no benefit. The pixel-based diffusion target never supervises the unseen hidden state, so the generated frames cannot carry it and the state has to live inside the architecture rather than in the tokens. For a Transformer, that architectural state is only an append-only KV cache, so the model has to re-derive the hidden arrangement from the whole history at every chunk. We find two mechanisms that do extrapolate, and both carry a state across chunks and revise it in place. Linear attention succeeds once its transition eigenvalues may be negative, and TTT with a nonlinear fast weight succeeds by updating the feature map through which it reads its own state. We further examine harder cases in dynamic world exploration tasks, and discuss the broader implications for building stateful video world models.

---


### 448. [Multimodal Adaptive Expert Selection with Text Routing and Ordinal Prototype Optimization for Sentiment Analysis](https://arxiv.org/abs/2608.30726)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiaode Chen, Jiakang Yu, Hongtao Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal Sentiment Analysis (MSA) is a fundamental component of affective computing that aims to decipher complex emotional states by integrating verbal content with non-verbal cues including vocal intonation and facial micro-expressions. While recent disentanglement-based approaches have advanced the field, their potential is hindered by two methodological challenges. First, static computation graphs process all samples indiscriminately regardless of semantic complexity, which leads to suboptimal representation for diverse emotional expressions and contextual scenarios. Second, generic contrastive objectives often neglect the intrinsic ordinal hierarchy of sentiment intensities. To systematically address these limitations, we introduce Multimodal Adaptive Expert Selection with Text Routing and Ordinal prototype optimization (MAESTRO), a novel framework designed to dynamically orchestrate and refine multimodal representations. Drawing inspiration from an orchestra conductor, we design a Text-Guided Hybrid Mixture-of-Experts (MoE) mechanism. Unlike static fusion, this module utilizes linguistic context as a routing signal to dynamically activate specific audio-visual experts, thereby resolving cross-modal ambiguity through adaptive feature enhancement. Furthermore, to capture fine-grained sentiment gradations, we propose an Ordinal-aware Prototype Contrastive Learning (O-PCL). By incorporating distance-based penalties into the prototype learning objective, O-PCL enforces a structured latent space that preserves the natural order of emotion. Extensive experiments on the CMU-MOSI and CMU-MOSEI benchmarks demonstrate that MAESTRO achieves state-of-the-art performance, and qualitative analysis further confirms the interpretability of our dynamic routing paradigm.

---


### 449. [A Composition-Aware Pretraining Framework for Geospatial Foundation Models](https://arxiv.org/abs/2608.30817)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Aryan Kashyap Naveen, Abhishek Srinivas, Pranav Moothedath 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geospatial foundation models have emerged as state-of-the-art methods for downstream Earth observation tasks. However, existing pretraining methodologies process imagery through a single-concept lens, failing to capture the highly compositional nature of complex satellite scenes. We propose a composition-aware pretraining framework that explicitly encodes fractional land-cover mixtures. Each satellite image cell is mapped to a histogram representing its fractional land-cover distribution, which we term the "composition target". These targets serve as the primary prediction objective and are distilled into the backbone using Earth Mover's Distance. Experimental evaluation shows that composition-aware pretraining yields substantial gains on region-level understanding tasks requiring semantic similarity judgment, including zero-shot image retrieval and scene classification, while remaining competitive on tasks requiring fine-grained spatial precision, such as segmentation and object detection. With a 36.8M-parameter backbone, our framework outperforms SatMAE and Prithvi-EO-2.0, which contain 303M and 600M parameters, respectively, in most retrieval and scene classification settings. On the fine-grained ForestNet-12 dataset, a rigorous testbed for compositional discrimination, our method boosts baseline mAP@10 from 0.279 to 0.434, a 55.6% relative improvement, providing direct evidence for the effectiveness of explicit composition modeling. The code implementation can be found at this https URL

---


### 450. [MR-JEPA: A General Purpose Video Foundation Model for Cardiac MRI](https://arxiv.org/abs/2608.30975)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Athira J. Jacob, Puneet Sharma, Dorin Comaniciu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cardiac magnetic resonance imaging (CMR) produces rich sequential data such as temporal cine videos and spatial LGE/mapping stacks, yet most deep learning approaches process individual 2D slices, discarding this context. We present MR-JEPA, a self-supervised video foundation model for CMR that extends LeJEPA to 3D spatiotemporal inputs through tubelet tokenization, spatiotemporal masking augmentation, and initialization from a 2D CMR foundation model. Unlike prior CMR video models limited to cine data, MR-JEPA is pretrained on multi-sequence data (cine, LGE, mapping) from 10,505 patients across two centers without annotations. We evaluate the frozen encoder on six downstream tasks using a unified multi-view gated attention architecture: LV ejection fraction, RV ejection fraction, three myocardial strains (GLS, GCS, GRS), and four-class disease detection. MR-JEPA outperforms other compared methods on all five regression tasks, including both a domain-specific CMR model pretrained on more data with text supervision and a natural-video foundation model, achieving an LV EF MAE of 4.79% (r =0.764) and a GLS MAE of 1.87 (r=0.805), with 21-27% MAE reductions over baselines on strain tasks. For disease detection, MR-JEPA achieved a macro AUG of 0.868, remaining competitive with the domain-specific baseline despite using a fully self-supervised pretraining objective. These results demonstrate the potential of a unified video encoder for robust, multi-view utilization of diverse CMR sequences in clinical cardiac quantification and diagnosis.

---


> [!TIP]
> 当前位于：**401-450**（第 9/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-452](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
