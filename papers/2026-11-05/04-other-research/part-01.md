# 📦 其他研究 | 2026年11月05日

> 本类共 **280** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-280](./part-06.md)

---

### 1. [CARD: A Proof-Carrying Certificate-to-Action Interface for Relative-Measurement Graphs](https://arxiv.org/abs/2611.03651)

**<font color=#1a73e8>作者：</font>** Yushan Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Geometric certificates make mathematical claims about specified estimator objects, while robotic action requires a physical transform, a service decision, and timely proof support. We present CARD, a proof-carrying interface that keeps these objects distinct and records how they combine. Its lifted-fiber formulation separates semantic motion from witness repair and characterizes when projected and proof-carrying costs coincide. Its actionability result gives an exact useful-service law: uniform sampling without replacement produces a hypergeometric yield, while sampling from the eligible population gives one useful service per request under the observed live-confirmation condition. The primary study contains 404 Full16 cases from 20 sorties of an AA15-X500 airborne survey system. All 404 checker-confirmed optimizer points are reference-discrepant, with median rotation and translation discrepancies of 1.9891 degrees and 21.6322 m. The paired causal-navigation transforms are reference-consistent in all 404 cases, with medians of 0.0036566 degrees and 0.0104519 m. Across five matched request budgets, the largest difference between the hypergeometric prediction and the observed ordinary-random mean is 0.8412 services. Ordinary matched random reaches 0/50 target successes, while actionability-matched random reaches 50/50 and matches the CARD policy. Public downstream evaluation on 11 KITTI, EuRoC, and TUM SLAM cases measures optimizer wall-time ratios of 1.128x-67.65x for random versus CARD graph interventions. Native solver records locate this difference in elimination fill, Cholesky factor size, and numeric factorization. Together, these results connect certificate semantics, physical execution, proof acquisition, and graph computation through explicit system objects.

---


### 2. [Latent Cluster Separation as a Regularizer for Lifelong Anomaly Detection](https://arxiv.org/abs/2611.03652)

**<font color=#1a73e8>作者：</font>** Sabarish Radhakrishnan, Nathalie Japkowicz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lifelong (continual) anomaly detection systems must learn a sequence of tasks without forgetting how to recognize anomaly types seen earlier -- a property known as backward transfer. A common way to try to improve backward transfer is to reshape a model's internal representation around learnable concept centroids, typically coupled with a new way of scoring anomalies based on distance to those centroids. Because these two design choices are usually introduced together, it is unclear which one is actually responsible for any performance gain. In this paper, we unbundle the two mechanisms within a VAE-based lifelong anomaly detector and study them separately. We find that used purely as a training-time regularizer -- while leaving anomaly scoring unchanged -- latent cluster separation can improve detection quality and backward transfer, though whether it outperforms the alternative scoring approach depends on the dataset's underlying representation. Switching to distance-based scoring is instead where most of the instability commonly associated with this class of method actually originates; we identify and explain the underlying mechanism. This benefit depends on the dataset's underlying representation, and we report this as practical guidance for choosing between the two design choices, rather than as a list of caveats.

---


### 3. [Four Extensions of the Universal Law of Robustness: Log-Concave Covariates, Heterogeneous Mixtures, Vector-Valued Predictors, and Markovian Data](https://arxiv.org/abs/2611.03653)

**<font color=#1a73e8>作者：</font>** Tobias J. Peter  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bubeck and Sellke's universal law of robustness says that fitting $n$ noisy samples below the noise level with a class of $p$ real parameters forces a Lipschitz constant of order $\sqrt{nd/p}$, when the covariate distribution on $\mathbb{R}^d$ is isoperimetric: smooth interpolation costs a factor $d$ of overparametrization. Its hypotheses are Gaussian-type concentration, a homogeneous covariate law, scalar outputs, and independent samples; we relax each one. Exponential concentration suffices, at the unchanged rate and absolute constant and at the price of a capacity burn-in, some form of which we show is necessary; this gives the law for normalized log-concave covariates, with a $\log d$ loss from the current KLS bound. For heterogeneous mixtures the worst component constant is replaced by the weighted average of the component constants, under a typicality condition on the mixture composition. For vector-valued predictors the bound at the Frobenius Lipschitz scale is free of the output dimension $K$, and the Euclidean bound loses only $K^{-1/2}$, a loss that covariate-independent noise removes. Stationary Markov covariates retain the i.i.d. rate, the pseudo-spectral gap entering only the sample-size conditions. One master theorem carries the shared argument, and constants are explicit throughout.

---


### 4. [Towards Automatic Heart Murmur Characterization from Multi-spot Phonocardiograms](https://arxiv.org/abs/2611.03654)

**<font color=#1a73e8>作者：</font>** Marcelo Nogueira, Jorge H. Oliveira, Carlos G. Ferreira 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cardiac auscultation traditionally detects the presence of a heart murmur, but clinicians further characterize it by timing, shape, pitch, quality, and grade. Most automatic phonocardiogram analysis systems stop at binary detection and do not estimate this richer description. In this work, we formulate automatic murmur characterization as five patient-level classification tasks and compare three multi-spot strategies on recordings from the aortic, pulmonary, mitral, and tricuspid auscultation locations. First, classical and deep-learning classifiers are trained independently at each location, and predictions are combined via a maximum-severity late-fusion rule. Second, a synchronous multi-input CNN jointly processes one representative segment per location for a single task. Third, a unified multi-input, multi-output CNN predicts all five attributes from one shared multi-spot representation. Using 735 patients from the CirCor DigiScope dataset with complete four-spot recordings, the best late-fusion configurations reach an unweighted mean sensitivity between 85.56% and 93.81% across the five tasks, with class-specific recalls between 80.00% and 100.00% for every relevant category. The multi-input CNN trails late fusion by 7-16 points depending on the task, while the multi-output model reaches values between 72.59% and 79.40%, estimating all five attributes from one shared representation. We further show that naively balancing training data by adding all minority-class segments degrades patient-level performance under the maximum-severity rule, since it introduces non-representative, noisy segments not filtered by the clustering-based segment selection used for evaluation. These results indicate multi-spot murmur characterization is feasible with both fusion-based and jointly learned architectures, outlining a path toward automatic, structured murmur reports complementing binary screening.

---


### 5. [Learning Directional Randers Geometry for Latent-Space Exploration](https://arxiv.org/abs/2611.03675)

**<font color=#1a73e8>作者：</font>** Théau Blanchard, Stéphanie Allassonnière  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks extract powerful latent representations from images, enabling fast and efficient downstream analysis. However, these latent spaces lack explicit geometric structure, leading to possibly poor interpolation fidelity and misleading extrapolation. Latent interpolation techniques assume symmetric transition costs which are often not the case for real world data. Their symmetric nature cannot capture directional processes, such as disease progression, where certain transitions are impossible (e.g. tumor growth dynamics or cognitive improvement in Alzheimer's disease). Although Riemannian metrics extend Euclidean geometry by incorporating curvature, they remain symmetric. We show that understanding asymmetry and not curvature alone directly addresses these problems. To do so we propose a new Finsler-Randers metric learning framework. It incorporates direction-dependent distances, thus enabling the computation of trajectories respecting monotonic sequential constraints. We demonstrate its potential for interpolation and extrapolation on controlled cross-sectional datasets.

---


### 6. [InterceptFuzz: Interception-based Stateful Fuzzing of Single-Process Targets](https://arxiv.org/abs/2611.03709)

**<font color=#1a73e8>作者：</font>** Ilja Siroš, Dave Singelée, Bart Preneel  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Stateful protocol implementations are commonly fuzzed by tools that act as a network client and exchange messages with the target over sockets. Some wireless and IoT protocol stacks instead provide a single-process simulation platform, in which all nodes run in one binary and exchange packets in memory. Such simulations are deterministic and fast, which suits fuzzing, but offer no socket to which existing stateful fuzzers can attach. Meanwhile, fuzzing infrastructure such as Google's OSS-Fuzz supports only stateless engines. This paper presents InterceptFuzz, a middleware that enables stateful fuzzing of single-process targets on top of an unmodified stateless fuzzing engine. InterceptFuzz requires only a hook where the target passes packets between nodes. Through this hook, it records benign traffic and injects fuzzed packets. It organizes the observed packet sequences in a Prefix Tree. Each seed carries a State ID that selects a node of this tree, and InterceptFuzz deterministically replays the recorded prefix before delivering the mutated packet. The tree grows with newly discovered sequences, while redundant states are pruned to keep its growth in check. InterceptFuzz powered by AFL++ is evaluated on the Nexus test framework of OpenThread and on the LTE and Wi-Fi models of ns-3, against an interception-based adaptation of AFLNet and against Concat, an AFL++-based baseline that mutates a whole message sequence as one input. On OpenThread and ns-3 Wi-Fi, InterceptFuzz covers significantly more branches than both baselines. Seven previously unknown crash signatures were found in OpenThread. Concat, despite its simplicity, covers more branches than AFLNet in every campaign on OpenThread and ns-3 Wi-Fi, and on OpenThread it exposes the same crash signatures as InterceptFuzz, although some of them in fewer campaigns.

---


### 7. [Physics-Informed Functional Tucker Method with RKHS Factors for Sparse Spatiotemporal Reconstruction](https://arxiv.org/abs/2611.03717)

**<font color=#1a73e8>作者：</font>** Zhengyang Liu, Jianguo Huang, Junxi Hu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing physical dynamics from fixed sparse sensors and missing frames is a fundamental challenge in scientific research. Sparsity leaves large regions of the field unconstrained, making the inverse problem ill-posed: a model may fit the observed sensors while producing inaccurate off-sensor structures or unreliable predictions between support frames. To this end, we propose PhysFTM---a physics-informed functional Tucker model that parameterizes the Tucker mode factors in reproducing kernel Hilbert spaces (RKHSs) and incorporates PDE constraints through finite-difference residuals evaluated at off-sensor collocation points. These residuals provide additional physical information in regions without direct observational supervision. PhysFTM first reconstructs continuous spatial fields at support frames via an alternating minimization scheme, optimizing the Tucker core tensor and the RKHS-based factors separately. To enable missing-frame reconstruction, PhysFTM constructs a continuous trajectory in Tucker-core space, which is decoded by the learned spatial RKHS-FTM representation to recover the full spatiotemporal field. Experiments on Allen--Cahn, Navier--Stokes, three-dimensional Heat equations, and a three-dimensional gridded Copernicus ocean reanalysis demonstrate accurate 2D/3D reconstruction under two missing-frame protocols. Code is available at this https URL.

---


### 8. [Auditing a Model-Hub Benchmark: Data Quality, Training Budgets, and Side Information in HuggingBench](https://arxiv.org/abs/2611.03727)

**<font color=#1a73e8>作者：</font>** Michal Podstawski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Benchmarks built from model hubs combine interaction data, knowledge graphs (KGs) and resource documentation, but valid files do not ensure that these artifacts describe the same objects. Treating the release as a data product, we audit HuggingBench (SIGIR 2025), a benchmark for recommending Hugging Face resources, through data validation, a replication of its eleven recommendation methods and controlled experiments with three training seeds. In three of its four external KGs, the files pass key and range checks but violate the item-entity identity constraint on which KG recommenders rely. Correcting this join improves every KG-based method in every seed, by up to 73% in mean Recall@10, and consistently reverses ten of 27 comparisons between KG configurations. The protocol matters as well: the 100-epoch budget ends before early stopping in seven to eight of 29 validation-selected settings, and 21 of 23 such setting-seed pairs improve with a longer budget. The released item text, which no reported method uses, is the strongest signal: closed-form linear models with text and the item graph exceed the best reported Recall@10 by 18% while fitting in minutes on a CPU. Checks of other recommendation releases show that individually valid releases of one dataset can use incompatible identifiers. We release corrected files, mappings, validators and logs, and derive practices for preserving identity and provenance across the artifacts of benchmarks and model lakes.

---


### 9. [Minimal Superior Penalties: Characterising and Calibrating Decision-Aware Proper Scoring Rules](https://arxiv.org/abs/2611.03734)

**<font color=#1a73e8>作者：</font>** Rouhollah Ahmadian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training a classifier means letting a validation metric decide which model is kept and when training stops. A natural requirement on that metric is superiority: every correctly classified forecast should score better than every incorrectly classified one, however close the underlying probabilities are. Neither the Brier score nor the logarithmic score satisfies this on its own. We show that superiority is governed by the separation between two endpoints -- the supremum of the score on correct predictions and the infimum on incorrect predictions -- and derive both in closed form for each score. Their difference is the infimal penalty, the greatest lower bound on the penalty needed to restore superiority. Prior work restores superiority with a penalty calibrated from the first endpoint alone; for the Brier base, our infimal penalty is smaller than that published penalty by a factor ranging from 4.00 at three classes to 2.11 at twenty. We further embed the published and infimal penalties in a one-parameter family and show that, under a single-valued tie convention, every member of the family is strictly proper. In a pre-specified two-dataset case study, mean selected-model macro-F1 rises with the penalty in the reported ten-class regimes, though not distinguishably from noise once seed/selection-mode nesting is accounted for; a fifth regime at forty-seven classes does not reproduce even this descriptive pattern. The intended no-superiority baseline is algebraically a rescaling of the family under test, so the experiment cannot attribute the observed pattern specifically to superiority. When superiority itself is the objective, any penalty strictly above the infimal value suffices; choosing a larger penalty is a separate calibration trade-off rather than a requirement for the guarantee.

---


### 10. [SSPE: Robust Sequential Staypoint Extraction in Degraded Trajectory Data](https://arxiv.org/abs/2611.03737)

**<font color=#1a73e8>作者：</font>** Yueyang Liu, Lance Kennedy, Andreas Züfle  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extracting semantically meaningful staypoints from raw trajectory streams is a foundational prerequisite for mobility analytics. However, real-world trajectory data is frequently degraded by severe spatial noise and protracted temporal dropouts. Classic threshold-based extraction methods, such as the widely adopted sliding-window algorithm, are highly sensitive to these anomalies, routinely fracturing continuous stationary episodes into disjointed fragments. To overcome this limitation, we propose the Sequential Staypoint Extraction (SSPE) algorithm. SSPE employs a resilient, state-driven architecture that replaces static spatial anchors with a dynamic centroid and introduces an $n$-step lookahead heuristic to structurally tolerate transient coordinate drift. Concurrently, it utilizes temporal bridging mechanisms to prevent artificial fragmentation during prolonged signal loss. Since optimal extraction parameters vary significantly across datasets, we further introduce a fully unsupervised, consensus-based parameter estimation framework. This framework derives baseline statistical scales directly from the raw trajectory data and identifies the optimal parameter configuration by maximizing structural agreement, thereby eliminating the reliance on annotated ground truth. We evaluate SSPE on the ExtraSensory dataset, a real-world mobility corpus with manually verified ground-truth staypoints, against the sliding-window implementation of Trackintel, one of the most widely adopted extraction baselines in the field. Empirical results demonstrate that SSPE achieves superior accuracy, yielding higher F1-scores while simultaneously improving computational efficiency over this standard.

---


### 11. [RATSIFT: Resolution-Adaptive Transformer for Solar Irradiance Forecasting and Temporal Downscaling](https://arxiv.org/abs/2611.03738)

**<font color=#1a73e8>作者：</font>** Jesto Peter, Timothy M. Hansen, Hossein Moradi Rekabdarkolaee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate forecasting and temporal downscaling of solar irradiance is critical for reliable renewable energy integration and grid management. Traditional methods often struggle to capture rapid irradiance variability. In this work, we develop a Transformer-based architecture for simultaneous forecasting and temporal downscaling. The model takes input data at arbitrary resolutions and generates outputs at any resolutions represented within the training data, leveraging both global and local contextual information. To improve training efficiency, a genetic algorithm-based optimization framework is implemented to identify suitable model hyperparameters, while reducing the computational cost of exhaustive grid search. The effectiveness of the proposed model is shown by analyzing real data in Dallas, Texas. The proposed model achieved root mean square error (RMSE) values of 28.785, 29.544, 30.157, 32.132~W/m\(^2\) for 15-, 30-, 60-minute, and irregularly spaced global input and producing forecast at 5-minutes resolution, respectively. Furthermore, this model produced reliable uncertainty estimates, exhibiting wider prediction intervals for high-resolution inputs during volatile solar conditions, whereas coarser-resolution inputs result in narrower intervals and significantly lower training time and computational cost. Our approach provides a scalable and efficient framework for multi-resolution solar irradiance forecasting and temporal downscaling, suitable for practical energy forecasting and grid management applications.

---


### 12. [Reasoning is topologically simple](https://arxiv.org/abs/2611.03739)

**<font color=#1a73e8>作者：</font>** Chris Kapulkin, Nathan Kershaw  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We formulate and investigate the hypothesis that reasoning text has simpler co-occurrence topology than non-reasoning text, and that higher-quality reasoning has simpler co-occurrence topology than lower-quality reasoning. We discuss and test applications to AI safety and AI evaluation.

---


### 13. [Beyond Proposals: Region-Consistent Open-Set Object Detection](https://arxiv.org/abs/2611.03741)

**<font color=#1a73e8>作者：</font>** Jiehui Tang, Yunlong Yu, Zhao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-set object detection (OSOD) suffers from a fundamental limitation under dense proposal mechanisms: highly overlapping proposals associated with the same object are often assigned contradictory known/unknown predictions. Existing methods perform open-set reasoning independently for each proposal, while ignoring the shared semantics among correlated proposals, resulting in fragmented detections and unstable open-set decisions. In this paper, we reformulate OSOD as an object-centric semantic inference problem, where correlated proposals jointly support a coherent region-level semantic decision. Based on this perspective, we propose OCSI-Net, a unified framework that combines object-centric semantic consistency with geometry-aware uncertainty stabilization. Specifically, OCSI-Net aggregates correlated proposals into structured region clusters and infers region-level semantics from aggregated semantic evidence, thereby enforcing coherent open-set predictions within the same object region. Furthermore, a geometry-aware uncertainty mechanism is introduced to stabilize optimization near open-set transition boundaries. Extensive experiments on multiple benchmarks demonstrate that OCSI-Net consistently achieves state-of-the-art performance, improving the harmonic mean of known and unknown detection by an average of 6.83\% over the second-best method.

---


### 14. [Fixed Detectors, Moving Code: How Well Do Static Security Analyzers Hold Up over a Decade of C/C++ Evolution?](https://arxiv.org/abs/2611.03742)

**<font color=#1a73e8>作者：</font>** Junhua Tang, Zhengsong Zhang. Haipeng Cai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Static application security testing (SAST) tools are often deployed on the assumption that detectors configured today will remain effective on future code, including previously unknown vulnerabilities. We test this assumption using 20,000 vulnerable and fixed C/C++ cases from 1,116 open-source projects (2016-2025), evaluated with three CodeQL releases, three Infer releases, and one Semgrep configuration. To distinguish temporal effects from shifts in code composition, we compare yearly populations, project- and label-matched year pairs, and within-project trajectories. We investigate the largest within-project declines through repair diffs, detection predicates, alert locations, and execution logs, while accounting for failed, degraded, and costly analyses. Under changed-file case-label scoring, overall F1 ranges from 0.066 to 0.478, but count-based AUROC stays near chance (0.495-0.526). Newer CodeQL releases attain higher F1 alongside nearly parallel rises in recall and false-positive rate, not stronger separation of vulnerable from fixed cases. In project-matched year pairs, CodeQL R2024 has negative mean later-minus-earlier F1 at every source-year gap, whereas Infer v1.1 and v1.3 have positive means throughout. Among selected drops, only 6 of 39 CodeQL and 2 of 620 Infer findings overlap a changed repair line. For Semgrep, 78.96% of cases show parser or timeout diagnostics even though every run reports success. These results suggest that apparent changes in temporal SAST effectiveness can arise from broader alerting, changing analysis coverage, and incidental findings, not solely from losses in vulnerability detection. Evaluations of temporal sustainability should fix detector conditions, control for projects, inspect repair-level evidence, and report failed or degraded analyses.

---


### 15. [CaRe-KT: Continuity-Aware Retrieval-Augmented Reasoning for Knowledge Tracing](https://arxiv.org/abs/2611.03744)

**<font color=#1a73e8>作者：</font>** Mehrnoush Mohammadi, Kamal Berahmand, Mohammad Morsali 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge tracing (KT) estimates learners' evolving knowledge states from interaction histories to support adaptive learning. Retrieval-augmented KT improves these estimates using cross-learner behavioral evidence, but existing approaches typically separate evidence retrieval from downstream prediction. This creates a retrieval-inference alignment gap because evidence relevance varies with the learner's evolving state and prediction context. We propose CaRe-KT, a query-adaptive framework that maintains relevance continuity between evidence acquisition and inference without equating retrieval relevance with predictive utility. CaRe-KT introduces an Evidence-Graph Cache (EGC) that combines persistent question-level relational compatibility with interaction-level temporal validity to construct query-specific evidence subgraphs. Historical learning trajectories retrieved through these subgraphs are encoded alongside the target learner's history in a shared representation space using outcome-supervised contrastive learning. An attention mechanism combines acquisition relevance with learned query-evidence compatibility, allowing relevance to inform, rather than determine, each trajectory's predictive influence. Experiments across five benchmarks show that CaRe-KT outperforms strong KT baselines and remains robust under sparse-history and cold-start conditions. These findings support relevance continuity as a design principle for retrieval-augmented knowledge tracing.

---


### 16. [LoRA-Patch: Defending Against Backdoored LoRA Adapters via Directional Steering](https://arxiv.org/abs/2611.03752)

**<font color=#1a73e8>作者：</font>** Shengyan Huo, Peihai Jiang, Xixiang Lyu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Third-party LoRA adapters introduce serious backdoor risks: malicious adapters can maintain normal task performance while embedding hidden, trigger-activated behaviors, making them difficult to detect through standard utility evaluations. Existing removal-based defenses typically sanitize backdoored models by updating, pruning, distilling, or mixing model parameters. However, these approaches are misaligned with adapter-based deployment, where the trusted base model is expected to remain frozen. In this work, we propose LoRA-Patch, a lightweight backdoor defense tailored to LoRA adapters. Our key insight is that backdoor injection distorts the directional geometry of a poisoned adapter relative to its trusted base model. Building on this insight, LoRA-Patch suppresses trigger-activated behaviors by realigning adapter directions through layer-wise steering, without modifying the base model weights. Extensive experiments across five backdoor attacks and three models show that LoRA-Patch effectively mitigates trigger-activated backdoors, outperforming existing baselines while preserving benign task performance. Moreover, LoRA-Patch is computationally efficient, constructing patches within 20 seconds across all evaluated models and adapters. Our code is publicly available at this https URL.

---


### 17. [The role of injected noise in diffusion model generalization](https://arxiv.org/abs/2611.03764)

**<font color=#1a73e8>作者：</font>** Vincent Emmerling, Felix Günther, David Kappel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models trained on distinct datasets can produce highly similar samples when prompted with the same noise input, suggesting that they learn a generalized data distribution. We investigate the role of noise injected during the sampling process, and show that it plays an important role in making or breaking this strong generalization effect. Based on this finding we investigate the robustness of sample similarity to changes in the injected noise, and find that its impact is largest in the sampling regime where broad structure already exists but the precise identity of the sample is not yet determined.

---


### 18. [FlowRig: Unified Skeleton Generation for 3D and 4D Meshes via Flow Matching](https://arxiv.org/abs/2611.03775)

**<font color=#1a73e8>作者：</font>** Fengzhi Guo, Nate Morrill, Shiqi Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic rigging is a fundamental task for both static 3D and dynamic 4D mesh animation, yet existing methods do not provide a unified feedforward solution for these two settings. While static 3D riggers achieve strong quality, they often provide limited control over bone count and become temporally unstable when applied frame by frame to dynamic meshes. Existing 4D methods, in contrast, typically rely on expensive per-sequence optimization. We propose MoTWorld, a template-free, data-efficient framework for unified 3D and 4D skeleton generation. Built on flow matching, MoTWorld generates temporally aligned skeletons for an entire sequence in a single feedforward pass, while naturally handling single-mesh 3D rigging. The model further supports explicit skeleton-count control, uncertainty estimation for candidate selection, and masking-based interpolation, forecasting, and backcasting. To address limited paired 4D rigging data, we adopt a curriculum that initializes from large-scale 3D rigging data and adapts to mid-scale 4D mesh-skeleton data. Experiments show that MoTWorld achieves strong static 3D rigging performance with controllable bone complexity, as well as high-quality and temporally consistent 4D reconstruction and prediction results.

---


### 19. [Proceedings of the CSCW 2026 Workshop on Women's Health as Cooperative Work: Participatory AI Across Care, Community, and Policy](https://arxiv.org/abs/2611.03776)

**<font color=#1a73e8>作者：</font>** Sherilyn Francis  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This submission indexes contributions to the CSCW 2026 workshop, "Women's Health as Cooperative Work: Participatory AI Across Care, Community, and Policy," held on October 11, 2026. The workshop examines women's health as cooperative work spanning patients, caregivers, clinicians, communities, institutions, and digital technologies. Contributions explore participatory AI, coordination breakdowns, the distribution of care labor, governance, decision-making authority, and accountability across care, community, and policy contexts.
The index provides paper titles, authors, affiliations, thematic areas, and unique report numbers to support discovery of the corresponding individual arXiv submissions.
The workshop proposal is separately published under DOI https://doi.org/10.1145/3785651.3818821.

---


### 20. [Probabilistic Steering of Generative Priors for Lab-in-the-Loop Antibody Optimization](https://arxiv.org/abs/2611.03844)

**<font color=#1a73e8>作者：</font>** Anisha Parsan, Sebastian Ober, Calvin McCarter 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Therapeutic antibody development is often framed as comprising two discrete stages: initial discovery of novel binders followed by iterative optimization to refine these hits into therapeutic-grade molecules. Models and methods often reflect these stages, with generative structure models applied to discovery and probabilistic black-box optimization methods applied to refinement. Here we propose to unify these stages by smoothly transitioning a generative discovery model into iterative optimization, allowing the handoff between the structure-based prior and supervision from wet lab data to be guided by the posterior uncertainty of a probabilistic surrogate. We show that this yields improvements in optimization efficiency in the low-N regime, as well as improved diversity amongst the optimized molecules.

---


### 21. [LaplaceDiag: Fault Diagnosis through Changes in Learned Actuator Effects](https://arxiv.org/abs/2611.03849)

**<font color=#1a73e8>作者：</font>** Oliver Niggemann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Identifying faulty components from sensor anomalies is difficult because fault effects can propagate through a plant and different faults can produce similar observations. Detailed component models and labeled fault examples may also be unavailable. We introduce LaplaceDiag, a data-driven method that uses changes in actuator effects to narrow the search for faulty equipment. Actuators act on specific devices and mechanisms, so their changed effects can provide clues to root causes. LaplaceDiag learns a healthy plant model with LaplaceNet, a neural network that operates in Laplace space. It separates nonlinear prediction based on measured history from an explicit matrix that describes how actuator values affect sensor values. Keeping the history predictor fixed allows current actuator effects to be estimated by linear regression without retraining the neural network. Comparison with a healthy reference accounts for estimation uncertainty and normal variation to detect changes and generate actuator-related diagnostic hypotheses. The method supports online and offline diagnosis, providing an intermediate step between anomaly detection and identifying faulty components. We successfully evaluate LaplaceDiag on two datasets.

---


### 22. [Predictive gains, causal losses: why interventional competence cannot be learned from data alone](https://arxiv.org/abs/2611.03861)

**<font color=#1a73e8>作者：</font>** Marcus Thomas  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retaining predictive gains can require persistent errors in a model's response to interventions. For deterministic predictors with finite second moments under squared-error loss, any observational advantage over the best predictor using only an outcome's direct causes requires dependence on other inputs, regardless of the learning rule. When admissible interventions vary inputs while preserving the worldly outcome, this dependence yields a positive lower bound on root-mean-square intervention-response error. We identify conditions under which population gradient updates introduce this dependence from a parent-only baseline or damage a previously correct mechanism through shared parameters while improving other predictions. These dependencies can also make model behavior vary with how the same intervention is realized. We characterize interventional alignment through a common output mapping across internal states and physical processes realizing the same intervention target and relevant context. Correction is limited by the causal hypotheses currently admitted within inquiry. The relevant hypothesis class comprises these causal alternatives, rather than the function class the computational system could in principle represent. For predictions restricted to these alternatives, interventional mean error cannot fall below the best approximation they permit, whether evidence is observational or interventional. Reducing error below a positive limit requires admitting better hypotheses, which may entail revising the causal variables, mechanism structure, or intervention interpretation. Interventional criticism constrains replacements without determining them. We conjecture that reliably acquiring and maintaining interventional competence when causal commitments fail requires autonomous participation in proposing alternatives, testing their consequences, and revising them in response to error.

---


### 23. [ExaTune: Exhaustive Hyperparameter Landscape Exploration at Scale](https://arxiv.org/abs/2611.03867)

**<font color=#1a73e8>作者：</font>** Kevin Dick, Katie Lonsway  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperparameter optimization (HPO) returns a single optimal configuration, systematically discarding the explored performance landscape that encodes how results depend on configuration choices. Fitness landscape analysis comprises a robust collection of methods from evolutionary computation offering ruggedness indices, autocorrelation functions, and fitness-distance correlation that have never been applied to machine learning hyperparameter spaces at scale, given that fine-grained ground-truth enumeration data has not existed. We present ExaTune, an open-source HPC system to produce a new artifact class: the hyperparameter landscape map. ExaTune exhaustively evaluates every point on a discretized hyperparameter grid via $K$-fold cross-validation, aggregates results into reproducible parquet benchmarks, and applies a suite of five formalized landscape metrics: spatial autocorrelation (Moran's $I$), ruggedness, local optima density, fitness-distance correlation (FDC), and variance-based parameter importance. We release a benchmark collection of 8 complete landscape maps (totalling 285,080 exhaustively evaluated configurations) spanning five model families (SVMs, random forests, XGBoost, ridge regression, and $k$-nearest neighbors) across six classification and two regression benchmarks, hosted on HuggingFace. Empirical analysis demonstrates that Bayesian optimization, Optuna, Hyperband, and Random Search at standard trial budgets systematically miss instability regions, secondary optima, and parameter interaction effects that are visible in complete landscapes; information that is structurally unavailable to any optimizer by design.

---


### 24. [The Information Limits of Neural Controlled Differential Equations Under Sparse Observations](https://arxiv.org/abs/2611.03887)

**<font color=#1a73e8>作者：</font>** Rostislav Gusev, Evgenia Romanenkova, Alexey Zaytsev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural controlled differential equations (Neural CDEs) evolve hidden states along continuous paths constructed by interpolating discrete observations. Sparse measurements leave the input between observation times undetermined, and admissible continuous paths consistent with the same data can produce different terminal states. We characterize this ambiguity for planar drivers with bounded speed. The set of compatible terminal states admits a leading-order zonotopic approximation determined by feasible signed areas and transported Lie brackets. Its projection onto a scalar prediction yields a computable, target-specific ambiguity certificate. We also study the number of measurements needed to reduce the remaining uncertainty. For nondegenerate planar CDEs, the optimal worst-case radius over deterministic adaptive sampling policies scales as $N^{-1}$ when speed is bounded and $N^{-2}$ when both speed and acceleration are bounded, where $N$ is the number of observation intervals. Synthetic experiments assess the certificate using admissible continuous completions and examine the role of path regularity.

---


### 25. [When Latent Dynamics Meet Data Assimilation: A Benchmark of Koopman-Type Representations](https://arxiv.org/abs/2611.03916)

**<font color=#1a73e8>作者：</font>** Zhiwei Zhang, Wenxuan Yuan, Xiaoyuan Cheng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Koopman representations describe nonlinear dynamics through linear evolution in a transformed space, offering an attractive framework for their linear simplicity and generality. Yet these advantages do not necessarily translate into improved performance in deep latent data assimilation (LDA). We systematically compare seven representative methods and structural baselines across five systems spanning approximately periodic to strongly chaotic dynamics and a broad range of state dimensions. We evaluate forecast and assimilation accuracy, physical state recovery, latent-trajectory behavior, and dynamical consistency, and assess Gaussian error assumptions, objective convexity, and uniqueness of analysis solutions. Our results reveal a trade-off between representational flexibility and optimization tractability. Linear evolution of the latent state can stabilize short-term forecasts but restrict expressiveness in strongly chaotic and high-dimensional systems, without consistently improving assimilation accuracy. Parameterized linear operators offer greater flexibility, yet their joint optimization with the encoder--decoder remains nonconvex. Methods with closed-form analysis updates generally perform better and exhibit greater robustness in our experiments, although matrix inversion remains a computational bottleneck. These findings show that the practical benefits of Koopman structure depend on both sufficient observational information and the choice of assimilation procedure.

---


### 26. [Sequential auditing of connected forecast errors under partial observations](https://arxiv.org/abs/2611.03928)

**<font color=#1a73e8>作者：</font>** Yuanbo Zhou, Junjie Xiong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph forecasting systems often rely on prediction intervals to quantify uncertainty across connected locations, but the true outcomes needed for evaluation may be only partially observed. We study how an auditor can selectively retrieve missing outcomes to determine whether there exists a connected group whose outcomes violate the same side of their respective forecast intervals. The audit stops when the observed labels determine the event or the query budget is exhausted. On three public graph time series, MOMS reduces mean queries by 19.6% to 38.5% relative to screened random acquisition when 30% of labels are hidden. Under localized masking on METR-LA, shortest witness finds more positive cases within ten queries, although the difference depends on node ordering. Direct component traversal reproduces all 9,696 screened random traces without enumerating connected subsets. The experiments show that reducing queries to a decision does not necessarily improve early event discovery or reduce local computation.

---


### 27. [Accelerating FastDEC Clustering Algorithm with GPUs](https://arxiv.org/abs/2611.03934)

**<font color=#1a73e8>作者：</font>** Mi Li, Eibe Frank, Bernhard Pfahringer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fast Dominance Estimation Clustering (FastDEC) is an efficient variant of Density Peak Clustering (DPC) that achieves high clustering quality through dominance-based density estimation, but remains constrained by the computational cost of exact k-nearest-neighbor (k-NN) construction and dominance component (DC) processing. We present SymWarp-FastDEC, a GPU-accelerated implementation of FastDEC. At its core is SymTrikNN, an exact self-k-NN kernel that exploits search symmetry using upper-triangular traversal and warp-cooperative top-k selection. We also introduce WP-DC, a warp-parallel DC reduction algorithm designed for modern GPUs. Combined with memory-adaptive execution planning and stream scheduling, WP-DC eliminates DC reduction as a runtime bottleneck. Experiments on synthetic and real-world datasets show that SymWarp-FastDEC produces clustering outputs identical to the original FastDEC on all evaluated equivalence benchmarks. Compared with a FastDEC variant using FAISS GpuIndexFlatL2 for exact k-NN search, our approach achieves approximately 1.7x to 4.9x higher end-to-end performance, with the advantage generally increasing with dimensionality. Compared with the original single-threaded Python FastDEC implementation, speedups reach approximately 2.5 x 10^4 in a very high-dimensional case where its k-d-tree-based search degrades; this extreme result is not representative of typical acceleration.

---


### 28. [Geometric Refinement and Distributional Alignment for Sim2Real Roadside LiDAR Detection](https://arxiv.org/abs/2611.03936)

**<font color=#1a73e8>作者：</font>** Aman Upganlawar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We describe our approach to the LUMPI track of the UrbanTwin Sim2Real LiDAR Challenge, in which a 3D object detector must be trained exclusively on synthetic data and evaluated on unseen real roadside LiDAR, while the synthetic point clouds are simultaneously scored for distributional realism. Our final entry scores 0.4793 combined, from a detection mAP of 0.1333 and a realism score of 0.9126. Our contribution is not a new architecture. Working from a PointPillars baseline, we obtained most of our gains from three sources. First, a diagnosis that small object failure in roadside LiDAR is a localisation problem rather than a detection problem, which led to a parameter free geometric refinement worth 86 percent relative on pedestrian AP. Second, an audit of our own post processing which revealed that a shipped rule was destroying valid predictions, the repair of which produced our single largest detection gain at 335 percent relative on the Van class. Third, treating the realism metrics analytically rather than as a black box, which showed that one of the four components is a closed form function of nine summary statistics. We also report an experimental methodology that we believe is the more transferable result. Because mean AP decomposes into independent per class terms, a single submission can carry several mutually controlled experiments, and a submission assembled entirely from previously measured components has a score that is known before it is sent. We predicted our final score to four decimal places prior to submission. We report negative results at equal length, and give a full account of data provenance and compliance in Section 8, including a full account of every mechanism contributing to the submitted score.

---


### 29. [Coordinate Frame Recovery, Per Class NMS and Null Return Modelling for Sim2Real V2X LiDAR Detection](https://arxiv.org/abs/2611.03940)

**<font color=#1a73e8>作者：</font>** Aman Upganlawar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We describe our approach to the V2X-Real track of the UrbanTwin Sim2Real LiDAR Challenge, in which a 3D object detector must be trained exclusively on synthetic data and evaluated on unseen real roadside LiDAR from an Ouster OS1-64 unit, while the synthetic point clouds are simultaneously scored for distributional realism. Our final entry scores 0.7457 combined, from a detection mAP of 0.4382 and a realism score of 0.9251. Three findings account for most of our result, and all three were diagnostic rather than architectural. First, a coordinate frame mismatch between our predictions and the evaluation ground truth was suppressing detection AP entirely; recovering it took our score from 0.3520 to 0.5147 in a single submission. Second, a single global non maximum suppression threshold was destroying genuine pedestrian detections, because pedestrians occur in groups and a 0.3 IoU threshold applied to a 0.7 m box suppresses distinct neighbouring people; correcting this per class raised overall mAP from 0.0751 to 0.4295. Third, approximately 31 percent of the real reference point cloud consists of null returns encoded as the literal point (0, 0, 0), a format feature entirely absent from our synthetic clouds, which pinned Earth Mover's Distance near its floor until we modelled it. Negative results are reported at equal length, and Section 9 gives a full account of data provenance and compliance. That section also accounts for every mechanism contributing to the submitted score.

---


### 30. [Camera Radar LiDAR Fusion via Point-Cloud Projection for Multi-Task Learning](https://arxiv.org/abs/2611.03942)

**<font color=#1a73e8>作者：</font>** Kavin Chandrasekaran, Sorin Grigorescu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles require robust perception systems to operate safely under diverse environmental conditions. While cameras provide high-resolution visual data, their performance significantly degrades in low-light and adverse weather. High Definition (HD) radar offers superior reliability and angular resolution under such conditions but lacks rich visual feature recognition. LiDAR, though expensive, delivers highly precise distance measurements and dense point clouds. Each sensor exhibits unique trade-offs, necessitating the development of advanced sensor fusion algorithms to harness complementary strengths while minimizing computational complexity and maintaining accuracy. In this study, the proposed fusion architecture performs early fusion by combining camera images with perspective-view point cloud data from HD radar and LiDAR sensors. The proposed model is trained to detect vehicles and segment free drivable space simultaneously. Experiments are performed on the RADIal dataset where we demonstrate that fusing point cloud data with camera images in front-view surpasses the performances of the most recent standalone and fusion models.

---


### 31. [Do We Still Need Rotation-Invariant Architectures? A Statistical Robustness Benchmark for Point Cloud Classification](https://arxiv.org/abs/2611.03952)

**<font color=#1a73e8>作者：</font>** Abdulla Nasir Chowdhury, Gulpi Qorik Oktagalu Pratamasunu, Kazuhiro Fukui  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A substantial line of work builds rotation invariance directly into point cloud architectures. We benchmark 10 architectures (PointNet, PointNet++, DGCNN, RIConv, RIConv++, RISurConv, PointMLP, PointTransformer, and the equivariant VN-PointNet and VN-DGCNN) across 5 domains under pose, noise, and occlusion, and analyze the results with confirmatory hypothesis tests rather than point estimates. The three rotation-invariant (RI) architectures achieve the best pose robustness but rank among the lowest on noise robustness in 4 of 5 domains. We ask whether this cost is intrinsic to invariance or specific to how invariance is obtained. We retrain all 10 architectures unchanged, with a simple invariance loss on the embedding and three training seeds each, and evaluate all models on the independently designed ModelNet40-C. Invariance training transfers narrowly but reliably. It improves exactly the corruption families its perturbations target wherever the baseline has headroom (mean occlusion +10.5, lidar +13.4 percentage points of accuracy). At matched training budget the best standard backbone and the best RI architecture end on par on unseen corruptions (within 2.5 percentage points in every seed), and invariance-trained RIConv++ is the most seed-stable top model. Once rotation augmentation is widened, standard backbones concede only a flat, angle-independent accuracy offset under full-sphere rotation. We release the benchmark along with a package for analyzing point cloud robustness and reproducing our results.

---


### 32. [Sampling Interventional Distributions with Orthogonal MMD Flow](https://arxiv.org/abs/2611.03962)

**<font color=#1a73e8>作者：</font>** Bariscan Bozkurt, Hugh Dance, Zonghao Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many causal inference problems require sampling from interventional outcome distributions rather than estimating low-dimensional summaries. Existing approaches often rely on fitting generative models of the target distribution together with additional nuisance components, which can be computationally demanding for high-dimensional outcomes. We propose Interventional Maximum Mean Discrepancy Flow (IMMD-Flow), a particle-based method that instead represents the target interventional distribution through its kernel mean embedding. This kernel embedding admits a doubly robust, Neyman-orthogonal estimator with finite-sample guarantees and can be efficiently reused to sample from the interventional distribution via MMD gradient flow. IMMD-Flow accommodates both hard and soft interventions, admits theoretical guarantees for estimation and particle approximation, and extends to high-dimensional image outcomes through frozen encoders. Across image-based benchmarks, IMMD-Flow matches or improves upon state-of-the-art generative approaches while showing significant speed advantages.

---


### 33. [Ermakov--Based embeddings as a parameter-free layer for physics-informed neural networks](https://arxiv.org/abs/2611.03964)

**<font color=#1a73e8>作者：</font>** Roberto Bernal-Jaquez, Roberto Romero Huerta, Alexander Schaum  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evolution equations with time-dependent coefficients force a neural solver to spend capacity on a scale that the equation already determines. We show that a single classical object, the Ermakov-Pinney scale function $\rho$, can be written into the input layer of a physics-informed neural network as a parameter-free embedding. One construction covers three problem families through the two signs of the Pinney constant $c$: linear diffusion ($c=-1$, $\omega\equiv0$), diffusion in a time-dependent confining trap ($c=-1$, $\omega\neq0$), and the quantum oscillator with time-dependent frequency ($c=+1$). An exact moment identity gives $\rho$ in closed form from the initial data alone, so no auxiliary network or knowledge of the solution is needed. Our central finding is comparative: each family requires a different component of the construction and has a different honest control. In family I, the diffusive-time reparametrisation alone reproduces most of the gain, so that family is a poor test of the idea and shows why an ablation is mandatory. In family II no time reparametrisation exists, the control degrades accuracy, and the amplitude prefactor becomes essential (40.8x). In family III the adiabatic approximation also fails, and the quadratic phase factor is what matters (5.7x). The method does not help when the reduced solution does not converge to a fixed point: its extrapolation advantage then disappears. The reduction itself is the classical scaling-variable change of the self-similar-asymptotics literature; what is new is the moment identity that makes it architectural for time-dependent coefficients, and the comparative anatomy above.

---


### 34. [One Mistake, Three Layers: Persistence Rules Under Depth Correlation](https://arxiv.org/abs/2611.03968)

**<font color=#1a73e8>作者：</font>** Maryam Rahimimovassagh, Michael Brown, Sanjeda Sara Jennifer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probing frozen representations layer by layer is now standard practice, but reporting when a signal first becomes decodable requires a rule for reading a depth curve, and the obvious rule is wrong. On synthetic curves with known ground truth, requiring a probe score to exceed a null-calibrated threshold for three consecutive stages reports an onset nineteen stages early under transformer-like depth correlation, with every resample returning an onset. The failure follows from correlation between neighboring layers, a hazard known in neuroimaging but not, to our knowledge, checked for depth curves.
We give an estimator whose error rate is calibrated rather than assumed. Null trajectories are built by permuting labels within each evaluation unit and holding each permutation fixed across depth, preserving the correlation structure the rule must survive; thresholds are per-layer order statistics; and the persistence requirement is calibrated rather than chosen.
Applied to pocket information in a frozen co-folding trunk, stratifying 1,820 post-cutoff targets by protein-family and pocket familiarity, the five-stage rule fires on 4 to 7 per cent of null trajectories against a nominal 5 per cent and the three-stage rule on 12 to 17: the synthetic failure reproduces on real data. Pocket membership is decodable above threshold at all 48 blocks in all four regimes, so the onset cannot discriminate them; the pre-declared accumulation depth does, and is latest for familiar families with structurally novel pockets in every feature set. That regime is also the weakest, by a margin surviving controls for length, pocket measure and alignment depth.
Separately, a widely used public co-folding checkpoint loads against its own code with 128 trunk parameters missing; those would be randomly initialized, and every representation extracted would be partly noise while appearing normal.

---


### 35. [Must AI Spell It Out? Pragmatic Comprehension of Alerts in a Time-Critical Task](https://arxiv.org/abs/2611.03976)

**<font color=#1a73e8>作者：</font>** Anwesha Das, Vera Demberg, Anna Maria Feit  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Assistive systems typically tell users everything, often spending time and attention on what a user already knows, leaving less for what happens next. People, on the other hand, leave out what they expect the listener can supply. Can people use their prior knowledge to understand an incomplete message when the speaker is a machine though? We studied this pragmatic comprehension in a monitoring task controlling users' prior knowledge and the available time to detect critical situations. In a preregistered study (N=114), we compared a pragmatic planner that reasons over a model of the listener's knowledge to decide what to say, when, and how explicitly, with a baseline specifying problems fully in onset order. Participants resolved underspecified alerts almost as reliably as fully specified ones and sooner, detected more problems, and rated the pragmatic assistant helpful more often, with no increase in reported mental demand. Our findings show that people can recover what the system left implicit and that pragmatic communication can support effective assistance under the constraints of a changing world.

---


### 36. [Rapid Mean-Field Formation Transport with a Shared-Representation Neural Fokker-Planck Controller](https://arxiv.org/abs/2611.03981)

**<font color=#1a73e8>作者：</font>** Zejian Zhou, Hao Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper develops a mean-field formation transport method with low online computational cost for large-scale multi-agent systems. Classical mean-field planners often require repeated solutions of coupled forward and backward partial differential equations, making online replanning computationally demanding. Density and control are therefore approximated by a common parameterized nonlinear map with separate scalar density and vector control outputs. Parameters are optimized using Fokker--Planck and initial-condition residuals, formation-matching costs on numerically simulated closed-loop particle trajectories, and control effort. Numerical computations are restricted to a bounded region of the state space, with an additional penalty on probability flux across its boundary. For the periodic-domain model, we establish well-posedness of the induced density evolution and bound the density-approximation error in terms of the dynamics and initial-condition residuals. Parameter optimization precedes online operation, during which controller coefficients remain fixed. Experiments quantify the accuracy--runtime trade-off relative to a mean-field planner, show lower transport error than classical feedback baselines, and demonstrate the benefits of the common parameterization.

---


### 37. [Revisiting Elliptic++ for Bitcoin Forensics: Feature Reconstruction and Leakage-Resistant Evaluation](https://arxiv.org/abs/2611.04000)

**<font color=#1a73e8>作者：</font>** Runlin Liang, Simon Trimborn, Noud van Giersbergen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Elliptic and its address-level extension Elliptic++ are widely used benchmark datasets in Bitcoin forensics, cited by more than 1300 academic studies according to Google Scholar. We identify future information leakage in Elliptic++. Its positional data split does not respect temporal order, and the exact definitions of its address-level features remain undocumented. We revisit how the 55 Elliptic++ address-level features are computed and propose a leakage-resistant pipeline. First, the exact feature definitions are recovered by linking Elliptic transactions to public ledger data. Second, we compute the features with a temporal split based on each address's first appearance, using only information available at the time of prediction. Once temporal ordering is enforced, the random forest (RF)'s strong predictive performance largely disappears: its F1 score on the illicit class falls from $0.846$ under the original leaky evaluation to just $0.291$ under our leakage-resistant pipeline. Furthermore, RF no longer outperforms a simple logistic regression baseline. We provide the exact feature definitions and executable code to reproduce the leakage-resistant features, so that future Bitcoin forensic models can be evaluated based on genuine predictive capability rather than temporal data leakage.

---


### 38. [Physics-Informed Identification of Tensegrity Prestress across Taut-Slack Transitions](https://arxiv.org/abs/2611.04007)

**<font color=#1a73e8>作者：</font>** Sandesh Lamsal, Sumit Kumar, Rubi Bhandari 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prestress governs the stability, stiffness, and dynamic behavior of tensegrity structures, but it is not directly observable from sparse structural measurements, and it may decrease during service life. Under strong excitation, the cables may slacken and the dynamics become nonsmooth. Existing identification methods are limited to the taut regime, and physics-informed networks for tensegrities solve only the forward problem of predicting the response from known member parameters. This study formulates the inverse problem. Neural networks are trained on the equation-of-motion residual in constrained Cartesian coordinates, where the mass matrix is constant and the force densities enter linearly. The force densities, damping, and axial stiffness are trainable parameters, and the tension-only cable law is kept. A Fisher-information analysis shows, before inversion, which member parameters a record can determine. The method is tested on simulated planar tensegrity frames with up to five modules and a three-dimensional prism, and on measured records of a biomimetic leg and a full-scale tensegrity simplex. On the one-module frame, the identifiable force densities are recovered within 1.5% from noisy accelerations at half the free coordinates, on records with and without taut-slack transitions. Records with transitions determine members that taut records leave undetermined. On the five-module frame, a 16-cable two-span bridge, the median force-density error rises moderately, to 4.2%. On measured records, an identified spring stiffness is within 0.1% of its independently measured value on average, and the identified simplex prestress at 13 levels agrees with its cable force transducers to 2.9% root-mean-square.

---


### 39. [Compression Forcing: Hierarchical History Tokenization Enables Flexible World Models](https://arxiv.org/abs/2611.04028)

**<font color=#1a73e8>作者：</font>** Siqiao Huang, Partha Kaushik, Michael Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Effective world modeling requires compressing salient history information that facilitates future prediction. However, most existing approaches inherit tokenization and conditioning mechanisms from video generation, where objectives are centered around perceptual realism rather than predictive utility. This discrepancy limits the world model's effectiveness, especially in environments dominated by visual nuisances or task-irrelevant background details. To this end, we introduce Compression Forcing (CF), a general framework that aligns history compression with the predictive objective of world modeling. Compression Forcing features Dynamics-Aware Tokenization (DAT), a novel tokenization method that compresses history observations into a sequence ordered by decreasing dynamics saliency. Built on a diffusion backbone, this structure enables Hierarchical History Guidance (HG-H), allowing selective amplification of dynamics-salient information during inference. Extensive experiments across various environments demonstrate improved prediction fidelity, physical realism, and downstream decision-making performance, establishing Compression Forcing as a highly flexible and effective approach for world modeling.

---


### 40. [Do Pretrained Backbones Transfer to Physical Sensors? A Systematic Study of Multimodal Initialization Across the Sensor Stack](https://arxiv.org/abs/2611.04034)

**<font color=#1a73e8>作者：</font>** Fabio Montello, Ronja Güldenring, Lucas Mogensen Sandby 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transfer learning from pretrained backbones has become standard practice in multi-sensor computer vision---yet two questions remain open: which pretrained weights transfer best to multi-sensor setups, and can in-domain pretraining outperform off-the-shelf solutions? Frameworks like MultiMAE demonstrate the utility of masked autoencoding in a multi-modal context, but rely entirely on dense, model-derived modalities. It is unclear how robustly these methods translate to real-world applications that use physical sensors, where the aggregation of diverse public datasets for large-scale pretraining inherently introduces modality sparsity. To investigate this systematically, we curate a multi-sensor autonomous driving collection of $2.82M$ images from 16 publicly available datasets, incorporating both physical hardware modalities (RGB, LWIR, NIR, Event) and model-derived modalities (Stereo Depth, Segmentation). We use this collection for in-domain pretraining based on the MultiMAE approach. We adapt MultiMAE's loss formulation to accommodate sparse samples, and study the effect of an enforced encoder bottleneck for modality alignment and of additional losses specific to dense reconstruction (SSIM and FFT). We then systematically compare against common pretrained backbones (ViT, MAE, DINO and MultiMAE) across downstream sensor fusion tasks. We find that MultiMAE is a surprisingly strong out-of-the-box baseline, transferring effectively even to modalities it has never seen, while our targeted modifications yield incremental but consistent improvements on multi-sensor transfer and overall robustness.

---


### 41. [Denoising Is Stein: Moment Access and a Resource Hierarchy for Learning Hidden Structure in Diffusion Models](https://arxiv.org/abs/2611.04043)

**<font color=#1a73e8>作者：</font>** Rui Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study score learning from denoising pairs when the data contain a hidden non-Gaussian component. If covariance reveals the component, its subspace can be recovered directly. If covariance is isotropic, the first distinguishing moment has order $k^\ast$, and the learner must extract that moment from clean points and their noisy views.
Correlations in the denoising loss are Stein discrepancies against a baseline; for polynomial fields they determine exactly the corresponding moment differences. Averaging fresh noisy views conditional on a clean point gives an exact moment query on the clean distribution. In the covariance-matched regime, orientation-independent dictionaries satisfying an $L^4/L^2$ condition need order $d^{k^\ast-1}$ features, and the stated dot-product kernel ridge models need the same power in samples. Small-step online SGD on one unit has this exponent up to logarithms. A two-stage learner uses the curvature of a smoothed denoising loss to recover the hidden direction, then sharpens it and fits a scalar readout. For every even $k^\ast$, it obtains a fixed score gain over the Gaussian baseline from $O(d^{k^\ast/2}\log d)$ clean points. In the covariance-visible regime, the frozen-feature threshold occurs at $d^J/J!$, while projection onto principal components makes the fitted-model, score-risk and generated-law distributions independent of ambient dimension.
In the covariance-matched experiments, the measured partial-trace overlaps are consistent with the proposed spectral transition. A width-8 network trained with clean-point reuse shows a $d^2$-like training-set threshold over $d=64$--$192$, with fixed validation and calibration overhead.

---


### 42. [On the (Quantum) Communication Complexity of Secure MPC from a Random Oracle](https://arxiv.org/abs/2611.04052)

**<font color=#1a73e8>作者：</font>** Alexander Hoover, Giuseppe Persiano, Kevin Yeo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Information-theoretic MPC among $n$ parties with $t$ corruptions can securely evaluate a circuit $C$ with $O(|C| \cdot t/(n-t))$ online communication in the preprocessing model and $O(|C| \cdot t/(n-2t))$ communication in the honest majority setting. Damgård, Larsen and Nielsen (CRYPTO 2019) showed that both communication bounds are tight for inner products. Fully homomorphic encryption and other assumptions known to imply public-key cryptography beat both communication bounds, but the communication complexity with symmetric-key cryptography alone is less understood. For MPC with preprocessing, we prove that the same $\Omega(|C| \cdot t/(n-t))$ lower bound holds in the random oracle model, so a random oracle cannot reduce the online communication. For honest majority MPC relative to a random oracle, we present an $\Omega(|C|)$ communication lower bound that is matched by a new construction for degree-2 polynomials (including inner products) when $n = O(\log \lambda)$, beating the information-theoretic bound.
We also study quantum MPC. First, we prove that information-theoretic protocols with quantum communication (and preprocessing) cannot reduce communication compared to their classical counterparts. Furthermore, we extend our lower bound for MPC with preprocessing to protocols with a quantum-accessible random oracle, but use only classical communication. In contrast, with both quantum communication and a post-quantum one-way function, we present a simple two-party protocol that evaluates the two-party instance of these circuits with $\mathrm{poly}(\lambda, \log |C|)$ communication, beating these lower bounds. Finally, such communication savings do not come for free. We prove that there exist circuits $C$ such that every blackbox protocol with $o(|C|)$ quantum communication must perform $\Omega(|C|)$ cryptographic operations.

---


### 43. [Spatial and Temporal Super-Resolution and Denoising of Intracardiac 4D Flow MRI](https://arxiv.org/abs/2611.04053)

**<font color=#1a73e8>作者：</font>** Yusuf A. Ozturk, Jie Zheng, Fanwei Kong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intracardiac flow is driven by complex, and time-varying cardiac motion and interaction with the heart valves, producing complex flow features that may provide valuable information for disease diagnosis and treatment planning. 4D Flow MRI enables non-invasive, time-resolved measurement of three-dimensional cardiovascular velocity fields. However, substantial noise and limited spatial and temporal resolution limit its ability to accurately resolve flow features. We propose 4D-MRAR (4D Magnetic Resonance Augmented Reconstruction), a deep learning (DL) method to super-resolve and denoise 4D Flow MRI data. Unlike prior DL methods that train and infer on static vascular regions, our method predicts intracardiac flow within hearts undergoing large deformation. Moreover, it uniquely allows for simultaneous super-resolution in 3D space and time. The method combines a residual convolutional neural network, a recurrent neural network, and an implicit neural field to predict high-resolution velocity and pressure fields while efficiently enforcing the governing equations of fluid flow during training. Trained on a synthetic dataset obtained from computational fluid dynamics (CFD) simulations of left ventricle (LV) flow, our method generalizes to synthetic whole-heart 4D flow MRI data, and demonstrated promising performance on real 4D Flow MRI. The produced super-resolved flow fields exhibit significantly improved accuracy and greater consistency with the governing equations of blood flow compared with prior methods.

---


### 44. [Forgetting to Improve: Principled Data Removal in Active Learning](https://arxiv.org/abs/2611.04054)

**<font color=#1a73e8>作者：</font>** Manuel Wendl, Erik Englesson, Andreas Krause 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The uncertainty of a statistical model is most commonly factorized into an aleatoric and an epistemic part. This factorization changes how predictions are interpreted in downstream decision tasks. Importantly, except for the idealistic scenario with no model mismatch, the quantification is a characteristic of the model and not the data generating process. In this paper, we propose Forgetting to Improve a method that reduces this discrepancy by incorporating the task into the modeling framework. Our key insight is to acknowledge that in scenarios of model mismatch, data can have a detrimental effect on the modeling for a specific task. Based on this insight, we propose an influence function for Gaussian process models that allows for principled removal of detrimental data samples. We showcase the flexibility of this approach by demonstrating significant improvements across a range of tasks, including Bayesian optimization, model-based reinforcement learning, and transductive learning.

---


### 45. [Structured Priors: Towards an algebra of component priors for prior-data fitted networks](https://arxiv.org/abs/2611.04056)

**<font color=#1a73e8>作者：</font>** Thomas Bartz-Beielstein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior-data fitted networks are typically trained using synthetic data generated by a single, manually constructed generator. In cases where such a generator combines multiple components, e.g., in TabPFN, Mitra, or TabICLv2, this is achieved through a mixture using manually specified weights, the impact of which on the network only becomes apparent after pre-training. Instead of such a hand-built generator, this work proposes a structured prior: a small set of named component priors, linked by operators whose algebraic properties are formally proven and whose influence on the trained network has been validated. Within a measure-theoretic framework, the operators of mixture, convolution, amplitude scaling, local transform, and projection are defined. Their governing laws are proven. These operators are implemented in the macl2l software package. Experiments demonstrate that the implemented generators reproduce the identities within the resolution of a permutation test. Furthermore, it is shown that trained networks obey the distributive law; that a mixed prior composed of small components performs as well as or better than any individual component in seven out of eight open regression benchmarks; and that on two of these tables a structured prior reaches, with a ninth of the data budget, an error that a generic random-function prior does not reach even with the full budget. A theorem on model averaging demonstrates that networks trained on individual components constitute the Bayes predictor for the mixture, provided that the component networks are themselves the Bayes predictors for their respective priors. However, the pre-registered test of this averaged predictor with trained component networks failed, because the networks identify the generating component too rarely. The paper proposes a research program focused on the algebra of structured priors for prior-data fitted networks.

---


### 46. [StreamLTT: Risk Certification for Policy Selection under Stream Dependence](https://arxiv.org/abs/2611.04062)

**<font color=#1a73e8>作者：</font>** Jinwen Xu, Qin Lu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learn-then-Test (LTT) provides a general framework for certifying deployment policies against a prescribed risk target, but its standard formulation targets a fixed population risk estimated from calibration losses. In sequential deployment, losses may instead be dependent and nonstationary, so the risk of a fixed policy can evolve with the observed history. We introduce StreamLTT, which replaces this fixed population risk with average predictable risk, defined by conditioning each decision's loss on the information available before its outcome is revealed. Conditional centering turns empirical deviations from this target into a martingale sum, enabling both a test that adapts to predictable variance and a finite-sample Hoeffding alternative. Combined with family-wise error rate control, StreamLTT yields a simultaneously certified policy region that supports subsequent deployment selection. Across seven forecasting datasets and seven deployment risks, StreamLTT places the certified frontier substantially closer to the prescribed risk target than IID, robust-variance, block-bootstrap, and concentration-based alternatives, while empirical family-wise error closely follows the prescribed level. A finite-sample ablation further shows that the predictable-risk formulation drives the tighter risk frontier, while adaptation to predictable variance makes more effective use of the available family-wise error budget. StreamLTT therefore extends risk-certified policy selection to dependent deployment streams by addressing both what risk should be certified and how it should be tested.

---


### 47. [TB-Transolver: Parallelized and Coherent Long-Horizon Rollouts via Temporal Bundling for Time-Dependent PDEs](https://arxiv.org/abs/2611.04063)

**<font color=#1a73e8>作者：</font>** Sidharth S. Menon, Ameya D. Jagtap  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transolver has recently gained widespread adoption for solving diverse physical problems on unstructured geometric meshes by leveraging its Physics-Attention mechanism, which seamlessly extends standard softmax attention to handle physical domains at scale. For time-dependent problems, existing literature relies on time-conditioned or autoregressive rollouts to preserve temporal causality while retaining Physics-Attention as the spatial backbone. However, a fundamental limitation of this formulation is its sequential execution model, wherein computational costs scale linearly with the temporal horizon, rendering standard Transolver inefficient for transient problems despite its exceptional spatial efficacy. This bottleneck has historically hindered its broader application in time-dependent physical modeling. To address this limitation, we introduce TB-Transolver (also referred to as Temporally Bundled Transolver), an efficient framework built on temporal bundling that scales Transolver for time-dependent PDEs. Furthermore, we propose \emph{spatiotemporal coherence} (${\rm C(K)}$) as a general metric to systematically quantify snapshot correlation within a temporal bundle, enabling the \emph{a priori} selection of optimal bundle widths using training data alone, thereby avoiding expensive grid searches. We demonstrate the computational efficacy of TB-Transolver across four physically distinct domains, namely, plasticity, fluid dynamics, reaction-diffusion, and global weather forecasting; achieving training speedups of up to $29\times$ over conventional autoregressive and time-conditioned baselines. Finally, these computational gains are further amplified through distributed multi-node and multi-GPU parallelism, yielding aggregated speedups of up to $45.6\times$ at optimal bundle widths for systems exhibiting high spatiotemporal coherence compared to single-GPU implementations.

---


### 48. [Graph-Localized Coverage for Conformal Prediction on Inductive Graphs](https://arxiv.org/abs/2611.04066)

**<font color=#1a73e8>作者：</font>** Jinwen Xu, Qin Lu, Georgios B. Giannakis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal prediction (CP) provides marginal coverage guarantees, but marginal coverage does not determine where prediction errors occur on a graph. Queries from different graph neighborhoods can exhibit substantially different levels of uncertainty even when aggregate coverage remains near its target. We introduce GLocalCP, an online CP framework for inductive node classification and edge prediction that combines marginal and graph-local calibration with uncertainty-adaptive prediction sets. Specifically, GLocalCP puts forth a novel uncertainty-adaptive nonconformality score that relies on the mutual information obtained from Monte-Carlo (MC) dropout based prediction. Then, it augments a global online threshold with a kernel-based local correction that propagates coverage feedback among similar graph queries. On the theoretical horizon, we establish pathwise $O(N^{-1/2})$ marginal calibration error without exchangeability or stationarity and, for the exact-kernel formulation, an explicit $O(N^{-1/2})$ graph-localized calibration guarantee. Experiments on seven node-classification and seven edge-prediction benchmarks show that similar marginal coverage can conceal substantially different local reliability. Our proposed GLocalCP maintains coverage near the target while consistently reducing graph-local calibration error. Uncertainty scaling in GLocalCP further reduces prediction-set size across all evaluated node and edge datasets while leaving marginal coverage essentially unchanged.

---


### 49. [Finite-Sample Convergence in Networked Average Reward MARL: Decentralization Pitfalls and Entropy Remedies](https://arxiv.org/abs/2611.04072)

**<font color=#1a73e8>作者：</font>** Yizhou Zhang, Yashaswini Murthy, Laixi Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the problem of average reward Multi-Agent Reinforcement Learning (MARL) where agents interact within a network. Each agent in the network conducts local updates with information within its $k$-hop neighborhood and collaboratively maximizes the overall reward of the entire network. We first provide impossibility results in achieving convergence to the global optimal joint policies in our setting. These impossibility results highlight the challenges of decentralized learning with local information in multi-agent systems, namely the issues of multiagency, where each agent independently optimizes its policy, and partial observability, where agents have limited visibility into the global state. Given these challenges which indicate that decentralized policy optimization can generally be certified only up to stationarity, we provide finite-sample convergence guarantees for a decentralized actor-critic algorithm with linear function approximation that converges to an approximate stationary point with small gradient norm. To overcome such impossibility results, we further show that adding fixed-state entropy regularization reshapes the objective landscape which leads to even stronger global convergence guarantees for our proposed actor-critic algorithm.

---


### 50. [RAPID: Increasing Efficiency of Internal Distillation via Randomized Methods](https://arxiv.org/abs/2611.04081)

**<font color=#1a73e8>作者：</font>** Ryan Swift, Konstantinos Psounis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation is a technique used to transfer the expertise of large teacher models into small, efficient student models. Recent advances have integrated the distillation of internal activations, more directly training students to learn similar representations as the teacher. One of the core challenges of internal distillation is the dimensional incompatibility between the student and teacher internal representations. Existing methods add learnable matrices to project the larger teacher activations into the smaller representation space of the student. This is a notable point of inefficiency, as learning additional parameters for the projectors increases training costs, only for them to be discarded immediately after training. We introduce RAPID (RAndomized Projection for Internal Distillation) a novel distillation methodology which eliminates the wasteful projection learning by leveraging randomized methods. RAPID utilizes an efficient transform construction based on the Johnson-Lindenstrauss lemma to compress the teacher representations into the student embedding space with strong theoretical guarantees of structural preservation. RAPID also employs a combination of exponential moving average (EMA) and homoscedastic uncertainty weighting in a novel multi-objective function designed for internal distillation. Our experiments in post-training for reasoning demonstrate that RAPID increases training efficiency by as much as 21.1% while maintaining performance comparable to existing methods.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-280](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
