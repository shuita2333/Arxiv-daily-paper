# 📦 其他研究 | 2026年07月29日

> 本类共 **442** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-442](./part-09.md)

---

### 351. [There Will Be Spam: Characterizing State-Invariant Transactions and Speculative MEV](https://arxiv.org/abs/2607.24172)

**<font color=#1a73e8>作者：</font>** Vabuk Pahari, Johnnatan Messias, Christof Ferreira Torres  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blockchains rely on transparency and immutability to ensure trust, but these guarantees come at the cost of an ever-growing ledger that increasingly threatens decentralization by making it more expensive to store and maintain the full transaction history. In this work, we introduce state-invariant transactions, defined as transactions whose inclusion or removal does not affect the resulting blockchain state beyond transaction fees. We argue that these transactions constitute a form of on-chain spam because they consume execution, bandwidth, storage, and blockspace without contributing to the final ledger state. We present the first large-scale measurement of state-invariant transactions across Ethereum, Optimism, and Base, identifying nearly 1.4 billion such transactions. While only 2.6% of Ethereum transactions are state-invariant, they account for 24% of transactions on Optimism and 37% on Base, representing a significant source of unnecessary resource consumption on Layer-2 blockchains. We show that speculative Maximal Extractable Value (MEV) is the dominant source of state-invariant transactions on Optimism and Base, accounting for 57% and 68%, respectively, but is not the only source as previously assumed. Moreover, despite its popularity, speculative MEV is not the most profitable strategy once the costs of state-invariant transactions are considered. Beyond MEV, we identify substantial malicious activity, with address poisoning campaigns accounting for 53% of non-reverted state-invariant transactions on Ethereum. Our findings suggest that mitigating state-invariant transactions could substantially reduce blockchain resource consumption and transaction costs while limiting phishing campaigns and other forms of blockchain abuse.

---


### 352. [Where Quality Breaks in Compressed Short-Text Generation: Staged Bottleneck Localization](https://arxiv.org/abs/2607.24176)

**<font color=#1a73e8>作者：</font>** Alexey Gavrilov, Alan-Barsag Gazzaev, Sergey Muravyov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Compressed short-text generators can fail in two different places: the codec may discard information before generation starts, or the latent generator may produce weak codes. Without separating these failure modes, researchers can spend compute improving the wrong component. We study this problem in a controlled 64-to-16 TinyStories case study built from a hierarchical VQ-VAE-2 codec and a masked discrete diffusion generator (MDLM). We use a staged validation protocol that separates codec reconstruction fidelity, latent generation quality, and auxiliary latent diagnostics under one shared external GPT-2 scorer, while reporting complementary semantic metrics for the geometry study. In the tested configuration, codec reconstruction alone raises median external perplexity from 15.17 to 27.36 (+80.4%) and p95 from 25.10 to 98.91 (+294.1%), showing that the dominant quality loss appears before latent generation begins. Under the same scorer, code-space MDLM remains materially stronger than token-space diffusion, reducing mean, median, and p95 by 32.9%, 30.9%, and 36.6%, respectively. Geometry-aware regularization improves local latent proxies but does not improve decoded-text metrics in the available runs. The contribution is methodological rather than algorithmic: the paper presents a reusable staged diagnosis for one concrete pipeline and shows that, in this setting, codec fidelity rather than latent denoising sets the practical quality ceiling.

---


### 353. [EXE-Bench: Ranking the Tradeoffs of AI-based Windows Malware Detectors for Real-World Usability](https://arxiv.org/abs/2607.24177)

**<font color=#1a73e8>作者：</font>** Andrea Ponte, Daniel Gibert, Matous Kozak 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Due to the lack of systematic evaluations, we are not yet able to determine which AI-based Windows malware detector to deploy in production, since existing evaluations (i) differ in terms of data used for both training and testing; (ii) do not consider temporal analysis to showcase whether models withstand the passage of time; (iii) avoid security evaluations with adversarial attacks that could highlight their brittleness against content-injection attacks; and (iv) neglect the computational requirements for deployment, risking slow inference on endpoints. For these reasons, we develop EXE-Bench, a comprehensive benchmark of AI-based Windows malware detectors. EXE-Bench assesses performance, temporal and adversarial robustness, and computational overhead, aggregating them into a single score for direct and fair model comparison. Through EXE-Bench, we highlight how evaluations conducted only after deployment are suboptimal and unable to provide a complete picture of their performance. In particular, through our analysis, we remark how much domain knowledge instilled through feature engineering is still extremely useful in this domain, resisting both time and adversarial attacks, in stark contrast with most of the deep networks that only excel right after deployment.

---


### 354. [Monitoring Post-Disaster Urban Recovery Using High-Resolution SAR Time Series and Unsupervised Learning: Evidence from the 2023 Türkiye-Syria Earthquake](https://arxiv.org/abs/2607.24180)

**<font color=#1a73e8>作者：</font>** Luigi Russo, Deodato Tapete, Silvia Liberata Ullo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Monitoring post-disaster recovery is essential for understanding how urban systems rebuild and progressively return to functionality. However, tracking reconstruction remains difficult because reliable ground-truth information is often scarce and recovery processes evolve over time. This paper proposes an unsupervised framework for recovery monitoring based on multi-temporal synthetic aperture radar (SAR) observations and deep-learning anomaly detection. COSMO-SkyMed time series are used to identify persistent temporal anomalies associated with reconstruction activities and to generate spatially explicit recovery maps. The framework is applied to four cities severely affected by the 2023 Turkiye-Syria earthquakes, revealing heterogeneous reconstruction dynamics across different urban contexts. The results show spatially structured patterns of persistent anomalies related to reconstruction over damaged and cleared areas, temporary container settlements, and new residential districts. Comparison with nighttime-light recovery indicators derived from SDGSAT-1 data highlights the complementary nature of the two modalities: nighttime lights reflect the restoration of electricity supply and nighttime socioeconomic activity, whereas SAR anomalies capture structural changes in the built environment and may reveal reconstruction at earlier stages. The results demonstrate that multi-temporal SAR data combined with unsupervised learning provide an effective and scalable approach for monitoring post-disaster reconstruction when labeled recovery datasets are unavailable.

---


### 355. [LCMamNet: A Lightweight Cross-scale Mamba Network for Infrared Small Target Detection](https://arxiv.org/abs/2607.24184)

**<font color=#1a73e8>作者：</font>** Yuhao Fan, Le Hui, Yuchao Dai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared small target detection (IRSTD) is important for low-altitude perception, unmanned-system warning, and security monitoring. However, weak targets in infrared imagery usually occupy only a few pixels and are easily submerged by cloud clutter, ground edges, and bright noise, making it difficult for lightweight segmentation-based methods to preserve local target structures while suppressing background interference. To address these challenges, we propose LCMamNet, a lightweight cross-scale Mamba network that progressively enhances local target structures, interacts cross-scale context in a latent space, and restores spatial details with background suppression. Specifically, a compact hierarchical encoder with cross-shaped directional bottleneck residual (CDBR) blocks strengthens direction-sensitive target structures under a small computation budget. A latent dense cross-scale fusion (LDCF) module then performs dense all-level interaction through bidirectional Mamba modeling and reorganizes the interacted features into stable hierarchical semantics. Finally, a progressive decoder selectively recovers shallow spatial details while suppressing irrelevant background textures. Extensive experiments on IRSTD-1k, NUAA-SIRST, and NUDT-SIRST show that the proposed network achieves mIoU scores of 71.25\%, 79.60\%, and 95.58\%, respectively, with only 1.175M parameters and 6.91 GFLOPs. It also runs with a mean inference latency of 6.62 ms, and deployment results on an NVIDIA Jetson Orin NX 16G SUPER further demonstrate its practical potential for real-time edge inference. The code and checkpoints are publicly available at this https URL.

---


### 356. [Myopia Prevention and Control 3.0: Artificial Intelligence--Driven Risk Stratification, Proactive Monitoring, and Personalized Intervention](https://arxiv.org/abs/2607.24187)

**<font color=#1a73e8>作者：</font>** Tieniu Wang, Cangzhu Huang, Qianhui Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The convergence of artificial intelligence (AI), digital sensing, and ubiquitous computing has created an unprecedented opportunity to transform myopia prevention from a reactive, population-based model into a proactive, precision-driven one. Despite evidence that half the world's population will be myopic by 2050, conventional approaches---school-based vision screening (Phase 1.0) and evidence-based risk factor management (Phase 2.0)---have proven insufficient. We review the emergence of Myopia Prevention and Control 3.0, defined by AI integration across three interconnected domains forming a closed-loop pipeline: (1) AI-driven risk stratification predicting individual-level risk through machine learning on multimodal data; (2) AI-enabled proactive monitoring via wearables, smartphones, and school screening networks; and (3) AI-powered personalized intervention with closed-loop feedback. We critically evaluate evidence across each stage, discuss challenges in data quality, model validation, ethics, and equity, and outline future directions including multimodal foundation models, digital twins, and causal machine learning.

---


### 357. [Effect of User-Prompted Priors on Semi-Automated Cancer Lesion Segmentation in Whole-Body Computed Tomography](https://arxiv.org/abs/2607.24210)

**<font color=#1a73e8>作者：</font>** Isac Stark, Johan Öfverstedt, Elin Lundström 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In clinical oncology studies, metastatic cancer is commonly evaluated using "Response Evaluation Criteria in Solid Tumors" (RECIST), in which the diameter of up to five lesions is measured and followed over the course of treatment. However, RECIST shows limited correlation with overall survival. Total tumour volume (TTV) is a stronger predictor but typically relies on manual ground-truth segmentation of all lesions, which is time-consuming and requires expert domain knowledge. Semi-automated approaches leveraging user-prompted priors, such as bounding boxes and single-slice contours, as inputs to automated segmentation methods can facilitate the generation of ground-truth segmentations. This work investigates the impact of different user-prompted priors on semi-automated cancer lesion segmentation performance in whole-body computed tomography. Across 3-fold cross-validation and external testing, more complex spatial priors consistently improved performance, with contour priors from three orthogonal planes (axial, coronal and sagittal) achieving the best results. On the external test (n=3865 lesions), this approach achieved a mean Dice score of 0.882, compared to a mean Dice score of 0.671 for the baseline model with no spatial prior. These findings suggest that the use of multi-plane orthogonal user-prompted priors can improve semi-automated tumour lesion segmentation and support efficient generation of high-quality volumetric ground-truth data.

---


### 358. [Integrating Factual and Normative Industrial Knowledge via Constraint-Aware Graph Attention for Process Plan Recommendation](https://arxiv.org/abs/2607.24213)

**<font color=#1a73e8>作者：</font>** Yuntong Chen, Yingqi Li, Yingying Xiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Integrating heterogeneous industrial knowledge, including factual relations and decision constraints, remains a core challenge in industrial information systems. Machining process planning exemplifies this problem because engineers must select operations by combining material properties, feature characteristics, and quality requirements. Existing methods rely mainly on similarity retrieval or classification, without a unified ranking objective or standardized evaluation. We propose PCA-GAT, which formulates machining process plan recommendation as a knowledge graph enhanced collaborative filtering problem. Bayesian Personalized Ranking provides the learning objective, while Recall@K and NDCG@K define evaluation. The knowledge graph supplies semantic structure when collaborative signals are sparse. Four domain constraints, material compatibility, precision requirements, feature applicability, and operation sequencing, are introduced as attention biases during graph propagation. Type-specific weights learn their importance, and an adaptive gate adjusts their influence using local context. On a real aerospace dataset with 115 parts and 507 plans, PCA-GAT achieves Recall@1 = 0.9087 and strong cold-start robustness, with about half the degradation of the strongest baseline under severe sparsity. Ablation studies show that knowledge graph enrichment is essential, constraints add value, and ungated constraint injection can hurt performance. The learned weights identify material-operation compatibility as the dominant factor, consistent with domain expertise. Results on three public benchmarks show no degradation when constraints are absent, supporting generalization beyond manufacturing. This study establishes a standardized recommendation protocol for engineering process planning and benchmarks seven methods across three categories, showing that knowledge representation is the main bottleneck.

---


### 359. [TreeAdapter: Hierarchical Taxonomy-Guided Adapter Composition for Fine-Grained Species Image Generation](https://arxiv.org/abs/2607.24215)

**<font color=#1a73e8>作者：</font>** Yuze Sun, Zhongjie Duan, Yingda Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although general text-to-image models excel in open-domain generation, their performance degrades significantly in specialized downstream domains, particularly when generating images of rare biological species. Hindered by long-tailed distributions, general models struggle to capture subtle fine-grained details, while per-species fine-tuning methods over-isolate individual species and consequently ignore the shared visual features among closely related taxa. To address this, we propose TreeAdapter, a novel framework that explicitly leverages hierarchical taxonomic data. Rather than using a monolithic model or independent per-species modules, TreeAdapter attaches lightweight adapters to every node of the taxonomic tree. Specifically, leaf-node adapters capture species-specific visual traits, while internal-node adapters encapsulate shared semantics among descendant taxa. We introduce a two-stage training paradigm where ancestor adapters are optimized to model only the residual visual features unexplained by their descendants. This model architecture and training paradigm enable the model to fully leverage hierarchical information, ensuring the accurate generation of visual features for each species. Extensive experiments across three large-scale biodiversity benchmarks demonstrate that TreeAdapter achieves state-of-the-art fine-grained generation quality, outperforming both general-purpose and domain-specific baselines.

---


### 360. [Every Client Is an Environment: Federated De-confounding for Spatio-Temporal Forecasting](https://arxiv.org/abs/2607.24218)

**<font color=#1a73e8>作者：</font>** Qingxiang Liu, Anqi Liang, Heng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning has emerged as a promising paradigm for spatio-temporal forecasting (STF), enabling collaborative model training without sharing raw observations. Existing federated STF methods primarily regard cross-client heterogeneity as an optimization challenge and mitigate it through personalized approaches. However, such heterogeneity fundamentally stems from diverse \emph{environmental conditions}, and these methods capture environment-specific forecasting patterns, hardly generalizing under environmental shifts. Our key insight is that the environmental diversity across federated clients should be exploited, as they provide \emph{complementary observations of the same underlying spatio-temporal system}. Based on this insight, we propose \method, a novel federated de-confounding framework that \textbf{treats clients as distinct causal environments}. \method leverages the client heterogeneity as distributed environmental evidence and learns a global prototype codebook to capture shared environmental regimes. We further derive a theoretical federated de-confounding bound that is linearly controlled by the averaged confounding strength. Extensive experiments demonstrate that \method consistently outperforms federated baselines, while providing transferable, interpretable, and communication-efficient environmental representations.

---


### 361. [MATS: A novel multi-modality multi-task learning framework for 3D perception in autonomous driving](https://arxiv.org/abs/2607.24224)

**<font color=#1a73e8>作者：</font>** Junchen Huo, Wanming Hao, Song Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modality data from different sensors provides rich complementary information for 3D perception, becoming an essential component in reliable autonomous driving systems. Current research typically designs intricate and complex fusion strategies to integrate information from multimodal data on a unified bird's-eye-view (BEV) feature map for the joint learning of multiple perception tasks. However, such a single feature map hardly carries sufficient information to simultaneously meet the requirements of various perception tasks, leading to a very limited perception performance. To mitigate this limitation, this paper proposes MATS, a novel multi-modality multi-task learning approach with modality-adaptive BEV fusion and task-specific Mixture-of-Experts (MoE) for 3D perception. Specifically, a simple modality-adaptive BEV fusion module is designed to adaptively recalibrate the BEV features by modeling the global cross-modality dependencies, generating diverse BEV feature maps for various perception tasks. For joint multi-task learning, this paper proposes a task-specific MoE module to decouple the tasks and enable the network to automatically choose the appropriate BEV feature candidates for each specific task. To validate the effectiveness of the proposed approach, we conduct extensive experiments on the large-scale benchmark nuScenes. With the camera- and LiDAR-modality input data, the proposed approach outperforms the state-of-the-art (SOTA) by a significant margin. Furthermore, the experimental results on the single tasks show that the proposed approach significantly outperforms the baselines. The code and trained models will be available upon publication.

---


### 362. [CAGE: Cognitive Attribution Graphs for Faithful Inline Citation Generation in Long-Form Question Answering](https://arxiv.org/abs/2607.24236)

**<font color=#1a73e8>作者：</font>** Zhichao Yan, Shizhao Li, Jiapu Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-form question answering increasingly relies on retrieved evidence to make LLM outputs verifiable, with inline citations tracing claims to source documents. However, existing systems often attach citations that are topically related but insufficient to support their claims. We identify attribution ambiguity as a structural challenge: end-to-end generation must implicitly resolve combinatorial claim--document assignments, obscuring evidential boundaries and increasing the risk of evidence-boundary overrun, where claims exceed cited support. To address this challenge, we propose CAGE (Cognitive Attribution Graphs for Citation Generation), a two-stage framework that introduces an explicit cognitive attribution map before answer generation. CAGE first trains a plug-and-play Cognitive Map Induction Model to construct answer-centered support subgraphs, aligning each semantic answer unit with supporting documents through explicit relations. A Structured Citation Reasoning Model then realizes these units as sentence-level claims with map-aligned citations. Experiments on ASQA, ELI5, and ExpertQA show that CAGE achieves state-of-the-art performance, demonstrating the effectiveness of attribution-space contraction and map-guided citation generation.

---


### 363. [Why does Greedy Search produce Optimal Clustering Outcomes? A Fixed-Core Assignment Theory](https://arxiv.org/abs/2607.24237)

**<font color=#1a73e8>作者：</font>** Kai Ming Ting, Kaifeng Zhang, Sanjay Chawla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many existing clustering methods are designed based on a set-oriented definition---a cluster is a set of similar points---relying a point-to-point similarity function to find similar points. This works well for compact clusters, but clustering performance can deteriorate badly when cluster shapes are irregular, and densities or sizes vary between clusters. Recent `Cluster-as-Distribution' (CaD) clustering has been shown to discover these generic types of clusters in practice by treating each cluster as a set of independent and identically distributed points generated from some unknown distribution via a greedy search, achieving a clustering objective equivalent to that of Spectral Clustering, but with better clustering outcomes without eigen-decomposition. However, a theoretical analysis of this phenomenon is still lacking. Our analyses are from two angles. First, we analyze the approximation error between the true and empirical distribution embeddings. Second, we show that the greedy search employed to achieve the CaD clustering objective can be mapped to a partition matroid---yielding greedy optimality. These yield a near-optimality guarantee for the CaD clustering objective, with regret controlled by the approximation error. This is the first analysis that explains why CaD clustering via greedy search can discover clusters of arbitrary shapes, densities and sizes (where all set-oriented clustering methods have failed to discover) when the estimated cluster embeddings faithfully approximate the underlying cluster distributions.

---


### 364. [FilmBench: A Film-Grade Benchmark for Cinematic Video Generation](https://arxiv.org/abs/2607.24241)

**<font color=#1a73e8>作者：</font>** Shengyi Wang, Niantong Li, Guangzheng Hu 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Progress in video generation keeps narrowing the visual gap between AI-generated and professionally produced footage, yet most benchmarks still draw prompts from web sources or LLM templates and score them with untrained, generic multimodal models. More fundamentally, their evaluation taxonomies remain rudimentary (overall visual quality, coarse text alignment and temporal smoothness) rather than the professional Cinematic Language criteria by which films are actually made and judged, so they assess basic video plausibility rather than film-grade craft. We introduce FilmBench, a text-to-video (T2V) and reference-to-video (R2V) benchmark grounded in the professional Cinematic Language of the film- academy tradition and co-developed with directors and faculty from the Beijing Film Academy and the Hujing Digital Media & Entertainment Group film studio. It rests on three choices. First, prompts are reverse-engineered from clips of award-winning films spanning 20 cinematic genres and chosen by professional directors, so every prompt is anchored to a verified live-action reference; the prompts follow real shot lists, and most script multiple shots (1,056 of the 1,169 prompts are multi-shot), unlike prior single-clip benchmarks. Second, evaluation follows a three-level Cinematic taxonomy of 3 axes, 12 components and 35 (T2V) +3 (R2V-only) sub-metrics. Third, we develop an in-house expert-grade automatic evaluation agent and open-source its core suite of Cinematic Language operators (FilmOps). Benchmarking leading video generation models (9 for T2V, 7 for R2V), the evaluator reproduces the human model ranking at model-level Spearman \r{ho} = 0.95 (T2V) and 0.96 (R2V). Scores fall well below prior web-style benchmarks, with two consistent gaps in dynamic aesthetics and a marked single- to multi-shot performance drop that widens for weaker models.

---


### 365. [SILICA: Repurposing Diffusion Priors for Joint Glass Segmentation and Depth Estimation](https://arxiv.org/abs/2607.24249)

**<font color=#1a73e8>作者：</font>** Tarun R, Anuj Verma, Laksh Nanwani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard depth sensors systematically fail on transparent surfaces, creating corrupted 3D maps and severe navigation hazards. While specialized hardware sensors can detect glass, they lack modularity and have extensive hardware dependencies. Consequently, learning-based monocular depth estimation has emerged as a compelling alternative. However, domain-specific glass-aware monocular depth estimators struggle with unfamiliar indoor layouts; restricted by the severe scarcity of real-world glass depth annotations, they fail to generalize zero-shot to new settings. This motivates us to explore whether the extensive priors of text-to-image diffusion models can enable generalizable perception of transparent surfaces. We introduce SILICA, a unified pipeline leveraging these priors to jointly predict glass segmentation and glass-aware depth. This mutual information exchange establishes a robust spatial hierarchy, entirely eliminating the need for paired real-world glass depth annotations. Subsequently, we use the predicted segmentation mask to explicitly filter incorrect glass depth points from standard sensors, recovering accurate metric glass depth for downstream 3D mapping and autonomous collision avoidance. Supported by our novel Mirage 18k dataset, extensive experiments demonstrate that SILICA achieves remarkable zero-shot transfer across diverse, unseen environments, outperforming state-of-the-art models by almost 20% and setting a new benchmark for transparent surface perception.

---


### 366. [ML-based Predictive Models for Power Consumption in Virtualised O-RANs](https://arxiv.org/abs/2607.24256)

**<font color=#1a73e8>作者：</font>** Rishu Raj, Genevieve Akude, Urooj Tariq 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As communication networks adopt virtualized and disaggregated architectures, achieving energy efficiency has become increasingly important for both economic and environmental reasons. Traditional methods for power modeling are inadequate in these dynamic software-defined environments due to their inability to model complex and nonlinear factors affecting energy use. We investigate the use of feature extraction and regressor-based machine learning methods for predicting power consumption in virtualized open radio access networks (O-RANs), utilizing datasets from a hardware-instrumented testbed. We test three variants of deep neural networks (DNNs), namely, a standard DNN, a regularized DNN, and a hybrid model combining DNN-based feature extraction with an XGBoost regressor. We evaluate the performance of these models for various system parameters such as transmission gain, modulation/coding schemes, and airtime. We show that the hybrid model consistently outperformed others, achieving a mean relative error below 0.5%. Results suggest hybrid models like DNN-XGBoost offer superior accuracy and could be integrated into O-RAN management tools to enable more energy-efficient network orchestration in future networks.

---


### 367. [Physics-Guided Generative AI for Property-Targeted 3D Porous Media Design](https://arxiv.org/abs/2607.24274)

**<font color=#1a73e8>作者：</font>** Peng Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inverse design of three-dimensional porous media is central to applications in filtration, catalysis, energy storage, fuel cells, thermal management, and biomedical scaffolds, but remains challenging because many distinct pore geometries can share similar porosity or permeability while small structural changes can strongly affect transport behaviour. This paper proposes a physics-guided generative AI framework for property-targeted porous media design, combining a property-aware variational autoencoder, a conditional latent diffusion model, and an independently trained differentiable structure-to-property surrogate. The framework learns a compact, physically informative latent design space, generates porous structures conditioned on target porosity and directional permeability, and refines generated samples using property-level feedback during denoising and decoding. Experiments on procedurally generated structures and real micro-CT porous-media datasets show improved target-property matching, directional permeability control, and property correlation compared with representative property-aware variational-autoencoder and latent-diffusion baselines. The results demonstrate a scalable route towards controllable inverse design of complex porous geometries and establish a foundation for simulation-informed generative AI tools in engineering and advanced materials discovery.

---


### 368. [Superpixel-Based QUBO for Scalable Quantum-Enhanced Medical Image Segmentation](https://arxiv.org/abs/2607.24288)

**<font color=#1a73e8>作者：</font>** Mohammad Chalhoub, Mahdi Chehimi, Laia Domingo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quadratic unconstrained binary optimization (QUBO) has emerged as a powerful framework for medical computing problems. Binary decision variables naturally represent clinical choices, making QUBO formulations well-suited for quantum annealing hardware. However, a fundamental scalability challenge limits practical deployment: problem size grows rapidly with input dimensionality, creating computational bottlenecks that restrict applications to simplified scenarios. This paper addresses this challenge through hierarchical problem reduction, as demonstrated in medical image segmentation, where pixel-level QUBO formulations create over 65,000 variables for a 256x256 image, forcing existing approaches to downsample to 42x42 resolution and discard 97% of pixel information. A superpixel-based QUBO framework is proposed using simple linear iterative clustering (SLIC) to group pixels into perceptually meaningful regions, then formulate segmentation as QUBO over a region adjacency graph (RAG) combining min-cut and smoothness objectives. Validation on INbreast mammography breast cancer images demonstrates a 4.2% improvement in segmentation quality (mean IoU 0.76 vs 0.73) with 33 computational speedup (0.67s vs 21.97s) and a 97.3% reduction in problem size (1764 to 48 variables), all achieved while processing full-resolution images rather than downsampled versions. The reduced problem size also fits well within current quantum annealer connectivity limits, removing the embedding overhead that has historically blocked direct deployment of pixel-level QUBO segmentation on quantum hardware.

---


### 369. [UMI3D: Robust 3D Generation on Unconstrained Multi-Image Inputs via Simultaneous Focus Cross-Attention Routing](https://arxiv.org/abs/2607.24298)

**<font color=#1a73e8>作者：</font>** Zefan Qu, Zhenwei Wang, Gerhard Petrus Hancke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent 3D foundation models can generate high-quality assets from a single image, but degrade markedly on unconstrained multi-image inputs, often producing distorted geometry, over-smoothed textures, and chaotic colors. We argue that this failure stems not from limited model capacity, but from a mismatch between single-image cross-attention and the multi-image setting: existing models lack a principled way to decide which image each 3D voxel should trust at each denoising step. Revisiting recent single-image 3D foundation models, we show that explicitly routing each voxel to its most informative image is sufficient to unlock strong performance on inconsistent multi-image inputs. Based on this observation, we propose UMI3D, a training-free and plug-and-play framework that restructures cross-attention for unconstrained multi-image 3D generation. Its core, Simultaneous Focus Cross-Attention (SFC-Attn), activates all conditioning images at each denoising step while allowing each voxel to focus on the single image that best explains it. To enable this routing, we derive the Voxel Reference Score (VRS), a model-intrinsic metric for voxel--image affinity that requires no external matching, segmentation, or correspondence models. Extensive experiments show that UMI3D unlocks the multi-image potential of single-image 3D generation frameworks across diverse tasks. Project Page: this http URL.

---


### 370. [Self-Authored Verification Is Unreliable in Heuristic Self-Improving Agents](https://arxiv.org/abs/2607.24300)

**<font color=#1a73e8>作者：</font>** Diandian Guo, Cong Cao, Fangfang Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-improving agents accumulate capability by repeatedly rewriting procedural policies, controllers, or heuristic rules. They typically rely on self-authored tests or metrics to decide whether to accept subsequent edits. The agent controls both the optimized object and its verifier. As a result, self-assigned scores can remain near perfect while real deployment performance degrades or stays low. We study this problem through the verifier--deployment gap. This gap refers to the discrepancy between an agent's self-authored verification signal and a sealed deployment evaluation that the agent cannot observe or access. We ask how self-authored verification fails under iterative policy-and-test rewriting, how the failure changes with capability, and how little exogenous trust is sufficient to prevent real regressions from being deployed. To address this problem, we introduce a Sealed Exogenous Acceptance Loop (SEAL). SEAL retains self-authored tests but compares each candidate with the incumbent through a fixed harness-side audit. The agent cannot author or inspect the audit, receives only accept/reject, and the whole incumbent state is retained after a clear regression. Our experiments show that this problem often appears in heuristic learning settings. These settings require trial-and-error discovery of the target objective. We further find that failures of self-written verification are stratified by capability. Weaker agents tend to damage previously acquired strategies behind easy self-tests. Stronger agents are more stable, but they still mismeasure the deployment distribution. Standard self-written constraints do not reliably close this gap. In contrast, SEAL outperforms unprotected baselines across six models and three random seeds. Reliable self-improvement need not abandon self-verification, but it requires at least one deployment-acceptance signal outside the agent's control.

---


### 371. [Multiview Multi-Person Human Mesh Recovery Under Large Scenes with Occlusions](https://arxiv.org/abs/2607.24302)

**<font color=#1a73e8>作者：</font>** Qi Zhang, Tao Yu, Jiechao He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human mesh recovery (HMR) aims to recover 3D human meshes from images. Most existing HMR benchmarks and methods focus on either multi-person reconstruction from a single view or single-person reconstruction from multiple views, where the number of subjects and the scene scale are relatively limited. Such settings are insufficient for real-world applications with large scenes and severe inter-person occlusions. To address this limitation, we introduce a large-scale synthetic benchmark for multiview multi-person HMR, termed MVMP-HMR. The proposed dataset contains 15 complex scenes with up to 50 camera views and 30 interacting persons, featuring large spatial coverage and severe occlusions, which significantly increases the difficulty of human mesh recovery. Based on this benchmark, we further propose a multiview multi-person whole-body human mesh recovery model, referred to as MVMP-HMR model. The model first fuses multiview features into a scene-level 3D feature volume, and then leverages pelvis joints predicted by a 3D pose estimation network to extract person-specific queries from the 3D feature volume. These human queries are cross-attended with the 3D feature volume and integrated to decode each person's 3D mesh. Moreover, we introduce two novel losses--the orientation loss and the 3D joint density loss--to alleviate orientation and pose ambiguities under severe occlusions. Experiments demonstrate that existing state-of-the-art HMR methods struggle on the proposed MVMP-HMR benchmark, while our method consistently outperforms prior SOTAs in large-scale scenes with severe occlusions.

---


### 372. [Unequal Trips, Unequal Places: Diagnosing and Mitigating Delay Inequity in Autonomous Vehicle Fleet Coordination](https://arxiv.org/abs/2607.24336)

**<font color=#1a73e8>作者：</font>** Nicole Hu, Mingtao Zhang, Haoyang LI 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> City-scale autonomous vehicle fleet coordinators are typically optimized for aggregate travel time, yet fleet averages conceal how delay is distributed across trips and regions. We conduct a distributional audit on three real-city road-network and taxi-demand datasets from Manhattan, Chicago, and San Francisco. The audit reveals pervasive trip-length inequity whose direction depends on the city and coordinator. After accounting for trip length, spatial inequity becomes more pronounced as demand grows and is consistently stronger when trips are grouped by origin rather than destination. These findings motivate SPatially Aware RErouting (SPARE), a budgeted online coordination framework that assigns limited replanning capacity to delayed vehicles and redirects them using recently observed waiting pressure. SPARE provides a per-review decision guarantee and explicitly bounds online route updates. Experiments on all three datasets against six representative baselines show that SPARE delivers the strongest joint efficiency-fairness performance while retaining city-scale scalability. The results demonstrate that bounded congestion-responsive rerouting improves performance and equity without full-fleet replanning.

---


### 373. [Perturbative-NeuSA: A Structured Spectral Framework for Time-Dependent PDEs](https://arxiv.org/abs/2607.24345)

**<font color=#1a73e8>作者：</font>** Xianli Zhu, Jia Yin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural spectral PDE solvers often learn an entire unresolved vector field even when an inexpensive approximate model can already capture most of the trajectory. Here we introduce Perturbative-NeuSA, a residual formulation that decomposes the target solution into a low-fidelity background and a high-resolution perturbation, so that only the unresolved dynamics is learned. Starting from the exact perturbation equation, the method combines a fixed spectral operator, a background-dependent correction, the background defect in the target PDE, and an optional neural closure. This construction makes the roles of physical structure and neural closure separately measurable. Across 2D Burgers, Klein-Gordon, and heterogeneous 2D wave equations, the deterministic structured solver outperforms the trained NeuSA baseline while requiring no neural-network training. The largest gains occur on Burgers, where the deterministic correction reduces training and extrapolation errors by factors of 24 and 44, respectively. In addition, a Klein-Gordon sweep over seven background resolutions shows that the effect of the closure is conditional: it improves a poor background by 3.6 times, becomes neutral at intermediate resolutions, and degrades a well-resolved background. For the wave equation, however, the closure provides an additional 18% reduction when the remaining residual is interface-localized. Multi-initial-condition diagnostics further show that the useful closure regime depends on the initial-condition spectrum and can disappear in extrapolation when structured correction already captures the dominant Burgers dynamics. Perturbative-NeuSA therefore reframes neural closure as a conditional, diagnosable correction governed by background fidelity, residual organization, and compatibility with the closure model.

---


### 374. [PRISM: Prompt Refinement via Image-grounded Self-rewarding Mechanism for Text-to-Image Generation](https://arxiv.org/abs/2607.24353)

**<font color=#1a73e8>作者：</font>** Guo Tang, HongJie Luo, Tianxu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image generation models can synthesize high-quality images from natural language descriptions, but their performance remains highly sensitive to prompt formulation. Existing prompt optimization methods mainly rely on text-side rewriting, prompt expansion, or external reward signals, offering limited image-grounded diagnosis and weak support for learning reusable optimisation policies. In this paper, we propose PRISM, a Prompt Refinement framework via Image-grounded Self-rewarding Mechanism. PRISM closes the prompt-image-feedback loop by interpreting generated images with structured visual diagnosis and scoring them along semantic consistency, aesthetic quality, and human preference alignment. It first initializes a unified VLM through multi-task supervised fine-tuning, and then improves the prompt policy via self-rewarding optimization with a hybrid ideal-point and Chebyshev reward. Extensive experiments show that PRISM improves holistic image quality and fine-grained semantic alignment, while providing interpretable feedback for targeted prompt refinement. The code is available at this https URL.

---


### 375. [TaoMate: Anchor-Guided Memory Bridging Evolving and Reference States for Real-Time Audio-Video Digital Human Generation](https://arxiv.org/abs/2607.24359)

**<font color=#1a73e8>作者：</font>** Qijun Gan, Chenwei Zhang, Meiguang Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time long-form digital-human generation relies on causal models to extend audio-visual content while preserving subject appearance and audio-video synchronization across successive segments. A bounded cache retains local motion and phonetic context but discards older evidence, whereas attending to the complete generated history is computationally expensive and can propagate accumulated errors. We present \method, an anchor-guided persistent-memory framework for few-step joint audio-video generation. The framework preserves an immutable visual anchor, compresses completed video and audio blocks into fixed-capacity dynamic states, and retrieves those states through modality-specific residual attention without extending the active cache. A reference-aware modulation method additionally conditions video features on dynamic and anchor appearance statistics. Anchor-preserving causal-context distillation varies rollout horizon, prefix provenance, and cache-history reliability while keeping the immutable visual anchor unperturbed. By separating persistent memory from stage-local denoising dependencies, \method further admits stage-parallel execution across blocks, accelerating autoregressive inference without pipeline-specific retraining. We evaluate long-form video continuations with appearance, temporal, synchronization, facial, and speech diagnostics. Results show that \method preserves stable appearance across prompt-conditioned segments and strong audio-visual synchronization under autoregressive generation. Our project page is this https URL.

---


### 376. [Order-Bound Companionship: The Practice of Emotional Labor in Professional Game Companionship](https://arxiv.org/abs/2607.24363)

**<font color=#1a73e8>作者：</font>** Xiaohe Mo, Yujie Zhang, Yizhen Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Labor in platform gig economy increasingly involves services involving relationship that demand significant emotional investment. Grounded in China's unique socio-cultural and multi-platform context, this study explores professional game companionship, an under-explored digital labor practice. Through interviews with 22 game companionship practitioners, we used a micro-level perspective to relational gig work to analyze how workers navigate intimate boundaries and stakeholder networks. We found that companions adopt an "order-bound" mechanism: performing immersive deep acting during paid sessions, followed by complete emotional disengagement post-order. We also identified a tripartite companion-centric network featuring scenario-based performances with clients, competitive-symbiotic peer relations, and interdependent governance with companionship clubs. Furthermore, significant identity fluidity exists, with individuals frequently transitioning between companion, client, and club operator roles. We provide implications for future labor governance and platform designs for intimate digital work that explicitly account for institutionalized boundaries and gig workers' shifting psychological needs.

---


### 377. [HistoGPA: A Context-Conditioned Gene-Prior Attention Framework for Histology-Based Spatial Gene Expression Prediction](https://arxiv.org/abs/2607.24364)

**<font color=#1a73e8>作者：</font>** Ziang Liu, Xinhai Chen, Yigui Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting spatial gene expression from routine hematoxylin and eosin (H&E) images provides a practical complement to experimental spatial transcriptomics. Existing approaches focus on local or multi-scale visual features and often treat pretrained gene representations as fixed priors, although the interpretation of local morphology and the relevance of gene priors depend on tissue context. We propose HistoGPA, a context-conditioned gene-prior attention framework that uses a shared slide-level representation in two parallel pathways: one modulates local morphological features, whereas the other conditions pretrained gene embeddings and retrieves gene-prior information through cross-attention. This design enables each spatial location to retrieve context-adapted gene-prior information using its local morphology, position, and slide context. Across ten cancer types in HEST-1k, HistoGPA achieves the highest macro-averaged gene-wise Pearson correlation coefficient among the compared methods under the same evaluation protocol for both the top-50 and top-1,500 highly variable gene sets. Additional analyses show that HistoGPA better recovers the spatial expression patterns of cancer-associated genes and yields greater agreement between clusters derived independently from predicted and ground-truth expression profiles. Together, these findings motivate a context-dependent view of histology-to-expression prediction, in which local morphological representations and gene priors are jointly adapted to the broader tissue context.

---


### 378. [MobiWave: Dispatch-Oriented Graph Wavelets and Drift-Guided Selective Optimization for Autonomous Fleet Rebalancing](https://arxiv.org/abs/2607.24365)

**<font color=#1a73e8>作者：</font>** Xiao Han, Pinbo Wang, Yuanshao Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous fleets enable mobility platforms to coordinate idle vehicles directly, making fleet-wide rebalancing possible. However, two obstacles limit reliable deployment: overlapping regional and local traffic patterns can hide roads that remain useful for dispatch, and mobility drift can make a trained policy unreliable. Existing spatial aggregation mixes these patterns, while updating all parameters from limited recent data is costly and can damage stable knowledge. We propose \name, a framework that connects a dispatch-oriented multi-scale graph wavelet module with Drift-Guided Layer-Selective Optimization (DGLS). The first module addresses the representation challenge by separating graph-frequency patterns and weighting each scale according to its value for demand prediction and feasible rebalancing. DGLS addresses the adaptation challenge by measuring Dispatch-weighted Spectral Drift, selecting affected layers within a resource budget, and separating short shocks from persistent changes through a drift-aware fast--slow update. Candidate validation further rejects updates that fail to improve held-out dispatch reward without worsening monitored service or safety constraints. Experiments on both real-world datasets and simluated environments demonstrate the effectiveness of \name\ in comparing with state-of-the-art methods. The source code and datasets are available at this https URL.

---


### 379. [Keep It InMind: Benchmarking the Implicit-Association Blind Spot in Agent Memory](https://arxiv.org/abs/2607.24368)

**<font color=#1a73e8>作者：</font>** Ruizhe Li, Mingxuan Du, Benfeng Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory systems store what a user says in an external store and retrieve it when a related query arrives. This interface rests on an assumption so natural that it is rarely stated: a memory that is needed will resemble the query that needs it. World knowledge breaks the assumption. A tree-nut allergy should change the answer to a macaron request through their almond-flour ingredient, yet the two texts share no cue a retriever can see. We call this failure mode the implicit-association blind spot and introduce InMind, a 125-task, expert-verified benchmark spanning ten life domains, with 113 tasks grounded in citable public sources. Its paired controls separate three explanations that existing evaluations conflate: the fact was never stored, the model lacks the bridging knowledge, or the fact was stored and never surfaced. The verdict is clean. With the decisive memory placed in context, the backbone answers 84.0 percent of indirect queries; when the same memory must be retrieved, six vector, graph, and agentic memory systems reach at most 14.4 percent, even though they recall the same facts on demand at up to 100 percent. An embedding with eight times the dimensionality raises answer-blind target recall for every system yet leaves the gap essentially intact. A minimal diagnostic probe that keeps memory visible before the query arrives recovers most of the gap, locating the failure in the query-conditioned interface itself and pointing to routing, deciding which facts must stay visible, as the open problem InMind is built to score.

---


### 380. [MXAttention: Data-Free Optimal Scaling and Pre-Normalization Quantization for MXFP4 Attention](https://arxiv.org/abs/2607.24377)

**<font color=#1a73e8>作者：</font>** Jianlin Yu, Jing Lin, Linghui Kong 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The quadratic cost of attention is a major bottleneck in diffusion-based video generation models. MXFP4 attention provides a promising path toward efficient inference, but direct MXFP4 quantization often degrades generation quality due to two numerical issues: the clipping-underflow trade-off from power-of-two scaling and the row-wise normalization error introduced in the softmax loop. We propose MXAttention, a data-free post-training quantization framework for MXFP4 attention. MXAttention introduces two components: Universal Optimal Scaling (UOS), which exploits the periodic structure of power-of-two microscaling to derive a distribution-independent optimal scaling boundary Qmax=7.25 without calibration or search, and Pre-Normalization Quantization (PNQ), which quantizes unnormalized softmax exponentials before row-wise summation to preserve normalization by construction. Experiments on Wan2.2 and HunyuanVideo show that MXAttention closes at least 95% of the VBench Imaging Quality gap between OCP MXFP4 and FP16, substantially improves frame-level similarity, and preserves FP16-level generation quality with less than 0.01 absolute degradation on all reported VBench metrics. MXAttention also achieves performance competitive with strong NVFP4-based baselines with negligible overhead when fused into the attention pipeline. The implementation is publicly available in MindIE-SD.

---


### 381. [Ambient pressure compensation and robust position control of oil-filled electric joint systems for underwater manipulators](https://arxiv.org/abs/2607.24384)

**<font color=#1a73e8>作者：</font>** Hongrui Wu, Songhui Wang, Xin Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Electric joint systems are significant elements of an underwater manipulator for its actuation, drive, and control. Working in an underwater environment, the joints suffer huge ambient pressure. To withstand it, the pressure compensation method is usually deployed, whereas the pressurized oil introduces sealing problems as well as parametric uncertainties and unknown disturbances for the dynamic model of the joint. To tackle these issues, this study proposes a design framework for the underwater oil-filled electric joint. The dynamics of the pressure compensation module is analyzed and the structure of the joint is optimized to seal the internal hydraulic oil. An uncertainty dynamic model of the oil-filled joint is established and a robust position controller is designed based on the structured singular value synthesis (mu-synthesis). Experimental results validate the feasibility of the proposed methods.

---


### 382. [GenSplatCodec: Feed-Forward Gaussian Splatting Compression via One-Step Diffusion](https://arxiv.org/abs/2607.24403)

**<font color=#1a73e8>作者：</font>** Qiang Hu, Zhenlong Wu, Lei Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting (3DGS) enables scalable scene reconstruction without per-scene optimization, yet produces dense Gaussians that are costly to store and transmit. Existing feed-forward Gaussian compression methods formulate decoding as deterministic representation recovery, which becomes inadequate at low bitrates when high-frequency textures and view-dependent appearance are discarded. Although generative models offer a promising alternative, using them as standalone post-processing decouples generation from the transmitted scene structure, thereby compromising cross-view consistency. To address these limitations, we propose GenSplatCodec, a unified feed-forward Gaussian codec that reformulates low-bitrate Gaussian compression as geometry-guided generative decoding. We present a detail-aware feed-forward Gaussian coding scheme within a dual-stream formulation, where the resulting compact Gaussian structural stream is complemented by a lightweight reference appearance stream. We further introduce a geometry-guided one-step generative decoding approach that jointly exploits decoded structural and appearance cues through hierarchical geometry control to reconstruct high-fidelity and view-consistent novel views. Finally, we develop a three-stage optimization strategy that stabilizes the learning of the unified codec and adapts the generative decoder to codec-derived structural and appearance cues. Extensive experiments across multiple datasets demonstrate that GenSplatCodec consistently achieves superior rate-distortion (RD) performance over existing methods.

---


### 383. [K-Survival Means](https://arxiv.org/abs/2607.24405)

**<font color=#1a73e8>作者：</font>** Abdallah Alabdallah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we propose K-SurvMeans, a novel extension of K-Means for clustering survival data. The method explicitly uses the survival outcome in the clustering process to optimize cluster centers, thereby maximizing pairwise survival differences between clusters. The objective function encourages the clusters to be well-separated from the survival perspective. Since the resulting optimization problem is non-differentiable, we employ the Particle Swarm algorithm for the Optimization process.
To further improve flexibility and mitigate the curse of dimensionality, we extend the framework to operate in a learned low-dimensional latent space obtained via a dimensionality reduction. This allows the method to capture better-separated clusters and enhance optimization efficiency by reducing the search space.
Experiments on multiple publicly available benchmark survival datasets demonstrate that K-SurvMeans consistently yields clusters with improved separation in survival distributions compared to existing deep learning-based survival clustering methods.

---


### 384. [Accuracy potential of visual localization exploiting high-end street-level imagery](https://arxiv.org/abs/2607.24409)

**<font color=#1a73e8>作者：</font>** Jonas Meyer, Stephan Nebiker, Pascal Theiler 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate and reliable pose information with respect to a reference frame is increasingly demanded across applications such as autonomous navigation, surveying, robotics, and augmented and mixed reality. Visual localization can serve as a complementary positioning modality to GNSS, whose applicability and accuracy are often limited. Yet, the accuracy potential of visual localization has not been systematically investigated against survey-grade demands. This is mainly due to the lack of publicly available, large-scale outdoor datasets with ground-truth poses in the sub-centimeter range. In this work, we address both gaps. We introduce a scalable visual localization pipeline that employs precisely georeferenced, high-resolution street-level imagery directly as the scene representation. It combines prior-guided reference candidate selection with on-the-fly local Structure-from-Motion reconstruction and PnP-based pose estimation. We further present the FHNW Muttenz dataset, a real-world dataset covering a contiguous 10 km street network mapped in two mobile mapping campaigns approximately 1.5 years apart. It consists of high-resolution reference imagery and query sequences acquired by four different cameras across five representative scenes. All images are precisely co-registered, yielding 6-DoF ground-truth poses in the sub-centimeter range. Using this dataset, we evaluate the accuracy potential of visual localization. Our experiments demonstrate median pose accuracies in the range of 1-5 cm for translation and 0.05-0.1° for rotation, reaching as low as 1 cm and 0.03° under favorable conditions. These results show that visual localization can complement survey-grade GNSS positioning, paving the way for 3D geospatial data acquisition using consumer devices and fully automated georeferencing approaches. The dataset is publicly available at: this https URL.

---


### 385. [Occluded Oculus: Operationalizing Stylistic Obscurement](https://arxiv.org/abs/2607.24411)

**<font color=#1a73e8>作者：</font>** Robert Dilworth  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> What did it take for Hermes, the devout messenger of the Olympian gods, to slay Argus Panoptes, the multi-eyed giant of Greek myth? As the perfect guardian, Panoptes' legion of ever-watchful eyes proved difficult -- but not impossible -- to defeat. The centerpiece of Hermes' strategy was obfuscation and sabotage. Posing as a shepherd, Hermes sealed each of Panoptes' eyes -- eyes that would otherwise have alerted the fearsome giant to Hermes' plot -- and vanquished him. The moral of the story: when a challenger must surmount a formidable foe -- one far greater in stature and vastly more equipped -- crafty maneuvers are not merely advisable but indispensable for victory. In this work, the "challenger" is a collective leveraging adversarial tactics to overcome the "multi-eyed giant" of stylometric systems and surveillance apparatuses. To successfully claw back the privacy siphoned by the multi-eyed giant, the challenger must carefully evaluate their plan of attack, $\textit{TraceTarnish}$, and determine what does and does not work to anonymize the authorship of text. To that end, we conduct an ablation study of $\textit{TraceTarnish}$ to better understand which module -- Translation, Obfuscation, Imitation, or Injection -- best confounds a stylometric system. Our results indicate that the most effective approach was Injection, meaning that inserting zero-width Unicode characters, homoglyphs, and intentional misspellings neutralizes the indefatigable eyes long enough to claim the head of the all-seeing giant.

---


### 386. [Near-Tight Theoretical Bounds for Incentive Compatibility in Bitcoin Mining](https://arxiv.org/abs/2607.24415)

**<font color=#1a73e8>作者：</font>** Akira Sakurai, Taishi Nakai, Kazuyuki Shudo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When is honest Bitcoin mining rational? This question is central to the incentive design of proof-of-work blockchains. Sapirshtein et al. computationally derived near-tight lower and upper bounds on the incentive-compatibility threshold using a Markov Decision Process. Kiayias et al.'s Blockchain Mining Games instead derived theoretical lower and upper bounds. However, this theoretical approach has two limitations: its model restricts miners to a narrow action space and assumes idealized tie behavior, and its lower and upper bounds are far from tight.
We resolve both limitations. We develop a more realistic model with a broader miner action space and asymmetric tie-breaking parameters $\gamma^-$ and $\gamma^+$. We then propose an algorithm that computes lower and upper bounds on the incentive-compatibility threshold with a maximum error of $9.98006\times10^{-4}$.

---


### 387. [Decentralised Consensus Learning Networks: SME Rotation Without Centralised Reward](https://arxiv.org/abs/2607.24416)

**<font color=#1a73e8>作者：</font>** Florin Neagu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Centralised reward signals dominate modern AI learning systems, but they impose a single external definition of correct or valuable knowledge. We present a decentralised, consensus-based multi-agent learning framework in which expertise emerges through peer validation rather than prescribed reward. Agents update beliefs via weighted social consensus, while trust is allocated according to competence inferred from peer consistency instead of ground truth. Subject-matter expert (SME) status is assigned dynamically as a top-percentile competence rank rather than a fixed label.
We evaluate the framework across 84 simulation runs spanning 30 to 10,000 agents, multiple graph topologies, sparse large-scale networks, scalar and vector belief representations, dimensionality sweeps (D=1-500), multi-seed robustness tests, and parameter sensitivity analyses. Phase 1 shows that SME rotation is robust, persistent, topology-invariant, and scale-invariant: 90-100% of agents attain SME status, with most expertise turnover occurring after belief convergence and increasing with network size. Phases 2 and 3 show that vector beliefs introduce heterogeneous convergence with cascade dynamics and reveal five distinct dynamical regimes as belief dimensionality increases. At high dimensionality (D=150-200), the network reaches stable partial consensus while expertise becomes increasingly concentrated in a single agent. ETA sensitivity analysis demonstrates that this concentration is driven by belief dimensionality rather than stochastic noise. We interpret this behaviour as an emergent property of decentralised learning: in complex high-dimensional consensus spaces, the agent most consistently aligned with the collective belief naturally emerges as the recognised expert.

---


### 388. [Failures Reveal What Metrics Miss: An Evidence-Driven Agent for Recursive Refinement of ECG Classifiers](https://arxiv.org/abs/2607.24419)

**<font color=#1a73e8>作者：</font>** Jinliang Deng, Yiming Niu, Yibo Pan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep models have substantially advanced 12-lead ECG classification, yet their refinement still relies heavily on human experts to inspect failures and iteratively revise classifier designs. Recent LLM-based agents have demonstrated the potential for automated model design, but when guided only by aggregate performance metrics, they lack insight into why individual cases fail and how the classifier should be revised. We present RecursiveECG, an evidence-driven LLM-as-Designer framework in which an LLM serves as an offline model designer that refines ECG classifiers based on concrete failures and objective ECG evidence. To ground failure diagnosis in executable evidence, Criteria-to-Measurement Compilation converts curated ECG criteria into validated deterministic functions that produce reproducible, reference-backed measurements for individual ECGs. Building on these measurements, Evidence-Grounded Failure Review analyzes failed and comparator cases by jointly considering raw waveforms, measurements, and model outputs, enabling the LLM to diagnose classifier limitations and formulate targeted revisions. Candidate revisions are executed and re-evaluated under a fixed problem contract, and only evidence-supported updates are retained. The resulting predictor is frozen after refinement and requires no LLM inference during deployment, while an audit trail links each accepted revision to its supporting evidence. Across PTB-XL, Georgia, and CPSC2018, RecursiveECG consistently outperforms strong baselines, achieving an average relative improvement of 10.0%. Extensive ablation and transfer studies further validate the effectiveness of its evidence-grounded refinement process.

---


### 389. [Context Is King: How In-Context Specification Shapes the Geometry of Concepts](https://arxiv.org/abs/2607.24425)

**<font color=#1a73e8>作者：</font>** Elad David, Max Fomin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models place structured concepts on geometrically faithful manifolds: weekdays lie on a circle, months on another, usually taken to be a fixed world-model the network stores and looks up. We show that context is king: the structure a model actually uses is set by the in-context specification. A declarative rule fixes not only which relations the geometry encodes but its topology type: the same tokens form a cycle or a branching tree on command, built even on arbitrary, meaning-free tokens with no prior to inherit, which a relabeled stored shape cannot do. When the specification conflicts with a strong pretrained prior, the context-set geometry dominates it in capable models, read from the same activations (representational similarity 0.6--0.9 to the imposed structure versus near-zero to the prior), across the priors we test and both families we study (Gemma, Qwen). Activation patching shows the map is causally used, not a probe correlate: swapping one entity's activation for another's makes the model answer with the other entity's successor under the imposed order. A rough map forms readily, present even in small and base models; what scale gates is using it cleanly: clean dominance and the causal crossover emerge only in the larger models (up to Gemma-31B and Qwen-27B) and weaken or reverse below, so a mechanism present in a large model can be absent in a smaller one of the same family. Whether the model builds this geometry anew or reconfigures a stored one we leave open; operationally, the geometry it uses is the one the context specifies.

---


### 390. [Let Me Look at You: Advanced Facial Expression Modeling for Conversational Speech Synthesis](https://arxiv.org/abs/2607.24430)

**<font color=#1a73e8>作者：</font>** Yifan Hu, Shuwei He, Rui Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversational Speech Synthesis is a fundamental component of human-computer interaction, aiming to generate contextually appropriate, expressive, and empathetic speech. However, facial expressions encode subtle and rich affective cues that are crucial for empathetic speech interaction, whereas existing approaches often overlook this important modality. In addition, the lack of large-scale natural conversational datasets with both speech and visual modalities also limits the development of visual affect understanding in conversational this http URL address these limitations, we propose FacialTalker, a facial-expression-aware CSS framework built upon a large language model backbone. To efficiently encode facial expressions, we propose AUTokenizer, a single-codebook visual tokenizer that discretizes each frame-level facial expression into a compact token, trained with supervision from combinations of facial Action Units. We further introduce a dual direct preference optimization (DualDPO) strategy, which extends the DPO by jointly imposing preference constraints on both visual and speech token sequences, to enhance the model's understanding of facial expressions and speech semantics in multimodal conversational contexts. Moreover, we construct VSDD-1K, a large-scale multimodal dialogue dataset collected through a fully automated pipeline from real-world Internet conversations, comprising over 1,033 hours of synchronized speaker videos and speech, with more than 85\% of frames containing valid faces. Extensive objective and subjective experiments demonstrate that FacialTalker consistently outperforms strong baselines in facial-expression perception and speech synthesis quality, generating speech that is more natural, expressive, and better aligned with the conversational context. The results also validate the effectiveness of our training strategy and dataset construction pipeline.

---


### 391. [InterOCF: Spatio-Temporal 2D-3D Interaction for Camera-Only 4D Occupancy Forecasting](https://arxiv.org/abs/2607.24431)

**<font color=#1a73e8>作者：</font>** Qi Zhang, Xinquan Yu, Kaiyi Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-only 4D occupancy forecasting enables autonomous vehicles to predict future 3D semantic scenes solely from historical multi-view images, which is critical for driving safety. Even though current methods have achieved good performance, the strong spatial-temporal modeling between the input multi-view frames is still underexplored, which limits the performance of those methods in future 4D forecasting. To address this gap, we introduce a novel framework, InterOCF, for 4D occupancy forecasting that jointly models temporal dynamics in both 3D voxel-based representations and multi-view segmentation sequences, while explicitly incorporating feature interaction between the 2D and 3D branches. Our framework incorporates three core components: 1) A 3D Spatio-Temporal (3DST) module that learns volumetric dynamics from historical voxel states to predict future voxel states; 2) A 2D Spatio-Temporal (2DST) module employing an auxiliary multi-view temporal segmentation forecasting task to enhance temporal semantic dynamics; 3) A Spatio-Temporal Interaction Modeling (STIM) module that enables feature interaction between 2D and 3D representations. Experiments on the nuScenes, Lyft-Level5, and nuScenes-Occupancy datasets show that InterOCF consistently outperforms existing baseline approaches.

---


### 392. [MSVS-VAE: Multi-Scale Anchored VecSet for High-Fidelity 3D Reconstruction](https://arxiv.org/abs/2607.24436)

**<font color=#1a73e8>作者：</font>** Dehao Hao, Kaiyi Zhang, Tanghui Jia 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity 3D generative modeling increasingly relies on the latent diffusion paradigm, where the reconstruction quality of the underlying 3D VAE becomes a primary bottleneck. Existing approaches largely follow two paradigms: sparse voxel-based representations achieve strong reconstruction quality but incur significant memory and computational overhead, while set-based representations are compact and continuous yet typically lag in fidelity due to latent sparsity and excessive global smoothness. We propose MSVS-VAE, a hierarchical set-based VAE that closes this fidelity gap without sacrificing compactness. Our key idea is to progressively densify anchored VecSet latents via hierarchical point-shuffle upsampling, increasing spatial capacity for fine-grained geometry modeling. To efficiently decode from the densified hierarchy, we replace global cross-attention with AVS-Conv, a geometry-aware local aggregation operator operating within local neighborhoods rather than the exhaustive latent set. We further introduce multi-scale query decoding to fuse coarse-to-fine latent features, where coarse scales provide stable global context, and fine scales refine localized geometry, reducing artifacts from overly local receptive fields. Extensive experiments on Objaverse, ABO, and in-the-wild benchmarks demonstrate that MSVS-VAE consistently outperforms prior set-based and voxel-based VAEs, delivering approximately 10x faster decoding than prior set-based methods and approximately 10x higher compactness than voxel-based baselines.

---


### 393. [ESRVS: Extreme Semi-Supervised Retinal Vessel Segmentation with a Single Annotated Image](https://arxiv.org/abs/2607.24453)

**<font color=#1a73e8>作者：</font>** Mingzhi Xu, Yizhe Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning from minimal human supervision is a long-standing goal in medical image analysis, where dense expert annotations are costly. We study retinal vessel segmentation in an extreme semi-supervised setting with one annotated image and a pool of unlabeled images. We propose ESRVS, which selects a representative reference image for manual annotation and transfers vessel cues using target-domain-adapted DINOv3 features. ESRVS constructs a multi granular vessel prototype, combines prototype-similarity maps with a physics-inspired prior to generate initial pseudo-labels, and refines the transferred supervision through weighted pseudo-label training and adversarial refinement. Across eight public datasets, ESRVS achieves the best Dice and clDice on six datasets, and the best HD95 on all eight datasets among the compared semi-supervised methods, although those methods use 10 to 20% labeled data. With Mask2Former, ESRVS retains on average 93.7% of fully supervised Dice and 95.1% of fully supervised clDice. These results demonstrate the potential of foundation-model label propagation for highly label-efficient retinal vessel segmentation. Code is available at this https URL.

---


### 394. [Rethinking Expert Training for Model Merging with Prompt Learning](https://arxiv.org/abs/2607.24465)

**<font color=#1a73e8>作者：</font>** Christos Georgakilas, Aniello Panariello, Samir El Karrat Moreno 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Model merging aims to combine multiple domain-specialized experts trained from a shared foundation model into a single multi-task model. Existing approaches largely focus on improving the merging procedure itself and typically assume experts obtained through full-parameter fine-tuning. In this work, we revisit expert training for model merging. We first show that prompt-based adaptation provides a strong baseline: independently learned prompts can be exploited across tasks while keeping the backbone fixed, avoiding the interference introduced by weight merging. Building on this observation, we introduce Dual-Tuned Experts (DTEs), a two-stage training strategy that first learns prompts and then fine-tunes the vision encoder. This reduces the magnitude of task-specific parameter updates and produces experts with higher merge compatibility. Experiments across multiple CLIP architectures, full fine-tuning, and LoRA experts show that DTEs consistently improve merged performance of standard merging approaches and remain effective even when combining heterogeneous sets of experts.

---


### 395. [Grounding latent algorithm routing in transformer reasoning](https://arxiv.org/abs/2607.24471)

**<font color=#1a73e8>作者：</font>** Xiangbo Zhang, Xiaoxu Ma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A central question in the in-context learning literature is whether transformers can organize episode-level adaptation around different inductive-bias families. We study this question in a controlled setting through latent algorithm routing: route-like behavior in which the solver-family preference changes with the latent data-generating regime while prompt form is held fixed, remains stable under nuisance perturbations, and is selectively influenced by targeted activation interventions without large losses in answer quality. We introduce ROUTEBENCH, a diagnostic benchmark whose regimes differentially favor global shrinkage, sparsity, robustness, and locality, operationalized by ridge-like, lasso-like, Huber-like, and kNN-like family representatives. Across dense decoder-only transformers trained from scratch at 44M-612M parameters, a 306M model closes 80.9 percent of the oracle-routing gap and achieves route F1 of 84.1. The effect remains substantial under natural-language renderings, shuffled supports, lexical paraphrases, and a unified four-way routing setting. Stronger adaptive alternatives, including an input-conditioned soft mixture and an unsupervised Gumbel router, narrow the gap but remain below the 306M and 612M models on route F1 and OOD performance. Probe controls and matched activation-patching controls further show that route-relevant internal directions are decodable and functionally involved in solver-family-consistent output behavior. These results provide controlled evidence that dense transformers trained on ROUTEBENCH can develop route-like internal variables, but they do not establish universal routing in pretrained language models or unrestricted natural-language reasoning.

---


### 396. [What do Reward Models Memorize?](https://arxiv.org/abs/2607.24484)

**<font color=#1a73e8>作者：</font>** Ivo Verhoeven, Pushkar Mishra, Ekaterina Shutova  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper studies what discriminatively trained reward models (RMs) memorize by measuring counterfactual memorization on two human preference datasets. We show that RMs 1) misallocate memorization to easy, high margin preference pairs, 2) memorize dataset-specific shortcuts (e.g., model identity, user sampling strategy), and 3) overgeneralize simple heuristic correlates of human preference (e.g., length, compliance) when confronted with unseen preference pairs. Overall, our findings indicate that discriminative training of RMs from human preference data results in biased RMs not yet capable of judging response quality in context-dependent scenarios.

---


### 397. [NSL-SLAM: High-Fidelity Neural Structured-Light Depth for Practical SLAM and Reconstruction](https://arxiv.org/abs/2607.24495)

**<font color=#1a73e8>作者：</font>** Jiaheng Li, Binsheng Zhang, Xinhai Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structured-light (SL) cameras power depth sensing in millions of devices, and recent neural SL decoding methods have substantially improved their depth quality. SLAM systems can benefit greatly from such strong depth sensing, where reliable geometry enables stable tracking and faithful reconstruction. In this work, we present NSL-SLAM, a practical SLAM system tailored for high-fidelity structured-light depth. We first strengthen SL depth sensing: inspired by the neural structured-light (NSL) method, we further incorporate strong monocular depth priors into the SL stereo decoding, reducing depth RMSE by 35% on Replica-SL compared to NSL. We then build a depth-centric SLAM pipeline with this stronger depth: because structured-light geometry is dense and metrically accurate, we keep it as the primary tracking signal, and add only sparse visual correspondences for geometrically degenerate cases and lightweight bundle adjustment for long-range drift. Our depth estimator and SLAM design reinforce each other: stronger depth makes a simple SLAM pipeline effective, and the depth-centric pipeline ensures this advantage transfers to downstream reconstruction. Experimentally, on the synthetic Replica-SL benchmark, NSL-SLAM achieves the best tracking accuracy and improves reconstruction F-score by 1.6 points over the SOTA baseline under a shared-depth protocol. On a real benchmark of 8 challenging scenes, it is the only method that avoids catastrophic failure on all sequences while achieving 43.3% lower trajectory deviation than selected baselines. The SLAM system runs online at 20.9 FPS, demonstrating that stronger structured-light depth and depth-centric system design together enable practical, robust SLAM.

---


### 398. [Physics Transformer: Tailoring Transformer for General PDE Prediction](https://arxiv.org/abs/2607.24513)

**<font color=#1a73e8>作者：</font>** Guoze Sun, Rui Zhang, Jiankai Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer architectures have attracted increasing attention for solving partial differential equations (PDEs), owing to their flexibility in handling irregular discretizations and their ability to capture long-range physical dependencies. However, unlike discrete language tokens or fixed-resolution image patches, observed physical fields are finite samples of underlying infinite-dimensional functions. Consequently, effectively applying Transformers to PDEs requires a tokenizer that respects the functional nature of physical fields and constructs physically expressive tokens from arbitrary this http URL this end, we propose \methodname{Physics Transformer}, a function-projection-based Transformer architecture for physical field prediction. Physics Transformer treats a physical field as a continuous function and partitions its discretization into locality-preserving spatial patches. Within each patch, it dynamically learns a set of adaptive local basis functions and projects the sampled field onto these bases to obtain compact physics tokens. The resulting tokens capture diverse latent physical states while preserving fine-scale spatial structures, enabling efficient global interaction through factorized attention across space and physical states. The projected representation further supports efficient decoding at arbitrary query locations. Extensive experiments on diverse benchmarks, ranging from two-dimensional PDE dynamics to industrial-scale three-dimensional CFD simulations, demonstrate that Physics Transformer accurately captures fine-grained physical structures and achieves state-of-the-art predictive performance. These results establish function projection as a practical and effective foundation for designing Transformer architectures for PDE solving.

---


### 399. [DecoupleMix: Decoupled Ratio Search and Convex Allocation for Scalable VLM Data Recipes](https://arxiv.org/abs/2607.24516)

**<font color=#1a73e8>作者：</font>** Jiahao Xie, Zhongbin Guo, Qianle Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While data curation for Vision Language Models (VLMs) is increasingly active, public practice for constructing pretraining mixtures remains largely heuristic: practitioners stack datasets that pass quality filters, set cross-domain ratios by intuition, and lack a principled, attributable criterion for admitting new data, while frontier recipes remain undisclosed. We formulate data construction as a systematic mixture-optimization problem and turn it into a reproducible engineering discipline by decoupling the mixture into two orthogonal sub-problems: inter-class ratios across capabilities and intra-class ratios within a category. For inter-class allocation, we use a single-variable iterative search; for intra-class composition, we apply a multidimensional, dataset-level assessment scoring Quality and Difficulty, and formulate selection as a constrained convex optimization with a diversity objective. The DecoupleMix framework delivers two critical capabilities: guiding what data to collect next and rendering dataset validation a controlled, attributable experiment. Experiments show our approach consistently surpasses heuristic baselines. Moreover, optimal ratios discovered on small-scale proxies transfer seamlessly to larger scales without retuning. Using 80B additional multimodal continue-pretraining tokens, our VLM is competitive with strong open-source models trained with substantially larger multimodal budgets.

---


### 400. [Low-Rank Dependence Decomposition via Accelerated Symmetric Non-negative Matrix Factorization](https://arxiv.org/abs/2607.24518)

**<font color=#1a73e8>作者：</font>** Lavinia Ghita, Dhruv Desai, Jake Goldberg 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symmetric non-negative matrix factorization (SymNMF) recovers latent group structure from a dependence matrix, but its dense, quadratic-memory objective has confined prior work to moderate sizes. We present a large-scale GPU study of seven algorithm families (over 30 configurations) on absolute Pearson correlation and tail pairwise dependence matrices from Extreme Value Theory, two proxies for empirical risk-factor estimation on large portfolios. A trace-identity reformulation eliminates all $n \times n$ intermediates, so a single GPU reaches $n \approx 10^5$ and multi-node distribution scales to $n = 10^6$ and beyond. Under a two-phase protocol, eleven methods converge at moderate scale; six remain efficient enough at $n = 10^5$ (five AdaGrad-family plus ADMM), and five AdaGrad-family methods still converge at $n = 10^6$: AdaGrad, RMSprop, and three we introduce (Piecewise AdaGrad, Row-Stochastic SVRG, Block-SVRG AdaptGrow). At $n = 10^6$ the fastest solver tracks the matrix spectrum: Block-SVRG AdaptGrow wins on the flat, ill-conditioned tail-dependence spectrum, where its lower per-iteration cost decides a long factorization, and full-batch AdaGrad wins on the dominant-low-rank correlation spectrum, where the run is short. We also benchmark spherical K-means as a hard-label baseline: cheaper when angular cluster structure is present, yet provably degenerate once the matrix collapses toward a single common factor, where the soft factorization remains necessary.

---


> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-442](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
