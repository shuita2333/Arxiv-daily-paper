# 📦 其他研究 | 2026年11月11日

> 本类共 **520** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-520](./part-11.md)

---

### 301. [Does Merge Form a Hopf Algebra? Coproducts, Traces, and the Prospects of Algebraic Minimalism](https://arxiv.org/abs/2611.11502)

**<font color=#1a73e8>作者：</font>** Daisuke Bekki  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Marcolli, Chomsky, and Berwick (2025; henceforth MCB) formulate the Merge operation of Minimalism on a Hopf algebra of Connes-Kreimer type, and claim that language and physics obey the same algebraic structure. This paper separates their program into the working hypothesis H, that Merge on workspaces can be described as a Hopf algebra, and the claim P placed on top of it, that language and physics obey the same principle, and examines the validity of H. MCB employs two coproducts in formulating Merge, corresponding to two different translations of movement (Internal Merge): $\Delta_d$, which deletes the lower copy, and $\Delta_c$, which leaves a trace. MCB uses the former in syntax and the latter at the syntax-semantics interface, but $\Delta_d$ is not coassociative, and $\Delta_c$ is not connected under the gradings MCB gives and, moreover, not coassociative as long as the labels of traces are retained. Consequently, MCB's algebra is not a Hopf algebra, and the Birkhoff factorization is not a consequence of the Hopf-algebra theorem but of a weaker statement that requires neither coassociativity nor connectedness. There are four ways to recover a Hopf algebra, but none of them can distinguish different traces, and hence none is compatible with Heim-Kratzer-style formal semantics, which reads traces as indexed variables. Thus H does not hold at present, and under the current formulation, making Minimalism a Hopf algebra and preserving its connection with formal semantics are mutually exclusive. Finally, we indicate three directions in which algebraic Minimalism may proceed.

---


### 302. [ConvLUT: Rethinking Convolutional Architectures for Ultra-Low-Latency LUT-Based Inference](https://arxiv.org/abs/2611.11507)

**<font color=#1a73e8>作者：</font>** Marta Andronic, Olivia Weng, Danial Zuberi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lookup-table (LUT)-based neural networks (NNs) offer a compelling path to ultra-low-latency inference on FPGAs. However, existing LUT-based neural networks have largely been restricted to MLP-style topologies, leaving structured vision and audio tasks underexplored. We present ConvLUT, a family of fully unrolled LUT-mappable convolutional architectures targeting the MLPerf Tiny benchmarks. It is comprised of a standard convolutional model built around a hierarchical tree of LUTs and a depthwise separable model following the MobileNet design philosophy. These architectures are enabled by four key contributions: a unified LUT-based convolutional framework supporting standard, depthwise, and pointwise convolutions under explicit fan-in constraints; a LUT-tree that addresses the $k^2c$ receptive field dimensionality bottleneck; a channel-partitioned LUT pooling layer that replaces conventional spatial pooling; and a hardware-aware iterative pruning strategy for stable convergence at scale. Evaluated on CIFAR-10, Visual Wake Words, and Keyword Spotting, ConvLUT achieves competitive accuracy with fully unrolled inference latencies below $\sim 50$ ns. On CIFAR-10 it reaches at least a $8844\times$ latency reduction over non-logic-based prior implementations, and outperforms existing MLP-style LUT-based models on the same task by at least $20$ pp in test accuracy.

---


### 303. [Detecting Common Golfing Faults Using AI and Video-Derived Biomechanical Features](https://arxiv.org/abs/2611.11515)

**<font color=#1a73e8>作者：</font>** Oliver Martin, Jeff Clark, Nawid Keshtmand  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how an athlete moves can improve both technique and safety, yet outside the laboratory technique is still assessed by eye. We present a pipeline that detects named golf swing faults from ordinary video, without markers or calibration. Instead of learning end to end, it tracks body pose and the clubhead in a body-centered frame, and classifies the biomechanical quantities a coach would measure, such as the height of the clubhead above the swing plane, with shallow boosted trees. We demonstrate the approach on two common faults, coming over-the-top (OTT) and early-extension (EE). On 160 swings and 143 swings from public sources it detects OTT and EE with a cross-validated ROC-AUC of 0.975 and 0.911 respectively. Because every feature is a biomechanical quantity a coach already uses, measured at a known phase of the downswing, each decision can be traced to the signals and the moments of the swing that drove it. The signals the model relies on most are the same ones a coach checks when diagnosing these faults. The pipeline processes phone video on a consumer laptop in seconds, so it could feasibly be developed into an app for golfers of all abilities and extended to other sports in which technique is judged against a biomechanical reference.

---


### 304. [InfCoiL: Coordinated Planner-Controller Learning for Closed-Loop Physics-Based Human-Object Interaction](https://arxiv.org/abs/2611.11517)

**<font color=#1a73e8>作者：</font>** Yude Zou, Yifei Yao, Yiwei Hao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text- and goal-conditioned human-object interaction (HOI) provides an intuitive interface for specifying high-level intents in physics-based character animation. Mapping such intents to physically plausible, contact-rich behaviors naturally calls for a generative planner and a physics-based controller, yet existing planner-controller systems either execute plans open-loop or close the loop while keeping the planner fixed, so execution feedback never reshapes what is planned. We present InfCoiL, a closed-loop framework for physics-based HOI from coordinated planner-controller learning. InfCoiL couples a morphology-aware flow-matching planner with a unified multi-morphology controller through a shared morphology interface in an autoregressive plan-and-execute loop, and alternately fine-tunes both components with reinforcement learning from the same physical rollouts. To optimize the flow-matching planner online, we introduce Semantic Flow Policy Optimization (SFPO), which stochasticizes selected denoising transitions with channel-wise semantic covariance over heterogeneous HOI features and assigns group-relative, sequence-level rewards from complete closed-loop executions. On held-out OMOMO sequences, InfCoiL outperforms open-loop hierarchical baselines in goal-reaching task success and physical tracking accuracy. Project page: this https URL

---


### 305. [Hydra: Towards Transferable Multi-Task Learning on Temporal Graphs](https://arxiv.org/abs/2611.11520)

**<font color=#1a73e8>作者：</font>** Kiarash Shamsi, Farimah Poursafaei, Tran Gia Bao Ngo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world evolving networks are naturally modeled as temporal graphs (TGs), where capturing temporal dynamics is essential for predicting future graph properties that support downstream decision-making. Existing temporal graph methods have been developed primarily for single-task prediction, and little is known about their generalization across tasks or transfer to unseen networks. This leaves the challenge of multi-task graph property prediction in TGs largely open. We address this challenge by introducing Hydra, a novel architecture that integrates local connectivity features from temporal GNNs with a spectral learning module that captures global connectivity patterns. This design enables joint learning of local and global information under a multi-task objective. In multi-task classification, Hydra achieves an 8.9% relative gain in AUC over the strongest competitor. In multi-task regression, Hydra achieves competitive results in all three tasks, while obtaining the best results in two tasks with a 8.2% relative gain in MAE compared to the strongest baseline. Moreover, Hydra delivers these gains with a 22% reduction in training time compared to temporal transfer models. These results provide the first systematic evidence that multi-task transferable learning on temporal graphs is effective. By delivering consistent top-ranked performance, Hydra highlights multi-task training on temporal graphs as a promising direction toward adaptable foundation models for temporal graphs.

---


### 306. [Boundary Mass in Feature Space as a Label-Budget Diagnostic for Representations](https://arxiv.org/abs/2611.11525)

**<font color=#1a73e8>作者：</font>** Siming Zhang, Zhehui Shen, Shijie Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-label transfer is often decided by a practical question: after a representation looks useful, how many labels are still needed to learn the downstream boundary? Transferability and probe-quality scores characterize global alignment, likelihood, margins, and calibration. Boundary-near target mass complements these diagnostics by measuring the ambiguous regions where scarce labels are most costly. We propose effective boundary complexity, a label-budget diagnostic for frozen representations and linear probes. It measures mass in a thin strip around the learned boundary and normalizes it by class balance, so dense ambiguous regions and predicted-class imbalance are both counted. We prove that, under a smooth representation map, density change and tangential surface change cancel at first order, leaving boundary-normal stretch or compression as the governing factor. This yields a cached-feature estimator that fits a probe on one split and counts independent held-out features near its boundary. Experiments support the diagnostic at three levels. Controlled transformations match the predicted law across 74 maps with 0.38% median relative error. On real frozen features, normal-direction changes move both measured boundary mass and label demand, while tangent controls preserve the first-order coefficient. A differentiable surrogate reduces measured complexity by 16-36% at matched top-1 utility. Finally, CIFAR-100 and Tiny-ImageNet experiments support boundary mass as a second-stage diagnostic for near-tied representations. Five-way experiments show strong OvR-interface backbone-ranking agreement (Spearman 0.872), while acquisition experiments show high correlations between initial boundary mass and realized label budgets across three sampling policies (0.779-0.830). Code is available at this https URL.

---


### 307. [A Stability Analysis of AdamW: Unstable Equilibria and Non-Convergence](https://arxiv.org/abs/2611.11526)

**<font color=#1a73e8>作者：</font>** Baiyu Su, Lizhang Chen, Qiang Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AdamW is ubiquitous in deep learning, yet its behavior remains poorly understood. We analyze its dynamics through the lens of dynamical systems and show that AdamW admits an implicit fixed-point objective: its fixed points coincide with the stationary points of a constrained and regularized optimization problem. However, not all of these fixed points are stable under AdamW's dynamics, and stability depends sensitively on curvature, weight decay, and momentum parameters. Even in one-dimensional settings, equilibria may be unstable, and trajectories can exhibit persistent oscillations rather than convergence to them. We further extend the analysis to higher dimensions, deriving sufficient conditions for local stability of the continuous-time dynamics, and propose a convergent modification that preserves AdamW's fixed points. These results clarify what optimization problem AdamW is associated with, when its convergence can be expected, and how its dynamics could inspire more reliable optimizers.

---


### 308. [Data Manipulation Attacks Against Machine Learning Integrated Cyber-Physical Systems](https://arxiv.org/abs/2611.11529)

**<font color=#1a73e8>作者：</font>** Soyon Choi, Scott Alfeld, Meiyi Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> There is a well-established body of work demonstrating that individual machine learning (ML) algorithms can be manipulated or deceived. However, in many real-world systems, multiple ML algorithms are composed to enable automated decision-making, particularly in Cyber-Physical Systems (CPS). Often such systems use a composition of vision, planning, and other ML models to affect their internal state and ultimate take actions in the physical world. While there is a huge literature on the (in)security of ML algorithms, it is not immediately clear how an attacker might leverage their ability to trick individual learners when attacking the composition as a whole. We develop methods for creating an attack policy (a mapping from state to attack) for a data-manipulating attacker affecting a CPS or other state-machine-based AI compositions. We describe our framework, a basic threat model and corresponding methods for computing an optimal attack policy, as well as planned extensions. The goal of this work-in-progress paper is to stimulate conversation and forge new collaborations regarding the security of compositional learning.

---


### 309. [Dashboard Remixing: Goal-oriented Organization and Enrichment of Visualizations and Insights](https://arxiv.org/abs/2611.11542)

**<font color=#1a73e8>作者：</font>** Junran Yang, Leilani Battle, Jane Hoffswell  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Dashboard creation requires iteratively authoring multiple views and organizing them into a structured format. However, creators often struggle to step back and assess their own work for organization and refinement due to cognitive limitations. In this work, we propose a pipeline to provide computational support for self-reflection during the design process. Our pipeline automatically infers analytical objectives, discovers implicit patterns, and structures those patterns to surface coherent analytical pathways. It further enriches existing dashboard designs by generating complementary visualizations and aggregating natural language insights based on relationships across data entities (e.g., contrasting, drill-down, and relatedness) to reveal chart connections. Our rule-based pipeline provides objective, verifiable feedback, offering an external perspective while enabling creators to tell their own data stories. Four case studies and six expert interviews demonstrate how this approach helps creators reflect on organizational alternatives and surface hidden analytical opportunities in a principled way, reducing the cognitive burden while encouraging deeper analytical exploration.

---


### 310. [Dropping Tokens Without Dropping Them: Causal Attribution for Diabetic Retinopathy](https://arxiv.org/abs/2611.11547)

**<font color=#1a73e8>作者：</font>** Pramath Girish Haritz, Chandra Sekhar Seelamantula  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we investigate whether attention-based attribution maps in a vision transformer provide causal explanations for diabetic retinopathy (DR) classification. We introduce a principled decomposition of attention into two attribution maps: the contribution ($c_t$), which satisfies the completeness axiom in explainable artificial intelligence (xAI), and the pull ($p_t$), which quantifies causal explanations. We define an identity relating $c_t$ and $p_t$ that characterizes when $c_t$ fails to capture causality. We test whether each map is causally faithful on the MAPLES-DR dataset by dropping/inserting tokens, and report Necessity ($N$), Sufficiency ($Su$), and Faithfulness Correlation ($FC$). The pull $p_t$ achieves the highest causal alignment ($FC = 0.53$, $N = 0.71\%$, $Su = 3.0\%$), outperforming Attention Rollout, Grad-CAM, and AttnLRP. Occlusion retains better sufficiency ($Su = 1.6\%$) but is about 800 times slower. Furthermore, on MAPLES-DR, $p_t$ achieves $70\%$ of the average precision (AP) of HRDecoder, a state-of-the-art supervised lesion segmentation model, despite the absence of pixel-level supervision. Together, these findings show that the pull $p_t$ and the contribution $c_t$ form computationally efficient attribution maps for reliable causal interpretation in safety-critical medical diagnostics. The code and demo are available at this https URL.

---


### 311. [From Sketch to Design: A Cross-scale Workflow for Procedural Generative Urban Design](https://arxiv.org/abs/2611.11561)

**<font color=#1a73e8>作者：</font>** Jin Gao, Sayjel Vijay Patel  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Urban designers use sketches and symbols to express spatial intentions, while many generative urban design tools rely on numeric parameters that are difficult to relate to this visual process. We propose a cross-scale workflow and a web-based prototype that translates symbolic sketches into controllable procedural urban generation. A vocabulary of shapes, informed by examples of urban design diagrams and sketching exercises with graduate urban design students, encodes attributes such as network structure, density, and program. The prototype uses the \$1 Unistroke Recognizer to map gestures to symbols and translates their locations and sizes into tensor-field attractors and weighted parameter grids. Grid and radial tensor fields guide street-network generation, while the parameter grids control building heights and programs. Implemented in JavaScript and TypeScript with React and this http URL, the prototype supports interactive sketching, visualization, and urban massing generation. We describe the methodology and illustrate prototype interactions, then discuss downstream integration with architectural-scale generative tools for further refinement and analysis. The work connects designers' symbolic input with an explicit procedural generation process.

---


### 312. [UTOPI: Efficient Egocentric Long-Video Understanding in AR via User-Guided Token Pre-Compression](https://arxiv.org/abs/2611.11562)

**<font color=#1a73e8>作者：</font>** Ziqi Wang, Su Chen, Qiance Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As long-video understanding gains increasing attention, augmented reality (AR) devices are emerging as a compelling deployment platform. However, egocentric videos exhibit significant temporal redundancy, imposing substantial memory and computational burdens on resource-constrained AR hardware. To address this challenge, we introduce UTOPI, a plug-and-play pre-compression module designed specifically for egocentric long videos on AR platforms. First, we leverage user motion signals to estimate inter-frame overlap and propose a viewpoint-shift-invariant pruning algorithm. Second, we exploit eye-tracking sensors to identify user fixations, enabling the separation of attended foreground content from background and its preferential retention via a fine-tuned neural network-based adjustment mechanism. Across multiple benchmarks and model backbones, UTOPI achieves up to 95% compression while preserving performance. Code and project page are available at this https URL.

---


### 313. [Continuous modeling of manipulative participation for stance analysis: Online discourse on the 2024 Street Animal Law in Türkiye](https://arxiv.org/abs/2611.11576)

**<font color=#1a73e8>作者：</font>** Ulya Bayram, Ebru Belkıs Güzeloğlu, Emel Kuşku Özdemir 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Studies of online political discourse commonly infer public opinion through stance analysis while implicitly assuming that observed user participation is authentic. Meanwhile, studies focusing on detecting manipulative participation are typically modeling it as a binary phenomenon, overlooking the varying degrees to which users may engage in coordinated or inauthentic behavior. This study proposes a continuous modeling approach for manipulative participation and examines its integration with stance analysis. Using online discourse on the 2024 Street Animal Law in Türkiye as a case study, we collected a dataset comprising 7,320,574 tweets from 537,994 users. From this corpus, 301 users were selected through a high-information sampling strategy and manually annotated by domain experts using a 10-criterion rubric that yields user-level continuous manipulative participation scores. Evaluation under a unified user-level cross-validation protocol showed that the proposed framework accurately estimates both manipulative participation and user stance, with gradient boosting methods providing the best manipulative participation estimates and BERTurk achieving the highest stance classification performance. External validation on an independently annotated user set demonstrated good generalization performance. The findings support modeling manipulative participation as a continuous construct rather than a binary label, providing a more informative basis for computational analyses of the relationship between manipulative participation and stance in online political discourse.

---


### 314. [FastGRT: Accelerating Training of 3D Gaussian Ray Tracing](https://arxiv.org/abs/2611.11586)

**<font color=#1a73e8>作者：</font>** Meet Banthia, Xiaoteng Liu, Hexu Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ray Tracing enables rendering capabilities that are difficult to achieve with rasterization-based approaches such as 3D Gaussian Splatting (3DGS). However, the training cost of Gaussian-based ray tracing (GRT) is much higher than that of 3DGS. In this paper, we study how ray tracing using Gaussians executes on GPUs and show that a considerable fraction of the training cost arises from how the computation is organized. We develop FastGRT, which decouples ray traversal from blending and reuses work done in the forward pass for the backward pass. FastGRT further incorporates optimizations such as fast gradient accumulation and a hybrid BVH update strategy to tackle other major bottlenecks in the training pipeline. We implement FastGRT in Vulkan. To the best of our knowledge, it is the first Vulkan-based GRT implementation that supports both training and rendering. Compared to 3DGRT, FastGRT improves training time by 1.9$\times$ to 4.97$\times$, while preserving the original rendering formulation. Our code is open source.

---


### 315. [Martine: Benchmarking Multi-View 3D Surface Reconstruction Across Viewpoint Coverage, Resolution, and Lighting](https://arxiv.org/abs/2611.11602)

**<font color=#1a73e8>作者：</font>** Robin Bruneau, Baptiste Brument, Frederic Giraud 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controlled acquisition setups are widely used for high-accuracy multi-view 3D surface reconstruction, as they allow sensor configuration, image resolution, viewpoint distribution, and illumination to be specified. Yet benchmarking remains difficult, since reconstruction accuracy depends jointly on the reconstruction paradigm, object properties, and acquisition regime. Existing benchmarks often restrict viewpoint coverage, resolution, or illumination, which can bias comparisons towards methods suited to the chosen setting. Others lack accurate 3D ground truth or quantified image-to-geometry alignment, limiting their use for metric surface evaluation. We introduce Martine, a benchmark for controlled 3D object surface reconstruction. Martine comprises 28 objects, including transparent materials and fine structures, captured at 9568 x 6376 pixels from 84 views over a spherical cap under both single-light and multi-light regimes. It provides object-independent camera calibration, accurate 3D ground-truth scans, calibration and image-to-geometry accuracy quantified on test images, and 3D property masks for analysing errors by material properties, visibility, curvature and fine structures. Experiments across photogrammetry, classical multi-view stereo, neural implicit surfaces, Gaussian-splatting-based reconstruction, and multi-view photometric stereo show that Martine enables regime-aware evaluation with explicit control over reference-data accuracy. The benchmark resolves sub-millimetric reconstruction differences, with a best observed Chamfer distance of 0.058 mm over the evaluated visible surface.

---


### 316. [Rethinking Geometric Depth in Monocular 3D Object Detection: A Projection-Consistent Reformulation](https://arxiv.org/abs/2611.11607)

**<font color=#1a73e8>作者：</font>** Zhihao Zhang, Abhinav Kumar, Huaizhi Qu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular 3D detection (Mono3D) hinges on recovering depth from a single image, for which the geometric formulation $z \approx f \cdot H / h_{2D}$ is widely adopted due to its simplicity and direct grounding in projective geometry. We show that this formulation harbors a systematic, projection-induced bias: substituting the 2D bounding-box height $h_{2D}$ recovers the depth of an object's visible front surface rather than its center, causing size-dependent underestimation that persists even under ground-truth inputs. We address this front-surface bias with MonoPCA, a unified framework built on a projection-consistent reformulation. At its core, PCDepth retains the measurable $h_{2D}$ and closes the gap to center depth through an orientation- and size-aware correction derived from perspective geometry, eliminating the bias without introducing ill-posed regression targets. Because PCDepth couples depth to predicted object size and orientation, attribute perception becomes essential. We therefore introduce GeoAlign, a teacher-student framework that transfers geometric representations from Vision Foundation Models into a lightweight student, strengthening attribute perception at no inference cost. Across four challenging benchmarks, MonoPCA achieves SoTA performance, including a +1.44% AP$_{3D}$ gain on the KITTI leaderboard and +2.80% on Omni3D$_{OUT}$. Code is available at this https URL.

---


### 317. [Building heterogeneous multistep workflows in automated microscopy: reward design and knowledge transfer for autonomous structure property discovery](https://arxiv.org/abs/2611.11609)

**<font color=#1a73e8>作者：</font>** Sergei V. Kalinin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous microscopy can turn fast acquisition into scientific progress when it decides not only where to measure, but also what information to acquire, at what scan rate, and when to recalibrate the instrument. We develop a budget constrained framework for such multistep structure-property workflows. It combines explicit scientific rewards, action costs, instrument observation models, transfer of pre experiment knowledge into the online campaign, and evaluation kept independent of the controller. The transferred knowledge includes predictor accuracy and computational cost, empirical learner maturity functions that weight model-derived rewards, and drift characteristics established before controller training. Using a real electron energy-loss spectroscopy dataset, we run two complementary campaigns. In the first, the controller chooses between imaging and spectroscopy, image size, and scan speed. In the second, the instrument drifts and the controller also decides when to recalibrate. The campaigns show that response discovery and structure-property learning favor different surrogate models and acquisition strategies. They also show that simple acquisition rules form strong, practical baselines. Independent error analysis reveals where model uncertainty is and is not a reliable learning signal. In the drift campaign, explicit registration greatly improves positional accuracy, and the framework measures what this costs in spectroscopy throughput. Together, these results provide a reproducible way to design, compare, and audit autonomous experiments, and they define what microscopes must provide for deployment: independently executable actions, characterized scan and detector responses, timestamped registration telemetry, and complete action records.

---


### 318. [Daily Emergency Call Volume Forecasting using Univariate and Multivariate TimeGPT](https://arxiv.org/abs/2611.11613)

**<font color=#1a73e8>作者：</font>** Feriel Fass, Djemel Ziou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study investigates the potential of TimeGPT, a pretrained foundation model for timeseries, for forecasting daily emergency call volumes. Real-world emergency call data, comprising 2,101 daily observations, are used to evaluate both univariate and multivariate forecasting settings under one-step-ahead and seven-day multi-step-ahead scenarios. The multivariate forecasting incorporates temporal, meteorological, demographic, and socioeconomic variables. A chronological training, validation, and test split is adopted to prevent information leakage, while hyperparameters are selected using the validation set through grid search and early stopping when applicable. Forecasting performance is evaluated using multiple error metrics. Its forecasting performance is compared with several established forecasting approaches, including Seasonal Autoregressive Integrated Moving Average with Exogenous Regressors (SARIMAX), Poisson regression (PR), Negative Binomial regression (NBR), Extreme Gradient Boosting (XGBoost), Multilayer Perceptron (MLP), and Long Short-Term Memory (LSTM). The results show that SARIMAX achieves the best overall performance in the univariate setting. In the multivariate setting, NBR and PR provide best performance. These findings indicate that the large-scale pretraining of TimeGPT do not necessarily translate into superior forecasting accuracy for emergency call volumes. Frugal methods trained solely on the available data remain better for this application.

---


### 319. [Delegating Computation with Approximate Arithmetic: Interactive Proofs for Wizards](https://arxiv.org/abs/2611.11618)

**<font color=#1a73e8>作者：</font>** Aritra Das, Debayan Gupta, Arup Mondal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We study interactive proofs for arithmetic circuits over the complex numbers $\mathbb{C}$ in which both the prover and the verifier compute approximately (unlike muggles, wizards can use magic, i.e., floating-point numbers). The goal is to prove that a claimed output $y$ is close to the exact output $C(x)$: for thresholds $0<\Delta_0<\Delta$, the honest prover is accepted whenever $|y-C(x)|\le\Delta_0$, and every prover is rejected with high probability whenever $|y-C(x)|>\Delta$.
Existing proof systems for real-valued data verify rounded finite-field computations. Bitan et al.~[EUROCRYPT~2026] gave an approximate sum-check protocol. We extend the protocol of Goldwasser, Kalai, and Rothblum (GKR) [STOC~2008] to public-coin interactive proofs for logspace-uniform layered circuits over $\mathbb{C}$ of size $S$, depth $L$, and $n$ inputs, under public bounds on gate values and wiring coefficients. At constant soundness error, the verifier runs in time $(n+1)\mathrm{poly}(L,\log S,b)$, the communication is $\mathrm{poly}(L,\log S,b)$, and the prover runs in time $\mathrm{poly}(S,b)$, where $b$ is the bit precision. To the best of our knowledge, these are the first doubly efficient interactive proofs in which both parties compute approximately. GKR reduces two claims about a layer to one on a random line, which leaves the unit circle, where our error bounds hold. We instead label gates by complex roots of unity and combine the two claims with a random root of unity as coefficient. We choose the error thresholds backward from the input layer, so that a large output error survives the verifier's rounding at every step. The honest prover needs only $O(S \log S)$ complex operations. We also obtain zero-knowledge proofs from one-way functions, one-round arguments from private information retrieval, and interactive PCPs whose proof length is polynomial in the witness length.

---


### 320. [GenISys: Integrated Ship Systems Design Using Subsystem-Conditional Tabular Diffussion](https://arxiv.org/abs/2611.11622)

**<font color=#1a73e8>作者：</font>** Noah J. Bagazinski, Faez Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ship design requires coordinating coupled subsystems to satisfy engineering constraints and balance competing performance and cost objectives. Generative artificial intelligence has supported component design, but integrated ship generation must also account for interactions among hull geometry, structure, propulsion, and operation. This paper presents GenISys, a framework for generating integrated systems, demonstrated through early-stage bulk-carrier design. Its dataset contains 217,999 proposed designs, including 16,247 that satisfy the formulated engineering constraints. The proposed simultaneous conditional denoising diffusion probabilistic model (SCDDPM) generates subsystems together, allowing each subsystem model to respond to changes elsewhere during generation. Experiments compare this approach with monolithic whole-ship generation and sequential subsystem generation across five independent training runs per architecture. In a study targeting lower cost per tonne of cargo transported, designs were generated for a required voyage range of 5,000 nautical miles. SCDDPM produced designs satisfying the formulated engineering constraints and meeting a common low-cost target in 55.70% of generation requests, compared with 51.10% for the monolithic model and 47.54% for the sequential model. These correspond to 9.0% and 17.2% more qualifying designs, respectively, while maintaining similar estimated transport costs. These results show how generative artificial intelligence can coordinate subsystems to generate feasible, high-performing integrated systems.

---


### 321. [Attack Injection to Vehicle Reactions: Extensible Closed-Loop Adversarial Evaluation Framework](https://arxiv.org/abs/2611.11627)

**<font color=#1a73e8>作者：</font>** Mohamed Gaber, Tahsin Wahid, Mohammad Mamun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles can use information exchanged with other vehicles and roadside infrastructure to support driving decisions. However, applications that rely on this information can make unsafe decisions when it is falsified. Studying the resulting traffic effects requires following received information through application decisions, vehicle reactions, and subsequent interactions. We present an extensible closed-loop adversarial evaluation framework built on VaN3Twin, a platform for traffic and wireless network simulation, with a diverse attack library and a labelled dataset covering benign and attack conditions. A key advantage of the framework is that it can be extended with additional attacks, message paths, receiving applications, and logging fields. The added library contains 76 configurable attack profiles adapted to message formats defined by the European Telecommunications Standards Institute. These profiles are organized into nine groups of related attacks, referred to as suites. The framework connects live attack injection and simulated network delivery to receiving applications, whose selected commands update vehicle movement. The resulting state feeds subsequent message generation, closing the loop. The dataset links physical vehicle states and message exchanges to attack labels, application decisions, selected commands, and traffic outcomes. Evaluation with individual and combined attack suites confirmed execution of all profiles, and every suite produced requests linked to attacked messages. A recorded sequence also showed a vehicle reacting to an attacked message and subsequently influencing another vehicle through an unmodified message describing its updated movement. These findings demonstrate how live injection and vehicle feedback support the study of direct and indirect effects as traffic evolves.

---


### 322. [Perturbation Profiles of Scanpath Classifiers: What Reading, Code-Comprehension and Video Decoders Are Sensitive To](https://arxiv.org/abs/2611.11632)

**<font color=#1a73e8>作者：</font>** Saleh Mozaffari, Abolfazl Nadi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a scanpath descriptor discriminates a task, it is rarely clear what the discrimination rests on. We propose a perturbation profile for trial-level descriptors. Five transformations each destroy one stated property while preserving a listed set of invariants: fixation order, duration-position coupling, the duration distribution, orientation and handedness, and fine spatial structure. The classifier is refit, and the drop in participant-held-out AUC is the pipeline's sensitivity to that property. Because refitting lets the learner use redundant information, this describes the refitted pipeline, not what a fitted classifier used. Intervals come from a participant bootstrap that refits; in simulations at the sample sizes analysed, where the target was zero they excluded zero at a pooled rate of at most 2.5%, and they covered the target in 99.6% of 2720 cases. We profiled seven descriptors on twelve binary problems from three public datasets: reading (SB-SAT, 95 participants), program comprehension (EMIP, up to 159) and video and game viewing (GazeBase, 60). Permuting fixation order raised the AUC of a descriptor built on mean saccade amplitude on three problems (by up to 0.23), because permutation turns amplitude into a measure of spatial spread. A "comprehension" contrast that pooled two programs reached AUC 0.70 with a spread-only baseline and fell to 0.47 within one program: the profile located the confound in stimulus layout. On native versus non-native readers, recurrence was sensitive to order and to jitter at the scale of text lines but not of characters, while a two-feature duration and amplitude descriptor reached the same AUC (0.65). A graph descriptor built on the code's tokens was the strongest non-baseline descriptor on the program contrast (0.78; 0.87 with boosted trees). The interpreted results held under longer runs and three seeds; under a second learner 15 of 16 kept t

---


### 323. [An Interpretable Fuzzy Tree for Turbofan Remaining Useful Life with an Auditable Per-Component Diagnostic Layer](https://arxiv.org/abs/2611.11633)

**<font color=#1a73e8>作者：</font>** Hugo Henry, Bharadwaj Dogga, Scott Philips 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data-driven remaining useful life (RUL) estimators for turbofan engines are accurate but opaque, and their internal features typically encode remaining life rather than any specific component's state. This paper presents an interpretable genetic fuzzy tree that predicts RUL from cruise-condition sensor means on N-CMAPSS while exposing a per-component diagnostic layer inspectable rule by rule. The tree follows the engine hierarchy: sensors to component health, then to bounded component damage, spool damage, and RUL, so each level answers a different maintenance question. Training is staged so the prognostic objective cannot reshape the diagnostic layers: health leaves are fitted to physical targets and frozen, a deterministic fuzzy damage map with fleet-referenced thresholds is imposed on each component, and only the aggregation is optimized for RUL. It consumes 13 cruise-mean scalars per cycle rather than a trajectory, which removes any sequence model. On the native split it reaches 8.44 cycles RMSE on the multi-fault subset and 11.51 across all modes with 333 free parameters, 411 total rules, 32 to 12,000 times fewer than compiled baselines. An exhaustive sensor search bounds which components are diagnosable under the tested cruise-mean design, and the rule base is structured to admit formal verification, which this study does not discharge.

---


### 324. [Trail Making Tests in Extended Reality: A Critical Review with Implications for Cognitive Ageing](https://arxiv.org/abs/2611.11636)

**<font color=#1a73e8>作者：</font>** Panagiotis Kourtesis  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Extended reality (XR) versions of the Trail Making Test and Color Trails Test are promising for assessing and training cognition in older adults. However, each XR adaptation is a new instrument, whose display, interaction technique, timing rules and layouts may change what it measures. This critical narrative review maps these implementations by software lineage and appraises their evidence for assessment and training against common criteria. The Trail Making Test in Virtual Reality (TMT-VR), whose source code was inspected, serves as a measurement case. XR trail-making tests showed convergence with paper and computerised versions, varying by test part and sample, and clinical group differences (e.g., Parkinson's disease, mild cognitive impairment). However, gaps in reliability (e.g., randomised forms), validation (e.g., norms, prospective samples) and reporting (e.g., error handling, build identity) emerged, and no training benefit attributable to the trail-making component was identified. The TMT-VR case shows how interaction technique, timing rule, error handling and unlogged layouts shape a score's meaning. Future tests should log layouts and events, estimate alternate-form reliability and undergo prospective validation, and training trials should isolate the trail-making component. Several XR trail-making tests have moved beyond feasibility, and reported tolerability during supervised sessions supports further evaluation in older adults.

---


### 325. [Feel My Focus: Gaze-Triggered Digital Twin Creation for Remote Collaboration](https://arxiv.org/abs/2611.11640)

**<font color=#1a73e8>作者：</font>** Shih-Yu Ma, Suibi Che-Chuan Weng, Ming-Yuan Pai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present Feel My Focus, a gaze-triggered mixed reality (MR) demonstration that enables rapid creation and sharing of lightweight 3D digital twins during remote collaboration. Unlike systems that use gaze primarily as a referential pointer, Feel My Focus treats sustained visual attention as a generative action: a fixation on a physical object initiates single-image capture, attention-guided segmentation, and one-shot 3D reconstruction, allowing a remote partner to inspect and discuss the object in situ. The system integrates gaze-tracking glasses, modular segmentation and reconstruction services, and an MR client for runtime streaming and interaction. This design prioritizes responsiveness and experiential continuity over photometric fidelity. We report observations from a public demonstration, highlighting design trade-offs, failure modes, and user control considerations for deploying gaze-triggered generative systems in real-world collaborative settings.

---


### 326. [A Trust Region Approach for Learning Schrödinger Bridges](https://arxiv.org/abs/2611.11649)

**<font color=#1a73e8>作者：</font>** Takeshi Koshizuka, Denis Blessing, Max Zimmer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the numerical approximation of Schrödinger Bridges in the setting where samples from the target distribution are unavailable and only an unnormalized target density is given. In this regime, the widely used iterative proportional fitting (IPF) procedure (and its variants) often exhibits severe numerical instabilities, stemming from ill-conditioned underlying control problems and from the fact that the optimal solution may lie far from the initialization. To address these issues, we propose a trust region variant of IPF that constrains successive updates to remain at a fixed Kullback-Leibler divergence from the current iterate. This restriction significantly improves numerical stability. Moreover, we show that the resulting method admits an interpretation as a mirror descent scheme with an adaptively chosen step size. We demonstrate the effectiveness of our approach on several challenging sampling tasks.

---


### 327. [Optimizing Multi-Tier Intermediation in Programmatic Advertising: A DAG-Based Mechanism for Supply Path Optimization](https://arxiv.org/abs/2611.11651)

**<font color=#1a73e8>作者：</font>** Amelia Bădică, Costin Bădică  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Digital programmatic advertising operates through complex, multi-hop supply chains. The opacity of these intermediary networks leads to significant efficiency losses, often referred to as the ``ad-tech tax.'' While current industry practices utilize heuristic Supply Path Optimization (SPO) to trim inefficient routes, they fail to optimize the equilibrium of the entire network. This paper extends previous work on Directed Acyclic Graph (DAG) intermediation models by applying them to traceable programmatic supply chains mapped via the OpenRTB SupplyChain object. We introduce multi-attribute utility functions and Mixed-Integer Linear Programming (MILP) to account for substitutable routing (OR nodes) and percentage-based fee structures. Furthermore, we outline a computational methodology and experimental framework using public \texttt{schain} and \texttt{this http URL} data to benchmark optimal Nash social welfare against current uncoordinated market outcomes.

---


### 328. [Exploring Mixed-Reality for Enhancing Driver Warning Systems: A Preliminary Study on Attention-Shifting Methods and Hazard Perception](https://arxiv.org/abs/2611.11653)

**<font color=#1a73e8>作者：</font>** Shih-Yu Ma, Nolan Robert Brady, Xu Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Modern vehicles are equipped with advanced sensors and capabilities, yet engaging human drivers effectively in hazard perception remains a challenging research area. This paper investigates the potential of mixed reality (MR) to enhance driver warning systems. The study examines the impact of attention-shifting methods, including visual cues, audio cues, and a combination of both, on drivers' hazard perception. A preliminary study involving six participants was conducted, and the NASA-TLX analysis did not yield significant differences. However, through the use of functional near-infrared spectroscopy (fNIRS), we unveil distinct brain activation patterns associated with visual and sound cues. Further research with larger sample sizes and diverse driving scenarios is required to validate and expand upon these preliminary results.

---


### 329. [A Theoretical Reduction From Membership Inference to Reconstruction Attacks Against Learners](https://arxiv.org/abs/2611.11680)

**<font color=#1a73e8>作者：</font>** Amnon Levi, Yuval Dagan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study reconstruction attacks, which recover training data from a learned model. In our adversarial model, the adversary designs a hard instance, drawn from a parameterized family of data distributions, and is given the parameter used to generate it. Our main contribution is a general reduction showing that, in this model, membership inference (determining whether a given datapoint was used for training) implies reconstruction: for a training set of size $n$, a membership test with recall at least $q(n)$ and false-positive rate $O(\delta^2/n^2)$ yields a reconstruction algorithm that, with probability $1 - O(\delta)$, outputs only training points, and recovers $\Omega(n \cdot q(n))$ of them in expectation. This reduction applies to any learning algorithm. For stochastic convex optimization (SCO), we make the reduction computationally efficient over exponentially large domains via structured distributions whose support is partitioned into polynomially many categories of exponentially many elements each, so that reconstruction iterates over categories rather than the full support. Combining this with an existing membership inference result for SCO, we prove that any learning algorithm achieving low excess risk over all distributions admits a polynomial-time reconstruction attack recovering $\Omega(n)$ training points, even when the underlying distribution has exponentially large support.

---


### 330. [Resolvent Ellipsoid for Minty Set Inclusions](https://arxiv.org/abs/2611.11691)

**<font color=#1a73e8>作者：</font>** Ashkan Soleymani, Gabriele Farina, Patrick Jaillet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study Minty set inclusion on a compact convex set $\mathcal{X} \subseteq \mathbb{R}^d$ with a set-valued operator $A : \mathcal{X} \rightrightarrows \mathbb{R}^d$. Under the Minty promise, the goal is to compute $x \in \mathcal{X}$ and $u \in A(x)$ such that $\sup_{y \in \mathcal{X}} \langle u, x - y \rangle \le \varepsilon$. Our approach is geometric and we work in the fixed-scale constrained-resolvent oracle model, where a query at anchor $a$ is assumed to return a resolvent point $x^+$ together with the Yosida vector $g_{\eta}(a) = (a - x^+)/\eta$. We prove that each oracle response yields a sharp dichotomy: either the returned point provides an $\varepsilon$-SVI certificate, or the Yosida vector defines a strict separating normal for the Minty set. Thus, a single black-box resolvent query supplies either a certified candidate solution or a valid geometric cut. Combining this separation principle with the ellipsoid method, we obtain RESOLVENT-ELLIPSOID, an algorithm that computes an $\varepsilon$-SVI in $\mathcal{O}\!\left(\operatorname{poly}(d, \log(1/\varepsilon))\right)$ black-box oracle calls to the fixed-scale constrained resolvent. For monotone inclusions, our algorithm gives, to our knowledge, the first $\mathcal{O}\!\left(\mathrm{poly}(d, \log(1/\varepsilon))\right)$ black-box guarantee in the fixed-scale resolvent model.

---


### 331. [Using the Planted Clique Conjecture for Cryptography: Public-Key Encryption from Planted Clique and Noisy $k$-$\mathsf{LIN}$ Over Expanders](https://arxiv.org/abs/2611.11701)

**<font color=#1a73e8>作者：</font>** Riddhi Ghosal, Isaac M Hair, Aayush Jain 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We give a public key encryption scheme that is provably secure against poly-size adversaries, assuming $n^{\log^\alpha n}$ hardness of the standard planted clique conjecture, for any $\alpha \in (0,1)$, and a relatively mild hardness conjecture about noisy $k\mbox{-}\mathsf{LIN}$ over expanders that is not known to imply public-key encryption on its own. Both of our conjectures correspond to natural average-case variants of NP-complete problems and have been studied for multiple decades, with unconditional lower bounds supporting them in a variety of restricted models of computation. Our encryption scheme answers an open question in a seminal work by Applebaum, Barak, and Wigderson [STOC'10].

---


### 332. [Scalable Counterfactual Explanations for Time Series via Policy Learning](https://arxiv.org/abs/2611.11704)

**<font color=#1a73e8>作者：</font>** Peiyu Li, Pouya Hosseinzadeh, Soukaina Filali Boubrahimi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating counterfactual (CF) explanations for time series is challenging due to complex temporal dependencies and the computational inefficiency of traditional instance-specific optimization. We propose a policy learning framework for counterfactual explanation in time series, trained as a one-step contextual-bandit policy-learning problem. By training an actor-critic agent in the latent space of a pre-trained autoencoder, our method learns a transferable policy that captures global structural regularities. Unlike existing methods that rely on iterative optimization for each new input, the learned policy enables direct generation of valid and plausible counterfactuals through a single forward pass, avoiding per-instance optimization at inference time. Experiments on 13 UCR benchmark datasets show that our framework achieves high validity and strong plausibility across multiple anomaly detection metrics. Overall, by decoupling counterfactual generation from per-instance optimization, the proposed method provides an efficient and scalable alternative to existing approaches for time series counterfactual explanations.

---


### 333. [Variational Approach to Optimal IPS Estimator for Multi-logger Off-Policy Evaluation](https://arxiv.org/abs/2611.11712)

**<font color=#1a73e8>作者：</font>** Joon Suk Huh, Junghoon Seo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study off-policy evaluation (OPE) in contextual bandits with data collected from multiple logging policies. Inverse propensity scoring (IPS) is a standard approach to OPE and extends naturally to the multi-logger setting. However, as highlighted by Agarwal et al. [2017], neither balanced nor weighted IPS consistently outperforms the other in this setting. We resolve this dilemma by deriving an optimal IPS estimator with sample-dependent weights that minimize variance subject to unbiasedness. Using a variational calculus approach, we obtain closed-form optimal weights, yielding an estimator that is unbiased and achieves asymptotically optimal variance within a generalized weighted-IPS estimator class. Instead of a reward model, the estimator needs only a $K\times K$ matrix and a $K$-vector of moments, where $K$ is the number of logging policies, and we quantify how much efficiency this costs relative to the semiparametric oracle. Experiments on benchmark datasets show that our estimator generally improves on existing multi-logger IPS methods. We also extend our estimator to a doubly robust form by incorporating a conditional reward estimator. We compare the resulting DR extension with the semiparametrically efficient DR estimator of Kallus et al. [2021], both theoretically and empirically. We show that the two estimators achieve the same asymptotic variance when the conditional reward estimator is consistent, while our estimator can retain semiparametric efficiency under certain forms of reward misspecification. Empirically, the proposed DR estimator often achieves lower estimation error than the existing DR baseline.

---


### 334. [The Dark Matter of Clinical Data: An Identification Limit on Disentangling Physiology from Care Process in electronic health records](https://arxiv.org/abs/2611.11726)

**<font color=#1a73e8>作者：</font>** Mohammad Shahin, Krittaphas Chaisutyakorn, Dimitrios Proios 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representations learned from electronic health record (EHR) data encode patient physiology together with the clinical process that decides what is measured, when, and for whom. We formalize the data-generating process with latent physiology, ordering intent, laboratory values that exist only when measured, a learned representation, and clinical environments, and analyze two strategies for undoing this entanglement. First, no division of the information carried by laboratory "value" and "ordering" channels is identified from a single dataset: when ordering depends on the analyte, its distribution among untested patients is not recoverable, and a sentinel code for the undefined recorded value makes it carry all the entropy of the ordering indicator, fixing partial information decomposition (PID) for every redundancy measure satisfying the Williams-Beer axioms and invariant under injective re-encoding. Second, cross-site invariance of representation-conditional outcomes is a falsifiable implication of biological invariance taken jointly with exclusion and representation-sufficiency conditions, but not an identification strategy: we construct observationally equivalent models that disagree about biological invariance, whether the invariance test fails or passes. For binary physiology this happens exactly when case mix differs, the representation is lossy, and physiology affects the outcome. A worked example yields a 9.6-percentage-point cross-site gap under an unchanged biological mechanism. Tests performed for every patient remove the ordering gate, and measured tests can restore identification: biological invariance is identified when a test exactly summarizes outcome-relevant physiology, or, for binary physiology, when two tests with independent errors are available at sites with different case mix. Cross-site analyses should be reported as tests of a stated joint hypothesis.

---


### 335. [Can the Remaining Answers Change the Prediction? Worst-Case Stability Checks for Personalized Rating Models](https://arxiv.org/abs/2611.11733)

**<font color=#1a73e8>作者：</font>** Priyanka Siddappa, Muntaqim Ahmed Raju, Shifat Haider Al Amin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Missing ratings can overturn a personalized model's current prediction. For completed models with additive response scores, exact worst case bounds check all missing assignments without changing the current predictor. We evaluate this audit retrospectively in two self-triage cohorts, 108 clinicians rating three simulated psychiatric interviews, and 126 counseling demonstrations annotated by ten experts. Under shared random half histories, Fisher adaptation based on observed ratings reduces log loss relative to response frequency by 0.1071 nats in the clinician audit (95% CI [0.0867,0.1261]) and 0.0223 in counseling (95% CI[0.0121,0.0321]). The counseling test excludes target experts and source videos from training. Certification covers 5.4% and 10.5% of targets; fixed width acquisition raises coverage to 13.7% and 28.6% at the same budgets. With weights and responses held fixed, the observed-rating update also has lower loss than an affine partial update while certifying exactly the same evaluated targets. The certificate establishes agreement with the completed model, not correctness or stability at intermediate updates. These rating tasks test the method; clinical usefulness remains untested.

---


### 336. [A Bifurcation-Theoretic Framework for the Controllability of Emergent Intelligent Systems](https://arxiv.org/abs/2611.11734)

**<font color=#1a73e8>作者：</font>** Hao Li, Shaowen Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world intelligent systems must reconcile two demands: the adaptability conferred by emergence and the steerability required for accountable deployment. We show that these demands are governed by two distinct bifurcations on the same object and that, consequently, increased capability does not imply increased controllability. Emergence is a bifurcation of the capability variable $S$, with criterion $\Gamma:=\mathcal F'(0)>1$ equivalent to the existence of a unique positive stable fixed point of a self-consistency equation, following solely from the concavity of $\mathcal F$. Controllability is a bifurcation of the permission variable $c$, whose dynamics include an erosion term and exhibit a saddle-node fold with hysteresis as the gate criterion $\rho^\ast$ crosses unity. Three quantitative results follow: the critical exponent distinguishes families rather than classifying the transition; the gating-cost bound $K(M)\propto\log(1+M)$ grows with scope, not capability; and the fold threshold is $\gamma_c\approx4\mu\kappa$. Calibrated in both directions, the criteria reproduce the two-dimensional Ising transition, admit two true-feedback order parameters, and reject nine candidate quantities, supporting the conclusion that the order parameter is geometric rather than capability-related. Since permission cannot be endogenized and no deployed system has been measured to satisfy $\Gamma>1$ and $\rho^\ast>1$ simultaneously, increased capability does not imply controllability.

---


### 337. [Correctness Metric Matters: NWD-Based Calibration Loss for Tiny Person Detection in UAV Infrared Imagery](https://arxiv.org/abs/2611.11735)

**<font color=#1a73e8>作者：</font>** Tian Zhang, Zhirong Su  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detection calibration aligns predicted confidence with empirical correctness. Existing calibration losses inherit their correctness definition from box regression, specifically IoU against a hard threshold. We show that this target is geometrically ill-posed for tiny objects in UAV infrared imagery, where persons occupy less than 0.1\% of the image. The same pixel error is penalized more heavily as the target shrinks, so binary prediction calibration (BPC) actively suppresses confidences that should be high. On HIT-UAV, BPC with an IoU target degrades image-level localization-aware ECE (LaECE) from 0.0689 to 0.0761, 0.0649 to 0.0733, and 0.0653 to 0.0682 across Low, Mid, and High signal-to-clutter ratio (SCR) groups. We replace the IoU target with a continuous, scale-invariant normalized Wasserstein distance (NWD). The NWD target reduces LaECE\(_{\mathrm{NWD}}\) relative to BPC+IoU on all three groups (\(p<10^{-7}\)) with mAP neutral (0.9356 vs.\ 0.9347), and an independent center-offset anchor confirms that the gain is a genuine geometric correction. The improvement holds across a broad plateau of calibration weights. The NWD formulation requires no inference-time mapping layer. If a validation-fitted isotonic map is applied on top of it, calibration is lowered further, and the two corrections act on different components of the same error. The metric-level remedy has a measurable boundary. Target-background thermal pairing in the training distribution and detection-level aggregation under per-image detection-count heterogeneity lie outside it. Both are quantified independently of the NWD target.

---


### 338. [Dense Flow from Adaptive Correspondence](https://arxiv.org/abs/2611.11738)

**<font color=#1a73e8>作者：</font>** Cheng-Lin Hsieh, Stella X. Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical flow requires reliable matching from sufficient visual context and precise motion at every pixel. Existing methods such as WAFT match and estimate flow on the same coarse grids, then recover dense flow through learned upsampling, without explicitly linking visual support for matching to dense flow reconstruction. Our key insight is that dense pixel-level flow does not require equally dense matching. We decouple correspondence scale from flow resolution by adapting the size and shape of spatial supports to image structure for reliable matching, while reusing these supports for precise dense flow reconstruction. We realize this in Flow from Adaptive Token Estimation (FATE), whose token supports expand within coherent regions and contract near motion boundaries. Shared pixel-to-token associations pool features for matching and reconstruct pixel flow from token motions. Flow supervision jointly trains pixel grouping, token matching, and flow estimation without grouping labels, allowing FATE to anticipate which pixels are likely to move together from appearance alone. Trained on FlyingChairs/FlyingThings3D, FATE achieves the highest zero-shot accuracy on Sintel Final and KITTI, a critical setting given scarce real-world flow labels. For visible pixels, FATE improves accuracy within coherent regions, and more near motion boundaries. Its largest gains occur where direct matches are unavailable: Occluded or out-of-frame pixels account for roughly 10% of valid pixels but 50% of WAFT's total error. Experiments show that adaptive correspondence through pixel-to-token grouping enables reliable matching and precise pixel-level flow, improving generalization to unseen real scenes.

---


### 339. [Reproducible quantum clustering for single-cell transcriptome atlases](https://arxiv.org/abs/2611.11745)

**<font color=#1a73e8>作者：</font>** Henry Han  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current single-cell clustering pipelines discard most genes and can yield inconsistent clusters across random seeds. We introduce KQE-2, a training-free hybrid quantum-classical framework for reproducible whole-transcriptome clustering. KQE-2 maps cells into entanglement-free quantum states, enabling exact feature evaluation on classical hardware and direct checks on a quantum processor. Theoretically, we prove that removing entanglement is necessary and sufficient to bound single-qubit feature variance locally. Practically, while retraining scVI shifted 14% of cells and altered rare-type markers and drug targets, KQE-2 delivered identical biology across runs. On standard highly variable genes, the quantum encoding alone raised accuracy on a developing cortex from 0.61 to 0.79. KQE-2 scales to 11.4 million nuclei on one server, outperforming the compared methods on eight of ten complete atlases (and within the best method's run-to-run range on two), and leads on six even under standard downstream clustering.

---


### 340. [SpinSCI: Mask-Conditioned Spatial-Temporal Spin Transformer for Video Snapshot Compressive Imaging](https://arxiv.org/abs/2611.11753)

**<font color=#1a73e8>作者：</font>** Seungki Hong, Zhishuai Zhang, Taekwang Jang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video snapshot compressive imaging (SCI) recovers multiple frames from one spatiotemporally coded measurement. This paper proposes SpinSCI, a mask-conditioned Spatial-Temporal Spin Transformer whose Mask-Conditioned Ising Refinement Block (MC-IRB) combines attention logits and sensing information to form signed spin couplings. Finite mean-field updates gate residual feature refinement. Physics-guided initialization and final data consistency incorporate the measurement model. Compared with HiSViT$_9$, SpinSCI achieves average PSNR gains of 0.51 dB, 0.23 dB, and 0.04 dB on small-scale gray, mid-scale color, and large-scale color benchmarks, respectively, with 16.9% fewer parameters, 21.0-21.6% fewer FLOPs, 17.1-49.9% lower latency, and 62.3-63.3% lower peak memory. Relative to DU-9stg, average PSNR differs by at most 0.13 dB across these benchmarks, with 28.2-28.7% fewer FLOPs, 64.6-71.7% lower inference latency, and 30.1-35.0% lower peak memory. Qualitative comparisons on the real benchmark further show recovery of fine details and textures. Code and reference checkpoints are available at this https URL.

---


### 341. [Calibrated Alarm Thresholds for Compact Fire and Smoke Detectors](https://arxiv.org/abs/2611.11757)

**<font color=#1a73e8>作者：</font>** Vikas Sandireddy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compact object detectors such as YOLOv8n are a common choice for camera-based fire and smoke detection on low-power devices. These detectors are usually evaluated with box-level metrics such as mean average precision, and their outputs are turned into decisions with a fixed confidence threshold such as 0.25 or 0.5. A fire monitoring system, however, makes one decision per image: raise an alarm or not. In this paper we evaluate two publicly available compact detectors on the D-Fire test set at the image level. We compare three simple rules for turning box detections into one alarm score per image, and we use a split conformal procedure to choose the alarm threshold from held-out images so that the expected fraction of missed fire and smoke images stays below a chosen target. We find that the same fixed threshold leads to very different miss rates for the two detectors, 17.3 and 8.4 percent at a threshold of 0.5, while the calibrated threshold meets miss-rate targets of 10, 5 and 1 percent for both detectors and all three rules. At a 5 percent target, the false alarm rate on images without fire or smoke stays between 1.2 and 3.0 percent. We also find that smoke-only images stay below the target even when the overall target is met, and we describe the main failure cases.

---


### 342. [LangDepth: Vision-Language Scene Priors for Semantic Binning and Cross-Domain Monocular Depth Estimation](https://arxiv.org/abs/2611.11763)

**<font color=#1a73e8>作者：</font>** Reyhaneh Ahani Manghotay, Jie Liang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular depth estimation has advanced through large-scale pretraining and strong visual backbones, yet metric depth remains sensitive to scene-level scale. Indoor rooms and outdoor driving scenes occupy very different depth ranges, but most depth decoders infer this global structure implicitly from visual features. We ask whether scene-level semantic structure can instead act as an upstream prior that shapes the metric output space before dense prediction.
We present LangDepth (SemanticBins), a monocular depth architecture that couples strong visual features with a scene-conditioned output space. A frozen CLIP encoder and a learnable bank of scene- and geometry-oriented concept keys convert image features into a compact scene descriptor, without requiring per-image text or an external captioner. A Scene Prior Module (SPM) maps this descriptor to a scene-conditioned metric depth interval, providing a global range anchor before dense decoding. In parallel, a DINOv2-L backbone with a lightweight FPN extracts dense visual features, and a Per-Pixel Assignment Network (PPAN) assigns pixels to the scene-prescribed bin structure. A confidence gate fuses the dense visual estimate with the SPM prior.
We train LangDepth jointly on NYU Depth V2 and KITTI under a modest supervised depth budget, without web-scale depth supervision or pseudo-labelled depth data. A single model achieves delta_1 = 0.960 on NYU, 0.960 on KITTI, 0.887 on DIODE indoor, 0.946 on iBims-1, and 0.861 on SUN RGB-D. Beyond aggregate accuracy, the SPM predicts compact indoor ranges and much wider outdoor KITTI ranges, the gate becomes SPM-dominant on outdoor scenes, and perturbing the routed scene context causes large drops on KITTI and iBims-1. These results support scene-conditioned output spaces as a practical and interpretable mechanism for cross-domain monocular depth estimation.

---


### 343. [Towards Rotation-Only Imaging Geometry: Multi-View Pose Estimation](https://arxiv.org/abs/2611.11770)

**<font color=#1a73e8>作者：</font>** Xinrui Li, Qi Cai, Yuanxin Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Global structure-from-motion (SfM) commonly refines relative poses on individual image pairs and then estimates global rotations by rotation averaging. Pairwise refinement does not explicitly combine feature-level constraints with multi-view consistency during rotation initialization. We introduce Global Rotations from Aggregated Matches (GRAM), which estimates global rotations directly from initial relative rotations and inlier matches by minimizing edge-wise rotation-only algebraic residuals. GRAM replaces two-view relative-pose optimization and rotation averaging with a single stage. We further extend rotation- only imaging geometry to multiple views and develop Multi-view Optimization with Rotation-only Reprojection Error (MORE) for nonlinear global rotation refinement. Analytical Rotation-guided Translation (ART) derives locally scaled triplet translations from Linear Global Translation (LiGT) constraints and recovers global translations using weighted least squares. Synthetic and real-world experiments demonstrate the accuracy, robustness, and efficiency of the proposed methods.

---


### 344. [Wireless AI Networks: Co-Adapting Communication Resources and Distributed Intelligence](https://arxiv.org/abs/2611.11774)

**<font color=#1a73e8>作者：</font>** Ziqiang Ye, Yue Xiao, Qiyan Zhan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Distributed artificial intelligence (AI) increasingly relies on wireless networks, where communication and computing resources shape how AI tasks are configured and executed. However, resource availability alone does not determine how effectively these tasks can be supported, since different information selections and transmission strategies may yield different AI performance under the same resource constraints. To address this challenge, this article presents Wireless AI Networks as a unified design perspective for bidirectional adaptation between wireless communication and distributed intelligence. Specifically, an AI-executable resource budget characterizes candidate AI configurations, while task-level information value guides their selection and wireless resource allocation. Building on these principles, a wireless-AI co-adaptation framework coordinates resource abstraction, joint configuration and allocation, and execution feedback. Two complementary experiments illustrate this perspective: update selection and statistical correction improve federated learning under identical model-update payload budgets, while sensitivity-aware power allocation reduces model accuracy degradation under the same average transmit-power constraint. Together, these results highlight the importance of coordinating resource feasibility and task-level information value in distributed AI execution.

---


### 345. [Payoff-Aware Prediction of Population Game Dynamics](https://arxiv.org/abs/2611.11786)

**<font color=#1a73e8>作者：</font>** Kang Wang, Xiao Wang, Bo Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Population game dynamics describe how aggregate behavior evolves in response to payoff signals. In many applications, the payoff function may change, and the goal is to predict the population trajectory induced by a new payoff design before trajectory data under that design are available. We study this problem as $\textbf{payoff-aware prediction of population game dynamics}$. Standard dynamics learning methods fit the motion observed under training payoffs, but do not separate the payoff-dependent incentive from the payoff-independent response structure needed for prediction under new payoffs. Building on the existing framework of Riemannian game dynamics, we propose PA-RmD, a payoff-aware learning method that keeps payoff information explicit and learns the payoff-independent response structure from data. Theoretically, we show that the learned model preserves fixed-payoff Nash equilibria and derive finite-time one-step prediction bounds under shared-response and payoff-coverage conditions. Empirically, we evaluate PA-RmD on synthetic zero-sum and potential games, as well as a YouTube Trending multi-country dataset, showing that our method performs well under changing payoff designs.

---


### 346. [FMA-Net: Flexible Modality Adaptation for Robust Multimodal Face Presentation Attack Detection](https://arxiv.org/abs/2611.11790)

**<font color=#1a73e8>作者：</font>** Yuhao Gao, Yichen Shi, Zitong Yu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal face presentation attack detection (fPAD) improves robustness using complementary RGB, depth, and infrared (IR) cues, but deployment remains challenging when modalities are unavailable or incomplete. Existing flexible-modality methods mainly use zero-filling or modality omission, potentially discarding cross-modal information and introducing modality-dependent bias. We propose the Flexible Modality Adaptation Network (FMA-Net), a unified framework that compensates for missing modalities through instruction-guided latent-space translation. The Face Modality Instruct Translator (FMIT) estimates target modality observations from RGB inputs, while context-aware category enhancement uses learnable text prompts as modality-invariant semantic anchors. A Facial Feature Adapter (F2A) integrates global facial structure and local spoof-relevant cues to enhance discriminative representations. Synthetic-to-Real Face Domain Alignment (SR-FDA) reduces feature discrepancies between translated and real modalities, with benefits depending on the missing-modality pattern and data domain. Experiments on WMCA and PADISI-Face validate the framework. On WMCA with a 70% modality missing ratio, FMA-Net achieves a mean ACER of 3.22% across four intra-domain missing-modality protocols, compared with 4.24% for the strongest baseline by the same criterion. When both depth and IR are entirely unavailable, it achieves 5.23% ACER, compared with 5.99% for the best competing result. Cross-domain experiments also reveal limitations of synthetic-to-real alignment under dataset shifts. These results support FMA-Net as a practical approach to fPAD with flexible and incomplete modalities.

---


### 347. [APO2CS: Advantage-Aware Preference Optimization for Two-Level Constructive Search in Combinatorial Optimization](https://arxiv.org/abs/2611.11792)

**<font color=#1a73e8>作者：</font>** Kaixi Yang, Linbo Qiao, Wei Shang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preference optimization has emerged as a promising alternative to reward-based training for neural combinatorial optimization. However, existing methods typically rely on binary pairwise labels, which discard the magnitude of solution-quality differences and provide supervision only at the complete-solution level. We propose Advantage-aware Preference Optimization for Two-level Constructive Search (APO2CS), a preference-based training objective for constructive neural solvers that integrates both macro-level and micro-level supervision. At the macro level, APO2CS enriches pairwise preferences with an advantage term derived from objective-value differences. At the micro level, it compares partial trajectories, thereby providing denser supervision throughout the sequential construction process. The resulting objective can be used either to train a policy from scratch or to fine-tune a pretrained one. Experimental results show that APO2CS improves the expressiveness and search capability of preference learning for combinatorial optimization, while demonstrating strong effectiveness and adaptability across multiple combinatorial optimization tasks.

---


### 348. [Ultrasound-Assisted Biometric Watermarking Against Face Video Deepfakes](https://arxiv.org/abs/2611.11800)

**<font color=#1a73e8>作者：</font>** Guodong Liu, Lei Wang, Dongxu Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Currently, artificial intelligence-generated content (AIGC) poses a severe threat to facial video deepfakes, and many AIGC companies employ video watermarking to mitigate unauthorized fake video usage, but its effectiveness is limited due to watermark tampering and private-model forgery. Additionally, some schemes actively add watermarks to user videos. However, current approaches focus primarily on the quality of watermark embedding in offline scenarios, and no existing work offers a solution for protecting human facial videos in real-time online applications. To fill this gap, we propose, to the best of our knowledge, a novel biometric video watermarking method, UltraGuard, for the first time. It uses the smartphone's built-in speaker and microphone to emit ultrasonic signals and capture biometric features, which are then fused with spatio-temporal dynamic features derived from the video content. The fused features are encoded as watermarks and embedded into videos in real time, enabling dynamic, content-aware watermarking throughout transmission and propagation. Extensive experimental validation demonstrates that UltraGuard can effectively defend against malicious attacks such as forgery and editing, both at the source and during propagation, proving the system's efficacy. In the future, it can be deployed on users' mobile devices to provide real-time protection for users' facial videos, thereby preventing security and privacy breaches caused by various malicious attacks.

---


### 349. [Efficient Online Submodular Maximization with Bandit Feedback](https://arxiv.org/abs/2611.11808)

**<font color=#1a73e8>作者：</font>** Iasonas Nikolaou, Evimaria Terzi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online monotone submodular maximization under a cardinality constraint with bandit feedback. On each round, the learner selects at most $k$ elements from a ground set of size $n$ and observes only the value of the selected set. We develop an efficient algorithm achieving $O\!\left(k\sqrt{nT\log(n/k)}\right)$ expected $(1-1/e)$-regret over $T$ rounds. To our knowledge, this is the first polynomial-time algorithm with $\sqrt{T}$ dependence on the horizon for arbitrary monotone submodular functions in the bandit setting. Our approach uses randomized sampling and a carefully constructed potential to reduce online submodular maximization to online linear optimization over the probability simplex.

---


### 350. [CaseLaw: A Policy-Decoupled Framework for Training-Free Content Moderation](https://arxiv.org/abs/2611.11812)

**<font color=#1a73e8>作者：</font>** Qi Lu, Sen Li, Likun Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Content moderation is inherently policy-dependent: moderation boundaries are often subtle, subjective, and frequently updated, while conventional rule based or fine-tuning based systems require costly rule rewriting, model retraining, or system redeployment. We propose CaseLaw, a policy-decoupled and training-free framework for adaptive content moderation. CaseLaw reformulates moderation as precedent-based retrieval and voting, where multimodal content is transformed into evidence-preserved structured semantics, embedded into a stable semantic space, and classified by thresholded voting over retrieved precedent labels. We train NoteCap on a large-scale corpus of structurally annotated notes to ensure consistent semantic extraction and freeze it during subsequent policy adaptation, which requires no additional training. Policy adaptation is achieved by updating the semantic case library, including case labels and mappings, without retraining models or modifying prompts. To evaluate CaseLaw, we construct MFO-RedNotes, a benchmark for the male-female opposition risk domain. We additionally provide a five category CoPro comparison. Experiments show that CaseLaw consistently outperforms competing baselines in both precision and recall across policy-dependent risk levels and broader safety categories, with category-wise precision/recall reaching up to 86.8%/90.1% on MFO-RedNotes across both policy settings and 94.5%/92.3% on CoPro. Our work highlights the potential of precedent-based reasoning for policy adaptive content moderation and offers a practical direction toward more stable, transparent, and training-free moderation systems.

---


> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-520](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
