# 🧠 大模型相关研究 | 2026年10月15日

> 本类共 **810** 篇论文：已确认 **758** 篇，待复核 **52** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 1. [LACRM: LLM-Guided Mining of Directed Advertiser Competition Relationships in E-Commerce Advertising](https://arxiv.org/abs/2610.13959)

**<font color=#1a73e8>作者：</font>** Xiang Shi, Yitian Kou, Bing Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In e-commerce advertising, ad platforms typically fail to model the externalities among advertisers when making optimization decisions: an advertiser's actual performance is largely shaped by rivals competing for the same users; these rivals typically operate in overlapping product categories and at comparable budget scales. However, capturing this rivalry as an explicit, reusable signal is challenging because it is directed, multi-faceted, and partially observable. Existing paradigms such as interaction graphs, taxonomy rules, and single-embedding models do not fully capture these properties. In this paper, we propose LACRM (LLM-driven Advertiser Competition Relationship Mining), a novel framework that constructs directed competition graphs with continuous edge intensities via a three-stage pipeline. LACRM moves beyond symmetric similarity through LLM-driven role-separated profiling, which enables asymmetric multi-route retrieval to uncover both realized and latent rivals. The framework further incorporates listwise learning-to-rank aligned with temporal auction behavior to accurately model directed competition intensity. In offline retrieval experiments on an industrial benchmark, LACRM outperforms strong directed GNN baselines and ablation variants. Multi-LLM and human studies provide complementary evidence that the recovered latent rivals reflect meaningful market competition rather than merely model-generated artifacts. In production A/B tests, LACRM-guided bidding and incentive allocation increase advertising revenue by 1.73% and 1.14%, respectively. The results demonstrate the practical value of explicit competition modeling in large-scale advertising systems.

---


### 2. [PRIME: Frequency-Aware Unified Pruning and Merging for MoE Compression](https://arxiv.org/abs/2610.13982)

**<font color=#1a73e8>作者：</font>** Shanfeng Huang, Rongqian Zhang, Zhou Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models have emerged as an effective paradigm for scaling large language models, yet their massive parameter footprint poses severe memory challenges for deployment. Existing compression methods typically treat expert pruning and merging as disjoint operations and rely on greedy heuristics, often leading to irreversible information loss or representational pollution. In this paper, we propose PRIME, a unified optimization framework for MoE compression via adaptive PRunIng and MErging. PRIME casts the discrete prune-merge assignment step as a global Integer Linear Programming over a frequency-weighted surrogate objective, jointly selecting pruning and merging decisions while accounting for expert usage. We motivate the frequency-aware objective through an error-bound analysis under fixed representative assignments, and show that the formulation favors high-frequency experts as centroids, promoting routing stability. Extensive experiments on Qwen3-30B-A3B and Qwen3.5-122B-A10B demonstrate that PRIME achieves strong accuracy retention across knowledge, coding, math, and long-context tasks, while serving benchmarks of merged models quantify the memory and throughput benefits of expert compression in vLLM.

---


### 3. [PsyBer-Agent: A Psychology-Driven User Agent for Recommender Systems](https://arxiv.org/abs/2610.13989)

**<font color=#1a73e8>作者：</font>** Chong Zhang, Qijie Shen, Haichao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating recommender systems before deployment requires simulators that remain realistic over long, closed-loop interaction cycles. Current LLM-based agents generally function as surface imitators that generate realistic short-term responses but fail to capture the underlying user dynamics such as fatigue, affect, and shifting preferences. We propose PsyBer-Agent, a psychology-inspired simulator that models these dynamics through its Psy-Engine. This engine represents each user with three evolving, model-defined latent states. To calibrate simulated behavior against real interaction logs, we align log-conditioned reference trajectories with simulator-generated latent-state trajectories via Unbalanced Gromov--Wasserstein optimal transport. This approach provides structured supervision for a lightweight policy without the computational burden of fine-tuning the backbone LLM. We also introduce WebSim and the PsyBer Benchmark, which encompass multimodal scenarios and seven recommender backbones. Our framework evaluates behavioral fidelity, latent-state consistency, robustness, and responses to social-cue perturbations. On the tested horizons, PsyBer-Agent shows lower behavioral discrepancy than the prompt-only simulators while maintaining stable performance under large-scale concurrent simulation for up to 5M queued simulation tasks under bounded concurrency. Code is available in the supplementary material and at: PsyBer-Agent: this https URL, WebSim Platform: this https URL.

---


### 4. [DoSA: Dots Sparse Attention](https://arxiv.org/abs/2610.13990)

**<font color=#1a73e8>作者：</font>** Fanxu Meng, Taosong Fang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse attention visits few keys, yet finding them can still require scoring every key with every indexer head. We introduce DoSA (Dots Sparse Attention), a lossless method for making this computation conditional while preserving exact token selection. Its central observation is that Top-K selection requires sufficient evidence to reject a candidate, not necessarily its full score. A seed set supplies a lower bound on the winning threshold. Nonnegative head projections and joint residual bounds upper-bound positive contributions, while activation-informed aggregation bounds the magnitude subtracted by negative heads. The certificate directs full scoring toward candidates that remain eligible; exact-score filtering further reduces writeback and selection work. We establish the certificate and its exact-selection conditions, and analyze how geometry and selection margins govern its effectiveness. Our GPU implementation accelerates the complete Indexer by up to 2.74 times over SGLang and 1.69 times over LiteTopK across English, Chinese, and code workloads. End-to-end evaluation on GLM-5.2 and DeepSeek-V3.2 achieves up to 1.94 times and 1.50 times time-to-first-token speedups over the two baselines, respectively.

---


### 5. [GameSmith: Scaling Zero-Sum Self-Play with Synthesised Games](https://arxiv.org/abs/2610.13995)

**<font color=#1a73e8>作者：</font>** Weixian Waylon Li, Jiaxin Zhang, Han Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training large language models (LLMs) on two-player zero-sum games provides a verifiable reward, and the gains have been shown to transfer to general reasoning. Existing pipelines, however, rely on a handful of hand-written games and on advantage estimators tied to them, so both the supply of games and the advantage estimate on a large corpus limit scaling. We present GameSmith, which scales both. An LLM synthesises games inside templates whose reward, observation, and hidden-information code is fixed. Each game is verified by seed-paired replay and by an independent re-implementation of its specification, then expanded into encoding, rule, and size variants, giving 26 new games in 29 families and 336 verified variants from the three SPIRAL templates. The model is distilled from the self-play of a larger teacher (Qwen3-32B) on these games and then trained by self-play reinforcement learning with CRAB, an advantage estimator that credits each decision against a shrinkage estimate of the expected return of its position and is defined on every variant. On Qwen3-4B-Base, distillation raises the 13-benchmark mean pass@1 from 45.5 to 62.5, above the three SPIRAL games at the same budget, and self-play with CRAB reaches 64.9. The ordering holds across models, and transfer grows with the number of game families.

---


### 6. [SemTree: Judge-Aware Semantic Decision Trees for Inspectable and Repairable Rule Decisions](https://arxiv.org/abs/2610.13999)

**<font color=#1a73e8>作者：</font>** Jincheng Gao, Wei Ding, Shuo Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rule decisions such as content moderation, advertising compliance, and eligibility checks combine several conditions, exemptions, and missing-information cases, and an error can be fixed only once the failing condition is known. We introduce SemTree, a framework that represents a rule decision as a semantic decision tree: each node is a natural-language question with explicit Yes/No/Unknown criteria, a pluggable semantic judge answers it, and the branching structure is compiled on the answers that this judge actually gives. The executed path is the reasoning behind every decision, so errors are repaired where they occur: a reviewer corrects a single node and replays the rule, corrected nodes become training labels for the judge, and a tool-using LLM editor revises questions and subtrees while observing execution results. On all 8,276 ShARC test cases, a tree executed by a hosted judge reaches 67.70% accuracy with 2.99 questions per case, on par with asking the same judge for the final label (68.23%); an earlier tree compiled for a different judge scores 47.87% when executed by this judge, while a new tree compiled on this judge's answers to a 12-question initial pool already scores 64.39%. Node-level repair raises BANKING77 accuracy from 82.04% to 86.16%, an explicit exemption node cuts the false positives of a Chinese e-commerce moderation clause from 24 to 5, and a trained editor raises the development accuracy of edited trees from 64.47% to 73.35%.

---


### 7. [VH-GPO: Verified Handoff for LLM Agent Reinforcement Learning](https://arxiv.org/abs/2610.14000)

**<font color=#1a73e8>作者：</font>** Haoze Li, Peng Zhou, Peiyuan Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-relative reinforcement learning methods such as GRPO train large language model (LLM) agents by comparing rollouts for the same task. When every trajectory in a group fails with the same reward, relative advantages collapse toward zero, leaving no useful learning signal. A frozen teacher can recover from a student-visited state, but letting it complete the task makes the recovered suffix entirely teacher-generated. We ask: after repairing a student failure, when should control return to the student? We propose outcome-verified teacher-student handoff, instantiated in Verified Handoff for Group Policy Optimization (VH-GPO). The teacher provides enough support to reach a state from which the student can succeed, then returns control so that successful experience is again student-generated. Given an environment-verified teacher recovery, VH-GPO selects the earliest independently confirmed handoff point found within a bounded search budget. With Qwen2.5-1.5B, VH-GPO increases success rates over GRPO from 59.38% to 94.79% on ALFWorld and from 71.62% to 77.34% on WebShop. Improvements also hold with the 7B student, for which additional teacher and student output tokens amount to 1.77% and 2.61% of regular student rollout output tokens on ALFWorld and WebShop, respectively. Ablation studies demonstrate the effectiveness of the key components. These results support using verified teacher assistance to repair failures while reinforcing the student's ability to complete tasks independently.

---


### 8. [PreSO: Privileged Representation Isolation for On-Policy Self-Distillation](https://arxiv.org/abs/2610.14001)

**<font color=#1a73e8>作者：</font>** Yuhang Yang, Mingxuan Xia, Chao Ye 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) uses a self-teacher conditioned on privileged information to turn the sparse outcome signal of reinforcement learning with verifiable rewards (RLVR) into dense token-level supervision. Yet the teacher's advantage may depend on information unavailable to the student at inference, raising a central question: which privileged changes are worth distilling? We use cross-problem recurrence as an empirical cue for potentially reusable guidance. Comparing the representation shifts induced by full solutions and compact hints, we find that hint-induced shifts are more concentrated and directionally consistent across problems, and yield more sustained downstream gains despite revealing less information. Motivated by this association, we propose Privileged Representation Isolation for On-Policy Self-Distillation (PreSO). At the source, PreSO uses compact hints to limit the solution-specific detail entering the privileged shift. At the target, it estimates a leading low-rank subspace from shifts pooled across related problems, projects the privilege-induced correction onto this subspace, and adds it to the student's unprivileged representation to form the representation-level distillation target. The selected subspace serves as an operational proxy for recurring structure, rather than a guaranteed separation of transferable and instance-specific information. On five competition-level mathematics benchmarks, PreSO consistently outperforms strong baselines across Qwen3-1.7B, 4B, and 8B, improving average accuracy over the base model by 6.8, 9.0, and 10.0 points. Beyond peak accuracy, PreSO attains the highest final-checkpoint average at every model scale, with improvements that persist through the end of training.

---


### 9. [Artificiality's First Exam: An LLM-Referenced C-test for Supraintelligence](https://arxiv.org/abs/2610.14005)

**<font color=#1a73e8>作者：</font>** Jose Hernandez-Orallo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Under the accelerated pace of AI development, any benchmark whose difficulty is calibrated with humans or current AI systems becomes circular, or saturates soon. How can we then evaluate machines that may become more capable than the current machines and the people who write the tests? One answer to the question hinges on inverse problems, inductive inference questions for which difficulty depends on the complexity of the underlying mechanism, given the observations and the previous knowledge. Levin's Kt, a computable variant of Kolmogorov complexity, puts a theoretical upper bound to that difficulty, balancing the simplest representation encoding for the mechanism and the logarithm of the time steps to run that mechanism. Previous tests derived from Levin's Kt, such as the original C-test, are based on minimalistic Universal Turing Machines (UTM), capable of very limited representations and no previous knowledge. Reasoning large language models (LLM) are UTMs that capture a compendium of human culture as knowledge, using prompts as natural language programs. This paper presents the first test based on Levin's Kt with LLMs as representational machines. Fresh test items can be produced at high difficulties, estimated in a ratio scale measured in bits, before any human or frontier model can solve them. We formalise the measure, devise a lightweight generation and certification pipeline, explore the effect of the power of the reference machine and the gap between examiner and examinee. We produce a first battery of certified items administered to twelve LLMs. The resulting agent characteristic curves decrease with difficulty, down to the uncharted high-difficulty region, the supra-intelligence window of items we can certify, yet beyond generations of frontier intelligence.

---


### 10. [Coding LLMs Can Be Harnessed to Learn Interpretable Models from Data](https://arxiv.org/abs/2610.14006)

**<font color=#1a73e8>作者：</font>** Aditya Kumar, Cassandra A. Cohen, William W. Cohen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Since compact, interpretable classifiers correspond to simple programs, it is natural to ask if LLM-based coding agents can be used to learn interpretable models from data. In this paper we present a simple harness that repeatedly prompts a coding LLM to produce the next rule in a rule set, given a sample of labeled examples. We show that this approach is competitive with, and often superior to, state-of-the-art rule-learning methods on tabular data, especially with small training sets, and wins by large margins on text, including against another LLM-based rule learner; that this approach outperforms standard harnesses, and that the approach immediately leads to new kinds of interpretable models, since coding agents are not restricted to search a highly restricted hypothesis space. In addition to the advances made in learning interpretable models, these results are of interest because they introduce a new class of coding benchmarks - construction of interpretable classifiers - which includes quantitative measurements of output quality (i.e., test-set error) and existing mature ``specialist coding algorithms'' (i.e., existing learning methods).

---


### 11. [What Can Language Models Inherit from Solomonoff Induction? Limits, Attainable Properties, and What Served Conditionals Reveal](https://arxiv.org/abs/2610.14007)

**<font color=#1a73e8>作者：</font>** Luan Ozelim, Abicumaran Uthamacumaran, Hector Zenil  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A familiar line of reasoning runs as follows: language models are flexible approximators trained under a strictly proper loss, so scale brings them closer to Solomonoff induction, and their predictive success is evidence of that approach. We apply known results from algorithmic information theory, universal prediction and Bayesian consistency. In its uniform form the conclusion holds for no computable model: each has cheap environments it never learns, and every uniformly computable family of total predictors shares one on which each member fails beyond a horizon growing with its index, so ``closer'' can hold only pointwise, one environment at a time. Nor could the offered routes certify even that: finite evaluation cannot certify agreement on rarely reached contexts, perfect corpus fit selects the corpus law as prior, and asymptotic criteria cannot see the constants that carry Solomonoff's guarantee. Our lens is the Kraft inequality read for predictors. Every model has at most the same budget of predictive success, so Solomonoff's predictor, which leaves part of it unspent, differs from a language model not in having more of it but in where it spends it; on mutually singular families this is exact, and only full-mass Bayes mixtures reach the frontier. We then discuss what is inheritable, including in-context learning as amortised Bayesian inference; what survives within a context window; which Solomonoff-like properties a deployed system should have or avoid; and what served conditionals determine. A closing table states what common practices certify and what to report. Tests are developed in a companion paper.

---


### 12. [When Log Parsing Removes What Matters: Detecting Failures in Distributed GPU Workloads](https://arxiv.org/abs/2610.14009)

**<font color=#1a73e8>作者：</font>** Boyuan Cui, Yuyang Zeng, Yifang Tian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large AI models increasingly rely on distributed GPU execution, yet it remains unclear whether established failure analysis methods transfer effectively to this setting. We introduce GF-Bench, a PyTorch-based framework and dataset for generating diverse failures in distributed GPU workloads. The framework supports extensible workload and fault-injection logic; based on this design, the current release targets failures visible in multi-GPU communication logs and provides 220 labeled two-GPU executions covering normal runs, CUDA out-of-memory fail-stop failures, and persistent straggler fail-slow failures. Using GF-Bench, we evaluate three sequence-based methods (DeepLog, LogAnomaly, and LogBERT) and the LLM-based LogPrompt on parsed logs, and additionally evaluate LogPrompt on raw logs. On parsed inputs, no method reliably detects both failure classes, and the highest overall F1 score is 0.667. Raw inputs raise the overall F1 score of in-context LogPrompt to 0.983, at 9.0x its average input-token usage and 8.7x its per-run cost. These results expose a substantial trade-off between effectiveness and efficiency: generic log parsing lowers operational cost but discards the distributed execution context required for accurate failure detection. GF-Bench provides a reproducible basis for studying cost-efficient analysis methods and can be extended to additional GPU workloads and failure types.

---


### 13. [OPMD: On-Policy Mechanism Distillation Beyond Output Supervision](https://arxiv.org/abs/2610.14022)

**<font color=#1a73e8>作者：</font>** Yingdong Shi, Zhihong Li, Changming Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) improves language-model by supervising a student on prefixes sampled from its own policy, but its supervision remains confined to the output space. Consequently, OPD transfers what a teacher predicts without supervising the intermediate computation that produces those predictions. Simply distilling intermediate representations like representation matching is insufficient since teacher and student representations may differ geometrically, and even well-aligned hidden states need not be usable by the student's subsequent computation. We introduce On-Policy Mechanism Distillation (OPMD), which transfers teacher-derived intermediate computation while explicitly accounting for its compatibility with the student. OPMD first constructs a student-compatible teacher that transforms teacher representations into intermediate states usable by the student's downstream computation, then it internalizes these states from on-policy trajectories. OPMD achieves the highest average accuracy among the evaluated distillation baselines in all three teacher--student settings, and generalizes to multi-teacher distillation and cross-family supervised fine-tuning. Further analyses show that mechanism supervision yields more effective reasoning and meaningfully alters the student's intermediate computation and solution strategies, supporting that it transfers information beyond output supervision alone. Together, these results establish mechanism-level supervision as an effective way to move on-policy distillation beyond output supervision, enabling students to learn inner mechanisms they can use and internalize.

---


### 14. [Beyond a Better Score: Long-Horizon Agentic ML Development and Evaluation Protocol for Physics Time Series](https://arxiv.org/abs/2610.14024)

**<font color=#1a73e8>作者：</font>** Yue Ma, Lucas Venetoulias, Akbota Assan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics time-series data are central to fundamental discoveries involving dark matter, neutrinos, and gravitational waves. Machine learning has shown strong potential to recover weak scientific signals buried in complex noise. Recent LLM-agent systems further automate ML development, but existing approaches are often driven primarily by one or a few numerical scores. In pursuit of a better score, agents may exploit shortcuts, trigger mode collapse, or game the evaluation procedure, producing models that achieve high scores but are scientifically invalid. We introduce SIDERIUS, an LLM agent system designed to move beyond a better score toward scientifically valid, long-horizon ML development. SIDERIUS combines contract-defined composable capabilities for flexible orchestration and human-in-the-loop, a multi-layer scientific evaluation protocol that distinguishes valid models from unhealthy or gaming models, and resource-aware exploration for computationally expensive scientific ML. In our TIDMAD benchmark, SIDERIUS with a GPT-based orchestrator achieves the highest Valid-model proposal rate of 63.8% and the best valid denoising score of 2.744, compared with 1.6% and -0.647, respectively, for the same GPT model using the general-purpose Codex coding agent. We further benchmark SIDERIUS on three additional physics time-series datasets, demonstrating its reuse and performance across different tasks. Together, these results suggest that progress in agentic scientific ML should be measured beyond a better score, by how an agent explores and by whether the models it produces can be trusted as science.

---


### 15. [Contrastive Covariance Subspaces for Activation Steering](https://arxiv.org/abs/2610.14025)

**<font color=#1a73e8>作者：</font>** Alexandros Xenos, Manos Plitsis, Niki Foteinopoulou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering controls large language model behavior by adding a direction to hidden activations during inference. For steering to work well, that direction must be a pure signal for the target concept: any confound entangled with it, such as an incidental topic or writing style, is injected into the residual stream alongside the concept itself and degrades the generated text. We introduce Contrastive Covariance Steering (CCS), a training-free method that eliminates this confound variation. CCS projects steering vectors to a low-dimensional subspace obtained in closed form by solving a contrastive variance objective, which retains the directions along which the target concept varies while suppressing directions shared with the other classes. Across three LLMs and four steering domains, CCS consistently beats all baseline steering methods in all $12$ model-domain settings. The largest relative improvement occurs on AxBench and Emotion where we outperform the next strongest steering baseline by $48$ to $70\%$ and $13$ to $27\%$, respectively. Furthermore, CCS outperforms naive difference-of-means steering by up to $151\%$, showcasing the importance of deconfounding concepts. A toy experiment verifies our motivation on why: planting a topic nuisance into the training data reduces unprojected steering by $46\%$, whereas CCS loses only $12\%$ and recovers most of the gap to an oracle that explicitly deletes the planted direction. A human study with $23$ raters on $296$ generations reproduces the LLM judge's ranking. Our extensive ablation verifies the importance of our method's components and robustness to the number of nuisance classes. Finally, we extend our method to multi-turn conversations, where CCS sustains both concept expression and fluency, matching system prompt performance as other steering methods drift.

---


### 16. [Pick the Mixture, Not the Samples: Combinatorial Data Selection for LLMs](https://arxiv.org/abs/2610.14028)

**<font color=#1a73e8>作者：</font>** Luyang Zhang, Jialu Wang, Bebei Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data selection for LLM fine-tuning faces two facts about real training: data pools draw from many distinct domains, and evaluation spans diverse tasks. As a result, the same sample helps different tasks differently, and samples interact during training so that a subset's value is not the sum of its parts. Current data-selection methods leave these realities largely unaddressed. We formalize them as Combinatorial Data Selection (CDS), a framework that separates attribution (how samples are scored) from selection (which subset to pick) and models the non-additive interactions among samples. On a real instruction-tuning data pool, we find substantial cross-domain complementarity (joint utility exceeds the sum of singletons), alongside redundancy within domains. Inspired by this, we propose Mixture-then-Select, a two-stage algorithm that first decides how many samples to take from each domain, then ranks samples within each domain by attribution score. Theoretically, the gap to the optimal subset is linear in the selection size and independent of data pool size. Empirically, Mixture-then-Select outperforms strong baselines by 20 to 54%, is robust across attribution methods, and works across different models and data pool sizes. The framework also extends to the data purchasing problem under a budget constraint when sample prices vary. Our findings suggest that allocating selection across domains offers a promising path toward more efficient and effective data selection for modern LLMs.

---


### 17. [Can We Trust This Evaluation? Instance-Level Reliability of LLM-as-a-Judge](https://arxiv.org/abs/2610.14029)

**<font color=#1a73e8>作者：</font>** Yang Ba, Michelle V. Mancenido, Rong Pan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-judge evaluation commonly aggregates multiple judges' decisions into a majority vote, yet this panel decision process does not guarantee that the evaluation of an individual item is reliable. We propose Structured Cross-fitted Uncertainty Risk (SCUR), a label-free approach for estimating instance-level evaluation reliability based on the judge panel's behavior. A latent measurement model serves as the backbone for measurement system analysis, from which SCUR derives three complementary signals capturing panel uncertainty, measurement cross-entropy, and perturbation sensitivity. These three sources of evidence are combined into a risk score. We evaluate the SCUR approach on five real-world benchmarks using majority-vote error ranking, selective trust, and risk stratification. Furthermore, we show our approach to be more effective at detecting high-consensus risk items, which are the blind spots for many other LLM-as-a-judge evaluation methods.

---


### 18. [Refuses in Chat, Complies with Arms: LLM Refusal Does Not Survive Robot Control](https://arxiv.org/abs/2610.14043)

**<font color=#1a73e8>作者：</font>** Edward Sun, Christopher Leet, Sravanthi Machcha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Frontier language models reliably refuse to explain how to cause physical harm. We ask whether this refusal survives when the same models control a robot. We introduce RoboHarm, a physical AI safety benchmark of harmful robot instructions, and test seven frontier models on it. We hold each model fixed and vary only the interface, from text to Code as Policies to vision agents that command end-effector poses or joint angles. In a MuJoCo simulation twin of a bimanual YAM arm robot, refusal falls from 73% of text requests to 18-25% once the model controls the robot, even when it is told what the objects are. On the physical robot, six models with end-effector control refused 18% of 612 trials against 19% in sim, and three with joint control refused 41% of 252 against 31%. GPT-5.6 Sol refused every text request and none of its trials on the real robot. Case studies of the robot transcripts show that models miss the hazard, name it without inferring its consequences, or act despite recognizing it, and their refusals often hinge on uncertainty about what an object is rather than on the harm of the action. Safety alignment learned in text thus fails to generalize to action, leaving current models with a poorly understood safety gap in the physical world.

---


### 19. [Auditing LLM Program Search for Bermudan Stopping with Primal--Dual Certificates](https://arxiv.org/abs/2610.14063)

**<font color=#1a73e8>作者：</font>** Yuhua Qian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM program-search agents are usually judged by the score that drives their search. We study LLM-driven search over Python exercise policies for Bermudan options, an optimal stopping problem where a trusted evaluator owns the simulation and a dual upper bound~$U$. For any policy, $0 \le V^\star - L_\pi \le U - L_\pi$; we report Monte Carlo estimates of both bounds with their sampling error. We audit 24 generation attempts from two pipelines, a six-pair feedback-representation ablation, and a holdout evaluated after selection was frozen. No selected generated program improves on Ridge LSMC consistently or by more than Monte Carlo uncertainty; holdout gap scores lie within $0.002$ of it. On six one-dimensional puts, a high-precision binomial reference places Ridge within Monte Carlo noise of optimal and attributes 99\% of the estimated gap to dual-bound looseness, so this dual audits validity but cannot certify progress at the search's scale. Structured memory showed no benefit over score-only memory in this ablation. Whether search ``worked'' depends on reporting rules: retaining the initial reference, freezing selection before holdout, and counting failures.

---


### 20. [Is the Future Predictable? Modeling Future Predictability for Reliable Temporal Reasoning](https://arxiv.org/abs/2610.14073)

**<font color=#1a73e8>作者：</font>** Yongyi Huang, Huaping Zhang, Wenyao Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) remain unreliable when reasoning about the future. Existing models often overlook the difference among future states, committing to specific answers even when the queried facts are inherently volatile. To capture this challenge, we introduce ChronoRegime, a future-oriented temporal reasoning task that requires models to determine whether historical temporal evidence justifies commitment to a future answer. Furthermore, we propose Confidence-Aware Temporal Reasoning (CTR), a framework that estimates future predictability from temporal dynamics and regulates answer commitment accordingly. Rather than performing unconditional forecasting, CTR commits only when the reconstructed evidence supports the target future state. Across multiple LLMs, CTR improves strict overall accuracy by 6.7 percentage points and reduces hallucination rates by 18.4 percentage points on average over the plain QA baseline. These results demonstrate that explicit predictability assessment is an effective mechanism for safer and more reliable temporal reasoning under future uncertainty.

---


### 21. [One Model, Multiple Compute Budgets: Multi-Ratio ConceptMoE for Flexible Compute Across Turns](https://arxiv.org/abs/2610.14074)

**<font color=#1a73e8>作者：</font>** Yiyang Fu, Zihao Huang, Dongchen Han 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models typically support different inference budgets through separate model sizes or fixed compute configurations. In multi-turn interactions, however, compute demand can vary substantially across turns. Using a high-compute model for every turn wastes computation, while routing among independent models may require rebuilding model-specific history states after switches. We therefore ask whether a single shared model can support multiple compute budgets that can be flexibly assigned across turns. We introduce Multi-Ratio ConceptMoE, which jointly supports token-to-concept compression ratios of 2, 4, and 8 (CR2/CR4/CR8) within a shared backbone. Lightweight full-token modules reduce compression-independent cost, ratio-specific boundary routers support distinct compression levels, and cross-ratio training enables mixed-ratio processing within the same context. Across PTBench and SFTBench, the three fixed modes outperform their compute-matched MoE baselines in all 6 comparisons while remaining competitive with independently trained fixed-ratio specialists. On CodeChat and CoSQL, mixed-ratio inference improves the accuracy--compute trade-off, outperforming the Large MoE by 5.87 and 2.68 percentage points while reducing FLOPs by 41.1% and 12.3%, respectively. Under the same turn-wise budget schedule, Multi-Ratio ConceptMoE further reduces FLOPs by 78.4% and 46.9% relative to routing among independent models. These results demonstrate that a single shared model can provide multiple compute budgets for flexible compute allocation across turns.

---


### 22. [SAGE: Efficient Protected Vision-Language Inference on Smart Glasses](https://arxiv.org/abs/2610.14089)

**<font color=#1a73e8>作者：</font>** Zhimin Li, Pan Wang, Jingxian Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smart glasses are a promising platform for vision-language assistants, but private split inference remains expensive: protecting visual representations before transmission does not remove the cost of on-device vision encoding, wide protected tokens, or hardware-unaware execution. We present SAGE (Smart-glasses-Aware Guarded Encoding), a hardware-aware framework for efficient protected VLM inference on smart glasses. SAGE keeps raw images and unprotected visual tokens on the trusted device, reduces visual input cost, executes shape-specialized INT8 graphs, and compresses protected representations into compact 256-dimensional INT8 packets before transmission. Unlike efficiency methods optimized only for nominal model size, SAGE selects its operating point using downstream answer quality together with measured latency, memory, and thermal behavior on real Mentra Live glasses. On a matched Qwen workload, SAGE reduces glasses inference latency by 39.18%, device-sensor temperature rise by 21.91%, and protected packet size by 96.56%, while retaining 85.62% of the protected reference's relaxed utility and comparable prompted containment. Direct glasses-to-phone tests deliver all 192 packets and reduce median packet-plus-acknowledgment time from 71.3 to 10.0 ms. The compact protected interface also transfers across four additional VLM families. These results show that private wearable VLM inference must be optimized jointly across representation protection, communication, and real-device execution rather than through model compression alone.

---


### 23. [Fin_Agent at FinEval 2026: Task-Aware Methods for Multilingual Financial NLP](https://arxiv.org/abs/2610.14101)

**<font color=#1a73e8>作者：</font>** Mohotarema Rashid, Tanzina Hossain, Xiaoying Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Fin_Agent, our submission to the FinEval 2026 shared task on multilingual fi nancial language understanding. Our sys tems address Greek financial named-entity recognition, Japanese implicit communication recognition, and multilingual financial ques tion answering. For Greek NER, we com bine annotation-aware numeric rules with zero shot Qwen2.5-32B classification, achieving 0.9521 public F1 and 0.8884 private F1. For Japanese implicit communication, an inter pretable cue-based ordinal scorer achieves 98.0% test accuracy. For multilingual financial QA, BGE-M3retrieval with Qwen3-32B gen eration achieves 0.3023 and 0.3419 ROUGE-1 F1 on the public and private splits. Key limita tions include dataset-specific rules, handcrafted cues, and limited supervision. Implementa tion code is available this https URL Rashidnira/finagent-fineval-2026.

---


### 24. [Does System One Transfer? Calibrated Typed-Decision Models, Label Budgets, and Translation for Indonesian Regional Languages](https://arxiv.org/abs/2610.14112)

**<font color=#1a73e8>作者：</font>** Romi Fadli, Rusdah, Wahyu Ramadani Putri Utami 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Calibrated typed-decision ("System One") models return a label and a probability in a single forward pass at a small fraction of the cost of large language models (LLMs), yet their evaluation has been almost entirely English. We report a pre-registered evaluation of the commercial Jev model and the open Laya-multilingual model on Indonesian regional languages, using the parallel NusaX sentiment (12 languages) and NusaTranslation sentiment and emotion (7 languages) test sets. Jev is more often correct on sentences that are lexically closer to Indonesian in all three datasets, and presenting the human Indonesian translation instead raises its accuracy by up to 37.2 points, most in languages distant from Indonesian. Its expected calibration error does not grow on regional languages, but its ability to rank its own errors degrades in all three datasets. Retrained classifiers need more than 500 labels per language to match zero-shot Jev in 9 of 10 NusaX regional languages. A confidence-gated cascade that sends Jev's 10-30% least confident decisions to a local IndoBERT classifier matches or exceeds the better of the two systems, and routing to an LLM instead matches that LLM at 24-77% lower API cost. Of six further commercial LLMs (three Claude and three GPT models), five are 4-14 points more accurate than Jev, at several hundred times the API cost where it is reported, while the smallest (Claude Haiku) is less accurate. We release the pre-registration, code and all predictions.

---


### 25. [The Silent Failures in Agentic Data Science](https://arxiv.org/abs/2610.14115)

**<font color=#1a73e8>作者：</font>** Xue Li, Hongqian Xia, Daniel Gomm 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have significantly lowered the barrier to writing code. Naturally, this has also led to the development of data science agents that promise automating the design and execution of data science from task formulation to model development. Existing evaluations of agentic data science (agentic DS) assess downstream predictive performance and code correctness, providing preliminary insight in agentic DS capabilities. We argue that these evaluations overlook the fundamental principles of data science: methodological data science- and domain knowledge. As such, only assessing downstream performance masks methodological failures such as data leakage and inappropriate validation, limiting the development of robust agentic DS systems. In this paper, we evaluate agentic DS beyond accuracy from three different angles: 1) a large-scale analysis of failure modes in common agentic DS frameworks and models across 220 data science tasks, 2) a reusable and extensible test suite with curated data science tasks that test for six specific failures in a controlled manner, and 3) a qualitative assessment of agentic DS pipelines against expert solutions on Kaggle competitions. We find that the majority of agentic solutions contain at least one failure mode despite the complexity of agentic harness or model capacity. Moreover, we identify a positive correlation between the occurrence of data leakage failures and predictive performance, confirming the necessity to evaluate agents beyond accuracy. Our qualitative analysis shows that DS agents generally lack problem solving creativity and domain knowledge, compared to competition-winning data scientists. We believe that principled failure mode analysis, as presented here, should be integral part of agentic DS evaluations, and that the insights we surface will be key in developing trustworthy agentic DS pipelines.

---


### 26. [ClawLoop: Self-Improving Agents via Harness-Native Training Loop](https://arxiv.org/abs/2610.14118)

**<font color=#1a73e8>作者：</font>** Hansi Yang, Linji Hao, Hongyan Hao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of Large Language Models (LLMs) has driven their deployment toward general-purpose harness environments, where LLM-based agents operate in sandbox workspaces and interact directly with file systems and shells. While numerous post-training pipelines exist for tool-use agents, their counterparts for harness-based agents remain scarce and are predominantly one-shot and teacher-dependent: a stronger external model synthesizes tasks and collects trajectories, the target agent is trained once, and evaluation results are consumed by human researchers rather than fed back into the loop. Such pipelines are inherently bounded by the capability of the external model and the scope of human prior, leaving no room for self-improvement. To address these limitations, we propose ClawLoop, a framework that enables self-improving without any external teacher model and with minimal prior dependencies. ClawLoop composes three phases into a self-sustaining cycle: Task Synthesis, which generates a diverse pool of training tasks via two complementary construction routines, applies diagnosis-conditioned difficulty growth followed by both agent-free and agent-based task validation; Training, which updates the agent via SFT and/or RL; and Diagnosis and Feedback, which analyzes the agent's rollout behaviors to produce a capability analysis report that will be used as feedback for task synthesis in the next iteration. Using Qwen3.6-27B as the loop model, ClawLoop yields consistent improvements on SkillsBench, Claw-Eval-Live, and ClawGym-Bench. The iteratively refined tasks are further transferred to smaller-scale Qwen3.5-4B and 9B models with gains across all benchmarks, validating data quality independently of the loop model.

---


### 27. [The AI's Poker Face: Contrasting Persuasion and Sycophancy in Voice-Based Multi-Turn Conversations](https://arxiv.org/abs/2610.14124)

**<font color=#1a73e8>作者：</font>** Ilia Frantzi, Bernie Hogan, Max M. Lang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As interactions with large language models (LLMs) become increasingly routine, concerns about their capacity to influence users' beliefs grow. Yet how such influence unfolds in sustained dialogue remains insufficiently understood. We conduct a randomized controlled experiment (N=616) where participants engage in multi-turn, spoken dialogue with an LLM under three conditions: non-directive, and two directive conditions maintaining opposing stances on a polarizing topic (the merits of feminism). We examine opinion change, rhetorical strategies, and sycophancy, distinguishing the semantic content of LLM argumentation from the pragmatic strategies used to manage the interaction. Both directive conditions shifted opinions toward their assigned stances, but asymmetrically: shifts were larger for pro-feminist positions, which also elicited distinct rhetorical strategies. The non-directive condition, likewise shifted opinions pro-feminism. Social sycophancy, though near-universal, was not associated with opinion change; instead it shaped users' subjective experience. Our findings highlight distinct roles for argumentation and sycophantic accommodation in AI influence.

---


### 28. [Long-Horizon-Terminal-Bench 2.0: Automating Diverse Task Construction and Measuring Sustained Agent Progress](https://arxiv.org/abs/2610.14146)

**<font color=#1a73e8>作者：</font>** Zongxia Li, Zhongzhi Li, Yucheng Shi 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon terminal benchmarks measure whether an agent can sustain progress through extended workflows with process rewards, not only whether its final state passes a binary check. We present Long-Horizon-Terminal-Bench 2.0 (LHTB 2.0), an extension of Long-Horizon-Terminal-Bench that preserves its 46 original tasks while correcting task and evaluation-infrastructure defects and extending 31 tasks. LHTB 2.0 contains 77 tasks across 13 domains and eight task types. The extended tasks are produced through a systematic reconstruction-task pipeline. We start from a working scientific or engineering artifact, then use a parameterized reference implementation to generate multiple scenarios, reveal six as behavioral evidence, hold out three for evaluation, and use dense progress ladders to reward partial progress while preventing memorization of public outputs. We also extend the evaluation horizon from 90 minutes to three hours and record verifier checkpoints every 30 minutes, enabling direct measurement of sustained progress within a run. Across 1,145 scored model-task runs from 15 frontier models, GPT-6-astra leads with dense mean reward 0.69 and 37 tasks at R at least 0.95, followed by GPT-5.6-sol with dense mean reward 0.67 and 32 tasks at the same threshold. On the 30 reconstruction tasks, binary verifier scores average 0.221, whereas dense ladder scores average 0.653, showing that outcome-only evaluation discards substantial intermediate progress. LHTB 2.0 provides a broader, hardened, and process-aware testbed for studying reliable agent execution over hours.

---


### 29. [Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation](https://arxiv.org/abs/2610.14162)

**<font color=#1a73e8>作者：</font>** Hermann Kumbong, Ishan S. Khare, Iddah Mlauzi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) offer parallel sampling for faster generation than autoregressive models, an increasingly important advantage as inference becomes a dominant computational workload. However, DLMs degrade quickly with fewer sampling steps, process the full sequence at every step, and require many passes over the dataset to reach good quality. We introduce Next-Concept Modeling (NCM), a two-stage, coarse-to-fine framework: a multiscale residual VQ-VAE encodes text into a hierarchy of discrete codes, and a transformer generates one level at a time, predicting all codes within a level in parallel. At matched parameter scales, NCM achieves better generative perplexity than the strongest DLM baseline on LM1B while running $21\times$ faster. On OpenWebText, NCM is competitive with the strongest DLM while running $10\times$ faster; on XSum, it matches the strongest DLM's ROUGE-L while being $31\times$ faster. On the reasoning task of Sudoku, NCM outperforms autoregressive and diffusion baselines across all difficulty levels, using fewer function evaluations. On the reasoning task of Sudoku, NCM outperforms autoregressive and diffusion baselines across all difficulty levels, using fewer function evaluations.

---


### 30. [Unconstrained CTI-REALM with Open-Weights](https://arxiv.org/abs/2610.14180)

**<font color=#1a73e8>作者：</font>** Sahil Garg, Ruhi Gottumukkala, Vishal Agarwal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Organisations that want language-model agents for security work face a choice between open-weight models, which they can run and audit themselves, and far more expensive closed frontier models. We study that choice on CTI-REALM (arXiv:2603.13517), a benchmark in which an agent turns a threat-intelligence report into a working detection by querying a live telemetry store. We evaluate twenty-six models, nineteen open-weight and seven closed, under a common harness, scorer and panel of LLM judges. Our main finding is that an open-weight model can match the strongest closed models at less than a tenth of their cost, provided it is given enough turns. The benchmark's published limit on agent messages is a confound: a task that exhausts the limit scores zero on every checkpoint, including those it had already passed, so results at that limit partly measure which models finish in time. At the published limit the leading open-weight and closed models cannot be distinguished. With the limit relaxed, the models it was truncating recover, and the highest rewards belong to open-weight models. Among the leading models, price is a poor guide to capability: models with similar rewards differ in cost by more than an order of magnitude. Because the benchmark's checkpoint scores largely record what an agent did or mentioned, we also introduce stage-level metrics that score what the agent submits, by executing its detection queries in the telemetry store and judging its outputs against the answer key. Rather than combining them into one more overall reward, we show that different models lead different stages, which suggests routing each stage of the workflow to the model that performs it best rather than choosing a single model by its overall score. We also report how many tokens each model generates, and find that the share of output spent on thinking does not track the reward.

---


### 31. [Cross-Modal Latent Influence: Patch-Level Training Sample Attribution for Vision-Language Models](https://arxiv.org/abs/2610.14190)

**<font color=#1a73e8>作者：</font>** Laura Yao, Shixing Yu, Jie Peng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Explaining a vision--language model (VLM) prediction requires tracing training-example influence to the multimodal evidence that mediates it, yet existing attribution methods largely operate only at the sample level. Recent latent-mediated influence methods provide feature-level attribution in language models, but lack the multimodal and spatial structure needed to ground influence in VLMs. We introduce MOSAIC (Multimodal Orthogonalized Sparse Autoencoders for Influence Characterization). It learns a shared sparse image--text latent space whose concepts are 1) sparse within each modality, 2) supported on contiguous image regions, 3) aligned to the phrases that describe them, and 4) approximately decorrelated. It then applies EK-FAC to decompose training-example influence through these concepts and localize their contributions to specific text phrases and image regions. We evaluate MOSAIC on Qwen and Gemma across captioning, chest X-ray understanding, and visual question answering. The learned features are more localized and coherent without degrading task behavior, and ablating influence-ranked latents changes model outputs more than ablating latents ranked by activation or frequency. We find that visual evidence can substantially reorganize training-data attribution while preserving more of the shared latent structure. MOSAIC thus connects where model behavior comes from with what multimodal evidence carries that influence.

---


### 32. [Token-Budgeted Candidate Retrieval for 3D Scene-Grounded VLMs: Category Names vs. Pairwise Geometry](https://arxiv.org/abs/2610.14207)

**<font color=#1a73e8>作者：</font>** Michał Zakrzewski, Mariia Shpir, Taras Rumezhak  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Under a fixed context budget, which objects and relations should a 3D scene-grounded VLM see first? On ScanNet indoor referring benchmarks (Dai et al., 2017), matching the query to object category names outperforms pairwise geometry scoring at every reported K. The gaps are largest at high recall. Analytic pairwise cues beat per-object cue scoring and query-agnostic kNN graphs, including on paraphrases. MiniLM and BGE-small still score higher on those splits. We evaluate token-budgeted candidate retrieval with axis-aligned boxes, a token-ratio metric, training-free baselines, two small encoders that match q to each object's category name, and QCRR (Query-Conditioned Relation Retrieval), a deterministic pairwise-geometry scorer. Across ScanRefer gt_val plus a custom 20% scan-id split of Nr3D and Sr3D (35,504 queries; not official ReferIt3D val), additive noun matching reaches R@10 0.864 on ScanRefer against QCRR's 0.626; MiniLM and BGE-small reach 0.911 to 0.913 on ScanRefer and 0.941 to 0.947 on Nr3D. A corrected 3DGraphLLM harness (native Acc@0.25 0.67 on the full graph, n=300 ScanRefer queries) shows that context selection changes downstream accuracy under a matched object budget (Random 0.44, QCRR 0.56, MiniLM 0.67, oracle 0.70). Semantic retrieval beats hand-designed geometry on that harness. We will release the protocol, retriever implementations, and per-query outputs so new selectors can be swapped in without rewriting the analysis.

---


### 33. [Should SLMs be in the Driver's Seat? A Study of Local Models as Interpreters in Cloud-Written Agent Programs](https://arxiv.org/abs/2610.14209)

**<font color=#1a73e8>作者：</font>** Boris Radovič, Marco Canini, Veljko Pejović  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The most accurate agents executing user-provided tasks are driven by large, cloud-hosted models, which solve them by reading the private data of the user. Agents powered by models small enough to run on edge devices keep that data local, but yield far worse results. A third option is to have cloud models write a program that devices execute: the data stays local, but as the program is written before any data is seen, it fails whenever a step depends on interpreting content that appears only at run time. We explore an intermediate architecture, in which the cloud-written program defers bounded questions over user data to a small local model through an ordinary function call. On AppWorld this improves the success rate of a code-only agent in all six combinations of backbone model and test partition we evaluate, by up to 14.9pp, recovering a substantial part of the gap to a cloud-hosted ReAct loop while keeping user data on the device.

---


### 34. [Modeling the Arrival Time of Information-Bearing Events in Natural Language](https://arxiv.org/abs/2610.14212)

**<font color=#1a73e8>作者：</font>** Leyi Lao, Yulin Ou, Yang Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding how information is distributed over time is fundamental to modeling natural language. While existing empirical studies primarily rely on post-hoc analysis of information-theoretic metrics, such as surprisal, little is known about the generation processes under the surface. We propose a novel approach for addressing this gap using the tool of neural temporal point processes (TPPs) by modeling the key information-bearing events in text sequences with learnable event intensity functions. Our model takes the history of event intervals and the contextual semantic representations from LLMs as input, and predicts the future arrival times for two types of events: new-word and high-surprisal-token. The experimental results reveal an interesting distinction in event intensities: LLMs tend to produce new words at significantly higher rates than humans, while high-surprisal tokens do not exhibit the difference. A decaying pattern of intensity over time is found in new-word events for both humans and LLMs, but not in high-surprisal-token events. Our findings revisit and extend previous studies that use simpler methods; provide supplementary evidence for theories about constrained context representation inherent in human language production; and find a new angle to view human and LLM generation differences.

---


### 35. [Embedding Graph Kernel Entropy (EGKE): Fine-grained Hallucination Detection for LLMs from Embeddings](https://arxiv.org/abs/2610.14214)

**<font color=#1a73e8>作者：</font>** Dilrangi Sankalpana, Pragatheeswaran Vipulanandan, Uthayasanker Thayasivam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hallucination detection is critical for ensuring the reliability of Large Language Models (LLMs) in real-world deployments. While recent works, such as Semantic Entropy (SE) and Kernel Language Entropy (KLE), identify hallucinations by measuring semantic disagreement across multiple generated responses using Natural Language Inference (NLI) models, these methods depend on separately loaded NLI classifiers to estimate pairwise semantic similarity, introducing significant computational overhead. We propose Embedding Graph Kernel Entropy (EGKE), a variant of Kernel Language Entropy (KLE) that replaces its NLI-derived semantic graph with a Radial Basis Function (RBF) kernel applied to dense sentence embeddings generated by a BGE embedding model, while retaining KLE's graph Laplacian, heat kernel, and von Neumann entropy formulation unchanged. By computing similarities directly in a continuous embedding space, the proposed method provides a symmetric and computationally efficient alternative to NLI-based semantic comparison. We evaluate our approach across 30 experimental setups (covering multiple question-answer datasets and open-weight LLM families) using both AUROC and AUARC, and demonstrate that this RBF-based method achieves competitive hallucination detection performance against state-of-the-art methods.

---


### 36. [Physical Side-Channel Attacks on Edge LLMs: Extracting Output Tokens and User Prompts](https://arxiv.org/abs/2610.14215)

**<font color=#1a73e8>作者：</font>** Najeh Alhalawani, Gunes Acar, Zhuoran Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The deployment of large language models (LLMs) on edge devices is largely motivated by privacy concerns over sharing sensitive user data with cloud servers. In this paper, we demonstrate that keeping inference local does not eliminate privacy risks: an adversary with physical access to the device may exploit hardware leakage to recover sensitive information without compromising or modifying the software system. In particular, we present an electromagnetic (EM) side-channel attack targeting LLM inference on edge devices. Targeting LLaMA-3.2-1B-Instruct running on a Raspberry Pi 5, we demonstrate that EM traces collected during inference can leak both generated tokens and user prompts. We propose three attacks under different threat assumptions. First, a profiling attack that identifies generated tokens among 50 medical and privacy-related keywords with 97.2% accuracy on profiled words. Second, a reconstruction attack recovers the model's hidden representations and uses them to predict tokens from the full 128k-token vocabulary, achieving 94.3% accuracy on profiled classes. For unseen words, the correct token is ranked within the first 100 positions of the 128k-token vocabulary in 67% of cases, with a median rank of 54. Finally, we present a hidden-state inversion attack that uses the recovered hidden state to reconstruct user prompts semantically. Our proposed attacks require only passive EM side-channel measurements and a limited number of traces during model training. These results demonstrate that local execution alone may not guarantee the confidentiality of generated tokens and user inputs.

---


### 37. [Harness^2: Recursive Agent Harnessing for an Open World](https://arxiv.org/abs/2610.14224)

**<font color=#1a73e8>作者：</font>** Ruiyao Xu, Yanfei Chen, Zhongying CuiZhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, open-world tasks are typically unseen during the harness design phase and novel at test time, leaving no ground-truth verifiers to reliably guide online harness edits. Second, the RSI process remains highly task-specific and fails to generalize to novel scenarios. We introduce Harness^2, a plug-and-play, recursive agent harnessing framework that addresses these challenges through two connected levels of recursion. Task-level recursion refines the current task's harness using a contrastive Propose-Probe-Compose step that reliably guides edits without ground-truth verifiers, and can be scaled further via parallel or sequential recursion. Harnessing-level recursion then extracts experience from these edits to update a continual improvement harness, enabling the agent to better adapt to future tasks. Across three professional benchmarks and four model-harness configurations, a single step consistently improves GLM-5 and Gemini 3.5 Flash over their base harnesses, yielding gains of up to 11.5 points on WorkBuddy-Bench, 4.5 points on JobBench, and 11.8 percentage points on LAB, with further gains as the task-level recursion budget increases.

---


### 38. [CAPTOR: a vision-language foundation model for Chest-Abdomen-Pelvis Oncologic CT](https://arxiv.org/abs/2610.14226)

**<font color=#1a73e8>作者：</font>** Séléna Jean-Mactoux, Sophie Loizillon, Ghina Jardali 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose : To develop and evaluate CAPTOR, a deep-learning vision-language foundation model for oncologic chest-abdomen-pelvis (CAP) CT interpretation.
Materials & Methods : CAPTOR (Chest-Abdomen-Pelvis foundaTion model for Oncologic Radiology) is a contrastive vision-language model, trained using a pretraining strategy for oncologic CAP CT (in single- or multiple-series acquisitions), on a multicenter retrospective dataset from North America, Europe and Asia, predominantly from tumor lesion examinations. CAPTOR was compared with state-of-the-art CT foundation models on three downstream tasks: disease detection, survival prediction using TumorImagingBench and image retrieval. Classification and retrieval were both evaluated on held-out internal and public test sets, stratified by anatomical coverage and indication. Bootstrap resampling was used to estimate confidence intervals, and pairwise comparisons were performed using permutation tests.
Results : CAPTOR was trained and tested on 25,512 and 10,794 CT-report pairs respectively. TumorImagingBench datasets comprised between 134 and 421 studies each. CAPTOR outperformed all baseline models, on the classification task, on the CAP subset (AUC 0.767, 95%CI: 0.734-0.793, vs. 0.695, 95%CI: 0.645-0.736 for the next-best, p<0.001) and oncologic subset (AUC 0.784, 95%CI: 0.759-0.805, vs. 0.734, 95%CI: 0.703-0.767 p<0.001), ranked first on three of the four oncologic prognostic benchmarks, and achieved superior retrieval performance on CAP and oncologic subsets.
Conclusion : A foundation model trained on oncology-enriched CAP CT data outperformed relevant state-of-the-art models in its target clinical context, underscoring the importance of clinically aligned pretraining.
We release our preprocessing, training and inference code : this https URL and model weights : this https URL

---


### 39. [Latent World Action Model for GUI Agents](https://arxiv.org/abs/2610.14228)

**<font color=#1a73e8>作者：</font>** Seungjun Yu, Hojun Choi, Seojeong Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel-space world models have recently emerged as a promising approach for GUI agents, predicting future screens prior to execution and subsequently re-perceiving them for action selection. However, this two-stage paradigm faces two key challenges in GUI environments: (L1) the high computational cost of pixel reconstruction and (L2) the need to reconstruct large and diverse appearance-level details beyond what is required for action selection. In practice, this screen-generation objective can induce an identity shortcut problem, where future-state prediction largely preserves the current state rather than capturing action-induced changes. In this work, we reformulate GUI world modeling by shifting the prediction target from full-screen reconstruction to action-induced future information in latent space. Concretely, we leverage a large multimodal model as the latent world model, whose shared representations support two dedicated heads for both action selection and predictive transition modeling. The action head directly translates these latent representations into action selection, while the transition head captures action-conditioned future information. To mitigate the identity shortcut, we further introduce an action-aware contrastive objective that encourages the transition representations to capture discriminative action-induced changes. Extensive experiments across offline and online GUI settings show that our method achieves up to 31.9% and 40.6% relative gains in success rate over pixel-space world models, respectively, while substantially reducing inference latency by up to 98.9%. Our code is available at this https URL.

---


### 40. [Agentic Data Engineering for LLMs: System Design and a Controlled Empirical Study](https://arxiv.org/abs/2610.14238)

**<font color=#1a73e8>作者：</font>** Ruomeng Ding, Qianli Shen, Zhaoyang Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM data engineering requires iterative experimentation to determine how data selection, rewards, and curricula affect model learning, making it a natural setting for AI-for-AI (AI4AI) research. Can agents use experimental feedback to progressively improve strategies, and do the resulting strategies improve target-model performance on held-out data? We study how agents use experimental feedback to develop data-engineering strategies under fixed training and evaluation protocols. Our Agentic Data Engineering (ADE) framework lets agents pursue, revise, or combine research directions using cumulative findings. Strategies are selected by in-loop scores and evaluated on held-out benchmarks. Across four tasks-math and code data selection, math reward design, and math curriculum learning-selected strategies achieve absolute gains over generic baselines of up to 13.34% on AIME25 Pass@32 and 5.85% averaged across four held-out benchmarks under fixed training conditions. In-loop scores improve over successive experiments, while held-out trajectories show that later in-loop gains do not always improve generalization. Comparisons of research organization and feedback access favor combining evidence analysis with cumulative findings. Research trajectories show how earlier findings inform strategy revisions and combinations across research directions.

---


### 41. [Thinking with Images without Coordinates](https://arxiv.org/abs/2610.14265)

**<font color=#1a73e8>作者：</font>** Meng Cao, Haoze Zhao, Yi Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in multi-modal large language models have shifted toward the "thinking with images" paradigm to improve reasoning faithfulness, yet existing methods rely heavily on explicit coordinate- based grounding. We identify two fundamental limitations in this approach, i.e., a semantic gap where sparse regressions miss high-dimensional latent structures, and a resolution gap due to the granularity mismatch between patch-level tokens and pixel-level coordinates. To address these, we propose TiCO (Thinking with images without COordinates). It reformulates visual reasoning as a semantic evidence discovery process within the latent space, and evidence is injected as token-level regions without pixel coordinates. Specifically, TiCO utilizes a dedicated probe token to estimate similarity distributions and performs importance sampling over spatially connected components to generate diverse, semantically dominant evidence rollouts. Extensive experiments across multiple high-resolution and general visual reasoning benchmarks demonstrate that our TiCO consistently outperforms state-of-the-art coordinate-based methods with significantly improved inference efficiency.

---


### 42. [The Thinking Leakage in Reinforcement Learning for LLMs](https://arxiv.org/abs/2610.14270)

**<font color=#1a73e8>作者：</font>** Wenxuan Zhu, Shuming Liu, Bang An 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hybrid reasoning models such as the Qwen3 series switch between a THINK mode and a NO-THINK mode through a few chat-template tokens. A popular recipe trains such models with reinforcement learning in NO-THINK mode and reports improved reasoning performance. We provide evidence that much of this gain can be explained by thinking leakage: the gain comes largely from partially reactivating the reasoning abilities of the original model's THINK mode instead of learning enhanced reasoning behavior. We train Qwen3-1.7B, 4B, and 8B with GRPO in NO-THINK mode. As accuracy improves, responses become longer and more reflective, are increasingly judged by the original model to resemble its own thinking, and the model's internal activations shift toward its THINK mode. We then investigate at the level of weights, activations, and attention heads: scaling the RL update further elicits THINK-mode behavior and approaches THINK-mode accuracy but does not exceed it; in Qwen3-8B, replacing a low-dimensional THINK-related activation subspace of the RL-trained model with its original-model value removes most of the RL gain, and the reverse exchange transfers a considerable fraction of the gain to the original model; and the RL-induced shift passes through the attention heads that read the empty think block. We further identify a possible mechanism in the GRPO training signal: responses favored by the advantage-weighted update are more THINK-like, and a gradient step computed from this signal moves the model toward its THINK state. Thus, gains in NO-THINK mode can largely reflect reactivation of reasoning abilities already present in the original model.

---


### 43. [Echo: Error-Compensated 4-Bit Tensor-Parallel Communication for LLM Training and Inference](https://arxiv.org/abs/2610.14277)

**<font color=#1a73e8>作者：</font>** Xingyu Xie, Xiaoyong Xie, Zhouchen Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tensor parallelism ends every layer with an all-reduce that sits between two dependent matrix multiplications, so its cost cannot be hidden and grows as compute outpaces interconnect bandwidth. Sending 4-bit instead of 16-bit values would cut this cost by nearly 4x, but the all-reduce must add the values it carries, and rounding the sum injects an error at every call. Model quality depends on how these errors accumulate over layers, yet existing methods treat each call on its own. We present Echo, a 4-bit all-reduce for training and inference that controls the accumulated error. Echo moves data in 4 bits and sums in high precision, so each value is quantized at most twice per call for any number of GPUs. The summation reveals each injected error, and Echo feeds it back into later calls, so old errors cancel instead of accumulating. We prove that the accumulated error stays bounded independently of depth. On A100 GPUs, Echo is 2.09x faster than the 16-bit NCCL all-reduce on 1 GB messages. It speeds up the time to first token by up to 1.16x and the training step by up to 1.09x on an idle interconnect, and by up to 1.44x and 1.38x as background traffic grows. It keeps the average accuracy over seven benchmarks within 0.4 points of 16-bit inference on Qwen3-8B. In 10B-token pretraining, its final loss is less than 0.9% above that of 16-bit training. Echo needs no FP8 or FP4 hardware.

---


### 44. [ASSET: Adaptive Speech Segmentation via Reinforcement Learning](https://arxiv.org/abs/2610.14309)

**<font color=#1a73e8>作者：</font>** Cihan Xiao, Yuan Tseng, Matthew Wiesner 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech large language models (LLMs) are often built using pretrained acoustic encoders as an audio interface to an LLM decoder. However, LLMs scale poorly with input sequence length, while acoustic encoders tend to produce substantially longer sequences than typical textual inputs. This motivates learning to compress encoder outputs while preserving task-oriented information. To this end, we introduce ASSET, a reinforcement learning (RL)-based framework that learns to adaptively compress encoder outputs by first partitioning them into variable-duration segments and then pooling each segment into a continuous audio token. We use group-relative policy optimization (GRPO) to train a segmenter with task performance feedback and a token-rate penalty. In automatic speech recognition (ASR) experiments, ASSET achieves performance comparable to a transcript-assisted character-boundary oracle with approximately 25% fewer audio tokens on English LibriSpeech, while improving on a phone-boundary oracle at a similar token rate on Mandarin AISHELL. Exploratory experiments on non-ASR tasks further illustrate how learned segmentation changes when the framework is adapted to tasks beyond transcription.

---


### 45. [Which Metadata Matters for LLM Tool Selection in MCP? Evidence from Controlled Factor-Level Interventions](https://arxiv.org/abs/2610.14334)

**<font color=#1a73e8>作者：</font>** Xiaofan Li, Fengchun Qiao, Xing Gao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In Model Context Protocol (MCP) systems, LLMs select tools from metadata rather than from their implementations. Names and descriptions summarize what a tool does, while the parameter schema specifies the fields a tool accepts and how they are organized. Our analysis of metadata for 367,174 MCP tools reveals substantial schema variation among functionally similar tools. Many of these tools share names and similar descriptions but expose different parameter schemas. This raises a key question: can parameter-schema differences influence tool selection before any call is made? We study this question through controlled metadata interventions across five LLMs and five tasks. Each comparison changes exactly one metadata factor (server name, tool name, description, or parameter schema) while keeping the others fixed. We balance tool positions and use conditional logistic regression to estimate position-adjusted effects. We find that: (1) parameter-schema changes produce the largest and most consistent selection shifts among the tested interventions. Models tend to favor separate top-level parameters over grouped or composite forms. (2) Descriptions that explain parameters also tend to increase selection, while name effects are weaker and less consistent. (3) Targeted comparisons show that schema effects depend on the specific parameter names and on how the request represents the same information. When only one schema satisfies an explicit request requirement, all five models select the compatible tool despite position preferences. These results show that parameter schemas influence not only how tools are called, but also whether they are selected. For MCP developers and evaluators, schema design and tool ordering can therefore affect which implementation is invoked even when functionality is unchanged.

---


### 46. [On the Depth Transfer of Neural Optimizers via L-Smoothness](https://arxiv.org/abs/2610.14344)

**<font color=#1a73e8>作者：</font>** Maximilian Wong, Chenyu Xu, Jiajin Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling deep learning models efficiently requires predictable performance transfer across compute regimes. Establishing reliable hyperparameter transfer allows optimal training dynamics and structural choices to be discovered on low-cost proxy models, avoiding catastrophic failures during massive-scale training. Existing depth-transfer analyses are architecture-specific and heuristic: hyperparameter transfer is only justified through toy blocks, and both rely on infinite-depth dynamics, a specific initialization, and feature-learning criteria. Building on $L$-smoothness framework of Xu et al. (2026), we understand hyperparameter transfer as how do the Lipschitz and $L$-smoothness constants of the loss scale with the depth $K$? We show that inverse-depth residual branch scaling $\alpha=\Theta(1/K)$ is sufficient to make both constants depth-independent at fixed width, uniformly over the bounded parameter domain and for arbitrary $p\to q$ geometries. Because the bounds depend on each residual branch only through its Lipschitz and smoothness constants, the argument applies to general residual networks (including branches of block depth $\geq 2$ such as transformer and ResNet blocks) without assumptions on initialization or correlations between layer weights. Since the smoothness constant controls the curvature penalty in the descent inequality, our bounds motivate a learning-rate scale without an additional depth-dependent curvature correction for updates bounded in the prescribed norm. This provides a geometric explanation of inverse-depth residual scaling and its application to the operator-norm geometries associated with AdamW, Muon, and MOGA. Learning-rate sweeps on GPT-2 (depths 2--128) and CIFAR-100 ResNets (8--32 residual blocks) confirm that Muon and MOGA exhibit stable learning-rate transfer under these prescriptions, with a common optimal rate across a 64-fold increase in depth.

---


### 47. [Evaluating LLMs as Agentic Workflow Executors in Real-World Customer Support Skills](https://arxiv.org/abs/2610.14346)

**<font color=#1a73e8>作者：</font>** Md Tahmid Rahman Laskar, Gundeep Singh, Xue-Yong Fu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprise customer-support agents increasingly rely on Large Language Models (LLMs) to execute bounded, tool-using workflows. We study this problem through the lens of Skill LLMs: specialized executors that operate within a selected skill context and must complete a narrow, stateful workflow under policy and tool constraints. We present a benchmark construction pipeline that mines recurrent workflows from real-world transcripts, converts them into structured skill descriptions, maps them to tool requirements, simulates environment state with Model Context Protocol (MCP)-compatible mocks, and generates multi-turn tool-using dialogues. Using this benchmark, we conduct a large-scale zero-shot evaluation of 17 language models spanning closed model families and deployment-oriented open-weight models from 1.7B to 14B parameters, each judged independently by five strong LLM judges, plus a deterministic rule-based evaluator that checks tool coverage, hallucinated tool use, and unsupported claims. We find a consistent ranking in which GPT-5.4 leads by a wide margin and QWEN3.5-9B is the strongest open-weight model (below 20B), outperforming several closed baselines under every judge. We also find that judge choice is not a negligible methodological detail: pairwise judge agreement on the pass/fail verdict averages Kappa=0.524 across 10 judge pairs. These results suggest that comprehensive zero-shot evaluation of skill execution requires judge reliability as carefully as model capability.

---


### 48. [Natural Code Transformation Confuses Agents in Vulnerability Analysis](https://arxiv.org/abs/2610.14350)

**<font color=#1a73e8>作者：</font>** Jie Zhu, Ronik Bhaskar, Heather Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Having demonstrated a strong potential for automating vulnerability discovery, AI agents can also be used to attack software systems at scale. Today's software systems need mechanisms to level the playing field by slowing down potential attacks, giving them time to patch vulnerabilities and strengthen software. Along this line, our study of agent trajectories in vulnerability analysis shows a surprising finding: agents produce dramatically different results across real-world code commits that carry the same functionality and the same vulnerability. This phenomenon appears consistently in multiple code domains and vulnerability categories.
It motivates us to study natural and functionality-preserving code transformations derived from real-world software development, and their potential as a defense against attacker agents. We build a corpus of natural transformations by mining recurring development patterns from real-world code commits, and apply them to evaluate impact on agentic vulnerability analysis. Our results show that even a single form of transformation can effectively "confuse" frontier agents, e.g., Codex with GPT-6 Sol, reducing successes in vulnerability discovery. We also study different agent failures, whether transformations can be composed to provide stronger protection, and adaptive attackers who seek to reverse them. Overall, our study of natural code transformation significantly expands the research space of using code transformations to defend against malicious agents.

---


### 49. [When Pleasing the User Compromises Care: AI Sycophancy in Caregiver-Mediated Healthcare](https://arxiv.org/abs/2610.14360)

**<font color=#1a73e8>作者：</font>** Priyadarsi Mishra, Arjun Beniwal, Ziyu Yi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) alignment often assumes that the user interacting with a model is also the primary beneficiary of its behavior. Yet in many consequential settings, one person directs the system while another bears the consequences. We study this problem in caregiver-mediated healthcare, where parents, pet owners, and caregivers make decisions for children, animals, and older adults. We introduce an evidence-grounded benchmark spanning veterinary, pediatric, and older-adult care, and test whether AI advisors maintain appropriate care when users express clinically inferior preferences. Holding patient facts fixed, we vary stated care preferences and communication styles and evaluate both initial recommendations and multi-turn follow-up. Across frontier and open-weight models, inferior preferences substantially increase switching from appropriate to inappropriate care beyond neutral conversational drift and increase agreement with the requested action, while communication style alone has a smaller effect. These failures accumulate across turns, including on cases models initially answer correctly, and often carry moderate or severe potential harm. In matched eldercare cases, the effect of an inferior preference is similar whether it is expressed by the patient or by a caregiver. Together with models' limited tendency to elicit patient preferences in caregiver conversations, this suggests that current models are highly sensitive to expressed user preferences but less sensitive to whose preferences are represented and who bears the consequences. Our results expose a broader limitation of user-centric alignment in settings with multiple stakeholders.

---


### 50. [ConformalGuard: False-Positive-Controlled Action Gating for LM Classifiers](https://arxiv.org/abs/2610.14365)

**<font color=#1a73e8>作者：</font>** Bishnu Bista, Dhanraj Haibatrao Jadhav, Vibha Choudhary 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language model classifiers are increasingly deployed for high-stakes decisions such as phishing screening, content moderation, and fraud triage, yet validation-set thresholds provide no finite-sample control of deployment-time false positives. We present ConformalGuard, a model-agnostic calibration layer that wraps a fixed scoring function with finite-sample control over the rate at which legitimate inputs trigger an intervention tier. Our contribution is empirical and operational, not a new conformal theorem: zero-shot LM API scores can be coarse enough (10--11 unique values here) to make temperature scaling and isotonic regression operationally identical to raw thresholding for low-FPR action gating. We compare these methods with conformal calibration for fine-tuned BERT, Claude Sonnet 4, and GPT-4o on public email corpora. For Claude, conformal calibration reduces FPR from 0.040 to 0.008 while recall falls from 0.938 to 0.875. For deterministic GPT-4o scores, the 1% operating point is too conservative to deploy (recall 0.564); three-run stochastic averaging raises recall to 0.732 at FPR 0.005. At 2% prevalence with BERT, conformal calibration removes 25 false-positive reviews per 10,000 emails (95% CI [10, 43]). The guarantee is legitimate-event-rate control under exchangeability; discrimination, workload effects, and robustness to shift remain empirical.

---


> [!TIP]
> 当前位于：**1-50**（第 1/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
