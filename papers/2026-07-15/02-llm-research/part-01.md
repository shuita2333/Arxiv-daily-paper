# 🧠 大模型相关研究 | 2026年07月15日

> 本类共 **199** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-199](./part-04.md)

---

### 1. [Format Sensitivity Index: Token-Controlled Prompt Wrapper Robustness and Schema Compliance in LLM Benchmarking](https://arxiv.org/abs/2607.09665)

**<font color=#1a73e8>作者：</font>** Deep Pankajbhai Mehta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prompt wrappers often differ only in formatting, yet they can change model scores enough to flip leaderboard conclusions. We study this variance under a token-controlled protocol and introduce two complementary metrics: the Format Sensitivity Index (FSI), the accuracy range induced by wrapper choice, and the Parseability Sensitivity Index (PSI), the corresponding range in answer parseability. Across 140,000 OpenRouter generations spanning 7 QA tasks, 5 wrapper families, and 4 instruct models from 7B to 72B parameters, we find that mean FSI varies by over 30x across models and is largely explained by compliance failures. A fixed-effects regression shows that parseability remains a strong predictor of accuracy even after controlling for task, model, and wrapper. We argue that reporting accuracy without wrapper variance and compliance is statistically fragile, and we give practical recommendations for both benchmarking and structured-output deployments.

---


### 2. [Reference-Based Distillation Detection in LLMs](https://arxiv.org/abs/2607.09692)

**<font color=#1a73e8>作者：</font>** Rajat Rawat, Sizhe Chen, Akshay Anand 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model distillation -- training on outputs from stronger third-party models -- is widely used to boost performance, but raises concerns about unfair advantages and policy violations. This motivates a fundamental question: can we detect whether a model was distilled from another? We show that, while identifying a teacher model from a student in isolation is highly challenging, it becomes tractable in a reference-based setting: given a model and an earlier-generation checkpoint from the same lineage, we can identify the teacher model used to train the later checkpoint. We introduce a distillation detection method based on reference-based membership inference. By comparing how strongly a student model preferentially aligns with outputs from different candidate teachers relative to a reference checkpoint, our method identifies the most likely teacher and detects evidence of distillation. To handle unknown distillation pipelines such as hidden prompts, we infer proxy prompt templates directly from model outputs. We additionally identify a distinctive glyph-level signal specific to o1/o3 models. Evaluating distillation detection is challenging because modern model lineages are already heavily entangled. To address this, we develop a hybrid evaluation spanning both controlled distillation experiments and real-world models. Across both settings, our approach recovers the true teacher with near-perfect accuracy in single-teacher distillation scenarios, even when the underlying distillation pipeline is largely unknown. We further introduce statistical tests for both teacher attribution and distillation detection, and extend our framework to open-world settings where no teacher is guaranteed to be present among the candidates. Applying our method to contemporary models yields new evidence regarding potential distillation relationships involving QwQ, DeepSeek-R1, and GPT-OSS.

---


### 3. [Depth-Entropy Guided Sampling for Training-Free LLM Reasoning](https://arxiv.org/abs/2607.09693)

**<font color=#1a73e8>作者：</font>** Zibin Meng, Peng Xie, Kani Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become the dominant paradigm for improving the reasoning capabilities of large language models, but it requires expensive training, curated data, and reward signals. Recent work shows that sampling from sharpened base-model distributions at test time recovers much of the RL gain, yet existing methods rely solely on output-layer likelihoods and ignore the transformer's internal forward-pass dynamics. We introduce Depth-Entropy Guided Sampling (DEGS), a training-free, test-time method that exploits layer-wise entropy collapse as an intrinsic quality signal. We observe that stronger reasoners -- including RL-posttrained variants -- exhibit a distinctive "late collapse": logit-lens decoded entropy stays elevated until deeper layers before converging. We define a per-sequence collapse depth $D(\mathbf{x})$ and a joint objective $\pi(\mathbf{x}) \propto p(\mathbf{x})^\alpha \exp(\beta D(\mathbf{x}))$ that combines sequence likelihood with this depth-entropy structure, instantiated inside an MCMC power-sampling framework (DEGS-MCMC). Across three open-weight models and four reasoning benchmarks, this near-chance per-candidate signal compounds over the sampling trajectory into state-of-the-art training-free accuracy, with gains largest out of domain and on the harder splits -- exactly where likelihood alone falls short -- at single-digit-percent wall-clock overhead. DEGS narrowly trails an in-house GRPO reference on the math splits GRPO was trained for, yet surpasses it out of domain on GPQA for all three models, without any training, reward model, or labeled data.

---


### 4. [Safe responses matter: Output-aware safety guardrail mitigate over-refusal in MLLMs](https://arxiv.org/abs/2607.09697)

**<font color=#1a73e8>作者：</font>** Jiayi Li, Kun Zhan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing safety mechanisms for multimodal large language models (MLLMs) face a fundamental trade-off between safety and utility. Model fine-tuning achieves robust safety but compromises general utility. Input-side safety guardrails offer a lightweight alternative, yet they suffer from severe over-refusal, indiscriminately blocking benign queries or those the model could have safely answered through refusal or advisory responses. We identify that the root cause of over-refusal lies in the input-aware paradigm: safety guardrails make safety decisions without considering whether the model itself is capable of generating safe responses. Usually, MLLMs already possess intrinsic safety mechanisms that can transform harmful inputs into harmless outputs, but input-side safety guardrails override this capability, degrading user experience. Motivated by this insight, we propose a paradigm shift toward output-aware safety guardrails. Our method operates within the model's hidden state space to predict whether the forthcoming generation will be unsafe before it is fully produced. By training a lightweight classifier via multi-instance contrastive learning on hidden state representations, our approach distinguishes between inputs that will lead to unsafe outputs and those that will not, even when the inputs themselves contain risky elements. This enables precise intervention only when the model's actual response would be harmful. Extensive experiments demonstrate that our output-aware safety guardrail matches the safety performance of existing methods while drastically reducing over-refusal, preserving the model's utility and built-in safety capabilities. Code is available at: this https URL

---


### 5. [Closed-Loop Control with Rule-Aligned Small Language Models and Multi-Agent Self-Correction](https://arxiv.org/abs/2607.09713)

**<font color=#1a73e8>作者：</font>** Yuchen Wang, Javal Vyas, Tong Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A key step toward autonomous industrial operation is the ability to create and reconfigure control policies from natural-language requirement specifications, with minimal or no manual redesign. In this setting, policy generation by AI agents can be a credible path when paired with a plant-aware validator (e.g., a digital twin) that can check generated candidate actions before execution. However, practical deployment is constrained by inference latency and compute footprint: large cloud-based models are often too slow, opaque, or data-sensitive for edge closed-loop use. This work investigates whether a compact Small Language Model (SLM) can be retrained for control reasoning and embedded in a validator-guided correction loop. We use a Qwen2.5-1.5B model aligned via Group Relative Policy Optimization (GRPO), combined with (i) an action agent, (ii) a symbolic/digital-twin-style validation layer, and (iii) a reprompting agent that iteratively steers outputs toward valid actions. In randomized thermal-control simulations (30 experiments with 500 steps each), the framework achieves 91.5% average action-alignment accuracy (86.3%--100% across cases) at 3.84\,s mean inference latency. Under symbolic re-mapping, it maintains a 95% in-range rate, indicating robust physical regulation despite reduced token-level agreement. These results support SLM+validator architectures as a practical path toward reconfigurable autonomous control at the edge.

---


### 6. [Coresets Before Score Sets: Evaluation-Unsupervised Prompt Subset Selection for LLM Benchmarks](https://arxiv.org/abs/2607.09739)

**<font color=#1a73e8>作者：</font>** Jihan Yao, Gantavya Bhatt, Arnav Das 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study LLM benchmark coreset selection: selecting a small subset of prompts over multiple benchmarks whose induced model scores and rankings approximate those obtained from the full benchmark suite. In evaluation-unsupervised benchmark coreset selection (our approach), the selection algorithm uses no model evaluation outcomes, and operates on a fine granularity by producing subsets of prompts over multiple benchmarks rather than producing a sub-collection of entire benchmarks. We use submodular subset selection, and we develop and evaluate many different submodular functions for this purpose, including determinantal point process (DPP) based approaches, submodular mutual information functions, and facility location-based functions. On a new large-scale suite of 35 heterogeneous benchmarks spanning five different capability categories, 18 frontier LLMs, and over 61K prompts, we find that the facility location (FL) function operating exclusively on inexpensive semantic prompt embeddings preserves LLM scores better than twelve separate score-based and diversity-based baselines, across a range of coreset budgets. Moreover, we show our proposed objective is not limited to the evaluation-unsupervised regime: in the setting where only a handful of whole benchmarks must be selected and a large amount of model scores are available, the same objective matches or outperforms state-of-the-art baselines on the MMLU and MTEB leaderboards, while being substantially cheaper to compute. Together, our results suggest that submodularity, in general, is a strong and reliable tool for benchmark compression.

---


### 7. [Scaffolding the Strategist: Architecture-Dependent Reasoning Interventions in Hotelling Spatial Markets](https://arxiv.org/abs/2607.09743)

**<font color=#1a73e8>作者：</font>** Pratyush Singh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We investigate whether structured reasoning interventions improve the strategic economic reasoning of large language models, and whether their effects depend on model architecture. Using Hotelling's linear city model as a diagnostic vehicle, we evaluate GPT-4.1-mini (a standard instruction-following model) and GPT-5-mini (a reasoning-optimized model) under five conditions - an unscaffolded baseline and four reasoning interventions - across eight questions spanning deductive and abductive reasoning, three prompt framings, and three repetitions per condition, yielding 720 individually judged responses. We find a statistically significant crossover interaction between scaffolding type and model architecture ($t(7) = 4.79$, $p = 0.002$, $d = 1.69$): commitment scaffolding improves the standard model ($+0.21$) while degrading the reasoning model ($-0.63$), and principled separation shows the opposite pattern ($-0.40$ vs. $+0.31$). Both crossovers are individually significant (commitment: $p = 0.040$; separation: $p = 0.002$) and hold across all eight questions with 7/8 directional consistency. Adversarial stress-testing harms both models, with $2.6\times$ greater degradation for the reasoning model ($-1.47$ vs. $-0.57$; $p = 0.038$), and the damage correlates negatively with baseline difficulty ($R^2 = 0.36$, $p = 0.014$). We further document a persistent declarative-procedural gap in which both models identify correct strategies at rates far exceeding their ability to execute them; separation fully closes this gap for the reasoning model while no intervention helps the standard model.

---


### 8. [Replicating Belief, Not Bits: Epistemic State Replication for Agentic Systems](https://arxiv.org/abs/2607.09748)

**<font color=#1a73e8>作者：</font>** Jun He, Deying Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In distributed systems, the classical State Machine Replication (SMR) model assumes that correct replicas execute deterministic transitions to yield identical bitwise states. However, the rise of agentic distributed systems -- where autonomous, stochastic, and model-driven agents orchestrate infrastructure -- presents scenarios where deterministic, bitwise replication is insufficient. Replicas operating with generative models may exhibit divergent reasoning paths, summaries, and token boundaries, yet reach semantically equivalent and correct operational decisions. Forcing bitwise agreement across these stochastic participants degrades execution flexibility, induces context amnesia, and limits performance.
We argue that in such settings replicas should agree on belief, not bits. We propose Epistemic State Replication (ESR), a belief-replication layer for agentic distributed systems that shifts the replication boundary from data visibility to knowledge visibility. We formalize the epistemic node state as a pair K = (L, B) separating the deterministic, immutable evidence log (L) from the stochastic, evolving belief lineage (B). To govern execution safety, we define Semantic Linearizability, which requires operations to reflect the latest committed operational meaning within a verifier-bounded semantic compatibility metric, and Bounded Eventual Coherence, which bounds expected semantic divergence under fair delivery, monotonic evidence, bounded verifier disturbance, and a contractive graft operator. We outline protocols for propagating derived insights using structured epistemic deltas, and formalize Verifiable Semantic Rollbacks to prune faulty premises from belief lineages without inducing context amnesia. We prototype ESR and report preliminary simulation results that show feasibility under the stated assumptions and illustrate reductions in secondary cognitive faults.

---


### 9. [BatteryLake: Agentic, Physics-Grounded Curation of Heterogeneous Battery Aging Data and Benchmarking](https://arxiv.org/abs/2607.09762)

**<font color=#1a73e8>作者：</font>** Tianwen Zhu, Hao Wang, Yonggang Wen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Public battery aging datasets are a critical asset for advanced health management, but their practical use is often limited by inconsistent formats, unclear schemas, and metadata scattered across repositories and publications. Current curation remains largely manual and hard to reproduce, while general-purpose data integration tools miss the domain-specific semantics of electrochemical time-series data. We present BatteryLake, a governed data lakehouse that turns raw public battery data into benchmark-ready assets through an agentic, physics-grounded curation framework, with three contributions. First, LLM agents extract metadata and synthesize dataset-specific converters, grounding every output in verbatim evidence and abstaining when none supports a value. Second, a human-in-the-loop mechanism frames verification as selective prediction and gates admitted data through 26 schema, statistical, and physical-plausibility rules. Third, we release an open benchmark of 41 datasets from over 25 institutions, with standardized SOH and RUL tasks, three split protocols, and eight baseline model families. The platform, benchmark, and curation protocol are publicly available at this https URL.

---


### 10. [Verification of Adaptive Agentic Controllers through Finite Rule Revision](https://arxiv.org/abs/2607.09770)

**<font color=#1a73e8>作者：</font>** Roberto Garrone  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial agentic AI systems increasingly exhibit a gap between prototype capability and production deployment. In particular, adaptive agents may generate plausible outputs while remaining difficult to verify under non-determinism, confidentiality constraints, limited context, and weak observability. This paper formulates a bounded verification protocol for adaptive agentic controllers represented by finite symbolic rules, explicit diagnostic predicates, explanation logs, and held-out re-evaluation. The central research question is: when an adaptive agentic controller is represented through finite rules, explicit diagnostic predicates, explanation logs, and held-out re-evaluation, which classes of controller failure can be detected, locally repaired, or rejected without relying on unrestricted human-in-the-loop judgment? The proposed framework treats the controller as a finite revisable object. Diagnostic failures are mapped to predefined rule-level edits, including rule addition, rule deletion, and priority revision. Repaired controllers are then evaluated on held-out simulation seeds or cloned initial states. Experiments in a stylized financially constrained inventory-control benchmark show three outcomes: resource-induced failures that remain non-repairable by one rule edit, partial repairs that are rejected because they violate thresholds or guardrails, and a local one-step repair of an order-volatility failure induced by removing a smoothing rule. The contribution is methodological and provides a simulation-compatible procedure for testing whether specific controller-level failures can be made observable, explainable, locally revisable, and empirically re-tested under controlled conditions.

---


### 11. [PHITSBench: an execution-scored benchmark for AI-assisted PHITS radiation-transport input generation using natural language](https://arxiv.org/abs/2607.09789)

**<font color=#1a73e8>作者：</font>** Xianglin Ji, Svetlana V. Boriskina  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce PHITSBench, an execution-scored benchmark for the Monte Carlo Particle and Heavy Ion Transport code System (PHITS). PHITSBench comprises 282 transport-scorable tasks spanning three common workflow categories: parameter editing (Edit), syntax repair (Repair ), and complete simulation generation from natural-language descriptions (Reproduce). Each task is evaluated using a Composite Metric Score that combines execution success with agreement between generated and reference transport observables. Using PHITSBench, we evaluate five GPT-5.4-based configurations ranging from zero-shot prompting to knowledge-augmented and agentic workflows. Without domain-specific knowledge, the model performs well on editing and repair tasks (95% and 70% success, respectively) but fails to generate correct simulations from scratch (0% success on the Reproduce track). A structured, machine-readable PHITS knowledge catalog, supplied alongside the user manual, raises single-shot Reproduce-task success to 57%. Agentic execution provides a further improvement to 66-73%, but at increased computational cost. Failure analysis shows that the remaining errors are dominated by incorrect selection and configuration of physical observables rather than syntax generation. These results suggest that future progress in AI-assisted radiation-transport modeling will depend as much on machine-readable knowledge bases, curated domain-training datasets, and execution-grounded evaluation environments as on advances in foundation models themselves.

---


### 12. [Agentic Context Learning with Self-Discovered Specification](https://arxiv.org/abs/2607.09794)

**<font color=#1a73e8>作者：</font>** Jike Zhong, Ming Li, Yuxiang Lai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Context learning is an emerging inference-time task where LLMs must learn and apply novel, task-specific knowledge from intricate contexts absent from pre-training; even frontier models score under 24% task success. In this work, we conduct a comprehensive empirical study to understand why this setting remains difficult. A natural hypothesis is that failures stem from content access; yet across twelve retrieval, reflection, and verification baselines on CL-Bench, an extensive context learning benchmark, we find limited gains over direct full-context prompting. Further failure analysis reveals a key finding: unlike typical long-context tasks such as long document understanding, context learning requires not only recovering local content but also acquiring local specifications that are often unspecified in the query but distributed across the context: domain-specific formats, local rules, and completeness conditions. Across all 31,592 rubric items, we find that 55.4% clearly evaluate specification acquisition, while only 22.6% evaluate content acquisition. Moreover, despite 76.7% of specifications being unspecified in the user query, 95.5% are traceable to the context, indicating these are learnable obligations rather than hidden requirements. To validate this diagnosis, we design a deliberately simple intervention PSCI (private specification-contract induction) which extracts local specifications and enforces them through adversarial checking and repair; PSCI achieves state-of-the-art 28.14% with GPT-5.1 (+5.59 pp absolute and +24.8% relative) on CL-Bench, replicated on Qwen3.5-27B (+5.28 pp) and Gemini 3 Pro (+6.17 pp). Seventeen ablations further isolate the role of task-specific specifications. Overall, our results suggest context learning hinges on not only content acquisition but also specification acquisition.

---


### 13. [Metadata-Free Meta-Reweighted Direct Preference Optimization under Noisy Preference Labels](https://arxiv.org/abs/2607.09796)

**<font color=#1a73e8>作者：</font>** Hua Qu, Yifan Li, Xiaodong Yuan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) has become an important method for aligning large language models (LLMs) with human preferences because it removes the need for explicit reward modeling and reinforcement learning optimization. However, its performance depends heavily on the quality of preference data, and noisy preference data in real-world settings can weaken alignment performance. To address this issue, we propose a bilevel optimization framework and prove, under certain assumptions, that this framework can recover the DPO optimum under clean data. We further derive a prior form for the learnable weighting function under asymmetric label-flipping noise. Considering that high-quality metadata may be difficult to obtain, we propose a task-agnostic meta-knowledge-driven method that enables meta-learning even when metadata is completely unavailable. To reduce the high cost of higher-order gradients in LLM meta-learning, we combine central-difference approximation with LoRA fine-tuning and develop a scalable training scheme. Experiments on TL;DR summarization and Anthropic HH single-turn dialogue show that the proposed method improves training performance over multiple DPO baselines under different noise rates.

---


### 14. [Memory-Conditioned Tool Calling for Camera-First Visual Agents](https://arxiv.org/abs/2607.09822)

**<font color=#1a73e8>作者：</font>** Xiaofan Wu, Xi Zeng, Miaoxia Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recognition tells an agent what is in an image; personal memory affects what is worth looking up next. In a camera-first setting the user can send only an image, so the agent must form the lookups. We study whether personal visual memory improves agent-side tool choice and tool arguments, and thereby more user-aligned multi-tool lookups. The design uses a three-layer personal visual memory (profile, short-term focus, observations) that is loaded on each turn to condition an LLM tool-calling loop under camera-first intake, and includes conflict-aware write-back intended to refresh the user model for later captures. On 800 images paired with synthetic memory blocks constructed for controlled ablation, removing the full three-layer memory block reduces tool-query relevance by 0.47 points absolute (4.21 -> 3.74 on a 5-point scale; 11.2% relative) and end-to-end utility by 0.082 absolute (0.842 -> 0.760; 9.7% relative). These results measure memory conditioning of tool policy under image-only intake with fixed synthetic blocks, not multi-session write-back from live user histories.

---


### 15. [Exploring Agentic Workflows for Generating High Quality Math Visual Aids](https://arxiv.org/abs/2607.09839)

**<font color=#1a73e8>作者：</font>** Rizwaan Malik, Ashna Khetan, Isabel Sieh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mathematical diagrams play a crucial role in K 12 education, both as problem components and as scaffolding for student comprehension. However, current AI tools, including Large Language Models (LLMs), struggle to reliably generate accurate and pedagogically sound visual diagrams, even when provided with detailed descriptions. A significant gap therefore remains in the reliable generation of diagrams for middle school mathematics. To address this, we introduce an agentic workflow that enables LLM agents to evaluate the quality of generated visuals and use this feedback to iteratively improve their outputs. This self improvement loop aims to enhance the accuracy and educational appropriateness of AI generated diagrams. Our research investigates two questions. First, can LLMs accurately generate quality assurance questions for a visual aid given specific criteria for visual quality? Second, given valid quality assurance questions, can Vision Language Models effectively evaluate generated K 12 visual aids and use the resulting feedback to improve them iteratively? We conduct an exploratory evaluation of our agentic workflow and identify key areas for improvement, including stronger spatial reasoning and more comprehensive coverage of diagram features in the generated quality assurance questions. Our results provide preliminary evidence that this approach can improve the reliability and educational value of AI generated mathematical diagrams.

---


### 16. [From Direction to Magnitude: How Multimodal Instruction-Tuning Reorganizes the Geometric Encoding of Identity-Specifying Prompts in Transformer Hidden States](https://arxiv.org/abs/2607.09842)

**<font color=#1a73e8>作者：</font>** Jorge A. Castillo, Marco Torres Yévenes, Juan Carlos Lanas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate whether identity-specifying system prompts produce statistically distinguishable geometric fingerprints in the hidden-state trajectories of four open-weight transformer language models spanning four post-training regimes: no training (Gemma-4-E4B base), multimodal RLHF (Gemma-4-E4B-it), RL distillation (DeepSeek-R1-Distill-Qwen-7B), and SFT (Qwen2.5-7B-Instruct). Three prompt conditions (an identity-specifying axis prompt, a length-matched generic-assistant prompt, and a 26-token vanilla baseline) are compared via five geometric metrics, principally the 1-Wasserstein distance between edge-wise distributions of Ollivier-Ricci curvature on k-NN trajectory graphs. Claims rest on trajectory-level permutation tests with multiple geometric controls (teacher-forced content controls, temporal-chain vs k-NN topology, ABT-projected k-NN, angular vs Euclidean graph construction, B=5000 permutations on borderline statistics). The central finding is a qualitative reorganization of identity encoding across the instruction-tuning boundary: in the base model the fingerprint is direction-coded (separation 0.034, p=0.002 under angular k-NN); in the multimodal instruction-tuned model it migrates into the magnitude (angular separation collapses to p=0.439 while Euclidean survives at p=0.042, and the mean norm of the first generated state inverts its length-ordering, being lowest for the identity prompt). This direction-to-magnitude reorganization is specific to the multimodal instruction-tuning regime, absent under RL distillation and SFT. A teacher-forced control attributes ~30% of the free-running cosine signal to prompt-driven effects. We position W_1 on edge-wise Ollivier-Ricci distributions on k-NN trajectory graphs as a methodological contribution of independent interest.

---


### 17. [Serving the Long Tail: Training-Free LLM Candidate Generation for Vacation Rental Marketplaces](https://arxiv.org/abs/2607.09877)

**<font color=#1a73e8>作者：</font>** Syed Mohammed Arshad Zaidi, Eric Rincon, Shayan Hassantabar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vacation rental marketplaces face a structural imbalance on the supply side: a small fraction of properties receive most user interactions, while the long tail of new, niche, and seasonal listings generates too little behavioral signal for collaborative filtering to serve effectively. At Vrbo, item-based k-nearest neighbors (IBKNN) is a core candidate generation channel, but leaves tens of thousands of properties with no candidates and produces weak neighborhoods for sparsely interacted ones. We present a training-free, LLM-based candidate generation pipeline that complements IBKNN using static property metadata alone. An off-the-shelf LLM synthesizes diverse semantic queries per property, a pre-trained text encoder embeds them, and an approximate nearest-neighbor index retrieves candidates from an 11.7M-property catalog. A Union fusion strategy merges these with IBKNN while preserving the behavioral channel's ordering, guaranteeing no degradation on well-served properties, and a downstream learning-to-rank model re-scores the fused pool. Evaluated on 1.6M focal properties, the system extends candidate coverage to tens of thousands of properties IBKNN cannot reach, delivers its largest gains on the long-tail segment where behavioral methods are weakest, and matches or beats IBKNN at every K on shared properties. A downstream learning-to-rank stage further lifts the fused pool, yielding a complete candidate generation and re-ranking stack that serves the long tail without regressing well-served properties. We additionally show that Union fusion collapses the recall gap between a 3B open-weights LLM and frontier API-based models from 27-46% to under 1%, supporting self-hosted small-model deployment at marketplace catalog scale.

---


### 18. [CLIR-Bench: Benchmarking Multimodal Question Answering over Irregular Clinical Time Series](https://arxiv.org/abs/2607.09880)

**<font color=#1a73e8>作者：</font>** Frank Nie, Ethan B. Liu, Yuan Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical time series are central to patient monitoring, risk assessment, and clinical decision support. However, they are often sparse, irregularly sampled, and asynchronous, making it difficult for models to identify the temporal evidence required for clinical Question Answering (QA). Existing benchmarks primarily focus on regularly sampled time-series QA or medical QA over static data, and therefore rarely assess whether models can faithfully ground their answers in irregular temporal observations. To fill this gap, we introduce CLIR-Bench, a benchmark for irregular clinical time series QA constructed from de-identified ICU records through a principled four-stage pipeline. CLIR-Bench contains 6,600 QA instances spanning 11 clinical variables, organized into four capability dimensions and 11 tasks. Each question is linked to explicit temporal evidence and task-specific answer derivation rules, enabling evaluation of both answer accuracy and evidence use. Experiments show that existing generalist models struggle to retrieve and reason over sparse clinical evidence, highlighting the need for stronger irregular time-series reasoning methods. Our code and data are available at this https URL.

---


### 19. [ShapKO: Shapley-Adaptive Modality Knockout for Robust Multimodal Learning](https://arxiv.org/abs/2607.09884)

**<font color=#1a73e8>作者：</font>** Nusrat Binta Nizam, Fengbei Liu, Sunwoo Kwak 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal medical models often degrade when inputs are missing, a common scenario in real-world clinical workflows. Separately, even when all modalities are present, modality dominance is observed during training, where optimization over-relies on a highly predictive modality and undertrains complementary sources, resulting in poor robustness under partial availability. While training-time modality knockout improves missing-modality robustness, existing approaches use static masking rates that cannot adapt to evolving modality utility during training. We introduce ShapKO (Shapley-Adaptive Modality Knockout), a dynamic training strategy that learns modality-specific knockout probabilities based on validation utility. ShapKO periodically evaluates performance across modality subsets, estimates modality importance via Shapley values, and updates masking probabilities to suppress dominant modalities more frequently. This adaptive process promotes complementary representations, while requiring no architectural modifications. We evaluate ShapKO on three datasets covering multitask clinical classification, survival prediction, and cancer detection. ShapKO consistently improves performance under modality absence and yields interpretable trajectories of learned masking behavior. Code is available at: this https URL

---


### 20. [Index SLM Technical Report](https://arxiv.org/abs/2607.09885)

**<font color=#1a73e8>作者：</font>** Lusheng Zhang, Shien He, Tianxing Yan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Index-1.9B, a series of open small language models developed at Bilibili. The series comprises four models: Index-1.9B-Base, a foundation model with 1.9 billion non-embedding parameters pre-trained on 2.8 trillion predominantly Chinese and English tokens; Index-1.9B-Pure, a control variant trained with an identical recipe but with all instruction-like data strictly filtered from the corpus; Index-1.9B-Chat, aligned from the base model with supervised fine-tuning and direct preference optimization; and Index-1.9B-Character, which augments the chat model with retrieval-augmented generation for few-shot role-playing customization. Pre-training employs a Warmup-Stable-Decay learning-rate schedule in which the concentration of curated data is raised substantially during the decay phase, together with a Norm-Head output layer that stabilizes training under large learning rates. On a suite of standard benchmarks covering examination, reasoning, mathematics, and code, Index-1.9B-Base attains an average score of 64.92, competitive with or exceeding open models of several times its size. We further report controlled studies on model depth, learning-rate magnitude and scheduling, the interaction between learning-rate decay and data quality, and the effect of including instruction data during pre-training, and we document an unexplained surge in benchmark performance midway through the constant-learning-rate phase. All models, together with evaluation code, are released at this https URL.

---


### 21. [When LLM Tutoring Responses Work: Evidence from Student Programming Conversations](https://arxiv.org/abs/2607.09919)

**<font color=#1a73e8>作者：</font>** Mohammad Fahim Abrar, Shayla Sharmin, Roghayeh Leila Barmaki  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As students increasingly use LLM tutors in computer science education, one question becomes especially important: what kind of response helps a student continue productively? Prior work has studied how students use LLMs in computer science education, but less is known about how tutoring response styles are associated with student follow-up across programming help-seeking contexts. This paper analyzes StudyChat (UMass, 2026), a public dataset of student and ChatGPT tutoring conversations from an artificial intelligence course. We transformed StudyChat into 16,851 assistant-response interactions from 203 students and 2,214 conversations. Using local LLM-assisted annotation with Gemma 4, we labeled student help-seeking situations, student state, assistant response style, and student next-turn outcome. Human validation showed 82\% agreement with the LLM-assisted labels (Cohen's $\kappa=.74$). We analyzed productive continuation and unresolved continuation across the full dataset and across help-seeking contexts. Globally, response style was significantly associated with productive continuation, $\chi^2(7)=100.39$, $p<.001$, $V=.078$, and unresolved continuation, $\chi^2(7)=125.77$, $p<.001$, $V=.087$, though effect sizes were small. Verification feedback had the highest productive-continuation rate (82.4\%), while direct answers had the lowest (62.7\%). Descriptively, response-style score ranges were smallest in low-confusion conceptual contexts (.017) and largest in high-cognitive-load contexts (.203). More detailed comparisons showed situation-dependent response patterns. For example, stepwise guidance was followed by greater confusion decrease in high-cognitive-load code requests, while direct answers were followed by more unresolved continuation in high-load debugging. These findings support context-aware evaluation and design of AI tutoring responses for programming education.

---


### 22. [Global Merger-Arbitrage Forecasting with Language Models](https://arxiv.org/abs/2607.09921)

**<font color=#1a73e8>作者：</font>** Hinal Jajal, Michal Mucha, Charles Sweat 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a language-model forecasting system for merger arbitrage, a specialized high-stakes financial setting in which the task is to predict the outcome of announced M\&A deals. Unlike prior work on judgmental forecasting with LLMs, which has focused on broad mixed-topic benchmarks and short context such as news snippets, we study a setting that requires long-context reasoning over hundreds of pages of technical documents. Our system combines expert-guided context engineering with finetuning on hindsight-guided reasoning traces derived from historical deals. Given an announced deal, it outputs a probability distribution over three mutually exclusive outcomes: closing at announced terms, a higher bid, or deal termination. On an out-of-sample set of more than 400 large deals spanning 42 countries, our finetuned system achieves the best performance of any method we evaluate, reducing class-balanced Brier score to 0.151. This is 24\% below calibrated market-implied probabilities, 19\% below XGBoost, and 25-42\% below frontier language models. These results, together with ablation studies, show that LLM-based forecasting can succeed in specialized, long-context financial workflows, with hindsight-based supervision and expert-designed context playing a critical role.

---


### 23. [Faithful by Design: Evaluating and Improving LLM-Generated Clinical Trial Summaries for Multi-Stakeholder Audiences](https://arxiv.org/abs/2607.09932)

**<font color=#1a73e8>作者：</font>** Robert Williams  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to summarize clinical trial results for healthcare providers, patients, and payers, but their tendency to hallucinate poses significant risks in this high-stakes context. This study introduces a benchmark evaluation framework for measuring the faithfulness of LLM-generated clinical trial summaries across three stakeholder audiences. The framework consists of 200 stratified trials drawn from the Aggregate Analysis of this http URL database, evaluated using audience-specific prompt templates and a six-dimension faithfulness annotation schema. Baseline measurements were established for GPT-4o, Claude Sonnet 4.6, and Gemini 2.5 Flash across 1,800 generated summaries scored using a cross-encoder natural language inference (NLI) model. Unsupported Claims was identified as the dominant failure mode across all three models, with a mean annotation score of 1.55 out of three. A knowledge-graph-augmented retrieval system was developed and evaluated against the baseline, producing statistically significant improvements in NLI-based faithfulness scores (entailment +0.0125, faithfulness +0.0130, p < 0.0001). Improvement pathways were model-dependent, with GPT-4o improving primarily through contradiction reduction while Claude Sonnet 4.6 and Gemini 2.5 Flash improved through increased entailment.

---


### 24. [SMETA-ZSL:Semantic Meta-Alignment for Zero-Shot Threat Classification](https://arxiv.org/abs/2607.09936)

**<font color=#1a73e8>作者：</font>** Ivan Alejandro Montoya Sanchez, Anantaa Kotal, Aritran Piplai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cybersecurity systems must adapt rapidly to emerging threats. However, labeled data for new threat categories is unavailable when those threats first appear. Generalized zero-shot learning offers a natural solution by enabling recognition of unseen classes through auxiliary semantic knowledge rather than labeled examples. Large language models are particularly promising in this setting because they can convert unstructured CTI reports into semantic prototypes for emerging threats. However, applying language-driven zero-shot learning to cybersecurity is difficult due to strong semantic overlap between threat descriptions, heterogeneity between behavioral attributes and text, severe class imbalance, and open-set conditions where unseen threats are unknown during training. We propose SMETA-ZSL, that learns semantic prototypes from overlapping language descriptions through contrastive finetuning, aligns behavioral features through episodic meta-learning and knowledge distillation, and performs adaptive routing for generalization across seen-unseen classes. Across 7 benchmarks, SMETA-ZSL delivers the strongest overall generalized zero-shot performance under the strictest inductive setting, surpassing prior methods by 10.8 points on average, with gains up to 18.1 points. Github:this https URL

---


### 25. [A Foundation Model for Multimodal Event Sequences in Financial Applications](https://arxiv.org/abs/2607.09955)

**<font color=#1a73e8>作者：</font>** Nikita Rusakov, Vladislav Meshkov, Konstantin Zorin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive modeling is a core component of modern financial services, where a wide range of tasks are traditionally addressed using separate models trained on manually engineered tabular features. This task-specific approach limits reuse and makes it difficult to fully exploit heterogeneous data sources such as transaction histories and digital interaction signals. In this paper, we present an approach based on pretraining a foundation transformer model on multimodal sequences of user events. Events from multiple data sources are unified into a single chronological sequence, enabling early fusion of heterogeneous modalities and learning of general-purpose representations via a next-event prediction objective. These representations are combined with existing engineered user features, on top of which lightweight neural models are trained for multiple downstream tasks. The proposed system outperforms traditional task-specific models while reducing development overhead. The approach was deployed in production at one of the biggest banks in Eastern Europe, resulting in measurable improvements in business metrics.

---


### 26. [Multimodal Routing for Interpretable, Robust, and Auditable Clinical Prediction](https://arxiv.org/abs/2607.09982)

**<font color=#1a73e8>作者：</font>** Nikkie Hooman, Zhongjie Wu, Eric C. Larson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electronic health record (EHR) data are inherently multimodal, and leveraging multiple modalities can improve predictive performance. However, most existing approaches rely on deep fusion, which obscures how individual modalities contribute to predictions and limits the interpretability of multimodal reasoning. We propose an explicit multimodal routing framework for clinical prediction that enables interpretable, robust, and auditable reasoning across three EHR modalities: structured longitudinal variables (L), clinical notes (N), and chest X-rays (I). Our model constructs discrete unimodal, directional bimodal, and trimodal routes to capture both individual modality signals and asymmetric cross-modal interactions. To audit multimodal reasoning and assess robustness, we introduce inference-time route masking, which simulates missing modalities and reweights the remaining routes without retraining. We analyze changes in performance and routing weights under these scenarios to understand model decision-making. We evaluate our framework on multi-label phenotype prediction (K = 25) and binary ICU mortality prediction using trimodal patient stays from MIMIC-IV, revealing systematic differences in modality reliance across clinical condition groups. Overall, our framework offers a transparent, auditable, and practical approach to multimodal clinical prediction, providing interpretability, robustness, and insights into how different data sources drive model decisions.

---


### 27. [Who&When Pro: Can LLMs Really Attribute Failures in AI Agents?](https://arxiv.org/abs/2607.09996)

**<font color=#1a73e8>作者：</font>** Jiale Liu, Huajun Xi, Shaokun Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated failure attribution uses LLMs to identify where and why agentic systems fail. As agents become more capable, their failures become subtler, making automated attribution increasingly important. We introduce Who&When Pro, a large-scale benchmark for automated failure attribution in agentic systems. Using a strictly controlled pipeline that injects a failure only after exactly replaying a successful prefix, we construct 12,326 failed trajectories with golden labels across 3 modalities and 26 benchmarks covering various scenarios. Beyond benchmarking, we conduct extensive experiments and analyses, revealing systematic patterns in how models attribute failures across modalities, protocols, and model families, and providing empirical guidance for future automated failure attribution systems.

---


### 28. [Vilya-1: An all-atom foundation model for macrocycle structure prediction and design](https://arxiv.org/abs/2607.09998)

**<font color=#1a73e8>作者：</font>** Vilya Research, Pascal Sturmfels, Milad Salem 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Macrocyclic peptides are an increasingly important therapeutic modality, but existing computational methods for modeling their structures and properties are limited in scope and do not generalize well across the synthetically accessible chemical space. In this work, we introduce Vilya-1, a deep learning model that addresses two central challenges in macrocycle design: sampling biologically relevant conformations across arbitrary chemistries and predicting key developability properties such as membrane permeability. Vilya-1 operates on a uniform all-atom representation and is trained on heterogeneous structural datasets spanning diverse topologies and chemical classes. Across a broad set of macrocycles composed of canonical and non-canonical residues, Vilya-1 substantially improves geometric accuracy relative to physics-based methods, co-folding networks, and deep-learning conformer generators, while maintaining broad chemical coverage that extends to small molecules. Vilya-1 also supports generative applications, enabling the design of novel macrocycles with tailored chemical, structural, and property profiles. Together, these capabilities establish Vilya-1 as a foundation model for accelerating the development of next-generation macrocycle therapeutics.

---


### 29. [Silent Failures in Quantized LLM Reasoning: A Taxonomy-Based Analysis of Hollow Convergence and Failure Mode Shifts](https://arxiv.org/abs/2607.09999)

**<font color=#1a73e8>作者：</font>** Renuka Oladri, Mohan Vamsi Varadaraju Priya, Jerry Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We show that post-training quantization can silently alter how large language models reason even when task accuracy is preserved. Using a six-category failure taxonomy validated by two independent human annotators (Cohen's $\kappa$ = 0.906), we classify 30,000 chain-of-thought outputs from five instruction-tuned LLMs (3B--14B parameters) across three quantization precisions (FP32, FP16, NF4) and four reasoning benchmarks. We find that while accuracy is robust across precisions (maximum 3.1 pp drop), Hollow Convergence (correct answers reached through incomplete or unverifiable reasoning) shows a significant size-dependent shift under NF4, dropping sharply for the two smallest models tested but remaining invariant for models at 12B parameters and above. This effect is also benchmark-specific: GSM8K is categorically immune while LogiQA and ARC-Challenge show the largest shifts. Furthermore, under NF4, Shortcut Collapse rises from 44% to 78% of wrong-answer failures in LLaMA 3.2-3B while Confidence Snowballing collapses from 15.8% to near zero, a qualitative shift invisible to accuracy metrics. Finally, we show Hollow Convergence cannot be reliably detected from surface-level text features (best F1 = 0.53), establishing it as a deployment-relevant failure mode that standard evaluation pipelines cannot catch.

---


### 30. [Model Guides You How to Draw: Adaptive Visual Gating for Unified Multimodal Reasoning](https://arxiv.org/abs/2607.10004)

**<font color=#1a73e8>作者：</font>** Wenxi Gao, Guanxi Lu, Didi Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models (UMMs) with interleaved reasoning, which generate both textual and visual steps as part of intermediate reasoning traces, have demonstrated great potential for visual mathematical reasoning tasks. However, we identify a key insight in this paradigm: generating intermediate visual reasoning steps is not always beneficial and can even be harmful, as self-generated visual steps may introduce erroneous visual evidence that misleads subsequent reasoning. Moreover, frequently triggering visual steps during reasoning incurs substantial computational and memory overhead, degrading inference efficiency. To address these accuracy and efficiency challenges, we observe that the model's internal signals can indicate whether a visual step will benefit reasoning before the entire visual generation is completed. Specifically, this work identifies two internal signals: 1) Generation Intent, which reflects whether the model has a concrete textual plan for what to draw, and 2) Visual Fidelity, which measures whether the visual generation remains grounded in the original input image. Leveraging these internal signals, we propose AdaViG, a training-free adaptive visual gating method for unified multimodal reasoning. AdaViG dynamically evaluates each triggered visual step at an early visual generation stage and aborts it when both signals are weak, thereby preventing misleading visual evidence from entering the reasoning trace while avoiding unnecessary computation. Comprehensive experiments demonstrate that AdaViG improves accuracy by up to 5.7% while reducing visual generation FLOPs by 25.0%-91.0% and wall-clock latency by 15.4%-45.6%.

---


### 31. [MLPs are Hebbians: Constructing Efficient Fact-Storing MLPs for Transformers](https://arxiv.org/abs/2607.10034)

**<font color=#1a73e8>作者：</font>** Roberto Garcia, Jerry Liu, Ronny Junkins 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) store factual knowledge in their parameters. While recent work has shown that this knowledge resides in MLP layers, existing constructive and mechanistic interpretability models of fact-storage in LLMs fail to explain the surprising empirical phenomenon that they store facts at an information-theoretically optimal rate. In this work, we develop a theoretical account of this phenomenon. We develop the first Transformer-compatible fact-storing MLP closed-form construction that satisfies the following three properties empirically observed in LLMs: it (i) attains optimal fact storage scaling, (ii) handles arbitrary input/output geometries, and (iii) works inside Transformers. Key to our work is to analyze the decoding margin of MLPs, whereas prior work only studies MLP fact storage. Under isotropic embeddings, our construction achieves information-theoretically optimal storage capacity scaling and requires $10$-$104\times$ fewer parameters at matched fact count than prior constructions. For arbitrary key and value embeddings, we show that our construction attains the same storage capacity scaling, up to penalization factors depending on the embedding geometries. Moreover, we demonstrate that our constructed MLPs can be used within Transformer blocks for factual recall tasks at optimal capacity scaling, requiring $15$-$63\times$ fewer parameters at matched fact count than prior constructions. Finally, as a proof-of-concept, we show that fact-storing MLPs enable modular fact editing by swapping a Transformer's MLP with a new one.

---


### 32. [AgentAbstain: Do LLM Agents Know When Not to Act?](https://arxiv.org/abs/2607.10059)

**<font color=#1a73e8>作者：</font>** Xun Liu, Yi Evie Zhang, Vira Kasprova 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent systems based on large language models (LLMs) are increasingly deployed for autonomous tasks, yet existing evaluations mostly focus on task success rather than whether agents know when to abstain. This gap poses real risks: under ambiguity, conflicting constraints, or tool failures, agents may execute unintended and irreversible actions. To close this gap, we present the first systematic evaluation framework for agentic abstention: the calibrated ability of tool-using LLM agents to recognize when not to act. At its core, AgentAbstain is a paired-task benchmark built on an agent-native taxonomy of 8 abstention scenarios across pre-execution reasoning and runtime discovery. It contains 263 paired tasks across 42 executable sandbox environments, where each pair consists of a should-act task and a should-abstain variant produced through a controlled perturbation to the instruction, tool, or environment state. To scale this paired design and resist data contamination, we propose AbstainGen, a fully automated pipeline that synthesizes sandbox environments and generates paired tasks end-to-end, validated by deterministic replay and semantic LLM judges; fresh task instances can be regenerated on demand, and three independent annotators rate 94-98% of sampled tasks as well-designed. Across 17 frontier LLMs in 4 agent harnesses, the best agent (Gemini 3.1 Pro) achieves only 59.5% paired accuracy (correct on both the act and abstain sides of each paired task). More importantly, abstention capability is largely independent of general task-solving capability, indicating that scaling task-solving alone will not close this gap. We further identify failure modes such as post-hoc abstention, in which agents execute irreversible actions before recognizing abstention triggers. Our code and dataset are open-sourced at this http URL.

---


### 33. [MAG: A Web-Agent Benchmark and Harness for Multimodal Action and Guide Generation](https://arxiv.org/abs/2607.10079)

**<font color=#1a73e8>作者：</font>** Chengguang Gan, Hanjun Wei, Yunhao Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Digital Adoption Platforms (DAPs) are embedded overlays widely used on web systems to guide users through operations inside a page, helping them get started with unfamiliar interfaces quickly. Completing a real task, however, rarely means clicking a few buttons on a single page: it takes a sequence of actions that unfolds across changing page states. Prior studies have also treated automated web agent actions and guide text generation as two separate problems, and most of them feed models textual page representations such as the DOM or accessibility trees rather than the rendered screens that humans actually operate on. In this work we introduce MAG, the first benchmark that unifies task execution and guide writing into a single Multimodal Action and Guide task, with two grounding schemes over screenshots: Set-of-Mark element selection and raw pixel coordinates. We further build a complete harness for this compound task, covering annotation with LLM assistance and human verification, training, evaluation in live environments, and joint metrics for actions and guides. With this harness we evaluate frontier API models and open multimodal models, and report detailed analyses. Finally, we design a GRPO training method augmented with expert trajectories, which nearly doubles the success rate of a supervised 9B agent (from 6.9% to 13.2%) and improves guide quality at the same time. Even the strongest model completes fewer than 40% of the tasks, leaving ample room for future research.

---


### 34. [Efficiently Adapting Spoken Language Models for the Singaporean Context](https://arxiv.org/abs/2607.10092)

**<font color=#1a73e8>作者：</font>** Ng Jia Sheng Jason  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Spoken language models (SLMs) unify speech perception and reasoning, but adapting them to sensitive domains is underexplored, especially when the original training data is inaccessible and the use case demands multilingual, spoken-query interaction. We adapt an open-source SLM to the Singaporean Home Team context across five speech tasks in Singapore's four official languages, combining LoRA fine-tuning, a surrogate text-QA dataset that guards against catastrophic forgetting, and a multi-task objective that adapts the CoBa reweighting scheme to speech. We also build HTD-multilingual-QA, a 504,853 sample multilingual QA dataset in text and spoken form. The resulting HT-Moonstone (5B) matches or outperforms SLMs up to 7x its size on most tasks, attains the best accent and gender recognition among all models evaluated, and loses under 2\% of its original speech QA ability.

---


### 35. [Looped State-Space Language Models with Adaptive Exit-State Selection](https://arxiv.org/abs/2607.10110)

**<font color=#1a73e8>作者：</font>** Zhenxuan Yu, Takeshi Kojima, Yutaka Matsuo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work on looped language models suggests that many reasoning problems benefit from greater computational depth rather than from additional independent parameters. Existing studies, however, focus almost exclusively on Transformer backbones, leaving open whether this principle also applies to state-space language models. We investigate Looped Mamba and Looped Hybrid Mamba-Transformer architectures, which repeatedly apply a shared Mamba (or hybrid) block to introduce explicit finite-depth recurrent computation. On two controlled reasoning tasks-Mano (modular-arithmetic manipulation) and p-hop induction-Looped Mamba consistently outperforms parameter-matched non-looped baselines and, in several settings, matches or exceeds non-looped models of equal effective depth. We then extend the study to language model pre-training under matched iso-parameter and iso-FLOPs protocols, which jointly disentangle the effects of parameter sharing and effective depth: looped models remain competitive on downstream benchmarks with substantially fewer distinct parameters, although deeper non-looped models retain an advantage in validation perplexity under strict iso-FLOPs comparisons. Finally, we adapt Ouro's two-stage exit gate to Looped Mamba for threshold-controlled selection among recurrent-step outputs. Since all recurrent steps are still executed, the selected exit step represents prediction depth rather than reduced wall-clock computation. At the scales studied, adaptive exit-state selection improves downstream performance at intermediate depths, while actual inference-time savings require additional state-handling mechanisms.

---


### 36. [GAE: Graph-Augmented Evolution for Scientific Discovery via Reinforcement Optimization](https://arxiv.org/abs/2607.10127)

**<font color=#1a73e8>作者：</font>** Xuanzhou Chen, Taoli Cheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evolutionary program search guided by Large Language Models (LLMs) has emerged as a powerful paradigm for automated scientific discovery. However, current approaches are fundamentally constrained by three bottlenecks: structurally blind parent selection, sparse whole-program evaluation rewards, and static mutation operators that fail to adapt during search. We present GAE (Graph-Augmented Evolution), a framework that resolves these limitations through a tightly coupled, three-pillar architecture. First, a relational graph neural network (GNN) parses programs into typed computation graphs, producing structure-aware embeddings. Second, an RL-optimized meta-controller leverages these embeddings to replace blind evolutionary sampling with a directed policy, dynamically selecting optimal parents and mutation directions based on reward history. Third, an online GRPO fine-tuning loop continuously updates the LLM mutation operator at test-time using group-normalized evaluation rewards, directly aligning the model's generation distribution with high-fitness structural edits. We evaluate GAE on a challenging scientific discovery task: symbolic regression for complex nonlinear oscillator systems. By transforming stochastic search into a directed, self-improving trajectory, GAE efficiently discovers closed-form physical equations, consistently matching or outperforming static LLM-driven baselines and achieving state-of-the-art out-of-distribution performance.

---


### 37. [TextGaze: Prompting Gaze Target Estimation with Textual Scene Cues](https://arxiv.org/abs/2607.10130)

**<font color=#1a73e8>作者：</font>** Junhui She, Fei Wang, Kun Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaze target estimation aims to infer the position of a person's gaze within a scene. Within mainstream design logic, multi-branch methods require extra supervision and annotations, while streamlined designs prioritize low-level visual saliency over true gaze intent. The former leads to a high annotation burden and hinders domain transfer, whereas the latter causes misalignment between predicted attention and actual gaze targets. To address this issue, we propose TextGaze, a unified cross-modal architecture that leverages a Large Vision-Language Model (LVLM) as scalable semantic guidance to balance the two design paradigms. The model extracts visual features from a frozen encoder and utilizes an LVLM to obtain gaze-aligned textual cues. We design a transformer-based fusion module with hierarchical text supervision to preserve task semantics. Lightweight decoding heads enable the joint prediction of gaze heatmaps and in-/out-of-frame status. We evaluate our method on four mainstream datasets, and the results show competitive performance across key metrics with robust cross-dataset generalisation without extra fine-tuning. Overall, we provide a streamlined alternative to traditional designs and highlight the potential of LVLMs as accessible auxiliary guidance for gaze estimation.

---


### 38. [LeRoPE: Learnable RoPE Frequencies Improve Language Modeling](https://arxiv.org/abs/2607.10134)

**<font color=#1a73e8>作者：</font>** Petros Karypis, Sean O'Brien, Shreyas Kadekodi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rotary Positional Encodings (RoPE) are currently the most popular positional encodings used in modern language models. RoPE rotates two-dimensional chunks of query and key vectors, operating as a function of their relative positional offset. The position-wise rates of rotation in RoPE typically follow a geometric sequence specified by a fixed base-frequency hyperparameter. Prior work has improved performance by either increasing this parameter to slow rotation or by applying RoPE to only a subset of QK dimensions. In this work we modify RoPE by learning a scalar per frequency, treating frequencies as learnable parameters rather than hyperparameters. We validate Learned RoPE by training a ladder of language models from scratch, ranging from 52M to 2.5B parameters. We observe and analyze the emergence of a high-norm, positional LeRoPE band. LeRoPE consistently outperforms RoPE and partial RoPE across all scales, with RoPE requiring 3.4% more compute (FLOPs) to match LeRoPE at the largest scale.

---


### 39. [RDQ: Residual Distribution Quantization for Large Language Models](https://arxiv.org/abs/2607.10137)

**<font color=#1a73e8>作者：</font>** Prateek Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) of large language models degrades sharply below 4-bit precision. We identify the root cause as residual stream distributional drift: quantization noise injected at each transformer layer accumulates in the shared residual representation, causing KL divergence from the FP16 baseline to grow super-linearly with depth (Pearson r=0.999 with log-perplexity, p<0.001, confirmed across all tested methods and bit-widths). We discover that 84% of LLaMA-3-8B layers exhibit non-Gaussian residual distributions (KS test, p<=0.05), and that per-layer residual stream variance grows 6,548x across depth. We propose RDQ (Residual Distribution Quantization), a PTQ framework whose central contribution is Cascaded Error Compensation (CEC): a sequential calibration procedure that captures the actual drifted activations each layer receives (computed by running calibration data through already-quantized upstream layers) and fits per-channel AWQ-style scales against those drifted inputs, with scales folded into preceding RMSNorm weights for exact mathematical equivalence at zero inference overhead. RDQ achieves state-of-the-art results on all three tested architectures: LLaMA-3-8B: 7.55 / 5.62 PPL (W3/W4); Qwen-2.5-7B: 7.46 / 6.38 PPL; Mistral-7B: 6.88 / 5.73 PPL. RDQ beats the best published baseline (LeanQuant/SpinQuant) at every model and bit-width combination, with gains up to -46.4% vs. RTN at W3A16 on LLaMA-3-8B. All output is standard group-128 asymmetric quantization, deployable on Qualcomm AIMET, GGUF, and any standard inference stack at zero runtime overhead.

---


### 40. [LLMs as a Jury: Cross-Model Consensus Can Outperform Process Reward Models for LLM Reasoning](https://arxiv.org/abs/2607.10139)

**<font color=#1a73e8>作者：</font>** Ning Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selecting the correct answer from a pool of candidate reasoning chains is the engine of test-time scaling, yet the standard selectors each carry a cost: self-consistency inherits the errors of the single model it resamples, and trained reward models need labeled data and transfer poorly off-distribution. We study a third signal, free at inference time: cross-model consensus, the degree to which independently trained models, each solving the problem once, agree on a final answer. We treat the panel as an LLM-jury, in which the structure of agreement, not any model's score of another, is the verification signal. Across seven benchmarks it selects correct answers better than self-consistency and far better than a model scoring its own candidates: on competition math it closes the entire gap to an oracle selector, while self-scoring closes almost none. The mechanism is error decorrelation: independently trained models err differently, so their wrong answers scatter while the correct one accumulates agreement. We make this precise with a parameter-free law, derived in closed form, that predicts consensus accuracy from three measured panel statistics to a mean absolute error of $0.03$ and exposes the method's ceiling: a shared-error floor where models share a misconception, near zero on math but non-trivial on science. Against four trained verifiers spanning discriminative, outcome, and generative reward models, the free LLM-jury matches the strongest inside their math training domain and is the top selector outside it. Cross-model consensus is thus a verifier we can characterize in advance: a law that says when to trust it, and a floor that marks where it cannot.

---


### 41. [UNIT: Unleash Large Language Models Potential for Graph Continual Learning](https://arxiv.org/abs/2607.10159)

**<font color=#1a73e8>作者：</font>** Tairan Huang, Yili Wang, Beibei Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In real-world multimodal web scenarios, graph-structured data often arrives in a streaming manner, making graph continual learning a crucial paradigm for continuously modeling such evolving structures. However, existing graph continual learning methods still face two fundamental challenges. 1) semantic-structural separation, where the graph-based methods excel at modeling topological relationships but neglect deep semantics. 2) imbalanced knowledge transfer, where existing models fail to effectively leverage general knowledge gained from early tasks to benefit subsequent new tasks. To address above issues, we propose a novel framework, \textbf{UN}leash Large Language Models PotentIal for Graph ConTinual Learning (UNIT). By fine-tuning large language model only on the first task, we bridge the distributional gap between the pre-trained LLM corpus and the target task dataset to enhance the adaptability of LLMs for graph-structured tasks. Meanwhile, we propose an uncertain-aware anchor generation mechanism to effectively preserve representative knowledge across tasks, avoiding the neglect of universal knowledge learned from previous tasks. Additionally, we introduce structural confluence modeling to explicitly integrates graph topology information into semantic information, enhancing the collaborative capabilities between semantic understanding and structural modeling. Extensive experiments demonstrate that our proposed method achieves state-of-the-art performance in the graph continual learning task.

---


### 42. [Beyond Euclidean Clipping: Overcoming Exploration Collapse in LLM RL via Riemannian Isometric Policy Optimization](https://arxiv.org/abs/2607.10169)

**<font color=#1a73e8>作者：</font>** Zhicheng Cai, Xinyuan Guo, Hanlin Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a dominant paradigm for enhancing LLMs' reasoning capabilities. However, RL algorithms with PPO-Clip are inherently limited by exploration collapse. Subsequent works remain primarily heuristic and fail to identify the essential cause of PPO-Clip's failure. This work reveals the fundamental flaw of PPO-Clip: it implicitly measures policy discrepancy using Euclidean metric, which is theoretically inconsistent with the intrinsic geometry on the policy Riemannian manifold. This geometric mismatch results in overly conservative updates in low-probability regions while aggressive in high-probability regions, ultimately collapsing exploration. To correct this geometric flaw, we propose Riemannian Isometric Policy Optimization (RIPO), which guarantees isometric policy updates on the Riemannian manifold, effectively balancing exploration and exploitation. We further show that RIPO achieves a favorable bias-variance trade-off, which stabilizes optimization. Extensive experiments demonstrate that RIPO significantly surpasses existing LLM RL algorithms across seven competition-level benchmarks (up to 60% improvement over GRPO on AIME24).

---


### 43. [Knowledge-Conditioned, Single-Pass LLM Synthesis of Executable Unity Game Scenes: A Compiler Error Census across 26 Goal Playable Concepts](https://arxiv.org/abs/2607.10187)

**<font color=#1a73e8>作者：</font>** Hugh Xuechen Liu, Kıvanç Tatar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) write Unity C\# for game scenes. Yet nearly all demonstrations rest on an iterative repair loop that regenerates code until it compiles, conflating what the model writes with what the loop fixes. We remove the loop and evaluate a single pass, where the first draft is final. This isolates the model's parametric knowledge, the most stringent test of unaided generation. Models instantiate Goal Playable Concepts, playable counterparts of goal patterns, across 10,400 generations (four open-weight models, 7B--30B; two generation modes; four intermediate-representation (IR) conditioning levels; 26 goal patterns; 20 seeds). None compiled into a runnable scene, leaving no survivorship bias. To understand how the generated C\# scripts fail, we categorize the 99 error codes behind 90{,}673 compiler-error occurrences as Grounding (invented or misused Unity types and APIs) or Hygiene (structural defects needing no Unity knowledge). The split differs sharply by goal pattern (e.g., Stealth fails mostly on invented engine references; Capture on plain C\# structure). Larger models, stricter IRs, and different generation modes move the errors but never yield a compiling scene. The bottleneck is missing engine-specific knowledge. The census orders goal patterns by that demand, showing designers where single-pass generation breaks.

---


### 44. [GRATE: Temporal Extensions for Inductive KG Foundation Models via Gated Rotary Attention](https://arxiv.org/abs/2607.10197)

**<font color=#1a73e8>作者：</font>** Jiaxin Pan, Osama Mohammed, Daniel Hernández 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge graph foundation models such as Ultra and Trix achieve strong inductive transfer by learning relation-graph representations that generalise to unseen entities and relations. Extending this transferability to temporal knowledge graphs (TKGs) remains challenging: existing temporal models tie their parameters to dataset-specific entities, relations, or timestamps and are not designed to transfer to TKGs with disjoint vocabularies. We propose GRATE (Gated Rotary Attention for Temporal Encoding), an entity-side message function that adds no learnable parameters and encodes time through relative time differences by rotating each edge message according to its time gap to the query and applying a query-conditioned gate to select temporally relevant signals. GRATE integrates into NBFNet-style KG foundation models while preserving structural transferability. Existing TKG benchmarks evaluate within shared train/test vocabularies and cannot directly test cross-dataset temporal transfer; we therefore construct GDELTIndT and WIKIIndT, inductive transfer benchmark suites with disjoint entities, relations, and timestamps spanning both interpolation and extrapolation. Across these benchmarks and held-out forecasting datasets, a single jointly pretrained GRATE checkpoint improves over the static base model in most settings.

---


### 45. [When Does Depth Survive Composition? Compute--Quality Regimes in Latent World Models](https://arxiv.org/abs/2607.10203)

**<font color=#1a73e8>作者：</font>** Achyuthan Sivasankar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive-compute world models -- early-exit or mixture-of-depths predictors that spend variable depth per step -- assume depth buys better predictions and can be routed adaptively. In autoregressive rollouts, the first assumption requires depth's per-step precision to survive composition. We test this with a pre-registered instrument, the shallow penalty $\rho=\mathrm{err}(\text{shallowest-exit rollout})/\mathrm{err}(\text{full-depth rollout})$, across nine DeepMind Control tasks under matched single-step ($K=1$) and multi-step ($K=4$) training, three seeds each. We find three regimes: on 6/9 tasks depth helps rollouts (intrinsic, $\rho$ up to $4.7\times$), on 2/9 the shallow exits beat the full stack (inversion, $\rho$ down to $0.85\times$), and one is flat. The robust inversion (cheetah) is not a property of the dynamics but is created by training: an ablation supervising early exits only at the first rollout step erases it ($\rho: 0.87\to1.18$, $n=8$, $\Delta=+0.31$), while an intrinsic-tradeoff task is unaffected -- a double dissociation we call the routability catch-22, since the supervision that makes exits routable is what trains them to out-roll the full stack. The regime is partly predictable a priori: observation/action dimensionality and one-step model error correlate with $\rho$ at $|\text{Spearman}|\approx0.75$ ($n=9$). Inside a CEM planner, $\rho$'s sign predicts whether planning benefits from depth, most sharply on the inversion task, where shallow planning beats deep. Finally, three cautions: a task's regime depends on the metric space, the rollout horizon, and the encoder. All thresholds and gates were fixed before the compute campaign, including a pre-registered negative for the hypothesis that motivated the study.

---


### 46. [Consensus vs. Dissent: Dynamic LLM Modeling of Subjective Preferences in Group Recommenders](https://arxiv.org/abs/2607.10235)

**<font color=#1a73e8>作者：</font>** Cedric Waterschoot, Nava Tintarev, Francesco Barile  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Previous work in group recommender systems has demonstrated a sensitivity to the distribution of preferences within a group. Specifically, the selection of the preference aggregation strategy benefits from considering such group configurations. In this paper, we study whether LLMs are able to mimic this sensitivity and to select the ideal aggregation strategy (and corresponding recommendation) according to nuanced human perceptions of fairness, satisfaction, and consensus.
We do this by fine-tuning Large Language Models (LLMs) on human survey data to serve as real-time judgmental models within the recommendation pipeline. Using a reasoning dataset distilled from DeepSeek-V3.1 and human ground truth assessments, we develop Judgmental Llama and Judgmental OLMo to simulate group assessments. Our pipeline successfully generates multiple recommendation candidates based on social choice-based aggregation strategies and dynamically selects the one that maximizes these predicted human-like evaluations. We further validate these suggestions in a user study (n=284) and find that our methodology achieved the highest scores for satisfaction and group consensus. Furthermore, we find that LLM judgments are most aligned with human perceptions of fairness, satisfaction and consensus when we also consider interaction effects between our LLM-based method and group configuration (e.g., minority or coalition). These findings give further support for dynamically adapting aggregation strategies to specific within-group preference distributions, and highlight the advantage of using LLMs for an adaptation that is aligned with subjective human judgments.

---


### 47. [What Does Your Short-Answer VQA Score Actually Measure? Evaluator-Dependent Instability in Multimodal Short-Answer Benchmarks](https://arxiv.org/abs/2607.10240)

**<font color=#1a73e8>作者：</font>** Guanhua Ye, Niu Jingbin, Yan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Short-answer VQA benchmarks conflate two distinct quantities: whether a model's answer is semantically correct, and whether that answer matches the surface form expected by the automatic evaluator. We study this conflation across six vision--language models and six benchmarks, using a human-validated semantic judge (97.6% precision) to audit over 37k official errors. A second text-only judge reproduces the same benchmark-level false-negative pattern, showing that the effect is not an artifact of a single audit model. On text-rich benchmarks, up to half of these errors are semantically acceptable answers penalized purely for surface-form mismatch. This instability is structured by answer type: extractive and multi-span answers are far more evaluator-sensitive than scalar answers. Benign prompt and context rewrites further destabilize official outcomes, flipping item-level correctness at substantial rates without changing the underlying task. A deterministic CPU-only contract repair confirms that the undercount is partially recoverable. These findings imply that official short-answer VQA scores should be accompanied by semantic audits and answer-type diagnostics to remain interpretable.

---


### 48. [PTEI: Integrating Personality Traits to Enhance Emotional Intelligence in Large Language Models](https://arxiv.org/abs/2607.10245)

**<font color=#1a73e8>作者：</font>** Amir Reza Jafari, Praboda Rajapaksha, Reza Farahbakhsh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite advances in Emotional Intelligence (EI), Large Language Models (LLMs) still significantly underperform humans in complex emotional reasoning. This gap originates partly from the limited incorporation of individual differences, particularly personality traits, which are fundamental to human emotional inference. To address this, we propose PTEI, a novel framework for integrating Personality Traits into Emotional Intelligence tasks using LLMs. In PTEI, MBTI and OCEAN personality traits are first extracted directly from the given emotional scenarios and then utilized as contextual knowledge within personality-aware prompts, guiding LLMs to accurately infer emotions and their underlying causes. To ensure optimal contextual grounding, we employ Contrastive Learning to construct an optimized retrieval system that surfaces emotionally and personally aligned scenarios, enhancing reasoning quality. Extensive experiments on established EI benchmarks show that PTEI enhances the Emotional Understanding (EU) capabilities of various LLMs, with the strongest improvement observed in GPT models. Combining PTEI with Chain-of-Thought (CoT) reasoning yields an additional 4 percent increase in accuracy. These findings underscore PTEI's contribution toward advancing AI systems with more sophisticated social and psychological grounding.

---


### 49. [One mechanism for many mental spaces: a shared router over a value slot in language models](https://arxiv.org/abs/2607.10248)

**<font color=#1a73e8>作者：</font>** Oliver Steele, Jiangtao Wen, Yuxing Han  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language builds discourse contexts other than the actual: a painting, a belief, a memory, a hypothetical. Each is a mental space in which the same entity can take a different value, as when a flower is red in reality but purple in a portrait. Formal semantics keeps these contexts apart because their logics differ (modal, temporal, doxastic, depictive); Fauconnier's mental-space theory treats them as one space-building operation. We ask which of these a transformer language model implements, and find a mechanistic version of Fauconnier's unification. The model uses one router/slot format across the inventory: a reusable value slot stores attributed content, and a causally manipulable router (the space index) selects which space is read. A subspace trained with Distributed Alignment Search to control one space type, counterfactual, belief, fictional, or temporal, also controls the others, well above a random floor, on three model families; belief, which formal semantics marks as a distinct case, is not specially separated. The router is low-rank, composes additively with entity identity, and acts through a few late-layer heads. Two further results show the mechanism drives inference and composes: a subspace trained on a rule-derived conclusion flips what the model infers while dissociating from what it reports, and composing space-builders mints a fresh router over the shared slot. This paper establishes the cross-type generality. A companion paper develops belief in depth, because of its special status in philosophy, psychology, and linguistics (epistemology, theory of mind, and propositional attitude reports).

---


### 50. [Behavioural Signatures of Risk-Sensitive Decision-Making in Large Language Models](https://arxiv.org/abs/2607.10251)

**<font color=#1a73e8>作者：</font>** Xuankun Rong, Wenke Huang, Bo Du 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly used in decision support, it is important to understand whether their choices under uncertainty exhibit stable and interpretable behavioural regularities. Human decision-making combines relatively persistent risk preferences with context-dependent adjustment, yet it remains unclear whether analogous behavioural structure can be observed in LLM-based decision systems. Here we examine this question using a controlled multi-model framework based on no-limit Texas Hold'em, where behaviour is quantified by Participation, measuring voluntary engagement in uncertain opportunities, and Proactiveness, measuring pre-flop risk escalation. Across homogeneous self-play and heterogeneous mixed-model interactions, frontier LLMs exhibit stable, model-specific risk profiles, forming a spectrum from conservative to aggressive decision styles. These profiles remain largely robust under changing opponent composition, while the most conservative and most aggressive models diverge further in mixed settings. Under global risk pressure and personal resource constraint, models adapt in structured but heterogeneous ways, ranging from broad behavioural contraction to selective de-escalation and near-invariant behaviour. These findings suggest that LLMs differ not only in baseline risk disposition, but also in the risk signals they respond to and the flexibility with which they adjust, providing a behavioural basis for auditing risk-sensitive decision-making in interactive settings. Our code is publicly available at: this https URL.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-199](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
