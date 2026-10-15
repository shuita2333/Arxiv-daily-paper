# 🧠 大模型相关研究 | 2026年10月16日

> 本类共 **313** 篇论文：已确认 **304** 篇，待复核 **9** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-313](./part-07.md)

---

### 1. [Lotus: Learning to Understand Time-series by Learning to Forecast](https://arxiv.org/abs/2610.18877)

**<font color=#1a73e8>作者：</font>** Van Dai Do, Huu Hiep Nguyen, Minh Hoang Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series language models typically align numerical signals with language using labels, captions, or question-answer pairs. Although such supervision encourages linguistic representations, it does not explicitly require them to preserve information about how the underlying time-series signal evolves. We introduce forecast grounding, a pretraining principle that requires language-aligned time-series representations to remain predictive of the future evolution before they are adapted to downstream tasks. We instantiate this principle in LOTUS, which divides each time-series channel into non-overlapping patches and maps them into the LLM embedding space. It then predicts the next patch from the LLM hidden states of the time-series tokens, encouraging the learned representation to retain temporal information. To capture both temporal changes and periodic patterns, we also propose a temporal-spectral patch representation that combines each raw time-series patch with its spectral representation before mapping it into the LLM embedding space. Across three language model backbones and six downstream evaluation datasets, LOTUS achieves the best average performance with minimal trainable parameters, reaching 59.91% accuracy and outperforming the strongest matched baseline by 3.36%. Our representation analyses further show that LOTUS uses the numerical input and preserves temporal structure in its learned patch representations. These results establish forecast grounding as a promising pretraining principle, enabling compact time-series language models to outperform models 25 to 50 times their size on TSRBench.

---


### 2. [Inverse Reasoning Models for Efficient Post-Training and Verification from Answer-Only Data](https://arxiv.org/abs/2610.18878)

**<font color=#1a73e8>作者：</font>** Eric O. Korman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training reasoning LLMs often requires making a tradeoff between costly supervision and compute inefficiency: supervised finetuning typically requires reasoning traces, which is data inefficient since in many applications one only has prompt-answer tuples and lacks the groundtruth chain-of-thought (CoT) sequence. On the other hand, reinforcement learning (with verifiable rewards, for example) can operate without CoT data but it is much more compute-inefficient since it requires multiple autoregressive completions per optimization step, none of which are guaranteed to give a non-zero policy gradient. In this work we explore a middleground, a self-distillation technique that uses answer-only data, treating CoT as latent variables. This relies on training a partner ``inverse reasoning LLM" that generates the original's reasoning traces conditioned on the answer. The inverse model is trained once and reused across incoming batches of answer-only data, with all generation happening offline and up front, making the approach particularly suited to continual post-training. Using Qwen3-0.6B on the Countdown and GSM8K tasks, we show that after GRPO training has saturated, a single offline distillation round from the inverse model roughly doubles pass@1 on hard prompts and, on Countdown, outperforms rejection-sampling self-distillation on every hard-tail metric at every mix ratio (with smaller gains on GSM8K); rejection sampling by construction has no signal on problems the model never solves on its own. Continued GRPO on the fresh data retains an edge at hard pass@1 but trails distillation at pass@8 and pass@32 while regenerating rollouts at every step. As an added bonus we see that the inverse model has a second application as an accurate verifier of correctness. When used for best-of-$n$ selection at test time, it raises selection accuracy on Countdown from 0.753 (majority voting) to 0.969.

---


### 3. [Following the Flow the Law Requires: Training Voice Agents to Transfer to Unseen Regulated Procedures in Debt Collection](https://arxiv.org/abs/2610.18881)

**<font color=#1a73e8>作者：</font>** Petmongkon Pornpichitsuwan, Krittin Pachtrachai, Touchapon Kraisingkorn  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Voice agents built on large language models (LLMs) now handle customer calls, but in regulated applications completing the task is not enough: the agent must follow a conversational flow set by law. In debt collection, it must confirm it is speaking to the debtor before mentioning the debt, identify itself and the creditor, state the amount, and avoid prohibited language. Every creditor turns these rules into its own procedure and revises it. We ask whether a small, self-hosted policy can be trained once and then follow regulated procedures it has never seen. One machine-readable specification per deployment, FlowSpec, generates the policy instruction, gates the tools, supplies the supervision and defines the tests; the agent speaks only approved catalogue sentences. We fine-tune a 9-billion-parameter model on 2,506 conversations from 297 randomized procedures and evaluate a Thai outbound-call agent on four unseen deployment procedures (three debt collection, one non-debt), one from a wholly withheld lineage. Documented checks, fixed by the procedure, rise from 67--71 percents to 93--100 percents, while grounded checks, fixed by the conversation, already pass at 97--100 percents before training; scenario pass rate rises from 15/43 to 40/43. An audit of the shared specification finds 11 defects, 3 of which its own metric did not expose.

---


### 4. [Token Utility for On-Policy Distillation via Local Trust-Region Optimization](https://arxiv.org/abs/2610.18883)

**<font color=#1a73e8>作者：</font>** Narayanan Sadagopan, Yilan Chen, Vijay Lingam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Token-selection methods for on-policy distillation (OPD) prioritize student-visited positions using diverse signals, including uncertainty, teacher-student disagreement, and mismatch direction. We instead derive token importance from the distillation objective itself: how much can each position's loss decrease under an equal local KL budget on the student's predictive distribution? The answer is the utility $s_t=g_t^\top F_t^\dagger g_t$, where $g_t$ is the logit gradient and $F_t$ is the categorical Fisher matrix. For reverse-KL it equals the student-weighted variance of the student-teacher log-probability ratio, and for forward-KL it equals the Pearson $\chi^2$ divergence, so the appropriate utility follows from the choice of objective. On shared training checkpoints, several independently motivated criteria, including student entropy, KL disagreement, and TIP, concentrate their importance on nearly the same positions as the derived utility at a 50\% selection fraction, while diverging at stricter fractions and for direction-specific criteria. We instantiate the utility as Fisher Utility Weighting (FUW), a continuous, mean-normalized token weighting. Across seven mathematical reasoning benchmarks and three Qwen3 student-teacher pairs, FUW improves over matched uniform OPD under both reverse-KL (1.35-4.0 macro points) and forward-KL (1.08-2.71 macro points), and is competitive with existing selective methods using a single closed-form score derived from the training objective.

---


### 5. [Why Static Skill Inconsistencies Do Not Equate to Runtime Risks: A Behavioral Analysis of LLM Agent Execution](https://arxiv.org/abs/2610.18927)

**<font color=#1a73e8>作者：</font>** Fengrui Fan, Huahao Wang, Jingyi Fang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agent frameworks heavily rely on external skill assets to standardize tool usage, encode operational workflows, and supply executable runtime resources. Despite their widespread adoption, multi-component skill packages frequently suffer from cross-artifact inconsistencies, where documentation, scripts, and configuration files specify conflicting behavioral constraints. Although static auditing techniques can uncover such contractual discrepancies, static defect volume cannot reliably reflect real-world agent performance degradation. This gap leaves practitioners without rigorous evidence to assess the practical risk of flawed agent skills.
This paper presents a systematic empirical study to demystify the runtime implications of skill inconsistencies. We conduct large-scale auditing over 575 community and benchmark skills, yielding 1,182 manually validated contract inconsistencies. We further build a controlled evaluation pipeline with 49 executable agent tasks and three representative LLMs across NoSkill, OriginalSkill, and FixedSkill experimental settings. Through fine-grained behavioral analysis of 441 paired execution trajectories, we quantify the actual performance impacts of resolved defects.

---


### 6. [The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery](https://arxiv.org/abs/2610.18933)

**<font color=#1a73e8>作者：</font>** Robert Tjarko Lange, Luca Grillotti, Yutaro Yamada 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern coding agents are fundamentally reshaping the role of human input for computational research: they write code, launch in silico experiments, analyze their results, and autonomously operate with ever-increasing time horizons. Despite these developments, fully autonomous research agents suffer from a limited ideation radius and myopic hill-climbing search dynamics. To bridge this gap, we introduce The Agentic Scientist, an end-to-end distributed pipeline for human researchers to conduct computational research alongside modern coding agents. Building on its predecessor, our system decomposes research into task drafting, idea generation, planning, sandboxed experimentation, result aggregation, baseline and ablation construction, post-hoc analysis, and report writing. Importantly, each step in the pipeline is powered by the next generation of coding agents and leverages agentic self-verification. The overall research process is driven by a meta-controller that manages parallel research agents and enforces rubric verification at each stage. This design enables the same orchestration layer to be reused across heterogeneous domains with different execution environments, agentic coding harnesses, and evaluation metrics. Our system can be used across a spectrum of autonomy: either as a co-scientist tool or to perform end-to-end scientific investigation. Within the co-scientist setting, we leveraged a development version of our system to submit a single research paper, which got accepted for publication at ALIFE 2026. We further apply The Agentic Scientist fully autonomously to open problem-solving tasks in machine learning, and demonstrate the system's capability of scientific discovery across different domains of computational research. Our ablations suggest that reliable scientific autonomy depends not only on base model capabilities, but also on the cross-agent orchestration layer.

---


### 7. [Limits of Statistical Assurance for Embodied and Agentic AI under Adaptive Adversaries](https://arxiv.org/abs/2610.18948)

**<font color=#1a73e8>作者：</font>** Inderjeet Singh  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Finite safety assessments cannot exclude an adversary that preserves unattacked behavior until certification and activates afterward. We characterize this limitation for embodied and tool-use AI. An adversary that matches the complete observation law until observable, irrevocable certification and retains intervention access afterward attains $v\mathbb{E}[(n-S_0)_+]$ expected post-certification events over $n$ trials, where $v$ is the active event probability and $S_0$ the unattacked certification time. The result covers adaptive and privately randomized evaluators. Switching at certification is exactly optimal for a fixed likelihood-ratio test under memoryless, event-increasing interventions without a binding intervention budget. A positive clean-certification requirement forces linear worst-case expected excess when intervention raises event rates over an authorized deployment horizon, even if certification is deferred to the deadline. In simulated RoCo collaboration, switching yields commanded-separation violations in 34 of 36 post-certification episodes. Preregistered randomized AgentDojo trials estimate 1.98 additional security violations per four-task continuation (95% interval [1.67, 2.29]). An adversarial language-model controller infers hidden certification from noisy evaluation receipts and times intervention accordingly. With permanent revocation, a mixture likelihood-ratio monitor bounds cumulative excess above a prespecified reference rate at square-root order, up to logarithmic factors, on every sample path. A single fixed alternative can permit linear expected excess under stationary attacks. Against a controller observing the monitor's rule and statistic, live mixture monitoring reduces violations from 12.00 to 3.81 per 24 assigned task opportunities. Revocation also reduces tasks executed.

---


### 8. [Evaluating Large Language Models for Multilingual Abstractive Summarization: A Comprehensive Study of English and Bengali](https://arxiv.org/abs/2610.19003)

**<font color=#1a73e8>作者：</font>** Khan Mahi Al Atahar, Nazifa Tasneem, Ajwad Abrar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Abstractive summarization remains challenging across languages, where linguistic quality and factual consistency may diverge, particularly in low-resource settings. We present a standardized zero-shot benchmark of eight closed-source and open-weight LLMs on size-matched English and Bengali XL-Sum test sets. Our evaluation combines lexical and semantic metrics with reference-free factuality verification and multidimensional LLM-as-a-Judge assessment, providing a comprehensive analysis of both surface-level quality and factual reliability in multilingual summarization. Results reveal substantial cross-lingual variation: GPT-5.6 Luna leads several English lexical metrics but does not maintain the same advantage in Bengali, where LLaMA 3.3 70B achieves the highest ROUGE and BLEU scores. Gemini 2.5 Flash obtains the highest observed Bengali factuality score. Furthermore, evaluation methods produce different model rankings, highlighting the limitations of relying on a single metric for multilingual summarization assessment. These findings demonstrate that strong English summarization performance does not necessarily transfer to Bengali and emphasize the need for comprehensive evaluation frameworks for low-resource languages.

---


### 9. [CyberArena: Benchmarking AI Agents in Live Symmetric Attack-and-Defense Combat](https://arxiv.org/abs/2610.19005)

**<font color=#1a73e8>作者：</font>** Bangya Liu, Jianhong Tu, Yueyang Pan 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents are demonstrating increasingly strong offensive and defensive cybersecurity capabilities in the real world. Current benchmarks mostly evaluate agents in isolation against static targets. Real cyber operations, however, are dynamic and coupled: security postures constantly change as attackers and defenders adapt to each other in real time. Static benchmarks quickly saturate and miss an agent's ability to attack and defend simultaneously under live pressure. To address this gap, we present CyberArena, a dynamic, symmetric adversarial benchmark built around multi-round attack-and-defense combat. In isolated sandboxes, two agents compete under identical rules, acting concurrently as both attackers and defenders over continuously changing services. This converts static targets into evolving, semi-open challenges, directly testing an agent's speed and precision in discovering, exploiting, and patching vulnerabilities. To sustain the benchmark's longevity, an automated agentic pipeline continuously generates, reviews, and validates new environments. Furthermore, because pairwise contests are notoriously hard to quantify, we introduce a dynamical model that maps match dynamics into unified, multidimensional scores across offensive, defensive, and domain-specific capabilities. Evaluating 12 frontier LLM agents across 40 challenges in 466 matches, CyberArena separates model capabilities where single-agent baselines hit a ceiling. The trajectories read like a fight rather than an exam: defenders patch one hole and miss the next and certify repairs on stale evidence, while capable agents think a move ahead, planting backdoors for later rounds and, in one case, writing their own packet sniffer to watch the opponent. Beyond a benchmark, CyberArena serves as an adaptable, scalable experimental platform for future research on cybersecurity agents.

---


### 10. [PMO-Dock: Benchmarking Docking, Specificity, and Generalization in Molecular Optimization](https://arxiv.org/abs/2610.19011)

**<font color=#1a73e8>作者：</font>** Gor Simonyan, Tatevik Abrahamyan, Narek Abelyan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Practical Molecular Optimization (PMO) benchmark standardized evaluation in molecular optimization, but it is built on simple property-based oracles that do not capture structure-based drug design. As the field has moved to docking-based objectives, evaluation practice has become unstandardized, and different methods report results on different docking tasks, often without a shared protocol for fair comparison or sample-efficiency constraints. To address this, we introduce Practical Molecular Optimization for Docking (PMO-Dock), a benchmark and protocol for docking-based optimization consisting of 25 tasks covering hit generation, lead optimization, and a new specificity task requiring strong on-target binding while penalizing off-target interactions. The protocol separates model development from final evaluation: validation tasks are used for hyperparameter tuning, and test tasks are held out for final evaluation and are not used during development. Evaluation on the test tasks is done under a strict oracle budget to reflect realistic drug-discovery settings. We benchmark four diverse high-performing methods spanning different optimization paradigms, Saturn (reinforcement learning), GenMol (discrete diffusion), Genetic-guided GFlowNet, and ChemLlama (LLM-based evolutionary search). Our results show no universally best method across tasks, additional analyses of hyperparameter transfer (cross-task and cross-category) and sensitivity show that transfer is often limited and varies by method, motivating method-dependent selection strategies. This benchmark provides a concrete standard for evaluating generalization to unseen tasks and sample efficiency under a limited test-time oracle budget.

---


### 11. [Can LLMs Access their World Knowledge for Event Prediction?](https://arxiv.org/abs/2610.19021)

**<font color=#1a73e8>作者：</font>** Zijun Wu, Zhitian Zhang, Hossein Hajimirsadeghi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent work has questioned whether large language models (LLMs) can be useful for temporal event prediction. Despite vast pretrained world knowledge, LLMs often underperform simpler specialized models. We ask whether this knowledge is truly inaccessible, or whether current methods fail to present event prediction in a form LLMs can use. We argue for the latter and show that LLMs become effective event forecasters when the interface is designed around two choices. The first grounds each event in a natural-language description, and the second separates event semantics from the prediction space to prevent semantic bias from label associations. To test this, we introduce DescribeEvent, a benchmark of ~150K events across seven datasets and six domains with event-level descriptions. We find that capable LLMs substantially benefit from descriptions and symbolic labels, outperforming description-free variants and non-LLM baselines, while weaker models gain little. These results suggest that accessing LLM world knowledge for event prediction is an interface problem, and that event descriptions offer a practical way to elicit the knowledge LLMs already encode.

---


### 12. [How Far Can Coding Agents Go in Visual Generation?](https://arxiv.org/abs/2610.19025)

**<font color=#1a73e8>作者：</font>** Hengguang Zhou, Yuanhao Ban, Jiaqi Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern image generation largely relies on specialized generative models that leave the process of image construction implicit in learned parameters. We explore an alternative: general-purpose coding agents that construct images through executable programs. Our study of zero-shot drawing on AgentDrawBench, a 200-prompt benchmark, reveals a distinctive capability profile. Agents excel at preserving structure and satisfying precise visual constraints, achieving competitive results in domains where compositional accuracy matters more than photorealistic appearance, while remaining limited in perceptual richness. Their visual expressiveness varies with the drawing interface, and a qualitative study on reconstruction shows how procedural skills extracted from human demonstrations support different artistic media. We then examine code as an external visual language of thought: a structured, executable representation that agents can construct and inspect. We test it in visual question answering task and find reconstructed visual code retains substantial information for question answering and, in some domains, supports higher accuracy than the original image. These abilities raise a further question: do agents draw on a shared internal representation of scene content beyond a particular drawing program? We explore an internal visual language-of-thought hypothesis, in which a shared, compositionally structured representation supports visual operations across drawing languages. Cross-harness drawings and images assembled from independent single-pixel queries exhibit related layouts and tones. Agents also maintain self-generated room arrangements across viewpoints after visible drawings are removed. These results demonstrate that the coding agent would maintain a consistent and coherent world inside its imagine even before the harness gets involved and the generation starts.

---


### 13. [Joint Subspace Sparse Attention for Efficient Long-Context Decoding](https://arxiv.org/abs/2610.19026)

**<font color=#1a73e8>作者：</font>** Jiwon Song, Yoongon Kim, Jae-Joon Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse attention reduces the KV-cache traffic that dominates long-context LLM decoding, but practical methods largely operate at coarse granularity. Token-level selection offers finer control, yet presents two challenges: low-dimensional scoring may lose query--key structure needed for accurate ranking, while gathering scattered selected tokens can offset the resulting latency benefit. We introduce Joint Subspace Sparse Attention (JSSA) to address both challenges. For selection quality, JSSA learns a shared low-dimensional query--key subspace by minimizing token-score preservation error. We upper-bound the resulting non-convex objective with a tractable marginal objective that admits a closed-form spectral solution; direct refinement of the exact objective provides no measurable improvement in the tested settings. For execution efficiency, we develop a gather-free token-level indexed-attention kernel that supports distinct per-KV-head selections under the standard grouped-query attention (GQA) KV-cache layout. Across standard GQA, hybrid sliding-window/global attention, and Multi-head Latent Attention (MLA) models, JSSA consistently remains close to full-KV accuracy while avoiding the substantial generation-length inflation and architecture-dependent failures observed with competing methods. On an NVIDIA B200 GPU, JSSA achieves up to $6.43\times$ the decoding throughput of full-KV attention at 128K context. JSSA achieves reasoning accuracy comparable to model-native DSA without model training and reaches 96--99\% of its decoding throughput even at 700B scale large models.

---


### 14. [How Many Ranks Does a Token Need? A Noise-Floor Squelch for Rank-One LoRA Experts](https://arxiv.org/abs/2610.19033)

**<font color=#1a73e8>作者：</font>** Mei Okonkwo, Owen Castellanos, Ingrid Solberg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) applies every rank-one component of its update to every token, and mixture-of-experts variants replace this with a learned router that activates a fixed number of components. We argue that the number of components a token needs is a detection question with a classical answer. A token's responses to the rank-one components of a trained LoRA consist of a few large values on a Gaussian noise floor whose width matches that of an untrained adapter, and the floor carries cross-talk rather than adaptation. We introduce SQUELCH, a router-free mixture of rank-one experts that (i) soft-thresholds each token's responses at a multiple of its own robust noise level, so the active rank varies per token; (ii) chooses that multiple for each module by Stein's unbiased risk estimate, so no rank budget is specified; and (iii) replaces the resulting marginal keep-or-drop decisions by one explaining-away step on the value Gram matrix, which suppresses redundant co-active components and recruits complementary ones. SQUELCH adds no trainable parameters to LoRA. We prove that the squelch is within a logarithmic factor of the oracle input-dependent allocation, that the selected threshold is risk-consistent, and that explaining away is a descent step toward the joint sparse code whose error is controlled by the coherence of co-active components. On commonsense reasoning, knowledge, math, code, and GLUE with LLaMA-3.1-8B, Qwen3, and DeBERTaV3, SQUELCH improves over LoRA by 2.2--3.2 points and over the strongest mixture baseline by 0.8--1.2 points while activating 8.6 of 32 components per token on average.

---


### 15. [Tracing Morphology, Semantics, and Divergence in Language Acquisition](https://arxiv.org/abs/2610.19041)

**<font color=#1a73e8>作者：</font>** Forough Shirin Abkenar, Haoshuo Fu, Liang Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding the dynamics of language acquisition in Large Language Models (LLMs) is crucial for uncovering how statistical representations evolve into structured linguistic capabilities. However, most existing studies focus primarily on fully trained models, leaving the developmental trajectory across intermediate training stages largely underexplored. In this work, we leverage intermediate checkpoints from open-source models (e.g., Pythia and OLMo) under teacher-forcing evaluation to systematically investigate language acquisition across training steps and model scales. We focus on four core characteristics: morphological structure acquisition, embedding drift, repetition dominance, and co-occurrence effects. Our findings reveal that models acquire morphological structures well before semantic embeddings stabilize. Furthermore, we show that training dataset size has a positive impact on divergence recognition, while co-occurrence during pre-training and repetition during inference have a negative impact on divergence recognition and associative link generation.

---


### 16. [Pre-Trained Language Models as Zero-Shot Tools for Social Science Research](https://arxiv.org/abs/2610.19048)

**<font color=#1a73e8>作者：</font>** Noah Dasanaike  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Record linkage and demographic inference from names are routine demands in social science. Most approaches to these problems require labeled training data that are difficult or costly to acquire. I show that pre-trained language models perform both tasks accurately without requiring task-specific training. For record linkage, I introduce EnsembleLink, an algorithm that uses pre-trained embeddings alongside string-based scorers to retrieve a short list of candidates and then identify the likeliest matches. EnsembleLink matches or exceeds the performance of most prior approaches while generalizing across scripts and formats that those methods are unable to handle. For ethnicity inference from names, I show that large language models (LLMs) achieve up to 83.8% accuracy on U.S. voter files, compared to 78.0% for name-supplemented BISG. Open-weight models offer reproducible implementations that approach these models in accuracy. Moreover, LLMs are able to infer group membership for religious, caste-based, and other ethnic group categories outside of the United States, and reduce bias in downstream estimates of geographic racial gaps. Where pre-training encodes the world knowledge required by each task, task-specific labels add less information.

---


### 17. [Smart Alone, Blind Together: Why Accuracy Fails to CertifyTheory of Mind in Multi-Agent Teams](https://arxiv.org/abs/2610.19051)

**<font color=#1a73e8>作者：</font>** Will Beaumaster, Paul Schrater  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coordinators that act on what they infer about teammates are usually certified by the accuracy of those inferences. We argue that accuracy is the wrong certificate, for two reasons. First, the accuracy needed to act depends on what a wrong action costs, so the bar belongs to the deployment, not the module. Second, a module's errors are rarely independent, and dependence has a sign: positively associated errors help where their damage overlaps and hurt where it compounds, so an accuracy threshold fails in a predictable direction, and once wrong beliefs interact and can do harm, no rule based on accuracy is right for every module. We test these predictions in task assignment, Level-Based Foraging and Hanabi, with injected errors, trained and Bayesian modules and five language models, and in human judgments. Accuracy fails in both directions, approving harmful language-model deployments in Hanabi, where shared errors compound, and rejecting beneficial ones in task assignment, where costly errors are rare. In our tasks it also buys far less redundancy than independence predicts: from GPT-5.4-mini to Claude Opus 5.5, error on teammates the models have evidence about falls from 32% to 11%, but the chance that all three observers misread one falls only from 16% to 9% (independence: 3.4% to 0.15%). We propose certifying the deployment, with a Blind-Spot Gate that prices error costs, pairwise interactions and measured dependence without deploying the module. On held-out data from the cells it was developed on, it makes no significant false approval in 20 splits (accuracy: 3.2 per split), and in preregistered tests on modules it was not developed on, it recovers what accuracy rejects (seven classifiers: regret 0.004 against 0.479) and catches what accuracy approves (a Bayesian module: significant false approvals in 17 of 20 splits for accuracy, 1 for the gate).

---


### 18. [Why Do VLMs Fail at Remote Physiological Measurement? Rethinking with Physiological Grounding and Numerical Alignment](https://arxiv.org/abs/2610.19052)

**<font color=#1a73e8>作者：</font>** Xiao Yang, Zekun Zhang, Yuxuan Fan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-based remote physiological measurement (RPM) has broad applications, while Vision-Language Models (VLMs) provide a promising opportunity to enable end-to-end physiological monitoring for future human-aware intelligent systems. However, existing RPM methods rely on task-specific models and cannot be seamlessly integrated with the multimodal understanding and interaction capabilities of VLMs. We revisit RPM with VLMs and provide empirical evidence for two major bottlenecks: generic visual semantic representations fail to preserve fine-grained physiological cues; while discrete token prediction in autoregressive generation is inherently misaligned with continuous numerical measurement. To address these challenges, we propose VITAL (Visual-physiological Token Alignment for Language Models), a visual-physiological token alignment framework for RPM and preserving general vision tasks. VITAL retains the original visual pathway for semantic understanding and introduces an independent physiological pathway to jointly model semantic and physiological information. Moreover, we propose a structured numerical alignment approach to improve the reliability of generative heart rate estimation by enhancing numerical relationship modeling. Extensive experiments show that VITAL improves cross-domain estimation performance on multiple rPPG datasets while preserving the general visual understanding capability of VLMs, demonstrating its effectiveness as a unified visual-physiological model. Code will be released.

---


### 19. [RLPE: Teaching LLMs to Prompt with Reinforcement Learning](https://arxiv.org/abs/2610.19062)

**<font color=#1a73e8>作者：</font>** Rahul Singhal, Karime Maamari, Pradyumna Tambwekar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prompting is a widely used method for adapting general-purpose LLMs to domain-specific tasks. Effective prompts can be tedious to create manually, so prompt writing is increasingly handed to LLMs, with recent work training LLMs to write prompts for other models. These techniques either write prompts without observing how the task model behaves, blind to the failure modes the prompt should address, or must run alongside the task LLM at inference time, adding overhead to every query. Neither reflects how prompt engineering is often practiced. To close this gap, we introduce Reinforcement Learned Prompt Engineering (RLPE), which trains a model to analyze traces of a separate task model and write a prompt targeting the failures it observes. RLPE rewards the trained model strictly on prompt performance, so it learns the prompting strategies that improve the task model. The prompt is generated once and reused across the task, so inference does not require the trained model. Since RLPE needs only query access to the model it prompts, it is also compatible with closed-source models. We apply RLPE to Enigmata, BIG-Bench Extra Hard, and PlanBench. We train a 9B-parameter model that writes better prompts than state-of-the-art frontier models (gpt-5.6-sol and claude-opus-5) and prompt optimizers (GEPA and TextGrad) on 2/3 benchmarks. Although the model is never explicitly trained to iterate on prompts, this capability emerges at a level that matches or beats frontier models. The learned prompting capability also generalizes, with the trained model improving task models 6x larger than the one it trained with, including ones from entirely different model families, and matching claude-opus-5 on a fourth benchmark held out from training.

---


### 20. [How Inner Optimizers Shape Replica Scaling](https://arxiv.org/abs/2610.19064)

**<font color=#1a73e8>作者：</font>** Eugene Belilovsky, Stefan Horoi, Edouard Oyallon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training large language models (LLMs) across geographically distributed and poorly interconnected compute pools or data centers has become a topic of significant interest. This has led to increased study of local optimization methods such as DiLoco for LLMs, especially those that use local (or inner) adaptive or preconditioned optimizers, which are critical for high-performance LLM training. However, a central challenge remains: it is well known that increasing the number of model replicas (replica scaling) while fixing the total training budget leads to monotonically decreasing performance. Existing work has empirically demonstrated that the choice of inner optimizer (Muon v.s. AdamW) can significantly improve this trend, but offers only limited explanation of the performance difference. In this work, we consider a range of inner-optimizers and identify two important factors that impact replica scaling: (1) the covariance structure of the pseudo-gradients and (2) the impact of batch size on the pseudogradient's noise scale. Based on these insights, we theoretically and empirically demonstrate that whitening-based pre-conditioning is a powerful inner-optimizer desideratum. Our empirical evaluation extends the results to reveal that whitening-based inner-optimizers achieve strong replica scaling (for 8-96 replicas), with performance relative to DP improving as parameters and data are scaled.

---


### 21. [Plan or Retrieve First? A Scale Study of Tool Discovery Architectures](https://arxiv.org/abs/2610.19068)

**<font color=#1a73e8>作者：</font>** Mingfei Zhang, Amit Surana, Ziauddin Majid 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-augmented LLM agents discover relevant APIs from large registries before planning execution, yet finite context windows prohibit injecting all tool definitions into a single prompt. The dominant approach, which we term Retrieve-then-Plan (RtP), embeds the user query and retrieves similar tools via approximate nearest-neighbor search. We study an alternative Plan-then-Retrieve (PtR) paradigm in which the LLM first generates Abstract Tool Stubs (hypothesized function signatures describing needed capabilities) which then serve as retrieval queries against the registry. Evaluating on ToolBench (46,984 unique API endpoints, 50 categories) across single-tool (G1), intra-category multi-tool (G2), and cross-category multi-tool (G3) query subsets, we find a clear complexity-dependent crossover: RtP outperforms PtR on single-tool queries while PtR outperforms RtP on multi-tool queries. This crossover holds at every retrieval budget (k=1 to 20), is robust across registry sizes from 1k to 47k APIs, and is consistent across model families (Gemini 2.5 Flash and gpt-oss-120b). We characterize a stub-hallucination failure mode (the LLM invents plausible but non-existent API names) that acts as a double-edged sword: on simple queries PtR's stubs abstract away proper-noun signals that RtP matches directly, yet on complex queries the same mechanism decomposes multi-faceted intent into functional sub-needs. We further analyze token overhead and show that PtR's extra discovery call roughly doubles inference cost, which pays off on multi-tool queries but hurts on single-tool ones, motivating complexity-adaptive routing as a practical direction, one that can be driven by a zero-cost signal already present in the pipeline (RtP's top-1 retrieval score).

---


### 22. [Backpropagating Verifier Rewards Through Continuous Flow Language Models](https://arxiv.org/abs/2610.19080)

**<font color=#1a73e8>作者：</font>** Xu Han, Jiajing Hu, Li-Ping Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has substantially improved the reasoning of autoregressive and discrete-diffusion language models. Language models that generate continuous token embeddings are emerging as a strong alternative, but RL post-training for them remains understudied. We propose \method{}, a post-training framework for continuous flow language models. Such a model denoises token embeddings over multiple steps and decodes them into discrete tokens only at the last step. To obtain pathwise gradients, which backpropagate through continuous actions and have much lower variance than REINFORCE, we introduce a critic that estimates the value of intermediate token embeddings, bypassing the non-differentiable decoding step. The critic must also keep track of the value function as the policy changes; to this end, we design a critic that predicts a value from every token representation and improves policy optimization. Across four reasoning tasks, \method{} reliably improves a continuous flow language model through RL post-training and outperforms baseline methods of the same type.

---


### 23. [Beyond Aggregate Accuracy: Item-Level Transitions in Prompt Optimization](https://arxiv.org/abs/2610.19084)

**<font color=#1a73e8>作者：</font>** Chinmoy Mitra, Tarek Mahmud  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatic prompt optimization (APO) uses feedback from model responses to improve prompts automatically. However, its effectiveness is usually measured through overall scores, which do not reveal which questions become correct, which previously correct answers become wrong, or whether improvements extend to unseen questions. We introduce Reflective Feedback-Driven Prompt Optimization (RFDPO), a tool that tracks recoveries (incorrect to correct), regressions (correct to incorrect), and churn (all changed outcomes). RFDPO uses this feedback to guide subsequent revisions and records prompt changes throughout optimization. We evaluate RFDPO across five benchmarks covering law, knowledge, instruction following, mathematics, and privacy, using GPT-5 as the optimizer and GPT-4o-mini and GPT-4.1 Mini as solvers. Our results show that overall accuracy can hide substantial changes: in five of nine configurations, churn was at least five times the absolute net change, and a single-item net change concealed up to 17 changed outcomes. Average validation gains were 7.9 percentage points, compared with 5.2 points on held-out tests. In a controlled ablation on LegalBench-Hearsay, item-level feedback reduced churn by 40% ($p=0.024$) while maintaining similar net gains. These findings motivate reporting recovery, regression, churn, and performance on unseen data alongside overall accuracy.

---


### 24. [Similar Models, Broken Odds: Where Luce's Axiom Fails in Chatbot Arena](https://arxiv.org/abs/2610.19095)

**<font color=#1a73e8>作者：</font>** Soovadeep Bakshi, Apurba Bose, Aishwarya Bose 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chatbot Arena ranks language models with the Bradley-Terry model, which gives each model one score and so assumes Luce's choice axiom. Choice theory predicts where this fails: near-copies are told apart more decisively than their scores imply. On 1.8 million Arena votes, votes between versions of one model are 1.37 times as decisive as Bradley-Terry predicts, between sizes of one generation 1.26 times and between models of one lab 1.12 times; a release a year later gives consistent multipliers, and the effect survives alternative tie treatments, prompt subsets and topics, and timing checks. How alike two models' answers are worded and formatted tracks the effect. A correction with four to six parameters predicts held-out votes better than Bradley-Terry and than models with hundreds of parameters, mostly by modelling ties; frozen and carried to new releases in a test fixed in advance, its gains are concentrated in ties, and better head-to-head odds are not established. The leaderboard order barely moves. With language-model judges and three-answer menus, a near-copy takes votes mostly from its twin when choices are pooled over prompts (log-odds shift +0.10, 95% interval 0.05 to 0.16); within a prompt the shift is smaller and clear for two of four judges.

---


### 25. [GroundGUI: GUI Grounding by High-Quality Data and Distillation-to-Reinforcement Learning](https://arxiv.org/abs/2610.19100)

**<font color=#1a73e8>作者：</font>** Qingsong Xie, Jiahao Tian, Jiacheng Tang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Constructing robust GUI agents relies on multimodal visual grounding: the ability to precisely map natural language intents to actionable on-screen components. Despite abundant desktop, web, and mobile benchmarks, high-fidelity resources tailored for diverse environments are surprisingly scarce. To bridge this gap, we introduce the Screen Referring Grounding Dataset (ScreenRef), a comprehensive GUI grounding dataset consisting of GUI screenshots paired with natural language referring expressions and box or point annotations. Spanning desktop, web, and mobile domains, ScreenRef comprises 586K screenshots and over 633K referring expression instances, covering tasks such as text recognition, visual matching, spatial understanding, and refusal scenarios. To boost the model's grounding performance, we propose the Distillation-to-Reinforcement Learning (D2RL) method to address the limited generalization of supervised fine-tuning and the sparse reward problem in reinforcement learning. Utilizing ScreenRef, we train Qwen3-VL-8B-Instruct via sequential SFT and D2RL training, yielding GroundGUI-8B. GroundGUI-8B achieves 95.2% on ScreenSpot-V2, 63.9% on ScreenSpot-Pro, 65.4% on OSWorld-G, 86.8% on MMBench-GUI L2, and 38.3% on UI-Vision. Among 8B-scale models, it produces substantial gains over models trained on open-source datasets, with performance comparable or even superior to models trained on closed-source data. Code, models, and datasets are available at this https URL.

---


### 26. [The Gap Is in the Geometry: A Convergent Meta-Analysis of Multi-Facet Aerial and Remote Sensing Video Understanding](https://arxiv.org/abs/2610.19102)

**<font color=#1a73e8>作者：</font>** Georgios Angelidis, Aggelos Psiris, Maria Vakalopoulou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial and remote sensing video is increasingly evaluated like web video, by posing multiple-choice questions to multimodal large language models (MLLMs) over sampled frames and reporting accuracy. This paper argues that this recipe measures the wrong aspect, and supports the claim with a convergent meta-analysis of a broad set of published results, organized in four evidence tiers, in which a claim becomes a position only when collected evidence agrees. Parameter scale exhibits a median of +3.4 accuracy points per tenfold increase on aerial benchmarks, far below a human gap of at least 19 points, whereas acquisition conditions control perception, as 315 of 318 evaluations in 19 within-paper contrasts lose accuracy when conditions such as altitude, view, object size or time horizon become harder. No aerial benchmark in the corpus combines video input with per-task human and random baselines, competence collapses from answering to acting in closed-loop navigation, and the same MLLMs score higher on the aerial benchmark than on ground spatial ones, but lower on studies that test cross-view geometry. From these findings the current study derives five falsifiable principles and proposes the AVU-Card, a reporting card for aerial video benchmarks

---


### 27. [Contextual Credit Policy Optimization](https://arxiv.org/abs/2610.19103)

**<font color=#1a73e8>作者：</font>** Huiwen Han, Ziyao Zeng, Zihao Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-based reinforcement learning enables large language model agents to learn from sparse outcome rewards in long-horizon tasks. Recent methods derive step-level credit by comparing observation-matched experiences across trajectories. However, identical observations can occur in different contexts, and matched peers are not equally informative for a given decision. Moreover, favorable terminal outcomes can obscure redundant actions or detours within successful trajectories. To address these two challenges, we propose Contextual Credit Policy Optimization (CCPO). For the first, CCPO weights observation-matched peers from other trajectories by contextual similarity, computed from frozen LLM representations and accumulated trajectory statistics, allowing peers from similar contexts to contribute more to a step's baseline. For the second, CCPO pairs historical credit, which compares the realized return against the weighted peer baseline, with future credit, which measures the change in contextual outcome value over a short realized continuation. A step is thus credited for the progress it makes, not only for its trajectory's eventual outcome. Both credits are computed in hindsight from rollouts already collected for training, enabling CCPO to address these challenges without an auxiliary value critic. Across two Qwen2.5-Instruct backbones (1.5B and 7B), CCPO achieves up to 97.4% success on ALFWorld and 79.4% on WebShop and outperforms GRPO by up to 21.6 and 18.5 points. Ablations show that contextual weighting outperforms uniform weighting, and that historical and future credit serve as complementary learning signals.

---


### 28. [Towards a Data-Centric Understanding of Spatial Reasoning in Multimodal Large Language Models](https://arxiv.org/abs/2610.19108)

**<font color=#1a73e8>作者：</font>** Mahdieh Mallahnezhad, Masoud Jafaripour, Mohamadali Tofigh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have been widely applied in embodied agents and robotics for vision tasks. However, MLLMs suffer from limitations in spatial reasoning and perception. Post-training techniques have shown promise for improving these capabilities; yet, there are limited data-driven surveys of such approaches. In this survey, we consider approaches to fine-tuning pretrained MLLMs for spatial reasoning tasks, ranging from supervised to reinforcement learning, with an emphasis on the datasets used. We investigate themes of dataset construction, data modality and annotation, and evaluation of the resulting models. Based on these themes, we categorize research into three groups: dataset design, dataset construction and evaluation. We find four main methods for constructing fixed spatial annotations: rules and templates, LLM prompting, procedural generation, and human-in-the-loop. We also observe substantial variation in evaluation approaches, including different scoring methods, tolerance metrics, and benchmark types. Finally, we identify opportunities for future research in unified dynamic annotation, efficient spatial reasoning, standardization of evaluation, expanded spatial range, and human-centered spatial interactions.

---


### 29. [From Copying to Composition: How Language Models Develop In-Context Learning](https://arxiv.org/abs/2610.19113)

**<font color=#1a73e8>作者：</font>** Minglai Yang, Xinyu Guo, Renxiong Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) allows language models to adapt their behavior from instructions and demonstrations in a prompt, but accuracy alone does not reveal how contextual information controls their predictions. We study the acquisition and trainability of ICL with a controlled diagnostic that separates copying a nearby demonstration from integrating information across the prompt. Across 17 models, about a third prefer the copied answer, a few are undecided, and the rest prefer the rule-consistent answer, which goes with higher accuracy and with control by the requested value rather than the closest conflicting example. Checkpoint analyses show that models begin prioritizing task-relevant prompt tokens over conflicting examples long before their accuracy improves beyond chance level. In matched training experiments, synthetic documents that define endings and then query them shift models toward compositional responses on the controlled diagnostic, whereas fine-tuning on definition exercises built from rewritten real documents improves accuracy when prompts reassign label meanings. The results suggest that ICL is not acquired as a single, uniform capability. Instead, prompt control, answer preference, construction without candidates, and transfer can develop along distinct trajectories.

---


### 30. [Genesis Steering: Better Activation Steering Through Training Data](https://arxiv.org/abs/2610.19114)

**<font color=#1a73e8>作者：</font>** Tora Bodin, Eric Aubinais, Ilaria Torre 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering controls large language models at inference time, but its effectiveness depends on the choice of reference data. We introduce genesis steering, which derives a genesis vector from contrastive examples in the model's own fine-tuning data. When these data are unavailable, we draw on the membership inference literature to identify likely training examples and construct a proxy dataset. We establish two theoretical results on optimal displacement to the decision boundary and reduced proxy-estimation bias. We evaluate genesis steering and membership-based proxy construction on Tülu-3-8B, whose fine-tuning data are publicly available, and Llama-3.1-8B-Instruct as a control. We find that safety data from Tülu-3-8B's training mixture yield stronger steering than external datasets on both models. On Tülu-3-8B, membership scores largely agree in identifying training examples, and vectors built from top-ranked examples achieve competitive performance against random subsets of the same size. In contrast, the results on Llama-3.1-8B-Instruct hint that a MIA method will only have a positive effect if the mean direction shift with MIA-filtered in-distribution data is much less severe than the direction shift with OoD data.

---


### 31. [Unlocking Structured Pruning for Reasoning Language Models via Attention-Preserving MLP Trimming](https://arxiv.org/abs/2610.19121)

**<font color=#1a73e8>作者：</font>** Woosang Lim, Haneul Yoo, Vincent-Daniel Yun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structured pruning reduces LLM inference costs by removing model components to produce smaller dense models. However, existing methods can cause reasoning performance to collapse on long-form reasoning tasks such as AIME. We propose \textit{LayerTrim}, a training-free structured pruning method that identifies redundant decoder layers and selectively trims their MLP features while preserving attention and decoder depth. LayerTrim is the first training-free structured pruning method designed to preserve long-form reasoning without gradients or recovery training. Across three reasoning language models and five benchmarks, LayerTrim outperforms existing structured pruning methods in most evaluated settings, improving average accuracy by up to 21.4 percentage points over RESP. On \texttt{Qwen3-14B}, LayerTrim achieves 1.24$\times$ faster prefill and 19.7\% lower peak GPU memory than the dense model, while better preserving reasoning ability. It also achieves the shortest average generation length among evaluated pruned models, while retaining the highest average accuracy. These results demonstrate that LayerTrim improves reasoning efficiency through both structural compression and reduced token generation.

---


### 32. [CLASHarness: Benchmarking Multi-Agent Conflict in Computer Use via a Controllable and Verifiable Generation Pipeline](https://arxiv.org/abs/2610.19128)

**<font color=#1a73e8>作者：</font>** Yuxiang Lai, Jike Zhong, Chengzhi Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly deployed in multi-agent systems to automate complex computer-use workflows, yet existing benchmarks mostly assume consistent, cooperative environments. In contrast, real-world collaboration rarely runs on consistent information: peer or sub-agents frequently report outdated states, issue contradictory instructions, or compete over shared permissions and files, forcing agents to check others' outputs and verify ground truth in the environment. Evaluating such conflict resolution remains challenging: manual authoring cannot scale across complex systems, while unconstrained LLM generation produces narrative drift, answer leakage, and unsatisfiable rubrics. We introduce CLASHarness (Conflict-Loaded Agent Scenario Harness), a controllable framework for generating verifiable multi-agent conflicts in computer use, with a benchmark of 600 multi-round tasks. By combining hierarchical scenario planning with an eight-step verified micro-pipeline, CLASHarness pre-commits decisive visual facts before rendering and compiles hybrid code and semantic graders directly from executed reference trajectories, guaranteeing every task is solvable by construction. Evaluating 15 frontier models on CLASHarness reveals three core bottlenecks. First, when sub-agent outputs conflict with the environment, weaker models blindly follow misleading information, whereas stronger models inspect visual evidence to verify ground truth. Second, resolving conflicts is much harder than finding them: while agents can spot inconsistencies, actively fixing system state drops task success significantly. Third, coordination protocols remain a universal bottleneck: even frontier models fail over 58% of closing actions, often forgetting to release shared locks or hand off tasks. CLASHarness provides a scalable, verifiable foundation for building reliable multi-agent systems.

---


### 33. [Plant Memory: Technical Language Processing and a Verified Maintenance Ontology for Agent-Accessible Failure Knowledge from SAP PM Work Orders](https://arxiv.org/abs/2610.19131)

**<font color=#1a73e8>作者：</font>** Akash Raj  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Maintenance work orders are the largest written record of how industrial equipment fails, yet in most plants they are close to unusable for analysis. Short texts are abbreviated and misspelt, asset identity is buried in free text, work-type labels contradict the work described, and the fields that matter most for reliability (symptom, root cause, action taken) are usually empty. As a result, diagnostic knowledge stays with senior technicians and leaves when they do. We present Plant Memory, a system that applies technical language processing (TLP) to SAP Plant Maintenance (PM) exports and builds an ISO 14224-aligned maintenance ontology in which every extracted statement is a reified fact carrying a confidence score, the evidence it was read from, and a verification state. Extraction is rule-first, with an optional large language model (LLM) acting as a second reader whose disagreements raise a fact's review priority rather than overwrite it. Technicians verify facts through a review queue, answer targeted knowledge-gap questions where failures repeat without a recorded cause, and approve or reject ontology drift proposals when new terms appear. The resulting graph is served to people through a web application and to AI agents through a Model Context Protocol (MCP) server, so both query the same verified knowledge and every answer cites the work orders behind it. On a synthetic 12-month export of 400 work orders from a parboiled-rice plant, rule-based extraction reaches 96.2% component accuracy, 88.9% failure-mode accuracy and 100% root-cause precision at 62% coverage; on 28 diagnostic questions, ranked root causes from the ontology are correct at top-1 in 82.1% of cases against 53.6% for the raw SAP root-cause column.

---


### 34. [Graph-Based Orchestration of Heterogeneous AI Models: A Control Node Approach to Composite Intelligence](https://arxiv.org/abs/2610.19136)

**<font color=#1a73e8>作者：</font>** G. Michael Youngblood, Filip Dvořák, Slavo Švancár 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a graph-based framework for Composite AI systems that integrate multiple AI techniques to address complex problems. We describe an architecture using specialized control nodes to orchestrate diverse models including planning, machine learning, constraint programming, and large language models. The system employs directed acyclic graphs and behavior trees to manage model relationships and execution sequencing. Our methodology encompasses data connectors, computational services, and a containerized deployment framework supporting hierarchical, sequential, and concurrent model composition patterns. Through case studies, we demonstrate how this architecture enables the creation of composite systems that leverage the strengths of multiple AI techniques within a unified operational schema, overcoming the limitations of single-model approaches.

---


### 35. [MA-Bench: Measuring Operational Planning in Language Models](https://arxiv.org/abs/2610.19138)

**<font color=#1a73e8>作者：</font>** Rodney Lafuente-Mercado, Robert Sincero, Phil Sage 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How well can a language model turn a large, incomplete and partly contradictory body of documents into a plan when no single correct answer exists? We introduce Mission Analysis (MA)-Bench, built on mission analysis, the first step of military operational planning, in which a staff reads the full situation and states the problem before anyone proposes a solution. Its 10 expert-built scenarios pair synthetic packets of ten to twelve documents with 1,257 expert-written pass/fail requirements, each containing information on their source, question type, and importance level. A reasoning-model judge grades each brief against the requirements without seeing the documents; it grades like a fifth credentialed planner, leaving a four-planner panel's agreement unchanged (Fleiss $\kappa$ 0.42 to 0.41), and a judge from a second provider reproduces the model ranking (Spearman 0.94). Across twenty frontier and open-weights models the best gets 62% of the rubric items right. Models are strongest on facts stated in the documents (58%) and weakest on judgments that must be inferred (33%), and six failures in ten are omissions rather than errors. MA-Bench grades the determinations, not the prose. We release the packets, rubrics, prompts, scorer and every graded brief with item-level verdicts.

---


### 36. [Demystifying On-Policy Distillation: Where Does the Teacher's Advantage Live?](https://arxiv.org/abs/2610.19145)

**<font color=#1a73e8>作者：</font>** Yiping Li, Fan Zhao, Zhibo Hou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) is increasingly studied as a cheaper alternative to reinforcement learning, yet it remains a form of knowledge distillation (KD) that relies on teacher supervision. We revisit OPD from the KD perspective by asking where the teacher's advantage lies along student-generated trajectories. Controlled token flips at teacher-student disagreements directly measure the accuracy gained from teacher corrections. Single-token flips yield a modest average gain on selected failed trajectories, whereas repeated flips raise accuracy from 28.4% to 74.5%, close to the teacher's 76.9%. Gains continue to accumulate with more flips, but mass- and KL-based selection outperform random flips by 15-18 percentage points at counts of similar magnitude. Selective intervention remains useful after OPD, but greater argmax agreement does not consistently improve accuracy across model pairs. We advocate training schedules that learn more valuable teacher corrections while maintaining distributional stability. Controlled flips and fork-resolution analysis evaluate OPD beyond accuracy by measuring which teacher preferences the student acquires and what further correction can recover.

---


### 37. [Compiling Expert Procedures into Verified Programs: When a Small Model Is Enough](https://arxiv.org/abs/2610.19148)

**<font color=#1a73e8>作者：</font>** Vishvesh Bhat, Asad Aali, Muhammad Ahmed Mohsin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In procedural tool-use domains, how much of the gap between base models is procedure rather than capability? We build an explicit program from a teacher's traces and run it in front of unchanged small models, including an 8B model. The construction, PLVR , takes the reasoning traces of a teacher, Kimi-K3, clusters their segments to locate recurring operations, has a frontier model author one typed primitive per operation, each run by a small frozen model and assembles the program by A* search over a mined rule library, under a reference-action objective. At inference the program takes one of two forms: for troubleshooting and tool search it produces the chain of thought the student would otherwise generate for itself, and the student acts on it; for multi-turn tool matching the student proposes each action and the program checks, repairs, or retries it before it goes out. On the official tau2-Bench Retail and Telecom test sets and on LiveMCPBench, with three Nemotron base models and the same program for each, the answer depends on the domain. On Telecom, Granite-4.2-8B as the student goes from 43.0% to 91.2% under the program, and every Nemotron student reaches 93.3-94.4%, against at most 58.2% for fine-tuning on the same traces, prompt optimisation of the student, or two token-matched baselines. With Granite-4.2-8B as the student, the program is within 2 to 3 points of the Nemotron students on Telecom and within 3 on Retail, and 3 to 13 points below them on LiveMCPBench: where the domain is procedural an 8B student is enough, and on tool search the student still matters. On Retail and LiveMCPBench the program is competitive with the best baseline. The spread between base models shrinks from about 7 points to about 2, averaged over the suites, with no weights changed.

---


### 38. [AgentCIScope: Grounded Contextual Integrity Evaluation for LLM Agents](https://arxiv.org/abs/2610.19158)

**<font color=#1a73e8>作者：</font>** Chengquan Guo, Zhaorun Chen, Zinan Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are becoming increasingly capable of handling daily workspace tasks by interacting with application environments through tool calls. However, as agents read and write sensitive user data across email, documents, and other applications, a central privacy question is whether they preserve contextual integrity (CI), that is, whether the information flows they produce comply with context-specific disclosure constraints. Existing work either focuses on model-level privacy leakage or evaluates agents in limited application environments with manually constructed disclosure constraints. In this work, we introduce AgentCIScope, a unified platform and benchmark for evaluating agent-level contextual integrity through executable, multi-step tasks across diverse, realistic application environments. AgentCIScope transforms public and synthetic privacy cases into executable agent tasks, with disclosure constraints grounded in three criteria: governing privacy policies, persona-based agreement, and a predefined sensitive-attribute taxonomy. Based on AgentCIScope, we evaluate 12 agents on 936 tasks and find that strong task-completion capability does not guarantee contextual-integrity preservation: single-run leakage rates range from 32.5% to 94.4%, while repeating each task five times further increases leakage by 4-19 percentage points. Leakage varies substantially across attributes: personal preferences and booking details have average leakage rates of 84.7% and 76.5%, compared with 17.1% for credit-card information and 29.4% for SSNs; environments: calendar has the highest average leakage rate as an information source, while WhatsApp ranks highest as an information destination; and governing privacy policies. AgentCIScope provides deep insights into agent privacy leakage and serves as a unified testbed for developing privacy-preserving agents.

---


### 39. [ListQA: A Benchmark for Evaluating List-Formatted Factual Knowledge Retrieval in Large Language Models](https://arxiv.org/abs/2610.19165)

**<font color=#1a73e8>作者：</font>** Mayank Kulkarni, Rakesh Vaideeswaran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many real-world questions demand not a single fact but an organized collection of them, yet existing factual knowledge benchmarks almost exclusively target single answer retrieval. We introduce ListQA, a benchmark of 9,045 human-curated, cross-validated questions (audited error rate of 1.7%) that require LLMs to recall multiple facts and compose them into structured lists of 3-10 elements. Questions range from flat lists ("Which NCAA teams went undefeated between 2000 and 2024?") to hierarchical lists with sub-attributes ("...and what was their record and result?"), spanning eight categories across 60+ countries. An evergreen design (explicit temporal constraints or historically immutable facts) keeps ground truth valid without periodic updates. For evaluation, we frame element matching as a linear sum assignment problem: optimal bipartite matching paired with LLM-based semantic grading jointly captures factual accuracy, hallucination, and format compliance. We benchmark 34 models (8 families, 42 configurations across standard and thinking enabled inference) and find: the best standard-inference model scores below 37% LLM-Judge-F1, multi-faceted questions are harder across the board, and providing the source Wikipedia page lifts scores dramatically, confirming that models can organize facts but struggle to retrieve them from parameters alone. Extended analyses cover base vs. instruction-tuned checkpoints and token efficiency. We release the dataset and evaluation code.

---


### 40. [Fantastic Metrics and How to Find Them: Meta-Evaluating Metrics for Multi-lingual Style-Personalized Generation](https://arxiv.org/abs/2610.19166)

**<font color=#1a73e8>作者：</font>** Anubhav Jangra, Adrian de Wynter  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Meta-evaluation of text generation metrics and LLM-judges is primarily conducted using metric-human correlations. However, prior work has shown that correlation is not an appropriate estimate of a metric's evaluation capability and can be unstable across evaluation settings, such as different datasets or languages. Therefore, we propose a regression-based meta-evaluation of metrics that learns on calibrated metric outputs to predict human ratings. We ground this measurement relative to a trivial constant-mean baseline and human agreements to provide a comparable measure of metric capability across evaluation settings. To test our meta-evaluation framework, we developed a large-scale multi-lingual style-personalized text generation (SPTG) benchmark, collecting multiple annotations across 10 topologically diverse languages and four evaluation dimensions, each with varying degrees of subjectivity. We meta-evaluated 32 metrics from three style evaluation paradigms (string-based, embedding-based, and LLM-judges) and their ensembles over these 40 evaluation settings. Our analysis revealed that even simple string- and embedding-based measurements can match strong LLM-judges when calibrated to human ratings. We also identified characteristics of human annotations that determine metric performance, as well as conditions under which a metric ensemble outperforms its individual constituents.

---


### 41. [Verification Turns Capability Gaps into Routing Decisions: Small Language Models for Clinical Documentation](https://arxiv.org/abs/2610.19169)

**<font color=#1a73e8>作者：</font>** Nina Fatehi, Meysam Ghaffari, Animesh Agarwal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical note generation from doctor--patient dialogue is high-volume and hallucination-intolerant: a fabricated laboratory value can create patient-safety risk, not a quality regression. We ask whether an agentic \emph{verification} architecture, rather than generator scale, can make a small language model viable here. Holding a four-evaluator verification stack and refinement policy fixed and swapping only the generator between a 4B-parameter model with a QLoRA adapter and a frontier baseline, the small model reaches $0.984$ claim-level factual entailment against $0.992$ and comes within $3.3$ points on completeness, generating entirely on-device. Its deficit is confined to \emph{inter-section structural fidelity}---arrangement rather than clinical comprehension, and the axis on which it also falls furthest below the corpus's reference notes. Because that deficit is an explicit verifier decision rather than a silent quality difference, it becomes a routing policy: run the small model by default, escalate what the verifier rejects. Measured end to end, that it achieved a similiar verified-rate acceptance to the frontier-only acceptance in this test set ($99.6\%$ vs.\ $98.4\%$ over $250$ encounters) while routing $62$, documenting three quarters without a frontier \emph{generation} call. Ablating the loop separates architecture from scale: unrefined, the small model is accepted on $26.8\%$ of encounters and the frontier model on $74.8\%$, so verification does the most work where the generator is weakest. We also contribute section-scoped refinement, which preserves unflagged sections by construction rather than instruction, and find the baseline is not uniformly stronger---its provider refused two trauma-related transcripts the on-device model handled and certified, one facet of a provider dependency a served adapter does not carry.

---


### 42. [Learning from Self-Generated Responses: Reliability--Uncertainty Self-Distillation for Reasoning](https://arxiv.org/abs/2610.19176)

**<font color=#1a73e8>作者：</font>** Jinhao Pan, Bowen Wei, Yuqing Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reference solutions and question-specific rubrics are not always available to guide the teacher in self-distillation. A large language model's own solution attempts offer an alternative, but their quality is difficult to assess in open-ended tasks without automatic correctness checks, and even correct attempts can involve uncertain token predictions. We propose Reliability--Uncertainty Self-Distillation (\method{}) to learn from these attempts. The same model serves as teacher and student: the teacher receives the question and completed attempt, and the student matches the teacher's token-level predictions using a question-only prompt. \method{} weights each attempt's distillation loss by additively combining judged reliability, estimated from a self-judge's score and confidence, with student predictive uncertainty. Across eleven reasoning benchmarks, \method{} outperforms all five baselines in average accuracy, reaching 70.47\% on Qwen3-4B and 76.69\% on Qwen3-8B (8.90 and 2.10 percentage points above the base models). Data and code are available at this https URL.

---


### 43. [Multi-System Cognitive Steering for Generative Communication](https://arxiv.org/abs/2610.19177)

**<font color=#1a73e8>作者：</font>** Eric Lacosse, Pablo Tano, Daniel C. McNamee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A fundamental bottleneck for translating thoughts to speech is the high physical cost of motor input forcing a strict tradeoff between communication speed and expressivity. Generative AI offers a promising solution by expanding highly abbreviated text input into fluent sentences, significantly reducing the motor burden on the user. However, sparse inputs are inherently ambiguous; without sufficient context, AI models frequently misinterpret these abbreviations and generate outputs that fail to align with the user's true cognitive intent. We propose \textit{Cognitive Steering}, a framework that can be leveraged to reconstruct user intent by grounding Large Language Models (LLMs) in multimodal context and applying AI control methods. We demonstrate that aligning frontier models with selected environmental referents, emotional states, and communication motives on simulated abbreviation benchmarks achieves up to $\sim$88\% top-5 expansion accuracy, doubling no-context baselines. We also reveal that different types of context require distinct AI control techniques: while physical objects in a scene are best provided through explicit text prompts, abstract factors like emotion may be more effectively managed by directly altering the AI's internal activations. These findings suggest a hybrid architecture for future interfaces that leverage Cognitive Steering to help users communicate both quickly and accurately, recruiting multiple AI control methods simultaneously to perfectly capture their intended communication goals.

---


### 44. [HERO: Harnessing Evidence for Test-time Refinement and Prompt Optimization in Program Generation](https://arxiv.org/abs/2610.19184)

**<font color=#1a73e8>作者：</font>** Mingyu Lu, Timothy Ossowski, Tristan Naumann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Harness optimization improves LLMs by refining reusable prompts and scaffolding, yet requires further adaptation for program generation tasks such as text-to-SQL and text-to-Python. Existing methods often rely on LLM reflectors to propose harness updates, which can fix observed failures but also disrupt previously correct behavior. Text-to-code tasks offer a natural way to mitigate this issue: we can execute generated outputs, allowing us to evaluate and verify the effects of proposed updates directly. Building on this signal, we introduce \textsc{HERO} (\textbf{H}arnessing \textbf{E}vidence for \textbf{R}efinement and \textbf{O}ptimization), which combines offline and test-time harness optimization. At the first stage, \method{} learns reusable prompt updates from execution-verified successes and failures and validates candidate revisions before adoption. At test time, we treat the generated code as an instance-specific harness and refine it using execution feedback. Across four SQL, Cypher, and Python benchmarks, \method{} achieves the best offline performance, improving pass@1 by \(7.6\) points over the initial prompt, while test-time refinement adds another \(2.0\) points and improves execution efficiency.

---


### 45. [How to Evaluate When You Don't Know How to Evaluate? Choosing Reliable Setups for Base Language Model Benchmarking](https://arxiv.org/abs/2610.19185)

**<font color=#1a73e8>作者：</font>** Shenbin Qian, David Samuel, Jindřich Helcl 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluation of large language models (LLMs) remains largely pre-scientific: it involves many design decisions, with little guidance on how to make them. These choices can substantially affect measured performance and, consequently, decisions about subsequent pretraining. To identify effective evaluation setups, we investigate 8 aspects, such as task formulation or the number of in-context examples. We compare the setups using three widely-used signal criteria, repurposed as normative meta-measures: monotonicity, non-randomness, and ranking consistency of the evaluation scores across intermediate checkpoints. In an early pretraining scenario, we evaluate these setups on 26 monolingual 2B-parameter models trained on different types of data, using 80 tasks in four languages. We also examine the setups on three larger LLMs ($\geq$7B) in the same four languages and explore how the preferred setups change with model scale. Our results yield concrete recommendations: some choices, such as the use of multiple prompts, are consistently useful, whereas others, such as task formulation, depend on model scale. More generally, our framework serves as a recipe for the choice of evaluation setups in new scenarios.

---


### 46. [NEPSEE: A Double-Annotated Benchmark for Nepali Sentiment Analysis](https://arxiv.org/abs/2610.19190)

**<font color=#1a73e8>作者：</font>** Gaurab Baral, Mimansak Nepal, Grishma Basnet  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many sentiment datasets use one annotator for each item, so the test labels show the conventions of that person. We build a Nepali benchmark from two annotators who labelled the same sentences blind. They labelled 5,614 sentences from tweets of Nepali public figures on a five-point scale. We keep only the 3,189 sentences where both give the same polarity. On the three-class benchmark, NepBERTa with a fixed tokenizer gets a macro-F1 of 0.877 and IndicBERTv2 0.867. Three commercial large language models (LLMs) get 0.882 to 0.896 zero-shot, and these differences are not significant. On the five-point scale, 766 sentences have two adjacent labels, for example Pos and SPos. We accept both labels and train on both. On this task, Claude Opus 5.5 beats the best encoders by 0.10 to 0.12 macro-F1. A tokenizer audit adds a second result. The default tokenizers of three Nepali BERT models delete the non-spacing Devanagari vowel signs and the virama. When we restore the marks, macro-F1 increases by 0.084 for NepBERTa but decreases by 0.095 for a model pretrained on stripped text.

---


### 47. [Embedding Geometry Shapes LLM Routing: Tracing Failure Modes and Improving Generalization](https://arxiv.org/abs/2610.19198)

**<font color=#1a73e8>作者：</font>** Leonardo Torti, Emanuele Rimoldi, Tomer Galanti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the growing number of LLMs available, selecting which one to use for a prompt has become a key question. A large part of the routing literature relies on semantically embedding prompts into a vector space and then applying a lightweight classifier to the embedded representations. These methods perform robustly in-distribution but they struggle to generalize to unseen tasks. By studying the geometry of semantic embeddings, we trace a clear failure mode: features that determine the neighbors of unseen prompts are an unreliable proxy for LLM selection. We therefore replace the semantic embedding with the following map: we run a partial forward pass of Qwen2.5-7B-Instruct on the prompt and use the hidden state of its last token at a deep layer as the representation. When applying kNN and other simple classifiers to this new representation, we obtain a clear result in generalization: on average across cost penalties, their performance improves. Moreover, kNN and another simple classifier that we propose outperform every evaluated semantic-embedding baseline. Our two simple methods also beat a recent SoTA hidden-states based router on RouterBench.

---


### 48. [Weighted Ensemble Sampling for Rare-Event Estimation in Language Models](https://arxiv.org/abs/2610.19202)

**<font color=#1a73e8>作者：</font>** Zixuan Liu, Gustavo Didier, Fangzheng Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rare but severe failures of large language models can become practically significant at deployment scale. Estimating their probabilities with direct Monte Carlo sampling is highly inefficient, while proposal-based methods typically require auxiliary learning of an additional proposal distribution. We introduce \textbf{Weighted Ensemble (WE)}, a training-free framework for rare-event estimation in language models. WE samples exclusively from the original language model and improves upon direct Monte Carlo by periodically reallocating the sampling budget toward prefixes that appear more likely to reach the target rare event. To guide this reallocation without learning a separate proposal distribution, we exploit internal LLM representations as prefix-level signals and empirically validate their effectiveness. We provide a theoretical analysis of the proposed algorithm. Experiments on safety-related tasks spanning both small-scale and modern large-scale LLMs demonstrate that WE improves the efficiency and reliability of rare-event probability estimation.

---


### 49. [DUALVIEW: Leveraging Broad and Output-Specific Evidence for LLM-based Multi-Output Text Regression](https://arxiv.org/abs/2610.19206)

**<font color=#1a73e8>作者：</font>** Yiheng Su, Junyi Jessy Li, Matthew Lease  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While work on LLM-based regression has largely focused on scalar prediction, multi-output text regression remains less explored. We present DualView, a parameter-efficient approach to leverage LLMs for multi-output text regression. \method{} first extracts broad and output-specific representations from a frozen LLM, then uses a dual-branch architecture to produce the full score vector. Across five heterogeneous regression tasks and eight LLMs (up to 122B), DualView outperforms seven supervised regression baselines while requiring 82--1842 times fewer fitted parameters than the three strongest baselines. These improvements extend across individual output dimensions and persist even with limited training data. Notably, DualView using a smaller open-weight LLM can outperform unsupervised prediction with Gemini 3.1 Pro. Controlled ablations show that broad and output-specific evidence provide complementary predictive benefits, while lightweight shared predictors achieve strong performance with fewer trainable parameters.

---


### 50. [Titan-Llama: Retrofitting Pre-trained LLMs with External Neural Memory Modules](https://arxiv.org/abs/2610.19210)

**<font color=#1a73e8>作者：</font>** Sarah Pan, Ali Behrouz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformers are efficient to pre-train at scale because attention permits parallel computation across sequence positions, but long-context inference requires increasingly large KV caches. Efficient recurrent alternatives reduce the asymptotic complexity of inference, but their sequential dependence limits token-wise parallelism during training, making them harder to scale. Further, the current paradigm of extending long context tasks creates competing notions of retaining information precisely and keeping long-context inference efficient. To address this gap, we introduce Titan-Llama, a post-training method for retrofitting attention-based language models with a hierarchical memory architecture that updates parameters at test-time. Titan-Llama applies a blockwise attention mask and preserves full-fidelity attention over recent tokens while compressing historical context into recurrent, fixed-size neural memory modules (NMMs). Our formulation allows pre-trained attention layers to be replaced without training a new language model from scratch. On Llama-3.2-1B-Instruct, Titan-Llama raises accuracy over segmented attention windows from 23.87\% to 40.51\% on QuALITY and from 14.50\% to 40.75\% on LongHealth. Inference benchmarks show more than 20\% faster prefill, 37\% faster decode at medium context lengths, and 24\% lower steady-state decode memory usage in the evaluated configurations. Together, these results demonstrate that incorporating memory architecture mechanisms that utilize test-time training effectively modulates long-context behavior of pre-trained models, offering a practical route to adapting pre-trained transformers for efficient long-context inference. Our code is released on Github \href{this https URL}{GitHub}

---


> [!TIP]
> 当前位于：**1-50**（第 1/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-313](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
