# 📦 其他研究 | 2026年10月26日

> 本类共 **211** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-211](./part-05.md)

---

### 101. [Verus-Insight: Towards Explainable Artifact Detection in AI-Generated Videos](https://arxiv.org/abs/2610.30866)

**<font color=#1a73e8>作者：</font>** Zhuoran Zhang, Yang Shi, Qixun Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video generation have made synthetic videos increasingly realistic, placing greater demands on reliable AI-generated video detection. Existing artifact-based detectors typically identify generation artifacts as evidence for source prediction, yet they may either fail to recognize subtle artifacts or reach the correct source decision without faithfully identifying the evidence underlying it. In this work, we systematically investigate how to design and train effective artifact detectors and formulate artifact detection as a structured process comprising three complementary capabilities: Inspection Planning, which determines what should be examined; Evidence Verification, which verifies whether the inspected content exhibits genuine generation artifacts; and Evidence Aggregation, which integrates the verified evidence into the final source decision. Building on this formulation, we introduce Verus-Insight, trained with human-anchored full-process supervision and progressive capability training to strengthen both fine-grained artifact detection and video-level detection. We further introduce Verus-Bench, a benchmark with fine-grained human annotations of perceptible artifacts for evaluating artifact detection. Extensive experiments across diverse benchmarks demonstrate that Verus-Insight achieves strong performance in both fine-grained artifact analysis and AI-generated video detection, with substantial gains in recovering human-perceived artifacts. Further analyses reveal that the three capabilities are complementary yet distinct, and that Verus-Insight more reliably converts relevant inspection targets into supported artifact evidence without increasing spurious artifact claims.

---


### 102. [HimmBO: High-Dimensional Interactive Model-Merging Bayesian Optimization for Image Generation](https://arxiv.org/abs/2610.30875)

**<font color=#1a73e8>作者：</font>** Jinyuan Mao, Zhihao Shen, Chenxi Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-tuning has become a common way to customize text-to-image models, leading to community collections of over 100K lightweight adapters. Adapters sharing a base model can be merged with continuous coefficients. This turns a large collection into a high-dimensional continuous design space, which recent work explores interactively using preferential Bayesian optimization (PBO). However, existing approaches are limited to a few dozen preselected adapters and require expensive image generation in every interaction round. We introduce HimmBO, a two-stage method that scales preference-driven adapter merging to much larger collections while reducing image-generation cost. Its screening stage recovers the active adapter set through level-set estimation over pre-generated images, requiring no image generation. The refinement stage then optimizes merge coefficients in the recovered low-dimensional subspace. Both stages use a style-aware kernel, allowing preference information to transfer between visually similar adapters. In simulated-user image-matching experiments, HimmBO achieves higher final similarity than all comparisons while reaching a given similarity with under one tenth of the image generations required by prior work. Its performance remains stable as the collection grows to 1080 adapters, while competing methods degrade substantially.

---


### 103. [One Teacher, Many Views: Reducing Reference Sensitivity in On-Policy Self-Distillation](https://arxiv.org/abs/2610.30880)

**<font color=#1a73e8>作者：</font>** Khouloud Saadi, Di Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) improves reasoning by training a model on its own trajectories with dense token-level supervision from a privileged copy conditioned on a reference solution. Existing methods typically use a single teacher distribution conditioned on the complete reference. We identify a limitation of this formulation: a reference is only one realization of the reasoning process. Although it provides evidence about the answer, it also encodes an ordering, phrasing, and solution path. Full-reference conditioning can therefore produce correct targets that depend excessively on information unavailable to the student at inference. We show that replacing one valid reference with another, while holding the problem and student state fixed, can substantially alter the teacher distribution, a phenomenon we call reference-induced target instability. To address this instability, we introduce Monte Carlo Privileged Distillation (MCPD), which models privileged context as a distribution over partial reference views and distills the marginal teacher distribution. MCPD evaluates the teacher under multiple views and averages the resulting next-token distributions. We show that this probability-space average is the exact target induced by minimizing the expected teacher-to-student KL divergence over privileged views. Across mathematical and scientific reasoning benchmarks, we show that MCPD produces more reference-consistent supervision and consistently improves over full-reference OPSD.

---


### 104. [From Perpetrators' Digital Footprints to Behavioral Communities: An Ontology-Driven Framework for Bengali Cyberbullying Analysis--- FULL VERSION](https://arxiv.org/abs/2610.30885)

**<font color=#1a73e8>作者：</font>** Md. Nesarul Hoque, Md Hanif Seddiqui, Miskatul Anwara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cyberbullying involves behavioral and contextual patterns beyond isolated abusive messages. However, existing approaches remain fragmented across content detection, semantic representation, and network analysis, with limited interpretable perpetrator representations, multi-scale structural modeling, and explanations of behavior-driven similarity and influence propagation. These limitations hinder the identification of persistent perpetrators, characterization of behavioral communities, and assessment of potentially influential users. This paper proposes Ontology-Driven Cyberbullying Behavior and Network Analysis (ODCBNA), a perpetrator-centric framework integrating requirements-driven ontology design, knowledge graph construction, behavioral modeling, community analysis, and influence modeling. Using the Bengali Contextual and Diverse Cyberbullying (BenCoDiC) corpus as a use case, ODCBNA identifies $1{,}063$ users with at least three bullying comments or replies as perpetrators and represents each through a $64$-dimensional behavioral and contextual feature vector. Cosine similarity and $k$-nearest-neighbor modeling produce a weighted network with $27{,}554$ edges. Louvain analysis identifies six communities with a modularity of approximately $0.495$ and $27$ sub-communities. Feature-contribution analysis identifies the Video, Impact, and User Profile groups as the strongest contributors to behavioral similarity and community separation, while contextual dimensions support interpretation. Community-constrained influence analysis shows that IM Greedy achieves small positive gains in all six communities, although different seed-selection methods produce comparable diffusion spreads despite limited seed overlap. These findings provide an interpretable basis for understanding perpetrator behavior, community organization, and potential influence patterns in Bengali online environments.

---


### 105. [Parameter Learning in Active Inference via Variational Message Passing](https://arxiv.org/abs/2610.30899)

**<font color=#1a73e8>作者：</font>** Benedikt Waldeck  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Active inference casts perception, learning and planning as variational inference, where the Expected Free Energy (EFE) defines the planning objective. Recent work showed that EFE minimization can be written as Variational Free Energy (VFE) minimization on a generative model augmented with epistemic priors, and that the resulting entropy-corrected objective is minimized by sum-product message passing (SP-MP) on modified factor functions. These formulations treat model uncertainty as inference over a finite set of known models. We extend them to planning during learning, where beliefs over the observation and transition parameters $\theta_A$, $\theta_B$ are Dirichlet priors. Closed-form Dirichlet updates are usually obtained by a structured mean-field factorization between parameters and states, but under exactly that factorization the information-gain corrections vanish. We resolve this by giving every factor its own parameter prior, frozen during a rollout. Conjugacy then makes each factor belief a product of a marginal over the categorical variables and a one-step Bayes posterior of the parameters. This reintroduces the datum-dependent parameter posteriors that mean-field factorization destroys. We show that evaluating the epistemic priors under the resulting Bethe joint recovers the information gains. Stationarity of this single closed-form objective yields SP-MP whose factor functions are augmented by the information-gain weight. Experiments on two grid POMDPs, in which only a planner that learns the model finds the safe route, show that the method plans to efficiently learn $\theta_A$ and $\theta_B$. It reaches the goal on every episode, whereas SP-MP planners with the same inference update plateau or take the risky route.

---


### 106. [When Annotation Patterns Are Learned: Skin-Tone Dependence in Dermatology Concepts](https://arxiv.org/abs/2610.30901)

**<font color=#1a73e8>作者：</font>** Y. Li, M.Bigliardi-Qi, S. Bedros 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept bottleneck models (CBMs) let clinicians inspect and correct skin disease diagnoses through clinical concepts, but only if the concept annotations are reliable. We therefore audit the reliability of SkinCon, a widely used dermatology concept dataset, across skin tones. Within the same disease and with near duplicates removed, erythema is annotated far less often on dark than on light skin, with an odds ratio of 0.17. In contrast, hyperpigmentation and hypopigmentation are annotated more often, with odds ratios of 6.2 and 4.5, respectively. We refer to this pattern as tone-dependent concept annotation. An evidential concept model trained on these annotations learns the same pattern and reproduces it on unseen images. Such a model may agree with potential erythema omissions rather than contradict them. Consistent with this, three label error detectors underperform a disease-only baseline at finding erythema that dermatologist captions mention but SkinCon labels as absent. The three detectors are based on confident learning, training dynamics, and the model's own evidential uncertainty. Concept annotations should thus be audited within each subgroup before explanations built on them can be trusted.

---


### 107. [Beyond Phenotypic Similarity: Relation Refinement and Selective Population Graph Learning for Multimodal Brain Disorder Diagnosis](https://arxiv.org/abs/2610.30902)

**<font color=#1a73e8>作者：</font>** Yinyu Lan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Population graph learning supports brain disorder diagnosis by sharing information across subjects. Its effectiveness, however, depends on whether the relationships guiding this exchange are relevant to diagnosis. Similarity in demographic or acquisition attributes does not necessarily indicate diagnostic agreement, and heterogeneous subjects may require different representation updates within the same population graph. We propose PopDRP, a framework that combines diagnosis-guided relation refinement with hierarchical selective state-space learning. Using only training labels, Contrastive Affinity Refinement calibrates attribute-based affinities according to diagnostic agreement. Neural Graph Rectification then refines these relationships using fused functional-connectivity and non-imaging representations, guided by graph reconstruction and dual-view alignment objectives. On the resulting graph, a Selective Pyramid State-Space backbone integrates input-dependent state updates, graph diffusion, and hierarchical pooling and unpooling to learn population representations at multiple resolutions. Together, these components connect the refinement of inter-subject relationships with selective representation learning over the population graph. Experiments on ABIDE and ADHD-200 under stratified ten-fold cross-validation show improved accuracy and AUC over the compared baselines. Ablation studies further support the contributions of relation refinement and the selective hierarchical backbone to classification performance.

---


### 108. [Query-Time Calibration of CLIP Features for Open-Vocabulary 3D Segmentation](https://arxiv.org/abs/2610.30908)

**<font color=#1a73e8>作者：</font>** Dominik Engel, Yousef Rajeh, Leon Sick 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lifting vision-language features such as CLIP into 3D Gaussian reconstructions enables open-vocabulary segmentation through natural-language queries. Although CLIP represents a broad range of semantic concepts, the lifted features of individual scenes can exhibit strong directional concentration, while raw cosine similarity does not account for the scene-specific feature distribution. We show that substantial segmentation gains can be obtained by changing how a fixed lifted feature field is compared with text. Our method partially subtracts a shared scene direction from visual features and text prototypes and whitens text prototypes using a fixed reference vocabulary of generic terms. It then uses soft clustering for multiclass prediction and CSLS with a relevance margin against the reference vocabulary for single-query prediction. Beyond reducing directional concentration, scene centering improves class-relative feature separation in every evaluated scene. Across seven lifting methods and four datasets, the resulting query-time calibration consistently improves mean intersection over union in both multiclass and single-query segmentation. These gains require no retraining, source-image re-encoding, or feature re-lifting, demonstrating the value of scene-conditioned comparison for making better use of existing lifted representations.

---


### 109. [Hierarchical Fine-Grained Cross-Modal Alignment via Dynamic Granularity Discovery and Optimal Transport](https://arxiv.org/abs/2610.30912)

**<font color=#1a73e8>作者：</font>** Pengfeng Song, Shaozhong Zhang, Pengfei Shao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained image-text retrieval requires a model not only to assess global semantic consistency between an image and a text, but also to model visual evidence for local textual semantics, including objects, attributes, quantities, actions, and relations, so as to distinguish semantically similar candidates. Existing methods commonly use fixed image patches, detected regions, or text tokens as the basic matching units and then aggregate local interactions through max pooling, cross attention, or similarity accumulation. Such strategies remain limited in semantic unit construction and global matching consistency. This paper proposes a hierarchical fine-grained cross-modal alignment framework, termed HFCMA. The framework progressively transforms low-level patch and token representations into adaptive visual regions and textual phrases, and then performs structured region-phrase matching within a global retrieval scoring process. Specifically, HFCMA first adopts dynamic granularity discovery (DGD) to aggregate raw patches and tokens into semantically compact visual regions and textual phrases. It then formulates region-phrase matching as an entropy-regularized optimal transport problem, thereby estimating a structured alignment matrix under global marginal constraints. To reduce background noise and local semantic drift, HFCMA further introduces background debiasing, textual importance weighting, and prototype consistency regularization. Experiments on Flickr30K and MS-COCO show that HFCMA effectively combines dynamic semantic unit construction with OT-based structured matching under a dual-encoder retrieval framework. The resulting fine-grained score provides structured local alignment information for candidate ranking and improves the discrimination of subtle semantic differences.

---


### 110. [MIG-COW: Transferable Adversarial Attacks on Deepfake Detectors via Gradient Decomposition](https://arxiv.org/abs/2610.30914)

**<font color=#1a73e8>作者：</font>** Wonjune Seo, Joonhyuk Baek, Yeseong Jung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite recent advances, deepfake detectors remain vulnerable to adversarial examples, particularly in diverse, real-world settings. We propose MIG-COW, a novel adversarial attack framework that generates highly generalizable and visually imperceptible adversarial examples. By combining momentum-integrated gradients with a consensus-orthogonal decomposition, MIG-COW captures both shared and model-specific vulnerabilities across heterogeneous CNN and ViT detectors. On the AADD-2025 Challenge benchmarks, MIG-COW achieves a 99.96% white-box attack success rate (ASR) with high perceptual similarity (SSIM), significantly outperforming existing baselines. However, its limited 7.16% ASR against official black-box targets - despite achieving the best overall score - highlights the ongoing challenge of transferability. We also demonstrate that incorporating low-performing but diverse models in the ensemble can degrade attack effectiveness, underscoring the need for careful surrogate model selection in real-world adversarial settings.

---


### 111. [ICGF-CXRMate: Image-Conditioned Clinical Context Compression and Gated Fusion for Chest X-ray Report Generation](https://arxiv.org/abs/2610.30928)

**<font color=#1a73e8>作者：</font>** Vu Minh Tran, Thuc Huynh, Son Thanh Luu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Auxiliary patient data can improve chest X-ray report generation, but directly concatenating heterogeneous clinical information with visual tokens produces long, variable-length decoder prompts and may expose the model to redundant or image-irrelevant context. We propose ICGF-CXRMate, an image-conditioned clinical context compression and gated fusion framework. Learnable queries are first conditioned on the current chest X-ray representations and then attend to the patient-data sequence, compressing it into a fixed number of clinical context tokens. Gated cross-attention selectively integrates these tokens into the visual stream, while the compressed tokens are retained in the decoder prompt as a direct clinical pathway. Experiments on linked MIMIC-CXR and MIMIC-IV-ED examinations show that ICGF-CXRMate improves report quality while reducing the average prompt length. In Stage~2, it improves RadGraph-F1 from 24.00 to 28.86, CXR-BERT similarity from 56.86 to 62.80, and BLEU-4 from 5.14 to 7.96 compared with CXRMate-ED, while reducing the average prompt length from 373.89 to 288.37 tokens, corresponding to a 22.9\% reduction. After self-critical sequence training, ICGF-CXRMate outperforms CXRMate-ED on six of eight report-quality metrics in Stage~3. Ablation studies confirm the complementary contributions of image-conditioned compression, gated fusion, and direct retention of the compressed clinical tokens.

---


### 112. [Bridging Number-Theoretic Primality Testing And Algorithmic Optimization: An Adaptive Cryptographic Framework](https://arxiv.org/abs/2610.30935)

**<font color=#1a73e8>作者：</font>** Tran Minh Thanh, Vo Hoai Viet  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The security of modern public-key cryptographic systems, such as RSA, Diffie-Hellman, and ECC, depends entirely on the computational intractability of the integer factorization and discrete logarithm problems. For these asymmetric algorithms to operate, a core requirement is that the system must be capable of generating, testing, and simultaneously proving the primality of extraordinarily large numbers. To meet those requirements, this study proposes a comprehensive framework, bridging clas- sical number theory with modern machine learning models and optimization algorithms. Specifically, the paper delineates an adaptive, arbitrary-precision architecture dedicated exclusively to primality testing. Concurrently, the research deeply analyzes the theoretical foundations of testing methods (both deterministic and probabilistic), hardware-level optimization techniques, and the application of quantum-secured entropy sources, while providing rigorous mathematical proofs to guarantee security even when the prime distribution is biased.

---


### 113. [The Geometry of Meaning in Neural Manifolds](https://arxiv.org/abs/2610.30938)

**<font color=#1a73e8>作者：</font>** Valentino Maiorca  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Just as different languages express the same concept through different words, neural networks express similar functions through incompatible coordinate systems. Different architectures, random initializations, and optimization trajectories produce incompatible parameterizations in extrinsic coordinates, obscuring functional relationships between independently trained models. When models independently solve similar tasks on related data, do their learned representations share exploitable structure despite incompatible coordinates? This thesis shows that semantic correspondence is a fundamental primitive revealing shared geometric structure beneath incompatible parameterizations. By identifying which elements refer to the same semantic content, correspondence breaks the symmetry of arbitrary implementation choices, anchoring incompatible systems to a shared semantic frame and revealing the intrinsic geometry that enables zero-shot transformation between independently trained models.
Building on this principle, fourteen contributions explore correspondence-based alignment across zero-shot model stitching, cross-modal translation, policy transfer, activation steering, and neural decoding. They span domains (vision, language, reinforcement learning, neuroscience), architectures (CNNs, Transformers, graph networks), and scales (from small supervised models to billion-parameter generative systems). Each exploits different geometric properties (angular, metric, spectral, sparse, or distributional), yet all instantiate the same principle. It extends beyond artificial systems: fMRI data show that different human brains processing identical stimuli exhibit alignable geometric structure.
By revealing intrinsic geometric structure beneath extrinsic parameterization, semantic correspondence transforms model isolation into interoperability.

---


### 114. [Attention-guided classification and tumor localization of combined hepatocellular-cholangiocarcinoma](https://arxiv.org/abs/2610.30944)

**<font color=#1a73e8>作者：</font>** Xiaowen Liang, Hélène Cazier, Aurélie Beaufrère 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Combined hepatocellular-cholangiocarcinomas (cHCC-CCA) are a type of cancer that share components of two other primary liver cancers: hepatocellular carcinoma (HCC) and cholangiocarcinoma (CCA). Accurate diagnosis of cHCC-CCA, of which the behavior may resemble that of either HCC or CCA, remains a challenge due to strong intratumoral heterogeneity. Since the prognoses differ between liver cancer types, it is necessary to improve their morphological characterization and recognition in order to accurately identify cHCC-CCA. In this work, we use whole slide images (WSIs) of the two main types of liver cancer (HCC and CCA) and cHCC-CCA, stained with Hematoxylin-Eosin-Safran (HES), to train a classification model that can distinguish between these subtypes and provides a potential solution for localizing different types of tumors in the combined liver cancer images.

---


### 115. [Ground-Truth-First Benchmarking of Reinforcement Learning via Converse Optimality: From Smooth, Fully Observed Systems to Non-Smooth or Partially Observed Tasks](https://arxiv.org/abs/2610.30954)

**<font color=#1a73e8>作者：</font>** Grégoire Ouerdane, Sinan Ibrahim, Stefan Streif 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Benchmarking in reinforcement learning is usually relative: algorithms are ranked by returns on environments with unknown optima. Distance to optimality remains unobservable, while conclusions may depend on reward design, stochasticity, hyperparameters, environment selection, and simulator details. We develop a ground-truth-first framework based on converse optimality, constructing each task with a certified optimal value function and policy withheld from learners and used only for evaluation. The framework unifies two modes: sensitivity benchmarking samples certified environments from continuous-time generators to assess robustness to task variation, while oracle-referenced comparison uses native discrete-time generators to evaluate policies via optimality gap, regret, and policy error. Continuous-time models support physically interpretable sensitivity studies but introduce dependence on the simulator step ($\Delta t$) and numerical scheme. Native discrete-time models align the environment, oracle, and learner on the same transition law, eliminating external integration choices as a confounder. We reproduce quantitative results covering optimizer sensitivity and oracle-referenced comparisons on serial planar arms, dynamically extended nonholonomic vehicles, and quadrotor-inspired tasks. The methodology extends beyond smooth affine Gaussian systems: virtual-input pullback handles non-affine raw-action interfaces and finite-covariance non-Gaussian disturbances. A non-smooth converse optimality formulation enables certified benchmarks with kinked value functions and switching surfaces. For partially observed evaluation, an information-state formulation reduces benchmarking to converse optimality on a sufficient statistic and provides an information-penalty reference. Code, fixtures, and diagnostics are available on the public project page.

---


### 116. [Doubly Robust Distributionally Robust Offline Contextual Pricing](https://arxiv.org/abs/2610.30957)

**<font color=#1a73e8>作者：</font>** Min Xu, Xinyi Yin, Yunfan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline contextual pricing often relies on logged observational data, but faces challenges from distributional shifts between training and deployment environments. Distributionally robust optimization (DRO) provides a principled approach to off-policy evaluation and learning (OPE/L). However, existing methods are mostly limited to discrete actions. Recent work has explored DRO for continuous treatments using inverse propensity weighting (IPW), while such IPW-based estimators can be sensitive to the convergence rate of propensity score estimates, particularly when estimated nonparametrically, which may lead to larger estimation errors and regret. In this work, we develop a doubly robust (DR) framework for distributionally robust OPE/L in continuous pricing settings. For evaluation, we propose a localized DR estimator that addresses the computational challenges of worst-case expectations by fitting only a small number of regressions, comparable to standard non-robust DR, while achieving semiparametric efficiency under mild product rate conditions. For learning, we leverage the inherent smoothness of demand noise to handle pricing-specific discontinuities in revenue outcomes (e.g., threshold-based purchase decisions), establishing a finite-sample regret bound of $\tilde{\mathcal{O}}_p(T^{-s/(2s+1)})$ for smoothness orders $s=1,2$. This bound improves upon existing regret rates in existing DRO-based off-policy learning (OPL) for continuous treatments. Extensive experiments under various levels of distribution shift validate our proposed framework.

---


### 117. [Energy and Latency First: How Deployment Constraints Reverse Time-Series Model Selection](https://arxiv.org/abs/2610.30965)

**<font color=#1a73e8>作者：</font>** Shruti Bothe, Illyyne Saffar, Ayush K. Varshney  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI models, and time-series models in particular are typically ranked by accuracy and deployed under constraints absent from that ranking. In this paper, we study a real setting where these constraints are explicit and measurable: handover pre- diction in cellular networks, where inference runs on the User Equipment once per 40 ms measurement period and must complete before the network acts. The timing bound is hard: a late prediction is superseded by the measurement it was predicting, while energy is a cumulative budget spent for the life of the device. Neither appears in the objective these models are selected on. We evaluate eight architectures under a protocol that screens for deadline feasibility at the tail rather than the mean, then ranks the feasible models on measured inference energy, count- ing the feature computation that precedes the forward pass and is usually omitted. Gradient-boosted trees on handcrafted temporal features are the most accurate model (F1=0.974) and among the cheapest to run, while the neural architecture an accuracy-only benchmark would rank first (CNN-1D, F1=0.914) costs over 3 times more energy per inference under a realistic duty-cycled deployment pattern. We give three conditions under which this outcome should be expected, so the finding applies beyond telecommunications. Accuracy-only benchmarking does not merely under-report deployment cost. It can rank first a model that cannot be deployed.

---


### 118. [GraphCAD: Geometry-Aware Diffusion on Edge-Adjacency Graphs for CAD Generation](https://arxiv.org/abs/2610.30974)

**<font color=#1a73e8>作者：</font>** Wenhao Zheng, Xianggen Liu, Li Yue 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative modeling for Computer-Aided Design (CAD) remains fundamentally challenged by the need to capture the intricate interplay between discrete topological connectivity and precise spatial geometry inherent in Boundary Representations (B-reps). Existing generative approaches largely formulate CAD construction as a sequence modeling problem, but consequently lack an explicit topological inductive bias. In this work, we present GraphCAD, a geometry-aware generative framework that centers modeling on the Edge-Adjacency Graph (EAG), a novel graph-based CAD representation tailored for generative tasks. GraphCAD adopts a hybrid graph diffusion formulation to jointly model the discrete and continuous components of EAG and introduces a geometry-aware denoising mechanism that renders node attributes into spatial point sets. These point sets are encoded by an SE(3)-equivariant backbone and fused into the node representations, thereby grounding the generative process in physical geometry. To support this study, we construct EAGBench, a large-scale dataset of engineering CAD models. Extensive experiments show that GraphCAD can generate complex CAD models with more than 50 faces and achieves state-of-the-art performance in geometric fidelity and distributional alignment compared with sequence-based baselines.

---


### 119. [Interpretive Variation and Discourse Structure in Detecting Enthymemes in Controversial Political Discourse](https://arxiv.org/abs/2610.30987)

**<font color=#1a73e8>作者：</font>** Martial Pastor, Nelleke Oostdijk  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enthymemes are arguments that leave a premise or conclusion unstated, and they are a common persuasion device on social media. Because readers must fill in the missing part themselves, they often disagree on whether a text contains one. This paper asks how to detect and evaluate enthymemes when such disagreement is part of the task. On tweets about vaccination and immigration, each labeled by five annotators, F1 stalls around 0.67 for every fine-tuned model we train, regardless of data size, added features or label type. We therefore ask how these models should be evaluated instead, and propose metrics that compare predictions with the full distribution of annotator votes, together with a model that predicts this distribution directly and captures disagreement better at no cost in F1. We then ask what role discourse structure plays. Models learn to rely on explicit argumentative structure: they reliably recognize tweets without an enthymeme but rarely commit on tweets that contain one. Both the models and a discourse parser miss arguments whose links are left implicit and must be inferred by the reader. Finally, we discuss what these blind spots mean for content moderation systems trained on majority labels.

---


### 120. [ColaBench: Evaluating Memory-Guided Knowledge Acquisition in Personal Agents](https://arxiv.org/abs/2610.30989)

**<font color=#1a73e8>作者：</font>** Wenjie Zhang, Zhichao Shi, Xuhui Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personal agents need to draw on long-term interaction history to retrieve and apply external knowledge suited to a user's current request. Even an answer grounded in relevant documents can be unsuitable when it overlooks the user's circumstances. This creates two connected challenges: using historical conditions to identify the knowledge needed for a new request, and applying that knowledge to the user's situation. Existing benchmarks advance memory recall, personalized retrieval, and memory-guided action, while the joint evaluation of these two challenges remains underexplored. We introduce ColaBench, a synthetic benchmark in health and daily living, with 349 tasks across 10 Profiles and a knowledge base of 13,033 documents. Its Evidence Graph connects personal conditions to their disclosures across public interaction sessions, records prior document exposure, and links answer requirements to personal and newly acquired document evidence. We also introduce MemKB, which uses state summaries to inform queries and rule application, and memory-document links to retrieve knowledge associated with the user's history. MemKB achieves 86.25% Accuracy with an average of 4.07 interaction rounds per task. Task-level analysis finds larger gains on tasks integrating information across multiple historical Facts; error analysis further identifies unsupported personal assumptions and rule misapplication as obstacles to using retrieved evidence. ColaBench provides traceable tasks and an evaluation framework for studying how memory guides knowledge acquisition and rule application.

---


### 121. [CARL: Chat Assisted Reinforcement Learning](https://arxiv.org/abs/2610.31014)

**<font color=#1a73e8>作者：</font>** Sanjiv Das, Harshad Khadilkar, Sukrit Mittal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Failure of applied Reinforcement Learning (RL) to solve a given problem predominantly stems from unaddressed specification gaps, where the intent of human experts in the problem's domain is inaccurately or incompletely translated by AI into mathematical objectives, constraints, and reward functions. Failure can also stem from unaddressed performance gaps, where human domain experts are unable to determine the validity of the RL based solution or where parameters (i.e., hyperparameters or weights on the reward terms comprising the reward) are poorly chosen. Chat Assisted Reinforcement Learning (CARL) bridges these gaps through a human-AI co-design interface architecture that enforces interactive specification prior to code generation and then enables subsequent verification and parameter alterations via iteration. More specifically, CARL leads domain experts through a structured ten-step workflow for each iteration using step-specific skill files, domain-aware suggestions via an assistant persona (called Trillian), and compact decision summaries that maintain context across iterations without context overload. Once the domain expert confirms the Markov decision process (MDP) specified by this procedure, CARL's autonomous tool-use loop generates, tests, executes, and debugs an end-to-end RL training pipeline, followed by an interactive post-training diagnosis and revisit step that allows for verification and parameter alteration before running a new iteration if desired.

---


### 122. [XALIGN: A Human-centric Visual Analytics Approach to Understanding AI Explanations](https://arxiv.org/abs/2610.31015)

**<font color=#1a73e8>作者：</font>** Bahavathy Kathirgamanathan, Gennady Andrienko, Natalia Andrienko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explainable AI (XAI) methods are usually evaluated for technical properties such as faithfulness and robustness. In high-stakes application domains, experts also need to check model predictions against established knowledge. Different explanation methods often disagree, and this disagreement is hard to see when each method is inspected separately. We propose XALIGN, a visual analytics workflow and interface that shows rule-based explanations and several feature attribution methods (TreeSHAP, KernelSHAP, and LIME) side by side for the same Random Forest model. Agreements and contradictions between the methods become visible signals that users can explore and compare with domain knowledge. We apply XALIGN in two case studies: the German Credit dataset and a meteorological dataset, in which events derived from ICON model output and Cloudnet observations are classified. In both, the views reveal discrepancies between the rule-based explanation and the attribution methods that a single method would not show. In an expert evaluation with three specialists, participants found XALIGN useful for identifying influential features and for avoiding over-trust in predictions. Linking rules to attributions was harder for the participant without an XAI background.

---


### 123. [CANNBot-CAKE: Collaborative Agentic Kernel Evolution for Ascend NPU](https://arxiv.org/abs/2610.31034)

**<font color=#1a73e8>作者：</font>** Deng Pan, Xue-Jian Gao, Junyi Fan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient custom operators are essential for modern deep learning workloads, yet developing high-performance kernels for Ascend NPUs remains slow, expert-intensive, and difficult to automate. Although AI agents now approach expert performance on GPU kernel benchmarks, current models remain less capable of generating AscendC kernels for NPUs, potentially reflecting the relative scarcity of relevant training data. We thus present CAKE, a CANN-native system for deployable custom operators that combines adaptive multi-DSL routing, separate Generation and Evolution modes, and reviewed knowledge reuse through CAKE Book and a Self-Evolving Agent. On 53 CANN-Bench v1.1 operators on Ascend 950PR, CAKE's aggregated results achieve $100\%$ case pass rate on the standard set (1,060/1,060) and $98.28\%$ on the hidden set (4,167/4,240), with an overall mean score of 78.63 out of 100 and an average performance speedup of $1.334\times$ over the baseline. Evolution then pushes correct operators further: EngramGateFusion cuts aggregate device time by $46.6\%$ over 20 rounds and roughly halves the mean roofline gap. These results offer a practical path toward closing Ascend's AI-for-kernel capability gap.

---


### 124. [Multichoice Modeling: Exploring Decision Configuration Space under Uncertainty](https://arxiv.org/abs/2610.31038)

**<font color=#1a73e8>作者：</font>** Mariia Kozlova, Roman Stepanova, Alexander Walzer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision support has become sophisticated at exploring uncertainty, but much less so at representing the architecture of the decision itself. As a result, the decision space is often narrowed before uncertainty is analyzed, leaving interactions among choices and the effects of alternatives they imply largely invisible. This paper introduces multichoice modeling, a framework for making large decision configuration spaces explicit and computationally explorable under uncertainty. Drawing on the logic of rugged landscapes, we conceptualize such problems as contingent performance landscapes, where interdependent choices generate configuration-specific outcomes whose value changes across uncertain futures. The computational framework combines multidimensional decision and uncertainty spaces in a single simulation. Further, variance-based sensitivity analysis is used for identifying influential choices, and conditional distribution analysis for comparing configuration-specific performance profiles. We demonstrate the framework through three case studies: a manufacturing process upgrade, M&A strategy, and mortgage design. By contrasting conventional uncertainty-only analysis with multichoice modeling, the cases show how opening the decision configuration space can reveal unexpected complementarities, near-best configurations with different risk profiles, and strategies that were not apparent as alternatives at the outset.

---


### 125. [ResGVC: Residual Coding for High-fidelity Generative Video Compression](https://arxiv.org/abs/2610.31039)

**<font color=#1a73e8>作者：</font>** Ding Ding, Daowen Li, Ying Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative video compression (GVC) methods usually employ decoder-side diffusion models to denoise reconstructed signals based on generative priors. Besides, most of these methods perform denoising in latent space rather than directly in pixel domain. In this paper, we propose ResGVC, a residual coding framework for GVC that guides denoising toward original pictures by transmitting residual signals. ResGVC first encodes the original pictures within a learned video codec, and then decomposes the distortion between the codec reconstruction and the original pictures into a sequence of residual segments, where each residual segment is acquired at each denoising step. Residual segments can further be compressed by a novel residual codec with a diffusion transformer as an entropy model. Unlike prior methods, ResGVC introduces explicit source constraints throughout denoising rather than relying on decoder-side generation alone. The diffusion-based entropy model also enables more effective distribution modeling capability based on the powerful generative priors. Moreover, denoising directly in pixel space avoids the irreversible information loss caused by latent representation bottlenecks. Experimental results show that, compared with the previous state-of-the-art method, ResGVC achieves 63.7% and 83.8% BD-rate reductions in terms of LPIPS and PSNR, respectively, while also delivering superior visual quality.

---


### 126. [Algorithmic drift in generative adaptive learning](https://arxiv.org/abs/2610.31041)

**<font color=#1a73e8>作者：</font>** Firuz Kamalov, Hana Sulieman, Ahmed El Sayed 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence promises to democratize personalized tutoring, yet the longitudinal stability of adaptive systems remains under-theorized. Current ethical discourse focuses on static bias. This paper argues that a distinct threat lies in algorithmic drift: a feedback loop in which minor, demographically asymmetric observation errors compound over time into systemic inequities. We make three contributions. First, we formalize algorithmic drift as a coupled learner--tutor dynamical system. Second, we corroborate this theory with an agent-based Monte Carlo simulation in which either a transparent online tracker or an LSTM deep-knowledge-tracing network drives an IRT-based curriculum policy. Third, we introduce the temporal fairness stabilizer (TFS), a targeted intervention that periodically re-probes learner capability, and benchmark it against standard exploration baselines with explicit group-fairness metrics and replication-level inference. Within the modeled environment, TFS closes the achievement gap where generic exploration does not, and we characterize the conditions under which it succeeds. We separate what is established analytically, what is demonstrated in simulation, and what remains to be validated with real learners. Our results reframe algorithmic fairness in education as a temporal property of a closed loop rather than a deployment-time checkbox.

---


### 127. [Conflict-Aware Logit Adapters for Utility-Preserving Anti-Distillation](https://arxiv.org/abs/2610.31046)

**<font color=#1a73e8>作者：</font>** Quoc Phong Dao, Binh Anh Nguyen, Linh Ngo Van 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While reasoning traces improve model capability, they also provide supervision signals for downstream distillation. Initial efforts to mitigate this issue rely on decoding-time interventions, but they incur high inference overhead and can harm the teacher model's natural fluency. We propose Conflict-Aware Logit Adapters (CALA), a lightweight training-time defense. CALA attaches a small residual adapter to a frozen teacher model and trains only the adapter. A proxy student identifies positions where imitation is most sensitive, and the adapter perturbs the output distribution at these positions while remaining within high-probability regions. A conflict-aware optimization strategy balances anti-distillation and utility objectives, while regularization preserves the teacher's performance and fluency. At inference time, CALA incurs modest overhead and requires no auxiliary model. Experiments on reasoning benchmarks show that CALA substantially reduces successful student imitation while maintaining near-original teacher performance and generation quality. These results establish CALA as a practical and efficient alternative to decoding-time approaches.

---


### 128. [Harm Is Behavioural, Moderation Is Lexical: How Language and Culture Decide Whom Automated Safety Systems Protect and Whom They Silence](https://arxiv.org/abs/2610.31047)

**<font color=#1a73e8>作者：</font>** Gabriel Lars Sabadin, Dr Nicola Harding, Sarah Kingston  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Content warning: this paper quotes slurs and hateful statements from published test suites; the racial slur among them is masked.
Automated systems decide at scale which messages are harmful, and they decide unevenly. Classifiers label African American English as offensive up to twice as often as other English, the accounts of prominent drag queens can score as more toxic than those of white nationalists, and safety behaviour that holds in English collapses in low-resource languages. We argue that over-flagging and under-protection share one cause: deciding harm from vocabulary and surface form rather than from what a message does. We organise the evidence into seven failure modes and argue, as testable hypotheses, that harmful behaviours (a request for secrecy, a demand for payment, an attempt to isolate someone) travel across languages better than the words that express them. We propose an evaluation protocol that makes the gap between the best- and worst-served language communities a headline result, and show that the naive gap is inflated under equal service and that its usual bootstrap interval is unreliable. Applied to five open systems in eleven languages, from a keyword lexicon to two current multilingual guard models, the protocol finds that none reaches native-speaker accuracy at separating harmful function from harmless form (51 of 55 system-language pairs fall short); that greater capability raises discrimination in nine languages while leaving Arabic and romanised Hindi near chance, so the gap between the best- and worst-served languages grows with capability; that one system both over-flags and under-protects the same language most; and that a language a system reads worst can look the most fairly treated when only false positives are reported.

---


### 129. [Adaptive Uncertainty Visualization With jk-Plots](https://arxiv.org/abs/2610.31050)

**<font color=#1a73e8>作者：</font>** Nikolaus Piccolotto, Daniel Pahr, Laura Lotteraner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> An important task of uncertainty visualizations is to communicate how the number of available observations influences the precision of estimates, such as a Normal distribution's mean. In this paper, we propose an adaptive approach to visualizing univariate data that produces salient representations while highlighting the uncertainty introduced by the sample size. We introduce jk-plots, inspired by educational material of Bayesian statistics, that combine visualizations of plausible reference models (emulating popular uncertainty visualization idioms) and the observations. We describe a visualization pipeline to create jk-plots, which we implemented in an R package. We demonstrate jk-plots using synthetic datasets of varying size and discuss possible usage scenarios in domain expert interviews.

---


### 130. [A General-Purpose Dual-Path Interaction Framework for Multi-View Medical Image Segmentation: Alleviating Data Volume Dependency in Small-Sample Regimes](https://arxiv.org/abs/2610.31065)

**<font color=#1a73e8>作者：</font>** Shuhuan Wang, Yuanyuan Cui, Pengju Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The performance of medical image segmentation depends on a large amount of annotated data, and most segmentation models experience a significant drop in performance in low-sample-size scenarios. Existing semi-supervised and weakly supervised methods rely on specific network architectures, while traditional multi-view-assisted segmentation methods require strictly paired samples, which limits their clinical applications. To address these issues, we propose DPIF, a general-purpose plug-and-play dual-path interaction framework compatible with arbitrary encoder-decoder segmentation networks, which leverages cross-view anatomical complementarity to reduce annotation reliance. DPIF first performs Sinkhorn optimal transport-based cross-view distribution alignment to establish global semantic correspondence without sample-level pairing. It then adopts conditional mutual information-guided feature decoupling to enable bidirectional knowledge transfer only within the shared semantic space, suppressing view-specific noise. Finally, persistent homology-based topological regularization encodes anatomical invariants as unsupervised priors to mitigate overfitting. Experiments were conducted using 24 baseline models on a private multicenter echocardiography dataset and two public datasets. The results show that DPIF-enhanced models outperform single-view baseline models when trained on comparable amounts of data. Notably, most dual-path variants trained on 40\% - 60\% of the data achieve performance comparable to that of single-view models trained on the full dataset. This demonstrates that DPIF provides a general-purpose and scalable solution for data-scarce multi-view medical image segmentation problems.

---


### 131. [Federated Differentially Private Optimization via Low-Rank Preconditioning](https://arxiv.org/abs/2610.31069)

**<font color=#1a73e8>作者：</font>** Antti Koskela, Tejas Kulkarni, Elias Raninen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider differentially private (DP) optimization in the federated setting, where a DP estimate of the feature covariance matrix serves as a Hessian approximation for generalized linear models. Existing central DP methods for covariance estimation have communication cost that grows quadratically in the data dimension, while existing baselines with linear communication cost are only locally private and degrade as the number of clients increases. As a remedy, we propose a federated DP-PCA framework that achieves linear communication cost while providing central DP guarantees under secure aggregation. It consists of a DP rank selection step, a DP power method, and a noisy release of the covariance projected onto the selected low-dimensional subspace. We give error bounds for this covariance estimate and for the resulting low-communication preconditioned DP gradient descent. Empirically, our proposed DP optimization method matches a centralized baseline with quadratic communication cost at a fraction of the communication.

---


### 132. [When Forgotten Facts Return: Relearning-Aware Unlearning of Knowledge Graph Embeddings via Tangent Kernels](https://arxiv.org/abs/2610.31075)

**<font color=#1a73e8>作者：</font>** Parnian Fazel, Mohammad M Maheri, Hamed Haddadi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Approximate unlearning answers a deletion request on a knowledge-graph embedding by editing entity embeddings instead of retraining from scratch. These embeddings keep being updated as new facts arrive. Under this ordinary continued training, forgotten facts recover more than in the exact-unlearning baseline, a model retrained without them and given the same continued training. We trace this relearning to entity embeddings shared by forgotten and new facts. To our knowledge, this is the first study of relearning in knowledge-graph embeddings. Relearning-robust methods developed for deep networks do not account for the graph structure underlying this recovery. We propose Kernel-Anticipated Unlearning (KAU), which uses the tangent kernel to model how continued training changes forgotten facts' scores through these shared parameters. KAU expresses this first-order response in closed form and differentiates through it inside the forgetting loss. The objective steers edits toward directions that continued training reverses less. We compare KAU with state-of-the-art knowledge-graph unlearners and relearning-robust methods under identical continued training, measuring leakage beyond the exact-unlearning baseline. Across three backbones, KAU reduces the strongest knowledge-graph unlearner's leakage by 46-63% on FB15k-237 and 50-82% on CoDEx-L, at higher retained utility.

---


### 133. [I$^2$-KAN: Interpretable Intra- and Inter-Modal Multi-Pathway Representation Learning for Multimodal Sentiment Analysis](https://arxiv.org/abs/2610.31087)

**<font color=#1a73e8>作者：</font>** Xiaoting Xie, Feng Qiao, Xianwei Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal sentiment analysis (MSA) aims to infer sentiment by integrating linguistic, acoustic, and visual information. However, many fusion methods integrate modality-specific representations and cross-modal interactions into joint representations, making it difficult to determine whether predictive utility arises from a modality itself or from its interactions with others. More fundamentally, a modality's standalone predictive utility may not faithfully reflect its interaction-conditioned predictive utility. To address this issue, we propose I$^2$-KAN, an interpretable multi-pathway framework that explicitly maintains intra-modal and pairwise inter-modal information in separate structural pathways. Each pathway is refined by a Task-Decoupled Linear-Gated Denoising Bottleneck (TDL-GDB) to learn compact and task-relevant representations, followed by structured Kolmogorov-Arnold Network fusion that retains explicit pathway associations and supports multi-level interpretation. Extensive experiments on CMU-MOSI, CMU-MOSEI, and CH-SIMS v2 demonstrate strong overall performance. Ablation and interpretability analyses consistently show across the three benchmarks that low standalone predictive utility does not necessarily imply low interaction-conditioned predictive utility: a modality that appears weak in isolation can remain informative through pairwise interactions. These findings highlight the interaction-dependent nature of multimodal utility and suggest that modality utility should be characterized from both standalone and interaction-conditioned perspectives.

---


### 134. [What Pairwise Evaluation Misses: Reward Scores across Prompts](https://arxiv.org/abs/2610.31090)

**<font color=#1a73e8>作者：</font>** Mateusz Modrzejewski, Tomasz Radzikowski  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reward models score responses for preference optimization, filtering and ranking, and pooling scores across prompts needs them to be comparable. Yet pairwise evaluation compares two responses to the same prompt, so any score component shared by a prompt's responses cancels and goes untested. We study this component by comparing between-prompt variation in model scores with the same variation in human ratings of the same responses. We propose a human-referenced audit, built from a between-prompt variance share, a sibling-rating regression and prompt substitutions, and apply it to eighteen released scorers and six matched training conditions. We find that scores cluster by prompt more than the ratings do: on HelpSteer2, six reward models have between-prompt shares of 0.34 to 0.64 against a human share near zero. Replacing the original prompt with a fixed instruction keeps substantial clustering but weakens agreement with prompt-level human ratings, so clustering alone does not show agreement with humans. Part of that variation is useful: subtracting prompt means lowers the helpfulness of globally selected responses, and scores stay sensitive to a wrong prompt even when training shuffles prompt means. We propose that reward evaluation check between-prompt variation, sensitivity to a wrong prompt and usefulness for selection separately.

---


### 135. [Co-Recursive Semantic Self-Extension: A Mathematical Foundation for Open-Ended Intelligence](https://arxiv.org/abs/2610.31097)

**<font color=#1a73e8>作者：</font>** Simon Hegelich, Bardh Prenkaj, Habiba Sarhan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence has advanced through scale, data, and computation, yet remains bounded by its representational framework. We ask what makes intelligence open-ended. Every inferential system selects meaningful distinctions, limiting what it can learn. Within a fixed purpose, performance reaches a ceiling set by its semantic domain. Teleological succession, in which purposes arise from earlier ones, faces a similar limit: Boolean-closed purpose-transformations exhaust their reachable semantic territory. We shift from purposes to inferential systems. Drawing on Kant and Gödel, we model cognitive states as partial evaluations over a formal language. Unresolved propositions may be undecided or undecidable. Reasoning can resolve the former but not the latter, leaving a frontier for extension. Non-trivial reductions of undecidable propositions expose undecidable intermediate premises whose reflective reification supports multiple decisive extensions. Finite trace-guided generation remains fallible, requiring meta-level selection and polycontextural exploration. Using Kolmogorov complexity, we show that no architecture with a fixed state description, transition mechanism, and initial condition can generate histories incorporating irreducible algorithmic information. Because physical systems are fixed in this sense, we examine collectives. Coupling finitely many finite agents does not remove the bound. Extension requires persistent external memory preserving semantic content and historical coordinates. Collective generative capacity depends on balancing overlap for transfer with difference for generation. We propose semantic self-extension as a design principle: intelligence should not merely resolve ambiguity within existing meanings, but transform unresolved structures into new spaces of meaning, generating new distinctions, questions, representations, and purposes.

---


### 136. [Solving Flood-It Puzzles: A Comparison of Tailored A* Search with Declarative Solver Approaches](https://arxiv.org/abs/2610.31100)

**<font color=#1a73e8>作者：</font>** Philipp von Manteuffel, Benjamin Blankertz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present an optimized approach for finding minimal move sequences to solve Flood-It puzzles using A* search and compare it with approaches using SAT, Integer Programming, and Constraint Programming solvers. The performance of A* search is considerably improved by using an appropriate heuristic and sophisticated equivalences of game states to limit the search space. Each aspect is systematically evaluated, providing insights that generalize to other problems. By comparing the best variant of each approach, the A* search is the fastest in finding a minimal solution in about 75 % of the Flood-It instances tested. This result is in line with our expectation since A* specifically looks for a minimum solution. In contrast, the SAT-based approach is designed to solve the decision problem of whether a solution with a given length exists. An iterative search is required to determine a minimum solution length using a SAT-based approach. However, with increasing complexity, quantified by the minimum solution length, the SAT-based approach outperforms A*. We also compared the different approaches to the decision problem, where A* again performed best for the largest number of puzzles. Here, again, SAT supersedes A* for higher complexities, albeit with a lower crossing point.

---


### 137. [DeepOpen: Decision-Oriented Intent Classification on BANKING77 and CLINC150](https://arxiv.org/abs/2610.31104)

**<font color=#1a73e8>作者：</font>** Shuang Song Zhongqiao Yuan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present DeepOpen, a decision-Oriented intent-classification framework with dataset- specific systems for BANKING77 and CLINC150. On BANKING77, a single English classi- fier continued with sharpness-aware minimization (SAM) achieves 94.1234% test accuracy (2,899/3,080). This is the best observed result among three fixed SAM seeds, selected for display after test evaluation; their mean is 94.0368%. On the 150 in-scope CLINC150 classes, probability fusion of one Laya specialist and three DeBERTa-v3-large classifiers achieves 98.0222% (4,411/4,500). We describe the two configurations, reproduce the reference com- parisons displayed in the accompanying evaluation explorer, and separate headline scores from evidence about improvement. Under a uniform BANKING77 evaluation path, the SAM mean exceeds the historical checkpoint by 0.0433 percentage points, with a shared-row 95% interval of [-0.2273, +0.3247]. Thus, the continuation does not establish a reliable accuracy gain. The report documents strong observed task-specific performance, selection effects, and unresolved historical execution-path differences, rather than a new backbone or a unified algorithmic advantage.

---


### 138. [Learning What to Ask for Tomorrow: Active Preference Acquisition for Long-Term Personalized Web Agents](https://arxiv.org/abs/2610.31107)

**<font color=#1a73e8>作者：</font>** Yiqi Wang, Zizhi Zeng, Jiaqi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Web agents increasingly serve the same user across repeated online tasks such as booking travel, shopping, and scheduling, so their long-term usefulness depends on how well they know the user's preferences. Passive memory and personalization methods cannot obtain preferences the user never reveals, and clarification methods that value a question by its benefit to the current task overlook the benefit of reusing the answer in later tasks. We study Active Preference Acquisition (APA): which missing preferences are worth the cost of asking? We define the Prospective Personalization Value (PPV) of a missing preference as its expected cumulative utility gain over future tasks minus the effort and disclosure-risk cost of asking, and select questions under a per-interaction budget. We characterize when cumulative reuse justifies acquisition despite insufficient single-task benefit, and evaluate this regime with an initial-profile diagnostic. APA computes the counterfactual gain of each candidate preference on public task prototypes with the agent's own task solver and aggregates it by the expected reuse of each task family. We evaluate it on ActiveWebPref, a controlled longitudinal benchmark with hidden but queryable user profiles and exact task utilities. At a horizon of 20 tasks, 34.4% of budget-feasible valuable missing preferences are amortization-dependent; APA acquires 80.3% of them, whereas current-task value of information acquires 5.1%. Under per-user asking-cost caps matched to APA's realized expenditure, APA achieves higher net utility than four heuristic selection baselines. In our cost setting, asking about every unknown preference yields lower net utility than not asking, while APA recovers 84.2% of its utility gain with 27.6% of its questions. The value of acquiring a user preference should account for its reuse across future tasks, not only its benefit to the task at hand.

---


### 139. [DRAFT: Decoding and Reconstructing 3D Room Layouts from fMRI and Camera Trajectories](https://arxiv.org/abs/2610.31108)

**<font color=#1a73e8>作者：</font>** Chi-Wei Lee, An-Kai Chen, Cheng-Han Chiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While functional magnetic resonance imaging (fMRI) decoders reconstruct images and 3D objects, recovering the metric geometry of rooms from a moving viewpoint remains an open challenge. We introduce, to our knowledge for the first time, the task of reconstructing 3D layouts of held-out scenes using only the known camera trajectories and the fMRI signals of participants watching indoor walkthroughs, without any visual frames. The task is hard because of the temporal mismatch between rapid visual changes and blurred fMRI signals. Our method, DRAFT (Decoding and Reconstructing 3D room lAyouts from fMRI and Trajectories), extracts a compact layout representation from the early visual cortex and fuses this neural code with the geometric free space derived from camera motion. To evaluate it, we propose layout r, the Pearson correlation between predicted and ray-cast log depths. On ten held-out scenes (20 participants), DRAFT reaches a layout r of 0.480, outperforming the camera path alone (0.446) and seven fMRI decoders (at most 0.429). DRAFT also works as a plug-in that improves all seven decoders without retraining, raising their layout r from 0.171-0.429 to 0.487-0.493. Brain activity and camera motion can thus recover the metric layout of unseen rooms, a first step toward reconstructing the 3D spaces people see.

---


### 140. [What Comes Next and Why: Interpretable Next-Event Prediction with Neuro-Symbolic Rules](https://arxiv.org/abs/2610.31114)

**<font color=#1a73e8>作者：</font>** Tim Nico Bauerschmidt, Isabel Valera, Jilles Vreeken  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In real-world applications, being able to explain why a prediction is made is often as important - if not more so - than achieving high accuracy. However, existing methods for sequential event prediction typically prioritize accuracy at the expense of interpretability. Neuro-symbolic approaches offer a promising direction to improve interpretability by learning symbolic rules, but extending them to next-event prediction is challenging due to the presence of temporal dependencies. We introduce RULES, a neuro-symbolic model that learns sequential rules directly from data, and combine it with a residual network to form RUNES (Rule Network for Event Sequences). RULES accurately recovers ground truth rules from synthetic data and discovers compact, interpretable rule sets on real data. RUNES combines these rules additively with a residual network, achieving competitive accuracy while providing transparent access to active rules and how residuals adjust predictions.

---


### 141. [A Grammar of French Civil Cassation: A Ground-Level Dataset and Tool](https://arxiv.org/abs/2610.31116)

**<font color=#1a73e8>作者：</font>** Avrile Floro, Tamara Dhorasoo, Nils Holzenberger 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents a dataset of 121,536 ground-reasons pairs across 86,464 rulings of the five civil chambers of the French Court of Cassation (2016-2025). An appeal on points of law cannot itself be appealed and often decides a case for good. Understanding how the Court rules is thus crucial and can help lawyers who draft those appeals. Inside a ruling, every ground of appeal (a distinct legal complaint against the appealed decision) has its own answer from the Court. This answer is called the reasons and it belongs to one of a few doctrinal families. Using a deterministic pipeline, we pair each ground with its reasons and attach the pair to its family, according to the established French taxonomy. We obtain a descriptive grammar of civil cassation that shows which grounds succeed, which legal texts they refer to, and how both evolve over the decade. We release the dataset, the code and an interactive consultation tool.

---


### 142. [WildDepth-v2: A Synchronized RGB--LiDAR--Radar Dataset and Benchmark for Metric Depth, Motion, and Tracking of Wildlife](https://arxiv.org/abs/2610.31123)

**<font color=#1a73e8>作者：</font>** Muhammad Aamir, Sangyun Shin, Naoya Muramatsu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Measuring animal distance and motion in metric units underpins abundance estimation, morphometrics, and movement ecology, yet monocular video lacks metric scale and wildlife datasets lack metric ground truth. We present WildDepth 2, extending the synchronized RGB-LiDAR WildDepth dataset in three directions. (i) Imaging radar: 37 RGB-LiDAR-4D-radar sequences (19,716 frames) with per-point Doppler velocity and a measured error budget, to our knowledge the first imaging-radar wildlife recordings. (ii) Benchmarking: a frozen, checksummed hidden test set for RGB-only distance estimation and RGB+sparse-LiDAR depth completion, evaluated separately on animal and background pixels. (iii) Motion and tracking: metric 3D trajectories obtained by lifting 2D tracks using LiDAR, radar, or monocular depth. Across 48,723 animal frames, object-level radar calibration improves monocular depth over scene-level LiDAR calibration without requiring LiDAR at inference (AbsRel 0.120 vs. 0.198), although animal-level LiDAR remains more accurate (0.052). Across 431 tracks, once-per-track radar scaling reduces 3D position error four-fold (2.20 to 0.58 m) and distance-sampling detection-function bias from -13% to -2%, matching once-per-track LiDAR calibration. Transferring radar Doppler onto LiDAR produces motion masks 3.7 times denser than radar alone at 72% precision, reduces moving-animal LiDAR accumulation error by 37%, and estimates radial speed (r = 0.60), albeit with approximately 50% underestimation.

---


### 143. [Post-Audit Mirage: Identifiability Limits of Offline Agent Verification](https://arxiv.org/abs/2610.31130)

**<font color=#1a73e8>作者：</font>** Aman Behera, Payal Payal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Offline tests can fail to reveal whether an agent update will remain safe after deployment. We operationalize this post-audit mirage using matched safe and harmful lifecycles that expose identical verifier-visible evidence while an isolated scorer records opposite deployment truth. Our theorem applies standard observational-equivalence and indistinguishability ideas to this executable audit boundary and states the resulting error-abstention tradeoff. The Post-Audit Mirage benchmark makes that boundary executable across authorization, scheduling, and shared-capacity environments. IdentifiedRangeMonitor uses fresh group-labelled harm outcomes to return deploy, hold, cannot determine, or unsupported. Experiments show that monitoring can recover the missing distinction in favorable settings but may remain undecided for rare groups, small effects, or missing observations. Verifier-agent evaluation must therefore test both calculation validity and whether the available evidence supports the deployment decision.

---


### 144. [Is High Local Accuracy Enough? Geometric Consensus with Support-Adaptive Statistical Personalization for Federated Learning](https://arxiv.org/abs/2610.31133)

**<font color=#1a73e8>作者：</font>** Junyu Lin, Bosong Qi, Pengcheng Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world deployment of personalized federated learning (PFL) requires adapting to heterogeneous clients while preserving recognition performance beyond local distributions. However, high local accuracy can conceal failures on locally rare or absent classes. Effective personalization should therefore strengthen global recognition while raising the personalization floor. We propose an evaluation protocol that complements local accuracy with global, rare-class, and unseen-class evaluations to reveal generalization obscured by local scores, and assesses personalization floors among the worst-performing clients to expose weaknesses hidden by aggregate performance. To meet these deployment challenges, we propose FedGRC, a unified PFL framework integrating generalization and personalization through (i) Consensus-Guided Representation Learning (CGRL), which learns discriminative representations through shared directional and magnitude guidance; (ii) Multilayer Metric Synthesis (MMS), which constructs a shared covariance metric from these multilayer representations for statistical classification; and (iii) Support-Adaptive Shrinkage Personalization (SASP), which adapts class means within this metric by shrinking local estimates toward shared means according to local sample support, enabling adaptation while retaining shared knowledge. Extensive experiments, including benchmarking against 21 methods across 5 heterogeneity settings on 3 datasets and comprehensive ablation studies, validate the effectiveness of FedGRC. On CIFAR-10 and CIFAR-100, FedGRC surpasses state-of-the-art (SOTA) baselines in global recognition and personalization floors by at least 2.17% and 2.13%, respectively. On the real-world heterogeneous FedRS dataset, it outperforms the respective best baselines by 2.15%, 3.30%, and 4.61% in local adaptation, global recognition, and the personalization floor.

---


### 145. [Mixing Matters: Evidence Position Bias Across Sequence Mixers in Long-Context Question Answering](https://arxiv.org/abs/2610.31135)

**<font color=#1a73e8>作者：</font>** Aman Behera, Namit Solanki, Mehul Anand  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context models often use answer-bearing evidence less effectively when it appears away from a prompt boundary. We compare this position bias across Transformer, state-space, and hybrid Mamba architectures by moving one gold document through a fixed set of nine distractors. The evaluated Transformers show a beginning advantage that the evaluated state-space models lack, while both families favor evidence near the end. A matched pure-versus-hybrid Mamba comparison points in the same direction but remains statistically uncertain. The family difference appears among models that can answer the task. Transformer primacy reappears on synthetic retrieval, where state-space ceiling prevents a family comparison. A corpus swap within one state-space architecture changes overall accuracy without a detectable change in curve shape. Prompt changes can create or nearly remove a beginning advantage. Position remains decodable across architectures even when response curves differ, and attention concentration near initial tokens covaries with beginning sensitivity in the tested Transformer family. These exploratory results show that effective context use depends on the evaluated architecture family, capability, task, and prompt, without isolating the sequence mixer as the sole cause.

---


### 146. [Pos4CHD: A Positive-Free Mask-Guided Counterfactual Synthesis Framework for Fetal Congenital Heart Defect Analysis](https://arxiv.org/abs/2610.31139)

**<font color=#1a73e8>作者：</font>** Wenjie Xuan, Yapeng Li, Hang Su 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The scarcity of positive cases remains a major bottleneck in developing automated diagnostic systems for fetal Congenital Heart Defects~(CHDs), particularly for rare subtypes. Although normal cases are accessible with effort, positive cases are hard to collect due to low incidence rates and privacy concerns, causing severe class imbalance or absence of positive training samples. Existing works resort to synthesizing positives with conditional generative models, but they are task-specific and require positive training samples, hindering application for fetal CHDs. To this end, we propose a positive-free mask-guided counterfactual generation framework for fetal echocardiography, namely Pos4CHD, which enables realistic, high-quality synthesis of pseudo-positive samples from semantic masks, with only normal samples at hand. Technically, we first develop FE-Gen, a mask-guided generative model tailored for fetal heart ultrasound synthesis that mitigates histogram drift and enhances image-mask spatial alignment. Building on FE-Gen, Pos4CHD employs a mask-to-image generation paradigm for CHD synthesis. It first manipulates semantic masks to simulate fetal-heart structural anomalies and then renders anatomically consistent images. Extensive experiments on in-house datasets, together with expert evaluations, demonstrate the visual fidelity~($-12.97$ FID) and anatomical consistency~($+3.96\%$ DSC) of synthesized images. Further validations across diverse real-world CHD diagnosis tasks exhibit promising results and consistent increments, including zero-shot classification~(achieving $93.25\%$ ACC on EbA and $72.92\%$ ACC on TAPVC), lesion detection~($+6.95\%$ mAP50 on VSD), and anatomy segmentation~($+10.49\%$ DSC on fetal heart) compared with baselines. Codes and models are publicly available on \href{this https URL}{GitHub}.

---


### 147. [GM-GReFEL: Geometry-Guided Spatiotemporal State-Space Learning for Robust Dynamic Facial Expression Recognition](https://arxiv.org/abs/2610.31140)

**<font color=#1a73e8>作者：</font>** Yudhistira Arditya Pratama, Yi-Zeng Hsieh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recognizing facial expressions in unconstrained video suffers from two coupled problems: self-attention grows quadratically in cost with clip length, and crowdsourced labels are noisy. We present GM-GReFEL, a spatiotemporal state-space network with a geometry-aware decision stage. Its Modulated GroupMamba backbone replaces a spatiotemporal Vision Transformer. Six channel groups are scanned separately, four over the frame plane and two over time, so the cost grows linearly with sequence length ($\mathcal{O}(N)$); after each layer, a Channel Affinity Modulation gate mixes the groups again. On top of the backbone, a GReFEL reliability module turns the normalized entropy of each prediction into a mixing weight between the classifier output and a vote from trainable geometric anchors, so that facial geometry counts for more when the network is unsure. The model is initialized by static-to-dynamic weight transfer and trained with a Triple Loss. In five-fold cross-validation, the best fold scores 66.57\%/76.46\% UAR/WAR on DFEW, 0.3 points or less below the strongest compared method, and 45.66\%/62.27\% on MAFW, ahead of all compared methods; on FERV39k the mean over five splits, 42.30\%/52.66\%, is competitive. The five-fold means are 64.07\%/74.54\% on DFEW, on par with recent large pre-trained models, and 38.90\%/54.37\% on MAFW, below the best of them. A paired $t$-test on DFEW indicates a modest benefit of temporal modeling (+1.61 UAR points, one-sided $p=0.031$). Attention stays on plausible facial regions, and latency is close to a ViT-B/16 baseline (47.4 vs.\ 46.8 ms per clip). Code: this https URL.

---


### 148. [Rethinking Fisher Vectors for Second-order Multi-scale Deep Feature Aggregation in Scalable Scene Retrieval](https://arxiv.org/abs/2610.31146)

**<font color=#1a73e8>作者：</font>** Alexy Bhowmick, Sarat Saharia, Shyamanta M. Hazarika  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aggregating CNN responses into a compact discriminative vector, given their lack of geometric invariance, is a challenge. To address this challenge, we propose a codebook-free method to encode second-order information of multi-scale CNN features within the Fisher Kernel framework. We use a scalable retrieval pipeline to show the efficacy of the proposed vector. The increased discriminative power is confirmed by experimental evaluation of our method on two difficult benchmarks (INRIA Holidays, UKBench). The significant improvement in retrieval accuracy over state-of-the-art approaches comes with only a slight dimension increase.

---


### 149. [PriMa-Causa: Causal Prescriptive Maintenance](https://arxiv.org/abs/2610.31147)

**<font color=#1a73e8>作者：</font>** Felix Saretzky  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated manufacturing requires data-driven decisions under uncertainty and sparse observational records, and unplanned downtime is a dominant cost of getting them wrong. Prescriptive maintenance recommends a maintenance action against an impending failure rather than merely predicting it. Established reference architectures couple predictive models with rule- or optimisation-based recommendation logic. Selecting a corrective action, however, requires an interventional quantity: how the line behaviour would change if the action were set. Manufacturing data is observational, so a model fitted to predict the outcome estimates an associational quantity and may misdirect the choice of action without the prediction error revealing it. Causal estimators target the interventional quantity but require an expert-led causal study per case, for which the bounded decision window of operation leaves no room. This dissertation analyses how causal reasoning can be embedded into prescriptive maintenance so that actions are ranked by their estimated interventional effect. The result is PriMa-Causa, built from three components: a causal reasoning layer that integrates the estimate into the PriMa reference model, a parametric simulator that supplies the interventional ground truth absent from manufacturing data, and a graph-conditioned tabular causal foundation model that, pre-trained once on this synthetic production-line prior, answers interventional queries in a single forward pass. PriMa-Causa attains a lower prescription error than associational baselines, with the largest margin under weak overlap and sparse context, and a partially disclosed causal graph reduces this error further. The causal inductive bias of the synthetic prior and the graph conditioning can thus replace per-case estimator fitting, a step toward automating causal inference for autonomous and self-healing maintenance.

---


### 150. [Navigating human-robot interaction challenges in private and residential aged care homes](https://arxiv.org/abs/2610.31149)

**<font color=#1a73e8>作者：</font>** David Ahmedt-Aristizabal, Mohammad Ali Armin, Akila Pemasiri 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This chapter explores how robotic systems and ambient intelligence can enhance care for older adults in residential aged care (RAC) homes and private homes. Although these settings differ, we frame both as extreme and challenging environments for human-robot interaction (HRI), characterised by cluttered and dynamic layouts, diverse resident needs, and limited on-site technical support. We review embodied and non-embodied systems that assist with daily living, safety monitoring, and social engagement, highlighting hybrid deployments where robots complement fixed and wearable sensors. To ensure these technologies are usable and effective, design considerations consider the cognitive, physical, and social needs of older adults. Interaction design prioritises accessibility for older adults with low digital literacy, using robust but simple voice interfaces, small sets of non-verbal cues, accessible screen-based companions, and safe object handovers. Privacy, trust, and acceptability are addressed via practical strategies such as on-device inference, data minimisation, visible consent controls, and transparent data handling aligned with emerging artificial intelligence (AI) and privacy regulation. Evaluation emphasises real-world metrics including false alarms per day, time to recover from faults, staff workload, and long-term system reliability. We close by outlining open research challenges and future directions for scalable, regulation-ready deployments that support aging with dignity, safety, and independence.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-211](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
