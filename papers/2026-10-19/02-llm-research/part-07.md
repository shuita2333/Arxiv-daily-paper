# 🧠 大模型相关研究 | 2026年10月19日

> 本类共 **321** 篇论文：已确认 **300** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-321**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-321**

---

## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 301. [Evaluating Model Capabilities After Benchmark Saturation](https://arxiv.org/abs/2610.20667)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Morio Hamada, Jehyeok Yeon, Matteo Migliarini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rapid advances in AI capabilities are causing benchmarks to saturate. Once several models approach perfect scores, a benchmark loses its power to differentiate between them, and with it its utility for informing AI safety cases and frontier policies. Yet benchmark items produce far more information than the scores we typically extract from them: a full transcript of how each model solved the task. We investigate whether these transcripts can be used to assess model capabilities even after benchmark scores have saturated. We simulate saturation retrospectively using historical benchmark and model releases, and test whether protocols that access only correctly solved transcripts from saturated benchmarks can predict capabilities measured on held-out, unsaturated items. We evaluate representative contemporary approaches for extracting information from model transcripts: pairwise judging, single-transcript absolute scoring, and predictions from deterministic transcript features or embeddings. We find that saturated transcripts retain capability information beyond benchmark accuracy. Amongst our evaluated protocols, pairwise judging performs best, reducing prediction error by 5.3 times compared to a baseline using only saturated benchmark scores. This capability-relevant information is distributed across transcript sections, but concentrated in specific channels of information such as reasoning and tool-calls. However, the predictive power of protocols does not always generalise across distribution shifts -- for example by underestimating the capabilities of the first reasoning models introduced in early 2025. Saturated benchmarks thus retain capability-predicting signal in their task transcripts, but extending the lifetime of existing benchmarks requires methods designed to extract these signals robustly.

---


### 302. [AlphaDiana: A Measurement System for Agents in Verifiable Reasoning Tasks](https://arxiv.org/abs/2610.20675)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhanke Zhou, Zongze Li, Weikai Huang 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents pair reasoning models with harnesses that organize model calls, execute tools, load skill instructions, and retain history in memory. Understanding agent performance requires linking execution conditions to outcomes, behavior, and resource use. We introduce AlphaDiana, a measurement system with modular interfaces for datasets, agents, environments, and scorers. It preserves harness-native control loops while controlling file reuse and memory retention separately. AlphaDiana supports macro analyses of complete agents and micro interventions on agent components such as tools, skills, and memory under matched conditions. We study three open-source models and three open-source harnesses on five answer-based benchmarks, with two models also tested on two interactive benchmarks. We find that harnesses do not consistently improve the accuracy of reasoning: gains on questions unsolved by the model alone can be outweighed by losses on questions it answers correctly without tools. This inconsistency extends to component interventions: neither skill guidance nor retained history reliably improves accuracy. Behavior and output-token use must be assessed with correctness: low token entropy can accompany wrong answers, and less output per execution can mean more output tokens per correct answer when accuracy falls. AlphaDiana links answer correctness and execution status to traces and resource records for comparing agents and diagnosing failures under shared task and resource policies.

---


### 303. [Causal Syntax Circuits in CodeLMs: Budget and Probe Decide What Looks Localised](https://arxiv.org/abs/2610.20683)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Harsh Kumar, Tanmay Shailesh Joshi, Rahul Maity 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Code models write Python when the prompt does not say which language to use. We ask a mechanistic question about that habit: is it produced by a small, findable group of components inside the model? We run one pipeline---mean ablation, activation patching, greedy circuit extraction, a random-control significance test, and activation steering---over 55 model-language settings spanning ten open code models (five base and five instruction-tuned), three target languages (Rust, C#, PHP), two prompt suites, and two component budgets. We report five findings. First, the preference is large, grows with model size, and survives instruction tuning: it is larger on every instruction-tuned checkpoint than on its base version, by 12% on average. Second, its measured size is mostly a property of the probe; replacing our aligned prompts with XLCoST parallel functions takes the same measurement on the same models from about 1.6 to about 0.01. Third, whether the preference looks localised depends on how many components the search may keep: with a budget of 12, 1 of 15 settings yields a circuit that beats size-matched random controls after multiple-comparison correction, and with a budget of 40, 6 of 15 do. Fourth, interventions that a smaller-budget study reports as uniformly failing do sometimes succeed: patching makes a Python prompt prefer target syntax in 2 of 45 settings, and steering changes the most likely next token in 9 of 45. Fifth, every circuit whose effect is significant but points away from the target language comes from a setting where circuit extraction failed, which makes such results a diagnostic rather than a phenomenon. The practical lesson is that a claim about whether a behaviour is localised can turn on analysis choices that papers rarely report. We release the full grid so those choices can be varied.

---


### 304. [From Detection to Decision: Calibration and Deferral for Prompt-Injection Detection](https://arxiv.org/abs/2610.20907)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Qianlong Lan, Anuj Kaul, Vinothini Pandurangan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prompt-injection defenses are commonly evaluated as binary detectors, although deployed LLM applications must make operational decisions about whether to allow, block, or escalate potentially malicious inputs. Recent probabilistic decision models aim to support such decisions through calibrated confidence estimates, but their reliability under distribution shift remains uncertain. We evaluate a native probabilistic decision model (Jev), two Llama Prompt Guard 2 classifiers (22M and 86M), and an LLM-based judge on 47,611 held-out examples spanning direct and indirect prompt injections, hard-benign inputs, obfuscation, and distribution shift. Using separate development and calibration splits, we assess detection performance, probability calibration, and allow-block-defer policies under a frozen evaluation protocol. The LLM judge achieves the highest overall discrimination (AUROC 0.897), followed by Jev (0.871), Prompt Guard 2 86M (0.757), and Prompt Guard 2 22M (0.714). However, Jev's native probabilities do not consistently outperform post-hoc calibrated classifier scores, and temperature scaling improves calibration without improving discrimination. At an empirical false-negative-rate target of 1%, all evaluated gate-reviewer systems require more than 91.8% escalation and incur substantial false-positive rates. These findings demonstrate that probabilistic outputs alone do not establish reliable security decisions under distribution shift. Effective LLM security systems must jointly evaluate detection, calibration, reviewer behavior, and operational decision policies.

---


### 305. [Screwtape: Adversarial Transcript Editing for Monitor Red-Teaming](https://arxiv.org/abs/2610.20941)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Gosha Kozhevnikov, Tyler Tracy  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present Screwtape, a pipeline that converts real agent transcripts into attacks that evade action-only monitors. An LLM attacker edits a transcript so that the agent causes a specified harm, such as leaking an API key or spawning an unmonitored agent. The edited actions are never executed, so we use an LLM verifier to reject attacks that are inconsistent with the original transcript or below a severity bar. The attacker revises the edit until the monitor no longer flags it. We applied Screwtape to 94 Claude Code and Codex transcripts from Redwood Research staff, optimizing against our own monitors. Across 252 runs, it produced 35 attacks that passed the verifier and evaded these monitors. Six of them, confirmed valid by human review, also evaded a held-out monitor provided by a frontier developer. We therefore demonstrate that a red-teamer without access to a developer's infrastructure can find confirmed failures of the developer's monitor. We expect to find more attacks when the pipeline runs inside the developer's infrastructure, with frontier attacker models that lack refusal safeguards and direct optimization against the production monitor. Developers can use these attacks to fix monitor blind spots, and evaluators can use them as counterexamples to safety claims about the monitor.

---


### 306. [PiCo: Physics-Informed Concept Probing for Geo-Foundation Models](https://arxiv.org/abs/2610.20973)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yihang She, Andrew Blake, Jianbo Qi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geo-foundation models (GFMs) are typically evaluated by downstream task predictive performance, revealing little about which physical features they are sensitive to or use in prediction. This limits developers' ability to test hypotheses about model behaviour and users' ability to select models for new tasks. We propose Physics-Informed Concept Probing (PiCo), a post-hoc framework for explaining GFM predictions. PiCo identifies concept vectors in a GFM's embedding space by generating synthetic multispectral satellite observations from a 3D radiative transfer model coupled with a game engine. These vectors reveal physical sensitivities that inform domain-based hypotheses about downstream performance. Projecting embeddings onto these concept vectors produces low-dimensional representations for quantifying concept importance in making predictions. We evaluate PiCo on three GFMs with different input modalities using seven physical concepts covering forest leaf optics and canopy structure. In ground-cover estimation, RGB restriction reduces dry-matter sensitivity and disproportionately degrades predictions for dry vegetation and bare ground, supporting a hypothesis derived from sensitivity analysis. For hierarchical forest type and tree species classification, concept representations retain 70.0-93.8% of full-embedding accuracy. Models capture similar physical contrasts between classes, such as structural differences between broadleaf forest and cleared ground and leaf-water-content differences between oak and beech, yet differ in the strength of these contrasts and the concepts driving classification. PiCo thus provides a physical basis for hypothesis testing and model assessment, with potential applicability beyond Earth observation wherever forward models enable controlled simulation and pretrained embeddings are accessible for probing.

---


### 307. [Failure Is the Mother of Success: Recovering Supervision with Grounding Hindsight](https://arxiv.org/abs/2610.21018)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sheldon Yu, Tong Yu, Nikki Lijing Kuang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When every rollout for a problem fails, GRPO receives neither a successful exemplar nor a nonzero group-relative advantage, so it learns nothing from exactly the problems it most needs to learn. The failed reasoning can nevertheless suggest what to try next. We present Replay-Selected Hindsight Distillation (RSHD), which turns failed attempts into an additional, tested source of supervision during GRPO training. The policy writes a corrective note about each failed attempt without seeing a reference answer or solution, then re-solves the problem with the note in context. A note is admitted only if its replays succeed more often than the original group did, after screening for notes that state the answer, and an admitted replay is distilled into the plain-prompt policy. Because admission is decided by fresh successes rather than by the failed rollout itself, the procedure can recover supervision from groups in which every attempt failed, and it applies equally to failures in mixed groups. Only the policy is trained, the only judge is the outcome verifier, and deployment requires no notes or extra inference. Across model families and sizes and two training domains, RSHD consistently improves over GRPO on in-domain benchmarks, and the gains carry over to out-of-domain evaluation sets.

---


### 308. [Noise-Space Reward Alignment for Few-Step Generative Models](https://arxiv.org/abs/2610.21125)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Woocheol Shin, Taeyoung Yun, Jiwon Sung 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Few-step generative models produce high-quality samples in one or a few evaluations. However, steering them toward desired properties remains difficult, especially when only black-box reward evaluations are available. While one could apply approaches developed for iterative diffusion and flow-based models, such as direct RL fine-tuning or test-time scaling, we find that neither transfers well to the few-step regime: direct fine-tuning suffers from severe reward over-optimization, and test-time scaling sacrifices the efficiency advantage of few-step generation. We propose Noise Policy Optimization (NPO), which explicitly targets the alignment problem for few-step generative models. The key idea is to learn an amortized flow policy over the initial noise space of the generator. The trained policy transports Gaussian noise to a reward-tilted noise distribution, whose pushforward distribution through the frozen generator is exactly the reward-tilted output distribution. By keeping the generator frozen, we can effectively utilize the knowledge encoded in the pretrained model, yielding a better reward-quality trade-off than direct fine-tuning. The amortized policy moves the search cost into training, so inference adds only a lightweight noise sampling step on top of the pretrained model. To improve sample efficiency during training, we use ELBO-based likelihood estimation that requires only sampled endpoints rather than simulated trajectories. Across image, language, and protein structure generation, NPO consistently achieves a better reward-quality trade-off than direct fine-tuning, and matches test-time search methods with 16 to 549 times lower inference cost.

---


### 309. [KBS: A Korean Benchmark Suite for Foundation Model Evaluation](https://arxiv.org/abs/2610.21227)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yeonkyoung So, Jongmin Kim, Sungmok Jung 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a Korean Benchmark Suite (KBS) comprising Ko-ARC, Ko-GSM8K, Ko-EQ-Bench, Ko-WinoGrande, Ko-LAMBADA, and Ko-IFEval, covering six capabilities across 9,396 items. The suite combines review, localization, direct Korean construction, and redesign for Korean, avoiding a translation-only approach to benchmark adaptation. We evaluate Korean-developed models, multilingual open models, and closed API models under protocols that account for model access, prompt format, and scoring differences. Results show that Korean benchmark scores depend on task construction, scoring rules, prompting, and model post-training. These findings suggest that Korean evaluation should report both final scores and the settings used to obtain them.

---


### 310. [Do Agents Need a New Kind of Paper? SPRA: Structured Paper Representation for Agents](https://arxiv.org/abs/2610.21424)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yutong Leng, Haojiong Chen, Fukai Shang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific agents must connect research problems, methods, and findings dispersed through narrative articles. We introduce SPRA (Structured Paper Representation for Agents), a paper-level representation of persistent research objects and typed relations. Its empirical-AI profile organizes Problems, Contributions, Components, ExperimentSetups, Measures, and Findings for querying, traversal, and reuse. Selected paper-level citation relations record dependencies, component use, and comparisons with prior work; source locations support verification. We instantiate SPRA across more than one million AI papers, with 19.95 million research units and 24.07 million internal relations. Evaluations access SPRA through Schema-RAG with task evidence fixed before inference. Across seven subfields, SPRA improves source-conditioned scientific QA by 0.381/5 over passage retrieval while remaining close to Full Compact (0.078/5 lower on average). In directed cross-paper reasoning, qualification improves by 0.184/5 over passage retrieval; Top-5 synthesis shows mixed quality effects. Across all paired RQ2 tasks, including Top-5, input+output tokens decrease by 28.5% relative to passage retrieval and 95.3% relative to Full Compact. In idea generation, a 0.067-point lower Overall score than Full Compact accompanies 93.7% fewer input+output tokens. Together, these results support SPRA as a usable representation of scientific content and a foundation for research workflows that connect, inspect, and reuse paper-level research objects. The SPRA resource is accessible through the SciVerse scholarly-data platform.

---


### 311. [What Survives Self-Evolution: Provenance Marks in Copied Agent Harnesses](https://arxiv.org/abs/2610.21458)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jieyu Li, Jingya Li, Sheng Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent harnesses, the prompt and tool code around a base model, leak. Claude Code's 512,000 lines were mirrored within hours of a packaging error. A plagiarist can pass a leaked harness through a published self-evolver and ship the result as its own. We define this as a covert rewriting attack. No one targets a provenance mark, yet a large language model (LLM) proposer rewrites the file that carries it and a score keeps the better rewrites. We give the first measurement of marks under this attack, with three evolvers, five proposers and two environments. Published marks fail. KGW in the prompt survives GEPA's rewrites in 0 of 12 copies, AgentMark as released in 5 of 12. The proposer's habits decide survival, by two orders of magnitude across models, and selection protects a mark only when each decision sees enough games. We then build a mark for this attack. Its key is the order of near-tied entries of a table of where objects are found, built from public games, so deleting the table costs success, rewrites that keep its rows keep the order, and a customer reads the key from the agent's actions alone. On held-out games it is detected in 62 of 76 copies whose lineage rewrote its file. A scheme-aware plagiarist reshuffles the ties at no measurable cost, and a plagiarist who asks the proposer for more general code removes the key in 75-100% of rewrites.

---


### 312. [From Adults to Children: Benchmarking Foundation Models for Chest X-Ray Classification under Domain Shift](https://arxiv.org/abs/2610.21809)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sara Inácio, Hugo Proença, João C. Neves  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models have shown significant potential across diverse fields and have been applied to medical imaging, but their robustness across patient populations remains unclear. In this work, we investigate foundation models' ability to generalize from adult to pediatric chest X-ray classification. To the best of our knowledge, this is the first benchmark to compare multiple foundation models under a common adult-to-pediatric evaluation setting while also analyzing the effect of adaptation depth. We harmonize VinDr-CXR and PediCXR into a five-label classification task and evaluate six foundation models and two CNN baselines. All models are adapted using adult data only and tested in both the in-domain and pediatric domains using linear probing, partial fine-tuning, and full fine-tuning. The benchmark reveals a clear and consistent trend: all models suffer a substantial performance degradation when transferred from adult to pediatric data, with drops exceeding 10 percentage points. While Macro-AUROC values reach approximately 92% on the adult test set, performance decreases to around 78% on the pediatric domain. Another important finding is that increasing the depth of adaptation does not significantly improve cross-population generalization. Moreover, strong in-domain performance does not translate into better performance on pediatric data.

---


### 313. [Physics-Aware Distillation of a Grid Foundation Model for Real-Time Edge Inference](https://arxiv.org/abs/2610.21833)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Vlad Alexandru Sănduleac, Shahariya Rasheed Rayamarakkarveettil Puthanpurayil, Noman Khan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Grid foundation models (GridFMs) are graph transformers pretrained on a masked power-flow objective, and evaluate power flow orders of magnitude faster than an iterative solver. Their size, however, targets data-centre inference, whereas low-inertia operation increasingly asks for inference at the edge, next to the measurement, at batch size one and within a single synchrophasor (PMU) reporting frame. We distil a 20.1M-parameter, 12-layer GridFM teacher into a 0.62M-parameter, 6-layer student, a $32.5\times$ parameter reduction at half the message-passing depth, using an objective that combines the masked power-flow loss with output, physics-residual, latent-state and attention transfer. The physics-residual term, which matches the teacher's power-residual profile, has not previously been applied to typed power-grid graphs. We evaluate on a renewable variant of the IEEE 118-bus benchmark grid in which 26 of the conventional (synchronous) generators are replaced by inverter-based renewables with battery flexibility and standardised reactive-power limits (IEEE 1547), giving $97\,529$ physically valid (AC-OPF-feasible) operating scenarios, and we ablate all eight combinations of the transfer terms, reporting accuracy against ground truth and fidelity to the teacher separately. Distillation lowers student error on all four predicted quantities, by up to $48\%$ on active-power dispatch, and every distilled student is more accurate than its teacher on reactive-power dispatch. The gain is largely carried by the output matching term. The physics-residual term, in the layer-aggregated form used here, is consistently harmful, which we attribute to the spatial averaging it applies to a bus-level residual field. The resulting student is $32.5\times$ smaller in parameter count and has half the message-passing depth, making it a candidate for subsequent edge-device benchmarking.

---


### 314. [The Tilted Sampling Problem: Optimism, Posterior Sampling, and Logarithmic Regret](https://arxiv.org/abs/2610.21908)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mohammad Pedramfar, Siamak Ravanbakhsh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many modern learning systems are used not to select a single best action, but to sample diverse high-quality outputs. Examples include entropy-regularized reinforcement learning, RLHF, and reward-guided generative modeling. Motivated by these settings, we study tilted sampling: an online learning problem in which the goal is to sample from the Gibbs distribution induced by an unknown reward function. We define sampling regret as the temperature-normalized cumulative KL divergence between the learner's distribution and the Gibbs target, corresponding to the suboptimality gap in entropy-regularized reward maximization. Our framework generalizes recent sampling-based and KL-regularized formulations in bandits and reinforcement learning. Our main contribution is a general regret framework that captures the different uncertainty structure of tilted sampling and classical regret minimization. While standard regret scales as $\widetilde{O}(\sqrt{T})$ due to first-order uncertainty, sampling regret is governed by squared confidence widths, yielding logarithmic-in-$T$ regret in standard settings at fixed temperature. We develop sampling analogues of UCB and Thompson sampling (UCS and TS$^2$) and provide unified regret decompositions that explain and extend recent logarithmic guarantees, including the first Bayesian sampling-regret decomposition based on new bounds for posterior-random Gibbs distributions. Our results show that learning to sample from a soft-optimal distribution is statistically distinct from learning to identify a hard optimum.

---


### 315. [Effectiveness of Hidden-State Probes for Localizing Reasoning Failures](https://arxiv.org/abs/2610.22046)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shubham Subhnil, Yannis Belkhiter, Erik Miehling 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Verifying the final answer of a long reasoning trace may show that the trace is wrong but it does not distinguish three cases. The problem may lie beyond the model's capability, another attempt would succeed, or one step in an otherwise recoverable trace made the trace fail. Standard hidden-state probes are trained on final-answer correctness, a label that conflates these cases. Monte Carlo rollouts distinguish the cases and locate the failing step at additional inference cost. We test the hidden states of 4B and 8B reasoning models for the failure type and the failing step and compare each probe with the strongest baseline that uses no hidden states. On incorrect 8B traces, the confidence probe, a calibrated correctness probe at a midpoint cutoff, misses 81% of cases in which a single step makes the trace unrecoverable and 47% of cases in which another attempt would succeed. A probe with a different training design over the same states reverses the ordering of these two kinds of failure, so either ordering can be read from those states. At both scales, no single tested probe locates the failing step more accurately than a rule based only on trace length, and at 4B a probe trained to predict that step fails to outperform this rule in any of 10 runs on identical traces. The confidence probe therefore indicates that an answer is wrong, but its failure-type ordering depends on its training design.

---


### 316. [FAOPs: Normal Forms and an Algebra for AI Agent Workflows](https://arxiv.org/abs/2610.22061)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ali Mohammadi Shanghooshabad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Organizations increasingly encode operational procedures as multi-step agent skills, here called Agent Operating Procedures (AOPs), that must be traceable, auditable, reproducible, access-controlled, and bounded in time and cost, requirements that regulated sectors make mandatory. Yet AOPs are typically kept as coarse-grained files, in which steps bundle actions, copied procedures drift apart, any step may reach any tool, and refactoring goes unchecked. We present Functional Agent Operating Procedures (FAOP), a formal theory that brings database-grade discipline to AI agent workflows. FAOP recasts each workflow as a typed function over scoped state and subjects an entire library to four progressive normal forms: Decomposed (FNF-1) splits a workflow into atomic steps, Typed (FNF-2) makes its data flow explicit and type-checked, Factored (FNF-3) gives each shared procedure a single canonical definition so a change propagates instead of drifting, and Scoped (FNF-4) confines every step to least-privilege tool access. Once normalized, every atomic step is a separate entity with a declared contract and can be type-checked, scope-confined, bounded, tested, traced, and audited on its own. A FAOP algebra of provably sound equalities turns refactoring and parallelization into compiler rewrites; orthogonal extensions add verified termination (+V), optimization (+O), and time and cost bounds (+B); and an architectural-level classifier (0-3) determines whether a workflow needs AI at all. Together, these make integrity, isolation, typing, termination, cost, and optimization compile-time concerns across the whole library, not runtime hopes. We implement the theory in SkillBase, an AOP management system (what PostgreSQL is to data, SkillBase is to AOPs), together with a separate executor that enforces these guarantees at run time. A worked financial workflow illustrates the approach end to end.

---


### 317. [Pathology foundation models for training-free case retrieval in salivary gland tumors](https://arxiv.org/abs/2610.22087)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Maximilian J. Roesel, Niklas Kiermeyer, Philipp Keyl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In pathology, pattern recognition relies on a frame of reference built through extensive training and experience, which may still fall short when encountering rare cancer subtypes. Archives of previously diagnosed tumors often contain relevant precedents, yet identifying the most relevant cases remains challenging. Here we explore whether content-based retrieval with current pathology foundation models facilitates rare cancer diagnostics without any task-specific training. Pathologists can query a digitized archive using a region of interest (ROI) from a whole slide image (WSI) and retrieve morphologically similar cases, along with their ICD-O codes and corresponding WSIs. The ROI can be selected manually or automatically using a gated attention-based multiple instance learning model. We evaluate our approach by leave-one-case-out on an imbalanced dataset of 137 salivary gland tumor cases spanning 12 ICD-O morphology categories, comparing four pathology foundation models (Atlas2, Atlas2-B, Atlas2-S, and UNI2h). Top-1/3/5 retrieval was 62.5%/76.7%/81.3% for Atlas2, 50.2/66.6/72.9% for UNI2h, 52.3%/71.5%/77.6% for Atlas2-B and 54.4/65.2/73.7% for Atlas2-S. Macro-averaged F1 ranged from 69.0% for the smallest model Atlas2-S to 76.6% for the largest model Atlas2 across the five classes with at least ten cases. Our modified Chamfer similarity separated correct from incorrect matches among the Top-5 more reliably for Atlas2 (AUC 0.754) than for Atlas2-B (0.679, p = 0.020) and Atlas2-S (0.653, p = 0.003), but not UNI2h (0.697, p = 0.196). Requiring no additional training or manual annotation, this approach makes departmental archives searchable with pathology foundation models, providing a low-barrier route to case-based differential diagnosis and extending the individual frame of reference to the collective experience of the department.

---


### 318. [MMSearch-OPD: Easy Made Hard, Hard Made Learnable for Long-Horizon Multimodal Search Agents](https://arxiv.org/abs/2610.22240)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Huanyao Zhang, Jiepeng Zhou, Jiaye Lin 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal deep search is moving from short queries to long-horizon investigations that continually acquire evidence. However, training such agents remains constrained by limited challenging training questions and insufficient process feedback.
We introduce MMSearch-OPD, combining controllable data refinement with joint reinforcement learning (RL) and on-policy distillation (OPD). Our Refine pipeline performs targeted expansion of reasoning chains derived from existing simple multimodal questions. Parameterized transformations control search depth and cross-modal evidence requirements while reusing existing image--question pairs. For training, answer rewards and lightweight behavior penalties guide RL, while the reward gap modulates token-level teacher guidance on imperfect student trajectories. An exponentially decaying distillation coefficient reduces teacher dependence as training proceeds.
Experiments show gains from data refinement and further improvements from joint training after SFT, indicating stronger long-horizon multimodal deep search capabilities.

---


### 319. [Routing Policy Optimization for Online Diffusion Reinforcement Learning](https://arxiv.org/abs/2610.22282)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Qiuhong Shen, Yiding Yang, Yuxin Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning can align visual generators with reward signals beyond their pretraining objectives, but existing score-function methods typically introduce stochasticity by perturbing the reverse denoising trajectory, leading to costly rollout-based optimization. We instead ask whether stochastic exploration can be introduced inside the generator while preserving its original sampler. Routing Policy Optimization (RPO) answers this question by turning attention routing into a stochastic exploration action. At a few selected denoising levels, each query block keeps its own block and samples further key blocks in proportion to the generator's native attention mass, or keeps dense attention. The sampled route perturbs the velocity of that transition, and a Gaussian likelihood around the dense velocity scores the perturbation with a score-function objective. RPO further uses a controlled two-rollout estimator: two rollouts share the same prompt, initial latent, routed denoising levels, and dense anchor layers, differing only in their sampled attention routes. Their reward difference provides an advantage signal for the routed transitions. Because the likelihood differentiates the dense velocity itself, the learned updates remain effective after routing is removed. At inference, RPO restores dense attention and retains the original deterministic sampler. Experiments on text-to-image and text-to-video generation show that RPO improves generation quality while achieving nearly 4x higher training efficiency than Flow-GRPO-style methods. Please see our project page at this https URL for visual results.

---


### 320. [Velox: Spatial Memory Makes World Models Efficient](https://arxiv.org/abs/2610.22311)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Qiuhong Shen, Shizun Wang, Xinchao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models turn actions and camera motion into long visual rollouts, making video a natural interface for interactive simulation. Such interaction requires responsive generation, yet coherent rollouts must retain visual memory of what has already been generated. Chunked video diffusion models usually keep this context in growing KV caches, so later chunks become progressively slower. To address this bottleneck, we introduce Velox, a training-free attention router for region-level context selection using frustum slab correspondences from streaming geometry. Velox represents historical blocks as camera frustum slabs with depth intervals and obtains current-block depth through recency-priority multiwarp. For well-covered regions, frustum slab overlap softly modulates each layer's model-derived block importance. Uncovered regions retain the model-derived route without geometric bias. The fixed token-block granularity matches FlashAttention-style tiled execution and reduces the attention term that grows with rollout length. Frustum slab construction runs asynchronously with denoising on the same H200. At chunk 48, Velox accelerates attention by $4.36\times$ and denoising by $2.43\times$. On the full 158-case WBench navigation split, it remains within 0.15 API-free average points of dense LingBot-Fast-Cam. Please see our project page at this https URL for more details.

---


### 321. [KnowGPO: Knowledge-Grouped Policy Optimization for Search Agents](https://arxiv.org/abs/2610.22331)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Siqi Chen, Zhengxi Lu, Yuchen Yan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep search agents solve knowledge-intensive tasks through long-horizon, multi-turn interactions, where assigning credit to individual search decisions is fundamentally difficult. Outcome-based reinforcement learning provides only a single terminal reward shared across an entire trajectory. Recent process-supervision methods aim to assign credit at finer granularity, but they typically anchor credit to either surface-level trajectory states or model-internal signals, both of which become unreliable in deep search where observations are heterogeneous and retrieved contexts are long and noisy. We propose KnowGPO, a reinforcement learning framework that aligns trajectories by the task-relevant knowledge they have acquired rather than by their surface observations. For each query, KnowGPO decomposes the information required to derive the answer into atomic knowledge conditions, and represents the state of a trajectory at each step by the subset of conditions it has satisfied. Trajectories sharing the same knowledge state are grouped for within-group comparison, and the incremental knowledge gain between consecutive steps serves as an environment-grounded process reward. Experiments on Xbench, BrowseComp-ZH, and GAIA show KnowGPO consistently outperforms outcome-only (GRPO) and process-supervision baselines (GiGPO, IGPO) by 3.8 to 4.2 points, with our 8B model rivaling or exceeding most 32B open-source systems.

---


> [!TIP]
> 当前位于：**301-321**（第 7/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-321**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
