# 📦 其他研究 | 2026年10月21日

> 本类共 **534** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**501-534**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-534**

---

### 501. [Towards Robust Model Organisms for Eliciting Latent Knowledge](https://arxiv.org/abs/2610.26698)

**<font color=#1a73e8>作者：</font>** Lennart Finke, Hardik Bhatnagar, Euodia Dodd 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A key problem in AI safety is eliciting latent knowledge (ELK), extracting information from a model that is misaligned and more knowledgeable than its overseer. For example, a misaligned model used to scan code for vulnerabilities may want to withhold its findings, i.e., sandbag, in order to exploit them later. To study ELK empirically, we need model organisms that mirror this setting. Existing model organisms fall short in several respects. In this work, we train model organisms to withhold solutions in a vulnerability detection task. We combine transcript distillation with counter-prompting and tamper-resistance training to instill three properties that we argue are critical for a useful ELK testbed: 1) Selectivity, the model sandbags when it thinks the overseer doesn't know the answer and complies otherwise, 2) Robustness, the model resists elicitation, and 3) Retention, the model retains a knowledge advantage over the overseer, as opposed to losing the relevant capability. We train a sequence of model organisms and show that our strongest model substantially outperforms prior models on robustness while keeping the other two properties intact. We hope that our model organisms provide a useful ELK testbed for the community, and that our methodology sparks the development of increasingly challenging model organisms.
All our code, models and the dataset are available at this https URL.

---


### 502. [Comparing Computer Use Behavior Across Multiple Levels of Abstraction](https://arxiv.org/abs/2610.26703)

**<font color=#1a73e8>作者：</font>** Ananya Gubbi Mohanbabu, Rosiana Natalie, Anhong Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Interaction traces record how people and agents use computers, and comparing them can reveal usability barriers, differences in expertise, and human--agent similarity. Yet traces are recorded as low-level, interface-specific actions, making comparisons difficult across tasks, interfaces, and input modalities. Existing approaches either compare these actions directly, reduce traces to aggregate outcomes, or summarize them at higher-level goals, obscuring where behavior differs. We present MAP (Multi-level Action Parsing), a hierarchical semantic representation and annotation pipeline that maps traces into a common vocabulary across linked levels of abstraction. MAP compares traces by sequence, recurring patterns, and effort, localizing differences by type and abstraction level. A technical evaluation across three computer use datasets shows high agreement with manual annotations and broad coverage of behavior. Applying MAP shows that sighted and blind users increasingly converge at higher levels despite navigation differences, while agents omit corrective, help-seeking, and recovery behaviors present in human traces.

---


### 503. [GeoSplit: Selective Edge--Server Map Acquisition for Cross-User Travel-Mode Recognition](https://arxiv.org/abs/2610.26707)

**<font color=#1a73e8>作者：</font>** Zepu Wang, Luyao Niu, Ruolin Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Networked mobility sensing couples local trajectory inference with remote geospatial context, making communication decisions part of the prediction system. We present GeoSplit, an edge--server framework for travel-mode recognition that separates the utility of map evidence, its training-time transfer, and its selective acquisition at runtime. On GeoLife with 10% labels, we evaluate these components under user-day and user-disjoint grouping. For unseen users, aligned full-map context raises macro-F1 from 0.7154 to 0.7864, while map-informed distillation yields a motion-only student at 0.7225. Through a compact query interface, entropy gating achieves 0.7729 macro-F1 versus 0.7738 for all queries, querying 39.5% of trajectories and reducing application payload by 60.5%. Under user-day grouping, selective and all-query scores are similarly close at a 21.6% query rate. Learned value estimation and probability fusion offer no consistent improvement. These results illustrate communication-efficient edge--server inference for an intelligent transportation sensing task.

---


### 504. [Doubly Robust Learning of Heterogeneous Survival Treatment Effects under Time-Varying Treatments](https://arxiv.org/abs/2610.26710)

**<font color=#1a73e8>作者：</font>** Tomàs Garriga, Munib Mesinovic, Luke De Bretton-Gordon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating heterogeneous survival treatment effects (HSTEs) from time-to-event data under time-varying treatments is important in fields such as medicine (e.g., to decide which sequence of treatments is better in terms of survival probability). However, this task is challenging because treatment decisions, patient characteristics, and censoring probability often evolve together, requiring sequential adjustment for both treatments and censoring. Existing survival learners mostly consider a single baseline treatment assignment, while longitudinal treatment-effect learners typically assume uncensored outcomes. In this paper, we introduce a novel doubly robust learner for heterogeneous survival treatment effects under time-varying treatments and history-dependent censoring. Our framework separates the intervention window from the survival horizon, with treatment prescribed for a finite period, after which care follows its natural course. We further establish the favorable theoretical properties of Neyman-orthogonality, rate double robustness and quasi-oracle efficiency. The framework accommodates flexible machine learning models for nuisance estimation and treatment-effect regression. We evaluate our learners through several numerical experiments, demonstrating their effectiveness.

---


### 505. [Deep Pontryagin Learning for Continuous-Time Stochastic Control with Jumps](https://arxiv.org/abs/2610.26718)

**<font color=#1a73e8>作者：</font>** Jean-Loup Dupret, Patrick Cheridito  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a deep Pontryagin learning framework for high-dimensional continuous-time stochastic control problems that naturally accommodates jump-diffusions. In contrast to direct policy optimization, which repeatedly differentiates the objective through the entire time-discretized dynamics, our method separates adjoint learning from policy improvement by explicitly incorporating state-sensitivity information from the Pontryagin stochastic maximum principle. For a fixed Markov control, we first compute pathwise adjoint labels by backpropagating the reward through time along simulated state trajectories, and project these labels onto the Markov state through a supervised regression step. The control is then updated by enforcing the pointwise Hamiltonian stationarity condition. We prove that the resulting projected adjoint process satisfies a discrete-time Pontryagin principle and converges, as the time step tends to zero, to the solution of the corresponding continuous-time adjoint backward stochastic differential equation. Numerical experiments illustrate the accuracy, stability, and scalability of the approach.

---


### 506. [A Flexible ROI Analysis Tool for Spatially Consistent Vegetation Index Extraction from Turfgrass Imagery](https://arxiv.org/abs/2610.26719)

**<font color=#1a73e8>作者：</font>** Kibon Ku, Thai Thanh Tuan, Jinhyun Ahn  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Time-series multispectral imaging is widely used to assess turfgrass condition; however, extracting plot-level vegetation index (VI) values remains labor-intensive when camera positions vary between acquisitions and automated plot tracking is unreliable. We developed an open-source software tool comprising (i) a graphical user interface (GUI) for the interactive placement of orientation-adjustable regions of interest (ROIs) with $N$-way subdivision to match plot geometry and (ii) a batch-processing script that computes plot-level mean VI values from single-band floating-point rasters and exports measurements and ROI coordinates in JSON format for reuse. Saved coordinates can be reapplied to measure NDVI, NDRE, and SAVI from identical pixel regions within a single time point without re-delineating ROIs. In a demonstration using rail-mounted multispectral turfgrass imagery (18 images), plot-level mean values were extracted in a single session, with coordinates reused directly for NDRE and SAVI rasters. The system reads non-georeferenced pixel-coordinate rasters natively, does not require GIS expertise, and supports reproducible VI quantification where static sensor deployment is impractical.

---


### 507. [PlanarCityLoc: Breaking Silhouette Ambiguity in LoD Aerial Localization via 3D Planes](https://arxiv.org/abs/2610.26729)

**<font color=#1a73e8>作者：</font>** Oussema Dhaouadi, Shao Jie Hu-Chen, Jakob Gollreiter 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial visual localization is crucial for autonomous drone navigation in urban environments where GNSS signals are often degraded. Lightweight textureless Level-of-Detail (LoD) city models provide a geometric map alternative to textured assets. Existing silhouette-based methods rely on image-space alignment, which can leave different camera poses indistinguishable and favor incorrect poses when segmentation errors distort the building outlines. We present PlanarCityLoc, which moves beyond silhouette overlap by leveraging the planar geometry of building facades and roofs. Following geometry-aware initialization, we match image-side planar patches to LoD model planes and use the resulting 3D-to-2D correspondences to refine pose with Perspective-n-Point (PnP). The framework uses off-the-shelf geometry and segmentation models without dataset-specific training or fine-tuning. Experiments on UAVD4L-LoDv2 and Swiss-EPFLv2 achieve state-of-the-art localization recall among the evaluated off-the-shelf LoD-based methods. By grounding image-space alignment in 3D planes, PlanarCityLoc enables more accurate aerial localization with lightweight, textureless city maps.

---


### 508. [Cross-Fitting for Neural Posterior Estimation](https://arxiv.org/abs/2610.26733)

**<font color=#1a73e8>作者：</font>** Jeffrey Regier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural Posterior Estimation (NPE) fits an amortized conditional density estimator to a simulated training set of complete-data realizations. NPE's training objective, log-likelihood, favors posterior approximations that assign arbitrarily high density to the training points, and typical families of amortized conditional density estimators (e.g., normalizing flows, Gaussian encoders) are flexible enough to oblige. The resulting policy of extreme overconfidence translates poorly to held-out data. Early stopping and other regularizers can prevent this degeneracy, but they are limited to selecting posterior approximations along an unfavorable optimization trajectory set by in-sample residuals, where the posterior mean is underfit while the posterior variance is overfit. To avoid this trade-off, we propose Cross-Fitting NPE (CF-NPE), which uses sample splitting to separate conditional-mean estimation from the estimation of the posterior's higher moments. Using $K$-fold cross-fitting, CF-NPE fits $K$ posterior-mean regressors and then fits a conditional density estimator to the resulting out-of-fold residuals. In experiments with synthetic data and in a cosmological application, CF-NPE achieves higher held-out log-likelihood than standard NPE and typically improves calibration. CF-NPE is most useful in high-dimensional, simulation-limited settings.

---


### 509. [CheckDistill: Adaptive Checklist Distillation for Efficient Distributional Reward Modeling in Image Editing](https://arxiv.org/abs/2610.26740)

**<font color=#1a73e8>作者：</font>** Yaqi Cai, Zuan Gao, Mengting Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning for instruction-guided image editing requires reward models that provide reliable, accurate, and efficient feedback. Direct scalar prediction compresses multidimensional editing preferences, whereas generative evaluators can expose their judgment through explicit reasoning. However, broad scoring criteria do not specify all instance-dependent editing and preservation constraints, and generating long reasoning trajectories is costly for online optimization. We introduce CheckDistill, a pointwise reward modeling framework that internalizes instruction-adaptive checklists. We decompose each editing condition into atomic, independently verifiable requirements and construct four-dimensional scoring labels together with structured verification evidence. After supervised score initialization, a privileged teacher conditions on checklists, item-level judgments, and dimension-level rationales to supervise the student's own scoring trajectories. A reliability-weighted on-policy self-distillation objective adjusts supervision at score tokens according to agreement between the teacher's expected scores and reference labels, while retaining candidate probability weights in a truncated token support. The deployed student directly predicts four score distributions without checklist inputs or explicit reasoning and aggregates their expectations into a scalar reward. CheckDistill achieves aggregate accuracies of 72.30%, 56.67% and 82.90% on MMRB2, MER-Bench and EditReward-Bench, respectively, exceeding the compared open-source baselines on all three metrics.

---


### 510. [Trajectory Replay: Continuous-Time Mixture Transport for Lifelong Generative Models](https://arxiv.org/abs/2610.26749)

**<font color=#1a73e8>作者：</font>** Alessandro Palma, Charles Jones, Tristan Cinquin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adapting pre-trained continuous-time generative models to sequentially incoming data without forgetting earlier tasks is a central challenge in lifelong learning. A leading strategy, generative replay, uses a generative model trained on historical tasks to augment its own continual update with synthetic samples from experience. However, it requires full trajectory simulations at every training step, which accumulate discretization errors and can degrade the replayed historical distribution. Here, we propose trajectory replay, which bypasses sample generation by training an updated velocity field to match both a frozen historical velocity along its trajectories and the incoming task's velocity field, weighted by a stability-plasticity coefficient. Through the lens of continuous-time transport, we show the resulting optimum averages the two task velocities by their respective densities and generates the mixture of their probability paths. Combined with mean velocity distillation, trajectory replay accesses historical trajectories using only a few network evaluations per continual update. Empirically, it outperforms generative replay and distillation baselines on class-incremental image generation. In two biological case studies, trajectory replay extends generative perturbation models to new contexts and experimental batches across two data modalities while preserving treatment-effect prediction.

---


### 511. [Simulation Priors for Rapid Adaptation in Model-Based RL for Autonomous Racing](https://arxiv.org/abs/2610.26757)

**<font color=#1a73e8>作者：</font>** Adrian Remonda, Jiajun Xi, Nicklas Hansen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning enables learning high-performance control policies, but its reliance on extensive interaction limits deployment on physical systems where data collection is costly, and failures are unsafe. We introduce Prior-Informed Adaptation (PIA), an offline-to-online model-based RL framework that uses structured simulation priors for rapid adaptation. PIA pretrains a world model on heterogeneous low- and high-fidelity simulated trajectories, then adapts it with limited target-domain interaction using uncertainty-regularized planning. Rather than requiring an accurate simulator for policy transfer, PIA treats simulated trajectories as biased priors whose residual mismatch is corrected during online adaptation. We evaluate PIA in autonomous racing using high-fidelity simulation and on a real full-size autonomous race car. In simulation, PIA adapts faster across track and surface shifts than strong baselines, achieving lower lap times and fewer failures. On hardware, PIA achieves reliable few-shot adaptation with less than one hour of on-vehicle interaction.

---


### 512. [AI Misconception and Adoption Among Indonesian K-12 Teachers](https://arxiv.org/abs/2610.26758)

**<font color=#1a73e8>作者：</font>** Alham Fikri Aji, Afifa Amriani, Rendi Chevi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Indonesia's fragmented geography and uneven infrastructure pose persistent challenges for adopting new educational technologies. While national initiatives aim to mainstream AI in K-12 schools by 2025, policy readiness does not automatically mean teachers are ready for the classroom. This study surveys Indonesian K-12 teachers to examine: (1) their understanding of AI, (2) how they and their students use AI, and (3) their views on the acceptability of AI in learning activities. Through semi-automated thematic analysis, we identify common misconceptions and use cases. Our findings reveal a notable mismatch: while teachers find AI use in education acceptable and support it for the sake of efficiency, they remain fully aware of the risks to learning depth and academic honesty. We also find that this high level of acceptance is currently coupled with a poor understanding of how AI actually works.

---


### 513. [Monsoon: Scalable Spontaneous Speech Collection for Low-Resource ASR in 50 Languages](https://arxiv.org/abs/2610.26776)

**<font color=#1a73e8>作者：</font>** Shobhit Banga, Manas Dhir, Aaditya Pareek 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> For most languages, automatic speech recognition (ASR) is limited less by model architecture than by a lack of accurately transcribed spontaneous speech. We present Monsoon, a framework for collecting such data at scale. It elicits unscripted conversations between paired contributors, screens recordings with automated classifiers, corrects transcripts over five levels of human review, and selects segments for lexical and acoustic coverage. It has collected speech in 50 languages; we analyse seven 3,500-hour corpora. At equal volume, its quality stages reduce semantic word error rate (WER) by 10-39% relative to a conventional protocol. Compared with an architecture-matched baseline trained on public corpora, Whisper fine-tuned on Monsoon performs comparably on the baseline's own test sets and reduces semantic WER by 20-44 points on conversational benchmarks. The gains transfer to a second architecture and grow with data volume. We release the framework, its quality-control models, and the fine-tuned models.

---


### 514. [Topological Sheaves of Irreducibility: A Theoretical Framework for Multi-Agent Task Obstructions](https://arxiv.org/abs/2610.26777)

**<font color=#1a73e8>作者：</font>** Steven Motta, Davide Mambelli, Alessandro Rozza  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems can differ under identical agents and communication budgets when they support different forms of joint interaction. We introduce Topological Sheaves of Irreducibility (TSI), a sheaf-theoretic framework separating task-level compatibility obstructions from system capability. A task is represented by an interaction complex $K$ and a capacity sheaf $\mathcal{F}$; nonzero $H^n(K;\mathcal{F})$ defines a structural signature, while registered interventions test capability. For cocycle data, cochain realization is solvable exactly when the represented cohomology class vanishes. Examples show that the signature is sheaf-relative, and the degree-1 reduction yields cycle-space witnesses and observation requirements. We evaluate two finite one-round models. Across 15,625 degree-1 inputs, an all-agent additive primitive solves decision and repair exactly; the optimal pairwise system reaches 88.80% on decision, one input above the 88.79% majority-class baseline, and 26.63% on repair. On a degree-2 tetrahedral-boundary task over 531,441 inputs, the same-2-skeleton system retains all four three-agent primitives yet matches the pairwise-only optimum throughout the registered separation window, whereas adding the class-filling four-agent primitive makes both tasks exact. Status-preserving robustness checks retain exact performance but are not cost-matched to the class-restoring ablation. Conditional on the registered primitives and cost models, TSI provides task-relative, falsifiable tests of higher-order interaction.

---


### 515. [V-JEPA Hand: Simple, Accurate and Fast 3D Hand and Camera Trajectory Recovery from Egocentric Videos](https://arxiv.org/abs/2610.26780)

**<font color=#1a73e8>作者：</font>** Ruicheng Li, Qixiu Li, Yu Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric video supports diverse applications, including robot learning, augmented reality, and human activity understanding. Recovering metric 3D hand trajectories from such video requires estimating both hand motion and camera egomotion to express the hands in a consistent reference frame. Many existing pipelines recover hand and camera motion in separate stages, combining hand detection, hand reconstruction, camera tracking, and trajectory refinement. We present V-JEPA Hand, a simple feed-forward video model that jointly reconstructs bilateral hand motion and camera motion from egocentric clips. It uses a self-supervised V-JEPA 2.1 encoder to extract spatio-temporal features from full-frame video and a query-based predictor to decode these features into per-frame hand poses, hand presence, and camera motion. We use the predicted camera motion to express the hand trajectories in a common world frame. The model accepts known focal lengths or predicts them when unavailable. It reconstructs each clip in a single forward pass. We train both components end to end in a single stage on a mixture of diverse pseudo-labelled videos and high-precision 3D annotations. A single model achieves the lowest coverage-aware mean per-joint position error (MPJPE) among comparable baselines on ARCTIC, HOT3D, and EgoStandard. It also yields lower world-frame trajectory errors than the compared SLAM-based pipelines. Ablations support the benefits of video pretraining, temporal context, and mixed supervision. V-JEPA Hand achieves a forward-pass throughput of 93.4 FPS on a single RTX A6000. Project page: this https URL.

---


### 516. [RESIN: Multi-Chain Reasoning with Entity-Structured Indexing](https://arxiv.org/abs/2610.26782)

**<font color=#1a73e8>作者：</font>** Xuanyu Meng, Jash Rajesh Parekh, Jiawei Han  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-chain reasoning is a challenging task not only because the multi-chain evidence is dispersed, but also because different parts of reasoning may require distinct, interacting chains of support. Flat retrieval can flood a model with loosely related text, whereas early selection of a single reasoning path can discard evidence that becomes useful only after other facts are considered. We introduce RESIN (Reasoning with Entity Structured Indexing), which uses structure to locate evidence while keeping the original source as the basis for reasoning. RESIN decomposes a question into focused one-hop needs, retrieves a small set of source-grounded units for each hop, and places only this relevant evidence in a compact reasoning buffer. The buffer preserves alternative supports until final composition, making intermediate decisions explicit without forcing a brittle path. On the full HolisQA benchmark, RESIN achieves 82.92 context recall and 76.70 answer relevancy over all questions, with higher reported CR and AR across five domains and higher F1 in four domains than the published baselines. Ablations show that both typed evidence diversity and hop-wise decomposition are essential, supporting a clear conclusion: Precise evidence organization and delayed commitment make multi-chain reasoning effective and auditable. Our code is available at this https URL.

---


### 517. [On Data Scaling in Tabular ML: More Data, Better Generalization?](https://arxiv.org/abs/2610.26794)

**<font color=#1a73e8>作者：</font>** Ivan Rubachev, Nikita Lazarev, Artem Babenko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work in tabular machine learning has emphasized the importance of diverse and realistic evaluation settings. The niche of large-scale (1M+) data, however, remains under-explored. To study training-data scaling, we assemble eight real-world tabular datasets with up to around ten million training examples, retaining the natural distribution shifts of the tasks and using random-split evaluation as a control. We find that GBDTs and MLP-based models show broadly similar scaling trends, with gains from both additional training data and algorithmic improvements. Tabular foundation models show more varied scaling behavior, with recent versions benefiting more consistently from larger contexts even under distribution shift. However, scaling training data under distribution shift introduces new challenges: in-distribution and out-of-distribution performance mostly improve together at smaller scales but can diverge at larger scales. We examine this through MLP capacity sweeps and comparisons of the validation distributions used for tuning and early stopping in MLPs and GBDTs. We also compare common practices of using validation data, contrasting its use for model selection in MLP pipelines with using it for in-context fitting in tabular foundation model pipelines. Under stronger shifts, MLPs selected using validation representative of the evaluation conditions generally maintain or improve performance as training data grows. In contrast, including such examples in context improves foundation-model performance, but does not prevent deterioration with increasing training size in our experiments.

---


### 518. [Two hidden layer suffice: the caterpillar net](https://arxiv.org/abs/2610.26795)

**<font color=#1a73e8>作者：</font>** Jakob Paul Zimmermann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Every continuous piecewise linear (CPWL) function is a finite signed sum of maxima of affine functions, making maximum representation a central problem in the study of the expressiveness of ReLU networks. A now-disproved conjecture predicted logarithmic depth for maxima. Inspired by the proof by Brunck et al. (2026) that two hidden layers suffice for general CPWL functions, we give the Caterpillar Net, a nonrecursive construction for the maximum of $N$ inputs with two hidden layers of widths $O(N^2)$ and $2^{O(N\log N)}$. The construction has a direct geometric interpretation.

---


### 519. [Learning to Refer: Inference-Time Collaboration in Decentralized Federated Learning](https://arxiv.org/abs/2610.26800)

**<font color=#1a73e8>作者：</font>** Yuheng Ma, Chendi Wang, Qiong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In decentralized federated learning, heterogeneous clients may develop complementary expertise, yet each query is typically evaluated only by the client where it arrives. To exploit this distributed expertise without global coordination, we formulate inference-time collaboration as budgeted local expert referral, a graph-constrained routing process in which a query can move only between neighboring clients and only visited clients contribute to its final prediction. EdgeDRM implements this framework by learning a density-based routing potential for each client: differences between neighboring potentials provide the comparisons used to select successive referrals, while local task models generate predictions that are aggregated along the resulting route. Both training and inference are decentralized, using only neighbor-local information without a central router or graph-wide client scoring. We establish estimation guarantees for the learned comparisons and characterize how local improvement and graph structure govern prior-weighted density gains from referral. Experiments on benchmark and real-world medical data show that EdgeDRM outperforms graph-matched decentralized baselines in most settings, with the clearest benefits under sparse connectivity.

---


### 520. [Mise-en-Video: Fine-Grained 3D Control for Multi-Shot Video Generation](https://arxiv.org/abs/2610.26801)

**<font color=#1a73e8>作者：</font>** Yingshuang Zou, Xiaoyu Shi, Yawen Luo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in text-to-video generation have enabled high-fidelity single-shot synthesis, yet practical storytelling creation requires multi-shot videos with both strong inter-shot consistency and fine-grained controllability. Existing multi-shot video generation approaches achieve strong consistency but still fall short in controllability. In this paper, we propose Mise-en-Video (MeV), a highly controllable multi-shot video generation framework that allows video creators to conduct staging the multi-shot in the 3D space and then generate the corresponding multi-shot video. To achieve this, our framework combines a hierarchical attention mechanism for multi-level narrative consistency with 3D-aware layout guidance for precise, per-shot spatial control. To support training and evaluation, we develop standardized annotation pipelines and construct a 160K-video dataset with hierarchical multi-shot texts and oriented 3D bounding boxes. Extensive experiments demonstrate that MeV consistently outperforms strong baselines in video quality, inter-shot consistency, and subject-level controllability.

---


### 521. [State World Models: Execute the Rules, Generate the Pixels](https://arxiv.org/abs/2610.26811)

**<font color=#1a73e8>作者：</font>** Chan Yan Ki, Yanran Zhang, Wenzhao Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing world models can generate action-conditioned video from a single image. Many focus on camera movement, allowing users to explore the generated scene. However, navigation alone does not ensure that an action follows persistent rules when its outcome depends on state that is invisible in the current frame. We present Stateful Harness, a framework that separates world evolution from video rendering to support stateful and rule-governed interaction. It maintains an evolving world state under specified rules, renders each resulting event with a frozen video model, and uses the generated clip to update the world state for the next turn. At each turn, the harness resolves the action selected by the user and compiles the resulting event into an instruction, while a preview clip from an editable 3D scene provides spatial and camera guidance. To evaluate rule compliance, we build WorldState-Bench, a benchmark of 50 counterfactual twin pairs that share an initial frame and action but differ in hidden state and required outcome. Under rule-only prompting, the best of the 11 evaluated video backends produces the required endings for both cases in 32% of pairs. For MiniMax-H3, specifying the required endings raises this rate from 32% to 64%, while the full harness reaches 92% with the same frozen model. These results support separating rule execution from video rendering for world interactions with hidden state.

---


### 522. [PICA-WAM: Visual Perturbation Invariance via Cross-Appearance Self-Alignment in World Action Models](https://arxiv.org/abs/2610.26813)

**<font color=#1a73e8>作者：</font>** Yude Zou, Yifei Yao, Guanbo Jiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) jointly predict future video and generate actions, yet remain sensitive to task-irrelevant visual perturbations, i.e., changes in visual appearance that should not affect robot behavior. We identify a gap in conventional WAM training: video prediction encourages representations to preserve appearance information, while action generation does not explicitly enforce invariance to task-irrelevant appearance. Data augmentation exposes WAMs to such perturbations but does not require perturbed and nominal observations to produce consistent action representations, and alignment with external pretrained features does not guarantee the desired invariance. To address this gap, we propose PICA-WAM, a self-supervised training framework that casts perturbation invariance as an auxiliary cross-appearance self-alignment task for WAMs. An exponential-moving-average (EMA) teacher processes the nominal observation to provide a deeper-layer target, while the online WAM processes a perturbed observation and aligns its shallower-layer action representation to this target through a lightweight projection head. Across four strong WAMs evaluated on RoboTwin 2.0, LIBERO-Plus, EBench, and a real robot, PICA-WAM consistently improves robustness under visual perturbations, preserves nominal performance in simulation, and raises the real robot success rate. PICA-WAM further reduces the sensitivity of video features to task-irrelevant appearance and its propagation into actions, as shown by paired layer-wise diagnostics. Code: this https URL

---


### 523. [Real-Time Radar Semantic and Panoptic Scene Understanding](https://arxiv.org/abs/2610.26816)

**<font color=#1a73e8>作者：</font>** Santosh Parit, Julia Hindel, Rohit Mohan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust scene understanding under varying environmental conditions is essential for safe autonomous driving. While cameras and LiDAR degrade in adverse weather and poor lighting, Frequency-Modulated Continuous-Wave (FMCW) spinning radar provides dependable 360° perception at extended ranges with minimal compute cost. However, real-time FMCW radar scene understanding is challenging due to complex signal returns, limited temporal resolution, and scarce annotated datasets. We introduce StreamRPS, a novel framework for streaming FMCW radar panoptic segmentation, comprising an automated label-generation pipeline via LiDAR scene completion and a real-time streaming network for semantic and panoptic segmentation. Our encoder-decoder streaming architecture comprises a radar-specific hierarchical Transformer encoder and task-specific decoders for semantic or panoptic prediction. Our encoder introduces a stem to capture range-dependent signatures, anisotropic patch embeddings to preserve angular resolution, and axial polar attention to separately model the periodic azimuth and bounded range axes. We further introduce azimuth roll rotation augmentation to simulate ego-vehicle rotation during training. Comprehensive experiments on the SAX and BOREAS datasets validate both our auto-labeling methodology and streaming segmentation network against established baselines. We outperform the strongest baseline by at least 1.4pp while processing sectors at over 400 FPS in a 4-sector streaming setting. We additionally provide manual annotations for 100 SAX radar scans, enabling independent evaluation of the entire framework.

---


### 524. [Next Best Action: Causal Constrained Offline RL for Business Action Targeting](https://arxiv.org/abs/2610.26817)

**<font color=#1a73e8>作者：</font>** Surya Ramachandiran, Yiming Li, Juan Mancilla-Caceres 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Next Best Action (NBA) systems must select among customer interventions (e.g., discounts, promotions, and lifecycle actions), maximize long-term economic value, satisfy complex operational constraints, and remain causally grounded. Existing approaches lack a rigorous framework for meeting these requirements jointly. We address this gap by formulating NBA as a Constrained Markov Decision Process (CMDP). We then integrate off-policy causal correction of the estimated customer dynamics directly into the Linear Programming (LP) formulation of the CMDP. The resulting policy selects actions based on customer states to maximize long-term value while explicitly enforcing business guardrails. Furthermore, the LP formulation yields shadow prices that quantify the economic trade-offs of operational constraints (e.g., fairness and user welfare), enhancing policy interpretability. We validate our proposed offline Reinforcement Learning (RL) framework on an industry case study involving rideshare coupon targeting, where customer states are defined by Recency, Frequency, and Monetary (RFM) stages. We evaluate performance using model-based off-policy evaluation, with causal dynamics estimated from a temporal holdout. Under the observed coupon budget and RFM state representation, our optimized policy improves customer lifetime value (LTV) by 19% over the estimated behavior policy and 8% over a myopic baseline. Although the demonstrated action space is binary, the proposed framework is action-agnostic, yielding a general-purpose decision module for targeting systems that manage multiple interventions.

---


### 525. [Open-Form Geometric Style Transfer](https://arxiv.org/abs/2610.26820)

**<font color=#1a73e8>作者：</font>** Adar Elad, Gal Metzer, Omer Dahari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A geometric style learned from one family of shapes is typically applied to new shapes from the same family. We consider a more challenging setting: learning the geometric design language of a stylized Latin alphabet and applying it to new forms, from Greek glyphs to entirely different structures such as human poses. We introduce Open-Form Geometric Style Transfer, where the forms to which a learned geometric style can be applied are not restricted to the shape family in which that style was observed. This setting is deceptively challenging: the difficulty is not merely learning a style, but learning the style without learning the shape family in which it was observed. We represent target forms by structural sketches and disentangle structural adherence from style realization using a Geometry LoRA and a style-specific LoRA. Critically, open-form transfer requires the Geometry LoRA to be universal. To achieve this, we devise a geometry-enrichment strategy that constructs a large and purposefully diverse collection of synthetic structural sketches spanning a broad range of unfamiliar geometries. Our experiments and ablations demonstrate the importance of both disentanglement and this universal geometry prior, enabling geometric styles learned from glyphs, pictograms, and other shape families to be transferred to substantially different, unseen forms.

---


### 526. [AfriBED: a Speech Recognition Bias Evaluation Dataset for Low Resource African Languages](https://arxiv.org/abs/2610.26821)

**<font color=#1a73e8>作者：</font>** Claytone Sikasote, Hussein Suleman, Jan Buys  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite advancements in automatic speech recognition systems (ASR), current systems exhibit speaker-attribute bias, i.e., their speech recognition performance is biased against certain speakers based on their demographic attributes such as gender, accents, and speaker type. However, accurately assessing speaker attribute bias in a given ASR system requires the availability of a bias evaluation dataset with comparable speech across subgroups of a speaker attribute. In this paper, we introduce African speech Bias Evaluation Dataset (AfriBED), a novel speech recognition bias evaluation dataset for two low resource African languages, Bemba and Nyanja, to detect and estimate gender and speaker-type bias for ASR systems. The dataset comprises 9 hours of speech with 3928 utterances recorded by 80 speakers for Bemba, while the Nyanja set includes 6260 utterances with approximately 18 hours of speech recorded by 127 speakers. The results of our baseline experiments demonstrate that the datasets are useful for examining gender and speaker-type attribute bias in the target languages.

---


### 527. [SpecMRL: Redesign Matryoshka Representation Learning within Parametric Spectrum](https://arxiv.org/abs/2610.26824)

**<font color=#1a73e8>作者：</font>** Zhongxin Chen, Songhao Wu, Heng Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Matryoshka Representation Learning (MRL) is designed to support flexible representation sizes by jointly optimizing nested prefixes. While effective, this design lacks an explicit constraint to ensure that the leading portion provides a suitable compact encoding. To address this, we propose SpecMRL, which reorganizes the feature space to enable more effective prefix readout. Specifically, we extend MRL with a parameter-derived spectral basis organized with feature importance. SpecMRL otherwise follows standard MRL, with prefix readout performed in the learned spectral space. Experiments on MTEB show that SpecMRL outperforms MRL at all evaluated reduced dimensions, with larger gains under more aggressive compression. These results suggest that the learned spectral basis better prioritizes informative directions, enabling more effective representation compression. Notably, SpecMRL extends the performance frontier of MRL, surpassing full-dimensional MRL with only half the embedding dimensions.

---


### 528. [KEEP-Bench: Evaluating Evidence Preservation in Context Compression](https://arxiv.org/abs/2610.26827)

**<font color=#1a73e8>作者：</font>** Ziqing Man, Di Wu, Jia-Chen Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Context compression improves long-context efficiency but may introduce faithfulness issues through an information bottleneck. Existing evaluations rely on QA metrics, but a reader can still answer correctly from an unfaithful compression, so these metrics underestimate such loss. To bridge this gap, we introduce KEEP-Bench, a diagnostic benchmark that directly assesses compression faithfulness with 4,102 cases across three challenging settings that require keeping evidence for plausible reference resolutions, explicit qualifiers, and minority perspectives. Experiments show that even with tailored prompting, the strongest models remain unreliable: despite context windows exceeding 100K tokens and inputs averaging only 3.1K tokens, the best open-weight model (31B) preserves all required evidence in only 66.8% of cases, and the best proprietary model in only 61.6%. Performance also varies sharply across evidence structures, so conclusions from limited structures may be biased. We further introduce a metric, Evidence Preservation Return (EPR), to relate evidence recall to inference FLOPs, and find that it peaks at moderate scales (4B-8B), where recall remains low. Additional output budget mainly benefits already strong models and widens capability gaps, yet the stronger preservation of these models comes at a steep computational cost. These findings highlight the importance for future work to investigate compressors with strong information preservation under a small computation budget, rather than relying on a large output budget or model scaling.

---


### 529. [ProteinGeoBench: Frontier Structural-Biology Agents Are Fluent at Lookup but Lost in Geometry](https://arxiv.org/abs/2610.26829)

**<font color=#1a73e8>作者：</font>** Matt Turk, Brandon L. Neel, Diana M. Lopez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier agents retrieve structural metadata well and compute geometry from coordinates less reliably. We ask how much of a benchmark score reflects that gap and how much reflects the evaluation configuration around the model. We study ProteinGeoBench, a suite of 131 protein-structure tasks, using 4,249 rollouts from four frontier models and 4,486 further trials across 26 models. Three of the four frontier models fall within 0.031 of one another (0.785 to 0.816) with no difference between them resolved, while the fourth scores 0.707 and all three gaps to it exclude zero. Three of the four do better on metadata lookup than on numeric calculation. The fourth is slightly better on numeric. Numeric tasks are 28 of the 131 but half of the twelve tasks that all four models fail. The ranking also depends on the evaluation budget: with one run per task, 23.9% of bootstrap replicates put a different model first. On a selected 15-task slice, removing network access lowers scores more than blocking eight structural-database domains, but the two contrasts were graded in different passes and cannot be cleanly decomposed. Swapping in each model's own command-line agent changes scores by -0.071 to +0.086, a comparison too small to rule out moderate harness effects. Across 26 models, numeric performance rises with non-numeric performance rather than staying flat. The experiments use different task subsets, so they cannot rank model, harness, access and task composition against one another. Evaluations should report results by task family, along with the number of runs, the harness and the access conditions.

---


### 530. [Kronecker Delta Rule for Long Context Linear Attention](https://arxiv.org/abs/2610.26834)

**<font color=#1a73e8>作者：</font>** Anamaria-Roberta Hartl, Levente Zólyomi, Michael List 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose KronLSTM, a linear attention architecture based on the Kronecker Delta Rule, a novel update rule for associative matrix memories. KronLSTM extends the xLSTM family with a memory-revision mechanism that corrects targeted associations while modifying the memory only along a single direction in matrix space. This minimally invasive memory revision reduces interference with previously stored information compared with delta-rule updates, making it particularly well suited for long-context language modeling. The resulting memory dynamics can be mathematically described as a Markov chain that converges to a steady-state distribution, while the expected norm of the memory matrix remains uniformly bounded throughout the entire input sequence. Hence, KronLSTM ensures stable memory dynamics without requiring additional normalization and stabilization mechanisms for the memory state. Experiments show that KronLSTM is competitive with, and often outperforms, existing linear attention architectures, including models of the (Gated) DeltaNet family, with particularly strong performance on long context benchmarks. These results establish the Kronecker Delta Rule as an effective and analytically tractable foundation for stable associative memory in recurrent linear attention architectures. Our code (this https URL) and models (this https URL) are open-source.

---


### 531. [AnyGoal: On World Model Generalization Beyond Expert Rollouts](https://arxiv.org/abs/2610.26844)

**<font color=#1a73e8>作者：</font>** Heejeong Nam, Divyat Mahajan, Quentin Le Lidec 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The goal of a world model is to capture the dynamics of an environment. This has the great appeal that it allows agents to plan and simulate a course of actions with the help of a world model. For these uses to be reliable, however, the learned dynamics must behave well beyond the specific state-action combinations observed in expert rollouts. Despite this, the relationship between data coverage, dynamics generalization, and downstream planning performance remains underexplored. We study this relationship through the lens of compositional generalization: can a world model recombine familiar state and action factors into valid dynamics? To answer this, we introduce AnyGoal, a benchmark of goal-shifted task variants built from widely used world-model environments, together with an open-source library. Each task is designed to be within reach of a world model that has learned the underlying dynamics: individual state factors and actions remain within their training support, but their combinations are underrepresented in expert trajectories. Across multiple environments and world model families, we find that current models consistently exhibit failures under these recombinations. By examining dynamics and representation failures across model families, interaction regimes, and evaluation metrics, we study where current world models generalize and where challenges remain for goal-shifted prediction and planning. Together, this framework, benchmark, and analysis provide a basis for evaluating progress toward world models that generalize to new planning tasks.

---


### 532. [Manga2Animate: An Agentic Framework for Faithful Manga Animation with Script and Storyboard Planning](https://arxiv.org/abs/2610.26851)

**<font color=#1a73e8>作者：</font>** Sheng-Wei Zhang, Hsi-An Chen, Yan-Ting Liou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adapting existing manga into coherent animation that stays faithful to the source is a valuable yet challenging task. Existing methods either access the manga mainly through text, losing its characters and art style, or feed manga pages directly into video generation models, which misinterpret the manga's structure and produce incorrect storylines. In this paper, we propose Manga2Animate, a multi-agent framework that grounds every stage of generation in the source manga. We decompose the task into two intermediate representations, an animation script and a visual storyboard. Each representation is produced by a creator agent and reviewed against the source panels by a paired reviewer agent. We tailor representation-specific selection and dual-level feedback to progressively refine both before synthesizing the final animation. Extensive experiments and a user study demonstrate that Manga2Animate produces animations more faithful to the source manga and more consistent across shots than state-of-the-art approaches. Project page: this https URL

---


### 533. [Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](https://arxiv.org/abs/2610.26855)

**<font color=#1a73e8>作者：</font>** Tianqi Liu, Hanfei Zhao, Qifeng Liang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heterogeneous action spaces and limited multimodal supervision. We present Ropedia W0, the first egocentric loco-manipulation world foundation model spanning humans and robots with diverse embodiments. We curate Xp-Data, comprising 10k hours of egocentric human data and 3k hours of robot data with unified multimodal annotations and systematic quality control. A unified kinematic representation encodes locomotion through camera poses and manipulation through projected skeletons, with robot skeletons combining embodiment-specific forward kinematics with extensive manual keypoint annotation and correction. We also introduce Xp-Teleop, a long-horizon loco-manipulation benchmark based on high-quality dexterous humanoid teleoperation data. Evaluations demonstrate state-of-the-art performance across five cross-embodiment benchmarks (DreamDojo, $\Psi_0$, $\omega$-HOME, Xp-Teleop, and AgiBot) and on held-out human egocentric video, from zero-shot inference to few-shot and full-data post-training. Scaling human pre-training data improves performance on both human and robot evaluations. After distillation, our model supports real-time, minute-long rollouts, enabling live VR interaction. Applications in policy evaluation, model-based planning, and world-action modeling further demonstrate the model's utility for embodied decision-making.

---


### 534. [VideoMaMa++: Temporally Consistent Video Matting via Preserve-and-Refine Token](https://arxiv.org/abs/2610.26857)

**<font color=#1a73e8>作者：</font>** Sangbeom Lim, Seoung Wug Oh, Heeji Yoon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based video matting has recently emerged as a leading approach, leveraging video diffusion priors from internet-scale pretraining to achieve strong zero-shot generalization from limited synthetic data. However, the heavy compute of these diffusion backbones limits inference to a short chunk of just 6 to 24 frames, so even ordinary videos span multiple chunks. Because each chunk is matted independently from coarse mask guidance, existing methods fail to maintain consistency across chunk boundaries, producing flickering edges and discontinuous transparency. We address this with a mask-guided diffusion-matting framework built on two ideas. The RGB and mask conditioning are represented as separate token streams that interact through full spatio-temporal self-attention, letting the model adaptively combine fine RGB texture with coarse mask layout rather than committing to a fixed channel-wise fusion. On top of this, we propose a novel pair of learnable embeddings, the preserve token and the refine token, that act as a per-frame conditioning interface and enable a sliding-window inference scheme in which already-generated mattes are propagated across chunk boundaries for local temporal consistency, complemented by a globally shared reference anchor at every chunk to prevent error accumulation in long sequences without any additional training. Across standard video matting benchmarks and in-the-wild long footage, our framework outperforms prior diffusion-based methods in both fine-detail accuracy and temporal consistency, and uniquely maintains consistency across chunk boundaries on long videos.

---


> [!TIP]
> 当前位于：**501-534**（第 11/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-534**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
