# 🧠 大模型相关研究 | 2026年08月14日

> 本类共 **164** 篇论文：已确认 **147** 篇，待复核 **17** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-164](./part-04.md)

---

### 1. [Dynamic Governance of Multi-LLM Agent Systems for Collaborative Conversational Outcomes](https://arxiv.org/abs/2608.11207)

**<font color=#1a73e8>作者：</font>** Alexander Liss, Nicholas Desmond, Santiago Gil Gallego  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When two LLM agents with structurally opposed objectives interact across multiple turns, the absence of a shared goal function produces not competition but collapse: the visitor capitulates, the site agent stops varying its approach, and the conversation terminates without achieving either agent's stated objective. This paper asks whether a control-theoretic governance layer can substitute for that missing goal function. The Experience Orchestrator (EO) addresses this in a simulated financial services environment where a site agent guides a visitor toward advisor contact while the visitor maintains psychologically realistic resistance. EO governs the joint trajectory through three mechanisms: a Contextual Bandit (CB) that selects content arms calibrated from real-world web analytics, a PID controller that enforces behavioral consistency via dynamic schema constraints, and a POMDP belief tracker that maintains a probabilistic model of visitor intent. Across 60,000 simulations, EO achieves a +32 percentage point lift in high-intent advisor contact rate (78.1% vs. 46.1% over a naive LLM control), with CB variant selection accounting for 97% of between-factor outcome variance -- confirming that the governance policy, not environmental initial conditions, determines where trajectories end up. Persona-level analysis reveals two distinct regimes: for visitors with no natural inclination toward conversion, the governance layer is the difference between a functional system and a non-functional one; for visitors already near alignment, a naive LLM's empathetic defaults are largely sufficient. All findings are conditional on LLM-to-LLM simulation. The PID controller has not been calibrated against real human unpredictability, and validating EO on live traffic is the critical next step.

---


### 2. [Distribird: Literature-Informed Prior Distribution Design for Bayesian Model Calibration](https://arxiv.org/abs/2608.11210)

**<font color=#1a73e8>作者：</font>** Patrik P. Süli, György Eigner, Roland Hollós  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Bayesian calibration of process-based models requires a prior distribution for each model parameter. Despite decades of methodological work, researchers almost always fall back on uniform priors. The main reason is that building informative priors from scientific literature is slow and needs both domain and statistical expertise. We present \textbf{Distribird}, an agentic web application that automates this process. Given a parameter name, physical description, and domain context, Distribird deploys a multi-agent pipeline that searches the literature, extracts and weights reported values by domain relevance, and fits a probability distribution via AIC model selection. When no literature is available, the system falls back to sensible uninformative alternatives, and clearly reports both the evidence behind and the confidence level of every prior it produces. It is designed for the problems where the models have physically interpretable parameters, where domain knowledge exists in the published literature. We evaluate the tool on 24~parameters across 10 scientific domains comparing three open-weight models (Qwen3.6 27B, Gemma 4 31B, Mistral Small 4 119B) with a single-prompt LLM baseline. On prior quality the full pipeline \emph{matches} this baseline. Every prior is traced to the specific papers and values from which it was constructed; a built-in validity layer declines to produce priors for out-of-scope requests, whereas the single-prompt baseline returns confident but unfounded priors for them in 11 of 30~model--parameter cases; and every language-model call runs locally, so no parameter description or unpublished modelling detail is transmitted to a third-party LLM provider (only generated search terms reach the public literature databases). For scientific use, we argue these properties matter more than a marginal improvement in point-estimate accuracy.

---


### 3. [Detecting a Route Flip Is Easier Than Knowing Whether to Fix It: Causal Route-Mediated Damage in Quantized Mixture-of-Experts](https://arxiv.org/abs/2608.11212)

**<font color=#1a73e8>作者：</font>** Parvel Gu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Top-k Mixture-of-Experts (MoE) routing is discontinuous, so a deployment-motivated numerical disturbance -- simulated 4-bit KV-cache quantization read by a protected BF16 gate -- pushes tokens across decision boundaries and flips which experts fire. This paper proposes no new mitigation; it supplies a causal apparatus, empirical findings, and a detection-limit result. A four-run apparatus prices the route-mediated fraction (RMF) of quantization damage, a token-level attribution decomposes it by mechanism, and pre-registered probes carry the findings across three architectures. On OLMoE-1B-7B at 4-bit KV (pilot), about a third of the damage is routing-mediated: RMF ~ 0.31 (discovery 0.31 [0.20, 0.41]; process-replicated mean 0.313 +/- 0.020; pre-registered re-execution 0.231). The deployable router margin detects that a flip occurred (AUC 0.772) but cannot tell a harmful flip from a helpful one (at chance): among the tested local, inference-observable router statistics we find no predictor of a flip's loss sign above chance -- an empirical benefit-detection barrier bounding selective repair restricted to this feature family. The signed-flip tax and sign-inseparability carry cross-model; the clean-reference remedy's payout is architecture-modulated; a controlled same-checkpoint flag-swap re-scopes the gate's normalization convention to a damage-magnitude moderator, not a route-recoverability mechanism. A real int4 KV kernel yields a fraction compatible with the fake-quant dose curve but underpowered (95% CI [-0.111, 0.394] includes zero) -- ruling out gross disagreement, not an independent replication. Hypotheses, thresholds, and evaluations were pre-registered before measurement, with misses reported; a pre-registered held-out read replicates the partition and the near-cancelling tax out of sample, while the strict impossibility exclusion narrowly misses.

---


### 4. [Poor Man's Agentic Modeling: Simulating Large LLM-Agent Societies on a Laptop](https://arxiv.org/abs/2608.11215)

**<font color=#1a73e8>作者：</font>** Igor Itkin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Simulating societies of many large language model (LLM) agents is expensive, yet the questions asked of such simulations are usually macroscopic: phase behaviour, stylised facts, and scaling with the number of agents $N$, not the cognition of any single agent. We turn a statistical-physics observation into a method: replace each LLM agent by a low-parameter model fitted from a few hundred to a few thousand cheap queries, then run the society at any $N$ on a laptop. Whether this works is decided before the simulation runs, chiefly by what each agent perceives. We introduce an [interaction order x memory] taxonomy that maps perception and memory to an effective theory and a predicted $N$-trend of the surrogate error. We validate it on a faithful reimplementation of the LLM macroeconomy EconAgent and seven further named LLM simulations, with agent decisions cloned from genuine LLM elicitations (primarily DeepSeek) for a few dollars; the predicted error trends hold cell by cell, and the two refuted predictions, both on a strongly saturating response and traced to its curvature, are themselves matched quantitatively by the theory with no free parameters.

---


### 5. [AutoWorldModel-Bench: A State-Centric Benchmark for Automated World-Model Research](https://arxiv.org/abs/2608.11216)

**<font color=#1a73e8>作者：</font>** Marjan Moodi, Xuankang Zhu, Fernando De Mesentier Silva 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World modeling is an unsettled field: architectures, training objectives, and state representations interact in complex ways, and no single recipe dominates across environments. This makes it an ideal testbed for AI coding agents acting as autonomous researchers--a setting in which the improvement direction is not specified in advance, unlike the engineering-to-spec tasks that dominate current agent benchmarks. We introduce AutoWorldModel-Bench, a closed-loop benchmark in which frontier coding agents autonomously improve a provided world-model starter under a fixed compute budget. The benchmark spans eight game environments under a unified structured-state representation--ground-truth entity state extracted from each game and consumed through a shared tensor format--which isolates dynamics modeling from perception and enables minutes-per-run iteration. Across 64 sessions, Codex-5.4 and Claude Opus 4.6 improve their starter on 63; in 91% of sessions the winning edit is a non-trivial research-style modification--a new objective, representation, rollout procedure, or architectural change--rather than a hyperparameter tweak. Our benchmark offers a setting in which frontier coding agents can be evaluated on open-ended research rather than engineering-to-spec problems.

---


### 6. [From Monolithic to Modular: Segment-level Automatic Prompt Optimization](https://arxiv.org/abs/2608.11219)

**<font color=#1a73e8>作者：</font>** Nikita Kulin, Viktor Zhuravlev, Artur Khairullin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic Prompt Optimization (APO) often rewrites prompts monolithically, which can improve one behavior while degrading others. We present SAPO, a segment-level APO method that decomposes prompts into role, context, tasks, and output format, then applies targeted improvements based on top-5 and bottom-5 examples. The optimization loop uses one LLM with static meta-prompts and structured outputs for segmentation, weakness analysis, and candidate generation. We describe a train/validation protocol and a two-stage generation process: (1) segment-level diagnosis and recommendation extraction, (2) candidate synthesis constrained by weak/strong segment signals. Using the evaluation setup across SQuADv2, TweetEval, XSUM, CommonGen, and GSM8K on GPT-3.5-Turbo and GPT-4o-mini, SAPO achieves the best average score against Zero-shot and strong APO baselines including APE, OPRO, EvoPrompt, GEPA, and StraGO.

---


### 7. [LLMs in Process Diagram Engineering: From Optimal PFDs to Validated P&IDs](https://arxiv.org/abs/2608.11220)

**<font color=#1a73e8>作者：</font>** Timur Zakarin, Sergei Voitov, Sergei Shumilin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Nowadays, the creation of a process flow diagram (PFD) and its subsequent transformation into a piping and instrumentation diagram (P&ID) is predominantly performed manually. Applying artificial intelligence in the task could potentially lead not only to process automation and time savings, but also to financial gains by exploring numerous diagram's topology options and reducing manual labor. This research presents P&ID Pilot - a practical end-to-end AI pipeline capable of handling flowsheet developing for both stages. The first stage focuses on PFD synthesis, whereas the second is directed toward modifying the generated PFD into P&ID. After comparing four different methods, the hybrid approach combining genetic algorithms (GA) and large language models (LLM) is shown to generate the optimal valid PFD topology, achieving the lowest loss value among all the methods, while satisfying the required outlet flow parameters without engineering-rule violations. For the second stage, the proposed LLM-based agent successfully transforms the generated PFD into a source-grounded P&ID by producing validated, executable modifications through a restricted engineering software development kit, achieving 100% execution success while maintaining compliance with domain-specific rules and reference graph structures. This unified pipeline - coupling GA/LLM-driven synthesis with an LLM-based transformation agent - offers a feasible path toward end-to-end process design automation by producing validated, deployable outputs and substantially reduces manual engineering effort.

---


### 8. [Harnessing agent memory to build lifelong AI partners for materials scientists](https://arxiv.org/abs/2608.11224)

**<font color=#1a73e8>作者：</font>** Siyu Liu, Bo Hu, Beilin Ye 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Materials research advances through accumulated experience - scripts that work, protocols that are trusted, warnings attached to failed calculations or experiments, and judgement that links a new question to an old result. This experience is essential for reproducibility and knowledge transfer, yet it is usually fragmented across notebooks, repositories, job logs and individual memory, and it is rarely portable across artificial-intelligence agents. Here we argue that a lifelong AI partner for materials science can be designed around persistent memory rather than around a particular agent implementation. We introduce a self-evolving memory framework that stores scientific experience as inspectable facts and executable skills, so that observations, failure boundaries, protocols and validation checks can be retrieved, revised and migrated across models. We evaluate the idea in three computational settings that expose different layers of materials-research competence. In 49 real-world materials-tool-use questions comprising 138 executable subtasks, memory nearly doubles GPT-5.2 task success without model-parameter updates. In elemental-solid equation-of-state calculations, memory converts a wavefunction-initialization failure into a pre-execution guardrail, improving outcomes from 22/1/4 to 25/2/0 Correct/Partial/Error and avoiding 92% of repeated errors. In 13 practical material simulation workflows, remembered skills and failure facts halve the aggregate trace burden (tokens) and reduce tool calls by over a factor of two by the third round, while preserving physically meaningful outputs in band-gap, phonon, vacancy and work-function analyses. These results show that agent memory can serve as a durable scientific asset; a portable, self-improving record of materials-research experience that outlives any single model or agent stack.

---


### 9. [Cutting AI Datacenter Energy with Reinforcement Learning: Measured Power Control of LLM Training from One GPU to the Fleet](https://arxiv.org/abs/2608.11226)

**<font color=#1a73e8>作者：</font>** Eliseo Curcio  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement-learning post-training dominates modern language-model development, yet its power behavior on GPU hardware has not been characterized, and datacenters manage GPU power with workload-blind mechanisms, static caps and reactive throttling, that slow hardware indiscriminately. We instrument GRPO training with half-second power telemetry at 7B, 14B, and 72B scales on one to four A100s (380,000+ samples), and train a PPO meta-controller that adapts the workload's own generation parameters to measured power. Against the full 500-step 7B trace, the controller cuts power-limit violations by 89.8% while increasing token output by 18.1% and energy efficiency by 26.2% (tokens per MWh). Deployed live at 72B, the same controller family yields replicated null results, diagnosed as the group-size actuator losing authority under model sharding. An actuator-authority sweep shows the same parameters applied as generation concurrency retain 17-22% power authority, isolating an occupancy-versus-volume principle; a controller rebuilt on that actuator controls a live 72B rollout-generation workload across three replications: 35.7% more output than a static safe baseline at 2.27 +/- 1.08% budget violations, 87.2% fewer violations than uncontrolled operation, and the best mean throughput and energy per token among constrained controllers, with an adaptive threshold rule matching it in one of three operating conditions. Under realistic measurement windows the original 72B transients fall from 23.6% at half-second resolution to 1.6% at 30 s and zero at 5 min; a composed 16-GPU fleet shows zero violations at 30 s and longer, with peak demand at 50-56% of nameplate. For this fleet mix, roughly twofold oversubscription of nameplate appears feasible, subject to operator validation. We quantify the economic and carbon consequences and specify a low-cost operator pilot.

---


### 10. [Forecasting Side Effects of Activation Steering](https://arxiv.org/abs/2608.11227)

**<font color=#1a73e8>作者：</font>** Chong Yong Ong, Alson Wei Jie Sim, Peixin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Activation steering modifies a language model by adding a learned direction to its hidden activations, enabling targeted behavioral changes without retraining. While effective, steering often produces unintended side effects on other behaviors, making it difficult to deploy safely. We therefore ask: can these side effects be forecasted before steering is applied? We answer this question by constructing a cross-effect matrix over a taxonomy of 67 behaviors across three open-weight language models. We find that side effects are common, structured, and often asymmetric, revealing interactions that cannot be explained by existing similarity-based heuristics. Despite this complexity, we show that side effects are largely predictable before steering is performed. Their magnitude depends primarily on the target behavior, while their direction can be forecasted from the model's unsteered representations with substantially higher accuracy than simple baselines. Our results demonstrate that activation steering has systematic and forecastable side effects, enabling proactive safety auditing and more informed deployment of steering interventions.

---


### 11. [LinearKV: One Cached State Suffices for Position-Independent Caching in Hybrid LLMs](https://arxiv.org/abs/2608.11231)

**<font color=#1a73e8>作者：</font>** Yirui Liu, Ruoling Qi, Longwen Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM serving is increasingly accelerated by position-independent caching (PIC). Existing PIC methods, however, are built for full-attention models, where a token-indexed KV cache underlies its core operations: matching reusable token chunks, concatenating their KV entries, and selectively recomputing a few tokens to restore cross-chunk context. Hybrid LLMs break these primitives---they replace most attention layers with linear recurrences that expose only a fixed-size state, leaving no token-indexed KV to concatenate or to locally repair. This raises a natural question: can PIC benefit hybrid models, and what would it take? We present LinearKV, a training-free hybrid-PIC framework. Its key insight is a \emph{decoupled initialization}: each linear layer maps its $K$ matched local states to a single initial state, while full-attention layers concatenate their KV as before. LinearKV is therefore compatible with existing PIC methods, reusing their token selection and recomputation as-is. Under this framework, we find that a \emph{single cached state} suffices as the linear layer's initializer. The algebraically principled alternative---composing all $K$ cached states into the exact full-prefix state, as concurrent work HYPIC does---is unnecessary and, on some architectures, even harmful. We compare the two across three hybrid models and three PIC selectors. On the two GDN models the two tie, both recovering most of full quality (up to $92\%$); on the Mamba-2 model, exact composition instead collapses under every selector---under EPIC, for instance, it recovers only $46.6\%$ of full quality, versus $86.8\%$ for a single cached block initializer. A single state initializer is also cheaper, cutting time-to-first-token to $0.46\times$ full prefill versus a further $5$--$17\%$ overhead for exact composition; results hold across LongBench QA and RULER at 8K--32K.

---


### 12. [Backtrader-Bench: Benchmarking LLM Agents on Algorithmic Trading with Self-Generated MCQs](https://arxiv.org/abs/2608.11232)

**<font color=#1a73e8>作者：</font>** Ruoxi Zhao, Maziar Raissi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating LLM coding agents in algorithmic trading is difficult because static benchmarks risk data contamination and numerical backtest outputs require ground truth from actual code execution. We present Backtrader-Bench, a framework with two complementary pipelines. A deterministic multiple-choice question (MCQ) pipeline generates questions from backtest configurations across five trading strategies, 33 templates, and three difficulty tiers, with an independent checker that re-derives every answer. A generator-solver filtering pipeline autonomously mines harder questions: a generator writes questions verified by executable code, converts them to MCQs, and discards any that a no-tool solver can answer without code execution. We evaluate 11 models without tools (10 runs each) and four with-tools configurations on a 30-question curated set. Tool-augmented agents reach 90.0% accuracy in a single pass (GPT-5.5 and Opus 4.7), outperforming the best no-tools baselines (73.0%, averaged over 10 runs) by 17 percentage points. On 38 separately mined questions, no-tools accuracy drops further, with half the models falling to roughly random-chance level (25%). Beyond evaluation, the scalable MCQ infrastructure is designed to produce a training corpus for reinforcement learning, with the ultimate goal of building a specialized agent for quantitative trading workflows.

---


### 13. [Retrofitting Recurrent Depth into a Pretrained Language Model: Installation, Extrapolation, Transfer, and Retention at Two Parameter Budgets](https://arxiv.org/abs/2608.11233)

**<font color=#1a73e8>作者：</font>** Mark Shapiro  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A dense, pretrained language model can be retrofitted with recurrent depth and learn an iterative latent transition that persists after outcome-only annealing. Qwen2.5-0.5B-Instruct is split into a Prelude, a weight-tied Recurrent Block, and a Coda, with an identity-preserving one-loop path and a re-entry bridge on later loops. At loop 1 the retrofit remains non-inferior to its base on a preregistered ARC battery. Three findings. First, the mechanism is a reusable procedure rather than terminal-answer lookup, and installs at two budgets: 6M trained parameters over frozen base weights and 180M full-block. With intermediate-step supervision, the model computes one task step per loop and persists when only final answers are graded. The adapter matched the full block overall (83.8% versus 84.0%), led through depth 11, and trailed beyond. Verbal fine-tuning reached 79-86% on controlled verbal renderings (zero-shot transfer was minimal), and adapter verbal training begun from the installed mechanism outpaced matched fresh training by 18.6 points, including on a held-out test set. Second, the operation extrapolates to roughly 1.5 times its supervised depth, holding 70% accuracy through depth 18. Third, a same-size scratchpad-trained model matched the recurrent model within its learned horizon but collapsed beyond it. The recurrent model won overall, 84% versus 72%, retained 53% versus 2.5% beyond depth 10, and answered 7.6 times faster. An iterative transformer can therefore perform deeper reasoning in latent space faster than comparable or larger models fine-tuned on the same task, in a system-level comparison. A second task, running the rule in reverse, exposed the limits: the inverse was learnable in isolation, but no continuation acquired it while preserving the installed mechanism and general capability, a catastrophic-interference boundary. Learned depth selection remains open.

---


### 14. [CORA-Diff: Confidence-Oriented Residual Acceptance for Efficient Diffusion Language Model Inference](https://arxiv.org/abs/2608.11235)

**<font color=#1a73e8>作者：</font>** Yifan Wu, Yufeng Zhang, Kenli Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) update many tokens in parallel, yet practical decoders often use a fixed denoising horizon. Many predictions stabilize early, but blockwise decoding continues until all positions are resolved, causing repeated dense forward passes. Existing accelerators often rely on learned filters, modified scores, dependency models, or cache-specific mechanisms. We ask whether native trajectory signals can identify residual positions likely to match the deterministic dense endpoint. We propose CORA-Diff, a training-free method that preserves the original transfer rule and applies confidence-and-persistence gating only to positions that rule leaves unresolved. Accepted tokens remain visible as context, and the block terminates once all positions are resolved. This requires no backbone change, learned acceptance model, or logit modification. Our theory explains why high-confidence, persistent predictions are more likely to match the fixed-horizon dense endpoint, and paired post-intervention trajectories provide direct empirical support. We select one operating point on a separate GSM8K calibration subset and freeze it for all evaluations. Under a matched Learn2PD-style LLaDA protocol, CORA-Diff has the lowest measured runtime in all eight task-length settings. Task scores match or exceed dense decoding in five settings, and the largest observed drop is 1.22 points. Its incremental speedups over EOS-aware dense decoding are 2.70x and 3.32x on GSM8K and HumanEval. It also reaches 13.14x under the fixed-horizon 1024/1024 mechanism-isolation protocol and transfers to Dream without retuning at 3.18x-3.53x. These results show that native confidence and persistence enable reliable residual acceptance, reducing repeated denoising computation while preserving task quality.

---


### 15. [Towards Query-Agnostic RAG Evaluation via Query Coverage and Claim Verifiability](https://arxiv.org/abs/2608.11238)

**<font color=#1a73e8>作者：</font>** Jeonghwan Choi, Taewon Yun, Minjeong Ban 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation improves the factuality of large language models by grounding responses in retrieved evidence, yet existing evaluation frameworks struggle to provide consistent, fine-grained diagnostics across the diverse spectrum of user queries, ranging from close-ended fact-seeking to open-ended explanatory requests. We propose Q-CARE, a query-agnostic and fully reference-free framework that enables fine-grained assessment by decomposing queries into sub-queries and answers into atomic claims. Q-CARE establishes a unified evaluation principle based on query coverage and claim verifiability, yielding coverage-aware retriever metrics (C-Prec@k, C-nDCG@k) and claim-level generator metrics (Completeness, Conciseness, and Verifiableness). On a human-annotated benchmark spanning eight datasets, Q-CARE achieves higher correlation with human judgments than four existing RAG evaluation metrics, including RAGEval and RAGChecker, proving its effectiveness as a reliable, automated evaluation framework. Code and data are publicly available at this https URL.

---


### 16. [RecSys Factory: Bounding LLM Agent Autonomy to Decision Points in the Industrial Recommender Lifecycle](https://arxiv.org/abs/2608.11241)

**<font color=#1a73e8>作者：</font>** Dongyang Ao, Kaixiang Fang, Shijie Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying LLM agents into industrial recommender operations exposes a three-way tension we frame as the autonomy-determinism-efficiency trilemma: general autonomy (interpreting operator intent, generating glue code zero-shot), industrial determinism (schema-conforming feature extraction, non-crashing A/B, zero compliance-path hallucination), and end-to-end efficiency. Any two can be maximized against the third. We present RecSys Factory, an LLM-agent platform deployed for 78 days across three heterogeneous Tencent recommender business lines. The design principle is autonomy at decision points, not over pipelines, made concrete through three deconstructions that each discharge one vertex of the trilemma. Runtime is deconstructed into three host-emitted event sources (Claude Code Stop hooks, corporate-IM webhooks, workflow scheduler APIs): the platform carries no long-running daemon during the wait phase and consumes zero CPU during the 94% of wall-clock spent waiting on Spark or GPU jobs. Capability is deconstructed into a 29-file skill ecosystem (8,971 lines of this http URL) whose per-skill pitfall tables mechanically compile into a 400-entry PitfallStore, confining autonomy to bounded typed decision surfaces inside pre-committed pipelines. Deployment spans three business lines with disjoint label semantics, A/B layer topologies, and operator personas; an onboarding-time compression is observed on two of the three and is reported as a case-study observation, not a generalization claim, and not measured against a controlled pre-platform baseline. The human is retained at the diagnostic-versus-execution boundary via a human-in-the-loop card protocol, deployed as an audit-trail primitive (schema-validated, idempotent, replayable) and reported from an 8-day 16-run pilot. Across the 78-day window the platform recorded 1,624 CLI-tool dispatches at a 78.6% aggregate success rate.

---


### 17. [Lost in Compaction: Evaluating Side-Constraint Loss under Context Compaction](https://arxiv.org/abs/2608.11242)

**<font color=#1a73e8>作者：</font>** Zhiqi Wang, Yichi Zhang, Dongwon Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When the context window is under pressure, LLM systems compact prior context to continue ongoing tasks. We identify a class of user-issued instructions, Session Constraints (SCs), such as "do not delete any emails until I confirm," that are meant to constrain LLM's behavior for the remainder of a session but are silently dropped during compaction. To quantify this loss, we introduce COMPINT, an evaluation suite that evaluates compactors across three long-context scenarios: multi-turn chat, agentic trajectory, and long-horizon research.
Current compactors retain only 17% of injected SCs on average, and most perform worse than running the same task without compaction. Retention varies sharply with compactor, prompt, context length, SC phrasing, and injection location, showing that the loss is systematic rather than tied to any single setting. We propose an SC-aware extractor that runs alongside the compactor as a plug-and-play module, achieving over 90% retention across all three scenarios without modifying the compactor or LLM. The COMPINT evaluation suite and accompanying implementation are available at this https URL.

---


### 18. [BEST-KAG: Enhancing Question Answering of Building Engineering Standards with Multimodal Knowledge Graph Modeling and Large Language Model](https://arxiv.org/abs/2608.11244)

**<font color=#1a73e8>作者：</font>** Jia-Rui Lin, Junxi Guo, Keyin Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Construction standards are critical for building safety and sustainability. Existing standard application workflows rely on keyword-based document retrieval and manual cross-clause interpretation, which cannot reliably support multi-clause reasoning, multimodal knowledge utilization, or traceable clause-level evidence linkage. To address these limitations, this study develops a multimodal knowledge-driven framework that supports question answering on standard knowledge named BEST-KAG (Knowledge-Augmented Generation for Building Engineering STandards). The framework introduces 1) a multimodal knowledge graph (MKG) for unified representation of document hierarchy and heterogeneous standard knowledge with various connections, 2) a rule-LLM hybrid knowledge construction pipeline for scalable multimodal knowledge extraction, creating a large MAG with 251 building engineering standards, 171,652 nodes and 310,914 edges, and 3) a graph-retrieval-based knowledge-augmented generation architecture for clause-grounded and traceable question answering. Experiments demonstrate that BEST-KAG consistently outperforms multiple mainstream LLMs in terms of Expert evaluation, and metrics including BLEU, and ROUGE, with the best improvement up to 74.01% compared to the baselines.

---


### 19. [Towards the Harness of Embodied Agents](https://arxiv.org/abs/2608.11246)

**<font color=#1a73e8>作者：</font>** Qi Wang, Tianyi Wang, Chengyang Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The success of coding agents has established the harness as a paradigm: what an agent achieves depends not on the model alone, but on the infrastructure around it. We ask whether the same paradigm extends to embodied agents in the physical world. We present Thea, a harness in which an agentic loop orchestrates robot capabilities, each wrapped as a callable tool. It inherits the core components of coding agents, modified as the physical world requires. The world, however, withholds two abilities that software grants for free: reading the state of the world, and judging the outcome of an action. To bridge these gaps, Thea introduces Scene Graph as Context, a persistent, symbolic representation of the world, and Evaluation as Exit Codes, which detects when an action should terminate, judges whether it succeeded, and on failure diagnoses the cause. Together they close the loop between the agent and the physical world. Rich behaviors then emerge from the composition of tools, and the closed loop carries long-horizon tasks to completion in real environments.

---


### 20. [Conformity Mitigations in Large Language Models Lie on a Single Resistance-Receptivity Frontier](https://arxiv.org/abs/2608.11247)

**<font color=#1a73e8>作者：</font>** Zafar Hussain, Kristoffer Nielbo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in language models have enabled collaborative settings in which multiple models leverage one another's capabilities, iteratively improving, transforming, and extending each other's outputs. Each agent sees what the others assert before it answers, so peer opinion competes with the model's own parametric knowledge, and a wrong majority can overturn an answer the model would otherwise get right. We measure that displacement in 23 open-weight models, 19 conditions, and three datasets, yielding more than a million graded responses. A unanimous wrong majority reverses 22.8% of a model's correct MMLU answers, 54.8% on GPQA and 71.0% on SimpleQA, and 84-89% of the reversed answers match the peers' answers. Existing mitigations aim to increase Resistance, the rate at which a model keeps its correct answer under this pressure, which is only half of what a collaborating agent needs. We pair it with Receptivity, the rate at which a model adopts a correct peer answer after initially answering incorrectly. We score six methods on both axes, four drawn from prior work and two of our own. Each gains Resistance only by losing Receptivity, and their means fall on a single Resistance-Receptivity frontier with $R^2$ between 0.80 and 0.90. Reflection, the strongest published method, gains 7.9 points of MMLU Resistance and gives up 15.3 of Receptivity. Reasoning is the one exception. On GPQA and SimpleQA it trades like the rest, but on the MMLU subjects whose answers a model can derive for itself it raises Resistance by 7.2 points and Receptivity by 9.6 at once, the only intervention we find that improves both.

---


### 21. [EvoGraph-Mem: Failure-Aware Editable Graph Memory for Long-Term Language Agents](https://arxiv.org/abs/2608.11248)

**<font color=#1a73e8>作者：</font>** Yuxi Qian, Yuxiang Ren  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory is essential for language agents operating across extended interactions and evolving tasks. Existing memory-augmented agents mainly focus on storing and retrieving past experience, but the quality of stored memories may degrade over time. In particular, previously distilled insights can become outdated, over-generalized, or harmful under new task contexts, causing memory pollution when repeatedly reused. To address this issue, we study insight-level memory maintenance for long-term language agents and propose a failure-aware memory maintenance framework based on an editable insight graph. Each insight node tracks positive evidence, negative evidence, and an activation state, enabling the agent to distinguish reusable insights from conflicting or invalid ones. We further introduce a utility-aware retrieval mechanism and a graph controller that updates the memory graph after task execution by keeping reliable insights, archiving invalid ones, revising outdated ones, and adding newly discovered reusable insights. Extensive experiments show that our method consistently outperforms representative memory-based agent baselines across different backbone models. Ablation studies further demonstrate that append-only memory is insufficient for long-horizon tasks, while evidence-aware retrieval and graph-level editing improve memory reliability and downstream task performance.

---


### 22. [Diffuse to Compress: Leveraging Diffusion LMs for Lossless Compression](https://arxiv.org/abs/2608.11249)

**<font color=#1a73e8>作者：</font>** Angelo Nardone, Paolo Ferragina  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study the problem of lossless text compression, motivated by the rapid growth in the collection and storage of digital textual data - including plain text, source code, and structured formats such as XML - and by recent advances in neural language model-based compression. In particular, recent LLM-based approaches, whether built on symbol-ranking pipelines or paired with a statistical compressor, have demonstrated compression ratios significantly superior to general-purpose compressors such as zstd, gzip, or bzip on text and code. However, these neural approaches suffer from severe throughput limitations, making them not yet practically usable.
For the first time in the context of lossless neural text compression, we introduce Diffusion Language Models (DLMs) as an alternative inference paradigm to autoregressive LLM-based approaches. We argue that replacing autoregressive LLMs with DLMs within the same compression framework could overcome the throughput bottleneck caused by their one-symbol-per-step limitation. However, achieving these improvements requires addressing algorithmic challenges introduced by applying DLMs to lossless compression, where the architecture allows the number and positions of symbols encoded at each forward pass to be decided independently. We design efficient and effective strategies to solve these challenges and evaluate them experimentally against LLM-based and general-purpose compressors on enwik8, a well-established textual benchmark.
Our results show that the newly proposed DLM-based framework advances the state of the art in lossless text compression. Moreover, as DLMs are still a relatively young paradigm, recent advances toward increasingly capable and efficient models suggest substantial room for further improvements.

---


### 23. [AgonAlpha: Autonomous Alpha Discovery via Prompt Economy and Scalable Agentic Search](https://arxiv.org/abs/2608.11250)

**<font color=#1a73e8>作者：</font>** Weicheng Ye, Youran Sun, Xingyu Ren 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models can propose many plausible trading factors, but an autonomous research system must also allocate its evaluation budget, verify its own evidence, and preserve how each candidate was produced. We present AgonAlpha, an architecture that searches over frozen research artifacts---hypotheses, executable expressions, platform evidence, rationales, and review status---rather than formulas alone. To our knowledge, AgonAlpha is the first alpha-mining system to combine verified artifact search, a fresh-context adversarial reviewer with re-execution and veto authority, and pending-aware parallel budget allocation, together with a complete public evidence trail. Independent deployments on WorldQuant BRAIN produced SPECTACULAR-grade alphas across five users and six model backends, with Fitness reaching 9.50 and Sharpe reaching 3.48, while retaining prompt-to-expression provenance for every submission.

---


### 24. [Why AI Detection Fails for Academic Integrity](https://arxiv.org/abs/2608.11256)

**<font color=#1a73e8>作者：</font>** Jonathan A. Karr Jr, Grigorii Khvatskii, Ting Hua 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Institutions use commercial AI detectors for academic integrity, yet detectors cannot distinguish AI editing from full LLM drafts and may treat both as misconduct. In a controlled study of published English abstracts (four domains; 2013 to 2015 vs. 2023 to 2025), we quantify this policy failure under proxy human/AI labels at tau=0.50. Light "refine abstract only" edits, a proxy for guideline-compliant AI assistance, are flagged at 64 to 80% (Pangram/GPTZero). Unmodified 2023 to 2025 originals are flagged at 9 to 15%, with non-STEM rates far above STEM (p<0.001); elevated scores track long-token and Academic Word List density, not authorship intent alone. After Undetectable AI humanization, evasion is near-total: fewer than 4% of AI-labeled rewrites remain flagged (post-humanization detection rate <4%; FNR >96%). Honest AI-editing results in a higher sanction risk than humanizer-assisted evasion. Therefore, detector scores should not serve as standalone misconduct evidence.

---


### 25. [Glance, Scrutinize, and Think: Advancing Video Anomaly Detection from Training-Free to Agentic Reasoning](https://arxiv.org/abs/2608.11260)

**<font color=#1a73e8>作者：</font>** Shibo Gao, Peipei Yang, Xu-Yao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Video Anomaly Detection (VAD) aims to identify anomalous events and localize their temporal intervals. Existing approaches exhibit a "when-what" dissociation: traditional DNN-based methods localize when anomalies occur but lack semantic understanding, whereas LLM-based methods explain what happens but neglect precise temporal grounding. We attribute this to the absence of a unified reasoning paradigm. Inspired by how humans inspect surveillance videos - glancing globally to form temporal hypotheses, scrutinizing suspicious segments, and thinking iteratively to correct errors - we study this global-to-local paradigm from two perspectives. We first propose Glance then Scrutinize (GtS), a training-free framework using static and dynamic textual guidance for coarse-to-fine anomaly grounding and understanding, balancing accuracy and speed. To break the ceiling imposed by frozen external modules, we further propose a tool-augmented agentic VAD method, where a multimodal large language model learns to invoke a video cropping tool, inspect densely resampled frames, and self-correct mislocalized hypotheses, via cold-start supervised fine-tuning followed by reinforcement learning with a joint answer-grounding reward. For training and evaluation, we extend our prior VAGU benchmark into VAGU-T (Video Anomaly Grounding, Understanding, and Thinking), comprising 7,567 real-world videos over 21 anomaly categories with human-validated grounding, explanations, QA pairs, and chain-of-thought tool-calling traces. We further introduce JeAUG, a metric jointly evaluating semantic interpretability and temporal precision. Experiments show that GtS substantially surpasses training-free baselines, while the agentic model delivers both higher accuracy and faster inference.

---


### 26. [Agent Safety Should Be a Runtime Contract](https://arxiv.org/abs/2608.11274)

**<font color=#1a73e8>作者：</font>** Albus W. Ng, Yi Han, Jusheng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The dominant paradigm treats AI safety as a property to be instilled during model training via RLHF, DPO, or Constitutional AI. We argue this is structurally insufficient for autonomous agents that execute code, mutate files, send messages, and modify databases. Agent safety should be a runtime contract enforced by the harness, and the contract has two complementary faces. The preventive face blocks dangerous actions before they happen via sandboxes, permission gates, output filters, and trajectory monitors. The evidential face requires verifiable proof that good actions actually happened, gating task submission on hard evidence such as test runs, log captures, file diffs, and citation grounding. We ground the position in four lines of public evidence, with row-level protocols and data released in the supplementary JSON files: a survey of 52 documented AI-agent and LLM safety incidents, a false-completion audit with 31 non-contested core cases plus one disputed illustrative case, a trajectory-schema audit of 12 public agent systems and harnesses, and a title-level audit of all 28,560 papers accepted at NeurIPS, ICML, and ICLR 2023-2025 showing a pooled 8-12x imbalance between training-time and deployment-time publication. Two prior communities that needed to enforce safety, computer security and the experimental sciences, converged on runtime contracts with both preventive and evidential elements; agentic AI is now under the same pressure. We formalize an Agent Trajectory Schema and Evidence Chain, state a compositional gating proposition based on standard monitor composition, and outline a research agenda. The right unit of safety in agentic AI is the trajectory-with-checkable-evidence, not the model.

---


### 27. [Knowledge-Graph-Guided Retrieval-Augmented LLMs for Explainable Root Cause Analysis in Automotive HiL Validation](https://arxiv.org/abs/2608.11277)

**<font color=#1a73e8>作者：</font>** Hamza Ouarrad, Mohammad Abboush, Andreas Rausch  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hardware-in-the-Loop validation of automotive software systems generates large multivariate time-series recordings whose manual analysis is time-consuming and often limited to anomaly detection and fault classification rather than root-cause analysis. Although deep learning methods have shown strong performance in fault detection and classification, they usually require task-specific training or retraining when new fault locations, systems, or operating conditions are introduced. They also tend to treat localization as a classification task, without explicitly representing the spatial and functional relationships between fault locations, sensors, and downstream subsystem effects. This limits their generalizability and their usefulness for engineering root cause analysis and diagnosis. This paper proposes a knowledge-graph-guided retrieval-augmented large language model framework for RCA (root cause analysis) and fault localization in automotive HiL data. The method converts raw time-series recordings into compact diagnostic evidence, enriches this evidence with sensor-to-location and propagation knowledge, and retrieves similar historical cases to support the final reasoning step. The LLM is then used as a decision and explanation layer rather than as a direct time-series classifier, producing a ranked fault-location prediction together with an interpretable RCA explanation. The framework is evaluated on two automotive HiL case studies: an ASM gasoline engine and an electric vehicle system. The best-performing model achieves Top-1 accuracies of 90\% and 94\%, respectively, while recording-level aggregation reaches perfect file-level fault localization in the evaluated subset. These results demonstrate the potential of KG-guided RAG-LLM reasoning for explainable and generalizable HiL RCA.

---


### 28. [Self-Evolving Code-with-Image Reasoning](https://arxiv.org/abs/2608.11292)

**<font color=#1a73e8>作者：</font>** Tianze Yang, Liang Wu, Ruitong Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal models increasingly reach for tools when solving visual tasks (crop, zoom, rotate, brighten), a paradigm known as thinking-with-images. The central challenge is one of perception: tools mostly serve to expose visual evidence, reasoning over that evidence stays in language, and most targets are ones a human could in principle determine by inspection. Some visual questions, however, are not bottlenecked by perception: recovering their answers requires executing a multi-step visual algorithm over the pixels. On such questions a model often names the correct algorithm at once yet still answers wrong, because language can describe an algorithm without being able to run one. Code-with-Image crosses that line: given nothing but a Python interpreter, the model must implement a genuine visual algorithm in code to solve the task; the program itself becomes the reasoning. The bottleneck then shifts from executing code to deciding which algorithm to implement. So we let the model teach itself: a training-free reflection loop studies its own failed programs, tests repairs against constructive ground truth, and keeps what survives as portable skills. On our Code-with-Image Bench (CwI-Bench), thirty task families induced by hidden visual computations with disjoint learning and evaluation splits, even GPT-5.6-luna stays below 30% with tool-free chain of thought; given a bare interpreter it reaches 43%, and with skills evolved through its own executable reflection, 67%. The open 27B model climbs the same ladder (9% $\rightarrow$ 33% $\rightarrow$ 56%), and the skills are plain text, transferable across scales and families. When code carries the reasoning, debugging code becomes debugging reasoning.

---


### 29. [Long-Horizon Forecasting of Complete Financial Statements with Forma](https://arxiv.org/abs/2608.11327)

**<font color=#1a73e8>作者：</font>** Travis L. Johnson, Jiannan Jiang, Soumyabrata Chaudhuri 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Specialist training beats generalist scale when forecasting financial statements. To our knowledge, no prior work jointly forecasts complete financial statements beyond one year, yet in a discounted-cash-flow valuation most firm value sits past that window. We release ProForma-20Q, a reproducible benchmark for forecasting 78 statement line items 1-20 quarters ahead, for anonymized firms, from past statements and an industry code, scored by change-space $R^2$. On it, Forma, a transformer that reads statements as sets of (account, quarter, value) tuples and maximizes a masked-tuple Gaussian likelihood, beats every competitor we field: classical machine learning, chained gradient boosting, a zero-shot time-series foundation model, and frontier large language models. Its lead widens with horizon, where valuation needs accuracy most, and its Gaussian predictive intervals never under-cover. Forma's forecasts nearly satisfy accounting identities; exact coherence is recoverable at no statistically significant accuracy cost. Its tuple interface supports scenario analysis without retraining, and we show that pinning future revenue paths sharpens the rest of the statement.

---


### 30. [Gloss-Free Representation Learning for Cross-Dataset Sign Spotting](https://arxiv.org/abs/2608.11332)

**<font color=#1a73e8>作者：</font>** Oğuz Akif Tüfekcioğlu, Ezgi Ekin, Mustafa Kaan Çevik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sign-language research for resource-constrained languages is often limited by the cost of dense linguistic labels such as glosses, temporal boundaries, and sign order. Broadcast news offers a practical alternative by pairing continuous signing with spoken-language transcripts, but this supervision is weak since text and signing are loosely aligned. Morphologically rich languages such as Turkish add further difficulty, as the same lexical meaning can appear in many inflected forms while some derived forms should remain distinct. We study whether weak transcript-based supervision can pretrain a reusable sign encoder in this setting, where poor text normalization can fragment pseudo-gloss targets and weaken representation learning. Unlike prior pseudo-gloss pipelines designed mainly to improve translation, we test whether the pretrained encoder transfers as a reusable representation for cross-dataset sign spotting. We pretrain on TSL-News, a new Turkish broadcast corpus, using pseudo-gloss labels derived from transcripts rather than manual annotation, comparing rule-based morphological lemmatization with constrained LLM-assisted normalization over a fixed vocabulary. We evaluate the learned representations via cross-dataset sign spotting on a new TSL Spotting Benchmark built from the TSL Dictionary corpus. The LLM-assisted encoder raises top-5 temporal localization mean IoU from 0.235 to 0.465, with 56.2% of examples reaching an IoU of at least 0.50; a frequency analysis suggests this gain is not mainly driven by memorizing frequent pseudo-gloss labels. In a downstream translation check, the same pretraining improves BLEU-4 from 9.60 to 11.04 and ROUGE from 23.48 to 27.43. These results show that loosely aligned broadcast data can provide effective weak supervision for learning sign representations that capture both lexical content and temporal structure.

---


### 31. [Better, Faster, Stronger: Programmatic Skill Learning Best Reduces Agent Cost](https://arxiv.org/abs/2608.11338)

**<font color=#1a73e8>作者：</font>** Zixi Huang, Xiheng Wang, Andrew Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recently, the practice of augmenting LLM agent capability with skills has gained prevalence. We explore the cost effective adaptation of agents to novel domains by means of learning skills. Existing works focus on performance gain over cost effectiveness. As a result, little is known about what skill learning strategies save cost. We argue that among all the different skill learning methods, those that view skills as programs can achieve the best cost reduction. By executing sequences of actions deterministically, a program-augmented agent can reliably and cheaply achieve goals that would otherwise require trial and error and risk degenerate behavior over long horizons. An agent can learn at inference time by incrementally discovering these programs and equipping them for future tasks. We hypothesize that past trajectories contain enough signal to guide skill learning, even without replay or validation, provided the agent can learn to analyze them. To test our claims, we propose SpeedRunner, a coding agent that analyzes trajectories and refactors skills for better performance on future tasks. Across three different embodied environments, we show that SpeedRunner consistently achieves the frontier in learning and cost reduction while remaining robust against distribution shifts and environmental randomness.

---


### 32. [Apodex Discovery: Reality Benchmarks and Environments for Evaluating and Building Discoverative Artificial Intelligence](https://arxiv.org/abs/2608.11341)

**<font color=#1a73e8>作者：</font>** Brian Wang, Bin Feng, Xiaoman Pan 等 29 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Apollo did not reach the Moon merely because its engineers could solve difficult equations. It succeeded by turning a distant ambition into a mission architecture of explicit objectives, simulation, verification, and repeated correction. AI now faces a similar transition: frontier models can solve difficult tasks once the problem, tools, and success criteria are specified, yet consequential real-world challenges rarely arrive in an executable or verifiable form.
We introduce Apodex Discovery, a framework for building and evaluating discoverative AI through the heavy-duty solver, a system comprising a foundation model, harness, tools, and control policies that pursues extended, stateful, verifiable investigations. It has three core components. First, a problem-scouting process surveyed 561 industries across 16 sectors, assembled 423 high-value real-world problems, and selected 20 for the initial release. Second, a common environment-task-episode abstraction provides data, tools, constraints, feedback, trajectory recording, and verification of intermediate artifacts and final submissions. Third, HDS6 evaluates Tools, Repair, Alternatives, Coherence, Evidence, and Scope independently of final-task success.
In AAV capsid design, Apodex surpassed the published state of the art by 7% across viability, tropism, structure prediction, and generative design. In drug repurposing and reformulation, a task-specific biomedical environment improved the mean normalized prediction score of GPT-5.5 and GPT-5.6-sol by 2.5 and 7.6 points over the same closed-book backbone. Controlled ablations show that the fixed TRACES episode interface enables attribution of performance differences to specific solver components. Apodex Discovery moves AI evaluation beyond predefined benchmarks toward verifiable investigations aimed at genuine discovery.

---


### 33. [Weightless Fine-Tuning: Personalizing LLMs via Logit-Space Transport](https://arxiv.org/abs/2608.11342)

**<font color=#1a73e8>作者：</font>** Bohan Zhang, Anqi Ni, Yixin Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) is a standard approach for adapting LLMs to a target distribution, but in settings such as personalization, where each author requires separate weight access, optimization, storage, and retraining, its costs become prohibitive. We propose Weightless Fine-Tuning (WFT), a training-free decoding-time method that approximates the distributional effect of SFT without weight updates. WFT computes supervised residuals on an author's training sequence and transports them to the current prompt through a cross-prefix transport operator estimated from dropout-induced cross-covariance. The operator captures how a perturbation at one context propagates to predictions at another, replacing gradient-based parameter updates with logit-space corrections. On three LaMP personalization benchmarks, WFT achieves the best average performance across datasets, matches or exceeds SFT on individual tasks, and outperforms other lightweight baselines on average. In a budget-controlled comparison, WFT approaches SFT performance using less than 7% of the effective computation. Logit-level analysis shows a cosine similarity of 0.875 between the logit shifts induced by WFT and SFT over 95% of the next-token probability mass, suggesting that WFT captures the distributional effect of supervised adaptation without modifying model weights.

---


### 34. [Can Frontier LLMs Match Natively Multimodal Embeddings? A Comparison on Hard-Negative Text-to-Image Retrieval](https://arxiv.org/abs/2608.11343)

**<font color=#1a73e8>作者：</font>** Archan Dutta, Vyanktesh Kanungo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal retrieval and classification across different types of media, spanning text, images,video and audio, has traditionally relied on dual-encoder models that align visual and textual representations through contrastive learning. The March 2026 release of Gemini Embedding 2, Google's first natively multimodal embedding model to map text, images, video, audio, and documents into a single shared space, raises competition among multimodal retrieval systems. Simultaneously, frontier Large language models (LLMs) have also demonstrated strong visual understanding, raising the question of whether they can serve as effective zero-shot rankers. Our study provides the first direct comparison of native multimodal embeddings against LLM-based visual ranking on Flickr30k. We observe that GPT-4.1 and Claude Sonnet 4.6 perform on par with Gemini Embedding 2. Additionally, once embeddings are precomputed, multimodal embeddings are better suited for low-latency applications.

---


### 35. [Inverse Theory of Mind Modeling for Content Recommendation: From Web Browsing to Dynamic Intelligent Interfaces](https://arxiv.org/abs/2608.11354)

**<font color=#1a73e8>作者：</font>** Mengyu Chen, Feiyu Lu, Chun-Fu Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern recommender systems treat observed actions as reliable proxies for user preferences, yet interactions often reflect exploration or comparison rather than stable preference expression. As interfaces evolve from static layouts toward generative UIs and immersive extended reality (XR), the need for deeper, modality-agnostic user understanding grows: these adaptive environments must decide not only what to present but where, when, how prominently, and most importantly why a user acts. We propose an Inverse Theory of Mind (IToM) pipeline that reasons backward from observed interactions to infer the beliefs, preferences, and decision-making traits that explain behavior. The pipeline reconstructs each user's decision context, including what was chosen and what alternatives were available, applies LLM-driven counterfactual reasoning to produce evidence-grounded natural-language belief statements, and synthesizes these beliefs through multi-hypothesis abductive inference into a structured user persona. We evaluate on the OPeRA dataset against ground-truth personality assessments, attitudinal surveys, and interview-based personas across four tasks: next action prediction, shopping attitude alignment, Big Five personality inference, and held-out category prediction. Results show that inferred personas match or exceed ground-truth personas and that multi-hypothesis reasoning is essential for accurate personality prediction. We further demonstrate cross-modal transferability with a persona-driven spatial banking application on VisionOS.

---


### 36. [Lifecycle-Optimal Tokenization: Vocabulary Size as a Deployment-Regime-Dependent Infrastructure Parameter](https://arxiv.org/abs/2608.11361)

**<font color=#1a73e8>作者：</font>** Rima Mittal, Ankit Gubrani, Satyanarayana Kakollu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tokenizer vocabulary size is a foundational design choice in large language model (LLM) infrastructure, yet it is typically fixed at training time based on convention rather than deployment analysis. We show that the cost-optimal vocabulary is not a constant but a function of the serving regime. We formalize total deployment cost as $C_{lifecycle}(V) = C_{train}(V) + \lambda \cdot C_{infer}(V, B)$, where $\lambda$ is inference volume and $B$ is the serving batch size. Through controlled experiments on two GPU families spanning the memory-bound to compute-bound regimes (A10G, ridge $\approx$ 117 FLOP/byte; A100, ridge $\approx$ 183 FLOP/byte), we demonstrate: (1) the inference-optimal vocabulary shifts 16x with serving batch, from 32k at $B=1$ to 524k at $B=64+$, driven by amortization of the $V \times d$ unembedding matrix read; (2) at 1.3-2.3B model scale, quality (bits per byte, BPB) is optimized at $V=65$k, confirming scale-dependent vocabulary preference; (3) the lifecycle-optimal vocabulary diverges from training-optimal by up to 16x for production deployments. Quality is approximately invariant across the optimal range ($<$2% BPB spread), making vocabulary a pure systems optimization with no quality penalty in the measured range. Our results provide actionable capacity planning guidance: on-device deployments ($B=1$) should use $V \approx 32$k; datacenter serving ($B \geq 64$, $\lambda \geq 10$) should use $V \approx 131$-262k.

---


### 37. [PAIR: Pairwise-Aware Inclusion Reweighting for Adaptive Rollout Allocation in RLVR](https://arxiv.org/abs/2608.11368)

**<font color=#1a73e8>作者：</font>** Pixel Nomand, Elena Voss, Marcus Hale 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) spends most of its compute generating groups of long reasoning trajectories. Recent allocators reduce this cost by assigning budgets to prompts, rollouts, or tokens according to a pointwise notion of difficulty or utility. We identify a statistical mismatch: the unclipped leave-one-out group-relative score gradient is not a sum of independent point contributions, but a second-order U-statistic over pairs of rollouts. Completing one rollout therefore reveals contrast with every other completed rollout, and adaptive endpoint selection changes which pair terms are observable. We introduce PAIR (Pairwise-Aware Inclusion Reweighting), which treats short rollout prefixes as vertices and pair-gradient terms as edges of a contrast graph. A prefix-only predictor estimates correctness and remaining token cost; a convex design chooses positive continuation probabilities under an expected suffix-token budget; and each edge induced by completed vertices is inverse-weighted by its logged joint inclusion probability. Under conditionally independent on-policy rollouts and an unclipped, unstandardized objective, the resulting estimator is design-unbiased for the complete candidate-pair gradient. Across compute-matched RLVR runs on Qwen3-1.7B/4B, PAIR improves average accuracy by +1.2 and +1.4 over the strongest pointwise allocator while using 51% and 52% fewer generated tokens than full-group GRPO. A frozen-population estimator audit confirms that unweighted adaptive selection is biased, whereas pair-inclusion correction recovers the complete-pair target at matched suffix cost.

---


### 38. [From Numbers to Judgment: Specialist LLM Agents and Reinforcement Learning for European Listed Real Estate](https://arxiv.org/abs/2608.11381)

**<font color=#1a73e8>作者：</font>** Pardis Taghavi, Santosh Bhavani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study whether the localized numerical operations and integrative judgments of financial analysis benefit from the same form of LLM specialization. Larix maps a 16-lens European listed-real-estate analysis framework to eight lens-aligned specialists; we compare a frontier LLM under monolithic versus specialist-decomposed prompting while holding the model, source evidence, task instructions, output schema, and scoring fixed. Across 19 firms spanning seven regulatory wrappers, decomposition improves the numerical-task aggregate by 15.8 percentage points but does not reliably improve, and can reduce, performance on judgment tasks, a pattern stable across four frozen-template dispatches; a single-agent control given the complete framework does not reproduce the numerical gain. Post-training Qwen3.5-9B with GRPO using task-aligned structured rewards then raises the development-split score by 12.0 points and the judgment aggregate by 14.2 points, with gains on all four sub-ceiling tasks; the gains transfer to unseen firms (+15.2 points overall; +40.4 on covenant stress) and to unseen regulatory wrappers (+4.3), with positive transfer on all three anti-memorization splits. Prompt-level decomposition thus improves modular numerical execution, whereas targeted parameter adaptation improves integrative financial judgment.

---


### 39. [When Self-Consistency Backfires: Majority Vote Hurts the Majority of Hard Science Problems for Small LLMs](https://arxiv.org/abs/2608.11403)

**<font color=#1a73e8>作者：</font>** Utkarsh Bahuguna  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-consistency (SC) via majority vote is a widely used way to spend inference-time compute: sample N chains of thought, return the plurality answer. On the full GPQA Diamond benchmark (198 graduate-level science questions), majority voting reduces per-problem accuracy on a majority of problems for two instruction-tuned models from different families: 56.6% of problems for Qwen2.5-7B and 65.7% for Llama-3-8B, with Qwen the primary demonstration and Llama corroborating the direction from a near-chance baseline. The effect was pre-registered on a 151-problem confirmatory split after being observed on 47 exploratory problems, and all four confirmatory hypotheses passed. A grid oracle that routes each problem to the best N across {1, 2, 4, 8, 16, 32, 64} marks a theoretical upper bound 14 accuracy points above N = 1 for Qwen and 17 for Llama, an oracle bound requiring ground truth rather than a deployable method. No verifier-free gate reaches it: neither a plurality-agreement gate nor a token-entropy gate moves accuracy more than 0.002 from fixed-budget voting at N = 64. The mechanism is direct: confidence does not track correctness on these problems. In the highest-agreement bin the plurality answer is correct about half the time for Qwen, and for Llama that bin is less accurate than its lowest-agreement bin. We pre-register and confirm these findings on small instruction-tuned models; we do not test reasoning-native models, which we flag as the central open question.

---


### 40. [Measure, Don't Optimize: Forecasting Recovery in LLM Unlearning](https://arxiv.org/abs/2608.11408)

**<font color=#1a73e8>作者：</font>** Zirui Song, Huaxing Liu, Xiang Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prior white-box studies show that large language models can retain latent traces of target knowledge after unlearning, even when the knowledge is no longer expressed in their outputs. However, existing audits remain limited to one-off diagnostics: it is unclear whether these residual signals can predict future recovery under continued training or serve as reliable optimization targets. Resolving this gap is essential to determine whether internal auditing can move beyond post-hoc evaluation toward proactive risk monitoring and safer unlearning. We propose J-Access, an inference-time audit that uses the Jacobian lens to map intermediate representations into vocabulary space and measures how often target concepts remain accessible along the model's output pathway. We hypothesize that residual accessibility reflects recovery susceptibility: knowledge that remains closer to the output pathway requires less fine-tuning to restore, leading to faster recovery. We audit 398 public unlearned models spanning eight unlearning methods. We find that: (1) most unlearned models retain access above the retain-only gold level; (2) pre-attack accessibility predicts recovery speed and extent at the model level, but cannot identify which specific facts will be recovered; and (3) directly minimizing J-Access does not promote genuine deletion. Instead, the model learns to hide knowledge from the audit, producing lower audit scores but greater post-attack recovery. These findings position J-Access as a model-level diagnostic for assessing residual susceptibility in unlearned models. We argue internal audits should serve as an independent diagnostic dimension in unlearning evaluation, and should not be converted into optimization targets without validation.

---


### 41. [Social Chain of Thought: A Multi-Agent Architecture Grounded in Medical Differential Diagnosis Methodology](https://arxiv.org/abs/2608.11420)

**<font color=#1a73e8>作者：</font>** Del Coburn, Scott Sanner, Dan Silver  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical diagnostic reasoning is a high-impact use case for LLMs that carries significant implications for the health and wellbeing of users. When OpenAI (2026) reports that more than 5% of ChatGPT messages globally are healthcare-related, the transparency of these systems becomes a serious design concern. This is especially true for complex cases, where differential diagnosis often requires integrating multiple forms of specialist reasoning. Existing work has proposed multi-agent approaches to medical diagnosis, but it remains unclear when such systems are needed, why they help, and where they outperform monolithic inference. We introduce Social Chain of Thought (SCoT),a multi-round pipeline for medical differential diagnosis that structures multi-agent interaction as a deliberative framework for collabora. tive LLM reasoning. Evaluating SCoT against single-agent baselines, one-agent pipeline ablations, and best-of-n scaling, we show that its recall advantage is not reproduced by monolithic inference alone. SCoT is most successful in the hardest diagnostic cases, where multiple rounds of specialist conversation help recover ground-truth diagnoses and converge on a higher-recall differential.

---


### 42. [Click2Poly: A VLM for vector mapping buildings and walls](https://arxiv.org/abs/2608.11424)

**<font color=#1a73e8>作者：</font>** Nicolas Girard, Jawher Ben Abdallah, Arno Gobbin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate vector mapping of buildings and walls is critical for geospatial applications but remains a labor-intensive process. While recent deep learning methods have improved automatic extraction, in order to meet cartographic standards they always require a human to perform quality control and fix complex cases in the extraction. We present Click2Poly, a human-in-the-loop AI assistant designed to speed up this manual step. Extending the Florence-2 Vision Language Model (VLM), Click2Poly responds to user clicks by editing the building or wall vector layer directly. Implemented as a QGIS plugin, Click2Poly speeds up the manual editing of building and wall vector layers in a real-world production environment.

---


### 43. [VLMs Win a Systematic Evaluation of Underwater Image Reconstruction](https://arxiv.org/abs/2608.11425)

**<font color=#1a73e8>作者：</font>** Sara Aghajanzadeh, Yingxue Wang, Ieva Bagdonaviciute 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater image restoration consists of recovering an image which looks like there is no water present. To date, evaluation has not been systematic. This paper describes a systematic evaluation pipeline for underwater reconstruction, which can be used to assess a method for accuracy; consistency of reconstruction over camera moves; and the effect of water parameters. We use this pipeline to evaluate a range of current procedures, from models constructed using explicit but approximate physical models of scattering to Vision-Language Models (VLMs which are not currently trained with explicit physical models). Overall, VLMs wholly and significantly outperform physically based models in our evaluation, likely because of the importance of a strong image prior. Results on images of real underwater scenes strongly confirm the evaluation.

---


### 44. [Benchmarking LLM Judges for Mobile Agent Evaluation](https://arxiv.org/abs/2608.11434)

**<font color=#1a73e8>作者：</font>** Ziqiang Wan, Li Gu, Zhixiang Chi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mobile agent benchmarks increasingly rely on LLM-based judges to evaluate task completion, yet the reliability of these judges on mobile agent trajectories remains largely unexamined. We introduce MobileJudgeBench, a benchmark for systematically evaluating LLM-as-judge methods on mobile agent trajectories. Our benchmark comprises 931 human-annotated trajectories spanning 6 mobile agent benchmarks, 4 agent models, and 68 apps. We evaluate 6 judge methods (five adapted from SPA-Bench, A3 with two modes, AndroidArena, and AgentRewardBench, plus a simple baseline we design) across multiple LLM backends. Our experiments reveal three key findings. First, a simple baseline judge with sampled screenshots is competitive with, and often exceeds, purpose-built methods, indicating that more elaborate judge pipelines do not consistently improve judge quality; among competitive methods, the LLM backbone is the primary driver. Second, benchmark quality metrics reliably predict real-world judge utility: they correlate with both agent ranking fidelity for evaluation and downstream performance when judges serve as reward signals for on-policy reinforcement learning. Third, failure analysis across two LLM backends uncovers qualitatively opposite failure profiles, one conservative and the other permissive, linked to the backbone's precision-recall characteristics.

---


### 45. [TangPoetryBench: A Multi-Dimensional Benchmark and Rubric-Conditioned Evaluator for Poetry-to-Image Generation](https://arxiv.org/abs/2608.11452)

**<font color=#1a73e8>作者：</font>** Haoqi Hu, Tongji Luo, Li Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) models are increasingly asked to illustrate literary and cultural content, yet we cannot measure how well an image renders the meaning of a poem. The task is many-sided: a good illustration must be visually sound, faithful to the poem's imagery and scene, culturally and stylistically apt, free of spurious text, and true to its emotion, and its deepest requirements, imagery and especially implicit emotion, are never stated in the words. Existing metrics (CLIPScore, BLIPScore, VQAScore) reward literal text-image correspondence and so cannot tell whether an illustration succeeds, let alone why, or even separate the best model from the worst. We introduce TangPoetryBench, a multi-dimensional benchmark of 1,280 images (320 classical Chinese Tang poems x 4 state-of-the-art T2I models) with quality-controlled human annotations across ten dimensions. Analyzing this data, we reveal the shared and model-specific strengths and weaknesses of current T2I models, including their ability to evoke a poem's implicit emotion. We further introduce PoemAutoEvaluator (PAE), an open, rubric-conditioned evaluator that reaches parity with a strong proprietary judge (Claude), generalizes to an unseen generator and a second poetic tradition (Song Ci), and lets the benchmark scale to new images without fresh human annotation. We release the benchmark, annotations, and evaluator.

---


### 46. [Multi-Agent Target-Existence Verification and Learned Mask Geometry Refinement: Winning Report of the MeViS-Text Track at the 8th LSVOS Challenge 2026](https://arxiv.org/abs/2608.11458)

**<font color=#1a73e8>作者：</font>** Jungyoon Lee, Gyuil Lim, Doeon Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present the first-place solution to the MeViS-Text track of the 8th Large-scale Video Object Segmentation (LSVOS) Challenge 2026: referring video object segmentation guided by written motion expressions, including deceptive no-target expressions that match no object in the video and must yield empty masks in every frame. Our pipeline, SSUPER, resolves each expression into a visual concept, generates full-video candidate masklets with SAM~3.1, and selects target IDs. At every reasoning stage, three heterogeneous multimodal large language models independently execute the same stage-specific prompt before a single synthesis pass commits one schema-validated verdict. Although this system rejects every no-target expression in validation, the leaderboard reveals that a substantial share of test no-target cases still slips through. The reason is that hard negatives name a plausible object and fail only under the complete temporal predicate, so when selection and existence are decided together, a category-plausible masklet anchors the verdict. Hence, we decouple existence verification into an independent multi-agent audit of the full predicate (category, count, action, trajectory, event order, and semantic role) that distinguishes absence from temporary invisibility, discounts apparent motion caused by camera movement, and requires contradicting evidence rather than mere uncertainty for a no-target verdict. Without any new segmentation call, this audit recovers most of the residual no-target errors. A training-data-only StyleRefiner then aligns mask geometry with the annotation style of MeViSv2 while preserving every presence decision by construction, showing that once the semantics are fixed, part of the remaining error is stylistic rather than semantic. The complete system reaches a Final score of 0.9081339614 on the official challenge leaderboard.

---


### 47. [Principal Trait Analysis: Towards Deriving "Skills" in Human-AI Collaboration](https://arxiv.org/abs/2608.11460)

**<font color=#1a73e8>作者：</font>** Hunter McNichols, Kai Du, Andrew Lan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model-powered agents are increasingly used in the workplace via human-artificial intelligence (AI) collaboration. In this new era of work, it is important to understand the kinds of prompting traits that contribute to task success. Moreover, we need to uncover key skills required for modern professionals and inform educators on how to foster these skills among students. Existing guidelines for human-AI collaboration are built from either top-down theory or context-specific observations of human-AI interactions. However, since LLM capabilities are rapidly improving, theory may not be able to explain emerging interaction patterns, and empirical guidelines may become obsolete quickly. In this work, we explore an automated, data-driven approach to uncover patterns, which we term traits, of effective human-AI interaction that are aligned with task outcomes. We propose Principal Trait Analysis, a Principal Component Analysis-inspired algorithm for deriving common traits from patterns in LLM conversations. Our algorithm uses LLM-based processing stages to analyze corpora of human-AI collaborative session traces, deriving common traits across the dataset and scoring each human collaborator's usage style by each trait. The approach also allows domain expertise to be injected during trait discovery and selects the most distinguishing traits to be those that exhibit the highest variance across collaborators. We evaluate PTA on two human-AI collaborative coding datasets, an educational setting (students working with an AI tutor) and a professional setting (developers working with an AI coding agent). We find that PTA-derived traits are significant in explaining collaborator behavior across both settings and can help predict task outcomes. However, whether traits qualify as skills remains to be seen, due to inconclusive results on generalizability and how user traits change over time.

---


### 48. [The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark](https://arxiv.org/abs/2608.11469)

**<font color=#1a73e8>作者：</font>** Jeremy Spence, Nicholas Assaderaghi, Jinhao Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents are rapidly improving in cybersecurity capabilities when the source code is available for analysis, yet much of the software most consequential to cybersecurity, including malware, firmware, and proprietary applications, is available only as binaries. Analyzing such software requires reverse engineering(RE): recovering program semantics before the analysis can be meaningfully performed. However, evaluating agentic RE poses a fundamental challenge: benchmark instances must be unseen as source code in the LLMs' training data to prevent models from taking shortcuts by recognizing them rather than really analyzing them, while also matching the scale and anti-analysis protections of real software. Unfortunately, however, existing benchmarks do not jointly satisfy these requirements. To this end, we introduce SRE-Bench, the first realistic, contamination-free RE benchmark. Built entirely from scratch by RE experts with over 5,000 hours, SRE-Bench comprises 19 private, real-world-scale programs averaging 16.9K lines of code. We further developed 44 in-house anti-analysis primitives, yielding 262 binary instances and 1572 deterministically graded tasks. Our evaluation across five frontier LLMs (GPT-5.6-sol,Claude-Opus-5,GPT-5.5,Grok-4.5, and GLM-5.2) shows that RE remains largely unsolved: the strongest model, GPT-5.6-sol, scores 61.4% per instance, and fully solves only 31.5% of the instances. Our analysis further reveals that agents behave differently from human engineers, where agents are relatively insensitive to compiler optimization and static linking. Controlled ablations also confirm that both contamination control and realistic scale are essential. These results indicate that strong source-code security capabilities do not yet transfer to binary analysis, highlighting RE as an important frontier for agentic cybersecurity and SRE-Bench as a rigorous testbed to measure progress.

---


### 49. [Test-Time Hallucination Control in Large Vision-Language Models](https://arxiv.org/abs/2608.11474)

**<font color=#1a73e8>作者：</font>** Mehran Tamjidi, Hamidreza Dastmalchi, Ali Cheraghian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object Hallucination in large vision-language models (LVLMs), where models generate non-factual content about input images, remains a critical barrier to their reliability in real-world applications. Existing mitigation strategies can be categorized into training-based and training-free methods. Training-based methods often achieve strong performance but are costly, requiring extensive computational resources, large-scale data, and time-consuming fine-tuning. Training-free approaches are particularly appealing due to their efficiency. However, existing training-free methods either require multiple decoding rounds, which adds computational overhead, or modify internal states in a model-specific way that risks degrading pretrained knowledge. We propose Test-Time Hallucination Mitigation (TTH) method, a novel training-free method that addresses both limitations. TTH introduces a token-validator module, implemented as a zero-shot Multi-Modal Classifier (MMC), to generate auxiliary logits grounded in the input image. These logits are fused with the original LVLM outputs at the token level for object tokens selected from a candidate pool. An entropy-based weighting scheme is then applied to enable robust and accurate predictions. Extensive experiments across multiple LVLM families and diverse benchmarks demonstrate that TTH consistently improves accuracy and robustness, underscoring its generalizability and practical effectiveness. Code is released at this https URL

---


### 50. [A Modular Agentic Framework for Synthetically Constrained Multi-Objective Hit-to-Lead Optimization](https://arxiv.org/abs/2608.11483)

**<font color=#1a73e8>作者：</font>** Kelvin P. Idanwekhai, Enes Kelestemur, Benjamin Strickland 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hit-to-lead optimization requires iterative design of hit analogs across competing potency, selectivity, physicochemical, pharmacokinetic, safety, and synthetic constraints. We present SABLE (Synthetically-accessible Agentic Bayesian Ligand Exploration), an open-source framework that employs natural-language orchestration to guide chemical structure optimization. SABLE uses an LLM to interpret user-defined goals and route tasks, while specialized tools perform reaction-templated analog enumeration, physicochemical and ADMET property prediction, structure-based affinity scoring, and Bayesian optimization. The resulting workflow is a computational twin of the analytical and prioritization stages of the design-make-test-analyze cycle, providing provenance of each numerical output. Across single, and multi-objective optimization studies, SABLE enriches candidate sets for user-defined computational objectives while evaluating only a subset of the enumerated search space. Its modular architecture allows tools and characterization backends to be replaced by editing a simple config file, without modifying operational logic. SABLE provides an extensible decision-support framework for prioritizing synthetically constrained analogs in early-stage drug discovery.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-164](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
