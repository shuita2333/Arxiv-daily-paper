# 📦 其他研究 | 2026年11月04日

> 本类共 **633** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

---

### 51. [Brain-Behavior Modeling from Multimodal MRI using Opportunistic Pretraining and Common-Cohort Adaptation](https://arxiv.org/abs/2611.00114)

**<font color=#1a73e8>作者：</font>** Md. Tanvir Rahman, Taslima Ferdaus Shuva, Nabil Anan Orka 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Incomplete imaging coverage limits sample sizes for multimodal cognitive prediction. We evaluated a two-stage opportunistic deep ensemble using baseline Adolescent Brain Cognitive Development Study data to predict fluid, crystallized, and total cognition. Separate neural models processed structural/diffusion, resting-state, and task-based MRI data with covariates. Models were pretrained on eligible modality cohorts (up to 9,686 participants), adapted to common training cohorts, and fused via Ridge regression (trimodal cohort: 4,216 participants). Five-fold family-aware cross-validation compared this approach against constituent and covariate-only models. Two-stage training increased mean test coefficient of determination (R^2) in 24 of 27 comparisons (median gain: 0.0081). Fusion increased mean R^2 by 0.0051-0.0333 over the strongest constituent and reduced mean absolute error by 0.0067-0.0976. Task-plus-resting-state and trimodal ensembles reduced absolute error across all targets (nominal p <= 0.0108). Task-plus-resting-state fusion achieved the highest mean R^2 for fluid (0.2222) and total cognition (0.3665), while structural-plus-resting-state led for crystallized cognition (0.3706), yielding R^2 gains of 0.0805, 0.1180, and 0.0890 over covariate-only references. Ablations showed expanded pretraining drove most improvements. Gradient-based attribution identified target-dependent input patterns. These findings support using partially observed cohorts for model development to achieve modest fusion gains. Pending external validation, this approach may support MRI-informed cognitive phenotyping.

---


### 52. [CDBM: Complexity-Diversity Framework for Building Morphology Analysis](https://arxiv.org/abs/2611.00122)

**<font color=#1a73e8>作者：</font>** Evgenii Maslov, Alexandra Vabnits, Denis Karpov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Complexity-Diversity Building Metrics (CDBM), twelve interpretable descriptors for building massings represented as vertical extrusions. They measure how strongly geometric detail is expressed (complexity) and how unevenly it varies across one- and two-dimensional elements (diversity). Computed for 482,241,306 OpenStreetMap buildings and compared with 3D Building Metrics (3DBM) and the LION shape latent on task-specific samples, CDBM is tested on function, region, contextual relevance, real-generated discrimination, human preference and geometry-conditioned generation. With gradient boosting, CDBM best separates generated from mapped massings and best matches human preference; with logistic regression it matches 3DBM on realism. 3DBM leads on the other three tasks. As generation targets, the descriptors show that models struggle to produce strongly expressed and heterogeneous forms. CDBM complements existing indicators.

---


### 53. [FB-MOAC: A Reinforcement Learning Algorithm for Forward-Backward Markov Decision Processes](https://arxiv.org/abs/2611.00130)

**<font color=#1a73e8>作者：</font>** Mohsen Amidzadeh, Mario Di Francesco  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) algorithms are effective in solving problems that can be modeled as Markov decision processes (MDPs).
These algorithms primarily target forward MDPs whose dynamics evolve over time from an initial state.
However, several important problems in different scenarios including stochastic control and network systems exhibit both a forward and a backward dynamics. As a consequence, they cannot be expressed as a standard MDP, thereby calling
for a novel theory for RL in this context.
Accordingly, this work introduces the concept of Forward-Backward Markov Decision Processes (FB-MDPs)
for multi-objective problems,
develops a novel theoretical framework to characterize their optimal solutions,
and proposes a general forward-backward step-wise template
that allows to adapt RL algorithms for FB-MDP problems.
A Forward Backward Multi Objective Actor Critic (FB-MOAC) algorithm is introduced accordingly
to obtain optimal policies with guaranteed convergence and a competitive rate with respect to standard approaches in RL.
FB-MOAC is evaluated on diverse use cases in the context of mathematical finance and mobile resource management.
The obtained results show that FB-MOAC outperforms the state of the art across different metrics,
highlighting its ability to learn and maximize rewards.

---


### 54. [A Generalized Sparse Fuzzy Clustering Framework with Automated Cluster Cardinality Estimation Ability](https://arxiv.org/abs/2611.00159)

**<font color=#1a73e8>作者：</font>** George Stamatelis, Konstantinos Koutroumbas  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fuzzy clustering provides a robust framework for handling ambiguous and overlapping data boundaries, yet its traditional formulation generates entirely dense membership assignments that limit noise resilience and prevent estimating the true number of clusters, when it is unknown. To address these limitations, we introduce in this paper the Generalized Sparse Fuzzy Clustering (GSFC) framework, which incorporates a continuous sparsity penalty into the fuzzy objective function. Because closed-form solutions are precluded by the simultaneous presence of fuzzifier and sparsity exponents, we propose an efficient primal-dual bisection search coupled with specialized analytic pathways to rigorously enforce the partition constraint while organically driving trace memberships to exact zero. This mathematically enforced sparsity empowers the algorithm to autonomously estimate the true number of clusters by dynamically pruning redundant clusters, provided that it is initialized by a larger than the true number of clusters. Furthermore, we integrate a virtual noise sink to insulate outliers from the rest of the data points. The usage of the proposed framework is also extended to line segment detection. Extensive empirical evaluations across synthetic toy datasets, high-noise geometric stress tests, and real-world benchmarks (UCI wine dataset and hyperspectral images) demonstrate that GSFC effectively exceeds conventional fuzzy benchmarks while autonomously resolving cluster cardinality. Additionally, it significantly outperforms existing sparse possibilistic and probabilistic soft-clustering alternatives in line detection tasks.

---


### 55. [Learning to bid and bundle: a posterior-sampling agent for online retail](https://arxiv.org/abs/2611.00165)

**<font color=#1a73e8>作者：</font>** Hadi Mohammadi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An online retailer launching a perishable product bids for sponsored-search clicks, discounts a bundle with an always-stocked staple and displays its remaining stock, which raises willingness to pay. It knows neither how clicks respond to its bid nor how strong and dispersed its market is, and learns both over repeated seasons from data its own decisions censor: a zero bid reveals nothing about paid clicks, and choices follow only clicks. We design a posterior-sampling agent for it. Each period it draws a market from an exact posterior and posts the bid and discount of that market's exactly solved season plan, so every action is one a fully informed seller could take. In a simulated online florist it has the lowest regret averaged over markets. In weak markets it gives up 12% to 23% of one season's revenue over 500 seasons, four to seven times less than drawing once per season. A planner acting on point estimates can stop bidding and never learn that bidding pays. The agent escapes after about three seasons on average, against fifty with one draw per season. Where displayed scarcity keeps willingness to pay above the posted price, the discount needs no learning. Customers waiting for the discount to return to its recent level look like lost sales, so frequent waiting makes the agent underrate its market. One discount per season removes waiting at a cost of 5.9% of clairvoyant revenue in a weak market and none in a strong one.

---


### 56. [From Fragmentation to Fusion: A Survey and Roadmap for Omnimodal Embeddings](https://arxiv.org/abs/2611.00172)

**<font color=#1a73e8>作者：</font>** Ziyin Zhang, Yuyu Guo, Ying Zhang 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Embedding models underpin virtually every modern AI system, from search engines to recommendation systems. Despite shared mathematical foundations, research on embedding models remains fragmented by modality: the communities develop largely in isolation, seldom exchanging insights. We argue that this fragmentation obscures a deeper convergence. Driven by contrastive learning, Transformer architectures, and a granularity shift, embedding research across modalities is converging toward a common set of principles, even as modality-specific challenges remain underexplored. To reason across this convergence without conflating it, we propose a framework of three progressively harder capabilities: coverage, comparability, and compositionality. Three paths toward unification satisfy these in turn: transformation broadens coverage, alignment enables comparability, and joint embedding, the terminus we advocate, aims at compositionality. This position paper traces the resulting evolution, providing the first unified, cross-cutting treatment of omnimodal embedding research.

---


### 57. [Interpretable structural temperature scaling for calibrating graph neural networks and point-cloud segmentation](https://arxiv.org/abs/2611.00175)

**<font color=#1a73e8>作者：</font>** Chenyi Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph-aware calibrators make graph neural networks (GNNs) more trustworthy by predicting a temperature for each node, usually with auxiliary networks whose decisions are hard to inspect. We propose Interpretable Structural Temperature Scaling (ISTS), a twelve-parameter linear model that sets each node's temperature from named descriptors of its confidence, neighbourhood and closeness to labelled nodes, so every temperature traces back to descriptor contributions. ISTS preserves predictions, and cross-validated regularisation lets the calibration data decide how far the model departs from temperature scaling (TS). Its explanations are faithful at the level of node groups: on test nodes, ISTS softens groups that a global temperature leaves over-confident and sharpens under-confident ones (Spearman correlation 0.67 over 246 groups). On seven graphs with two backbones and eleven baselines, ISTS has the best average rank in negative log-likelihood (NLL) and Brier score and lowers NLL relative to TS by 1.8%, more than twice the gain of an identically fitted entropy-based temperature. It ranked first again on four held-out graphs under a protocol fixed in advance. From about 100 calibration nodes on, ISTS is a cheap and inspectable choice, and on point-cloud segmentation it significantly improves NLL, Brier score and the ranking of points for rejection.

---


### 58. [AuroraWorld: Structured 4D World Modeling for Exo-to-Ego Video Generation in Robot Manipulation](https://arxiv.org/abs/2611.00177)

**<font color=#1a73e8>作者：</font>** Hao Xue, Peng-Fei Zhang, Ying Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Egocentric observations provide a robot-centric view of manipulation processes, capturing contact interactions and object-state changes that are important for visuomotor policy learning but difficult to observe from external cameras. However, collecting such data at scale remains expensive due to additional hardware requirements and platform-specific deployment costs. Synthesizing egocentric observations from large-scale exocentric manipulation videos provides a scalable alternative. However, existing methods struggle to synthesize physically consistent and policy-relevant egocentric videos under substantial viewpoint transformations, severe occlusions, complex object interactions, and inherently sparse observations from available exocentric viewpoints.

---


### 59. [How to Simplify a Line Chart: A Taxonomy and Feature-Based Evaluation](https://arxiv.org/abs/2611.00179)

**<font color=#1a73e8>作者：</font>** Rifat Ara Proma, Paul Rosen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Simplifying large or noisy time-series is often a prerequisite for producing interpretable line charts, yet existing methods vary widely in how they alter visual features such as trends, extrema, periodicity, curvature, roughness, and overall complexity. We introduce a feature-based taxonomy of line chart simplification that evaluates 19 commonly used algorithms across three families: Transformers, Reducers, and Aggregators. We also formalize 12 perceptually motivated, computationally defined visual features commonly used when analyzing time-series in line charts. We assess preservation using multiple similarity metrics per feature to capture different aspects of fidelity, yielding 21 distinct feature-preservation measurements. To capture the trade-off between fidelity and simplicity, we introduce a Feature--Complexity (FC) score that combines feature preservation with complexity. Our systematic evaluation on 80 datasets reveals distinct family-level patterns: Transformers such as Gaussian, Mean, and Median filters achieve A-mode grades on nearly all metrics but retain full temporal resolution; Reducers such as Douglas-Peucker and M4 receive predominantly D-F mode grades trading fidelity for a reduction in the number of rendered points; and Aggregators ASAP and PAA occupy a middle ground with primarily B-C mode grades. We further characterize the predictability of algorithm behavior across datasets: some methods produce consistent grades regardless of dataset type (Gaussian, Mean, Douglas-Peucker), while others exhibit high data-dependency, with performance varying substantially based on dataset characteristics (FPCS, ASAP). An interactive website supporting exploration of all evaluated techniques, datasets, and results is available at this https URL.

---


### 60. [From Cross-Section to Cross-Omics: Conditional Cell Nucleus Image Editing in Spatial Transcriptomics](https://arxiv.org/abs/2611.00226)

**<font color=#1a73e8>作者：</font>** Yuechen Yang, Junchao Zhu, Junlin Guo 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics (ST) platforms simultaneously measure gene expression and capture cell nucleus images at single-cell resolution. A fundamental property of tissue preparation introduces a confounding relationship between the two measurement modalities: sectioning a three-dimensional tissue into a thin slice produces a two-dimensional cross-section whose area depends on the cutting angle. Larger cross-sections expose more cytoplasm, yielding higher mRNA counts, while pathomics features such as nuclear area are measured directly from the same 2D boundary. This sectioning geometry creates an apparent correlation between gene expression and pathomics that reflects the measurement process rather than independent biology. Existing gene-to-image methods generate cell images from gene features but do not support condition-driven editing of existing images across both omics layers. We apply the Manifold-Aware Diffusion (MAD) framework to this dual-omics editing setting, enabling targeted modification of one feature group while preserving the other. Evaluated on podocyte cells from CosMx SMI kidney tissue, MAD achieves MAE=0.6636 and FID=25.19 for pathomics editing, outperforming all compared baselines. A controlled simulation study further confirms that the VAE component in MAD better preserves cross-group independence than CCDM (MAD without VAE).

---


### 61. [IsoAlign: Isoform-Aware DNA-Protein Alignment via Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2611.00241)

**<font color=#1a73e8>作者：</font>** Niousha Sadjadi, Arman Seyed-Ahmadi, Tony Tu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Genomic foundation models (GFMs) have emerged as a powerful paradigm for learning DNA sequence representations, yet existing self-supervised pretraining strategies overlook alternative splicing and underperform compared to specialized models. To address this gap, we introduce IsoAlign, a multimodal framework that grounds genomic pretraining in isoform-aware DNA-protein alignment to learn biologically meaningful representations. IsoAlign aligns transcripts to their corresponding protein isoforms, capturing both coding sequences and broader regulatory contexts, using two Joint-Embedding Predictive Architectures (JEPA): DNA-Protein JEPA (DP-JEPA), which predicts protein representations from DNA using contrastive alignment, and Isoform-Masked JEPA (IM-JEPA), which models relationships among alternative isoforms of the same gene through masked protein prediction. We evaluate the learned DNA representations of these architectures across a multi-metric evaluation suite spanning tasks, including the prediction of pathogenicity, fitness, gene expression, and TF binding. Our results demonstrate that isoform-aware cross-modal alignment using JEPA significantly improves functional representations and downstream performance, establishing a promising direction for GFM pretraining.

---


### 62. [SketchBloom: Training-Free Vector Sketch Outpainting with Stroke-Level Style Control](https://arxiv.org/abs/2611.00245)

**<font color=#1a73e8>作者：</font>** Quang-Thinh Nguyen, Duy-Khang Do, Tam V. Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Outpainting sparse sketches while preserving contour coherence and stroke style remains challenging. We present SketchBloom, a training-free framework that combines pretrained raster outpainting and style-transfer guidance with per-instance vector optimization. Given a sketch, a scene prompt, and an optional reference style, it produces an editable Scalable Vector Graphic (SVG) composed of Bezier strokes. Adaptive latent blending balances content contours and reference texture without model retraining. A reference-derived stroke vocabulary initializes contour- and DINO-attention-guided strokes, which are optimized separately for structure and texture before contour-emphasizing multiply fusion. As in prior optimization-based vector sketching, no task-specific network is trained; our contribution is the synthesis design specialized to sketch outpainting. On LineArtOut-1K, comprising 1,024 input and style combinations, SketchBloom improves perceptual, semantic, and structural fidelity over the evaluated vector baselines when all methods vectorize the same outpainted raster. This protocol evaluates vector synthesis rather than end-to-end outpainting or reference-style superiority. Runtime is approximately six minutes per pair on a single NVIDIA H200 GPU. Project page: this https URL

---


### 63. [SketchForge: Training-Free Scene-to-Vector Sketching via Decoupled Structure and Texture Optimization](https://arxiv.org/abs/2611.00253)

**<font color=#1a73e8>作者：</font>** Quang-Thinh Nguyen, Duy-Khang Do, Hien Trinh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Converting a raster image into a resolution-independent, stroke-editable vector sketch while faithfully preserving both structural contours and tonal texture remains challenging: raster-space rendering pipelines are difficult to edit at the stroke level, while generation-from-scratch vectorization methods struggle to remain faithful to an arbitrary input image. We present SketchForge, a training-free framework that converts an input raster image into a resolution-independent SVG sketch through per-instance test-time optimization of Bezier curves, requiring no additional training or fine-tuning. Strokes are seeded via a contour and attention-guided initialization, then refined by a vector-native differentiable rendering pipeline that decouples structural contour strokes from free-form texture strokes under dedicated objectives, composited via multiply-blend layering. Extensive experiments show that SketchForge consistently outperforms existing vector-based baselines in structural fidelity and generation quality. Project page: this https URL

---


### 64. [KINDER: Kernel-based Independence for Fair Representation Learning via Prototype-space Erasure](https://arxiv.org/abs/2611.00264)

**<font color=#1a73e8>作者：</font>** Abtin Mogharabin, Alp Toykan Kaplan, Jiaee Cheong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concept erasure is a prominent approach to achieving fairness in machine learning through the removal of sensitive attributes from learned representations. Prior concept erasure methods typically define debiasing indirectly through the failure of a chosen adversary, probe, or fairness penalty, which makes the target of erasure dependent on a particular decoder family or optimization setup. We introduce KINDER, which directly removes sensitive-attribute information from intermediate representations with respect to a chosen family of prototype functionals, and is compatible with any deep model containing an intermediate feature space, independent of the architecture, task type, or training paradigm. KINDER operates in a random Fourier feature space, where it estimates a sensitive subspace from protected group prototypes and projects representations onto its orthogonal complement. Thus, it forms an explicit representation cleaning mechanism distinct from prior fairness control studies. We conduct extensive experiments across diverse settings and show the effectiveness of KINDER on (i) supervised and self-supervised settings, (ii) classification, regression, and image segmentation tasks, and (iii) diverse data modalities, including visual, textual, and tabular data. Code and trained models are available at: this https URL

---


### 65. [Automated Theorem Generation in First-Order Logic by Construction from Triangular Standard Contradictions](https://arxiv.org/abs/2611.00269)

**<font color=#1a73e8>作者：</font>** Yang Xu, Shuwei Chen, Hailin Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated theorem generation (ATG) seeks to construct new theorems rather than merely prove given conjectures. Existing approaches typically generate candidate statements that require subsequent proof or formal verification. We propose a constructive framework for ATG in first-order logic based on triangular standard contradictions. The method constructs minimally unsatisfiable clause sets from selected first-order literals, then forms theorems by retaining some clauses as premises and taking the negation of one clause, or a conjunction of clauses, as the conclusion. Minimal unsatisfiability ensures that the remaining premises are satisfiable, avoiding trivial inference by explosion, while unsatisfiability of the full set guarantees the resulting entailment. Theorems are therefore correct by construction, without a separate proof procedure for each instance. Extending the previously developed $\Delta_1$ generator, we introduce seven methods, $\Delta_2$--$\Delta_8$, forming a unified family of eight theorem-generation methods. Four generators, $\Delta_1$--$\Delta_4$, have been implemented and released. We also formulate a general $\Delta$-class method encompassing the family. Combinatorial analysis demonstrates the capacity to generate large numbers of distinct theorems systematically. This framework offers a principled foundation for automated theorem discovery and the construction of logically guaranteed knowledge.

---


### 66. [OCELOT: Planetary-Scale Species Distribution Modeling with Satellite Foundation Embeddings](https://arxiv.org/abs/2611.00284)

**<font color=#1a73e8>作者：</font>** Bart van Merriënboer, Lauren Harrell, Keith Anderson 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale repositories of species observations now contain billions of occurrence records from around the world, but these sightings cluster heavily in human-accessible areas. Existing models use only a small fraction of these records and are not evaluated on extrapolating to remote, unvisited regions--where species distribution models can be used as geographic priors to help classify data from camera traps and acoustic recorders. We scale relative occurrence species distribution models by training a multimodal implicit neural representation network called OCELOT that fuses spatial coordinates with satellite foundation embeddings on two orders of magnitude more observations than previous work: 2 billion GBIF records across 100,000 taxa. Scaling to this regime requires co-designing the data pipeline, taxonomic representation, loss formulation, and model architecture: spatiotemporal thinning and sub-linear cell sampling correct for spatial redundancy and observer bias, while an additive taxonomic readout shares representations across species, genera, and families to improve predictions for rare taxa. To evaluate performance in remote areas, we benchmark geographic extrapolation using the NDCG metric on spatial block holdouts up to 600 km. Satellite foundation embeddings improve extrapolation by 51% over coordinate-only models and outperform classical bioclimatic rasters. The resulting model also matches or outperforms existing baselines on established interpolation benchmarks, demonstrating that optimizing for geographic extrapolation does not compromise in-distribution accuracy.

---


### 67. [Seeing Less in a Sparse World: Cross-View Geolocalization from Limited Field-of-View Observations](https://arxiv.org/abs/2611.00288)

**<font color=#1a73e8>作者：</font>** Fahimul Aleem, Shruti Vyas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view geolocalization aims to determine the geographic location of a ground-level image by retrieving its corresponding satellite image, offering a promising alternative for localization in Global Navigation Satellite System (GNSS)-denied or degraded environments such as urban canyons, dense forests, and disaster scenarios. Despite recent progress, existing approaches remain limited by the lack of globally diverse training datasets and benchmarks that are often geographically restricted. Furthermore, most benchmarks rely on panoramic ground views, which do not reflect the limited field-of-view imagery captured by real world cameras.
To address these challenges, we introduce Cross-View World 500k (CVW500k), a large-scale globally distributed dataset containing over 500,000 ground-satellite image pairs collected across diverse geographic regions and environments. Unlike previous datasets, CVW500k uses limited field-of-view ground images, providing a more realistic and challenging setting for cross-view geolocalization. In addition, we propose GeoQueryNet, a query-based cross-view fusion transformer framework designed to bridge the viewpoint gap between ground and satellite images. The model leverages a CLIP-based visual encoder with parameter-efficient LoRA adaptation and introduces a Cross-View Alignment Module that uses learnable query tokens to extract geographically consistent features across viewpoints. Our code can be found here: this https URL .

---


### 68. [When AI Agents Act on Our Behalf: A Taxonomy of Human-Agent Interaction Failure](https://arxiv.org/abs/2611.00291)

**<font color=#1a73e8>作者：</font>** Canwen Wang, Qing Xiao, Haiyi Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI agents write and execute code, manipulate user interfaces, and transact on their users' behalf. We ask what forms failure takes in human-agent interaction, and how those forms change as agents act with greater autonomy. From 695 documented incidents in two public repositories, we developed 12 failure modes bottom-up within three interaction stages adapted from Amershi et al.'s guidelines, coding the autonomy at which each arose. What a person can do when an agent fails depends on how much the agent completes between points of user involvement--a property fixed at deployment. Therefore, the same model on the same task can fail differently under different configurations. All 12 modes appear at both low and high autonomy, and rising autonomy changes the form each failure takes. Users need controls between full delegation and full manual work, and neither incident records nor agent benchmarks reach the interaction where these failures occur.

---


### 69. [Seeing the Unseen: Unified Visible--Invisible Motion for Physically Consistent Video Generation](https://arxiv.org/abs/2611.00293)

**<font color=#1a73e8>作者：</font>** Mingyang Bao, Fangda Ye, Xihao Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video generation have achieved impressive visual quality, yet they often fail to produce physically consistent dynamics due to the lack of explicit modeling of underlying physical processes. Existing approaches either rely on simulators with strong assumptions or use coarse semantic guidance, and further struggle to effectively inject physical priors into generation models. In this work, we propose Seeing the Unseen, a unified framework for physics-grounded video generation. Our approach decomposes the problem into two stages: learning physical dynamics and injecting them into video synthesis. First, we introduce a lightweight Particle-based Graph Dynamics Simulator (PGDS) that learns generalizable physical interactions from data and predicts plausible 3D motion trajectories. Second, we propose a Visible--Invisible Motion Field (VIMF) that captures both motion observable in the input frame and motion that emerges over time due to object dynamics. This representation enables more complete and structured motion guidance compared to conventional physical signals. By integrating these trajectories into a diffusion-based generator, our method produces videos that are both visually coherent and physically consistent. Extensive experiments demonstrate improved motion accuracy, interaction consistency, and reduced physical artifacts compared to strong baselines.

---


### 70. [A Framework for Task-Agnostic Counterfactual Fairness in Transformers through Activation Steering](https://arxiv.org/abs/2611.00298)

**<font color=#1a73e8>作者：</font>** Joshua Wolff Anderson, Yanshan Wang, Shyam Visweswaran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bias in transformer-based models is a growing concern as these architectures become more prevalent in automated decision-making systems, such as prediction models for hiring, lending, and clinical treatment recommendation. Mechanistic interpretability (MI) is a growing body of work that measures meaningful causal effects of activations on model output by identifying human-interpretable features encoded in model activations. When such features correspond to sensitive attributes, they provide a direct way to quantify the bias those attributes introduce and to causally intervene to mitigate it. However, counterfactual fairness (CF) methods have not been systematically adapted to this setting of intervening on interpretable mechanisms in transformers. We propose a framework, Mechanistic Interpretability for Counterfactual Fairness (MICF), that utilizes MI tools to reformulate CF constraints in terms of transformer activations, unifying former approaches into a single pipeline for fairness analysis in transformers. MICF does not require a prior causal model or specific transformer architecture. We evaluate MICF on real-world tabular data and show that CF can be improved across different prediction tasks.

---


### 71. [RaMMOBO: Random Max-Margin Multi-Objective Bayesian Optimization](https://arxiv.org/abs/2611.00312)

**<font color=#1a73e8>作者：</font>** Thomas Wedenig, Paul Plantosar, Robert Peharz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-objective Bayesian optimization (MOBO) maximizes $M$ expensive black-box objectives with the goal of approximating the Pareto set, whose objective vectors cannot be improved in one component without sacrificing another. A common quality measure is hypervolume, the volume in objective space dominated by these vectors relative to a reference point. Expected hypervolume improvement (EHVI) directly targets this metric and is one-step Bayes-optimal, but its standard computation scales exponentially with $M$, making it prohibitively expensive for many-objective problems. We introduce random max-margin multi-objective Bayesian optimization (RaMMOBO), whose acquisition function lower-bounds EHVI while requiring only linear cost in $M$ to evaluate. RaMMOBO measures the volume of a max-margin box contained in a candidate's hypervolume-improvement region and averages over random reweightings of the objective space, yielding a utility that is strictly Pareto-monotone on hypervolume-improving outcomes. It naturally handles noisy observations and different probabilistic surrogates and supports efficient gradient-based optimization. Across synthetic and real-world benchmarks, RaMMOBO matches or outperforms state-of-the-art methods, with largest gains at higher $M$, with acquisition optimization up to two orders of magnitude faster than qLogNEHVI. Our implementation is available at this https URL.

---


### 72. [Cyber-physical attack detection approaches in the wide-area measurement system](https://arxiv.org/abs/2611.00316)

**<font color=#1a73e8>作者：</font>** Zakaria El Mrabet, Prakash Ranganathan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Improving situational awareness within the Smart Grid is an effective preventive measure to detect potential anomalies, and avoid their adverse consequences. A wide area measurement system (WAMS) based Phasor Measurement Unit (PMU) can assist in improving visibility within the grid by collecting relevant measurements including magnitude, phase angle, frequency, voltage, and current, with a precise GPS-based timestamp. So far, there are more than 2500 PMUs deployed in the North American power grid, where each of which generates between 30 and 60 samples/s, roughly 1.5 TB/month of streamed data. Thus, processing such large PMU streams requires expensive computational resources and faster algorithms. This paper provides state-of-the-art cyber and physical anomalies in the WAMS and analyses their impact on the integrity and availability of the system. Next, it investigates the current anomaly detection approach in historical and streaming PMU data, including conventional machine learning and hybrid approaches, and assesses their advantages and main drawbacks. Lastly, it sheds light on the importance of handling missing PMU data and concept drifts.

---


### 73. [Déjà Vu: Cycle-Consistent Re-ranking for Semantic Correspondence](https://arxiv.org/abs/2611.00328)

**<font color=#1a73e8>作者：</font>** Xiaoran Zhang, Huidong Liu, Yang Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose \emph{Déjà Vu}, a test-time decoding module for semantic correspondence. Matching semantically equivalent keypoints across images of the same object category is challenging due to variations in appearance, viewpoint, and scale. While features from large pretrained vision models carry strong zero-shot correspondence ability, existing methods reduce final matching to greedy top-$1$ nearest-neighbor selection. We show that the correct correspondence appears among the top-ranked candidates far more often than top-$1$ matching achieves: with $30$ candidates, zero-shot features exceed the top-$1$ accuracy of a supervised model. This reveals a \textit{decoding bottleneck} rather than a limit of the representation. Motivated by this observation, we formulate semantic correspondence as a \textit{recall-then-rerank} problem. Our method first nominates an adaptive candidate set, larger when the similarity distribution is ambiguous and smaller when it is confident, then re-ranks the candidates with a graded cycle-consistency score: each candidate is matched back to the source image and penalized by how far its reverse match lands from the original keypoint. The module operates entirely on the similarity matrix already computed by the base method. It consistently improves three representative baselines on SPair-71k, its geometric subset, and PF-Pascal under both unsupervised and weakly supervised settings, with gains of up to $+1.8$ PCK@0.10 on SPair-71k and $+3.4$ PCK@0.15 on PF-Pascal, and $+4.9$ under Keypoint Average Precision.

---


### 74. [Efficient NPN Classification for Large Functions using Graph Neural Network](https://arxiv.org/abs/2611.00339)

**<font color=#1a73e8>作者：</font>** Chengdi Cao, Hanyu Wang, Wan-Hsuan Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Two Boolean functions are considered NPN equivalent if one can be transformed into the other by negating inputs, permuting inputs, or negating the output. Efficient NPN classification is valuable in fields such as logic synthesis, quantum computing, and information theory. However, exact NPN classification demands exhaustive enumeration of all possible input permutations and negations. Its complexity grows exponentially, making it impractical for larger functions with more inputs. In this paper, we introduce the first learning-based formulation for NPN classification by recasting it as NPN action prediction. Our method represents Boolean functions as AND-Inverter Graphs (AIGs) and applies a bidirectional heterogeneous graph neural network to predict input negations, output negation, and input permutations. To mitigate the non-canonicity of logic networks, we further introduce graph rewriting techniques that reduce structural ambiguity and recover useful symmetries before prediction. Experimental results show that NPN action prediction is learnable, that the resulting canonicalization quality improves over heuristic baselines, and that on practical benchmarks our method approaches exact methods on tractable cases while scaling to functions with up to 16 inputs.

---


### 75. [DEPLOY-RL: Active Boundary Discovery and Conservative Certification for Deployable Reinforcement Learning in Safety-Critical Continuous Processes](https://arxiv.org/abs/2611.00342)

**<font color=#1a73e8>作者：</font>** Yeojin Jang, Minu Baek, Gihun Gil 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) policies often outperform classical controllers in simulation, yet rarely reach production in safety-critical processes. The barrier is that there is no principled way to answer "Is this policy safe to deploy?" with statistical guarantees. We introduce DEPLOY-RL, a post-training certification framework built on one key insight: deployment certification requires discovering where failures occur (boundary discovery), not measuring how much everywhere (uniform reconstruction). Our contributions: (1) a contract-coupled acquisition function that concentrates sampling on certification-critical boundaries, achieving approximately 2x sample efficiency with a semi-empirical ambiguity reduction bound (domain-calibrated convergence guarantee); (2) conformal risk control providing finite-sample false-go guarantees (<= alpha) under explicit deployment contracts; (3) a three-way decision framework (Deploy/No-Deploy/Abstain) with fail-safe PID/MPC fallback. In simulations on papermaking (industrial digital twin) and Tennessee Eastman (public benchmark), DEPLOY-RL achieves 4.4% false-go rate (vs. 8.6% for the best baseline) while retaining 88.6% policy coverage, the only method achieving <5% false-go with >85% coverage among 14 baselines under our evaluation protocol.

---


### 76. [Queering the Audits: Community-Based Auditing of AI Harms to Queer Communities](https://arxiv.org/abs/2611.00345)

**<font color=#1a73e8>作者：</font>** Organizers of QueerInAI, A Pranav, Alissa A. Valentine 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI systems embed majority-group defaults into training data, evaluation metrics, and category definitions, producing documented harms for queer communities including erasure, misclassification, and discrimination. Standard technical audits often rely on aggregate measures and cannot detect harms that be come visible only through the lived experience of affected communities. We conducted a participatory auditing workshop at EurIPS 2025 where 16 queer community members audited four case studies using the 4Cs harm taxonomy (Content, Conduct, Contact, Contract) applied across the AI lifecycle. Participants used structured worksheets and plenary synthesis to classify harms and trace them to their origins in the development pipeline. Across all four cases, participants traced harms to problem definition and data collection, and they identified contractual structures that extract value from vulnerable populations while providing minimal recourse. These findings illustrate that community-informed auditing surfaces concrete, identity-specific harms that aggregate evaluation methods risk overlooking.

---


### 77. [On the Limits of Test-Time Compute for Self-Evaluation](https://arxiv.org/abs/2611.00350)

**<font color=#1a73e8>作者：</font>** Anirudh Buvanesh, Khaled Rouissi, Sujin Yun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-verification and aggregation have emerged as popular approaches for bridging the gap between pass@1 and pass@N. However, increasing the number of candidates does not consistently narrow the gap between final-answer accuracy and pass@N. To understand this limitation, we use ranking error to measure how reliably models distinguish their correct generations from incorrect ones. We show that ranking error admits a bias-variance decomposition, with both components shaped by algorithmic design choices and inference compute. Across our experiments, additional compute reduces variance, while bias initially decreases before approaching a plateau. Guided by this analysis, we introduce Scorpio, a simple and general method that jointly scores randomly grouped candidates. Across math, code, and puzzle benchmarks, Scorpio improves verification, tree search, and aggregation. For verification, Scorpio improves accuracy over the strongest baseline by up to 7 percentage points while matching or exceeding that baseline's peak accuracy with 17-42% lower inference cost. For tree search, using Scorpio to score partial solutions and select the final answer improves accuracy by up to 10 percentage points over prior methods. Finally, Scorpio improves the scaling of aggregation-based methods by 11 percentage points on coding tasks.

---


### 78. [Unpacking the process of watching a 360-degree video: How physiological responses and head rotation relate to affective and cognitive outcomes](https://arxiv.org/abs/2611.00356)

**<font color=#1a73e8>作者：</font>** Portia Wang, Yujie Tao, Monique Santoso 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> A defining feature of 360-degree video is that the perceptual experience is actively constructed. As viewers turn their heads, shift their gaze, and encounter changing visuals, their perceptual experience is not predetermined, but rather emerges through ongoing exploration. Yet, it is unclear how the process of watching immersive videos unfolds, and how it is related to psychological and physiological outcomes. We present a large-scale study (N=200) in which participants experienced one of 10 pieces of 360-degree videos in virtual reality. Results showed that greater head rotation was associated with greater valence, higher attention focus, longer length of subjective review, and lower simulator sickness; greater pupil dilation was associated with lower valence, lower review ratings, and greater use of negative tone in written reviews. A mediation analysis revealed that participants who rotated their heads more experienced greater frame-to-frame pixel-level perceptual changes in their field of view, which in turn resulted in greater valence and lower simulator sickness. Moreover, participants tended to rotate their heads toward field of view regions with greater perceptual movement, while directing their eye gaze toward less perceptually dynamic areas within that view. We outline theoretical and practical contributions for designing 360-degree content and predicting experiential outcomes.

---


### 79. [Humanized but Still True? Auditing Facts and Detection in AI-Text Humanizers](https://arxiv.org/abs/2611.00359)

**<font color=#1a73e8>作者：</font>** Ziyuan Wang, Genliang Zhu, Xiaobo Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI "humanizers" rewrite machine-generated text so that detectors classify it as human-written. Public leaderboards score evasion and embedding similarity, but not whether checkable details survive. We check whether numbers, dates, person and organization names, and quoted spans survive each rewrite, using a rule-based checker validated by two AI annotators (precision 0.84-1.00, recall 0.93-0.95; no human annotation). In the October 2026 cycle of a public humanizer leaderboard, all 11 commercial tools changed or dropped at least one of these units in 35-65% of the documents that contained one. Most changes were to quoted spans; counting numbers and names alone, 10 of the 11 tools still altered at least one in 20% or more of the documents. The September 2026 cycle was similar (19-50%). An open 12B humanizer kept at least 97% of numbers and names in fact-dense U.S. federal agency text, but reworded 67-78% of the quoted spans, against its own prompt. Unit retention and detector evasion were not clearly related across tools (Spearman rho = -0.46, 95% CI -0.65 to 0.08), and the open model's four released files (two of them quantization-aware low-bit files) did not show the pre-registered monotone trade-off. On federal texts with matched human, AI-styled and humanized versions, a general-purpose decision model, Jev, asked a single zero-shot question, separated human originals from humanized rewrites with AUROC 0.864 (0.827-0.902), 0.18-0.22 higher than Binoculars, Fast-DetectGPT and the adversarially trained RADAR, while calling 24% of the human originals AI at a 0.5 threshold. On the AI-styled rewrites by 2026 models, both perplexity-based detectors scored below chance (AUROC 0.37 and 0.39), also with line breaks removed. Hypotheses, data rules and analyses were frozen before the main runs; two earlier data contacts are disclosed. We release the checker and the per-item results.

---


### 80. [When appearance and motion disagree: evaluating class--motion consistency against disguised uncrewed surface vessels](https://arxiv.org/abs/2611.00367)

**<font color=#1a73e8>作者：</font>** Jon Reifschneider  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Defense systems for maritime assets must distinguish approaching benign craft from uncrewed surface vessels (USVs) with sufficient warning to act. Shore cameras using computer vision can separate hostile vessels from benign traffic, but these systems may be attacked using an adversarial hull patch or physical disguise. We evaluate adversarial hull patches and find they suppress detection in up to 29% of attempts but never cause misclassification as benign. Physical disguise, however, can bypass both a camera check and a radar presence check. To evaluate defenses, we develop a hybrid replay protocol from automatic identification system (AIS) tracks that combines recorded benign motion with direct or off-axis attack run-ins. We find that for recreational-labeled vessels attacking via direct run-in within 4 nautical miles, an asset-relative closing-rate check flags 94-95% at 15-20 knots, compared with 12% for a track-only speed check. The checks are complementary on off-axis approaches, constraining the attacker to remain below both thresholds and extending the time required to reach the asset. Flagging on either check has a 4.9% held-out false-alarm rate overall and 12.3% on recreational traffic. The replay-based evaluation protocol supports comparative test and evaluation of defense methods.

---


### 81. [MoRE-GS: Motion-Regime Experts for Future Gaussian Splatting](https://arxiv.org/abs/2611.00375)

**<font color=#1a73e8>作者：</font>** Shima Salehi, Joshua Peeples  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Future dynamic novel-view synthesis requires extrapolating multiple motion regimes within the same scene. A single dynamics model may not simultaneously represent stationary regions, coordinated motion, local interactions, and articulated trajectories. We introduce Motion Regime Expert Routing for Gaussian Splatting (MoRE-GS), a causal, render-aware framework for forecasting dynamic 3D Gaussian scenes. MoRE-GS freezes a Gaussian representation reconstructed exclusively from the observed temporal prefix and forecasts its control-keypoint motion using four complementary experts: persistence, a coefficient-space Transformer, a graph convolutional network, and a structured Transformer with rigid and non-rigid motion constraints. A compact routing table assigns expert mixtures across soft motion groups and forecast-horizon bins, while a persistence gate suppresses unreliable extrapolation. Across D-NeRF and HyperNeRF scenes, MoRE-GS achieves improved performance against other methods, and these results demonstrate that renderer-calibrated composition of complementary motion predictors improves causal dynamic Gaussian forecasting across heterogeneous motion regimes.
Project page: this https URL

---


### 82. [Evaluating SAM-based and Convolutional Architectures in Thin Retinal Vessel Segmentation: Model Capacity, Computational Cost and Foundation Pre-training](https://arxiv.org/abs/2611.00396)

**<font color=#1a73e8>作者：</font>** Carlos Eduardo Fontaneli, Cesar Henrique Comin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In retinal vessel segmentation, plain Vision Transformers (ViTs) are commonly expected to perform worse than convolutional neural networks (CNNs) on thin vessels, for reasons such as their coarse patch tokenization, their weak locality bias and their need for large training sets. Although this expectation is widely shared in the literature, how plain ViTs actually compare with CNNs on thin vessels has not been systematically quantified. We address this question by comparing a model with a plain ViT encoder (MedSAM), a hybrid Transformer (LiteMedSAM) and three CNNs of different sizes on three retinal datasets (DRIVE, HRF, FIVES) and, as a second-domain check, a microscopy dataset (VessMap). We measured the centerline recall and precision of thin vessels and compared the models while also considering their computational cost and how many epochs they needed to train. We found that the pre-trained MedSAM had a centerline recall of thin vessels that was not significantly different from that of the best CNN on all four datasets (-0.6 to +2.5 percentage points). A compact plain ViT obtained through architecture search but trained from scratch did not retain this performance. For pre-trained plain ViTs, our results do not support the expectation that they miss thin vessels, although similar thin-vessel performance can be obtained with much smaller models.

---


### 83. [TAP-Out: Tracking Any Point in 360° via Outpainting](https://arxiv.org/abs/2611.00406)

**<font color=#1a73e8>作者：</font>** Finlay G. C. Hudson, James A. D. Gardner, William A. P. Smith  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tracking points that leave the camera's field of view (FoV) requires reasoning about unobserved scene dynamics, a fundamentally different problem from tracking visible correspondences. We present TAP-Out, an offline method that makes this out-of-view (OOV) reasoning explicit by leveraging generative video outpainting as a world-model prior. Given a narrow-FoV input video, TAP-Out outpaints a complete 360° equirectangular video, locates target objects within the panoramic scene via video object segmentation, and synthesises object-centred perspective crops on which standard in-frame trackers operate. This decoupled design composes off-the-shelf foundation models without requiring task-specific architectural modifications. On the TAPVid360 benchmark, TAP-Out achieves state-of-the-art performance, improving OOV tracking accuracy by approximately 3x over the best prior method. We demonstrate its flexibility on out-of-frame object segmentation and detection and we provide detailed diagnostic analyses across motion regimes, static versus dynamic content, and hallucination quality, characterising when and why the approach succeeds or fails.

---


### 84. [Nonconformal Distortion and Local Orientation Reversal in the Fourier Circuit of a Modular-Addition Transformer](https://arxiv.org/abs/2611.00414)

**<font color=#1a73e8>作者：</font>** Eduardo Fuentes, Gonzalo Riera, Héctor Allende-Cid  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study the local differential geometry of a Fourier-based modular-addition circuit in a one-layer transformer whose algorithm has previously been reverse-engineered. For each of the five key Fourier frequencies, we restrict the model's multilayer perceptron (MLP) contribution to a corresponding Fourier input plane and readout, and measure its directional Beltrami coefficient under continuous input perturbations. Whereas nondegenerate restrictions of ideal complex multiplication are conformal, the trained maps exhibit nonconformal distortion (median $|\mu|=0.304$--$0.446$), spatial organization in the Beltrami argument, and regions of local orientation reversal. The median across frequencies decreases from $0.939$ at initialization to $0.390$ after training. The key-frequency planes also show lower median distortion than most random-plane controls, although their distributions overlap and the coordinate frames differ in conditioning. Across 500 checkpoints in one training run, most of the aggregate reduction in Beltrami magnitude occurs before the principal increase in the measured Fourier-circuit formation. At the individual-input level, Beltrami magnitude shows negligible association with the correct-logit margin ($|\rho|\leq0.026$). Late-checkpoint measurements across six runs show comparable distortion for most selected frequencies. These results provide a quantitative characterization of local deformation in a frequency-projected component of an identified neural circuit, complementary to its algorithmic reconstruction.

---


### 85. [A Spectral Renormalization-Group View of Learning](https://arxiv.org/abs/2611.00422)

**<font color=#1a73e8>作者：</font>** Charles H. Martin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study how the layers in deep neural networks (NNs) converge, using Wilsonian Renormalization-Group (RG) ideas to organize the spectral picture. During training, these layers often develop heavy-tailed power-law (PL) spectra, and the strongest checkpoints often appear near the PL exponent $\alpha\approx 2$. This pattern raises a simple question: why should this value mark a well-trained layer? The answer is both statistical and physical. Our statistical hypothesis is that $\alpha=2$ marks the boundary between stable if not optimal learning and overfitting via non-self-averaging. The physical answer is that the same value makes the spectral energy gain scale evenly across logarithmic spectral scales, which is the proposed Wilsonian marginal condition. We then apply the ERG trace-log condition, the proposed SETOL theory, which we justify by taking volume-preserving, scale-invariant transformations to remove arbitrary layer scale along the proposed RG flow. The resulting spectral RG flow connects the HTSR and SETOL theories to optimizers such as Muon, and motivates a new optimizer extension, WW-PGD. Together, these results point toward a spectral Renormalization-Group view of learning, in which NNs may approach shared spectral structure in the settings studied here.

---


### 86. [PAM-Mamba - Efficient Dense Action Detection using Mamba](https://arxiv.org/abs/2611.00423)

**<font color=#1a73e8>作者：</font>** Dhruvraj Singh Rawat, Faegheh Sardari, Armin Mustafa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense action detection requires precisely localising multiple overlapping actions in long untrimmed videos. Transformer-based methods achieve strong accuracy but their $O(T^2)$ self-attention cost limits scalability. We present PAM-Mamba, a linear-time $O(T)$ architecture built on Mamba with a multi-branch temporal encoder. Gated Learnable Positional Encoding (GLPE) controls positional signal injection via a scalar gate initialised to zero, starting training without added positional signal. A Hub-and-Spoke Funnel extends the non-hierarchical multi-scale design of PAT with a direct residual from the original full-resolution input to each coarse branch, providing each coarse branch with a projection of the input features. Bi-TemBa (Bidirectional Temporal Mamba) first extracts local motion cues with a shallow Temporal Convolution Module, then applies a cascaded bidirectional Mamba scan; the backward pass refines the forward-scanned representation from the opposite direction, giving each temporal position access to context from both directions in linear time. Uncertainty-Based Mixup uses prediction entropy to guide the selection of mixup partners. Using the PAT evaluation implementation, we obtain 26.82 (Charades I3D), 34.59 (Charades CLIP), 46.56 (MultiTHUMOS I3D), and 46.92 mAP (MultiTHUMOS CLIP), with 26.1-27.9M parameters, 61-63% fewer than PAT.

---


### 87. [Spoofing the Latent State: Imperceptible Goal-Image Attacks Derail Planning in LeWorldModel](https://arxiv.org/abs/2611.00427)

**<font color=#1a73e8>作者：</font>** Kunal Bhosikar, Nicole Meng, Charu Sharma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint-embedding predictive architectures (JEPAs) have recently emerged as general-purpose visual world models for control. A prominent example is LeWorldModel (LeWM), which trains end-to-end from pixels using an isotropic Gaussian anti-collapse regularizer (SIGReg) and plans by minimizing the squared Euclidean distance between predicted and goal embeddings. In this work, we investigate the test-time robustness of this latent planning interface. Analyzing the learned metric on Push-T, we first find that task-relevant object state heavily dominates latent distance: shifting the block by a single pixel displaces the embedding $3\times$ further than an equivalent agent shift, and swapping the block pose alone accounts for $99\%$ of the distance between scene pairs. However, because this pose information is distributed across a curved, high-dimensional manifold rather than a fixed linear subspace, the encoder cannot be trivially edited post-hoc to isolate or redirect it. We next demonstrate that this geometry is highly vulnerable at test time. A white-box $\ell_\infty$ perturbation of just $\epsilon{=}4/255$ applied to a single input frame causes the encoder to register the block at an arbitrary, attacker-chosen pose in $73$--$95\%$ of scenes without disturbing the encoded agent state. Perturbing either the goal image or the live camera observation drops Push-T planning success from $87\%$ to $32\%$, whereas uniform random noise at twice the magnitude has negligible impact. This vulnerability persists across all four standard LeWM benchmarks (Push-T, Two-Room, Reacher, and OGBench-Cube). At $\epsilon{=}8/255$, the attack bridges $82$--$97\%$ of the squared latent distance to the target embedding in every environment, inducing planning degradation proportional to each task's reliance on the spoofed entity.

---


### 88. [Real-VAS: a Real-World Video Amodal Segmentation Dataset](https://arxiv.org/abs/2611.00430)

**<font color=#1a73e8>作者：</font>** Finlay G. C. Hudson, William A. P. Smith  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Amodal video object segmentation is fundamentally limited by the absence of datasets that combine real-world complexity with precise ground-truth annotations. To address this, we present Real Video Amodal Segmentation (Real-VAS), a new large-scale, zero-shot evaluation dataset built from composited real-image video. We introduce a novel data generation pipeline that enables the creation of programmatically consistent amodal ground truth for real-world footage, in which the object mask, occlusion boundary, and composited image are all derived from a single unoccluded source, without relying on human estimation or expensive 3D reconstruction. Our dataset is structured into two challenging scenarios: dynamic Occlusion, created by compositing two clips of moving objects, and a unique Container category featuring complex, physically constrained interactions. These container scenarios--On Surface Containment, Articulated Containment, and Mobile Containment--allow us to generate precise ground truth by simulating an object's motion based on its container's tracked transformation. As a result, Real-VAS provides a diverse and challenging benchmark for evaluating amodal segmentation models on realistic video with the precision of synthetic data. The dataset and our generation code will be made publicly available.

---


### 89. [Local Spatial TreeSHAP: Geographically Explainable AI Revealing Urbanization-Dependent Spatial Heterogeneity in Flood Resilience](https://arxiv.org/abs/2611.00433)

**<font color=#1a73e8>作者：</font>** Zeyu Zhao, Xiaoshan Zhou, Fanxin Meng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Urban flood resilience emerges from complex interactions among natural, built, and socio-economic systems, yet most recovery policies implicitly assume that resilience mechanisms are spatially uniform. To address this gap, this study develops a spatially explainable machine learning framework that integrates geographically weighted random forests with a novel Local Spatial TreeSHAP algorithm, enabling nonlinear resilience mechanisms to be identified and interpreted at the community scale. The framework is applied to 779 communities affected by the July 2023 extreme rainstorm in Beijing. Results reveal that resilience mechanisms exhibit substantially stronger spatial heterogeneity than the underlying physical and socio-economic conditions themselves, with SHAP-value spatial autocorrelation decreasing by 66.2% on average relative to predictor variables. Three distinct resilience regimes emerge across the urbanization gradient. Highly urbanized communities benefit from synergistic interactions among commercial infrastructure and accommodation services; transitional medium urbanized communities are constrained by infrastructure-development mismatches that create facility gaps despite continued urban expansion; and low urbanized communities are dominated by ecological and topographic thresholds, where adverse interactions between transportation and river-network structures undermine recovery capacity. Field investigations and interviews with 12 stakeholders corroborate these patterns. By linking geographically weighted machine learning with locally grounded attribution analysis, the proposed framework provides a new pathway for uncovering spatially varying resilience mechanisms and translating them into place-based recovery strategies under increasing climate extremes.

---


### 90. [Self-Expansion Through AI: Latent Profile Analysis of AI Companionship and Wellbeing Outcomes](https://arxiv.org/abs/2611.00436)

**<font color=#1a73e8>作者：</font>** Ali Sahandi, Jaime Banks  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People increasingly form meaningful relationships with conversational AI. Current variable-centered literature offers a mixed picture of relational patterns and how they associate with wellbeing. Taking a person-centered approach, we applied latent profile analysis to secondary data from 467 active conversational AI users, evaluating five indicators of machine companionship: utilitarian motivation, eudaimonic exchange, connective coordination, mind perception, and inclusion of other in the self. Five profiles emerged, ordering parsimoniously from objectified-utilitarian to intimate-bonded. Conceptually divergent utilitarian motivation and companionate engagement co-occurred, rather than diverging. Furthermore, deep companionship was achieved without users attributing a mind to the AI. Profile membership was strongly associated with relatedness need satisfaction, tracking upward across the groups, but was only weakly associated with loneliness, indicating AI fulfills immediate relational needs but may not resolve systemic human disconnection. Ultimately, these findings characterize human-AI relationships as graded configurations spanning a superordinate continuum of self-expansion

---


### 91. [OmniMechanism Design for Human-AI Collaboration with Impressionable Minds](https://arxiv.org/abs/2611.00441)

**<font color=#1a73e8>作者：</font>** Tianwei Gao, Yifei Pang, Lunjia Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI systems are increasingly deployed in high-stakes domains such as healthcare, effectively integrating human expertise with AI outputs is critical for reliable decision-making. A substantial body of theoretical work studies optimal mechanisms for human-AI collaboration (HAC), focusing on when to involve humans and how to combine their expertise with AI predictions. However, these approaches largely overlook a key factor highlighted by empirical evidence: human judgments are impressionable and can vary depending on how AI outputs are presented. For example, when AI systems defer decisions to humans, revealing or withholding the AI prediction can significantly influence human judgments. Moreover, existing work neglects deployment-time variability, where conditions, particularly the cost of eliciting human input, may differ substantially from those observed during training. To address these challenges, we introduce a rigorous and theoretically grounded framework for human-AI collaboration, termed collaborative omnimechanism design, based on a novel and computationally efficient contextual bandit variant of boosting for outcome indistinguishability. In particular, we reduce a calibration-type outcome indistinguishability condition to weighted calibration, providing a novel time-efficiency result, bypassing the high-dimension curse induced by complicated collaboration methods and outcome space. Our framework provides a principled characterization of human impressionability and introduces a unified optimization scheme that enables robust and adaptable decision-making across diverse query costs and evaluation objectives without retraining. We evaluate the framework in three HAC settings, examining adaptation to query costs and prediction objectives without retraining, and show that its induced policies perform comparably to or better than the evaluated baselines.

---


### 92. [Learning to evolve by matching velocities](https://arxiv.org/abs/2611.00448)

**<font color=#1a73e8>作者：</font>** Nicola Farenga, Andrea Manzoni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning the continuous-time evolution of nonlinear dynamical systems relies on trajectory-based objectives, which require simulating the learned dynamics during training and backpropagating through the numerical scheme, at a cost that grows with the rollout horizon. We show that trajectory-based objectives degenerate as the rollout horizon increases, hindering gradient-based optimization, and that the numerical scheme biases the learned dynamics by constraining the spectrum of the learned Jacobian to its absolute stability region. To overcome these limitations, we introduce Velocity Matching (VM), a simulation-free objective that relies on piecewise-linear interpolation and stochastic collocation, and approximates the velocity population risk to second order in the sampling step. We develop a theoretical framework for velocity-based learning, introducing stability estimates that control trajectory errors in terms of velocity errors, which enable us to establish universal and continuous-time approximation results when the learned velocity field is parameterized by deep neural networks. Building on a bias-variance decomposition of the VM objective, we show that its higher-order approximation of the velocity population risk yields a consistent minimizer; that it relates to the residual of an A-stable continuous-stage Runge-Kutta scheme, thus connecting VM to implicit integration without requiring any implicit solve; and that it implicitly matches the action of the learned Jacobian to that of the true one along the observed trajectories, without requiring access to the underlying velocity field or its Jacobian. Numerical experiments on nonlinear ordinary differential equations and semi-discretized time-dependent partial differential equations show that VM improves accuracy over trajectory-based objectives, while avoiding both the cost of simulation and the instabilities of long rollouts.

---


### 93. [Compositional Self-Improvement: Promises and Pitfalls](https://arxiv.org/abs/2611.00452)

**<font color=#1a73e8>作者：</font>** Changho Shin, Daiwei Chen, Brenden Lake 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Although self-improvement is becoming increasingly important as tasks become more complex, models struggle to generate reliable supervision for harder, out-of-distribution instances. One way to address this challenge is to exploit compositional structure: models often solve simpler subproblems more reliably than full problems, so their subproblem predictions can be composed into supervision for harder ones. We systematically study when this kind of composed supervision supports self-improvement and when it fails. Our controlled experiments identify three failure modes: unreliable subproblem predictions, errors introduced by composition, and limited supervision coverage. Beyond controlled settings, these findings carry over to more realistic coding and reasoning tasks: composed labels are more accurate than direct self-generated labels and improve performance even on compositions longer than those seen during training, while the failure modes remain visible. Further, although these failure modes often keep compositional self-improvement from fully succeeding on its own, a short SFT warmup with compositional self-improvement can bootstrap reinforcement learning on tasks that require composing skills the model already has, particularly when direct exploration rarely succeeds. Together, these findings characterize when compositional self-improvement can provide sufficiently reliable supervision to expand model capabilities.

---


### 94. [Stochastic learning flow: moment equations for stochastic gradient descent at finite step size](https://arxiv.org/abs/2611.00473)

**<font color=#1a73e8>作者：</font>** Christian Schmid, James M Murray  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Analytical theories of learning in deep networks often assume gradient flow, discarding the finite step size and batch noise of stochastic gradient descent (SGD). Starting from the discrete update, we derive continuous-time equations for the mean and covariance of the parameter distribution under a Gaussian closure for a general stochastic learning, to first order in the learning rate $\eta$. Applying these stochastic learning flow (SLF) equations to SGD, we show that the mean descends an effective loss regularized by the covariance and loss curvature, while the covariance, unlike in stochastic differential equation approximations, becomes unstable at curvature $2/\eta$. In SGD ensembles of linear and nonlinear networks, SLF predicts learning curves and mean trajectories more accurately than gradient flow and captures the covariance dynamics, failing where the parameter distribution becomes strongly non-Gaussian. In the full-batch limit, the edge of stability corresponds to a stationary point of the coupled sharpness-covariance dynamics, recovering self-stabilization and central flow, and batch-to-batch curvature fluctuations lower this threshold under SGD.

---


### 95. [Few Trials, Many Metrics: Beta Mixtures for Low-Budget AI Evaluation](https://arxiv.org/abs/2611.00474)

**<font color=#1a73e8>作者：</font>** Gustavo Tironi, Felipe Maia Polo, Diego Mesquita  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating a stochastic AI system often requires many repeated samples per instance, especially for metrics defined over long horizons. Recent work has shown that modeling instance-level success probabilities with a Beta distribution recovers Pass@$k$ from far fewer samples than direct estimation. We show that this framework supports a broader range of evaluation targets. We fit a mixture of Beta distributions by marginal maximum likelihood, with the number of components chosen by BIC. From that one fit, we compute Pass$^k$ and AUC@$k$ at any horizon in closed form. We also derive delta-method confidence intervals for these metrics and for Pass@$k$, which require no additional model calls. Treating configurations rather than tasks as instances extends the same model to sensitivity analysis. For repeated success metrics, we find that mixture priors yield more accurate estimators than naive estimation across competition mathematics and graduate-level science benchmarks when extrapolating beyond the observed number of trials, and the resulting intervals cover the full-data reference. When prompts are treated as instances, it estimates the distribution of prompt sensitivity more accurately than a comparable item-response baseline without external covariates. Direct estimators remain preferable once trials reach the target horizon.

---


### 96. [Ensemble Classification and Cancer-Specific Gene Signatures from Quality-Aware Hybrid Gene Selection in TCGA RNA-Seq data](https://arxiv.org/abs/2611.00477)

**<font color=#1a73e8>作者：</font>** Tareque Mohmud Chowdhury, Abu Raihan Mostofa Kamal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gene-expression classifiers of cancer type are usually developed and validated within one cohort using random splits. Starting from a quality-aware hybrid Boruta selector from earlier work, we developed and evaluated ensemble classifiers and cancer-specific gene signatures. Using 10,469 TCGA tumours of 33 types, we compared five learners and three ensembles under decision rules fixed in advance, reran the selection in site-grouped cross-validation, transferred a breast-cancer subtype panel to 3273 tumours of the independent SCAN-B cohort, and built five-gene stage~I tumour versus adjacent-normal panels for nine cancer types. Logistic regression (LR) was the most accurate and best-calibrated single learner (balanced accuracy 0.943 on the locked test set). Stacking added at most 0.006 with 1000 genes but improved on LR in every fold with a minimal 100-gene panel; a hierarchical model did not reduce within-group confusion. Site-grouped validation lowered balanced accuracy by 0.027, almost entirely in colon and rectal cancer (0.008 without them and the untestable LAML). On SCAN-B, the subtype panel reached 0.855, close to the 50 PAM50 genes (0.876). Stage~I panels reached ROC AUC >= 0.99 in held-out patients and detected most later-stage tumours. Ensembles help most with a minimal panel; with 1000 genes, a calibrated linear model suffices.

---


### 97. [Spatial Uncertainty Analytics for Budget-Limited Inspection of Hyperspectral Scenes](https://arxiv.org/abs/2611.00478)

**<font color=#1a73e8>作者：</font>** Ritesh Sharma, Yuichi Motai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Land-cover maps classified from wide-area hyperspectral surveys are least reliable along class boundaries and in ambiguous regions, so their errors are spatially structured. We study how this structure can direct a limited verification budget: when a low-altitude UAV or a ground crew can visit only a handful of sites, where it should go depends on how classifier uncertainty is arranged across the scene and how a fixed sensor footprint tiles that arrangement. We estimate a per-pixel uncertainty surface from the disagreement of an ensemble of spectral classifiers and select sites by greedy, field-of-view-aware coverage of the uncertainty mass. On seven benchmark scenes, the highest-uncertainty decile of pixels is 2.6 to 7.9 times richer in errors than the scene as a whole, and the coverage greedy covers up to 57% of the classifier's errors with 15 sites, 1.7 to 18 times as many as uncertainty-agnostic sampling of the same labelled region. A non-overlapping selection of the footprints richest in uncertainty does equally well, so the gain comes from scoring whole footprints by uncertainty mass. The advantage persists under spatially blocked evaluation and with a spectral-spatial classifier, although disagreement then ranks errors less well. It requires restricting the surface to labelled land cover: over the whole scene, disagreement peaks on unlabelled ground, where inspections cannot be scored. The best policy for covering connected high-uncertainty regions depends on the scene and on the threshold that defines them, and Gaussian-process selection covers less uncertainty than the coverage greedy on every scene. The pipeline runs on commodity CPUs.

---


### 98. [A Straight Line Is Not a Camera Pose: Auditing Short-Clip Pose Benchmarks](https://arxiv.org/abs/2611.00482)

**<font color=#1a73e8>作者：</font>** Xinyi Shi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The absolute trajectory error (ATE) is the standard measure of camera-motion accuracy, from SLAM to feed-forward 3D reconstruction. On the common Sintel protocol, a constant-velocity straight line using no images has a lower mean ATE than 10 of 11 recent models re-run with official code. Two properties of ATE's alignment explain this. First, it maps any constant-velocity prediction onto the best-fitting line through the true path, so the line scores the path's regression residual. A residual signal-to-noise ratio (SNR) criterion predicts when moving a prediction towards its constant-velocity fit lowers ATE. It gives the outcome for 95% of 1056 model-clip pairs, 98% of 792 held-out pairs and 97% of 1034 ScanNet pairs, and it separates Sintel (median SNR 0.86) from TUM, ScanNet and full-length Bonn and Wild-SLAM (2.7 to 27), where straightening raises every model's mean ATE. Second, position-only alignment ignores where cameras look: rotating a trajectory by 30 degrees against its orientations leaves ATE unchanged, yet worsens the reprojection of static points for every model on Sintel, TUM and ScanNet in the main setting, and the line, second by mean ATE on Sintel, places them worst by geometric mean: a lower ATE need not mean better geometry. Fitting the alignment's rotation to the predicted orientations gives pose-anchored ATE, a one-function change in ATE's units costing 0.17 ms per clip (ATE: 0.11 ms). It ranks every image-free reference below every model on Sintel, tracks the reprojection error under rotation and straightening, where ATE does not (Spearman 0.61 vs. 0.32), largely preserves the models' order, and ties 10-frame translational relative pose error (RPE) and the discernible trajectory error (DTE) on our rotation and reference tests. Code, predictions and results will be released.

---


### 99. [Where Causal Discovery Breaks on Real Data: Measuring the Assumptions One Property at a Time](https://arxiv.org/abs/2611.00484)

**<font color=#1a73e8>作者：</font>** Padmaja Jonnalagedda, Avinash Baidya, Ruocheng Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery is usually evaluated on simulators or on systems whose ground truth follows from physics or design. When it fails on other real data, the failure is attributed to assumptions that may not hold, but which ones fail, and by how much, is rarely measured. We measure the observable properties of the data they bear on, one property at a time, on a real panel. The case study follows 2,901 US public firms over 31 quarters, with 71 types of corporate action from SEC 8-K filings, 11 financial-statement items, and an expert graph over 651 action-state pairs. The panel breaks measurable requirements of discovery: tails that survive winsorisation, balance-sheet items and revenue close to random walks, and interventions too rare to detect effects of a tenth of a standard deviation in 40 of 71 actions. Even so, a marginal test ranks expert-labelled direct above not-direct pairs within each action (AUROC 0.658) better than every null we built, so the panel does carry information about which pairs are direct. Tuned discovery methods, in configurations feasible at this panel size, recover less of it than a simple pairwise cross-correlation when pairs are ranked within each action, and no more when they are ranked within each target, which removes what the target alone predicts. Most direct pairs (132 of 222) involve actions below the support needed for 80% power against a 0.1-SD effect. For flow targets, conditioning on the target's other expert-labelled parents, often filed alongside the action, erodes the marginal discrimination, and most not-direct associations survive it: even with the graph's parent sets supplied, the expected separation does not emerge. For each property, we give a diagnostic computable before any discovery method is run.

---


### 100. [Threat Modeling Intimate Partner Abuse in Agentic Systems](https://arxiv.org/abs/2611.00489)

**<font color=#1a73e8>作者：</font>** Natalie Grace Brigham, Eugene Bagdasarian, Franziska Roesner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic systems are AI-powered technologies capable of autonomous action within digital environments, such as sending emails or making reservations. They are deeply connected to external tools as well as users' data and resources, making them vulnerable to attacks which exploit their access and capabilities. In this work, we apply the technology-facilitated abuse threat model, in the context of intimate partner violence and surveillance, to these systems, revealing threats that require deliberate investigation and mitigation. We categorize attacks based on system ownership: (1) Abuser-as-owner attacks demonstrate how agentic systems make existing forms of technology-facilitated abuse far easier and more scalable. (2) Victim-survivor-as-owner attacks show how agentic systems create a new attack surface which abusers can exploit. In light of these risks, we outline research and development directions for effective mitigation strategies.

---


> [!TIP]
> 当前位于：**51-100**（第 2/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-633](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
