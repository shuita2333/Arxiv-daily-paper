# 📦 其他研究 | 2026年10月30日

> 本类共 **257** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-257](./part-06.md)

---

### 101. [Balanced State Subspaces for Mamba-2 State Compression](https://arxiv.org/abs/2610.36617)

**<font color=#1a73e8>作者：</font>** Shang Tingyu, Cao Wenfei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mamba-2 compresses all context into a fixed-size recurrent state that dominates decoding memory and bandwidth. Existing compressors quantize state values or prune state coordinates, scoring each channel independently in the native basis. We examine trained Mamba-2 states and find that energy is almost rank-one, but the output does not read the energetic directions: energy concentrates in a bias-like direction accumulated by the recurrence, while the content the output reads lives in a low-dimensional subspace that is not aligned with the state's coordinates. Even output-aware scores are computed coordinate by coordinate, so they miss the directions that determine the input--output map. Compression should therefore target the write--read subspace rather than individual coordinates. We propose \method{}, a post-training transform that instantiates balanced truncation with full controllability and observability Gramians and applies the rotation exactly via Mamba-2's scalar-identity transition. Because the useful rank varies widely across layers, we further introduce HARP, which allocates ranks per layer from the Hankel spectrum and protects retrieval-sensitive layers, improving both perplexity and retrieval over uniform budgets. Calibration takes a single forward pass, an order of magnitude faster than GHOST's released protocol, with lower peak memory. With HARP, \method{} halves the state dimension at an average WikiText-2 perplexity increase of $0.3$ points ($1.8\%$) across 130M--2.7B, versus $1.6$ ($9.3\%$) for GHOST, and the gap widens at 25\% retention.

---


### 102. [Adapting Video Models for Robot Control via Motion-guided Asymmetric Prediction](https://arxiv.org/abs/2610.36624)

**<font color=#1a73e8>作者：</font>** Taeyoung Kim, Junyoung Sung, Heeseung Kwon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) leverage pretrained video generative models for robotic control by jointly predicting future visual observations and actions. The visual prediction objective plays a key role in adapting pretrained video representations to the target robot domain. Yet standard visual prediction inherited from video pretraining treats all visual regions uniformly, despite their differing relevance to robotic control. We therefore investigate the spatial allocation of visual supervision in WAMs and show that focusing supervision on dynamic regions can substantially improve policy performance. Building on this finding, we introduce Motion-Guided Asymmetric Prediction (MoGAP), which augments WAM training with motion-focused visual prediction. MoGAP allocates noise asymmetrically across regions, training the model to reconstruct more heavily corrupted dynamic regions using less corrupted static regions as context. MoGAP is trained alongside standard video-action prediction through a training-only auxiliary prediction path within the shared video diffusion backbone. It uses motion cues derived directly from training videos, requiring neither an external teacher nor additional modalities. Across robot manipulation benchmarks and WAM architectures, MoGAP consistently improves policy performance, increasing success rates on the GR-1 tabletop benchmark from 38.8% to 47.5% for Fast-WAM (Wan2.2-5B) and from 52.3% to 62.3% for Cosmos3-Nano.

---


### 103. [Polarity--Time Interaction and Multi-Level Reliability for Event-Based Spacecraft Pose Estimation](https://arxiv.org/abs/2610.36625)

**<font color=#1a73e8>作者：</font>** Yonglong Zhang, Zongwu Xie, Yang Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse event responses produce uneven keypoint errors whose effects on spacecraft pose depend on correspondence geometry and the reliability of successive observations. We present a reliability-aware framework connecting polarity--time localization, geometric recovery, event--CAD refinement, and trajectory optimization. A three-branch representation combines positive events, negative events, and recent-event timing through cross-branch attention and gating, followed by spatiotemporal aggregation. An ordered semantic-point head estimates relative correspondence precision for geometrically constrained pose recovery. Event-edge and CAD-projection agreement then guide local pose refinement under keypoint-geometry safeguards. At the sequence level, a ten-dimensional descriptor combines heatmap shape, reprojection consistency, and geometric conditioning to set time-aligned observation scales. On the official SPADES challenge test set, the complete system achieves a combined pose score of 0.0474, approximately 5.4\% below PASAN+IRIS. Validation ablations reduce the score from 0.0772 for base localization with uniform PnP to 0.0514 for the complete cascade; on identical single-frame observations, quality weighting reduces the score from 0.0549 with constant-weight optimization to 0.0514.

---


### 104. [The Batch Size Can Be One: Test-Time Adaptation from Classifier Geometry](https://arxiv.org/abs/2610.36628)

**<font color=#1a73e8>作者：</font>** Jaeho Hwang, Yujin Oh, Juhyeon Shin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation updates a deployed model on an unlabeled test stream. In practice this stream often arrives one sample at a time, with the classes in no particular order. A single sample then provides limited information for estimating distribution-level statistics, and selecting samples by confidence can admit predictions that are wrong yet confident. A corruption, however, shifts the features while leaving the decision regions of the frozen classifier unchanged. We therefore propose Origin-recentered Test-Time Adaptation (OriTTA), which constructs fixed geometric targets from the source model and adapts selected features toward them. Seen from the origin of the feature space, the classes lean toward a common direction. We choose a new origin to bring class scores closer together while keeping it near the mean feature of one synthetic prototype per class. From this origin, prototype directions spread more evenly, and each class obtains an axis and an ideal point before any test data arrives. During adaptation, OriTTA aligns selected features with their predicted class axis and penalizes excessive radius, keeps one input per predicted class in memory to limit feature changes for classes absent from the stream, and resets the model when re-classifying this memory reveals collapse. Without tuning for each setting, OriTTA achieves the highest mean accuracy at batch size 1 on CIFAR-10-C, CIFAR-100-C and ImageNet-C in all sixteen combinations of four backbones, two protocols and two stream orders. On ImageNet-C fog, recent methods collapse in up to two thirds of one hundred runs, while OriTTA never does.

---


### 105. [The uneven rise of AI-generated web content](https://arxiv.org/abs/2610.36631)

**<font color=#1a73e8>作者：</font>** Adam Visokay, Soumyakanti Pan, Molly Griston 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In less than five years, generative artificial intelligence (AI) has dramatically reshaped the public-facing web. Using a sample of more than 5 million crawlable webpages, we demonstrate that the share containing AI-generated text has increased precipitously, but unevenly. Our analyses reveal substantial differences in AI composition across language and domain categories (e.g., .edu, .com, or .gov). A higher fraction of English-language webpages contain AI-generated text compared to pages in other languages, and prevalence is substantially lower on .gov and .edu domains compared to .com. These distinctions persist even after accounting for compositional effects. We also find heterogeneity based on a page's position in the connectivity structure of the web. AI-generated text is most common and has increased most rapidly in pages that are the least central in the graph, which drives much of the overall growth in AI-generated text. A slower increase has taken place for more central pages, with the most central tier emerging as the least likely to contain AI-generated text. Methodologically, we use multiple AI detection tools, and generate estimates using a Bayesian hierarchical model that incorporates corrections for the detectors' statistical properties (both false positives and false negatives) and allows for different detector performance across groups, while propagating uncertainty in detector error rates into prevalence estimates. Our work suggests that AI is a prominent, but varied, contributor to public information and internet-based communication.

---


### 106. [Deep Bayesian Approaches for Interpretable Nonlinear Structural System Identification](https://arxiv.org/abs/2610.36633)

**<font color=#1a73e8>作者：</font>** Wei Liu, Konstantinos Vlachas, Eleni Chatzi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> System identification, namely the inference of mathematical representations of dynamical systems from measured data, is fundamental to engineering diagnostics, prognostics, and decision-making. Bayesian filtering offers a principled framework for probabilistic state estimation but traditionally relies on prescribed transition and observation models. Recent advances in deep Bayesian filtering address this limitation by embedding learnable representations within probabilistic state-space formulations, enabling data-driven identification of unknown dynamics while retaining physical structure and uncertainty-aware inference.
This tutorial provides a systematic introduction to deep Bayesian filtering for nonlinear structural system identification, focusing on the interplay between learned dynamics, physical inductive biases, and posterior inference. The Deep Markov Model serves as a data-driven reference, while the Physics-guided Deep Markov Model (PgDMM) and Neural Extended Kalman Filter (Neural EKF) illustrate complementary approaches based on amortized variational inference and differentiable Kalman filtering, respectively. Their capabilities are examined through dynamic state estimation and joint dynamic state and parameter estimation on a three-dimensional shear-frame benchmark with hysteretic Bouc-Wen connections and sparse acceleration measurements. The results highlight important distinctions between measurement-conditioned reconstruction and open-loop forecasting, demonstrate how physical structure can improve latent-state interpretability without necessarily ensuring predictive fidelity, and reveal differences in the robustness of response and parameter estimation. Practical guidelines for model construction, training, evaluation, and deployment are provided, together with an outlook on remaining challenges in uncertainty calibration, identifiability, and real-world validation.

---


### 107. [When Does Perturbation Consistency Add Information Beyond Softmax Confidence? Theory and Evidence for the Decision Consistency Framework](https://arxiv.org/abs/2610.36640)

**<font color=#1a73e8>作者：</font>** Amit Kalitaa, Moirangthem Tiken Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Perturbation consistency scores judge whether a prediction survives small input changes. The Decision Consistency Framework (DCF) scores each image by label stability (LS) and confidence deviation (CD) under six mild operators, combines them into a consistency score (CS), and summarises a model by the gap between accuracy and mean consistency (CAG). We ask when these scores carry information that the clean softmax output lacks. Across 201 evaluations with three seeds per configuration, CS detected misclassifications on clean data less well than the maximum softmax probability (MSP) in every model family. For frozen CNNs, the deficit was 0.057 in area under the ROC curve (AUROC; 95% CI 0.043 to 0.073), at 8 to 15 times the compute. A label flip requires the logit margin to be at most the square root of two times the logit displacement, and at a fixed margin, the displacement predicted errors at AUROC 0.515. The same inequality gives a label-free split-conformal no-flip certificate, never violated in 84 runs. Consistency did add information where confidence is misled: under noise corruptions of CIFAR-10-C, it beat the margin, and under projected gradient attacks, it separated clean from attacked inputs with AUROC 0.83 against 0.37 for MSP at a budget of 2/255, as pre-specified. The gain under noise did not transfer to unseen shift families. The large negative CAG on OCTMNIST persists under full fine-tuning and in-domain training and is partly a class-prior effect: correcting the prior recovers about 40% of the gap.

---


### 108. [When Is a Cheap Fairness Edit Safe? Screening Post-Hoc Edits in Two-Sided Matching Markets](https://arxiv.org/abs/2610.36649)

**<font color=#1a73e8>作者：</font>** Moirangthem Tiken Singha, Rabinder Kumar Prasada  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two-sided matching systems, such as admissions pipelines, allocate opportunities jointly. Reducing a protected at tribute's influence usually requires encoder retraining. We study a closed-form linear projector that does this at inference time. For markets that stay vertically ordered before and after the edit, we bound the mean welfare change by the edit-induced appeal shift and an explicit remainder. A probabilistic refinement replaces worst-case constants with a data-dependent deviation term. A pre-deployment screen combines a verticality test with a welfare sweep and returns PASS, KILL, or OUT-OF-SCOPE. An exact tier requires every opportunity to rank applicants by appeal, and a graded tier admits near-vertical markets. On 30 held-out synthetic markets, the screen agrees with every pre-specified regime verdict, with no observed false PASS. On 60 exactly vertical markets, no bound is violated, and the probabilistic bound is informative in 69% to 87% of configurations. On 2700 configurations from three realistic markets, which do not reach the exact tier, no plug-in bound expression is violated. A closed-form factorization stays within graded scope in 90% to 100% of instances, whereas two-tower and graph neural network encoders fall outside it in every instance. Architecture choice thus appears to affect whether a post-hoc edit is admissible.

---


### 109. [TACO-Graph: Automated Construction of Text-Atributed Graphs](https://arxiv.org/abs/2610.36650)

**<font color=#1a73e8>作者：</font>** Amiri Hayes, Kristina Wicke  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph-structured representations of text data have become foundational across machine learning, yet it remains unclear how to systematically construct a graph from a given dataset for a target task. Choices about which entities become nodes, which relationships become edges, and what text each node contains can substantially affect downstream performance. In practice, finding optimal constructions often requires expert knowledge or manual trial and error. We introduce TACO-Graph, a decision tree framework for learning which graph construction choices are most effective for a given dataset and task. Specifically, we focus on text-attributed graphs (TAGs) constructed from multi-attribute tabular data. TACO-Graph enumerates valid TAG representations, scores each using fast proxy evaluation on small representative subsets, and trains an interpretable decision tree on those scores. Across five datasets spanning citation networks, product reviews, and bibliographic relationships, our decision trees predict construction quality on separately drawn evaluation samples with mean Spearman $\rho$ above $0.9$ for node classification and above $0.8$ for GraphRAG retrieval. Our trees systematically identify which constructions perform better across both GNN and GraphRAG tasks, and the full pipeline is released as an open-source library to support evaluation on new tasks and datasets at this https URL. TACO-Graph provides a systematic and interpretable guide for determining how to convert tabular data to text-attributed graphs for downstream tasks.

---


### 110. [Log-Derivative Trick for Parametric Markov Chains](https://arxiv.org/abs/2610.36655)

**<font color=#1a73e8>作者：</font>** Arthur Gall, Ichiro Hasuo, Thomas Seiller  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimizing expected rewards and reachability probabilities in parametric Markov chains (pMCs) is central to the analysis and synthesis of probabilistic systems with loops. While traditional symbolic synthesis approaches--such as parameter lifting and rational function generation--suffer from scalability bottlenecks, gradient-based optimization emerges as an effective alternative. However, existing gradient-based techniques still rely on symbolic gradient computation--such as solving large linear systems--over the global state space, inheriting scalability limits. Finite-horizon approximation is possible but introduces uncontrollable bias.
In this paper, we introduce a scalable Monte Carlo gradient estimator based on a measure-theoretic generalization of the log-derivative trick. We prove that our estimator provides unbiased gradient estimates under almost-sure termination and standard regularity conditions. Crucially, our method avoids global state-space materialization and linear system solving entirely: it operates purely along sampled trajectories, requiring only black-box evaluations of local transition probabilities (or densities) and their derivatives. Unlike existing pMC techniques that are fundamentally restricted to finite discrete systems, our measure-theoretic framework naturally extends to continuous and general $\sigma$-finite state spaces. Empirical evaluations on synthetic discrete pMCs and continuous-state case studies demonstrate that our method scales to state spaces far beyond the reach of existing solvers, significantly reducing execution time without introducing bias.

---


### 111. [The View from Nowhere: Population-Centered Agent Evolution](https://arxiv.org/abs/2610.36660)

**<font color=#1a73e8>作者：</font>** Shuo Yan, Ningning Hou, Haoyu He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-improving AI systems can revise the designs that govern their own behavior. Yet existing approaches center improvement on selected parent agents and their evolutionary experience, leaving the broader population largely underused. We identify a substantial gap between population coverage (i.e., the tasks solved by at least one evolved variant) and the performance of the best individual agent. This gap shows that useful capabilities and diagnostic evidence emerge across the population without being consolidated into its leading agents.
These observations motivate the view from nowhere, a principle for agent evolution: an agent should be improved by interpreting its behavior through population-wide patterns of success, failure, and prior self-modification. We instantiate this principle as Population-Centered Evolution (PCE). PCE distils task records and modification histories from the population into a population block, which captures recurring failures, complementary successes, and the effects of previously attempted modifications to guide improvements to a selected parent's harness.
Under matched models, initial harnesses, and evolution schedules, PCE achieves 72.1% success on SWE-bench Verified and 96.7% on Polyglot, improving over a strong group-evolution baseline by 3.2 and 5.9 percentage points. In our evaluation, PCE reduces the gap between population coverage and best-agent performance by one-third on SWE-bench and closes it on Polyglot. These results suggest that treating the population as evidence--not merely as candidates for selection--provides a complementary principle for agent evolution.

---


### 112. [Haste Makes Waste? Towards Safe Few-Step Text-to-Image Models](https://arxiv.org/abs/2610.36665)

**<font color=#1a73e8>作者：</font>** Lior Ziv, Mahmood Sharif  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While few-step distilled text-to-image models have gained traction due to their fast generation times, the speed-up implications on their unsafe generation rates remain unknown. We uncover an inherent tension between speed and safety: few-step models are often more unsafe than their teachers, and reducing the number of inference steps consistently raises unsafe generation rates. We further find that acceleration makes unsafe concepts harder to erase in few-step models, with existing concept-erasure methods markedly less effective than in teachers. We offer a mechanistic diagnosis for why erasure methods fail on few-step models, finding that the fragility of few-step models' generation process and the way generation guidance is usually distilled into those models may hinder established concept-erasure methods. To address the speed-safety trade-off, we propose DICE (Distillation-Integrated Concept Erasure), a post-distillation erasure method tailored for few-step models. DICE aligns both its latent construction and its generation-preservation loss with the distillation method that produced the model, keeping erasure faithful to few-step models. DICE demonstrates strong results in our evaluation. For example, on FLUX Schnell, DICE reduces unsafe-generation rate to 0.046 (vs. at least 0.161 for prior erasure methods we test), while mostly preserving benign generation quality.

---


### 113. [Learning Where to Trust: Reliability-Guided Expert Routing and Velocity Gating for 3D Deformable Registration](https://arxiv.org/abs/2610.36672)

**<font color=#1a73e8>作者：</font>** Chenyu Guo, Wenjie Dai, Yiqian Chang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deformable image registration relies on accurate anatomical correspondences. However, explicitly coupling local matching reliability with spatial context selection and deformation update strength remains insufficiently explored in learning-based registration. This challenge is particularly pronounced in homogeneous, weakly textured, and severely deformed regions, where ambiguous matches may induce erroneous deformation updates. We propose ReliMorph, a reliability-routed symmetric framework for 3D deformable registration that couples correspondence assessment with spatial context selection and update this http URL correlation distributions characterize correspondence ambiguity using shared anatomical features with modality-specific adaptation. These reliability cues guide spatial expert fusion and gate residual velocities during coarse-to-fine refinement. Updated inverse-inconsistency feedback guides routing and gating at finer pyramid levels. To our knowledge, ReliMorph is the first 3D deformable registration framework to jointly condition spatial expert routing and residual velocity gating on correspondence reliability. Extensive experiments demonstrate that ReliMorph consistently outperforms competing methods in anatomical overlap, highlighting its effectiveness across unimodal and multimodal registration tasks.

---


### 114. [Beyond the 1D Reality-Virtuality Continuum: A 2D Framework for Seven Extended Reality Paradigms](https://arxiv.org/abs/2610.36674)

**<font color=#1a73e8>作者：</font>** Rajashekhar Vachiravelu Saminathan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The Reality-Virtuality (RV) continuum helps in describing the relationship between physical and computer-generated environments. However, the increasing number of Extended Reality (XR) paradigms introduces new technologies. Their characteristics cannot be completely represented by a single real-virtual dimension. It can be noted that XR systems not only vary in their proportion of real and virtual content but also adds, suppresses, or transforms information available to the user. This work proposes a framework for characterizing seven XR realities, namely Virtual Reality (VR), Augmented Reality (AR), Mixed Reality (MR), Augmented Virtuality (AV), Phenomenal Reality (PR), Annexing Reality (AnR), and Diminished Reality (DR). It uses a two-dimensional extension of the conventional 1D RV continuum. The first dimension helps in identification of the position of an XR technology between real and virtual environments. The second dimension captures information addition and subtraction. The proposed approach gives a qualitative basis for comparing existing and emerging XR paradigms within a unified XR framework.

---


### 115. [An Empirical Study of Undisclosed Charges in Hook-Based Decentralized Exchanges](https://arxiv.org/abs/2610.36682)

**<font color=#1a73e8>作者：</font>** Kai Ma, Tianle Sun, Shun Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Many decentralized exchanges use automated market makers (AMMs) to trade assets against liquidity pools. Modern AMMs allow third-party contracts, called Hooks, to customize this process. However, Hooks can impose additional deductions that fee breakdowns based on standard pool parameters do not itemize. We present, to the best of our knowledge, the first large-scale empirical study of the production Hook ecosystem, focusing on these undisclosed settlement charges. Our study covers 7,873 Hook deployments, 50,011 pools, and 296M pool events on Uniswap v4 and PancakeSwap Infinity across Ethereum and BNB Smart Chain (BSC) through August 1, 2026. We develop a bytecode analysis that reconstructs how Hooks change traders' payments and receipts, separating charges from exchanged assets and standard fees. We then reconstruct historical settlements to measure charging frequency and economic burden. We find that direct settlement adjustment is the dominant Hook capability, supported by 71.37% of registered Hooks. Charging capability is widespread and often exercised: 24.30% of Hooks can impose undisclosed deductions, and these deductions occur in 59.23% of accounted swaps involving such Hooks. These charges generate millions of dollars in revenue, with $3.97M recorded across Hooks with available token prices. These findings reveal a gap between standard fee displays and actual trading costs, motivating explicit disclosure of Hook deductions alongside standard fees.

---


### 116. [Quantifying and Prioritizing Stealthy Source-Manipulation Threats Against Multi-Source Anomaly Detectors](https://arxiv.org/abs/2610.36693)

**<font color=#1a73e8>作者：</font>** Indraveni Chebolu, Seema Panghal, Arnab Mallick 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security pipelines often fuse several data sources and protect a downstream model with a cross-source anomaly detector. Such detectors are usually judged by their clean false-positive rate and by how well they catch random corruption. Neither metric captures an adversary who controls some sources and targets a specific downstream decision. We propose a threat-quantification score, the \emph{task-conditioned visibility margin}, defined as the least detector evidence a manipulation must reveal per unit of harm to the downstream task. The margin has a closed form, takes about $85\,\mu$s per certificate, yields a minimum-evidence attack, and identifies task-relevant directions the detector cannot see. On a 17-channel industrial telemetry benchmark, a detector that flags 82.8\% of random single-channel corruptions is first-order blind on 64.7\% of task/subset pairs in an audit of one- to four-channel subsets. Task-conditioned manipulations cause more than twice as many falsely reassuring errors as generic stealthy ones, and more of them evade the alarm on four of five splits, mainly at small budgets. Used to prioritize audits on held-out subsets, the margin finds a median of four verified failures in ten checks, compared with none for random order and two for alarm-based ranking, and performs comparably to the task-gradient baseline. It also ranks vulnerable configurations of the learned GDN and TranAD detectors and of a five-source crop-yield panel.

---


### 117. [HeteGCD: Statistics-Aware Dual-Prototype Learning for Generalized Category Discovery on Heterophilous Graphs](https://arxiv.org/abs/2610.36696)

**<font color=#1a73e8>作者：</font>** Xuanzhi Xi, Tongze Zhang, Zhili Qin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heterophilous graphs are prevalent in real-world applications, where connected nodes often exhibit dissimilar attributes or belong to different classes, posing significant challenges to conventional graph learning methods based on homophily. This limitation becomes particularly pronounced in generalized category discovery (GCD), which requires models to recognize known classes and discover novel ones using labels from known classes only. However, existing graph GCD methods typically rely on aforementioned homophily-based inductive biases, which are ill-suited to heterophilous graphs. Meanwhile, although current heterophilous graph learning methods exploit diverse neighborhood signals, their selection and fusion are often guided by supervision across all classes, including novel classes whose labels are unavailable in GCD. These limitations raise a key question: how can heterogeneous neighborhood information be effectively leveraged for category discovery without any novel-class supervision? To answer this question, in this study we propose HeteGCD, a new statistics-aware dual-prototype learning perspective for generalized category discovery on heterophilous graphs. The key idea is to examine both statistics of local attribute differences and neighborhood class distribution to extract discriminative information in feature and probability spaces simultaneously. Specifically, a gated dual-stream encoder integrates both node attributes and local attribute-difference statistics to learn informative node representations. Afterwards, a dual-prototype classifier combines feature-based similarity with distribution-based consistency to support category discovery. Experiments on five heterophilous graphs show that HeteGCD achieves competitive performance against 24 baseline combinations.

---


### 118. [Translating Poetic Emotion into Dynamic Mathematical Visuals: A Strange Attractor-Based Approach](https://arxiv.org/abs/2610.36698)

**<font color=#1a73e8>作者：</font>** Subhadra Nayak  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Poetry conveys emotional experiences through language. This project investigates how poetic emotional experiences can be represented through dynamic mathematical visualisations while further developing a pipeline for this purpose. By leveraging a pretrained RoBERTa-based emotion classifier, the system analyses the fine-grained emotional states within a poem. These detected emotions are then mapped onto the parameters of strange attractors, complex structures from dynamical systems theory, to generate abstract, deterministic, and dynamic imagery. This work situates itself at the intersection of poetry, psychology, and mathematics, aiming to extend the poetic experience beyond language into the sensory domain

---


### 119. [RankFormer: Rethinking Time Series Transformers through Representation Capacity Analysis and Progressive Decoding](https://arxiv.org/abs/2610.36703)

**<font color=#1a73e8>作者：</font>** Peiwang Tang, Cheng HE, Xijie Liang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time series forecasting plays a critical role in Web and cyber-physical systems, where large-scale services and IoT infrastructures generate complex temporal data. Transformer-based models have achieved strong empirical performance in this domain, yet the principles governing the expressive capacity of their learned representations remain insufficiently understood. Moreover, many existing models rely on simplified decoding strategies, including channel-independent modeling and direct projection heads, which limit their ability to capture complex multivariate dynamics. To address these challenges, we propose RankFormer, a novel encoder-decoder architecture for multivariate time series forecasting. We establish a rank-based analysis framework to investigate how tokenization, embedding, and attention designs affect the representation capacity of time series Transformers. Our analysis reveals that patchification increases the potential representation capacity by aggregating multiple temporal observations into each token, while subsequent encoding operations determine how much of this capacity is realized. Guided by these insights, we develop a rank-enhancing encoder with Hourglass Attention to improve rank stability during information interaction. Furthermore, we introduce the Interactive Progressive Decoder (IPD), which improves future trajectory modeling through global-guided cross-channel interaction and progressive refinement. Extensive experiments on real-world long-term forecasting benchmarks demonstrate that RankFormer achieves competitive performance against state-of-the-art methods. Code repository: this https URL.

---


### 120. [A Harness Reducing over-Defensive Writing in Agents by Isolating Objections](https://arxiv.org/abs/2610.36717)

**<font color=#1a73e8>作者：</font>** Xiaochen Chang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When expanding a report, writing with agents may introduce a stronger claim than the article makes and then disclaim it. This is called over-defensive writing. We assume that this is because the agent is writing for responding to an adversarial AI reviewer, instead of a human reader. The defensive context may also influnce the consequent when we simply ban defensive writing in the output through prompts. In order to reduce over-defensive writing, we produce a harness that separates the reviewer, filter, and writer. The writer agent receives only the problems choosen by the filter, which is an independent context. We evaluate this harness on 25 business-project drafts expanded into formal reports, the result shows that the defensive propositions decreased from 59 to 2, which is a 96.61\% reduction, no unsupported factual additions were identified while the source-claim retention rises from 80.35% to 93.12%.

---


### 121. [Nonlinear Direct Feedback Alignment for Scalable Backpropagation-Free Training](https://arxiv.org/abs/2610.36718)

**<font color=#1a73e8>作者：</font>** Wu Lin, Yan Fan, Chenxiang Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Backpropagation (BP) remains the predominant algorithm for training deep neural networks, but it is biologically implausible and suffers from the backward locking problem, constraining parallelization across layers. Direct Feedback Alignment~(DFA), which propagates the global output error directly to each hidden layer via fixed feedback matrices, has emerged as a promising alternative for addressing these limitations. However, a significant performance gap persists between DFA and BP, which we attribute to the limited ability of fixed feedback matrices to capture the nonlinear transformation from hidden representations to the network output. To address this limitation, we propose Nonlinear Direct Feedback Alignment (NDFA), which constructs each hidden-layer feedback using a lightweight nonlinear surrogate subnetwork. To enhance the effectiveness of the feedback throughout training, we further propose a learning strategy to update the surrogate subnetwork, thereby better approximating the underlying nonlinear transformation. Extensive experiments across residual networks and vision transformers on CIFAR-10, CIFAR-100, SVHN, and ImageNet datasets demonstrate that NDFA consistently outperforms existing DFA-based methods and substantially narrows the performance gap to BP, while maintaining efficient parallel training. The code is available at this https URL.

---


### 122. [SAGE: Saliency-Annealed Gated Encoder for Universal Vision Recognition](https://arxiv.org/abs/2610.36719)

**<font color=#1a73e8>作者：</font>** Le Yang, Yucheng Huang, Junyu Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When adapting self-supervised Vision Transformers (ViTs) to dense prediction, existing methods often treat the ViT as a passive feature extractor and may underuse the rich priors encoded in its representations, including saliency, global context, and high-frequency details. We propose SAGE (Saliency-Annealed Gated Encoder), an enhanced ViT-Adapter backbone that explicitly exploits these priors through three complementary innovations: (1) a saliency-guided architecture that extracts DINO-style class-token (CLS) saliency to guide feature gating and high-frequency enhancement, together with dynamic multi-layer aggregation and a local-detail branch; (2) an annealing-based training paradigm designed to improve convergence and feature quality during early training while reducing feature drift later in training; and (3) a two-stage, quality-aware training mechanism that smoothly transitions from focal loss to Varifocal Loss (VFL) within a single training run. Across the evaluated tasks (Fig.~\ref{fig:fig_com}), SAGE achieves state-of-the-art (SOTA) or competitive results on COCO (62.8 box AP and 55.3 mask AP), COCO keypoint estimation (78.5 AP), ADE20K (60.3 mIoU for semantic segmentation and 44.9 mask AP for instance segmentation), TinyImageNet classification (94.76\% Top-1 accuracy), and DIOR-R oriented object detection (78.8 AP$_{50}$). The same backbone is used across tasks, with task-specific decoders. To the best of our knowledge, SAGE is the first framework to achieve multi-task state-of-the-art results on Huawei Ascend NPUs. Code and pretrained models will be released after internal review.

---


### 123. [Progressively Refining SAM for Accurate Phytoplankton Segmentation](https://arxiv.org/abs/2610.36722)

**<font color=#1a73e8>作者：</font>** Jialin Li, Jinkun Jiang, Yuezun Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate phytoplankton segmentation is essential for ecological monitoring, yet it remains largely underexplored due to the subtle visual characteristics of phytoplankton and the scarcity of pixel-level annotations. To address these challenges, we propose PhySeg, a SAM-based segmentation framework equipped with a lightweight refinement module that progressively restores fine-grained details through multi-scale feature fusion. In addition, we construct a phytoplankton segmentation dataset by manually annotating instance-level masks for an existing dataset, providing a valuable resource for future research. Experimental results demonstrate that PhySeg improves segmentation accuracy, validating the effectiveness of the proposed module. Code is available at this https URL.

---


### 124. [Hy-Nomas: Towards Free-form Interactive World Generation](https://arxiv.org/abs/2610.36729)

**<font color=#1a73e8>作者：</font>** Qiaoling Chen, Jiaxiang Cheng, Xueqing Deng 等 38 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive world generation requires models to follow successive commands while preserving relevant history and action consequences. We present Hy-Nomas, a video world model with an 8B diffusion backbone that supports free-form text instructions and continuous camera control across multiple interaction turns. It generates variable-length segments conditioned on current inputs and cached history. Our central design aligns structured video captions with action-aware causal attention: descriptive context remains accessible across segments, while action instructions are restricted to their intended temporal windows. A vision-language Prompt Enhancer (PE) translates user requests and multimodal interaction histories into structured conditions for the next segment. A multi-stage curriculum progressively introduces causal generation, text interaction, camera control, and training on model-generated histories, followed by diffusion distillation. In human evaluation, Hy-Nomas shows superior performance over existing world models. We release model weights, code and benchmarks, together with a lightweight adaptation workflow, to support reproducible research on interactive world generation.

---


### 125. [Beyond LWE: Post-Quantum Assumptions under a Counterfactual Break of the Dihedral Coset Problem](https://arxiv.org/abs/2610.36731)

**<font color=#1a73e8>作者：</font>** Ramses Fernandez  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A refuted 2026 claim of an efficient quantum algorithm for the Dihedral Coset Problem (DCP) motivates this survey of the consequences of a genuine breakthrough. We distinguish a noiseless cyclic coset-state solver, a solver with a prescribed failure exponent, and an extrapolated-state solver. Regev's rare-corruption observation already makes the first hypothesis sufficient for lattice algorithms at some polynomial approximation factors; the witnessing algorithm determines the quantitative bounds. We compose unstructured reductions with explicit sample, state-preparation and success conditions, and compare their sufficient guarantees with more than thirty lattice and non-lattice assumptions. We restate the structured state conversion of Wen and Zheng and audit its forward parameter certificate; the printed bound supplies no certificate at the ML-KEM ring and modulus. We use an explicit affine embedding for heuristic gap estimates, explain the lossiness connection from decision NTRU to search Ring-LWE, and distinguish ordinary from module uniqueness. Chen's withdrawn 2024 quantum algorithm for LWE and a proposed repair of its post-processing would, if correct, reach only a many-sample, small-noise LWE regime that the failure-exponent hypothesis already covers for exponents below $1/2$, and no deployed parameter set. Tables separate rigorous consequences, heuristic comparisons and unverified applications, and distinguish solving a proof assumption from attacking a scheme. Classical structural attacks on Classic McEliece, which do not involve DCP but put the concrete security of the scheme under revision, are summarised here and analysed in detail in a companion paper. The survey closes with open questions and a scenario-planning checklist that requires a complete efficient reduction.

---


### 126. [Readout and Operating-Point Sensitivity in Event-Stream Candidate Selection](https://arxiv.org/abs/2610.36743)

**<font color=#1a73e8>作者：</font>** Yifan Shuai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event-triggered recording needs a useful combination of target capture and false triggers, yet representation comparisons can change with readout and threshold calibration. We evaluate real event accumulations from 520 DailyDVS-200 clips and 47 participants using participant-disjoint training, validation, and testing. The original study varies frozen encoder scale, accumulation duration, and temporal view count; a post-review extension adds two supervised-pretrained convolutional encoders, a 61,586-parameter trained CNN with three seeds, ten repeated participant partitions, and calibration sensitivity. At 50 ms/eight views under the primary handshake-or-fall policy, DINO-S CLS captures 101/132 targets with 40/388 false triggers, versus 78/132 and 35/388 for patch mean. DINO-B CLS has lower selected-threshold capture but higher fold-wise low-FPR partial AUC (0.746 versus 0.732). MobileNetV3-Small captures 97/132 with 53/388 false triggers, demonstrating why lightweight baselines and actual operating points matter. Across ten dependent repartitions, mean normalized partial AUC is 0.738 for DINO-B CLS and 0.674 for MobileNet. The original LeJEPA S-to-B capture difference is 8.3 points, but its multiplicity-adjusted interval includes zero. Duration and view-count effects remain policy dependent. We find no established JEPA-specific advantage. The evidence concerns offline action-defined candidate selection on previously used development data; it does not establish personal recording value, continuous false alarms per hour, or eyewear energy.

---


### 127. [Multi-task Disentangling Fusion Mamba-CNN for MODIS Spectral-Temporal Unmixing with Endmember Variability Modeling](https://arxiv.org/abs/2610.36750)

**<font color=#1a73e8>作者：</font>** Motasem Alkayid, Yimin Zhu, Naser El-Sheimy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spectral-temporal unmixing of MODIS time series is essential for applications such as abundance mapping and spectral library construction, yet it remains challenging due to (i) spectral-temporal information coupling in MODIS data, (ii) intra-class endmember spectral variability and inter-class signature ambiguity, and (iii) the instability of naively fusing multiple expert representations. This paper presents the Multi- task Disentangling Fusion Mamba (MDF-Mamba) to address these limitations. To resolve spectral-temporal coupling, we design a disentangling architecture that pairs per-channel spectral experts with a dedicated bidirectional state-space (Mamba) temporal branch. Convolutional modules each process a single spectral channel, while the Mamba branch encodes the cross-channel seasonal trajectory, forming a multi-branch expert ensemble with soft inter-expert reweighting based on squeeze-and-excitation. For the integration of these spectral and temporal expert outputs, we introduce mHCFusion, adapting the manifold-constrained hyper-connection framework to merge the outputs in a stable and interpretable manner. Endmember variability is addressed by extending the linear mixing model with pixel-wise learnable spectral variability weights that capture intra-class endmember variation. Finally, we design a multi-task training objective that combines supervised abundance estimation with self-supervised spectral reconstruction and endmember regularization terms on the same training data, yielding a highly efficient framework for spectral-temporal unmixing. Experiments on MODIS time series covering the Alberta and Saskatchewan provinces show that MDF-Mamba achieves the best performance on 12 of 14 evaluation metrics across both datasets (7 of 7 on Alberta; 5 of 7 on Saskatchewan), ranking second on the remaining two.

---


### 128. [Generative Refinement Learning for Temporal Interpolation in Scientific Machine Learning](https://arxiv.org/abs/2610.36751)

**<font color=#1a73e8>作者：</font>** Pu Ren, Michael W. Mahoney, N. Benjamin Erichson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computationally expensive simulations and real-world observations often provide data at a lower temporal resolution than downstream tasks require. Averaging observations at fixed grid points can introduce errors, and motion estimates alone do not determine how the physical field values change. In this work, we study whether learning to correct a simple numerical interpolation improves the reconstruction of intermediate scientific fields. Our model, interpolative FLow EXpert (iFLEX), first estimates the missing field by taking a weighted average of the two observations at each grid point, giving more weight to the observation closer to the requested time. During training, subtracting this estimate from an observed intermediate field gives the residual that a conditional diffusion model learns to generate. Both observations condition the model, together with the target time, the interval between observations, and available physical parameters. To reconstruct an unobserved intermediate field, the generated residual is added to the weighted average. We evaluate iFLEX on Navier-Stokes Kraichnan turbulence, Shanghai radar precipitation, and sea surface temperature. Across these datasets, iFLEX achieves lower reconstruction error than the evaluated baselines, including optical-flow and diffusion models developed for video frame interpolation in computer vision. In a controlled turbulence comparison at a Reynolds number of 36,000, learning the residual reduces relative Frobenius norm error from about 13.7 for direct field generation to 10.5, with the diffusion backbone and training setup held fixed. Code is available at this https URL.

---


### 129. [Efficient Remote Sensing Image-Text Retrieval via Interaction-Free Recall and Text-Guided Reranking](https://arxiv.org/abs/2610.36756)

**<font color=#1a73e8>作者：</font>** Xi Chen, Xu Chen, Xiamgyang Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing (RS) image-text retrieval plays a critical role in understanding massive RS imagery. However, the dense multi-object distribution and complex backgrounds in RS imagery make it difficult to simultaneously achieve fine-grained cross-modal alignment and efficient retrieval. Existing methods either rely on complex cross-modal interactions that lead to low retrieval efficiency, or depend on large-scale vision-language adaptation, which requires massive data and computational resources. To address these issues, we develop a fast-then-fine (FTF) retrieval framework centered on interaction-free multi-granular recall and parameter-free text-guided cross-modal reranking with the Balanced Text-guided Interaction Block (BTIB). Specifically, interaction-free multi-granular recall pre-computes gallery embeddings and matches them with the corresponding query embedding without full-gallery token-level text-image interaction, while text-guided cross-modal reranking with BTIB refines local semantic correspondence within the top-K candidate set. Furthermore, an inter- and intra-modal loss is designed to jointly optimize cross-modal alignment across multi-granular representations. Extensive experiments on public benchmarks demonstrate that the FTF achieves competitive retrieval accuracy while significantly improving retrieval efficiency compared with existing methods.

---


### 130. [GeoGSplat: Geometry-Grounded Non-Pixel-Aligned Gaussian Splatting](https://arxiv.org/abs/2610.36760)

**<font color=#1a73e8>作者：</font>** Jiale Wang, Chen Zhao, Haoyang Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward Gaussian Splatting enables efficient novel view synthesis, but pixel-aligned prediction makes the primitive count grow with image resolution and view count, leading to substantial redundancy and increased computational cost. Non-pixel-aligned methods address this limitation by predicting a fixed number of Gaussians. Without explicit ray and depth constraints, these methods yield misplaced Gaussian centers, causing rendering artifacts under large viewpoint changes. To address this issue, we introduce GeoGSplat, a geometry-grounded feed-forward model that explicitly incorporates geometric priors into the non-pixel-aligned framework. A dual-branch encoder constructs Anchors and Triplane to capture coarse 3D structure and fine-grained scene features, respectively. Subsequently, a hierarchical decoder progressively decodes dense 3D points and Gaussian primitives, enabling 3D reconstruction and novel view synthesis. GeoGSplat surpasses both state-of-the-art pixel-aligned and non-pixel-aligned Gaussian Splatting methods on DTU and NRGBD in terms of novel view synthesis and reconstruction. The advantage of our geometry-grounded paradigm further increases as target viewpoints move farther from the input cameras, demonstrating stronger generalization to large viewpoint changes. Project Page: this https URL

---


### 131. [Evaluation-Guided Demonstration Refinement for Vision-Language-Action Policies: The Winning Entry in the MetaFine Open Competition](https://arxiv.org/abs/2610.36765)

**<font color=#1a73e8>作者：</font>** Lifan Zheng, Guotao Chen, Zhenyang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We fine-tuned a separate $\pi_{0.5}$ policy for each of the five tasks in the MetaFine Open Competition, with a task-specific training mixture and number of actions executed per prediction. Training started from the official demonstrations and expert procedures. Local evaluation exposed recurring grasping, pushing, and insertion failures. We addressed them by revising the demonstrated motions and by adding expert continuations from states the policy reached, while keeping nominal demonstrations in training. Checkpoints were compared on every instruction, so that a gain on one instruction could not hide a loss on another. Our submission, MAI, ranked first overall with a score of 96.66.

---


### 132. [Externalizing Hand Grip Pressure Through Real-Time Visual Feedback](https://arxiv.org/abs/2610.36769)

**<font color=#1a73e8>作者：</font>** Andrew L. Huard, Avinash Ajit Nargund, Misha Sra  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Grip pressure, including contact force and its distribution across the hand, is central to skilled grasping but is not directly visible. This makes it difficult to teach, learn, and self-correct in grip-dependent motor tasks, where verbal instruction and tactile demonstration provide only partial guidance and no real-time, spatially resolved feedback tied to the learner's own grip. Using an instrumented glove, we compare pressure feedback visualizations for such guidance, evaluating how visualization type and, secondarily, sensor-region mapping shape pressure-matching performance in novices. In a study using baseball and table tennis as representative grip tasks (N=28), we find that a continuous gradient visualization produces significantly more accurate pressure matches and lower gaze entropy than a discrete bar display, despite participants perceiving the bar as more precise for pressure magnitude. Perceived precision and objective performance therefore diverged: the encoding participants judged more precise was not the one they matched more accurately with. Grip-tailored sensor-region mappings further reduced perceived temporal demand and effort, although this subjective workload advantage did not extend to objective matching accuracy. Overall, continuous pressure feedback supported more accurate grip matching and more concentrated viewing, and we present design considerations for real-time pressure feedback in motor skill guidance.

---


### 133. [Batching the Reflective Optimization Loop: Parallel Proposals Make GEPA Faster and Better](https://arxiv.org/abs/2610.36774)

**<font color=#1a73e8>作者：</font>** Jialin Zhang, Lakshya A Agrawal, Shangyin Tan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reflective text optimization makes agentic systems better, but the optimization loop is itself a resource-hungry workload whose sequential structure leaves parallel evaluation capacity idle. We extend the open-source GEPA optimizer to propose and evaluate a batch of candidates on each optimization step instead of one candidate at a time. In our sweep on two tasks, most batched runs finished in half the wall-clock time or less, and the fastest in about a quarter to a third. Batched settings also achieved higher held-out test scores, from 68.9% to 72.1% on LiveBench-Math (with $2\times2$) and from 49.0% to 60.0% on HoVer (with $8\times1$). A simple runtime model explains the measured speedups under a finite worker pool, and batched settings also spend their metric-call and dollar budgets more efficiently. We frame the axes along which a reflective optimization step can scale in parallel, a first look at allocating a fixed optimization budget across them.

---


### 134. [CVBL-CCTV-Face Dataset for Real-World Face Enhancement and Recognition in Surveillance](https://arxiv.org/abs/2610.36781)

**<font color=#1a73e8>作者：</font>** Manish Das, Ajay Kumar Yadav, Shiv Ram Dubey 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In real-world surveillance settings, facial captures from closed-circuit television systems suffer from degradations such as low resolution, motion blur, noise, and occlusions, which undermine dependable face recognition. In this study, we propose a framework for super-resolution and identity recognition, aimed at surveillance applications. For this purpose, we present the CVBL-CCTV-Face Dataset which is a dataset of real-world images taken in an unpaired manner where each pair consists of a low-quality (LQ) image of a face captured by a 8MP IP Dome CCTV camera together with a high-quality (HQ) reference image that is taken in controlled settings. In order to cope with the various problems posed by such datasets, we construct a modular system that involves face detection, deep learning-based super-resolution of low-quality face images, and identity recognition through L2-normalized embeddings extracted by an embedding model. Enhancement models are trained and tested according to three different setups, and the system is deployed for identity verification in a real-time unconstrained environment.

---


### 135. [OmniGlimpse: Asymmetric Identity Memory for Online Multi-View Tracking](https://arxiv.org/abs/2610.36785)

**<font color=#1a73e8>作者：</font>** Rangya Zhang, Jiaping Xiao, Yujing Shang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view tracking extends visual coverage beyond a single camera, providing complementary observations when targets are occluded or leave the view. This raises a question: how can observations from different views be matched to the correct identities without offline scene-specific training or camera calibration? Progress toward this goal remains limited because many offline formulations assume such deployment-specific knowledge, while online adaptation can amplify association errors. We study this problem as online multi-view identity maintenance (OMIM): targets are initialized once per view, with no further identity labels provided after each initialization. To this end, we introduce OmniGlimpse, an asymmetric propose-verify framework that separates adaptive association from stable identity consolidation. At the representation level, short-term local and cross-view evidence is mapped into target-specific adaptive spaces to propose associations, whereas long-term identity distributions are maintained for verification in a canonical space defined by a frozen encoder. At the update level, short-term evidence may guide current associations, whereas, after bootstrapping, only verified observations may update persistent memory or drive adaptation. Under a unified target-specified evaluation protocol, OmniGlimpse improves over the best evaluated online baseline for each metric by 9.1 IDF1 and 22.1 CVIDF1 points on M3Track. The corresponding gains on MvMHAT are 20.3 and 26.2 points. Despite using no offline scene-specific training, it outperforms offline-trained references in IDF1 and remains competitive in cross-view association. These results support an approach to online identity maintenance that adapts to changing appearances while consolidating reliable evidence into stable identity anchors.

---


### 136. [Visual Autoregressive Generation with Next Token Imagination](https://arxiv.org/abs/2610.36793)

**<font color=#1a73e8>作者：</font>** Ruihang Jiang, Zongyao Zhao, Zhaolin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The space of possible visual content is enormous, and arguably unbounded. Any training set, however large, therefore covers only a tiny fraction of it. Yet generative models are typically trained to fit only the images they are given. In visual autoregressive (AR) generation, for example, each token is predicted from the preceding ground-truth (GT) tokens and supervised solely by the GT next token. Confining learning to observed data in this way limits how much of the visual distribution a model can capture. In this work, we hypothesize that letting a model imagine beyond its training data, by exploring plausible visual realizations it has never observed, can ease this limitation. We use visual AR generation as a proof of concept, since its fixed, discrete token space makes imagination easier to steer and constrain. We propose Next Token Imagination (NTI), a method that allows the model to explore beyond the GT next token, subject to a carefully designed criterion that keeps this imagination bounded by the underlying visual distribution. Extensive experiments on ImageNet show that NTI substantially and consistently improves the fidelity of generated images, approaching state-of-the-art diffusion and AR models while using a smaller model and lower training cost.

---


### 137. [HqcLethe: Streaming HQC Encapsulation for Tiny Stateless Servers](https://arxiv.org/abs/2610.36808)

**<font color=#1a73e8>作者：</font>** Wind Wong, Klaus v. Gleissenthall  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Stateless post-quantum authenticated key exchanges such as post-quantum WireGuard hedge against unexpected cryptanalytic advances by combining a lattice KEM with code-based Classic McEliece. However, recent attacks have led Germany's BSI to advise against McEliece, which leaves these protocols with lattices alone. HQC, the code-based KEM that NIST selected, could restore diversity, but its keys do not fit in a single packet, so a server would have to buffer multi-packet handshakes. This would leave an attack surface for memory exhaustion, which is what WireGuard's stateless handshake was designed to avoid in the first place. McTiny demonstrated that stateless key encapsulation for Classic McEliece is possible by streaming key blocks one-at-a-time. However, HQC's encapsulation does not split as easily into individual packets, as cyclic polynomial multiplication, unlike matrix-vector multiplication, is inherently non-local.
We present HqcLethe, a stateless key exchange that streams an HQC encapsulation in packet-sized pieces. It uses the Chinese remainder theorem to split the polynomial multiplication into independent remainders, one per packet, and masks them so that they reveal no more than an ordinary HQC ciphertext, which we prove in Rocq with SSProve; we also verify session secrecy, server authentication and forward secrecy in ProVerif. Client puzzles bound CPU exhaustion, and HqcLethe removes memory exhaustion: on a Raspberry Pi 3B+, each worker runs in a fixed 1.2-1.6 MiB. At category 5 it sends 27x fewer bytes and uses 9.0x less server CPU than McTiny, the earlier stateless code-based design.

---


### 138. [An Incremental Knowledge-Graph Learner Digital Twin for Evidence-Grounded Early Warning](https://arxiv.org/abs/2610.36820)

**<font color=#1a73e8>作者：</font>** Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Early-warning models in learning analytics can identify learners at risk of failure or withdrawal, but the resulting alerts are often only weakly connected to inspectable learning evidence. A risk score may indicate that intervention is needed without showing which traces, assessment events, or temporal patterns justify the alert. This paper introduces an incremental Learner Digital Twin for evidence-grounded early warning, implemented as a lightweight knowledge graph. The twin is updated at temporal checkpoints by replaying learning traces and assessment records, and it serves both as a feature-extraction substrate and as an explanation-grounding substrate. Predictive features are derived through graph-mediated queries, while features, attributions, alerts, evidence items, and raw records are represented as queryable graph entities. The framework is instantiated and evaluated on a public learning-analytics benchmark under a temporal protocol. The results show that graph-mediated feature extraction preserves the predictive behavior of equivalent raw-table features across model families and checkpoints. Generated alerts are materialized as evidence chains linking risk decisions to feature attributions, evidence items, and raw platform records. The study shows that early-warning prediction can be routed through a semantic and provenance-aware representation while preserving predictive performance and adding traceability, verifiability, and evidence-grounded explanation.

---


### 139. [Drop the Details, Get the Gist: Dynamic Conceptual Representation for Video Recognition](https://arxiv.org/abs/2610.36832)

**<font color=#1a73e8>作者：</font>** Ryoya Yoshiyama, Bowen Wang, Yuta Nakashima  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept Bottleneck Models (CBMs), which route predictions through a layer of human-interpretable concepts, have substantially improved the interpretability of visual classification by exposing an explicit, language-based rationale for each prediction. Most existing work focuses on static images, and temporal dynamics in videos have been underexplored in conceptual representation. We propose a framework that extends concept-based image recognition to procedural video understanding. It represents a multi-step video as a temporal sequence of segment-level concept score vectors and feeds this sequence into a Transformer encoder to predict the class label. We also explore a way to estimate the contribution of each concept for further interpretability. We evaluated three concept sets of different granularities on cooking and household-activity videos and found that coarser-grained concepts are sufficient for classifying these videos, which implies that fine-grained textual descriptions may be unnecessary.

---


### 140. [MVRCap: Towards Comprehensive Video Captioning via Hierarchical Multi-Dimensional Verifiable Rewards](https://arxiv.org/abs/2610.36838)

**<font color=#1a73e8>作者：</font>** Weihuang Lin, Xianing Chen, Zhibin Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite significant progress, current models struggle to generate comprehensive video captions, constrained primarily by coarse-grained supervision, which often fails to capture spatial-temporal dynamics and the underlying logical intent. To address this issue, we introduce MVRCap, a novel framework that reformulates video captioning as a reinforcement learning task steered by structured verification. Central to our approach is a Fine-Grained Verifiable Reward mechanism, serving as dense supervision to enforce rigorous visual-semantic alignment. Specifically, we construct this reward system anchored by three complementary pillars: a Hierarchical Concept Coverage Reward utilizing our newly constructed MVRCap-QA dataset to ensure multi-dimensional completeness and semantic depth, a Factuality Verification Reward to enhance factual consistency, and a Conciseness Constraint to maximize semantic density. Furthermore, we curate the high-quality MVRCap-SFT dataset, providing structured annotations across six key dimensions, to serve as a robust foundational initialization for the RL policy in this training pipeline. Extensive experiments demonstrate that MVRCap achieves state-of-the-art performance on authoritative benchmarks including VDC, CAPability, and VC4VG.

---


### 141. [AxisQ: Depth-Adaptive Channel--Frequency Quantization for Camouflaged Object Detection](https://arxiv.org/abs/2610.36844)

**<font color=#1a73e8>作者：</font>** Chi Ruan, Tianqi Li, Xin He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camouflaged object detection (COD) depends on weak texture and boundary cues that can be destroyed by aggressive post-training quantization (PTQ). Existing PTQ methods mainly optimize quantizers or reconstruct network blocks, while using a single precision-allocation domain throughout hierarchical backbones. Instead, we introduce AxisQ, a depth-adaptive bit-allocation framework motivated by the observation that the useful allocation axis changes with feature depth. Under a fixed per-layer average activation-bit budget, AxisQ allocates precision in the channel domain for shallow features and in the local-frequency domain for deep features, using COD-aware sensitivity to better preserve subtle foreground regions and ambiguous boundaries. We also formulate a boundary-aware Hessian approximation for reconstruction by incorporating boundary-weighted gradient and error statistics. Experiments across multiple COD models and diverse benchmarks demonstrate improved accuracy over the strongest baselines at low bit widths, with relative weighted F-measure gains of 12.7% for CFRN and 33.3% for CamoFormer-P on CAMO under W2A2 quantization. These results support adapting the allocation domain to feature depth as a transferable quantization strategy for hierarchical COD models.

---


### 142. [Conservative Policy Iteration For Zero-Sum POSGs](https://arxiv.org/abs/2610.36847)

**<font color=#1a73e8>作者：</font>** Erwan C. Escudie, Matthia Sabatelli, Jilles Steeve Dibangoye  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Occupancy-state reductions make dynamic programming possible for zero-sum partially observable stochastic games (zs-POSGs). Existing point-based solvers usually optimise a central value function. This restores Bellman recursion, but it requires point-based updates over high-dimensional occupancy spaces. We introduce an approximate policy-iteration algorithm for finite-horizon zs-POSGs. The method maintains one policy per player and updates both jointly along occupancy trajectories induced by conservative policy updates. Instead of approximating a full central value function, each update uses a single supporting hyperplane induced by the current joint policy. The algorithm alternates local policy improvements, conservative updates, and persistent exploration. Computation is therefore concentrated on occupancy regions where the current joint policy is exploitable. On finite-horizon zero-sum POSG benchmarks, the method is competitive at small horizons and often improves the runtime-exploitability trade-off at larger horizons compared with PBVI, HSVI, and CFR+.

---


### 143. [uTHCD-C: A Corruption-Robustness Benchmark for Tamil Handwritten Character Recognition](https://arxiv.org/abs/2610.36850)

**<font color=#1a73e8>作者：</font>** Preethi S, Meeradevi T, Arun Prakash A  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluation of Tamil handwritten character recognition (HCR) has largely focused on clean test images, and a standardized multi-corruption robustness benchmark for isolated Tamil HCR has not been established. We introduce uTHCD-C, a corruption-robustness benchmark based on the unconstrained Tamil Handwritten Character Database (uTHCD). The benchmark defines ten corruption types, including a handwriting-specific stroke-thinning corruption, at five severity levels. We evaluate nine convolutional and transformer-based architectures using five-fold stratified cross-validation and writer-independent testing. Robustness is quantified using mean Corruption Error (mCE), normalized against a VGG16-BN reference. We additionally compare parameter count, computational complexity, and inference throughput to characterize the computational requirements of the evaluated architectures. The results establish comparative robustness baselines for Tamil HCR, revealing substantial differences across architectures: ConvNeXt and Swin achieve the lowest mCE values (0.75 and 0.83, respectively), whereas ShuffleNet and MnasNet exhibit higher values (1.55 and 1.85, respectively). The accompanying efficiency measurements characterize the trade-offs between corruption robustness and computational requirements. By providing standardized corruption configurations, evaluation protocols, and comparative results, uTHCD-C establishes a reproducible basis for future research on robust and computationally efficient Tamil HCR.

---


### 144. [LingGS: Decoupling Feed-Forward Geometry Prediction from Camera Tracking for High-Fidelity Gaussian SLAM](https://arxiv.org/abs/2610.36853)

**<font color=#1a73e8>作者：</font>** Da Li, Yihan Zang, Ivan Viola 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving high-quality reconstruction and responsive camera tracking remains challenging for monocular RGB Gaussian splatting SLAM under a limited optimization budget. We present an online system that addresses this challenge by combining learned geometric priors with explicit geometric camera tracking, which can substantially outperform learned camera prediction in terms of tracking accuracy. A frozen streaming 3D foundation model serves as a virtual RGB-D sensor, providing depth estimation from monocular video. An explicit geometric solver then estimates camera motion through feature reprojection, and a streaming Gaussian mapper integrates the resulting observations into a dense scene representation. We further show that geometric tracking improves camera pose accuracy across representative streaming geometry backbones, demonstrating the broader applicability of our approach. Extensive experiments on indoor and outdoor datasets show that our method significantly improves reconstruction quality over existing approaches, achieving about 7 FPS on a single RTX 4090 and delivering 2-3 times the throughput of the evaluated prior SLAM systems.

---


### 145. [Evaluating AlphaEarth Embeddings for Crop Classification: Separability, Temporal Dynamics, and Cross-Regional Transferability](https://arxiv.org/abs/2610.36857)

**<font color=#1a73e8>作者：</font>** Priyanka Goyal, Maitreyee Sar, Adway Mitra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Earth Observation (EO)-based agricultural monitoring is shifting from pixel-level spectral analysis toward representation-driven modeling, yet systematic evaluation of learned representations across spatial, temporal, and domain-generalization dimensions remains limited. Geospatial foundation models generate high-dimensional embeddings encoding spatio-temporal land-surface properties, but their utility for agricultural applications remains insufficiently understood. This study presents a representation-agnostic evaluation framework integrating geometric separability, temporal dynamics, spatial robustness, and cross-regional generalisation. A 64-dimensional AlphaEarth embedding space is benchmarked against Sentinel-2 reflectance, NDVI-derived phenology, and harmonic features using field-scale data from the Conterminous United States (CONUS; 2017-2023) and Northern India (2021).
Traditional features achieve strong linear separability (Fisher ratio), while embeddings provide superior distribution-aware separation -- Bhattacharyya and Mahalanobis distances up to an order of magnitude higher for spectrally similar pairs (e.g. Corn/Soybeans: 3.9 vs. 0.10). Embeddings uniquely capture multi-year crop rotation dynamics, reaching a separability ratio of 1.784 versus a maximum of 1.003 across all engineered features, and exhibit lower residual spatial autocorrelation of errors (mean Moran's $I \approx 0.17$). However, harmonic and NDVI features show stronger cross-continental transferability (US $\to$ India Macro F1: 0.493 vs. 0.326 for embeddings), reflecting better distributional alignment. The combined feature space yields balanced performance, supporting hybrid modeling. These findings reveal a fundamental trade-off between representational richness and cross-region transferability, providing a structured framework for feature selection in large-scale crop classification.

---


### 146. [Forget the Data, Keep the Capability: Switchable Unlearning for Retrieval](https://arxiv.org/abs/2610.36858)

**<font color=#1a73e8>作者：</font>** Jingong Chen, Kyle Gao, Guangyuan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Privacy compliance requires re-identification models to selectively forget individuals while preserving their ability to recognize others. For this, we present MoME, a switchable framework that can adapt pre-trained backbones for privacy compliance, allowing the same model to switch between Full mode for standard inference and Core mode for unlearned inference. MoME splits one backbone into core parameters that preserve retrieval and zero-initialized parasitic parameters that carry the full-data knowledge, and training them under gradient isolation so the core never receives a forget-set gradient. Disabling the branch yields Core, which satisfies a request to delete a person's training data, and enabling it yields Full, which retains what the deleted data taught, so honoring the request is a flag flip rather than a retraining run. We prove Core independent of the forget set up to an audited set of coupling channels and introduce the rank-based Forgetting-Rank statistic to audit that independence in a trained model. On Market-1501, VeRi-776 and RegDB, Core reads at a retrained reference under three membership attacks while retrieving above it, and the retrieval advantage carries to ResNet and CLIP backbones. Code and weights are available at this https URL.

---


### 147. [UniPCH: A Unified Framework for Cross-Chain Payments via Payment Channel Hubs](https://arxiv.org/abs/2610.36866)

**<font color=#1a73e8>作者：</font>** Yuanming Shao, Yuming Feng, Weizhe Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Payment channel hubs (PCHs) enable private cross-chain payments, but existing protocols remain difficult to extend across heterogeneous blockchains. Their payment flows often depend on how particular blockchains represent transactions, authorize channel updates, and settle balances. Some protocols do not explain how their channels are implemented on actual blockchains. Supporting a new ledger or execution model requires a corresponding channel realization and may also require protocol adaptation and security analysis. We present UniPCH, a framework with two layers that separates native channel execution from private cross-chain payment logic. The lower UniPC layer defines common state transitions and security requirements. It separates task authorization from confirmation of the complete channel state. We provide realizations for UTXO ledgers and account ledgers that support smart contracts. At the upper layer, we develop selective re-signing blind conditional signatures (S-RBCS) to coordinate conditional authorization across hubs. Using S-RBCS, we construct a payment protocol that coordinates different channels in four phases. Our analysis establishes local UniPC security, griefing resistance, economic atomicity, and session unlinkability. We implement a Go prototype and evaluate the running time and bandwidth of each phase under different network conditions and system parameters. Results show modest computational overhead from the common interfaces. Most evaluated configurations run faster than comparable schemes under network delay. A full refresh ablation shows that reusing valid task evidence reduces computation and communication costs in the account realization.

---


### 148. [Tail Cues, Principal Corrections: Plug-and-Play Rectification for Open-Set Test-Time Adaptation](https://arxiv.org/abs/2610.36870)

**<font color=#1a73e8>作者：</font>** Yingkai Yang, Chaoqi Chen, Hui Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open-Set Test-Time Adaptation (OSTTA) operates on non-stationary target streams where covariate and semantic shifts coexist. Existing TTA methods often obtain adaptation signals by updating model parameters or maintaining mutable memories, which can be costly and vulnerable to unknown samples. We present TALOR, a lightweight, backward-free rectification module that uses the source linear head as a geometric anchor. The head-induced basis decomposes each normalized feature into high-gain principal coordinates and low-gain tail coordinates. TALOR estimates a soft-routed affine correction in the principal subspace, combining a regime-level principal bias with a tail-conditioned slope that captures sample-level tail-to-principal coupling. Using weighted ridge regression, it subtracts this drift estimate from the principal coordinates, reconstructs the feature and feeds it into the source head. On the ImageNet-C benchmark with six csOOD datasets, TALOR outperforms the next-best UniEnt by 2.2% H-score while running 2.5x faster and using only 12% of its GPU memory; as a post-correction plug-in, it further boosts COME to 68.4% H-score with only 2% additional memory overhead.

---


### 149. [RangeRectQuant: Compressing Scientific Fields for Every Future Rectangular Sum](https://arxiv.org/abs/2610.36873)

**<font color=#1a73e8>作者：</font>** Jiahao Zhang, Xinling Wen, Yu Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scientific rasters are often stored before the regions to be measured are known. Independent pixel-error bounds can force exact integer reconstruction when one absolute error budget covers every future rectangle. Coordinated changes allow every pixel to change while every rectangular sum remains accurate. A prefix sum accumulates values from the top-left corner. Four such sums determine any rectangular total. RangeRectQuant preserves the pixel range and designated exact samples while controlling errors in prefix sums. At each row position, we characterize exactly which errors let the remaining pixels meet these constraints. These errors form a single integer interval, even when many completions exist. A backward pass finds its endpoints; a forward pass uses them to choose quantized pixels. The resulting field meets the prescribed error budget for every axis-aligned rectangle, with linear work and workspace proportional to one row. Experiments on geographically held-out built-surface and water-occurrence maps show substantial storage savings over alternatives meeting the same requirements. Data producers encode once; later users measure arbitrary rectangles without the source, re-encoding, or query-specific correction.

---


### 150. [HoloRecon: Incremental Reconstruction of Long-Range Panoramas with Global Consistency](https://arxiv.org/abs/2610.36876)

**<font color=#1a73e8>作者：</font>** Zhuoxiao Li, Xinyi Liu, Hongye Hou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-sequence panoramic reconstruction requires detailed scene geometry and globally consistent camera poses across distant revisits. Panoramic SLAM and incremental SfM rely on feature correspondences, but repeated, similar structures and small partial overlap make reliable long-range connections difficult to establish, leaving accumulated drift unresolved. Feed-forward models offer detailed local geometry, but their high computational costs limit inference window size, necessitating additional constraints for global consistency. This motivates combining continuous feature-based tracking and sparse mapping with rapid, high-quality local reconstruction from feed-forward models to achieve accurate localization and globally consistent dense mapping over long sequences. We therefore propose a panoramic reconstruction framework that couples an ORB-based sparse panoramic mapping frontend with a fine-tuned feed-forward model. Our key insight is that predicted local geometry enables 3D verification of feature matches across distant revisits, yielding long-range camera constraints even between regions. We calibrate predicted depths with sparse landmarks and use verified connections to optimize the global pose graph, updating dense geometry with the corrected camera poses. We also introduce PanoRecon, a seven-scene benchmark with repetitive architecture, large and small loops, and reference camera poses and LiDAR geometry for evaluating global consistency. Our method achieves the lowest mean absolute trajectory error and high F-1 Score among the evaluated methods. Project Page:this https URL

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-257](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
