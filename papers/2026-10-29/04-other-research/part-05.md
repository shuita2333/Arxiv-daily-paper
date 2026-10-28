# 📦 其他研究 | 2026年10月29日

> 本类共 **257** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-257](./part-06.md)

---

### 201. [GameVerse: A Minute-Scale Gameplay Dataset for Long-Horizon Interactive World Modeling](https://arxiv.org/abs/2610.37257)

**<font color=#1a73e8>作者：</font>** Kang He, Wenshuo Peng, Chuanhao Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in interactive world models have made it possible to generate controllable, dynamic environments from action inputs. Yet current models struggle to maintain coherence beyond roughly one minute of rollout, a limitation rooted not in model capacity but in the scarcity of long-horizon training data. Existing gameplay video datasets typically consist of clips under ten seconds, with captions that describe whole clips in coarse and undifferentiated text, which is insufficient for controllable long-horizon generation. We address this with GameVerse, a minute-scale gameplay video dataset purpose-built for long-horizon interactive world modeling. GameVerse contains 69.7K clips spanning 1,655 hours and 349.6 million frames across diverse first- and third-person gameplay, including 1,358 hours of continuous two-minute sequences, an order of magnitude longer than prior datasets. Clips pass through a unified pipeline of scene-consistent segmentation, quality filtering, camera pose estimation, and event-based caption annotation. Each clip is paired with a temporally stable camera trajectory that remains coherent across minutes, together with captions that separate static scene context from dynamic foreground events and align to event boundaries rather than fixed time windows. Comprehensive analysis shows that GameVerse surpasses existing public datasets in scale, diversity, and annotation quality. Experiments further demonstrate that training on GameVerse substantially extends the temporal horizon of interactive world models.

---


### 202. [An Interactive Mobile Augmented Reality System for Efficient Virtual Model-to-Patient Registration in Thoracic Surgery](https://arxiv.org/abs/2610.37271)

**<font color=#1a73e8>作者：</font>** Emmanuel Ajaero, Pascal Spiegler, George Rakovich 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Video-Assisted Thoracoscopic Surgery (VATS) is a minimally invasive procedure, where precise surgical port placement is vital, yet it relies heavily on surgeon experience and mental mapping of pre-operative imaging in the operating room. To address this challenge, we present an accessible, interactive mobile augmented reality (AR) framework, HILMARTS, to enable accurate and efficient pre-operative virtual model-to-patient registration for AR-guided surgical navigation. Our system runs on a commercially available LiDAR-equipped iPad and supports a user-in-the-loop workflow through a two-stage coarse-to-fine registration process. First, the user performs a manual alignment using the AR view on the iPad. This initial maneuver is then refined through automatic point-cloud registration leveraging the LiDAR sensor. We further introduce a novel occupancy-grid-based Surface Coverage Score to provide real-time, actionable feedback to the operator on the geometric completeness of LiDAR data capture for reliable point-cloud-based alignment. In a phantom study with 16 participants, the system achieved a 3.31+/-1.26mm registration accuracy in ~4 min with a mean System Usability Scale (SUS) of 84.1. These findings highlight the system's accuracy, efficiency, robustness, and potential clinical usability, and could support its applicability to other AR-based surgical navigation tasks.

---


### 203. [Bayesian Inference of Expensive Simulators: Survey and Comparison of Design Choices](https://arxiv.org/abs/2610.37284)

**<font color=#1a73e8>作者：</font>** Šimon Soldát, Václav Šmídl  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a survey of approaches to Bayesian inference with simulator forward models, focusing on settings with prohibitively expensive simulators. In this domain, Bayesian optimization-based methods have emerged as the most promising approach. We unify existing methods into a general framework, enabling consistent reasoning about shared algorithmic structure across the fragmented literature. Within this framework, we identify the primary design choices and perform a systematic empirical comparison of their effects on inference efficiency in terms of required simulation budget.
A key result of our study is that inference efficiency is often dominated by the choice of surrogate-model response variable, as it directly governs the complexity of the modeled function. Specifically, we demonstrate that the prevalent scalar log-likelihood is a poor response variable, as it discards crucial information. Based on this insight, we introduce the concept of custom \emph{proxy variables}: transformations of simulator outputs engineered to retain more information and provide smoother response surfaces, substantially improving inference efficiency over standard response variables.
We provide actionable guidance and a numerically robust Julia package to facilitate practical adoption of Bayesian optimization for simulator inverse problems.

---


### 204. [Taming Noise Initialization for Zero-shot Video Restoration with Image Diffusion Priors](https://arxiv.org/abs/2610.37290)

**<font color=#1a73e8>作者：</font>** Chong Wang, Zixuan Fu, Hao Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in diffusion models have achieved remarkable success in restoring high-quality images in a zero-shot manner. Unfortunately, extending this success to video restoration is challenging due to the substantial computational resources required to pre-train video diffusion models. A rising trend seeks to address video restoration by utilizing a pre-trained image diffusion model, initiating restoration from either frame-wise independent or identical Gaussian noise. Yet, these approaches often fall short, as such simple noise initiations fail to capture and utilize the inherent temporal correlations within degraded video frames. In this work, we propose taming noise initialization for zero-shot video restoration, which preserves the intrinsic temporal correlations by generating initial noises directly using DDIM inversion on the corrupted video frames themselves. Building on this, we introduce an adaptive noise blending strategy that suppresses degradation patterns encoded during DDIM inversion while gradually steering the noise toward a Gaussian distribution. To further emphasize temporal consistency, we propose measurement-guided trajectory attention to better align features across frames. Extensive experiments on multiple video restoration tasks demonstrate that our method outperforms existing zero-shot approaches, consistently achieving superior results on the DAVIS, REDS4, and Set8 datasets.

---


### 205. [Multi-Label Agreement: A Flexible Framework for Inter-Annotator Reliability](https://arxiv.org/abs/2610.37292)

**<font color=#1a73e8>作者：</font>** Tim Menzner, Jochen L. Leidner  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable evaluation of inter-annotator agreement (IAA) is important for assessing the consistency of annotation processes. While established IAA metrics such as Cohen's kappa, Fleiss' kappa, and Krippendorff's alpha are commonly applied in single-label settings, multi-label tasks require additional decisions about how full label sets, joint selections, and joint omissions should be compared.
In this work, we present Multi-Label Agreement (MLA), a flexible framework for evaluating agreement in multi-label annotation tasks. MLA preserves the full binary label vectors assigned to each item and uses average pairwise Hamming agreement, thereby accounting for both joint selections and joint omissions. Its pooled-marginal form is not a mathematically independent coefficient: it is a chance-disagreement-weighted average of label-wise Fleiss/Scott-type coefficients and is closely related to Krippendorff's alpha with normalized Hamming distance. The framework supports pooled-marginal, Gwet AC1, and fixed-baseline normalizations, yields item-level, label-level, and corpus-level results, and includes a conditional minimum-agreement diagnostic. Through a worked example and Monte Carlo simulations, we show how the resulting values depend on label prevalence, the declared label inventory, and the selected model of expected agreement. We also provide a Python implementation. MLA thus offers a transparent and interpretable framework for multi-label agreement analysis without claiming that one normalization is universally preferable.

---


### 206. [TRUCO: A Scalable Lock-Free Algorithm for Parallel Contour Extraction](https://arxiv.org/abs/2610.37297)

**<font color=#1a73e8>作者：</font>** Rafael Munoz-Salinas, Francisco J.Romero-Ramirez, Manuel J. Marin-Jimenez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transforming binary masks into geometric contours remains a critical step in many computer vision pipelines, particularly for post-processing high-resolution segmentation outputs. Yet, standard algorithms such as the Suzuki-Abe method are limited by their sequential nature and the overhead of building topological hierarchies. As modern applications transition to high-resolution imaging, there is a critical need for contour extraction that leverages multi-core CPU architectures without the complexity of tile stitching or heavy synchronization.
This paper presents TRUCO (Threaded Raster Unrestricted Contour Ownership), a lock-free parallel algorithm designed for high-performance geometric boundary extraction. TRUCO introduces a start-point ownership rule, combined with a speculative tracing model, in which threads trace contours downward into adjacent regions and use an upward-termination logic to ensure each contour is processed exactly once.
Experimental results on synthetic and real-world datasets, conducted on both consumer and server-grade CPUs, demonstrate that TRUCO significantly outperforms existing baselines. The method achieves speedups of over an order of magnitude compared to the industry standard while maintaining robust scalability on high-resolution scenes across diverse hardware architectures.

---


### 207. [Understanding Human-Robot Collaboration through Joint Action](https://arxiv.org/abs/2610.37298)

**<font color=#1a73e8>作者：</font>** Chengwen Zhang, Jianyang Wang, Chang Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-robot collaboration requires partners to coordinate interdependent contributions toward a shared goal. Joint Action theory provides concepts for understanding this coordination, but how these concepts are instantiated and combined across empirical research remains fragmented. We conducted a systematic review following PRISMA 2020, identifying 83 empirical papers published between 2021 and 2026. Through theory-driven framework analysis, we organized the literature into nine constructs across three capacities: Representation, Prediction, and Integration. We analyze how these constructs are distributed and co-occur across studies, revealing where empirical evidence concentrates and where it is absent. By mapping empirical HRC research onto a unified Joint Action framework, this review offers a coherent overview of HRC studies, identifies gaps in current evidence, and provides guidelines for future research.

---


### 208. [Structured Representation Probing for Risk Anticipation in End-to-End Autonomous Driving](https://arxiv.org/abs/2610.37299)

**<font color=#1a73e8>作者：</font>** Jiawei Liang, Tianrui Lou, Le Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> End-to-end driving policies form structured internal representations of traffic, ego behavior, and road constraints. These representations offer a monitoring interface for anticipating failures, complementing risk signals from trajectories, controls, and manually designed features. We introduce the Structured Representation Probe (SRP), a lightweight monitor that reads actor, ego, and map representations from a frozen policy. SRP learns a separate linear risk direction for each source and aggregates element scores through cardinality-normalized log-mean-exp pooling, retaining sensitivity to salient evidence while reducing dependence on token count. Event-window supervision links the readout to upcoming hard failures, and auxiliary event type heads jointly train the source directions across failure modes. Online alerting uses a single generic score without modifying the driving policy. Bench2Drive experiments on DriveTransformer, UniAD, and VAD show higher frame-level PR-AUC and ROC-AUC than the evaluated runtime baselines. On DriveTransformer at a horizon of 2 seconds, ROC-AUC reaches 0.833 versus 0.715 for temporal consistency, with 2.67% readout runtime overhead. The trained probes also retain the ability to distinguish impending failures on new routes.

---


### 209. [MvT: Event-based Multi-view Projection for Multiple Object Tracking](https://arxiv.org/abs/2610.37309)

**<font color=#1a73e8>作者：</font>** Muxi Zha, Banglei Guan, Minzu Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras are increasingly used for Multiple Object Tracking (MOT), but their asynchronous event output often requires specialized methods. Existing processing methods primarily follow two paradigms, pseudo-frames and event-by-event. The former is the prevailing approach since its data format aligns with images, making image-based techniques applicable. However, it suffers from tracking failures when trajectories overlap or are spatially close on pseudo-frames. Facing this challenge, we propose a multi-view pipeline, Multi-view Tracking (MvT), which preserves the 2D data format to leverage image-based techniques directly while introducing additional spatio-temporal views to resolve tracking ambiguities in a single view. MvT comprises a Multi-view Projection (MvP) module and a Multi-view Fusion (MvF) stage. MvP encodes events into three complementary spatio-temporal views while mitigating the pattern discretization. Within MvF, multi-view results are unified into a 3D coordinate system, and tracklets are associated through an optimization model subject to specific criteria combination. Evaluations on four datasets, including our self-collected Small Objects Dataset (SOD), show that MvT seamlessly integrates image-based methods and outperforms existing non-learning and learning trackers in generalized scenarios, and effectively resolves the single-view tracking ambiguities. Being training-free, MvT is applicable when ground-truth annotation is infeasible, thereby highlighting its practical, data-efficient potential. Code is available at this https URL.

---


### 210. [A Lightweight Attention-Based CNN with Saliency-Map Interpretability for Skin Cancer Detection](https://arxiv.org/abs/2610.37314)

**<font color=#1a73e8>作者：</font>** Sanjana Islam Kasfia, Md. Ismiel Hossen Abir, AKM Bahalul Haque 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skin cancer is among the most prevalent and life threatening forms of cancer worldwide. Early and accurate diagnosis significantly improves patient survival rates. However, manual dermoscopic assessment remains challenging due to visual similarity. This study proposes an Explainable AI-driven framework for automated binary classification of skin lesions using a lightweight attention-based convolutional neural network (CNN-Attention). The model integrates channel attention to focus on informative regions of dermoscopic images while maintaining low computational complexity. A publicly available dataset comprising 2,637 training and 660 test images was used, with balanced class weights. The proposed model achieved 87 percent accuracy with 1.95 million parameters and 7.45 MB of storage, matching the best baseline (MobileNet) while using approximately half as many parameters and half as much storage. ROC AUC and PR AUC scores reached 0.9475 and 0.9430, respectively. Additionally, saliency maps were incorporated as an explainability technique to visualize regions that influence model decisions. Comparative analysis with VGG16,VGG19,ResNet101,and MobileNet demonstrates the proposed models effectiveness in balancing classification results, computational efficiency, and interpretability.

---


### 211. [Hierarchical Sparse Graph for Multi-dimensional Assignment in Event-based Tracking](https://arxiv.org/abs/2610.37321)

**<font color=#1a73e8>作者：</font>** Muxi Zha, Yang Shang, Wenlong Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing event-based tracking methods typically operate in an online manner, associating tracklets across adjacent batches. However, this limited temporal window often leads to failures in challenging scenarios, such as long-term occlusions or missed detections, where broader temporal context should be incorporated for high-precision tracking. To achieve robust and accurate tracking, this paper concentrates on the event-based multi-dimensional assignment that associates tracklets across multiple batches simultaneously. Unlike image-based detectors, event-based detectors can generate multiple correct yet spatially distinct tracklets for a single object per batch. This violates the one-to-one rule in classic data association, making event-based association an underdetermined many-to-many matching problem. To the best of our knowledge, this is the first work to tackle this NP-hard problem. To address its underdetermined nature, we formulate the assignment problem via fuzzy logic, where pairwise tracklet correlations are quantified through multiple long-range kinematic metrics. This fuzzy design eliminates the need for hard tracking thresholds and enables multiple heterogeneous metrics to be integrated into a unified correlation. By treating tracklets as nodes and their fuzzy correlations as edges, we construct a Hierarchical Sparse Graph (HSG). Building upon the HSG, we pose assignment as a graph partition task, and employ a heuristic solution that measures vertex affinity for partitioning adaptively. The entire pipeline is training-free. Comprehensive experiments on two challenging event datasets, eTram and Ev-UAV, show that our method outperforms existing event-based and most image-based association models. Particularly, it achieves over 2$\times$ the performance of OC-SORT across all metrics in the many-to-many association scenario.

---


### 212. [UCVE: Graph Structured Retrieval for Compliance Validation](https://arxiv.org/abs/2610.37323)

**<font color=#1a73e8>作者：</font>** Emily Chen, Michelle Menachery, Himanshu Kumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structured compliance validation requires determining whether every obligation in a predefined requirement space is satisfied, violated, or unaddressed by a given document. This can be described as a coverage problem that existing retrieval and classification systems, by treating requirements as independent, are not designed to solve. We introduce \textbf{\ac{UCVE}}, a domain-agnostic framework that represents compliance requirement spaces as a \ac{CRG} and performs retrieval via spectral reranking over its reinforcement learning-weighted Laplacian. Edges between requirement nodes are learned via reinforcement learning with a traversal reward grounded in violation detection, reshaping the graph's community structure such that low-pass spectral filtering distinguishes relevant from irrelevant obligation clusters. Evaluating across three compliance domains, \ac{UCVE} averages 4.3\% matched-$K$ recall lift over flat cosine retrieval and consistently outperforms strong retrieval and graph-based baselines.

---


### 213. [ScIntBench: Physical Interaction Plausibility in 3D Scene Generation](https://arxiv.org/abs/2610.37326)

**<font color=#1a73e8>作者：</font>** Wendi Ying, Daochang Liu, Leonid Sigal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing evaluations of text-conditioned 3D indoor scene generation largely emphasize semantic fidelity and physical validity at rest, leaving interaction-time physical reliability insufficiently assessed. To address this gap, we introduce ScIntBench, a unified benchmark centered on interaction readiness: it executes prescribed manipulation actions (e.g., pushing, opening, and surface probing) in physics simulation and measures task success, capability and progress, post-interaction integrity, and dynamic plausibility. Multi-view semantic and static physical evaluations complement these metrics and help explain interaction outcomes. We systematically evaluate 12 state-of-the-art scene generation systems across 10 room types. Our results reveal that strong semantic and static physical performance does not necessarily translate into interaction readiness: a system with near-perfect static plausibility completes only 11.54% of interactions, 7 of the 12 systems produce scenes that cannot support any interaction, and even the best system succeeds in only 36.92% of prescribed tasks. These findings highlight two fundamental challenges in generating interaction-ready scenes: providing the necessary physical interaction capabilities and ensuring reliable physical behavior under active manipulation.

---


### 214. [WCC: A Learning-Based Framework for Deciding When to Apply Cooperative Coevolution in Large-Scale Optimization](https://arxiv.org/abs/2610.37329)

**<font color=#1a73e8>作者：</font>** Wenjie Qiu, Hepei Li, Jianfeng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cooperative Coevolution (CC) and Non-Decomposition Algorithms (NDAs) are two primary approaches for large-scale global optimization (LSGO). Although both have achieved success, they exhibit markedly different performance across problem types and each faces approach-specific limitations, leaving the question of "when to use CC" unresolved. We address this gap with WCC, a novel learning-based framework that dynamically decides when to deploy CC in LSGO. WCC employs a streamlined design for efficient adaptive learning. We formulate the decision as a Markov decision process, designing a targeted feature set, a robust reward, and a tailored network architecture to provide the agent with rich information about the problem state and optimization progress. Our auto-regressive policy enables WCC to perform fine-grained, dynamic switching between CC and NDAs while conditionally allocating the computational budget without expert specifications. WCC shows strong competitiveness and superior generalization across problems, optimization horizons, and baseline optimizers. It realizes a "train-once and reuse" paradigm under a low budget, significantly curbing LSGO cost. Additionally, in-depth analyses yield insights not captured by existing theory, offering practical guidance on when and how to effectively deploy CC.

---


### 215. [Normative Deviation Modeling for EEG-based Depression Detection](https://arxiv.org/abs/2610.37338)

**<font color=#1a73e8>作者：</font>** Wan Jiang, Jingqi Cheng, Hui Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Web-enabled digital health services are expanding access to physiological monitoring and mental health screening. However, electroencephalography (EEG)-based major depressive disorder (MDD) detection remains challenging across heterogeneous data sources, where individual variability and acquisition differences may affect disease-related representations. In this work, we investigate the use of healthy normative references for EEG-based MDD detection. Specifically, structural and distributional reference models are independently trained using healthy control (HC) recordings to characterize departures from healthy EEG patterns. We develop two diagnostic approaches that incorporate normative deviations at different representation levels. Scalar-level Normative Deviation-guided Diagnosis (S-NDD) summarizes structural and distributional deviations into scalar scores and integrates them with deep EEG representations. Feature-level Normative Deviation-guided Diagnosis (F-NDD) retains dimension-wise residuals and combines them with deep EEG representations through attention-based aggregation and auxiliary supervision. We also employ target HC-assisted score calibration for cross-source evaluation without updating the trained models. Experiments on two public EEG datasets examine both approaches under subject-independent within-source and bidirectional cross-source settings. The results demonstrate the effectiveness of normative deviation-guided diagnosis across different evaluation settings.

---


### 216. [Aligning Institutional Power and Operational Ability](https://arxiv.org/abs/2610.37342)

**<font color=#1a73e8>作者：</font>** Andrea Marino, Giovanni Sileno, Thomas van Binsbergen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> To be socially sustainable, Agentic AI systems require normative designs that align responsibilities with the ability to fulfil them. Identifying incongruences such as unsatisfiable expectations or privilege escalation is crucial in avoiding normative pitfalls. In this study, we discuss design dimensions suitable for describing multi-agent systems in light of this norm-ability alignment requirement. We propose a formal framework centred on process-oriented modelling and institutional power for the analysis of a given normatively relevant process, discuss strategies for repairing it, and elaborate on how the symmetrical relation between operational process and institutional state affects the lifecycle of normative positions.

---


### 217. [EmbeddingGemma 2: Unified and Efficient Multimodal Representations](https://arxiv.org/abs/2610.37364)

**<font color=#1a73e8>作者：</font>** Henrique Schechter Vera, Sahil Dua, Jovan Andonov 等 73 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present EmbeddingGemma 2, an open multimodal embedding model which natively represents text, images, audio, video, and combinations thereof in a unified space. Our approach introduces improvements such as simplified per-layer embeddings and a multi-stage curriculum with modality and objective progression which ensure strong quality across unimodal, cross-modal, and mixed-modal evaluations. Notably, in comprehensive embedding benchmarks across all modalities, EmbeddingGemma 2 establishes a new Pareto frontier, outperforming both specialist models and models two to twelve times larger. Furthermore, our design offers flexibility for resource-constrained environments, supporting selective modality encoder loading, adjustable vision token budgets, truncatable embedding dimensions, and quantized weights. We present ablations analyzing key decisions and release EmbeddingGemma 2 to promote further research.

---


### 218. [TRIDENT-Seq: Profile-Matched Prefix-Future Contrast for Label-Efficient Payment Risk Modeling](https://arxiv.org/abs/2610.37365)

**<font color=#1a73e8>作者：</font>** Weiyu Han, Haoyu Jiang, Jie Sheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ant International accumulates large volumes of transaction history across users and payment businesses. Confirmed fraud and chargeback outcomes, by contrast, are scarce, delayed, and specific to each business. A single encoder pretrained on unlabeled histories could serve all businesses, but only if pretraining captures the behavior that separates risk. Coarse activity differences can make contrastive pretraining on transaction logs too easy: transaction volume, amount, and timing can distinguish a history's continuation from arbitrary candidates without modeling how payment resources are used. We present TRIDENT-Seq, a transaction foundation model trained with Prefix-Future Contrast (PFC). PFC matches each prefix to a summary of its subsequent behavior among candidates with similar activity profiles; activity prediction and dispersion regularization act on the encoder output. Across three production payment businesses, the pretrained encoder improves average precision (AP) and recall at a 0.5% intervention budget over architecture-matched scratch training in all six business-budget settings. With a fixed validation set, it exceeds full-label scratch training in mean AP and recall using 10% of the training labels on Wallet and 25% on Shopping and SME. Pretraining only on another business's histories still helps. Replacing profile-matched candidates with random ones cuts recall from 24.62% to 5.64%. In Ant International's deployment evaluation, recorded amount-based chargeback and overall loss rates are 37.7% and 37.9% lower than those of the previous XGBoost-based system under the same intervention budget.

---


### 219. [Euclidean Crowding-Driven Adaptive Euclidean-Hyperbolic Graph Learning](https://arxiv.org/abs/2610.37373)

**<font color=#1a73e8>作者：</font>** Hao Chen, Jian Sun, Chuan Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperbolic graph representation learning has emerged as a powerful paradigm for modeling hierarchical data. Unlike Euclidean space, which exhibits polynomial volume growth, hyperbolic space grows exponentially with radius, naturally accommodating tree-like structures without the geometric distortion known as Euclidean crowding. Despite strong empirical performance, the theoretical mechanisms underlying hyperbolic embeddings remain poorly understood. In this work, we provide a geometric quantifcation research for Euclidean crowding, a generalization-theoretic explanation for the superiority of hyperbolic space on hierarchical data, and further develop an adaptive Euclidean-hyperbolic fusion learning framework toward bridging this gap. Specifically, we \textbf{first} establish a geometric quantification of Euclidean crowding by analyzing layer-wise minimum separation in node embeddings, proving that fixed-dimensional Euclidean embeddings of tree-like graphs inevitably exhibit layer-wise crowding that leads to weaker margin-based generalization bounds. \textbf{Second}, we provide a generalization-bound for the superiority of hyperbolic geometry on hierarchical data. \textbf{Third}, we propose EH-Fusion, a geometry-adaptive framework that lifts Euclidean GNN representations into hyperbolic space via exponential mapping and adaptively fuses both geometries based on node-level neighborhood expansion patterns. Extensive experiments validate our theoretical insights and demonstrate the effectiveness of EH-Fusion on benchmark datasets.

---


### 220. [Comparing Temporal Deep Learning Architectures for Discrete Cross-User Myoelectric Control](https://arxiv.org/abs/2610.37374)

**<font color=#1a73e8>作者：</font>** Ethan Eddy, Evan Campbell, Scott Bateman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The recognition of dynamic gestures via discrete myoelectric control is becoming an attractive input modality for event-based human-machine interaction. While recent work suggests that discrete cross-user models are possible (i.e., no calibration data is required from the end user), few have evaluated techniques to optimize these systems and their generalizability to new randomly prompted data simulating real-world discrete control is relatively unknown. Using the 612-user EMG-EPN dataset, this work benchmarks five temporal deep-learning approaches, evaluates the tradeoff between performance and model complexity, and compares hand-crafted and machine-learned feature extraction techniques. The CNN-GRU achieved the best accuracy of 93% when tested on 184 previously unseen users. These models were then evaluated on a different, more realistic, unsegmented dataset, wherein users were randomly prompted to elicit discrete gestures during a continuous data collection. This dataset was recorded five years apart and in a separate country from the data used to train the original model. Results show that the cross-user results scale to this new dataset (accuracies of 96%) even though no feedback was given to users during the elicitation of gestures. These findings highlight the exciting potential of discrete zero-shot cross-user myoelectric control and offer valuable insights for the continued advancement of this promising technology.

---


### 221. [Para-Gaussian Approximations of Random Deep Neural Networks](https://arxiv.org/abs/2610.37388)

**<font color=#1a73e8>作者：</font>** Mihai Nica, Janosch Ortmann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> It is known that randomly initialized neural networks have Gaussian behaviour in the $n\to \infty$ limit. Unfortunately, this approximation can be poor for finite $n$ and gets worse as one goes deeper into the network. In this work, we develop a more accurate approximation that is \emph{slightly} non-Gaussian, which we call the para-Gaussian distribution and is constructed from the Hermite polynomials. We show how this para-Gaussian approximation can lead to a practical recursive method to approximate the deeper layers of the network. Finally, we apply this theory to linear neural networks (where things can be solved exactly) and to ReLU neural networks (where things can be approximated).

---


### 222. [How Many and How Much? Contrastive Learning with Negative Samples for Knowledge Graph Embedding](https://arxiv.org/abs/2610.37389)

**<font color=#1a73e8>作者：</font>** Sooho Moon, Yunyong Ko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge graph embedding (KGE), a fundamental technique for knowledge-centric Web and KG-augmented AI applications, is commonly trained through contrastive learning with negative samples to learn discriminative representations. Despite its empirical success, two crucial questions regarding negative samples remain underexplored: (Q1) how many negative samples should be used for each positive sample and (Q2) how much should each negative sample contribute to learning? To answer these questions, we propose RADAR, a novel contrastive learning framework for KGE models with two effective strategies, respectively: (1) Risk-aware negative budget allocation quantifies false-negative sampling risk by modeling an open-world KG as a stochastic partial observation of its closed-world counterpart and adaptively assigns a negative budget to each positive sample based on its risk; (2) Distribution-calibrated negative weighting assigns negative weights by calibrating the weighting strength for each positive based on two complementary characteristics of the negative-score distribution: dispersion and concentration. Extensive experiments on 3 real-world KGs with 4 KGE models reveal that RADAR achieves the best KGE performance on average across all model--KG combinations and reduces sampled false negatives by over 90% compared with conventional fixed-budget methods.

---


### 223. [CTBakeGS: training-free baking of photorealistic CT volume renderings into 3D Gaussian splats](https://arxiv.org/abs/2610.37406)

**<font color=#1a73e8>作者：</font>** Haruki Fukuda, Constantin Lux, Wolf Schweitzer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Photorealistic volume rendering of computed tomography (CT) may convey anatomy intuitively, but it needs the CT data, dedicated software and a powerful graphics processor. Three-dimensional Gaussian splatting (3DGS) displays photorealistic scenes in real time on less powerful devices, but existing medical approaches train each scene for minutes to hours. We aimed to convert a CT volume rendering directly into a 3DGS model without training. Splats were placed on an adaptive octree of millimetre-sized cells. Their colour and opacity were computed on the graphics processor with the renderer's lighting, cell opacity was converted analytically into splat opacity, and faint splats were retained stochastically above the 1/255 opacity floor of standard 3DGS rasterisers. Six public CT scans (1.5-mm voxels) were converted with three transfer functions and compared with converged references by peak signal-to-noise ratio (PSNR), structural similarity and a learned perceptual metric. Two-million-splat models reached a PSNR of 32.6 +/- 0.9 dB for bone, 30.1 +/- 1.0 dB for contrast-enhanced vessels and 32.3 +/- 1.5 dB for skin and bone. A conversion pass (usually two or three per model) took 4-30 s on a current laptop and 9-60 s on a desktop with a 4-GB graphics card. On the laptop, the models rendered at 68 frames per second at 800 x 800 pixels. Training-free conversion produced real-time 3DGS models of photorealistic CT renderings in about a minute or less per conversion pass on ordinary computers, with fidelity that we consider sufficient for interactive viewing.

---


### 224. [Constraining the Commit Boundary: A DIO/ODI-Informed Authorization Guardrail for Agentic Entity Resolution](https://arxiv.org/abs/2610.37407)

**<font color=#1a73e8>作者：</font>** Daniel Beránek  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic Entity Resolution (ER) systems iteratively plan actions, retrieve evidence, revise hypotheses, and propose graph mutations. An erroneous identity hypothesis may condition later retrieval and produce apparent confirmation. This paper proposes a Digital Identity Optimization (DIO) and Ontology of Digital Identity (ODI)-informed authorization boundary between evidence available for agent reasoning and evidence eligible to authorize persistent identity-changing mutations.
A domain-governed constraint-binding function maps selected reconstruction-failure distinctions to explicit identity-preserving constraints. An abstract two-phase supervisor permits a commit only when claim-specific authorization-eligible evidence supports every required proposition, relevant conflicts are resolved, the operation remains within its authorized scope, and relevant state and policy versions remain valid. Admission as UNVERIFIED does not confer authorization eligibility. Separate claim-specific promotion governs evidentiary use; insufficient support or unresolved material conflict leads to deferral.
The contribution is a specification connecting diagnostic-to-constraint mapping, evidence promotion, proposition coverage, conflict handling, scope binding, and commit-time version integrity. A proposed evaluation protocol is designed to assess the mapping's incremental value beyond generic authorization and conventional identifier rules. This is a conceptual architecture without implementation or empirical validation, not a theorem of semantic correctness. Its property depends on domain-policy adequacy, evidence promotion, and enforcement. It does not prevent erroneous hypotheses or hypothesis-conditioned retrieval; dependency-aware evidence flow remains future research.

---


### 225. [Displacement Moments and Path-Terminal Separation in Brownian Interpolant Sampling](https://arxiv.org/abs/2610.37413)

**<font color=#1a73e8>作者：</font>** Zhong Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Brownian stochastic interpolants connect paired endpoint samples, yet their sampling error can depend on displacement moments even when neither endpoint has a first moment. For arbitrary Borel couplings, we prove early-stopped, target-to-output KL guarantees for standard Euler sampling from the true source. A fourth displacement moment gives an explicit $O(N^{-1})$ bound; a second moment suffices for fixed-law convergence as drift error vanishes. For one fixed coupling with no displacement moment above two, original bridge-path KL stays of order one, comparison-path KL is of order $1/\log N$, and terminal KL is at most $C/N^2$ on the same grid. The path decomposition identifies the information about the source discarded by Markov projection. When the original bridge is Markov, current-state Euler sampling instead has a second-moment $O((M_2+d)/N)$ bound; finite-entropy Schroedinger bridges for the probability Brownian reference are included. We also construct a current-state learner with expected output KL consistency from iid endpoint pairs. Numerical diagnostics illustrate the distinct errors. Conditional diffusion identities specify a restoration interface, while image controls find no iterative advantage over cheap probabilistic predictors. Uniform terminal rates for general second-moment couplings remain open.

---


### 226. [Time-Dynamic Semantic-Activity Entanglement: Quantifying Communication-Based Synchrony in Collaborative VR](https://arxiv.org/abs/2610.37427)

**<font color=#1a73e8>作者：</font>** Pooja Pol, Jianing Zhang, Qing Huang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Collaborative virtual reality (VR) produces rich multimodal traces of team behavior, yet practical methods for characterizing time-varying team communication remain limited. We present time-dynamic semantic-activity entanglement (TSAE), inspired by the entanglement concept introduced by Gloor et al. (2022), to describe communication-based team synchronization within discrete time windows. TSAE is modeled by combining relative speaking activity with contextual semantic alignment for participant pairs, which is aggregated into participant-level trajectories and summarized through the Gini coefficient to understand the distribution of team-level communication synchrony. This approach is employed with German-language transcripts from fifteen collaborative VR gameplay sessions. Transcript utterances are represented using a long-context embedding model with a late-chunking strategy and analyzed within fixed game-time windows. A representative session illustrates shifting dyadic alignment and low-to-moderate participant contributions, with sporadic periods of high entanglement. Across fifteen game sessions, the metrics indicate complementary insights, offering a qualitative contrast to the core-periphery pattern reported in the foundational work. Hence, these descriptive findings support the study of communication as a dynamic process and provide a mathematically grounded approach to analyze its evolving distribution in shared interactive VR spaces.

---


### 227. [Segmentation Confidence for Arbitrary CNNs](https://arxiv.org/abs/2610.37431)

**<font color=#1a73e8>作者：</font>** Baris Oguz, Xing Yao, Claudia Tawil 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Convolutional neural networks (CNN) are widely used for medical image segmentation. However, they lack an inherent measure of confidence. Existing methods for estimating prediction uncertainty often require a custom network architecture and/or dedicated training setups and need to be trained from scratch. In addition, the deduction of a single confidence score per input from the uncertainty maps is not always straightforward. In this study, we explore voxel-based uncertainty estimation methods that can be added to existing segmentation pipelines without training from scratch. We also propose a novel method to estimate a single confidence score from the uncertainty maps. Our evaluations on different ROIs and modalities suggest that our confidence score can predict segmentation performance in unseen data.

---


### 228. [Representing the Unseen: Rethinking Visual Imagination for Spatial Reasoning](https://arxiv.org/abs/2610.37437)

**<font color=#1a73e8>作者：</font>** Zengqi Zhao, Zun Wang, Shoubin Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual world models increasingly support spatial reasoning by generating RGB views of unobserved states. However, RGB has become the default interface largely because it is well suited for visual generation, rather than necessarily being the most effective representation for downstream reasoning. Different spatial questions may benefit from different representations of the same imagined state: top-down geometry can facilitate global distance comparisons, while panoramic views provide broader context for reasoning about open space. To isolate the role of representation in spatial imagination, we introduce ImagiRep, a simulator-grounded benchmark of 922 questions spanning seven question types across two settings, Viewpoint Imagination and Cross-view Integration, providing oracle RGB and six alternative representations (e.g., depth, panoramic views, and top-down geometry) of the same unobserved state. This controlled comparison reveals that even accurate imagined RGB does not guarantee accurate spatial reasoning, and different questions benefit from different representations. Similar trends hold for representations derived from world-model-estimated states. Notably, estimated RGB alone can mislead spatial reasoning, while alternative representations retain complementary benefits. Building on these findings, we introduce GEARS, a lightweight test-time strategy for adaptive representation selection, outperforming existing spatial imagination methods and showing that reasoning about unseen states requires more than generating RGB views.

---


### 229. [Test-Time Communication in Trading Agent Swarms](https://arxiv.org/abs/2610.37448)

**<font color=#1a73e8>作者：</font>** Avid Fayaz, Harry Zhang, Håvard Alstadheim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Communication between agents has mostly been studied on tasks with a shared objective and fast, clear feedback. Trading has neither: each agent manages its own account, with decisions being scored by markets late and noisily. A trading swarm is thus a population of independent decision-makers rather than a team, for which convergence is a risk and not the goal. We ran 200 agents from four model families in groups of ten under five communication regimes, from isolation to message boards and shared notes, over seven US trading days (1 to 9 October 2026), logging everything each agent read before every decision. In two of the four families, communicating groups came to hold far more of the same stocks than the isolated group. A group's return was largely the return on what its members held in common. Seeing a post from a groupmate made an agent 7 percentage points more likely to reuse an eight-word phrase from it. Agents that started too close together to see each other's posts shared such a phrase in 14% of cases, the rate that common inputs produce. Seeing the post did not detectably change that morning's trades. Case studies traced the adoption of positions and decision rules over subsequent days, and communicating groups sold in step more often than isolated ones. Because isolated groups also converged on the same stocks, sometimes completely, assessments of herding need to measure excess convergence relative to a no-peer baseline.

---


### 230. [SecDMP: Provably Secure Data Memory-Dependent Prefetching (Extended Version)](https://arxiv.org/abs/2610.37454)

**<font color=#1a73e8>作者：</font>** Jens Sprengers, Marton Bognar, Lesly-Ann Daniel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Data memory-dependent prefetchers (DMPs) are a microarchitectural optimization recently introduced in mainstream desktop and server CPUs. Although DMPs offer performance improvements, they have been shown to enable side-channel leakage of secrets, even from constant-time code that has been hardened against Spectre attacks. Unfortunately, existing defenses either incur significant performance overhead or, as we show, fail to prevent all DMP leakage.
In this work, we address this gap by designing a defense that is both secure and efficient. First, we propose a classification of DMP leakage, categorize existing and novel attacks, and analyze which leakage classes are mitigated by existing defenses. We validate this analysis empirically by implementing the first open-source DMPs on a RISC-V processor, showing that the only existing defense that aims to preserve DMP performance fails to protect against entire leakage classes. Next, we propose SecDMP, a provably secure and efficient hardware-based defense. SecDMP requires secrets to be marked in memory and ensures that DMPs never encode these secrets in the microarchitecture---without compromising performance for public data. We formally prove that SecDMP introduces no leakage beyond a baseline semantics without DMPs. Notably, when combined with speculative-execution defenses, SecDMP restores complete microarchitectural security for constant-time code. Finally, our empirical evaluation shows that SecDMP prevents all DMP leakage while incurring minimal performance overhead and hardware cost.

---


### 231. [An Input Skip Can Reparameterize a VAE Without Improving the Generator](https://arxiv.org/abs/2610.37456)

**<font color=#1a73e8>作者：</font>** Kevin Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An input skip can reduce reconstruction error while leaving a model's distribution of new samples unchanged. For a Gaussian variational autoencoder (VAE) with constant input skip $0\leq\alpha<1$, a model without a skip can be written in skip form by multiplying its decoder output by $b=1-\alpha$ and its noise variance by $b^2$. The distribution of observations and latent variables and its exact generative scores stay the same, while reconstruction mean squared error (MSE) is multiplied by $b^2$. Separate training can produce different generators because optimization depends on the parameter coordinates. In a Gaussian experiment with known density, changing skip and observation variance together reduces MSE but worsens energy score and the estimate of negative log density from importance sampling. On seven annual Deep-ocean Assessment and Reporting of Tsunamis (DART) records, energy score differences at the same observation variance have both signs on four original records and favor the skip on three records from 2018. Probabilistic principal component analysis (PPCA) has lower mean energy scores than every neural DART fit. With the encoder and decoder kept the same, estimating observation variance from training reconstruction error can also worsen energy score. Assessing generation requires more than reconstruction error.

---


### 232. [Penny for Your Prompts: A Measurement Study of Contextual Leakage in AI Chat Platforms](https://arxiv.org/abs/2610.37467)

**<font color=#1a73e8>作者：</font>** Paschalis Bekos, Billy Tsouvalas, Nick Nikiforakis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI chatbot platforms have become one of the most popular web interfaces users interact with online, routinely receiving personal and intimate information shared under an expectation of privacy. Yet, on the web application side, these platforms have the ability to embed third-party analytics, advertising, and session replay scripts that operate silently alongside the chatbot, creating an underexamined channel for conversational data leakage towards third parties. We conduct the first systematic large-scale measurement study of contextual leakage in AI chatbots, auditing the web interfaces of 42 general-purpose and domain-specific (health, legal, and education) platforms. Beyond standard network interception, we instrument the browser at the JavaScript engine level to attribute each data flow to the exact user action that triggered it, and the DOM capture mechanism used to retrieve its content, a granularity invisible to network-layer analysis alone. We find that 21 of these platforms leak conversation titles to third-party trackers, while nine leak verbatim user prompts. Beyond content, we observe a substantial amount of chatbot platforms sending user emails to third-party trackers, enabling the association of conversational context with a user's identity. Our findings cast traditional web privacy issues under a new light, highlighting the privacy issues that are inherent in how users interact with modern AI chatbots.

---


### 233. [Who Shaped What? Untangling Human and AI Creative Contributions Through Spatial Provenance in Image Editing](https://arxiv.org/abs/2610.37469)

**<font color=#1a73e8>作者：</font>** Riya Sahni, Christine Dierk, Lydia Chilton 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Images co-edited with AI are often labeled to disclose AI use. However, creators feel these labels do not sufficiently describe their contributions to the editing process. Editing histories preserve requests, suggestions, and revisions, but how do creators use these logs to judge contribution? We investigated this with Roop, a mixed-initiative design probe that links image regions to editing histories (spatial provenance) and summarizes interactions in a heat map. Twenty participants edited images, annotated human and AI contributions, then reviewed the spatial provenance heat map. Participants credited themselves for directing changes while crediting AI for determining visual details. They judged contribution partly by whether their interactions achieved their intentions. Reviewing provenance helped participants remember interactions without always changing whom they credited. These findings motivate provenance systems that preserve enough context for creators to explain how interactions shaped their work, alongside the record of what happened.

---


### 234. [How Reliable Is Individualized Functional-Network Attribution in Resting-State fMRI Cognitive Prediction in ADNI?](https://arxiv.org/abs/2610.37472)

**<font color=#1a73e8>作者：</font>** Sheethal Bhat, Mahfuzur Rahman Chowdhury, Imam Ahmed Shaik 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Individualized attribution estimates which functional networks drive a model prediction for a given subject and is often proposed as an interpretable resting-state fMRI (rs-fMRI) biomarker, but its test-retest reliability is rarely quantified. We evaluate per-subject network-ablation attribution for a frozen resting-state functional connectivity (FC) predictor (Schaefer-200 FC predicting MMSE/ADAS-Cog13) trained on N=875 subjects from the Alzheimer's Disease Neuroimaging Initiative (ADNI), using, and (iii) a subject-level permutation null. Split-half reliability is near-ceiling (Spearman p=0.948/0.950) but drops on scan-rescan (p=0.609/0.616). Under the mismatched-subject null, correlations remain substantial (p~0.46-0.47), indicating strong population-shared structure, yet matched pairs exceed this null (z~6.6-6.9, p<=10-4). Thus, in ADNI, individualized network attribution contains a modest but non-zero person-specific component atop a strong population-shared pattern. We recommend reporting scan-rescan reliability together with a permutation-null control, rather than within-session proxies alone, to avoid overstating individual specificity.

---


### 235. [When POST Becomes GET: Investigating HTTP Method Interchangeability and Its Security Implications](https://arxiv.org/abs/2610.37474)

**<font color=#1a73e8>作者：</font>** Matteo Golinelli, Seif Errahmane Hannachi, Bruno Crispo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> HTTP method semantics are a common boundary between safe retrieval and state-changing operations; however, deployed web applications do not always enforce this boundary consistently. In this paper, we study HTTP method interchangeability, a behavior where a POST request can be rewritten as a GET request to the same endpoint, with POST body parameters moved into the query string, while preserving an equivalent observed response. We present Method Interchange Detection Engine (MIDE), an automated pipeline that crawls web applications in a browser, records POST requests generated by page loads and user-interface interactions, converts supported POST bodies into GET candidates, and compares replayed responses with the original POST response. To avoid counting generic or parameter-independent responses as interchangeable, MIDE also sends a no-query GET baseline. We treat as high-confidence evidence of interchangeability only the cases where the converted GET matches the POST, while the baseline does not. We perform a large-scale unauthenticated experiment on the Tranco top 10k. We find high-confidence interchangeable requests on 407 of 10,000 tested sites (4.1%), 407 of 3,200 sites with captured POSTs (12.7%), and 407 of 2,734 sites with replayed POSTs (14.9%). A targeted Cross-Site Request Forgery (CSRF) token-replay check finds cases where invalid tokens are rejected for POST but accepted for the equivalent GET. We also observe Web Cache Deception (WCD) conditions and cacheable GET responses for interchangeable request instances. These results demonstrate that method interchangeability is observable in real web applications and can expose method-scoped defense gaps.

---


### 236. [From Interaction to Capability: Task Advancement as State and Supervision for GUI Agents](https://arxiv.org/abs/2610.37482)

**<font color=#1a73e8>作者：</font>** Ziyang Chen, Qian Li, Chengwei Qin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> GUI memory should preserve the results of past actions and learn reusable operations. This is difficult in long-horizon workflows, where agents must use information across applications and useful operations are interleaved with failed attempts. We introduce Task Advancement Memory (TAM), which defines task advancement as verified task progress, and supports ongoing task execution and learns reusable operations. During execution, Task Advancement State represents how verified task progress changes the remaining goals, allowing the agent to build on earlier achievements across applications. After each task, advancement supervision identifies and abstracts the interactions that produced a verified local result. The learned operations preserve the relation between required inputs, expected outcomes, and verification conditions. This retains locally successful operations from both successful and failed tasks. On MobileWorld GUI-only tasks, Advancement State alone raises success from 12.0% to 28.2%. Full TAM achieves a 17.6% relative gain in task success over the strongest evaluated baseline and reduces lifecycle tokens per solved task by 38.7%. On SPA-Bench, TAM achieves state-of-the-art task success in the single-app English Level 3 setting.

---


### 237. [Revisiting Privacy Risks in Quantized Deep Neural Networks](https://arxiv.org/abs/2610.37488)

**<font color=#1a73e8>作者：</font>** Jie Fu, Ren Li, Wendy Hui Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model quantization has become a fundamental technique for enabling the efficient deployment of large-scale deep neural networks (DNNs) in data-intensive applications by reducing model size. Despite its widespread adoption, the impact of quantization on training data privacy --- particularly vulnerability to membership inference attacks (MIAs) --- remains largely unexplored. In this paper, we present the first comprehensive empirical study of privacy risks in quantized DNNs, evaluating eight state-of-the-art MIA attacks across six representative quantization methods. Our results reveal that practical quantization levels (4-8 bits) have limited impact on membership privacy risks, with quantized models remaining largely as vulnerable as their full-precision counterparts. Although aggressive low-bit quantization (e.g., 2-bit) can provide meaningful privacy gains, these benefits come at the cost of substantial utility degradation. To understand the underlying causes of these observations, we systematically analyze how different quantization strategies affect model behaviors and outputs, and how these changes influence privacy vulnerability. Beyond evaluating attack risks, we further investigate whether existing privacy defenses developed for full-precision DNNs can effectively protect QNNs. Our results show that these defenses provide only limited additional privacy protection when applied to quantized models, while further amplifying utility degradation. Our study provides practical guidance for privacy-aware deployment of quantized DNNs and motivates the development of new attack and defense mechanisms for QNNs. Our code and datasets are publicly available at this https URL.

---


### 238. [ALADDIN: Adversarial Latent Diffusion Distillation for One-Step Identity Swapping](https://arxiv.org/abs/2610.37503)

**<font color=#1a73e8>作者：</font>** Ivan Shchekotov, Timofei Gritsaev, Viacheslav Pirogov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face swapping transfers a source identity onto a target image while preserving the target's pose, expression, hair, and lighting. The most realistic current methods are diffusion-based, but they need many network evaluations per image. GAN-based methods are fast, yet trained from scratch they must learn realism from the adversarial signal alone and produce visibly weaker results. We present ALADDIN (Adversarial Latent Diffusion Distillation for One-Step Identity Swapping), a one-step face swapper obtained by initialising the generator from a pre-trained multi-step flow-matching model and training it adversarially under identity and target-preservation constraints. We expose a controllable trade-off between identity transfer and target-attribute preservation by training a student model with triplet pseudo-label supervision. We additionally identify a bias in the standard evaluation protocol, which favours methods trained against the same identity encoder used to score them, and re-evaluate all baselines with an independent one. ALADDIN is state-of-the-art among one-step methods in realism and target preservation at comparable identity transfer, and matches the best multi-step model with 28 times fewer network evaluations and an order of magnitude fewer training pairs.

---


### 239. [Strategyproof Deep Reinforcement Learning for Online Resource Allocation](https://arxiv.org/abs/2610.37504)

**<font color=#1a73e8>作者：</font>** Fariba Dehghan, Sebastian Stein, Vahid Yazdanpanah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Online resource allocation faces two coupled challenges: (1) allocating scarce resources efficiently under uncertain future demand, and (2) ensuring that agents report task valuations and requirements truthfully (strategyproofness). Reinforcement Learning (RL) adapts allocation decisions through experience but does not necessarily ensure strategyproofness. Existing strategyproof RL uses a linear allocation rule, which limits the resource interactions it can represent. Neural mechanism design methods offer greater expressiveness, but provide only approximate incentive guarantees. Against this background, we introduce the first strategyproof deep RL mechanism for online resource allocation. It integrates three novel components: (i) a monotonic neural network that learns nonlinear interactions by construction (higher reported value cannot reduce acceptance, while a longer reported duration or larger resource requirement cannot increase it); (ii) a generalised critical payment: the lowest accepted value, with all other inputs fixed; and (iii) training by either RL or imitation of an existing rule. Together, monotonicity and the critical payment ensure strategyproofness and individual rationality, while the neural rule provides flexibility and imitation improves training efficiency. Empirically, on a four-resource stream with two partner pairs that a linear difference cannot represent, the neural rule achieves 97.8% of an offline welfare upper bound, compared with 93.8% for a linear learner and 89.0% for first-come, first-served, closing 65% and 80% of the remaining optimality gap, respectively. Moreover, imitation reaches 97.5% in only 261 seconds, about 89 times faster than RL.

---


### 240. [The Structure Gap: When More Data Cannot Replace Structured Reasoning](https://arxiv.org/abs/2610.37523)

**<font color=#1a73e8>作者：</font>** Kheer Sagar Patel, Mojtaba Soltanalian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A persistent belief in modern AI is that sufficiently large learners trained on sufficiently much data can make explicit domain knowledge optional. This paper examines a limitation of that belief. We define structure-encoded problems: tasks whose input-output map is determined, or sharply constrained, by known structure such as a solver, symmetry group, graph, physical law, measurement operator, grammar, combinatorial search space, or optimization objective. For such tasks, the central question is not expressivity--a dense neural network may contain the desired map--but finite-data identification, extrapolation, and certification. We introduce the structure gap: the finite-resource gap between a method that receives the governing structure and a learner that receives only examples. The strongest useful form of the claim is asymptotic rather than absolute: structure-agnostic learning may approach a structured solver as coverage grows, but every finite dataset can leave residual uncertainty that the structure resolves by construction. We prove this exactly for a Gaussian inverse problem: the known-operator Wiener solver attains Bayes risk, while the dense empirical learner in the correct linear class has persistent expected excess risk. We also prove a cell-coverage lower bound and an unobserved-orbit non-identifiability result. Controlled experiments in known-operator inversion, sparse recovery, and graph reachability with size extrapolation instantiate the mechanisms. When validated structure is available, it can constrain the hypothesis space before learning begins, leaving learning to address components the structure does not specify.

---


### 241. [GTFormer: A Syntax-Free Graph Network Alternative to Transformers for 8192$\times$ Length Extrapolation in Linear Time](https://arxiv.org/abs/2610.37524)

**<font color=#1a73e8>作者：</font>** Elisabeth Fink  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-attention mechanisms have established the Transformer as the dominant backbone across natural language processing, source code intelligence, and automated theorem proving. However, all-to-all pairwise token comparison enforces a quadratic $\mathcal{O}(N^2)$ compute and memory barrier alongside severe softmax attention dilution as sequence length $N$ scales beyond the training horizon. Inspired by recent advances in algebraic graph learning (\textbf{WPNet}), this work introduces \textbf{GTFormer}, a syntax-free hierarchical Graph Neural Network (GNN) that replaces flat self-attention for general long-context sequence modeling. GTFormer organizes raw token streams into a bounded-degree hierarchy combining a balanced binary reduction tree ($\lceil \log_2 N \rceil$ depth), horizontal boundary-bridging shift edges, random expander shortcuts, multi-channel convex highway gating, and a top-down broadcast pass. Across eight long-context code, log, and multi-hop retrieval benchmarks trained exclusively on sequences of length $N \le 512$, GTFormer extrapolates zero-shot to $N = 4{,}194{,}304$ ($8192\times$) on a single commodity GPU in linear $\mathcal{O}(N)$ memory, maintaining near-perfect accuracy where standard and RoPE Transformers suffer from out-of-distribution attention collapse and out-of-memory exhaustion.

---


### 242. [GroundControl: Satellite-Conditioned Multi-View Diffusion for Reconstruction-Free Novel View Synthesis](https://arxiv.org/abs/2610.37545)

**<font color=#1a73e8>作者：</font>** Akshay Krishnan, Matias Turkulainen, Jamie Wynn 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view or video diffusion models have recently emerged as state-of-the-art approaches for novel-view synthesis from sparse image collections. While they can produce high quality images, they tend to hallucinate unrealistic spatial layouts when synthesizing views outside the input views (scene extrapolation). We propose to address this challenge for outdoor scenes by using satellite images as an additional information source to condition the multi-view generative model. We introduce a new satellite-conditioned multi-view diffusion model that combines conditioning from a satellite image and street-level input images when generating novel-views. Our cross-attention based conditioning allows us to retain pretrained multi-view diffusion priors to generate seamless, realistic, novel views from a handful of source views, while also adhering to the scene layout as seen from satellite images. Our model does not use 3D scene reconstruction, and only relies on posed street and satellite views. Our experiments on outdoor datasets show that our model is better than both satellite-conditioned or street-view conditioned baselines on novel-view synthesis, especially on challenging cases where target views have very little overlap with source views. Project page: this https URL

---


### 243. [When uncertainty quantification fails: structural vulnerabilities and corrections for selective prediction under clinical class imbalance](https://arxiv.org/abs/2610.37561)

**<font color=#1a73e8>作者：</font>** Walter Endrizzi, Flavio Ragni, Raffaele Marchesi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background. Selective prediction systems improve the safety of clinical artificial intelligence by deferring ambiguous cases to human experts while automating high-confidence decisions. However, this safety mechanism relies entirely on the premise that uncertainty scores accurately reflect clinical ambiguity. In prognostic tasks characterized by severe class imbalance, where the clinical outcome of interest is a minority, this assumption breaks down. Standard uncertainty measures cease to capture clinically aligned ambiguity; instead, they become a proxy for class membership, systematically penalizing minority patients regardless of their individual predictive clarity.
Results. Across 56 synthetic conditions and three neurodegenerative cohorts spanning severe class imbalance to near-balanced conditions (multiple sclerosis, Parkinson's Disease, Alzheimer's Disease), our framework consistently maintained bounded, balanced risk across trajectories. In contrast, global metrics either collapsed minority Sensitivity or protected the minority at the expense of majority patients. Applying CCR with standard entropy fails to protect the minority because it breaks within-class monotonicity when tau=0.5. Combining CCR with threshold-aware metrics restores strict monotonicity, correctly identifies ambiguous patients, and safely mitigates minority exclusion.
Conclusions. Under clinical class imbalance, standard uncertainty quantification measures dataset sparsity rather than clinical ambiguity, creating a systemic illusion of safety. This bias is a correctable structural flaw. Clinical pipelines deploying selective prediction under imbalance should adopt threshold-aligned uncertainty measures and class-stratified evaluation. This reduces class-specific risk imbalance, supporting safer selective prediction under the evaluated conditions without silently excluding the most vulnerable patients.

---


### 244. [Pneuma: A Large-Scale Real-World Time Series Benchmark for Commercial Aircraft Predictive Maintenance](https://arxiv.org/abs/2610.37563)

**<font color=#1a73e8>作者：</font>** Jiafeng Lin, Yutian Zhang, Huan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive maintenance is vital for commercial aviation, yet progress remains hindered by the lack of public, large-scale real-world datasets. As a result, most methods are developed and evaluated on proprietary data, limiting reproducibility. We introduce Pneuma, the first publicly available large-scale benchmark for predictive maintenance using onboard time series from in-service commercial aircraft. Built around bleed air systems, Pneuma contains over 920 million multivariate time steps across four aircraft types and 9 verified fault scenarios, directly aligned with real maintenance logs. The dataset exhibits key real-world challenges, including substantial class imbalance, subtle fault evolution patterns, and significant variance across aircraft configurations. We structure the benchmark around three tasks: multivariate forecasting, supervised fault classification, and unsupervised anomaly detection, with labels derived from actual maintenance records. Under unified settings, we evaluate over 25 models from four methodological families on 9 carefully curated subsets. The results reveal that even strong contemporary models struggle with subtle fault signatures. Further analyses show consistent gains from additional in-context examples and multivariate inference, while forecasting quality is strongly associated with anomaly detection performance. Together, these findings provide practical insights into effectively modeling complex real-world aviation time series. We hope Pneuma will serve as a rigorous and reproducible foundation for advancing data-driven predictive maintenance toward real-world deployment in commercial aviation.

---


### 245. [ReferStream: Interactive Subject Injection for Streaming Video Generation](https://arxiv.org/abs/2610.37566)

**<font color=#1a73e8>作者：</font>** Shuolin Xu, Guanyuan Li, Boyu Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Injecting new subjects naturally during streaming video generation requires integrating newly supplied visual references into the existing video while preserving established subjects and the scene. Encoding references independently of the current scene provides little guidance for this integration, while keeping their features in persistent memory can interfere with established context. We propose ReferStream, a framework that requires no additional training and combines reference construction using the current scene with transient cache injection. Joint Latent places reference latents in target regions of the latest scene latent, allowing reference features to be extracted in context. Cache Restoration uses these features to condition the injection chunk, then restores the overwritten global cache entries while retaining the newly generated history. This procedure incorporates new visual conditions without retraining the generator or revising emitted frames. We further introduce ReferStream Bench, a new benchmark with scheduled reference arrivals, evolving instructions, and explicit annotations of subject presence for InShot and MultiShot generation. Evaluation follows the event schedule and measures both the fidelity of new subjects and the preservation of established subjects, alongside video quality, text adherence, and count accuracy. Experiments on ReferStream Bench show higher scores for text adherence, subject similarity, and count accuracy than the compared baselines, including offline methods given all references in advance. Project page: this https URL.

---


### 246. [The Noise Plane: A Diffusion Bridge Across Exponent and Dispersion](https://arxiv.org/abs/2610.37576)

**<font color=#1a73e8>作者：</font>** Xuran Hu, Yuru Jia, Tengxi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based denoising commonly uses Gaussian perturbations, whereas sensor noise follows diverse signal-dependent statistical laws. In this paper, we propose $p$-Bridge, a unified measurement-indexed diffusion framework for Tweedie noise. The noise exponent $p$ describes the variance--intensity relation, while accumulated measurement $\nu$ controls the noise level. Together, they define a noise plane that includes Gaussian, Poisson, and Gamma models. The stochastic bridge connects measurement distributions through independent increments, giving denoising a physical interpretation as progressive measurement accumulation. Both the starting and stopping indices can be specified, allowing restoration from an observed measurement level to a prescribed higher level. Measurement superposition yields a shared reverse-mean update, paired with a deviance-based objective for learning the required conditional mean. A latent compound Poisson--Gamma construction enables sampling at intermediate exponents. A single exponent-conditioned network adapts to different Tweedie noise models without separate training for each exponent. Experiments show that exponent conditioning improves cross-exponent robustness over fixed-exponent models. Using estimated exponents, the shared network achieves robustness comparable to an oracle-selected set of five specialist models. Experiments on synthetic images, FMD fluorescence microscopy, and multi-sensor SAR images further demonstrate its effectiveness across different signal-dependent noise regimes.

---


### 247. [Zero-Shot Multimodal Event Spotting in Soccer Broadcasts](https://arxiv.org/abs/2610.37583)

**<font color=#1a73e8>作者：</font>** Sadia Kamal, Mahmudul Hasan, Tony Braskich  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic soccer event spotting supports highlight generation, video indexing, and sports analytics, but existing methods depend on large annotated datasets and soccer-specific training. We present a zero-shot framework that detects, classifies, and temporally localizes events in full-length soccer broadcasts without task-specific parameter training. Each match is segmented into overlapping clips represented by a compact visual storyboard and the aligned commentary transcript, which a general-purpose multimodal model processes jointly. On three manually annotated matches containing 130 events, the best configuration achieves 72.0% F1@5s and outperforms SoccerNet-trained CALF and NetVLAD++ in a cross-dataset setting, while the storyboard representation reduces inference cost by 72% compared with individual frames. We further analyze the effects of model family, input representation, and prompt optimization, and introduce an evidence-grounded excitement-scoring stage that ranks detected events with natural-language explanations for highlight selection.

---


### 248. [Timestral](https://arxiv.org/abs/2610.37585)

**<font color=#1a73e8>作者：</font>** Adrien Petralia, Alexandre Gavaudan, Artjom Joosen 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Timestral, a family of four time series foundation models for probabilistic forecasting, with 5M, 28M, 123M, and 209M parameters. Timestral sets a new state of the art on GIFT-Eval, TIME, and fev-bench, where Timestral-209M and Timestral-123M take the top two places on every metric. We achieve this with three ingredients: Decoupled Horizon Forecasting (DHF), which separates prediction tokens from the causally encoded context, so that longer horizons are trained without masking context and each observed value is both a forecast target and context for later forecasts; a covariate framework that natively supports known-future covariates within a causal architecture; and a two-stage pipeline that pretrains exclusively on a diverse, large-scale synthetic corpus before post-training on a mix of real and synthetic data with extended context. This report describes the model design and its benchmark results. Weights for all four models are available on Hugging Face and inference code on GitHub.

---


### 249. [Understanding the limits of latent world models](https://arxiv.org/abs/2610.37588)

**<font color=#1a73e8>作者：</font>** Rodrigo Gonzalez Laiz, Steffen Schneider  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models are widely proposed as core components for enabling agents to reason over long temporal and spatial horizons. Yet current evaluations often emphasize task performance while providing limited insight into whether learned world models acquire predictive latent dynamics that reflect the underlying structure of the environment. Here we introduce the concept of faithful latent world models as an equivariance condition between the environment's transition map and the learned latent dynamics. We propose latent rollout consistency (LRC) as a metric to evaluate action-conditioned latent prediction. Strikingly, we find that across the studied state of the art latent world models, none solves the task by actually faithfully modeling the dynamics of the environment.

---


### 250. [TANDEM: Balancing Centralized and Decentralized Critics to Address the Information Gap in Complex Multi-Agent Environments](https://arxiv.org/abs/2610.37592)

**<font color=#1a73e8>作者：</font>** Alireza Saleh Abadi, Leen-Kiat Soh, Adam Eck 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Cooperative multi-agent reinforcement learning under centralized training with decentralized execution (CTDE) shapes decentralized policies with a centralized critic that observes the global state, then removes the critic at execution. The policies are optimized to rely on information they will not have when they act, an information gap between training and execution. It widens under partial observability, observation noise, and openness, where the set of agents and tasks present changes during an episode. Existing methods transfer centralized guidance in one direction only, removing or distilling the critic once, so the policies never rehearse acting without the critic while they can still be corrected. We propose TANDEM, which keeps one centralized critic and reads it two ways at each training step: a centralized read from the global state, and a decentralized read restricted to the information each agent will have at execution. A parameter-free gate compares the two reads for each agent and trains the policy on the decentralized read where they agree, reinstating the centralized read only where the local view is misleading. A shared target pulls the decentralized read toward the centralized one. We formalize the setting as a task- and agent-open decentralized partially observable Markov decision process (TAO-Dec-POMDP) and evaluate TANDEM on three cooperative domains, each isolating one form of the information gap: discovery for partial observability, sampling for observation noise, and openness in wildfire suppression. We compare against six CTDE baselines and ablate the gate and the shared target; the supplementary material holds the full variant sweep, diagnostics, and learning curves. We measure return at execution, once the centralized critic is removed. TANDEM is the best method on eight of the nine setups and never significantly worse than any baseline.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-257](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
