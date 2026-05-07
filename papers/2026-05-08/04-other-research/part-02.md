# 📦 其他研究 | 2026年05月08日

> 本类共 **270** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-270](./part-06.md)

---

### 51. [Binary Image-Based Intrusion Detection for Operational Technology Networks: Extending the SPHBI Methodology from IoT to Modbus TCP](https://arxiv.org/abs/2605.04250)

**<font color=#1a73e8>作者：</font>** Aamir Omar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper extends the Single Packet Header Binary Image (SPHBI) intrusion detection methodology from IoT to Modbus TCP, evaluating five approaches spanning a gradient of protocol depth on the CIC Modbus 2023 dataset (11.4 million packets, eight detectable attack types). TCP/IP headers alone achieve only 51.8% binary accuracy, confirming that header-level heterogeneity exploited in IoT traffic is absent in uniform SCADA environments. Adding eight bytes of application-layer information improves binary accuracy to 98.1% with just 63 parameters, directly relevant to per-packet classification on resource-constrained OT edge devices. The best-performing approach achieves 94.4% +/- 2.2pp multiclass accuracy across nine classes (95% CI [92.9%, 95.9%], 10 seeds) with 56,873 parameters, roughly 430 times fewer than comparable ResNet50-based approaches. Per-class recall analysis shows seven of eight detectable attack types identified with recall above 94%, while replay attacks remain structurally undetectable by any single-packet method.

---


### 52. [Root-Cause-Driven Automated Vulnerability Repair](https://arxiv.org/abs/2605.04251)

**<font color=#1a73e8>作者：</font>** Hulin Wang, Zion Leonahenahe Basque, Jie Hu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent LLM-based systems have made automated vulnerability repair increasingly practical, but two challenges remain. First, without strong signals about where a bug originates, repair agents drift toward shallow edits that silence the observed failure while leaving the underlying defect unresolved. Second, finding the root cause for bugs is hard: even developers familiar with the codebase frequently produce fixes that address symptoms rather than the root cause, and LLM-based agents, operating with noisier context and less program understanding, are no exception. We present Kumushi, a root-cause-driven patching agent that addresses both challenges by combining diversified dynamic fault localization with evidence-weighted ranking to focus the LLM on the code most relevant to the defect. To rigorously measure whether Kumushi produces genuinely better patches, we also introduce a two-tier patch quality metric that pairs automated oracle validation with structured expert assessment of patches. Evaluated on 178 C/C++ vulnerabilities, Kumushi substantially outperforms prior specialized repair agents under automated evaluation while matching a frontier commercial coding agent. Expert assessment then reveals differences that oracles cannot: Kumushi produces more root-cause fixes and fewer superficial patches, and is preferred in the majority of decisive pairwise comparisons. Together, these results demonstrate that progress in automated vulnerability repair requires not only stronger patching systems, but also richer evaluation methods capable of distinguishing genuine fixes from oracle-passing ones.

---


### 53. [Hierarchical Support Vector State Partitioning for Distilling Black Box Reinforcement Learning Policies](https://arxiv.org/abs/2605.04254)

**<font color=#1a73e8>作者：</font>** Senne Deproost, Mehrdad Asadi, Ann Nowé  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce State Vector Space Partitioning (SVSP), a novel method to mimic a black box reinforcement learning policy using a set of human-interpretable subpolicies. By partitioning a distillation dataset of state action pairs with linear support vector machine splits, SVSP constructs a compact and structured representation of the original policy. Our method improves mean return by +7.4\% over previous critic driven state partitioning attempts such as Voronoi State Partitioning (VSP) and +2.8\% over the original TD3 policy, while reducing the number of required subpolicies against VSP by 82.1\%. Our results pave the path towards a more flexible form of distillation where both the decision boundary and surrogate models can be chosen within a margin of the original black box behavior.

---


### 54. [HUGO-CS: A Hybrid-Labeled, Uncertainty-Aware, General-Purpose, Observational Dataset for Cold Spray](https://arxiv.org/abs/2605.04257)

**<font color=#1a73e8>作者：</font>** Stephen Price, Kyle Miller, Marco Musto 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cold spraying is an increasingly common approach for repairing and manufacturing components due to its solid-state manufacturing capabilities. However, process optimization remains difficult due to many interdependent parameters and the lack of large-scale, machine-readable data to support modeling. While the scientific literature contains many relevant experiments, results are inconsistently reported (often in tables and figures) and use non-uniform units, limiting utilization at scale. To address these limitations, this work presents HUGO-CS, a literature-derived dataset of 4,383 cold-spray experiments with 144 features from 1,124 sources, exceeding the previous largest dataset (137 samples) by 30x. With completely manual extraction requiring an average of 91 minutes per document, this work designs and leverages a Hybrid-labeled, Uncertainty-aware, General-purpose, Observational extraction framework, called HUGO, to support this extraction. HUGO combines automated LLM-based labeling with targeted manual label refinement to handle this experimental result extraction process from scientific literature. To balance labeling efficiency with extraction accuracy, HUGO introduces a Hierarchical Risk Mitigation (HRM) to route LLM outputs with a high risk of potential errors for manual review, while retaining low-risk records as auto-labeled. Lastly, HUGO post-processing consolidates categorical descriptors, maps reported feedstock chemistries into structured continuous compositions, and normalizes units across sources. Of the 4,383 reported experiments, 1,765 are hand-labeled, providing a high-quality labeled subset for benchmarking, error analysis, and higher-fidelity data points. All code to replicate this work, along with the complete HUGO-CS dataset, are released under a CC-BY license at this https URL.

---


### 55. [Lightweight Vulnerability Detection from Code Metrics and Token Features](https://arxiv.org/abs/2605.04260)

**<font color=#1a73e8>作者：</font>** Chun Yin Chiu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vulnerability detection for C/C++ code increasingly relies on heavy representations such as code graphs and deep models, while many practical workflows still benefit from fast and reproducible ranking baselines for human triage. This preprint studies a lightweight function-level vulnerability triage pipeline that combines sparse token n-grams from raw function text with a small set of inexpensive code metrics, including NLOC, approximate cyclomatic complexity, token count, maximum brace depth, and parameter count. We use TF-IDF token features and a class-weighted logistic regression classifier, avoiding deep learning, transformers, and program graphs.
Using the Devign function-level labels, we evaluate random and cross-project settings, including a FFmpeg-to-QEMU transfer experiment. We emphasize precision-recall AUC and Recall@10% as ranking-oriented metrics for skewed or triage-oriented workloads. On the random split, the best combined variant reaches PR-AUC 0.642 and Recall@10% 0.161, while cross-project generalization is substantially harder, with PR-AUC around 0.436. We further report ablations, test-only identifier-renaming robustness, and end-to-end efficiency. The results suggest that simple token and metric features provide a useful transparent baseline, but also expose sensitivity to superficial lexical cues and limited cross-project transfer.

---


### 56. [Imagery Dataset for Remaining Useful Life Estimation of Synthetic Fibre Ropes](https://arxiv.org/abs/2605.04262)

**<font color=#1a73e8>作者：</font>** Anju Rani, Daniel Ortiz-Arroyo, Petar Durdevic  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remaining useful life (RUL) estimation of synthetic fibre ropes (SFRs) is critical for safe operation in offshore-crane, wind turbine installation, and heavy-load handling applications, where rope failure can result in catastrophic safety incidents and costly downtime. Despite growing research interest in data-driven condition monitoring, there is no publicly available image dataset that captures the complete degradation lifecycle of SFRs under controlled cyclic fatigue loading. To address this gap, we present a novel image dataset comprising approximately 34,700 high-resolution images of eleven Dyneema SK75/78 high-modulus polyethylene (HMPE) rope samples subjected to cyclic fatigue on a sheave-bend test stand at seven distinct axial load levels ranging from 60 kN to 280 kN. Ropes were loaded until mechanical failure, with fatigue lifetimes ranging from 695 cycles to 8,340 cycles. After every fixed number of sheave cycles (an inspection burst), ten images were captured at different cross-sectional positions along the rope, providing spatially representative sampling of surface degradation throughout the rope's entire service life. The images obtained from each load are annotated with the corresponding elapsed cycle count, enabling a direct computation of RUL for any rope in the sequence. This dataset aims to support a broad range of machine learning (ML) tasks including RUL regression, damage progression modelling, anomaly detection, and load-conditioned prognostics. The dataset is intended to serve as a benchmark resource for the development and comparison of vision-based condition monitoring (CM) and prognostics algorithms for SFRs.

---


### 57. [Parallel Prefix Verification for Speculative Generation](https://arxiv.org/abs/2605.04263)

**<font color=#1a73e8>作者：</font>** Yuncheng Yao, Yuxuan Xia, Shengjie Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce PARSE (PArallel pRefix Speculative Engine), a speculative generation framework that accelerates large language model (LLM) inference by parallelizing prefix verification on a semantic level. Existing speculative decoding methods are fundamentally limited by token-level equivalence: the target model must verify each token, leading to short acceptance lengths and modest speedups. Moving to semantic or segment-level verification can substantially increase acceptance granularity, but prior approaches rely on sequential verification, introducing significant overhead and limiting practical gains. PARSE introduces parallel prefix verification, enabling semantic-level verification without sequential checks. Given a full draft from a draft model, the target model evaluates correctness across multiple prefixes in a single forward pass using a custom attention mask, directly identifying the maximal valid prefix. This eliminates sequential segment verification, and makes verification compute-efficient. PARSE is orthogonal to token-level speculative decoding and can be composed with it for additional gains. Across models and benchmarks, PARSE delivers $1.25\times$ to $4.3\times$ throughput gain over the target model, and $1.6\times$ to $4.5\times$ when composed with EAGLE-3, all with negligible accuracy degradation. This demonstrates parallel prefix verification as an effective, general approach to accelerating LLM inference.

---


### 58. [QUIVER: Cost-Aware Adaptive Preference Querying in Surrogate-Assisted Evolutionary Multi-Objective Optimization](https://arxiv.org/abs/2605.04267)

**<font color=#1a73e8>作者：</font>** Florian A. D. Burnat  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interactive multi-objective optimization systems face a budget allocation dilemma: one can spend resources on expensive objective evaluations or on eliciting decision-maker preferences that identify the relevant region of the Pareto set. Moreover, preference elicitation itself spans modalities with different information content and cognitive burden, ranging from cheap, noisy pairwise preference statements (PS) to richer but costlier indifference adjustments (IA).
We study cost-aware optimization under an unknown scalarization and introduce QUIVER (Query-Informed Value Estimation for Regret), a surrogate-assisted evolutionary multi-objective optimizer that adaptively chooses between objective evaluations and heterogeneous preference queries. At each step, QUIVER selects the next action by maximizing the expected decision-quality improvement per unit total cost. Across DTLZ and WFG benchmarks under synthetic decision-maker models, QUIVER achieves the lowest final utility regret on challenging WFG problems (utility regret of 2.14 on WFG4, 2.82 on WFG9: a 25% improvement over baselines), outperforming all single-modality baselines. We analyze how the optimal mix of PS and IA adapts to problem difficulty: on easy problems (DTLZ2), QUIVER selects 80\% PS queries; on hard problems (WFG9), it shifts to 35% IA queries. This adaptive modality selection demonstrates cost-aware preference learning in action.

---


### 59. [OPENJ: A Conceptual Framework for Open-Source Digital Human Modeling and Ergonomic Assessment in a CAD Environment](https://arxiv.org/abs/2605.04270)

**<font color=#1a73e8>作者：</font>** Sinan Bank, Casey E. Eaton  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Industrial workplace challenges range from musculoskeletal disorders -- a leading cause of occupational injury -- to suboptimal workstation layouts, inefficient task sequences, and poor human-equipment fit. Digital human modeling (DHM) tools address several of these challenges by placing a scalable virtual mannequin in a computer-aided design (CAD) environment, enabling engineers to evaluate ergonomic risk through standardized assessment methods (RULA, REBA, NIOSH Lifting Equation, OWAS), optimize workstation layouts for reach and visibility, predict task postures through inverse kinematics, and simulate operations before physical implementation. Despite four decades of development since the Jack system originated at the University of Pennsylvania in the 1980s, the integrated DHM capability set -- anthropometric mannequin, posture prediction, ergonomic assessment, and CAD integration -- remains exclusive to commercial platforms such as Siemens Tecnomatix Jack (Process Simulate), Dassault DELMIA, Humanetics RAMSIS, and the University of Iowa's Santos system. These platforms operate under proprietary, vendor-quoted pricing models, and their acquisition and operating costs, together with closed-source implementations, have been repeatedly identified as practical adoption barriers for individual researchers, small-to-medium enterprises, and educational institutions. Organizations without access resort to manual observational methods -- paper-based worksheets applied to photographs or video -- sacrificing the predictive power and reproducibility that computational analysis provides. The paper serves as a design blueprint for (OpenJane/Joe), positioning the project for subsequent open-source implementation and community adoption.

---


### 60. [A Mean Curvature Approach to Boundary Detection: Geometric Insights for Unsupervised Learning](https://arxiv.org/abs/2605.04274)

**<font color=#1a73e8>作者：</font>** Alexandre L. M. Levada  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate boundary detection in high-dimensional data remains a central challenge in unsupervised learning, particularly in the presence of non-linear structures and heterogeneous densities. In this work, we introduce Mean Curvature Boundary Points (MCBP), a novel geometric framework grounded in Geometric Machine Learning that departs from traditional density-based approaches by explicitly modeling the intrinsic curvature of the data manifold. The method relies on a discrete approximation of the shape operator, estimated from local k-nearest neighbor patches, to compute pointwise mean curvature without requiring explicit manifold parametrization. The key insight of MCBP is to use mean curvature as a principled descriptor of boundary structure: high-curvature regions naturally correspond to transitions between clusters, geometric irregularities, and low-density interfaces. This yields a unified geometric interpretation of boundary, outlier, and transition points. We further introduce an adaptive percentile-based thresholding scheme that enables multiscale boundary extraction without relying on ad hoc density parameters. Beyond detection, we propose a curvature-driven data decomposition that separates samples into smooth (low-curvature) and boundary (high-curvature) subsets, effectively acting as a non-linear geometric filtering mechanism. This representation enhances cluster separability and improves the robustness of downstream unsupervised algorithms. Extensive experiments on synthetic and real-world datasets demonstrate that MCBP consistently improves clustering performance, particularly in complex and high-dimensional scenarios. These results position MCBP as a concrete contribution to Geometric Machine Learning, highlighting the potential of curvature-aware analysis as a unifying paradigm bridging differential geometry and data-driven modeling.

---


### 61. [Gradient Flow Structure and Quantitative Dynamics of Multi-Head Self-Attention](https://arxiv.org/abs/2605.04279)

**<font color=#1a73e8>作者：</font>** Ayan Pendharkar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformer self-attention can be interpreted as a gradient flow on the unit sphere, in which tokens evolve under softmax interaction potentials and tend to form clusters. While prior work has established clustering behavior for single-head attention, the multi-head setting remains less understood due to geometric interference between heads, which invalidates standard monotonicity arguments.
In this work, we develop a theoretical framework for multi-head self-attention dynamics and resolve several open questions. We show that, under suitable conditions on the score matrices, a natural multi-head energy functional is non-decreasing along both flat and spherical dynamics. We identify the key obstruction to per-head monotonicity as radial shadow terms, which are projections of each head's output onto token directions, persisting even under orthogonality assumptions. We introduce a sufficient condition ensuring monotonicity and establish robustness to approximate orthogonality.
In a simplified scalar-head regime with equiangular token configurations, we derive a closed-form expression for the critical inverse temperature governing clustering behavior, and show that heterogeneous heads exhibit super-additive clustering rates. In this regime, we also prove a separation in clustering time between ReLU and softmax attention in the linearized dynamics. Finally, we establish an entropy production identity and show that attention entropy increases monotonically toward equilibrium as clustering progresses.
Our results provide a unified perspective on the dynamics of multi-head attention and clarify the mechanisms underlying clustering and stability in transformer models.

---


### 62. [Revocation-Ready CP-ABE Key Management for Blockchain-Based IoT Data Sharing](https://arxiv.org/abs/2605.04280)

**<font color=#1a73e8>作者：</font>** Chun Yin Chiu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blockchain-based IoT data sharing systems increasingly adopt a hybrid architecture in which a permissioned ledger stores tamper-evident metadata while encrypted payloads are placed in content-addressed storage. In such systems, a central security bottleneck is key access control: enforcing dynamic, multi-user authorization for releasing or using bulk-data decryption keys. Existing designs often rely on always-online RBAC or smart-contract gates that return keys to authorized users, reintroducing a trusted online policy enforcement point and weakening auditability. This paper presents a revocation-ready key management layer that replaces online key release with ciphertext key publication: the ledger records metadata of the form (CID, CK, PolicyID, epoch), where CK is a CP-ABE ciphertext encapsulating an AES-GCM key. Users retrieve CK from the ledger and decrypt locally if their attributes satisfy the policy.
To support forward revocation and policy evolution without re-encrypting large files, the design introduces an epoch/time-bound attribute and a lightweight CK-rotation protocol that updates only small ciphertext keys and ledger entries. We implement a minimal end-to-end prototype using a local content-addressed store, a hash-chained ledger, and a CP-ABE backend, with the goal of isolating key-management costs rather than benchmarking production blockchain throughput. Experiments on a commodity MacBook show that CP-ABE encryption dominates store latency, with approximately 186 ms for a k=6 mixed-Boolean policy, while ledger and storage operations remain around 1-2 ms. Epoch-based revocation amortizes key update cost under churn, gateway-assisted mode reduces median client-side decryption time by more than 4x under a simulated 4x client slow-down, and ledger growth scales with the number of shared assets rather than the number of readers.

---


### 63. [Hardware-Aware Neural Feature Extraction for Resource-Constrained Devices](https://arxiv.org/abs/2605.04282)

**<font color=#1a73e8>作者：</font>** Francesco Tosini, Simone Pedroni, Christian Veronesi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Visual SLAM is a core component of spatial computing systems, yet deploying learned local feature extractors on microcontroller-class hardware remains challenging due to memory, bandwidth, and quantization constraints. While modern neural descriptors provide strong robustness, their practical adoption is often hindered by system-level bottlenecks that are not captured by FLOP-based efficiency metrics. In this work, we introduce Gideon, a hardware-aware neural feature extractor explicitly designed for resource-constrained devices. Our approach combines relational knowledge distillation from a SuperPoint teacher with differentiable neural architecture search (DNAS) under strict memory and operator constraints. Unlike conventional design pipelines, we treat quantization stability and dynamic-range compactness as first-class objectives. We show that architectural choices such as replacing Batch Normalization with affine layers significantly improve INT8 robustness, and that descriptor dimensionality directly governs quantization resilience. Deployed on STM32N6, Gideon achieves 9.003 ms inference time (111 fps) while remaining below a 1.5 MB memory footprint. Remarkably, INT8 quantization induces negligible degradation and occasionally matches full-precision performance. These results demonstrate that robust learned feature extraction can be reconciled with embedded hardware constraints through holistic hardware-algorithm co-design.

---


### 64. [Probabilistic Classification and Uncertainty Quantification of Sahara Desert Climate Using Feedforward Neural Networks](https://arxiv.org/abs/2605.04286)

**<font color=#1a73e8>作者：</font>** Stephen Tivenan, Indranil Sahoo, Yanjun Qian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Climate classification plays a vital role in agricultural planning, hydrological studies, and climate science. One of the most widely used systems for classifying global climate zones is the Köppen-Trewartha (KT) classification. However, the KT classification is fundamentally deterministic, offering discrete labels to spatial locations without accounting for uncertainties in classification. In this paper, we provide a framework for probabilistic modeling of climatic zones. We implement a feedforward artificial neural network (ANN) for classification, allowing for efficient, uncertainty-aware categorization of climatic regions, thereby offering a more nuanced understanding of transitional climate zones compared to traditional deterministic methods. We apply this method to the Sahara Desert region over the 30-year period of 1960 - 1989, using data at more than 400,000 space-time locations from the first 11 years to train our model. We assess the model's short- and long-term classification capabilities to evaluate its stability and accuracy over time. We also compare the probabilistic classification from our model with the traditional KT classification. In addition, we use fluctuation analysis methods to highlight the temporal evolution of climatic zones across the Sahara region and identify areas undergoing significant flux of probabilities of their climate classes, providing insights into broader trends in desertification.

---


### 65. [Beyond Fixed Thresholds and Domain-Specific Benchmarks for Explainable Multi-Task Classification in Autonomous Vehicles](https://arxiv.org/abs/2605.04299)

**<font color=#1a73e8>作者：</font>** Maryam Sadat Hosseini Azad, Shahriar Baradaran Shokouhi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene understanding is a vital part of autonomous driving systems, which requires the use of deep learning models. Deep learning methods are intrinsically black box models, which lack transparency and safety in autonomous driving. To make these systems transparent, multi-task visual understanding has become crucial for explainable autonomous driving perception systems, where simultaneous prediction of multiple driving behaviors and their underlying explanations is essential for safe navigation and human trust in autonomous vehicles. In order to design an accurate and cross-cultural explainable autonomous driving system, we introduce a comprehensive confidence threshold sensitivity analysis that evaluates various threshold values to identify optimal decision boundaries for different tasks. Our analysis demonstrates that traditional fixed threshold approaches are suboptimal for multi-task scenarios. Through extensive evaluation, we demonstrate that our adaptive threshold selection methodology improves F1-scores across different tasks. In addition, we introduce IUST-XAI-AD, a novel dataset consisting of 958 images with human annotations for driving decisions and corresponding reasoning. This dataset addresses the critical gap in domain-specific evaluation benchmarks for distinct driving contexts and provides a more challenging test environment compared to existing datasets. Experimental results demonstrate that confidence threshold sensitivity analysis can significantly improve model performance, while the introduction of the IUST-XAI-AD dataset reveals important insights about cross-cultural driving behavior patterns. The combined contributions of this work provide both methodological advances and practical evaluation tools that can accelerate the development of more reliable, explainable, and culturally-adaptive autonomous driving systems for global deployment.

---


### 66. [Hierarchical Visual Agent: Managing Contexts in Joint Image-Text Space for Advanced Chart Reasoning](https://arxiv.org/abs/2605.04304)

**<font color=#1a73e8>作者：</font>** Qihua Dong, Ruozhen He, Junwen Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Advanced chart question answering requires both precise perception of small visual elements and multi-step reasoning across several subplots. While existing MLLMs are strong at understanding single plots, they often struggle with multi-step reasoning across multiple subplots. We propose HierVA, a hierarchical visual agent framework for chart reasoning that iteratively constructs and updates a working context in a joint image--text space. A high-level manager generates plans and maintains a compact context containing only key information, while specialized workers perform reasoning, gather evidence, and return results. In particular, the agent maintains separate visual and textual contexts, using a zoom-in tool to restrict the visual context. Experiments on the CharXiv reasoning subset demonstrate consistent improvements over strong multimodal baselines, and ablation studies verify that hierarchical architecture, scoped visual context, and distilled context contribute complementary gains.

---


### 67. [SWAN: Semantic Watermarking with Abstract Meaning Representation](https://arxiv.org/abs/2605.04305)

**<font color=#1a73e8>作者：</font>** Ziping Ye, Gourab Dey, Christos Christodoulopoulos 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce SWAN (Semantic Watermarking with Abstract Meaning Representation), a novel framework that embeds watermark signatures into the semantic structure of a sentence using Abstract Meaning Representation (AMR). In contrast to existing watermarking methods, which typically encode signatures by adjusting token selection preferences during text generation, SWAN embeds the signature directly in the sentence's semantic representation. As the signature is encoded at the semantic structure level, any paraphrase that preserves meaning automatically preserves the signature. SWAN is training-free: watermark injection is achieved by prompting an LLM to generate sentences guided by a selected AMR template while maintaining contextual coherence, and detection uses an off-the-shelf AMR parser followed by a simple one-proportion z-test. Empirical evaluation on the RealNews benchmark shows SWAN matches state-of-the-art detection performance on unaltered watermarked text, while significantly improving robustness against paraphrasing, increasing detection AUC by up to 13.9 percentage points compared to prior methods. These results demonstrate that SWAN's approach of anchoring watermarks in AMR semantic structures provides a simple, effective, and prompt-based method for robust text provenance verification under paraphrasing, opening new avenues for semantic-level watermarking research.

---


### 68. [dtour: a steerable tour de vis through high-dimensional data](https://arxiv.org/abs/2605.04306)

**<font color=#1a73e8>作者：</font>** Fritz Lekschas, Nezar Abdennur  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Understanding high-dimensional data requires projecting it into lower-dimensional spaces, but any single projection inevitably loses information or introduces distortions. Tours address this limitation through animation of 2D projection sequences, yet existing tools present tradeoffs in the freedom and steerability of projection traversal, providing little to no ability to move between expert-guided paths and unrestrained exploration. We present dtour, a tour interface that combines static projection previews, reversible scrubbing along continuous geodesic projection paths, manual projection manipulation, and a wandering grand tour, all within a single progressive exploration interface. dtour scales to millions of points via GPU-accelerated rendering, runs in any modern browser, and integrates with both Python and JavaScript ecosystems. We demonstrate dtour on text, image, and single-cell data for two usage scenarios: gradually revealing structure in high-dimensional data and validating non-linear dimensionality reduction outputs.

---


### 69. [Memory as a Markov Matrix: Sample Efficient Knowledge Expansion via Token-to-Dictionary Mapping](https://arxiv.org/abs/2605.04308)

**<font color=#1a73e8>作者：</font>** Kaustubh Pethkar, Ziyang Xiong, Zuofeng Shang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual incorporation of new knowledge is essential for the long-term evolution of large language models (LLMs). Existing approaches typically rely on parameter-update algorithms to mitigate catastrophic forgetting, yet they suffer from fundamental limitations: 1) forgetting is unavoidable as the amount of newly injected knowledge grows; and 2) model updates are often irreversible. As modern LLMs become increasingly expressive, it is natural to question whether large-scale weight updates are necessary for acquiring a small amount of new knowledge. In this work, we propose a principled framework that models autoregressive language generation as a Markov process over tokens, where model memory is represented by a Markov transition matrix. Under this formulation, incorporating new knowledge/tokens corresponds to extending the state space, and preserving existing transitions guarantees retention of previously learned knowledge. We then prove a sample complexity bound for incorporating new tokens via a token-to-dictionary mapping strategy. In particular, for learning the transition behavior of each new token, the required number of samples scales linearly with the number of existing tokens it is mapped to. To realize this mapping, we propose an embedding-tuning algorithm that requires minimal parameter updates and induces zero forgetting. Experimental results further demonstrate the effectiveness of our method and validate our theoretical findings.

---


### 70. [Agent Island: A Saturation- and Contamination-Resistant Benchmark from Multiagent Games](https://arxiv.org/abs/2605.04312)

**<font color=#1a73e8>作者：</font>** Connacher Murphy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Static capabilities benchmarks suffer from saturation and contamination, making it difficult to track capabilities progress over time. We introduce Agent Island, a multiplayer simulation environment in which language-model agents compete in a game of interagent cooperation, conflict, and persuasion. The environment yields a dynamic benchmark designed to mitigate both saturation and contamination; new models can always outperform the current leading player in this winner-take-all game, and agents compete against other adaptive agents rather than face a fixed task set. We rank players with a Bayesian Plackett-Luce model, allowing us to quantify uncertainty in player skill. In 999 games involving 49 unique models, openai/gpt-5.5 dominates its peers with a posterior mean skill of 5.64, compared with 3.10 for the second-ranked model, openai/gpt-5.2, and 2.86 for the third-ranked model, openai/gpt-5.3-codex. We release the game logs as a dataset for analyses of model behavior. As an example, we investigate same-provider preference in final-round votes and find that models are 8.3 p.p. more likely to support a same-provider finalist than finalists from other providers. This preference is not uniform across providers: among separately estimated providers, the effect is strongest for OpenAI models and weakest for Anthropic models.

---


### 71. [NoisyCausal: A Benchmark for Evaluating Causal Reasoning Under Structured Noise](https://arxiv.org/abs/2605.04313)

**<font color=#1a73e8>作者：</font>** Zhi Xu, Yun Fu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Causal reasoning in natural language requires identifying relevant variables, understanding their interactions, and reasoning about effects and interventions, often under noisy or ambiguous conditions. While large language models (LLMs) exhibit strong general reasoning abilities, they struggle to disentangle correlation from causation, particularly when observations are partially incorrect or irrelevant information is present. In this work, we introduce NoisyCausal, a new benchmark designed to evaluate causal reasoning under structured noise. Each instance is generated from a ground-truth causal graph and contextualized with a natural language scenario by injecting controllable forms of noise, such as irrelevant distractors, value perturbations, confounding, and partial observability. Moreover, we propose a modular reasoning framework that combines LLMs with explicit causal structure to address these challenges. Our method prompts the LLM to extract variables, construct a causal graph from context, and then reformulates the reasoning task as a structured prompt grounded in this graph. Rather than relying on statistical patterns alone, the LLM is guided by symbolic structure, enabling more interpretable and robust inference. Experimental results show that our method significantly outperforms standard prompting and reasoning baselines on NoisyCausal. Furthermore, it generalizes well to external benchmarks such as Cladder without task-specific tuning. Our findings highlight the importance of combining causal abstractions with language-driven reasoning to achieve faithful and robust causal understanding in LLMs.

---


### 72. [DeFed-GMM-DaDiL: A Decentralized Federated Framework for Domain Adaptation](https://arxiv.org/abs/2605.04324)

**<font color=#1a73e8>作者：</font>** Rebecca Clain, Eduardo Fernandes Montesuma, Fred Ngole Mboula  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralized multi-source domain adaptation seeks to transfer knowledge from multiple heterogeneous and related source domains to an unlabeled target domain in a decentralized setting. We address this challenge through a fully decentralized federated approach, DeFed-GMM-DaDiL, an extension of the GMM-Dataset Dictionary Learning (DaDiL) framework. Each client models its dataset as a Gaussian Mixture Model (GMM), and the federation jointly approximates them via labeled Wasserstein barycenters of shared, learnable GMM atoms. This design enables adaptation without a central server while preserving clients' privacy. We empirically study the stability of the learned representations in scenarios where the target domain has missing classes. Empirical results demonstrate that DeFed-GMM-DaDiL maintains stable and consistent shared representations across clients, effectively reconstructs missing classes, and achieves competitive performance on multi-source domain adaptation benchmarks.

---


### 73. [On the Architectural Complexity of Neural Networks](https://arxiv.org/abs/2605.04325)

**<font color=#1a73e8>作者：</font>** Nicholas J. Cooper, François G. Meyer, Michael L. Roberts 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a unified theoretical framework for the rigorous analysis and systematic construction of deep neural networks (DNNs). This framework addresses a gap in existing theory by explicitly modeling the structure of tensor operations -- lower level information that is often abstracted. Our framework enables two novel objectives: (1) analysis of the evolution of architectural complexity over deep learning history, and (2) automatic construction of novel architectures based on new types of tensor operations. Our study of DNNs introduced over the past 40 years reveals a connection between groundbreaking architectures and increases in different types of architectural complexity. Moreover, we identify several large classes of higher complexity architectures that have not yet been explored. We then collect a dataset of 3,000+ higher complexity architectures, which we publicly release at: this https URL.

---


### 74. [The Scaling Properties of Implicit Deductive Reasoning in Transformers](https://arxiv.org/abs/2605.04330)

**<font color=#1a73e8>作者：</font>** Enrico Vompa, Tanel Tammet  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We investigate the scaling properties of implicit deductive reasoning over Horn clauses in depth-bounded Transformers. By systematically decorrelating provability from spurious features and enforcing algorithmic alignment, we find that in sufficiently deep models with a bidirectional prefix mask, implicit reasoning approaches explicit CoT performance across graph topologies and problem widths, though CoT remains necessary for depth extrapolation.

---


### 75. [Learning-based Statistical Refinement for Denoising](https://arxiv.org/abs/2605.04332)

**<font color=#1a73e8>作者：</font>** Rihuan Ke  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work proposes a learning-based statistical refinement method for improving the denoising results of a given denoiser without knowing the precise noise distribution or accessing clean images or calibration data. While there are many existing successful denoising approaches for handling different kinds of noise, they typically require accurate modelling of the images and the noise (implicitly or explicitly), and hence the denoising results can be suboptimal due to different practical factors such as imperfect models, unreliable noise assumptions, or low quality data. In particular, when clean image samples are not available and there is a lack of knowledge of the underlying noise distribution, which is the case in various practical situations, the results may not well align with the noise statistics. The unawareness of the useful statistical information leads to suboptimal results. This work aims to make the best use of the statistical information to improve the consistency between the given denoising results and the noise statistics, under the assumption that the noise is conditionally pixel-wise independent given the clean signal. A method, based on a Bayesian formulation of an auxiliary signal in the noisy data, is proposed for evaluating the consistency of the denoising results, without precise information on noise distribution. By leveraging the statistical information from noisy data, the method enhances the statistical noise consistency and improves denoising quality.

---


### 76. [Structural Equivalence and Learning Dynamics in Delayed MARL](https://arxiv.org/abs/2605.04345)

**<font color=#1a73e8>作者：</font>** Jules Sintes, Ana Bušić, Jiamin Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We formally establish the equivalence between Observation Delay (OD) and Action Delay (AD) in cooperative partially observable multi-agent systems using observation-action histories. We show that both systems generate identical admissible joint-policy sets, and their induced state-action-observation trajectories are identical in distribution, leading to identical optimal solutions in Decentralized Partially Observable Markov Decision Processes (Dec-POMDPs). This formally generalizes existing infinite-horizon single-agent results to any-horizon partially observable cooperative multi-agent problems with decentralized policy execution, and allows any mixed-delay configuration to be reduced to a pure OD system. We further prove that in Transition-Independent MDPs (TI-MDPs), the observation-action history reduces to a tractable minimal local augmented state.
However, we show through numerical experiments that although the optimal solution spaces are structurally isomorphic, the practical learning dynamics are fundamentally different. First, using the minimal local augmented state, the equivalence no longer holds when transitions are not independent. Second, operational constraints and causal credit-assignment errors in Temporal Difference (TD) algorithms induce different learning behaviors across regimes. Finally, leveraging this structural equivalence to bypass these learning challenges, we demonstrate successful multi-agent zero-shot policy transfer from OD to AD, paving the way for unified, efficient solution methods in complex delayed systems.

---


### 77. [Covariance-Aware Goodness for Scalable Forward-Forward Learning](https://arxiv.org/abs/2605.04346)

**<font color=#1a73e8>作者：</font>** Xiaoyi Jiang, Bashir M. Al-Hashimi, Kai Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Forward-Forward algorithm eliminates global gradient flow and full network activations storage. However, in convolutional settings, existing BP-free FF methods significantly under-perform backpropagation on complex benchmarks such as ImageNet-100 and Tiny-ImageNet. We identify this gap as a structural bottleneck in goodness extraction: standard sum-of-squares formulation collapses feature volumes into channel-wise activation energies which omits critical second-order dependencies. To address this, we propose a framework centered on three key components. First, Bi-axis Covariance Goodness(BiCovG) explicitly augments the standard goodness function with structured second-order information along two axes: cross-channel projections that model inter-feature covariance, and nested multi-scale aggregation that encodes spatial correlation statistics. This provides a tractable approximation to covariance-aware goodness without the prohibitive O(C^2) complexity of explicit matrix estimation. Second, a lightweight Logistic Fusion module aggregates layer-wise predictions, amplifying the contribution of deeper representations. Third, the Feature Alignment Layer(FAL) introduces a zero-initialized correction at block boundaries to mitigate representation misalignment in deep locally trained networks. By introducing these three components, we effectively double the depth of viable Forward-Forward learning, extending robust layer utilization from shallow baselines to 16 layer architectures like VGG-16. The resulting BP-free model achieves 73.01% on ImageNet-100 and 50.30% on Tiny-ImageNet. As a practical extension, Hybrid Goodness Blocks control the scope of gradient propagation via configurable block sizes, further narrowing the ImageNet-100 gap to 3.6% and matching BP on Tiny-ImageNet, while still reducing peak memory by approximately 50% relative to BP.

---


### 78. [InterFuserDVS: Event-Enhanced Sensor Fusion for Safe RL-Based Decision Making](https://arxiv.org/abs/2605.04355)

**<font color=#1a73e8>作者：</font>** Mustafa Sakhaia, Kaung Sithua, Min Khant Soe Okea 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous driving systems rely heavily on robust sensor fusion to perceive complex envi- ronments. Traditional setups using RGB cameras and LiDAR often struggle in high-dynamic- range scenes or high-speed scenarios due to motion blur and latency. Dynamic Vision Sensors (DVS), or event cameras, offer a paradigm shift by capturing asynchronous brightness changes with microsecond temporal resolution and high dynamic range. In this paper, we propose an extended architecture of the state-of-the-art InterFuser model, integrating DVS as an additional modality to enhance perception reliability. We introduce a novel token-based fusion strategy that incorporates accumulated event frames into the transformer-based backbone of InterFuser. Our method leverages the complementary nature of RGB, LiDAR, and DVS data. We evaluate our approach on the Car Learning to Act (CARLA) Leaderboard benchmarks, demonstrating that the inclusion of DVS improves the robustness of the driving agent, achieving a competitive Driving Score of 77.2 and a superior Route Completion of 100%. The results indicate that event-based vision is a promising direction for improving safety and performance in adverse lighting and dynamic conditions.

---


### 79. [Intermediate Representations are Strong AI-Generated Image Detectors](https://arxiv.org/abs/2605.04358)

**<font color=#1a73e8>作者：</font>** Zhenhan Huang, Pin-Yu Chen, Tejaswini Pedapati 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement in generative AI models has enabled the creation of photorealistic images. At the same time, there are growing concerns about the potential misuse and dangers of generated content, as well as a pressing need for effective AI-generated image detectors. However, current training-based detection techniques are typically computationally costly and can hardly be generalized to unseen data domains, while training-free methods fall short in detection performance. To bridge this gap, we propose a search-based method employing data embedding sensitivity in intermediate layers to detect AI-generated images. Given a set of real and AI-generated images, our method examines the similarity between original image embeddings and perturbed image embeddings, and detects AI-generated images based on the similarity. We examine the proposed method on two comprehensive benchmarks: GenImage and Forensics Small. Our method exhibits improved performance across different datasets compared to both training-free and training-based state-of-the-art methods. On average, our method achieves the largest performance gain on the Forensics Small benchmark by 39.61% compared to the best training-free method and 5.14% compared to the best training-based method in AUROC score.

---


### 80. [When Context Hurts: The Crossover Effect of Knowledge Transfer on Multi-Agent Design Exploration](https://arxiv.org/abs/2605.04361)

**<font color=#1a73e8>作者：</font>** Saranyan Vigraham  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The prevailing assumption in agent orchestration is that more context is better. We test this on multi-agent software design across 10 tasks, 7 context-injection conditions, and over 2,700 runs, and find a crossover effect: the same artifact type improves design exploration on some tasks (up to 20$\times$ tradeoff coverage) and actively degrades it on others (up to 46% reduction). On several tasks, an irrelevant document performs as well as or better than every relevant artifact. The direction is predicted by a single measurable variable--baseline exploration without context--with Pearson $r = -0.82$ ($p < 0.001$). Probing the mechanism by manipulating convergence pressure through prompt design reveals two distinct regimes: convergence driven by training data priors (natural) responds to artifact disruption, while convergence driven by explicit instructions (induced) does not. The implication is that context injection should be conditional, not universal: one no-context trial is a cheap diagnostic that predicts whether knowledge artifacts will help or hurt a given task.

---


### 81. [Online Nonstochastic Prediction: Logarithmic Regret via Predictive Online Least Squares](https://arxiv.org/abs/2605.04364)

**<font color=#1a73e8>作者：</font>** Chih-Fan Pai, Yang Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study online prediction for marginally stable, partially observed linear dynamical systems under nonstochastic disturbances. Our objective is to minimize the cumulative squared prediction loss and compete with the best-in-hindsight Luenberger predictor. Standard online learning methods typically rely on bounded domains/gradients, and thus their guarantees may fail to deal with potentially unbounded trajectories in marginally stable systems. In this paper, we introduce an unconstrained online least squares method that stabilizes the learning process via tailored predictive hints. With model knowledge, we prove that hints constructed from any stabilizing Luenberger predictor render the hint residuals uniformly bounded, achieving logarithmic regret despite unbounded trajectory growth. We also discuss model-free prediction and introduce a simple universal hint for symmetric systems, under which logarithmic regret is maintained without model knowledge. Our results provide an adaptive, instance-wise optimal online predictor compared to classical fixed-gain observers under nonstochastic disturbances.

---


### 82. [Extending Differential Temporal Difference Methods for Episodic Problems](https://arxiv.org/abs/2605.04368)

**<font color=#1a73e8>作者：</font>** Kris De Asis, Mohamed Elsayed, Jiamin He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differential temporal difference (TD) methods are value-based reinforcement learning algorithms that have been proposed for infinite-horizon problems. They rely on reward centering, where each reward is centered by the average reward. This keeps the return bounded and removes a value function's state-independent offset. However, reward centering can alter the optimal policy in episodic problems, limiting its applicability. Motivated by recent works that emphasize the role of normalization in streaming deep reinforcement learning, we study reward centering in episodic problems and propose a generalization of differential TD. We prove that this generalization maintains the ordering of policies in the presence of termination, and thus extends differential TD to episodic problems. We show equivalence with a form of linear TD, thereby inheriting theoretical guarantees that have been shown for those algorithms. We then extend several streaming reinforcement learning algorithms to their differential counterparts. Across a range of base algorithms and environments, we empirically validate that reward centering can improve sample efficiency in episodic problems.

---


### 83. [$p$-adic Manifold Learning and Benchmark Tasks from Impartial Games](https://arxiv.org/abs/2605.04374)

**<font color=#1a73e8>作者：</font>** Tomoki Mihara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce $p$-adic manifold learning, propose an algorithm to solve it, and propose benchmark tasks from impartial games.

---


### 84. [GraphPI: Efficient Protein Inference with Graph Neural Networks](https://arxiv.org/abs/2605.04376)

**<font color=#1a73e8>作者：</font>** Zheng Ma, Jiazhen Chen, Lei Xin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The integration of deep learning approaches in biomedical research has been transformative, enabling breakthroughs in various applications. Despite these strides, its application in protein inference is impeded by the scarcity of extensively labeled datasets, a challenge compounded by the high costs and complexities of accurate protein annotation. In this study, we introduce GraphPI, a novel framework that treats protein inference as a node classification problem. We treat proteins as interconnected nodes within a protein-peptide-PSM graph, utilizing a Graph Neural Network-based architecture to elucidate their interrelations. To address label scarcity, we train the model on a set of unlabeled public protein datasets with pseudo-labels derived from an existing protein inference algorithm, enhanced by self-training to iteratively refine labels based on confidence scores. Contrary to prevalent methodologies necessitating dataset-specific training, our research illustrates that GraphPI, due to the well normalized nature of Percolator features, exhibits universal applicability without dataset-specific fine-tuning, a feature that not only mitigates the risk of overfitting but also enhances computational efficiency. Our empirical experiments reveal notable performance on various test datasets and deliver significantly reduced computation times compared to common protein inference algorithms.

---


### 85. [Critical Windows of Complexity Control: When Transformers Decide to Reason or Memorize](https://arxiv.org/abs/2605.04396)

**<font color=#1a73e8>作者：</font>** Sarwan Ali  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that Transformers' compositional generalization is governed by \emph{complexity control}, initialization scale and weight decay, which steers training toward low-complexity reasoning solutions rather than high-complexity memorization. Existing analyses, however, treat complexity control as a single static hyperparameter choice, leaving open \emph{when} during training this control is actually decisive. We show that the memorization-versus-reasoning fate of a Transformer is determined within a sharp, identifiable window of training. On a controlled compositional task we find that (i)~weight decay applied for a single 25\%-of-training window matches full-training weight decay in out-of-distribution (OOD) accuracy ($0.93$ vs $0.91$); (ii)~holding total regularization budget constant, placing it in the middle of training yields $5{-}9\times$ higher OOD accuracy than placing it early; (iii)~the boundary of the critical window is remarkably sharp, window onset shifted by as little as $100$ optimization steps causes mean OOD to jump from chance ($0.15$) to reasoning-regime ($0.61$); (iv)~the window's position depends systematically on initialization scale, but the basin of attraction for reasoning solutions \emph{shrinks} at small initialization, contradicting the prevailing recommendation that smaller initialization is uniformly better. We further show that the critical-window phenomenon is task-specific: it does not appear on grokking with modular arithmetic, where properly tuned constant weight decay matches scheduled weight decay.

---


### 86. [Optimize-at-Capture: Highly-adaptive Exposure Controlling for In-Vehicle Non-contact Heart-rate Monitoring](https://arxiv.org/abs/2605.04397)

**<font color=#1a73e8>作者：</font>** Jieying Wang, Xinqi Cai, Caifeng Shan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote photoplethysmography (rPPG) holds great promise for continuous heart-rate monitoring of drivers in intelligent vehicles. However, its performance is severely degraded by the highly dynamic illumination changes. A critical yet overlooked factor is the lack of exposure controlling during video acquisition -- most existing systems rely on either fixed exposure settings or camera build-in auto-exposure, both of which fail to maintain stable facial brightness under rapidly changing lighting conditions during driving. To address this gap, we propose a highly-adaptive exposure controlling framework that proactively adjusts exposure parameters based on predictive modeling of historical skin reflections. Unlike standard auto-exposure, our method is specifically optimized for rPPG measurement, ensuring the skin region of interest (ROI) remains within the optimal dynamic range for rPPG signal extraction. As an important contribution of this study, we introduce ExpDrive, a public in-vehicle physiological monitoring dataset comprising synchronized facial video and reference ECG from 48 subjects captured under real driving conditions. Extensive experiments demonstrate that our method consistently outperforms fixed exposure and standard auto-exposure strategies. Specifically, it reduces the Mean Absolute Error (MAE) by 6.31 bpm (from 14.1 to 7.79 bpm) and significantly increases the success rate by 32.3 percentage points (p < 0.001) (from 24.9% to 57.2%) across challenging driving scenarios. Notably, it clearly improved the performance of non-contact heart-rate monitoring in both low-light (rainy) and high-glare (sunny) conditions, validating the efficacy of exposure-aware acquisition design.

---


### 87. [Detecting Deepfakes via Hamiltonian Dynamics](https://arxiv.org/abs/2605.04405)

**<font color=#1a73e8>作者：</font>** Harry Cheng, Ming-Hui Liu, Tianyi Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driven by the rapid development of generative AI models, deepfake detectors are compelled to undergo periodic recalibration to capture newly developed synthetic artifacts. To break this cycle, we propose a new perspective on deepfake detection: moving from static pattern recognition to dynamical stability analysis. Specifically, our approach is motivated by physics-inspired priors: we hypothesize that natural images, as products of dissipative physical processes, tend to settle near stable, low-energy equilibria. In contrast, generative models optimize for statistical similarity to real images but do not explicitly enforce structural constraints such as geometric smoothness, leaving deepfakes more likely to occupy unstable, high-energy states. To operationalize this, we introduce Hamiltonian Action Anomaly Detection (HAAD), comprising three contributions: \textbf{i)} We model the image latent manifold as a potential energy surface. Under this hypothesis, real images are expected to produce basin-like low-energy responses, whereas fake images are more likely to induce high-potential, high-gradient responses. \textbf{ii)} We employ Hamiltonian-inspired dynamics as a stability probe. By releasing latent states from rest, samples near stable regions remain bounded, while high-gradient samples produce larger trajectory responses. \textbf{iii)} We quantify these dynamic behaviors through two trajectory statistics, \ie, Hamiltonian action and energy dissipation. Extensive experiments show that HAAD outperforms evaluated state-of-the-art baselines on challenging cross-dataset transfer benchmarks, supporting a physics-inspired stability prior for digital forensics.

---


### 88. [Beyond Rigid Geometries: The Spline-Pullback Metric for Universal Diffeomorphic SPD Representation Learning](https://arxiv.org/abs/2605.04406)

**<font color=#1a73e8>作者：</font>** Tushar Das, Subrata Dutta, Sarmistha Neogy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The integration of Symmetric Positive Definite (SPD) matrices into deep learning has historically relied on fixed algebraic Riemannian metrics. Analogous to hand-crafted features in classical machine learning, these static formulations impose rigid geometries limiting network expressivity and adaptability. Recent attempts to parameterize these geometries often violate the axioms of primary matrix functions through unconstrained powers or rank-dependent scaling, inviting spatial folding, loss of global surjectivity, and gradient collapse at spectral singularities. In this paper, we introduce the Spline-Pullback Metric (SPM), instantiated as Spectral-SPM and Cholesky-SPM, marking a paradigm shift from static metric selection to universal geometric approximation. By parameterizing the global diffeomorphism via a rank-invariant, monotonically constrained B-spline, SPM acts as a dense universal approximator for strictly increasing $C^1$ diffeomorphisms and theoretically subsumes existing pullback metrics while enabling localized non-linear spectral modelling. Topologically, SPM provides a globally bijective pullback geometry precluding rank-swapping discontinuities and gradient instabilities. Empirically, SPM achieves a state-of-the-art performance across 3 datasets utilizing Linear Probes, SPDNets, and deep Riemannian ResNets.

---


### 89. [Assessing Generalisation Capability of Machine Learning Models for Intrusion Detection](https://arxiv.org/abs/2605.04407)

**<font color=#1a73e8>作者：</font>** Md Zakir Hossain, Md Ayshik Rahman Khan, Md Rafiqul Islam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The growth of networked and IoT systems has intensified cyber-security threats and exposed the limits of traditional signature-based intrusion detection. Although machine-learning-based intrusion detection systems often report strong benchmark performance, high ac- curacy within a single dataset does not necessarily guarantee reliable performance in unseen network environments. This study investigates the generalisation capability of supervised machine learning models for intrusion detection using UNSW-NB15 and TON_IoT. Random Forest, Logistic Regression, and Naive Bayes were evaluated under same-dataset and cross-dataset settings. Random Forest achieved the strongest same dataset performance, with 95.08% accuracy on UNSW-NB15 and 99.79% on TON_IoT, but performance dropped sharply in cross-dataset testing. When trained on UNSW-NB15 and tested on TON_IoT or vice versa, below 40% accuracy. These results reveal a significant generalisation gap in intrusion detection. We connect this challenge to affective computing and human-centric AI, where behavioural signal analysis, anomaly detection, domain shift, and context-sensitive modelling are also central. This framing highlights the need for adaptive, generalisable cyber-security models that can operate across changing network and IoT environments.

---


### 90. [UAV as Urban Construction Change Monitor: A New Benchmark and Change Captioning Model](https://arxiv.org/abs/2605.04409)

**<font color=#1a73e8>作者：</font>** Yupeng Gao, Tianyu Li, Guoqing Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote Sensing Image Change Captioning (RSICC) aims to generate spatially grounded natural language descriptions of scene evolution from bi-temporal imagery, moving beyond binary change masks toward semantic-level understanding. However, existing methods rely on implicit feature differencing without explicitly modeling structured change semantics, and struggle to reconcile the conflicting representation demands of change detection and caption generation. In addition, current benchmarks provide limited coverage of high-resolution urban construction scenarios. To address these challenges, we propose PTNet, a prototype-guided task-adaptive framework for joint change captioning and detection. PTNet explicitly models structured change semantics through a learnable prototype bank that guides cross-temporal interaction, disentangles task-specific representations via multi-head gating, and injects detection-derived spatial priors into caption generation, enabling coherent semantic correspondence while preserving fine-grained spatial sensitivity. Furthermore, we construct UCCD, a large-scale UAV-based benchmark comprising 9,000 high-resolution image pairs and 45,000 annotated sentences for urban construction monitoring. Extensive experiments on UCCD and WHU-CDC demonstrate that PTNet consistently outperforms existing methods. The dataset and source code are publicly available at this https URL.

---


### 91. [Evaluation Cards for XAI Metrics](https://arxiv.org/abs/2605.04410)

**<font color=#1a73e8>作者：</font>** Rokas Gipiškis, Olga Kurasova  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The evaluation of explainable AI (XAI) methods is affected by a lack of standardization. Metrics are inconsistently defined, incompletely reported, and rarely validated against common baselines. In this paper, we identify transparency of evaluation reporting as a central, under-addressed problem. We propose the XAI Evaluation Card, a documentation template analogous to model cards, designed to accompany any study that introduces an XAI evaluation metric. The card covers explicit declaration of target properties, grounding levels, metric assumptions, validation evidence, gaming risks, and known failure cases. We argue that adopting this template as a community norm would reduce evaluation fragmentation, support meta-analysis, and improve accountability in XAI research.

---


### 92. [Structured 3D Latents Are Surprisingly Powerful: Unleashing Generalizable Style with 2D Diffusion](https://arxiv.org/abs/2605.04412)

**<font color=#1a73e8>作者：</font>** Yiran Qiao, Yiren Lu, Yunlai Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D asset generation plays a pivotal role in fields such as gaming and virtual reality, enabling the rapid synthesis of high-fidelity 3D objects from a single or multiple images. Building on this capability, enabling style-controllable generation naturally emerges as an important and desirable direction. However, existing approaches typically rely on style images that lie within or are similar to the training distribution of 3D generation models. When presented with out-of-distribution (OOD) styles, their performance degrades significantly or even fails. To address this limitation, we introduce $\textbf{DiLAST}$: 2D Diffusion-based Latent Awakening for 3D Style Transfer. Specifically, we leverage a pretrained 2D diffusion model as a teacher to provide rich and generalizable style priors. By aligning rendered views with the target style under diffusion-based guidance, our method optimizes the structured 3D latent representation for stylization. We observe that this limitation stems not from insufficient model capacity, but from the underutilization of structured 3D latents, which are inherently expressive. Despite being trained on comparatively limited data, 3D generation models can leverage 2D diffusion guidance to steer denoising toward specific directions in latent space, thereby producing diverse, OOD styles. Extensive experiments across diverse data and multiple 3D generation backbones demonstrate the effectiveness and plug-and-play nature of our approach.

---


### 93. [Counterfactual identifiability beyond global monotonicity: non-monotone triangular structural causal models](https://arxiv.org/abs/2605.04413)

**<font color=#1a73e8>作者：</font>** Pengcheng Tan, Jiang Chen, Dehui Du  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structural causal models provide a unified semantics for interventions and counterfactuals, but most identifiability results rely on restrictive assumptions like global monotonicity, which are often violated in embodied interaction, where the same exogenous perturbation can induce opposite responses under different contact contexts. We ask what structure still suffices once global monotonicity is dropped. We introduce non-monotone triangular structural causal models (NM-TM-SCM), which retain triangular recursion but replace global monotonicity with mechanism-wise invertibility and context-independent inverse transport. We prove that these conditions are equivalent to exogenous isomorphism and imply complete counterfactual identifiability, and we give a counterexample showing that local invertibility alone is insufficient. We instantiate the theory in CausalInverter, with triangular invertible layers, orientation gates, and transport-stability regularization. On synthetic non-monotonic mechanisms, the structural bias yields systematic counterfactual gains as non-monotonicity increases. On MuJoCo Door, our model achieves perfect event-level counterfactual recovery, lowers continuous angle error relative to a Transformer baseline, and delivers substantially more stable recovery than Transformer and conditional-flow predictors. On MuJoCo Push, where non-monotonicity is weaker, the same low-data predictors remain competitive or better, consistent with a bias-variance boundary. These results identify a broader identifiable regime between globally monotone triangular models and unconstrained black-box world models.

---


### 94. [FLUID: Continuous-Time Hyperconnected Sparse Transformer for Sink-Free Learning](https://arxiv.org/abs/2605.04421)

**<font color=#1a73e8>作者：</font>** Waleed Razzaq, Yun-Bo Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous-time (CT) Transformers improve irregular and long-range modeling over CT-RNNs by exploiting inputs or outputs embeddings with continuous dynamics. However, the core scaled-dot-product-attention (SDPA) mechanism remains inherently discrete. We propose FLUID (Flexible Unified Information Dynamics), a CT Transformer that incorporates continuous dynamics directly into the attention computation by replacing it with Liquid Attention Network (LAN). LAN reinterprets attention logits as continuous dynamical system and reformulates them as the solution to a linear ODE modulated by input-dependent nonlinear recurrent gates. Theoretically, we establish stability guarantees for LAN dynamics and show that it serves as an interpolating middle ground between SDPA and CT-RNNs, recovering each as special case under well-defined parameterization of its gating functions. LAN also introduces an explicit attention-sink gate to eliminate disproportionate attention mass on uninformative nodes. FLUID replaces standard residual connections with input-dependent Liquid Hyper-Connections to adaptively regulate interlayer information flow. Empirically, we evaluate FLUID on a broad set of learning tasks, including (i) irregular time-series, (ii) long-range modeling, (iii) lane-keeping control of autonomous vehicles, and (iv) learning physical dynamics under a scarce data regime. Across all the tasks, FLUID consistently matches or outperforms CT baselines, achieving improvements of up to 47% in certain scenarios and enhancing generalization under distributional shifts. Additionally, FLUID demonstrates superior noise robustness and a self-correcting inductive bias in autonomous vehicle control. We also provide a detailed analysis of key hyperparameters to guide tuning and show that FLUID occupies an intermediate position among competing approaches in terms of runtime and memory efficiency.

---


### 95. [Telegraph English: Semantic Prompt Compression via Structured Symbolic Rewriting](https://arxiv.org/abs/2605.04426)

**<font color=#1a73e8>作者：</font>** Mikhail L. Arbuzov, Sisong Bei, Ziwei Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Telegraph English (TE), a prompt-compression protocol that rewrites natural language into a symbol-rich, formally-structured dialect. Where token-deletion methods such as LLMLingua-2 train a classifier to delete low-importance tokens at a fixed ratio, TE performs a full semantic rewrite: it decomposes the input into atomic fact lines, substitutes verbose phrases with $\sim$40 logical and relational symbols, and lets the compression ratio adapt to each document's information density. A consequence of the line-structure rule is that compression and semantic chunking become the same operation -- each output line is an independently addressable fact, so the compressed representation is simultaneously a semantic index. We evaluate TE on 4{,}081 question-answer pairs from LongBench-v2 across five OpenAI models and two difficulty levels. At roughly 50\% token reduction, TE preserves 99.1\% accuracy on key facts with GPT-4.1 and outperforms LLMLingua-2 at matched compression ratios on every model and task tested. The gap widens on smaller models -- up to 11 percentage points on fine-detail tasks -- suggesting that explicit relational structure compensates for limited model capacity. We release the grammar specification, compression prompt, benchmark data, and reference implementation.

---


### 96. [Ground4D: Spatially-Grounded Feedforward 4D Reconstruction for Unstructured Off-Road Scenes](https://arxiv.org/abs/2605.04435)

**<font color=#1a73e8>作者：</font>** Shuo Wang, Jilin Mei, Fuyang Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feedforward Gaussian Splatting has recently emerged as an efficient paradigm for 4D reconstruction in autonomous driving. However, in unstructured off-road scenes, its performance degrades due to high-frequency geometry, ego-motion jitter, and increased non-rigid dynamics. These factors introduce conflicting Gaussian observations across timestamps, leading to either over-smoothed renderings or structural artifacts. To address this issue, we propose Ground4D, a spatially-grounded 4D feedforward framework for pose-free off-road reconstruction. The key idea is to resolve temporal conflicts through spatially localized conditioning. Specifically, we introduce voxel-grounded temporal Gaussian aggregation, which partitions the canonical Gaussian space into spatial voxels and performs query-conditioned temporal attention within each voxel. Intra-voxel softmax normalization ensures that temporal selectivity and spatial occupancy become mutually reinforcing rather than conflicting. We furthermore introduce surface normal cues as auxiliary geometric guidance to regularize the geometry of Gaussian primitives. Extensive experiments on ORAD-3D and RELLIS-3D demonstrate that Ground4D consistently outperforms existing feedforward methods in reconstruction quality and generalizes zero-shot to unseen off-road domains. Project page and code:this https URL.

---


### 97. [A cross-modal network for facial expression recognition](https://arxiv.org/abs/2605.04439)

**<font color=#1a73e8>作者：</font>** Chunwei Tian, Jingyuan Xie, Qi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks enriched with structural information have been widely employed for facial expression recognition tasks. However, these methods often depend on hierarchical information rather than face property to finish expression recognition. In this paper, we propose a cross-modal network with strong biological and structural information for facial expression recognition (CMNet). CMNet can respectively learn expression information via face symmetry on a whole face, left and right half faces to extract complementary facial features. To prevent negative effect of biological and structural information fusion, a salient facial information refinement module can obtain salient facial expression information to improve stability of an obtained facial expression classifier. To reduce reliance on unilateral facial features, a half-face alignment optimization mechanism is designed to align obtained expression information of learned left and right half faces. Our experimental results demonstrate that CMNet outperforms several novel methods, i.e., SCN and LAENet-SA for facial expression recognition. Codes can be obtained at this https URL.

---


### 98. [LEGO: LoRA-Enabled Generator-Oriented Framework for Synthetic Image Detection](https://arxiv.org/abs/2605.04445)

**<font color=#1a73e8>作者：</font>** Yutong Xiao, Ran Ran, Jiwei Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of generative technologies has made synthetic images nearly indistinguishable from real ones, thereby creating an urgent need for robust detectors to counter misinformation. However, existing methods mainly rely on universal artifact features that are shared across multiple generators. We observe that as the diversity of generators increases, the overlap of these common features gradually decreases. This severely undermines model generalization. In contrast, focusing only on unique artifacts tends to cause overfitting to specific forgery patterns. To address this challenge, we propose LEGO (LoRA-Enabled Generator-Oriented Framework). The core mechanism of LEGO employs an MLP to modulate multiple LoRA (Low-Rank Adaptation) blocks, each pretrained to capture the unique artifacts of a specific generator, followed by attention-based feature fusion. Unlike conventional methods that seek a single universal solution, LEGO delegates unique artifact extraction to specialized LoRA modules by dividing its training procedure into two stages. Each LoRA module is individually trained on a single-generator dataset to learn generator-specific representations, then MLP and attention layers are trained on mixed datasets to dynamically regulate the contribution of each module. Benefiting from its modular yet robust design, LEGO can be naturally extended by incorporating new LoRA modules for adaptation to newly emerging next-generation datasets, while still achieving substantially better performance than prior SOTA methods with fewer than 30,000 training images, less than 10% of their training data, and only 5 epochs in each training stage.

---


### 99. [GEM: Graph-Enhanced Mixture-of-Experts with ReAct Agents for Dialogue State Tracking](https://arxiv.org/abs/2605.04449)

**<font color=#1a73e8>作者：</font>** Ziqi Zhu, Adithya Suresh, Tomal Deb 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dialogue State Tracking (DST) requires precise extraction of structured information from multi-domain conversations, a task where Large Language Models (LLMs) struggle despite their impressive general capabilities. We present GEM (Graph-Enhanced Mixture-of-Experts), a novel framework that combines language models and graph-structured dialogue understanding with ReAct agent-based reasoning for superior DST performance. Our approach dynamically routes between specialized experts: a Graph Neural Network that captures dialogue structure and turn-level dependencies, and a finetuned T5-Small encoder-decoder for sequence modeling, coordinated by an intelligent router. For complex value generation tasks, we integrate ReAct agents that perform structured reasoning over dialogue context. On MultiWOZ 2.2, GEM achieves 65.19% Joint Goal Accuracy, substantially outperforming end-to-end LLM approaches (best: 38.43%) and surpassing state-of-the-art (SOTA) methods including TOATOD (63.79%), D3ST (58.70%), and Diable (56.48%). Our graph-enhanced mixture-of-experts architecture with ReAct integration demonstrates that combining structured dialogue representation with dynamic expert routing and agent-based reasoning provides a powerful paradigm for dialogue state tracking, achieving superior accuracy while maintaining computational efficiency through selective expert activation.

---


### 100. [RemoteZero: Geospatial Reasoning with Zero Human Annotations](https://arxiv.org/abs/2605.04451)

**<font color=#1a73e8>作者：</font>** Liang Yao, Fan Liu, Shengxiang Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geospatial reasoning requires models to resolve complex spatial semantics and user intent into precise target locations for Earth observation. Recent progress has liberated the reasoning path from manual curation, allowing models to generate their own inference chains. Yet a final dependency remains: they are still supervised by human-annotated ground-truth coordinates. This leaves the reasoning process autonomous, but not its spatial endpoint, and prevents true self-evolution on abundant unlabeled remote sensing data. To break this bottleneck, we introduce RemoteZero, a box-supervision-free framework for geospatial reasoning. RemoteZero is motivated by a simple asymmetry: an MLLM is typically better at verifying whether a region satisfies a query than at directly generating precise coordinates. Leveraging this stronger discriminative ability, RemoteZero replaces geometric supervision with intrinsic semantic verification and enables GRPO training without box annotations. The resulting framework further supports iterative self-evolution, allowing the model to improve from unlabeled remote sensing imagery through its own verification signal. Experiments show that RemoteZero achieves competitive performance against strong supervised methods, demonstrating the potential of self-verifying training for geospatial reasoning localization.

---


> [!TIP]
> 当前位于：**51-100**（第 2/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-270](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
