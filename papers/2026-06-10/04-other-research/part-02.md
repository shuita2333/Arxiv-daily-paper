# 📦 其他研究 | 2026年06月10日

> 本类共 **527** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-527](./part-11.md)

---

### 51. [Detecting Aimbot Cheaters in MOGs](https://arxiv.org/abs/2606.07650)

**<font color=#1a73e8>作者：</font>** Salman Shaikh, Tao Ni, Marc Dacier  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multiplayer Online Games have become a multibillion dollar industry in the entertainment sector. However, the presence of cheaters undermines the experience of honest players and devalues the effort of game developers, as it directly affects player retention, competitive integrity, the legitimacy and trustworthiness of a game, and most importantly the overall revenue streams. Among various cheating techniques, visual aimbots represent an emerging threat. They use computer vision models to detect opponents from client screen captures rather than accessing game memory, making them completely undetectable by commercial kernel level anti cheat solutions. In this paper, we introduce PATCH, a novel proactive defense strategy that deploys adversarial patches as in game honeytokens to mitigate the presence of visual aimbot cheaters. Our approach centers on deliberately triggering the cheaters' object detection model, enabling either direct detection, or rendering the game unplayable for the cheater via patch flooding on their viewport. We evaluate our approach on various criteria; analyzing the effectiveness of different patch sizes, scalability of patches to different screen resolutions, efficacy against diverse visual aimbot cheat configurations and also explore various YOLO models to assess patch transferability. Evaluation on a custom Unreal Engine game demonstrates over 90 percent detection rate in white box scenarios for almost all patch sizes, and reaches 60 to 90 percent cross model transferability with larger patches. We further validate our approach on Fortnite, a commercial MOG, demonstrating real world applicability.

---


### 52. [KITE: A Tri-Modal Transformer Integrating Text, Images, and Knowledge Graphs for Fake News Detection](https://arxiv.org/abs/2606.07651)

**<font color=#1a73e8>作者：</font>** Kevin Patel, Shashi Bhushan Jha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional fake news detection methods are falling behind as multimodal misinformation grows more advanced, seamlessly blending deceptive text, manipulated visuals, and factually incorrect claims. Most prior work focuses on text-image fusion or applies external knowledge only as a post-processing step, limiting their ability to detect deeper semantic inconsistencies. In this paper, we introduce KITE (Knowledge-Integrated Text-Image Encoder), a tri-modal fake news detection framework that jointly models textual, visual, and factual knowledge representations. KITE leverages Roberta [23,14] and CLIP [24] for linguistic and visual encoding, while a Graph Attention Network (GAT) processes structured facts retrieved from Wikidata. KITE uses cross-modal attention [9] within a multimodal transformer to integrate text, visual, and knowledge features, helping it understand how each modality relates to one another. Modality-specific confidence scores are generated alongside the final prediction, offering interpretability by indicating which input type most influenced the decision. Evaluations on benchmark datasets demonstrate that KITE significantly outperforms unimodal and bimodal baselines, particularly in scenarios involving image-text mismatches or contradictions with external knowledge.

---


### 53. [What neurosurgeons need to see: synthetic intra-operative MRI from ultrasound for brain-shift compensation in brain tumour surgery](https://arxiv.org/abs/2606.07658)

**<font color=#1a73e8>作者：</font>** Santiago Cepeda, Olga Esteban-Sinovas, Ignacio Arrese 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Maximal safe resection is the primary objective in glioma surgery. Neuronavigation guidance is progressively degraded by brain shift after dural opening. Intraoperative MRI can compensate but needs dedicated infrastructure and is rarely available, whereas intraoperative ultrasound (ioUS) is inexpensive, repeatable, and compatible with routine workflows. Navigation systems combining ioUS with preoperative MRI usually rely on rigid registration; even deformable multimodal registration is limited by ultrasound speckle contrast, a narrow field of view, and the inability to represent structures absent from the preoperative scan, most critically the resection cavity and residual tumor. We propose an end-to-end pipeline that generates a new whole-brain MRI volume in the preoperative imaging space by merging the preoperative MRI, a synthetic MRI generated from the ioUS, and a deformable registration anchored on that synthetic image. It integrates a 2.5D residual-transformer synthesis backbone (ResViT-2.5D) and a two-stage registration coupling NiftyReg with a synthesis-anchored SynthMorph stage, operating directly on raw scanner inputs. On a post-resection ReMIND cohort, ResViT-2.5D produced synthetic images closely matching the intraoperative T2 across structural, intensity, and perceptual metrics. In 14 subjects with 215 expert landmarks, the synthesis-anchored registration reduced the mean target registration error from 6.27 to 5.86 mm, matching a strong classical NiftyReg baseline (5.85 mm) while yielding a diffeomorphic deformation field in every subject. The contribution is not a gain in registration accuracy but the integrated volume itself, which inside the ultrasound field of view it reflects the intraoperative post-resection state. This provides the surgeon with an MRI-like update of the operative field with potential for integration into surgical-navigation workflows.

---


### 54. [Real-Time Industrial Defect Detection on Edge Hardware Using Fine-Tuned YOLOv8: A Systematic Benchmark on the NEU Surface Defect Database and MVTec AD with Automotive & Battery Manufacturing Extensions](https://arxiv.org/abs/2606.07659)

**<font color=#1a73e8>作者：</font>** Emmanuel Ezeji Somtochukwu, Nitesh Rijal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated surface defect detection is critical for ensuring rigorous quality control in high-speed manufacturing environments. While deep learning models offer remarkable accuracy, deploying them on resource-constrained edge hardware without introducing significant latency remains a persistent challenge. This paper presents Industrial-YOLO, an edge-optimized framework built upon a fine-tuned YOLOv8 architecture specifically engineered for real-time industrial defect detection. We conduct a systematic benchmark utilizing the NEU surface defect database for steel sheets and the MVTec AD dataset, supplemented with custom automotive manufacturing extensions representing real-world structural anomalies (scratches, pits, and inclusions). To bridge the gap between algorithmic complexity and edge hardware constraints, target-specific optimizations are introduced via TensorRT and OpenVINO acceleration engines. Experimental results demonstrate that Industrial-YOLO achieves a high-velocity inference speed exceeding 120 FPS on the NVIDIA Jetson Orin platform while maintaining an exceptional mean Average Precision (mAP) of 98.5%. The proposed framework showcases highly robust, zero-latency performance when deployed directly onto an active automotive assembly line, offering a scalable blueprint for next-generation automated optical inspection (AOI) systems.

---


### 55. [MemoVAD: Resource-Efficient Video Anomaly Detection via Dynamic Semantic Memory in Edge Computing Scenarios](https://arxiv.org/abs/2606.07669)

**<font color=#1a73e8>作者：</font>** Guo Li, Jiandian Zeng, Yang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying Video Anomaly Detection (VAD) in real-world surveillance faces a fundamental tension between the demand for high-level semantics to ensure effectiveness and the limited computational resources of edge devices. Vision-Language Models (VLMs) provide rich open-vocabulary semantics, but their latency and computational cost preclude on-device deployment. To address the challenge, we propose MemoVAD, an edge-cloud collaborative framework that selectively incorporates VLM semantics into streaming VAD. MemoVAD runs most inference on the edge with a lightweight detector and a causal Temporal Context Encoder (TCE) to model temporal dependencies. Specifically, we introduce an Uncertainty-Aware Gating (UAG) policy grounded in Subjective Logic to model perceived uncertainty and query the cloud-based VLM only for high-uncertainty and semantically novel clips. Besides, a Dynamic Semantic Memory (DSM) is designed to cache VLM-verified prototypes for efficient retrieval, enabling the edge model to progressively incorporate VLM-level semantics via a semantic adapter. Experiments on UCF-Crime and XD-Violence datasets via a real edge device show that MemoVAD substantially reduces communication overhead while surpassing state-of-the-art performance.

---


### 56. [Liquid Neural Networks as a Drop-in Continuous-Time Deformation Field for Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2606.07670)

**<font color=#1a73e8>作者：</font>** Mingzhao Li, Arghya Pal, Guan Yuan Tan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deformable 3D Gaussian Splatting (D-3DGS) re-constructs dynamic scenes from monocular video by deforming a canonical set of 3D Gaussians through a positional-encoded MLP of frame time t. Although fitted to a continuous variable, the MLP couples no two values of t in its architecture and effectively predicts discrete per-frame offsets, leaving temporal smoothness to emerge only as a byproduct of optimisation. We redesign the deformation field as a stack of Closed-form Continuous-time (CfC) cells, a Liquid Neural Network (LNN), that is the closed-form solution of the Liquid Time-constant ODE while preserving every other part of the D-3DGS pipeline. Each cell exposes a sigmoidal time gate that interpolates between two candidate hidden states, baking a learned smooth response to t into the loss landscape without invoking any numerical solver. On the eight D-NeRF and seven NeRF-DS scenes the liquid field matches or exceeds the MLP baseline in aggregate, with its largest gains concentrated on the scenes with the most high-frequency articulated motion. The result is a near-zero-friction architectural design that turns the discrete MLP deformation field into an explicit continuous-time function of t.

---


### 57. [Test-Time Adaptive Composition for Machine Learning as a Service (MLaaS) in IoT Environments](https://arxiv.org/abs/2606.07685)

**<font color=#1a73e8>作者：</font>** Deepak Kanneganti, Sajib Mistry, Sheik Mohammad Mostakim Fattah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The dynamic nature of Internet of Things (IoT) environments affects the long-term effectiveness of Machine Learning as a Service (MLaaS) compositions. Existing adaptive composition methods are mainly based on service replacement or re-composition, where identifying suitable substitutes is difficult and time-consuming. To address this, we propose a novel Test-Time Adaptive (TTA) composition framework for MLaaS in IoT environments. First, we introduce a TTA-aware composability model to determine whether adapted services remain compatible with the existing composition. Next, we design a service-level adaptation model to adjust individual services during inference while preserving composition performance. Experimental results demonstrate that the proposed framework reduces computational time more effectively than traditional adaptive approaches.

---


### 58. [Knowledge-Inclusive Adaptive Physics-Informed Neural Network for Microbial Interaction Modelling](https://arxiv.org/abs/2606.07686)

**<font color=#1a73e8>作者：</font>** Ravisha Rupasinghe, Rajith Vidanaarachchi, Asela Hevapathige 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Network (PINN) is a way of including knowledge in the form of equations in Machine Learning methods. Beyond equations, knowledge exists in other forms, such as text and network structure. While existing PINN-based approaches discover equation parameters from data, they rely solely on experimental measurements. We propose a new PINN framework that enriches parameter discovery by incorporating auxiliary knowledge sources. We instantiate our framework for microbiology, where generalised Lotka-Volterra (gLV) serves as a biological foundation for modelling microbial communities. We demonstrate that incorporating knowledge improves microbial community modelling. Our framework enriches the gLV parameters using peer-reviewed metagenomics literature, as text provides biological context on external influences that gLV alone cannot capture. We combine this knowledge with experimental measurements of microbial abundance using a data-driven integration approach. We integrate network-based structural knowledge by explicitly modelling microbial interactions. Our knowledge-inclusive framework infers microbial networks, revealing ecological insights. We validate these findings against ecological roles documented in the literature. We evaluate on real and simulated datasets spanning human- and plant-associated microbial communities. Our framework improves over the state-of-the-art by up to 53%, even without knowledge. Knowledge addition yields gains of up to 23% in Bray-Curtis Dissimilarity-based accuracy and 47% in $\mathrm{R}^2$.

---


### 59. [Vessel Traffic Flow Prediction on Sparse Data via Spatio-Temporal Graph Neural Networks with a Learnable Tweedie Head](https://arxiv.org/abs/2606.07694)

**<font color=#1a73e8>作者：</font>** Kyeongjun Lee, Heeyoung Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate vessel traffic flow prediction is crucial for smart port operations and navigational safety. However, maritime traffic flow data are often highly sparse with intermittent bursts, making robust forecasting challenging. Under such conditions, conventional spatio-temporal graph neural networks (ST-GNNs) can degrade toward conservative near-zero predictions and fail to capture non-zero activity. Although zero-inflated negative binomial (ZINB) models partially address excess zeros, their two-part formulation can still remain conservative around abrupt transitions. To address these issues, we propose a model-agnostic learnable Tweedie head that can be attached as a plug-and-play output module to arbitrary ST-GNN backbones. Instead of likelihood-based Tweedie training, which typically requires surrogate objectives, our approach optimizes the closed-form Tweedie unit deviance and predicts the mean for point forecasting while learning a node-level variance power to capture heterogeneous variability across port areas. Experiments on a maritime traffic graph constructed from real-world AIS data in the Port of Los Angeles and Long Beach show that the proposed head consistently improves RMSE across multiple ST-GNN backbones, especially on non-zero events, leading to more reliable forecasts for practical maritime traffic control.

---


### 60. [DSFNet: Learning Dual-Domain Spectral Operators for Multi-Modality Spatio-Temporal Forecasting in Urban Transportation Systems](https://arxiv.org/abs/2606.07695)

**<font color=#1a73e8>作者：</font>** Yongchao Li, Yang Li, Zhuoxuan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-Modality Spatio-Temporal Forecasting (MoSTF) extends traditional spatio-temporal forecasting by incorporating diverse traffic modalities. Despite significant recent strides in spatio-temporal modeling, existing approaches often fail to explicitly model the coupling relationships between different modality variables. Accurate MoSTF is challenging, as it requires modeling (1) temporal dynamic heterogeneity under exogenous influences and (2) heterogeneous spatial dependencies alongside complex cross-variable couplings. To address these challenges, we propose the Dual-Domain Spectral Filtering Network (DSFNet). Our framework employs dual-domain spectral filtering to capture heterogeneous spatial patterns and explicitly model the relationships between variables. Unlike graph-based message passing or dense attention over node-modality pairs, DSFNet factorizes space-modality interactions into feature-domain and spatial-domain spectral operators, enabling scalable modeling of nonlocal dependencies and cross-modality couplings. Furthermore, we introduce an external gating mechanism to adaptively regulate temporal dynamics under external influences. We validate our method through extensive experiments on five representative real-world traffic datasets. Compared with the second-best baselines, DSFNet reduces MAE by 3.21%-10.16% across these datasets. The results demonstrate that DSFNet significantly outperforms existing state-of-the-art baselines in accuracy while exhibiting efficiency and robustness.

---


### 61. [Pharmacogenomic Knowledge Graph Augmentation for Graph Neural Network-Based Drug-Drug Interaction Prediction](https://arxiv.org/abs/2606.07698)

**<font color=#1a73e8>作者：</font>** Juergen Dietrich  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) applied to drug-drug interaction (DDI) prediction rely exclusively on molecular structure encoded as SMILES-derived graphs. Prior work in this series demonstrated that model performance is bounded by the structural information content of training labels -- an Information Ceiling -- that architectural refinements alone cannot overcome. The present study investigates whether pharmacogenomic prior knowledge from the PharmGKB database partially closes this ceiling by providing metabolic pathway context that is independent of, and complementary to, molecular structure. Cytochrome P450 (CYP) enzyme substrate, inhibitor, and inducer annotations for four clinically relevant isoforms (CYP2D6, CYP3A4, CYP2C19, CYP2C9) are extracted and incorporated as a 12-dimensional feature vector concatenated to the molecular embedding prior to interaction prediction. Experiments are conducted under both pair-level and drug-level data splits to quantify generalization to unseen drugs. Results indicate that knowledge graph (KG) augmentation substantially improves DDI type classification under pair-level split conditions (F1-macro: 0.532 vs. 0.241 baseline), while binary interaction detection and drug-level generalization remain bounded by the Information Ceiling (AUC inflation: 0.224 vs. 0.250 baseline). Mechanistic validation on strictly held-out compounds confirms that augmentation preferentially improves CYP2C9-mediated interaction prediction, with probabilities increasing from 0.033-0.117 (baseline) to 0.560-0.586 (KG-augmented). An extension to single-molecule toxicity prediction on the Tox21 benchmark confirms that the effect is contingent on pharmacogenomic annotation coverage. These findings motivate the multimodal framework proposed for the subsequent study in this series.

---


### 62. [EssentialGIN: a new approach for gene essentiality prediction based on graph isomorphism neural networks](https://arxiv.org/abs/2606.07700)

**<font color=#1a73e8>作者：</font>** Sahar Mansouri-Rad, Zahra Narimani, Parvin Razzaghi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background: Prediction of essential genes (proteins), is a basic and challenging problem but at the same time very costly and time-consuming in wet-lab experiments. Predicting essential genes, only based on computational methods (to introduce wet-lab candidates) using centrality measures are not accurate and result in large number of false positives; therefore, more complex models such as deep learning and also integration of biological information are used in recent research to identify essential genes.
Methods: In this work we focus on graph isomorphism networks, in order to embed proteins as a node in PPI network to conserve topological features of PPI network, and also integrate biological data such as gene expression data, gene orthology information and gene subcellular localization information, and introduced a deep architecture for predicting essential genes. Graph isomorphism network architecture is modified in this work for embedding node information.
Results: Our experiments proved that the proposed method outperforms baseline centrality-based methods and also machine learning based methods such as Node2Vec, MLP, and also graph attention networks (GAT).
Conclusion: In this paper we observed that using graph isomorphism networks that integrate biological data (as node attributes) and preserve network topology can significantly improve the essential gene prediction accuracy. In simpler organisms such as E. coli and D. melanogaster, methods such as multi-layer perceptron using Node2Vec embedding also performs very good, but in H. sapiens the introduced architecture significantly outperforms deep learning and other graph neural network solutions.
Keywords: Essential gene prediction, graph neural network, graph isomorphism network, PPI network, node embedding

---


### 63. [EvoCSFL: Surrogate-Assisted Evolutionary Client Selection for Efficient and Robust Federated Learning](https://arxiv.org/abs/2606.07702)

**<font color=#1a73e8>作者：</font>** Lin Qiang, Sun Xiaoyan, Hu Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The heterogeneity of client data and systems makes it difficult to achieve satisfactory convergence speed and robustness in federated learning with random client selection. To address this issue, this paper proposes a surrogate-assisted client evolutionary selection framework for federated learning. In this framework, some typical client selection strategies are first used to generate candidate sets, and a metric function that integrates model performance, communication latency, and energy consumption is developed to formulate the client selection problem as a combinatorial optimization one. Subsequently, a surrogate model is constructed using the candidate selections and metric to efficiently approximate the performance of selected client subsets. An evolutionary algorithm is employed to search the combinatorial space of client selections, guided by the surrogate model to accelerate convergence. Experiments on MNIST, CIFAR10, CINIC10, and TinyImageNet demonstrate that the proposed algorithm achieves faster convergence, lower energy consumption, and improved robustness compared to existing methods.

---


### 64. [How Much Dense Attention is Necessary? Oracle-Guided Sparse Prefill for Full/GQA Layers in Hybrid Long-Context Models](https://arxiv.org/abs/2606.07703)

**<font color=#1a73e8>作者：</font>** Hongxing Wang, Harenome Razanajato, Zhen Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context prefill remains expensive because full/GQA layers still score the historical sequence, even in hybrid models with local, sparse, linear, or recurrent components. We study how much dense attention is needed to preserve task-level behavior under explicit support granularity and top-k budgets.
We introduce an attention-mass top-k oracle for existing GQA checkpoints: for each layer and query position, it computes dense attention, selects head-averaged token support, and recomputes attention only on that support. The oracle is a diagnostic reference, not a deployable accelerator, and separates sparse-budget feasibility from indexer error and runtime realization effects.
On Qwen-family retrieval-heavy evaluations, the longest per-query oracle rows stay within 1 point of dense, and a Qwen3.5-9B RULER-style sweep from 4K to 100K stays within 0.48 points. Guided by the oracle, we derive a head-collapsed auxiliary indexer trained by KL distillation from dense attention-mass distributions while keeping the backbone frozen. With separately distilled Qwen3.5-0.8B and Qwen3.5-9B indexers, the reported 16K/32K validation macro gaps are +2.04 and +1.13 points, treated as quality preservation rather than improvement; fused selection-block-shared support can introduce a larger realization gap.
Preliminary single-card TTFT measurements show distilled-indexer sparse serving speedups of 1.71x for Qwen3.5-0.8B on NPU and 1.93x for Qwen3.5-9B on GPU against its dense FlashAttention-2 baseline. Additional random-init stress rows reach 3.44x, indicating sparse-runtime headroom but not validated output quality. This first release separates oracle feasibility, distilled-indexer quality, and runtime headroom, leaving a fully matched quality-latency frontier to future work.

---


### 65. [Cross-View Urban Traffic Dataset: Drone-Supervised Ground Truth for Monocular Bird's-Eye View Localization](https://arxiv.org/abs/2606.07708)

**<font color=#1a73e8>作者：</font>** Prakhar Bhardwaj, Simone Weikl, Kilian Mang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce a dataset and benchmark for cross-view urban traffic perception built from synchronized ego-centric bicycle videos and aerial drone videos recorded at real urban intersections. The benchmark targets two linked tasks: cross-view identity matching between street-view and drone-view object tracks, and ego-to-bird's-eye-view prediction using aerial supervision. In contrast to prior urban driving and V2X datasets, our benchmark provides identity-level alignment across radically different viewpoints together with standardized evaluation, annotation tooling, and baseline implementations. This setting is motivated by intersection-centric traffic analysis, where identity preservation, local interactions, and global spatial structure must be reasoned about jointly across views. We evaluate methods at both the track and frame levels, including cross-view ID precision/recall/IDF1, near--far breakdowns, temporal stability, and consistency metrics. We also provide baseline results for wedge-based cross-view matching and for three BEV prediction baselines: inverse perspective mapping, a MonoLayout-style learned baseline, and a regression baseline. The results show that the benchmark is feasible but challenging: cross-view matching achieves strong recall yet remains limited by over-assignment and temporal inconsistency, while ego-to-BEV prediction benefits from aerial supervision but remains far from saturated under lightweight monocular sensing. We hope that this benchmark will support future research on cross-view perception, urban scene alignment, and ego-to-global traffic understanding.

---


### 66. [Attention at the Theoretical Minimum: A Mathematics of Arrays Framework for Memory-Optimal Transformer Kernels](https://arxiv.org/abs/2606.07713)

**<font color=#1a73e8>作者：</font>** Lenore Mullin, Gaetan Hains  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The attention mechanism is the dominant computational bottleneck in modern transformer-based AI. Its standard implementation incurs quadratic memory traffic in the sequence length~$n$, and DRAM accesses cost 100--1000$\times$ more energy than arithmetic operations on contemporary hardware, so any analysis focused solely on FLOP counts fundamentally mischaracterises the bottleneck.
We present a Mathematics of Arrays (MoA) reformulation of scaled dot-product attention and its numerically stable softmax, deriving a Denotational Normal Form (DNF) that eliminates all intermediate arrays -- including the implicit transposed-key buffer and every softmax temporary -- by algebraic construction rather than empirical tuning. The DNF achieves $O(n_{dk} + n{_{dv}})$ data movement versus $O(n^2 + n_{dk} + n_{dv})$ for the standard implementation, where $n$ is the sequence length, $dk$ is the key dimensionality and $dv$ the value dimensionality, and is verified numerically against PyTorch at full double-precision floating-point on concrete inputs.
Unlike hardware-specific accelerators or empirical tiling schemes such as FlashAttention, MoA simultaneously provides array fusion, shape-transformation correctness, and predictive cost models from a single algebraic framework. Memory minimality is a theorem established before any code is written. A predictive performance model projects $2$--$100\times$ speedup and $2$--$50\times$ energy reduction, with the advantage widening at exascale. The derivation establishes a formally verified pipeline from Python specification through (ONF) Operational Normal Form, and dimension-lifted hardware mapping, providing performance-portable AI kernels of direct relevance to DARPA edge-deployment and DOE exascale priorities.

---


### 67. [Beyond Accuracy: Interpreting Topic Representation in Suicide Ideation Detection Models](https://arxiv.org/abs/2606.07714)

**<font color=#1a73e8>作者：</font>** Hamideh Ghanadian, Isar Nejadgholi, Hussein Al Osman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Suicide ideation detection models are typically evaluated using aggregate performance metrics, yet little is known about how they internally represent psychologically meaningful risk factors. In high-stakes mental health applications, understanding these internal representations is essential for safety, transparency, and responsible deployment. In this work, we move beyond accuracy and analyze how suicide detection models trained on original and topic-augmented datasets encode psychological risk factors in their internal representation space. Using visualization and geometric analysis, we examine the coherence and separability of topic-related features. Our results show that topic-aware augmentation increases the clarity and distinctness of underrepresented psychosocial risk factors such as immigration, family issues, and financial crisis. These findings suggest that augmentation not only improves model performance but also leads to more structured and interpretable internal representations.

---


### 68. [SHIELD-IDS: Structurally Heterogeneous Ensemble with Integrated Layered Defense for Intrusion Detection Systems](https://arxiv.org/abs/2606.07716)

**<font color=#1a73e8>作者：</font>** Maryam Zaman, Muhammad Khuram Shahzad  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Adversarial attacks pose a serious and growing threat to Machine Learning (ML)-based Intrusion Detection Systems (IDS), where imperceptible perturbations to network flow features can systematically mislead classifiers into accepting malicious traffic as benign. The IDS-Anta framework partially addresses this through Z-score normalization, Singular Value Decomposition (SVD), and Multi-Armed Bandit (MAB) classifier selection with Thompson Sampling, yet its classifier pool lacks sufficient structural diversity for robust adversarial resistance. This work introduces IDS-Anta++, which incorporates XGBoost and LightGBM gradient boosting models into the ensemble and wraps the extended pool in a three-layer black-box defense: Isolation Forest anomaly screening, median feature smoothing, and six-way majority voting. Experiments conducted on CIC-IDS-2017, CEC-CIC-IDS-2018, and CIC-DDoS-2019 under both Fast Gradient Sign Method (FGSM) and Zeroth Order Optimization (ZOO) attacks confirm detection accuracy above 99% on clean data, with measurable robustness gains under adversarial conditions relative to the baseline IDS-Anta configuration.

---


### 69. [A case study of evaluating AI agents on a neuroscience data-to-discovery pipeline](https://arxiv.org/abs/2606.07718)

**<font color=#1a73e8>作者：</font>** Kai A. Horstmann, Ethan Lin, Alice A. Robie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI tools offer a promising path to automating software development bottlenecks in scientific research pipelines, particularly for stages that take domain experts days to months to build, where scientists care about correctness and robustness, not implementation details. We present an empirical study of general-purpose coding agents on a fly optogenetics data-to-discovery pipeline. We assess agents on tasks substantially larger than existing benchmarks, datasets orders of magnitude bigger, and evaluation criteria grounded in domain expert standards. We show that agents can solve several individual pipeline stages, suggesting stage-level automation is tractable. By analyzing agents' code iterations, we show that they struggle most when there is not a pre-defined criterion to iterate on, and they must instead use their scientific judgment to assess their current solution, a key open challenge. Mirroring scientific practice, they sometimes attempt visual inspection of intermediate outputs for self-evaluation, but largely fail to interpret what they see or act on it appropriately. Solving the end-to-end pipeline correctly requires stringing together successes across all pipeline stages, and this is beyond agents' current abilities. We identify challenges largely absent from existing benchmarks, including computational resource management and generalization to large held-out data collections. Finally, we distill principles for constructing scientific tasks and rigorous evaluation criteria for open-ended problems.

---


### 70. [A Geometry-Aware Triplane Field Network for Vehicle Aerodynamic Prediction](https://arxiv.org/abs/2606.07724)

**<font color=#1a73e8>作者：</font>** Kangkang Qi, Huiyu Yang, Keqi Ding 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-fidelity computational fluid dynamics (CFD) is crucial to vehicle aerodynamic analysis, but its cost still constrains early-stage design exploration. Machine-learning-based surface-field prediction offers a faster alternative if the model can efficiently capture both global flow context and local geometric detail. This work proposes a machine-learning-based method, named the geometry-aware triplane field network (GTF-Net), for vehicle aerodynamic pressure and wall shear stress prediction. GTF-Net constructs triplane features directly from sampled surface points through a shared multilayer perceptron (MLP) and smooth bilinear rasterization. The planes are then processed by a dual-stream backbone that combines adaptive Fourier neural operator (AFNO) spectral mixing with convolutional neural network (CNN) refinement, so long-range aerodynamic coupling and local geometry-induced variations are modeled in the same representation. At query stage, sampled triplane features are combined with vehicle-aligned directional coordinates, normal-projection features, and a voxel-based curvature proxy. GTF-Net is compared with Transolver, geometry-informed neural operator (GINO), and TripNet, a triplane-based surrogate model. GTF-Net improves the relative L2 error from the strongest baseline value of 0.157 to 0.145 for pressure prediction and from 0.237 to 0.226 for wall shear stress prediction. Ablation results show that AFNO mixing, local CNN refinement, and query-side geometric encoding each contribute to accuracy, supporting the proposed mechanism of combining structured triplane representation with explicit aerodynamic geometry cues.

---


### 71. [Characterizing the Discrete Geometry of ReLU Networks](https://arxiv.org/abs/2606.07728)

**<font color=#1a73e8>作者：</font>** Blake B. Gaines, Jinbo Bi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> It is well established that ReLU networks define continuous piecewise-linear functions, and that their linear regions are polyhedra in the input space. These regions form a complex that fully partitions the input space. The way these regions fit together is fundamental to the behavior of the network, as nonlinearities occur only at the boundaries where these regions connect. However, relatively little is known about the geometry of these complexes beyond bounds on the total number of regions, and calculating the complex exactly is intractable for most networks. In this work, we prove new theoretical results about these complexes that hold for all fully-connected ReLU networks, specifically about their connectivity graphs in which nodes correspond to regions and edges exist between each pair of regions connected by a face. We find that the average degree of this graph is upper bounded by twice the input dimension regardless of the width and depth of the network, and that the diameter of this graph has an upper bound that does not depend on input dimension, despite the number of regions increasing exponentially with input dimension. We corroborate our findings through experiments with networks trained on both synthetic and real-world data, which provide additional insight into the geometry of ReLU networks. Code to reproduce our results can be found at this https URL.

---


### 72. [ReadingMachine: A Computational Methodology for Structured Corpus Reading and Large-Scale Synthesis](https://arxiv.org/abs/2606.07753)

**<font color=#1a73e8>作者：</font>** James Morrissey  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> ReadingMachine is a computational methodology for structured corpus reading that uses large language models to perform bounded reading operations over entire document collections. Rather than relying on retrieval or recursive summarization, the approach decomposes analysis into inspectable stages including insight extraction, semantic clustering, theme generation, and iterative omission detection. By delaying irreversible compression and explicitly tracking intermediate representations, the method prioritizes coverage, traceability, and preservation of disagreement across large corpora. The system is demonstrated on a heterogeneous corpus of 152 industrial policy documents, producing more than 17,500 extracted insights and a structured thematic map. ReadingMachine is released as an open-source experimental framework for large-scale qualitative synthesis and corpus analysis.

---


### 73. [DroneDAR: Long-Range Drone Distance Estimation Using Monocular Vision and Bounding-Box Features](https://arxiv.org/abs/2606.07756)

**<font color=#1a73e8>作者：</font>** Knut Peterson, Zaid Mayers, David Han  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate distance estimation for small drones in long-range imagery is important for tracking and situational awareness, yet remains challenging due to extreme target scale variation, background clutter, and noisy visual cues. This paper studies monocular drone distance estimation using image crops together with bounding-box geometry, a practical setting in which a detector provides a candidate drone region and the model predicts range from appearance and box-derived features. We evaluate a Droneranger-style baseline, and introduce a new DroneDAR (Drone Detection And Ranging) model that combines a convolutional backbone with explicit bounding-box cues through a lightweight gating mechanism. Experiments analyze how backbone capacity, crop resolution, and regression loss functions affect performance across distance regimes. We further examine common failure modes at long distances, including sensitivity to bounding-box noise and reduced texture detail in the crop. The results provide guidance for designing and training range estimators that remain robust under real-world long-range conditions and highlight directions for improving reliability when drones occupy only a few pixels.

---


### 74. [scCBGM: Interpretable Single-Cell Counterfactual Editing](https://arxiv.org/abs/2606.07760)

**<font color=#1a73e8>作者：</font>** Alma Andersson, Aya Abdelsalam Ismail, Edward De Brouwer 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding cellular phenotypes and how they respond to perturbations is critical for disease biology and therapeutic design. Single-cell RNA sequencing enables characterization at cellular resolution, yet the combinatorial space of conditions makes exhaustive experimental mapping infeasible. We introduce single-cell Concept Bottleneck Generative Models (scCBGM), a framework for interpretable and precise counterfactual editing of individual cells. scCBGM adapts concept bottleneck architectures for single-cell data through decoder skip connections and a cross-covariance penalty that promotes disentanglement without dimensional constraints. We extend the framework to flow matching models, enabling concept-guided editing in both encoding-decoding and generation regimes. To enable rigorous evaluation, we develop a synthetic benchmark with ground-truth counterfactuals. Across multiple real datasets, scCBGM demonstrates superior performance in combinatorial generalization and counterfactual prediction, supported by cell-level validation on synthetic data and population-level benchmarks on real datasets.

---


### 75. [ScaleDisturb: Exploiting Temporal Asymmetry to Amplify Read Disturbance in Modern DRAM Chips](https://arxiv.org/abs/2606.07761)

**<font color=#1a73e8>作者：</font>** Jikun Wang, Haocong Luo, Ataberk Olgun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> DRAM suffers from read disturbance phenomena (e.g., RowHammer and RowPress), where repeatedly accessing or continuously keeping open a DRAM row (aggressor row) induces bitflips in other physically nearby unaccessed rows (victim rows). The disturbance mechanism is practically exploitable from the software stack and worsens across generations with continued density scaling. DRAM read disturbance is highly sensitive to memory access patterns, yet prior work explores read disturbance under only a limited set of access patterns. We present ScaleDisturb, a new DRAM access pattern that can amplify DRAM read disturbance by asymmetrically extending the open time of two aggressor rows. Our rigorous experimental characterization of 196 DDR4 and 3 HBM2 DRAM chips shows that ScaleDisturb (1) leads to bitflips at significantly fewer row activations, compared to state-of-the-art memory access patterns, (2) makes read disturbance attacks easier across all tested DRAM chips, (3) increases DRAM vulnerability to read disturbance as DRAM manufacturing technology scales down to smaller node sizes. We showcase a proof-of-concept attack on a real system where a user-level program leveraging ScaleDisturb induces more bitflips than state-of-the-art RowHammer and RowPress memory access patterns. We describe and evaluate four solutions for mitigating read disturbance bitflips in the presence of ScaleDisturb and call for more research on the topic.

---


### 76. [Quantum-Enhanced Similarity Measures for Polarimetric Materials Classification](https://arxiv.org/abs/2606.07766)

**<font color=#1a73e8>作者：</font>** Sara Shojaei, Seyed Mohamad Ali Tousi, Emma Bennett 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a quantum--classical hybrid pipeline for polarimetric material classification that casts this as a point-matching problem. Voxel cubes, containing polarized light reflections, are used to train an encoder to produce 32-dimensional embeddings for the voxels of the cubes. At inference, the encoder head is discarded and the embeddings are encoded as probability amplitudes of quantum states. Next, a SWAP-test circuit estimates the fidelity between each of the 32D embeddings from the query cube and a dataset of anchor cubes. The aggregated fidelity serves as materials similarity scores, and the class of the anchor with highest aggregated fidelity is deemed as the class of the queried material. We evaluate our approach on a dataset of 23 materials ($\approx$800 samples each) derived from their Mueller matrices. The point-matching approaches from the proposed quantum SWAP-test and a classical classifier using Optimal Transport are compared. Our results demonstrate the competitive classification accuracy alongside open-set discrimination potential, establishing it as a viable path toward NISQ-based material recognition.

---


### 77. [Contrast encodes inductive bias: separating slow noise from dynamics in predictive representation learning](https://arxiv.org/abs/2606.07770)

**<font color=#1a73e8>作者：</font>** Paarth Gulati, Ilya Nemenman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised methods that learn representations and predict dynamics fully in the latent space, such as JEPA, have been shown to confuse slowly varying noise with the dynamical signals they aim to capture. Specifically, when noise features remain approximately constant within each trajectory, contrastive predictive objectives preferentially encode these features instead of the true latent variables governing the system. The learned representation then becomes dominated by trajectory-specific noise, so downstream performance degrades with noise strength and does not improve even as the number and duration of training trajectories increase. We argue that this failure is a property of the objective itself, shared by a long line of contrastive predictive objectives that sample negatives across trajectories. To illustrate this generality, we study the failure mode and its remedy in two settings: a standard SimCLR-style JEPA on a synthetic moving-dot dataset, and DySIB, a recently introduced method designed for extracting physically interpretable representations of dynamics, on movies of a rigid-body pendulum. When negatives are instead sampled within a single trajectory, the slow noise can no longer distinguish frames within that trajectory, removing the predictive shortcut. Training one encoder simultaneously on many such trajectories then forces it to encode the variables relevant for the dynamics, with longer trajectories yielding better representations even for strong slow noise. Our results point toward principles for designing contrastive predictive objectives in dynamical representation learning, especially for physical systems with noisy experimental observations.

---


### 78. [Understanding Human and Interface Design Factors in Canadian Cybercrime Reporting](https://arxiv.org/abs/2606.07773)

**<font color=#1a73e8>作者：</font>** Charlotte Carr, Ananta Chowdhury, Asra Sakeen Wani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cybercrime affects a majority of Canadians, yet most incidents go unreported. We conducted two studies to examine the factors influencing cybercrime reporting and the role of interface design in victims' reporting experiences. Our survey provides individual-level insights into the persistent gap in cybercrime reporting in Canada, showing how perceived incident severity and personal characteristics shape reporting behaviour. Our usability study compared reporting with an AI chatbot to an online form; chatbots facilitated more complete reports and led to higher user satisfaction, highlighting how interface design impacts reporting outcomes.

---


### 79. [Unlocking Latent Value: Taxonomy-Guided Recovery of High-Performing Data from Low-Tier Web Corpora](https://arxiv.org/abs/2606.07778)

**<font color=#1a73e8>作者：</font>** Neeraj Varshney, Sanket Lokegaonkar, Nasser Zalmout 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dominant web data curation pipelines for pretraining collapse document quality into a single composite score, systematically missing high-value content along dimensions the scorer underweights. We present a taxonomy-driven framework that recovers this value by filtering along semantically meaningful dimensions that composite scores fail to capture. First, building on the ESSENTIAL-WEB taxonomy, we introduce two novel dimensions: timeliness and cultural specificity, both of which show low pairwise NMI with existing ones. We annotate 14M documents using Qwen2.5 32B and distill into a lightweight 0.5B model. To enable rapid corpus-wide annotation, we additionally train a 73M multi-task MLP on E5 embeddings, achieving 50x inference throughput. Second, to navigate the combinatorial explosion of filter configurations, we introduce a compute-efficient two-pass framework: Pass 1 identifies the strongest dimension signals at small scale; Pass 2 constructs and evaluates conjunctive and disjunctive compound filters from the top performers - identifying high-performing configurations at a fraction of full scaling-law cost. Applying the selected filters to deprioritized web data, taxonomy-filtered subsets outperform their unfiltered baselines and even surpass the highest-quality tier. On mid-tier data, our best filter improves over its unfiltered baseline by 12.1% on reasoning, 9.5% on coding, and 2.0% on knowledge benchmarks, exceeding unfiltered top-tier data by 6.7% on reasoning and 13.7% on coding. Furthermore, filtered data from two tiers below the typical production threshold improves by 22.3% on reasoning and 19.5% on coding over its unfiltered baseline, surpassing top-tier data on coding benchmarks. These results establish that vast latent value remains locked in deprioritized web data, and that multi-dimensional taxonomy filtering is a principled, compute-efficient key to unlocking it.

---


### 80. [Land cover and flood type govern the detection limits of satellite-based flood mapping across diverse global flood events](https://arxiv.org/abs/2606.07780)

**<font color=#1a73e8>作者：</font>** Venkatesh Kolluru, Rajat Shinde, Abdelhak Marouane 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Floods are among the most destructive natural hazards, and their increasing frequency under climate change makes satellite-based inundation mapping essential for disaster response. Geospatial foundation models pretrained on satellite archives offer geographic transferability, but their operational reliability across diverse, unseen events remains uncharacterized. Here we deploy Prithvi-EO-2.0 across 19 out-of-distribution flood events (2017-2025) spanning six continents, eight climate zones, and six flood mechanisms, validating against two independent reference products. Detection accuracy depended jointly on land cover and flood type, with cropland yielding the highest agreement (IoU=52%) and riverine events the strongest detection (F1=0.69), while tree cover and built-up areas showed near-zero detection (IoU=4%) regardless of flood mechanism. Dual-reference validation revealed that apparent model error partly reflects definitional inconsistency between reference products rather than detection failure. Iterative pipeline testing identified 23 failure modes, with pipeline engineering dominating initial error over model capacity. These findings establish environment-dependent detection boundaries for operational satellite flood mapping.

---


### 81. [A Framework for Evaluating and Benchmarking Concept Drift Detection Methods](https://arxiv.org/abs/2606.07789)

**<font color=#1a73e8>作者：</font>** Vitor Cerqueira, Heitor Murilo Gomes, Marco Heyden 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data stream mining is fundamentally challenged by concept drift, where distributional changes can degrade model performance. Despite the proliferation of drift detection methods, progress in the field is hindered by inconsistent evaluation practices: studies rely on oversimplified synthetic data generators, adopt incompatible metrics, and lack transparency in hyperparameter selection, making fair comparisons difficult. We address this gap with a novel benchmarking framework comprising three contributions: (1) a drift simulation method that injects controlled distributional changes into real-world datasets via Monte Carlo trials, enabling supervised evaluation while preserving real-world data complexity; (2) an evaluation protocol for drift detection with timing-aware criteria, including the derivation of new metrics (e.g., F1 detection score, normalized detection time) that are comparable across streams; and (3) we advocate for a leave-one-dataset-out hyperparameter optimization protocol for drift detection methods that promotes configuration robustness across heterogeneous stream dynamics. We benchmark 14 widely used drift detection methods on 7 realworld datasets across 4 drift types (class prior, label swap, feature permutation, feature filtering), each under both abrupt and gradual transitions. Our experimental results provide insights into the strengths and weaknesses of current drift detection approaches while establishing baseline performance metrics for future research in this area. All code and experiments are publicly available.

---


### 82. [MOLOT System Card: Malicious Operational Logic Observation Transformer](https://arxiv.org/abs/2606.07792)

**<font color=#1a73e8>作者：</font>** Daniil Lopatkin, Maksim Mitrofanov, Stanislav Rakovsky 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> MOLOT (Malicious Operational Logic Observation Transformer) is a static malicious-code detection system designed for SAST setup where package metadata, maintainer history, and dynamic execution traces may be unavailable or unreliable. The system represents source code as behavior sequences derived from static call graphs, includes an explanation stage that ranks suspicious behavior activities and maps them back to source-code locations. The approach is evaluated on Python and JavaScript packages from PyPI and npm, compared with opensource detection tools, and validated under product constraints including runtime, memory use, and false-positive rates observed in a real moderation workflow. We also release Open Malicious-Code Bench, a public benchmark for reproducible evaluation of malicious-package detection methods. The results show that static behavior-sequence modeling can provide accurate, explainable, and deployable malicious-code detection for modern DevSecOps workflows.

---


### 83. [The Choreography of Augmented Reality Timelines: Studying the Relative Position, Chronology, & Situatedness of Event Sequences](https://arxiv.org/abs/2606.07794)

**<font color=#1a73e8>作者：</font>** Isabelle Kwan, Jessica Ziyu Chen, Matthew Brehmer  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Timelines are effective ways to tell historical and personal stories. However, most timeline visualization tools impose an inflexible model of time prioritizing chronological clarity. On the other hand, unconstrained representations can better capture the irregular and contextual nature of lived time, but often at the cost of interpretability. In this work, we explore this continuum with a study of how historical and personal timelines could manifest in physical spaces. We conducted a formative study (N=12) in which participants freely arranged events within a physical environment. We observed a diversity of strategies reflecting the personal and context-dependent nature of temporal mental models. We also invited participants to consider how others could move through their timelines. Our analysis led to a choreographic approach to timeline creation, as well as a proof-of-concept tablet-based augmented reality (AR) application that supports spatial timeline drawing and viewing. Finally, we reflect on the design implications of encoding chronology, pacing, and spatial context in immersive timeline stories.

---


### 84. [Belief-Space Quantum-Inspired Reinforcement Learning for Partially Observable Autonomous Cyber Defense in the Internet of Vehicles](https://arxiv.org/abs/2606.07796)

**<font color=#1a73e8>作者：</font>** Anwar Shah, Rohan Farooq, Sajid Anwer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Internet of Vehicles (IoV) faces a dynamic, adversarial security environment where attackers adapt to defenses. Existing intrusion detection systems rely on static classifiers that fail to capture sequential decision-making, attacker adaptation, and uncertainty. We formulate IoV security as a sequential attacker-defender interaction and model defense as a reinforcement learning problem under partial observability. We propose Quantum Belief-Integrated Reinforcement Defense (Q-BIRD), using quantum-inspired belief representation to encode defender uncertainty about hidden attacker intent via amplitude-based states, enabling non-Bayesian belief evolution. Integrated into a Proximal Policy Optimization (PPO) defender, Q-BIRD selects cost-aware mitigation actions. In simulated environments with adaptive, probing attackers, Q-BIRD reduced cumulative mean damage, damage variance, and attack success rate (ASR) by 60.4%, 90.2%, and 50.0%, respectively, while increasing survival probability by 46.4%. Compared to classical Bayesian PPO, damage variance reduction and ASR improved by 10.2 times and 50%. Ablation and explainability analyses confirm that amplitude-based belief is the primary decision signal during strategy transitions when classical belief collapses, providing superior IoV security without additional hardware.

---


### 85. [Reconstructing and forecasting disease trajectories of patients with Alzheimer's disease using routine data in resource-constrained settings](https://arxiv.org/abs/2606.07798)

**<font color=#1a73e8>作者：</font>** Ratnadeep Das, Atri Chatterjee, Sitikantha Roy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Alzheimer's disease is a progressive neurodegenerative disorder, and its progression varies substantially across patients. Existing work aims to forecast patients' future cognitive state, with minimal focus on reconstructing the state from past visits. Furthermore, in current research, quantifying predictive uncertainty remains underexplored and relies on costly modalities such as MRI, PET, and CSF, limiting their deployment in resource-limited settings. In this research, our primary objectives are: First, bidirectional prediction of cognitive scores from irregular visits to present the complete disease trajectory. Second, to enable interpolation and extrapolation capabilities to assist clinicians in informed prognostic decision making, and third, to provide a well-calibrated uncertainty estimate for all predictions, and finally, to achieve the objectives using the modalities available during routine visits. We propose a unified framework, GNOVA: A GRU-Neural ODE Variational Autoencoder. The architecture combines a Gated Recurrent Unit encoder and a Neural ODE decoder within a variational autoencoder framework. In our work, we forecast the CDR-SB and MMSE Scores. The GRU encoder allows for any number of inputs at any time point. The Neural-ODE decoder performs continuous estimation, allowing interpolation and extrapolation at any desired time point. The Variational autoencoder allows for uncertainty estimation in predictions. We worked with 1,727 patients from the ADNI dataset over 10 years; the model achieved mean absolute errors of 1.35 and 2.28 for CDR-SB and MMSE scores, respectively, without requiring any neuroimaging or biomarker data. Feature-ablation studies revealed that age, BMI, and APOE4 status were strong predictors. The proposed framework enables the reconstruction of incomplete patient histories and the anticipation of future cognitive states.

---


### 86. [Quantum-Inspired Reinforcement Learning for Low-Latency Intrusion Detection in V2X and Internet-of-Vehicles Networks](https://arxiv.org/abs/2606.07804)

**<font color=#1a73e8>作者：</font>** Sajid Anwer, Rohan Farooq, Anwar Shah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smart cities increasingly depend on dense edge, IoT, and vehicular networks to deliver critical urban services, including traffic control, connected mobility, infrastructure monitoring, and energy management. In this ecosystem, the Internet of Vehicles (IoV) is central to intelligent transportation, enabling continuous communication among vehicles, roadside infrastructure, and cloud-edge platforms. This connectivity, however, also enlarges the attack surface and exposes smart city and vehicular systems to evolving cyber threats that can compromise safety, privacy, data integrity, and service continuity. Conventional static defenses are often inadequate because they cannot autonomously adapt to changing attack behaviors or multi-stage intrusion patterns. This paper proposes QIRL, a Quantum-Inspired Reinforcement Learning framework built on a lightweight Deep Q-Network architecture for next-generation autonomous cyber defense. QIRL combines amplitude-phase quantum state encoding, rotation-gate-based exploration, and quantum interference reward augmentation within a cost-sensitive Markov Decision Process formulation. It further addresses class imbalance through training-only SMOTE balancing and asymmetric cost-sensitive reward shaping, while sequential MDP modeling captures temporal dependencies in multi-stage attack campaigns. The framework is evaluated on CICIDS2017 and UNSW-NB15. QIRL achieves accuracies of 97.89\% and 91.04\%, F1-scores of 95.22\% and 91.66\%, AUC-ROC values of 0.9945 and 0.9713, and True Skill Statistics of 0.9443 and 0.8244, respectively. It also attains ultra-low inference latencies of 32.5 and 45.7 microseconds per sample, corresponding to 67.77 times and 51.77 times speedups over ensemble baselines. These results show that QIRL offers a lightweight, latency-aware, and adaptive defense for smart city and IoV infrastructures.

---


### 87. [Scaling Participation in Modular AI Systems](https://arxiv.org/abs/2606.07812)

**<font color=#1a73e8>作者：</font>** Shangbin Feng, Yike Wang, Weijia Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Humanity is a mosaic of multifaceted talents and needs, and any truly intelligent AI must reflect that richness. Yet the LLMs used by all are built by the few -- a centralized market of monolithic AI models structurally ill-suited to capture the diversity of human knowledge, reasoning, and values. Here we introduce scaling participation, a new paradigm in which modular AI systems are built from the bottom up through the contributions of diverse stakeholders. Participants contribute small models trained on their own interests and priorities; these models then collaborate in modular frameworks as compositional AI systems. Participatory AI systems outperform monolithic LLMs by up to 15.4% across 15 tasks, such as reasoning and factuality, surpassing models larger than all contributed components combined. Further experiments show that participatory AI systems benefit from contributor diversity, substantially improve on each contributor's original priorities, and exhibit emergent capabilities that allow them to solve over 15% of problems where all individual models fail. Scaling participation provides a technical foundation for transitioning from the monolithic status quo toward an open, bottom-up, and collaborative AI future.

---


### 88. [Representational Similarity and Model Behavior in Multi-Agent Interaction](https://arxiv.org/abs/2606.07818)

**<font color=#1a73e8>作者：</font>** Yujin Potter, Seun Eisape, Shiyang Lai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Researchers have shown that neural similarity among humans predicts social closeness and cooperative success, whereas innovation often emerges from interactions among dissimilar individuals. We investigate whether these principles extend to artificial intelligence by examining interactions between large language models. In our experiments, 276 model pairs interact across eight games spanning both cooperation and novelty. We find that pairs with more similar representation spaces achieve significantly higher cooperation but exhibit reduced novelty and creativity. The effects of representational similarity on cooperation and novelty remain robust even after controlling for other factors such as performance disparity and model size. We also find that similarity in the early layers consistently shows the strongest association with cooperation and novelty, compared to the middle and later layers. This suggests that a central factor underlying these patterns could be the extent to which the two models share lexical and semantic grounding. Overall, representational similarity can be an important consideration in multi-agent system design.

---


### 89. [Ternary public-key cryptosystem](https://arxiv.org/abs/2606.07832)

**<font color=#1a73e8>作者：</font>** Steven Duplij, Qiang Guo, Na Fu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Public-key cryptosystems eliminate the requirement for pre-shared secret keys by enabling encryption with a publicly disclosed key and decryption with a corresponding private key. In this article we generalize the public-key cryptosystems to ternary algebraic structures, with particular attention to ElGamal as a representative family. We introduce the necessary algebraic background for nonderived ternary structures, including special elements, ternary group rings, and a matrix ternarization procedure that maps binary rings and group rings to antidiagonal symbolic matrices closed under ternary multiplication. Building on these foundations, we formulate a ternary analogue of the ElGamal three-step protocol (key generation, ephemeral encryption, and decryption via querelements) and derive explicit ternary power and querelement formulas that enable correct decryption. Concrete instantiations and numerical examples over a ternary fraction field, a matrix-ternarized finite group ring, and a finite \((6,3)\)-ring (field) validate the construction and illustrate admissible word-length quantization and cycle behaviour of ternary powers. The ternary framework highlights two practical advantages: richer algebraic structure (querelements replace binary inverses) that increases algebraic complexity for attackers, and higher information density (matrix ternarization transfers paired/plaintext vectors). Formal hardness assumptions, optimized parameter choices, and comprehensive security and performance analyses remain necessary future work.

---


### 90. [Mitigating the Contractivity Trap in Diffusion ODEs via Stein Stabilization](https://arxiv.org/abs/2606.07835)

**<font color=#1a73e8>作者：</font>** Shigui Li, Delu Zeng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A fundamental tension exists in the large-step inference of diffusion models via their deterministic probability flow ordinary differential equation (PF-ODE) trajectories, which we identify as the contractivity trap: efficient inference favors large step sizes, while aggressive steps and highly expressive denoisers can undermine contraction-based stability certificates for error suppression. To address this, we propose SteinDiff, a step-wise inference-time stabilization framework that employs Stein-derived corrections without requiring reference samples. Specifically, SteinDiff introduces a geometry-aware residual correction mechanism that regularizes large-step solver updates without retraining. To this end, we derive a closed-form Stein correction coefficient for step-wise solver adjustment, enabling reference-free adaptation to local data geometry. We further establish a score-controlled perturbation bound under distributional shifts and provide a complementary Stein perspective on EDM-style parameterizations. Extensive experiments demonstrate that SteinDiff mitigates severe artifacts and improves generative quality across large-step inference settings.

---


### 91. [Teacher-Free Self-Training Amplifies but Does Not Compound: A Pass@$K$ Crossover on a Free-Verifier Domain](https://arxiv.org/abs/2606.07856)

**<font color=#1a73e8>作者：</font>** Igor Lima Strozzi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a language model trains on its own verified outputs, does it acquire capability beyond its base, or merely get better at expressing capability the base already had? We make the question decidable with a teacher-free "constellation" -- a generator, a learned critic, and a free exact verifier -- on a FlashFill-style "trapdoor" DSL, where verified (problem, solution) pairs are cheap to synthesize, hard to invert, and free to check exactly. Everything runs on one 4-bit Qwen3-4B on a single 24 GB GPU, with no model in the loop larger than the base. We report three findings. (i) Critic-guided selection beats verifier-filtered best-of-$k$ by $+9.1$ pp ($6/6$ seeds), with the entire gain localized to tasks where candidates disagree on held-out inputs. (ii) Per-round STaR self-training raises the ceiling but never accelerates -- the gain tracks remaining headroom and decelerates across $K=4$ independent training trajectories. (iii) The domain has no clean zero-capability frontier, so the usual "$0\% \to$ climb $=$ emergence" test is invalid here. A measured pass@$K$ crossover settles the diagnosis: the trained model wins at the operating budget (pass@$8$) but the base overtakes it at a large budget (pass@$64$) on every trajectory, so self-training concentrates probability mass rather than expanding reach. This is amplification, not compounding. ($K=4$ is indicative, not yet a robust across-trajectory CI.)

---


### 92. [Instrumented data for causal scientific machine learning](https://arxiv.org/abs/2606.07865)

**<font color=#1a73e8>作者：</font>** Daniel N. Wilke  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific machine learning is limited less by model size than by the data it is trained on. Observational data records what happened but not why; template synthetic data has a known generating process but only for the simulator's template, not the case a user faces. We argue a third option is now operationally feasible: instrumented data, in which every datum carries the mechanistic model that produced it, an explicit uncertainty over that model, and an executable family of counterfactuals. Verification-and-validation (V&V) instrumented image-to-simulation pipelines are one realisation: a sensor observation becomes a fully specified, solver-backed simulation with explicit, editable parameters and a propagated aleatoric/epistemic uncertainty. The substrate is case-specific, mechanistically supervised, and supports causal interventions through Pearl's do-operator. Near-term consequences for validation, auditing, and surrogate training span computational biology, climate, materials, fluid mechanics, and medical imaging; a longer-term, falsifiable implication concerns foundation models for scientific reasoning.

---


### 93. [Overcoming the Regulatory Bottleneck via Agent-to-Agent Protocols: A Nuclear Case Study](https://arxiv.org/abs/2606.07866)

**<font color=#1a73e8>作者：</font>** Akshay J. Dave, David Grabaskas, Joseph A. Renevitz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Regulatory review of advanced nuclear reactor designs routinely spans more than three years and consumes hundreds of millions of dollars in combined regulator and applicant labor. We present the Regulatory Context Protocol (RCP), an Agent-to-Agent communication standard that replaces the formal human-to-human pipeline between regulators and applicants with a structured, auditable agentic channel, while preserving human oversight at safety-significant decision points. The protocol is calibrated against an analysis of 1,236 documents from U.S. Nuclear Regulatory Commission advanced reactor dockets and demonstrated with a working multi-agent pilot. Against an 89M USD, 42-month Reconstructed Baseline, RCP cuts costs by 50-77 percent (21M-44M USD) and timelines by 65 percent (15 months). Without a shared protocol, Standalone Agents reach only 54M-74M USD and 21 months. The residual cost-and-time gap is structural, not algorithmic: it traces to the inter-organizational pipeline that only an agent-to-agent standard can compress. The same bottleneck - formal multi-party review under strict auditability requirements - characterizes pharmaceutical approvals, environmental permitting, financial supervision, and aviation certification. The US regulatory paperwork burden carries a 426.5 billion USD annual opportunity cost; replicated broadly, the projected 50-77 percent reduction implies savings on the order of 210-330 billion USD per year - approaching 1 percent of US GDP.

---


### 94. [Still: Amortized KV Cache Compaction in a Single Forward Pass](https://arxiv.org/abs/2606.07878)

**<font color=#1a73e8>作者：</font>** Charles O'Neill, Alex Sandomirsky, Harry Partridge 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The KV cache is the memory bottleneck of long-horizon language model deployment. Practically, a deployable compactor must be lightweight enough to call during inference, expressive enough to preserve context under constraint, and reusable across a trajectory. Existing compaction methods satisfy only part of this requirement: selection methods are lightweight but subset-bound, while synthesis methods are expressive but rely on per-context optimization. Here we introduce Still, a small per-layer Perceiver trained once against a frozen base model that produces compact keys and values in a single forward pass. On Qwen and Gemma models, Still occupies the favorable side of the speed--quality frontier across compression ratios from $8\times$ to $200\times$ and context lengths from $8$k to $128$k. On the long-context RULER grid, Still exceeds the strongest baseline by 8--22 points. The same compact cache also supports free-form summarization, preserving most of the full-context gain on HELMET and winning a pairwise LongBench summarization comparison against KV-Distill. Because compaction is a forward pass, Still can be applied iteratively, entering a long-horizon regime unavailable to per-context methods. We show that amortization makes long-context cache compaction tractable, and synthesis makes its compact state useful at extreme compression.

---


### 95. [Breaking the Bubble: Asynchronous Pipeline Parallel Training with Bounded Weight Inconsistency](https://arxiv.org/abs/2606.07881)

**<font color=#1a73e8>作者：</font>** Itay Elam, Eliron Rahimi, Avi Mendelson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pipeline parallelism is essential for training large neural networks, but existing schedules trade off throughput, memory, and optimization consistency. Synchronous pipelines preserve forward/backward weight consistency but suffer from bubbles; asynchronous pipelines remove bubbles but introduce weight-version mismatch, typically requiring weight stashing, prediction, or correction mechanisms. We introduce PACI (Pipeline Asynchronous training with Controlled Inconsistency), a bubble-free asynchronous pipeline method that bounds forward/backward version drift without weight stashing, prediction, additional parameter copies, or global synchronization. The key idea is to use local gradient accumulation as a version-control mechanism: by slowing parameter-version evolution relative to pipeline delay, PACI limits the number of optimizer updates crossed by any micro-batch while preserving steady-state utilization. In GPT-style language-model pretraining, PACI matches the stability and final perplexity of synchronous 1F1B-flush, retains the same peak memory footprint, achieves fully utilized pipeline throughput, and improves training time-to-accuracy by up to $1.69\times$ over the fastest flush baseline. These results show that forward/backward inconsistency need not be eliminated: when explicitly bounded, it can be safely traded for substantial efficiency gains.

---


### 96. [The Cross-Architecture Substrate: A Domain-Transcendent, Calibration-Surviving Geometric Invariant of Modern Vision Encoders](https://arxiv.org/abs/2606.07882)

**<font color=#1a73e8>作者：</font>** Yousef Radwan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Different vision neural networks -- trained to classify, contrast, reconstruct, or match images to text -- should have correspondingly different internal representations. We report that they do not. After training, the top sixteen principal directions of variation inside thirteen modern vision encoders converge to the same sixteen-dimensional geometric object. We call this the cross-architecture substrate and study it with PCA, centred kernel alignment (CKA), and Pang 2026 calibration. The substrate transports across four visual domains (natural photographs, medical CT, satellite, microscopy) at median Procrustes-CKA 0.679, and across eight domains (adding sketches, depth, thermal infrared, astronomy) at 0.604, every pair >0.40. It survives Pang calibration globally (7.4x disc-vs-MAE separation, n=13,394) and locally (4.82-5.30, p<10^{-44}). It is not pixel statistics (0.263), not Gabor features (0.31), not a random projection (0.041), and emerges in the first 10% of training while accuracy keeps climbing. We deliver four applications: a label-free transferability filter beating LogME (3x faster, +0.15 Kendall-tau); a four-way domain detector (99.6% accuracy); a frozen low-shot probe (16 dims beat 768-dim DINOv2 by 3.78pp at N=50 labels per class); and a teacher-free distillation auxiliary matching trained-teacher KD on 33 pairs (7.56pp peak gain at 10% label fraction). The substrate does not cross modalities, does not help cross-paradigm distillation, and does not predict transfer quality (rho=0.08 against transfer accuracy).

---


### 97. [DP4SQL: Differentially Private SQL with Flexible Privacy Policies](https://arxiv.org/abs/2606.07883)

**<font color=#1a73e8>作者：</font>** Andrew Cascio, KinChin Tong, Daniel Kifer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The plausible deniability model of differential privacy for single-table datasets is well-understood. However, applying differential privacy to relational databases is much trickier: each application needs flexibility in specifying the pieces of information about an entity, spread across multiple relations, that require plausible deniability guarantees. Existing differentially private SQL systems only support rigid privacy policies. Even seemingly small changes, such as specifying that some tables need to protect the existence of records while others only need to protect the record contents, require significant manual effort in updating their privacy accountants and proving their correctness.
One example of a challenge is the presence of partially public data. Public columns in a table (e.g., faculty names in a university dataset and partial course enrollment information) can cause some queries to require more noise (compared to fully private data), while others require less noise. This kind of reasoning is not supported in existing systems. Another example is when different parts of records (e.g., demographics, financial data) require different levels of privacy protection. Again, existing differentially private SQL systems need to rewrite their rules for calculating query stability in order to support such a feature. This paper presents DP4SQL, a differentially private SQL system that allows data curators to better customize the plausible deniability requirements for their relational databases. This avoids the drawbacks of the "one-size-fits-all" systems that would either underprotect the data or inject too much noise into query answers.

---


### 98. [Strained Coherence: A Pre-Failure Signal in Coding Agent Execution Trajectories](https://arxiv.org/abs/2606.07889)

**<font color=#1a73e8>作者：</font>** Marut Pandya, Kasey Zhang, Baiqing Lyu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-based coding agents sometimes acknowledge a problem in their own reasoning and then proceed anyway. We call this pattern strained coherence: a safety-relevant failure mode in which an agent has information that should change its behavior, states that information, and still acts against it. The pattern overlaps with verbalized reward hacking, where an agent names a tension between a task proxy and the underlying goal yet optimizes the proxy anyway. We give an operational definition, build a Claude Sonnet 4.6 judge that reads full trajectories and flags spans where the pattern occurs, and evaluate it on 44 Terminal-bench-2 trajectories using a Qwen3.5-35B-A3B backbone. Flagged trajectories fail 94% of the time versus 46% for unflagged trajectories (47-point gap, Fisher's exact p = 0.003; 46 points after excluding three prompt-embedded examples, p = 0.006). At matched selectivity, the detector reaches 94% precision versus 88% for a lexical discourse-marker baseline; the 10-trajectory intersection of the two methods has a 100% failure rate (Clopper-Pearson 95% CI [69%, 100%]). We replicate on Gemma4-31B with 43 trajectories: the overall signal is directionally consistent but not significant (20-point gap, p = 0.31), with attenuation driven largely by 13 trajectories with zero think content, where the detector has no substrate to analyze. In the high-verbosity Gemma tertile, the gap is +30 points; in the mid- and high-verbosity Qwen tertiles, it is +40 points each. The first flag appears at a median of 83-84% of elapsed trajectory time across both models, and the binary flag survives paraphrases that soften explicit conflict markers (8/8 trajectories). Unlike univariate predictors, the detector emits interpretable span-level output -- quoted acknowledgment, quoted action, and typed conflict -- showing what the agent saw and ignored.

---


### 99. [Partially Performative Prediction](https://arxiv.org/abs/2606.07890)

**<font color=#1a73e8>作者：</font>** Jaewook Lee, Tijana Zrnic  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Performative prediction studies feedback loops that arise when predictive models are deployed in consequential domains. In these settings, deploying a model can change the population whose patterns the model aims to predict, inducing a distribution shift that is endogenous to the learning system. This perspective departs from classical treatments of distribution shift, where shifts are typically modeled as exogenous changes in the data-generating process. Yet, in practice, distribution shift is rarely one or the other. Predictive models may influence future data through the decisions they support, while the world itself continues to drift for reasons beyond the learner's control. We study partially performative prediction, a framework that captures both endogenous and exogenous sources of distribution shift. The framework generalizes performative prediction by allowing the data distribution to evolve both in response to the deployed model and according to an external, time-varying process. We extend the central notions of performative stability and performative optimality to this setting by defining their online analogues that track the evolving partially performative environment. We analyze practical learning heuristics, including repeated retraining, and characterize when they successfully adapt to partially performative environments.

---


### 100. [C3VD-DEFCOL: A Deformable Colonoscopy Dataset with Time-Resolved 3D Ground Truth and Realistic Appearance](https://arxiv.org/abs/2606.07891)

**<font color=#1a73e8>作者：</font>** Ethan Luk, Mayank V. Golhar, Anthony Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D reconstruction could improve colonoscopy by estimating mucosal coverage and alerting clinicians to missed regions during screening. However, algorithm development is limited as no current datasets provide both a realistic in vivo appearance and dense, time-resolved 3D ground truth, especially under non-rigid deformation. We present C3VD-DEFCOL, a framework and dataset for evaluating deformable colonoscopy reconstruction with paired geometry and realistic texture. Starting from C3VD/C3VDv2 colon meshes and camera trajectories, we generate controlled deformations of the colon surface, including peristaltic waves and centerline motion, and render per-frame depth, surface normals, optical flow, camera poses, and time-stamped 3D meshes. We then use the rendered geometry, primarily depth, to condition an LTX-2.3-based sim-to-real translation model that produces RGB clips with in vivo-like mucosal color, texture, vasculature, and specular appearance while preserving the underlying 3D scene structure. The resulting dataset contains 110 videos from 11 unique colon mesh geometries, with varying camera trajectories, appearances, and parameterized deformation regimes, including three peristaltic severity levels that serve as controlled evaluation axes. We evaluate the generated videos using appearance realism, geometric consistency, and temporal consistency metrics, and use the paired ground truth to benchmark the downstream task of pose estimation in deformable 3D reconstruction. Our experiments show how pose estimation error increases with increasing deformation severity, providing a controlled stress test that is not possible with existing in vivo datasets. Overall, C3VD-DEFCOL is designed as a reproducible, quantitative evaluation platform for testing deformable 3D reconstruction algorithms, with the goal of reducing the domain gap between synthetic datasets and in vivo colonoscopy.

---


> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-527](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
