# 📦 其他研究 | 2026年08月10日

> 本类共 **167** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-167](./part-04.md)

---

### 101. [Density-aware Hierarchical Clustering Based on Element-Categorized Connection Subgraphs](https://arxiv.org/abs/2608.06990)

**<font color=#1a73e8>作者：</font>** Yuning Yu, José Rodríguez-Piñeiro, Xuefeng Yin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clustering is a fundamental data mining technique for pattern recognition through unsupervised learning. Among various clustering methods, hierarchical clustering, density-based clustering, and graph clustering stand out as representative approaches. For hierarchical clustering, it can be categorized into agglomerative and divisive modes to construct clusters in a recursive manner. The key aspect of both modes is the calculation of inter-cluster similarity, which determines whether to merge the sub-clusters into one cluster or divide a current cluster into sub-clusters. Traditionally, the similarity is derived from pairwise distances, often overlooking density variations and structural connectivity in graphs. To address this, we propose a density-aware hierarchical clustering method based on element-categorized connection subgraphs (DHC-ECS), which effectively integrates the hierarchical clustering, density-based clustering, and graph clustering. Particularly, a novel inter-cluster similarity metric is introduced that considers not only distances but also the element categorization in the KNN connection subgraphs, kernel density estimation, and local connectivity within sub-clusters. Extensive evaluations on heterogeneous benchmark datasets demonstrate that DHC-ECS exhibits superior overall performance in terms of clustering accuracy and parameter robustness compared with the baseline methods (including AChameleon, RNN-DBSCAN, McDPC, and G-RMS). The work indicates the great potential of the proposed clustering algorithm for low-dimensional datasets by leveraging local density and graph-structured connectivity (i.e., the duality of vertices and edges), as well as the possibility to determine an intrinsic threshold, reducing the reliance on manual parameter tuning.

---


### 102. [HRDiT: Training-Free High-Resolution Image Generation with Off-the-Shelf Diffusion Transformer Models](https://arxiv.org/abs/2608.07003)

**<font color=#1a73e8>作者：</font>** Yu Xue, Haoxuan Qu, Zhuoling Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free text-to-high-resolution image generation has recently attracted growing research attention. However, existing studies on this task primarily focus on adapting off-the-shelf U-Net-based diffusion models to high resolutions, with limited progress on adapting off-the-shelf Diffusion Transformer (DiT) models despite their strong text-to-image generation capabilities at limited resolutions. In this work, we find two key challenges particularly hindering the application of off-the-shelf DiT models for high-resolution image synthesis in a training-free manner, namely, spatial disorder and long generation time. To address these challenges, we propose a novel method tailored to adapt off-the-shelf DiT models for high-resolution image synthesis. Extensive experiments show the efficacy of our method. Our code is available at: this https URL.

---


### 103. [FedLBW: A Loss-Based Weighting Strategy for Federated Learning on Non-IID Data in Wireless Networks](https://arxiv.org/abs/2608.07007)

**<font color=#1a73e8>作者：</font>** Majid Kundroo, Tinku Singh, Taehong Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables collaborative machine learning (ML) across distributed clients while preserving privacy. However, efficient model convergence in FL remains challenging, especially in wireless networks where non-independent and identically distributed (non-IID) data and frequent client dropouts are common. Traditional FL algorithms, such as FedAvg, rely solely on dataset size to weight client updates. This introduces biases towards clients with larger datasets and makes the process sensitive to non-IID data, outliers, and client dropouts. To address these challenges, we propose Federated Learning with Loss-Based Weighting (FedLBW), a novel aggregation method that assigns each client's update a weight proportional to the inverse of its validation loss, computed using a small proxy dataset on the server, rather than its dataset size. This ensures that lower-loss models exert greater influence during aggregation, prioritizing the most reliable updates and boosting overall performance. Through extensive experiments across multiple datasets, including FashionMNIST (CNN), CIFAR-10 (ResNet-18), and CIFAR-100 (ResNet-34), we demonstrate that FedLBW achieves higher accuracy and faster convergence compared to baseline algorithms such as FedAvg, FedAvgM, FedProx, FedNova, FedLAW and FedDkw, with notable improvements of up to 7.6 % higher accuracy on CIFAR-10 in extreme non-IID cases. Moreover, FedLBW showcases exceptional resilience to increasing dropout probabilities, consistently maintaining significantly higher accuracy even in challenging conditions. These results establish FedLBW as an effective and resilient solution for FL in wireless network environments, offering marked improvements in model accuracy, convergence speed, and robustness to non-IID data and client dropouts.

---


### 104. [Scenix: Sparse-View 3D Scene Reconstruction via Executable Scene Programs](https://arxiv.org/abs/2608.07012)

**<font color=#1a73e8>作者：</font>** Kai Li, Lutao Jiang, Zhenyang Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesizing a structured and editable 3D indoor scene from a few uncalibrated RGB views requires more than generating high-quality individual assets: a system must infer the room structure, associate objects across incomplete observations, and recover a globally consistent spatial configuration. Previous methods mainly focus on 3D scene generation with text input or require continuous visual inputs with additional priors, \ e.g., human-annotated masks or accurate 3D layouts, which makes these methods labor demanding and hard to apply in general cases. We present \textsc{Scenix}, a sparse-view 3D scene reconstruction framework via executable scene programs, a structured representation that can be directly instantiated into editable 3D scenes. Given sparse views, \textsc{Scenix} predicts executable scene programs through perception-grounded asset instantiation and closed-loop spatial refinement. % We present \method, a framework that predicts an executable scene representation from sparse views and realizes it through perception-grounded asset instantiation and closed-loop spatial refinement. To support this task, we construct \dataset, a dataset of approximately 110,000 synthetic and real indoor scenes with multiview imagery, room structures, object-centric descriptions, and metric spatial annotations. We further introduce observation-consistent supervision that aligns each target scene with the visual evidence available in its input views. Experiments on held-out \textsc{XScene} scenes, real indoor images, and out-of-distribution SpatialGen cases evaluate structured scene prediction, object grounding, and spatial refinement.

---


### 105. [Understand Before Detect: Vision--Language Learning for Omni-Domain Infrared Small Target Detection](https://arxiv.org/abs/2608.07015)

**<font color=#1a73e8>作者：</font>** Haoyang Yuan, Boyang Li, Yingqian Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omni-domain infrared small target (IRST) detection is crucial for infrared surveillance, yet remains challenging due to heterogeneous imaging domains and inconsistent target characteristics. Previous deep learning-based methods have been developed for visual-only paradigms and achieved promising performance on domain-specific tasks. However, existing methods follow the task-specific supervised learning paradigm. This paradigm simplifies the full-scene infrared observations to sparse target supervision, discarding the semantics that remain invariant across heterogeneous domains. Consequently, detection performance suffers substantially under domain shifts. To handle this issue, we introduce \textbf{``understand before detect''}, a paradigm that formulates omni-domain IRST detection as an understanding-driven process, where holistic infrared target understanding precedes precise detection. Building on this paradigm, we propose \textbf{JinSight}, which first develops holistic IRST understanding through language supervision and then transfers the learned cross-domain representations to precise small-target detection. By grounding infrared representations in language semantics, JinSight enables a single model to generalize across heterogeneous infrared domains. We then introduce Latent Semantic Interaction (LSI), which exchanges language-aligned global semantics with fine-grained spatial features in a compact low-rank space. To address the lack of multimodal omni-domain IRST benchmarks, we build \textbf{OmniIRST-VL}, the first large-scale, highly diverse vision--language dataset for omni-domain IRST detection. It comprises over 39k annotations across six complementary instruction tasks covering both scene-level understanding and target-centric reasoning.

---


### 106. [Effects of parental controls in the context of Digital Forensics](https://arxiv.org/abs/2608.07016)

**<font color=#1a73e8>作者：</font>** Selina Märchya, Mauro Vignatia, Frank Breitinger  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Parental control systems are designed to protect minors online, but can inadvertently obstruct digital forensic investigations. When enabled, these systems restrict administrative privileges, disable debugging options, and alter data accessibility, complicating evidence acquisition and analysis. This study empirically examines the impact of Microsoft, Google, and Apple parental controls on forensic processes across fifteen Windows, Android, and iOS devices. Through controlled experiments, we evaluate their impact on evidence accessibility and identify forensically sound methods to overcome these limitations. The findings provide practical guidance for investigators and contribute to improving forensic readiness in environments governed by parental control systems.

---


### 107. [Hyperbolic Graph Embedders for Link Prediction and Topology Reconstruction](https://arxiv.org/abs/2608.07029)

**<font color=#1a73e8>作者：</font>** Robert Jankowski, Maksim Kitsak, Dorota Celińska-Kopczyńska  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperbolic embeddings provide compact geometric representations of complex networks in hyperbolic spaces, but systematic comparisons of methods developed in machine learning, network science, and algorithmics remain rare. We benchmark 13 unsupervised hyperbolic graph embedders under a unified protocol for link prediction and topology reconstruction on synthetic and empirical networks. The protocol captures both missing-link recovery and the preservation of local and global network structure. Maximum-likelihood and representation-learning-based approaches, including hybrid variants, achieve the strongest overall performance, although no method dominates across all tasks and structural regimes. Performance is more strongly associated with embedding paradigm than with disciplinary origin. We identify the network regimes in which different paradigms succeed or fail and provide practical guidance for method selection in downstream applications.

---


### 108. [Accounting Graph Transformer for Short-History Multi-KPI Forecasting in Small Businesses](https://arxiv.org/abs/2608.07037)

**<font color=#1a73e8>作者：</font>** Shrutendra Harsola, Vignesh Subrahmaniam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small businesses often have only 12-24 months of accounting history, yet planning and risk workflows require coordinated forecasts across financial statements. We study joint 12-month forecasting of 13 income-statement, balance-sheet, cash-flow, and working-capital key performance indicators (KPIs) from 71 monthly ledger series. We introduce the Accounting Graph Transformer (AGT), which represents each ledger series as a masked token, exchanges information through typed attention on a fixed accounting-relation graph, pools target-specific context, and fuses it with a gated three-month recency path. Across 11,993 forecast origins from 1,060 unseen companies, AGT achieves sample-weighted KPI-macro mean absolute error (MAE) $0.6990 \pm 0.0013$ over three independent seeds, compared with $0.7378 \pm 0.0014$ for the strongest baseline, LightGBM. At the pre-specified seed 42, a paired company-clustered bootstrap gives a LightGBM-minus-AGT difference of 0.0395 with 95% confidence interval (CI) $[0.0350,0.0439]$. AGT is best on all 13 KPIs against LightGBM, TimeMixer, and SOFTS in the matched seed-42 comparison, while final-architecture ablations show that relational attention, accounting topology, and the recency path each improve validation and test accuracy. On 7,094 additional unseen companies with origins sampled from January-May 2025, AGT obtains 0.7548 MAE versus 0.7694 for SOFTS. A single 5.3M-parameter model produces 156 aligned forecasts without company-specific fitting, providing one forecasting layer for integrated planning, liquidity, and working-capital analysis.

---


### 109. [KnifeHunter: Structured Local Representation Learning for Fine-Grained Knife Image Retrieval in Law Enforcement](https://arxiv.org/abs/2608.07057)

**<font color=#1a73e8>作者：</font>** Syed Sameed Husain, Eng-Jon Ong, Stephen Simpson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knife-enabled violence presents a major public safety challenge, and law enforcement agencies require scalable tools for catalogue-level knife identification, intelligence analysis, and source attribution. Manual visual comparison is specialist, time-consuming, and difficult to scale under operational imaging conditions. We introduce KnifeHunter, an end-to-end forensic knife image retrieval system developed with UK law enforcement. The work contributes the KnifeHunter dataset, comprising 25,843 images across 543 knife classes from police evidence, retail catalogues, and border-force seizures, with structured metadata, Medium/Hard evaluation protocols, and large-scale distractor evaluation. We further propose CoRe-Net, a compact single-descriptor retrieval architecture that combines global context with spatially localised discriminative evidence. CoRe-Net introduces Structured Complementary Representation Learning (SCRL) to organise local evidence into complementary prototype-based representations, and Bi-Directional Reciprocal Fusion (BDRF) to integrate global and local evidence through residual projection and gated local-to-global injection. Using an EVA02-Base backbone and cosine-similarity retrieval, CoRe-Net achieves 88.0% mAP and 86.7% mP@10 on the Medium protocol, and 85.1% mAP and 83.8% mP@10 under distractor conditions. KnifeHunter was deployed by UK police forces during Operation Sceptre deployments from 2023 to 2025, achieving 99.2% mP@1 on field queries. These results demonstrate a practical and effective multimedia retrieval framework for fine-grained forensic knife matching in operational law-enforcement settings.

---


### 110. [Explanation Stability of Test-Time Adaptation in Computational Pathology: A Large-Scale Benchmark](https://arxiv.org/abs/2608.07062)

**<font color=#1a73e8>作者：</font>** R. G. Bahumanya, Harshith V. M., Shreyank N. Gowda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) has become a practical way to adapt deployed models to unlabeled target data, a setting that is especially relevant in computational pathology where staining, scanner, and cohort shifts are routine. While most TTA methods are evaluated by their effect on accuracy, clinical use also depends on whether the model's explanations remain reliable after adaptation. In this paper, we take a closer look at this largely unmeasured effect. We study explanation stability under TTA across two histopathology benchmarks, Camelyon17 and NCT CRC-HE, using five architectures ranging from convolutional networks to vision transformers and a pathology foundation model, seventeen TTA methods, and four attribution families. Across 2,958 adaptation runs, we observe a clear and systematic pattern: TTA methods differ sharply in how much they move model explanations, with frozen-backbone methods leaving attributions almost unchanged and continual methods such as CoTTA and RoTTA causing the largest drift. This effect is not uniform. Convolutional networks are substantially more sensitive than transformer and foundation-model backbones, and explanation drift increases with adaptation strength while remaining largely insensitive to batch size. Surprisingly, explanation stability is only weakly coupled to adaptation quality. Some methods preserve explanations almost perfectly while degrading calibration or accuracy, producing silent failures that would be missed by accuracy-only or explanation-only evaluation. These findings show that explanation stability is a distinct reliability axis for TTA in computational pathology. We release the metric, protocol, and full benchmark to support future work on adaptation methods that are not only accurate, but also stable and clinically auditable. Code: this https URL

---


### 111. [Soft Redaction of Image Provenance via Zero-Knowledge Proofs](https://arxiv.org/abs/2608.07063)

**<font color=#1a73e8>作者：</font>** Muhammad Awan, John Collomosse  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Content provenance standards, such as C2PA, are increasingly used to attach signed records of origin, editing history, and rights to digital images. However, provenance transparency can conflict with privacy -- assertions that strengthen trust in an image may also reveal sensitive information about the creator or capture context. We propose soft redaction for image provenance: a mechanism that replaces sensitive provenance assertions with zero-knowledge proofs (ZKPs) of selected properties over hidden data. Our work focuses on distance proofs. We first show how location assertions can support proofs of proximity to a public reference point, using Chebyshev polynomial approximations within the ZKP proof circuit. We then extend the approach to L2 distance proofs over biometric embeddings, enabling privacy-preserving claims related to likeness to help enforce personality rights with images. Finally, we apply the same distance-proof construction to perceptual hashes (visual fingerprints), supporting an anti-spoofing use case in watermark-based recovery of stripped provenance metadata. Our results demonstrate that ZKPs over image provenance can provide practical soft-redaction capabilities, compatible with C2PA, that may be constructed in seconds and verified in milliseconds.

---


### 112. [XGait: A Multi-Modality Wireless Sensing Dataset for Indoor Human Tracking and Identification](https://arxiv.org/abs/2608.07064)

**<font color=#1a73e8>作者：</font>** Wei Xu, Zhu Wang, Yifan Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Wireless sensing has emerged as a promising approach for tracking and identification using commodity Internet of Things devices. However, the features derived from a single wireless modality are often fragile to variations in environmental layouts and walking trajectories. Furthermore, most existing studies are based on datasets collected in specific scenarios with limited trajectory diversity and sensing modalities, preventing a robust evaluation of system generalization. \textcolor{blue}{To address this gap, we introduce \textbf{XGait}, a multi-modality wireless sensing dataset that synchronously captures human walking using Wi-Fi and acoustic transceivers across three indoor scenarios, with vision-based measurements serving as ground truth. Specifically, XGait contains more than 22K walking samples from 27 participants, covering diverse directions and trajectories to support both indoor tracking and identity recognition. To bridge the heterogeneity of wireless sensing modalities, we propose a unified Doppler spectrogram representation that maps Wi-Fi and acoustic signals into a shared time--frequency space, along with a standardized benchmark pipeline for pre-processing, temporal alignment, and feature construction, enabling reproducible evaluation and systematic cross-modal analysis. Extensive evaluations demonstrate that Wi-Fi and acoustic sensing exhibit complementary strengths, particularly under complex trajectories and challenging propagation conditions, thereby paving the way for novel research in the field of multi-modality wireless sensing.} The dataset and code are available at this https URL.

---


### 113. [PTQ4SNN: Membrane-Aware Post-Training Quantization for Spiking Neural Networks](https://arxiv.org/abs/2608.07066)

**<font color=#1a73e8>作者：</font>** Hui Xie, Tong Shi, Haotong Qin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spiking neural networks (SNNs) enable sparse and event-driven computation, but their low-bit deployment remains incomplete because recurrent membrane states are commonly retained in floating point even after weight quantization. Quantizing these states is challenging because their distributions differ across channels and from the preceding weights, while small perturbations near the firing threshold may alter spike decisions and accumulate over time. We propose PTQ4SNN, a membrane-aware post-training quantization framework that jointly quantizes weights and recurrent membrane states using only a small calibration set. First, a channel-wise Unified Scale Bridge constrains the membrane scale as s_mem,c = s_w,c * 2^k_c, adapting to membrane distributions while enabling shift-compatible scale conversion. Second, Mixed-Precision Bit Allocation assigns 2/4/8-bit precision to membrane channels according to firing activity and quantization sensitivity under an average-bit budget. The framework operates on reusable projection-LIF pairs and supports both convolutional SNNs and spike-driven Transformers without backbone retraining. Experiments on static and event-based classification and semantic segmentation show that PTQ4SNN effectively preserves model accuracy under W4 quantization and approximately 4-bit membrane precision.

---


### 114. [DocMemo: Dynamic Evidence Discovery via Probabilistic Memory-Guided Retrieval for Multi-Modal Document Understanding](https://arxiv.org/abs/2608.07067)

**<font color=#1a73e8>作者：</font>** Hanshu Yao, Janfeng Zhong, Niu Lian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-document understanding requires locating sparse and heterogeneous evidence across hundreds of pages, yet existing systems remain limited by static retrieval and fragile cross-round memory. Mainstream single-round methods commit to a fixed top-$k$ page set at the outset and struggle to recover from early retrieval errors; recent iterative approaches allow multi-round evidence acquisition, but they do not investigate the propagation mechanism of cross-round states, making it difficult to track the dynamic changes in page relevance. To address these limitations, we propose DocMemo, a memory-guided framework that formulates long-document reasoning as dynamic evidence exploration. DocMemo maintains a tri-level retrieval state consisting of Document Schema Memory, Page Belief Memory, and Question Episodic Memory, which respectively capture structural priors, dynamic relevance estimation, and query-specific reasoning trajectories. During reasoning, DocMemo continuously refines cross-round page selection through Bayesian page belief updating with Thompson sampling, spatial proximity propagation, and structure-aware adaptive-granularity evidence access, while supplementing page-level evidence with fine-grained visual regions. Experiments on 3 benchmarks show that DocMemo achieves state-of-the-art performance and validate the efficacy of structured memory and dynamic page belief updating. Code is available at this https URL.

---


### 115. [Beyond Isolation: Unlocking Reinforcement Learning Component Synergy for Sample-Efficient Continuous Control](https://arxiv.org/abs/2608.07086)

**<font color=#1a73e8>作者：</font>** Qi Zhao, Guozheng Ma, Yilun Kong 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning systems are significantly more complex than other machine learning paradigms due to inherent properties, causing RL system design to jointly account for many tightly coupled factors. Despite advances in individual algorithmic components, their functional interdependencies remain underexplored: do they exhibit mutual synergy or counterproductive interference? To bridge this gap, we conduct a systematic investigation and find that the efficacy of different components exhibits significant task-dependency, and naively stacking state-of-the-art techniques does not necessarily yield performance gains; instead, it often triggers emergent challenges, such as compounded non-stationarity. Building upon these findings, we distill a suite of actionable insights into the principled coordination of these components. Guided by these insights, we propose ROSER, an RL framework that coordinates three critical dimensions: Model-based Representation, Optimization Stability, and Experience Replay. Across diverse continuous-control benchmarks, ROSER consistently outperforms vanilla baselines and achieves 17.60% gains over naive stack. Our findings underscore the necessity of a holistic perspective in RL system design and paves the way for developing sample-efficient agents.

---


### 116. [International Transfer of Stochastic Cortical Self-Reconstruction](https://arxiv.org/abs/2608.07092)

**<font color=#1a73e8>作者：</font>** Fabian Bongratz, Zhizheng Zhuo, Chao Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stochastic cortical self-reconstruction (SCSR) enables personalized mapping of gray matter atrophy, a hallmark of neurodegenerative disorders such as Alzheimer's disease (AD), onto high-resolution cortical surfaces. Unlike conventional normative modeling approaches, which typically operate at a coarse regional level and remain inherently constrained by the covariates included during training, SCSR estimates an individualized healthy reference directly from the observed cortical thickness at the vertex level. This allows the detection of subtle, subject-specific deviations from healthy cortical shape. In this work, we investigate the generalization and transferability of SCSR, originally trained on UK Biobank (UKB) data, to an independent Chinese population dataset. Specifically, we evaluate the ability of SCSR-derived Z-scores to discriminate between healthy scans, individuals with mild cognitive impairment (MCI), and patients with AD, while also assessing model robustness across the lifespan. We compare four training strategies: direct application of the UKB-trained model, fine-tuning on Chinese data, training from scratch, and joint training on UKB and Chinese cohorts. As reconstruction backbones, we consider both a multilayer perceptron (MLP) and a Spherical UNet (SUNet). Our results demonstrate that SCSR provides robust detection of cortical atrophy in the Chinese population across all evaluated models. The highest discriminative performance was achieved by the fine-tuned SUNet model (average pairwise AUC = 0.848), followed closely by the UKB-trained SUNet. Moreover, reconstruction errors remained low across the lifespan, even when the training population exhibited a substantially narrower age distribution, indicating strong cross-population transferability.

---


### 117. [SoK: Cryptographic Key Recovery for Cryptoasset Custody and Financial Technologies](https://arxiv.org/abs/2608.07104)

**<font color=#1a73e8>作者：</font>** Francisco Javier Becerra Sanchez, Antonio Ken Iannillo, Radu State  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptoasset systems often bind cryptographic key control to financial control: losing a wallet seed, custody share, hardware device, or smart-account credential can remove spend authority, while compromised recovery can enable theft. Existing work treats recovery through separate vocabularies--key backup, secret sharing, account recovery, credential re-issuance, social recovery, and asset migration--making mechanisms and tradeoffs difficult to compare.
This paper presents a Systematization of Knowledge (SoK) on cryptographic key recovery for cryptoasset custody and financial technologies. Starting from a 118-paper systematic-review discovery corpus, we derive a 77-paper synthesis corpus and code each retained system in a master matrix covering recovered objects, recovery semantics, mechanisms, enrollment and storage, authorization, trust placement, failure events, post-recovery state, validation evidence, deployment status, privacy, usability, and limitations. The matrix supports an axis-first taxonomy that separates secret-restoring, hybrid, control-restoring, forensic/extractive, and framework-oriented recovery.
Our central observation is that recovery is not a single operation: systems may reconstruct an original secret, regenerate a seed, restore a share, reissue a credential, migrate signing authority, restore account control, move assets, or extract forensic artifacts. We derive a generalized construction model, check it against production-facing designs, and identify six findings: recovery semantics are heterogeneous; recovery shifts trust; liveness improvements create abuse paths; post-recovery lifecycle management is uneven; protocol evidence outpaces user evidence; and recovery metadata remains underprotected. These gaps motivate a research agenda for recovery-aware financial technologies.

---


### 118. [Synthetic LiDAR Data Generation and Deterministic Downsampling for Point Cloud Classification on the Edge](https://arxiv.org/abs/2608.07106)

**<font color=#1a73e8>作者：</font>** Niclas Meyer, Stefan Reitmann  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying three-dimensional deep learning frameworks to low-power embedded processors is bottlenecked by the unstructured nature of spatial data and the resource-intensive distance sorting algorithms often used before neural network inference. To address this gap, this paper presents a hardware-constrained workflow optimized for native execution on the Raspberry Pi 5. To account for the reality gap between noiseless, clean computer-aided design (CAD) datasets and real-world sensor data, we use physics-based simulation to construct a synthetic LiDAR dataset. Cross-dataset evaluations demonstrate a substantial drop in classification accuracy when networks trained on clean CAD data are evaluated on synthetic LiDAR sensor data, highlighting the critical need for sensor-aware training. To address the latency bottleneck of traditional geometric preprocessing on edge CPUs, we integrate an isolated, feature-driven Critical Points Layer (CPL) as a frontend filter. Our results show that the pretrained CPL deterministically compresses raw 1024-point clouds to a subset of 40 to 60 unique coordinates. When profiled on the ARM Cortex-A76 processor, the complete pipeline achieves an inference throughput of approximately 50 FPS while maintaining an instance classification accuracy of 88.36%, demonstrating the viability of deterministic real-time 3D perception at the edge.

---


### 119. [Geometry-Aware Camera Localization for Bronchoscopy](https://arxiv.org/abs/2608.07116)

**<font color=#1a73e8>作者：</font>** Lumin Chen, Qingyao Tian, Jinpeng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera localization in bronchoscopy remains a challenging problem due to stringent accuracy requirements, real-time constraints, and limited training data. Compared to natural scenes, the confined anatomical structures demand millimeter-level precision, while intraoperative guidance necessitates low-latency inference. However, existing methods often fail to effectively exploit preoperative geometric priors, limiting their robustness and accuracy. To address these limitations, we propose a unified geometry-aware bronchoscope localization framework (GABL) that effectively fuses preoperative structural priors with paired intraoperative video to estimate 6-DoF camera poses. Specifically, to address visual ambiguity in complex airways, we propose a graph-guided coarse-to-fine localization scheme that effectively leverages structural priors for precise pose estimation. Furthermore, to mitigate pose jitter and bridge the visual-structural gap, we integrate a Transformer-based tracking model with a novel RGB-depth matching objective, jointly enforcing spatio-temporal and geometric consistency. Extensive experiments demonstrate that our method yields remarkable reductions of 8.37% and 31.76% in translation and rotation errors over the prior state-of-the-art, alongside 4 times inference speedup (33.6 FPS) for robust real-time bronchoscope localization. Project website: this https URL.

---


### 120. [Multiple Hypothesis Flow Estimation for Video Frame Interpolation under Matching Ambiguity](https://arxiv.org/abs/2608.07120)

**<font color=#1a73e8>作者：</font>** Zibo Su, Jing Kong, Ruixing Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many flow-based video frame interpolation (VFI) methods synthesize an intermediate frame by estimating optical flow fields, warping the two input frames, and blending the warped observations. These latent flow fields are typically learned through image-level reconstruction supervision without direct flow annotations. In ambiguous regions containing repetitive or stochastic textures, rotating symmetric structures, or fast motion with blur, the matching evidence for a single query may contain multiple comparable and spatially separated peaks. Although the ground-truth intermediate frame provides indirect supervision, it may not uniquely identify the latent correspondence in ambiguous this http URL several locations provide multiple plausible matches, a single-flow estimator can retain only one displacement and discard the remaining candidates. If the selected match is incorrect or inconsistent with those of neighboring pixels, warping samples content from mismatched locations, producing ghosting, structural distortion, or this http URL address this limitation, we propose a multiple hypothesis flow estimation framework that preserves top-K candidate correspondences and selects one per location through a reliability-guided router. Each hypothesis is initialized from a coarse matching anchor and refined separately through anchor-centered local attention. Frame synthesis is thus conditioned on one selected flow-appearance hypothesis rather than a soft combination of candidate this http URL on the proposed MA-HD benchmark and public VFI benchmarks show that our method achieves the best LPIPS and DISTS among the compared methods.

---


### 121. [Thermodynamic Human-Computer Interaction](https://arxiv.org/abs/2608.07123)

**<font color=#1a73e8>作者：</font>** Uzafir Ahmad Rafaq, Muaz Hassan, Ali Muzaffar  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Traditional human-computer interaction models rely on domain-specific techniques to model target prediction; models designed for cursor interaction prediction fail to generalize to mobile interfaces and vice versa. We introduce a unifying framework grounded in thermodynamics, proposing that human interaction is composed of phases in thermodynamic equilibrium and non-equilibrium. To demonstrate this, we derive Fitts' law and the proposed target prediction model from equilibrium thermodynamics by assigning kinetic and potential energies to a moving agent and target. Subsequently, we analyze the shortcomings of the prediction model and Fitts' law in edge cases, such as predicting intent for large targets. This analysis demonstrates that large targets cannot be accurately modeled using equilibrium thermodynamics. The proposed model scales across interaction modalities without modification, requires zero training data, and evaluates in constant O(1) time. Furthermore, we show that design properties such as the color of a button act as independent parameters that influence the attractive force exerted on an agent. Applied to live web prefetching tasks, the framework achieved an efficient Fetch:Click ratio of 1.37 and predicted the user's target with an accuracy of 98.1%.

---


### 122. [Online Conformal Prediction Beyond Feedback](https://arxiv.org/abs/2608.07139)

**<font color=#1a73e8>作者：</font>** Joar Skalse, Edoardo Pona, Osvaldo Simeone 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty quantification is essential when deploying machine learning models in safety-critical applications. Online conformal prediction (OCP) provides theoretically principled uncertainty quantification for arbitrary black-box classifiers and non-i.i.d. data streams by constructing prediction sets that are guaranteed to contain the true label at a user-specified frequency. OCP usually updates prediction sets using feedback from previously deployed predictions. We instead study an OCP setting beyond feedback: on each round, the learner can either output a prediction set or query the correct label, but not both. Thus, no deployed prediction is ever evaluated directly. We reduce this problem to a partial monitoring game in which prediction actions return no observation and a separate query action reveals the label. The reward function is constructed in a way that encourages the learner to output small prediction sets while ensuring that the correct label is covered with a sufficiently high probability. To solve this game, we develop OCP with queries (OCPQ) by adapting the label efficient forecaster of Cesa-Bianchi, Lugosi, and Stoltz (2004) to our setting. For any black box classifier and any (non-i.i.d.) oblivious data stream of length $T$, OCPQ has $O(T^{2/3})$ expected regret and expected coverage at least $\beta-O(T^{-1/3})$ for a user-defined $\beta$, while querying only an expected $T^{-1/3}$ fraction of rounds. This provides coverage comparable to bandit-based OCP methods while requiring no feedback from deployed prediction sets. Experiments on real-world datasets further demonstrate the effectiveness of our approach.

---


### 123. ["Operator, can you hear me?" A Faithful Line into the UNISOC Baseband](https://arxiv.org/abs/2608.07143)

**<font color=#1a73e8>作者：</font>** Eduard Vlad, Philipp Mao, Marcel Busch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Baseband processors are reachable over the radio at all times. Their most security-relevant logic runs deep inside protocol state machines: the control-plane handlers that gate registration, authentication, and session setup. Analyzing that logic systematically requires introspecting the firmware as it runs, which makes re-hosting the baseband necessary. Existing re-hosting work approximates the execution environment and under-approximates the SoC complexity of the baseband processor together with its surrounding components, bringing this state practically out of reach. We instead model each surrounding component, co-processors, SIM, application processor, from what a real device does, and step them in lockstep with the baseband on one shared clock. That makes faithfulness checkable at component interfaces, rather than assumed.
We call this method Unislop and demonstrate it on the UNISOC UDX710, a platform in an estimated 10-15% of cellular modems and in automotive systems, not systematically analyzed before. Starting from a Quectel RM500U-CNV module, we gain code execution, defeat its firmware-integrity check, instrument the baseband, and recover its peripheral environment from the running device. The resulting re-host reaches the same control-plane states as the real device, establishes a full PDU session, and carries real IP traffic on both ingress and egress. The recovered components are shared across UNISOC's baseband lineup, so with additional reverse-engineering effort the same design extends to further targets.

---


### 124. [InstanceSplat: Instance-Aware Feed-Forward 3D Gaussian Splatting for Scene Understanding](https://arxiv.org/abs/2608.07144)

**<font color=#1a73e8>作者：</font>** Minchao Jiang, Xiaoxuan Ma, Shunyu Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting (3DGS) enables efficient and generalizable 3D reconstruction, but current feed-forward 3DGS methods for scene understanding remain largely category-oriented. In contrast, instance-aware 3DGS methods typically rely on per-scene optimization and often decouple reconstruction from instance and semantic learning, limiting reciprocal interactions among them. We present InstanceSplat, a unified feed-forward 3DGS framework for generalizable 3D reconstruction and instance-aware scene understanding from pose-free multi-view images. In a single forward pass, InstanceSplat constructs an instance-aware Gaussian representation that jointly encodes appearance, geometry, instance identity, and language-aligned semantics. Shared 3D Gaussians ground instance identities across views, producing renderable and cross-view-consistent instance features. To allow reconstruction and scene understanding to benefit from each other, we further design an instance-centric learning strategy that connects reconstruction, instance learning, and semantic learning through shared instance structure. Specifically, instance cues guide reconstruction, language-aligned semantics strengthen the discrimination of confusing same-category instances, and instance regions aggregate semantic evidence into coherent object-level predictions. Experiments on novel-view synthesis, instance segmentation, and open-vocabulary semantic understanding under varying input-view settings and on an unseen dataset demonstrate state-of-the-art performance, practical efficiency, and strong generalization.

---


### 125. [Interpretable reinforcement learning with decision-tree pruning](https://arxiv.org/abs/2608.07151)

**<font color=#1a73e8>作者：</font>** Mark Leon Ringer, Michel Tokic  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning policies are difficult to inspect, but interpreting them is a prerequisite for trustworthiness. Converting a trained policy into explicit decision-tree rules improves transparency and the resulting artifacts often remain too complex for human understanding. We present a pruning process that simplifies such rule-based policies while preserving task performance and making edits to the policy auditable. The process defines a small set of structural and usage-aware operators and evaluates candidate edits by re-executing the policy to measure return and interpretability proxies. This exposes an transformation process from complex to compact policy structures. We investigate this approach on classic control and MuJoCo benchmarks, where pruning traces reveal consistent interpretability improvements while maintaining high performance.

---


### 126. [Machine Learning-Based Inter-Crystal Scatter Recovery for Ultra-High Resolution PET Imaging](https://arxiv.org/abs/2608.07155)

**<font color=#1a73e8>作者：</font>** Alexandre Bernier, Roger Lecomte, Jean-Baptiste Michaud  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inter-crystal scatter (ICS) events pose a significant challenge in ultrahigh- resolution positron emission tomography (UHR-PET), especially as detector crystals become smaller and their readouts increasingly segmented. Current approaches either reject these events, reducing sensitivity, or accept them with suboptimal positioning algorithms, degrading image resolution. We present a feed forward neural network to optimize ICS event recovery by inferring the line-of-response belonging to the first Compton interaction. Our approach was validated using both Monte Carlo simulations and experimental data from the fully pixelated LabPET-IIbased preclinical and brain UHR-PET this http URL demonstrate a 70% to 106% increase in sensitivity while preserving sub-millimeter spatial resolvability (down to 1.6 mm) compared to conventional methods. This ICS recovery approach is an effective solution that compensates for the lower detection efficiency of small, pixelated detectors in UHR-PET, enabling reduced scan times and lower radiation doses while largely preserving image quality.

---


### 127. [Capacity Confounds and Coverage Guarantees in Adaptive Sub-model Federated Learning](https://arxiv.org/abs/2608.07157)

**<font color=#1a73e8>作者：</font>** Alireza Moayedikia, Alicia Troncoso Lora  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sub-model federated learning lets resource-constrained clients train width-reduced versions of a global model, but existing methods allocate capacity by device resources alone. A natural next step, allocating capacity by each client's data heterogeneity as estimated from the updates the server already observes, has been repeatedly suggested. We ask whether that step is possible, using HAS-FL, an adaptive capacity-allocation framework, as a test case. Our findings are threefold. First, validated against ground-truth label-distribution divergence on reproducible partitions, update-divergence estimates of client heterogeneity are dominated by capacity rather than data: across two corrected estimators, multiple datasets, and all seeds, the estimates correlate strongly and negatively with device capacity, and no data signal remains once capacity is controlled for. This previously undocumented confound affects any method estimating client statistics from sub-model updates. Second, adaptive allocation has a hidden failure mode: when every client is capped below full width, the uncovered parameters stay at random initialization and progressively corrupt the global model. A simple coverage guarantee removes the failure and explains why uniform allocation collapses. Third, a matched-budget control settles what adaptivity contributes: random allocation to the same average budget performs no differently on both image benchmarks, and on the naturally partitioned text benchmark the adaptive policy is the weakest of the three strategies while consuming the most capacity. Sub-model training remains valuable because it admits constrained clients at quadratically reduced cost, but what protects accuracy is parameter coverage rather than allocation intelligence. Its apparent benefits come from capacity budgeting and coverage, and future designs need heterogeneity signals separable from capacity effects.

---


### 128. [Edge Sparsification via Temporal Forman-Ricci Curvature for Dynamic Graph Learning](https://arxiv.org/abs/2608.07158)

**<font color=#1a73e8>作者：</font>** Poupak Azad, Cuneyt Gurcan Akcora, Kiarash Shamsi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal graph learning has become essential for analyzing real-world systems whose interactions continuously evolve over time, including financial transaction networks, communication systems, and online social platforms. However, learning from large-scale temporal graphs remains computationally challenging when networks are dense and rapidly changing. To address this limitation, we propose a network-curvature-inspired edge sparsification framework for dynamic graph learning. Our proposed method, TRicci, extends classical Forman-Ricci curvature to directed weighted temporal graphs by capturing structural support, temporal recency, and local interaction competition.
Experiments on 9 transaction networks and 3 temporal graph benchmark datasets demonstrate that the proposed framework preserves predictive performance across multiple graph-level prediction tasks. The results show that TRicci sparsifies temporal graphs by approximately 80% while reducing end-to-end downstream training and inference time by an average of 55.94%, without substantial degradation in predictive performance. Our findings suggest that temporal curvature can serve as a principled basis for scalable temporal graph learning by preserving predictive temporal-structural information under substantial sparsification.

---


### 129. [Fluid-DiT: Graph-Free Diffusion Transformers for Fluid Flow Simulations Learning](https://arxiv.org/abs/2608.07161)

**<font color=#1a73e8>作者：</font>** Shentong Mo, Guolin Ke  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simulating complex fluid flows requires capturing full equilibrium distributions rather than just mean trajectories, yet high-fidelity solvers remain computationally prohibitive. Recent advances, such as Diffusion Graph Networks (DGNs), have combined diffusion models with graph neural networks to sample equilibrium states directly from unstructured meshes, enabling distributional accuracy even from short simulations. However, graph-based diffusion approaches suffer from hand-crafted architectural constraints, limited receptive fields in message passing, and costly multi-scale designs, which restrict scalability to larger and more complex domains. We propose Fluid-DiT, a Graph-Free Diffusion Transformer that replaces graph message passing with attention-based denoising, eliminating explicit graph design while preserving the ability to model distributions of chaotic flows. Our framework introduces a latent-space formulation that disentangles geometric fidelity from distributional learning, reducing high-frequency artifacts and accelerating sampling. By leveraging the transformer's global receptive field, Fluid-DiT naturally captures both local flow structures and long-range correlations without requiring hierarchical graph coarsening. On canonical benchmarks including laminar cylinder wakes, ellipse-flow systems, and turbulent 3D wing experiments, Fluid-DiT consistently outperforms graph-based diffusion baselines in both sample quality and distributional accuracy, achieving higher $R^2$ correlations and lower Wasserstein distances. Moreover, it generalizes robustly from short, incomplete trajectories to unseen Reynolds numbers and geometries, demonstrating strong scalability.

---


### 130. [Representation-driven Endoscopic Visual Embedding Alignment for Latent Generation](https://arxiv.org/abs/2608.07176)

**<font color=#1a73e8>作者：</font>** Francisco Caetano, Tim J.M. Jaspers, Haiko Middeljans 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Developing foundation generative models for endoscopy is limited by the gap between natural and clinical images and the computational cost of training large Diffusion Transformers. Although representation alignment has improved efficiency in general computer vision, its role within the highly specialized endoscopic image space remains unclear. We introduce REVEAL (Representation-driven Endoscopic Visual Embedding Alignment), the largest generative foundation model for endoscopy to date, trained on GastroNet-5M (GN-5M), a multicenter dataset of 5 million endoscopic frames. Instead of depending on out-of-domain priors, REVEAL employs encoders pretrained directly on the endoscopic distribution to align diffusion latents with domain-specific visual features, preserving fine textures and intricate anatomical structures. Beyond image generation, REVEAL also serves as a powerful feature extractor; in multiple benchmarks, it delivers performance that is competitive with, and in several cases exceeds, endoscopic foundation models such as EndoViT and Endo-FM, specifically tuned for classification tasks, while demonstrating strong representation robustness under realistic imaging corruptions. REVEAL produces high-fidelity images and maintains robust structural coherence in latent-space edits such as inpainting and outpainting. This high-capacity backbone lowers the computational threshold for building specialized clinical tools, offering an open, versatile foundation for conditional synthesis, segmentation, and out-of-distribution detection in future intelligent gastroenterology systems.

---


### 131. [Momba: Network Modernization Improves Multi-Objective Reinforcement Learning](https://arxiv.org/abs/2608.07180)

**<font color=#1a73e8>作者：</font>** Adam Štafa, Santeri Heiskanen, Petr Novotný 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in deep reinforcement learning (RL) have shown that improving neural network architectures can yield substantial gains in sample efficiency and asymptotic performance without altering the underlying algorithms. In contrast, work on multi-objective reinforcement learning (MORL), which aims to discover a set of policies that balance trade-offs among conflicting objectives, has predominantly focused on algorithmic innovations, leaving the area of architectures underexplored. While the optimal policies and value functions can differ significantly depending on the trade-offs, MORL algorithms commonly represent them with simple feedforward networks conditioned on the trade-off. This raises the question of whether the performance of the algorithms could be improved with more expressive function approximators. In this paper, we integrate recent advances in neural network design: (i) observation and feature normalization, (ii) weight normalization, and (iii) modeling of distributional returns with an entropy-regularized MORL algorithm. The empirical results across standard continuous control benchmarks demonstrate that these changes substantially improve the quality of the produced solution sets without requiring major changes to the underlying algorithm.

---


### 132. [Conformal Fusion Under Missing Modalities](https://arxiv.org/abs/2608.07183)

**<font color=#1a73e8>作者：</font>** Alireza Moayedikia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal fusion architectures typically assume all modalities are available at inference, yet sensor failures, acquisition variability, and cost constraints routinely produce incomplete observations. Existing work treats modality absence as a prediction-accuracy problem, leaving a more basic question unanswered: whether a model's confidence estimates remain calibrated when an entire input stream is removed. We argue that missing-modality robustness and calibrated uncertainty are a single coupled property, and introduce Modality-Conditioned Conformal Fusion (MCCF), an architecture that addresses both at once. MCCF combines a multimodal bottleneck fusion backbone trained with modality dropout, per-modality evidential heads producing modality-decomposed Dirichlet distributions, and a Dempster-Shafer combination rule that fuses the per-modality evidence into a joint predictive distribution; an absent modality contributes vacuous evidence that is structurally ignored, so the fused uncertainty automatically reflects the reduced information without test-time imputation. A Mondrian conformal calibration module keyed on the modality-presence mask then provides finite-sample group-conditional coverage for every non-empty modality subset. MCCF is, to our knowledge, the first method with formal coverage guarantees under arbitrary modality availability through architectural integration rather than post-hoc recalibration, and the evidential decomposition yields per-modality vacuity scores that localise uncertainty to the absent modality responsible. Across a synthetic problem and three real multimodal benchmarks, MCCF holds its target coverage on every modality-presence subset, substantially narrows the coverage gap between full and partial modalities relative to a marginal split-conformal baseline, and imposes no measurable accuracy cost relative to temperature-scaled and evidential baselines.

---


### 133. [SetEasy: A Multi-Modal Classroom Engagement Assessment and Seating Optimization Framework](https://arxiv.org/abs/2608.07188)

**<font color=#1a73e8>作者：</font>** Zhihao Xie, Hongye Yang, Shien Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> SetEasy optimizes classroom engagement in fixed seating grids. It fuses multimodal sensing (wristband physiology, 4K video, environmental data) and trains a v-Gage model grounded in a revised ISEQ. Each week, two-week engagement forecasts are mapped to a student-seat utility matrix, and CP-SAT generates seating plans under visual-access and social-dynamics constraints. In a four-week deployment (23 students, 331 classes), v-Gage converged across affective, behavioral, cognitive, and overall dimensions, cutting RMSE from 0.75 to 0.53. Optimization raised mean engagement from 0.30 to 0.70, with over two-thirds of seats reaching high engagement and back-row low-activity patterns markedly reduced. These results show that, without hardware changes, interpretable, data-driven seating strategies can substantially enhance engagement. The multimodal "assessment + optimization" paradigm offers a transferable, sustainable path to culturally responsive, differentiated spatial design amid global homogenization.

---


### 134. [MAUPITI: On-Device Prototype-Based Learning on a Smart Infrared Sensor](https://arxiv.org/abs/2608.07192)

**<font color=#1a73e8>作者：</font>** Beatrice Alessandra Motetti, Tanguy Dugas du Villard, Matteo Risso 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-resolution infrared (IR) array sensors represent an interesting solution for privacy-preserving human sensing in embedded systems. In this letter, we describe a smart multi-pixel IR sensor integrating a 16$\times$16 thermal MOSFET (TMOS) array and a RISC-V microcontroller extended with low-precision SIMD instructions, capable of on-device learning and continual adaptation for pose and gesture recognition tasks under tight memory and power constraints ($<$32kB on-chip memory, $\approx$1.5mW). To avoid the memory overheads of backpropagation and replay buffers, we adopt a prototype-based Nearest Class Mean (NCM) classifier in which a simple Convolutional Neural Network (CNN) encoder is trained and quantized offline, while class prototypes are stored and updated on the device in streaming mode. With experiments on two datasets, we show that this approach yields accuracy on par with a conventional classifier, with negligible latency overheads in both the classification and the prototype update ($<$0.29% considering both phases), effectively enabling online adaptation of the perception framework.

---


### 135. [Flow-Corrected Shape Optimization: Taming Manifold Drift in High-Dimensional 3D Models](https://arxiv.org/abs/2608.07199)

**<font color=#1a73e8>作者：</font>** Emilien Seiler, Nicolas Talabot, Yingxuan You 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optimizing 3D shapes within the latent spaces of deep generative models is fundamental to computer assisted engineering, yet remains prone to a critical failure mode we term manifold drift: the tendency of gradient-based optimization to move latent vectors away from the manifold of valid shapes. This problem is exacerbated in state-of-the-art 3D shape generative models that operate in increasingly high-dimensional latent spaces where valid shapes occupy a vanishingly small fraction of the full space. Existing mitigation strategies, including latent regularization and flow-matching approaches, either sacrifice expressiveness, demand a difficult trade-off between objective guidance and generative fidelity that remains prone to manifold drift, or are computationally infeasible to scale to modern, large-capacity 3D shape models. We introduce a novel optimizer-corrector framework that alternates between gradient steps for objective minimization and guided flow matching to drive the latent state back to the valid shape manifold. By decoupling objective minimization from flow-based correction, optimizing freely and correcting strictly, this alternating design avoids inherent trade-offs, preserving geometric validity without sacrificing expressiveness while remaining computationally feasible on modern 3D shape models. We demonstrate its effectiveness across generative priors of varying complexity, from simple vector latent spaces to large-scale architectures across a variety of downstream optimization tasks, including aerodynamic drag reduction and object compliance optimization.

---


### 136. [HNR-DAC: Hard-Negative Reranking and Distribution-Aligned Classification for Scientific Claim Verification](https://arxiv.org/abs/2608.07204)

**<font color=#1a73e8>作者：</font>** Zhenchao Wang, Xin Chen, Luoxi Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific claim verification over a cited paper requires predicting the claim--paper relation and identifying the paragraphs that justify that prediction. This setting poses two linked challenges: within-paper distractors often resemble genuine evidence, while a classifier trained on gold evidence must operate on retrieved evidence at inference. We present HNR-DAC, a two-stage framework that trains each stage on the cases it will actually encounter. Hard-Negative Reranking (HNR) quantifies evidence confusability using a base reranker's scores on non-gold paragraphs and contrasts gold evidence against the most confusable candidates. Distribution-Aligned Classification (DAC) trains on the Top-1 paragraph produced by the same frozen HNR used to construct inference inputs, while HNR's Top-3 paragraph identifiers provide the evidence output. On the NLPCC 2026 Task 10 Track 2, the final configuration obtains 97.21% Hit@3, 95.79% Macro-F1, 94.47% Joint@3, and an average score of 95.13%. The corresponding submission ranks third on the official Track 2 leaderboard while achieving the highest overall Macro-F1 of 93.05%, alongside 70.16% Joint@3 and an average score of 81.61%.

---


### 137. [Beyond the Black Box: Interpretable Models of Human Randomisation Failures](https://arxiv.org/abs/2608.07220)

**<font color=#1a73e8>作者：</font>** Ngoc Linh Dao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixed strategy equilibrium predicts i.i.d play: past actions should not help predict future decisions. Human players, however, systematically depart from this benchmark, and in O'Neill's zero sum card game, these departures can be predicted by black box sequence models such as LSTMs. This paper asks whether that predictive power can be achieved by transparent alternatives that also reveal the behavioural structure behind it. Using 84,060 decisions from 2,802 pairs, the analysis first benchmarks naive and behavioral models against interpretable machine learning and deep learning models, then evaluates the modified EWA specifications of prior work against these benchmarks and uses the LASSO diagnostics to motivate a further nested frequency tracking extension. The results show that repeat or avoid behavior, especially players' management of their own recent action histories, accounts for most of the interpretable and strategically exploitable signal, while frequency tracking adds little out of sample.

---


### 138. [From probability to causality in probabilistic logic programming](https://arxiv.org/abs/2608.07230)

**<font color=#1a73e8>作者：</font>** Zora Wurm, Kilian Rückschloß, Felix Weitkämper  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Probabilistic logic programming is a formalism of statistical relational artificial intelligence that supports causal queries, including interventions from outside the system. When the structure of a probabilistic logic program is learned from data, however, only probabilistic information is used, and a single probability distribution may be compatible with several causal orders. This leads to ambiguity in interventional reasoning, raising the question of when the causal order is uniquely determined by the distribution. Exploiting the relationship between acyclic probabilistic logic programs and Bayesian networks, we derive conditions under which the probabilistic information encoded in a program determines a unique causal order. We also incorporate constraints arising from relational structure by taking into account prescribed sets of causal symmetries induced by the underlying relational vocabulary. The result is a method for verifying when a learned probabilistic logic program supports well-defined intervention semantics.

---


### 139. [CANIS: Generation-Assisted 3D Canonicalization via an Image-Semantic Bridge](https://arxiv.org/abs/2608.07256)

**<font color=#1a73e8>作者：</font>** Kendong Liu, Yuxin Yao, Junhui Hou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Canonicalizing 3D object orientation is fundamental to 3D understanding and analysis. Existing approaches often rely on geometric cues, although 3D canonicalization ultimately requires a semantically meaningful orientation. To address this gap, we propose CANIS, a category-agnostic, generation-assisted framework that introduces the semantic orientation prior of a frozen image-to-3D generative model into 3D canonicalization, without canonicalization-specific training or category-specific templates. Specifically, CANIS first renders the input object from candidate viewpoints, selects an informative view, and generates a proxy in a canonical orientation. During generation, a sparse structural latent encoded from the input guides the proxy to preserve the geometry of an object. CANIS then uses the selected image as a semantic bridge between the input and the proxy. Image patches identify semantic regions on the proxy, and depth back-projection locates the corresponding regions on the input. The resulting semantic anchors constrain geometric matching, from which we estimate the rigid transformation that canonicalizes the input. Experiments on synthetic benchmarks validate CANIS and its key components, while qualitative results on partial observations and OmniObject3D suggest its applicability to incomplete and real-world scans. CANIS also improves downstream 3D classification, part segmentation, and dense correspondence under arbitrary rotations. Project page: this https URL.

---


### 140. [Incidental Visualizations: Augmented Reality as a Medium for Contextual Information](https://arxiv.org/abs/2608.07271)

**<font color=#1a73e8>作者：</font>** Matilde Heitor, João Moreira, Daniel Gonçalves  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In today's fast-paced world, delivering information efficiently and unobtrusively is essential. While ambient and glanceable visualizations provide real-time data, they can increase cognitive load and disrupt primary tasks. We investigate incidental visualizations, a novel concept in information visualization designed to present contextually relevant information briefly and spontaneously, with minimal user interaction. Augmented Reality offers an ideal medium for this integration, embedding visualizations directly within the user's environment. Through controlled user studies on logic-based game tasks (Sudoku and Connect 4), this work compares ambient, periodic, and incidental visualization patterns in terms of comprehension accuracy, performance, and disruption. Results indicate that IVs deliver information as effectively as ambient displays while minimizing disruption, highlighting their potential for adaptive, context-aware information delivery in AR environments.

---


### 141. [TOFD: Target-Oriented Feature Decoupling against Poisoning Attacks in Split Federated Learning](https://arxiv.org/abs/2608.07274)

**<font color=#1a73e8>作者：</font>** Yuhan Xie, Jingrong Huang, Chen Lyu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Split Federated Learning (SFL) facilitates privacy-preserving collaborative training with reduced client-side overhead. However, its split architecture introduces unique attack surfaces, rendering it vulnerable to diverse poisoning attacks. Most existing defenses fail to exploit the split paradigm, limiting their ability to detect and contain malicious behaviors at an early stage. To bridge this gap, we propose Target-Oriented Feature Decoupling (TOFD), a unified framework that jointly enables proactive detection and robust optimization against a wide range of poisoning attacks. TOFD operates in three stages: (1) Target Inference, which identifies potential attack targets by refining class-wise safe zones via class-specific Margin Perturbation (MP); (2) Sample Purification, which adaptively filters poisoned smashed data using thresholds calibrated through cross-class min-max normalization of MP; and (3) Decoupling Optimization, which leverages an adversarial guidance model to capture attack-induced patterns and decouple their influence during optimization, thereby suppressing residual adversarial effects. We provide theoretical guarantees for the convergence of TOFD. Extensive experiments on five datasets demonstrate that TOFD consistently outperforms state-of-the-art defenses under diverse attack scenarios, achieving superior robustness with low computational overhead suitable for practical deployment.

---


### 142. [Why Study Emergent Behavior When You Can Regulate It? Aligning Multi-Agent Systems with Reward Prediction](https://arxiv.org/abs/2608.07280)

**<font color=#1a73e8>作者：</font>** Assaf Caftory, Almog Zemach, Moshe Butman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent simulations are widely used to study complex social and ecological systems, where rich and often unexpected emergent behaviors arise from local interactions. A large body of prior work has focused on analyzing such emergent dynamics across domains. In this paper, we move beyond analyzing emergent behavior and introduce a learning-based mechanism for actively shaping it via social reward modeling. We introduce Multi-Agent Reward Prediction (MARP), a simple framework that extends preference-based reward modeling to multi-agent reinforcement learning. While the framework is designed to be applicable across multi-agent settings, the present empirical validation is limited to a single environment, and we therefore present MARP as a proof of concept within the studied domain. Rather than relying on handcrafted rewards, MARP learns a shared reward model from episode-level evaluations of collective outcomes, enabling decentralized agents to align their behavior with global social objectives.
We study MARP in the Harvest Game, a canonical sequential social dilemma modeling common-pool resource management and related real-world challenges. Our results show that MARP can be tuned to produce behavior that is more closely aligned with target social metrics than standard reward-based baselines, while the learned reward model captures subtle environmental structure without explicit programming. Crucially, MARP supports multiple and composite social objectives within a single training regime. By modifying only the high-level evaluation metric, the same framework seamlessly aligns agent behavior with diverse goals, including sustainability, equality, and peace, as well as combinations of individual and group-level objectives. These findings demonstrate that emergent multi-agent behavior can be treated not only as a phenomenon to study, but as a target of principled, data-driven regulation.

---


### 143. [FUSE: Feature-Wise Unified Specialization with Cross-Column Exchange for Mixed-Type Tabular Flow Matching](https://arxiv.org/abs/2608.07294)

**<font color=#1a73e8>作者：</font>** Suman Cha, Seongchan Lee, Dohyun Ko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating mixed-type tabular data requires jointly modeling diverse feature distributions and their complex cross-column dependencies. Variational flow matching handles distinct endpoints via factorized distributions, yet leaves feature-specific processing and cross-column interactions implicit within a shared backbone. We introduce Feature-wise Unified Specialization with cross-column Exchange (FUSE) to explicitly separate these roles. FUSE applies separate adaptive mixture modules to numerical and categorical features, allowing each feature to combine shared specialized subnetworks, while joint attention preserves information exchange across all columns. We also characterize the excess population risk from restricted conditioning contexts and bound the continuous Wasserstein generation error by endpoint-prediction risk. Comprehensive experiments on eight tabular datasets demonstrate that FUSE achieves strong and consistent performance across distributional fidelity and downstream utility metrics.

---


### 144. [Learning Long-Term Educational Investment Policies under Residential Sorting](https://arxiv.org/abs/2608.07295)

**<font color=#1a73e8>作者：</font>** Honglei Guo, Shuo Chen, Mingjie Bi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Allocating public-school investment effectively and fairly is difficult when school access depends on residence. School improvements can raise nearby housing demand and prices, reshape enrollment, and potentially limit access for lower-income households. These effects evolve as residential sorting changes school composition, quality, and future investment needs. Existing approaches often study school funding, household choice, and housing markets separately, while static models can miss their interconnected, long-term effects. We address this gap with a dynamic multi-agent framework that links government investment, household sorting, housing prices, population turnover, enrollment, and evolving school quality. A government planner uses reinforcement learning (RL) to identify multiyear allocation policies that account for household responses while balancing aggregate educational access and equity. In simulations, our RL-based policy attains the highest access level (0.4780) and second-lowest access Gini coefficient (0.0164) among representative baselines, demonstrating a favorable effectiveness-equity balance. The results also indicate reduced socioeconomic stratification in educational access. By making education-housing feedback explicit, our framework supports long-term analysis of how school investment shapes educational opportunity over time.

---


### 145. [EliSeg: Verified Target Construction for Report-Grounded Abnormality Segmentation](https://arxiv.org/abs/2608.07299)

**<font color=#1a73e8>作者：</font>** Chengyi Peng, Haoyu Yang, Meixing Shi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiology reports describe clinical observations but do not specify executable segmentation targets. They may contain present, negated, prior,uncertain, or irrelevant findings, while multiple valid abnormalities may coexist. Existing segmentation methods largely bypass this ambiguity by receiving a target identity or spatial prompt before inference, which acts as a hidden target oracle. We study report-grounded abnormality segmentation, where a model must determine target eligibility, cardinality, and finding-to-mask correspondence directly from an unfiltered report before delineating the corresponding regions. We propose \textbf{EliSeg}, an atcor--verify--revise framework that integrates target construction with mask generation. A grammar-constrained Actor proposes target slots and masks, an independent text-only Verifier reconstructs the eligible finding inventory, and Revision selectively re-executes the shared Actor when their target structures disagree. EliSeg requires no predefined target identity, finding prompt, point, or bounding box. Experiments on MIMIC-CXR-ILS show that EliSeg consistently outperforms direct segmentation methods and extract-then-segment cascades across findings, while effectively suppressing masks for ineligible report mentions. Ablation studies confirm the complementary roles of verification and revision, and evaluation on CheXlocalize demonstrates effective transfer of the EliSeg to an external this http URL is available at this https URL.

---


### 146. [From Optimal Actions to World Models: Identifiability of Transition Kernels in Discounted MDPs](https://arxiv.org/abs/2608.07301)

**<font color=#1a73e8>作者：</font>** Neal Batra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study what can be recovered about the transition probabilities of a Markov decision process from optimal actions alone. This is closely related to the inverse problem considered by Letcher et al., who ask when the dynamics can be recovered from numerical \(Q\)-values. Here the numerical values themselves are not observed; only the optimal actions are known, for every reward in a given class.
For state-action rewards \(r(s,a)\), knowing the optimal actions for every reward also tells us how much better one action is than another when each is followed by the same fixed policy. This is still not enough to determine the transition probabilities uniquely. We prove that two kernels give the same optimal actions for every reward exactly when \[ Q_{s,a} =
\Bigl(P_{s,a}+\tfrac1\gamma e_s^{\mathsf T}(L-I)\Bigr)L^{-1} \] for one invertible matrix \(L\) satisfying \(L\mathbf 1=\mathbf 1\). Near a kernel with strictly positive entries, there is an \(n(n-1)\)-dimensional family of different kernels with this property. The result is unchanged if we consider only rewards having a unique optimal action at every state.
We then compare this with rewards of the forms \(r(s)\) and \(r(s,a,s')\). Rewards that depend on the next state can usually recover the transition kernel itself: every row at a state with at least two actions is determined, and we describe exactly when a row at a state with one action can remain hidden. State rewards reveal less: two kernels give the same optimal actions exactly when every deterministic policy is optimal for the same set of rewards. The results show how the form of the reward affects what can be learned about the dynamics from optimal actions alone.

---


### 147. [Winning by Peeking: Unenforced Budgets and Test-Set Selection Inflate Short-Budget AutoML Comparisons](https://arxiv.org/abs/2608.07303)

**<font color=#1a73e8>作者：</font>** Guilin Zhang, Kai Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Comparisons between AutoML systems at short time budgets -- tens of seconds rather than hours -- are common in tool READMEs and workshop papers, and they are easy to get wrong. We report a case study in which a simple AutoML engine, Orcetra, appeared to beat FLAML and AutoGluon on 513 OpenML datasets, winning 57.1% of them at a nominal 60-second budget and 78.4% of datasets against FLAML alone at 30 seconds. Both margins came from protocol defects that a results table cannot show. The search loop scored every candidate on the test split and reported the best, making the headline metric a maximum over dozens of noisy estimates while the baselines selected on training data and touched the test set once; and the budget was checked before launching a candidate but never enforced during one, so the system consumed a median of 120 s against a 60-second budget, 2.24x the wall-clock AutoGluon used. Re-running with selection moved to a validation split, the deadline enforced externally and every framework pinned to an equal share of the machine, Orcetra's win rate on the re-run subset falls from 59.4% to 34.3% and no pairwise difference against either competitor remains significant. Recording both estimands inside a single search lets us attribute the collapse: the selection rule accounts for 4.8 percentage points and unequal compute for most of the rest. The same traces give the selection bias as a function of budget, measured rather than assumed: it grows with $K$ but reaches only 0.27 accuracy points, about five times below the $\sigma\sqrt{2\ln K}$ bound a marginal-standard-error argument predicts, because candidates scored on shared test rows cancel most of the noise. We close with a checklist for short-budget comparisons. Code, per-dataset results and the scripts that regenerate every number and figure in the paper are released with it.

---


### 148. [When GNNs Fail: Quantifying and Overcoming Temporal Correlation Volatility in Time Series](https://arxiv.org/abs/2608.07333)

**<font color=#1a73e8>作者：</font>** Chen Shao, Yue Wang, Zhenyi Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modeling multivariate time series by representing them as graphs, where individual series act as nodes and pairwise temporal corre- lations serve as edges, has gained significant traction. Recent advances in Graph Neural Networks (GNNs) have demonstrated strong perfor- mance by assuming a static graph topology and aggregating information from neighboring series. In this work, we investigate the representa- tional power of GNNs for forecasting under both static and dynamic settings (i.e., when pairwise correlations evolve drastically over time) and identify critical limitations in current architectures. To formalize this, we first propose Temporal Correlation Volatility (TCV), a model- agnostic metric designed to quantify the distributional evolution of these latent structures. We establish a clear connection between TCV and performance degradation, demonstrating that many popular models, including Transformers, generalize poorly in high-TCV settings and are often outperformed by simple structure-agnostic baselines. To address these limitations, we propose Graph Layer for Inference in Dynamic En- vironments (GLIDE), a novel GNN layer enhanced by two theoretically grounded design mechanisms: (D1) Path-based Message Passing, which captures path-based neighborhoods and (D2) Static and Dynamic Propagation Separation, which identifies optimal dynamics via local static approximation. These components significantly improve learning under dynamic topology while preserving robustness in static scenarios. Ex- tensive experiments on synthetic and real-world benchmarks show that GLIDE improves average performance by up to 45.6% across static and dynamic settings, with the largest gain reaching 85.7%. The source code is available at this https URL.

---


### 149. [Aftab: A Comprehensive Benchmark of CNN Encoders and Advanced Value Functions in Parallelized Q-Networks](https://arxiv.org/abs/2608.07335)

**<font color=#1a73e8>作者：</font>** Taha Shieenavaz, Shabnam Zareshahraki, Loris Nanni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advancements in deep reinforcement learning have increasingly favored simplified, highly parallelized paradigms. Notably, the Parallelized Q-Network (PQN) algorithm achieves stable off-policy learning without relying on computationally expensive replay buffers or target networks. However, the representational capacity and parameter efficiency of visual encoders operating in these buffer-free settings remain underexplored. In this work, we systematically investigate the architectural design space of Convolutional Neural Networks for PQN. We design and rigorously evaluate eight distinct CNN topologies, optimizing for sample efficiency under strict parameter constraints. Furthermore, we study the impact of representation and value estimation enhancements by integrating the Hadamax encoding paradigm and advanced Q-learning extensions, including distributional, ensemble, and dueling heads. Extensive experiments on the Atari-57 benchmark demonstrate that our proposed composite architecture, Aftab, achieves an Interquartile Mean (IQM) Human-Normalized Score of 6.479, establishing a 0.86 Probability of Improvement over the standard PQN baseline. Additionally, structural resilience evaluations on the highly non-stationary Procgen Hard benchmark confirm out-of-distribution generalization, with Aftab yielding an IQM Procgen Normalized Score of 0.418 compared to the baseline's 0.382. Ultimately, this work establishes an efficient, probabilistically superior structural reference for model-free reinforcement learning, all while preserving the simplicity and memory efficiency of unbuffered, parallelized optimization.
The complete Aftab framework, including all model definitions, training configurations, and raw experimental logs, is open-sourced and available on our GitHub repository: this https URL

---


### 150. [H2AL: Hyperbolic Hierarchy-aware Aggregative Learning for Registration-based Few-shot Medical Image Segmentation](https://arxiv.org/abs/2608.07340)

**<font color=#1a73e8>作者：</font>** Jia Wang, Jiaming Cai, Zunying Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Registration-based Few-shot medical image segmentation (RFMIS) aims to generate pseudo-labels for unlabeled images by warping a labeled image through registration. However, existing methods primarily perform pixel-level optimization and inference in Euclidean space, treating anatomical structures as flat and disjoint. This neglect of inherent hierarchies degrades pseudo-label quality and weakens the discrimination of ambiguous regions, limiting the segmentation performance. To overcome this challenge, we propose a Hyperbolic Hierarchy-aware Aggregative Learning framework for RFMIS, termed H2AL, that enhances both deformation plausibility and anatomical discrimination for dual-task learning. Specifically, we introduce a Hyperbolic Hierarchy-aware Infusion (H2I) module, which leverages the hierarchical modeling capability of hyperbolic space to learn precise hierarchy-aware representations via transformation-guided supervised hyperbolic contrastive learning, and injects such hierarchical priors into Euclidean space through a gated infusion block while preserving semantic richness. Furthermore, we propose an end-to-end joint optimization algorithm by gradient aggregation, where the gradients from the registration and segmentation decoders, embedding semantic and hierarchical cues, are aggregated to update the shared encoder to promote collaborative learning across tasks. Extensive experiments on two anatomical regions, with five experimental settings, demonstrate the effectiveness and efficiency of our method in both registration and segmentation. The code is publicly available at this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-167](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
