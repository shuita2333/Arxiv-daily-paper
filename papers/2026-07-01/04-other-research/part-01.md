# 📦 其他研究 | 2026年07月01日

> 本类共 **489** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-489](./part-10.md)

---

### 1. [Generating in the Limit with Infinitely Many Hallucinations](https://arxiv.org/abs/2606.28354)

**<font color=#1a73e8>作者：</font>** Irene Strauss, Alexandra Butoi, Ryan Cotterell  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The classic paradigm of language identification in the limit models learning as a game between an adversary, who reveals strings from an unknown target language, and a learner tasked with identifying that language. The recently introduced framework of language generation in the limit shifted the objective to better reflect modern language modeling, requiring the learner to produce valid, unseen strings from the target language. Related work highlighted a fundamental tension: a broad coverage of the target often comes at the cost of validity. We introduce a new notion of precision and recast this problem as the classic recall-precision trade-off. We analyze generation in the limit under varying constraints on enumeration, novelty, and validity, aimed at reflecting settings closer to those encountered by large language models. A key contribution is our analysis of learners that are not eventually valid: we allow infinitely many mistakes, provided their frequency tends to zero so that precision remains one. We show that this relaxation can strictly increase recall when the adversary permanently withholds a large portion of the target language. We also study a continuous relaxation of the novelty constraint that requires only a fixed fraction of outputs to be novel. Taken together, our results move toward a more realistic model of language generation where occasional errors and repetitions are unavoidable, but their rates are controlled.

---


### 2. [GeoISF: Instance Semantic Forest Inspired Large-Scale Cross-View Geo-Localization via Ground LiDAR-to-Satellite Image](https://arxiv.org/abs/2606.28371)

**<font color=#1a73e8>作者：</font>** Di Hu, Xia Yuan, Chunxia Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The problem of localization on a large-scale satellite image given a frame of query ground view point clouds remains challenging. Existing LiDAR-to-image cross-view localization methods struggle in large-scale scenarios due to limited semantic alignment and the modality gap between point clouds and satellite images. This paper introduces the large-scale LiDAR-to-image geo-localization pipeline called GeoISF. GeoISF introduces an instance semantic forest constructed using WordNet, which enhances temporal semantic representation and discriminative power by integrating semantic trees from multiple frames. By leveraging environmental semantic representation as a shared medium, GeoISF effectively bridges the modality gap and improves semantic matching accuracy. Extensive experiments demonstrate the superior performance of GeoISF in large-scale cross-view localization, 13.22 times better than the parallel LiDAR-to-image method in the R@10 metric on the KITTI dataset. The proposed method addresses the existing gap in large-scale LiDAR-to-image cross-view localization, offering a robust solution to the computational and accuracy challenges inherent in such scenarios. We will release the code as an open-source resource available online for the broader research community.

---


### 3. [Recursive Self-Evolving Agents via Held-Out Selection](https://arxiv.org/abs/2606.28374)

**<font color=#1a73e8>作者：</font>** Michael Nguyen, Quoc Nguyen, Paul Vuong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly improved without weight updates by evolving a natural-language artifact, such as reflections, workflows, playbooks, cheatsheets, or optimized prompts, that conditions a frozen policy. Such methods are typically reported as wins on the single benchmark where they help. We study them apples-to-apples and surface a sharper picture. We introduce RSEA, a Recursive Self-Evolving Agent that carries a compact three-layer natural-language state: an imperative strategy, reusable skills, and a procedural playbook. Across generations, RSEA rewrites all three layers from its own trajectories and commits a candidate only if it does not regress on a disjoint held-out split, using a strict keep-better gate.
Across four diverse benchmarks, ALFWorld, GAIA, (\tau)-bench, and WebShop, and six faithful baselines, ReAct, Reflexion, GEPA, AWM, ACE, and Dynamic Cheatsheet, all evaluated on one shared local backbone, we find three main results. First, no artifact universally wins. RSEA is the strongest single-pass method on ALFWorld, reaching 69.3% compared with 64.6% for ReAct (McNemar (p=0.015)), and reaches 79.4% with retry, the best overall result. However, concrete-workflow induction, represented by AWM, is best on the strong-backbone tool-use tasks. Second, unguarded context evolution is high-variance and unsafe. Dynamic Cheatsheet, which curates context online without a held-out gate, is near-best on ALFWorld at 70.7%, yet collapses on WebShop, with a score of 0.14 compared with 0.43 for ReAct. Third, RSEA's strict held-out selection is what makes recursive self-evolution monotone-safe: it never significantly underperforms the base agent on any benchmark and falls back to vanilla ReAct when evolved context would hurt.

---


### 4. [Memory-Augmented LSTM Autoencoder for Unsupervised Activity Recognition with IMU Sensor Fusion](https://arxiv.org/abs/2606.28377)

**<font color=#1a73e8>作者：</font>** Saeid Arabzadeh, Farshad Almasganj, Mohammad Mahdi Ahmadi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> HAR using Inertial Measurement Unit (IMU) sensors is vital for healthcare monitoring and rehabilitation. Despite deep learning advancements, major challenges remain: reliance on labeled data, multi-sensor fusion complexity, and the limited ability of unsupervised methods to capture spatiotemporal dependencies. These issues are pronounced in real-world scenarios with noisy data, overlapping activities, and missing labels. We propose a fully unsupervised spatiotemporal feature fusion framework using a memory-augmented autoencoder. It enhances activity representations via short temporal windows of multi-sensor IMU data, enabling real-time applications. Our framework extracts hierarchical static features via a Stacked Autoencoder, fusing them within and across sensors. A sequence-to-sequence LSTM Autoencoder then temporally refines these features, incorporating historical motion patterns without labels. We analyze key hyperparameters to identify configurations that maximize feature separability under short-window constraints. Evaluated on DaLiAc and PAMAP2 using realistic inter-class window segmentation, our method achieves 96.6% and 98.4% accuracy, respectively, surpassing supervised baselines and unsupervised approaches. Our method improves feature separability by up to 9% despite shorter temporal windows. While our realistic inter-class segmentation reduces accuracy by ~7%, it was intentionally adopted to better reflect real-world activity transitions and practical relevance.

---


### 5. [Formation of Circular Directed Networks with Shared Link Costs](https://arxiv.org/abs/2606.28382)

**<font color=#1a73e8>作者：</font>** Juan M.C. Larrosa, Fernando Tohmé  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This paper develops a noncooperative model of directed network formation in which agents create links to access valuable information while sharing the costs generated along the paths through which information is obtained. Each agent is endowed with a positive amount of information and chooses, simultaneously, which other agents to contact. A directed link initiated by one agent allows her to access the information of the contacted agent and of the latter's reachable network, but each link in the resulting information path entails a unit cost. Payoffs therefore depend on the total value of accessible information net of the accumulated connection costs required to obtain it. The paper characterizes the relationship between strategy profiles and directed graphs, defines accessibility, paths, components, and minimal connectedness, and studies the Nash architectures induced by individual best responses. The central result is that strict Nash equilibria must take the form of circular directed networks. Moreover, circular networks are exactly the Nash networks that use the minimum number of links while allowing every agent to access all available information. Although noncircular weak Nash networks may exist, they are structurally redundant and do not satisfy the same minimality property. The model also shows that strict Nash networks are both Pareto optimal and efficient in terms of aggregate welfare. Finally, the paper compares this framework with Bala and Goyal's model, emphasizing that shared path costs and heterogeneous information values generate different equilibrium implications. The analysis supports the equivalence between strict stability and minimal connectivity in directed information networks.

---


### 6. [Zero-Label Driving Scenario Complexity Detection via Joint Embedding Predictive Architecture](https://arxiv.org/abs/2606.28383)

**<font color=#1a73e8>作者：</font>** Santosh Jaiswal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identifying complex and safety-critical driving scenarios in large unlabelled datasets is an important but expensive problem. Existing approaches rely on human annotators, supervised classifiers, or carefully engineered rule sets, all of which require substantial prior knowledge about what constitutes a difficult scenario. We ask whether a model can discover scenario complexity on its own, with no labels at any stage. We train a minimal Joint Embedding Predictive Architecture (JEPA) on structured agent state data from the nuPlan mini dataset and use the temporal prediction error as a zero-shot complexity score. Without access to any ground-truth labels during training or evaluation setup, the model assigns significantly higher scores to scenarios involving unprotected turns, crosswalk interactions, and pedestrian proximity, and significantly lower scores to lane-following and stationary-traffic scenarios. We validate this finding through four ablation experiments that isolate the source of the signal, and through a downstream anomaly detection evaluation that achieves Average Precision of 0.512 against a 0.436 chance baseline. The results show that temporal prediction error in a self-supervised latent world model is a practical proxy for driving scenario complexity.

---


### 7. [Data Provenance for Image Auto-Regressive Generation](https://arxiv.org/abs/2606.28386)

**<font color=#1a73e8>作者：</font>** Bihe Zhao, Louis Kerner, Michel Meintz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image autoregressive models (IARs) have recently demonstrated remarkable capabilities in visual content generation, achieving photorealistic quality and rapid synthesis through the next-token prediction paradigm adapted from large language models. As these models become widely accessible, robust data provenance is required to reliably trace IAR-generated images to the source model that synthesized them. This is critical to prevent the spread of misinformation, detect fraud, and attribute harmful content. We find that although IAR-generated images often appear visually identical to real images, their generation process introduces characteristic patterns in their outputs, which serves as a reliable provenance signal for the generated images. Leveraging this, we present a post-hoc framework that enables the robust detection of such patterns for provenance tracing. Notably, our framework does not require modifications of the generative process or outputs. Thereby, it is applicable in contexts where prior watermarking methods cannot be used, such as for generated content that is already published without additional marks and for models that do not integrate watermarking. We demonstrate the effectiveness of our approach across a wide range of IARs, highlighting its high potential for robust data provenance tracing in autoregressive image generation.

---


### 8. [SoccerNet 2026 Player-Centric Ball Action Spotting: Per-Player Attention with Agreement-Based Ensembling](https://arxiv.org/abs/2606.28389)

**<font color=#1a73e8>作者：</font>** Faisal Altawijri, Ismail Mathkour  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present our submission to the SoccerNet 2026 Player-Centric Ball Action Spotting challenge, which uses a two-stage pipeline: a Track-Aware Action Detector (TAAD) produces per-player action logits from broadcast video, and a Denoising Sequence Transduction (DST) transformer converts game-state features and TAAD logits into structured event sequences. We improve the TAAD with a temporal transformer that adds cross-frame context, alongside several training fixes. For the DST stage, we introduce a two-stage per-player attention mechanism operating on game-state features, and show that a spatial-first attention ordering (cross-player attention before temporal attention) improves validation Macro-F1 by 1.87%. To exploit architectural diversity, we train four model variants and combine them with a Weighted Event Fusion ensemble that applies agreement filtering to suppress single-model false positives while preserving recall, plus a dedicated exception for the rare tackle class. Our final system improves the challenge Macro-F1 from a baseline of 48.6 to 58.94.

---


### 9. [Automated Quality Assessment of Geospatial Vector Data: A GeoAI Approach using Spatial Representation Learning](https://arxiv.org/abs/2606.28390)

**<font color=#1a73e8>作者：</font>** Hao Li, Chen Chu, Filip Biljecki 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geospatial vector data quality is a foundational research topic in GIS, yet classic rule-based quality assessment algorithms often struggle with diverse urban morphologies and massive data volumes. Recently, Geospatial Artificial Intelligence (GeoAI) shows promising potential for automating geospatial analysis, while its application to native vector data remains largely underexplored. To fill this research gap, we proposed Topo4Vec, an automated GeoAI framework, designed for scalable vector data quality assessment via advanced Spatial Representation Learning (SRL). Specifically, Topo4Vec relax the labor-intensive manual annotation process via topological error simulation, such as overlapping polygons and street network connectivity errors e.g., overshoots and undershoots. Then, it leverages state-of-the-art SRL approaches to encode complex, native vector geometries (e.g., polylines and polygons) into a latent space where topological errors are isolated from valid ones. A systematic performance evaluation across three study areas (Los Angeles, Munich, and Singapore) demonstrates the effectiveness and robustness of Topo4Vec, achieving a peak accuracy of 0.99 for detecting overlapping building footprints and 0.60 for overshoots and undershoots in street networks. Moreover, lessons learned from Topo4Vec shed a promising light into a scalable and autonomous GeoAI approach for large-scale vector data consistency and quality monitoring within the fast-growing geospatial data ecosystems. The code and data used in the paper are made openly available in this https URL.

---


### 10. [Few-class Fidelity: Evaluating Explanations of Real-conditions CNN classifiers with Optimized Perturbations](https://arxiv.org/abs/2606.28391)

**<font color=#1a73e8>作者：</font>** Wistan Marchadour, Pedro Soto Vega, Franck Vermet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The wide use of Convolutional Neural Networks (CNN) in numerous domains and real-world classification applications is justified by their high precision and automation speed, helping users concentrate on higher-expertise tasks. To better understand the models and avoid bias during deployment, eXplainable Artificial Intelligence (XAI) techniques can be used after training. But as the list of XAI solutions expand, comparisons between them diverge, and consensus over their evaluation cannot be reached. This paper proposes a variation of Fidelity-based XAI metrics, with a focus on real-conditions applications, where the number of classes is often low. The approach generates in-distribution, uncertainty-provoking perturbations, to ensure proper measurement of the XAI methods faithfulness. As demonstration of the evaluation framework usefulness, it is compared with human-centric object localization and segmentation metrics. Once applied to both medical and natural imaging applications, it highlights the intricate correlation between domain, data curation, and XAI solution choices in order to validate training of a new CNN model.

---


### 11. [Transition-Aware best-of-N sampling for Longitudinal Chest X-ray Reports](https://arxiv.org/abs/2606.28393)

**<font color=#1a73e8>作者：</font>** Halil Ibrahim Gulluk, Max Van Puyvelde, Wim Van Criekinge 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In longitudinal clinical practice, every chest X-ray is read in the context of the patients prior exam, and much of what the radiologist communicates is the change from one visit to the next. To the best of our knowledge, we present the first training-free best-of-N sampling scheme for pre-trained chest X-ray report generators that is explicitly aware of this longitudinal prior to current transition. We call it transition-aware best-of-N sampling, each report is split into sentences and embedded into an unordered set in Rd; each (prior, current) pair is reduced to a fixed-dim directional vector via a set-to-set distance designed to encode the change between the two sets; and candidates are scored by cosine distance from their candidate transition vector to a cached bank of ground-truth training transition vectors, aggregated as min or kNN. We instantiate the framework with four directional set distances (mean-shift, novelty residual, directed-Hausdorff anchor, and cost-weighted optimal transport) and evaluate on a multi-visit AP-PA cohort, running inference under three prompts on three vision-language generators. Transition-aware best-of-N outperforms random selection across the board, with the largest relative gains on the Impression section.

---


### 12. [GPU-Accelerated Inverse Structural Anastylosis from Block Collapse Dynamics](https://arxiv.org/abs/2606.28394)

**<font color=#1a73e8>作者：</font>** L.A. Muñoz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The physical anastylosis of collapsed architectural monuments -- the meticulous reassembly of fallen stone elements into their original structural configuration -- represents one of the most intellectually demanding challenges in conservation science. Traditional approaches depend heavily on expert archaeologist judgement and manual block-by-block correspondence, a process that is both labour-intensive and inherently subjective. Inspired by the combinatorial complexity of this problem as manifested in the game of Jenga, we present Jenga Inverse Predictor , a GPU-accelerated deep learning framework that addresses structural anastylosis as an inverse prediction task. Given an image of a collapsed block assembly, JIP-2 reconstructs the most probable prior tower configuration by: (1) implementing a complete rigid-body physics engine with OBB/SAT collision detection and a Projected Gauss-Seidel (PGS) contact solver accelerated with Numba JIT and CuPy CUDA; (2) applying the analytical force thresholds of Ziglar (CMU, 2006) -- F_app = 3*mu_s*m*g (Y-axis, torque-free) and F_app = 4*mu_s*m*g (X-axis, torque risk) -- over three friction levels (mu_s in {0.25, 0.40, 0.60}) across 450 simulated episodes; (3) training a dual-stream ResNet-18 that injects a friction one-hot vector and jointly predicts block removal count, per-position removal probabilities, centre-of-mass imbalance, and Ziglar torque risk; and (4) generating a smooth 3-D video of the block-by-block reverse reconstruction. We discuss implications for computer-assisted anastylosis at the UNESCO Maya site of Uxmal, Yucatan, and provide a detailed technical description of the full pipeline, architecture, and loss formulation.

---


### 13. [JASPR: Joint Spatial Representation learning of histology and spatial genomics for improved virtual genomic screening and clinical prognostication](https://arxiv.org/abs/2606.28395)

**<font color=#1a73e8>作者：</font>** Marija Pizurica, Eric Zimmermann, Neil Tenenholtz 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent studies have shown that spatial properties of tumors are critical for understanding disease biology and predicting patient outcomes. These spatial properties are increasingly uncovered through complementary modalities: spatial transcriptomics (ST) captures spatially-resolved molecular states, while hematoxylin and eosin-stained whole slide images (HE) reveal tissue morphology. While approaches are emerging to fuse these modalities, effective methods that learn not only joint representations but also incorporate spatial context across modalities are lacking. Here, we present JASPR (Joint Spatial Representation learning), a self-supervised deep learning framework that integrates HE images and ST data through a cross-modal reconstruction objective that incorporates spatial context within HE images and ST profiles. It employs shared modules to capture universal spatial properties across modalities, while modality-specific experts encode features unique to morphological and genomic data. We train and validate JASPR on breast cancer datasets, demonstrating that its learned joint representation substantially improves HE-based prediction of 9,248 genes and provides prognostic value for breast cancer outcomes.

---


### 14. [RadarTwin: Scene-Specific mmWave Radar Simulation and Learning for Mobile Indoor Perception](https://arxiv.org/abs/2606.28396)

**<font color=#1a73e8>作者：</font>** Emily Bejerano, Federico Tondolo, Devang Gupta 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Millimeter-wave (mmWave) radar perception is limited by data scarcity: models trained on existing radar datasets fail to generalize to new objects, environments, and sensing trajectories. We present RadarTwin, a framework for generating deployment-specific radar training data before real data collection. Given a 3D reconstruction of a target space (phone LiDAR, robot-mounted sensing, or RGB-to-3D), RadarTwin uses a vision-language model to infer radar-relevant surface materials and a physics-based ray tracer to synthesize raw frequency-modulated continuous-wave (FMCW) radar measurements with multi-bounce propagation. To study what transfers from simulation to reality, we collect a paired real-simulated dataset spanning household objects, material classes, distances, rotations, translations, and mobile sensing trajectories. We show that simulated and real radar share the same object-discriminative shape and material features, and that modeling the environment's multipath is essential to matching real measurements. A representation trained on simulation alone recognizes real objects at 2.5 times chance with no real radar labels, and a few labeled examples raise this to 95.3% on a 12-way recognition task. RadarTwin enables training radar perception for a new space before any real radar data is collected there.

---


### 15. [CLOSER-VLN: Closed-Loop Self-Verified Retrieval-Augmented Reasoning for Aerial Vision-Language Navigation](https://arxiv.org/abs/2606.28397)

**<font color=#1a73e8>作者：</font>** Shaoxuan Li, Xiangyu Dong, Xiaoguang Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language navigation (VLN) has recently advanced with large language and multimodal models, enabling agents to follow natural-language instructions in unseen environments without training a task-specific navigation policy. However, most existing VLN methods relying on large models still adopt an open-loop decision-execution approach, where candidate actions are generated from instructions and observations but are rarely verified or corrected before execution. This causes critical issues in aerial VLN, where minor errors in intermediate actions may quickly accumulate into large trajectory deviations and lead to target loss. To address this issue, we propose Closed-loop Self-verified Retrieval-augmented Reasoning (CLOSER), a training-policy-free method that sequentially performs action reasoning, reliability verification, targeted retrieval, and action correction in a closed-loop manner before executing concrete actions. We instantiate the CLOSER in aerial VLN tasks and develop a CLOSER-VLN framework, which is composed of three components: a hierarchical reasoner for generating candidate actions based on available information, a multidimensional action verifier for assessing the reliability of actions generated by the reasoner, and a verification-triggered multimodal retriever for retrieving targeted exemplars from a memory bank only when verification fails. We conduct experimental evaluations on the CityNav benchmark, where CLOSER-VLN achieves 32.01% SR and 21.28% SPL on the test-unseen split, confirming the effectiveness of closed-loop reasoning.

---


### 16. [Semantic-Aware Generative Image Transmission for Resource-Constrained Visual IoT Systems](https://arxiv.org/abs/2606.28398)

**<font color=#1a73e8>作者：</font>** Chenyang Zhang, Changwang Liu, Jinqi Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Resource-constrained visual Internet of Things (IoT) systems, such as edge cameras, unmanned sensing platforms, industrial inspection nodes, and remote monitoring sensors, often need to transmit task-relevant visual evidence over low-rate wireless links to an edge/cloud service. Existing image communication methods usually compress or transmit complete global representations, leaving limited room to exploit receiver-side generative restoration. This paper proposes a semantic-aware generative image transmission framework for edge-assisted visual IoT. The image captured by an IoT visual sensor is encoded into a discrete token grid by a VQ encoder. At the IoT transmitter or nearby gateway, token recoverability, estimated from prediction entropy and local structure complexity, is fused with semantic importance obtained from instance segmentation and category-aware scoring. A spatial dispersal sampler then selects the tokens to be transmitted under a bitrate budget. The transmitter sends only the quantization indices of kept tokens and a binary mask map, while the edge/cloud receiver recovers masked tokens through MaskGIT with Halton sequence scheduling. Experiments on Kodak and VisDrone scenes under AWGN and Rayleigh channels show that the proposed method provides a flexible bitrate-quality tradeoff for narrowband visual IoT links. At 0.074 bpp, it uses 44.6% of the transmitted bits of the 0.167-bpp DeepJSCC/WITT reference while achieving 29.9 dB PSNR. A pseudo-GT downstream detection study on Kodak further shows that semantic-aware masking preserves task-relevant objects better than random masking at both 30% and 50% mask ratios.

---


### 17. [Meta-learning as a principle for human-like visual representations](https://arxiv.org/abs/2606.28399)

**<font color=#1a73e8>作者：</font>** Can Demircan, Marcel Binz, Alireza Modirshanechi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The structure of human visual representations underpins our capacity for adaptive behaviour. While pretrained neural networks model human visual representations with unprecedented success, a large discrepancy remains. We propose one reason: these networks optimise a single fixed objective, whereas human representations must support open-ended tasks. We hypothesise this flexibility arises from meta-learning (learning to learn), a pressure shaping representations to acquire new tasks from few observations. To test this, we train a sequence model, without any supervision from human data, across thousands of semantically rich tasks mapping images to high-level concepts. Compared to their pretrained base encoders, meta-learned representations better predict human similarity judgements, semantic rule learning, and high-level visual cortex. Behavioural gains depend on disentangled, high-level task distributions, while brain alignment is driven primarily by the learning-to-learn pressure. Our results suggest the flexibility of human visual representations reflects the functional demand to learn new semantic relationships on the fly.

---


### 18. [DCSNet: Multiscale Feature Aggregation for Small Medical Object Segmentation with Detection-guided Hierarchical Cropping](https://arxiv.org/abs/2606.28402)

**<font color=#1a73e8>作者：</font>** Shanfeng Zhang, Bo Gou, Yue Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Small object segmentation in medical imaging is primarily hindered by class imbalance and inherent boundary complexity. Consequently, conventional global networks frequently fail to detect sparse targets or suffer from severe edge degradation. To overcome these limitations, we propose the Detection-guided Cropping Segmentation Network (DCSNet), an end-to-end framework that transforms global dense prediction into a localized refinement process. This framework integrates two core components, namely Detection-guided Hierarchical Cropping (DGHC) and Multiscale Feature Aggregation (MSFA). The DGHC module leverages region proposals to dynamically extract object-centric features, effdataectively filtering out massive background interference to mitigate class imbalance. Subsequently, the MSFA module operates strictly within these purified regions, synergizing a Transformer encoder with a pixel-adaptive fusion strategy. This mechanism dynamically aggregates multiscale features to capture both semantic context and fine-grained details for sharp boundary delineation. Extensive experiments across three diverse medical datasets demonstrate that DCSNet significantly outperforms existing state-of-the-art methods, yielding substantial improvements in boundary precision and offering a highly robust solution for clinical micro-lesion segmentation.

---


### 19. [Enhancing Layer Interaction Using Key-Correlated Layer Attention](https://arxiv.org/abs/2606.28405)

**<font color=#1a73e8>作者：</font>** Jianlong Xiong, ChuanBo Xie, Le Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in network architecture design have introduced layer attention to enhance inter-layer interactions. In such frameworks, each layer queries all preceding layers to establish cross-layer connections. However, layer attention results in quadratic computational complexity with respect to network depth. To mitigate this issue, prior works have proposed Recurrent Layer Attention (RLA) and linear attention mechanisms, which suffer from static information updates and limited long-range cross-layer dependency modeling. To overcome these limitations, we propose Key-Correlated Layer Attention (KCLA), inspired by our observation that Key representations in layer attention exhibit high cosine similarity. KCLA achieves linear computational complexity while preserving dynamic information updates, directly derived from the foundational definition of layer attention. Furthermore, KCLA maintains long-range cross-layer connections and features a fixed spatial complexity, independent of network depth. Empirical evaluations demonstrate that KCLA delivers good performance across diverse tasks, including image recognition, object detection, and medical image segmentation. The code is publicly available at this https URL.

---


### 20. [RSGPNet: Geometric Prompting for Remote Sensing Open-Vocabulary Semantic Segmentation](https://arxiv.org/abs/2606.28410)

**<font color=#1a73e8>作者：</font>** Shanwen Wang, Xin Sun, Sirui Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary semantic segmentation (OVSS) enables text-guided segmentation of unseen objects, breaking fixed-class limitations to achieve open-world understanding. However, existing OVSS methods primarily focus on modifying the CLIP attention mechanism, which still suffers from unstable local segmentation for remote sensing (RS) domain. To address these limitations, we propose RSGPNet, a training-free geometric prompting framework for RS OVSS that refines segmentation by leveraging object geometric areas and consistency constraints. Specifically, RSGPNet comprises three core modules: a Text-guided Coarse Mask module (TCM), a Geometric Re-prompting Module (GRP), and a Coarse-to-fine Consistency Verification Mechanism (CVM). TCM utilizes text prompts and the input image to construct initial coarse segmentation masks. GRP then converts these coarse masks into geometric box prompts, feeding them back into the segmentation model to generate refined masks. Finally, CVM employs consistency computation to prevent prompting from reinforcing erroneous regions. They allow the model to improve segmentation accuracy in complex areas, such as category boundaries. Extensive experiments on RS datasets demonstrate that RSGPNet significantly outperforms state-of-the-art methods across both quantitative and qualitative metrics while exhibiting excellent interpretability. The code is released at \href{this https URL}{this https URL}.

---


### 21. [On the Necessity of a Liquid Substrate for Mesh Intelligence](https://arxiv.org/abs/2606.28413)

**<font color=#1a73e8>作者：</font>** Hongwei Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A mesh of sovereign agents has no center: no shared clock, no shared model, and no coordinator to gather data or retrain. Its competence rests on each agent folding the projections its peers emit into a single internal state, online, from observations that arrive at irregular, unscheduled times, on a substrate whose weights it cannot retrain. Any one of these constraints is tractable on its own; folding optimally under all three at once is not. We ask what such a substrate must be, and prove two necessary conditions from one model of a self-evolving latent observed at irregular, exogenous times. Because the latent changes, its optimal estimator is time-varying: an adaptive timescale is necessary, and every fixed-gain filter is strictly suboptimal. And because arrivals are clock-free, the optimal estimate depends on the elapsed gap between them, which no gap-blind network recovers at any width or depth. This second condition is capacity-independent: scale cannot substitute for the missing dependence. The two conditions intersect in the continuous-time liquid class. An LSTM satisfies the first, a fixed continuous-time filter the second, and a multi-timescale liquid network both. Synthetic experiments confirm each: the network attains the timescale, and the separation is computed exactly. The characterization is necessary, not sufficient, and binds fixed-weight substrates: a network free to retrain reaches the class by other means. Proved per agent, the necessity binds every agent of a mesh, a structural condition on mesh intelligence.

---


### 22. [AEGIS: A Semantic GAN and Evidential Learning Frameworkfor Robust Adversarial Detection in Vision Sensors](https://arxiv.org/abs/2606.28416)

**<font color=#1a73e8>作者：</font>** Maher Boughdiri, Mounira Msahli, Albert Bifet  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks (DNNs) have shown outstanding performance in visual recognition tasks within vision sensor networks; however, they are still vulnerable to adversarial manipulations and imperceptible perturbations that can lead to erroneous predictions. To address that, this paper presents AEGIS, a semantic aware and uncertainty guided adversarial detection framework designed for robust image classification in vision sensors pipelines. At its core, a SemantiGAN module functions as a multi class semantic discriminator, identifying and filtering visually inconsistent adversarial inputs before they propagate further in the pipeline. For inputs that pass this stage, a stochastic augmentation process generates test time variations, from which handcrafted instability metrics FlipScore, Prediction Inconsistency, Layerwise Cosine Similarity (early and mid layers), and Entropy are computed. These features are aggregated into a compact five dimensional vector and processed by an Evidential Deep Learning (EDL) classifier, which models output evidence using a Dirichlet distribution to yield both class predictions and calibrated uncertainty estimates. Evaluations on the Tiny ImageNet dataset across six categories clean, FGSM, PGD, patch based, functional, and geometric attacks demonstrate the effectiveness of AEGIS. The proposed framework achieves an AUROC of 92.1\%, an AUPRC of 90.2\%, and an accuracy of 90.7\%, outperforming conventional softmax-based detectors in terms of detection performance, robustness, interpretability, and uncertainty calibration.

---


### 23. [DiffRGD: An Inference-Time Diffusion Guidance Through Riemannian Gradient Descent](https://arxiv.org/abs/2606.28417)

**<font color=#1a73e8>作者：</font>** Jia-Wei Liao, Li-Xuan Peng, Mei-Heng Yueh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, diffusion models have been widely adopted in generative modeling and have served as foundational models for many image generation tasks. To control the generation without costly re-training or fine-tuning, many works seek inference-time guidance methods to steer the latent via a differentiable objective at inference time. However, these methods cannot effectively preserve the original Gaussian distribution because they introduce distributional drift, thereby degrading the sample quality. To address this gap, we propose DiffRGD, a distribution-aware guidance framework that explicitly preserves the latent Gaussian structure. DiffRGD formulates each sampling step as a constrained optimization problem on a spherical manifold induced by the latent Gaussian distribution, and solves it efficiently via Riemannian Gradient Descent (RGD). DiffRGD is a plug-and-play method that can be seamlessly integrated into any pre-trained diffusion model. Extensive experiments demonstrate that DiffRGD outperforms previous methods in most image restoration and conditional generation tasks. Our codebase is available at this https URL.

---


### 24. [MedDiffuseMix: Preserving Diagnostic Evidence with Saliency-Aware Diffusion Medical Image Data Augmentatio](https://arxiv.org/abs/2606.28419)

**<font color=#1a73e8>作者：</font>** Teerath Kumar, Raja Vavekanand, Muhammad Turab  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Limited data availability, class imbalance, and domain variability remain major barriers to reliable medical image classification. Conventional augmentation can improve training diversity but may distort diagnostically informative structures, whereas unconstrained generative augmentation may introduce label-inconsistent content. This paper proposes MedDiffuseMix, a saliency-guided diffusion mixing framework for controlled medical image augmentation. The method uses classifier-derived saliency maps to separate high-saliency diagnostic regions from low-saliency background areas and applies diffusion-guided mixing mainly to regions with lower diagnostic importance. Adaptive mixing, Gaussian boundary blending, and a saliency-preservation constraint reduce semantic distortion and reject or attenuate samples that shift model attention away from clinically relevant evidence. The framework is evaluated on four public benchmarks: the Radiological Society of North America pneumonia chest radiography dataset, Musculoskeletal Radiographs, PatchCamelyon, and the Breast Cancer Histopathological Image Classification dataset. Experiments with convolutional and transformer-based classifiers show that MedDiffuseMix improves accuracy, F1-score, and area under the receiver operating characteristic curve compared with standard augmentation, Mixup, GenMix, SaliencyMix, and diffusion-based augmentation baselines. Ablation studies confirm the importance of saliency guidance, adaptive region mixing, and smooth boundary blending. Visual attribution analysis further indicates that MedDiffuseMix better preserves diagnostically salient regions. These results suggest that saliency-guided diffusion mixing is an effective augmentation strategy for limited-data medical image classification.

---


### 25. [Position: RL Researchers Need to Distinguish Between Solving Simulators and Using Simulators as a Proxy](https://arxiv.org/abs/2606.28433)

**<font color=#1a73e8>作者：</font>** Matthew Vandergrift, Esraa Elelimy, Martha White  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One goal in reinforcement learning (RL) research is to understand general-purpose sequential decision-making, using benchmark simulators as a proxy for learning in deployment settings. When running experiments, however, the goal of achieving high performance in the simulator can mutate into focusing exclusively on solving the simulator. To achieve high scores, researchers may adopt solutions exclusively meant for solving simulators, rather than learning while the agent is deployed outside a simulator. Solving simulators is also worthy of investigation, but it is a fundamentally different RL research question. In this paper, we argue that RL researchers need to distinguish between two use cases of simulators: solving simulators and using simulators as a proxy for learning in deployment. We first discuss how these two use-cases are importantly different, in terms of constraints on how the agent can use the simulator, which algorithms are appropriate, and which evaluation metrics are appropriate. We then highlight several issues and misleading conclusions that can occur by not making the distinction between these two settings clear, supported with examples and simple experiments. This work is a call to the community to begin clearly distinguishing how they are using simulators in their work, hopefully sparking further discussion on which empirical practices work best in each setting.

---


### 26. [PLAA: Packet-level Adversarial Attacks in Network Traffic Detection](https://arxiv.org/abs/2606.28439)

**<font color=#1a73e8>作者：</font>** Jinhao You, Zan Zhou, Shujie Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep neural networks (DNNs) are widely applied in Network-based Intrusion Detection System (NIDS) due to their high accuracy. However, DNNs are highly susceptible to adversarial attacks, which generate malicious traffic to evade NIDS detection. Existing approaches often adapt adversarial attacks from computer vision (CV) tasks to the NIDS domain, overlooking the fundamental differences between CV and NIDS. This results in two major issues: 1) The generated network traffic may become invalid, 2) The generated traffic may lose its original attack semantics. To address these issues, this paper proposes an adversarial attack specifically designed for NIDS. Instead of directly generating flow-level features, our approach incrementally generates packet-level features to construct adversarial traffic. During the generation process, the semantic integrity of the traffic is monitored at each stage, effectively avoiding the issues of invalid traffic and semantic loss observed in existing methods. We evaluate our attack algorithm against current NIDS models using the CIC-UNSW-NB15, CIC-DDoS2019, and CIC-IDS-2017 datasets. The proposed method achieves an average evasion success rate of 92.78%, while ensuring that the generated adversarial traffic remains semantically consistent with the original malicious traffic.

---


### 27. [Learning to Distributedly Estimate under Partially Known Dynamics: A Covariance-Agnostic Neural Kalman Consensus Filter](https://arxiv.org/abs/2606.28441)

**<font color=#1a73e8>作者：</font>** George Stamatelis, Kyriakos Stylianopoulos, George C. Alexandropoulos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online latent state estimation constitutes a fundamental challenge within the artificial intelligence field, serving as a foundational tool for diverse applications, including sequential decision making, anomaly and change-point detection. In this paper, a novel online distributed sensing framework, where agents collaborate and exchange information to perform latent state estimation, is presented. The proposed estimator combines available partial domain knowledge with the representation capabilities of deep neural networks. In particular, the designed sensing framework incorporates prior estimates, optimized consensus weights, and Kalman-like recursive updates to perform decentralized inference, without relying on knowledge of noise statistics. Extensive experiments on linear, chaotic (Lorenz), and practical wireless tracking environments reveal that the proposed Covariance-Agnostic Neural Kalman Consensus Filter (CA-NKCF) outperforms traditional distributed Kalman and particle filters as well as purely model-free deep neural networks, exhibiting robustness even when the underlying motion and observation models are misspecified. It is also demonstrated that CA-NKCF's performance advantage remains stable across varying noise levels, random communication topologies, latent state dimensions, and observation clutter densities induced by scattering objects in wireless systems.

---


### 28. [S-GAI: Spectral Geometry-Aware Initialization for Sigmoidal MLPs -- From Dataset Geometry to Network Weights](https://arxiv.org/abs/2606.28444)

**<font color=#1a73e8>作者：</font>** Yi-Shan Chu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical universal approximation theorems establish the expressive power of sigmoidal multilayer perceptrons, but they do not prescribe how initial weights should encode the geometry of a data distribution. We propose S-GAI, a spectral geometry-aware initialization framework for one-hidden-layer sigmoidal MLPs. Starting from the constructive idea that sigmoid units can act as smooth half-space gates, we move from hand-specified planar geometry to class-wise spectral geometry estimated from image data. For each class, SVD provides a mean, principal directions, and spectral scales. An energy threshold selects the retained directions, and each retained direction is represented by two sigmoid gates. These class-specific gates form a shared hidden layer initialized directly from the training set. We also formulate a SVD-based subspace classifier as a non-neural geometric reference, which tests whether the estimated spectral class geometry is already discriminative before being embedded into the MLP. Experiments on MNIST, Fashion-MNIST, and a more challenging CIFAR-10 test show that the S-GAI-initialized MLP starts from a substantially more informative hidden state than Xavier initialization and reaches comparable final accuracy under full training. When the hidden layer is frozen, training only the output layer still gives stronger performance than frozen random gates, providing evidence that S-GAI effectively embeds class-wise spectral geometry into the MLP.

---


### 29. [Extracting Knowledge from an Arabic-English Machine-Readable Dictionary Using Information Extraction](https://arxiv.org/abs/2606.28457)

**<font color=#1a73e8>作者：</font>** Diaa M. Fayed, Aly A. Fahmy, Mohsen A. Rashwan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural language processing (NLP) applications need large and rich amount of linguistic knowledge. Furthermore, electronic language sources such as dictionaries, encyclopedia, and corpora became available. So, automatic methods are emerged to extract lexical information from those sources to overcome the knowledge acquisition bottleneck. We presented a method to automatically extract lexical information from a machine-readable version of the Arabic-English Al-Mawrid dictionary. We used n-gram analysis and key-word-in-context (KWIC) analysis to discover lexical patterns that manifest morphologic, syntactic, or semantic information. Then, we used hand-crafted rule-based information extraction to extract that information. Furthermore, we used punctuation marks and some heuristics to extract a set of synonyms in a subentry. This study registered high precision for all types of information, high recall for synonyms, and low recall for the other information. The study also showed that the Al-Mawrid has significant amount of derivations (morphologic information) and synonyms, domain labels, and hyponym/hypernym relations (semantic information).

---


### 30. [scKDGM: KAN-guided Dynamic Graph Masked Learning for Single-Cell RNA-seq Clustering](https://arxiv.org/abs/2606.28459)

**<font color=#1a73e8>作者：</font>** Jun Tang, Pengwei Hu, Sicong Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-cell RNA sequencing (scRNA-seq) clustering is essential for identifying cell types, but high dimensionality, sparsity, dropout, and technical noise hinder robust expression representation and cell graph construction. Existing masked autoencoders mainly use expression recovery for feature reconstruction, while graph clustering methods usually depend on fixed KNN graphs and do not feed recovered expression back into graph optimization. We propose scKDGM, a KAN-guided dynamic graph masked learning framework for scRNA-seq clustering. scKDGM uses graph-aware distribution preserving gene masking (GDP-Mask) to perturb cell identity, a KAN-based TAKGCN encoder to learn masked-view representations, mask-guided expression recovery to construct a dynamic graph, and cross-view contrastive learning to transfer recovery signals into topology updates. A ZINB loss models overdispersion and zero inflation. Experiments on 12 real scRNA-seq datasets show that scKDGM outperforms 10 baselines in average NMI and ARI.

---


### 31. [Counterfactual Residual Data Augmentation for Regression](https://arxiv.org/abs/2606.28460)

**<font color=#1a73e8>作者：</font>** Hossein Mohebbi, Oliver Schulte, Ke Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven modeling in real-world regression tasks often suffers from limited training samples, high collection costs, and noisy observations. Inspired by the impact of data augmentation in vision and language, we propose a novel Counterfactual Residual Data Augmentation (CRDA) technique for tabular regression. Our key insight is that once a regressor has modeled the systematic component of the data, the remaining noise can be viewed as an invariant residual that remains stable under small perturbations of carefully selected features. We exploit this residual invariance to generate new, yet realistic, training samples, effectively expanding the dataset without requiring additional real data. Our method is model-agnostic and readily applicable to various types of regressors. In experiments across datasets from a variety of benchmark repositories, on average, CRDA reduces an MLP Regressor's MSE by 22.9% and an XGBoost Regressor's MSE by 6.4%. When compared to existing state-of-the-art data generators and augmentation techniques, CRDA consistently outperforms in MSE reduction. By adding principled counterfactual variations to the training data, our method offers a simple and efficient remedy for noise-prone, small-sample regression settings.

---


### 32. [Singular Learning and Occam's Razor in Deep Monomial Networks](https://arxiv.org/abs/2606.28464)

**<font color=#1a73e8>作者：</font>** Kathlén Kohn, Giovanni Luca Marchetti, Farhan Shabir 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the optimization of neural networks, gradient dynamics are influenced by critical points that arise from the model's architecture. These critical points occur where the Jacobian of the model's parametrization is rank-deficient, and are the most pronounced singularities studied in Singular Learning Theory. We investigate such points in deep fully-connected networks with monomial activations via tools from polynomial algebra such as Mason's Theorem. We show that, for sufficiently large activation degree, criticality occurs precisely at subnetworks, i.e., at parameter configurations where some neurons are inactive or redundant. This offers a mathematical perspective on the implicit bias in deep neural networks, explaining the tendency of these models to converge toward simpler functions.

---


### 33. [Modelling Emotional Memory in Children with Tensor Networks](https://arxiv.org/abs/2606.28470)

**<font color=#1a73e8>作者：</font>** Henry Groves, Lucia F. Jackson, Barbara-Anne Robertson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We demonstrate how emotional valence influences the order-dependent structure of children's recognition memory: correct recall of a sequence of emotionally-valenced toys depended not just on the valence of a given toy itself, but also on the valence of the toys shown before and after it. Whilst standard psychological models confirm that order-dependence differs across an event (a set of toys shown in sequence), accuracy is low and the model does not reflect how memory for an emotional object influences others in the set. A classical tensor network model factoring in valence is able to achieve a 77.98\% accuracy in modelling the results of the study. While not strictly a ``quantum cognition'' model, this massive increase in accuracy shows the value of quantum-inspired methods for modelling order-dependent phenomena, such as emotional memory. Further, the task protocol we introduce presents a novel, real-world tool for exploring emotional temporal memory in children for analysis using classical and quantum-like models of cognition.

---


### 34. [Data and Evaluation Closed-Loop for Model Capability Enhancement](https://arxiv.org/abs/2606.28471)

**<font color=#1a73e8>作者：</font>** Zhixuan Li, Jiangan Yuan, Han Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model capability is the central variable in LLM pre-training, yet is never observed directly: data shapes it prospectively, while evaluation reveals it only retrospectively, compressing samples, prompts, decoding, and scoring rules into one noisy score. Practical optimization runs this backward: a failure is observed first, and the engineer must infer the corpus fix. The two sides speak incompatible vocabularies -- benchmark names and per-sample correctness versus data sources, domains, and quality labels -- so this inference is usually intuition, not method. We close this gap with the \emph{capability slice}: a group of evaluation samples sharing background condition, task type, solving operation, and output constraint -- precise enough to localize a single weakness yet stable enough to survive aggregation, unlike a benchmark name, too coarse, or a single sample, too noisy. Built around this unit, an evaluation taxonomy, a non-instruction data taxonomy, and mapping rules form a closed loop turning a benchmark-level failure into a targeted, testable data intervention. We test this loop on two case studies pulling in opposite directions. First, the loop rules the data out: continued pre-training drives BBH down by $-46.82\%$, but diagnosis traces this to a single masked \texttt{\textless EOS\textgreater} loss rather than weakened reasoning; restoring it recovers BBH to $66.44$, above the original checkpoint, without changing the data. Second, the loop rules the data in: a persistent math-reasoning weakness is decomposed by solving operation into specific failing combinations, and a weakness-targeted sampling procedure built from it lifts AIME2025/AIME2026 Pass@128 from $6.67$/$0.00$ to $26.67$ each. The same unmodified loop reaches opposite, correct verdicts in both cases, showing the evaluation-to-data inference can be routine, auditable, and experimentally validated rather than intuitive.

---


### 35. [Generative AI Literacy Training Improves Intelligence Analysts' Discrimination of Real and AI-Generated Images](https://arxiv.org/abs/2606.28510)

**<font color=#1a73e8>作者：</font>** Negar Kamali, Candice Rockell Gerstner, Jessica Hullman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Across social and online platforms, people are increasingly exposed to AI-generated images. As a consequence, the task of distinguishing AI-generated from authentic images is becoming a central challenge for information ecosystems. While humans perform better than chance, accuracy falls short of many operational needs. Initial evidence shows that visually oriented training can improve deepfake detection but does not improve participants' ability to identify real images as real. Here, we investigate the efficacy of a brief training intervention for intelligence analysts employed by the United States government in 2024. We conducted a counterbalanced within-subject randomized experiment in which we showed participants real and AI-generated images varying in pose complexity and scene context and asked them whether each image was real or AI-generated, both before and after an expert delivered a 30-minute training that pointed out patterns in seven real and 50 AI-generated images. We collected 2,544 image-level judgments from 32 intelligence analysts. We find training increased overall accuracy by 9 percentage points (95% CI: [2.7, 15.4]) from a baseline of 72%. We find the improvement is driven by a 14.2 percentage point increase in accuracy for real images (95% CI: [0.7, 27.7]). Through a careful experimental setup that curated matched pairs of real and AI-generated images across pose complexity categories, we reveal how these trainings influence people with different levels of digital forensics and generative AI experience and identify the kind of image-based content where this training intervention appears to be most effective. Ultimately, these results provide causal evidence that a brief, structured training can improve human judgment across a diverse array of real and AI-generated images, informing organizational responses to AI-generated visual misinformation.

---


### 36. [A Trainable-by-Parts Operator Learning Framework: Bridging DeepONet and Karhunen-Loeve Expansions for Large-Scale Applications](https://arxiv.org/abs/2606.28519)

**<font color=#1a73e8>作者：</font>** Christian Munoz, Alexandre Tartakovsky  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training operator-learning models for large-scale problems governed by partial differential equations (PDEs) is challenging due to the curse of dimensionality, memory constraints, and limited training data. These challenges arise in many scientific and engineering applications, including subsurface flow, climate modeling, and geological carbon storage (GCS). In this work, we propose a scalable operator-learning framework based on the Karhunen-Loeve Deep Neural Network (KL-DNN) and demonstrate its performance for modeling GCS. The model is trained on a dataset comprising 100 samples of large-scale simulations in a three-dimensional domain with 1.7 million cells and 50 time steps. The KL-DNN method constructs latent spaces using low-rank singular value decomposition of static properties and a nested Karhunen-Loeve expansion for dynamic pressure fields, enabling full-resolution predictions without subsampling or spatial coarsening. The KL-DNN model achieves an average root mean square error (RMSE) of 1.1 psi for pressure (0.04% relative error with respect to the average pressure in the domain) and RMSE of 0.0146 for CO2 saturation (5% relative error with respect to the average saturation inside the plume). The model requires 20 minutes of training on a single GPU, representing a 19% reduction in the pressure errors, 7% reduction in the saturation error, and a two-order-of-magnitude speedup compared to DeepONet trained on the same dataset. These results, along with inference time of less than one minute, establish the proposed model as a practical and accurate solution for large-scale PDE problems, enabling rapid uncertainty quantification, history matching, and real-time decision support.

---


### 37. [A French OSCE Dialogue Dataset and Controllable Virtual Patient System for Clinical Training](https://arxiv.org/abs/2606.28526)

**<font color=#1a73e8>作者：</font>** Doria Bonzi, Tom Bourgeade, Fabrice Lefèvre 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The clinical and communication skills of medical students are commonly assessed through Objective Structured Clinical Examinations (OSCEs), which consist of brief scenario-driven simulations of doctor-patient interactions. However, training is often limited by the low availability of human standardized patients, motivating the development of realistic virtual patients (VPs). To address this gap, we introduce a French OSCE dialogue dataset comprising 240 student-patient training interactions. We build upon it a controllable LLM-based pipeline to generate synthetic OSCE dialogues. The pipeline integrates modular components, such as retrieval-based grounding and a reflection loop, to ensure patient fidelity, coherence, and realism. Additionally, we propose a multi-level evaluation framework assessing patient simulation quality, student performance, and linguistic quality, using an LLM-as-a-Judge approach. Experiments suggest that controllability modules generally improve patient fidelity and student evaluation consistency. Finally, we implement an interactive prototype in which students can practice with a VP and receive automatic feedback.

---


### 38. [MammoFlow: Multiview Mammogram Synthesis with Anatomically Consistent Flow Matching](https://arxiv.org/abs/2606.28537)

**<font color=#1a73e8>作者：</font>** Yuexi Du, Leya Barrientos, Laura Sheiman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multiview mammography relies on paired craniocaudal (CC) and mediolateral oblique (MLO) views to provide complementary projections of a 3D breast volume, enabling precise anomaly localization. However, acquiring high-quality, balanced datasets remains challenging for deep learning applications. We propose a novel method to synthesize multiview mammograms by leveraging the inherent geometric relationship between CC and MLO views. To enforce an implicit 3D consistency prior during generation, we develop an alignment module that searches a 2D affine transformation subspace to establish optimal anatomical correspondence. Leveraging this alignment, we introduce a pixel-space self-consistency loss based on the Earth Mover's Distance (EMD) between the 1D anteroposterior (AP) axis tissue distributions of the generated images. Integrated into a pretrained flow matching model, MammoFlow forces synthesized pairs to share physically plausible tissue distributions from the chest wall to the nipple. To our knowledge, this is the first work to guide multiview mammogram generation using implicit geometric tissue correspondence. Our method demonstrates superior image quality, passes expert radiologist evaluation, and generates physically consistent pairs that improve downstream classification AUC by 5%. Code is available at this https URL

---


### 39. [Legal Domain Adaptation of Modern BERT Models](https://arxiv.org/abs/2606.28538)

**<font color=#1a73e8>作者：</font>** Dominik Stammbach, Peter Henderson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate domain adaptation of modern BERT models in the legal domain. We further pre-train ModernBERT on all US court opinions using the masked language modeling objective. Although ModernBERT has been trained on roughly 500x more data than original BERT, we still find that this model benefits from further pre-training and domain adaptation in the legal domain: we report significant improvements compared to vanilla ModernBERT on all datasets connected to US court opinions. We find gains similar to those reported in early work on domain adaptation of BERT-like models. However, from scratch pre-training does not match the performance of further pre-training an existing ModernBERT checkpoint in our experiments. The resulting models are capable of processing sequences up to 8,192 tokens, and can be used to compute meaningful embeddings of legal passages, or could quickly rerank hundreds of legal passages for a given search query. We release all model checkpoints publicly.

---


### 40. [Improving Coherence in Hierarchical Time Series Forecasting using Structured Temporal Fusion](https://arxiv.org/abs/2606.28553)

**<font color=#1a73e8>作者：</font>** Ruchi Pakhle  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many real-world applications, such as retail sales, energy usage, and supply chain planning, forecasting is performed across hierarchical structures. These structures often represent aggregations (e.g., products to categories to regions), where forecasts must not only be accurate but also coherent, meaning that lower-level predictions sum correctly to higher-level forecasts. Traditional statistical methods, such as Bottom-Up and MinT, enforce coherence through post-processing but fail to model complex nonlinear temporal dependencies and covariate interactions.
We propose Hierarchical Temporal Fusion (HTF), a novel extension of the Temporal Fusion Transformer (TFT) that integrates structured hierarchical embeddings with a coherence-aware loss function to ensure consistent forecasts across all levels of a hierarchy. Rather than applying reconciliation after forecasting, HTF embeds coherence directly into the training objective. The coherence loss penalizes the difference between aggregated child forecasts and their corresponding parent forecasts during training, enabling the model to learn both temporal dynamics and structural consistency simultaneously.
We evaluate HTF on two publicly available benchmark datasets: the M5 Walmart forecasting dataset and a publicly available hierarchical energy consumption dataset. Results demonstrate that HTF substantially reduces forecast incoherence while improving forecasting accuracy compared with classical reconciliation methods and deep learning baselines. In addition, attention visualization and embedding analysis provide insight into how temporal and structural information contribute to hierarchical forecasting performance.

---


### 41. [Depth-Staggered Fibonacci Spacing for Sparse Attention: Static Schedules Beat Learned Dilation and Extrapolate Where Dense Attention Fails](https://arxiv.org/abs/2606.28560)

**<font color=#1a73e8>作者：</font>** Chad A. Capps  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study sparse self-attention in which each query attends to a dense local window plus a set of Fibonacci-spaced offsets, with a per-layer scalar alpha that compresses or expands the spacing. Across 21 language models trained under one matched recipe (60M parameters, 512 hidden, 16 layers, 426M tokens), we compare four ways of setting alpha across depth: fixed, per-layer learned, a static linear stagger, and a coprime (anti-gridding) reassignment of that stagger, together with a reach-matched power-of-2 control. Three results stand out. First, a static per-layer stagger improves perplexity over both fixed and learned alpha, and the gain is base-agnostic: applying the same stagger to a power-of-2 base lifts it above fixed Fibonacci and to parity with learned Fibonacci attention. Second, learning per layer is inert: it does not beat the static schedule and costs roughly five times the inference latency. Third, and most consequential, all sparse variants extrapolate to four times their training length with little or no degradation, whereas a recipe-matched dense baseline collapses (perplexity rises by 201% at 4x length); we attribute this to fixed-offset attention only ever querying relative positions seen during training. We also report two honest negatives: at training length the best sparse model has about 26% higher perplexity than the dense baseline, and the staggering gain is uniform across context positions rather than concentrated at long range.

---


### 42. [SEAD: Competence-Aware On-Policy Distillation via Entropy-Guided Supervision](https://arxiv.org/abs/2606.28562)

**<font color=#1a73e8>作者：</font>** Chia-Hsuan Lee, Zelei Cheng, Yu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has a property absent in offline distillation and RL: teacher supervision quality depends on student competence. Incoherent rollouts yield noisy gradients; already-mastered tokens yield redundant ones. This creates waste at three scales (tokens, training phases, and prompts) yet existing methods supervise uniformly. We introduce SEAD, which uses entropy as a unified probe of this competence-dependent degradation at three scales: (1) joint teacher-student entropy partitions tokens into zones receiving tailored divergences or zero gradient (approx. 50% skipped); (2) a cosine schedule anneals from forward to reverse KL as competence grows; (3) a competence-gated curriculum introduces prompts easy-to-hard. These components are symbiotically necessary: token selection requires coherent rollouts (curriculum), annealing requires monotonic improvement (also curriculum). On OLMo-3 (7B to 32B), SEAD achieves +4.8 avg accuracy over vanilla OPD across six math benchmarks, with ablations confirming super-additive interactions.

---


### 43. [KM-Speaker: Keypoint-Based Style Control for High-Quality Speech-Driven 3D Facial Animation and Dialogue Localization](https://arxiv.org/abs/2606.28568)

**<font color=#1a73e8>作者：</font>** Arthur Josi, Emeline Got, Abdallah Dib 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Speech-driven 3D facial animation methods face significant challenges in simultaneously achieving high-fidelity motion and precise artistic control at production quality. Existing controllable models typically learn global style control by relying on large-scale, low-quality \emph{in-the-wild} datasets that compromise overall animation realism. Furthermore, these frameworks often lack the fine-grained temporal precision required for demanding tasks such as dialogue localization (e.g., dubbing), where matching specific facial expressions is as critical as lip synchronization. We present KM-Speaker (Keypoint-Matching Speaker), a novel keypoint-conditioned flow-based generative framework that provides both global style guidance and frame-level temporal control from reference performances. We propose a disentanglement strategy that separates audio-driven lip motion from keypoint-driven upper-face dynamics, together with a global style context preservation mechanism to ensure coherent full-face expressiveness. KM-Speaker advances example-based 3D facial animation by achieving high-fidelity motion and flexible controllability in a data-constrained setting, consistently outperforming state-of-the-art methods in lip-sync accuracy, style adherence, and expressive temporal control.

---


### 44. [Geometric Measurements of the Axiom of Choice in Neural Proof Embeddings](https://arxiv.org/abs/2606.28572)

**<font color=#1a73e8>作者：</font>** Rodrigo Mendoza-Smith  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The axiom of choice has divided the foundations of mathematics for over a century, but the distinction between classical and constructive proofs has remained a philosophical and methodological one. We use Lean 4's kernel-level tracking of axiom dependence to show that the axiom of choice has a measurable geometric correlate in proof space that obeys a one-parameter mixture law and has operational consequences for neural theorem provers. To do this, we partition $471{,}260$ declarations of Mathlib by transitive dependence on the axiom of choice and represent a filtered population of $42{,}355$ traced theorems by their sequences of tactic invocations. We use the constructive proofs in this dataset to train a self-supervised proof encoder and show that when using it to measure classical proofs, three complementary measurements (anomaly score, reconstruction loss, and density-superlevel containment) exhibit a common decline with the proof's distance from the axiom in the dependency graph, from sharp separation at the shallow boundary (AUC $0.847$ at distance $2$) to indistinguishability at distance~$9{+}$. Robustness controls show that the signature survives length, file, author, and topic controls, and replicates under full-source encoders trained on normalised proof source. Operationally, we show that on an evaluation sample of $251$ Mathlib theorems, Lean's \texttt{aesop} tactic solves constructive theorems at $13\times$ the rate of classical ones, and a neural-guided hybrid using the ReProver tactic generator compresses the gap to $5\times$. The geometric anomaly score predicts \texttt{aesop} failure beyond proof length, providing an operational link between the geometric signature and prover performance.

---


### 45. [Replica Symmetry Breaking and Algorithmic Thresholds in Empirical Risk Minimization under Multi-Index Model](https://arxiv.org/abs/2606.28573)

**<font color=#1a73e8>作者：</font>** Andrea Montanari, Kangjie Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern machine learning models are trained by optimizing high-dimensional non-convex empirical risk functions. Such cost functions can have a multitude of local optima and yet, gradient-based optimization appears to converge to near-global optima.
Within a simple supervised learning setting, we develop a precise picture of which parts of the empirical risk landscape are accessible by polynomial-time algorithms. We are given i.i.d. pairs $\{(\boldsymbol{x}_i,y_i):\; 1 \le i\le n\}$ with $\boldsymbol{x}_i\in \mathbb{R}^d$ standard Gaussian feature vectors, and $y_i\in\mathbb{R}$ response variables that depend on $\boldsymbol{x}_i$ through their projections on an unknown $k$-dimensional subspace. We use empirical risk minimization to learn a model that depends on an $m$-dimensional projection of the data (e.g., an $m$-neurons neural network).
We propose an incremental approximate message passing (IAMP) algorithm and precisely characterize the training error it achieves, as well as the relation between test and training error, in the high dimensional asymptotics $n,d\to\infty$, with $n/d\to\alpha \in (0, +\infty)$. Based on earlier work in related models, we expect that the performance achieved by our algorithm is optimal among polynomial-time algorithms.

---


### 46. [SatSplat: Geometrically-Accurate Gaussian Splatting for Satellite Imagery](https://arxiv.org/abs/2606.28581)

**<font color=#1a73e8>作者：</font>** Shuang Song, Jiyong Kim, Rongjun Qin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution satellite imagery demands 3D reconstruction methods that deliver both speed and geometric accuracy. Recent adaptations of 3D Gaussian Splatting (3DGS) to satellite imagery demonstrate strong efficiency, but reconstruction quality often degrades under diverse illumination across multi-date, high-altitude acquisitions (with small intersection angles), limiting applicability to remote sensing and vision tasks. We present SatSplat, the first framework to adapt 2D Gaussian Splatting (2DGS) to satellite photogrammetry, with online camera adjustment. We approximate satellite cameras with an affine model and learn a minimal delta parameterization for in-splat camera refinement from dense observations. The formulation is implemented with a 2DGS scene representation. To handle time-varying shadows and illumination changes, we integrate geometric shadow mapping and per-camera color correction during training. Across the evaluated DFC2019 and IARPA2016 benchmark sites, SatSplat achieves strong geometric accuracy while significantly outperforming prior 3DGS-based baselines. On our processed DFC2019 benchmark, SatSplat reduces mean absolute error by 11.93% and peak video memory by 31% relative to the previous state of the art. Our approach enables large-scale digital surface modeling with practical computational efficiency. The project page is available at this https URL.

---


### 47. [Animation2Code: Evaluating Temporal Visual Reasoning in Video-to-Code Generation](https://arxiv.org/abs/2606.28593)

**<font color=#1a73e8>作者：</font>** Anya Ji, Abhijith Varma Mudunuri, David M. Chan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While recent vision-language models (VLMs) have achieved significant improvements on static visual-to-code tasks such as generating code for webpages, charts, or SVGs, it remains unclear whether they can recover temporal dynamics when motion is present. To this end, we introduce Animation2Code, a benchmark for evaluating temporal visual reasoning via reconstructing executable web animation code from videos. Animation2Code consists of 1,069 web animation videos with diverse visual appearances and motion patterns, paired with corresponding HTML/CSS/JavaScript implementations. We propose two human-aligned metrics, appearance similarity and temporal similarity, which allow us to disentangle visual fidelity from temporal alignment when comparing rendered animations against ground-truth samples. Benchmarking state-of-the-art VLMs on this dataset shows that current VLMs struggle to maintain temporal consistency in reconstruction, even when achieving high appearance similarity, including under finetuning and iterative refinement settings. Code and data are available at this https URL .

---


### 48. [IMU-HOI: A Symbiotic Framework for Coherent Human-Object Interaction and Motion Capture via Contact-Conscious Inertial Fusion](https://arxiv.org/abs/2606.28604)

**<font color=#1a73e8>作者：</font>** Lizhou Lin, Songpengcheng Xia, Zengyuan Lai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Capturing full-body human motion with object interactions is crucial for AR/VR and robotics applications, yet it remains challenging for conventional vision-based methods due to occlusions and constrained capture volumes. Inertial measurement units (IMUs) offer a compelling alternative without line-of-sight requirements, but existing IMU-based motion capture assumes an isolated human and ignores object contacts and dynamics. To bridge this gap, we present IMU-HOI, a novel framework that jointly recovers full-body human pose and 6-DoF object trajectory from sparse IMUs on the body and object, explicitly modeling human-object interaction. Our approach first infers probabilistic hand-object contacts directly from IMU streams and uses them as a high-level signal to route between kinematic and inertial reasoning. These contact cues drive a three-stage fusion pipeline that refines human pose and root translation, and fuses hand-based forward kinematics with object-IMU integration for object motion, yielding coherent, drift-resilient trajectories for both human and object. Experiments on challenging human-object interaction scenarios demonstrate substantial accuracy gains over prior inertial motion capture methods. Moreover, IMU-HOI can be plugged into existing sparse-IMU mocap backbones with minimal changes, effectively extending the scope of purely inertial motion capture from isolated humans to full human-object interaction and joint motion estimation.

---


### 49. [Randomized Exploration for Linear Bandits via Absolute Perturbations](https://arxiv.org/abs/2606.28616)

**<font color=#1a73e8>作者：</font>** Toshinori Kitamura, Shuai Liu, Csaba Szepesvári  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In stochastic linear bandits, the canonical Upper Confidence Bound (UCB) algorithm admits a simple frequentist regret analysis but can be computationally demanding, while Thompson Sampling (TS) is computationally attractive yet typically harder to analyze due to its non-optimistic nature. We propose Absolute Thompson Sampling (ATS), a simple modification of TS that ensures optimism in expectation by replacing the signed exploration noise with its absolute value. This preserves the computational efficiency of TS while avoiding the technically involved anti-concentration arguments common in TS analyses, enabling a simple UCB-style regret analysis. We show that ATS achieves $\tilde{O}(d^{3/2}\sqrt{K})$ regret, matching existing bounds for TS in linear bandits. We further introduce Ensemble Absolute Thompson Sampling (EATS), which takes the maximum over multiple absolute perturbations with normalization by the ensemble size. As the ensemble size grows, EATS converges to the UCB objective, recovering UCB behavior in the limit. Experiments show that moderate ensemble sizes already yield strong performance. Our results point to a bridge between randomized exploration and deterministic optimism both in theory and practice.

---


### 50. [A Fast Convergent Algorithm for Solving Non-convex Partially-Decoupled Generalized Nash Equilibrium Problems](https://arxiv.org/abs/2606.28617)

**<font color=#1a73e8>作者：</font>** Bennet Outland, Vishala Arya  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Solving multi-agent optimal control problems in aerospace such as pursuit-evasion and contested space operations can be modeled as non-convex differential games for which, there are limited algorithms. In this work, a relaxation of generalized Nash Equilibrium problems (GNEPs) to exclude inter-agent control coupling in dynamics, which is representative of many multi-agent systems is introduced. The main contribution is an algorithm for solving a broad class of differential games named FALCON: Fast Augmented Lagrangian Convexification for Open-loop Nash equilibria is presented. Methodologically, sequential convex programming (SCP) is utilized to create tractable convex sub-games which can then be solved via standard convex programming methods involving a potential game reformulation. FALCON is demonstrated to have global convergence guarantees to an open-loop Nash equilibrium for non-convex differential games under mild assumptions. This is numerically shown through both cooperative and competitive differential games.

---


> [!TIP]
> 当前位于：**1-50**（第 1/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-489](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
