# 🧠 大模型相关研究 | 2026年08月28日

> 本类共 **209** 篇论文：已确认 **195** 篇，待复核 **14** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-209](./part-05.md)

---

### 51. [GRAPE: Gradient Refinement and Progress-Aware Exploitation for Query-Efficient High-Dimensional Bayesian Optimization](https://arxiv.org/abs/2608.25116)

**<font color=#1a73e8>作者：</font>** Richard Cornelius Suwandi, Feng Yin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimizing expensive, high-dimensional black-box functions remains a central challenge in modern machine learning and scientific discovery. While local Bayesian optimization mitigates the curse of dimensionality, existing techniques often prioritize the probability of descent over the magnitude of progress. This leads to overly conservative steps that yield negligible improvement, wasting queries on directions that are nearly certain to descend but offer little decrease. We introduce Gradient Refinement and Progress-Aware Exploitation (GRAPE), a two-stage framework that first sharpens the local gradient posterior via a closed-form acquisition function, then selects update directions by maximizing the expected decrease conditional on descent. Theoretical analysis proves that this gradient refinement stage monotonically minimizes local uncertainty and that the progress-aware direction converges to true steepest descent as the posterior sharpens. Empirically, GRAPE demonstrates superior query efficiency across high-dimensional tasks: in black-box adversarial attacks, it achieves an average 5.4$\times$ speedup over baselines, and on large language model prompt optimization tasks, it outperforms the second best method by a reduction of 3.8 log-units in the final average regret.

---


### 52. [SelfGraphRAG: Bridging the Supervision Gap in Graph-Based RAG with Synthetic QA Generation](https://arxiv.org/abs/2608.25123)

**<font color=#1a73e8>作者：</font>** Ben Lagnese, Manas Gaur  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) improves large language models by incorporating external knowledge without retraining, but existing methods often underuse the relational structure encoded in knowledge graphs. Graph-based RAG can capture entity relationships, yet supervised graph retrieval typically requires labeled question-answer data that may not be available for newly constructed graphs. We address this limitation with SelfGraphRAG, a framework that generates question-answer pairs directly from knowledge graph structure and uses them to train a query-conditioned graph retriever. The generated questions capture multi-hop paths and local neighborhoods, providing relational supervision without manual annotation. Experiments on multi-hop question answering and classification benchmarks show that SelfGraphRAG improves retrieval precision and downstream reasoning performance over embedding-based baselines. These results suggest that knowledge graph structure can provide useful supervision for training graph retrievers when labeled data are unavailable.

---


### 53. [RefLAM: A Reference-Grounded Line Annotation Pipeline for Historical Arabic Manuscripts](https://arxiv.org/abs/2608.25140)

**<font color=#1a73e8>作者：</font>** Mohamed Guechaoui, Mohamed Diaa Zellagui, Souleyman Chaib 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing approaches to building line-level Arabic handwritten-text-recognition (HTR) training data either rely on fully manual annotation, which does not scale, or on automatic OCR-to-reference alignment methods not yet extended to multi-script, two-zone (main-plus-margin) manuscript layouts with a provable correctness guarantee. We present RefLAM (Reference-grounded Line Annotation for Manuscripts), a pipeline converting manuscript page images and clean transcriptions into validated, line-level ground truth without sacrificing human oversight. RefLAM couples a deep-learning page-segmentation model with a multimodal large language model (MLLM) for structured OCR and a diacritic-agnostic fuzzy alignment engine that grounds each OCR line in a contiguous span of the reference text, with a character-level confidence score in $[0,100]$. A perfect score is provably equivalent to character-for-character identity of the normalised strings (the Confidence-100 rule), verified with no counterexample across the released corpus. A reviewer can thus trust a perfect score, confirming most lines at a glance rather than retyping them, so annotation becomes triaged, with attention concentrated on uncertain alignments. Across 7 fully page-validated books we measured a 75$\times$ throughput gain over manual annotation (3,000 vs. 40 lines/hr); applying the same guarantee to 7 further books, we retained 16,533 confidence-100 main-text lines within one week, excluding sub-100 lines rather than manually correcting them. Using RefLAM, we release AraMS-28k: 14 historical Arabic manuscript books, 3,043 pages, and 27,971 main-text and 629 margin-line annotations with bounding boxes, layout labels, and insertion anchors for 191 margin entries (30.4%). We also finetune Muharaf-pretrained baselines (including HATFormer) on AraMS-28k and report CER results confirming its practical utility for downstream HTR training.

---


### 54. [Belief Cascades Drive Persuasion in LLM Agent Networks](https://arxiv.org/abs/2608.25152)

**<font color=#1a73e8>作者：</font>** Haoyi Qiu, Genglin Liu, Pranav Narayanan Venkit 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems increasingly debate answers, coordinate research, simulate users, and mediate information flows, making agent-to-agent persuasion a basic but undermeasured capability. We introduce a controlled testbed for studying how goal-directed persuaders shift elicited stances in networks of LLM agents grounded in real-world ego-network topologies. Across four LLM backbones, five graphs, and 55 policy statements, we find that persuasion dynamics depend on the interaction between topology, competition, topic, and model prior. Additionally, we show that direct exposure reliably predicts next-round stance change in competing runs, and peer relays carry smaller but measurable influence, showing that agents not assigned to persuade can still transmit persuasive force. Finally, analyzing post text alone misses important movement: planned strategies are only partly realized in executed messages, action choices can diverge from message content, and persuadees rarely state the stance shifts detected by probes. These results argue for evaluating multi-agent persuasion as a trajectory- and exposure-level process, using belief probes, exposure provenance, and action logs to identify who influenced whom and whether visible language reflects underlying stance movement.

---


### 55. [FuzzingBrain-Bench V1: Evaluating Open-Ended Bug Discovery by LLMs](https://arxiv.org/abs/2608.25158)

**<font color=#1a73e8>作者：</font>** Ze Sheng, Aleksandar Kezic, Zhicheng Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating the ability of large language models (LLMs) to discover software bugs is increasingly important. Existing benchmarks typically evaluate this capability by asking the model to generate a proof-of-concept input that triggers a predefined target vulnerability. However, this setup may overlook valid crashes discovered by the model when they do not match the predefined target. As a result, the evaluation may not reflect the model's real capability.
We present FuzzingBrain-Bench, a benchmark for assessing AI models' ability to discover bugs in open-source software. Models are given an open-source project and a sanitizer-instrumented harness in a self-contained Docker image. Their goal is to generate inputs that trigger as many distinct crashes as possible through the harness. A model's performance on each challenge is scored based on the number of distinct crash signatures it produces, capped at a predefined maximum and weighted by a difficulty coefficient.
FuzzingBrain-Bench V1 consists of 77 challenges drawn from 43 open-source projects, with 36 C, 32 C++, and 9 Java/JVM challenges. We evaluate Claude Haiku 4.5, Claude Sonnet 4.6, and Claude Opus 4.8 on the full benchmark. Claude Opus 4.8 performs best, triggering crashes in 60 of 77 challenges and achieving a score of 196 out of 579. None of the three models triggers a crash in 13 challenges. The FuzzingBrain-Bench corpus and harnesses are publicly available at this https URL.

---


### 56. [The Changing Geometry of Grammar: Dimensionality and Neighborhood Reorganization across Transformer Layers](https://arxiv.org/abs/2608.25166)

**<font color=#1a73e8>作者：</font>** Samuele Vallisa, Federico Ravenda, Claudio Palominos 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer representations describe trajectories through high-dimensional vector spaces, which are shaped dynamically as tokens incorporate relational context across layers. Such data tend to concentrate on lower-dimensional sub-manifolds, a form of compression quantified by the Intrinsic Dimensionality (ID), the minimum number of independent variables needed to represent them without significant information loss. In this work, we ask whether the grammatical role of tokens, as marked by their part-of-speech (PoS) tag, shapes the local geometry of this manifold. To this end: (1) We investigate the layer-wise evolution of ID, finding that closed-class items expand earlier and collapse sooner than open-class ones; (2) We show its expansion and contraction to be explained by changes in the neighborhood structure, and hence in the relations between words within a sentence; (3) We compare encoders (ModernBERT, bigbird-roberta-large) and decoders (gemma-2-2B, Llama-3.2-3B), finding that the two families evolve differently across layers, consistently with how each integrates context;(4) We show that geometric features alone recover a token's grammatical role, and use them to interpret how the semantic content of each PoS evolves across layers in a downstream classification task.

---


### 57. [Transforms for LLM Quantization: The Great Inversion and Format Co-Design](https://arxiv.org/abs/2608.25188)

**<font color=#1a73e8>作者：</font>** Ehsan Jokar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most competitive 4-bit LLM research pipelines now open the same way: apply a linear, function-preserving transform (rotation, scaling, permutation, non-orthogonal affine) so the outlier mass sits more favorably against the group scales, and only then round. Yet we are aware of no survey dedicated to this transform stage, and its literature is quietly re-deriving an older theory. We identify and formalize the principle that organizes it, the Great Inversion: allocation-flexible coding rewards energy concentration, whereas the grouped shared-scale quantization a deployed matrix instruction performs rewards within-group flattening. Classical transform coding (1963: decorrelate, allocate bits, quantize) spends different bits per coordinate at a fixed total rate; for a Gaussian source at high rate the Karhunen-Loeve transform's concentration minimizes distortion. A deployed operand tile instead carries one absolute-maximum scale per group and equal bits everywhere, with no allocation; on a uniform grid that objective rewards flattening, approached by Hadamard incoherence. We prove that opposition under within-group majorization: the prescriptions point in opposite directions, each backed by a proof against its own objective, and for a generic spectrum no optimality guarantee transfers. A second axis is the number format: the non-uniform FP4 grid makes flattening buy less, MXFP4's power-of-two block scale still rewards a rotation confined to that block, and NVFP4's mantissa-carrying scale largely removes that pull, so the target pole depends jointly on allocation regime and format. We survey 200 works to a June 2026 cutoff; classify 43 transform methods by structure, data-awareness, searched-versus-constructed, and runtime cost; record, where reported, how they compose with GPTQ rounding; distill a first-choice guide by deployment regime; and close with the open problems it exposes.

---


### 58. [What Should a Large Language Model See? Physical Invariants as a Data Representation for PDE Discovery](https://arxiv.org/abs/2608.25189)

**<font color=#1a73e8>作者：</font>** Fan Yang, Matt Thomson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how molecular interactions govern macroscopic behaviour is a central challenge in molecular sciences. However, conventional theory building cannot keep pace with the vast datasets modern experimentation routinely produces. Large language models offer a promising route to automating theory construction, but a spatiotemporal field cannot be directly placed in a prompt. Existing models generally learn about the data only through a score measuring how well each proposal fits it. Here we introduce data interpretation, a stage that measures the field into the quantities a theorist would consult and supplies them to the model as a direct input. On a benchmark of simulated fields, interpretation nearly triples the accuracy of recovered equations relative to showing the raw data, at negligible computational cost and without any training. By allowing a language model to read field data as a theorist does, data interpretation offers a practical route to automated field theory construction that can coevolve with experimentation.

---


### 59. [Tunable Tool-Call Rates in LLM Agents via Representation Steering](https://arxiv.org/abs/2608.25198)

**<font color=#1a73e8>作者：</font>** Yuqi Chen, Vincent Siu, Yang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deciding whether to call a tool is a core competence of an LLM agent, and a costly one to get wrong: needless calls add latency, accrue cost, and may trigger irreversible side effects, while missing calls leave the model confidently wrong on questions it could only answer through tool-calls. Models manage this balance poorly, both over-using and under-using tools. Existing methods such as post-training and prompt engineering are expensive and difficult to modify at inference time. We show that whether an instruction-tuned model calls a tool can be controlled by a single linear direction in its residual stream, extracted without any training from the model's own tool-use preference signal and turned into an inference-time intervention with no prompt change. Adding the direction with strength $\alpha$ moves the call rate monotonically from near $0\% $ to over $90\%$ while keeping calls well-formed. The steering works in both directions: dialing it down suppresses calls, and dialing it up induces new calls that land precisely on the questions the model cannot answer from its own knowledge. We also show that the direction generalizes to unseen tools with strength comparable to each tool's own direction and without favoring any specific tool choice. With live tool execution, a single sweep of the steering traces a cost/accuracy Pareto frontier and nearly doubles open-domain QA accuracy ($0.29 \! \rightarrow \! 0.56$); the same recipe transfers across a diverse range of models spanning dense, MoE, and multimodal architectures, without any training. Our code is publicly available at this https URL.

---


### 60. [Learning Mixtures of Plackett-Luce Models for Multi-Objective Alignment](https://arxiv.org/abs/2608.25200)

**<font color=#1a73e8>作者：</font>** Dongyue Li, Ziniu Zhang, Lu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the problem of learning a mixture of $k$ Plackett-Luce models given multi-way ranking responses from annotators that may represent heterogeneous underlying preferences. This problem has many applications in AI alignment and preference optimization. Prior work has studied mixtures of Bradley-Terry models from pairwise comparisons. However, uncovering mixture models is theoretically unidentifiable when $k$ exceeds $m/2$, where $m$ is the length of a ranking. We propose an efficient implementation to address this limitation, which involves first augmenting the rankings to a larger size by generating new responses from a base language model, followed by a gradient-based estimation to reduce inference cost in the input embedding space. Based on this procedure, we then design an expectation-maximization algorithm with these two steps to fit a mixture of Plackett-Luce models, called MoPLEx. Extensive experiments are conducted to verify this approach. First, we show that the gradient-based approximation estimates true probabilities with less than 5% error on models with up to 34 billion parameters. Second, we show that MoPLEx improves clustering and ranking accuracy by an average of 43.7% and 15.2% over baselines using single ranking and mixtures of Bradley-Terry models, on preference optimization datasets. These results demonstrate the effectiveness of MoPLEx for tackling multi-way rankings from heterogeneous preferences through measuring alignment between gradients.

---


### 61. [Federation Is Nearly Free, Reasoning Is Not: Tradeoffs for AI Co-Scientists in Protein Characterization Workflows](https://arxiv.org/abs/2608.25215)

**<font color=#1a73e8>作者：</font>** Maia Kapur, Timothy Boe, Abby Jerger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural language driven autonomous co-scientist workflows involve a fundamental trade-off between flexibility and reasoning at the expense of determinism, reproducibility, and observability. Such agents increasingly must communicate across institutional boundaries, where federation topology can shape latency and cost. We systematically evaluated these tradeoffs using a controlled ablation on a production agentic platform for science. We use a verifiable task: given a protein sequence, we ask an agent to confidently characterize its function by routing across common tools. We compare federation topology, classic RL vs LLM-driven harnesses, language model, and prompt expertise. We also stratify results by protein novelty. We find that the choice of LLM dominated prediction quality far more than topology or prompting (Opus ~92%-94% vs o4-mini ~40%-50%). The PPO policy was nearly as accurate as the best LLM (88%) at zero token cost, fastest latency, and perfect consistency, but yields no reasoning trace. Expert prompted LLMs reached the highest accuracy but were high-cost and less consistent; prompt dependence was largest when the task was hardest. Federation imposed a negligible penalty on performance. These results offer actionable guidance for deploying agents for scientific workflows: for routine, verifiable tasks, a cheap deterministic policy delivers near-frontier accuracy with complete reproducibility, while flexible LLM reasoning is best reserved for open-ended discovery.

---


### 62. [LLM-Driven, Datasheet-Aware Automated Hardware Compatibility Verification for Early-Stage, Pre-Schematic Embedded System Design](https://arxiv.org/abs/2608.25217)

**<font color=#1a73e8>作者：</font>** Haotian Qiao, Robert P. Dick  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present an LLM-driven, datasheet-aware framework for early-stage hardware compatibility verification that identifies documentation-level interface incompatibilities based on hardware datasheets and high-level component connectivity descriptions. It does not require, and can therefore be used, before detailed schematic simulation and implementation. We view trustworthy LLM-assisted design automation not as directly generating answers from documents, but as transforming engineering information through traceable verification stages. Given hardware datasheets and high-level component connectivity descriptions, the framework constructs a design graph that captures device connectivity and shared interaction domains, retrieves only the engineering properties required by explicit, domain-oriented verification criteria , and generates deterministic scripts for compatibility evaluation. By decomposing compatibility analysis into modular stages and preserving intermediate results, the framework reduces context overhead, improves transparency and tractability, enables scaling, and avoids reliance on LLMs for numerical computation. Evaluated on seven embedded-system designs comprising 34 datasheets, our framework achieves 97.5% compatibility-verification accuracy and an 8.6 times reduction in input context size compared with ``upload-and-query'' workflows. These results demonstrate the feasibility of LLM-assisted, specification-based hardware compatibility verification at an early design stage, as well as the need for, and substantial benefits of, modular task decomposition, formalized verification criteria, and task-aware compact context construction.

---


### 63. [FLARE: Verifying MILP Reformulations with LLM-Based Theorem Proving](https://arxiv.org/abs/2608.25220)

**<font color=#1a73e8>作者：</font>** Henry Robbins, Connor Lawless, Madeleine Udell 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixed-Integer Linear Programming (MILP) is a fundamental tool for combinatorial optimization with extensive real-world applications. A central challenge is designing computationally efficient MILP formulations. Large Language Models (LLMs) offer new opportunities to automate the modeling process, from deriving formulations to strengthening them. Reliable automation requires robust methods for verifying that proposed formulations preserve the underlying optimization problem. However, existing approaches evaluate formulations numerically and fail to reason about general problem instances. We resolve this limitation by introducing a constructive definition of MILP reformulation that can be formalized in Lean and machine-checked. We develop FLARE (Formulation-Level Automated Reformulation Evaluation), a method that uses an LLM-based agent and the Lean proof assistant to verify proposed reformulations against a reference formulation. To evaluate our approach, we introduce FormulationBench, a challenging dataset of 20 problems and 109 formulations. FLARE outperforms existing methods, with 100% accuracy on the NP-hard subset of FormulationBench. Furthermore, FLARE produces a machine-checkable certificate for every reformulation it accepts. For cases where formal guarantees are not necessary, we introduce FLARE-NL, a fast and cheap LLM proxy that matches FLARE's accuracy but produces no certificate. These methods enable reliable verification in automated optimization modeling.

---


### 64. [Trust the Mass: Forced Weights in KV-Cache Eviction](https://arxiv.org/abs/2608.25230)

**<font color=#1a73e8>作者：</font>** Jack Shi, Jerry Gu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Every deployed sparse-attention or KV-cache-eviction rule keeps a subset of the keys, discards the rest, and renormalizes the attention weights over the kept set. Enumerating the exact best subset under that constraint on $168{,}192$ attention rows from five models shows that keeping the largest weights is already near-optimal, since the best subset closes only a median $2$ to $5\%$ of the remaining gap to full attention. If selection closes this little, published margins between eviction methods must come from elsewhere, so we measure the bytes each method holds. In the shared evaluation pipeline, the strongest query-agnostic methods hold the full cache because their per-head selections are stored as masks, and only ragged per-head storage frees that memory. Enforcing a nominal budget on one fixed selection costs $14$ to $62$ benchmark points. We trace an $87.6$-point retrieval margin to rankings computed while the question is visible. ContourKV, a training-free allocator built from the dropped-mass statistic, wins $93$ of $160$ paired comparisons against that state of the art and loses $22$ at the byte count of the budget-enforcing baselines, and it ties the strongest of them.

---


### 65. [Output Dilution: Redundant but Fragile Representations in MoE Models](https://arxiv.org/abs/2608.25231)

**<font color=#1a73e8>作者：</font>** Orion Reblitz-Richardson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models appear to encode moral content as robustly as dense models, yet prove far more fragile in their encoding. In OLMoE-1B-7B, linear probes recover moral valence from nearly every expert-layer combination, with mean peak-layer accuracy above 90%. But these representations collapse under levels of activation noise that a dense model of matched size easily tolerates, with a 4.2-fold difference in robustness.
We trace this to output dilution. Because the MoE block averages across active experts before contributing to the residual stream, the feedforward signal reaching downstream layers is nearly two orders of magnitude smaller than in a dense MLP. Moral information, our interest, survives aggregation intact but at a scale trivially overwhelmed by perturbation. Routing itself remains stable under noise while the vulnerability originates entirely in the diluted aggregate.
Checkpoint trajectories confirm this is architectural, not learned. Experts never specialize and accuracy saturates within the first few thousand steps. In sparse architectures, redundant encoding does not imply robust encoding.

---


### 66. [From Memorization to Absorption: Mixed-Policy RL for Continual Knowledge Injection](https://arxiv.org/abs/2608.25243)

**<font color=#1a73e8>作者：</font>** Zhibo Hou, Fan Zhao, Zhiyu An 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continual knowledge injection is essential for keeping large language models up-to-date in a fast-evolving world. Existing methods rely on supervised fine-tuning (SFT), which memorizes injected facts in their training format but fails to generalize across paraphrasing, document combinations, and reasoning. To address this, we propose Golden-GRPO Injection (GRIN), a three-stage self-learning framework for continual knowledge injection. Golden-GRPO is a mixed-policy reinforcement learning algorithm designed specifically for knowledge injection, which injects a golden answer to provide learning signal even when on-policy rollouts fail on novel facts. We further introduce Blank and Counter, two document-level benchmarks targeting novel acquisition and counterfactual overwrite respectively, each evaluating single-fact recall, multi-source retrieval, and inferential reasoning. Our experiments establish a clear empirical claim: mixed-policy reinforcement learning enables knowledge absorption beyond what supervised fine-tuning can achieve. GRIN substantially outperforms SFT and mixed-policy RL baselines on the harder question types while matching them on basic fact recall.

---


### 67. [What Do Medical Vision-Language Models Learn in Radiology? Transfer, Alignment, and Source-Proxy Leakage Under Distribution Shift](https://arxiv.org/abs/2608.25251)

**<font color=#1a73e8>作者：</font>** Ayoub Louaye Bouaziz, Lokmane Chebouba, Yassine Himeur  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language models (VLMs) can appear reliable in-domain while failing when acquisition domain, paired supervision, or evaluation protocol changes. We study this failure mode as a representation-level blind spot relevant to epistemic intelligence, without claiming a formal estimator of epistemic uncertainty. Using NIH ChestXray14 and CheXpert, we first isolate source-only cross-dataset visual transfer from unsupervised domain-adaptation diagnostics. Using PadChest and OpenI, we then evaluate multimodal alignment under strict pair-index retrieval and quantify metadata-derived source-proxy information retained in frozen embeddings. Self-supervised visual initialization improves NIH-to-CheXpert transfer over supervised ImageNet initialization in matched ResNet-18 comparisons, whereas adversarial adaptation is useful only in a narrow regime and becomes unstable as adversarial pressure increases. Multimodal exact-pair retrieval remains low under external OpenI stress testing, and source-proxy information remains recoverable from learned representations. Qualitative nearest-neighbor and Grad-CAM analyses show clinically plausible cross-dataset structure and thoracic attention patterns in many cases, while device-heavy and false-positive cases remain ambiguous. Auxiliary architecture checks are task-dependent and do not support a universal backbone ranking. Overall, the study shows that apparent competence under a single protocol can conceal transfer, alignment, and shortcut-related failure modes, motivating stress-tested evaluation of medical VLMs under distribution shift.

---


### 68. [Hierarchical MoE for Multi-Modal ILD Diagnosis](https://arxiv.org/abs/2608.25261)

**<font color=#1a73e8>作者：</font>** Alec K. Peltekian, Gorkem Durak, Halil Ertugrul Aktas 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts (MoE) models combine specialized predictors under learned routing, offering a principled mechanism for leveraging heterogeneity in medical data. We present a hierarchical multimodal MoE for interstitial lung disease (ILD) classification that integrates a frozen, pre-trained imaging expert with structured electronic health records (EHR) via two-stage gating. A modality-level gate assigns patient-specific weights to imaging and EHR predictions, while a sub-gating module decomposes the EHR branch into clinically defined feature groups with learned, group-specific contributions. This design preserves stable imaging representations while enabling input-dependent clinical weighting and explicit EHR specialization. Under strict patient-level cross-validation, the model achieved the highest mean AUC among the evaluated methods (0.8750 +- 0.0443), compared with 0.8646 for imaging-only REN and 0.7685 for SwinUNETR. The framework extends interpretability across anatomical regions, imaging--EHR utilization, and clinically defined EHR feature groups.

---


### 69. [Mitigating LLM sycophancy with RL-based fine-tuning: Bayesian Truth Serum approach](https://arxiv.org/abs/2608.25267)

**<font color=#1a73e8>作者：</font>** Serhii Mytsyk, Yiming Zhang, Vikram Krishnamurthy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) frequently exhibit \emph{sycophancy}: they adapt their answers to a user's stated beliefs or preferences instead of reporting what they hold to be true, which lowers factual accuracy and can amplify misinformation. This paper proposes a methodology for mitigating sycophancy that employs the Bayesian Truth Serum (BTS), a peer-prediction mechanism, as the reward in Group Relative Policy Optimization (GRPO) to fine-tune an LLM. BTS pays an answer for being \emph{surprisingly common}, that is, more frequent among respondents than those respondents themselves predicted. We treat a group of responses from a model for one question as those respondents, so the reward is a function of the model's own outputs and fine-tuning needs neither labels nor preference annotations. We prove that in the large-group limit a sycophantic response earns strictly lower expected reward than an honest one. We also prove that if the entire group agrees in advance on a symmetric answering rule, it cannot earn a higher information score than under truthful reporting. On our true/false benchmark the reference model's answer-flip rate under user pressure decreases from 23% to 4%, and its accuracy under that pressure increases from 80% to 93%. Our reward outperforms SMART and is comparable to synthetic-data fine-tuning and to pinpoint tuning, all three of which train on labels. It spends considerably more compute in exchange, which makes it suitable when labeled data is scarce. Peer Truth Serum, which also pays a premium for a rare answer but elicits no prediction report, reproduces the effect. A peer-prediction reward computed inside a single GRPO group therefore reduces sycophancy without labels, and comparing mechanisms suggests that the premium paid for a rarer answer drives the effect.

---


### 70. [Groundhog Bit-Flip Attack: Seeding Infinite Generation Loops in Mixture-of-Experts LLMs through Bit Flips](https://arxiv.org/abs/2608.25276)

**<font color=#1a73e8>作者：</font>** Huakang Lin, Tiancheng Zheng, Mingxuan Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures enable scalable and efficient large language models (LLMs) by selectively activating expert sub-networks through a routing mechanism. However, this adaptive design introduces a new attack surface: specific experts become disproportionately correlated with certain tokens (e.g., end-of-sequence), allowing adversaries to manipulate model behavior via lightweight perturbations. In this work, we present \textbf{Groundhog Bit-Flip Attack (GBFA)}, the first bit-flip-based \textit{ Denial-of-Wallet availability attack} against MoE-based LLMs. By identifying and flipping routing-layer bits associated with related expert activations, we demonstrate that GBFA substantially extends the decoding token usage across three different LLM modes: conversational, reasoning, and agentic tasks, while largely preserving semantic fidelity. Across four main real-world MoE-based LLMs, manually deactivating on average fewer than \textbf{4 experts} drives average output inflation to $\mathbf{5912\%}$, with the majority of test samples reaching max tokens. These results reveal a robustness vulnerability of MoE architectures to bit flip, and highlight the potential of GBFA as an availability attack against LLMs.

---


### 71. [Routed Graph Handoff: Adaptive Format Selection for Multi-Agent LLM Delegation](https://arxiv.org/abs/2608.25277)

**<font color=#1a73e8>作者：</font>** Pratyay Banerjee, Ankit Chadha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems coordinate through natural-language messages that consume 40--60\% of their token budget. Replacing these with structured graphs reduces cost but fails on tasks requiring adaptive reasoning. We propose \textbf{Routed Graph Handoff}, where a lightweight LLM router (155 tokens, 0.15\% overhead) selects between a typed dependency graph and natural language for each delegation. On four benchmarks (1,050+ trajectories), the routed system matches or exceeds NL-only on every task: \textbf{+12.7\,pp} on $\tau$-retail at 3.2$\times$ compression ($p{<}0.01$), \textbf{+8.7\,pp} on BrowseComp at 2.2$\times$ compression ($p{<}0.05$), and parity on BFCL and AppWorld. Without the router, graph-only delegation regresses 14.6\,pp on AppWorld; the router eliminates this at near-zero cost. A graph-aware executor prompt is required: the same schema without interpretation guidance yields no gain. An oracle analysis reveals 8.6\,pp of additional headroom, motivating execution-time adaptive routing as future work.

---


### 72. [BixBench3: Benchmarking AI agents on research-study-scale computational biology tasks](https://arxiv.org/abs/2608.25286)

**<font color=#1a73e8>作者：</font>** Zane Koch, Asmamaw T. Wassie, Javier Valdes-Aleman 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) promises to accelerate biological research by automating computational analyses. Yet the ability of AI agents to carry out computational biology at the scale of complete research studies has not been systematically evaluated. Here we introduce BixBench3, a benchmark that measures the capacity of AI agents to process raw biological data through to scientific results. We designed BixBench3 tasks to mirror the delegation of work from a scientist to an agent: the scientist chooses the research question and high-level methods, then delegates implementation of all analyses to the agent. In each task, an agent receives a research objective, methodological guidance, and raw data derived from a published scientific study, and must execute a sequence of analyses to achieve the research objective. The data artifacts resulting from these analyses - such as peak call matrices or differential expression tables - are programmatically graded against the corresponding artifacts generated and reported in the original study. Across 20 BixBench3 tasks encompassing the generation of 138 unique artifacts, we find that 13 frontier models achieve scores ranging from 0.00 for Gemini 3.1 Flash Lite to 0.48 for GPT 5.6 Sol. Agents perform worse on tasks with larger raw datasets (0.36 on tasks with <100 GB versus 0.10 on tasks with >100 GB) and on analyses requiring more sequential steps (0.36 at 1-2 steps vs 0.24 at 3+). On average, agents use 6.8 hours, 102 million tokens, and $43 to complete each task, with the longest attempts consuming 24 hours, 1.07 billion tokens, and $525. Notably, the highest-scoring agents used fewer tokens and were cheaper than less performant options. These results reveal that LLMs vary substantially in their ability to (1) execute multiple sequential analysis steps coherently, (2) manage large quantities of raw data, and (3) work across scientific domains.

---


### 73. [InsightSR: Refining Symbolic Regression Search Spaces via Parallel Semantic and Structural LLM Guidance](https://arxiv.org/abs/2608.25291)

**<font color=#1a73e8>作者：</font>** Yating Ling, Wenjing Cun, Zhitang Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic regression (SR) seeks to discover parsimonious mathematical laws from observational data, yet conventional approaches often struggle with the vast combinatorial search space of physically meaningful expressions. We present InsightSR, a framework that embeds Large Language Models (LLMs) as a guiding layer around the PySR genetic programming engine. Rather than relying on LLMs to generate expressions directly, InsightSR uses LLMs to progressively transform the search space itself through two complementary pathways: a Semantic Seed Pathway that proposes dimensionally consistent functional skeletons, and a Structural Feature Pathway that recommends nonlinear feature transformations. These transformations accumulate over iterations, broadening the input space and shifting the symbolic search from constructing deep expression trees over raw variables to assembling shallow trees over a rich, semantically informed feature set. A post-generation feedback loop evaluates candidates, categorizes features by their empirical utility, and refines the guidance for the next iteration, transforming the discovery process from open-ended generation into iterative, self-correcting refinement. Across three benchmarks, InsightSR achieves a 95% exact recovery rate on the Feynman benchmark and 80.18% accuracy on the LLM-SRBench LSR-Transform task, substantially outperforming state-of-the-art genetic programming and neural-symbolic methods while maintaining strong out-of-distribution generalization on real-world datasets.

---


### 74. [PointRL: Learning Point-Level Vision-Language Grounding from Verifiable Annotation Evidence](https://arxiv.org/abs/2608.25299)

**<font color=#1a73e8>作者：</font>** Jingyang Su, Pu Cao, Xiuze Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) increasingly rely on point coordinates as a compact and executable interface for visual grounding in GUI interaction, robotic manipulation, and interactive visual systems. However, learning reliable pointing behavior remains difficult because the supervision space is inherently non-unique: many coordinates may be valid within the same target region, while multi-instance instructions require target coverage, count consistency, and duplicate suppression. This work presents PointRL, a verifiable reinforcement learning framework that learns point-level grounding from existing heterogeneous annotation evidence. PointRL converts bounding boxes, masks, and instance labels into pointing instructions, while retaining their target supports, instance membership, and set constraints as hidden verifier evidence, i.e., annotations kept outside the prompt and used by a deterministic checker to score predictions. The proposed reward evaluates parseability, point validity, instance coverage, cardinality consistency, and redundant or missing predictions. On PointArena, PointRL improves the overall accuracy of Qwen3.5-4B from 56.11% to 65.58%. Further evaluations on RoboSpatial, BLINK, and Ref-Adv show same-backbone gains on the evaluated external benchmarks, suggesting that verifiable point-level feedback may benefit spatial grounding in these settings.

---


### 75. [V-Link: Recovering Lost Visual Representations in Action DiT for Vision-Language-Action Models](https://arxiv.org/abs/2608.25308)

**<font color=#1a73e8>作者：</font>** Yehao Lu, Jiarui Yang, Yuning Su 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models provide a scalable path toward generalist robotic manipulation by integrating visual perception, language understanding, and continuous action control. However, we reveal a critical limitation of VLA architectures: the action expert has limited access to the 3D geometric and 2D semantic information available in VLM features. This accessibility gap weakens perceptual grounding and limits performance on fine-grained robotic manipulation. To address this issue, we propose V-Link, which explicitly recovers visual representations during the vision-language (VL) to action (A) feature transfer. Specifically, V-Link learns complementary Spatial and Semantic Query representations within the VLM and injects them into Action DiT through asymmetric pathways. Semantic Queries complement the original VLM image tokens, whereas Spatial Queries provide dedicated geometric conditioning for spatially grounded action generation. Across LIBERO, LIBERO-Plus, and RoboTwin 2.0, our V-Link improves the average success rate over base model GR00T N1.6 by +1.9%, +31.2%, and +18.8%, respectively. On the AGIBOT A3 Ultra, V-Link further achieves gains of +20% and +24% on two real-world humanoid tasks.

---


### 76. [Prefix-Denoising Consistency: Test-Time Verification for Diffusion Language Models](https://arxiv.org/abs/2608.25311)

**<font color=#1a73e8>作者：</font>** Yuki Ichihara, Naoto Iwase, Mohammad Atif Quamar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion Language Models (DLMs) have recently become increasingly competitive with autoregressive (AR) models, and even outperform them on certain tasks. Unlike AR models, DLMs produce output through iterative denoising without a left-to-right order. To further improve the performance of DLMs, we introduce PDC (\emph{Prefix-Denoising Consistency}), a test-time self-verification method for DLMs. PDC exploits a distinctive test-time signal in DLMs under prefix conditioned regeneration, correct trajectories are more stable and reproducible than incorrect ones. Concretely, given an initially generated sample, PDC splits the sentence at an intermediate position and regenerates the remaining tokens conditioned on the fixed prefix. Across mathematical reasoning and commonsense reasoning benchmarks, PDC consistently improves upon the initial sample, outperforms independent generations under a computational constrained comparison, and is robust to different unmasking strategies and parameter settings. These results highlight prefix-conditioned regeneration as an effective DLM-specific primitive for test-time verification.

---


### 77. [Activation-Space Order-Swap Geometry: A Site-Asymmetry Audit](https://arxiv.org/abs/2608.25315)

**<font color=#1a73e8>作者：</font>** Anqi Peter Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Order-dependent activation statistics are often interpreted as evidence of interaction, but that interpretation can be confounded by where interventions enter the network. We introduce a no-fit site-asymmetry audit. For a twice-differentiable readout, the open-path order-swap decomposes into a canonical additive response measured by single interventions and an antisymmetrized second difference free of first-order and pure self-curvature terms to second order. Across six open-weight language-model families, the single-intervention baseline explains 84.3-97.7 percent of the bracket norm (mean 93.7 percent), while the no-interaction self-curvature term is 1.8-5.2 times larger than the corrected residual in the two families with the plus/minus injection split. The corrected residual clears a generic-interaction null in three of six families under a confound-free prompt split and two of six after configuration robustness. A known-positive surrogate recovers planted mixed interaction, while a matched site-separation test changes the baseline share and a random architecture reproduces the first-order regime. The same estimator transfers to released non-language references: trained residual fractions fall below a fixed Gaussian-direction null in 11/12 contrasts (5/6 ViT-B/16, 6/6 ResNet-50), a portability check rather than pooled evidence. The contribution is a reusable measurement criterion: run the single-intervention baseline before reading an order-swap vector as interaction or geometric structure; if it explains the vector, form the second difference instead. All claims are scoped to activation-space interventions at distinct sites; we do not claim that representation geometry is globally Abelian.

---


### 78. [LLMscope: Extracting LLM Assets from Edge AI Chips via Optical Probing](https://arxiv.org/abs/2608.25321)

**<font color=#1a73e8>作者：</font>** Dev Mehta, Lily Dukette, William Folan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The move of LLM inference to edge AI accelerators introduces new physical vulnerabilities. During execution, model parameters and intermediate inference states are repeatedly loaded into and processed on the chip, making them suscep- tible to physical side-channel attacks. In this work, by deploying laser voltage imaging, we show that one can extract LLM assets during inference, namely embeddings, attention, and quantized MLP weights, activations, and other inference states, from localized memories and compute subcircuits. To validate our claims, we perform an attack on an FPGA-based LLM accelerator. Since such accelerators reuse the same buffers and compute subcircuits across addresses, tiles, modules, and layers, reading asset values comes down to probing different memories during inference. We demonstrate full recovery of the targeted values; however, we also establish a methodology to recover asset values even if some weights or bits remain unread. We further derive lower bounds that relate imaging effort to asset dimensions and show that even direct recovery scales linearly with the size of the targeted asset

---


### 79. [FinRiskAtlas: Decision-Aligned Evaluation of Large Language Models for Financial Risk Review](https://arxiv.org/abs/2608.25325)

**<font color=#1a73e8>作者：</font>** Suyang Zhong, Jingzhe Zhu, Qi Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying large language models for professional financial review requires more than measuring general financial competence: models must perform the specific review operation required by a workflow and determine whether available evidence is sufficient for a defensible decision. Existing financial benchmarks cover knowledge, reasoning, compliance, and professional tasks, but their evaluation units are often organized around datasets or task formulations rather than the decisions that deployed systems support. We introduce FinRiskAtlas, a Chinese-language benchmark that evaluates financial LLMs along two complementary dimensions: operation execution under fixed evidence states and evidence-state control under evolving review conditions. The static benchmark contains 9,742 instances across 53 task families, including 42 Domain Knowledge families and eleven downstream review operations defined by explicit evaluation contracts. FinRisk-Ask extends this framework through offline replay of 680 pre-action states from 104 de-identified professional trajectories, withholding future evidence during inference and using it only to construct expert-verified evidence targets. Across 33 model configurations, operation-level evaluation yields non-redundant rankings (mean pairwise Spearman correlation 0.42 across downstream operations), and knowledge-based shortlisting can incur up to 18.01 points of regret on individual operations. FinRisk-Ask further shows that entering the Ask branch more frequently does not necessarily improve request targeting or end-to-end evidence acquisition. These results show that broad financial capability scores do not fully capture where models are reliable in professional workflows, motivating evaluation units aligned with the decisions and evidence states that deployed systems must support.

---


### 80. [Learning What to Share and What to Personalize: Hierarchical Strategy Co-Evolution for Agent Memory](https://arxiv.org/abs/2608.25329)

**<font color=#1a73e8>作者：</font>** Yupeng Han, Shuochen Liu, Kai Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory-augmented agents maintain compact user profiles throughout extended conversations, enabling personalized and consistent responses without the need to process the entire dialogue history. The quality of these user profiles relies on the underlying memory management strategy: at each step, the agent must determine what to retain, compress, or discard. However, existing methods typically employ a static, one-size-fits-all strategy established before training. In practice, the optimal memory decision is inherently user-specific and dynamically evolves alongside policy optimization. To address this, we propose \textbf{HiPS} (\textbf{Hi}erarchical \textbf{P}ersonalized \textbf{S}trategy), a framework that decouples memory management into a globally shared foundation and a user-specific adaptive tier. Specifically, HiPS employs \textbf{Universal Strategy} to extract shared principles from cross-persona trajectories, alongside \textbf{Persona Delta Distillation} to generate tailored rules for users whose behaviors diverge from general patterns. \textbf{Cross-Level Rule Flow} dynamically calibrates their boundary by promoting broadly validated personal rules and demoting contradicted global ones. The architecture establishes a co-evolution loop where a mechanism guarantees that all strategy refinements are anchored to task outcomes. Extensive experiments demonstrate consistent improvements over memory-augmented baselines.

---


### 81. [Not All Attention Heads Contribute to Critical Visual Token Selection: Head-Aware Pruning Matters More](https://arxiv.org/abs/2608.25332)

**<font color=#1a73e8>作者：</font>** Chaofang Ma, Lin Jiang, Carol Jingyi Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have exhibited impressive performance across diverse visual scenarios. However, this success comes at the cost of explosive growth in visual tokens, which imposes substantial memory and computational overhead during inference, ultimately increasing latency. To improve VLM inference efficiency, a typical class of visual token pruning methods estimates token importance by aggregating attention scores across all heads in the pruning layer of the Large Language Model (LLM) backbone and prunes tokens based on aggregated scores. However, in this paper, we reveal a compelling phenomenon: the capability to pinpoint critical visual tokens is concentrated within a small fraction of heads. Aggregation exclusively on these heads can improve task performance. Inspired by this observation, we propose ProViP, a training-free progressive visual token pruning framework. ProViP first removes redundant visual tokens based on the embedding similarity of input tokens before reasoning of the LLM backbone, and then further prunes tokens during reasoning via head-aware pruning. Experiments demonstrate that ProViP delivers outstanding task performance and inference efficiency. For instance, when applied to LLaVA-1.5-7B, ProViP retains 95.9% of the original performance and achieves 1.62x inference speedup under an 88.9% pruning ratio.

---


### 82. [Provenance Before Prose: Claim-Locked Reporting](https://arxiv.org/abs/2608.25336)

**<font color=#1a73e8>作者：</font>** Xiao Fan, Jingyuan Li, Hongbin Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can fluently verbalize statistical evidence, yet statistical reports can still drift numerical values, invert effect directions, or restate thresholded contrasts as categorical effects. We frame these failures as a control problem: the evidence-bearing content of a scientific report should be fixed by structured statistical results rather than sampled during prose generation. We therefore use cross-run reproducibility to stress-test whether report-visible numbers and claims are bound before prose generation. Existing controls operate at the text or slot level; a deterministic hybrid template reproduces only 61.1% of report-visible numerical content across seeds because the LLM still selects which findings and numbers the template renders. We propose claim-locked reporting, a provenance-before-prose protocol that fixes the evidence source, numbers, direction, and allowed language strength of each reportable claim before the LLM writes only connective prose. Across fMRI functional-connectivity reporting and randomized controlled trial reporting on Evidence Inference 2.0, claim-locked reporting improves reproducibility over the hybrid template by 37.4 and 20.5 points, respectively. Blinded human audits support the observed direction-preservation and governance trends. In an fMRI cost analysis with DeepSeek, claim-locked reporting also yields the lowest observed token use and median generation latency.

---


### 83. [GUIDE: Generative Unsupervised Chinese Query Correction via Phonetic and Visual Shared-ID Encoding](https://arxiv.org/abs/2608.25343)

**<font color=#1a73e8>作者：</font>** Lei Yang, Binbin Huang, Jiwei Tan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chinese query correction (CQC) is important for search and query recommendation on content platforms, but supervised methods rely on large annotated correction pairs that are costly to maintain as query vocabularies evolve. Unsupervised correction with language models is attractive, yet in the short-query setting, unconstrained generation often over-corrects ambiguous inputs toward high-frequency phrases, causing intent drift. We propose \textsc{GUIDE}, a generative unsupervised framework for CQC based on a confuse-then-clarify paradigm. \textsc{GUIDE} encodes phonetically or visually confusable characters with shared-IDs and reconstructs the original query with an encoder--decoder architecture, which constrains correction to plausible confusion neighborhoods while learning from unlabeled query streams. A time-decayed, query-frequency-weighted objective further supports adaptation to rapidly changing query vocabularies. Experiments on \textit{QSpell 250K} and a large-scale real-world dataset (\textit{KwaiSearch}) show that \textsc{GUIDE} consistently outperforms strong baselines, while online A/B testing further confirms gains in correction quality and downstream engagement.

---


### 84. [Short Horizons and Sparse Concepts: a Mathematical View of the Readout in the J-lens](https://arxiv.org/abs/2608.25347)

**<font color=#1a73e8>作者：</font>** Shi-Qi Yan, Kai-Xuan Ding, Chao-Hong Tan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Jacobian lens (J-lens) has been proposed as a way to read verbalizable representations from language models. However, its principle and meaning lack a detailed and theoretical discussion. We provide a mathematical view of this interpretation and of its assumed causal structure. Besides treating the J-lens as a heuristic probe, we further regard it as a first-order causal transfer operator from intermediate activations to expected future readouts. We study the Jacobian matrix as the optimal local linear approximation of the downstream mapping, analyze its global approximation behavior and bias, and identify its mathematical meaning as an expectation over anticipated future readouts. Further analysis of the Jacobian energy distribution reveals that its causal geometry is highly sparse. The energy decays with depth, concentrates in an extremely small proportion, and decomposes into diagonal pathways and specific critical positions. This decomposition further resolves the expectation of the J-lens over future outputs into short-horizon and sparse concept predictions, providing a more intuitive attribution and explanation for the ability of the J-lens to visualize concepts during the thinking process. Based on the theory, we propose a simple but effective improvement strategy and decoupling method for the J-lens, which significantly enhances the ability of the J-lens to read out correct intermediate concepts.

---


### 85. [Beyond Pairwise Feedback: Listwise Vision-Language Supervision for Preference-Based Reward Learning](https://arxiv.org/abs/2608.25350)

**<font color=#1a73e8>作者：</font>** Srivalli Katkuri, Maxwell Kawada, Juan Wachs  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have emerged as a powerful source of supervision for reinforcement learning, enabling agents to leverage rich semantic knowledge during training. Inspired by the success of preference-based reward learning (PbRL) in reinforcement learning from human feedback (RLHF), vision-language model generated image-based preferences provide an effective source for learning reward functions. This can be done by visually comparing two outcomes through the Bradley-Terry (BT) model. However, this pairwise formulation utilizes only two observations at a time, despite VLMs being capable of ranking multiple candidates. The Plackett-Luce (PL) formulation can shape a reward model with listwise rankings as opposed to pairwise preferences, allowing for a more suited use of a VLM based ranking. In this work, to our knowledge, we introduce the first framework that combines VLM-generated preferences with the Plackett-Luce model for reward learning. We evaluate our approach on Meta-World manipulation tasks and show that Plackett-Luce (PL) reward models can train robotic policies from VLM-generated rankings as effectively as pairwise Bradley-Terry, $K$-wise Bradley-Terry, and RL-VLM-F baselines. Across all environments, at least one PL ranking size ($K \in \{3,4,5\}$) consistently performs with or outperforms other methods in mean success rate. Unlike pairwise methods, which are restricted to $K=2$, PL supports different ranking sizes and can therefore be adapted to the environment and desired feedback format. Our best PL configuration achieves an 86% mean final success rate and matches the Oracle baseline on Drawer Open. Overall, these results demonstrate that listwise VLM preference supervision is a competitive and flexible approach to reward learning for reinforcement learning.

---


### 86. [Escaping Low-Dimensional Overlap: Multi-Task Model Merging via High-Dimensional Sparse Disentanglement](https://arxiv.org/abs/2608.25354)

**<font color=#1a73e8>作者：</font>** Yihang Zhang, Shengke Sun, Junjie Wen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model merging provides an efficient way to construct multi-task generalist models without additional training, but its performance often degrades under severe task interference. Task interference in model merging primarily stems from \textit{superposition}, where task-specific features become entangled within the parameter space. This entanglement renders conventional decomposition methods insufficient for effectively isolating useful task directions from interfering components. In this paper, we propose a sparse-representation-based merging framework that uses Sparse Autoencoders (SAEs) to project task vectors into a high-dimensional sparse feature space, enabling feature-level disentanglement before fusion. To reduce computational overhead, we further introduce a lightweight Group-Ranked Zeroth-Order Optimizer (GR-ZOO) to identify task-critical layers for selective merging. Experiments on both Qwen2.5-1.5B and Qwen2.5-7B demonstrate that our method consistently outperforms representative baselines, including Task Arithmetic, TIES-Merge, DARE, Fisher-Merge,and several recent training-free merging methods, across mathematical reasoning, code generation, instruction following, and general knowledge tasks. In a highly conflicting four-task setting on Qwen2.5-1.5B, our method further achieves a 2.78\% improvement over the strongest baseline.

---


### 87. [Where to Look Matters: On-Policy Self-Distillation for Long-Video Understanding](https://arxiv.org/abs/2608.25356)

**<font color=#1a73e8>作者：</font>** Kaishen Wang, Dongdi Zhao, Yijun Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have made substantial progress in long-video understanding, with standard backbone models typically answering questions from frames sampled across the full video. However, as videos become longer, the full-video context inevitably contains more question-irrelevant temporal content, which can distract the model from the evidence needed to answer a specific question. We empirically find that focusing the visual input on short annotated clue intervals containing question-relevant evidence consistently improves prediction accuracy across model scales compared with using the corresponding full videos, while requiring fewer input frames. Based on this finding, we introduce Clue-OPSD, a clue-privileged on-policy self-distillation framework for long-video understanding. During training, a full-video student learns from a self-teacher conditioned on the corresponding clue interval by aligning their next-token distributions along student-generated trajectories. Clue-OPSD thus uses clue intervals as privileged supervision without relying on ground-truth answer labels, while requiring no clue annotations or additional modules at inference time. Extensive experiments across multiple long-video understanding benchmarks and Qwen3.5 model scales demonstrate consistent improvements over the corresponding backbone models and strong performance against supervised post-training baselines.

---


### 88. [Where vs What: Decomposing Structural and Content Failures in LLM-Generated Structured Outputs](https://arxiv.org/abs/2608.25358)

**<font color=#1a73e8>作者：</font>** Yiwei Zhang, Chengke Wu, Li Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Structured outputs such as JSON and tables are central to modern LLM-based systems, yet generation failures are evaluated monolithically, conflating two distinct error modes: placement errors (correct values at wrong positions) and value errors (wrong values at intended positions). We introduce Structure-Content Decomposition (SCD), a framework that independently measures structural fidelity and content accuracy. Applying SCD to nested JSON and table tasks across six models (7B to frontier), we uncover a consistent phenomenon: structural fidelity degrades earlier and more sharply than content accuracy as complexity increases. At the highest complexity, even DeepSeek-V4-Flash (with reasoning) misplaces 35% of recalled values, while Qwen2.5-7B misplaces 74%. Controlled ablations suggest that this pattern is associated with reliance on semantic shortcuts rather than topological understanding of output structure. Based on these findings, we propose SA-RLVR, converting SCD metrics into verifiable rewards for reinforcement learning via GRPO. SA-RLVR successfully optimizes structural addressing across distinct topologies: it lifts JSON Value Placement Accuracy (VPA) from 26% to 63% while generalizing to held-out schemas; moreover, it consistently drives VPA improvements in the table domain, demonstrating that structure-aware rewards can directly enhance multi-domain structural positioning.

---


### 89. [Adaptive Triggering for Bias Correction in LLM Reasoning](https://arxiv.org/abs/2608.25379)

**<font color=#1a73e8>作者：</font>** Nayoung Kim, Mickey Mancenido, Huan Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought prompting can expose and amplify demographic stereotypes within an LLM's intermediate reasoning and create a failure mode that final-answer debiasing alone cannot address. Mitigating such bias during generation presents a fundamental timing problem: intervening too late allows biased reasoning to propagate, while unnecessarily intervening can disrupt otherwise correct reasoning. Existing approaches largely avoid this decision by either evaluating completed reasoning chains post hoc or intervening at predetermined steps, leaving open when a developing reasoning trajectory provides sufficient evidence to warrant correction. We formulate this decision as an online change-point detection problem. A per-step bias signal updates a CUSUM statistic and a targeted correction is injected only when accumulated evidence crosses a detector-specific threshold calibrated on held-out data. We instantiate the framework with a white-box signal derived from next-token probabilities and a black-box signal obtained from an LLM judge, enabling deployment with both open-weight and hosted models. On gpt-4o-mini adaptive black-box triggering recovers most of the disambiguated-context accuracy lost under fixed-interval intervention while requiring substantially fewer interventions. That result holds even with an independent judge. Across six open-weight models, the white-box signal improves ambiguous-item accuracy on all six but reduces disambiguated-item accuracy on five because it cannot distinguish unsupported stereotype reliance from correct, stereotype-congruent evidence.

---


### 90. [Q&A or Document-Based? The Effects of Interface Type on How Screen Reader Users Access Interconnected Documents](https://arxiv.org/abs/2608.25382)

**<font color=#1a73e8>作者：</font>** Colleen F. Cipriano, Yichun Zhao, Miguel A. Nacenta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Blind and low-vision (BLV) users are increasingly engaging with large language model (LLM) interfaces to access documents, but it is unclear how such systems support or hinder their ability to build interconnected knowledge. To examine this gap, we compared a Question-Answer Interface (QAI) that supports open-ended conversational inquiry, with a Document Interface (DI) based mostly on traditional structured text document navigation. We recruited 16 BLV screen reader users where they used both interfaces to explore two fictional worlds. Data from interaction logs, concept maps, decision-based tasks, and semi-structured interviews provide comparative insights into how interface design supports knowledge construction. Findings show that participants visited more distinct documents with the DI and formed larger and more correct mental models with the DI than with the QAI. They were also more able to apply knowledge they had gained. Simultaneously, many still preferred the QAI and often estimated that they had explored more, formed better mental models and applied their models better when acquiring the information with the QAI, despite this not being the case. Our analysis suggests possible interface design reasons for these differences and highlights some of the risks introduced by using question-answer interfaces to access information spaces.

---


### 91. [Efficient Training with Foresight: Multi-Token Auxiliary Supervision for Autoregressive Image Generation](https://arxiv.org/abs/2608.25386)

**<font color=#1a73e8>作者：</font>** Guo Niu, Xiongfei Yao, Teng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) image generation has shown strong potential for scalable high-fidelity synthesis by modeling images as discrete token sequences. However, traditional next token prediction (NTP) continues to suffer from sparse and myopic supervision, insufficiently discriminative representations, and high training cost caused by dense computation over the full token sequence. To address these issues, we propose multi-token autoregressive (MTAR), a unified training framework that improves autoregressive image generation from three aspects: prediction objectives, representation regularization, and training efficiency. Specifically, MTAR introduces multi-token prediction (MTP) to alleviate the sparsity and myopia of traditional NTP by imposing joint supervision on multiple future tokens; employs token-level contrastive regularization (TCR) to explicitly enhance the separability of sampled token representations and thereby improve representation discriminability; and incorporates semantic dropping (SD) as a semantics-aware training acceleration strategy to reduce redundant computation on low-information tokens while preserving informative learning signals. All three components are applied only during training and introduce no additional overhead during autoregressive inference. On ImageNet, MTAR achieves a better balance between generation quality and training efficiency. Compared with LlamaGen, MTAR achieves up to 0.95 lower FID and 39\% faster training. Moreover, even with only 1/3 of the training iterations, it still attains performance comparable to or better than the baseline, substantially reducing training time.

---


### 92. [Refusal geometry reflects refusal training: diverse refusal prefixes can raise stable rank and weaken refusal vector ablation attacks](https://arxiv.org/abs/2608.25390)

**<font color=#1a73e8>作者：</font>** Andrey Labunets  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Refusal training protects AI models from jailbreaks by training models to decline unsafe queries, reducing the risk of misuse. Recent work finds that refusal behavior in aligned language models can be mediated by a single activation direction or a low-dimensional refusal subspace shared across harmful prompts: ablating those directions suppresses refusals while largely preserves other model capabilities. Yet it remains unclear why safety-critical features in a wide range of models emerge and concentrated, low-dimensional structure. In a case study of OLMo-2-0425-1B-Instruct we find that the refusal geometry reflects refusal training: activation updates resulting from refusal-completion first-token losses explain the resulting refusal direction and refusal subspace. We study refusal directions through the training dynamics across refusal datasets and reveal that their brittleness is associated with repetitive refusal starts, which in turn is linked to concentration of gradients and refusal features in a low-dimensional subspace. Across frozen-model analyses and controlled synthetic fine-tuning, we find evidence of a hardening lever: diverse refusal starts can raise stable ranks of gradients and activation changes, making refusals harder to remove with a vector ablation attack.

---


### 93. [OmniPhys: A Unified Multimodal Benchmark for Physics Understanding and Generation from Chinese Educational Corpora](https://arxiv.org/abs/2608.25398)

**<font color=#1a73e8>作者：</font>** Hao Chen, Yumin Lin, Nadila Yushanjiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated strong abilities in solving diverse visual and textual reasoning tasks. However, their development in the physics domain is significantly hindered by the lack of a comprehensive benchmark. To fill this gap, we introduce OmniPhys, a large-scale benchmark for multimodal physics understanding and reasoning, covering middle school through university-level problems from Chinese Educational Corpora. OmniPhys consists of 15,246 questions and 19,850 images, accompanied by detailed annotations that support fine-grained analysis of reasoning processes and knowledge usage. Beyond conventional evaluation, OmniPhys is a benchmark that systematically evaluates multimodal outputs in the physics domain, including models' ability to generate structured physics diagrams, which constitute a fundamental component of authentic physics problem solving. Extensive evaluations reveal critical gaps in the capabilities of current MLLMs, especially in complex reasoning and visual generation. To address this, we release OmniPhys to serve as a foundational resource for advancing multimodal intelligence in physics and scientific domains. Codes and data are available at this https URL.

---


### 94. [Can your AI agent be cheaper? Investigating the effects of task specifications on token spend in agentic coding tasks](https://arxiv.org/abs/2608.25399)

**<font color=#1a73e8>作者：</font>** Jakub Smékal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic coding workflows are now widely deployed in real-world systems. With long-horizon reasoning and tool use, token usage has become an important consideration for both cost and efficiency. Two engineers using AI will solve the same problem differently. How the specification of a task shapes an agent's token spend, and whether that spend can be predicted in advance, are open questions. Here, we study the effects of different task specifications on agentic token spend with the Kimi K3 model at three thinking efforts. Across $2,700$ runs, we show that reducing a full task specification to a bare user story raises token spend by $29.7\%$, while run-to-run variance remains unaffected by any prompt changes. We show that prompt-sensitivity is task-dependent, running from $13\%$ to $115\%$. We fit a simple predictor that can price a full distribution of task specifications and thinking effort configurations from a single cheap probe on an unseen task within $36\%$, improving over prior work in predicting token spend. Our work provides initial results quantifying the effects of task specification on agentic token spend and introduces a method that can be used to systematically evaluate the cost of AI coding workflows.

---


### 95. [DCGC: Draft-Conditioned Global Correction for Complex Reasoning with Masked Diffusion Models](https://arxiv.org/abs/2608.25428)

**<font color=#1a73e8>作者：</font>** Minhae Oh, Nakyung Lee, Jungwoo Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Correcting flawed reasoning traces remains a significant challenge for Large Language Models (LLMs), whose autoregressive generation can propagate early mistakes into subsequent reasoning. We introduce DCGC, a Masked Diffusion Model (MDM) framework for global correction that uses an imperfect solution draft from an upstream solver as auxiliary context. DCGC combines task-specific Supervised Fine-Tuning (SFT) with a novel inference-time mechanism called Dynamic Dual-CFG. This mechanism separates problem-only and joint problem-draft branches and scales the draft-conditioned residual using a relative confidence gap. Across math, code, and knowledge reasoning benchmarks, DCGC outperforms standard sampling and simpler CFG variants, with additional results suggesting transfer to different diffusion backbones. In test-time setting where ground-truth failure labels are unavailable, DCGC improves full test set accuracy by correcting low-consensus upstream outputs, highlighting its utility as a verifier-free global correction module for difficult reasoning instances.

---


### 96. [Distance Is Not Enough: Forget-Retain Alignment Gap Predicts LLM Relearning Robustness](https://arxiv.org/abs/2608.25429)

**<font color=#1a73e8>作者：</font>** Yi Chen, Hanna Hsieh, Shuhong Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to make a model forget specific data, yet unlearned LLMs often fail to stay unlearned: brief fine-tuning can revive removed knowledge. Existing robustness predictors rely on global weight-space displacement, but distance alone can be misleading when random or destructive updates collapse performance. We argue that relearning robustness depends on update structure: robust unlearning should affect forget-critical weights while sparing retain-critical ones. We introduce the Forget-Retain Alignment Gap (FRAG), a training-free predictor that scores an update's forget-retain alignment without running a relearning attack, and separates selective from dense updates more reliably than global distance. Building on the forget-critical, retain-sparing principle, Forget-Retain Pruning (FRP) improves relearning robustness. Our results suggest that weight selectivity better explains robustness than distance alone. Code is available at this https URL.

---


### 97. [Here is a GIFT: Enforcing User Data Isolation in LLM Serving via GPU Information Flow Tracking](https://arxiv.org/abs/2608.25431)

**<font color=#1a73e8>作者：</font>** Jiacheng Shi, Xunjie Wang, Cheng Tan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM serving frameworks process large volumes of user data--often containing sensitive information--on shared infrastructure. Ensuring isolation between users who share the same serving framework (on CPUs) and LLM operators (on GPUs) is critical for privacy protection.
This paper presents GIFT, a GPU Information Flow Tracking system that enforces user data isolation in LLM serving with minimal overhead. Moreover, the design of GIFT is non-intrusive and allows CPU-side serving frameworks to evolve freely. It rests on two key insights. First, encryption-as-isolation leverages the observation that CPU components only orchestrate data flow, not content manipulation; thus, per-user encryption can provide isolation without modifying serving logic. Second, GPU kernels exhibit limited and predictable information flows, enabling static flow analysis. GIFT precomputes information flow rules for each kernel and uses decoupled flow tracking, avoiding instrumentation or GPU stalls.
Furthermore, we extend GIFT to GIFT-CC, which integrates confidential computing to protect against untrusted operating systems and hypervisors (LLM service providers). Implemented on vLLM and DistServe, GIFT and GIFT-CC enforce user data isolation with a 4-10.7% throughput overhead while maintaining the same latency level.

---


### 98. [MathAdv: What Theorem Provers Know, Reason, Formalize, and Generalize](https://arxiv.org/abs/2608.25449)

**<font color=#1a73e8>作者：</font>** Jiaxin Yuan, Connor Martinez Lockhart, Xiaoyu Liu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Formal theorem proving enables machine-verifiable evaluation of mathematical reasoning, yet existing benchmarks often emphasize aggregate proof accuracy, concentrate on a narrow range of mathematics, and provide limited evidence of robustness to equivalent reformulations. We introduce MathAdv, a diagnostic benchmark spanning 13 domains across undergraduate- and graduate-level mathematics. Alongside Lean 4 theorem proving, MathAdv provides up to three auxiliary tasks: multiple-choice questions that probe mathematical knowledge, fill-in-the-blank problems that isolate informal reasoning, and expert-crafted transformations that test robustness to problem presentation. Our evaluation of contemporary theorem provers yields four findings: formalization remains a major bottleneck; performance varies substantially across mathematical domains; natural-language guidance helps general-purpose LLMs but can hinder proof-specialized models; and mathematically equivalent reformulations expose substantial robustness limitations. Together, these results show how component-wise evaluation can reveal model capabilities and failure modes that aggregate theorem-proving accuracy obscures. The dataset and evaluation scripts are available at this https URL.

---


### 99. [VGA-BenchV2: An Expanded Unified Benchmark and Multi-Model Framework for Evaluating Video Aesthetics and Generation Quality](https://arxiv.org/abs/2608.25452)

**<font color=#1a73e8>作者：</font>** Longteng Jiang, DanDan Zheng, Qianqian Qiao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce VGA-BenchV2, an extended human-aligned benchmark and optimization framework for jointly evaluating and improving video generation quality and aesthetic value. Built upon VGA-Bench, VGA-BenchV2 preserves the original fine-grained taxonomy with two primary dimensions-Aesthetic and Generation-and 52 sub-dimensions. Guided by this taxonomy, we curate 1,016 diverse prompts and collect over 60,000 videos generated by 12 mainstream video generation models. More importantly, VGA-BenchV2 substantially expands human-labeled supervision by adding 36,000 task-level annotations, including 16,200 for aesthetic quality, 13,200 for aesthetic tagging, and 6,600 for generation quality, corresponding to 13.46x, 11.15x, and 1.55x scale-ups over VGA-Bench, respectively. Leveraging this enlarged annotation corpus, we develop a hybrid evaluator architecture consisting of VAQA-Net for continuous aesthetic scoring and two Qwen-based Large Vision-Language Model evaluators, VTag-Net and VGQA-Net, for aesthetic tagging and generation quality assessment. Extensive experiments demonstrate strong alignment with human judgments across diverse generation models. Beyond evaluation, VGA-BenchV2 further introduces an evaluation-to-optimization pipeline, where the learned aesthetic evaluator serves as a reward model for reinforcement learning-based generator fine-tuning. This closes the loop from benchmark construction and human supervision to automated evaluation and model optimization, enabling video generators to improve not only in realism but also in aesthetic quality and human preference alignment. Resources are available at this https URL.

---


### 100. [Training Alignment Auditors via Reinforcement Learning](https://arxiv.org/abs/2608.25460)

**<font color=#1a73e8>作者：</font>** Paul Rosu, Rowan Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Alignment auditing of frontier models increasingly relies on LLM auditors to surface undesirable behaviors at scale, but current automated auditors can struggle with coherent investigation and audit realism. In this work, we improve LLM auditors with reinforcement learning. In our best training environment, the policy investigates target models that potentially possess hidden behaviors planted via their system prompt. An LLM judge, which knows whether the target has a hidden behavior, holistically compares the policy's investigation to a reference investigation to determine the reward. With systematic ablations, we find that pairwise rewards yield more robust training compared to pointwise rewards, and that adding targets without planted behaviors helps maintain a low false positive rate. Training improves investigation quality against targets with planted behaviors, the rate of concerning behaviors surfaced in unmodified production models, and audit realism, while false-positive rates stay below 1%. Furthermore, auditing capabilities generalize across scaffolds: performance on AuditBench's adversarially fine-tuned targets substantially improves [Sheshadri et al., 2026].

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-209](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
