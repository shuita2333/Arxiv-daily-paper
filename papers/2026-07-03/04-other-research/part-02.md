# 📦 其他研究 | 2026年07月03日

> 本类共 **236** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-236](./part-05.md)

---

### 51. [MVDGC: Joint 3D and 2D Multi-view Pedestrian Detection via Dual Geometric Constraints](https://arxiv.org/abs/2607.00273)

**<font color=#1a73e8>作者：</font>** Thinh Phan, Hao Vo, Khoa Vo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The core challenge in multi-view pedestrian detection (MVPD) lies in effective aggregation of visual features from different viewpoints for robust occlusion reasoning. Recent approaches have addressed this by first projecting image-view features onto a Bird's Eye View (BEV) map, where ground localization is then performed. Despite impressive performance, the perspective transformation induces severe distortion, causing spatial structure break and degrading the quality of object feature extraction. The blurred and ambiguous features hinder accurate BEV point localization, especially in densely populated regions. Moreover, the strong mutual relationship between the BEV ground point and image bounding boxes is not capitalized on. Although multi-view consistency of 2D detections can serve as a powerful constraint in BEV space, these detections are commonly treated as auxiliary signals rather than being jointly optimized with the primary this http URL this work, we propose \textbf{MVDGC}, a unified framework that \emph{jointly estimates pedestrian locations on the BEV plane and 2D bounding boxes in image views}. MVDGC employs a \emph{sparse set of 3D cylindrical queries} that embraces geometric context across both BEV and image views, enforcing dual spatial constraints for precise localization. Specifically, the geometric constraints is established by modeling each pedestrian as a vertical cylinder whose center lies on the BEV plane and whose projection casts a rectangular box in the image views. These queries function as shape anchors that directly extract 2D features from the intact image-view features using camera projection, eliminating projection-induced distortions. The 3D cylindrical query enables the unification of BEV and ImV localization into a single task: 3D cylinder position and shape refinement. Code is available at: this https URL

---


### 52. [Entropy-Regularized Probabilistic Gates for Sparse Model Discovery in Scarce-Data Federated Learning](https://arxiv.org/abs/2607.00275)

**<font color=#1a73e8>作者：</font>** Krishna Harsha Kovelakuntla Huthasana, Alireza Olama, Andreas Lundell  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) is a distributed machine learning (ML) paradigm with collaboration among multiple clients without sharing data. FL is challenging under data heterogeneity and partial client participation. Learning sparse models is useful for communication and computational efficiency in FL, but it is especially difficult in the small-sample high-dimensional regime (d >> N) where optimization can yield parameter configurations that fail to generalize to unseen test data. While magnitude-based pruning doesn't account for uncertainty exploration in the parameter space, a formulation with probabilistic gates and an L0 constraint allows sampling from competing sparse configurations during training. In this work, we study entropy regularization of gate distributions as a mechanism to maintain uncertainty in sparse federated optimization by preventing early commitment to sparse support. We examine its impact under data heterogeneity, client participation heterogeneity, and sparsity. Experiments on synthetic and real-world benchmarks show consistent improvements over federated iterative hard thresholding (Fed-IHT) and pruning after dense federated averaging (FedAvg) training, both in statistical performance on test data and in sparsity recovery accuracy.

---


### 53. [AEGIS: A Multi-Task Joint-Embedding Predictive Architecture for Mammography](https://arxiv.org/abs/2607.00277)

**<font color=#1a73e8>作者：</font>** Scott Chase Waggener, Sai Karthik Navuluru, Lakshman Tamil  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Aegis, a joint-embedding predictive architecture for breast cancer detection and density assessment in mammography. We train three Vision Transformer variants (Small/Base/Large) using self-supervised joint-embedding predictive architecture (JEPA) pre-training on 71,103 studies from 14 clinical sites, followed by supervised fine-tuning with progressive resolution scaling up to 2048x1536. On a curated 785-study test set, our largest model achieves area under the receiver operating characteristic curve (AUC) 0.949 for breast cancer triage with 93% sensitivity and 75% specificity at the optimal operating point. An ensemble combining our model with a U.S. Food and Drug Administration-cleared baseline further improves discrimination to 0.952 AUC. For breast density classification, the model achieves 0.953 AUC for binary (dense vs. non-dense) classification and 62.6% exact accuracy across four Breast Imaging Reporting and Data System (BI-RADS) categories, with 98.8% adjacent accuracy comparable to reported human inter-reader agreement. External validation on the public VinDr-Mammo dataset provides evidence of cross-population transfer under a different reference standard, with the largest model achieving 0.871 AUC for triage in a zero-shot setting.

---


### 54. [Understanding Guest Preferences and Optimizing Two-sided Marketplaces: Airbnb as an Example](https://arxiv.org/abs/2607.00280)

**<font color=#1a73e8>作者：</font>** Yufei Wu, Daniel Schmierer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Airbnb is a community based on connection and belonging -- many hosts on Airbnb are everyday people who share their worlds to provide guests with the feeling of connection and being at home; Airbnb strives to connect people and places. Among our efforts to connect guests and hosts, we provide tools to enable hosts to set competitive prices, which helps improve affordability for guests while helping hosts get more bookings. We also personalize the guest experience to show them the listings that match their needs.
To help inform these efforts, we combine economic modeling and causal inference techniques to understand how guests book stays based on the prices hosts set, among other factors, and how that preference varies across different guests and listings. Such understanding helps us identify opportunities for Airbnb to support the marketplace and better connect guests and hosts. For example, understanding how much guests respond to different prices helps optimize the tools that we provide to hosts, in order to enable hosts to choose and set competitive prices that further balance demand and supply. As another example, understanding heterogeneity in guest preferences helps us personalize the guest experience and better match them with the listings that meet their needs, based on how much they respond to different prices and other factors.

---


### 55. [OnPoint: Offline-to-Online Multi-Level Distillation for Point-Supervised Online Temporal Action Localization](https://arxiv.org/abs/2607.00289)

**<font color=#1a73e8>作者：</font>** Sakib Reza, Gauri Jagatap, Mohsen Moghaddam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporal Action Localization (TAL) typically relies on segment annotations or offline access to full videos, limiting scalability and online use. We introduce Point-Supervised Online TAL (POTAL), which localizes actions in streaming videos using only one temporal point per instance. To solve POTAL, we propose OnPoint, an offline-to-online multi-level distillation framework that transfers knowledge from a point-supervised offline teacher to an online student via (i) pseudo-segment instance distillation, (ii) class-activation sequence distillation, and (iii) anticipatory window-level distillation. We further improve robustness by incorporating the original point labels into student training and by refining anchor decoding with actionness-guided attention calibration. Experiments on five datasets show OnPoint consistently outperforms strong baselines, establishing a solid foundation for POTAL.

---


### 56. [Learning When to Listen: Gated Affect Fusion for Human Motion Prediction](https://arxiv.org/abs/2607.00296)

**<font color=#1a73e8>作者：</font>** Jingni Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human motion forecasting in unconstrained real-world videos remains challenging due to the ambiguity of future behaviors and the presence of noisy multimodal observations. While facial affect potentially provides complementary behavioral cues, its practical utility and mechanistic boundaries within motion forecasting frameworks remain poorly understood. In this work, we present a systematic study investigating the utility and temporal limitations of affect-conditioned forecasting in-the-wild. We establish a rigorous multimodal pipeline combining MediaPipe body pose trajectories with HSEmotion facial affect representations, and introduce the Gated Affect Transformer (GAT) to dynamically regulate cross-modal information flow. Through extensive multi-horizon evaluations under a strict subject-wise protocol, we demonstrate that naive early cross-modal concatenation consistently degrades forecasting accuracy relative to pose-only baselines. Conversely, our proposed gating mechanism stabilizes cross-modal integration by adaptively controlling the affective stream. Crucially, controlled counterfactual experiments using shuffled and randomized affect inputs reveal that the learned gate successfully suppresses unstructured cross-modal noise while remaining responsive to plausible affective signals. Furthermore, our empirical results indicate that facial affect features provide bounded, horizon-dependent predictive cues strictly within short-to-medium windows (e.g., 30 frames), whereas long-term trajectories remain predominantly governed by intrinsic kinematic continuity. Our findings provide empirical evidence that facial affect should be regarded as a complementary behavioral cue rather than a dominant driver of future motion, offering practical guidance for selective multimodal fusion in unconstrained human motion forecasting.

---


### 57. [Generative Modeling of Quantum Distribution with Functional Flow Matching](https://arxiv.org/abs/2607.00301)

**<font color=#1a73e8>作者：</font>** Jaehoon Hahm, Tak Hur, Joonseok Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The emergence of powerful deep generative models based on diffusion and flow matching has enabled the learning and modeling of complex distributions. Learning quantum distributions, however, remains challenging due to the inherent difficulty of accurately modeling the meaningful physical properties of quantum states. We propose Quantum Flow Matching (QFM), a novel generative model designed to learn quantum distribution by utilizing spin Wigner function and flow matching. By converting density matrix into the spin Wigner function and leveraging functional flow matching to learn distributions in function space, QFM enables accurate and effective learning of multi-qubit quantum distributions. We demonstrate the effectiveness of our method by evaluating physical quantities such as trace, purity, and entanglement entropy of the generated quantum states, accurately capturing the underlying physics of the given quantum distributions.

---


### 58. [Mapping the Evaluation Frontier: An Empirical Survey of the Bias-Reliability Tradeoff Across Eleven Evaluator-Agent Conditions](https://arxiv.org/abs/2607.00304)

**<font color=#1a73e8>作者：</font>** Zewen Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The bias-reliability tradeoff conjectures that LLM evaluation systems are constrained in (gamma, H, CV) space, where evaluator coupling (gamma), strategy diversity (H), and small-sample measurement reliability (CV(N)) cannot be simultaneously optimized at fixed sample size N. Prior evidence rests on n=5 conditions with complete metrics from a single study. We expand the empirical base to 11 conditions, measuring gamma and H for all 11 (nine with valid weight vectors) and CV(N=5) for seven with sufficient seeds (N >= 5). Five conditions provide the complete (gamma, H, CV) triple. The data confirm the trade-off: conditions with low evaluator coupling (gamma < 0.2) exhibit high measurement noise (CV(N=5) > 1.0), while conditions with strong coupling (gamma > 0.9) achieve low noise (CV(N=5) < 0.16). The correlation r(H, gamma) = -0.989 (n=5, excluding GPT-4o conditions) confirms that evaluator coupling suppresses strategy diversity. Four GPT-4o conditions show gamma=0.000 and H=1.000 across all seeds -- a pattern we attribute to version drift in the June 2026 GPT-4o API. No condition occupies the region {gamma < 0.2, CV(N=5) < 0.3}. We release all per-condition metrics as a standardized benchmark dataset for evaluator comparison.

---


### 59. [Typography-Based Monocular Distance Estimation for Advanced Driver-Assistance Systems](https://arxiv.org/abs/2607.00319)

**<font color=#1a73e8>作者：</font>** Manognya Lokesh Reddy, Zheng Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating the distance to a leading vehicle is a basic input to forward collision warning, adaptive cruise control, and automated emergency braking. Production systems obtain this distance from radar, laser scanners, or stereo camera pairs, which add cost, power draw, and packaging constraints. This paper asks whether a single ordinary camera can recover the same distance by using a target that is standardized in size and present on every road vehicle: the rear license plate. U.S. plates share a fixed outer size and a character height that is set by regulation and varies only narrowly between states, so the height of a plate character in the image is a direct measure of distance once the camera geometry is known. The proposed method (Typography-Based Monocular Distance Estimation) detects the plate, measures the height of its printed characters, identifies the issuing state to select the correct physical character height, and recovers distance from the camera projection. Three measurements taken from the same plate: the character height, the stroke width, and the character spacing. Together with the spacing of the two mounting holes and a single-image depth network, are combined so that a weak or corrupted measurement is given less weight automatically. The distance, its rate of change, and a time-to-collision estimate are smoothed across frames and used to raise a warning with the timing used by U.S. collision-warning regulations. The same plate that anchors the scale also identifies the vehicle, so the method returns a distance, a bearing, and an identity from one passive sensor. It reads scale from a printed standard instead of from time of flight or parallax, making it a cheap, low-maintenance complement to those sensors in a fault-tolerant perception stack, achieving the cost-effective distance estimation with error less than 0.13 m.

---


### 60. [CORGI: Consistency-Aware 3D Dog Reconstruction from a Single Image in the Wild](https://arxiv.org/abs/2607.00321)

**<font color=#1a73e8>作者：</font>** Yuxiao Wu, Weile Li, Boyi Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing high-fidelity 3D models of highly articulated animals, such as dogs, from a single in-the-wild image remains a formidable challenge. In this paper, we introduce CORGI, a novel framework for consistency-aware 3D dog reconstruction from a single unconstrained image that completely eliminates the need for 3D supervision. To overcome generative inconsistencies and the lack of multi-view capture, our pipeline introduces three core components. First, we propose a Canonical-Driven Orbital Generation (CDOG) strategy, utilizing specialized Canonical and Orbit LoRAs to normalize arbitrary input poses and synthesize reliable 360-degree video observations. Second, we design a Consistency-aware Deformable 3DGS (CA-3DGS) module that anchors on a D-SMAL prior, explicitly modeling per-view generative errors through dedicated neural deformation fields to learn accurate vertex-level displacements. Finally, to eliminate structural distortions and recover high-frequency details, we introduce a self-supervised Deformation-Conditioned Generative Repair (DCGR) module. Extensive experiments demonstrate that CORGI achieves state-of-the-art performance, generalizing seamlessly across diverse dog breeds to produce geometrically accurate, visually coherent, and fully animatable 3D assets ready for downstream applications.

---


### 61. [Watermarking for Proprietary Dataset Protection](https://arxiv.org/abs/2607.00325)

**<font color=#1a73e8>作者：</font>** John Kirchenbauer, Brian R. Bartoldson, Bhavya Kailkhura 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A growing body of literature suggests that training data membership inference problems are fundamentally hard tasks in modern language modeling settings. We argue that output watermarking techniques are the right gadget to make training membership tests for generative models more tractable, based on prior results showing that language models exhibit residual watermark "radioactivity" under partially watermarked training datasets. We pit a watermark-based dataset inference approach head-to-head against traditional loss-based membership inference methods and show that watermarking can achieve comparable membership detection performance when subset exposure is high enough, under an alternate set of assumptions.

---


### 62. [K-Inverse-RFM: A Modified RFM that Bridges the Gap to Neural Networks for Data-Corrupted Mathematical Tasks](https://arxiv.org/abs/2607.00329)

**<font color=#1a73e8>作者：</font>** Gil Pasternak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive Feature Machines (RFMs) are a class of kernel machines that utilize the Average Gradient Outer Product (AGOP) as a mechanism for feature learning. They have been shown to effectively replicate the learning dynamics and feature representations of Feedforward Neural Networks (FNNs) across various settings. However, despite comparable capacity for feature learning and the similarities in the features they acquire, RFMs exhibit significantly lower performance than neural networks in certain data-corrupted scenarios. In this work, we investigate these limitations in mathematical problems. As a solution, we introduce a remarkably effective transformation applied to the training labels which promotes learning in noisy, complexly represented, and class-imbalanced data. This simple yet powerful adjustment enables RFMs to close the performance gap with FNNs and, in some cases, even surpass them.

---


### 63. [(A)I Sees What You Don't: Exploiting New Attack Surfaces in Third-Party Mobile Agents](https://arxiv.org/abs/2607.00333)

**<font color=#1a73e8>作者：</font>** Zidong Zhang, Zhentao Xie, Wenrui Diao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Third-party mobile agents powered by Vision-Language Models (VLMs) have emerged as a promising paradigm for automating smartphone interactions. These agents act as high-privilege decision-makers, perceiving device states through screenshots and executing actions via VLM reasoning, transforming how an agent app interacts with the environment (i.e., other apps or the OS). Correspondingly, this transformation introduces new attack surfaces or transforms benign/harmless interfaces into exploitable ones for mobile devices. In this paper, we summarize key differences between third-party mobile agent apps and general apps when interacting with the environment, analyze the security posture of agents, and identify two unique attack surfaces compared to general mobile apps: the Screen Perception Attack Surface, which exploits the gap between human and machine vision, and the Misused Channel Attack Surface, which intercepts or manipulates the agent's execution pipeline. We design and implement seven concrete attacks, from subliminal text injection and invisible pixel zone exploitation to screenshot tampering and host PC command injection. Our evaluation of five popular mobile agent frameworks demonstrates that a malicious app can hijack agent actions and achieve arbitrary command execution even without any privilege permissions, while remaining visually indistinguishable to users. These findings reveal a fundamental trust mismatch in autonomous agent design and highlight the urgent need for perception-aware security models on multi-tenant platforms.

---


### 64. [Managed Autonomy at Runtime: Gear-Based Safety and Governance for Single- and Multi-Agent Cyber-Physical Systems](https://arxiv.org/abs/2607.00334)

**<font color=#1a73e8>作者：</font>** Srini Ramaswamy, Wang Miaosheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agents, whether LLM-driven software agents or robotic physical agents, face a common class of failure modes when operating without continuous human oversight: safety violations from unverified actions, behavioral instability from unconstrained loops, and continuity loss from unhandled error states. We develop \system{}, a discrete-time control system that combines five execution gears (\Gobs{}, \Gsug{}, \Gplan{}, \Gexec{}, \Gint{}) with utility-gated dispatch and event-driven fallback. For the single-agent case, we prove monotonic stability, execution safety, eventual stabilization, fallback completeness, and equivalence to a gear-constrained Markov decision process. For multi-agent cyber-physical systems (CPS), we apply the established \smart{} managed-autonomy lifecycle and map runtime evidence into its four governance states (\Stable{}/\Meta{}/\Assisted{}/\Regulated{}). Consensus gating, swarm-level Lyapunov analysis, per-agent gear authority, and rendezvous control provide distributed safety and stability guarantees, including zero collision under the stated assumptions. We evaluate the resulting runtime on a three-agent UR5 robotic assembly cell using fault magnitudes calibrated from the NIST \emph{Degradation Measurement of Robot Arm Position Accuracy} dataset across 10,000 Monte Carlo episodes. It achieves a 99.6\% anomaly detection rate versus 2.1\% for the single-agent baseline, reduces detection latency by $3.5\times$, and supplies a formal physical-workspace safety certificate. The execution gears act as micro-level permissions beneath the \smart{} runtime governance states, separating action control from autonomy governance.

---


### 65. [TRACE: State-Aware Query Processing over Temporal Evidence Graphs for Conversational Data](https://arxiv.org/abs/2607.00339)

**<font color=#1a73e8>作者：</font>** Maolin Wang, Yu Wang, Zichun Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational data is increasingly used as a persistent source of user state for long-running assistants and AI agents. However, querying this data remains challenging because conversations naturally evolve: plans are revised, preferences change, and later messages frequently supersede or contradict earlier information. Existing long-memory pipelines largely treat memories as independent text or vector objects. This approach often retrieves semantically similar but stale evidence, offering limited support for state-aware reasoning. To address this problem, we present TRACE, a query processing framework over temporal evidence graphs for evolving conversational data. TRACE models conversations as a hierarchical graph spanning events, sessions, and topics, enriched with typed temporal, causal, update, and contradiction relations. Crucially, the framework maintains validity annotations so obsolete facts remain accessible for historical queries but are discounted for current-state answers. At query time, TRACE combines vector-based note retrieval with graph-guided evidence search, generating validity-aware support paths and a hybrid context for answer generation. This design separates lexical recall from evidence reconstruction, enabling bounded query-time reasoning over long conversational histories. Experiments on long-conversation query-answering (QA) benchmarks show that TRACE improves temporal and multi-hop reasoning, with ablations highlighting the importance of hierarchy, update-aware seeding, and path-grounded evidence.

---


### 66. [PRISM: Prioritized Channel Importance with Semi-supervised Domain Adaptation for Cross-Subject EEG Emotion Recognition](https://arxiv.org/abs/2607.00358)

**<font color=#1a73e8>作者：</font>** Xin Zhou, Xiang Zhang, Hao Deng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalogram (EEG) captures endogenous brain activity with high temporal fidelity and holds substantial promise for precise emotion decoding. However, channel redundancy and pronounced inter-subject variability remain key obstacles to scalable generalization. To address these limitations, we propose a novel framework termed PRioritized channel Importance with Semi-supervised doMain adaptation (PRISM), enabling label-efficient cross-subject emotion decoding. On the channel side, PRISM assigns differentiable, data-dependent channel weights via a lightweight expert ensemble, amplifying reliable electrodes while suppressing distractors. On the domain side, PRISM leverages unlabeled data through confidence-filtered pseudo-labels to drive consistency regularization and domain alignment, mitigating subject-specific heterogeneity. Extensive experiments show that PRISM surpasses state-of-the-art methods on DEAP, DREAMER, and SEED datasets, achieving robust cross-subject generalization given limited annotations.

---


### 67. [SoK: Attack and Defense Landscape of Mobile On-device AI Systems](https://arxiv.org/abs/2607.00362)

**<font color=#1a73e8>作者：</font>** Yujin Huang, Xin Zheng, Xingliang Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mobile on-device AI (MoAI) systems that integrate locally deployed AI models with conventional mobile software components are emerging as a key paradigm for delivering intelligent functionality directly on end-user devices. By moving inference from remote cloud services to the local mobile environment, such systems enable privacy-preserving, low-latency, and offline-capable AI functionality, yet introduce new security risks arising from the local storage of AI models. This paper presents the first comprehensive systematization of knowledge on MoAI security, covering security pillars, attack landscape, and defense landscape of MoAI systems. We further identify unresolved gaps in current attack and defense research and point to promising directions for future research in this emerging area. Our work establishes the first systematic framework for understanding the attack and defense landscapes of MoAI systems, serving as a foundation for building secure MoAI systems and advancing research in this critical domain. Companion resources are available at this https URL.

---


### 68. [SFDATrack: Generalized Source-Free Domain Adaptive Tracking Under Adverse Weather Conditions](https://arxiv.org/abs/2607.00369)

**<font color=#1a73e8>作者：</font>** Siyuan Yao, Ziqi Wang, Ruiqi Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain adaptive visual object tracking under adverse weather conditions has garnered significant attention in recent years. Despite the impressive performance, existing methods heavily rely on the large-scale video frames from both source and target domains, which is impractical under rigid resource constraints where source data is unavailable. To overcome this limitation, we propose SFDATrack, a generalized source-free domain adaptive tracker that merely leverages adverse weather samples from the target domain for robust state estimation. Specifically, SFDATrack first employs a mean-teacher backbone with Dual Interactive Mamba (DIM) blocks to distill the candidate target tokens that are resilient to weather variations from classified, augmented samples. Afterwards, we introduce a hyperspherical prototype projection (HPP) module to project these tokens onto multi-domain prototypes within a latent hyperspherical space. By enforcing both domain-specific and domain-invariant properties of the multi-domain prototypes, SFDATrack can be seamlessly adapted to diverse weather conditions with powerful generalizability. Extensive experiments evaluated on various benchmarks demonstrate that SFDATrack achieves superior performance compared to state-of-the-art approaches. The code is available at this https URL.

---


### 69. [Learning to Compose: Revisiting Proxy Task Design for Zero-Shot Composed Image Retrieval](https://arxiv.org/abs/2607.00374)

**<font color=#1a73e8>作者：</font>** Jingjing Zhang, Lei Zhang, Zheren Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composed Image Retrieval (CIR) retrieves a target image from a reference image and a textual modification. While supervised CIR relies on costly triplets, Zero-Shot CIR (ZS-CIR) alleviates this reliance through proxy tasks trained on image-text pairs. However, existing proxy tasks primarily enhance visual and textual representations to accommodate a predefined composition mechanism such as pseudo-word injection into a frozen text encoder or linear feature arithmetic. As a result, the composition function itself remains unlearned, limiting the model's ability to express diverse and fine-grained semantic modifications. To address this, we propose FoCo, which models composition as two coordinated stages: focusing on modification-relevant visual content, and then completing the target semantics. We realize these through two proxy tasks: text-anchored visual aggregation to selectively gather visual content guided by localized textual semantics, and context-conditioned semantic completion to transform these aggregated visuals with the remaining scene context into a coherent composed representation. The tasks are trained jointly with a cross-instance contrastive objective, encouraging semantic diversity and discouraging shortcut composition strategies. Extensive experiments on four ZS-CIR benchmarks show FoCo's state-of-the-art performance and improved generalization.

---


### 70. [LIST3R: Long-sequence Instance-aware 3D Reconstruction](https://arxiv.org/abs/2607.00375)

**<font color=#1a73e8>作者：</font>** Jing Gao, Wei Wang, Feiran Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present LIST3R, an instance-aware framework for long-sequence 3D reconstruction inspired by the way humans organize spatial memory around stable and recognizable objects. LIST3R organizes long-sequence reconstruction around instance anchors, using them to reconnect fragmented subsequences and consolidate local observations into a coherent global 3D scene. Given a long video, our approach partitions it into overlapping subsequences and builds a structured local instance library for each partial reconstruction, maintaining persistent trackable anchors with semantic and geometric evidence. These anchors are matched across subsequences to recover revisited regions and provide object-aware constraints for fragment alignment, producing a consistent global reconstruction. During this process, the evolving geometric evidence updates the local instance libraries and progressively organizes them into a unified global 3D instance library. Experiments on long-sequence benchmarks show that our method produces more accurate trajectories and higher-quality 3D reconstructions, highlighting the effectiveness of persistent instance anchors for organizing long-horizon 3D reconstruction. Our code is available on the project page: this https URL.

---


### 71. [SAOT: Self-Supervised Continual Graph Learning with Structure-Aware Optimal Transport](https://arxiv.org/abs/2607.00377)

**<font color=#1a73e8>作者：</font>** Yuting Zhang, Yanbei Liu, Zhitao Xiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised Continual Graph Learning (CGL) aims to successively learn from a graph sequence with different tasks without label supervision - a paradigm that has attracted widespread attention. Most existing self-supervised CGL methods rely on instance-level consistency objectives that enforce stability of individual node (or node-pair) embeddings. Due to optimizing nodes in isolation, these methods fail to maintain global relational structure, causing inter-node correspondences to progressively distort under continual learning. To this end, we propose a novel Structure-Aware Optimal Transport (SAOT) framework that explicitly captures and preserves relational structure within graph representations across sequential tasks. Specifically, SAOT leverages optimal transport theory to capture global inter-node correspondences, thereby facilitating and enhancing graph representation learning. Simultaneously, SAOT incorporates a cross-task knowledge distillation mechanism to preserve the previous structural knowledge. Extensive experiments on four CGL benchmark datasets demonstrate that SAOT outperforms existing self-supervised baselines. In particular, SAOT achieves significant performance gains, improving average accuracy by up to 5% on CoraFull-CL and over 15% on Products-CL compared with state-of-the-art methods in the Class-IL setting.

---


### 72. [Radial Interaction Tomography: Recognizing Non-Transitive Evolutionary Games from One Range-Expansion Image](https://arxiv.org/abs/2607.00378)

**<font color=#1a73e8>作者：</font>** Faruk Alpay, Baris Basaran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Colored sectors in a microbial range expansion encode more than lineage survival counts. We formulate a computer-vision inverse problem: from one endpoint image of an accretive multi-type expansion, recover the radius-indexed pairwise boundary-flow field and test whether the visual pattern is compatible with a transitive scalar fitness hierarchy. The observable is a geometric signal extracted from sector-boundary curves in log-polar coordinates. We prove endpoint observability and stability for frozen fronts, weighted transitive/cyclic decomposition, contact-complete circular design, physical-clock and mechanism non-identifiability, exact Gaussian cyclicity testing, and Bonferroni-valid interval scanning. The benchmark is deterministic: analytic endpoint images, blurred/noisy pixel round trips, scalar-null stress tests, public-image tracing, multi-resolution mechanistic endpoints, and a non-learning frozen-front simulator. The implementation recovers pairwise edge-flow histories from endpoint images, detects cyclic residuals in a mechanistic four-type expansion, and uses those residuals as forcing signals for a dimensionless active design-control layer covering reaction-diffusion control, phenotype-frontier optimization, protocol synthesis, Monte Carlo robustness, and a downstream population-state bridge.

---


### 73. [Vitality-Aware Compression for Efficient Image-to-Shape Diffusion Transformers](https://arxiv.org/abs/2607.00382)

**<font color=#1a73e8>作者：</font>** Jaeah Lee, Hyunjin Kim, Jaewoong Cho 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose the first compression approach for image-to-shape Diffusion Transformers (DiTs) that substantially reduces model size while preserving geometric fidelity. Despite remarkable progress in 3D shape generation, large DiT-based models remain computationally prohibitive in resource-constrained settings. Furthermore, it is difficult to directly transfer existing diffusion model compression strategies developed for different domains to 3D generation, and prior 3D efficiency approaches focus primarily on inference speed rather than backbone compression. To address this limitation, we build a geometry-aware compression framework tailored to image-to-shape DiTs. Guided by the observation that 3D DiT layers exhibit non-uniform importance for geometry synthesis, we introduce a vitality-guided framework integrating structured pruning, adaptive quantization, and targeted fine-tuning. Our method achieves up to 66% model-size reduction across state-of-the-art image-to-3D models while maintaining synthesis fidelity comparable to full-sized counterparts. This highlights the potential of our framework as a plug-and-play solution for efficient 3D shape generation across diverse models.

---


### 74. [Learning Generalizable Skill Policy with Data-Efficient Unsupervised RL](https://arxiv.org/abs/2607.00392)

**<font color=#1a73e8>作者：</font>** Jongchan Park, Seungjun Oh, Seungho Baek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised Reinforcement Learning (URL) aims to pre-train scalable, skill-conditioned policies without extrinsic rewards, serving as a foundation for downstream control tasks. Despite recent progress, we argue that current off-policy URL methods are limited by two critical, overlooked bottlenecks: (1) non-stationary skill semantics and (2) brittle generalization. To address these challenges, we propose GenDa (Generalizable Data-efficient Agent), a unified framework for robust unsupervised reinforcement learning. First, we introduce a skill relabeling mechanism to mitigate non-stationarity and significantly improve data efficiency for pre-training. Second, we propose a Complementary Information Bottleneck (CIB), encouraging the learned skill policy to focus on ego-centric features and become robust to distribution shifts for downstream tasks. Through various experiments, we demonstrate that GenDa significantly enhances the scalability of URL with superior generalizability and data efficiency. Our code and videos are available at this https URL.

---


### 75. [Child Safety in Generative AI: An Expert-Guided and Incident-Grounded Evaluation Framework](https://arxiv.org/abs/2607.00395)

**<font color=#1a73e8>作者：</font>** Haein Kong  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As generative AI is increasingly used by children and adolescents, there is a growing need for risk evaluation frameworks that account for child-specific harms. However, most existing safety evaluation frameworks focus on general user populations, often overlooking risks unique to younger users. To address this gap, we propose an evaluation framework that integrates expert-guided risk factors with real-world AI incident data for child safety. The framework identifies hazard categories from expert guidelines and AI incident databases and uses this information to construct a synthetic test set for model evaluation. Particularly, we apply the framework to the education domain and evaluate three Llama Guard models on their ability to detect unsafe user prompts. Our results show that current Llama Guard models struggle to identify education-related unsafe user prompts. We conclude by discussing how future work can extend the evaluation to additional risk categories and incorporate domain experts throughout the evaluation pipeline.

---


### 76. [DriveVer: Lightweight Trajectory Evaluator as Test-Time Verifier for Autonomous Driving](https://arxiv.org/abs/2607.00399)

**<font color=#1a73e8>作者：</font>** Chong He, Yuechen Luo, Fang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end autonomous driving models often encounter performance bottlenecks, as training-time scaling leads to high computational costs and diminishing marginal returns. Existing planners typically adopt a one-shot generation paradigm, lacking secondary validation and active correction mechanisms to detect and revise suboptimal or unsafe trajectories during inference. To address this issue, we propose DriveVer, a lightweight, plug-and-play Test-Time Verifier that leverages the test-time scaling paradigm to enable autonomous driving systems to validate and refine trajectories without costly and heavy training. We construct a dedicated trajectory dataset based on the NAVSIM benchmark through condition-driven clustering and balanced sampling according to ego-vehicle states and navigation commands. Employing a dual-head architecture, DriveVer efficiently fuses candidate trajectories with multi-view visual representations and ego-vehicle kinematic features to simultaneously predict a safety confidence score and an absolute geometric refinement vector. Extensive experiments on the NAVSIM benchmark show that DriveVer significantly improves the performance of base planning models. Notably, as an extremely compact model with only 34M parameters, DriveVer introduces minimal computational overhead, achieving competitive results while maintaining real-time inference efficiency.

---


### 77. [MedCAGD: Context-Aware Gated Decoder for Efficient Medical Image Segmentation](https://arxiv.org/abs/2607.00409)

**<font color=#1a73e8>作者：</font>** Saad Wazir, Patrick Dominique Vibild, Dinh Phu Tran 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation relies on the ability of encoder-decoder architectures to translate rich feature representations into accurate pixel-level predictions under challenging conditions such as low contrast, structural ambiguity, and scale variability. While recent advances in large-scale pretraining and transformer-based encoders have substantially improved feature extraction, segmentation accuracy remains constrained by decoder design, particularly in terms of cross-scale alignment, contextual integration, and boundary preservation. In this work, we revisit medical image segmentation from a decoder-centric perspective and propose a context-aware gated decoder that systematically regulates feature fusion and contextual aggregation throughout the decoding process. The proposed decoder integrates lightweight multi-scale channel recalibration, gated skip fusion with spatial competition and a global context aggregation mechanism that injects encoder-wide information into intermediate decoding stages. This design enables effective translation of strong pretrained encoder representations into spatially consistent predictions. Extensive experiments across 11 medical image segmentation benchmarks validate the effectiveness and demonstrate that the proposed approach consistently outperforms strong baselines while remaining computationally practical. Code: this https URL

---


### 78. [Speech Playground: An Interactive Tool for Speech Analysis and Comparison](https://arxiv.org/abs/2607.00418)

**<font color=#1a73e8>作者：</font>** Stephen McIntosh, Daisuke Saito, Nobuaki Minematsu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents Speech Playground, an interactive speech visualization and comparison tool. While existing tools such as Praat are excellent, it can be cumbersome to integrate them with modern deep learning representations and use them for comparison. Speech Playground addresses this by combining a Python backend with a web-based frontend for interactive exploration of multiple feature types, including continuous, discrete, and variable-length representations. It includes TextGrid and forced alignment support together with configurable distance and alignment settings for visual and auditory comparison. Speech Playground is intended for use in speech research, representation validation, and computer-aided pronunciation training (CAPT)-oriented experimentation.

---


### 79. [A Simple Solution to Improving Human Supervision of Algorithms: Evidence from Smart Vending](https://arxiv.org/abs/2607.00420)

**<font color=#1a73e8>作者：</font>** Minda Zhao, Brian Rongqing Han, Xin Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Organizations increasingly deploy autonomous artificial intelligence (AI) systems for operational decisions, such as inventory replenishment. Yet fully granting override rights can degrade performance due to human bias and noise, while prohibiting them may overlook valuable private information. This raises a key question: How should override rights be structured to improve human supervision of autonomous AI? Methodology/results: We propose a constrained override policy that limits overrides per decision episode to enable selective filtering that prioritizes high-value overrides. We tested it through a randomized field experiment with 553 workers at a major Chinese smart vending machine retailer that manages more than 59,000 machines and 4,000 SKUs. Workers were assigned to no overrides, free overrides, or a two-per-machine limit on downward overrides. Free overrides reduce inventory by 1.95% but also cut sales by 1.19%. Constrained overrides reduce inventory by 1.28% without harming sales, as workers select better SKUs to override, confirmed via local average treatment effects. Gains are largest for experienced workers, high-incentive SKUs, and growth-stage SKUs. A simulated personalized policy further increases sales probability by 9.1%. Managerial implications: Academics gain novel insights from the causal effects of discretion design in human-supervised AI, emphasizing selective filtering to enhance decision quality. Managers can benefit from a scalable, low-cost policy for operations such as retail, logistics, and resource planning, reducing excess inventory without sales loss while harnessing private human information, with no need for algorithmic redesign, information customization, or additional training.

---


### 80. [Selective Test-Time Debiasing for CLIP via Reward Gating](https://arxiv.org/abs/2607.00423)

**<font color=#1a73e8>作者：</font>** Jaeho Han, Jisoo Yang, Hyeondong Woo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision language models (VLMs) demonstrate strong zero-shot performance, but often perpetuate social stereotypes in person-centric queries, yielding skewed demographic distributions. Current debiasing methods apply uniform bias corrections across all input queries regardless of their bias sensitivity, creating a fundamental fairness--utility trade-off. Strong debiasing distorts semantically meaningful information in bias-insensitive queries, while weak debiasing fails to mitigate stereotypes in bias-sensitive ones. This one-size-fits-all approach hampers simultaneously achieving high utility on bias-insensitive queries and fairness on bias-sensitive queries. We introduce Reward-Gated Test-Time Adaptation (RG-TTA), a reinforcement learning-based test-time adaptation framework that selectively applies debiasing based on input sensitivity. RG-TTA adaptively triggers fairness regularization based on the bias sensitivity of each input during test-time policy adaptation, while focusing exclusively on optimizing cross-modal alignment for bias-insensitive inputs. Experiments on fairness benchmarks (e.g., FairFace, UTKFace) demonstrate substantial bias reduction while simultaneously improving zero-shot utility, resolving the trade-off of uniform debiasing.

---


### 81. [Timesynth: A Temporal Fidelity Framework for Health Signal Digital Twins](https://arxiv.org/abs/2607.00431)

**<font color=#1a73e8>作者：</font>** Md Rakibul Haque, Shireen Elhabian, Warren Woodrich Pettine  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting models for health-signal digital twins must preserve the oscillatory, frequency, phase, and state-transition dynamics of physiological signals, yet the pointwise metrics used to benchmark them cannot detect when these fundamental properties are lost. We show that this blind spot misranks models: across 11 architectures, models with comparable pointwise error diverge by up to 53° in phase accuracy, equivalent to roughly 123 ms for a 1.2 Hz cardiac rhythm and invisible to standard metrics. To enable development of models that escape such failures, we introduce TimeSynth, a controlled benchmarking framework with two reusable components: a physiologically grounded generator producing signals with analytically known ground-truth dynamics from parametric models fitted to real electroencephalography, electrocardiography and photoplethysmogram signals, along with diagnostics quantifying amplitude, frequency, phase, and state-transition fidelity. Linear and full-sequence attention models systematically lose frequency and phase information despite acceptable amplitude error, whereas architectures with localized temporal structure better preserve dynamical fidelity and adapt to observable state transitions; none, however, reliably preserves stochastic switching. Because the dominant determinant of fidelity is architectural, model choice becomes a principled, use-case-driven decision rather than a search for a single winner. TimeSynth thus supplies the controlled preclinical stress test missing before models are coupled to patient data, with a reusable generator and diagnostics for fidelity-aware development.

---


### 82. [Minos: A Multi-Agent Collaborative Framework for Provenance-Based Backward Tracking](https://arxiv.org/abs/2607.00440)

**<font color=#1a73e8>作者：</font>** Jiahui Wang, Zhenyuan Li, Zhengkai Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Sophisticated cyber attacks, particularly Advanced Persistent Threats (APTs), require effective post-intrusion forensic analysis. Provenance-based backward tracking reconstructs attack scenarios by tracing causality from security alerts, but existing methods rely on low-level statistical features and rigid traversal strategies, limiting their ability to capture high-level adversarial intent and suffering from dependency explosion. We present Minos, a multi-agent framework that formulates backward tracking as an LLM-driven reasoning process. Minos adopts a two-tiered architecture: for event-level analysis, it combines hierarchical context management, retrieval-augmented reasoning with citation verification, and adversarial deliberation to improve reasoning quality; for graph exploration, it coordinates four specialized agents under a finite state machine (FSM), replacing exhaustive traversal with hypothesis-guided reasoning and count-first query protocols to efficiently prune the search space. Experiments on 14 attack scenarios across five public datasets show that Minos achieves an average recall of 0.92 and precision of 0.64, significantly outperforming state-of-the-art baselines while producing attack subgraphs that are 49% more compact. Moreover, Minos generates interpretable reasoning throughout the tracking process, facilitating forensic auditing and system refinement. These results demonstrate the effectiveness of LLM-driven reasoning for automated provenance-based backward tracking.

---


### 83. [Gaze-Informed Proactive AI Assistance for Children's Picture Exploration](https://arxiv.org/abs/2607.00445)

**<font color=#1a73e8>作者：</font>** Zekun Wu, Man Su, Huiyong Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Proactive assistance with large language models (LLMs) has received growing attention in the human computer interaction (HCI) community. However, most past work on proactive LLMs' assistance has focused on adult users and task-oriented settings, leaving open how such systems could support children, whose interests and needs are often expressed through gaze and other nonverbal behaviors rather than explicit requests. In this study, we focus on two key challenges of proactive assistance in children's picture exploration: when to provide assistance and what assistance to provide based on children's nonverbal behaviors. To address these challenges, we introduce Ollie, a gaze-informed proactive artificial intelligence (AI) assistant that offers short narrative descriptions based on where a child is looking. Ollie uses children's gaze to estimate their attention, identify their current visual focus, and select a related picture region for the LLM to verbally describe. In a within-subject experiment, we compared gaze-informed assistance with random assistance. Results show that gaze-informed assistance kept children's attention on their current focus for a longer period of time, and guided them more effectively to related picture regions. Children, parents, and a participating kindergarten teacher viewed Ollie positively and consider that it better matched children's interests when compared with the random assistance. This work shows the feasibility of using gaze as an implicit input for proactive AI assistance for children and provides design implications for future child-centered AI systems.

---


### 84. [VideoSearch-R1: Iterative Video Retrieval and Reasoning via Soft Query Refinement](https://arxiv.org/abs/2607.00446)

**<font color=#1a73e8>作者：</font>** Seohyun Lee, Seoung Choi, Dohwan Ko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As video corpora continue to expand in both scale and task complexity, there is increasing demand for approaches that retrieve relevant videos from large-scale corpora (inter-video reasoning) and subsequently perform fine-grained, query-conditioned tasks (intra-video reasoning) within the retrieved content, such as temporal grounding. However, existing approaches typically treat retrieval as a preprocessing step, and consequently, when the initial retrieval fails, there is no mechanism to refine the search, leading to the failure of subsequent fine-grained intra-video reasoning. Moreover, while recent agentic frameworks have advanced video understanding, they typically assume that the query-relevant video is already given, focusing exclusively on intra-video reasoning tasks. To address these limitations, we propose VideoSearch-R1, an agentic framework for iterative video retrieval and reasoning through multi-turn interaction with a video search engine. Specifically, we introduce Soft Query Refinement (SQR) to refine search query tokens in a continuous latent space rather than rewriting queries in the discrete text space, enabling more efficient and fine-grained adjustments. SQR and its reasoning process are trained using Group Relative Policy Optimization (GRPO), guided by task-level reward signals derived from retrieval and downstream tasks. Building upon this, VideoSearch-R1 achieves state-of-the-art performance across three datasets on Video Corpus Moment Retrieval (VCMR), iteratively retrieving videos from large-scale corpora, refining search queries, and performing precise query-conditioned temporal grounding within the retrieved content. Our analyses show that SQR effectively refines the original query, requiring significantly fewer generated tokens than explicit text-level query refinement. Code and model checkpoints are publicly available at this http URL.

---


### 85. [Gauging, Measuring, and Controlling Critic Complexity in Actor-Critic Reinforcement Learning](https://arxiv.org/abs/2607.00452)

**<font color=#1a73e8>作者：</font>** Konstantin Garbers  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Actor-critic methods depend on learned critics, but critic quality is often evaluated only indirectly through return, temporal-difference error, or value loss. Critic complexity is introduced as an additional diagnostic and intervention dimension for actor-critic reinforcement learning. The analysis uses spectral effective-rank entropy, a rank-like summary of the singular-value distributions of critic weight matrices, to assess critic model complexity. Across TD3 and PPO experiments, critic complexity is tracked together with return and Monte Carlo value-estimation bias. The results show that critic complexity is measurable throughout training and is systematically associated with training behavior, while also making clear that the relationship is heterogeneous across algorithms, tasks, and hyperparameters. A direct complexity-control intervention is then evaluated by adding a spectral-entropy penalty to the critic loss. This intervention reliably changes the targeted spectral quantity, demonstrating that critic complexity can be controlled rather than only observed. Return effects are treated as task-dependent evidence rather than as a general performance claim, because overall complexity-control results vary.

---


### 86. [MolSafeEval: A Benchmark for Uncovering Safety Risks in AI-Generated Molecules](https://arxiv.org/abs/2607.00464)

**<font color=#1a73e8>作者：</font>** Tong Xu, Xinzhe Cao, Zhihui Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current molecular generation benchmarks emphasize task complexity, molecule novelty, and property alignment; they largely overlook a critical concern: the potential safety risks of AI-generated molecules. In practice, many generative models may produce molecules with toxic, reactive, or otherwise hazardous characteristics - posing hidden dangers that remain insufficiently addressed. To address this gap, we introduce MolSafeEval, a benchmark dedicated to evaluating and analyzing the safety risks of molecular generation. Unlike prior approaches that rely on narrow toxicity predictors, MolSafeEval integrates heterogeneous safety knowledge - ranging from toxicological databases to hazard rules - into a structured molecular safety knowledge graph. This graph serves as a foundation for large language model-based reasoning, enabling systematic detection and explanation of unsafe features in generated compounds. We further categorize molecular generative models into four representative task types - unconditional generation, property optimization, target protein-based design, and text-based generation - and provide standardized datasets and safety evaluation protocols for each. By systematically revealing the safety vulnerabilities of current generative approaches, MolSafeEval offers a new lens for benchmarking molecular models and provides essential guidance toward safer, more trustworthy molecular design.

---


### 87. [How Early Is Early Enough? Design-Dependent Observation-Window Sufficiency in Subscription Churn Prediction](https://arxiv.org/abs/2607.00473)

**<font color=#1a73e8>作者：</font>** Xiao Han, Yao Xiao, Chenyu Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How many days of early behavior suffice for subscription churn prediction? In the public KKBox dataset, the early indicator of churn is typically an indicator of someone's contract status; however, when looking in the heavily churned manual-renewal segment, having access to early behavior creates a substantial increase in prediction for that specific segment (PR +0.10 at 120 days). A nine-window sufficiency curve shows a diminishing-returns knee in a 45-90 day band. However, stress-testing over three cohort/task designs shows that this curve is singular to the design being tested; for example, in our test with a moving target, the curve inverts and can shift depending on the feature set used. Therefore, any window-sufficiency claim should state its cohort construction, target definition, and feature families. All evidence is from one music-streaming dataset; the mechanism should generalize but the magnitudes may not.

---


### 88. [Interpretable vs Learned Encoders for High-Cardinality Fraud Detection](https://arxiv.org/abs/2607.00477)

**<font color=#1a73e8>作者：</font>** Xiao Han, Jingjing Liu, Moxuan Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A total of seven categorical encoding methods were tested on the IEEE-CIS fraud benchmark dataset (590,540 records, 3.5% positives, 8 high-cardinality columns). The encoders were evaluated using a stratified 5-fold cross-validation (CV) with three repetitions. Five of the encoders had identical frozen LightGBM learners in the downstream phase, allowing for controlled comparisons of their performance to each other. CatBoost and TabNet were included as comparisons across paradigms using different learners. The entity embeddings produced the highest AUC-ROC (0.9612), with a statistically significant tie with that of CatBoost (0.9602) and statistically superior to tier group encoding (0.9548), whereas target encoding was only 0.0023 worse than tier group encoding and the auditor-friendly tier boundaries were maintained. Off-the-shelf TabNet did not outperform tree-based pipelines and collapsed under data scarcity. On AUC-PR, CatBoost leads (0.822 vs. 0.793); no encoder dominated both metrics. Per-column analysis confirmed the embedding advantage arises from joint multi-column representation.

---


### 89. [Know When to Stop: Segment-Level Credit Assignment for Reducing Overthinking](https://arxiv.org/abs/2607.00482)

**<font color=#1a73e8>作者：</font>** Chia-Hsuan Lee, Sihui Dai, Mingyang Zhou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning language models frequently overthink: generating extended chains of behaviors such as hedging, approach abandonment, and self contradiction that consume tokens without improving answers. We show that these behaviors are not merely a consequence of length; even when controlling for response length, incorrect traces exhibit higher rates of unproductive self-reflection than correct ones. Addressing this requires identifying where self-reflection helps vs hurts, but obtaining these step-level annotations is costly. We observe that intermediate answer commitments within reasoning traces can provide a cheap proxy: by comparing each final answer candidate in the trace to the ground truth, we can determine whether subsequent reflection is productive without any additional supervision. Building on this insight, we propose DASH (Drift Aware advantage SHaping), which assigns segment-level credit based on whether each reasoning segment leads toward or away from correctness. On competition-level math benchmarks, DASH achieves the highest accuracy where overthinking is prevalent (AIME25: 50.8% vs. 45.4% GRPO) while reducing overthinking behaviors and achieving more productive self-correction than baselines.

---


### 90. [Efficient Multilingual Reasoning Transfer via Progressive Code-Switching](https://arxiv.org/abs/2607.00485)

**<font color=#1a73e8>作者：</font>** Zhijun Wang, Junxiao Liu, Hao Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) have achieved strong reasoning capabilities in English, yet their performance degrades significantly when required to reason in other languages. A natural solution is to transfer the model's English reasoning ability to target languages. However, existing transfer approaches typically rely on distilled target-language reasoning traces from stronger LRMs or online supervision from external judge models, which are costly and difficult to scale. In this paper, we propose PCS (Progressive Code-Switching), a more efficient transfer framework that requires only lightweight translation without any stronger model for distillation or judging. PCS first constructs code-switched reasoning traces by translating a subset of English reasoning steps into the target language, and uses them to initialize the model's code-switching ability via supervised fine-tuning. It then applies reinforcement learning with a step-level language consistency curriculum, progressively raising the target-language ratio until the model reasons entirely in the target language. This progressive design provides a smooth transfer path that avoids the instability and performance degradation commonly observed when directly enforcing target-language reasoning. Experiments on multiple benchmarks and five typologically diverse languages show that PCS substantially narrows the performance gap between target-language and English reasoning, yielding more language-consistent reasoning while maintaining competitive accuracy.

---


### 91. [MindEdit-Bench: Benchmarking Object-Level Counterfactual Spatial Reasoning in VLMs from In-the-Wild Photos](https://arxiv.org/abs/2607.00491)

**<font color=#1a73e8>作者：</font>** Leyuan Yu, Xiao Tang, Minghao Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Benchmarks for vision-language models (VLMs) mostly test observational spatial reasoning: models describe relations already visible in the input. Existing what-if tasks typically vary the observer while keeping the scene fixed. Can VLMs instead predict the consequences of hypothetically moving or rotating an object? We introduce MindEdit-Bench, a benchmark of six spatial reasoning tasks built from three-photo smartphone triplets of newly captured indoor scenes via an automatic in-the-wild 3D scene-graph extraction pipeline. Four tasks probe perception and perspective transformation over observed structure; two new tasks, L4 (spatial editing) and L5 (cross-view visibility editing), probe object-level counterfactual reasoning, where correct answers are absent from all input images. Each question provides 8-24 structured answer choices, enabling answer-letter-level diagnosis of spatial and fallback errors. The benchmark covers 120 private indoor scenes not drawn from public datasets, reducing public-data pretraining-overlap risk. Across 15 VLMs on 1,003 human-verified questions, task-wise mean VLM accuracy is only 8%-31%, versus 81%-97% human majority-vote accuracy. The pooled human--best-VLM gap is 53 pp, with at least 39 pp on every task. The structured answer space further reveals non-uniform failures, including weaker camera-depth-axis inference and fallback behavior on difficult visibility-editing cases.

---


### 92. [GenSP: Consistent Spherical Parameterization via Learning Shape Generative Models](https://arxiv.org/abs/2607.00492)

**<font color=#1a73e8>作者：</font>** Sai Karthikey Pentapati, Shashank Gupta, Rajesh Sureddi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce GenSP, a data-driven framework that learns consistent spherical parameterizations across a collection of genus-0 shapes. Instead of optimizing the parameterization of each shape independently, our method learns a neural generative model that predicts a continuous mapping from the unit sphere to shapes in a dataset. Under this formulation, spherical parameterizations are obtained through the inverse mappings of the learned generator, which encourages similar shapes to share consistent parameterizations. To make this formulation practical, we address several key challenges in learning such a generative model. First, we introduce a continuous neural deformation model that predicts surface points from sphere coordinates and latent shape codes, avoiding discretization artifacts common in mesh-based formulations. Second, we augment the training space with intermediate shapes that bridge the sphere and input shapes, allowing the model to learn meaningful deformations across a heterogeneous shape collection. Third, we compute reliable initial correspondences by propagating mappings along a spanning tree of training shapes in the latent space. Experiments on the ShapeNet dataset demonstrate that our approach significantly reduces geometric distortion and improves cross-shape consistency compared with state-of-the-art spherical parameterization methods.

---


### 93. [HieDG: A Hierarchical Discrete Geometry-Guided Framework for Multi-Animal Tracking](https://arxiv.org/abs/2607.00494)

**<font color=#1a73e8>作者：</font>** Chenxun Deng, Zhongde Zhang, Ye Yuan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-animal tracking (MAT) is critical for wildlife monitoring and behavioral analysis, yet remains challenging due to uniform appearance, high density, and irregular motion. Existing methods typically follow heuristic- or query-based paradigms: the former relies on handcrafted geometric associations without end-to-end optimization, whereas the latter enables joint optimization but relies heavily on appearance embeddings. In such conditions, continuous geometric embeddings can be unstable, as small coordinate perturbations may disproportionately alter cross-frame attention weights, degrading identity association performance. To address this limitation, we propose HieDG, a Hierarchical Discrete Geometry-guided tracking framework that reformulates geometric dynamics as structured discrete representations within a query-based tracker. Instead of directly using raw geometric signals, HieDG employs a two-stage residual codebook to discretize position, scale, and velocity cues, transforming unstable continuous geometry into structured, stable discrete tokens. These tokens are aligned with visual embeddings and integrated into the tracking queries to enhance identity consistency. Extensive experiments on animal-specific benchmarks (AnimalTrack, BFT, and BuckTales) demonstrate state-of-the-art association performance with significant improvements in HOTA, AssA, and IDF1. Additional evaluations on generic multi-object tracking benchmarks, including DanceTrack and SportsMOT, show competitive performance, indicating the broader applicability of discretized geometric modeling beyond animal-specific scenarios.

---


### 94. [Prior-Anchored Debiasing for Long-Tailed Multi-Organ Pathology Report Generation](https://arxiv.org/abs/2607.00499)

**<font color=#1a73e8>作者：</font>** Feng Yang, Jie Liu, Yubo Pang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated pathology report generation from Whole Slide Images (WSIs) has
attracted increasing attention in digital pathology. However, existing methods
are predominantly developed under single-organ settings, overlooking the
multi-organ scenarios encountered in clinical practice, where organ types
typically follow a long-tailed distribution. To address this gap, we identify
two critical biases: (1) visual representation bias, where the encoder favors
head-class patterns over tail-class discriminative features, and (2) textual
decoding bias, where the decoder overfits to head-class narrative patterns,
yielding diagnostically unreliable outputs for tail-class organs. To mitigate
these two biases, we propose a novel Prior-anchored multi-Organ pathology
report Generation framework (PriOrGen). Specifically, a Visual-Prototype
Anchored Bottleneck module leverages the information bottleneck principle with
learnable anchor representations to selectively retain diagnostically relevant
visual information while filtering out head-biased redundancy. Secondly, a
Meta-Report Anchored Bank module constructs an organ-specific meta-report
anchored bank and retrieves organ-faithful textual priors to steer the decoder
away from head-class narrative patterns. Extensive experiments on a multi-
organ pathology dataset demonstrate that our method effectively mitigates
long-tail biases and achieves superior report generation performance across
both head and tail organ categories compared to state-of-the-art methods.

---


### 95. [A Task-State Representation for Long-Horizon Mobile GUI Agents](https://arxiv.org/abs/2607.00502)

**<font color=#1a73e8>作者：</font>** Yujie Zheng, Zikang Liu, Xin Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While long-horizon mobile GUI agents typically rely on thought-action-observation loops, they struggle to separate persistent task states from transient screen observations. As execution histories grow, this entanglement imposes a severe context burden, causing agents to forget initial requirements, hallucinate progress, or repeatedly interact with stale interfaces. To address this, we introduce Task-State Representation (TSR), a training-free framework that explicitly decouples task state from sensory input. Acting as a lightweight external wrapper, TSR maintains three structured components: a global instruction summary, a dynamic progress tracker for subgoals, and a transition-aware action verifier. By continuously updating through pre- and post-action visual comparisons, TSR effectively guides the agent's reasoning without requiring architectural modifications. Experiments across four mobile GUI benchmarks validate TSR's effectiveness, yielding up to a 12 absolute point increase in success rate on complex cross-application and memory-intensive tasks.

---


### 96. [AnF-DiffPET: Anatomy- and Frequency-Guided Diffusion for PET/CT Denoising](https://arxiv.org/abs/2607.00509)

**<font color=#1a73e8>作者：</font>** Xuepeng Liu, Ruili Li, Zetong Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Positron emission tomography (PET) provides essential functional information for disease assessment, however reducing injected activity or acquisition time produces low-dose (LD) PET with stronger count dependent noise and less reliable uptake quantification. Diffusion models offer a promising solution for PET denoising by progressively recovering high-dose (HD) PET images from LD inputs. However, LD-to-HD PET denoising is still challenging due to insufficient anatomical guidance, unstable multi-scale feature propagation, and uncertain frequency domain uptake recovery. We propose AnF-DiffPET, an anatomy- and frequency-guided diffusion framework for computed tomography (CT) conditioned LD PET denoising. The framework integrates Anatomical-Frequency Guidance (AFG), Multi-Scale Cross-Transformer Reconstruction (MSCTR), and Frequency-Contrastive Hard Mining (FCHM) to enhance anatomy aware feature modulation and frequency domain consistency during denoising. Experimental results across four PET/CT datasets show that the proposed method improves image fidelity, anatomical consistency, and quantitative fidelity over representative CNN-based, GAN-based, transformer-based, and diffusion-based methods. The code and trained models will be publicly released upon acceptance.

---


### 97. [From Structural Equation Modelling to Double Machine Learning: Robustness Analysis for Survey-Based Research](https://arxiv.org/abs/2607.00512)

**<font color=#1a73e8>作者：</font>** Ka Ching Chan, Qiana Liu, Sanjib Tiwari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structural equation modelling (SEM) is widely used in survey-based business and information systems research to assess latent constructs and theory-driven structural relationships. However, SEM path significance is obtained within a particular model specification and may not show whether findings remain stable under alternative estimation frameworks. This study develops and demonstrates a staged robustness analysis framework that connects SEM, ordinary least squares (OLS) regression, and Double Machine Learning (DML). SEM is first used to refine the measurement structure and estimate the robustness-baseline SEM model, in which the full theory-specified structural path system is retained for downstream robustness analysis before final structural path evaluation. OLS regression is then applied to SEM-derived construct scores as a transparent regression benchmark. Finally, DML-style residualisation is used to examine whether each tested focal relationship remains stable after flexible machine-learning-based adjustment for observed controls. Learner-sensitivity checks compare Random Forest, Gradient Boosting, and Support Vector Machine learners, and selected reverse-direction diagnostics are used to examine directional sensitivity. The framework is demonstrated using a FinTech Digital Customer Intimacy survey model. The findings identify which relationships are stable across SEM, OLS, and DML-style checks, and which require more cautious interpretation. A reproducible Google Colab workbook and generated result files are publicly available, providing a reusable template that researchers and students can adapt to other survey-based latent-construct studies. The paper contributes a practical robustness workflow and interpretation guide for survey-based researchers seeking to complement SEM with conventional and machine-learning-based robustness checks.

---


### 98. [Cross4D-JEPA: Dense Cross-modal Correspondence Distillation for 4D Point Cloud Representation Learning](https://arxiv.org/abs/2607.00514)

**<font color=#1a73e8>作者：</font>** Trung Thanh Nguyen, Hai Nguyen-Truong, Tu Vo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automatic understanding of dynamic 4D point clouds, the 3D-point sequences captured over time by depth sensors and LiDAR, is central to robotics and embodied perception. Yet annotating them densely is expensive, making self-supervised pretraining the natural route to transferable representations. Existing pretext tasks, however, are almost entirely intra-modal, and the few methods that transfer knowledge from 2D foundation models rely on a single global embedding per clip, discarding the rich per-patch semantics that these models compute. To address this gap, we propose Cross4D-JEPA, a teacher-student method that distills a frozen 2D foundation model, an image model DINOv2, or a video model V-JEPA 2, into a 4D point encoder. The proposed method combines (1) a dense cross-modal correspondence that maps every 3D point to the teacher patch feature it projects to, and (2) a per-point objective that trains the student to match these features in latent space with no masking, negatives, or decoder. We evaluate Cross4D-JEPA on four benchmarks, MSR-Action3D, DeformingThings4D, NTU-RGB+D 60, and HOI4D, against intra-modal and global cross-modal baselines. Experimental results show that, under a matched protocol, the proposed method consistently outperforms intra-modal and global cross-modal baselines across the four benchmarks and is competitive with heavier published 4D methods; further analysis attributes this gain primarily to the granularity of the correspondence rather than the teacher modality. Beyond recognition accuracy, the dense representation learned by Cross4D-JEPA transfers across domains, improves label efficiency, and improves full-label fine-tuning under the same training budget, while a 13x smaller encoder matches a heavyweight pooling backbone.

---


### 99. [Draped Surfaces: A Contour-Adaptive Interface Overlaid on the Physical Environment for Mixed Reality Workspaces](https://arxiv.org/abs/2607.00518)

**<font color=#1a73e8>作者：</font>** SoonUk Kwon, Barrett Ens, Pourang Irani  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conventional Mixed Reality (MR) workspaces are frequently organized in cockpit-like layouts, where multiple floating windows surround the user. While this configuration facilitates access to digital content, it often induces occlusion, reducing understanding of the physical environment and limiting access to real-world objects. To overcome this challenge, we present the Contour-Adaptive Mixed Environment Overlays (CAMEO), a contour-adaptive MR interface that drapes virtual windows onto physical surfaces. This design integrates digital content with nearby items, thereby improving users' visual access to background objects and supporting interaction with them. We evaluate CAMEO in two controlled studies. The first demonstrates that draping reduces hand-movement detours relative to flat mid-air surfaces, enabling more direct interaction with nearby items. The second shows that controlled window deformation does not significantly impair text legibility when compared to flat surfaces. Together, these findings contribute a novel design paradigm for MR workspaces that balances immersion, readability, and environmental understanding.

---


### 100. [Restore3D: Breathing Life into Broken Objects with Shape and Texture Restoration](https://arxiv.org/abs/2607.00522)

**<font color=#1a73e8>作者：</font>** Xiaolong Shen, Zongxin Yang, Yi Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Restoring incomplete or damaged 3D objects is crucial for cultural heritage preservation, occluded object reconstruction, and artistic design. Existing methods primarily focus on geometric completion, often neglecting texture restoration and struggling with relatively complex and diverse objects. We introduce Restore3D, a novel framework that simultaneously restores both the shape and texture of broken objects using multi-view images. To address limited training data, we develop an automated data generation pipeline that synthesizes paired incomplete-complete samples from large-scale 3D datasets. Central to Restore3D is a multi-view model, enhanced by a carefully designed Mask Self-Perceiver module with a Depth-Aware Mask Rectifier. The rectified masks learned by the self-perceiver guide an image integration and enhancement phase, helping retain observed shape and texture patterns while refining the generated regions and mitigating the low-resolution limitations of the base model, yielding high-resolution, semantically coherent, and view-consistent multi-view images. A coarse-to-fine reconstruction strategy is then employed to recover detailed textured 3D meshes from refined multi-view images. Experiments on synthetic and real broken-object benchmarks show that Restore3D improves multi-view restoration quality and textured-mesh reconstruction over representative inpainting, completion, and reconstruction baselines in the evaluated settings. Project Page: this http URL

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-236](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
