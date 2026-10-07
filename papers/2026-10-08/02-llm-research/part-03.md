# 🧠 大模型相关研究 | 2026年10月08日

> 本类共 **303** 篇论文：已确认 **280** 篇，待复核 **23** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-303](./part-07.md)

---

### 101. [Harmful SFT Leaves a Continuous Trace in LLM Checkpoint Updates](https://arxiv.org/abs/2610.07518)

**<font color=#1a73e8>作者：</font>** Ziqun Bao, Xinyu Zhang, Yuchen Shao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety auditing of post-trained large language models typically relies on model behavior, requiring model execution and depending on the coverage of available evaluations. This work asks a different question: Do the target behaviors optimized during supervised fine-tuning (SFT) leave readable evidence directly in checkpoint updates? We find that harmful-compliance SFT induces a continuous, objective-dependent ordering in checkpoint-update space. Using a reference geometry defined by pure harmful-compliance, safety-targeted, and benign-utility SFT, we find that a checkpoint-level coordinate s_H tracks controlled harmful-objective composition with Spearman correlations of 0.986-0.992 across four 7-8B backbones, with the same ordering persisting at larger model scales. Matched compliance-versus-refusal controls show that this checkpoint trace reflects the SFT objective rather than harmful-input exposure, while additional controls rule out simple explanations based on harmful-example count or generic training intensity. Building on this structure, we introduce TRACE, a weights-only auditing method that localizes an unknown checkpoint update relative to frozen harmful and non-harmful reference prototypes and converts this geometry into a continuous harmful-objective score. TRACE requires neither model queries nor access to the unknown SFT data, and can be evaluated directly from checkpoint updates. Across distribution shifts, unseen data, different SFT configurations, partial checkpoint access, and LoRA/full-parameter fine-tuning, the trace remains stable and is positively associated with independently measured attack success rates. TRACE remains informative even at low harmful-objective proportions, providing a complementary auditing signal when behavioral evaluation is unavailable or incomplete. Code is available at this https URL.

---


### 102. [Activation Denoising: A Robustness View on Parallel vs Sequential LLM Quantization](https://arxiv.org/abs/2610.07522)

**<font color=#1a73e8>作者：</font>** Yan Scholten, Rachel Lawrence, James Hensman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization is a powerful tool for compressing large language models. The most scalable methods quantize every layer in parallel, but quantization errors then compound through the residual stream, as no layer corrects for the errors of the layers before it. Sequential quantization accounts for this error compounding by re-calibrating each layer on the already-quantized outputs of its predecessors, yielding stronger results but at the cost of a serial schedule that becomes a bottleneck at scale. As a solution, we propose parallel quantization with activation denoising, which recovers much of the sequential benefit while keeping quantization fully parallel. Rather than re-calibrating layer-by-layer, we take a robustness perspective and model the upstream error as noise, regularizing to be robust to it through a preprocessing step followed by metric-weighted rounding. Applied at every layer, this regularization forms a depth-compounding smoothness penalty that dampens how strongly quantization errors amplify through the model. Unlike orthogonal rotations commonly used in quantization, which must preserve the model's function, we multiply the weights by a more general linear transformation. We find that the two are complementary and their effects compound. Empirically, our robustness regularization recovers a significant part of sequential quantization's benefit in a single parallel pass, at a fraction of its time. Overall, by treating compounding quantization errors as a robustness problem, we offer a principled foundation for more efficient and accurate LLM quantization at scale.

---


### 103. [Disentangling Models from Personas in Heterogeneous LLM Simulations](https://arxiv.org/abs/2610.07535)

**<font color=#1a73e8>作者：</font>** Dani Roytburg, Daphne Ippolito  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent simulations with large language models (LLMs) often operate networks of agents with a single base model. This overlooks the inter-model effects which may dominate engagement dynamics in real-world deployments. To show this, we simulate a heterogeneous social network powered by several different base models and show that the amount of engagement an agent receives depends more on its base model than on its assigned persona. The attraction or repulsion effects of a base model strengthen dramatically when more models are added in the mix, suggesting that networks dynamics may converge to base model effects at scale. To help explain this effect, we conduct a series of content-mediating analyses, showing the predictability of base models across contexts as well as the relationship between a model's lexical patterns and an engagement-maximizing style. In light of recent developments in mass multi-agent interaction, this work underscores the relevance of heterogeneous compositions in driving the outcomes of those networks

---


### 104. [A Systematic Investigation of Bias in Large Language Models for Advertising Relevance](https://arxiv.org/abs/2610.07544)

**<font color=#1a73e8>作者：</font>** Weiwei Wang, Yinchuan Xu, Jialu Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to judge how well an advertisement matches a query, but the fairness of these judgments has received limited attention. We conduct a systematic study of fairness in relevance judgments made by LLMs for queries and advertisements. Our counterfactual framework examines the effects of advertiser identity and possible popularity, input language, and demographic wording. We study GPT-4o as a categorical relevance judge and a Qwen-7B model trained specifically for relevance prediction. The advertiser and language experiments use query and advertisement pairs sampled from real advertising logs. Controlled synthetic queries are used to study demographic associations in employment, housing, and credit. For both models, changing the advertiser identity or input language can alter the relevance assessment. Selected demographic comparisons also show patterns consistent with common stereotypes, particularly those involving gender and occupation. We further study mitigation during model inference and training. The results indicate that its effectiveness depends on whether advertiser information is relevant to the query and how advertiser labels are distributed in the training data. These findings can help advertising practitioners identify fairness risks and develop suitable mitigation methods for LLM relevance systems.

---


### 105. [Which and When to Admit: Gradient Admission for Data-Centric Small Language Model Finetuning](https://arxiv.org/abs/2610.07553)

**<font color=#1a73e8>作者：</font>** Hongyu Cao, Yanchi Liu, Kunpeng Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LoRA fine-tuning adapts small language models (SLMs) to heterogeneous instruction data within a low-rank update subspace, making it vulnerable to three structural problems: conflicting gradients that cancel, static data selection that cannot track evolving learning dynamics, and subspace saturation that causes later updates to overwrite useful directions. We argue that effective adaptation therefore requires controlling which data-induced gradients enter the LoRA subspace and when. We propose GRADE (GRadient-Aligned Data-centric rEcipe), a data-centric framework combining two mechanisms: a state-aware selector that continually admits samples aligned with the evolving multi-task gradient field, and a self-calibrating step-level gate that rejects updates likely to cause destructive overwrite near saturation. Across three current-generation backbones and a heterogeneous seven-dataset instruction pool, GRADE outperforms strong data-selection and PEFT-stabilization baselines in accuracy and robustness. It is the only method to improve consistently over standard LoRA on every architecture, while producing more coherent gradient trajectories and less destructive overwrite. These results show that successful SLM adaptation depends not only on which data are selected, but also on which gradients are allowed to enter and persist in the constrained update subspace.

---


### 106. [Decoupled Multi-Agent Orchestration](https://arxiv.org/abs/2610.07556)

**<font color=#1a73e8>作者：</font>** Xinle Wu, Yao Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Learned orchestration can automatically construct effective language-model multi-agent systems, but existing approaches couple planning to fixed worker pools and train decomposition and collaboration from the same terminal outcome, limiting transfer and obscuring credit assignment. We introduce DeOrch, which separates worker-agnostic planning from concrete worker selection. Its two-stage planner first decomposes the task without worker information, then chooses collaboration operations using compact, worker-identity-free matchability feedback from the pool, enabling conditional credit assignment to decomposition and collaboration decisions. A lightweight matcher estimates worker suitability from behavior on a fixed probe set and adapts online with a contextual bandit, allowing new workers to be incorporated without retraining the planner or matcher. Across diverse in- and out-of-distribution tasks, DeOrch outperforms prior automatic MAS orchestration methods with fewer worker calls than competing learned orchestrators, remains effective when transferred to an entirely unseen worker pool without retraining, and shows consistent gains from both components.

---


### 107. [HouseholdBench: Evaluating Large Language Models as Predictors of Household Economic Behavior](https://arxiv.org/abs/2610.07563)

**<font color=#1a73e8>作者：</font>** Jin Huang, Diego Ferreras Garrucho, Yutong Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have the potential to meet a key goal in economics: a quantitative model of household decision making, across a variety of settings. Yet existing evaluations cover few surveys and outcomes, and do not study how households adjust to changing economic conditions. We introduce a new evaluation, HouseholdBench, which unites 6 U.S. household surveys and 32 prediction tasks spanning numeric, categorical and probabilistic outcomes, related to consumption, income, labor, expectations, and housing. Using past behavior, demographics and macroeconomic conditions, the tasks test whether LLMs predict behavior, including how households adjust to changes in various policies. We evaluate 13 proprietary and open-weight LLMs against a no-change baseline and a gradient-boosted tree model. Most LLMs outperform the no-change baseline, including for policy response tasks -- with the best model lowering error for numeric outcomes by 12.2%. Across most tasks, gradient-boosted trees rank first; leading proprietary LLMs approach their performance, but open-weight models lag. LLMs exhibit systematic over- and underprediction across different tasks. We identify methods that enable a 4 billion parameter open-weight model to match proprietary models' performance: fine-tuning and aggregating 16 predictions per observation. Improvements generalize to policy-response tasks, which are excluded from fine-tuning. We release our datasets, code, and leaderboard on our website: this https URL

---


### 108. [Unanimously Wrong: Certified Abstention from How Medical LLM Consensus Forms](https://arxiv.org/abs/2610.07570)

**<font color=#1a73e8>作者：</font>** Xiaoyang Wang, Tianrui Wang, Christopher C. Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In clinical practice, agreement among independent experts is treated as evidence of reliability, and multi-round consensus has become a core mechanism of agentic medical question-answering systems. When such a system must decide whether to trust its own answer, the prevailing signal is again agreement, now among the sampled answers. But agreement is a fragile proxy for correctness. A system can be unanimously wrong, returning the same incorrect answer on every sample, and on these questions agreement-based signals carry no information. The cause is that these signals read only the final state of the consensus and discard how it was reached. Agreement that was reached by resolving disagreement with evidence looks identical, at the end, to agreement that was present from the first sample because every sample shares one misconception. ProbeGuard is a certified abstention framework that bases the abstention decision on how the consensus formed. Process features trace agreement trajectories, minority persistence, and retrieval saturation. For unanimous votes, rationale semantic entropy checks whether the reasons behind the vote cohere, and an active probe retrieves counter-evidence and measures whether the consensus survives. A stratified Learn-then-Test calibration then converts these scores into a distribution-free bound on selective risk. We evaluate ProbeGuard on three medical QA benchmarks and a hard-frontier reference, with a published multi-round agentic RAG substrate, against six abstention baselines. On MedQA, 13.4% of unanimous votes are wrong, and no agreement-based signal can flag them. Process signals raise the discrimination of correct from incorrect consensus from chance to 0.696 AUROC. The certified rule answers six in ten unanimous-layer questions at an observed selective risk of 9.0%, and nine in ten once in-domain calibration data accumulate.

---


### 109. [Two Vectors Replace In-Context Demos: Structured Task Adaptation via Embeddings](https://arxiv.org/abs/2610.07572)

**<font color=#1a73e8>作者：</font>** Xi Ding, Naichen Shi, Jiawei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) adapts frozen large multimodal models (LMMs) to new tasks from a few demonstrations (demos), but re-encodes them at every query, where each demo image adds up to hundreds of visual tokens. Demo-free methods remove this cost with a compact task state. However, they add it at locations searched per task or at every decoder layer, where task parameters grow with depth. Moreover, inserted tokens or keys cannot change how the original prompt divides its attention within a layer. To address these issues, we propose Structured Task Adaptation via Embeddings (STAVE), which replaces demos with two task-specific vectors added to existing input embeddings. Specifically, a readout vector updates the answer-producing tokens and a context vector updates the other structural token groups. Both are trained with answer labels on prompts with and without demos. We justify these design choices theoretically using a first-order analysis of the loss and a margin bound. Extensive experiments on six LMMs and five large language models show that STAVE matches or outperforms state-of-the-art methods on multimodal tasks with far fewer task parameters and surpasses 15-shot ICL and prior task vectors on 18 text tasks, all at zero-shot inference cost.

---


### 110. [LOGIC: An LLM Benchmark for Intent-Grounded Change Impact in Aerospace Electrical Systems](https://arxiv.org/abs/2610.07580)

**<font color=#1a73e8>作者：</font>** Muhammad Faraz Shoaib, Muhammad Qasim, Raisulhaq Mohammed Rizwan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aerospace electrical-design revisions can contain multiple genuine changes, although an engineering request may authorize only a subset. Propagating every detected difference can therefore produce overly broad impact reports. We present LOGIC, a controlled benchmark and evaluation framework in which locally deployable language models ground a request in a deterministic candidate-change inventory before selected changes are propagated through a typed electrical traceability graph. This separation permits candidate-selection errors to be distinguished from downstream propagation errors. LOGIC contains 168 scenarios, including 144 selection and 24 abstention cases. We evaluate three 7--8B models against intent-agnostic, lexical, and structured-evidence methods, with an oracle-root upper bound. On 96 explicitly anchored selection cases, gate-only structured evidence achieves candidate F1 of 1.0000, compared with 0.9677 for token-lexical matching. On 12 relational-paraphrase cases, token-lexical F1 is 0.1772 and gate-only F1 is 0.0000, compared with 0.5000--0.6400 for the large language models. Model grounding degrades as candidate inventories grow from 4 to 64 changes, while affected-element and typed-path accuracy remain comparatively stable when frozen selections are replayed over graphs of approximately 1K to 100K nodes. Strict evidence gating suppresses false positives but can remove correct semantic selections. An exploratory evidence-empty abstention policy raises strict abstention accuracy to 0.6667 for all three models and reduces unsafe-report rates to 0.1667, while decreasing answerable-case coverage by 16.0--27.1 percentage points. Four of six conflicting requests remain unsafe for each model. These findings support combining literal evidence and language-model reasoning with engineering review when intent cannot be established reliably.

---


### 111. [Large Language Model Orchestration under Heterogeneous Preferences via Explicit Persona Inference](https://arxiv.org/abs/2610.07587)

**<font color=#1a73e8>作者：</font>** Shuqing Shi, Ziyan Wang, Milind Tambe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM orchestration investigates how an orchestrator coordinates a group of autonomous agents to achieve common goals or maximize collective welfare. The agents are typically heterogeneous, each holding a private preference that it pursues but does not reveal. Inferring such hidden preferences from behavior has been a subject of long-standing research in game theory and multi-agent systems. The core challenge lies in maintaining a belief over every agent's preference and updating it from the agents' observed actions. Existing LLM orchestrators carry that belief as prompt text with no explicit update rule. This lets early errors persist and propagate rather than be corrected. We therefore propose \textbf{HARP} (Heterogeneous-preference Agent oRchestration via Preference inference), a novel framework that moves the belief out of the prompt. Specifically, HARP maintains one numeric posterior per agent over a finite set of candidate preferences and updates it in closed form by Bayes' rule. The language model supplies only actions and per-candidate likelihoods, so estimation is decoupled from its reasoning. We prove that HARP attains the same $\tilde O(\sqrt K)$ Bayesian regret as explicit joint inference when the factorization is exact. Furthermore, HARP\textsuperscript{+} augments planning with a bonus for actions that distinguish the candidates, so inference continues even when the optimal action is uninformative. Empirical results on three substrates, ranging from payoffs the preferences fully determine, through payoffs that depend on more than them, to scales where explicit joint inference is infeasible, demonstrate that HARP\textsuperscript{+} is the strongest non-oracle method across the class our theory identifies.

---


### 112. [Personal-Agent Mediated Recommendation with Cross-Platform User History](https://arxiv.org/abs/2610.07588)

**<font color=#1a73e8>作者：</font>** Yu Xia, Jiangfan Zhang, Jun Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern recommendation is shifting from platform-centric personalization toward user-governed personalization, where a personal LLM agent can act on the user's behalf across services. We formalize this emerging paradigm as Personal-Agent Mediated Recommendation: a platform recommender ranks a candidate set using platform-local information, and a personal agent uses user-authorized cross-platform history to mediate the resulting ranking and produce the final top-K slate. Such mediation is nontrivial: the platform ranking can encode strong population evidence that the personal agent cannot observe, so effective mediation must therefore balance beneficial rescues against harmful overrides. To study this trade-off, we introduce MediateRec, a benchmark that includes scalable proxy cross-platform environments and a real cross-platform test under a controlled platform-agent information boundary. To train the agent to use cross-platform history effectively, we further propose Personal Attribution Mediation Optimization (PAMO), which counterfactually masks that history to estimate personal mediation support and reallocates rank-aware advantage mass under a platform-relative value floor. We theoretically prove that PAMO preserves cutoff-level advantage mass and is locally optimal among first-order reallocations that preserve this mass without lowering average platform-relative value. Experiments on MediateRec show that personal-agent mediation enables meaningful platform corrections, yet even strong proprietary LLMs introduce non-negligible harmful overrides. PAMO consistently improves over matched outcome-only RL across seen and unseen target platforms and on the real cross-platform test, while achieving a better rescue-harm balance.

---


### 113. [LSC-DPO: Learning-Signal-Controlled Direct Preference Optimization](https://arxiv.org/abs/2610.07592)

**<font color=#1a73e8>作者：</font>** Yang Qu, Yusheng Han, Chengjia Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) has become a standard reward-model-free approach for aligning language models with preference data. However, as the scaled preference margin grows during training, the logistic DPO loss becomes progressively less sensitive to further changes. We study DPO from a loss-level geometric perspective and identify the sigmoid factor as a learning signal that characterizes the local sensitivity of the objective. Based on this view, we propose Learning-Signal-Controlled Direct Preference Optimization (LSC-DPO), which dynamically regulates the learning signal near a target regime. A log-space analysis establishes conditions for stable tracking of the target learning-signal regime. Experiments on AlpacaEval 2, MT-Bench, and Anthropic-HH show that LSC-DPO consistently improves over DPO and strong preference-optimization baselines. We further find that different coefficient initializations induce distinct transient learning-signal trajectories even when their later signal levels become similar. Based on this observation, we derive a signal-budget compensation rule that adjusts the target learning signal to compensate for these transient differences. The resulting compensation substantially reduces performance variation across coefficient initializations.

---


### 114. [VALSE: Vertical Adaptive Layer Skipping for Efficient Inference in Large Language Models](https://arxiv.org/abs/2610.07606)

**<font color=#1a73e8>作者：</font>** Jia-Dong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper establishes a theoretical framework for vertical adaptive layer skipping, proving three foundational results: (i) an Expected FLOPs formula (theorem 2) giving a closed-form expression for the computational cost of arbitrary per-sample skip schedules as a function of layer-wise skip probabilities; (ii) function-space superset (theorem 10) and strict inclusion (theorem 11) theorems showing that skip-layer models are strictly contained in---yet meaningfully approximate---the full-layer function space, with an explicit separating example; and (iii) a structural duality between VALSE and Mixture-of-Experts architectures (proposition 6), positioning vertical depth-wise sparsity as the orthogonal counterpart to horizontal width-wise sparsity. Building on this theory, we propose VALSE (Vertical Adaptive Layer Skipping for Efficiency), a per-sample, non-contiguous layer skipping method: a lightweight difficulty estimator scores each input from the first few layers, and per-layer gates selectively skip redundant layers---including arbitrary middle layers while retaining deeper ones---so that only the necessary depth is activated for each input, whose feasibility is preliminarily assessed at prototype scale.

---


### 115. [Explore, Then Commit: Measurement-Efficient Scientific Law Discovery with Language Models](https://arxiv.org/abs/2610.07620)

**<font color=#1a73e8>作者：</font>** Kautik Mandve, Dileepa Fernando  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific law discovery requires selecting measurements and converting evidence into a governing equation. We evaluate an explore-then-commit protocol in which a large language model proposes hypotheses, a programmatic planner gathers measurements, and a fresh prompt synthesizes the final law from fixed observations. The protocol combines structured probes, automatic numerical diagnostics, restricted measurement batches, and optional interpreter access. Across 576 NewtonBench trials, we compare eight configurations on 12 physics modules using GPT-4.1-mini and a medium-difficulty GPT-4.1 replication. On medium tasks, interpreter-enabled planners use 8.6 versus 22.5 measurements per trial for GPT-4.1-mini and 8.9 versus 43.0 for GPT-4.1. Their mean magnitude-based root-mean-squared logarithmic error falls from 2.514 to 0.202 and from 0.626 to 0.149, respectively. An additional audit retains incomplete and invalid submissions in a coverage-sensitive analysis. Observed symbolic-accuracy gains are less consistent across modules, and random acquisition is competitive with disagreement scoring. Measurement savings occur in every module, but unequal batch constraints prevent attributing them solely to acquisition quality. These results support the complete protocol as a promising measurement-efficient configuration, while leaving its causal components and generalization beyond noiseless direct-equation tasks unresolved.

---


### 116. [Stateless Language Agents: Scaling Long-Horizon Automated Research](https://arxiv.org/abs/2610.07625)

**<font color=#1a73e8>作者：</font>** Qizheng Zhang, Changxiu Ji, Isaac Sun 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated research systems increasingly run LLM agents over long horizons, but more inference does not by itself produce more progress: agents replay growing histories, duplicate one another's work, or stop experimenting while token consumption continues. Yet most evaluations use short budgets or benchmarks that saturate early, leaving these failure modes untested. We trace these failures to two choices: where research state lives and who decides what to try next. We introduce Stateless Language Agents (SLAs), built on the principle of stateful search with stateless agents: no agent carries its conversation across invocations; instead, the harness owns the research state (candidate solutions and measured outcomes) and reconstructs a fresh and role-specific context for every invocation. What each agent sees becomes an explicit design choice rather than a history that grows with the run. We implement this principle in the SLA framework, where a stateless Advisor reads harness-summarized evidence across search directions and assigns concrete experiments to parallel Workers. We evaluate SLA against three recent frameworks on software engineering, kernel optimization, and algorithm design at budgets of up to one billion tokens. SLA achieves the best final result on every task and reaches the strongest kernel baseline's final performance with over 84% fewer tokens. Ablations from shared checkpoints show that focused contexts and explicit assignments each contribute to SLA's progress, with effects that can compound over full runs, while the Advisor consumes less than 0.6% of tokens. These results argue for SLAs, which keep durable research state out of agent conversations, and show that short evaluation horizons can misjudge research systems and their components.

---


### 117. [Monte Carlo Estimation for KV Cache Eviction](https://arxiv.org/abs/2610.07643)

**<font color=#1a73e8>作者：</font>** Ahsan Bilal, Muhammad Ahmed Mohsin, Muhammad Umer 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most KV-cache eviction methods ask, in effect, which memory appeared important while reading the prompt? We instead ask, which memory will matter while answering? Since decoding queries are unavailable at eviction time, prior future-aware methods rely on pseudo-responses or synthetic future-query estimates. We cast fixed-budget future-aware eviction as distributional estimation over plausible model-conditional query trajectories and introduce LORE-KV (Lookahead Output-perturbation with Reliability-weighted Ensembles for Key-Value caches), a training-free method that samples short autoregressive continuations from the frozen target model and uses their response-side query states to estimate prompt-token utility. Tokens are scored by projected leave-one-out attention-output deletion cost and aggregated across sampled futures with optional trajectory weighting. The temporary continuations are discarded before final decoding, requiring no auxiliary model or training. Ablations isolate the mechanism: at B=128, a single response-side continuation recovers about 89% of the gain over the prompt-window control, while additional futures provide smaller improvements. At B=128, LORE-KV raises the LongBench average on Qwen2.5-14B from 45.49 to 48.24 (+2.75) and the 16K RULER average on Mistral-7B from 45.20 to 51.05 (+5.85). Gains diminish at larger cache budgets and coexist with task-level regressions. LORE-KV incurs 1.46-2.77x AnDPro's per-sample wall-clock time as a one-time compression overhead across six dense and hybrid-attention backbones.

---


### 118. [Matching Object or Relation? Tracing Abstract Reasoning Inside VLMs](https://arxiv.org/abs/2610.07646)

**<font color=#1a73e8>作者：</font>** Gouki Minegishi, Hiroki Furuta, Takeshi Kojima 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) excel on visual benchmarks but fail systematically on tasks requiring abstract reasoning. Existing benchmarks document this failure but cannot say \emph{why} it happens or which cognitive capability is missing. We close this gap by adopting the Relational Match-to-Sample (RMTS) paradigm from comparative and developmental psychology and pairing it with a mechanistic analysis of the model's internals. On a parametrically controlled stimulus set evaluated across frontier API models (GPT, Claude, Gemini) and three open-source families (Qwen3.5, Gemma-4, InternVL3), we identify four levers that shift VLMs toward the relational match---capability tier, model scale, the number of objects per scene, and the absence of per-object stimulus noise---together producing a developmental-like trajectory that mirrors the human \emph{relational shift}. Opening up the model, a per-layer representational similarity analysis and a causal mediation analysis reveal that VLM abstract reasoning is implemented by two competing circuits: an early circuit that organises images by their surface object features, and a late circuit that organises them by their abstract relation. Extending the analysis to ARC-AGI-1, we find that ablating the relational heads identified on RMTS degrades performance more than ablating random heads, indicating that the relational circuit is recruited beyond our controlled stimuli. We hope this mechanism-level view serves as a step toward understanding how abstract reasoning is implemented in VLMs.

---


### 119. [Where Rules End and Judges Begin: Measuring the Judgment Boundary in Multi-Agent Systems Security](https://arxiv.org/abs/2610.07657)

**<font color=#1a73e8>作者：</font>** Shaswata Mitra, Raj Patel, Subash Neupane 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems (MAS) engage tools, share memory, and delegate tasks, often encountering adversarial content. Current defenses for MAS are typically evaluated in isolation, focusing on one attack type at a time, which can lead to costly and hard-to-audit outcomes. This study organizes defenses into five principles, implementing them as DEFER1 (DEterministic-First Enforcement with Residual judgment), which includes a cascade of 28 checks that blocks what it can and refers the rest to a panel of four judges. In independent testing across four domains, attack success rates drop from about 30.0% to approximately 3.0%, with 78% of blocked attacks handled by deterministic checks. Only a quarter of proposals reach the judges in the security-operations domain, illustrating that the rules provide security for attacks violating clear policies, while judges manage those that only misrepresent intent. Both systems have weaknesses, such as a risk-score approval gate that inaccurately approves most attack proposals but few legitimate ones, highlighting the challenges in assessing threats accurately.

---


### 120. [DLoop: Looped Speculative Decoding](https://arxiv.org/abs/2610.07659)

**<font color=#1a73e8>作者：</font>** Geonmo Gu, Byeongho Heo, HeeJae Jun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates autoregressive generation in large language models. In each drafting stage, a lightweight draft model proposes tokens that the target model subsequently verifies. With increasingly capable draft models, we find that the target model frequently accepts all tokens produced in a drafting stage. A verification nevertheless follows each drafting stage, resulting in unnecessary target-model forward passes even when drafting could have continued. Adaptive draft length methods decide during decoding how many draft tokens precede a verification, but they raise the speedup only for autoregressive draft models. For a parallel draft model, drafting further requires target-model hidden states for draft tokens that have not been verified. We propose DLoop, a looped form of speculative decoding that adaptively performs multiple drafting stages before verification. DLoop continues drafting while the draft model remains confident and verifies all accumulated draft tokens together. Loop-aware training keeps the draft model reliable in the additional drafting stages by exposing it to its own hidden states for unverified draft tokens. By spending additional draft-model forward passes, DLoop reduces the number of target-model forward passes required for verification. Across diverse speculative decoding methods including EAGLE-3, DFlash, Domino, DSpark, and multi-token prediction modules, DLoop improves the wall-clock speedup by 5 to 41 percent while preserving lossless decoding. Code will be available at this https URL.

---


### 121. [When the Commons Appropriates a Large Language Model: How WikiVault Reshaped Korean Wikipedia](https://arxiv.org/abs/2610.07660)

**<font color=#1a73e8>作者：</font>** Inhwa Song, Sohyeon Hwang, Ted Yoo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have disrupted the balance between content production and quality assurance that sustains knowledge commons, leading many to prohibit or restrict their use. But what happens when a community instead appropriates an LLM-powered tool for its own needs? We investigate this question through WikiVault, an LLM-powered editing tool developed within the Korean Wikipedia community and used primarily for translation. Combining ten interviews, platform-scale analyses, and matched quasi-experimental comparisons, we examine how WikiVault reshaped knowledge production on Korean Wikipedia. We find the tool 1) drastically amplified the production capacity of a small group of experienced editors, producing longer and more widely viewed articles; 2) shifted work toward reviewing articles and importing content; 3) imported not only content but also editorial judgments from English Wikipedia. Our findings show how LLM adoption can rebalance the interdependent work that sustains knowledge commons, while illustrating how communities can learn from emerging technologies through use and adapt their governance accordingly.

---


### 122. [Massive Activation Gating Channel in Large Language Models](https://arxiv.org/abs/2610.07661)

**<font color=#1a73e8>作者：</font>** Minjia Mao, Shi Chen, Bowen Yin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Massive activations, a phenomenon in which a small number of hidden channels exhibit exceptionally large magnitudes, are pervasive in large language models (LLMs). However, the mechanism by which a token develops massive activations as it propagates through a pretrained LLM remains poorly understood. In this paper, we find that the emergence of massive activations is controlled by a single channel in the input embedding to a spike feed-forward network (FFN). The position of this channel is fixed for a particular LLM. We name this channel the massive activation gating channel (MAGC). When the value of the MAGC is sufficiently large (or small, depending on the LLM), the output of the spike FFN exhibits massive activations. Examining six LLMs across four model families and different model sizes, we verify the existence and effect of MAGC. We further provide a theoretical explanation of the mechanism by which MAGC induces massive activations. When the value of MAGC is sufficiently large (or small), the output of a spike FFN asymptotically reduces to a quadratic form that mixes a few columns of the down-projection matrix of the FFN. Since these columns exhibit the shape of massive activations, the output therefore exhibits massive activations.

---


### 123. [SENSE: State-aware Emotion Navigation Storytelling Engine](https://arxiv.org/abs/2610.07666)

**<font color=#1a73e8>作者：</font>** Yi Xia, Pablo Carrasco Velo, Mudit Paliwal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper presents SENSE, a state-aware framework for generating playable branching visual novels with multi-track emotional navigation. Integrating a state-based narrative architecture called MIND, a structure analyzer, and a path-aware context management module, SENSE produces narratives that are both structurally coherent and emotionally rich. From minimal high-level inputs, it generates multiple intersecting routes while preserving character consistency and narrative causality. Evaluations using LLM judges, affective metrics, and visual assessments indicate SENSE outperforms baselines in narrative diversity and robust asset integration, while preliminary human trials show directional improvements in emotional fidelity alongside comparable enjoyment.

---


### 124. [Unlocking Fine-Grained Perception in CLIP via Structurally-Aware Latent Masked Modeling](https://arxiv.org/abs/2610.07689)

**<font color=#1a73e8>作者：</font>** Juntong Li, Lingwei Dang, Haomin Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) such as CLIP excel in global semantic alignment but often lack fine-grained perceptual capabilities. This hinders dense prediction tasks and bottlenecks the visual potential of Multimodal Large Language Models (MLLMs). Existing research has attempted to enhance CLIP's visual representations by incorporating geometric priors from vision-centric models. However, these strategies often struggle to achieve deep alignment for both local spatial structures and global semantics, potentially even distorting the original image-text space. To address these limitations, we propose SALM, an unsupervised embedding alignment framework based on structurally-aware latent mask modeling. SALM effectively synergizes local and global alignment via a dual-path design combining explicit and implicit mechanisms, without requiring any image-text pairs. First, we introduce a dual-matrix alignment strategy that explicitly calibrates intra-sample spatial correlations and activation intensities, thereby effectively injecting local geometric priors. Based on this, we further design a latent mask modeling mechanism to guide CLIP to restore the missing semantic details of the target model, thereby implicitly aggregating fine-grained structures into the global semantic space. Furthermore, driven by the empirical observations that CLIP's shallow features inherently possess strong spatial observational capabilities, we naturally extend SALM to a highly efficient self-distillation paradigm, SALM-Self. This unlocks CLIP's intrinsic fine-grained potential without relying on any external models. Extensive experiments demonstrate that SALM not only significantly improves performance in dense prediction tasks but also boosts CLIP's zero-shot accuracy, effectively enhancing the fine-grained understanding capabilities of MLLMs. Project page at this https URL.

---


### 125. [Improving Synthetic Data Generation for Argument Mining via Adversarial Reinforcement Learning](https://arxiv.org/abs/2610.07699)

**<font color=#1a73e8>作者：</font>** Zhijun Zhang, Qianlong Wang, Keyang Ding 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Argument Mining (AM) is fundamentally constrained by the scarcity of high-quality structure-annotated datasets. While LLMs have shown promise in synthetic data generation, producing synthetic AM data that is both structurally accurate and sufficiently diverse remains a challenging problem. To address this problem, we revisit synthetic data generation for AM from a new perspective and propose a novel adversarial reinforcement learning framework for data synthesis. The proposed framework jointly optimizes the generator and the discriminator in an adversarial loop, in which the generator produces structured AM instances, and the discriminator provides learning signals by distinguishing real data from synthetic candidates. This enables the generator to progressively improve both the structural accuracy of generated argument data while maintaining diversity through adversarial feedback. Extensive experiments demonstrate that the proposed framework consistently improves AM performance on three benchmark datasets in both full-data and low-resource settings, validating its effectiveness and scalability.

---


### 126. [Detecting LLM-Assisted Vietnamese Writing via Keystrokes under Behavioral Manipulation](https://arxiv.org/abs/2610.07700)

**<font color=#1a73e8>作者：</font>** Thanh Dong, An Ngo, Minh Dau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study the robustness of keystroke dynamics for detecting large language model (LLM)-assisted writing. We introduce a Vietnamese keystroke dataset capturing realistic writing modes, including bona fide composition, transcription, and paraphrasing. We also define a behaviorally grounded threat model in which users deliberately alter typing patterns. To implement the threat model, we create behaviorally manipulated variants of the data designed to evade keystroke-based detection. We evaluate four keystroke modeling approaches: temporal and rhythmic representations, and sequential representations modeled with a one-dimensional convolutional neural network (1D-CNN) and TypeNet, under user-independent and context-independent settings. The results show that sequential models outperform feature-based approaches in most cases and that keystroke signals encode discriminative information about the writing process. However, detection is not uniformly robust: transcription is reliably identified, while paraphrasing and adversarially manipulated samples are frequently misclassified as bona fide when not explicitly modeled. To address this, we incorporate adversarial training using behaviorally manipulated data, which substantially improves separability and robustness. These results suggest that keystroke-based detection depends critically on exposure to diverse writing behaviors, and that strong performance under limited conditions does not generalize to realistic or adversarial settings without targeted modeling.

---


### 127. [WASD: Wasserstein-based Knowledge Distillation for Large Language Models](https://arxiv.org/abs/2610.07706)

**<font color=#1a73e8>作者：</font>** Byeonghu Na, Donghyeok Shin, Yeongmin Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive large language models (LLMs) have rapidly advanced in capability, but their increasing scale comes with substantial computational and memory costs at inference time. Knowledge distillation (KD) offers a practical solution by transferring knowledge from a large teacher model to a smaller student model via alignment of discrete probability distributions. However, existing KD methods for LLMs primarily rely on divergences that evaluate discrepancies through probability values at each vocabulary index, without explicitly leveraging token-level semantic information. We propose Wasserstein-based knowledge distillation (WASD) for LLMs, which incorporates token-level semantic information via the Wasserstein-based distance with a cost matrix derived from token embeddings. To ensure computational tractability, we adopt the Sinkhorn divergence and derive a gradient-equivalent objective that can be efficiently optimized without introducing additional networks. Experiments across multiple LLM families and scales show that WASD consistently improves distillation performance on diverse tasks, including instruction following, mathematical reasoning, and code generation. Our results highlight the importance of semantic information encoded in the token space for effective distribution alignment in LLM distillation. The implementation is publicly available at this https URL .

---


### 128. [Evidence Before Sampling: Interpretable Implicit Negative Candidate Discovery for Recommendation](https://arxiv.org/abs/2610.07708)

**<font color=#1a73e8>作者：</font>** Shreya Rajpal, Sonia Sharma, Swapnil Parekh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recommender systems learn from observed user-item interactions, but explicit negative feedback is often unavailable. Since deep learning models require negative signals for training, negative sampling methods typically treat selected unobserved interactions as negatives. However, a missing interaction does not explain why a user is uninterested in an item or whether there is sufficient evidence to label it negative. This is especially important in business recommendation, where negative signals should be interpretable and aligned with business objectives. We formulate implicit negative candidate discovery to identify unobserved interactions supported by observed customer behavior. We encode these patterns as symbolic rules, score them based on support, informativeness, and product relevance, and rank the retained rules by evidence. An LLM then interprets the retained rules using business objectives and domain knowledge; the interpretations are combined with the statistical evidence in the final report. We evaluate our method in an industrial B2B setting and across five public recommendation datasets. Candidate-quality evaluations in the industrial setting and three public datasets show higher precision than the evaluated baselines, while symbolic selection improves downstream test PR-AUC by 12.5% over random selection with four negatives per positive example in the industrial task. Our results show that negative candidate validity can be evaluated separately from downstream recommendation performance. This distinction enables evidence-based, business-aligned, and explainable negative selection, improving both interpretability and model training in sparse, skewed, real-world recommendation settings.

---


### 129. [Readout Stability in Prefill-Only Decision Models:Zero-Label Prediction and Inference-Time Compute Allocation](https://arxiv.org/abs/2610.07716)

**<font color=#1a73e8>作者：</font>** Ran Li, Lei Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prefill-only decision models inspired by the Jev model score every candidate in a menu during a single forward pass and never decode, which makes one call one to two orders of magnitude cheaper than a same-scale generative language model. We show that this read-out structure comes with a testable property. When an intervention changes only the candidate menu and leaves the input text fixed, the post-intervention accuracy is already determined by the cached first-pass distribution. The estimator restricts the pass-1 probabilities to the menu, renormalizes, and reads off the argmax; it uses no labels and no second forward pass. Across seven model families, ten datasets and two task types, menu-only interventions are predicted to within 4.2 points, and for one family the prediction is exact. A probability-level variant of the same estimator errs by 21.0 points, so the property lives in the ranking rather than in the probabilities and is not recovered by calibration. Same-scale generative language models do not share the property. On those models the same estimator errs by 1.6 to 15.8 points and degrades as the model grows. The property turns inference-time compute into a decision that can be made before deployment. Uniform extra passes buy calibration but almost no accuracy; at matched cost a confidence cascade outperforms every scheme that re-asks the same model, and curating the menu beats enlarging the model, with a 0.8B model on a curated 5-candidate menu reaching 95.4% on CLINC150 against 80.0% for a 4B model on the full 150-label this http URL and data are available at this https URL.

---


### 130. [Does Steering Break Your Model? A Multi-Dimensional Evaluation Suite for LLM Steering Methods](https://arxiv.org/abs/2610.07722)

**<font color=#1a73e8>作者：</font>** Haotian Yang, Huikang Jiang, Yucheng Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering provides a lightweight and flexible way to control large language model (LLM) behavior. However, effective steering requires more than inducing the intended behavior: it should also limit unintended changes and remain robust across inputs and training data. Existing evaluations cover these dimensions only in fragments. As a result, the trade-offs between efficacy and side effects have not been systematically characterized. We introduce SteerScope, a two-axis, multi-dimensional evaluation suite that jointly characterizes steering outcomes and method properties through 15 metrics. We score target efficacy and side effects on language quality, task capabilities, and safety and reliability, and further assess generalization and data dependence through steering-specific metrics for sample efficiency and sample sensitivity. Rather than comparing methods at a single operating point, we characterize the trade-offs between efficacy and side effects. Under matched models, tasks, and evaluation protocols, we benchmark 23 methods spanning 4 families, including prompting, LoRA, and SFT as baseline methods, and release the suite as an extensible codebase. We find that current activation steering methods do not yet surpass the Prompt Steering baseline in their overall balance between steering efficacy and side effects: across both model scales, no evaluated activation steering method achieves higher efficacy without incurring greater composite side effects. We further uncover a consistent coupling between steering efficacy and side effects. Under OOD prompts, target efficacy is often preserved, whereas side effects tend to become more pronounced, particularly through declines in instruction relevance and fluency. Methods also exhibit sharply different sample-efficiency profiles.

---


### 131. [Foveated Compression: Selective High-Resolution Preservation for Token-Efficient VLMs](https://arxiv.org/abs/2610.07729)

**<font color=#1a73e8>作者：</font>** Donghyun Han, Jangho Park, Yuseok Bae  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual tokens are a major source of inference cost in vision-language models, yet simple image downsampling remains a surprisingly strong compression baseline. This raises a complementary question: under a fixed token budget, where should visual fidelity be preserved? We introduce Foveated Compression, which encodes a full-resolution image once and represents it with a mixture of native- and compressed-resolution visual tokens. A behaviorally self-distilled Foveated Merger compresses local visual tokens while preserving compatibility with their native counterparts, and a lightweight Foveated Selector chooses one of nine spatial cells to retain at native resolution using exhaustive budget-matched intervention supervision. At 11.11% visual tokens, uniform Foveated Compression shows no significant paired difference from iso-token downsampling. At 20.99%, the learned selector significantly outperforms random and fixed allocation, but remains below strong whole-image resizing, showing that localized fidelity is not universally preferable. A budget-matched region-choice oracle reaches 82.73 macro accuracy versus 69.61 for the learned selector, revealing substantial headroom within the same spatial action space. Matched probing further shows that signals predicting when compression breaks the answer are substantially more accessible after language-model computation than to the lightweight prefill-free selector. These results expose complementary bottlenecks in region selection and compressed-region fidelity.

---


### 132. [SanSi: A Looped Typed Decision Model for System 1.5 Thinking](https://arxiv.org/abs/2610.07730)

**<font color=#1a73e8>作者：</font>** Shuyu Gan, Young-Jun Lee, Dongyeop Kang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Typed decision models answer a declared question without generating text: a decision head returns a probability for each of the declared options in a single forward pass. A single pass is fast, intuitive System 1 thinking. We study what lies between one pass and generated reasoning: looping, in which the same layers are recursively applied several times before one typed readout. Each loop lets the model revise its hidden state before it commits to an answer, without generating a token; we call this System 1.5 thinking. We propose SanSi, which turns a pre-trained looped language model into a typed decision model. The option probabilities are read after every loop, and every loop is trained with a proper scoring rule, so that one model serves every budget from one loop to eight in a single run. On 10,027 test decisions from 59 sources, SanSi reaches 72.0% accuracy: 13.5 points above a non-looped model of the same shape trained with the same recipe, 5.3 points above a newer non-looped model of its size, and 1.8 points below one with three times the parameters. On two depth-controlled tasks, loops extend the solvable depth beyond the depths seen in training, where the larger single-pass model fails. Used as the judge for policy optimization with reinforcement learning, without gold answers, SanSi raises the generator's F1 by 7.7 points.

---


### 133. [Who Is Talking to the Agent? LLMs in Multi-User 3D Virtual Environments](https://arxiv.org/abs/2610.07732)

**<font color=#1a73e8>作者：</font>** Mohammad Al-Ratrout, Shayla Sharmin, Roghayeh Leila Barmaki  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> When several people share a 3D virtual room with an LLM agent, the agent must decide not only what to say, but whether an utterance was addressed to it and, if accessible, what profile information about the others present it may use. To study both problems, we construct LookAway, a controlled corpus of 40 sessions involving 80 distinct personas and an LLM agent (1,200 turns), including ambiguous-addressee turns in which speaker orientation agrees or conflicts with the intended addressee. Across three open-weight large language models and five conditions varying which profiles the agent sees and whether it is told where each person faces (18,000 decisions), adding speaker orientation increased addressee accuracy from 56% to 99.5% when orientation was congruent, but when the speaker faced someone other than the addressee, two of the models went by where the speaker faced on more than 85% of those turns. Warning one model that orientation could be misleading reduced this only modestly. A browser-based 3D demonstrator shows the effect live: the same sentence gets an answer when the speaker faces the agent and silence when they face the other person. Providing both personas' profiles improved responses about the person being asked about, but also increased the use of profile attributes not revealed in the shared conversation, reaching 45.3% of answers for one model. More context thus improves multi-user interaction but also leads to oversharing, so shared LLM agents need mechanisms for weighing spatial cues and controlling when user-specific information enters a response.

---


### 134. [Cite What You Explore: Budget-Aware LLM Reasoning over Medical KGs with Verifiable Evidence](https://arxiv.org/abs/2610.07739)

**<font color=#1a73e8>作者：</font>** Chen Chen, Dongjie Wang, Mei Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-discharge risk prediction from electronic health records (EHRs) is difficult because many dependencies that link discharge-time observations to downstream complications, such as comorbidity cascades and drug-disease interactions, are absent from the record. External medical knowledge graphs (KGs) can supply these missing dependencies, but tracing them demands three properties: KG exploration must remain cost-bounded, retrieved evidence must be differentiated by source quality, and the resulting rationale must be citable for retrospective review. Large language models (LLMs) can plan and verify over structured evidence, making them natural candidates for KG reasoning, but existing LLM-based methods do not satisfy these three properties jointly. In this paper, we propose BAR, a Budget-Aware LLM Reasoning framework over medical KGs with three contributions. First, BAR refines the raw KG into disease-specific evidence graphs whose edges carry support scores and provenance records, turning the KG into a quality-annotated reasoning space rather than a static feature source. Second, an LLM then reasons over this graph through a plan-navigate-verify loop that decomposes the question into steps, retrieves evidence under a patient-specific budget, and revises when verification fails. Third, a reasoning policy is trained with a reward that compares predictions with and without acquired evidence, combined with acquisition cost and citation-integrity terms. Across 8 diseases and 3 prediction horizons on MIMIC-III and MIMIC-IV, BAR improves AUPRC by 3.4 points over the strongest baseline, raises citation precision from 59.8% to 77.9%, and consumes only 62-65% of the budget cap.

---


### 135. [A Pedagogically Demonstrative Model Visualizing the Pathway from Online Interactions to Personalized Recommendation](https://arxiv.org/abs/2610.07744)

**<font color=#1a73e8>作者：</font>** Sushmita Khan, Connor Pennington, Bart P Knijnenburg  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Personal digital activity increasingly shapes online experiences, yet few users have been educated regarding the processes transforming raw interactions into personalized suggestions. We developed an education artifact that illustratively simulates how AI leverages users' digital activities to shape online recommendations (e.g., ads). Our artifact processes users' digital activity using a locally-hosted LLM to generate user profiles of their inferred interests and personalized recommendations. A three-layered Sankey diagram maps data sources through inferred interests to personalized recommendations. Interactive filters enable users to explore how different combinations of data sources influence personalized outcomes. This paper describes the artifact and its educational value, and reports findings of a pilot think-aloud study with six young adults. We find that the artifact effectively taught participants the conceptual relationship between digital activities and personalized recommendations. While this did lead participants to develop privacy awareness, they anticipated minimal behavior change due to the perceived unavoidability of platform participation.

---


### 136. [How Well Do LLMs Reason with Noisy Evidence? An Active Visual Reasoning Benchmark](https://arxiv.org/abs/2610.07751)

**<font color=#1a73e8>作者：</font>** Bach Nguyen, Zhaonan Li, Mau Son Nguyen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world reasoning rarely reduces to static question answering: agents must actively gather information from tools and sensors that are often noisy and unreliable. Yet most existing active reasoning benchmarks assume that environmental feedback is trustworthy, or introduce noise without exposing an explicit, calibrated uncertainty signal, leaving open how LLMs should reason when the evidence itself is uncertain. We introduce VisualNoiseQA, a novel benchmark for active reasoning under noisy visual feedback. A text-only LLM must solve VQA problems by iteratively querying a fixed, off-the-shelf VLM treated as a stochastic visual sensor. For each query, we draw multiple samples and expose an empirical uncertainty signal via self-consistency, enabling the reasoner to probe from different angles and decide what to ask next and when to stop. Our construction is automatic and scalable: starting from diverse VQA sources and two noisy VLMs, we retain only questions where the sensor is inconsistent yet human-solvable. We evaluate multiple LLM reasoners on 1,000 instances spanning perception, chart understanding, and knowledge-intensive reasoning. VisualNoiseQA thus provides a controlled playground to study how different LLMs exploit uncertainty signals for robust reasoning.

---


### 137. [From Evidence to Action: How Tool-Using Agents Fail](https://arxiv.org/abs/2610.07753)

**<font color=#1a73e8>作者：</font>** Hongzhan Lin, Shidong Cao, Ziyang Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool-using agents make consequential changes to external state, yet correct outcomes do not guarantee that their actions were supported by evidence established beforehand. We study where this evidence-to-action chain breaks as agents move from deciding whether to act to executing single actions and dependent workflows. Across ten model-harness configurations, strong static action assessment can coexist with much weaker interactive execution. Failures often begin before execution: agents stop with incomplete investigation or act before required evidence is established. Once required evidence is obtained, single-action execution is usually reliable, while multi-action workflows additionally expose unresolved prerequisites and incomplete execution. For this analysis, we introduce SafeActBench, comprising 656 cases across six operational domains and five protocols that progress from static action judgment and investigated non-action to single- and multi-action workflows. A provenance-bound Evidence Ledger and deterministic trajectory evaluator track what information was established, when actions occurred, and whether downstream dependencies were satisfied. These results show that failures arise not only from missing information, but also from how agents use established evidence when deciding and executing actions.

---


### 138. [ST-Bench: A Spatial-Temporal Benchmark for Multi-Agent System Generation on Scientific Research Tasks](https://arxiv.org/abs/2610.07763)

**<font color=#1a73e8>作者：</font>** Qi Cheng, Rongchao Dong, Shengyu Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid progress of LLM-based multi-agent systems (MAS) has shown that they largely outperform single agents on coding, math, and QA tasks, where executable tests provide a binary success signal. Whether this advantage transfers to real scientific data analysis remains untested. We introduce ST-Bench, a benchmark designed to answer two questions: whether MAS outperform single agents on complex scientific data analysis tasks, and if so, by how much and at what additional cost. ST-Bench contains 100 data science tasks adapted from published Earth science studies across hydrology, agriculture, and wetland methane research, expanded into 2,067 queries grounded in additional published studies and validated by domain experts. Using ST-Bench, we evaluate five recent MAS generation methods under two training protocols, against single-agent baselines on the same GPT-5 backbone. Nine of the ten MAS configurations exceed the cheapest single-agent baseline, with the strongest reaching nearly three times its composite score. This gain is primarily attributable to coverage: trained workflows produce realistic numerical metrics on a larger fraction of queries, while the quality of those metrics, conditional on producing realistic output, is comparable to that of the single-agent baseline. The strongest configuration requires approximately four times the single-agent inference time, whereas a more economical workflow captures the majority of the benefit at less than twice the cost. MAS specialization confers measurable benefit on scientific data analysis, but the benefit is conditional rather than universal.

---


### 139. [No Transformer Beats Six Covariates: Long-Horizon Prediction of Depressive Symptoms from Childhood Essays](https://arxiv.org/abs/2610.07764)

**<font color=#1a73e8>作者：</font>** Daniel Kua, Emrul Hasan, John-Jose Nunez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural language processing (NLP) models can detect depression-related language in text written near the time symptoms are measured, but whether pretrained transformers can predict depressive symptoms from text written twelve years earlier is largely untested. In the National Child Development Study, a British birth cohort, we predict probable depressive symptoms at age 23 from essays the same people wrote at age 11. Our baseline, a logistic regression on six childhood covariates, outperforms every text model that sees only the essay: seven fine-tuned transformers, a bag-of-words model, frozen embeddings and four zero-shot large language models. Its area under the receiver operating characteristic curve (AUC-ROC) is 0.737 against 0.670 for the best transformer on the primary seed, and no added text score detectably raises the baseline's AUC-ROC. None of the five domain-pretrained transformers detectably beats its general-domain control after Bonferroni correction. For long-horizon prediction, the baseline remains the model to beat.

---


### 140. [OTel: Open Telco AI Datasets, Benchmarks, and Models](https://arxiv.org/abs/2610.07766)

**<font color=#1a73e8>作者：</font>** Farbod Tavakkoli, Gregory Diamos, Kenneth Church 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Open Telco (OTel), an open telecom AI resource that releases derived telecom datasets for retrieval, reranking, instruction tuning, and safety/abstention, together with 30 full-parameter post-trained baselines spanning 10 embedding models, 3 rerankers, and 17 language models. The community has already engaged substantially with the resource: as of May 3, 2026, the released models have been downloaded over 16 million times and the project has received 157+ pieces of media coverage worldwide. Building on prior open telecom datasets and benchmarks, OTel provides documented telecom data sources, held-out evaluation partitions, trained embedding models, rerankers, context-grounded LLMs, and safety/abstention data in one unified resource. Each baseline starts from an open-weight model and is post-trained on OTel-derived data using an open training recipe, then evaluated on held-out OTel evaluation partitions. OTel post-training improves performance across all three model families: embedding retrieval reaches 93.1% NDCG@10, reranking reaches 0.947 MRR@10, and language-model correctness reaches 87.8%. We release OTel as a reproducible starting point and invite the community to expand the data, improve embedding and reranking models, and build stronger context-grounded telecom LLMs.

---


### 141. [TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning of MoE Language Models](https://arxiv.org/abs/2610.07767)

**<font color=#1a73e8>作者：</font>** Xin Wang, Hao Yu, Zhengyang Zhuge 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) for post-training large language models (LLMs) incurs substantial computation and memory overhead during rollout generation, which motivates low-precision rollout for efficient RL training. However, existing FP4 RL methods suffer from a key limitation: they primarily optimize quantization accuracy on the training and rollout paths independently rather than directly reducing the discrepancy between the two quantized execution paths. In this work, we propose TRACE (Train-Rollout Quantization Alignment via Compact GuidancE), an FP4 quantization framework for RL training of Mixture-of-Experts (MoE) language models that addresses the limitation of existing FP4 RL methods. TRACE incorporates rollout-guided quantization-aware training that uses rollout-side quantization outcomes to guide training-side FP4 rounding decisions, directly reducing train-rollout discrepancy. Moreover, TRACE adopts an efficient quantization-information caching scheme that selectively retains mantissa and scale information from deeper layers to reduce the storage and communication overhead introduced by rollout guidance. We evaluate TRACE on four large-scale MoE language models across reasoning, coding, and long-horizon RL tasks. Our results demonstrate that TRACE enables joint FP4 weight/activation and FP4 KV-cache rollout with RL performance comparable to BF16 rollout, while achieving up to 5.4xrollout speedup and strong final FP4 performance compared with post-hoc FP4 quantization of BF16-trained policies.

---


### 142. [Reading, Not Manipulating: Leveraging Router Logits for Multimodal Safety in MoE Vision-Language Models](https://arxiv.org/abs/2610.07774)

**<font color=#1a73e8>作者：</font>** Ziyuan Yang, Wenxuan Ding, Shangbin Feng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) face compositional safety risks where harmful intent emerges from the interaction between visual and textual inputs. As mixture-of-experts (MoE) VLMs become increasingly common, recent work has explored various safety interventions, including prompting, supervised fine-tuning, and routing-based expert steering. However, these methods show inconsistent improvements across models and evaluation distributions, and the intervention into model behavior or internal states introduce safety-utility tradeoffs by over-refusal. Rather than manipulating internal states to steer model behavior, we instead ask whether routing states can serve as diagnostic signals for multimodal safety. We find that router logits indeed provide highly predictive signals of whether a multimodal input is safe or not. Motivated by this observation, we introduce a lightweight router-logit safety detector that reads out routing signals during prompt prefill and identifies unsafe requests before generation, without modifying model parameters or expert routing. Across Qwen3-VL and Kimi-VL, the proposed detector substantially reduces safety errors on the HoliSafe benchmark and resoundingly generalizes to out-of-distribution safety benchmarks featuring different safety patterns, including MISHard and MM-SafetyBench. The success of the proposed router-logit detector also suggests a broader perspective on model internals: rather than focusing only on manipulating internal components to steer behavior, simply reading naturally emerging signals and linking them to an external safety mechanism can provide a simple, effective, and non-intrusive complement to existing safety interventions.

---


### 143. [APEX: Speculate smarter, not deeper](https://arxiv.org/abs/2610.07780)

**<font color=#1a73e8>作者：</font>** Manvi Jha, Zach Zhang, Zhichao Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding reduces large language model inference latency by drafting multiple tokens before target-model verification, but its effectiveness depends on both the proposal mechanism and draft depth. Fixed configurations cannot respond to changes in predictability, repetition, and acceptance during generation, so deeper drafting can increase wasted computation without proportional speedup. We introduce APEX, a learned controller that balances decoding speed and draft-token waste through request-level expert selection and block-level depth adaptation. APEX-Router selects among EAGLE-3, n-gram, and draft-model speculation for each request, while APEX-Depth adjusts draft length at each verification block using causal decoding signals and recent verifier feedback. APEX models accepted draft length as censored survival feedback, learning position-wise rejection hazards, block execution costs, and an action utility that balances throughput, accepted progress, and wasted tokens. This allows the controller to adapt speculation while retaining the target model's verification procedure. We integrate APEX into vLLM and evaluate it with Qwen3-8B across six workloads, achieving up to 5.24X speedup over autoregressive decoding. Across the aggregate evaluation, APEX-S achieves 4.27X speedup, while APEX-B achieves 3.27X speedup with a 41.0% relative reduction in wasted-token percentage compared with fixed n-gram speculation at k=16, providing distinct operating points for balancing acceleration and draft-token utilization.

---


### 144. [Quantization Effects on Tool-Failure Recovery Vary Across Prompts and Evaluation Designs](https://arxiv.org/abs/2610.07781)

**<font color=#1a73e8>作者：</font>** Yuhe Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-training quantization reduces the cost of deploying language-model agents, but its effect on recovery from temporary tool failures can depend on how recovery is evaluated. We compare 8-bit and 4-bit variants of Llama-3.1-8B-Instruct and Qwen2.5-7B-Instruct on twenty deterministic tool-use tasks and five prompts. The 8-bit-4-bit recovery comparison changes direction across prompts and evaluation targets. On tasks that both variants complete without faults under the same prompt, the difference ranges from 0 to +20.2 percentage points for Llama and from -50.0 to +35.0 points for Qwen. Full-pipeline point estimates favor 8-bit Llama under all five prompts, whereas the Qwen comparison changes direction across prompts. The evaluation target can also reverse the result. For Llama under one prompt, scoring each variant only on its own clean-passing tasks favors 4-bit by 17.5 points; scoring the same tasks for both variants gives no difference, while scoring the full pipeline favors 8-bit by 28.3 points. Executor leniency is a third such choice. Rescoring the same logs with strict output parsing, which 8-bit Llama violates far more often than 4-bit Llama under that prompt, turns that +28.3 into -15.0 while leaving Qwen essentially unchanged. These findings show that one prompt, one screened task set, and one scoring policy do not establish a stable conclusion about quantized-agent robustness. Evaluations should compare variants on matched tasks, report full-pipeline success for deployment decisions, state the scoring policy, and quantify uncertainty across tasks rather than injected fault sites.

---


### 145. [Persistent Memory in Multi-Agent LLM Inference: What It Costs, What It Buys, and When You Can Tell](https://arxiv.org/abs/2610.07782)

**<font color=#1a73e8>作者：</font>** Hochan Son, Kyungdoe Han, Jaehan Koh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decomposing long-context inference across cooperating agents bounds the active KV cache per call rather than total evidence, which matters when KV-cache memory binds. Many such systems add a persistent tier storing and recalling reasoning traces, usually validated by an ablation reporting an accuracy gain. We measure both on one three-tier agent architecture. Decomposition delivers: peak KV working set of 14.3 MiB per query against 35.5 and 35.3 MiB for single-pass and retrieval-augmented baselines. The persistent tier does not: across eight controlled dataset pairs at n=100 per arm it costs +0.368 MiB [+0.167, +0.590] of peak cache and produces no detectable accuracy change (+0.015, 95% CI [-0.011, +0.046]). We argue the null is structural: single-question benchmarks supply each item with its own evidence and score it independently, and correctness requires resetting stored traces between conditions, so recall has nothing informative to retrieve. Reaching it took four measurement corrections -- three inflating the apparent benefit, the fourth making an effect that size look resolvable -- none visible in the results table. We give the conditions an agent-memory ablation must satisfy and detection procedures that need no knowledge of the specific defect.

---


### 146. [OOPMAS: Object-Oriented Multi-Agent Systems for Query-Level Workflow Generation](https://arxiv.org/abs/2610.07787)

**<font color=#1a73e8>作者：</font>** Qi Cheng, Shengyu Chen, Wei Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) powered by large language models have shown strong performance across code generation, mathematical reasoning, and question answering. However, existing methods for automating MAS design mostly operate at the task level, producing a single fixed workflow per benchmark that is applied uniformly to all queries. This assumption fails under realistic conditions. Query difficulty varies widely within a task, and real-world workloads mix heterogeneous task types. We introduce OOPMAS, a training-free framework that generates both the agent set and the coordination workflow at the granularity of individual queries. Agents are represented as object-oriented class definitions with dedicated roles, tools, and persistent state, and workflows are expressed as executable main functions over these agent objects. A dynamic skill library accumulates structured lessons from execution feedback across optimization rounds, enabling in-context improvement without any gradient updates or fine-tuning. On a mixed-task benchmark of queries spanning code, math, and QA, OOPMAS achieves 89.6% accuracy, outperforming the strongest baseline by 18.1 percentage points. A model-swap study across four LLM backbones shows consistent scaling, reaching 92.4% with the strongest model.

---


### 147. [Illusory Pattern Perception Drives Spurious Inference in Large Language Models](https://arxiv.org/abs/2610.07791)

**<font color=#1a73e8>作者：</font>** Peihua Mai, Zhuoyan Shao, Xinbao Qiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Illusory pattern perception is a well-documented human cognitive tendency to infer meaningful relationships in data that is actually random. Such a tendency, often described as "connecting the dots" where none exist, can result in systematic reasoning errors. This paper investigates whether Large Language Models (LLMs) exhibit such perceptual tendencies, which can lead to systematic errors in downstream applications. To our knowledge, this work presents the first systematic study of illusory pattern perception in LLMs, adapting classic psychological paradigms to three tasks with direct empirical comparison to human behaviors. We find that LLMs frequently exhibit stronger illusory pattern perception than humans. In particular, models tend to over-associate frequent positive attributes with majority groups or large organizations, and show increased tendencies to construct causal narratives from ambiguous events. To uncover the mechanism behind these behaviors, we develop a feature interpretability framework based on Sparse Autoencoders (SAEs) to analyze internal representations. Our results reveal that holistic frequency perception and analytic cognitive orientation are linked to the emergence of illusory perceptions. These findings highlight a previously underexplored cognitive-like illusion that may affect the reliability of LLM reasoning. Code available at this https URL.

---


### 148. [ServeLearnBench: How Well Can Agents Self-Improve from Serving Experience?](https://arxiv.org/abs/2610.07792)

**<font color=#1a73e8>作者：</font>** Haizhong Zheng, Yizhuo Di, Ranajoy Sadhukhan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model agents are increasingly deployed to perform complex tasks in real-world environments. However, the knowledge required for correct behavior in these environments is often implicit, undisclosed, and subject to change over time. Recent continual-learning harnesses seek to address this challenge by enabling agents to improve from serving experience. Yet the effectiveness and limitations of these methods are not yet well characterized. Existing benchmarks provide only partial coverage: some explicitly provide the target knowledge, others assume a static environment, and those that support continual adaptation remain limited in scale and knowledge diversity. To enable systematic evaluation, we formalize an evolving-environment streaming dataset (EESD), in which agents must infer, apply, and revise latent environment knowledge from interaction and outcome feedback as hidden policies evolve, and introduce ServeLearnBench, spanning retail support, banking, and sales-pitch generation with 53 environment windows and 7,718 tasks. We evaluate five learning harnesses (RAG, Mem0, SkillOpt, Continual Harness, and Prime) across six models (GPT-5.6 Terra, Opus 5, Kimi K3, GLM-5.3, DeepSeek V4.1 Flash, and GLM-5.3 Flash), covering 28 model-harness pairs and 252 learning runs. Our evaluation reveals three main findings: a substantial gap remains between task capability and learning from experience; continual adaptation is costly and can degrade already-correct behavior; and insufficient exploration emerges as a key bottleneck to effective adaptation. Overall, ServeLearnBench provides a controlled testbed for diagnosing these limitations and tracking progress toward agents that continually and reliably improve through serving experience.

---


### 149. [Thin Evidence, Thick Priors: How Language Models Substitute Identity for Missing Financial Facts](https://arxiv.org/abs/2610.07798)

**<font color=#1a73e8>作者：</font>** Saanvi Khetan, Sankar Balasubramanian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> People increasingly ask large language models what to do with their money, yet seldom describe their finances in full. This paper asks what a model does with the gap. Holding finances fixed and changing only who the investor is said to be, we grade the financial evidence in the prompt from eight facts to none and measure how far the recommended equity allocation moves. Across 96,600 prompts to Llama-3.1-8B-Instruct, built from 100 financial profiles, 138 personas and seven disclosure conditions, the average gap between two personas with identical finances rises from 4.78 percentage points at full disclosure to 10.34 points with no financial facts. A two-way cluster bootstrap counting duplicated prompts once places the ratio at 2.16 (95% interval 1.69 to 2.79), and the rise is already 1.69-fold with a single fact left. Identity explains 5% of within-profile variation in advice at full disclosure and 96% with no disclosure. Household size is the only attribute whose influence grows reliably as evidence is withdrawn. Once standard errors are clustered on the persona, the unit to which identity was assigned, most attribute-specific interactions reported in the conference version lose significance, and gender instead appears as a small standing gap that full disclosure does not close. Stating risk appetite alone brings the swing into the range seen with two to seven generic facts. With no facts, the model's one-line rationale cites incomes, debts and savings it was never told, and these invented finances turn adverse more often for larger households. Inside the network, gender is linearly decodable at every layer, and ablating the gender direction at five layers leaves the aggregate identity swing unchanged. Advisory systems built on such models should be audited at the disclosure levels users actually reach, and judged across the whole identity space rather than one attribute at a time.

---


### 150. [ThinkFuse: Trajectory-Aware Test-Time Fusion for Small Reasoning Models](https://arxiv.org/abs/2610.07803)

**<font color=#1a73e8>作者：</font>** Myunghoon Kang, Jungseob Lee, Jaehyung Seo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Small reasoning models (SRMs) have shown strong performance on complex reasoning tasks by generating extended chain-of-thought trajectories, but they often fail to recover once their reasoning enters an erroneous path. Existing test-time fusion methods rely on local fusion signals to determine when to trigger fusion, which can be misled by transient uncertainty fluctuations and may reinforce unstable reasoning trajectories. We propose ThinkFuse, a training-free test-time fusion framework that selectively intervenes in unreliable reasoning segments. ThinkFuse compares segment-level uncertainty shifts with trajectory-level uncertainty trends to identify unstable reasoning points and fuse auxiliary reasoning paths into the primary model's trajectory. Extensive experiments demonstrate that ThinkFuse outperforms baselines on mathematical and knowledge-intensive reasoning benchmarks, with consistent gains across model-family combinations, and remains robust with a smaller primary model. Our analysis shows that ThinkFuse requires fewer fusion triggers and generates fewer tokens, highlighting the efficiency of selective triggering. Our code is available at this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-303](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
