# 📦 其他研究 | 2026年10月07日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**551-571**（第 12/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-571**

---

### 551. [To Learn is to Wander: Learning Across Graphs and Tasks with Random Walks](https://arxiv.org/abs/2610.06694)

**<font color=#1a73e8>作者：</font>** Louis Tichelman, Xingyue Huang, Jinwoo Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph foundation models aim to transfer across graphs, feature spaces, relational schemas, and prediction tasks, yet existing approaches typically generalize only within particular graph modalities or tasks. We propose Wander, a graph foundation model designed to operate across these settings within a single pretrained checkpoint. Following the prior-predictive perspective, we formulate graph learning as completion of a partially observed graph. We realize this task-general view through a common interface based on random walks, allowing the same model to operate across homogeneous and multi-relational graphs with varying features, labels, and relational schemas. Wander can increase its structural context at inference time without changing its learned parameters and, under suitable assumptions, universally approximates the corresponding Bayes-optimal predictor on bounded connected graphs. Empirically, a single pretrained checkpoint achieves state-of-the-art or highly competitive results across node classification, homogeneous link prediction, and knowledge-graph link prediction. Moreover, joint pretraining across graph modalities and tasks preserves performance in specialized settings while enabling positive transfer and the composition of separately learned capabilities at inference time.

---


### 552. [Extending Dynamic World Surface Water Mapping to Sentinel-1 with AlphaEarth Embeddings](https://arxiv.org/abs/2610.06704)

**<font color=#1a73e8>作者：</font>** Rohit Mukherjee, Frederick Policelli, Beth Tellman 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic World (DW) maps land use and land cover globally at 10 m from Sentinel-2 (S2) imagery, but only for cloud-free observations, which limits where and when surface water can be mapped. We use the DW water class as weak supervision for a Sentinel-1 (S1) synthetic aperture radar (SAR) model so that DW-like water maps can be produced for every S1 acquisition. Google's AlphaEarth Foundations (AEF) annual embedding supplies spatial context, while S1 backscatter supplies the acquisition-time observation. On 53 globally distributed scenes with independent annotations of 3 m PlanetScope imagery acquired within 48 h of the S1 overpass, the S1-only model already reaches a pooled water intersection over union (IoU) of 0.77, comparable to 0.75 for the operational OPERA DSWx-S1 product, and adding AEF raises it to 0.85. The fused model improves on the S1-only model on 44 of 53 scenes and exceeds OPERA on 48, and on the independent S1S2-Water benchmark it reaches 0.94, compared with 0.87 for OPERA. Optical land-cover products can thus provide scalable training labels for SAR surface water mapping.

---


### 553. [SAFE-MR: Evidence Sufficiency Learning for Selective Multimodal Rumor Detection](https://arxiv.org/abs/2610.06708)

**<font color=#1a73e8>作者：</font>** Shiwen Ni  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal rumor detectors increasingly rely on retrieved evidence, yet relevant evidence is not necessarily sufficient for verification. Missing provenance, duplicated reports, and unresolved contradictions can produce confident predictions without adequate support. We introduce SAFE-MR, a framework that separates claim veracity from evidence sufficiency. The method decomposes image-text posts into verifiable claims, constructs a relation-aware claim-evidence graph, and aggregates evidence using provenance and contextual compatibility. Separate veracity and sufficiency heads support selective prediction, while evidence interventions encourage stability under irrelevant additions and sensitivity to evidence removal. On NewsCLIPpings, VERITE, and XFacta, SAFE-MR achieves macro-F1 scores of 91.2%, 75.8%, and 85.2%, respectively. Against the matched backbone with evidence, its macro-F1 gains are 2.2, 4.9, and 4.8 percentage points. On the diagnostic selection set, SAFE-MR reduces AURC from 0.105 for maximum-probability rejection to 0.075 and lowers error at 80% coverage from 13.8% to 8.5%. Evidence-perturbation and ablation results support the role of sufficiency learning and intervention training in improving selective verification.

---


### 554. [Domain adaptation of Russian ModernBERT for long legal documents](https://arxiv.org/abs/2610.06715)

**<font color=#1a73e8>作者：</font>** I. Litvak, D. Gvozdetsky, F. Lashkin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate whether continued pretraining on Russian legislative documents improves a Russian ModernBERT encoder on legal text. The adapted model, RuModernBERT-ruLaw, was trained on a corpus reported to contain 304,382 legislative documents and 194,425,905 corpus tokens. Corpus token counts are distinguished from positions produced by the model tokenizer. We compare the original and adapted encoders on a fixed external collection of 1,031 court-decision segments. Both models receive the same hidden positions in each of five masking realizations. At maximum input lengths of 512, 2,048, and 8,192 tokens, mean masked-token cross-entropy decreases by 0.10942, 0.07052, and 0.06604 natural-log units, respectively. The reported 95% intervals summarize sensitivity to masking on this fixed collection; they do not quantify uncertainty across document collections. A second evaluation addresses legal-entity extraction. The original and adapted models achieve entity-level F1 scores of 0.99852 and 0.99820. However, 99.95% of test spans have the same normalized surface form and class in the training split. This evaluation therefore provides limited evidence about transfer to previously unseen forms. The paper explains the masking objective, overlapping windows, averaging rules, and exact entity-boundary scoring using editable diagrams and clearly marked illustrative examples. The comparison supports lower masked-token prediction loss for the studied pair of models and collection. It does not isolate the contribution of distant context or establish practical legal utility.

---


### 555. [Decoupling Time and Space: A Temporally Conditioned Refinement for EEG Source Imaging](https://arxiv.org/abs/2610.06726)

**<font color=#1a73e8>作者：</font>** Marco Morik, Jesse Palarus, Carmen Vidaurre 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) offers millisecond temporal resolution, but inferring underlying neural sources is a severely ill-posed spatial inverse problem. While deep learning has advanced spatial reconstruction, current architectures face a critical dilemma: frame-by-frame models discard vital temporal context, whereas full 4D spatiotemporal networks introduce an architectural trade-off between reconstruction accuracy and inference cost. We propose a novel two-stream framework that explicitly decouples global temporal representation learning from per-time-point spatial refinement. A Transformer-based Temporal Condition Encoder processes the entire EEG sequence via factorized spatiotemporal attention, retaining sensor-resolved features. A fixed inverse then maps these features into source-indexed conditioning for a per-timestep Source-Space Transformer or volumetric convolutional refiner. Extensive evaluations on realistic synthetic data demonstrate that this temporal prior dramatically improves spatial localization, outperforming classical and spatiotemporal baselines, particularly in high-noise and multi-source regimes. Training across diverse leadfields and explicit operator mismatches improves transfer to unseen head geometries and brings template-based reconstruction closer to subject-specific inversion. Furthermore, we apply the model trained only on synthetic EEG data to real-world EEG. A logistic regressor fit on source power differences in eyes-open, eyes-closed conditions successfully decodes age groups.

---


### 556. [ufakzeka-karar: An Open Turkish Typed-Decision Model with Order-Invariant Option Scoring](https://arxiv.org/abs/2610.06744)

**<font color=#1a73e8>作者：</font>** Sait Furkan Teke  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> ufakzeka-karar is an open Turkish decision model with 182,494,466 parameters. Given a Turkish text and questions of a fixed answer type (a choice, a level on an ordered scale, or yes or no), it returns a temperature-scaled probability for every option and an expected error that serves as a "not sure" signal, without generating text and in one CPU forward pass for up to ten options. Built on the lab's ufakzeka-1-base, its head scores each option blind to the others at shared positions, so the answer does not depend on option order. A sequential head trained with shuffled options was about as accurate but changed 2.3 to 2.8 percent of its answers when only the option order changed; REINFORCE lost 10.2 points (0.102) of macro F1 to cross-entropy. On the open set of HakemBench v1.0 (4,275 questions, 7 tracks) the released model ranks 7th of 16 rows with a composite of 0.660 (95% interval 0.642 to 0.677). Temperature scaling lowers calibration error (smooth ECE) on the development set but raises it on held-out support questions, from 0.027 to 0.045 for the first scored run, which never trained on them; the released model later trained on them, so its 0.036 to 0.064 is not an unseen-question test. The released model is the last of three runs scored on HakemBench, and its numbers are not blind. The second run's new training data was aimed at the first run's errors on the full test set in guardrails, moderation and customer support, and the released run was trained after the second run's guardrail results on the full test set were read, under a protocol fixed in writing before any of its data, code or runs. All its numbers come after these readings; its guardrail, moderation and customer support numbers carry the flag "shaped by reading the test results". With every model scored on the other four tracks only, its composite is 0.678, 6th of 16. Weights and code are under Apache-2.0.

---


### 557. [Hyperbolic Graph Representation Learning: Embed in One Metric, Optimize with Another](https://arxiv.org/abs/2610.06745)

**<font color=#1a73e8>作者：</font>** Federico Larroca, Paola Bermolen, Marcelo Fiori 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hierarchical graphs embed in hyperbolic space with lower distortion than in Euclidean space owing to its negative curvature. However, their gradient-based learning is hampered at large radii, where the Poincaré ball and the Lorentz hyperboloid models fail numerically. Polar coordinates avoid this problem, but the hyperbolic metric scales the angular step by the hyperbolic sine of the radius, freezing angular motion. We observe that this factor is a choice, silently fixed by existing implementations: the Euclidean tangent parametrization, for instance, uses the radius itself. We show that other choices are not only possible but preferable. They are endpoints of a one-parameter family of optimization preconditioners with curvatures from $-1$ to $0$, while the embedding remains at curvature $-1$. We show that since the Euclidean preconditioner rearranges a layout but refines it poorly, while an intermediate one refines far better once a layout is in place, combining them in two stages reduces the loss on real-world trees by 46-74% over the best single curvature.

---


### 558. [On Learning Optimal Corners in Orthogonal Partially Observable Cooperative Guard Art Galleries](https://arxiv.org/abs/2610.06777)

**<font color=#1a73e8>作者：</font>** Yassin Ben Mansour, Edwin Meriaux  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The CADENCE algorithm solves the Partially Observable Cooperative Guard Art Gallery Problem (POCGAGP) with formal coverage and connectivity guarantees, but leaves unspecified which valid corner each agent should be deployed to, a choice that strongly affects efficiency. We introduce two learned corner-selection heuristics that preserve these guarantees: a CNN scoring candidates on a grid encoding, and a GATv2 network trained with Deep Q-Learning (DQN) on a visibility graph. Across 7,500 runs on random orthogonal environments (50x50 to 250x250), our heuristics outperform baseline CADENCE in both steps to full coverage and peak agent count, with gains growing with scale, and improve on Incremental Self-Deployment (ISDA) baselines in agent utilization while providing guarantees ISDA lacks. Learned corner selection thus improves CADENCE in speed and agent utilization at no cost to its formal properties.

---


### 559. [IdeaLens: Detecting AI Ideas in Long-form Writing](https://arxiv.org/abs/2610.06778)

**<font color=#1a73e8>作者：</font>** Rishanth Rajendhran, Minjoon Choi, Jenna Russell 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While modern AI detectors identify who wrote the words, emerging policies on AI use increasingly hinge on a different question: who came up with the ideas? We introduce IdeaLens, a detector that identifies whether a document's ideas came from a human or AI (idea provenance), regardless of who wrote its words. To focus IdeaLens on ideas rather than prose, we represent documents as outlines: lists of items that each pair a discourse role with a brief, paraphrased description of the content, minimizing word-level overlap with the raw text. We train IdeaLens on 1M FineWeb documents with silver labels from Pangram, a prose provenance detector. Since the outlines are largely stripped of surface-level information, the labels must be fit mainly through the ideas. In a controlled study, IdeaLens's AI flag rate drops from 95% to 7% as models write from increasingly detailed human plans, while Pangram 4 still flags 92%; from AI-derived plans, IdeaLens stays above 96%. Conversely, on a new dataset of 50 stories that human authors wrote from AI-generated plans, IdeaLens flags 68% of the stories as AI, compared to 8% for Pangram 4. On a comprehensive suite of 19 existing detection benchmarks, we show that IdeaLens maintains strong detection rates at low false positive rates, suggesting that ideas themselves provide a powerful discriminative signal, and its performance holds across domains, formats, and languages. Finally, we examine 90K predictions from IdeaLens to characterize systematic differences between human and AI ideation. We release our models and labeled datasets to facilitate future research on idea provenance detection.

---


### 560. [Round-Trip KNN Clustering: multiscale hierarchical cluster detection on directed nearest-neighbour graphs](https://arxiv.org/abs/2610.06795)

**<font color=#1a73e8>作者：</font>** Eraldo Pereira Marinho, Caetano Mazzoni Ranieri, Fabricio Aparecido Breve  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Round-Trip KNN Clustering (RTKNNC), a graph-based method for finding cluster structure at several neighbourhood scales without requiring the number of clusters in advance. Unlike approaches that first make a $k$-nearest-neighbour (KNN) graph undirected, RTKNNC keeps both directions of the neighbour relation: which points a given point selects and which points select it. Incoming selections are treated as weighted votes that help decide which local connections remain visible during a recursive forward-and-reverse traversal. Repeating the procedure for increasing $K$ reveals how groups persist or merge as the neighbourhood scale grows; for the reference inverse-square model before structural refinement, clusters can merge but do not split. Because graph connectivity can occasionally join distinct groups through a sparse bridge or a small region of overlap, we add an optional label-free refinement. It first tests whether an already formed component is better described by two or three Gaussian subpopulations, and accepts a subdivision only when the proposed groups are large enough and consistent with the visible KNN graph. Across eight synthetic datasets and $K=2,\ldots,16$, independent C and Python implementations produced identical partitions in all 120 reference runs. Refinement increased adjusted Rand index from $0.7817$ to $0.9627$ on a variable-density benchmark and from $0.8083$ to $0.9853$ on a sparse-bridge benchmark. Comparisons with seven external clustering methods show competitive performance while preserving a label-free cluster-construction process.

---


### 561. [MC-Sparse: Deconstructing and Closing the Dense-Sparse Attention Gap in Diffusion Transformers](https://arxiv.org/abs/2610.06801)

**<font color=#1a73e8>作者：</font>** Jiarui Chen, Zeqiang Lai, Jiangshan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse attention is a primary approach to reducing the latency of diffusion transformers in long-sequence generation tasks, such as video and high-resolution 3D asset generation. However, existing methods can degrade generation quality and fidelity at high sparsity levels. Through controlled oracle comparisons, we trace this degradation to three sources: constraints imposed by token grouping, inaccurate interaction selection, and the attention contributions lost when tokens are discarded. Guided by this analysis, we propose Meta-Cached Sparse Attention (MC-Sparse), a training-free framework that selects individual key-value (KV) tokens while organizing similar queries into tile-aligned groups for efficient GPU execution. MC-Sparse caches metadata comprising query groups, KV indices selected using exact attention probabilities, and residuals between dense and sparse attention outputs, and reuses them across subsequent denoising steps. Across video and 3D generation models, MC-Sparse achieves higher fidelity to dense-attention outputs and larger denoising speedups than existing sparse-attention baselines, without visible quality degradation. Relative to dense attention, it delivers a $1.80\times$ denoising speedup on Minimax-H3-Base and a $2.32\times$ speedup on 3D asset generation, both with negligible quality loss.

---


### 562. [H-JEPA: End-to-End Learning of Hierarchical World Models for Visual Planning](https://arxiv.org/abs/2610.06805)

**<font color=#1a73e8>作者：</font>** Wancong Zhang, Basile Terver, Michael Rabbat 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon planning with latent world models requires reasoning across timescales and levels of abstraction. Existing task-agnostic JEPA world models predict and plan at a single timescale or with multiple horizons in one shared latent space. We introduce H-JEPA, an end-to-end recipe for training a hierarchy of action-conditioned JEPAs in which each level predicts farther ahead in its own learned latent space. Planning proceeds top-down: the top level optimizes progress toward the goal, and each level's predictions become subgoals for the planner below it. When factors in the data evolve at separated timescales, higher levels discard fast, unpredictable detail and retain slower task-relevant state. Across four simulated navigation and manipulation environments, hierarchical planning improves over a flat JEPA; on Visual AntMaze, a three-level hierarchy raises success from 18% to 73% using less planner compute. Ablations attribute these gains to both temporal decomposition and higher-level goal representations. With inverse-dynamics supervision, the approach extends to diverse real-robot videos from DROID, where hierarchy improves offline planning fidelity at lower planner compute.

---


### 563. [Block Disentanglement in CRL: Bridging Identifiability and Visual State Estimation](https://arxiv.org/abs/2610.06809)

**<font color=#1a73e8>作者：</font>** Emre Acartürk, Pranamya Kulkarni, Puranjay Datta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal representation learning (CRL) is the process of recovering causally-related latent variables from high-dimensional observations. As a label-free inference method, CRL is particularly attractive for applications where data labels are unavailable or impractical to obtain. While there has been significant progress in understanding the identifiability guarantees of CRL, such guarantees often hold under highly stylized assumptions, which temper the direct application to real-world problems. This paper has a two-fold objective for interventional CRL. First, it establishes identifiability guarantees for substantially weaker interventional assumptions, resulting in block disentanglement of the causal variables, where the block structure depends on the realistically available intervention mechanisms. Secondly, the block disentanglement framework is used for embodied visual state estimation, in which the objective is to recover the latent physical variables of a robotic system directly from visual data (images and videos) without labeled data. These two components are critically complementary. The block disentanglement theory delineates identifiability guarantees under weakened assumptions, and the application demonstrates that the resulting objective remains effective in a controlled embodied setting despite further assumption violations, providing a theory-to-practice bridge needed to translate the promise of label-free CRL into practical problems.

---


### 564. [TAPDreamer: Transferable Adversarial Patches for World Action Models](https://arxiv.org/abs/2610.06814)

**<font color=#1a73e8>作者：</font>** Xuanyu Lu, Fengqing Jiang, Kaiyuan Zheng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models learn to predict how their environment will evolve, making them an important foundation for general-purpose robotic control. Yet world action models depend on camera inputs whose manipulation can corrupt the visual representations used across tasks and action policies. Existing attacks on these models optimize against the victim's actions or predicted futures and therefore require access to target-model outputs. In this paper, we propose an attack, TAPDreamer, against world action models that instead uses a public encoder alone to construct a fixed local perturbation that transfers across tasks and action architectures. TAPDreamer requires no target-policy queries. Our key insight is that interactions between patch-induced changes in attention weights and value vectors broadcast a nearly identical representation shift far beyond the patch footprint, and this shift remains stable across task observations. Guided by this insight, TAPDreamer uses six frames from one source task to maximize the global L1 distance between clean and patched encoder representations. In closed-loop evaluation, one frozen patch per benchmark, covering about 6.5% of the input, reduces FastWAM's success rate from 97.7% to 0.0% across 40 LIBERO tasks and from 90.8% to 0.0% across 50 RoboTwin tasks; matched random patches retain 81.5% and 79.2% success. The same patches reduce success to 2.1% and 0.8% on two DreamWAM configurations and to 10.0% on Motus. These results show that protecting downstream action generation alone is insufficient: defenses for world action models must also secure shared visual encoders against persistent local perturbations.

---


### 565. [Private online learning and prediction for Littlestone classes](https://arxiv.org/abs/2610.06822)

**<font color=#1a73e8>作者：</font>** Amartya Sanyal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study mistake bounds for differentially private online learning and online prediction under oblivious realisable adversaries. Online learning requires the learner to release a hypothesis at each time step whereas in online prediction, the learner only needs to make predictions without releasing a hypothesis. Using a novel lower bound for private online learning and an upper bound for private prediction, we show that the sample complexity of these two problems are separated by a factor that grows with the time horizon for every class of finite Littlestone dimension $d$. First, we prove that every $\br{\epsilon,\delta}$-private online learner has a deterministic realisable stream of length $T$ on which the mistake bound is at least $\bE\bs{M_T}=\Om{\frac d\epsilon \log\br{ T}^{2/3}}$. In particular, this is the first non-trivial lower in the range $1/T<\delta<1/\log T)$ left open in earlier works[SR22,DSS24,LWY24]. Second, we prove that for every class of of Littlestone dimension $d$, there exists an $(\epsilon,\delta)$-jointly private predictor with at most $2^{2^{cd^2}}\epsilon^{-2}\log^2\br{2/\br{\epsilon\delta}}$ expected mistakes, independently of $T$, for some absolute constant $c>0$. Thus, for every fixed class of finite Littlestone dimension when $\delta=\Theta\br{1/\log T}$, private learning requires $\Om{\br{\log T}^{2/3}}$ expected mistakes, whereas private prediction admits $\bigO{\br{\log\log T}^2}$.

---


### 566. [Deep Learning for Sleep Heart Rate Estimation from Accelerometers: Toward Population-Scale Cardiac Insight Without Optical Sensors](https://arxiv.org/abs/2610.06823)

**<font color=#1a73e8>作者：</font>** Tanbin Islam Rohan, Pranjol Sen Gupta, Tanusree Debi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large longitudinal cohorts often contain wrist accelerometry without optical heart-rate sensing, motivating recovery of cardiac information from motion signals already collected during sleep. We present SeqSmoother, a transformer-based temporal corrector for sleep heart rate (HR) estimation from wrist accelerometry. SeqSmoother combines spectral descriptors with an intermediate Nightbeat-derived frequency anchor and a physics-motivated sub-harmonic feature designed to identify harmonic frequency lock-on. All inference-time features are derived from wrist accelerometry, while ECG is used only to construct reference HR labels and training-label quality weights. We evaluate SeqSmoother using 13 participant-disjoint held-out folds and compare it with the official Nightbeat implementation under a matched 60-s window and 15-s step protocol. Across all out-of-fold predictions, SeqSmoother achieved a participant-macro MAE of 1.60 bpm. On Nightbeat-retained matched intervals, Nightbeat achieved lower absolute error than SeqSmoother (0.615 versus 1.091 bpm), while SeqSmoother provided estimates over a larger portion of the eligible recording; Nightbeat produced final estimates for 72.85% of the SeqSmoother-eligible out-of-fold grid. Separately, the proposed sub-harmonic ratio achieved an AUROC of 0.972 for identifying reference-defined harmonic lock-on candidates. These findings reveal an accuracy-availability trade-off between learned temporal modeling and quality-gated signal processing while providing empirical support for a physics-informed approach to identifying frequency-tracking failures in accelerometer-based sleep HR estimation.

---


### 567. [TasteVal: Measuring the Experimental Research Taste of AI Systems Against Human Experts](https://arxiv.org/abs/2610.06824)

**<font color=#1a73e8>作者：</font>** Oliver Jaffe, Dane Sherburn  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce TasteVal, a benchmark to evaluate the experimental research taste of frontier models. We define research taste as the ability to pick interesting problems to solve, design experiments, and interpret experimental results. TasteVal measures the experimental component of research taste; given a fixed research problem, we measure how well a model iteratively designs experiments and draws conclusions from their outcomes. We operationalize experimental research taste as compute efficiency; a Researcher who reaches the same score as an expert human using half the serial experimental compute has twice the experimental taste. Experimental taste thus acts as a multiplier on experimental compute, making it a key input to forecasts of AI progress. TasteVal consists of 8 novel, challenging, open-ended tasks representative of frontier AI R&D. To isolate taste from coding ability, the model under evaluation acts as a Researcher that iteratively designs experiments while a fixed Coder agent implements them and reports their results. The Researcher executes until either the 40 H100 hour or 120 wall-clock hour budgets are exhausted. We recruit 24 human experts, at least 2 per task, and take the best expert attempt per task as the expert baseline. We evaluate 20 models released between 2023 and 2026. The best-performing model, Opus 5.5, exceeds our expert baseline, with a compute multiplier of 2.3x (95% CI 1.15-4.37), at roughly 1/30 of our baseliners' average per-run cost. On TasteVal, the compute multiplier of frontier models has doubled approximately every 3.0 months since December 2025 (95% CI 1.7-5.0), up from every 14 months between 2023 and December 2025. Measured by final normalized performance, frontier models show no trend break, doubling every 14.6 months. To keep TasteVal uncontaminated, we do not release the tasks.

---


### 568. [UniSlider: Perceptually Uniform Sliders for Continuous Image Editing](https://arxiv.org/abs/2610.06831)

**<font color=#1a73e8>作者：</font>** David Serrano-Lozano, Duygu Ceylan, Yannick Hold-Geoffroy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sliders provide an intuitive interface for continuous image editing. In current generative approaches, however, the slider is simply a rescaling of the method's strength parameter, such as an adapter coefficient, a prompt weight, or an interpolation factor. This strength relates poorly to perceptual change. The image can partially revert as the slider moves, long stretches of the range produce no visible difference, and short intervals transform the image abruptly. Remapping the strength could fix this uneven pace, but only if the trajectory is monotone, which current methods do not enforce. We therefore distinguish the slider from the strength, and require perceptual distance from the input to grow linearly with the slider value. We introduce UniSlider, a lightweight LoRA trained on a few-step editing backbone so that its strength approximates this ideal slider. Few-step sampling lets us impose this objective in pixel space without intermediate ground truth, and the backbone's output is preserved at full strength. However, a low-rank adapter cannot make the strength fully uniform. Our slider is thus an inference-time remapping of the strength, obtained by adaptive sampling. Since training optmizes to make the trajectory monotone, this remapping closes the remaining gap without extra training or parameters. On a new benchmark of 300 continuous edits evaluating uniformity, monotonicity, edit fidelity, and identity preservation, UniSlider outperforms all prior methods and is preferred in a user study.

---


### 569. [Anatomy-aware Fine-grained Multimodal Fusion for Laryngopharyngeal Cancer T-Staging Prediction Using CT and Radiology Report](https://arxiv.org/abs/2610.06837)

**<font color=#1a73e8>作者：</font>** Xingyue Zhao, Yanzhou Su, Fang Zhang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate T-staging is crucial for guiding personalized treatment strategies for laryngopharyngeal cancer. However, current clinical practice relies on invasive biopsy procedures, whereas CT-based staging remains challenging due to the complex patterns of tumor invasion. Recent computer-aided approaches face two key challenges: 1) Structural relationship modeling: existing methods underrepresent anatomically structured patterns of tumor invasion, as they either process whole CT volumes without tumor-specific anatomical constraints or rely on labor-intensive tumor segmentation. 2) Fine-grained cross-modal alignment: while radiology reports contain organ-specific invasion details, current methods that apply global feature fusion struggle to accurately align individual anatomical structures with their corresponding textual descriptions. To address these issues, we propose an anatomy-aware multimodal framework that integrates organ-level CT context and radiology reports into a unified representation for laryngopharyngeal T-staging. The framework first constructs an Anatomy-Structured Organ Graph (AOG) that captures invasion patterns between primary sites and surrounding organs, then performs Organ-Anchored Cross-Modal Alignment (OCA) so that each organ node aggregates textual evidence from the radiology report, and finally refines this graph representation by injecting organ-specific invasion cues extracted from the report via Report-Enhanced Graph-Refinement (REG), yielding a multimodal organ graph that combines spatial and textual evidence. Extensive experiments demonstrate that the proposed framework achieves superior performance in T-staging of laryngopharyngeal cancer.

---


### 570. [BiasFlow: Geometric Monitoring and Backbone Regularization for Spurious Feature Reliance](https://arxiv.org/abs/2610.06846)

**<font color=#1a73e8>作者：</font>** Haojin Deng, Zhiping Lin, Yimin Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Worst-group accuracy (WGA) evaluates a trained predictor but does not characterize how its frozen backbone behaves when a new head is learned. We introduce BiasFlow, a hook-based toolkit for monitoring class-attribute centroid alignment (IBMI), within-class centroid separation (W-IBMI), and feature-projection sensitivity. IBMI is confounded by class-attribute correlation and is not a measure of causal feature reliance. We pair these diagnostics with BiasFlow Regularization (BFR), a supervised, composable class-conditional centroid-alignment penalty. W-IBMI verifies the quantity BFR optimizes; it is scale dependent and does not independently establish attribute removal. Across the reported small-scale benchmarks, adding BFR improves or preserves mean WGA, with gains up to +26.0 pp on UrbanCars. The principal independent stress test freezes CelebA-Std backbones and trains fresh heads on biased data: BFR+GroupDRO improves WGA from 40.7% to 64.1%, while Male probe accuracy decreases from 92.5% to 72.2%. Attribute information remains recoverable, and cross-task results are mixed. A controlled synthetic-watermark ImageNet experiment additionally improves watermark-shift accuracy by +23.0 pp under matched training. These results support evaluating centroid geometry and resistance to biased head retraining alongside WGA, within the tested protocols.

---


### 571. [S2PD: Serial-to-Parallel Diffusion for Physically and Logically Consistent Video Generation](https://arxiv.org/abs/2610.06847)

**<font color=#1a73e8>作者：</font>** Jeffrey Hu, Daniel Olmeda Reino, Ayush Tewari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bidirectional video diffusion models denoise entire videos in parallel, yet when trained on effectively unlimited in-distribution data from procedural generators, continue to violate physical laws and simple symbolic rules. We introduce Serial-to-Parallel Diffusion (S2PD), which performs autoregressive diffusion at high noise before switching to parallel diffusion at low noise. The autoregressive phase provides the serial computation needed to coordinate interdependent events and produce valid state transitions while the parallel phase jointly refines the entire video and reduces sampling time relative to fully serial generation. We implement S2PD with two architectures: a pixel-space diffusion transformer trained from scratch and a pretrained video model adapted through LoRA fine-tuning with causal attention. Across games, physical simulations, and real video, S2PD follows rules more reliably than matched bidirectional baselines and generates videos with greater temporal stability and sampling efficiency than other serial methods.

---


> [!TIP]
> 当前位于：**551-571**（第 12/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-571**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
