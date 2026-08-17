# 📦 其他研究 | 2026年08月18日

> 本类共 **165** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-165](./part-04.md)

---

### 101. [From Fixed Grids to Moving Particles:A Transferable Latent Operator for Fluid Dynamics](https://arxiv.org/abs/2608.14120)

**<font color=#1a73e8>作者：</font>** Meng Li, Chuqi Chen, Zhengqing Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Lagrangian modeling is vital to fluid dynamics, as it characterizes particle transport and complements the Eulerian this http URL, Lagrangian trajectories are less commonly available than Eulerian fields, while most neural operators are trained and evaluated primarily in the Eulerian representation. This mismatch motivates a new learning problem: can a model trained solely on Eulerian observations generalize zero-shot from Eulerian field prediction to Lagrangian particle rollout, without Lagrangian supervision or task-specific adaptation? To address this problem, we propose the Transferable Latent Operator (TLO), which learns a unified flow representation shared by Eulerian field prediction and Lagrangian particle rollout. TLO decouples latent flow evolution from coordinate-dependent decoding: querying the evolving latent representation at fixed spatial coordinates yields Eulerian fields, whereas querying velocities at particle positions and recursively updating these positions enables Lagrangian rollout. Across five fluid-dynamics benchmarks, TLO consistently outperforms existing neural operators in both Eulerian field prediction and zero-shot Lagrangian rollout, with further gains from limited Lagrangian fine-tuning.

---


### 102. [Overcoming Shortcut Learning in Graph Neural Networks through Active Explanation Guidance](https://arxiv.org/abs/2608.14121)

**<font color=#1a73e8>作者：</font>** Taraneh Younesian, Steve Azzolin, Antonio Longa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) can solve prediction tasks by unintentionally exploiting shortcuts---that is, edges, nodes, and features that correlate with but are not causal for the prediction---which compromise their reliability in out-of-distribution tasks. We introduce XIGL, an architecture-agnostic human-in-the-loop strategy for removing such shortcuts from GNNs. Our key insight is twofold. On the one hand, reliance on shortcuts can be detected by inspecting GNN explanations. On the other hand, once made aware of such shortcuts, sufficiently expert users can provide tailored corrective feedback, which helps deconfound the model. XIGL supports any query strategy; however, since corrective feedback can be expensive to acquire, we develop an active learning strategy for prioritizing explanations that are more likely to display shortcut behavior, lowering annotation and cognitive costs. We showcase the effectiveness of XIGL, including both existing and proposed explanation-based strategies, on several GNN architectures. Our implementation is available online.

---


### 103. [Reinforcement Learning-Based Production Scheduling in an Industry-Based Coating Scenario Using the Digital Model Playground](https://arxiv.org/abs/2608.14122)

**<font color=#1a73e8>作者：</font>** Arne Kröger, Ralf Buschermöhle, Wilhelm Hasselbring 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Production scheduling in complex manufacturing environments is challenging when sequence-dependent setup times, stochastic disturbances, and due-date constraints must be addressed simultaneously. While reinforcement learning (RL) methods have shown promising results in research, most studies rely on simplified benchmark processes, limiting their industrial relevance. This paper demonstrates the applicability of RL-based scheduling in an industry-inspired coating process that reflects practical complexities such as sequence-dependent setup times, machine breakdowns, and variable utilization. The open-source Digital Model Playground (DMPG), a discrete event simulation framework, is used to model the scenario and to train RL agents. Two standard algorithms, Deep Q-Networks and Proximal Policy Optimization, are benchmarked against conventional dispatching rules to illustrate feasibility and to provide a transparent testbed for further research. Results indicate that RL-based scheduling achieves balanced improvements across key performance indicators, with PPO delivering the most robust performance. The main contribution of this work is to bridge the gap between academic research and industrial practice by validating RL-based scheduling in a realistic, shareable scenario and by providing a reusable open-source framework for future studies.

---


### 104. [Traj-LeWM: Path-Aware World-Model Planning via Latent Trajectory Cost](https://arxiv.org/abs/2608.14125)

**<font color=#1a73e8>作者：</font>** Xiaodi Huang, Ziyi Ding, Jingtian Wan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LeWM is a lightweight visual world model that learns latent dynamics end-to-end from pixels and ranks candidate action sequences by the distance between their predicted endpoints and the goal. However, LeWM has two limitations. First, during training, it learns local next-step transitions without evaluating complete trajectories relative to the task goal. Second, during planning, it ranks candidates solely by predicted endpoint distance. Because model predictions may differ from actual execution outcomes, the candidate whose predicted endpoint is closest to the goal may not perform best when executed in the environment. The evolution of the complete predicted trajectory can therefore provide complementary information beyond endpoint distance. To address these limitations, we propose Traj-LeWM, which retains LeWM's local-dynamics objective and endpoint score while introducing a goal-conditioned latent trajectory cost (LTC) that aggregates trajectory-level information as a complementary signal. During training, LTC-based trajectory-preference supervision complements next-step prediction in shaping the shared representation. During planning, LTC is combined with endpoint distance to incorporate intermediate-path information into candidate ranking. With joint endpoint-plus-LTC scoring, Traj-LeWM outperforms LeWM on Push-T, OGBench-Cube, Reacher, and Two-Room by $3$, $14$, $7$, and $7$ percentage points, respectively. Controlled experiments and ablations further verify the complementary roles of trajectory-level representation shaping and path-aware candidate ranking.

---


### 105. [BGA: A noise-immune neural distillation framework for malicious signature extraction in high-entropy encrypted flows](https://arxiv.org/abs/2608.14126)

**<font color=#1a73e8>作者：</font>** Sheng Hong, Yixuan Huang, Weiwei Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> To mitigate attention dilution in high-entropy TLS 1.3 flows, we propose BGA, a noise-immune neural distillation framework for encrypted threat this http URL methodology first employs Analysis of Variance (ANOVA) to decouple high-discriminatory control-plane features - specifically industrial setpoints - from stochastic cryptographic noise. To resolve the extreme class imbalance within a corpus of 86,878 flow records, a Wasserstein GAN with Gradient Penalty (WGAN-GP) module, enforcing the 1-Lipschitz constraint, is integrated to synthesize high-fidelity minority samples, elevating the detection recall of rare Malicious State Command Injections(MSCI) attacks by 43.2%. At its core, the BGA architecture integrates Bidirectional Long Short-Term Memory (BiLSTM) for temporal dependency extraction and an Adaptive Gated Multi-Head Attention mechanism. This gated unit functions as a neural filter to dynamically suppress encryption artifacts while amplifying malicious signatures. Extensive evaluations on CIC-IDS-2018 and Edge-IIoT benchmarks demonstrate a performance ceiling exceeding 95.2% across all key metrics. Furthermore, noise-injection stress tests confirm BGAs superior structural resilience with a 8.57% performance margin over vanilla Transformers, while its ultra-low inference latency of 0.2820 ms (estimated 1.6920 ms via theoretical scaling for ARM) indicates a high potential for real-time feasibility on heterogeneous industrial edge gateways, providing a promising architectural baseline for future hardware implementation.

---


### 106. [HiCo-GS: Hierarchical Context Aggregation and Geometric Consistency for Octree Gaussian Splatting](https://arxiv.org/abs/2608.14136)

**<font color=#1a73e8>作者：</font>** Wei Zhang, Shengkai Yu, Shiqiang Gong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Octree-based anchor Gaussian Splatting has emerged as a scalable representation for city-scale novel view synthesis, where multi-level anchors adaptively capture scene content from coarse building structures to fine architectural details. However, we identify a fundamental limitation in existing methods: cross-level feature isolation, where each level's anchor features are optimized independently with no inter-level communication, causing color drift on building facades and over-smoothing in textured regions. We present HiCo-GS, a high-fidelity reconstruction framework with two complementary modules. Cross-Level Context Aggregation (CLCA) enables bidirectional hierarchical prior injection by leveraging the octree's spatial containment structure to aggregate per-level context vectors into parent-self-child triplets, fused via a lightweight MLP with residual connection. Coarse-level structural priors flow down to inform fine-level anchors, while fine-level detail statistics feed back to prevent over-smoothing, at negligible computational overhead. Depth-Normal Geometric Consistency (DNGC) regularization enforces agreement between rendered normals and depth-derived normals through an alpha-weighted consistency loss, complemented by edge-aware smoothness losses with progressive warmup that exploit the strong planar priors ubiquitous in urban geometry to suppress floating artifacts. We further introduce the China-Pagoda dataset comprising 8 ancient Chinese pagodas with over 1,200 images each, featuring dense ornamental carvings, curved multi-layer eaves, and repetitive fine-grained textures. Extensive experiments on Mill19, UrbanScene3D, MatrixCity, and China-Pagoda demonstrate that HiCo-GS achieves state-of-the-art rendering quality and substantially cleaner geometry across real-world and synthetic urban this http URL: this https URL.

---


### 107. [SPARGen: Unifying Spatial Perception and Reasoning through Native Multimodal Generation](https://arxiv.org/abs/2608.14138)

**<font color=#1a73e8>作者：</font>** Jinsheng Quan, Jianhua Li, Siyi Xie 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial perception and reasoning from visual observations require recovering geometric structure, establishing correspondences, and understanding spatial relations. Existing approaches typically address these capabilities separately using task-specific architectures or external geometric modules, limiting knowledge transfer among complementary representations of the same physical scene. We introduce SPARGen, a unified multimodal framework that casts 3D reconstruction, dense correspondence, and spatial reasoning as instruction-conditioned generation tasks. SPARGen serializes compact structured and linguistic outputs as token sequences while generating dense geometric fields in image-aligned forms, enabling spatial supervision to jointly shape shared representations within a native multimodal generative model. Experiments across benchmarks for 3D reconstruction, correspondence, and spatial reasoning show that SPARGen achieves competitive performance across heterogeneous spatial tasks within a single native multimodal generative framework.

---


### 108. [Smart routes: a system for development and comparison of algorithms for solving vehicle routing problems with realistic constraints](https://arxiv.org/abs/2608.14140)

**<font color=#1a73e8>作者：</font>** Andrew Soroka, German Mikhelson, Alexander Mescheryakov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The problem of route optimization with realistic constraints is becoming extremely relevant in the face of global urban population growth. While we are aware of approaches that theoretically provide an exact optimal solution, their application becomes challenging as the problem size increases because of exponential complexity. We investigate the Capacitated Vehicle Routing Problem with Time Windows (CVRPTW) and compare solutions obtaining by exact solver SCIP with heuristic algorithms such as LKH, 2-OPT, 3-OPT, the ORTools framework, and the deep learning model JAMPR. We demonstrate that for problem of size 50 deep learning and classical heuristic solutions became close to SCIP exact solution but requires less time. Additionally for problems with size 100, SCIP exact methods around 13 times slower that neural and classical heuristics with the same route cost and on around 50% worse for the first feasible solution on the same time. To conduct experiments, we developed the Smart Routes platform for solving route optimization problems, which includes exact, heuristic, and deep learning models, and facilitates convenient integration of custom algorithms and datasets.

---


### 109. [PISA: A Pseudo-Individual Source-Domain Feature Adaptation Framework for Test-Time Open-Vocabulary Object Detection](https://arxiv.org/abs/2608.14142)

**<font color=#1a73e8>作者：</font>** Ziyan He, Xiongtai Yang, Tao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary object detection test-time adaptation (OVOD-TTA) aims to address the performance degradation that pre-trained base models suffer when encountering image-domain shifts. Existing source-free OVOD-TTA methods rely either on refined test-time information for re-scoring or on pseudo-labels for self-training, leading to significant accuracy degradation when initial predictions are poor. Meanwhile, most conventional source-domain estimation methods recover abstract, sparse representations suitable for the classification task, but fail to capture the dense, concrete features required for detection. To address these issues, we propose PISA, a novel source-free OVOD-TTA method that can be seamlessly integrated into open-vocabulary visual backbones. The core components of our method are the Corruption-Invariant Feature Extractor (CIFE), the Feature Alignment Module (FAM), and a multi-scale alignment framework (BAA). To capture detection-suitable features, we develop CIFE to exploit the invariance of CLIP's visual features across corrupted images, ensuring robustness against various corruptions. We further develop FAM and BAA for the pre-training and adaptation to transform the corruption-invariant features into pseudo-individual source-domain features that are close to the original source-domain features. In this way, dense and concrete pseudo-individual source-domain features are used for supervision instead of unreliable pseudo-label signals. Experiments on the corrupted VOC-C, COCO-C, and LVIS-C benchmarks across three base models demonstrate that PISA substantially improves both the localization precision and the category recognition accuracy of the original models. Notably, PISA achieves state-of-the-art performance without requiring access to source-domain data, surpassing existing methods by 3.92% in AP@50% on COCO-C.

---


### 110. [CSG-Mamba: A Convolutional Scoring Gating Vision State Space Network for Endoscopic Polyp Segmentation](https://arxiv.org/abs/2608.14146)

**<font color=#1a73e8>作者：</font>** Yuliang Wang, Jiaqi Wu, Jiaye Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate polyp segmentation is critical for computer-aided colonoscopy, yet endoscopic images often contain low-contrast boundaries, mucosal texture interference, specular highlights, and device-dependent appearance shifts. Vision State Space Models (SSMs) provide efficient long-range modeling with linear complexity, but existing Vision Mamba segmentation models typically convert 2D features into 1D scanning sequences, which may weaken local geometric continuity and over-smooth irregular contours. We propose CSG-Mamba, a convolutional scoring gating Vision State Space network for endoscopic polyp segmentation. Built on a VM-UNet-style asymmetric U-shaped encoder-decoder, CSG-Mamba inserts a Convolutional Scoring Gating (CSG) module at the semantically rich bottleneck. CSG generates a local spatial score map through pointwise and large-kernel depthwise convolutions and recalibrates state-space features by multiplicative gating. Experiments with three random seeds show that CSG-Mamba achieves 0.9220 Dice and 15.87 HD95 on Kvasir-SEG, and 0.7418 Dice and 0.6570 mIoU on CVC-ColonDB, outperforming the baselines on most overlap and recall metrics while maintaining competitive boundary accuracy.

---


### 111. [SCVIB: Editable State-Conditioned Visual Instance Binding forMulti-Turn Personalized Localization](https://arxiv.org/abs/2608.14148)

**<font color=#1a73e8>作者：</font>** Xiongtai Yang, Ziyan He, Tao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce editable state-conditioned visual instance binding, a multi-turn localization setting in which several support-defined instances are introduced across turns and protocol-defined state events determine the final target. We instantiate this setting as SCVIB, comprising 1,050 manually verified support--query base pairs and 1,500 episodes spanning five visual domains, three difficulty levels, and four target-state dependency groups. Direct Seq-free inference reaches only 60.13\% Joint@0.5, indicating that resolving the final reference does not ensure effective use of the corresponding visual evidence for query-side localization. We address this gap with TT-VG (Transition-Tree Visual Grounding), which combines a Target-State Transition Tree (TSTT) with Visual Evidence Grounding Adaptation (VEGA). TSTT compiles the visible interaction into protocol-defined events, executes them over versioned target states, and resolves the final-query reference to the corresponding support evidence. Adapted on trajectory-derived same-instance pairs, VEGA performs support-conditioned grounding of the resolved instance using a Visual Evidence Package. TT-VG reaches 70.27\% Joint@0.5; under matched target resolution, VEGA exceeds the strongest comparison method by 16.20 points. Gains over direct inference are largest on Counter-Recency and Rollback, which require routing to non-latest or restored support evidence. Together, these results establish SCVIB as a controlled testbed and highlight the effective use of resolved support evidence for query-side same-instance localization as a central challenge in multi-turn personalized localization.

---


### 112. [QuaSAR: Quantization Compensation via Stable Activation-Aware Rank Truncation](https://arxiv.org/abs/2608.14149)

**<font color=#1a73e8>作者：</font>** Lin-Fa Lee, Yi-Yu Chang, Kuo-Hei Yeh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent training-free post-training quantization methods restore model accuracy through closed-form residual compensation. To constrain additional model storage overhead, several existing methods gate layer selection by goodness-of-fit, retaining only those layers whose compensation yields a positive residual fit score and discarding the rest. In this paper, we show that, under the low-bit W4A4 setting, this gating mechanism fails to distinguish poorly predictable quantization error from numerical solver failure. Rank-deficient input activations yield severely ill-conditioned or numerically singular Gram matrices, causing the closed-form solver to become unstable and produce spuriously negative fit scores. Consequently, existing goodness-of-fit gates misclassify affected layers as uncompensable and discard them. Many of these discarded layers can nevertheless provide substantial error recovery when their compensation is computed using a numerically stable solver. To address this problem, we propose a parameter-free truncated pseudoinverse solver which removes collapsed directions prior to inversion. On ViT-B with the W4A4 setting, our training-free method achieves 81.42\% top-1 accuracy, outperforming prior post-training methods and fine-tuning-based baselines. Combined with joint low-rank and quantization compression, the proposed method reaches a deployable operating point of 80.26\% accuracy at 54.7 MB, providing a well-balanced trade-off between model size and accuracy.

---


### 113. [Deep Reinforcement Learning solution for pickup and delivery routing problems with time window and capacity constraints](https://arxiv.org/abs/2608.14156)

**<font color=#1a73e8>作者：</font>** Andrew Soroka, Alex Meshcheryakov, Sergey Gerasimov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The task of constructing vehicles optimal routes for pickup and delivery of goods is one of most promising tasks in the context of global urban population growth. Although this kind of problems with small size can be solved by various classical approaches, a fast (or realtime) route optimizer under the constraints of the real world (such as capacity and time windows constraints) for medium-large size problems still remains a highly challenging task. In this work we, for the first time, successfully applied a deep Reinforcing Learning approach (modified JAMPR model) to solve Pickup and Delivery problem with Capacity and Time Window constraints (CPDPTW). We obtained a robust model that gives a fast optimal solution for problems of small and medium size, and gives fast suboptimal solution for problems of larger (> 200) size.

---


### 114. [Removing Temporal Note Redundancy Improves Multimodal Reinforcement Learning for Medicine](https://arxiv.org/abs/2608.14157)

**<font color=#1a73e8>作者：</font>** Chenran Weng, Joo Seung Lee, Malini Mahendra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mechanical ventilation is a critical life-support intervention, requiring dynamic adjustments to ventilator settings as a patient's condition evolves. While reinforcement learning (RL) offers a promising framework for optimizing these sequential decisions, standard approaches rely primarily on structured electronic health record (EHR) data, missing crucial clinical context recorded in free-text notes. Integrating longitudinal clinical notes into RL state spaces is challenging because notes are heavily inflated by temporal redundancy, such as copy-forward text, templating, and repetitive documentation, which dilutes time-local updates and degrades state representation quality. To address this, we propose a redundancy-aware multimodal state representation framework that explicitly removes duplicated note text over time before policy learning. We evaluate two computationally efficient temporal decomposition strategies for removing duplicated note text: (1) an embedding-space decomposition using singular value decomposition on local history subspaces, and (2) an interpretable sentence-level diff operation that filters out previously documented sentences before text encoding. Using real-world ICU data, we demonstrate that state representations constructed by stripping temporal note redundancy significantly outperform both structured-only and raw-note baselines across multiple off-policy evaluation methods (Model-Based Rollouts, Fitted Q-Evaluation, Weighted Importance Sampling, and Weighted Doubly Robust Evaluation). Our findings show that explicitly isolating new clinical information from repeated note text yields higher-quality state representations and directly improves RL performance for clinical decision support.

---


### 115. [Concept Guidance: Precise, Training-Free Latent Control for Text-to-Image Generation](https://arxiv.org/abs/2608.14172)

**<font color=#1a73e8>作者：</font>** Nikolai Röhrich, Isabell Hans, Felix Krause 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models have two major drawbacks that severely limit their practical utility: (1) standard models lack an intrinsic mechanism for continuous, concept-specific guidance (e.g., for precisely controlling how aesthetically pleasing an image looks), and (2) they lack reliability for tasks requiring high local coherence (e.g., generating text or human hands). To tackle these issues, we introduce a novel notion of concept-wise mutual information and find large, concept-dependent differences between individual layers, demonstrating that the generation of specific structures is localized in distinct parts of the network. We exploit this insight by reinforcing the impact of concept-relevant layers in Concept Guidance (CoG), a precise, target-specific guidance method that works for models out-of-the-box without additional training, external models, gradients, or prompt engineering. CoG first quantifies each layer's concept-specific impact and then guides denoising using a weighted combination of predictions generated with concept-relevant layers skipped. We demonstrate performance increases across various targets and popular models like PixArt-alpha, SD3, SD3.5, and FLUX.1-dev. Code is available at this https URL

---


### 116. [Physics-Bounded mmWave Sensing for Schedulable, Privacy-Preserving Human Pose Estimation](https://arxiv.org/abs/2608.14176)

**<font color=#1a73e8>作者：</font>** Shuntian Zheng, Hongyang He, Jiaqi Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Millimeter-wave (mmWave) is a promising modality for human pose estimation (HPE) in mobile deployments with strong privacy requirements and limited resources, such as fall detection in bathrooms or activity monitoring in bedrooms, where cameras are inadmissible and computationally demanding processing is infeasible. Although mmWave signals naturally confine human reflections to compact, physically bounded regions, the algorithmic foundations of existing systems fail to provide deterministic execution and accuracy guarantees. They either process the full spectrum uniformly, resulting in unpredictable latency that varies across different scenes, or apply lossy compression that discards vital pose structures. To address this, we present PRISM, a framework that exploits the spatial concentration of RF reflections to achieve schedulable edge HPE. PRISM introduces three core components: 1) Physics-Bounded Integral Processing (PBIP), which restricts computation via constant-time integral queries; 2) Physics-Adaptive Instance Proposal (PAIP), which decomposes scenes involving multiple people into bounded local subproblems; and 3) Deadline-Aware Operation Profiles (DAOP), which provide offline-verified worst-case bounds for runtime quality-latency trade-offs. We evaluate PRISM on four public datasets spanning diverse radar configurations, reporting physical-bound and pose-accuracy measurements across this suite and examining deadline-aware scheduling on multi-person recordings together with an additional single-person set. Under single-threaded isolated execution, PRISM reduces 99th-percentile latency by 24\%--58\% relative to baselines that miss the deadline, records a 0.0\% miss rate on the evaluated traces, and attains the highest pose accuracy among deadline-feasible configurations, providing a practical route toward schedulable mmWave sensing on mobile edge hardware.

---


### 117. [Structure-Guided Spatiotemporal Attention Graph Neural Network for Traffic Flow Prediction](https://arxiv.org/abs/2608.14177)

**<font color=#1a73e8>作者：</font>** Xuanmian He, Can Li, Wanjing Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep spatiotemporal models integrating graph convolutions and attention mechanisms have demonstrated excellent performance in network-level traffic flow prediction, owing to their exceptional ability to capture complex spatiotemporal dependencies. Despite their predictive success, deployment of such models in safety-critical urban systems remains constrained by their inherent lack of transparency. Existing post-hoc diagnostic methods often struggle with spurious correlations and fail to unveil the intrinsic decision-making mechanisms governing traffic dynamics, resulting in suboptimal interpretability and limited operational trustworthiness. To address these challenges, this paper proposes the Structure-Guided Spatiotemporal Attention Graph Neural Network (SGSAN). Departing from traditional architectures that rely on unconstrained adaptive graphs, SGSAN explicitly learns a static Directed Dependency Graph (DDG) to identify the invariant macroscopic propagation paths of traffic states. We further introduce an InfoNCE-based soft-coupling mechanism that anchors the model's dynamic spatiotemporal attention to this structural prior, offering a mechanistic account of the model's decision-making process while ensuring robust forecasting by aligning attention-based reasoning with identified macroscopic dependencies and preventing over-reliance on ephemeral local noise. Furthermore, a decoupled two-stage optimization framework is developed to resolve the fundamental conflict between structural discovery and predictive error minimization. Extensive experiments on multiple real-world datasets demonstrate that SGSAN achieves state-of-the-art predictive accuracy while providing built-in interpretability that organically aligns with the physical logic of traffic networks.

---


### 118. [LightTeaNet: A Weakly Supervised Lightweight CNN for Multi-Label Tea Leaf Disease Detection and Localization](https://arxiv.org/abs/2608.14178)

**<font color=#1a73e8>作者：</font>** Naif Haider Chowdhury, Md Rahim, Syed Farhan Hasan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tea is known as an important crop in many parts of South and Southeast Asia, yet the production of tea is still hampered by the multiple diseases that decrease the quantity and quality. Traditional methods of inspection, which are manual, are not consistent, labor-intensive, and depend on extensive monitoring. This paper introduces a lightweight convolutional neural network (CNN) designed for weakly supervised multi-label classification and disease localization in tea leaves called LightTeaNet. LightTeaNet learns directly from image-level labels and employs Class Activation Mapping (CAM) to localize disease-affected regions automatically, unlike conventional object detection models such as YOLO, which require extensive bounding box annotations. For Parameter efficiency, the network integrates Depthwise Separable Convolutions, and for enhanced feature discrimination, it integrates Channel Attention. LightTeaNet has achieved a Precision of 0.9615, a Recall of 0.8772, and an F1-score of 0.9179, while it shows mAP@0.50=0.1810 without any manual annotations, which delivers a competitive localization performance in the experimental results. These results validate the model as an interpretable as well as a resource-efficient framework for intelligent disease monitoring in agriculture.

---


### 119. [Revisiting Energy-based Tabular Anomaly Detection: Energy and Reconstruction are Complementary](https://arxiv.org/abs/2608.14186)

**<font color=#1a73e8>作者：</font>** Junichiro Niimi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular anomaly detection is dominated by classical density-proxy methods (Isolation Forest, OCSVM, LOF), reconstruction-based detectors (Autoencoders, VAEs), and modern non-parametric scorers (COPOD, ECOD, Deep SVDD), all of which approximate the inlier distribution only indirectly; explicit energy-based models are largely absent. Motivated by the recent revival of EBMs in deep learning (e.g., Energy-Based Transformers, JEPA), we revisit the classical Deep Boltzmann Machine (DBM) for this task and hypothesize that its mean-field energy combines more effectively with a reconstruction-based score than same-lineage pairs do. We evaluate a two-hidden-layer DBM on two tabular benchmarks spanning distinct domains (UCI Bank Marketing and NSL-KDD) against eight classical and modern baselines across twenty random seeds. The DBM mean-field energy matches the strongest baseline (the Autoencoder) on Bank Marketing and statistically beats it on NSL-KDD, while significantly outperforming the remaining seven on both datasets. When fused with the Autoencoder via rank fusion, the DBM energy yields a statistically significant improvement on both datasets (AUROC=+0.014, p<0.01 on Bank Marketing; +0.002, p<0.001 on NSL-KDD); every non-DBM-derived base model instead fails to improve or significantly degrades the AE-paired ensemble. Our position is that classical EBMs, exemplified by the DBM, deserve a place in the tabular anomaly detection toolbox as a non-redundant complementary view to the reconstruction-based scores that dominate current practice.

---


### 120. [Adaptive Protection for Evolutionary Feature Construction in Symbolic Regression with Application to Credit Classification](https://arxiv.org/abs/2608.14209)

**<font color=#1a73e8>作者：</font>** Hengzhe Zhang, Qi Chen, Bing Xue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evolutionary feature construction has shown strong promise in symbolic regression by automatically discovering informative transformations of input features that enhance a simple base learner. However, existing approaches often lack explicit mechanisms to preserve important constructed features discovered during evolution, and valuable genetic material can be lost when genetic operators disrupt effective features. This paper introduces an adaptive protection mechanism that leverages feature importance metrics to selectively preserve constructed features during evolution. The mechanism provides stronger protection for more important constructed features while still allowing less important features to be modified and to incorporate useful building blocks from more important features. We evaluate the approach using multiple feature importance calculation methods and demonstrate its robustness across different base learners. Experimental results on 98 regression benchmark datasets show that the proposed mechanism consistently improves solution quality over baseline approaches, and experiments on two credit classification datasets demonstrate that the method also extends effectively to improve search effectiveness beyond symbolic regression.

---


### 121. [Connected Subspace Clustering: Hardness, a Scalable Heuristic, and an Application to Sea Level Geodesy](https://arxiv.org/abs/2608.14215)

**<font color=#1a73e8>作者：</font>** Johanna Hillebrand, Jan Höckendorff, Jürgen Kusche 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constrained optimization extends classical optimization by integrating side information, making it widely applicable across scientific and engineering domains. Consider a setting where we measure variables at different physical locations. When grouping these measurements, we often want clusters that are both internally similar and physically coherent. Thus, we have a constrained clustering problem where the constraint models coherence. Motivated by an application in geodesy, where contiguous regions of the sea surface must be identified for principal component analysis, we introduce the Connected Subspace Clustering problem: given high-dimensional points and a connectivity graph, partition them into $k$ connected clusters, minimizing their total squared distance to the clusters' best-fit $m'$-dimensional affine subspaces. We prove that, even for $m' = 0$ and a grid graph with holes, the problem is NP-hard to approximate within $\Omega(n^{1/2-\varepsilon})$ for every $\varepsilon>0$, where $n$ is the number of measurements. We then introduce an efficient Lloyd-style heuristic that alternates subspace fitting with an iterative merging procedure to enforce connectivity. Our method returns exactly $k$ connected regions by construction, whereas unconstrained methods leave up to $1{,}966$ disconnected fragments at higher cost. In a study of 160 configurations on global sea level time series, our merging-based repair is the strongest of four strategies in $73.75\%$ of cases, and consistently outperforms competitors such as (connected) Ward's method across all tested cluster counts. The resulting regions isolate signals aligning with climate indices such as the El Nino-Southern Oscillation and Indian Ocean Dipole. Although developed for geodesy, the approach applies to other spatially embedded multivariate time series, such as climate fields, remote sensing, neuroimaging, and sensor networks.

---


### 122. [A Generalized Parallelogram Rule for Proportional Analogies on Riemannian Manifolds](https://arxiv.org/abs/2608.14220)

**<font color=#1a73e8>作者：</font>** Pierre-Alexandre Murena, Marcelo Hartmann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Analogies are quaternary relations of the form "a is to b as c is to d", usually denoted a : b :: c : d. This notion is formalized in particular with the notion of proportional analogy, which imposes some constraints on the valid analogies. Whereas proportional analogies have been studied mostly in symbolic domains and in vector spaces, their use is limited in non-Euclidean spaces. In this paper, we introduce a proportional analogy relation in Riemannian domains, extending the parallelogram rule used for arithmetic analogies in Euclidean spaces. We illustrate the introduced analogy on various manifolds, such as the sphere, shape spaces and manifolds of probability distributions.

---


### 123. [MathForm: Scaling Mathematical Autoformalization with Knowledge Retrieval and Verification-Guided Refinement](https://arxiv.org/abs/2608.14221)

**<font color=#1a73e8>作者：</font>** Lushi Pu, Weiming Zhang, Xinheng Xie 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoformalization is commonly framed as translating natural-language mathematical statements into machine-verifiable formal languages such as Lean 4. However, faithful formalization requires more than translation. Models must map mathematical concepts to the complex hierarchy of types and definitions in formal libraries such as Mathlib, while ensuring that generated statements preserve the meaning of the source propositions. Existing approaches struggle because they rely heavily on the model's parametric memory for library-specific knowledge, while common data construction pipelines often resort to filtering single-pass outputs and lack mechanisms for feedback-driven revision. To address these challenges, we introduce MathForm, an autoformalization framework for constructing verified training data through Mathlib knowledge retrieval and verification-guided iterative refinement. Before generation, a retrieval planner gathers relevant definitions and existing formalizations from Mathlib to guide the formalization generator. Generated statements are then revised using compiler diagnostics and semantic-consistency feedback. Using this framework, we construct FormalVerse, a Lean 4 dataset containing approximately 367K verified examples across diverse mathematical domains and sources. We then train MathForm-8B through supervised fine-tuning followed by reinforcement learning. Across six benchmarks, MathForm-8B achieves average Pass@8 rates of 88.06% under Syntax Check (SC) and 72.37% under Consistency Check (CC), outperforming multiple specialized 32B autoformalizers. On the challenging FATE-H and FATE-X subsets, it attains CC pass rates of 63% and 37%, exceeding the strongest specialized baselines in both cases.

---


### 124. [AppleScab-LT: A Longitudinal Real-Field Apple Scab Dataset for Temporal Disease Progression Analysis](https://arxiv.org/abs/2608.14235)

**<font color=#1a73e8>作者：</font>** Aamir Hilal, Shabir Ahmad Sofi, Neeraj Goel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The development of reliable plant disease monitoring systems is constrained by limited longitudinal datasets capturing disease progression under natural field conditions. Although existing plant disease datasets have advanced image-based recognition, most consist of static images acquired at a single time point, limiting analysis of temporal disease evolution and severity progression. To address this gap, this study presents AppleScab-LT, a longitudinal real-field dataset developed to monitor apple scab progression through repeated observations of individually tracked infected leaves. Guided by a research-question-driven framework, the dataset was systematically developed, validated, and characterized for reliable longitudinal disease analysis. AppleScab-LT was constructed through systematic orchard monitoring under natural environmental conditions, incorporating longitudinal leaf tracking, expert-guided disease verification, polygon-based annotation, leaf isolation, disease severity quantification, and temporal sequence construction. A comprehensive quality assurance framework, including standardized annotation protocols, expert validation, automated integrity checks, sequence-level verification, and temporal consistency analysis, was applied throughout curation. The dataset contains 21 longitudinal leaf sequences, 2,101 high-resolution images, and 264 progressive temporal samples from repeated monitoring of same infected leaves. It captures variability in severity accumulation, progression rates, monitoring duration, and inter-leaf progression. Quantitative disease descriptors based on pixel severity, color-intensity severity, and normalized relative severity provide standardized measurements for temporal disease analysis. AppleScab-LT provides a reliable resource for temporal disease intelligence, disease progression modelling, precision agriculture, and future crop health monitoring

---


### 125. [Zero-Shot Skeleton-Based Action Anticipation](https://arxiv.org/abs/2608.14243)

**<font color=#1a73e8>作者：</font>** Hongsong Wang, Pengbo Yan, Yang Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action anticipation (AA) aims to recognize ongoing human or humanoids actions from partial observations, enabling robots to predict intentions before the actions are completed. Although skeleton-based AA offers efficiency advantages, existing approaches assume that all action classes are seen during training, which limits their deployment in real-world scenarios where novel actions inevitably arise. To address this gap, we study the new task of Zero-Shot Skeleton-Based Action Anticipation (ZS-SkAA). This task requires recognizing unseen action classes using only limited early-stage skeleton sequences, combining the challenges of partial observations, temporal dynamics, and zero-shot generalization. To establish foundational research for ZS-SkAA, we introduce:(1) A baseline model comprising a spatio-temporal feature extractor and a mutual information estimation and maximization module. This baseline model explicitly aligns partial visual features with semantic class embeddings across modalities by estimating and maximizing their mutual information, enhancing generalization to unseen classes.(2) A benchmark protocol using the NTU RGB+D dataset, which is adapted for rigorous ZS-SkAA evaluation. Experiments demonstrate the effectiveness of our model as a strong baseline for ZS-SkAA, achieving high zero-shot accuracy on NTU RGB+D. This work establishes ZS-SkAA as a vital research direction for real-world systems requiring generalization to novel actions.

---


### 126. [Polaris : Multi Agentic System for Conversational Enterprise Analytics](https://arxiv.org/abs/2608.14246)

**<font color=#1a73e8>作者：</font>** Varuni H K, Soham Sarkar, Jay Kumar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In today's fast-paced environment, the ability to swiftly access, understand, and act on data is no longer optional; it is essential. Yet most organizations remain data-rich but insight-poor, constrained by the complexity of querying, interpreting, and explaining enterprise-scale information. We present Polaris, a supervisor-led multi-agent framework for conversational enterprise analytics that bridges this gap. Polaris introduces Dynamic Task Coordination (DTC), a decision-theoretic orchestration layer that models agent-task assignment as adaptive bipartite matching, enabling real-time coordination, recovery, and optimization across specialized agents for querying, visualization, and reasoning. By coupling DTC with reason-first, ReAct-style agents, Polaris transforms natural-language queries into coherent analytical workflows that not only retrieve and visualize data but also explain the underlying "why." Evaluation on structured enterprise datasets demonstrates high semantic fidelity and answer relevancy, underscoring the potential of multi-agent orchestration to deliver trustworthy, end-to-end business intelligence at scale.

---


### 127. [Learning to Forecast Crop Growth from Earth Observation Data](https://arxiv.org/abs/2608.14281)

**<font color=#1a73e8>作者：</font>** Dominik Senti, Mehmet Ozgur Turkoglu, Michele Volpi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forecasting crop growth across agricultural landscapes is important for improving the productivity, resilience, and operational management of farming systems. In this work, we investigate whether Earth observation time series and meteorological drivers can be used to predict future canopy development at country scale. We focus on winter wheat and formulate crop growth prediction as forecasting future leaf area index (LAI) trajectories beyond the last available Sentinel-2 observation. We evaluate this task on a multi-year dataset which spans the entire country of Switzerland, containing over 20 million pixel-level Sentinel-2-derived LAI time series paired with meteorological variables. Because cloud cover and revisit gaps leave LAI supervision sparse, models fit the few valid (cloud-free) LAI observations yet oscillate implausibly between them, producing trajectories no real canopy could follow. We introduce a lightweight unimodal shape regulariser which improves trajectory plausibility with negligible loss in accuracy. We compare deep learning sequence-to-sequence (Seq2Seq) models with classic machine learning baselines and show that Seq2Seq models generalise well across years, achieving $\mathrm{R}^2$ above 0.8 and consistently outperforming conventional approaches. Together, these results demonstrate that remote sensing and weather-driven sequence modelling can learn crop growth dynamics at landscape scale. S

---


### 128. [MAGneT-3D: Monocular and Domain-Generalizable Temporal 3D Detection](https://arxiv.org/abs/2608.14282)

**<font color=#1a73e8>作者：</font>** Mohamed Kotb, Johannes Meier, Christoph Reich 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular temporal 3D detection aims to detect objects in 3D, given a monocular video. Query-based 3D detectors unify detection and cross-view association, but their learnable queries fit the spatial distribution of the training data (e.g., field-of-view). We show that this issue is especially severe when these models are applied to monocular video, hindering generalization to unseen datasets and environments. To address this limitation, we introduce MAGneT-3D, the first method for domain-generalized monocular temporal 3D object detection. Instead of relying on static learnable queries, we propose a Domain-Robust Anchor Generator (DRAG) approach that adaptively derives 3D proposals during inference. To further enable domain generalization, we propose a Temporal Refinement and Identity Merging (TRIM) strategy, reducing dependence on specific 3D proposals. To enable comprehensive domain-generalization evaluation, we establish a cross-dataset benchmark spanning nuScenes, Waymo, Lyft, and ONCE. Under zero-shot domain shifts, MAGneT-3D outperforms all baselines, improving NDS from 12.1% to 18.6% while also increasing in-domain accuracy.

---


### 129. [Convex losses and their applications to SVM, SVR, and Shallow Neural Networks](https://arxiv.org/abs/2608.14288)

**<font color=#1a73e8>作者：</font>** Filippo Portera  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose multiple new convex losses for SVM and Neural Networks, applied to binary classification tasks. While there are practical limitations in exploiting them with the dual SVM models, we are able to use them with SVM primal formulation and Neural Networks. In detail, the primal SVM problem with the modified losses has been solved with the Particle Swarm Optimization algorithm. We prove that the proposed losses are a generalization of the standard loss, and we experiment them with several small data-sets. This preliminary study shows that using pattern correlations
inside the loss function could in theory enhance the generalization performances on some data-sets. To evaluate the performance of each loss, we adopt a Nested Cross-Validation procedure. Results show that generalization measures are the same with or without the new losses.

---


### 130. [Human and Artificial Intelligence - Promoting Trustworthy and Understandable Collaboration](https://arxiv.org/abs/2608.14291)

**<font color=#1a73e8>作者：</font>** Gilbert Drzyzga  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Methods of Artificial Intelligence (AI) enable the personalization of information for individual user experiences in many domains; however, they can also conflict with established design principles, e.g., due to uncertainties regarding the real world. Building trust and understanding can serve as an approach to create a more balanced relationship between humans and AI. Building upon a pilot study, an online survey was conducted to investigate 12 individual aspects related to the topics of explainability and controllability. The results indicate that both topics, despite their different and numerous facets, are generally perceived as important by respondents; simultaneously, however, a wide dispersion of opinions is frequently observed. This could be an indication that, alongside a fundamental consensus, individual perspectives, technical knowledge and understanding, context-specific factors, or personal experiences play a role in the perception of such systems.

---


### 131. [Conditional Neural Optimal Transport for Predicting Cellular Phenotypes from Molecular Structure](https://arxiv.org/abs/2608.14293)

**<font color=#1a73e8>作者：</font>** Gauthier Avité, Maxime Sanchez-Renauld, Nicolas Bourriez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-content microscopy enables systematic profiling of cellular responses to chemical perturbations, but the scale of the chemical space makes exhaustive phenotypic characterization experimentally infeasible. This motivates computational models that can predict image-derived phenotypes without acquiring the corresponding treated cells. We formulate molecule-induced phenotype prediction as an inductive conditional transport problem in image representation space. Given a negative-control phenotype and the structure of a molecule, we aim to predict the phenotype induced by the corresponding molecule. We first evaluate classical optimal transport baselines and show that static couplings do not yield useful predictions on large-scale phenotypic image datasets. We then introduce a molecule-conditioned Neural Optimal Transport (NOT) model with a Monge-Gap regularization training objective that learns to transport negative-control unperturbed phenotypes toward perturbed phenotypes using molecular structure as conditioning information. NOT recovers molecule-specific phenotypic effects while reducing microscopy-associated technical variation, thereby facilitating comparisons across experimental batches. On unseen active molecules, the model outperforms baseline approaches, demonstrating that chemically conditioned transport can generalize beyond the molecules observed during training. We identified the molecular encoder as the main limitation to this generalization, while transport in a compressed representation space improves performance and scalability. These results establish NOT as a promising framework for predicting cellular phenotypes from molecular structure and negative-control phenotypes, while highlighting the development of more informative molecular representations as a key direction for improving out-of-distribution performance.

---


### 132. [Sensor-Driven Mission Synthesis for UAV/UGV Swarms: A TB-CSPN Coordination Architecture with Hardware-Enforced Safety](https://arxiv.org/abs/2608.14306)

**<font color=#1a73e8>作者：</font>** Uwe M. Borghoff, Paolo Bottoni, Remo Pareschi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents a coordination architecture for heterogeneous UAV/UGV swarms that synthesises mission actions from uncertain, multi-modal sensor evidence while preserving hardware-enforced safety at the actuation boundary. The approach combines radar, RF, acoustic, and visual observations with Topic-Based Communication Space Petri Net (TB-CSPN) orchestration to support incremental mission formation under partial and evolving information. Consultant agents transform sensor outputs into temporally bounded semantic tokens, while supervisor agents provide authorisation and policy-governed release of mission transitions. This separation between interpretation, coordination, and execution yields auditable decision paths, constrains non-determinism within the coordination layer through guards and synchronisation, and enables bounded-time integration of heterogeneous evidence. To improve resilience in contested environments, including cyber compromise, spoofing, jamming, and communication loss, the digital coordination layer is complemented by independent analogue safety envelopes that clamp or veto unsafe actuator commands issued to individual vehicles. A coastal-surveillance case study illustrates how the proposed architecture enables dependable, governed, and physically safe swarm coordination under operational uncertainty.

---


### 133. [Intelligent Detection of Mechanical, Electrical, and Plumbing (MEP) Metrics Based on 2D Floor Plans](https://arxiv.org/abs/2608.14317)

**<font color=#1a73e8>作者：</font>** Tarandeep Singh Mandhiratta, ANK Zaman, Abdul-Rahman Mawlood-Yunis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This research developed a neural network-based model to extract various information from 2D floor plans. We detect lighting symbols, identify the appropriate type of light, and extract the associated texts with lights. The study aims to enable efficient floor designing and determining the number and type of lights needed per floor, i.e., allow efficient design and estimate the power requirement of the floor plan. The model was developed using Mask RCNN as the base. The images were annotated and converted into a Coco data format for training the model. The model achieved bbox\_mAP and segm\_mAP values of 0.7596 and 0.7111, respectively. It also performed well at different IoU thresholds, i.e., with bbox\_mAP 50 and segm\_mAP 75 values of 0.9850 and 0.9219, respectively. The developed model will help various industries, such as architecture and construction, to improve design time and create efficient workflows by automatically detecting Mechanical, Electrical, and Plumbing (MEP) objects from floor plans, and it is the first step towards building tools that will help energy-efficient building design.

---


### 134. [Quantum Multi-Armed Bandits and Linear Bandits: Lower Bounds and Algorithms](https://arxiv.org/abs/2608.14319)

**<font color=#1a73e8>作者：</font>** Maoli Liu, Zhuohua Li, John C.S. Lui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study quantum multi-armed bandits (QMAB) and quantum linear bandits (QLB) in the model of Wan et al. [2023], where the learner queries each arm or action through a quantum reward oracle or its inverse. Prior work gives algorithms over horizon $T$ with regret $O(K\log T)$ for QMAB with $K$ arms and $O(d^2\operatorname{polylog} T)$ for $d$-dimensional QLB. This leaves open whether the $K\log T$ scale is unavoidable and whether the $d^2$ dependence can be improved. We prove the first minimax lower bounds of $\Omega(K\log(T/K))$ for QMAB and $\Omega(d\log(T/d))$ for finite-action QLB, resolving the question raised by Wan et al. [2023] of whether regret independent of $T$ is achievable. At the heart of our argument is a high-confidence single-arm quantum testing lower bound for distinguishing a fixed reward mean from an interval of alternatives, proved by the polynomial method and a Remez-type inequality for trigonometric polynomials. A bandit-to-testing reduction then lifts it to the QMAB lower bound, while a linear embedding gives the finite-action QLB lower bound. Complementing the lower bounds, we give a design-based elimination algorithm for finite-action QLB. When the action set has size $\operatorname{poly}(d)$, its regret is linear in $d$, improving the prior $d^2$ dependence and matching our lower bound up to polylogarithmic factors. The algorithm couples a low-bias low-variance quantum mean estimator with a small-support $G$-optimal design through a query allocation matched to the design weights. The design-based elimination reduces the dimension dependence from $d^2$ to $d^{3/2}$ when using Quantum Monte Carlo estimates. The low-variance estimator then makes reconstruction error aggregate through variance rather than worst-case absolute error, removing the remaining $\sqrt d$ factor.

---


### 135. [TRIAGE: Risk-Controlled Pseudo-Label Admission for Annotation-Efficient Semi-Supervised Retinal OCT Classification](https://arxiv.org/abs/2608.14321)

**<font color=#1a73e8>作者：</font>** Md Ashraful Hossen Akash, Shyla Afroge, Abdullah Al Mamun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The advanced retinal disease diagnosing imaging modality, optical coherence tomography (OCT), encounters a lack of automation because of the high expenses for annotations performed by specialists. The use of SSL solves the problem of insufficient annotations using unlabeled B-scans; however, most of the current techniques for generating pseudo-labels are based on prediction confidence without considering the asymmetry between different types of errors. This paper proposes TRIAGE, a risk-controlled semi-supervised framework for OCT scans classification, which uses the concept of a patient-level conformal risk controller with an asymmetric cost matrix. TRIAGE unites three crucial modules: a hierarchical classifier that is capable of working with partially abnormal supervision of the disease subtypes, a patient-grouped conformal risk controller with primal-dual coverage control, and a context-aware Transformer teacher for cross-slice verification. On the dataset from Noor Eye Hospital (16,822 B-scans, 161 patients, and 554 volumes) with a test set of unseen patients, TRIAGE demonstrates 89.66% scan-level accuracy, 0.8805 macro-F1, 0.9641 macro-AUC, and an 8.34% under-grading rate when using only 20% of the labeled data. With only 5% of the labeled data, TRIAGE keeps 76.88% accuracy and a 0.1656 under-grading rate. Compared with the other six state-of-the-art semi-supervised methods, TRIAGE significantly outperforms them with ablation study demonstrating the contribution of each module in the overall framework performance (by 42.7% in terms of under-grading rate comparing to fixed threshold methods). TRIAGE demonstrates 98.00% accuracy for 3-class classification with 1% labeled data and 95.94% accuracy for 8-class classification with 10% labeled data on the OCT-C8 dataset.

---


### 136. [Program-space Diffusion for Morphology-to-Transcriptomics Prediction](https://arxiv.org/abs/2608.14330)

**<font color=#1a73e8>作者：</font>** Ruyter Swann, Dorent Reuben, Racoceanu Daniel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics (ST) enables genome-wide gene expression profiling while preserving tissue architecture, but its cost and limited scalability remain major bottlenecks. This has motivated models that predict spatial expression directly from routine histology. Despite promising results, most existing approaches operate at the gene level without leveraging established transcriptomic modeling practices and rely on heterogeneous gene selection strategies, which complicates fair comparison across methods.
We propose to reformulate morphology-to-transcriptomics prediction as conditional generation in transcriptional program space, thereby exploiting coordinated transcriptional variation instead of predicting genes independently. Using consensus non-negative matrix factorization (cNMF), we extract a low-dimensional set of transcriptional programs capturing coordinated expression variation in the training data, and train a conditional diffusion model to generate program activations from histology. This formulation exploits coordinated transcriptional variation and substantially lowers the dimensionality of the conditional generative task.

---


### 137. [Non-Parametric Spatiotemporal Trajectory Prediction via State-Conditioned Transition Sampling](https://arxiv.org/abs/2608.14349)

**<font color=#1a73e8>作者：</font>** Michael Fore, Akshay Jain, Justin Downes 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a training-free method for multi-modal trajectory prediction that achieves comparable accuracy to a 57M-parameter transformer while requiring no GPU and zero learned parameters. The method builds a transition table of historical state-to-next-position pairs and retrieves neighbors using a product kernel over spatial proximity, bearing, speed, and temporal context. Two inference modes operate over this shared representation: diversity-penalized sampling produces trajectories covering distinct plausible routes, while beam search finds the highest-likelihood path. On the TrAISformer benchmark (Danish Maritime AIS), our method achieves competitive accuracy at full data availability and dramatically outperforms the transformer in data-scarce regimes---remaining stable down to 10% of training data where TrAISformer degrades catastrophically. This enables deployment in new geographic regions from an order of magnitude less historical data, and with no GPU training.

---


### 138. [Disentangled Shared Representations Improve Morpho-Transcriptomic Integration](https://arxiv.org/abs/2608.14355)

**<font color=#1a73e8>作者：</font>** Julian Ostermaier, Swann Ruyter, Reuben Dorent 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics (ST) enables the simultaneous profiling of gene expression and tissue morphology, creating an opportunity to learn multimodal representations capturing shared morpho-transcriptomic structure. However, standard multimodal models often compress modalities into a common latent space without explicitly separating shared and modality-specific sources of variation, which may limit downstream utility. We investigate whether explicit disentanglement of shared and private latent components improves multimodal representation learning for paired Hematoxylin \& Eosin (H\&E) and ST data. We compare VAE-based and contrastive approaches, each in standard and disentangled variants, across two cancer cohorts under matched experimental conditions. Representations are evaluated using cross-modal reconstruction, downstream probing and cross-modal probe transfer. The experiments suggest two main trends. First, contrastive objectives yield higher downstream probing performance than VAE-based models. Second, disentangled variants improve the selected reconstruction and probing metrics, although the gains depend on the model family, task, direction, and disentanglement strength. Overall, our results suggest that explicitly factorizing shared and modality-specific information can improve multimodal representation learning for spatial transcriptomics and provides a useful evaluation framework for future foundation models.

---


### 139. [Designing Sustainable Federated Learning as a Service using Neural Architecture Search](https://arxiv.org/abs/2608.14359)

**<font color=#1a73e8>作者：</font>** Keya Patel, Sajib Mistry, Sheik Fattah 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The sustainability constraints of FLaaS consumers pose significant challenges to maintaining carbon-feasible federated training in FLaaS environments. These constraints often lead to infeasible consumer participation and unstable federated training under hard carbon constraints. We propose a Sustainable Federated Learning as a Service (SFLaaS), a carbon- constrained Neural Architecture Search (NAS) framework for heteroge- neous sustainable constraints. We introduce a requirement-driven search space that transforms consumer sustainability profiles into a feasible architecture region before federated execution. We develop a consumer-level carbon feasibility estimation mechanism to evaluate candidate architectures under dynamic carbon conditions. We propose a sustainable con- sumer scheduling strategy that adaptively selects feasible consumers and allocates local workloads to preserve consumer participation and statistical data coverage. An evolutionary search strategy jointly optimised for predictive performance, consumer feasibility, and participation coverage under hard carbon constraints. Experiments on real-world datasets and a simulated environment demonstrate the effectiveness of the proposed approach.

---


### 140. [Epistemic Tensions: Reframing A Visualization Co-Design through Entanglement Theory](https://arxiv.org/abs/2608.14364)

**<font color=#1a73e8>作者：</font>** Wei Wei, Foroozan Daneshzand, Zezhong Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In this work, we present how employing the lens of entanglement helped us examine and reframe epistemic tensions arising in a visualization co-design project. Entanglement theory challenges traditional assumptions in the visualization research community by emphasizing that knowledge is not produced through linear, isolated processes, but is inherently entangled with phenomena and apparatuses. While this perspective offers a compelling critique of conventional research practices, its practical value for visualization research remains underexplored. We apply the entanglement lens to examine and reframe the epistemic tensions that emerged in a longitudinal community-based visualization co-design project. Our experience shows that the entanglement perspective not only provides a richer understanding of these tensions, but also helps transform them into generative opportunities for methodological and theoretical reflection. Applying this lens enabled us to critically interrogate the language used in research, to develop a more nuanced understanding of visualization co-design, and to surface ``dark sides'' of conventional visualization design pipelines. These contributions illustrate the practical value of embracing entanglement as an epistemological lens for visualization research.

---


### 141. [Weakly Supervised Polar Low Segmentation in Sentinel-1 SAR Imagery](https://arxiv.org/abs/2608.14366)

**<font color=#1a73e8>作者：</font>** Andrea Federici, Jakob Grahn, Giacomo Boracchi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Polar lows are intense maritime cyclones that form rapidly at high latitudes. Deep learning can detect them in Synthetic Aperture Radar (SAR) imagery, but pixel-level segmentation remains an open challenge. No pixel-level masks are available for training, and a polar low's extent is inherently subjective, with diffuse boundaries that even experts delineate inconsistently. We propose Constrained Region Erasing with Soft Targets (CREST), a Weakly Supervised Semantic Segmentation (WSSS) framework that generates masks solely from image-level labels. Our approach builds on Adversarial Erasing (AER), which iteratively mines discriminative regions, erases them, and retrains a classifier to reveal complementary cues that become pseudo-labels for segmentation. However, standard AER also collects irrelevant background features, degrading pseudo-label quality. CREST addresses this with (i) a Constrained Ordinal Region Expansion (CORE) module that encodes the spatial-connectedness prior of polar lows, constraining region expansion from a high-confidence seed, and (ii) a Dynamic Bootstrapping (DB) loss that treats the mining order as a proxy for label reliability, attenuating supervision from noisier, later-mined regions. On Sentinel-1 SAR data, CREST follows the cyclone structure more closely than standard AER, and returns a multi-class rather than binary mask whose classes indicate the reliability assigned to each region. We further evaluate on BUS-UCLM breast ultrasound and PASCAL VOC person data, whose targets satisfy the same connectedness prior but come with the dense masks the SAR data lacks. On both datasets, CREST performs better than the equivalent AER pipeline under identical settings.

---


### 142. [Mind the Long Tail: Understanding the Difficulty of Delay Detection in Business Processes](https://arxiv.org/abs/2608.14367)

**<font color=#1a73e8>作者：</font>** Keyvan Amiri Elyasi, Lukas Kirchdorfer, Heiner Stuckenschmidt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The early detection of delayed cases in business processes is a critical capability for organizations. Predictive process monitoring (PPM) supports this task by using historical event logs to predict the remaining time of ongoing cases, enabling timely interventions to avoid missed deadlines and service level violations. Although remaining time prediction has advanced considerably through sophisticated deep learning architectures, little is known about the intrinsic difficulty of delay detection itself. Since performance is typically assessed using aggregate metrics, prior work provides limited insight into how models perform across the target distribution, especially on the operationally most critical cases with large delays. In this paper, we address this gap by analyzing the difficulty of delay detection. Across 14 event logs, we show that remaining times are typically strongly right-skewed, with only a small fraction of cases exhibiting large delays. Existing models capture the mode of this distribution well but perform poorly on high-delay cases. We further uncover pronounced heteroscedasticity, showing that predictive uncertainty increases with delay magnitude. Based on these findings, we evaluate approaches to mitigate the imbalance problem, but find only limited benefits, suggesting that the key underlying problem may not be imbalance but higher uncertainty associated with delayed cases. We show that this correlation can be exploited to substantially improve the identification of delayed cases. Overall, our work provides new insights into the sources of difficulty in delay detection and identifies uncertainty-aware modeling as a promising direction for future PPM research.

---


### 143. [Catching the Imposter: Self-Supervised Learning of Physical Coherence with Cross-Entity Feature Permutations](https://arxiv.org/abs/2608.14372)

**<font color=#1a73e8>作者：</font>** Aleksei Rozanov, Arvind Renganathan, Vipin Kumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific data often describe entities whose features are jointly governed by the laws of physics, yet existing self-supervised learning (SSL) objectives largely ignore this physical coherence. We introduce imposter, a discriminative pretext task that replaces subsets of an entity's features with real observations donated by another entity and trains the encoder to identify the swapped features. Because every donated value is individually plausible, the task can only be solved by learning cross-feature physical dependencies. We evaluate the proposed objectives on global ERA5-Land reanalysis data using 21 environmental variables and assess the learned representations on seven downstream tasks spanning climate classification, carbon flux estimation, and streamflow prediction. Our study includes, to our knowledge, the first systematic comparison of self-supervised objectives for land-surface modeling under a shared architecture and pre-training budget. We find that the most effective pretext task depends on the downstream task family rather than any single objective's superiority, and that imposter provides complementary information when combined with existing SSL objectives. These results suggest that physical coherence is a valuable new source of self-supervision for scientific foundation models.

---


### 144. [Boosting Data Augmentation with Stochastic Weight Averaging](https://arxiv.org/abs/2608.14373)

**<font color=#1a73e8>作者：</font>** Longde Huang, Axel Flinth, Jan E. Gerken  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The symmetries of a learning task have become an important factor in designing modern deep learning solutions. Data augmentation is a straightforward and effective way of incorporating symmetries into a generic neural network. Recent results show that infinitely large deep ensembles show perfect symmetry when trained on augmented data. However, since training ensembles requires repeating the training process many times, this method is costly. In this work, we study stochastic weight averaging (SWA) as an alternative ensembling technique that does not require repeated training runs. We analyze SWA by approximating the stochastic training trajectory at the end of training with an Ornstein--Uhlenbeck process. We show that in the infinite-width limit, SWA on augmented data provides an equiviariance boost that goes beyond what could be expected from the performance increase due to SWA alone. We verify our results with extensive numerical experiments on numerous models spanning computer vision and graph classification with both discrete and continuous symmetries.

---


### 145. [GBU-Palm: A Multimodal Video Dataset and Benchmark for Palm Presentation Attack Detection](https://arxiv.org/abs/2608.14389)

**<font color=#1a73e8>作者：</font>** Yingjie Ma, Zitong Yu, Wei Jia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing palm presentation attack detection (PAD) datasets are often limited by static imagery, restricted acquisition conditions, or insufficient multimodal video data, hindering systematic evaluation across environments, modalities, and attack types. We present GBU-Palm, a large-scale multimodal video dataset and benchmark containing 21,326 videos from 105 subjects and 210 palms across six acquisition environments, including bona fide, Print, and Replay presentations, with 6,310 synchronized RGB-NIR samples. We construct leakage-controlled protocols that separate palm identity and attack lineage and benchmark four representative video architectures under environment-matched and held-out-environment settings. Results reveal substantial architecture-dependent degradation under environmental shift and show that RGB-NIR fusion does not consistently outperform RGB-only input. We further analyze model behavior through true accept (TA), true reject (TR), false accept (FA), and false reject (FR) decomposition, spectral masking, temporal-order intervention, and frozen-backbone NIR probing, revealing distinct failure patterns and evidence utilization across architectures. GBU-Palm provides a unified and challenging benchmark for developing and evaluating robust multimodal palm PAD methods under cross-environment conditions.

---


### 146. [Submodular Policy Learning for Distributed Task Allocation in Open Multi-Agent Systems](https://arxiv.org/abs/2608.14390)

**<font color=#1a73e8>作者：</font>** Jing Liu, Luca Ballotta, Yangyang Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This paper studies policy learning for distributed task allocation in open multi-agent systems, where agents may join and leave in a time-varying fashion, with submodular stage team utilities. At each time, the active agents select actions from local categorical policies such that the feasible joint agent-action pairs form a partition matroid. Standard continuous relaxations of submodular set functions are based on independent Bernoulli sampling, making them inconsistent with agents' this http URL solve this mismatch, we propose the \emph{partition multilinear extension} (PME), a policy-based relaxation whose continuous support matches feasible actions under categorical this http URL prove that the marginal gains of the stage utility provide an unbiased estimator of the gradient of the PME and that maximizing the PME over action distributions is equivalent to maximizing the stage utilities over agent actions, which are critical to devise principled policy this http URL on this, we design \emph{SubMAPL}, a centralized-training decentralized-execution KL-mirror policy-learning method that uses local marginal gains as stochastic PME gradients during training. KL-mirror updates preserve categorical feasibility without Euclidean this http URL the case where agents run tabular-softmax policies, we introduce open policy migration and an open-system KL tracking variation to handle agent arrivals and departures. Using dynamic regret analysis, we establish a lower bound on the cumulative utility which accounts for the openness of the environment and for the gap between optimal stage-wise and global utilities. Simulations on multi-agent coverage demonstrate that SubMAPL outperforms policy-gradient and online-learning baselines.

---


### 147. [IRGNN: Efficient Invariant Radar Graph Neural Network for Radar Point Cloud Object Detection](https://arxiv.org/abs/2608.14394)

**<font color=#1a73e8>作者：</font>** Xiao Guo, Wanke Xia, Lili Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perception is a fundamental component of autonomous driving systems. While LiDAR-based methods have achieved remarkable progress in object detection, their reliability can degrade under adverse weather conditions. Radar point clouds provide a robust alternative due to their resilience to bad weather and low-illumination scenarios. However, radar point clouds are typically sparse, unordered, and less informative than LiDAR data, making it challenging to directly apply existing LiDAR-based perception methods. To address these challenges, we propose IRGNN, an Invariant Radar Graph Neural Network for radar point cloud object detection. IRGNN first reconstructs radar point clouds into graph representations using translation- and rotation-invariant feature designs, enabling robust modeling of sparse radar measurements. It then employs an improved message passing neural network (MPNN) with residual connections and a virtual node layer to enhance local feature propagation and global context modeling. Finally, task-specific heads are applied to the learned graph representations for object classification and bounding box prediction. Experimental results on the RadarScenes dataset show that IRGNN outperforms existing radar-based object detection methods and achieves competitive performance. In addition, IRGNN significantly reduces computational cost and memory usage during inference, demonstrating its effectiveness and practical potential for efficient radar-based perception in autonomous driving.

---


### 148. [The Past and Future of AI Scientists](https://arxiv.org/abs/2608.14407)

**<font color=#1a73e8>作者：</font>** Ross D. King  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a survey of the past and future of AI Scientists: machines capable of automating science. AI Scientists can originate hypotheses, deduce their consequences, design and execute experiments, interpret their results, and revise their beliefs. Such systems are integrated scientific agents, connected to the literature, formal knowledge, mathematical models, simulations, data-analysis systems and physical laboratories.
Adam was the first machine to make novel scientific discoveries through cycles of hypothesis formation and physical experimentation. Eve established the architecture of the modern self-driving laboratory. Foundation models, autonomous agents and laboratory robotics now make it possible to build systems far more general than either Adam or Eve.
The central problem is no longer whether individual components of science can be automated. They can. The problem is integration. AI Scientists must combine neural learning with logic, probability, mathematics, causal reasoning, simulation, experimental design, robotics and formal scientific records.
AI Scientists have the potential to transform science: to make science faster, cheaper, more systematic and more reproducible. AI Scientists could investigate systems too complicated for unaided human science, and enable thousands of AI scientists to work together on single problems.
The Nobel Turing Challenge sets the goal of developing by 2050 AI systems capable of automating Nobel-quality discoveries. Progress is ahead of schedule. When we succeed it will create a new form of science and transform the world.

---


### 149. [The Dynamics of Intelligence Explosions](https://arxiv.org/abs/2608.14426)

**<font color=#1a73e8>作者：</font>** Toby Ord  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI is increasingly being used to help with AI R&D. Under certain conditions this feedback loop might be able to produce an intelligence explosion, with rapidly escalating AI capabilities. I explore the mathematics of the most explosive possibilities, with an eye to understanding what drives the dynamics. I show that singular growth (towards a vertical asymptote) is harder to achieve than would be expected from recent economics-inspired modelling, and that there is an important but neglected class of growth rates that are faster than exponential but don't lead to a vertical asymptote. I draw out the generation time (the time to go around the feedback loop) as a neglected parameter that plays a pivotal role in determining the behaviour of any intelligence explosion --- one cannot have singular growth unless the generation time rapidly approaches zero.

---


### 150. [GhostPoint: Self-Supervised Representation Learning by Hallucinating Occluded LiDAR Structure](https://arxiv.org/abs/2608.14428)

**<font color=#1a73e8>作者：</font>** Mohamed Abdelsamad, Bin Yang, Michael Ulrich 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D object detection from LiDAR point clouds is a core problem in autonomous driving. Recent advances in self-supervised learning (SSL) enable scalable pretraining and transfers well to per-point tasks such as semantic and panoptic segmentation, but transfer to 3D detection remains weaker. We analyze recent SSL methods and find that most objectives are defined only on measured LiDAR returns from visible surfaces, leaving occluded and unobserved regions unconstrained. This visible-surface bias can be sufficient for point-wise prediction, but 3D detection requires robustness to missing structure. To address this gap, we propose GhostPoint, an SSL framework that hallucinates latent features in local neighborhoods around discovered instances, generated via a novel instance voxel dilation. In GhostPoint, an encoder processes observed returns, and an additional predictor infers neighborhood representations from observed context. In addition to standard encoder-level supervision, we introduce a predictor-level supervision scheme on sampled voxels from generated neighborhoods. Specifically, observed (visible/masked) voxels match teacher-encoder targets, while unobserved voxels match teacher-predictor hallucinations. This design encourages the learned representation to explicitly model structure beyond observed returns. Extensive evaluations on nuScenes and Waymo demonstrate that our method achieves state-of-the-art performance, consistently improving downstream 3D detection, especially under sparse scans and limited labels.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-165](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
