# 📦 其他研究 | 2026年10月22日

> 本类共 **288** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-288](./part-06.md)

---

### 101. [Cross-Visibility-Gap Identity Persistence for 4D Scene Graphs](https://arxiv.org/abs/2610.27505)

**<font color=#1a73e8>作者：</font>** Jiahui Hu, Li Gao, Yu Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D scene graphs require persistent object identity when an object disappears inside an opaque carrier and later reappears as a fresh detection. When appearance and target-centric motion are unavailable, identity recovery must rely on relational history. We formulate cross-visibility-gap identity persistence as historical-node recovery through a remembered target--carrier binding.
We introduce CVG-SGM, a perception-frontend-compatible transfer--maintain--read memory. Geometry-weighted cross-node interaction transfers target-specific evidence into carrier states, a shared per-node GRU maintains this information during transport, and a two-time readout combines stored carrier--identity compatibility with current detection--carrier geometry to recover the historical identity.
In the controlled one-identity-per-carrier setting, CVG-SGM achieves 1.000 re-link accuracy, compared with 0.570 for both no-memory and parameter-count-matched no-write controls. It also generalizes to scene-disjoint, unseen longer visibility gaps. On real RGB-D/SAM2 feature-level episodes, it correctly re-links 36/36 held-out detections, compared with 28/36 for the strongest fixed carrier--identity control. Counterfactual carrier-memory swaps redirect predictions according to the swapped bindings, supporting the role of stored relational information in identity recovery. The current approach remains limited by shared-carrier identity ambiguity and does not provide end-to-end raw-video re-identification.

---


### 102. [Complete Street Design informed by Multi-Agent Simulation](https://arxiv.org/abs/2610.27509)

**<font color=#1a73e8>作者：</font>** Sharika J. Hegde, Amirmohammad Khakpour, Pedram Beigi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Objectives: Complete Street design is currently guided largely by qualitative principles despite the increasing complexity of multimodal urban traffic. This paper develops a microscopic simulation framework for quantitatively evaluating alternative street designs by explicitly representing heterogeneous road users, including Autonomous Vehicles (AVs), Connected Vehicles (CVs), Human-Driven Vehicles (HDVs), pick-up and drop-off (PUDO) services, and micromobility users. The framework jointly evaluates mobility and safety within a unified testbed. Methods:The framework enriches microscopic simulation with behavioral models for heterogeneous road users. It explicitly captures lateral movements, parking maneuvers, pedestrian crossings and jaywalking, and shared-lane bicycle and scooter interactions. Safety is quantified using a conflict severity measure grounded in collision physics, while candidate street layouts are optimized using a genetic algorithm. Findings: Applied to a segment of Belmont Avenue in Chicago, Illinois, the framework shows that dedicated bicycle lanes reduce conflict severity at the expense of vehicular throughput. Increasing AV penetration mitigates congestion by reducing traffic shockwaves while improving interactions with pedestrians relative to CVs and HDVs. The optimization framework efficiently identifies Pareto-efficient street layouts that balance mobility and safety. Novelty: The proposed framework integrates heterogeneous behavioral modeling, physics-based conflict assessment, stochastic performance evaluation, and design optimization within a single quantitative framework for Complete Street design. Practical Applications: The framework provides transportation planners with a predictive virtual testbed for evaluating street designs and quantifying the tradeoff between mobility and safety before implementation.

---


### 103. [Structured-Token Attention for Fine-Grained mmWave Liquid Identification](https://arxiv.org/abs/2610.27512)

**<font color=#1a73e8>作者：</font>** Junseo Min, Joongheon Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-grained liquid identification requires a classifier to distinguish similar substances from compact millimeter-wave measurements. We investigate structured-token attention, which represents a radar feature tensor through complementary antenna, feature, branch, and global views. The proposed StructAttn model embeds these views into eleven tokens and combines them with a three-layer transformer. Experiments on the public FG-LiquID data cover 30 liquids and 3,000 samples. Over five seeds on the released split, StructAttn achieves 96.70\% mean best-epoch accuracy, matching the original-recipe MMNet baseline and exceeding a scalar-token attention model by 1.50 percentage points. A five-seed probability ensemble reaches 97\%, corresponding to 18 errors among 600 test samples. Final-epoch and five-fold results complement the checkpoint-selected comparison, with StructAttn obtaining 95.30\% out-of-fold accuracy. Token and feature analyses show that structured views are useful for prediction, while residual confusions concentrate in water, soft-drink, and edible-oil classes. These results support structured tokenization as a practical design choice for attention-based liquid recognition.

---


### 104. [Multiscale Temporal-Spectral-Spatial EEG Learning With Modality-Specific and Modality-Invariant Representations for Emotion Recognition](https://arxiv.org/abs/2610.27521)

**<font color=#1a73e8>作者：</font>** Jian Zhang, Manrong Liu, Yilei Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal physiological signals provide complementary cues for emotion recognition. They also raise two related challenges. Emotion-related EEG patterns vary across time, frequency bands, electrodes, and brain regions. Different physiological modalities also contain both modality-specific and shared affective information. This paper presents GMSI-Net, an EEG-centered multimodal emotion recognition framework. It has three key components. The temporal-spatial-spectral-region (TSSR) encoder models multiscale temporal-channel patterns, differential entropy features, and local-to-global brain-region relations. The modality-specific representation (MSR) branch uses bidirectional cross-modal attention and learnable gates. It controls information transfer while retaining modality-specific cues. The modality-invariant representation (MIR) branch learns a shared affective representation. An adaptively weighted contrastive loss aligns this representation across modalities. Independent multiscale Conv-Transformer encoders process the peripheral physiological signals. GMSI-Net is evaluated on DEAP and MAHNOB-HCI using within-subject random ten-fold cross-validation. The model reaches 96.21 (1.47) and 96.41 (1.60) for valence and arousal on DEAP. It reaches 94.10 (2.86) and 94.48 (3.77) on MAHNOB-HCI. These results indicate that combining EEG features with complementary physiological information can improve emotion recognition.

---


### 105. [OmniVLoc: Topo-metric Visual Localization for Omnidirectional Cameras](https://arxiv.org/abs/2610.27522)

**<font color=#1a73e8>作者：</font>** Zhuo Yu, Shuyang Zhang, Huihua Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omnidirectional cameras provide surround-view information, significantly overcoming the field-of-view constraints for traditional visual localization systems. However, existing localization systems fail to fully exploit the characteristics of omnidirectional cameras, struggling to deliver accurate and robust localization performance amidst scene content variations and illumination-induced appearance changes. In this work, we propose OmniVLoc, a surround-view localization system based on a topo-metric framework. By integrating state-of-the-art global place recognition and monocular depth estimation methods, we introduce a multi-constrained visual localization paradigm. By solving a scale-aware pose graph and performing precise spherical bundle adjustment, we accurately recover the metric-level pose for each query this http URL, a hierarchical verification mechanism is designed to filter out erroneous outputs across different stages, effectively bolstering the overall system robustness. Extensive experiments on both public and our custom datasets validate the superior accuracy and reliability of OmniVLoc. To benefit the community, our source code and dataset will be made publicly available upon publication.

---


### 106. [MemDev-Bench: Does Memory Help Code Agents?Benchmarking Memory Systems over Real Repository Histories](https://arxiv.org/abs/2610.27524)

**<font color=#1a73e8>作者：</font>** Guorui Chen, Tao Liu, Zhenzhen Huang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Code agents increasingly work on evolving real repositories, and memory systems aim to help them reuse earlier experience. However, such experience is diverse and evolving, so it remains unclear how memory systems organize it and thereby affect code agents. Existing benchmarks cannot answer this reliably because they lack either temporally valid histories or control over prior-task relevance. In this paper, we present MemDev-Bench to evaluate how memory systems affect code agents over diverse repository histories. It pairs each task with relevance-annotated earlier tasks from the same repository to build histories with controlled relevance. We also build an automated pipeline that reliably makes these earlier tasks executable and verifiable, producing 4,869 historical tasks for 555 base tasks. Based on MemDev-Bench, our systematic evaluation of memory systems across diverse development scenarios yields three main findings. (1) Memory mainly improves fine-grained localization and editing, increasing functional correctness. (2) Memory also causes failures on otherwise solvable tasks even with related history, and unrelated history tends to increase such failures. These failures mainly stem from agents reusing memory without reassessing its applicability. (3) Compared with using memory systems, directly providing agents with raw historical trajectories substantially reduces their steps. Further analysis suggests that agents save these steps by reusing process information that compressed memories tend to omit. These results suggest that future memory systems should preserve process information and reassess memory applicability against current task context.

---


### 107. [Judging the Justification: Decision Certificate Supervision for Generative Reward Models](https://arxiv.org/abs/2610.27528)

**<font color=#1a73e8>作者：</font>** Guiquan Sun, Bing Bai, Martin Renqiang Min 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative reward models (GenRMs) generate natural language rationales to justify preference judgments, yet a correct verdict does not guarantee a sound justification. Existing approaches often rely on reference explanations to supervise rationales, but obtaining such references can be costly and does not necessarily establish whether generated rationales support the resulting verdict. To address these limitations, we propose DeCert, a framework that evaluates the validity and verdict consistency of generated rationales without requiring reference explanations. Crucially, DeCert translates these assessments into preference supervision that accounts for both verdict correctness and justification quality. In particular, when multiple sampled judgments share the same correct verdict, differences in certificate quality enable DeCert to construct rationale preference pairs that distinguish stronger from weaker justifications. Extensive empirical studies across two model families and multiple in- and out-of-distribution benchmarks demonstrate that DeCert consistently outperforms strong generative judge baselines while improving rationale quality. Moreover, DeCert effectively mitigates positional bias, improving position-consistent accuracy by up to 14.8 points. These results highlight the importance of supervising not only which verdict is correct, but also how that verdict is justified.

---


### 108. [Automated Multi-Agent Organization Design: From Architecture Search to Organizational Learning](https://arxiv.org/abs/2610.27531)

**<font color=#1a73e8>作者：</font>** Shao-Jun Xia, Yuner Zhang, Huixin Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic system design is increasingly shifting from hand-crafted prompts and workflows toward automated search over agentic programs and interaction structures, with multi-agent systems receiving growing attention. Yet a central question remains unresolved: when does an automatically generated multi-agent structure exhibit a functionally meaningful division of responsibility? We argue that automated multi-agent design should move beyond searching for effective architectures toward identifying which responsibilities are functionally necessary, how they should be allocated, and when they should change. To explore this, we propose Automated Multi-Agent Organization Design (AMOD), which treats organization itself as a first-class design object, explicitly modeling how agent teams are composed, what functional responsibilities the agents assume, how they coordinate, and how collective decisions are made. We formulate AMOD as an execution-driven design loop. For each task, an automated designer instantiates an organization by assigning functional responsibilities and coordination rules to a set of agents. After execution, task outcomes, intermediate artifacts, and interaction traces are examined to identify which responsibilities may be missing, duplicated, or ineffective, and the organization is revised accordingly. We also propose testing discovered responsibilities by removing them, replacing them with generic roles, or changing their assignment under matched resource budgets, with complementary evaluations. AMOD provides a principled foundation for evidence-based and adaptive multi-agent organization design.

---


### 109. [Adversarial Benchmarks and BenchDoor Attacks: Exploiting Benchmark Incentives for Backdoor Attacks](https://arxiv.org/abs/2610.27533)

**<font color=#1a73e8>作者：</font>** Yixin Wu, Rachel Hong, Jamie Morgenstern 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning benchmarks act as guideposts for model development and spur the creation of training datasets intended to improve benchmark scores. We introduce BenchDoor, a family of data poisoning attacks that exploits this incentive. Beyond preserving benign performance, BenchDoor requires benchmark gains that encourage adoption of data that also implants a backdoor. The adversary either manipulates a benchmark's training or test data, creating an adversarial benchmark, or supplies an independent training dataset while leaving the benchmark unchanged. We formalize five attack scenarios, including training on rewritten test examples and applying similarity-based decontamination. Across multiple-choice Q&A, text classification, and open-ended Q&A with Qwen and Gemma models, BenchDoor achieves positive benchmark gains for all 30 evaluated configurations, with held-out attack success rates of 82.33% to 100.00% at poisoning rates of 2% to 10%. Both objectives remain achievable after synthetic data generation and similarity-based decontamination, with attack success rates of at least 90.33%. These findings show how benchmarks can serve as attack vectors both through their own data and through training resources that deliver improvements on them.

---


### 110. [BEACON: Bridging Multimodal Semantics and Asynchronous Propagation for Cloud System Anomaly Detection](https://arxiv.org/abs/2610.27542)

**<font color=#1a73e8>作者：</font>** Zhe Li, Tengxue Zhang, Yang Shu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern large-scale cloud systems continuously generate massive and multimodal observability data, such as time-series metrics, log records, and system dependency graphs, which reflect the health state of the system. To ensure reliable cloud system operation, anomaly detection models identify abnormal states by analyzing these multimodal observations. However, existing approaches rely on simple fusion strategies and graph learning, ignoring the semantic gap among modalities and the asynchronous spatio-temporal dependencies across system instances over time. To this end, we propose BEACON, a framework to Bridge multimodal sEmantics and Asynchronous propagation for Cloud system anOmaly detectioN. Specifically, we introduce a Dynamic Interpretable Multimodal Aggregator (DIMA) that leverages an information-bottleneck mechanism to compress information from the semantics and temporal dynamics of metrics, and aligns them with logs in a shared prototype space. Furthermore, we propose an Asynchronous Spatio-Temporal Propagator (ASTP) that captures temporal dependencies with multi-scale temporal attention and models spatial relations with topology-aware aggregation. This enables asynchronous propagation of anomalies across system instances. Extensive experiments on three real-world cloud system datasets demonstrate that \textbf{BEACON} consistently outperforms state-of-the-art baselines in anomaly detection.

---


### 111. [SynCalib: Breaking Dataset Shortcuts in LiDAR-Camera Calibration via Extrinsic-Controllable Synthesis](https://arxiv.org/abs/2610.27547)

**<font color=#1a73e8>作者：</font>** Huihua Zhu, Shuyang Zhang, Dongqing Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online LiDAR-camera calibration remains a fundamental yet challenging task in the field of robotics. Recently, deep learning-based data-driven approaches have emerged, offering high-precision, targetless calibration capabilities. However, existing methods often suffer from a critical dataset shortcut phenomenon due to the lack of extrinsic diversity in their training data. Networks tend to overfit to fixed nominal extrinsic configurations, leading to severe performance degradation and poor generalization in real-world deployments. To address this limitation, we propose a highly generalizable data generation framework tailored for training LiDAR-camera calibration networks. Our framework leverages existing omnidirectional image datasets annotated with depth ground truth to synthesize multi-modal calibration data under rigorous extrinsic constraints. Extensive experiments demonstrate that the data generated by our pipeline significantly enhances the generalization and robustness of typical learning-based calibration networks. Furthermore, we conduct comprehensive real-world evaluations across various camera-LiDAR configurations, validating the zero-shot transfer capability of models trained exclusively on our synthetic data. To facilitate future research and community use, the code for data generation, the pre-trained models, and online benchmark datasets will be made publicly available.

---


### 112. [Timing-Aware and Interpretable Self-Attention for Event-Based Wearable Task Transition Detection](https://arxiv.org/abs/2610.27549)

**<font color=#1a73e8>作者：</font>** Anda Ouyang, Siyuan Chen, Julien Epps  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Task transition detection aims to identify when a person shifts from one task to another, providing a foundation for continuous health monitoring and timely context-aware interventions. While statistical and deep feature representations have demonstrated strong classification performance, they often rely on aggregated or latent features that are difficult to interpret in behavioural terms. Event-based features provide a compact and interpretable alternative by encoding behavioural and physiological patterns as discrete tokens with explicit semantic meaning, making them well suited for behavioural analysis in health informatics. Self-attention offers a mechanism for modelling interactions among such tokens; however, conventional self-attention classifiers primarily rely on token order and do not explicitly incorporate timing or duration information. As a result, informative temporal cues in event representations may not be fully exploited for task transition detection. This study proposes an event-based time-aware self-attention framework that represents behavioural signals as sequences of discrete events augmented with onset timestamps and durations. Event timing is encoded using a parameter-efficient kernel-based representation, while a novel type-aware duration embedding modulates information propagation according to event persistence. Experiments on a semi-naturalistic wearable dataset show that the proposed model outperforms existing event-based approaches, achieves performance beyond or comparable with statistical and deep-learning models with a more compact input representation, and provides improved interpretability through integrated-gradient-based analysis. These results indicate that explicit modelling of event timing and duration enhances both classification performance and interpretability, supporting reliable deployment in biomedical and health informatics applications.

---


### 113. [AnchorRM: Parallel Intra-Batch State Reconstruction with Anchor-Based Residual Memory for Temporal Graph Neural Networks](https://arxiv.org/abs/2610.27558)

**<font color=#1a73e8>作者：</font>** Haroon Gharwi, Kai Shu, Yue Dai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Memory-based temporal graph neural networks (TGN) rely on recurrent node memories to capture evolving interaction histories. However, temporal mini-batching introduces a trade-off between computational efficiency and temporal fidelity: when a node appears multiple times within the same batch, later interactions are evaluated using stale pre-batch memory because the intermediate memory updates have not yet been committed. This problem becomes more severe as temporal batch size increases. To overcome this challenge, we propose AnchorRM, an anchor-based residual memory mechanism that reconstructs event-specific intra-batch node states without executing sequential recurrent updates. AnchorRM treats the last committed node memory at the beginning of each batch as a pre-batch fixed anchor and uses causally preceding same-batch interactions to infer the missing state evolution relative to that anchor. The learned residual then calibrates the anchor to reconstruct an event-specific node memory for each interaction. Because each event-specific residual is predicted directly from the fixed anchor and its causal history, reconstructed states do not depend on previously reconstructed states and can therefore be computed in parallel within the batch while preserving temporal causality. Experiments across four temporal graph datasets and three memory-based backbones demonstrate that AnchorRM achieves an average 6.16x training speedup (up to 10.05x) and 28.67x batch scaling (up to 40x). These results demonstrate that AnchorRM substantially improves the scalability and training efficiency of memory-based temporal graph learning while maintaining competitive predictive performance.

---


### 114. [CityPaint: A Free Lunch from 2D Diffusion for City-Scale 3D Texturing](https://arxiv.org/abs/2610.27564)

**<font color=#1a73e8>作者：</font>** Yuchen Zou, Lihuang Fang, Siyu Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating high-fidelity, city-scale 3D environments plays a crucial role in applications such as virtual reality, gaming, and urban digital twins. However, the scarcity of real-world city-scale 3D training data forces existing methods to either stitch independently generated assets or learn from synthetic urban corpora, often sacrificing realism and global consistency. In contrast, 2D image data and their corresponding generative models are abundant and encode rich visual priors. To bridge this gap, we propose CityPaint, a novel framework that leverages 2D diffusion models to generate globally consistent city-scale 3D textures without relying on city-scale 3D training data. Specifically, CityPaint integrates geometric priors with the generative power of 2D diffusion models, introducing a robust top-$K$ camera baking strategy for iterative texture projection. To address the artifacts of 2D-to-3D projection, we further propose a decoupled refinement mechanism that separately optimizes terrain and building textures. Extensive experiments show that CityPaint produces globally coherent textures with fine local details and achieves favorable results against strong baselines in both visual quality and cross-view consistency.

---


### 115. [TRCM: Topology-Aware Route-Consistency Modeling for Robust Neural Vehicle Routing](https://arxiv.org/abs/2610.27568)

**<font color=#1a73e8>作者：</font>** Peiheng Jian, Zhenwei Wang, Tiehua Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural combinatorial optimization has enabled fast constructive solvers for the Capacitated Vehicle Routing Problem (CVRP), yet most autoregressive models still construct solutions through sequential node selection and represent route organization only implicitly. We investigate whether route-level customer co-assignment can be modeled explicitly and used to guide this node-level decision process. To this end, we propose TopologyAware RouteConsistency Modeling (TRCM), which reuses node representations from a standard autoregressive construction pipeline to predict pairwise same-route probabilities and injects them into customer selection as a route-consistency signal. Because sameroute supervision is both class-imbalanced and structurally uneven, TRCM combines structure-preserving augmentation with Topological Entropy (TE)- based reweighting to emphasize locally ambiguous customer pairs. Under matched decoding budgets, TRCM reduces the optimality gap from 3.67% to 3.28% on CVRP50 and from 2.11% to 1.99% on CVRP100; under 8-fold augmented inference, it reduces the CVRP100 gap from 1.61% to 1.49%. On XML100, TRCM*8Aug improves the average objective by 0.24%, with larger gains on several structurally informative factors. A controlled demand-reassignment test over 500 variants further shows more concentrated objective fluctuations. These results support explicit route-consistency modeling as an effective structural principle for autoregressive neural routing.

---


### 116. [Two Is Enough: Binary Classification Priors Suffice for Multi-Class In-Context Tabular Prediction](https://arxiv.org/abs/2610.27569)

**<font color=#1a73e8>作者：</font>** Zhixiong Cheng, Shiyuan Han, Jingjing Suo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) pretrain a transformer on large-scale synthetic priors so that a single forward pass yields zero-shot tabular prediction. TabICLv2 samples the class count of its classification prior during pretraining, and the prevailing configuration caps it at ten. We report a counter-intuitive result: setting this cap directly to two---making every pretrained classification task binary---still yields weights that perform zero-shot K-way classification 2. On the 38 TabArena classification datasets (200 bootstrap rounds, anchored at default RF = 1000), the binary two-stage recipe reaches 1590.1 Elo, above the official default at 1568.0 (+22.1), above TabPFN-v2.6 (1577.1) and RealTabPFN-v2.5 (1521.6). A production-scale validation on 60 real-world credit-scoring institutions independently confirms the direction: the same checkpoint improves test AUC on 44 of 60 institutions (paired Wilcoxon p = 0.0007 for AUC, p = 0.0002 for KS) at +1.5 inference cost. Mechanistically, classification in TabICLv2 is carried not by a fixed-cardinality output head but by an in-context comparison operator matching query-row embeddings against class-conditional embeddings, so the cardinality of the output space is set by the labels present in the context, not by the label space seen during pretraining. This makes a binary prior structurally cheaper to generate and cache than a ten-class prior, demotes "number of classes" from an architectural constraint to a tunable hyperparameter, and points to a class-count-agnostic regime of TFM pretraining.

---


### 117. [Text-Anchored Modality Experts with Uncertainty-Guided Routing for Multimodal Sentiment Analysis](https://arxiv.org/abs/2610.27571)

**<font color=#1a73e8>作者：</font>** Xiaohua Huang, Bingrui Lei, Xiuyan hao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal sentiment analysis (MSA) aims to understand user-generated videos by integrating multiple modalities. Existing methods often treat modalities as symmetric, overlooking the fact that language provides a dominant semantic prior while nonverbal signals are complementary and noise-prone. To address this, we propose a Text-Anchored Modality Experts with Uncertainty-Guided Routing, termed TAME, that reformulates MSA as an uncertainty-guided refinement paradigm, where the language prior is calibrated and enhanced by selectively trusted nonverbal evidence. Specifically, TAME adopts an asymmetric Mixture-of-Modality-Experts framework, in which textual features act as a fixed and always-activated shared expert, while audio-textual and video-textual cross-modal branches serve as dynamically routed auxiliary experts. Furthermore, we introduce lightweight Prophet Heads to quantify the sample-level predictive uncertainty of each individual modality, and this uncertainty metric is further incorporated into the modality router to realize reliability-aware expert aggregation and fusion. Experiments on CMU-MOSI, CMU-MOSEI, and CH-SIMS datasets demonstrate that TAME achieves state-of-the-art performance on the majority of metrics while reducing parameter count by up to 78.7% and FLOPs by up to 41.2% over the mixture-of-expert baseline. %These results confirm that asymmetric expert construction with uncertainty-guided routing is an effective paradigm for MSA.

---


### 118. [RaspAssistant as an Agentic Framework for Automating Adsorption Simulation Research in Porous Materials](https://arxiv.org/abs/2610.27572)

**<font color=#1a73e8>作者：</font>** Marko Petković, Susanne Gooijer, José Manuel Vicent-Luna 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Porous-material adsorption studies require coordinated structure preparation, force-field selection, simulation, validation, and interpretation, making end-to-end automation difficult. We test whether RaspAssistant, a hierarchical multi-agent framework, can carry an adsorption study from force-field preparation through validation and downstream separation analysis. Across twelve multi-agent workflow-reproduction runs spanning four adsorption and separation benchmarks, overall scores ranged from 8.50 to 10.00 on a rubric evaluating workflow correctness, simulation validity, and analysis consistency. In a separate eight-case force-field extraction benchmark, the mean weighted score was 0.967, combining parameter agreement and RASPA readiness. In open-ended studies, the system diagnosed and refined an acetylene force field and, after validating a CO$_2$ force field against MFI experiments, screened 197 pure-silica zeolites that passed automated input checks. These results demonstrate autonomous workflow execution after task specification and input provision: RaspAssistant coordinates, validates, adapts, and documents extended adsorption-simulation workflows while exposing model sensitivity and methodological limitations for expert review.

---


### 119. [From POMDP Theory to Deep RL with Particle Filters](https://arxiv.org/abs/2610.27575)

**<font color=#1a73e8>作者：</font>** Kevin Tan, Ziping Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-based reinforcement learning in partially observable environments requires inferring hidden states, learning latent dynamics, and planning under the resulting belief. Practical algorithms often solve one aspect of the above pipeline while relying on approximations for the others that are often poorly understood, while existing POMDP theory typically analyzes computationally inefficient theoretical algorithms far from modern deep RL practice. To fill this gap, we propose a practical end-to-end algorithm that approximately solves the hidden state filtering problem via sequential Monte Carlo (SMC), updates a latent dynamics model online, and performs approximate online planning for $d$ steps before bootstrapping leaves with a state-value critic (a QMDP approximation). We analyze each approximation and prove an end-to-end regret bound decomposing the error into model estimation error, particle filter error, Monte Carlo rollout error, and a structural bias term induced by the QMDP approximation controllable by the planning depth that we further analyze in various special cases. The resulting guarantee makes explicit how statistical sample size, particle budget, rollout budget, and planning depth affect performance. We instantiate our algorithm in an MPC-based deep RL framework, demonstrating its practicality on a variety of environments. On a POMDP that satisfies our assumptions, each term of the bound decays at its predicted rate. Our results provide a practical and theoretically grounded route for bridging theory and practice within online decision-making in POMDPs.

---


### 120. [Bridging Digital Deception and Physical Fidelity: A Spatio-Temporal Attack on Cognitive Radars](https://arxiv.org/abs/2610.27585)

**<font color=#1a73e8>作者：</font>** Tongrun Xing, Yongjun Dai, Xuan Liao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As cognitive radars evolve towards the end-to-end processing of one-dimensional complex baseband sequences, deep networks face severe adversarial threats. However, existing attacks encounter dual limitations in practical electronic warfare: low cross-architecture transferability and severe vulnerability to physical channel distortions, which degrades their tactical reliability. To overcome these bottlenecks, we propose a physical prior-driven Segmented Spatio-Temporal Attack (SSTA). First, a global-local feature decoupling segmentation mechanism interrupts the adversarial gradients' dependence on long-range sequence coherence, bridging the cross-architecture feature gap. Second, moving beyond static norm constraints devoid of physical semantics, we abstract channel distortions into differentiable spatio-temporal operators, integrating them into momentum iterations via an Expectation over Transformation (EoT) strategy. Comprehensive cross-evaluations across 9 heterogeneous models spanning CNNs, RNNs, and Transformers demonstrate that SSTA outperforms the state-of-the-art baseline by 10.36% in Average Black-Box Attack Success Rate. Furthermore, baseband equivalent simulations confirm that the generated waveforms survive extreme physical distortions and, after matched filtering, achieve zero main-lobe attenuation (0 dB) with noise floor lift strictly within Constant False Alarm Rate tolerances. SSTA successfully unifies digital-domain deception and physical-domain fidelity, providing crucial support for CEW security assessment.

---


### 121. [Benefit and Cost of Random-Token Replacement under Repeated Data: A Known-Entropy Decomposition and Evidence from Ten Real Corpora](https://arxiv.org/abs/2610.27590)

**<font color=#1a73e8>作者：</font>** Wonsup Shin, Jingu Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When unique pretraining data is scarce, models see the same tokens many times and are thought to memorize. Random-token replacement, an input-corruption augmentation, is one remedy reported to lower validation loss, but a lower loss alone does not reveal which source of error it reduces. On a controlled source whose entropy rate is known in closed form, we show that replacement shrinks predictions toward the corpus average. We also introduce a decomposition that separates validation loss into approximation, estimation, and memorization terms. This shrinkage view predicts that replacement's bias cost needs no memorization but its benefit does. Memorization raises validation loss after its minimum, so we report the effect at two points, the minimum validation loss and the end of a fixed budget. Where replacement helps, it reduces this rise by about 60%. At the end of the budget, it turns from harmful to helpful as the controlled source becomes less predictable; at the minimum, it helps at no predictability level under the fixed recipe. On Korean and Japanese web text, replacement removes about a third of the loss rise after the minimum by the end of the budget, but its effect at the minimum is much smaller. Across ten real corpora, replacement lowers the final loss on nine. It harms only the census corpus, program-generated JSON that is the most redundant of the ten and much more redundant than any of 64 further prose and code corpora we measure.

---


### 122. [Real In, Real Out: What If We Only Use Real Data for Scene Text Editing?](https://arxiv.org/abs/2610.27592)

**<font color=#1a73e8>作者：</font>** Xingsong Ye, Yongkun Du, Jiaxin Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aiming to modify textual content while preserving the original style, Scene Text Editing (STE) has significant practical value in many applications. STE typically requires paired images before and after editing for training. However, recent approaches rely heavily on synthetic paired data and complex disentanglement strategies. They struggle to faithfully capture the diversity and complexity of natural scenes, often producing artifacts or hallucinations. In this work, we challenge the common practice and investigate whether STE can be driven by turning each real sample into its own paired supervision. Concretely, we explore multiple ways to disrupt the original image (e.g., Crop, Shuffle, Mask) to construct self-paired training data, and build a strong baseline (TextRIRO}) upon a conditional diffusion architecture. Our experiments show that combining character-column shuffling with image cropping (Shuffle&Crop) effectively destroys text semantics while preserving key style cues, enabling the model to learn editing behaviors directly from the real text image. With this concise yet real-oriented design, TextRIRO achieves promising performance in both accuracy and visual realism across real-world benchmarks, substantially mitigating the synthetic-to-real domain gap. Furthermore, we leverage TextRIRO to build TextRIRO-3M, a large-scale realistic dataset for long-text recognition by concatenating edited and original images. Experimental results show that training recognition models with TextRIRO-3M significantly improves recognition accuracy, demonstrating that TextRIRO provides highly useful training resources for downstream tasks. Overall, TextRIRO lifts STE to realistic, reliable, and widely applicable new levels. Code is available at this https URL.

---


### 123. [Causal Spatiotemporal State Evolution for Monocular 4D Reconstruction](https://arxiv.org/abs/2610.27594)

**<font color=#1a73e8>作者：</font>** Qiaowei Miao, Yijing Guo, Lipei Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While feed-forward models excel in static 3D geometry estimation, extending them to dynamic 4D scenes requires modeling visual geometry as a causally evolving state. Current methods typically rely on unordered temporal aggregation, which lacks the directional structure of physical time. Furthermore, existing supervision often treats geometry and motion as disjoint objectives, failing to exploit their inherent physical coupling. Consequently, they lack a unified constraint to effectively supervise temporal state transitions, leading to inconsistent 4D scene representations. To address this, we propose a feed-forward framework for causal 4D visual geometry learning from monocular videos. At its core, Causal Spatiotemporal Mamba augments temporal aggregation with directional state propagation. Through complementary Temporal-Spatial and Spatial-Temporal Scans, CSM continuously propagates geometry-aware states across frames to model spatiotemporal evolution. To align this causal state evolution with observable dynamics, we introduce Unified Motion Supervision. Rather than treating motion as an independent objective, UMS leverages geometry-aware predictions from the camera and depth heads to construct a unified forward motion field that is consistent with the underlying 3D structure. This geometry-grounded supervision explicitly constrains inter-frame state transitions, enabling stable states propagation across frames. Extensive evaluations on dynamic benchmarks demonstrate state-of-the-art performance across video depth, camera pose, and optical flow estimation. These results validate that the synergy between the directional state propagation of Causal Spatiotemporal Mamba and Unified Motion Supervision effectively captures continuous scene evolution, significantly reducing temporal drift and reinforcing spatial-temporal consistency in 4D representation learning.

---


### 124. [WORTH Benchmark: Evidence Discovery under Not-Fully-Cooperative Information -- A Two-Episode Pilot](https://arxiv.org/abs/2610.27597)

**<font color=#1a73e8>作者：</font>** Bo Zou, Chao Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing reasoning evaluations typically provide task-relevant information to models as available premises, rarely examining concurrently how models discover evidence autonomously and how information presentation within narratives guides or obscures judgment. This paper proposes the WORTH Benchmark: models read original mystery narratives without clue annotations, autonomously select key clue sentences, identify case participants, and explain their reasoning process. The narrative materials are designed by professional authors such that evidence facilitating reasoning coexists with narrative arrangements that delay the revelation of truth. We report a pilot experiment under full-story conditions across two episodes, conducting a total of 70 formal runs on models, of which 67 runs are content-scorable. Scoring separately records hits on author-designated key clue sentences and participant selections; natural language explanations are used for case diagnosis and are not scored independently. The results show that clue hits and participant judgments are not synchronized; across 37 content-scorable runs in Episode 02, 31 runs simultaneously selected the same set of incorrect participants, while adjacent suspicion-oriented and exoneration-oriented sentences were selected 25 times and 0 times, respectively. These phenomena illustrate the diagnostic value of component-wise analysis and suggest that not-fully-cooperative informational relationships may influence evidence selection and judgment. This study only implements full-story conditions for two episodes, and does not establish stable model rankings or infer general mechanisms on this basis; human player records have not yet been cleaned, and this version does not report human-model comparisons.

---


### 125. [HiQGS: Hierarchical Spatiotemporal Querying for Feed-Forward Gaussian Reconstruction](https://arxiv.org/abs/2610.27604)

**<font color=#1a73e8>作者：</font>** Qiaowei Miao, Qifeng Cheng, Yijing Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward Gaussian reconstruction from sparse posed monocular frames requires reasoning over observations that vary jointly in viewpoint and time. Existing methods either predict Gaussian primitives from observation-aligned features or aggregate multi-frame information through compact latent queries. However, the former tightly couples Gaussian allocation to individual frames, while the latter does not explicitly structure observed evidence according to its temporal relation to the requested timestamp. Consequently, evidence across spatial scales, viewpoints, and timestamps can be difficult to align and integrate. We present \textbf{HiQGS}, a query-based hierarchical framework for feed-forward Gaussian scene reconstruction from sparse monocular frames. HiQGS introduces a \textbf{Hierarchical Spatiotemporal Encoder} that organizes multi-resolution geometry-appearance visual features according to image location, observation time, and camera pose, thereby preserving complementary appearance and structural cues. Our \textbf{Time-Adaptive Decoder} use target timestamp queries the resulting hierarchical representation to retrieve relevant spatiotemporal evidence and predicts the corresponding Gaussian scene state. Experiments on static and dynamic scene reconstruction benchmarks demonstrate strong rendering quality and geometric accuracy, validating the effectiveness of hierarchical visual encoding and target-time-aware Gaussian querying.

---


### 126. [DART: Scaling a Shape Representation Across Anatomical Classes and Imaging Modalities](https://arxiv.org/abs/2610.27605)

**<font color=#1a73e8>作者：</font>** Koushik Swarna, Pedro R. A. S. Bassi, Lam Ngo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current state-of-the-art segmentation models still produce anatomically implausible shapes, such as broken vessels and fragmented glands, on the structures that are hardest to segment. Learned shape representations capture what structures look like and can help correct these errors, but most cover a fixed set of anatomical classes. Extending this coverage across classes and imaging modalities is costly because it often requires new voxel-level annotations. We propose Diffusion for Anatomical Reshaping with Text (DART), which learns a shared shape representation from segmentation probabilities. It uses anatomical descriptions to correct these probabilities without receiving medical images. Across 13 public benchmarks, absolute Dice gains reach 31% for individual gallbladder cases in CT and 10% for individual prostate cases in MRI. Using existing segmentation predictions, we scale a single shape representation from 50 to 377 anatomical classes without new voxel-level annotations for correction training. The shared representation also corrects four lesion classes absent from training and transfers from CT to MRI without retraining. Corrected labels also improve segmentation models, raising one model's Dice from 57.1% to 67.5%. The same pipeline supports annotations for 45,000 CT scans. These results suggest that sharing shape information within and across classes can reduce the need for new voxel-level annotations when extending segmentation to more anatomical classes and imaging modalities. The model is available at this https URL

---


### 127. [What should AI forget? A design and taxonomy for negative space governance in AI memory](https://arxiv.org/abs/2610.27607)

**<font color=#1a73e8>作者：</font>** Eryue Xu, Ke Ding, Ting-Yu Chang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI memory personalizes assistants, yet users want some disclosed information forgotten. We characterize the negative space of AI memory, where protection should take precedence over potential future personalization benefits. From 179 incidents reported by 146 users, we developed a taxonomy of 15 information categories users want excluded from memory, revealing sensitivity concerns beyond conventional taxonomies. We operationalize this taxonomy in FENCE, a policy-level memory gate that automatically applies user-selected category-based rules to subsequent conversations, preventing information from protected conversations from entering AI memory by default while allowing case-by-case overrides. In a within-subjects study (N=15), participants described FENCE as making memory governance more usable, interpretable, and trustworthy than conventional post-hoc management. Our findings demonstrate how taxonomy-based rules can potentially support user-defined memory boundaries. We call for collective efforts to establish policies governing what AI should not remember, rather than leaving protection to individual retrospective management.

---


### 128. [WaveSpec: Multi-Spectral Iris Presentation Attack Detection via Wavelength-Conditioned Spectral Coherence Adaptation](https://arxiv.org/abs/2610.27608)

**<font color=#1a73e8>作者：</font>** Raghavendra Ramachandra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multispectral iris presentation attack detection benefits from observing the same iris across multiple near-infrared wavelengths, but existing methods often use wavelength information mainly for conditioning or fusion. This can limit their ability to explicitly model whether the spectral response of a sample is coherent across bands. In this paper, we propose \textbf{WaveSpec}, a multispectral iris PAD framework that performs feature-level spectral coherence adaptation. Each NIR band is first encoded with a DINOv2 backbone. The proposed Set Conditioned Spectral Coherence Adapter then updates each band feature using the consensus of the available spectral set, the band-specific deviation from that consensus, and wavelength identity. The adapted features are projected into structural, spectral, and anomaly representations, adaptively pooled, and classified as bona fide or attack. We evaluate WaveSpec on the MSIrPAD benchmark under a strict cross-artefact protocol, where the model is trained with one presentation attack instrument and tested on unseen attacks. WaveSpec reduces the average D-EER from 8.45\% for SpectraIrisPAD to 3.33\%, and reduces average BPCER@APCER=1\% from 43.16\% to 12.07\%. Ablation results show that the SCSA adapter and spectral residual are central to the improvement, while a band-subset analysis shows that WaveSpec remains effective under partial spectral observations and performs best when all five bands are available. The method adds only modest computational overhead, with 11.15 ms end-to-end latency per five-band sample on an NVIDIA L40S-48Q GPU.

---


### 129. [Big Secrets Small Shares: Revisiting Secure Multi-Party Computation](https://arxiv.org/abs/2610.27609)

**<font color=#1a73e8>作者：</font>** Wilton Kim, Van Long Phuoc Pham, Stanislav Kruglik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> At CRYPTO 2007, Damgård and Nielsen introduced a preprocessing approach to multi-party computation (MPC) to achieve linear communication complexity. Another approach to reduce communication complexity was proposed by Cramer, Damgård, and de Haan at EUROCRYPT 2007, which involved using ramp-secret sharing schemes to jointly share base-field components of secrets from the extension field. In this paper, we combine these two ideas to achieve a non-asymptotic reduction of communication cost in a multi-phase MPC setup. We introduce a new modification of the ramp secret sharing scheme, called compact sharing, and tailor the MPC protocol to accommodate this modification. Compact sharing masks the polynomial coefficients that would otherwise leak during degree reduction. The protocol provides perfect security against static semi-honest adversaries under an explicit tradeoff between the corruption threshold and the extension degree. When the extension degree scales linearly with the number of parties, the gate-evaluation core achieves constant communication overhead relative to an extension-field element, amortized over full preprocessing batches; input and output communication is counted separately.

---


### 130. [Learning Inter-Graph Interactions Between Heterogeneous Substructures of Chemical Systems](https://arxiv.org/abs/2610.27614)

**<font color=#1a73e8>作者：</font>** Gyoung S. Na  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complex chemical systems containing heterogeneous substructures are common in real-world applications. Various physical phenomena of the complex chemical systems are derived from the interactions between the heterogeneous substructures. However, existing graph representation learning methods for inter-graph interactions assumed graph-level interactions between homogeneous structures, such as organic molecules and inorganic crystalline materials. We propose a data descriptor of the complex chemical systems and a graph neural network for learning inter-graph interactions between organic and inorganic compounds. We applied the proposed method to predict the physical properties of hybrid solar cell materials containing heterogeneous substructures, which have received significant attention for sustainable energy resources. By learning heterogeneous inter-graph interactions, the proposed method achieved state-of-the-art accuracy in predicting band gaps of 1,682 hybrid solar cell materials.

---


### 131. [DISTA-LP: Privacy-Preserving Distributed Linear Programming for Metric Differential Privacy](https://arxiv.org/abs/2610.27615)

**<font color=#1a73e8>作者：</font>** Michael Oluwole, Ruiyao Liu, Aleksander Stevens 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Linear-programming (LP) mechanisms for metric differential privacy (mDP) enable fine-grained, task-aware utility control, but they are computationally expensive and become privacy-fragile in distributed settings: uploading user-specific LP coefficient matrices (e.g., distance and loss blocks) to a central solver can itself leak sensitive information. We present DISTA-LP, a privacy-preserving distributed mDP optimization framework that replaces raw coefficient uploads with compact surrogate parameterizations and releases only calibrated, perturbed parameter vectors, thereby reducing both upload-stage leakage and problem dimensionality. On the server side, DISTA-LP reconstructs approximate coefficients and solves a scalable mastersubproblem formulation via Benders decomposition. To certify end-to-end privacy, we introduce a probabilistic mDP (PmDP) auditor that empirically quantifies the privacy loss induced by parameter release, allocates the required privacy budget prior to optimization, and composes it with the downstream mechanism to obtain an end-to-end mDP guarantee. Experiments on large realworld road-network datasets (Rome, New York City, and London) show that DISTA-LP achieves near-zero mDP violation rates, substantially reduces computation time compared to monolithic and hybrid baselines, and matches or improves utility, thereby demonstrating stronger upload privacy and significantly improved scalability.

---


### 132. [Provisioning Robust and Efficient LiDAR Perception for Autonomous Driving](https://arxiv.org/abs/2610.27617)

**<font color=#1a73e8>作者：</font>** Tingxu Han, Zijie Shen, An Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR-based 3D object detection is a core perception service for autonomous driving, but deployment requires robustness to point-cloud corruption while meeting latency and memory requirements. Existing approaches address robustness and resource efficiency separately, resulting in compact detectors that are fragile under corruption or robust detectors that remain costly to deploy. We therefore formulate LiDAR perception provisioning as constructing a detector that remains accurate under point-cloud corruptions while meeting constraints on inference latency and peak GPU memory. To achieve robustness, we first craft corrupted samples that mimic extreme weather conditions. Then we train candidate detectors offline by ordering clean and corrupted samples by perturbation sensitivity, through which detectors learn more from hard corrupted samples. We estimate perturbation sensitivity using an ensemble of seven heterogeneous 3D detectors by tracking changes in confidence, BEV overlap, and unmatched detections. To improve efficiency, we narrow the network and use offline neighborhood-density measurements to determine how many points and neighbors each sampling stage processes. We evaluate our method using AP (Average Precision) under clean and corrupted conditions, inference latency, and peak allocated GPU memory. On KITTI for Car detection with PointRCNN, our method improves Moderate AP under corruption by 3.32 points over the original detector while reducing mean latency by 19.8% and peak allocated GPU memory by 53.9%. Across two datasets, two detector architectures, and three object classes, our method improves AP under corruption by 4.03 points on average over the corresponding original detectors, while reducing mean inference latency and peak allocated GPU memory by 14.4% and 38.0%, respectively. Our code is available at this https URL.

---


### 133. [A Two-Way Street: Surveying the Interplay between Code-Mixing and Native Languages in Text and Speech](https://arxiv.org/abs/2610.27631)

**<font color=#1a73e8>作者：</font>** Debajyoti Mazumder, Akash Anil  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Systems for code-mixed (CM) text and speech rarely start from scratch. CM data is scarce, so most work borrows from the languages being mixed, which we call native languages. This transfer can also run in reverse, when CM data is used to improve models for the native languages. Existing surveys focus on processing CM itself, and none brings the two directions together. This paper fills that gap with a systematic survey of transfer in both directions, across text and speech. We organise the surveyed work in a taxonomy of transfer direction, route and modality. Through this taxonomy, we find that most transfer runs from native languages into the CM setting. The reverse direction is younger, and in it code-switching mainly helps by aligning the two languages. Text and speech work share methods but rarely cite each other. On a shared speech benchmark, native data helps more than new architectures. These findings point to open challenges, such as how much native and CM data to mix in training, and how to evaluate CM text written in different scripts.

---


### 134. [When Does Feedback Help? Auditing Learned Voltage-Clamp Experimental Design](https://arxiv.org/abs/2610.27632)

**<font color=#1a73e8>作者：</font>** Rayan Nyaupane, Abhiram Bhupatiraju  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A learned scientific controller can outperform a misspecified planner without benefiting from feedback. We audit two synthetic voltage-clamp tasks with a training-selected fixed protocol, current masking, a Bayesian reference, and an excluded target. Five recurrent policies repeat one fixed protocol in all 1,200 off-grid rollouts; masking current changes no decision. In a crossed four-hypothesis task, a fixed diagnostic pulse is followed by one learned choice. Policies then use the first current, but tie a correctly specified Bayesian controller, and a fitted threshold reproduces the learned actions without being that controller. The excluded-target prediction gain is $4.6991\times10^{-6}$ nats per sample. Feedback use and protocol quality are separate tests. These cases establish neither biological discovery nor general RL superiority.

---


### 135. [Ensemble-Aware Structural Encoding (EASE): Conditioning Protein Encoders on Peptide Conformational Ensembles](https://arxiv.org/abs/2610.27638)

**<font color=#1a73e8>作者：</font>** Ruoyao Zhang, Hongxuan Li, Jie Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein foundation models provide transferable representations for downstream peptide prediction tasks. However, existing representations typically reduce a peptide to a single sequence or structure, which may miss conformational variability relevant to key peptide properties, including antibacterial activity, hemolysis, toxicity, stability, and binding. For example, protease resistance correlates more strongly with conformational dynamics measured by hydrogen exchange than with average helicity. Therefore, we introduce Ensemble-Aware Structural Encoding (EASE), a framework for effectively extracting structural information from conformational ensembles for peptide representation. To extract useful information from noisy conformers, EASE selects central conformers representing a peptide's major structural states and fuses their individual representations with a permutation-invariant operator to produce a peptide-level representation for downstream prediction. We then evaluate our framework on six peptide property-prediction tasks under leakage-controlled splits. Against matched single-structure baselines, EASE improves performance consistently on six tasks with a mean absolute gain of about 3.0% across two structural encoders. Gains keep growing as we add conformers through K=20. A single peptide conformer therefore provides a limited basis for structural representation, whereas our framework distilling and fusing multiple conformers yields a more informative representation.

---


### 136. [Secure Multimodal Federated Optimization via Hierarchical DNA-Based Key Management](https://arxiv.org/abs/2610.27644)

**<font color=#1a73e8>作者：</font>** Yuping Yan, Yaochu Jin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated optimization over heterogeneous multimodal data enables distributed institutions to collaboratively optimize a shared model using medical images, genomic profiles, clinical records, and physiological signals without centralizing raw data. However, protecting modality-specific data throughout the optimization lifecycle remains insufficiently explored, particularly when heterogeneous modalities require separate encryption keys and selective local access. This paper proposes a secure multimodal federated optimization framework that separates local data protection from federated-update protection. A trusted key-management authority securely provisions one client key through Hybrid Public Key Encryption (HPKE), from which each client locally derives modality-specific symmetric keys using the domain-separated HMAC-based Extract-and-Expand Key Derivation Function (HKDF). Heterogeneous modalities are mapped into a unified DNA-domain representation and processed through a DNA-origami-inspired structural transformation before authenticated encryption with AES-GCM. During local optimization, only the required modalities are decrypted within an authorized client environment. Individual model updates are independently protected through secure aggregation, allowing the coordinator to observe only aggregated updates rather than each client's contribution. Together, these components establish a structured approach to modality-specific protection and secure collaborative optimization, integrating hierarchical key management, authenticated local encryption, and aggregation-level update protection within a unified framework.

---


### 137. [CAESAR: Mixed Reality Search-and-Rescue Platform for Cognitive Attack Evaluation](https://arxiv.org/abs/2610.27654)

**<font color=#1a73e8>作者：</font>** Mingyu Zhu, Jiangong Chen, Yu Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mixed Reality (MR) enables immersive training by tightly coupling virtual content with the physical environment and supporting embodied interaction. In safety-critical collaborative tasks such as search-and-rescue, however, users rely heavily on virtual elements for perception, coordination, and decision-making, making them vulnerable to cognitive attacks that subtly distort visual feedback, virtual content, or system synchronization. While prior MR security research has examined individual attack mechanisms, evaluations are typically conducted in isolated or single-user settings, and there is a lack of standardized collaborative testbeds for systematic adversarial experimentation. In this paper, we develop CAESAR, an end-to-end multi-user MR framework for systematic evaluation of cognitive attacks in collaborative search-and-rescue training. CAESAR features a modular architecture that integrates four classes of cognitive attacks within a synchronized collaborative scenario and incorporates a multimodal data collection pipeline that captures behavioral, performance, and subjective measures under adversarial conditions. We conduct a controlled user study with an in-depth analysis of the latency-based attack, demonstrating measurable effects on task performance and user behavior while characterizing users' subjective experience under adversarial conditions.

---


### 138. [Inferring continuous cognitive traits from limited neuroimaging data using pairwise convolutional neural networks](https://arxiv.org/abs/2610.27668)

**<font color=#1a73e8>作者：</font>** Marjan Rashidi, Robert Bain, Craig Stark 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Individual differences in cognitive abilities vary widely, yet the structural brain features supporting these differences remain poorly understood. Traditional brain-behavior analyses rely on predefined metrics such as volume or cortical thickness and typically assume linear relationships with behavior, limiting sensitivity in small datasets. Here, we introduce a pairwise convolutional ranking framework that learns directly from whole-brain T1-weighted MRI by making comparative rather than absolute predictions, which performs well even with small samples (N=108). We tested this method with four small-scale spatial abilities tasks. Regression analysis predicted performance with high accuracy across all tasks, achieving greater predictive power over standard regression and pointwise deep learning baselines. Iterative cortical-region removal (backward elimination) revealed brain regions supporting individual performance common to all four tasks, as well as task-specific regions. These results demonstrate that pairwise learning extracts meaningful behavioral information from structural MRI, providing prediction and interpretable insight into the neuroanatomy of individual differences.

---


### 139. [Pairwise Learning Increases Data Efficiency in Deep Neural Networks](https://arxiv.org/abs/2610.27669)

**<font color=#1a73e8>作者：</font>** Robert Bain, Marjan Rashidi, Elizabeth Chrastil  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks often fail at small-sample regression, collapsing to low-variance predictions that miss individual differences. Here, we introduce a pairwise comparison framework that reframes regression as aggregated relative rankings. This method improves data efficiency across model architectures and dataset sizes. On the UTKFace dataset (23k images), pairwise learning generates over one billion training comparisons without additional supervision. The paired ranking allows a lightweight ResNet10 trained from scratch on home hardware to achieve a 3.64-year MAE-surpassing previous models, including those with large-scale pretraining. For classification into categories, pairwise supervision consistently outperforms an otherwise identical 10-way crossentropy model on STL10 with 500-2000 labeled examples, improving accuracy by up to 5.2%. Overall, pairwise supervision enhances data efficiency and enables strong regression and classification performance when labeled data are limited, particularly in clinical settings.

---


### 140. [Reusing Multimodal Agents: Efficient Evaluation of Sound Designs in Games](https://arxiv.org/abs/2610.27670)

**<font color=#1a73e8>作者：</font>** Thai Nguyen Van, Ibrahim Khan, Mury Fajar Dewantoro 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper introduces a novel framework for efficiently evaluating in-game sound designs using multimodal learning and reinforcement learning. Sound design significantly influences gameplay and accessibility; however, objective evaluation methods, defined here as automated assessments based on agent performance rather than human ratings, often require retraining agents from scratch for each sound design. Our approach first pre-trains a multimodal encoder that encodes visual and auditory information into a shared latent space. A reinforcement learning agent is then trained using this latent representation. We fine-tune the multimodal encoder for each sound design while keeping the trained policy fixed, allowing us to isolate the effects of sound changes on agent behavior. To evaluate the proposed method, we conducted experiments on games from multiple genres, comparing the performance of blind agents (agents using only sound input) under various sound designs. Experimental results suggest that this approach can detect differences in agent performance caused by degraded or altered sound design. Moreover, we significantly reduce the computational cost compared to retraining the agent from scratch. Experimental results suggest that this approach provides a practical and scalable solution for evaluating in-game sound designs. The source code, data and supplementary document are available: this https URL.

---


### 141. [Neural Operator Splitting for Fluid Dynamics in Complex Geometry](https://arxiv.org/abs/2610.27671)

**<font color=#1a73e8>作者：</font>** Jianxiang Li, Xi Deng, Hong Chul Nam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solving dynamical systems in complex and diverse geometries remains challenging for both numerical solvers and learning-based surrogate models. We propose Neural Operator Splitting, a framework for learning fluid dynamics while preserving the physical structure of fractional-step numerical schemes. Instead of learning the full-step evolution monolithically, we decompose each time step into physically interpretable steps, and learn each operator separately using intermediate states from the underlying numerical solver. Guided by the linearity properties of the fractional steps, we introduce a conditional-linear Fourier neural operator (CL-FNO) whose linear state mappings are modulated by nonlinear conditioning on inputs such as boundary geometry. We further introduce two complementary strategies, symmetry sampling and corrective cycling, to mitigate error accumulation during autoregressive rollout. Experiments on 2D and 3D fluid flows with varying geometries and initial conditions show that our full model reduces mean relative $L^2$ rollout error by 68\% in 2D and 40\% in 3D compared with a single full-step neural operator. At comparable error levels, neural-operator inference is approximately $10^3$ times faster per step than the Monte Carlo solver.

---


### 142. [Reusing Assurance Evidence in AI Pipelines: Validity Conditions, a Fail-Closed Release Gate, and a Replay of 714 Public Data Version Control Pipelines](https://arxiv.org/abs/2610.27672)

**<font color=#1a73e8>作者：</font>** Atanu Mukhopadhyay, Shravya Reddy Nalla  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rerunning every governance control after every change to an artificial intelligence (AI) pipeline is expensive, so teams reuse earlier results. Reuse is safe only if each control's declared dependencies cover everything that can change its outcome, and only if the release gate checks that reused evidence describes the candidate being released. This article makes both conditions explicit and measures how often the first fails in practice. It defines when a signed evidence record is valid for a candidate and gives sufficient conditions under which change-local re-execution reaches the same release decision as rerunning every control. A reference gate implementing these checks with Ed25519 digital signatures blocks eight of nine manipulation scenarios, against one for a gate that trusts the planner and three for a gate that only verifies signatures; a dependency the policy never declared passes every gate. A replay of 38,083 commits from 714 public Data Version Control (DVC) pipelines measures that failure mode. Reusing stage results according to declared dependencies avoids 83.4% of stage executions, but in 3.3% of commits it reuses a stage whose imported code or referenced configuration changed, and 31% of pipelines are affected. A manual audit confirms the undeclared dependency in 36 of 40 sampled events. Evaluation stages, whose outputs are the evidence, are the most exposed. Adding each stage's static import closure lowers stale reuse to 0.4% while still avoiding 81.6% of executions; sampled shadow re-execution removes far less, and rerunning everything after unexplained changes avoids only 45.3%.

---


### 143. [CyberHull: Deterministic Malicious URL Isolation via Convex Hull](https://arxiv.org/abs/2610.27675)

**<font color=#1a73e8>作者：</font>** Avijit Gayen, Aniket Ghosal, Durba Chakraborty 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The emergence of increasingly sophisticated and evasion-resistant phishing attack strategies represents a significant threat to modern cybersecurity, particularly in cyber-physical systems and internet-based networks. Traditional probabilistic methods and certain machine learning approaches often struggle to detect novel attacks and may lack interpretability or portability. To address these challenges, we introduce CyberHull, a resource-efficient and deterministic framework for identifying malicious URLs through mathematically defined convex hull boundaries across multiple orthogonal feature domains, including structural content entropy, hyperlink graph topology, and semantic token distribution. CyberHull constructs compact convex hulls, referred to as vaults, using the QuickHull algorithm, with a training complexity of O(n log n) under suitable assumptions. URL classification is performed through point-in-polyhedron tests that impose relatively low computational overhead on standard CPUs. Experimental results demonstrate that CyberHull achieves 92 percent detection accuracy, substantially outperforming a baseline linear approach based on Principal Component Analysis (PCA), which achieves 32 percent accuracy. Furthermore, CyberHull offers a computationally efficient alternative to resource-intensive deep learning approaches for malicious URL detection.

---


### 144. [Temporal Evidence Allocation For Longitudinal Clinical Retrieval: A Position And Technical Report](https://arxiv.org/abs/2610.27682)

**<font color=#1a73e8>作者：</font>** Soumya Ranjan Sahoo, Divya Bharti, Sanand Sasidharan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electronic health records are written to support care, not retrieval. Across years of oncology notes, the primary diagnosis is restated in report after report, while the events that shape a patient's course, such as a recurrence or a change in therapy, may be recorded only once. A retriever that ranks passages by similarity to the query keeps returning the repeated material and can miss these transitions, that is, it exhibits temporal redundancy across historical narratives. We argue that longitudinal clinical retrieval should be treated as allocating a limited evidence budget across time, not just ranking by relevance. We separate the task into three objectives: temporal evidence allocation, candidate reconstruction, and clinical validation. In Study A (13 clinical queries over 20 patient records, with two-stage reconstruction), the Temporal-15 configuration reaches a milestone slot recall of 0.538, compared with 0.388 for the Global-50 baseline. However, it also retrieves far more evidence (496 versus 50 indexed units per query), so the gain cannot be credited to allocation alone. When evidence is held fixed, removing prompted precedence rules raises schema-order reversals from 0.010 to 0.080. A five-patient, single-query pilot with fixed budgets finds that wider temporal coverage does not reliably yield more dated milestones. Together, these results suggest that how much a record says about a period is a poor guide to how useful that period is as evidence. Because no expert reference timelines are available, our measurements describe retrieval behavior rather than clinical accuracy. This position and technical report presents the retrieval analysis behind the Onco-CONSTRUE framework and sets out a research agenda for budget-constrained longitudinal clinical retrieval.

---


### 145. [Influence Is the Target-Response Jacobian Times Residuals](https://arxiv.org/abs/2610.27689)

**<font color=#1a73e8>作者：</font>** Paul Geertsema, Simon Geertsema  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce the target-response Jacobian $J = [\partial \hat y_i/\partial y_j]$, which measures how model predictions respond to changes in individual training targets. $J$ complements training-data attribution (TDA) methods, which characterize sensitivity to the weights placed on training observations in the loss rather than to their targets, and can be computed matrix-free at the same cost as influence-based TDA methods. We show that sample-weight influence $\mathcal{I}$ and $J$ follow from the same implicit differentiation argument and differ only by a per-example multiplier: for pointwise losses, $\mathcal{I} = J\operatorname{diag}(m)$ exactly at any stationary point with an invertible Hessian. For canonical-link losses (squared error, logistic, Poisson) the multiplier is the training residual, $\mathcal{I} = J\operatorname{diag}(r)$, and softmax cross-entropy obeys a multiclass version. The identity predicts three ways in which influence fails when used in place of $J$: small residuals shrink its predicted shift towards zero (interpolation collapse), residuals of mixed sign wash out its direction (direction washout), and under softmax cross-entropy it collapses a training point's per-class sensitivities towards its own true class (true-class collapse). We score both operators against refitting with a per-prediction $R^2$ across target perturbations, with no rescaling. On tanh networks trained with squared error (Friedman #1) and logistic loss (MAGIC, HIGGS), with $N$ from 2,000 to $10^6$, $J$ reaches $R^2$ between 0.99 and 1.00, whereas influence's $R^2$ is negative on every dataset. On an MNIST softmax classifier, influence's $R^2$ is again negative, while $J$ reaches 0.92. On HIGGS, one row of $J$, holding all $10^6$ sensitivities of one prediction, takes under 0.2 seconds on an RTX 3090 after a one-time setup of under five minutes, whereas refitting would take $10^6$ refits.

---


### 146. [EASformer: Environment-Action-State Alignment for Industrial Generative Ranking](https://arxiv.org/abs/2610.27691)

**<font color=#1a73e8>作者：</font>** Bohao Li, Dinglun Cao, Pengcheng Huang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern industrial ranking systems increasingly adopt generative recommendation (GR) paradigms, in which user behavior sequences and non-sequential (NS) features are tokenized and jointly modeled by Transformer-style backbones. This unified formulation provides a scalable interface for modeling long histories and heterogeneous features. However, sequence and NS representations often carry asymmetric semantics: historical representations may combine environment context with observed-action semantics, whereas candidate-side NS representations contain no observed action but incorporate richer supplementary context, such as user-item interaction features and recent behavior lists. Direct interaction between such representations can make query-key dot products compare different semantic objects, limiting meaningful cross-token interaction. To fill this gap, we propose EASformer, an Environment-Action-State disentangled architecture for industrial app ranking. EASformer constructs an explicitly aligned context environment space shared by historical and non-sequence tokens, while disentangling user actions from historical token and candidate-specific context form non-sequence tokens. Based on this aligned space, EASformer enables complementary historical action retrieval and state-conditioned action prediction. Furthermore, the disentangled design supports a Cloze-style self-supervised objective by masking historical actions and reusing the candidate prediction pathway. On an offline benchmark from a real-world industrial app marketplace, EASformer achieves an AUC of 0.89411, yielding a 0.88% relative improvement over the deployed baseline. Online A/B tests further support this advantage, with relative eCPM lifts of 1.26% and 3.94% across two real-world ranking scenarios.

---


### 147. [PanoGraphGS: Unifying Panoptic Segmentation and Hierarchical 3D Scene Graphs with Gaussian Splatting](https://arxiv.org/abs/2610.27696)

**<font color=#1a73e8>作者：</font>** Jinghan Gao, Siyu Wang, Dongyu Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D scene graphs support language-guided navigation by organizing physical entities and their containment and spatial relations into hierarchical maps. Building such structured maps requires a scene representation that consistently distinguishes semantic regions and object instances across viewpoints. To this end, we present PanoGraphGS, a unified framework that integrates panoptic 3D Gaussian representation learning with hierarchical 3D scene graph construction. The framework learns semantic and instance features on shared Gaussian geometry. Prototype-based semantic learning and association-based instance learning produce consistent panoptic predictions across viewpoints. The learned representation supports novel-view panoptic segmentation and direct Gaussian-level panoptic decoding. A semantic-aware scene graph module further recovers a floor-room-stuff-object hierarchy with containment and spatial relations. We further release NaviGS, a real-world dataset for panoramic scene understanding. The dataset provides 3DGS, mesh, RGB, semantic, and depth data. For 3D scene graph identification, PanoGraphGS outperforms the strongest evaluated baseline in object-node accuracy by more than 50\% points on average across Replica and NaviGS. PanoGraphGS also achieves state-of-the-art performance among the evaluated methods in 2D panoptic segmentation. These results demonstrate the effectiveness of PanoGraphGS in both hierarchical 3D scene understanding and 2D panoptic segmentation. The project website is available at: this https URL.

---


### 148. [Understanding Data Augmentation under Label Noise](https://arxiv.org/abs/2610.27701)

**<font color=#1a73e8>作者：</font>** Hong Zheng, Fei Teng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data augmentation (DA) has become a fundamental component of modern machine learning systems and is widely regarded as an effective strategy for improving robustness and generalization. Despite its empirical success, the theoretical impact of DA under label noise remains poorly understood. In this work, we first theoretically explain when DA is beneficial and when it becomes detrimental, and provide sufficient conditions for distinguishing between these two regimes under both the i.i.d. learning setting and the more challenging domain generalization scenario. Then, we reveal a counterintuitive phenomenon: DA essentially acts as an uncertainty amplifier in the learning process, decreasing model stability and generalization performance. This finding is supported by the proposed learning and generalization bounds. Our analyses do not depend on specific DA techniques and require only mild assumptions, indicating that the results are applicable to a broad range of machine learning scenarios. Namely, we provide a unified theoretical foundation for understanding, analyzing, and designing DA methods in the presence of label noise.

---


### 149. [Multi-Objective Evolutionary Semi-Supervised Learning for Resource-Aware Smart City Classification](https://arxiv.org/abs/2610.27703)

**<font color=#1a73e8>作者：</font>** Francisco José Sedeño, Jamal Toutouh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Smart-city applications often combine scarce labeled data with abundant unlabeled observations. Semi-supervised learning (SSL) exploits both labeled and unlabeled data to improve classification under limited supervision. This article presents MOEA-SSL, a multi-objective evolutionary approach for lightweight semi-supervised tabular classification that jointly optimizes predictive quality and feature usage. Experimental evaluation on three Smart City classification datasets, considering 1\%, 5\%, and 10\% labeled data, shows that MOEA-SSL achieves competitive predictive performance compared with established lightweight SSL methods while significantly reducing feature usage relative to EA-SSL in all evaluated conditions. The computed Pareto fronts also provide lower-feature-use alternatives with limited degradation in classification performance.

---


### 150. [VEOcc++: Learning Persistent Voxel Feature Maps for Embodied Online Semantic Occupancy Mapping and Offline Refinement](https://arxiv.org/abs/2610.27704)

**<font color=#1a73e8>作者：</font>** Ruoyu Wang, Jiahan Li, Yong Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic occupancy mapping supports embodied perception during exploration and detailed scene understanding afterward, giving rise to two complementary requirements: online incremental mapping for maintaining an up-to-date global map under causal constraints, and offline global map refinement for improving the completed scene representation with additional computation. We present VEOcc++, a unified voxel-centric framework that connects both stages through a persistent sparse voxel feature map. During exploration, the map expands with newly observed regions and integrates aligned local features through reliability-guided updates, while context-aware decoding produces the current semantic occupancy map. After exploration, cached local features are consolidated as complementary evidence and combined with the completed online representation for multi-scale spatial refinement. On EmbodiedOcc-ScanNet, VEOcc++ achieves 67.12\% IoU and 58.40\% mIoU, establishing new state-of-the-art performance for online incremental mapping. With the local predictor fixed, our online mapping pipeline outperforms VEOcc fusion by 3.70 IoU and 3.74 mIoU points, demonstrating substantial gains from the proposed global mapping design. Offline global map refinement further improves the completed map to 67.79% IoU and 59.37% mIoU using only the observations acquired during exploration. Zero-shot deployment on a mobile robot further demonstrates transferability to unseen environments, onboard feasibility, and scalability to large-scale indoor mapping. Project page: this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-288](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
