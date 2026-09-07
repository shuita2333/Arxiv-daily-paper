# 📦 其他研究 | 2026年09月08日

> 本类共 **190** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-190](./part-04.md)

---

### 101. [SimFuse3D: Source-Guided Target Simulation and Confidence-Guided Multi-Stage Localization Reweighting for Cross-Platform 3D Object Detection](https://arxiv.org/abs/2609.04886)

**<font color=#1a73e8>作者：</font>** Yongchun Lin, Xinliang Zhang, Yun Zou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Changes in sensor height and viewpoint alter object-level point distributions, making cross-platform LiDAR unsupervised domain adaptation (UDA) difficult. Self-training uses labeled source scans and unlabeled target scans, yet a retained prediction may provide a useful target location while enclosing sparse foreground returns, background clutter, or points inconsistent with the predicted box. We refer to this mismatch as box-point inconsistency. We introduce SimFuse3D, which preserves the target placement and repairs the associated pseudo-object using measured geometry from labeled source scans. Object Memory retrieves a compatible labeled source instance. Target Simulation places its ground-truth box at the target location, aligns its points with the target viewing geometry, and filters the aligned crop to approximate the target observation. Confidence-Guided Multi-Stage Localization Reweighting (CMLR) maps each target pseudo-object confidence score to a bounded weight shared by RPN localization and R-CNN box regression. All components operate only during adaptation, leaving the detector architecture and inference graph unchanged. Across six cross-platform transfers, SimFuse3D exceeds Pi3DET-Net on every reported AP metric and ranks first among the compared adaptation methods on nearly all metrics. On nuScenes-to-KITTI, it ranks first among the compared adaptation methods with both evaluated detectors.

---


### 102. [The Security Feature Location Problem](https://arxiv.org/abs/2609.04899)

**<font color=#1a73e8>作者：</font>** Kevin Hermann, Sven Peldszus, Thorsten Berger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Software security must be realized through security features such as authentication and encryption, but which features does a system implement, and where? We present security feature location: the task of relating code locations to security features, enabling developers to understand security implementations and assess whether intended security properties are enforced.

---


### 103. [Sound-based Multi-Person 3D Pose Estimation](https://arxiv.org/abs/2609.04902)

**<font color=#1a73e8>作者：</font>** Yusuke Oumi, Yuto Shibata, Go Irie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can we recover the 3D poses of multiple people using only sound? This paper presents the first attempt to estimate multi-person 3D poses solely from acoustic signals. Estimating the poses of multiple individuals using acoustic signals is inherently challenging due to the superposition of motion-dependent signal variations. Unlike single-person scenarios, the presence of multiple subjects leads to overlapping acoustic signatures, making it difficult to attribute specific signal changes to an individual's pose. Furthermore, the complexity is compounded by inter-person reflections, which introduce intricate propagation delays that obscure the temporal motion-acoustic relationship. To address these issues, we propose SoundMHPE (Sound-based Multi-person Human Pose Estimator), a novel encoder-decoder framework consisting of two key components. First, the Acoustic Multi-scale Encoder captures diverse temporal and fine-grained frequency features to isolate subtle acoustic signatures from complex, overlapping signals. Second, the Temporal Pose Decoder employs an attention mechanism to disentangle multi-person information across successive frames. By jointly accounting for temporal dynamics and inter-person dependencies, this component precisely reconstructs frame-wise individual poses. To validate our approach, we constructed the 6-hour Acoustic Multi-person Pose (AMP) dataset consisting of 432K synchronized frames of multi-person pose and acoustic data, and demonstrated that our SoundMHPE outperforms baseline models. Project page: this https URL

---


### 104. [InterSing: Explicit Interaction Dynamics for 3D Duet Singing Animation and Beyond](https://arxiv.org/abs/2609.04903)

**<font color=#1a73e8>作者：</font>** Yihan Zhou, Zikai Huang, Yuyang Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present InterSing, a framework for generating realistic 3D head animations for duet singing performances. Unlike solo singing, duet performance requires each singer to balance individual expressiveness with intermittent interaction at musically salient moments, such as phrase boundaries, synchronized rhythms, and call-and-response passages. Because these interactions are sparse and rhythm-dependent, existing audio-driven animation methods and conversational interaction models do not adequately capture their structure. Our key insight is that duet coordination can be represented as a time-varying signal that reflects how strongly performers engage with one another throughout a song. Based on this observation, we introduce interaction logits, an interpretable latent representation that models the degree of cross-performer engagement at each time step. We learn these logits using weak supervision and use them to condition an interaction-aware diffusion model jointly driven by audio features and interaction dynamics. This formulation enables unified multi-mode generation, spanning independent motion, coordinated behavior, and smooth transitions between them. Experiments show that InterSing generates realistic and expressive singing head animations with stronger coordination and musical alignment than existing methods, while preserving each performer's characteristic motion style. We further demonstrate that the same formulation generalizes to multi-singer performances and provides intuitive control over when and how performers engage.

---


### 105. [Methane Detection On Board Satellites from Unorthorectified Imagery](https://arxiv.org/abs/2609.04906)

**<font color=#1a73e8>作者：</font>** Luca Marini, Maggie Chen, Hala Lamdouar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As a potent greenhouse gas, methane is a major driver of climate change. Its effective mitigation relies on timely detection. Conventional detection methods rely on orthorectification to correct geometric distortions and matched filters to enhance plume signals, which are steps designed for ground processing and poorly suited to onboard execution. We introduce UnorthoDOS, a dataset and approach for training machine learning models directly on unorthorectified hyperspectral imagery, bypassing both orthorectification and matched-filter products. Our U-Net models trained on unorthorectified data approach the performance of models trained on orthorectified data (IoU 16.91% vs. 18.47% on all plumes), while both substantially outperform the mag1c matched-filter baseline (IoU 4.76%). We further demonstrate the feasibility of onboard deployment: FP16 compression halves model size with under 0.3% output deviation. The trained ML models and two ML-ready datasets -- orthorectified and unorthorectified hyperspectral imagery from the EMIT sensor -- are publicly available at this https URL, with code at this https URL.

---


### 106. [Fast Gauss Sums via Flash Attention](https://arxiv.org/abs/2609.04910)

**<font color=#1a73e8>作者：</font>** Nicolaj Rux, Sebastian Neumayer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gaussian kernel sums are the computational core of maximum mean discrepancies (MMDs), kernel gradient flows, Stein variational gradient descent (SVGD), and many other kernel methods. At the same time, softmax attention has received an extraordinary amount of hardware-aware code engineering, culminating in flash attention. We show that Gauss kernel sums with arbitrary, signed weights can be evaluated via flash attention: two small input augmentations turn the normalized softmax reduction into the unnormalized Gauss sum, without writing a single line of custom GPU code. For feature dimension D>8 in fp16, this approach beats compiled PyTorch code as well as PyKeOps kernels (often significantly) in speed, memory-overhead and accuracy. Indeed, its memory scaling remains linear.

---


### 107. [TourPhysics: Bringing Physics to World Models for Exploration and Manipulation from a Single Image](https://arxiv.org/abs/2609.04911)

**<font color=#1a73e8>作者：</font>** Xin Zhang, Yabo Chen, Zixuan Duan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive visual world models must distinguish observation from physical intervention. Camera motion reveals new surfaces, whereas intervention changes object motion, contact, and deformation. Current video world models are largely driven by appearance priors and often lose physical or spatial consistency over long horizons. We present TourPhysics, an online framework initialized from a single image and a declarative physical configuration. TourPhysics extends PhysOmni, our ACM Multimedia 2026 work, from finite physics-grounded video synthesis to persistent exploration and manipulation. TourPhysics combines deterministic simulation with video generation while assigning separate roles to simulator state, geometric evidence, generator controls, and appearance memory. For each action, the simulator computes a finite physical and camera trajectory before the corresponding observation is generated. Accepted observations publish the terminal state and update the appearance memory and subsequent generator controls, while the committed state and simulator geometry remain fixed throughout synthesis and retry. We further separate the simulator geometry used for projection and visibility from the relative depth used to condition the generator. A reference-anchored memory retrieves accepted static appearance through geometric cross-view correspondence and incorporates it through a bounded residual that reverts to the native path when no valid correspondence exists. On simulator-defined camera tours and object manipulations, TourPhysics follows prescribed camera and object trajectories more closely than the evaluated baselines, preserves the input scene, and reduces appearance drift during long-horizon revisits.

---


### 108. [One Diffusion Model, Two Roles: Guided Trajectory Planning and Safety-Critical Scenario Generation in Closed-Loop Simulation](https://arxiv.org/abs/2609.04921)

**<font color=#1a73e8>作者：</font>** Arka Pal, Rajesh Kumar, Hannes Eriksson 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion probabilistic models can capture the multi-modal, interaction-rich distribution of joint future trajectories in driving scenes. We show that a single pretrained diffusion traffic model can serve two complementary roles in the autonomous driving development loop: as an ego motion planner, and as a controllable generator of safety-critical scenarios for stress-testing the planners. On the planning side, we introduce a Single-Stream Dual-Stream (SSDS) diffusion-transformer decoder that fuses scene context via joint attention rather than late cross-attention, improving closed-loop performance on nuPlan. We further propose Decoupled Annealing Posterior Sampling with Energy (DAPSE), a training-free guidance scheme that injects arbitrary energy functions at the clean-sample level, avoiding the first-order approximation errors while requiring no auxiliary networks. Beyond planning, we leverage the same diffusion model as a controllable scenario generator to create realistic long-tail driving interactions for closed-loop evaluation. Through inference-time guidance, selected agents are steered toward safety-critical behaviors, including aggressive cut-ins, lead-vehicle braking, and combined longitudinal-lateral interactions, while preserving realistic traffic behaviors. Evaluated in closed-loop nuPlan simulations with independent black-box planners, the generated scenarios expose failure modes that remain hidden under standard benchmarks. Although the SSDS-based planner achieves stronger nominal performance, it experiences larger degradation under these challenging scenarios, demonstrating that benchmark superiority does not necessarily translate to robustness. These results demonstrate that a single learned traffic prior can simultaneously improve motion planning and provide a realistic framework for systematic planner robustness evaluation.

---


### 109. [Solving Hard XAI Queries Based on a Compiled Dual-Rail Encoding](https://arxiv.org/abs/2609.04931)

**<font color=#1a73e8>作者：</font>** Arthur Ledaguenel, Florent Capelli, Jean-Marie Lagniez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The widespread adoption of artificial intelligence (AI) within real-world applications has raised a lot of concerns regarding their trustworthiness, especially in critical applications. The field of eXplainable AI (XAI) has emerged with the objective of providing explanations to the users about the decisions made by AI systems. Several explanations for boolean classifiers have been introduced in the literature, including abductive and contrastive explanations, each giving a different insight on the decision of the classifier. However, computing an explanation for a decision of a boolean classifier is a hard problem in general. One way to deal with this complexity is to rely on a compiled representation of the classifier for which each explanation can be computed efficiently. Unfortunately, we prove in this paper that several classes of abductive explanations, remain hard to compute even for Ordered Binary Decision Diagrams, one of the most tractable subsets of the knowledge compilation map. Included in such classes are shorter abductive explanations or abductive explanations that include the explainee's preferences. To recover the benefits of working with compiled representations, we show that a proper representation of the dual-rail encoding of the classifier can be used to compute efficiently these classes of explanations.

---


### 110. [LensStyle: Learning the Optical Aesthetics for Controllable Stylized Lens Effect Rendering](https://arxiv.org/abs/2609.04939)

**<font color=#1a73e8>作者：</font>** Yachuan Huang, Liwen Xiao, Liao Shen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The visual aesthetics of photographs are deeply influenced by lens characteristics such as aperture shape, optical vignetting and optical diffraction, which together define a camera's unique optical style. Existing lens effect rendering methods primarily focus on accurately simulating the blur transition from small to large apertures but overlook the stylistic aspects of lens effects. As a result, they fail to produce diverse bokeh effects under large apertures or capture distinctive photographic phenomena such as starbursts that emerge under small apertures. In this work, we introduce LensStyle, a unified framework for controllable stylized lens effect rendering that explicitly models lens aesthetics through joint continuous-discrete control. Our model incorporates a Dual-Path Controller that disentangles continuous optical parameter modulation (e.g., focus distance and blur strength) from discrete lens-style conditioning (e.g., circular, polygonal, donut, cat-eye, and starburst effects), enabling fine-grained, interpretable, and physically grounded lens manipulation within a single unified framework. To support model training, we curate a comprehensive MultiLens dataset containing multi-lens image pairs synthesized under real optical constraints. Extensive experiments demonstrate that LensStyle achieves superior realism, controllability, and aesthetic quality compared with existing lens effect rendering approaches and diffusion-based image editing models, advancing computational photography toward multiple-lens-style simulation.

---


### 111. [Physics-Aware Random Walk Fingerprints for Scalable Power Grid Graph Classification](https://arxiv.org/abs/2609.04943)

**<font color=#1a73e8>作者：</font>** Adnan Anwar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent benchmarks such as PowerGraph provide large collections of power-grid graphs for cascading-failure classification. Graph neural networks (GNNs) achieve strong predictive performance on this task, but typically require end-to-end training and model-specific tuning, while their latent representations can be difficult to relate to physically meaningful propagation patterns. Random Walk Fingerprints (RWF) offer a scalable and interpretable alternative, but existing variants primarily emphasise topology and node-level information, leaving grid-relevant operational edge states in the walk dynamics. We propose Multi-Channel Physics-Aware Random Walk Fingerprints (MC-PA-RWF) for power systems, a lightweight graph-level representation framework that introduces physical edge states into random-walk propagation. The method constructs multiple edge-weighted channels from domain-relevant attributes, extracts a channel-specific fingerprint from each weighted graph, and concatenates the resulting vectors into a compact representation. Experiments on three \textit{PowerGraph} benchmark systems show substantial improvements over topology-only RWF and competitive balanced accuracy against strong GNN baselines, including Graph Convolutional Networks (GCN), Graph Attention Networks (GAT), Graph Isomorphism Networks with edge features (GINE), and Transformer-based Graph Convolutional Networks (TransformerConv). At the largest evaluated settings, the node-edge extension MC-PA-RWF+ achieves around 98.04% - 99.32% balanced accuracy and improves failure-class F1 over the strongest GNN baseline by 1.60 -- 5.84 percentage points, with statistically significant gains across all three systems.

---


### 112. [VICAL: Vicinal Consistency Alignment for Long-Tailed Visual Recognition](https://arxiv.org/abs/2609.04948)

**<font color=#1a73e8>作者：</font>** Jiangang Zhu, Zheng Wang, Bin Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-expert models have become the dominant paradigm for long-tailed learning, largely attributed to their presumed ability to benefit from expert diversity. However, we revisit this central assumption and reveal that diversity induced by logit adjustment or explicit regularizers does not guarantee better ensemble accuracy. Our work suggests that multi-expert models benefit more from variance reduction than diversity maximization. We introduce \textbf{VICAL}, a \textbf{VI}cinal \textbf{C}onsistency \textbf{AL}ignment framework that improves long-tailed recognition not by enforcing expert diversity, but by reducing prediction variance. Specifically, our approach comprises two key components: Self-Consistency Learning and Deep Ensemble Distillation. Self-Consistency Learning discourages reliance on unstable high-frequency information, smoothing the local loss landscape and mitigating overfitting, especially for tail classes. Deep Ensemble Distillation promotes cross-expert low-frequency semantic agreement using a low-resolution view, thereby sidestepping optimization conflicts with established knowledge. Extensive experiments on CIFAR-LT, ImageNet-LT, and iNaturalist 2018 show that VICAL consistently outperforms state-of-the-art methods, validating the effectiveness of our consistency-driven design. Our code is available at \href{this https URL}{VICAL}.

---


### 113. [MINT: A Unified Model for World-Space Camera and Hand Motion Estimation from Scalable Egocentric Pipeline Supervision](https://arxiv.org/abs/2609.04958)

**<font color=#1a73e8>作者：</font>** Zijie Zhu, Weiren Cai, Yizhou Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering camera and hand motion in world coordinates from egocentric video is a key capability for activity understanding, robot learning, and augmented reality. Existing systems typically decompose this problem into separate stages for camera motion, depth, hand reconstruction, and trajectory refinement, resulting in substantial computational overhead and preventing the joint modeling of camera and hand motion. We introduce MINT (Minting IN-the-Wild Trajectories), the first foundation model that directly produces complete world-space two-hand trajectories from ego-centric RGB video. From a single shared spatiotemporal video representation, MINT jointly predicts the camera trajectory, camera-frame hand states, and per-frame hand presence, and then produces world-space hand motion via explicit coordinate transformations. Training such a model at scale is challenging, since paired world-space camera and hand annotations are scarce. We therefore develop an open-source labeling EGOPIPELINE that converts large collections of public egocentric videos into structured camera-and-hand trajectory supervision. MINT is first pretrained on these large-scale pseudo-labels and then fine-tuned on a small set of high-quality joint annotations. Across public benchmarks, MINT achieves [xxx] improvement in world-space hand trajectory accuracy, [xxx] improvement in camera trajectory estimation, and [xxx] faster end-to-end trajectory generation than the labeling pipeline, while generalizing zero-shot to unseen egocentric datasets. We release the model, training and inference code, labeling pipeline, and a curated 1,021-hour egocentric trajectory dataset.

---


### 114. [Discourse Dependency: A Continuous Criterion for Translation Difficulty](https://arxiv.org/abs/2609.04959)

**<font color=#1a73e8>作者：</font>** Ahrii Kim, Chanjun Park, Seong-heum Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent calls for harder machine translation benchmarks have not clarified what difficulty should mean. We argue that one meaningful and currently unmeasured axis is referential reach, the distance a segment must look back into its document to resolve the entities and pronouns it contains. We formalize this as discourse dependency (DDP), a metric-free, source-side measure computed from named entity re-mentions and pronominal coreference. Validated against gold coreference, DDP errs one-sidedly in 99.2% of segments, so a high-DDP segment is certified to require long-range context. Applying DDP to WMT24++ and WMT25 shows that both are heavily skewed toward low-DDP segments, which domain labels do not distinguish. Building on DDP, we compare five context injection strategies in an English-Korean post-editing setup, varying context size and selection. As DDP grows, no strategy keeps pace with human post-editing. On segments with DDP >= 15 raters prefer human translations, while automatic metrics register no difference. As frontier systems saturate aggregate scores, DDP shifts evaluation from how well models score to how far they can reach.

---


### 115. [Why We Care About Understanding: Competence through Predictive Compression](https://arxiv.org/abs/2609.04962)

**<font color=#1a73e8>作者：</font>** Matthieu Queloz, Pierre Beckmann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> What is the relation between understanding and compression, and why does human understanding take such a heavily compressed form? Across information theory, machine learning, and AI research, a substantial tradition identifies understanding with compression-a thought captured in Gregory Chaitin's dictum that "comprehension is compression." Philosophers, by contrast, have characterized understanding in terms of grasping connections, giving explanations, and handling novelty. This paper bridges the two pictures through three interlocking theses. The first concerns the concept of understanding: it serves as an efficient proxy for a distinctive form of robust competence, enabling us to identify whom to trust and whom to learn from. The second concerns the state of understanding: to understand a domain is to possess a mental model of its relational structure that enables prediction, and what enables prediction enables compression, because what becomes predictable need not be stored separately. Compression is therefore not identical with comprehension, but its representational shadow. The third concerns the characteristically human form of understanding: the fiduciary and transmission functions highlighted by the first thesis impose pressures of demonstrability and transmissibility that drive human understanding toward principled simplicity. The resulting framework explains both the appeal and the limits of compressionist accounts of understanding while shedding light on the inscrutability of AI systems.

---


### 116. [ARC-Loc: Leveraging Azimuthal Ray Convergence as a Geometric Cue for Direct Cross-View Localization](https://arxiv.org/abs/2609.04965)

**<font color=#1a73e8>作者：</font>** Hyeongsik Kim, Mincheol Kim, Heejoon Moon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-view localization (CVL) estimates the pose of a ground image by matching it to a geo-referenced satellite image. To bridge the extreme viewpoint gap, mainstream pipelines rely on Bird's-Eye-View (BEV) transformations or 2D-to-3D lifting. However, deriving 3D structures from a single ground image is fundamentally ill-posed, causing these methods to endure geometric distortions and computational costs during 3D lifting or BEV projection. Furthermore, relying on external depth foundation models to resolve this introduces latency and remains susceptible to noisy predictions. In this work, we present a different approach inspired by a human navigation technique called resection, that can perform direct ground to satellite image matching and localization without relying on external depth foundation models. The key insights of our method are that (i) ground keypoints can be translated into azimuthal rays on the satellite map, and (ii) these rays ideally converge at the user location. Exploiting this geometric constraint through direct line-to-point correspondences, we introduce a minimal Azimuthal Ray Convergence (ARC) solver to identify the intersection, alongside an ARC loss to optimize the matching network. By eliminating dependencies on computationally heavy BEV transformations and external depth foundation models, our approach achieves faster, memory-efficient inference, while its explicit feature matching ensures straightforward compatibility with existing frameworks. Experiments on VIGOR and KITTI demonstrate that ARC-Loc maintains competitive localization accuracy compared to recent approaches, highlighting its practicality.

---


### 117. [Robust Coverless Linguistic Steganography via Sentence Embedding Space with Global Resynchronization](https://arxiv.org/abs/2609.04970)

**<font color=#1a73e8>作者：</font>** Lizhi Xiong, Yuping Lu, Jun Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Linguistic steganography enables covert communication through natural language. Existing methods heavily rely on token-level operations and struggle to maintain reliability under word- and sentence-level textual perturbations. Moreover, variable-length coding-based schemes are highly susceptible to bit-slippage under minor disturbances, as perturbations cause desynchronization between embedded and extracted bit sequences. To address these issues, we propose a robust coverless steganographic framework that operates in the sentence embedding space rather than the token space. Specifically, secret messages are encoded as hierarchical clustering paths in the sentence embedding space, which enhances decoding stability against word- and sentence-level textual perturbations. To tackle the bit-slippage problem, we introduce a Global Resynchronization Mechanism (GRM) that reframes variable-length bitstreams as discrete symbols anchored to semantic subspaces, decoupling local embedding failures from global message recovery. Experimental results demonstrate that under word- and sentence-level perturbations, our approach achieves substantial improvements in robustness, while maintaining effective embedding capacity and exhibiting strong resistance to statistical analysis.

---


### 118. [RefDiT: Local Attribute Guidance in Reference-Based Image Generation](https://arxiv.org/abs/2609.04976)

**<font color=#1a73e8>作者：</font>** Rameshwar Mishra, Srikrishna Karanam, A V Subramanyam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalization models generate new images guided by a few subject references, while style transfer methods aim to produce images aligned with a global style derived from a reference image. Recent approaches perform well when the reference image contains a single object, effectively capturing a global style that encompasses all implicit attributes. However, when applied to complex real-world scenes containing multiple objects with distinct attribute characteristics, these methods, due to their global-level guidance, fail to localize relevant elements in the reference image. The global guidance restricts their ability to generate new images based on the local attributes in the reference image. Moreover, existing methods typically employ a single identifier token to capture all details from the reference, resulting in a lack of individual, attribute-level control. Motivated by these limitations, we propose RefDiT, a novel framework for reference-guided image generation. RefDiT takes as input a reference image, a text prompt, and an optional user-provided guidance context. RefDiT employs local region guidance using the attributes of local elements. It constructs an attribute-aware conditioning signal from the reference image by performing attribute-level decomposition of the identifier token and performs context adjustment in the inference prompt to train low-rank adapter (LoRA) blocks of a diffusion transformer (DiT)-based generative model. RefDiT learns the correspondence between identifier tokens and local regions in the reference image, enabling more effective local guidance.

---


### 119. [Global to Local: Topology-Preserving Adaptive Graph Pooling via Granular-Ball](https://arxiv.org/abs/2609.04978)

**<font color=#1a73e8>作者：</font>** Sen Zhao, Gaojie Xu, Shuyin Xia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph pooling aims to compress the graph, including both node embeddings and their underlying topological patterns, into a more compact representation. Previous works focus primarily on the overly fine-grained representation of nodes, progressively coarsening the graph by removing nodes or merging them into clusters, thus neglecting the global-to-local patterns and adaptive granularity of the graph's topological structure. In the real scenario, graphs as a whole can be considered the coarsest level of granularity, encapsulating the global topological structure, with progressively finer-grained local topological structures represented from top to bottom. This process continues until the adaptive granularity for each subdomain is reached. To this end, we propose a novel Topology-Preserving Adaptive Graph Pooling (TPAGP) method that dynamically partitions graphs into granular balls by integrating node features and topological information, enabling the generation of multi-granularity representations that effectively capture both local and global structural patterns. Additionally, we design a multi-granularity graph network model that facilitates feature interaction and optimization across different granularities, significantly enhancing performance in graph classification tasks. Experimental results demonstrate that TPAGP outperforms existing pooling methods across various benchmark datasets, effectively mitigating information loss caused by fixed-granularity strategies.

---


### 120. [MIVAIS: A Study Environment for Multi-Agent Mixed-Initiative Visual Analytics Applications](https://arxiv.org/abs/2609.04983)

**<font color=#1a73e8>作者：</font>** Tobias Stähle, Simon Schneider, Rita Sevastjanova 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mixed-initiative Visual Analytics (VA) systems empower human users by interleaving human intuition with software agents and their machine intelligence. However, the development and rigorous evaluation of such systems remain constrained by engineering overhead. Developers must, e.g., implement complex, low-level state synchronization to manage asynchronous agent behaviors, while researchers struggle to capture the multimodal provenance required to study and evaluate human-AI collaboration. We present MIVAIS, a dual-layered research platform designed to abstract the structural complexities of mixed-initiative VA. First, it contributes a computational Infrastructure that standardizes human-software agent interaction, state synchronization, and communication between the agents. Second, it provides a declarative Study Environment that automatically logs multimodal human-AI telemetry - including application/system state, screen capture, audio, and additional sensor data - enabling seamless, in-situ user studies and post-session analysis. We technically validate our infrastructure by replicating three state-of-the-art systems (Podium, Voyager 2, and ProactiveVA). Furthermore, we evaluate the framework's expressiveness and efficiency through expert case studies with HCI and VA researchers, demonstrating how MIVAIS effectively lowers the barrier to prototyping and evaluating intelligent, co-adaptive interfaces.

---


### 121. [Temporal Residual Neural Radiance Fields for Monocular Video Dynamic Human Body Reconstruction](https://arxiv.org/abs/2609.04984)

**<font color=#1a73e8>作者：</font>** Tianle Du, Jie Wang, Xiaolong Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the field of computer vision and graphics, high-quality reconstruction of the human body in static scenes has been achieved in recent years by a single multilayer perceptron (MLP) in a number of approaches. However, MLPs have capacity limitations, requiring substantial training time and computational resources for dynamic scene reconstruction. And the quality of reconstruction is significantly constrained. This paper proposes a method for effectively processing complex spatiotemporal signals in dynamic scene human 3D modeling. The proposed method uses Temporal Residual Neural Radiance Fields to achieve novel view rendering and new pose synthesis of human this http URL address the problem of representing temporal signals in video sequences, we construct a temporal residual field which is not related to the MLP architecture. Secondly, to improve reconstruction efficiency, we propose an integrated approach that reduces trainable parameters and accelerates rendering, thereby enhancing the network's feature representation capability. Finally, we design a multi-dimensional loss function to accurately measure the loss between predicted and actual spatial pixel values. The experimental results show that our proposed approach improves the peak signal-to-noise ratio (PSNR) and structural similarity index (SSIM) accuracy metrics compared to the latest representative methods. It maintains similar accuracy to Anim-NeRF and Neural Body while achieving a nearly 780-fold increase in time efficiency.

---


### 122. [Beyond Homoscedasticity: Decoupled Uncertainty Optimization for Deep Imbalanced Regression](https://arxiv.org/abs/2609.04995)

**<font color=#1a73e8>作者：</font>** Juncheng Zhou, Jiaxi Lu, Weijing Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep Imbalanced Regression (DIR) is pervasive in continuous prediction tasks across diverse modalities, such as age estimation, depth prediction, and protein mutation activity prediction, where label-scarce tail samples often carry higher practical value. However, most existing methods still learn deterministic point mappings under mean squared error or its simple variants, implicitly assuming a uniform uncertainty level across all samples and thereby overlooking the instance-wise heteroscedasticity that is widespread in long-tailed data. We further point out that even heteroscedastic negative log-likelihood suffers from a gradient coupling issue, which, under DIR scenarios, weakens the learning signal of hard tail samples and leads to optimization inertia as well as tail underfitting. To address this, we propose DUO, an uncertainty-aware long-tailed regression framework. Specifically, the proposed method models the regression target as a conditional Gaussian distribution to explicitly characterize instance-level predictive uncertainty, and transforms uncertainty into a dynamic enhancement signal for tail samples through decoupled mean-variance optimization. Furthermore, we design a distribution-guided contrastive learning mechanism that adaptively constructs positive and negative pairs based on the overlap between sample distributions, thereby alleviating feature looseness and cross-label semantic entanglement. Across visual and biological DIR benchmarks, DUO achieves the best few-shot bMAE and GM on IMDB-WIKI-DIR, AgeDB-DIR, and AAV2-DIR while remaining competitive on few-shot MAE.

---


### 123. [TPMSpy: Validation of Measured Boot Systems by Low-Level Tracing of TPM Usage](https://arxiv.org/abs/2609.05011)

**<font color=#1a73e8>作者：</font>** Roman Lacko, Petr Svenda  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Measured Boot extends trust in a booted system by recording cryptographic measurements of executed software and system state into a Trusted Platform Module (TPM), enabling subsequent verification through remote attestation. Although this mechanism is increasingly deployed in contemporary operating systems, its practical security depends on whether implementations measure the expected components under the expected conditions, yet this is not checked systematically.
We propose a platform-agnostic method for analysing low-level TPM usage at the level of virtualized system--TPM interactions. It enables independent reconstruction and validation of the TPM Event Log without relying on the quoting mechanism itself. Because it does not depend on implementation details, it is applicable to both open and closed systems. We demonstrate the method on both Linux and Windows and conduct a systematic longitudinal analysis of Linux systems with systemd versions 245--258 (2020--2025), examining how Measured Boot usage evolved and observing wide divergence. No single usage pattern emerged amongst systems, warranting customized analysis.
The analysis identifies undocumented behavioural changes, reveals inconsistent measurements of user-space systemd services, which prevent reliable remote attestation and LUKS disk decryption on such systems.

---


### 124. [Solution-space heterogeneity shapes federated learning dynamics across partial differential equations](https://arxiv.org/abs/2609.05012)

**<font color=#1a73e8>作者：</font>** Ping Luo, Jiahuan Wang, Ziqing Wen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated scientific machine learning enables institutions to train neural surrogates without centralizing local physical data, yet studies of partial differential equations (PDEs) lack a transferable definition of non-independent and identically distributed data. Existing protocols partition coordinates, coefficients, boundary conditions, or geometries according to equation-specific rules. Here, we introduce solution-space PDE-Dirichlet, a protocol that converts continuous supervised responses into reusable solution bins and quantifies the realized separation between clients through optimal transport over the geometry of these bins. We derive an exact inverse relation between population allocation heterogeneity and the Dirichlet concentration, and we establish conditions under which response heterogeneity induces gradient disagreement, local-update dispersion, and parameter divergence. Across seven controlled and public PDE tasks, three neural-operator families, and five random seeds, a lower concentration consistently increases the realized solution distance and optimization heterogeneity. The degradation in final error is task dependent: the largest effect occurs for low-viscosity Burgers, reaching 4.157 percentage points under the most heterogeneous setting, whereas additional communication or smoother dynamics can reduce the final gap despite persistent parameter separation. These results distinguish a reproducible geometric mechanism from task-dependent generalization outcomes and provide a common basis for evaluating non-IID federated PDE learning.

---


### 125. [Has MIMO decoding been proved hard from lattice problems?](https://arxiv.org/abs/2609.05013)

**<font color=#1a73e8>作者：</font>** Yang Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Multiple-input multiple-output (MIMO) technology is fundamental to modern wireless communication. Physical layer security seeks to protect transmitted information by exploiting properties of the noisy communication channel. Dean and Goldsmith proposed a polynomial time reduction from lattice problems to MIMO decoding by adapting Regev's reduction for learning with errors (LWE). If valid, this reduction would give physical layer security a strong computational foundation based on the hardness of established lattice problems. Subsequent works presented attacks and counterexamples against the resulting construction, casting doubt on its security but leaving the precise validity and limitations of the underlying reduction incompletely understood. We provide a theoretical examination of the revised reduction and identify the structural features of the LWE reduction that fail to carry over to the non-modular MIMO setting, hence showing that its published proof does not establish the claimed hardness of MIMO decoding. Our results distinguish flaws in the hardness proof from direct attacks on particular parameter choices and clarify what would be required of any attempted repair. We do not rule out physical layer security for MIMO systems in general, but show that the claimed lattice hardness guarantee does not follow from the existing reduction.

---


### 126. [Amortizing Scaling Law Construction Costs](https://arxiv.org/abs/2609.05016)

**<font color=#1a73e8>作者：</font>** Abhash Kumar Jha, Diana Alexandra Onuţu, Neeratyoy Mallik 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling laws guide the design choices for training large foundation models, but deriving them involves training an exhaustive grid over hyperparameters, token budgets, and parameter counts, which is computationally expensive. Fitting a scaling law, however, only requires the best-loss frontier across compute scales, discarding most of the trained configurations. We propose a framework for efficient scaling law construction that formulates data collection as a Bayesian optimization problem, and introduce metrics for comparing scaling law fitting methods under constrained compute budgets. We find that progressively expanding the compute budget during acquisition, mirroring the compute-ordered evaluation of configurations in practice, substantially improves recovery efficiency. Augmenting the observed configurations with surrogate-fantasized evaluations then recovers the broader experimental grid, allowing accurate scaling law fitting without training every configuration. Together, these can closely match scaling law fits over a full dense grid at computational savings of up to $10\text{--}100\times$.

---


### 127. [Compositional Reward Models for Conditional Medical Image Generation](https://arxiv.org/abs/2609.05028)

**<font color=#1a73e8>作者：</font>** Aayush Kumar Tyagi, Prathosh A.P., Mausam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Acquiring high quality annotated medical image data is critical for training deep learning models; however, annotation is expensive, time consuming, and requires domain expertise. Conditional diffusion models, such as ControlNet, offer an alternative by generating images conditioned on semantic masks and text. However, existing approaches fail to capture fine grained properties (e.g., intensity and texture), as well as semantic consistency expected by domain experts, limiting their effectiveness for downstream tasks. Recent attempts to address these issues using reinforcement learning fine-tuning remain limited due to the reliance on a single scalar reward, which conflates diverse failure modes and provides weak corrective signals. We propose PRISM, a Compositional Reward Model (CRM) framework for conditional medical image generation. Instead of assigning a single reward, we decompose image quality into verifier grounded stages, each evaluating a distinct aspect of correctness from fine to coarse properties, including low level attributes (intensity and texture), structural alignment with conditioning inputs, and high level semantic fidelity. These stage wise rewards are composed through a Hierarchical Constrained Propagation (HCP) mechanism that enforces a fine to coarse notion of correctness, ensuring that lower level deficiencies are resolved before higher level rewards are accrued, preventing easier objectives from masking critical failures.
We evaluate PRISM across three datasets spanning diverse medical imaging tasks: PanNuke (multi-class cell segmentation), CeDeM (villi/crypt detection and measurement), and ISIC (skin lesion classification). Training downstream models with data generated by PRISM yields improvements over closest baselines, including a 2.3% increase in mDice on PanNuke, a 8.5% reduction in Mean Relative Error (MRE) on CeDeM, and increases ISIC F1 by 5.9%.

---


### 128. [PuTR-CouT: Counting-by-Tracking in Camera-Trap Image Sequences](https://arxiv.org/abs/2609.05038)

**<font color=#1a73e8>作者：</font>** Fagner Cunha, Juan G. Colonna, Eulanda M. dos Santos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Species identification in camera trap images has been widely studied, but key ecological modeling tasks such as species abundance or density estimation also require counting individual animals. However, the lack of counting labels in most datasets and low frame rates (typically ~1 frame per second) make sequence-level tracking and count estimation particularly challenging. In this work, we present PuTR-CouT, a counting-by-tracking framework built on a transformer-based learned association mechanism for sequence-level animal counting in camera trap images. To address the scarcity of annotated tracking data, we generate synthetic training data by exploiting structural priors, such as static backgrounds and short temporal bursts, to heuristically create pseudo-tracking labels in a weakly supervised manner. The resulting tracker associates detections across frames, using these tracks to estimate per-species counts. We also refine the MaxBoxCount heuristic used by the top solutions of the iWildCam 2021 challenge as a strong baseline, setting the highest score reported to date. When evaluated on the iWildCam 2021 benchmark, our framework PuTR-CouT delivers competitive counting results compared to the improved MaxBoxCount, with the added capability of multi-species predictions and track-level verification.

---


### 129. [Towards Efficient Evaluation of Evolutionary Transfer Optimization: Case Studies on Task-Parameterized Applications](https://arxiv.org/abs/2609.05040)

**<font color=#1a73e8>作者：</font>** Yanchen Li, Xiaoming Xue, Kay Chen Tan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As evolutionary transfer optimization (ETO) scales to larger collections of related tasks, problem evaluation can become a major source of runtime growth. This work studies problem-side evaluation scaling in task-parameterized applications and reformulates application-specific serial computations into forms suitable for parallel execution. We organize evaluation scaling into two levels: the number of evaluated tasks and the workload within each task. In multi-task optimization, matrix-recursive kinematic-arm evaluation is reformulated using an accumulation-matrix representation of cumulative link directions. In sequential transfer optimization, pointwise B-spline trajectory evaluation is reformulated using a blending-matrix representation for trajectory and collision computations. Both reformulations maintain close numerical agreement with their reference evaluations and substantially reduce runtime, yielding $256.72\times$ and $93.91\times$ end-to-end speedups, respectively. These results demonstrate problem-side reformulation as a practical route toward scalable ETO. Both application implementations and experimental scripts are released as open source to support reproducibility and reuse.

---


### 130. [Scales, Reflections, and Conversations: A Multi-Modal Approach to Emotion Annotation](https://arxiv.org/abs/2609.05046)

**<font color=#1a73e8>作者：</font>** Pragya Singh, Prashasti Gupta, Hitesh Bhandari 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mental health concerns are increasing worldwide, highlighting the need for interventions that support everyday emotional well being. Prior work has demonstrated the potential of wearable and mobile technologies to deliver data driven interventions. However, developing effective data-driven systems requires access to emotion data that captures individuals' emotional variability and change in everyday contexts. Existing approaches to data collection largely rely on frequent, prescheduled prompts and predefined scales or questionnaires. These methods often fail to account for participants' availability, agency, or the complexity of their emotional experiences, resulting in shallow, context poor data. In this paper, we present a feasibility study of a participant centric, multimodal emotion-annotation application designed around users' emotional intensity and availability. Our findings show how multimodal emotion logging can shape participants' experiences and data logging behaviors, and demonstrate its potential to support the collection of richer, more nuanced emotion data.

---


### 131. [Efficient Multi-Timescale Event Representations for Feed-Forward Object Detection](https://arxiv.org/abs/2609.05049)

**<font color=#1a73e8>作者：</font>** Fredrik Lundell, Per-Erik Forssen, Mårten Wadenbäck 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous systems require robust low-latency perception under rapidly changing scene dynamics and challenging illumination. In event cameras object detection commonly relies on recurrent architectures to accumulate sparse temporal information over time. This work investigates how temporal information can be encoded directly within the event representation. We propose a confidence-normalized continuous multi-timescale representation based on logarithmic B-spline temporal encoding together with a geometry-aware local confidence mechanism that exploits the spatial structure of event generation. Using a fixed feed-forward EventCenterNet detector, we show that the proposed representations consistently outperform the compact CSTR representation on PEDRo and Gen1 datasets. We further introduce a recursive exponential-polynomial approximation that enables efficient event-by-event updates while largely preserving detection performance. These results demonstrate that carefully designed event representations can capture a substantial portion of the temporal information learned through recurrent temporal modeling, providing a promising foundation for efficient feed-forward, event-driven, and future neuromorphic object detection.

---


### 132. [Adaptive Multi-Granularity Temporal Modeling for Weakly Supervised Video Anomaly Detection](https://arxiv.org/abs/2609.05066)

**<font color=#1a73e8>作者：</font>** Changyi Li, Yu Xiao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As the scale of video surveillance data outpaces manual annotation capacities, weakly supervised video anomaly detection (WSVAD) has emerged as a critical research frontier. Most existing approaches formulate WSVAD within a Multiple Instance Learning (MIL) framework that relies on rigid, hand-crafted temporal priors to supervise anomaly scoring. However, such formulations exhibit limited adaptability to the wide variation in anomaly durations and temporal dynamics observed in real-world videos, often leading to unstable or unreliable snippet-level predictions. To address this limitation, we propose an adaptive temporal modeling framework for WSVAD that explicitly accounts for variations in video dynamics across multiple temporal granularities. First, we introduce a Temporal Refinement Module (TRM) that leverages dynamic positional encoding and a learnable class token to model long-range temporal dependencies while distilling a stable global video-level representation. Second, to capture anomalous events with varying frequency and duration, we develop an adaptive Event Segmentation Module (ESM) that identifies event boundaries through temporal discontinuity analysis and aggregates snippet features into discriminative event-level representations. Finally, for snippet-level and event-level predictions, we propose an adaptive similarity-based fusion strategy that dynamically integrates anomaly scores into video-level predictions, replacing fixed top-k aggregation heuristics with global semantic relevance. Extensive experiments on two benchmarks demonstrate that the proposed framework consistently outperforms state-of-the-art methods.

---


### 133. [MultiAttenGastro: Multi-Dimensional Attention Augmentation for Gastrointestinal Endoscopy Classification](https://arxiv.org/abs/2609.05070)

**<font color=#1a73e8>作者：</font>** Sadhana Devarajan, Praveen Kumar Chandaliya, Dhruvin Jashvant Kumar Shah 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated gastrointestinal (GI) endoscopy classification requires models that generalize across diverse modalities and class distributions, often far from natural-image pretraining. We propose MultiAttenGastro, a plug-and-play attention framework with parallel 1-D channel, 2-D spatial, and 3-D contextual heads, and present the first systematic cross-dataset evaluation across eight CNN and transformer backbones on five public GI datasets (80 backbone--dataset runs). We find that attention effectiveness is not universal but tracks the representational gap between ImageNet features and the target distribution: MultiAttenGastro improves 6 of 8 backbones on Kvasir-Capsule (14-class WCE, large gap; best macro F1 98.33\%), is uniformly negative on the small-gap Kvasir-v2 benchmark (0/8), and shows mixed outcomes on datasets with intermediate gap. Five-seed ablation on the strongest case (Kvasir-Capsule, ConvNeXt-Tiny) shows this improvement is directionally consistent, but not statistically decisive (paired $t$: $p=0.47$; Wilcoxon: $p=0.63$), and that individual attention heads are not uniformly beneficial in isolation only their combination yields a positive mean effect. Centered Kernel Alignment (CKA) analysis links this pattern to representational redundancy: low inter-head CKA under large domain gaps coincides with the framework's only consistent gains, while high redundancy under small gaps coincides with its losses. We report these results, including the non-significant margins, as evidence for when and why multi-dimensional attention helps GI endoscopy classification, rather than as a claim that MultiAttenGastro is a strictly superior architectural choice.

---


### 134. [Confounding-Valid Conformal Inference for Counterfactual KPIs in Wireless Networks](https://arxiv.org/abs/2609.05073)

**<font color=#1a73e8>作者：</font>** Abdessamed Qchohi, Jessica Moysen Cortes, Matteo Zecchin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Conformal counterfactual inference enables network operators to use logged telemetry to reliably answer 'what-if' questions about network operation. These answers typically take the form of prediction sets that contain, with a user-defined probability, the key performance indicators (KPIs) that would have been observed under alternative control actions. A key challenge is that logged telemetry may omit variables used by the controller, resulting in hidden confounding and invalidating the statistical guarantees of counterfactual analysis. In principle, this issue can be addressed using randomized telemetry, collected by assigning control actions independently of the network state. However, because such randomization may disrupt normal operation, randomized telemetry is typically scarce, causing counterfactual analysis based solely on it to produce uninformative prediction sets. To address these challenges, we propose Confounding-Valid Counterfactual Conformal Inference (CV-CCI), which combines abundant, potentially confounded observational telemetry with limited randomized data through the General Synthetic-Powered Inference (GESPI) principle. CV-CCI leverages observational data to improve efficiency while using randomized data to retain finite-sample coverage guarantees under arbitrary hidden confounding. Experiments on two representative radio access network (RAN) control tasks show that CV-CCI remains valid under hidden confounding while producing more efficient prediction sets than state-of-the-art confounding-valid baselines.

---


### 135. [MePo++: Unifying Representation Refinement and Reconciliation for General Continual Learning](https://arxiv.org/abs/2609.05075)

**<font color=#1a73e8>作者：</font>** Guanglong Sun, Kanglei Zhou, Liyuan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> General continual learning (GCL) aims to learn from evolving data streams without task identities, explicit boundaries, or repeated access to previous data, making it a realistic yet challenging setting for continual intelligence. Although pretrained models (PTMs) provide rich prior knowledge for addressing the limited supervision and non-stationary nature of GCL, existing PTM-based methods often directly adapt pretrained representations and overlook two critical gaps: the misalignment between upstream pretraining and downstream continual adaptation, and the unreliability of conventional output alignment under blurry streams. Here we propose MePo++, a unified post-training framework that bridges pretrained knowledge and downstream GCL through representation refinement and reconciliation. MePo++ introduces two complementary components: MetaPrep, which improves representation plasticity for continual adaptation through unsupervised meta-refinement over pseudo continual sequences; and StreamAlign, which reinforces representation stability by reconciling evolving online features with a stable pretrained geometry. By improving representation learnability before adaptation and preserving alignment during continual learning, MePo++ enables PTMs to remain both plastic for new concepts and stable over evolving streams. Experiments across diverse PTMs, datasets, and continual learning baselines demonstrate the consistent effectiveness and generality of MePo++ for PTM-based GCL. Our code is available at this https URL.

---


### 136. [Deep Microcompression: Structured Pruning and Bit-packed Quantization for Microcontrollers](https://arxiv.org/abs/2609.05081)

**<font color=#1a73e8>作者：</font>** Opegbemi Matthias Busoye, Tolulope Matthew Busoye, Eghonghon-aye Eigbe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces Deep Microcompression (DMC), a hardware-aware pipeline for deep learning inference on bare-metal microcontrollers. DMC integrates structured pruning, quantization-aware training, and fixed-length bit-packing to achieve a 55.8$\times$ weight compression ratio on LeNet-5 (98.77\% accuracy), generating a dependency-free C library with deterministic latency. On the RP2040 (Cortex-M0+), DMC reduces binary size by 3$\times$ versus TensorFlow Lite while matching its accuracy. Critically, DMC enables the first documented deployment of a standard CNN on the ATmega328P, a device constrained to 2KB SRAM, previously considered infeasible for CNN inference.

---


### 137. [Constructing and Evaluating Clinical Reasoning Trajectories for Medical Agent](https://arxiv.org/abs/2609.05090)

**<font color=#1a73e8>作者：</font>** Yunqi Zhu, Wensheng Zhang, Xuebing Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluation of medical artificial intelligence agents remains predominantly answer-centric, assessing only the correctness of final outputs while overlooking the quality of intermediate reasoning. In clinical settings, however, a correct answer reached through fabricated evidence or incoherent logic is as dangerous as an incorrect one. We propose MedTraj, a framework that treats reasoning trajectories as critical objects for construction, evaluation, and optimization. The pipeline generates structured multi-step reasoning chains from medical reasoning sources. Each trajectory is then parsed into clinical observations, evidence, numbered reasoning steps, and a final conclusion, and scored across five quality dimensions: coherence, evidence support, hallucination, completeness, and traceability. Controlled error injection introduces targeted faults into otherwise correct trajectories to establish causal links between specific reasoning failures and measurable quality degradation. Building on this, step-level filtering based on marginal contribution identifies which individual reasoning steps drive or undermine trajectory quality. Finally, quality-weighted context learning feeds trajectory evaluations back into the model at inference time, allowing it to learn from both strong and weak reasoning demonstrations. Experiments across CareQA, PubMedQA, and CECMed demonstrate that trajectory context consistently improves reasoning coherence, with gains of +0.029 to +0.041 over a zero-shot baseline. On CECMed, quality-weighted context nearly doubles the correctness over the zero-shot baseline while cutting the hallucination ratio by 87%. Marginal-contribution analysis further shows that a small minority of reasoning steps carry most of the quality signal, and that extending chains beyond four steps yields diminishing returns.

---


### 138. [Training-Free Logical and Structural Anomaly Detection via Calibrated Fusion](https://arxiv.org/abs/2609.05091)

**<font color=#1a73e8>作者：</font>** Changyi Li, Miao Yu, Kai Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial anomaly detection must handle two distinct defect families: structural anomalies, which manifest as local texture corruptions, and logical anomalies, which violate global rules on object count, composition, or arrangement. Existing detectors typically favor one family at the expense of the other. In particular, training-free methods effectively exploit frozen representations but lack an explicit notion of object count, while methods that reason about counts usually rely on category-specific component modeling. We show that counting ability can be introduced into training-free anomaly detection without additional training or part-level supervision. Our key idea is a normal-set calibration that aligns heterogeneous anomaly cues using statistics from normal images, enabling their direct fusion within a unified training-free framework. Built upon this calibration, our detector combines complementary frozen cues to address both logical and structural anomalies. On MVTec-LOCO, our method achieves image-level AUROCs of 89.0 and 95.9 on logical and structural anomalies, respectively, yielding a 92.5 average---the best among training-free detectors in our comparison. It remains competitive with methods requiring network training or part annotations, while its structural variant matches PatchCore on MVTec-AD (99.1 image-AUROC), suggesting that the proposed calibration generalizes beyond logical anomaly detection.

---


### 139. [Operational Roles of QRNG-Derived Quantum Entropy in Bitcoin Proof-of-Work Architectures](https://arxiv.org/abs/2609.05092)

**<font color=#1a73e8>作者：</font>** Ricardo Fernandes da Silva, Paulo Vitor Batista Santos  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Replacing classical entropy with QRNG output does not change honest Bitcoin PoW success probability when candidate headers remain distinct. The original contribution of this paper is a reproducible benchmark that locates and measures the operational value of quantum entropy in hybrid quantum-classical mining infrastructure through two scheduler-level observables, the entropy-efficiency factor $\eta$ and the reboot-diversity index $\rho$. Monte Carlo and scheduler simulations with confidence intervals show parity for competent deterministic and strong-classical baselines, while QRNG value emerges in assurance-oriented scenarios involving correlated restart faults, namespace reuse, and entropy provenance. The study is therefore positioned as a simulation-based validation framework rather than as a device-level QRNG demonstration; hardware-in-the-loop validation with recorded or live QRNG streams is identified as the next experimental step.

---


### 140. [ProCA: Progressive Contrastive Alignment for Robust EEG Visual Decoding](https://arxiv.org/abs/2609.05094)

**<font color=#1a73e8>作者：</font>** Kanglei Zhou, Chunyan Lan, Dongyang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Electroencephalogram (EEG) visual decoding aims to recover visual semantics from non-invasive neural time-series signals, for which robust alignment between noisy neural responses and stable semantic representations is key to achieving high-performance decoding. Despite recent advances in contrastive learning, robust EEG decoding remains challenging because existing methods rely on fixed visual or textual anchors whose semantic relations may become misaligned with EEG representations that vary across trials, subjects, and learning stages. Our empirical evidence shows that this instability appears across both standard EEG decoding protocols and more challenging robustness settings, including strict cross-subject transfer and realistic personalized continual adaptation. We provide a formal analysis showing that fixed semantic supervision can bias optimization when EEG-specific relations evolve, and that structure-agnostic perturbations may distort semantically important EEG components. To address these issues, we propose Progressive Contrastive Alignment (ProCA), a unified and model-agnostic framework for adaptive neural-semantic alignment. ProCA progressively refines class-level contrastive supervision from frozen vision-language priors to EEG-aware semantic relations, and introduces structure-consistent interpolation to constrain feature mixing according to channel-wise and temporal importance. Across subject-dependent, subject-independent, strict cross-subject transfer, and continual adaptation settings, ProCA achieves average relative Top-1/Top-5 gains of 7.4%/3.9%, 10.0%/4.6%, 28.1%/17.8%, and 16.8%/11.6%, respectively.

---


### 141. [NEAT-POCKET: Pocket-Conditioned Autoregressive 3D Molecular Generation with a Neighborhood-Guided Set Transformer](https://arxiv.org/abs/2609.05097)

**<font color=#1a73e8>作者：</font>** Roxane Axel Jacob, Daniel Rose, Thierry Langer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI-driven de novo molecular design offers a promising route to accelerate early-stage drug discovery by generating novel ligands directly within target protein binding pockets. We present NEAT-POCKET, a pocket-conditioned extension of the autoregressive NEAT model for 3D molecular generation. NEAT-POCKET generates molecules atom by atom in protein pocket environments while preserving atom permutation invariance and explicitly modeling hydrogen atoms. Benchmarks on the CrossDocked and SPINDR datasets show that NEAT-POCKET achieves competitive structure-based generation performance while sampling substantially faster than existing baselines. Beyond full-molecule generation, NEAT-POCKET naturally enables pocket-conditioned fragment completion, a task directly relevant to lead optimization and scaffold elaboration. These results position NEAT-POCKET as a fast, flexible, and practical framework for structure-based drug design.

---


### 142. [Compact Bellman-Grounded Cognitive Maps for Cost-Aware Navigation](https://arxiv.org/abs/2609.05104)

**<font color=#1a73e8>作者：</font>** Yuzhe Han, Mingkun Xu, Yujie Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biological agents navigate familiar environments not by re-solving routes for each new goal, but by reusing a learned map built once and read off as goals change. Existing artificial cognitive-map models mimic this reuse, yet their guidance is not explicitly grounded in additive heterogeneous route costs. Furthermore, they often struggle with memory efficiency: representative state-indexed and high-rank spectral constructions incur substantial storage growth as the environment scales. We present BCM, which grounds a reusable cognitive map in local edge costs through a self-supervised Bellman-grounded objective and a compact coordinate encoding, supporting changing goal queries without per-goal retraining. On weighted grids of up to $N=1600$ nodes, BCM maintains full success and only a 5\% mean Gap relative to exact Dijkstra search, compared with about $45\%$ for a connectivity-based spectral baseline. Notably, as the graph size increases from $N=400$ to $N=3600$, its memory footprint grows sublinearly while maintaining competitive performance, making our method scalable to complex environments. Together, these results show that additive route costs can be written into a compact, reusable cognitive-map representation, bridging the gap between biological flexibility and optimal path planning.

---


### 143. [A Comparative Study of Counterfactual Explainers for Graph Neural Networks Enabling Multiple Types of Graph Edit](https://arxiv.org/abs/2609.05113)

**<font color=#1a73e8>作者：</font>** Maria Myrto Villia, Filippos Gouidis, Theodore Patkos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual explanations for graph-structured data seek to determine minimal and realistic modifications required in an input graph to alter a model's prediction to a predefined output. Although counterfactual explainers that support modifying the graph by both adding and removing edges have recently emerged, there is still a lack of general and efficient methods, especially when considering the quality of the generated explanations. Moreover, the problem remains far from solved, as existing methods exhibit different strengths and weaknesses, often trading off between explanation size, coverage and quality. For this reason, it is important to identify where each method performs well and where it falls short, so as to guide future research in the field. Thus, our study compares six state-of-the-art (SOTA) models on a diverse set of real-world and synthetic datasets, covering both binary and multi-class graph and node classification tasks, and evaluates their performance using diverse quantitative and qualitative metrics.

---


### 144. [VoxelFix: Post-Hoc Semantic Correction of Completed 3D Voxel Maps](https://arxiv.org/abs/2609.05114)

**<font color=#1a73e8>作者：</font>** Sunesh Praveen Raja Sundarasami, Taehyoung Kim, Johannes Scherer 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic 3D maps are increasingly constructed automatically for aerial robotics by integrating learned semantic predictions into 3D representations. While this avoids costly manual 3D annotation, errors in the perception and mapping pipeline can persist in the resulting map, reducing its reliability for downstream autonomous tasks. Existing 3D semantic map refinement methods either rely on the original observations, treat occupancy as part of the prediction problem, or apply non-learned local regularization to completed maps. Instead, we study post-hoc semantic correction, asking whether semantic accuracy can be recovered directly from the completed map while keeping its geometry and occupancy fixed. We introduce \method, a graph-based model that corrects voxel labels based on local geometry and neighboring semantic information. To obtain training pairs, we corrupt contiguous regions of annotated OccuFly maps according to class confusions observed in upstream maps. We evaluate \method on completed OccuFly maps generated from predictions of four independently trained 2D segmentation models. \method consistently improves mIoU by 4.23--5.00 percentage points, with gains broadly distributed across the evaluated semantic classes and particularly strong improvements for tree, roof, and wall. Results on an independently reconstructed out-of-distribution aerial scene further suggest that the learned correction can transfer beyond the environments seen during training.

---


### 145. [Coarse-Graining Hidden Representations: Unsupervised Neuron Selection via Mapping Entropy](https://arxiv.org/abs/2609.05126)

**<font color=#1a73e8>作者：</font>** Margherita Mele, Andrea Castagna, Roberto Menichetti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Overparameterized neural networks carry far more hidden units than a task nominally requires, raising the question of which neurons are essential and whether that distinction is legible in the representation itself, without labels or gradients. We cast neuron selection as the problem of coarse-graining the hidden layer by retaining a subset of its neurons, and score each putative selection by the mapping entropy (ME). This quantity measures the loss of discriminatory power inherent in discarding part of the network neurons, and the selection that minimises the ME is taken as particularly informative. This criterion is fully unsupervised, in that it depends only on hidden-activation statistics. In teacher-student networks, ME optimisation recovers the minimal teacher-consistent representation and retains extra units in proportion to the hidden layer's residual variability; in a non-linear Gaussian process task, it selects coherent functional-class mappings whose preferred class shifts across training. On this task and on translation-augmented MNIST, ME-selected subnetworks outperform random subsets of equal size, most clearly under strong compression - linking configurational distinguishability to predictive performance.

---


### 146. [MomentQuant: an even more minimalist interval method with linear time complexity for time series classification](https://arxiv.org/abs/2609.05136)

**<font color=#1a73e8>作者：</font>** Johann Faouzi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series data is very common in many real-world applications and in numerous domains, with increasing interest for automated information extraction using machine learning. One of these subfields is time series classification, which consists in assigning a label to each new, unseen time series. Many algorithms have been developed over the past decades, with the trade-off between predictive performance and computational cost being consistently discussed. Quant, an interval-based algorithm extracting quantiles from recursive, fixed, dyadic intervals, was shown to achieve high accuracy, while being very fast. We propose two changes to make this algorithm even faster. The first one is a better optimized implementation of the exact same algorithm. The second one is to derive approximate quantiles, using the Cornish-Fisher expansion, instead of exact quantiles. This change removes the necessity to sort the time series, leading to a smaller computational complexity. We call this novel algorithm MomentQuant. We provide evidence that our implementation of Quant is faster than the original one, and that MomentQuant is even faster than our implementation of Quant, at the cost of a tiny decrease in predictive performance. These improvements are especially relevant for real-life applications, where inference is performed much more often than training.

---


### 147. [From 80x to 385x: A Best-Matching-Unit Search at the L2 Roof, Measured Against a Symmetrically Tuned Baseline](https://arxiv.org/abs/2609.05138)

**<font color=#1a73e8>作者：</font>** Andrew James Amos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Comparisons between GPU implementations are usually asymmetric: one side is tuned by its author, the other is run as found. I report a programme that tuned both a novel SOM algorithm (SparseBin) and the baseline algorithm it was being compared to (cuSPARSE). The best-matching-unit search that dominates self-organizing map training was tuned through four levers - tile size, tile-membership clustering, neuron-axis chunking and vectorised loads - reaching 5.6-10.1x per epoch over the previously published configuration at map sizes from 32x32 to 512x512, and lifting the margin over the CUDA implementation behind our earlier MEDLINE atlases from ~80x to ~385x. cuSPARSE, the implementation SparseBin is compared against, received every lever with an analogue on its side, and became 2-3x faster in the process. The tuned kernel pressed the L2 bandwidth roof at 77% of peak with every other unit at 40-65%, bounding any further lever at ~1.3x - a terminal result rather than a waypoint, and every untested lever was either capped by that bound by construction or measured null.

---


### 148. [SciDocBench: A Workflow-Centered Benchmark and Data Pipeline for Scientific Document Understanding](https://arxiv.org/abs/2609.05141)

**<font color=#1a73e8>作者：</font>** Shenxi Wu, Yuhong Liu, Haosong Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific papers require models to reason jointly over text, equations, figures, tables, code, and datasets while preserving the provenance of supporting evidence. Existing benchmarks typically evaluate these capabilities in isolation, leaving unclear whether multimodal models can support realistic scientific-reading workflows. We introduce SciDocBench, a workflow-centered benchmark for scientific document understanding. It contains 124 expert-authored and difficulty-screened questions organized into seven research-assistant capability groups and 19 subtasks across five scientific domains. Each question is instantiated under four matched conditions combining English or Chinese questions with all-images-first or interleaved document representations, yielding 496 evaluation instances for controlled analysis. The strongest evaluated system achieves only 62.6/100, with pronounced weaknesses in document perception, evidence grounding, verification, and cross-document reasoning. To translate these diagnostics into scalable training signals, we introduce SciDocIR, a typed evidence-graph representation that preserves scientific document objects, layout and cross-reference relations, and provenance. Building on SciDocIR, we construct SciDocDataset, comprising approximately 15K supervised fine-tuning samples and 8K reinforcement-learning samples across 14 verifiable subtasks. Together, SciDocBench, SciDocIR, and SciDocDataset form an evaluation-to-training framework for diagnosing and improving scientific-document assistants. The project page is available at this https URL.

---


### 149. [A Hybrid Predictive Ensemble of Machine Learning and Deep Neural Networks for Early Cardiovascular Disease Risk Assessment](https://arxiv.org/abs/2609.05146)

**<font color=#1a73e8>作者：</font>** Balaji Venkateswaran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study introduces an intelligent framework that integrates machine learning and deep neural network ensemble techniques for early detection and prognosis of cardiovascular diseases. The system utilizes real-time physiological data collected from Internet of Medical Things (IoMT) devices, including ECG sensors, heart rate monitors, and blood pressure trackers. To ensure the accuracy and reliability of input data, preprocessing steps such as noise reduction, normalization, and missing value imputation are employed. The most significant health indicators are identified through effective feature selection methods and then processed using optimized classifiers such as Support Vector Machines (SVM), Random Forests, and eXtreme Gradient Boosting (XGBoost), which are combined in an ensemble architecture to improve diagnostic precision. The framework demonstrates remarkable performance in predicting cardiovascular disease risk, achieving higher accuracy, reduced false positives, and enhanced consistency compared to conventional methods. It is designed on a cloud-based infrastructure that ensures scalability and real-time processing for continuous patient monitoring. Experimental evaluation on real-world cardiovascular datasets confirms the framework's efficiency in early-stage risk assessment and clinical decision support. The results highlight the potential of combining traditional machine learning and deep learning paradigms to achieve proactive healthcare management and improve patient outcomes.

---


### 150. [Beyond Stationarity in Time Series: Discovering Causal Structures and Latent Regimes via Markov Blankets](https://arxiv.org/abs/2609.05150)

**<font color=#1a73e8>作者：</font>** Lei Zan, Charles K. Assaad, Emilie Devijver 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces Regime-aware Constraint-Based and Noise-Based causal discovery with Markov Blankets (RCBNB-MB), a novel causal discovery algorithm for time series that relaxes the common assumption of a single, time-consistent causal structure. Time series are typically observed at discrete time points and often exhibit regime changes that challenge the assumption of a static causal structure, a limitation in many real-world dynamic systems. To address this challenge, RCBNB-MB identifies latent causal regimes, defined as subsets of time points within which a stable causal structure holds. The algorithm follows an iterative strategy that segments the time series into regimes and discovers the causal graph within each regime. By leveraging the Markov blanket rather than direct parents, RCBNB-MB gains robustness to errors in causal discovery and preserves predictive information. We provide theoretical guarantees for RCBNB-MB's ability to recover both regime transitions and causal graphs under reasonable assumptions. Furthermore, we validate its effectiveness through extensive experiments on simulated datasets with known ground truth and real-world IT monitoring data, where taking into account regime shifts is critical. Empirical results show that RCBNB-MB systematically outperforms baseline approaches in accurately detecting regime changes and their associated causal graphs, positioning it as a robust and versatile framework for non-stationary time series analysis.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-190](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
