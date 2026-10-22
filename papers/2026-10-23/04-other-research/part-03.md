# 📦 其他研究 | 2026年10月23日

> 本类共 **232** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-232](./part-05.md)

---

### 101. [Certified Abstention for Provably-Unidentifiable Index-Phase Recovery in Image Registration](https://arxiv.org/abs/2610.29272)

**<font color=#1a73e8>作者：</font>** Dinh Tuan Nguyen, Trong Nhan Nguyen, Vu Nguyen Minh Hung 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image registration underpins measurement across scanning, camera, and microscopy imaging, yet a fundamental question is rarely posed: when is the sample-to-position map recoverable at all, and when does any estimator that reports a position necessarily fabricate one? We show that in reference-perturbed sampled imaging, where samples are localized through a perturbed reference, position fidelity (where samples land) and phase fidelity (which reference index becomes each block's origin) are logically independent: no policy acting on position information alone can guarantee phase fidelity. We derive a tight resolution threshold separating recoverable from provably-unidentifiable registration, and a recovery framework that certifies identifiable regions--recovering them exactly--while abstaining on provably-unidentifiable regions rather than hallucinating structure. On a deployed scanning system we measure a direction-bimodal registration offset consistent with the theory. Against classical and learned restoration baselines, certificate-free offset estimators fabricate structure on the unidentifiable regime, whereas the certified method abstains rather than fabricating. Finally, the certified-abstention mechanism carries across scanning, rolling-shutter, and cryo-electron-microscopy imaging--declining rather than fabricating on the regime it flags--though how completely it abstains and how tightly it bounds kept-region risk stay modality-specific (at extreme SNR the cryo-EM certificate abstains only partially): a structural-versus-statistical boundary in registration reliability.

---


### 102. [Latent space configuration for neural network finetuning, fast ranking, and embedding dimensionality reduction](https://arxiv.org/abs/2610.29295)

**<font color=#1a73e8>作者：</font>** Nikita Gabdullin, Anton Raskovalov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Finding K most similar elements for a query in a large gallery of neural network (NN) embeddings is essential in various areas of computer science and industrial applications of artificial intelligence. This paper proposes search algorithms for structured latent spaces (LS) of NNs which allow to speed up top K item retrieval owing to O(1) complexity small candidate gallery subset search. ArcFace-pretrained IResNet50 models are finetuned using Latent Space Configuration (LSC) methodology to obtain new distribution of embeddings with desired geometric properties. Applying the proposed algorithms to embeddings obtained from finetuned models leads to several times speed-up over baseline exhaustive search. Specifically, we report up to 3 times speed-up on GPU and 40% speed-up on CPU compared to the baseline method GPU speed. These results are obtained for the original and reduced numbers of LS dimensions. The results show that LS dimensionality reduction allows to further accelerate the search and even improve rank-N metrics.

---


### 103. [Interpretable Cutting Plane Selection for Mixed-Integer Linear Programming Using Genetic Programming](https://arxiv.org/abs/2610.29311)

**<font color=#1a73e8>作者：</font>** Gwen maudet, Mathis Da Cunha, Grégoire Danoy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cutting planes (cuts) remove fractional solutions from mixed-integer linear programs (MILPs) without excluding any feasible integer solutions, making them a key ingredient in modern MILP solvers. Current state-of-the-art solvers rely on fine-tuned handcrafted cut strategies, which, despite their effectiveness, remain inherently static and can be suboptimal. More recently, learning-based approaches have been proposed to design adaptive cut strategies; however, most of these methods are based on neural networks, offering limited interpretability and providing no guarantees of convergence. In this paper, we propose \emph{Genetic Programming and Statistics-based Cut Selection} (GPSCS), the first learning-based framework that explicitly generalizes handcrafted cut selection heuristics into a fully interpretable policy. First, a genetic programming model evolves a symbolic scoring function that ranks candidate cuts using features derived from the cuts and the solving context. Second, a lightweight statistics-based mechanism adaptively determines the number of top-ranked cuts to add at each separation round by detecting significant score dropouts. We evaluate GPSCS within the SCIP solver on seven classes of synthetic and real-world benchmark instances, with a strong emphasis on generalization: evaluation instances are on average 41 times harder than those used for training. Experimental results show that GPSCS improves average solving time by $6\%$ compared to SCIP's default cut selection strategy and achieves a two-fold speedup over both a recent neural-network-based approach and a no-cut baseline, demonstrating strong robustness and generalization across heterogeneous MILP families.

---


### 104. [DISRL: Dual-Scale Incremental Semi-Supervised Reinforcement Learning for Dynamic Community Tracking](https://arxiv.org/abs/2610.29315)

**<font color=#1a73e8>作者：</font>** Tianming Zhang, Jinxu Wang, Yixuan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic local community detection tracks the evolving community of designated seed nodes across graph snapshots. However, it faces two critical challenges: temporal supervision uncertainty, where sparse and outdated labels fail to provide seed-specific guidance under topology changes, and unbounded error cascades, where sequential policy transfer accumulates exploration errors over long horizons. To address these challenges, we propose DISRL, a Dual-scale Incremental Semi-supervised Reinforcement Learning framework. DISRL introduces a supervision construction module that dynamically generates seed-specific guidance from sparse known communities, and a dual-scale community exploration module that stabilizes policy evolution by decoupling short-term adaptation within temporal windows from long-term parameter consolidation across windows. Furthermore, we construct a dynamic graph benchmark with diverse community evolution scenarios. Extensive experiments demonstrate that DISRL consistently outperforms state-of-the-art baselines under various dynamic settings.

---


### 105. [SpatialBrain: Spatial Intelligence Growing from Experience](https://arxiv.org/abs/2610.29317)

**<font color=#1a73e8>作者：</font>** Yifan Zhou, Ziyang Gong, Xiaojun Ye 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning requires more than access to geometric tools: a reasoner must decide when direct observation is sufficient and when to reconstruct, measure, or change reference frames. We present SpatialBrain, a framework that retains experience about these decisions while keeping its vision-language backbone fixed. The key distinction is between evidence about a scene and experience about how to reason with that evidence. 3DFusionMemory fuses current-scene observations into queryable spatial relations. A Spatial Skill Library provides reusable tool procedures, and Spatial Cognition associates task conditions with experience about when and how to use memory and skills. Completed trajectories are abstracted into process records and consolidated between task blocks, allowing later decisions to draw on earlier execution without transferring scene coordinates or reference answers. Across five spatial-reasoning benchmarks, SpatialBrain improves on direct answers from the same backbone on four and ties on the fifth. Component comparisons, experience-coverage curves, and traced resource decisions characterize how the framework accumulates and uses these resources.

---


### 106. [OpenMAP-HIE: Pathology Informed Score-based Diffusion Model for Unsupervised Neonatal Hypoxic-Ischemic Encephalopathy Lesion Segmentation](https://arxiv.org/abs/2610.29322)

**<font color=#1a73e8>作者：</font>** Pengyu Kan, Craig Jones, Kenichi Oishi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate localization of neonatal hypoxic--ischemic encephalopathy (HIE) lesions on apparent diffusion coefficient (ADC) images is clinically important but is limited by scarce expert annotations and substantial variation in lesion appearance. We propose OpenMAP-HIE, a pathology-informed score-based diffusion model for unsupervised HIE lesion localization without voxel-wise lesion supervision. A denoising diffusion model learns the healthy neonatal ADC distribution, while a ControlNet-based conditional branch preserves patient-specific anatomy. At inference, anomaly evidence is derived directly from differences between conditional and unconditioned noise predictions at independently evaluated diffusion noise levels, avoiding dependence on a final pseudo-healthy reconstruction or sequential reverse-diffusion chain. Based on the characteristic ADC reduction associated with acute HIE, only discrepancies consistent with the expected pathological direction are retained and aggregated across noise levels using a geometric mean. Spatial mean filtering further suppresses isolated responses. The framework was evaluated on the BONBID-HIE dataset. The ADC-only method achieved a Dice score of $0.283\pm0.244$, average precision of $0.505$, Hausdorff distance of $25.45\pm15.63$ mm, mean average surface distance of $9.40\pm8.49$ mm, and normalized surface distance of $0.355\pm0.236$, providing the best overlap and surface-distance performance among the evaluated unsupervised methods and Dice performance comparable to supervised ADC-only models. Optional population-derived ADC $Z$-map refinement further increased Dice to $0.602\pm0.269$. These findings support pathology-informed score discrepancies as a useful signal for neonatal HIE lesion localization, while highlighting remaining challenges in detecting small and low-contrast lesions.

---


### 107. [OACap: Caption-Guided Active Observation for Detailed Video Captioning](https://arxiv.org/abs/2610.29327)

**<font color=#1a73e8>作者：</font>** Hao Shi, Hong Yan, Xiaoyang Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unlike question answering, where a query specifies a perceptual target, open-ended detailed captioning must determine what evidence to acquire and how to integrate it into a coherent global description. We propose Observation-Adaptive Video Captioner (OACap), a caption-centered agent that turns unsupported or missing information into targeted observation requests, uses spatiotemporal tools to acquire evidence, and iteratively verifies and revises the caption. OACap captions consistently improve performance across general video-understanding benchmarks using a fixed text-only reader. To better diagnose the information they preserve, we introduce Factual-Semantic Captioning Bench (FSCap-Bench). Its Core-Support Factuality Score (CSFS) combines claim precision with importance-aware fact coverage and responds as expected to four controlled perturbation types on 93.0-98.3% of valid caption pairs. Its Cross-Modal Semantic Round-Trip Score (CSRS) measures semantic preservation through a video-caption-video-caption round trip by matching atomic facts from source and recovered captions. Together, they connect downstream textual-memory utility with factual and semantic preservation.

---


### 108. [Policy Central: Detecting Conflicts, Redundancy, and Similarity in Deployed Police Policy](https://arxiv.org/abs/2610.29338)

**<font color=#1a73e8>作者：</font>** Holly Baker, Michael Kuo, Kyana Pollas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Policy Central is a deployed system that helps police departments find relationships between sections of their written policy: whether two sections conflict, are redundant, are merely similar, or are different. We describe the system and compare two architectures. Retrieve-Judge, a retrieve-then-classify pipeline, runs as a cheap library-wide health signal; Screen-Confirm, a screen-then-confirm cascade, is a selective audit of the documents a reviewer chooses, checking them exhaustively against one another. On a 302-pair benchmark drawn from one department's ~84 real policy documents, given each pair Screen-Confirm reaches 0.795 aggregate recall and 0.885 on Conflict, so current models judge well. Finding the pair is the hard part: Retrieve-Judge's composed recall falls to 0.457, and Screen-Confirm recovers 0.472 (0.615 on Conflict). Today these pairs are found by reading the whole library, nearly 20,000 sections, checked against one another and re-checked after every revision. A scan that returns half of them in minutes, at low cost, and can be re-run on demand changes the economics of policy review even before recall improves.

---


### 109. [ChronoSynth: Constraint-Aware Question Synthesis over Temporal Knowledge Graphs](https://arxiv.org/abs/2610.29339)

**<font color=#1a73e8>作者：</font>** Feng Liang, Weixin Zeng, Runhao Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge graph question generation (KGQG) generates natural-language questions from structured graph evidence and a target answer. When the input graph is temporal, a valid question must also preserve the answer field, time condition, reference event, and temporal order that determine the answer set. Existing KGQG methods and prompting baselines can produce fluent questions that alter these conditions, causing temporal semantic drift. This paper studies temporal KGQG as a constraint-preserving graph-to-question problem and proposes ChronoSynth, a memory-augmented and constraint-aware generation framework. ChronoSynth first constructs a Temporal Intent State to make the intended question semantics explicit. It then retrieves compatible typed question patterns from an indexed pattern memory, adapts them to the input graph, and validates the generated question. Validation feedback guides revisions when a supported inconsistency is detected. Experiments on CRONQUESTIONS and MultiTQ demonstrate state-of-the-art generation performance, with ablations supporting the contributions of its components.

---


### 110. [Reader--Writer Coupling in Transformer MLPs](https://arxiv.org/abs/2610.29340)

**<font color=#1a73e8>作者：</font>** Giyeong Oh, Sunghee Ahn, Youngjae Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A transformer MLP gives each hidden channel two roles: a reader that decides when the channel responds, and a writer that decides what it adds back to the residual stream. Read as a key--value memory, the layer can be measured one factor set at a time: the pairing of readers to writers is carried only by their shared index, invisible to any quantity computed from one factor set alone. Yet training couples the two factors through their joint update, so we ask what reading them together shows. The block supplies the joint instrument: the MLP writes back into the very stream it reads, so the exact Jacobian of its update is square, and its agreement with its own transpose resolves into reader--writer terms whose inner products give each channel, read as a couple, a signed pairing coordinate. Ranked by this coordinate, each block we measure has a small core of strongly coupled channels; where initialization gives either sign equally, the core is nearly all opposed: each writer points against the direction its reader responds to. This opposed core recurs from the smallest models trained from scratch to released checkpoints; its sign is in place within a few percent of training and holds while the coupling grows. Read as couples, most channels return their contribution against the reader that fired it, and the readers of later blocks take it up; few show in the logits. Training holds the couples in place: flipping the opposed writers moves the output toward common tokens, and a writer permuted onto another reader regrows to fit that reader while the reader stays.

---


### 111. [MASAR: Multi-stage Attack Surface Analysis and Reasoning Framework for Telecom Networks](https://arxiv.org/abs/2610.29343)

**<font color=#1a73e8>作者：</font>** Heba Osama, Wessam DeifAllah, Ahmed Saafan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing complexity of modern telecommunications networks introduces security challenges that require systematic threat analysis. However, a gap remains between architectural threat modeling frameworks, such as Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege (STRIDE), and operational knowledge bases, such as the MITRE Five-G Hierarchy of Threats (FiGHT). This gap limits the ability to connect architectural weaknesses with specific protocol behaviors and attack sequences. This paper presents Multi-stage Attack Surface Analysis and Reasoning (MASAR), a formal framework that bridges this gap through three layers: strategic threat mapping, logical attack path decomposition using directed acyclic graphs (DAGs), and operational synthesis of tactics, techniques, and procedures (TTPs). MASAR is evaluated using a 5G-ready IP Multimedia Subsystem (IMS) architecture, examining two signaling attack scenarios: early media billing bypass through Session Initiation Protocol (SIP) signaling and subscriber information disclosure and topology discovery through the Diameter Cx interface. MiniZinc constraint models are used to analyze the reachability of unsafe protocol states. The analysis demonstrates how MASAR connects architectural threats with specific protocol behaviors and supports security controls that account for network states in telecommunications systems.

---


### 112. [Don't Stop Long-Context Continual Pre-Training Too Early: An Empirical Scaling Law](https://arxiv.org/abs/2610.29352)

**<font color=#1a73e8>作者：</font>** Ziqing Qiao, Xiaoyue Xu, Sikui Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context continual pre-training (LCCP) is widely used to improve long-context capability, but how its benefits scale with the number of tokens used for LCCP remains unclear. We investigate this question through modeling, monitoring, and validating the benefits of scaling LCCP. First, we establish an empirical additive power law relating long-context performance to model size and the respective token budgets of short-context pre-training and LCCP. Experiments across five model scales and more than one hundred short- and long-context budget configurations show that the fitted law reproduces the observed trends and extrapolates well to held-out model scales. Second, we introduce \textsc{Constant-Last4}, a training and observation protocol that averages the four most recent consecutive checkpoints from a constant-learning-rate run to enable stable monitoring along a single extensible training trajectory. Under this protocol, the same scaling-law form fits well and accurately predicts the LCCP performance trajectory of a 1.22B-parameter model trained on approximately 100B LCCP tokens. Finally, downstream evaluations along this trajectory show continued improvements in long-context performance, with no clear sign of saturation within the evaluated range. These gains persist after both 128K context extension and supervised fine-tuning, with benefits extending to long-context understanding and agentic tasks. Together, these results argue for continuing to scale LCCP rather than stopping early: its gains are stably observable along an extensible trajectory, quantitatively predictable, and transferable to downstream tasks.

---


### 113. [Seeing through Denoising: Frequency-guided One-step Denoising for Infrared Small Target Detection](https://arxiv.org/abs/2610.29361)

**<font color=#1a73e8>作者：</font>** Xuelin Qian, Zixuan Wang, Chang Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared small target detection (IRSTD) is a challenging task due to the extremely small size of targets, low signal-to-noise ratios, and heavy background clutter in infrared imagery. While the progress of deep learning has advanced this field, existing methods primarily adopt discriminative paradigms that directly map images to target masks, overlooking the potential of generative modeling. In this paper, we propose DiffIRSTD, a novel generative framework that reformulates infrared small target detection as a background reconstruction problem. Instead of explicitly predicting target regions, we reinterpret small targets as noise-like signals and leverage a diffusion-based model to recover a clean, target-free background from a perturbed input image. The residual between the reconstructed background and the original image is then exploited to highlight candidate target regions, providing explicit cues for subsequent detection. To address the computational cost typically associated with diffusion sampling, we introduce a one-step denoising strategy that enables efficient background reconstruction while maintaining practical inference speed. Furthermore, we present a frequency-guided perception loss to preserve high-frequency background details and focus more on the reconstruction quality of target regions. More importantly, our DiffIRSTD operates as a plug-and-play framework, compatible with existing IRSTD models without increasing the computational complexity of detectors. Extensive experiments on IRSTD-1K, NUAA-SIRST, and NUDT-SIRST datasets demonstrate the superiority of our method, achieving state-of-the-art performance across three benchmarks.

---


### 114. [Compositional neural networks for multimodal X-ray and neutron scattering inversion](https://arxiv.org/abs/2610.29362)

**<font color=#1a73e8>作者：</font>** Valentin Munteanu, Alexander Hinderhofer, Dmitry Lapkin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> X-ray and neutron scattering are indispensable for structural characterization across condensed-matter physics and materials science. Yet, because scattering experiments generally record intensities without phase information, distinct structures can yield similar scattering patterns, rendering the corresponding inverse problems non-unique. This ambiguity can be reduced by combining complementary measurements, but their integration into machine-learning frameworks remains challenging. Here we introduce a modular framework for probabilistic multi-measurement analysis based on prior-amortized flow matching. Single-observation posterior estimators are trained separately for individual observation types or physical probes and combined only at inference time through a compositional sampler. This late fusion approach allows pretrained single-observation models to be reused without dedicated joint retraining. As a case in point, we consider reflectometry, which provides depth-resolved, nanometer-scale information about thin films and interfaces. Our single-observation demonstrations span X-ray, time-of-flight neutron and polarized neutron reflectometry. In separate co-refinement studies, task-matched estimators enable homogeneous composition across multiple neutron contrasts and heterogeneous multimodal composition of X-ray and neutron measurements. Together, these results establish compositional flow matching as a modular approach to uncertainty-aware inversion and co-refinement, with potential applicability to other scattering problems in which multiple observations constrain a common physical structure while retaining measurement-specific parameters.

---


### 115. [AOV-GS: Active Open-Vocabulary Semantic Mapping with 3D Gaussian Splatting](https://arxiv.org/abs/2610.29374)

**<font color=#1a73e8>作者：</font>** Rodion Shkokov, Tatiana Zemskova, Dmitry Yudin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robots deployed in human-centered environments need maps that support both geometric navigation and open-vocabulary semantic queries beyond a fixed label set. A key challenge is enriching such maps with semantic information without relying on manually annotated segmentation masks or closed-set semantic categories. Existing geometry-driven active mapping maximizes coverage but treats semantics as a passive by-product of the collected trajectory, whereas active semantic mapping typically depends on supervised semantic segmentation. We present AOV-GS, an active 3D Gaussian mapping system that guides exploration using frozen foundation models. During coarse exploration, AOV-GS re-ranks geometrically promising candidate views according to CLIP mask-embedding novelty computed from SAM instance segmentation, biasing exploration toward semantically informative regions. Frozen SAM and CLIP provide instance masks and language-aligned embeddings throughout mapping, while a lightweight scene-specific language field is fitted offline directly to the collected CLIP embeddings rather than manually annotated masks, enabling open-vocabulary text-query segmentation on novel views. In a controlled comparison using the same SAM-CLIP perception stack, AOV-GS improves average language-field mIoU over geometry-only active planning by 1.3 percentage points on Replica (34.6% on eight scenes) and by 1.8 points on Matterport3D (23.1% on five scenes). With CorrCLIP, AOV-GS reaches 35.6% on Replica, 2.0 points above the matched Geometry-based + CorrCLIP baseline. Novel-view PSNR remains comparable to the geometry-only baseline on both datasets while depth L1 improves on Replica. Code is available at this https URL.

---


### 116. [AdvFidelity: Unifying Preference Alignment and Few-Step Image Generation within Reinforcement Learning](https://arxiv.org/abs/2610.29380)

**<font color=#1a73e8>作者：</font>** Sicong Kang, Fangao Zeng, Yuhan Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Practical image generation requires both human preference alignment and few-step efficiency, yet combining reinforcement learning (RL) with distillation is often multi-stage and may erode RL gains We observe that few-step RL progressively improves structural coherence, even with specialized rewards, but leaves low-level artifacts that these rewards may fail to penalize. To address this gap, we propose AdvFidelity, which integrates artifact-sensitive fidelity supervision into RL through an online adversarial reward. This enables joint reward alignment and high-fidelity few-step generation within a single RL stage, without distribution matching distillation (DMD) or other explicit distillation objectives. We train a discriminator to rank high-quality references (positives) above content-matched reconstructions (negatives) produced by the current generator. Reconstructing moderately noised references largely preserves style and scene layout while exposing low-level degradations. This encourages the discriminator to assess artifacts rather than content differences. With negatives reconstructed online, alternating updates adapt fidelity supervision to the generator's evolving failure modes. References can come from existing target-domain data or full-step model samples. Built on LeapAlign, AdvFidelity backpropagates gradients from both rewards through the few-step sampling trajectories used at inference. Across two model backbones and three task settings, AdvFidelity matches full-step LeapAlign in alignment, task performance, and overall generation quality and remains highly competitive with other evaluated full-step RL methods, using only 4 or 8 steps without CFG.

---


### 117. [Cascading Bandits with Noisy Observations: Algorithms and Regret Bounds](https://arxiv.org/abs/2610.29381)

**<font color=#1a73e8>作者：</font>** Yashaswini Kaluguri, Nikhil Karamchandani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a novel stochastic cascading bandit setup where probing an ordered shortlist of $K$ out of $L$ arms incurs position-dependent costs, and the learner observes only noisy feedback regarding each arm's true output. We identify a sub-class of noise models for which the optimal shortlist can be found by sorting arms according to a per-arm score: such a score exists for both selection and ordering when the channel has no false positives, and for ordering alone (but not selection) when measurements are costless; however in general neither selection nor ordering is separable once noise and cost are both present. For the case where both selection and ordering scores exist, we provide a UCB-based algorithm with $O((L-K)\log T)$ instance-dependent regret over a time horizon $T$, which matches an algorithm-agnostic lower bound (up to constant factors). For the more challenging scenario where scores don't exist, we develop a new algorithmic template, DP-UCB, that embeds optimism directly inside an exact dynamic program, yielding $O\big(LK\log T\big)$ regret. Finally, we validate our theoretical results through extensive numerical evaluations and simulations over both synthetic and real-world datasets.

---


### 118. [FM-Occ: Feature-Diverse Upsampling and Memory-Aware Decoding for 3D Occupancy Prediction](https://arxiv.org/abs/2610.29388)

**<font color=#1a73e8>作者：</font>** Yujia Zhai, Guoming Huang, Zhuanghuai Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D semantic occupancy prediction estimates voxel-wise occupancy and semantic labels throughout a scene. Our experiments reveal that conventional sparse transposed-convolution upsampling yields poorly differentiated voxel responses and that successive decoder layers discard previously correct semantic predictions. To address these issues, we present Feature-Diverse Upsampling and Memory-Aware Decoding for 3D Occupancy Prediction (FM-Occ), comprising two components. First, 3D Sparse Subvoxel Shuffle (3S) mitigates feature homogenization by constructing candidate child features in the channel dimension, jointly transforming and normalizing them, and then rearranging them onto a finer sparse grid with explicit feature-coordinate correspondence. Second, Entropy-Regulated Layer-wise Memory (ER-LM) retains semantic information across decoder layers by maintaining a layer-wise memory for each query through gated recurrent updates and using prediction entropy to regulate the historical information propagated to the next layer. During training, a class-weighted entropy loss Lcwe provides label-guided regularization for matched semantic queries. On SemanticKITTI, 3S increases the spatial coefficient of variation of normalized voxel-wise root-mean-square (RMS) responses from 0.41% to 4.03%, while ER-LM reduces semantic degradation and improves error correction across decoder layers. The combined FM-Occ improves mIoU from 12.16% to 12.73% with negligible memory overhead. ER-LM further improves mIoU in the BEV-based DISC framework from 16.78% to 17.17%, supporting its applicability across 3D voxel-based and BEV-based architectures.

---


### 119. [Progressive Permutation Alignment with Temperature-Controlled Spectral Sharpening](https://arxiv.org/abs/2610.29396)

**<font color=#1a73e8>作者：</font>** Yuta Horioka, Naoya Chiba, Yuki Uranishi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In implicit neural representations (INRs), 3D signals are encoded directly in network weights, making stable weight-space operations essential. However, permutation symmetry causes independently trained yet functionally equivalent models to appear distant in weight space, often inducing large loss barriers under linear interpolation. Existing neuron alignment methods either commit early to discrete matches and become trapped in inconsistent local optima or rely on computationally expensive gradient optimization over continuous relaxations, both of which are unreliable in challenging cases such as NeRF. We adopt progressive alignment, a layer-wise strategy that follows inter-layer dependencies from input to output. At each layer, a correlation matrix is estimated and aligned with a discrete anchor obtained by the Hungarian algorithm, after which temperature-controlled spectral annealing gradually sharpens the correlation structure toward a permutation matrix. This update is deterministic and lightweight, avoiding the inner-loop gradient optimization required by continuous relaxation methods. A final refinement stage further optimizes the network layer-by-layer via weight matching, starting from the aligned solution. Experiments on MLPs, CNNs, and Neural Radiance Fields (NeRFs) show that the proposed method reliably recovers neuron correspondences and achieves stable alignment across architectures. In practical experiments aligning independently trained NeRF models, our method reduces the loss barriers under weight interpolation compared with existing approaches.

---


### 120. [Region-Aware Multi-View Inspection Using Deep Learning and Domain-Informed Decision Fusion](https://arxiv.org/abs/2610.29398)

**<font color=#1a73e8>作者：</font>** Srivishnu Ethirajulu Krishnaraj, Rishikesh R. Chopade  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated optical inspection of precision components with tiny surface defects remains challenging when different regions of the same component exhibit different defect characteristics and, therefore, different acceptance criteria. This paper presents a region-aware, dual-model inspection framework that combines instance segmentation of localized seat-region defects with image-level classification of global shaft-region anomalies. Rather than treating these two model detections as sufficient evidence for component rejection, a deterministic decision fusion layer that formalizes industrial Standard Operating Procedures is applied to the model outputs to make the final component level decision. A PLC-synchronized imaging system acquires 18 seat and 18 shaft images over a full 360-degree rotation to provide multi-view circumferential coverage. The framework was evaluated on 380 automotive fuel injector needles, covering representative operational defect types, using identical model predictions in all configurations. Direct model-output aggregation via simple union logic (where any single-view detection flags a rejection) identified all 104 non-conforming components but produced a component level false rejection rate of 57.6%. Inclusion of a complete decision layer maintained the observed non-conforming (NOK) recall of 100% while reducing the false rejection rate to 10.9%, corresponding to an 81.1% reduction in false-positive component decisions. The results demonstrate that formalized manufacturing acceptance criteria can complement sensitive visual models by translating frame-level detections into practical and traceable component-level decisions.

---


### 121. [LiveAct: Towards Real-Time Multi-Agent World Models with Heterogeneous Action Interfaces](https://arxiv.org/abs/2610.29408)

**<font color=#1a73e8>作者：</font>** Xinyu Wang, Huafeng Shi, Yue Ma 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive video world models predict how an environment evolves under user actions, but most existing systems assume one controlled agent and one task-specific action interface. We study multi-agent video world modeling, where one model generates a joint visual future for multiple controlled agents while interpreting heterogeneous controls ranging from binary game buttons to continuous robot commands. This task presents two complementary challenges. First, every agent-indexed action stream must control its intended visual entity independently. Second, the model must adapt the meaning of each control variable across different tasks, where the same tensor dimension may denote an attack, steering command, or robot command. We introduce LiveAct, centered on a Heterogeneous Action Interface (HAI) whose two components mirror this decomposition. To support independent control, Agent-Aware Spatial Modulation uses language-driven spatial gates and agent-specific attention to bind each action stream to its intended visual agent. To accommodate heterogeneous controls, Schema-Guided Action Adaptation describes each control variable in language and modulates its semantic token with the synchronized numerical value. We further transfer the complete interface to a blockwise causal generator through teacher forcing and rollout-aware distribution matching, enabling efficient streaming generation while retaining agent-specific control and action semantics. We instantiate the formulation on six multi-agent sources spanning games and multi-robot manipulation, and evaluate visual quality, action following, agent attribution, and latency. Across games and robot manipulation, LiveAct reaches 0.898 and 0.942 agent-attribution accuracy without agent locations or identity crops, and the causal generator attains 17.70 FPS at $512\times 448$.

---


### 122. [The Predictive--Optimization Gap in GuanDan Self-Play](https://arxiv.org/abs/2610.29411)

**<font color=#1a73e8>作者：</font>** Qicheng Zou, Biao Yuan, Siyu Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Outcome-predictive signals are often treated as promising optimization targets in reinforcement learning, but predictive validity and optimization utility are different claims. We expose this distinction in GuanDan, a multi-round imperfect-information game in which the implication of a round outcome depends on the public match state. Held-out analysis shows that state--gain interactions provide incremental predictive value beyond a constant signed-gain effect, establishing that match progress is predictively meaningful. We then use changes in a frozen match-win predictor, $\Delta\Phi$, as a controlled round-level supervision intervention in a matched DanZero-style Monte Carlo self-play protocol. The intervention can succeed in an individual lineage: a selected progress-augmented checkpoint substantially outperforms its matched Baseline on a locked evaluation. Yet the method-level result reverses this impression: none of five preregistered replication seeds is positive, the pooled ten-seed interval includes zero, and across-iteration effects repeatedly change sign without a common late-stage advantage. These results identify a predictive--optimization gap: under the studied learner, a signal can describe outcome-relevant progress while failing to provide a reliably beneficial optimization direction.

---


### 123. [Beyond Small Talk: Modeling Disclosure Trajectories in Human-AI Conversation](https://arxiv.org/abs/2610.29413)

**<font color=#1a73e8>作者：</font>** Keith Kwok, Wanting Ning, Tej Deep Pala 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recently, we see a rise in conversational agents as a form of social and emotional support, where disclosure will unfold over time. Yet, current evaluations of these agents typically examine isolated conversational states. In analyses of naturally occurring conversations, disclosure history and current disclosure are confounded which tends to make their effects difficult to isolate. We thus introduce Trajectory-based Disclosure Evaluation (TraDE), an evaluation framework grounded in Social Penetration Theory that utilizes predefined disclosure trajectories and evaluates how preceding disclosure history shapes model behavior under matched current disclosure. Through the use of TraDE, we demonstrate across multiple models and relational behavior benchmarks that responses to disclosures matched on depth can differ depending on the preceding trajectory, particularly in whether models accept or challenge the user's framing. We also observed that these differences track accumulated exposure to deeper disclosure rather than any single moment of vulnerability or the order of disclosures. It also tends to persists for several turns after disclosure returns to shallow levels. For several behaviors, we also demonstrate that models diverge most consistently from human supporters in the Emotional Support Conversation corpus (ESConv) not when users open up but rather when they step back in their disclosure. TraDE thus provides a systematic way to expose history-dependent relational behavior that evaluations of isolated conversational states would otherwise miss.

---


### 124. [Solving Go under Positional Superko: Sound Proof Transfer and New Board Values](https://arxiv.org/abs/2610.29414)

**<font color=#1a73e8>作者：</font>** Sami Kharma, Florian Schintke  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Positional superko (PSK) forbids recreating any earlier whole-board position. It is part of the Chinese rules as written and of the rules used in computer Go. Yet almost all solved Go boards were computed under a simpler basic-ko rule set. PSK makes solving hard: legality depends on the whole game history, and this breaks the three tools that make solving tractable, namely transposition tables (the graph-history interaction problem), static life-and-death recognition, and safe move pruning. We present Sanko, a parallel depth-first proof-number solver that restores all three soundly. Its core is a cheap proof-transfer theorem: a stored proof stays valid on a new path unless a board that the proof's winner must create has already occurred. Sanko proves 5x5 Go in 16 minutes with six threads, where the previous state of the art needed 5.25 hours with six processes, and in about a minute and a half on one 192-thread machine. It also establishes the first PSK values of twenty-three further boards, eleven of which were unsolved under any rules. Superko changes game-theoretic values: 4x7, a full-board win under basic ko, is worth only 12 points under PSK, and we pinpoint the move at which the previously published optimal line fails. Unlike earlier solutions of empty Go boards, we release the solver source together with the command line and outcome of every run behind our values and measurements, so that all reported values can be reproduced.

---


### 125. [CCG Diffusion: Combinatory Categorial Grammar-Driven Compositional and Syntactically Disambiguated Text-to-Image Generation](https://arxiv.org/abs/2610.29415)

**<font color=#1a73e8>作者：</font>** Ryosuke Yamaki, Daichi Mochihashi, Nobutaka Shimada 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image generation models do not explicitly receive the syntactic structure of the prompt, i.e., which word modifies which and where each phrase attaches. Consequently, they often struggle to bind attributes to the correct objects, to depict spatial relations and counts correctly, and to render syntactically ambiguous prompts in the intended interpretation. Existing syntax-based control methods mainly address attribute binding and have limited ability to control spatial relations and counts or to specify the interpretation of syntactically ambiguous prompts. They rely on phrase-structure or dependency grammars and require additional rules or constraints on the tree structure to extract modification relations between words or to specify a syntactic interpretation. We propose CCG Diffusion, a training-free method that controls image generation using Combinatory Categorial Grammar (CCG). In CCG, the category of each word carries rich syntactic information: it specifies what the word combines with and what phrase it forms. Modification relations between words can therefore be read directly from a CCG parse. Moreover, prepositional phrase (PP) attachment ambiguity, a representative syntactic ambiguity, can be resolved simply by fixing the preposition's category. CCG Diffusion applies the same two CCG-based mechanisms, prompt rewriting and attention guidance, both to controlling attribute binding, spatial relations, and counts and to resolving PP ambiguity. On two architecturally different backbones, Stable Diffusion and Sana, CCG Diffusion achieves the highest scores among the compared methods in attribute binding and 2D spatial relations and significantly outperforms all of them in PP ambiguity resolution.

---


### 126. [Alternative Strategies for Active Learning with Bayesian Bradley Terry Model](https://arxiv.org/abs/2610.29416)

**<font color=#1a73e8>作者：</font>** Saman Jayasinghe, Sean Walton, Alma Rahat 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Comparative judgement uses pairwise comparisons to rank items, but recovering accurate rankings from a limited number of judgements depends on both the inference method and the pairs selected. We developed a Bayesian Bradley-Terry model (BBTM) that uses Polya-Gamma data augmentation for efficient Gibbs sampling and quantifies uncertainty in latent abilities and ranks. We propose three active learning strategies based on the knowledge gradient (KG) principle. We define our acquisition functions using Kendall's tau distance, posterior rank entropy, and posterior separation. Approximate one-step updates to posterior moments reduce the computational cost of evaluating candidate pairs. We also introduce Posterior Separation Reliability (PSR), which measures the spread of posterior mean abilities relative to posterior uncertainty. It provides an internal indicator of ranking reliability without requiring a reference ranking. In synthetic experiments covering different item counts, comparison budgets, and noise levels, BBTM generally recovers ranking more accurately than preference-based Bayesian comparative judgement (PBCJ). At low to moderate noise levels, the pairwise entropy pair selection strategy performs best in ranking recovery. However, at the highest noise levels, the KG strategy based on posterior separation produces better point rankings. PSR increases alongside improvements in ranking accuracy as comparisons accumulate. Robustness experiments identify the proportion of informative outcomes needed to meet specified accuracy targets within a fixed comparison budget. In a moderate noise setting, replacing 30\% of outcomes with random choices has little effect on ranking performance. These findings demonstrate the value of Bayesian inference and active learning pair selection for recovering ranks from limited, noisy paired comparisons.

---


### 127. [A KAN-based Non-linear Factorization for Embedding Layer Compression](https://arxiv.org/abs/2610.29424)

**<font color=#1a73e8>作者：</font>** Oliver Giudice, Anna Russo Russo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Among existing embedding compression approaches, low-rank factorization provides a simple and mathematically principled solution by approximating the embedding matrix with a reduced-rank decomposition. However, its practical effectiveness is often limited, as the resulting linear bottleneck constrains representational capacity. To overcome these limitations, we propose an enhanced factorization scheme that increases expressive power by introducing learnable non-linear projections within the compressed embedding layer. Our method is inspired by the Kolmogorov Arnold Networks (KAN) paradigm, which replaces fixed linear transformations with learnable univariate functions. Despite promising results in other domains, applications of KANs in NLP remain scarce and have so far been largely limited to final or task specific layers, rather than core representational components such as embedding layers.
We evaluate the proposed approach by integrating the compressed embedding layer into the Skip-gram framework and comparing it against a standard low-rank baseline under matched parameter budgets on the Word Analogy and Semantic Similarity benchmarks. We further introduce an effective initialization strategy from a pre-trained, uncompressed embedding layer. The behavior of the model is analyzed both immediately after initialization and after a brief post-initialization refinement phase, considering training with the standard Skip-gram objective as well as variants augmented with distillation from the original embedding layer. Overall, our results show that augmenting low-rank factorization with learnable non-linear projections effectively mitigates the limitations of linear bottlenecks, yielding more faithful compressed embeddings under fixed dimensionality and suggesting a promising direction for embedding layer compression beyond purely linear methods.

---


### 128. [Generalization Bounds via Vector-Valued $L_p$ Correlation $V_α$](https://arxiv.org/abs/2610.29425)

**<font color=#1a73e8>作者：</font>** Mohammad Hossein Momeni Hamaneh, Mohammad Mahdi Mojahedian, Mohammad Hossein Yassaee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding generalization of randomized learning algorithms remains a central challenge. Mutual-information and total-variation bounds provide complementary ways to quantify data--hypothesis dependence, but they can behave quite differently in high-dimensional regimes. We study a one-parameter family of dependence measures, the vector-valued $L_p$-norm correlation $V_\alpha$, and derive generalization bounds whose dependence terms interpolate between total variation (TV) at $\alpha=1$ and variance and $\chi^2$ related behavior at $\alpha=2$. For $\alpha>2$, the Hölder-conjugate loss moment is below two, yielding heavy-tailed specializations that can remain finite even when the loss variance is infinite. A particularly interpretable specialization occurs at $\alpha=2$, where the bound can be expressed in terms of the variability of the algorithm's output density across datasets, $\int \sqrt{\mathrm{Var}_S[p(w\mid S)]}~ dw$. We show that the entire $V_\alpha$ family is invariant under smooth bijective reparameterizations of the hypothesis space. We also introduce an adaptive density stability (ADS) condition that implies explicit control of $V_2$, and we verify it for Gibbs-type posteriors under bounded losses (yielding rates that depend on the inverse temperature and sample size). To address scaling, we extend the framework to a conditional formulation using supersamples, analogous in spirit to conditional mutual information (CMI), and discuss evaluations in the output space as a practical surrogate for estimating dependence. Simulations on Bayesian linear regression illustrate how tuning $\alpha$ can change the tightness of the resulting bounds across regimes. Additional supersample experiments on noisy MNIST and on a pretrained ResNet-50 for CIFAR-10 show similar behavior of the projected loss-space bounds beyond the original clean-MNIST setting.

---


### 129. [VIRA-Bench: Diagnosing Pedagogical Contingency Understanding in Online Tutoring Videos](https://arxiv.org/abs/2610.29428)

**<font color=#1a73e8>作者：</font>** Weihang Wang, Hansu Gu, Guanming Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Understanding a one-to-one tutoring video requires more than recognizing its events. A model must connect a visible teacher intervention to the learner response it elicits and to the follow-up adjusted to that response. Existing video and educational-dialogue benchmarks typically emphasize event recognition, temporal reasoning, social-state inference, or transcript-based interaction, but rarely diagnose this action-response-adjustment relation. We introduce VIRA-Bench, a focused diagnostic benchmark for short-horizon pedagogical contingency in one-to-one online tutoring. VIRA-Bench contains 1,005 tutoring clips and 1,322 multiple-choice questions with researcher evidence audit and expert verification, organized into Observable Evidence Grounding (OEG), Interaction Contingency Reasoning (ICR), and Support-Response Modeling (SRM). Across 11 models, the best reaches 61.3%, well below the 91.0% human reference on a stratified subset, and ICR generally has the lowest layer accuracy among leading models. Under controlled input manipulations, removing video most strongly degrades OEG, whereas disrupting temporal order most strongly degrades ICR. Free-response, Stem+Options, and synchronized-shuffle controls show that response format, static question cues, and video-ASR mismatch do not explain these layer-specific patterns. The results identify distinct behavioral evidence dependencies without claiming an internal architectural mechanism. VIRA-Bench provides a focused evaluation resource for multimodal dialogue grounding, pedagogical discourse, and temporal reasoning in online tutoring.

---


### 130. [MERP: A Latent-Bottleneck Framework for Robust Multi-Modal Multi-Label Emotion Recognition](https://arxiv.org/abs/2610.29430)

**<font color=#1a73e8>作者：</font>** Chuangxin Zhao, Meimei Zhang, Canran Xiao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal multi-label emotion recognition is important for affect-aware systems, but models trained with complete text, visual, and acoustic streams often degrade sharply when some streams are unavailable at deployment. We address this train-test gap by learning a compact representation that preserves emotion-specific evidence from any available subset of modalities. We propose the Multi-modal Emotion Recognition Perceiver (MERP), which maps the joint sequence into a fixed-size latent bank, thereby keeping repeated reasoning independent of raw input length; it extracts label-specific evidence before and after latent reasoning and aligns the two levels through reconstruction. MERP further uses positive and negative class prototypes, a noise-gated feature enhancer with frequency-shaped perturbations during training, and confidence-aware class-wise fusion to strengthen separability, reduce sensitivity to missing inputs, and combine complementary predictors. Under 20 percent test-time random modality drop, MERP achieves micro-F1 scores of 0.563 on CMU-MOSEI and 0.780 on M3ED, exceeding the strongest evaluated baselines by 0.004 and 0.005, respectively; in the severe CMU-MOSEI audio-only setting, it retains 0.473 micro-F1 versus 0.022 for LDDU. These results show that fixed latent reasoning provides a practical, testable route to robust multimodal emotion recognition without requiring missing-modality examples during training. Code is available at this https URL.

---


### 131. [Look Beyond the Question: Preserve-Focus-Fuse for Whole-Slide Image Question Answering](https://arxiv.org/abs/2610.29431)

**<font color=#1a73e8>作者：</font>** Xiangyu Li, Jincheng Li, Tianle Du 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A question about a whole-slide image rarely names every morphological finding needed to answer it. Question-guided patch selection can therefore overlook supporting morphology, while slide-level compression can dilute focal evidence. Inspired by how pathologists combine broad slide review, question-directed examination, and integration of their findings, we introduce BEYONDPATH, a Preserve-Focus-Fuse framework for whole-slide image question answering. Preserve learns a question-agnostic Morphology Bank through answer supervision across multiple questions about each training slide. Focus retrieves questionspecific evidence from all foreground patches, including regions outside the Bank. Fuse integrates the preserved morphology at the retrieved evidence positions through Morphology-on-Visual-Evidence Fusion, producing a fixed 96-token visual prefix. On WSI-Bench, BEYONDPATH achieves an Avg-9 of 0.769 and leads all eight reported report-generation metrics using the same checkpoint. It also achieves 0.639 zero-shot overall accuracy on SlideBench-BCNB. Controlled ablations show complementary benefits from morphology preservation and question-directed retrieval, and support cross-question supervision and fusion at the evidence positions. These results support looking beyond the question's explicit cues: preserving broader slide morphology while retaining the ability to seek evidence for each question.

---


### 132. [Events, Not Pixels: Where World Models Get the Return Wrong](https://arxiv.org/abs/2610.29435)

**<font color=#1a73e8>作者：</font>** Haoyue Liu, Xiaoying Tang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models are increasingly used for planning, where a planner ranks candidate actions by returns imagined by the model. However, these models are judged mainly by how well they render frames, even though a visually faithful rollout can still assign the wrong return. To identify where this mismatch arises, we introduce a transition-level diagnostic that replaces imagined transitions with real ones and measures the reduction in return error against a budget-matched random control. Our analysis yields two findings. (1) Event transitions, the few steps where a reward is earned or an episode ends, are rendered as well as other steps (median pixel-error ratio 0.85), yet restoring them removes a median of 70% of the return error. In contrast, restoring transitions with the largest MSE, SSIM or LPIPS error removes less than a random choice. Across the 44 Atari-100k model--collection pairs that pass our reliability checks, including three released families, event patches outperform random patches in 39 (sign test p=1.4 x 10^{-7}), with a median gain of +44 percentage points. (2) The remaining error is structured: a complementary patch separates errors at true events from those elsewhere, while an eight-step timing tolerance recovers few events missed by our deterministic models. This structure also guides repair: a rule recorded before four repair outcomes were known predicts when a diffusion model repairs these failures. Event patches improve plan ranking, and the same concentration appears on control tasks with rare reward events.

---


### 133. [Sparsity Should Be ALLOTted by Output: Training-Free Allocation of Block-Sparse Attention for Video Diffusion Transformers](https://arxiv.org/abs/2610.29441)

**<font color=#1a73e8>作者：</font>** Tianze Xia, Xiaoling Zhou, Ruya Lan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Full 3D attention is costly in video Diffusion Transformers. Block-sparse attention reduces this cost by computing only selected attention blocks. However, existing methods either overlook the potential to optimize sparsity allocation or rely on heuristic rules or local metrics to guide it. In this work, we observe that sparsifying attention in different layers and at different denoising steps affects final-video fidelity to substantially different degrees. Yet the identities of the most sensitive layer-step pairs remain nearly unchanged across inputs. Building on these findings, we propose Allocating Layer-step Latency by Output Tests (ALLOT), a training-free sparsity allocation method. Treating each layer-step pair as a cell, ALLOT estimates each cell's contribution to final-video error through (i) cell probing and (ii) trajectory calibration, then jointly optimizes cell densities under a measured-latency budget. It preserves existing selection strategies and kernels, replacing only the allocation component. At equal or shorter wall-clock time, ALLOT outperforms every compared allocation strategy with XAttention, with an 11.8 dB PSNR gain on HunyuanVideo. Extensive experiments across four additional published pipelines on Wan2.1, Wan2.2, and HunyuanVideo show that ALLOT outperforms or ties the default in all nine settings.

---


### 134. [Beyond Shortcut Learning: Hierarchical Spatial Prototype Regularization for Face Forgery Detection](https://arxiv.org/abs/2610.29442)

**<font color=#1a73e8>作者：</font>** Chao Shuai, Shaojing Fan, Kun Pan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative models have enabled highly realistic face forgeries, yet generalizing deepfake detectors to unseen manipulation pipelines remains a major challenge. One critical yet underexplored issue is that the learned forensic representation itself may fail to remain stable across different manipulation sources. In this paper, we provide new evidence that naively fine-tuned vision models suffer from severe \textit{forensic representation collapse}: their extracted cues are often entangled with unstable, dataset-specific artifacts, resulting in structurally fragile representations and poor cross-domain generalization. Leveraging this insight, we propose \textbf{H}ierarchical \textbf{S}patial \textbf{P}rototype (\textbf{HSP}) regularization, which explicitly models the forgery manifold by learning a structured prototype subspace over spatial features. We further introduce prototype orthogonality and second-order assignment balance, which jointly preserve the geometric independence of latent forgery factors and promote high-effective-rank utilization of the forensic representation, thereby reducing reliance on dataset-specific shortcuts. Empirical results demonstrate that our method substantially improves generalizability, yielding average frame-level AUC gains of 5.6\% and 5.3\% in the cross-dataset and cross-manipulation settings, respectively. Moreover, when used as a plug-in module, HSP boosts the average video-level AUC of existing state-of-the-art detectors to 95.3\% (+1.8\%). These results demonstrate the practical value of HSP as an easy-to-adopt regularization module for enhancing deepfake detectors.

---


### 135. [BlazeVGGT: 13x Faster VGGT at 2,000 Frames via Camera Token without Training](https://arxiv.org/abs/2610.29454)

**<font color=#1a73e8>作者：</font>** Shujun Yao, Junhui Lin, Congying Han 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward visual geometry models, exemplified by VGGT, have demonstrated strong multi-view reconstruction capabilities through dense global attention. However, the resulting all-to-all cross-view computation scales quadratically with the number of input views, making long-sequence inference particularly expensive due to substantial frame-level redundancy among highly overlapping observations. We uncover a topology-first, geometry-later evolution in VGGT camera tokens: shallow-layer tokens reliably capture local view neighborhoods, whereas deeper-layer tokens progressively encode globally organized inter-view geometry. Motivated by this observation, we introduce BlazeVGGT, a training-free framework for structure-aware frame-level key--value sparsification. At each global-attention block, BlazeVGGT constructs a view-level similarity kernel from camera-token relations and employs greedy determinantal point process inference to select a compact set of mutually complementary views. The selected views constitute the key--value context, while all input frames are retained as queries. This asymmetric attention design preserves dense per-frame predictions while eliminating redundant cross-view computation, allowing our method to be directly integrated into pretrained VGGT as a plug-and-play module without parameter updates. Its advantages become increasingly pronounced with sequence length: at 2,000 frames, BlazeVGGT achieves approximately 13$\times$ faster inference than VGGT while reducing the Chamfer Distance from 0.41 to 0.32. Extensive experiments demonstrate a favorable accuracy--efficiency trade-off in point-cloud reconstruction and camera-pose estimation, compatibility with existing VGGT accelerators such as FastVGGT and LiteVGGT, and transferability to VGGT-based models including StreamVGGT and PAGE-4D. Codes are publicly available at this https URL.

---


### 136. [PreCoMem: Predictive Cognitive Memory for Self-Evolving Long-Term Dialogue Agents](https://arxiv.org/abs/2610.29467)

**<font color=#1a73e8>作者：</font>** Jian Zhong, Zeyu Liu, Pingchuan Cao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon dialogue agents need to keep user memories stable enough for personalization while adapting when the user genuinely changes. Existing memory systems often append every observation or overwrite old entries by heuristic rules, which makes transient noise hard to distinguish from real belief drift. We introduce PreCoMem, a memory consolidation framework inspired by predictive coding that represents memory as confidence-weighted beliefs about the user's state. Its core signal, Effective Surprisal, combines semantic deviation and contradiction evidence, then downweights this signal when retrieval is diffuse and unreliable. According to effective surprisal, a two-threshold gate maps each turn to one of three deterministic updates: MAINTAIN reinforces supported beliefs, PROFILE stores ambiguous cues as low-confidence hypotheses, and CORRECT softly decays reliably contradicted facts. The PROFILE stage acts as an explicit waiting room, preventing premature commitment to noisy evidence. Experiments on LoCoMo, LongMemEval-S, and PersonaMem-v2 show consistent state-of-the-art accuracy; our new DiMoBench confirms that PreCoMem adapts to non-stationary belief drift without over-reacting to noise. The code is available at this https URL.

---


### 137. [Asymmetry Tunneling Beyond Adaptive Equivariance Relaxation](https://arxiv.org/abs/2610.29473)

**<font color=#1a73e8>作者：</font>** Eunho Jeong, Joon Jang, Hyeonjin Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equivariant neural networks encode prescribed symmetries as powerful inductive biases, yet real-world data may exhibit symmetry-breaking structure that these priors cannot fully capture. Prior work has largely addressed this challenge through model-side equivariance relaxation, seeking an appropriate level of equivariance for the data. This raises a complementary question: must equivariance relaxation be adaptively controlled? To investigate this question, we introduce a residual path alongside a strictly equivariant model and deliberately restrict their interface to examine the transmission of task-relevant structure. Across five benchmarks, we observe both residual collapse and survival despite these restrictions; we call the latter phenomenon asymmetry tunneling. We further characterize this phenomenon through four complementary diagnostics. Our results suggest that adaptive control of equivariance relaxation is not a prerequisite for capturing potential symmetry-breaking structure.

---


### 138. [Extending Affordance Segmentation for Wearable Robots to Multi-Object Images](https://arxiv.org/abs/2610.29474)

**<font color=#1a73e8>作者：</font>** Simone Lugani, Matteo Montani, Paolo Gastaldo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes a refinement to existing vision-based portable pipelines for the recognition of graspable object parts. Such pipelines can effectively support automatic grasp selection and preshaping in upper-limb prosthetic devices. However, realistic scenarios in which multiple objects are present still represent a challenge. The proposed method exploits a minor modification to the conventional hardware setup and a custom training approach to extend the applicability of vision-based pipelines. A laser pointer is introduced in the setup as an effective mechanism for object disambiguation. Accordingly, a suitable retraining of the deep convolutional neural networks supporting recognition of graspable parts is implemented. A mixed reality strategy allows the reuse of available high-quality segmentation masks to generate realistic images procedurally, extending the range of scenarios supported by the final device. Experimental results confirm that the proposed pipeline improves target disambiguation accuracy by up to 9% compared with existing solutions, while preserving the computational cost.

---


### 139. [Density-Level Backward Error for Low-NFE Generative Flows](https://arxiv.org/abs/2610.29475)

**<font color=#1a73e8>作者：</font>** Ewsey Obzherin, Valentin Khrulkov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-NFE generative ODE sampling is constrained not only by solver order, but also by how a fixed budget of network evaluations is distributed along the flow. We develop a density-level backward-error framework that identifies the component of a solver's modified-equation defect that changes the evolving marginal, while excluding solenoidal trajectory distortion that is invisible in Wasserstein tangent geometry. The resulting residual induces a solver-order-aware compute-allocation rule and, through gauge freedom, an objective for selecting numerically favorable velocity representatives of the same density path. This separates our approach from schedule search driven by trajectory or endpoint surrogates and from higher-order solver design. Exact Gaussian and mixture models establish the mechanism, including cases where curvature-based allocation fails and continuum-optimal transport is not discretization-optimal. On a pretrained CIFAR-10 EDM probability-flow ODE, density-aware allocation consistently improves fixed-update Euler sampling in the low-NFE regime. Matched-seed convergence to a dense Euler reference confirms that the method accelerates approximation of the same high-NFE flow rather than changing the asymptotic sampler.

---


### 140. [Generative Modeling via Nonlinear Schrödinger Bridges and Branching Diffusions](https://arxiv.org/abs/2610.29476)

**<font color=#1a73e8>作者：</font>** Mathias Grau, Pierre Henry-Labordère  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a new generative modeling framework grounded in forward-backward partial differential equations (PDEs). These equations arise naturally in mean-field game (MFG) theory, and are closely related to nonlinear Schrödinger systems. Our main contribution is to reinterpret this connection within the setting of generative modeling and to develop an efficient numerical methodology for its practical implementation. Specifically, we derive and characterize a nonlinear extension of the classical Schrödinger bridge problem through a coupled system of PDEs, yielding a model we call SBNL (Schrödinger Bridge NonLinear). To compute its solution, we design a simulation algorithm based on branching diffusions and the probabilistic representation of semilinear PDEs. The resulting method is embarrassingly parallel, scalable to high dimensions, and applicable to a broad class of nonlinear interaction functionals. We validate the approach through numerical experiments, including recovery of the classical Schrödinger bridge, nonlinear extensions with convex penalties (Gross-Pitaevskii) as well as potential interaction terms, and high-dimensional generative tasks such as image synthesis on the MNIST and FFHQ human face dataset. Furthermore, the same framework embeds score-based generative modeling, diffusion models, and tractable gaussian Schrödinger bridges.

---


### 141. [RubricOpt: Self-Revision of Semantic Rubrics for Preference Optimization](https://arxiv.org/abs/2610.29491)

**<font color=#1a73e8>作者：</font>** Wei Chen, Yubing Wu, Shigui Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A model's failures can reveal gaps in the behavioral criteria guiding its training. We introduce RubricOpt, a framework that lets a policy revise these criteria within preference optimization. The policy diagnoses its own rubric-free outputs, retains requirements already covered by the rubric, and edits clauses that leave recurring failures unaddressed. A shared semantic representation connects task demands, preference-data contrasts, and rubric clauses, while a deterministic gate checks evidence references and fixed semantic anchors. The rubric then guides Direct Preference Optimization (DPO) during training, with preference pairs, labels, and the objective held fixed, and is removed at evaluation. Our analysis relates the local effect on rubric-free success to semantic alignment and a residual beyond the measured factors. Experiments on capability and open-ended generation benchmarks show that rubric conditioning can improve outcomes over ordinary DPO, with gains and regressions varying across models and datasets. A matched continuation isolates the contribution of revision from additional training and finds mixed incremental effects for the tested edit, whose feedback overlaps the evaluation set. RubricOpt thus brings the behavioral specification itself into the policy's feedback loop.

---


### 142. [An Exact 93-Move Solution to a Nonlocal Crystal-Exchange Puzzle](https://arxiv.org/abs/2610.29493)

**<font color=#1a73e8>作者：</font>** Zilai Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We determine the minimum number of directional commands needed to solve alevel of Order of the Sinking Star, modeled as a crystal-exchangepuzzle on an 11*11 board. A command swapsthe player with the nearest crystal in the selected row or column, regardlessof distance; only an empty ray permits an ordinary unit walk. Two gates admitthe player to the exit exactly while all sixteen crystals occupy their targetcells. We give an explicit 93-command solution and exclude every shortersolution by an exact, cost-bounded breadth-first search. The search representsa position by its seventeen occupied cells and one active cell. Its admissibleheuristic partitions command costs between a compressed core abstraction andresidual motion, strengthened by a necessary activation detour and a cornervisit condition. The completed computation retained 605,349,215 occupied setsand 1,863,925,136 states. We prove the reductions and pruning conditions,describe the exact storage scheme, and provide source code, execution logs,and a reproduction driver. The result is a computer-assisted proof for thespecified instance, with an explicit implementation trust boundary.

---


### 143. [Rethinking Agentic Model Orchestration for Time Series Forecasting](https://arxiv.org/abs/2610.29504)

**<font color=#1a73e8>作者：</font>** Tong Guan, Tianxiang Zhan, Shirui Pan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series foundation models (TSFMs) perform unevenly across forecasting tasks. Recent work uses agentic model orchestration (AMO) to select or combine TSFMs, often outperforming individual forecasters. Yet these gains may reflect stronger or more complementary candidates rather than better orchestration. To disentangle these effects, we introduce FairAMO, a controlled evaluation protocol with frozen candidate forecasts. Experiments on GIFT-Eval show that AMO improves accuracy, but its gains are bounded by the candidate TSFMs. The best orchestrators reduce MASE by less than 6% relative to the best single TSFM across all tasks. These gains depend on complementarity (different candidates excel on different tasks) rather than the number of candidates. Adding members yields diminishing returns, and a redundant member can erase these gains. The value of historical evidence also saturates quickly. A few recent windows capture all gains, and further history adds none. These findings separate system-level forecasting gains from the contribution of orchestration itself.

---


### 144. [Shortcut-Resistant CAM Distillation for Long-Tailed Recognition](https://arxiv.org/abs/2610.29508)

**<font color=#1a73e8>作者：</font>** Wenhai Wan, Teng Zhang, Shao-Yuan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world datasets often follow a long-tailed distribution, making generalization to tail classes difficult. We revisit this problem through the lens of shortcut learning, where models prefer the easiest predictive cues (e.g., background or textures) over object-centric semantics, especially under scarce and biased supervision. We find that this tendency is amplified for tail classes: limited examples often share similar contexts, making non-semantic signals highly correlated and thus tempting shortcuts, whereas head classes with diverse appearances and environments encourage more stable object-focused representations. Motivated by this observation, we propose Shortcut-Resistant CAM Distillation (SRCD), a plug-and-play framework that transfers object-focused explanations from head to tail classes. SRCD operates in the Class Activation Map (CAM) space, where a CAM provides a class-specific spatial evidence map for a prediction. SRCD aggregates CAMs from a small set of head-class candidates into a shortcut-resistant teacher using an energy-model weighting based on coherence and concentration, and distills it to the tail-class CAM. We provide a theoretical analysis that quantifies shortcut reliance as shortcut-region evidence mass in CAM space and shows that SRCD suppresses tail shortcuts. Extensive experiments on long-tailed benchmarks consistently improve strong baselines. The code is available at this https URL.

---


### 145. [BRIDGE: An Acceptance Gate to Block False Improvements in Model Updates, with a Retrospective Clinical Evaluation](https://arxiv.org/abs/2610.29515)

**<font color=#1a73e8>作者：</font>** Dwi Sunaryono  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Models are updated repeatedly, and an update that looks better on validation data but not on new data is a false improvement that can misguide clinical decisions. The naive rule accepts every positive validation gain and is optimistic when the same data choose and judge the update. BRIDGE is a model-agnostic acceptance gate that decides each update from predictions and the available labels, with fixed settings. Each fold of the data judges the update chosen on the other folds (cross-fitting) to reduce selection bias; acceptance requires the gain's lower bootstrap bound to exceed a margin. The four settings are (A) 11 new datasets, (B) synthetic tasks, (C) 12 retrospective clinical tasks, and (D) 39 supporting datasets. The false-improvement rate falls from 19.1% (naive) to 1.1% (BRIDGE) in (A), 20.7% to 1.7% (B), 20.0% to 0% (C), and 12.5% to 0.5% (D); every 95% confidence interval of the reduction over datasets or tasks excludes zero (not over the clinical sources). An equal-size random draw from the naive acceptances contains more false improvements in (A)-(E) (post hoc, p<0.001). On the OpenML collection (E) of 14 new datasets, the false-improvement rate falls from 25.6% to 1.0%. BRIDGE removes 97% to 100% of the false improvements that the naive rule accepts, and its mean gain per deployed update is 1.8 to 3.1 times the naive rule's. The 95% upper bound on the false-improvement rate is below 5.5%: formal in (B) for independent tasks (3.56%), and conditional on the real data tested (0.33% to 5.40%).

---


### 146. [AutoPhyX: Automatic Text-Condition Physics Property Generation](https://arxiv.org/abs/2610.29517)

**<font color=#1a73e8>作者：</font>** Bei Huang, Yixin Chen, Hongbin Zha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity 4D physical simulation requires accurate physical parameter assignments that align with diverse material properties. Previous methods struggle with critical bottlenecks: they either rely on computationally intensive per-scene optimization or predict parameters from purely visual inputs. The latter suffers from inherent ambiguity, e.g., the inability to distinguish the stiffness of rubber from its appearance alone. To bridge this gap, we propose AutoPhyX, a text-conditioned framework for predicting spatially-varying physical properties. Since training robust feed-forward models requires fine-grained supervision, we first introduce a novel part-controllable data generation pipeline that decomposes complex 3D assets into semantically distinct components and pairs them with physically plausible, diverse parameters and corresponding text descriptions. Leveraging this dataset, AutoPhyX employs a cross-modal modulation mechanism where text features dynamically modulate visual features for precise physical grounding. By formulating property prediction within a voxel field, AutoPhyX ensures compatibility with diverse 3D representations, including meshes, point clouds, Gaussian Splatting, and NeRF. Experiments demonstrate that our method enables physically plausible, text-driven parameter assignment in a single forward pass. It achieves high accuracy and robust generalization to in-the-wild objects, paving the way for future physics-intensive embodied and robotic applications.

---


### 147. [Supervision-Adaptive Curriculum and Guarded Anti-Curriculum Learning for Dense Prediction](https://arxiv.org/abs/2610.29519)

**<font color=#1a73e8>作者：</font>** Chunming He, Dingming Zhang, Fengyang Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Curriculum learning orders samples by difficulty, but difficulty alone does not establish supervision reliability for dense prediction. Easy samples can expose shortcuts, hard samples can be informative, and noisy or ambiguous samples can mislead training. Building on our conference method CurriSeg, we present PaceShift, a stabilize-then-challenge paradigm combining supervision-adaptive curriculum selection with guarded spectral post-training. A learning-dynamics view motivates separating supervision reliability from temporal update value and applying spectral challenges after stabilization. The first phase estimates reliability from available supervision, augmentation consistency, model disagreement, and prediction certainty. Temporal statistics guide sample weighting, while pixel-uncertainty weights reduce the early influence of uncertain regions. The second phase ranks predictions from multiple spectral views using supervision agreement, robustness, reference consistency, and penalties. A pairwise preference objective measured against the frozen Phase-I reference, together with an anchor, refines the prediction. The framework supports full, weak, semi-supervised, and model-derived supervision. Experiments across context-entangled content segmentation (CECS), broader dense-prediction tasks, and foundation-model and cross-modal adaptations show accuracy gains. Targeted diagnostics indicate improved pooled calibration and corruption robustness in the evaluated settings. PaceShift preserves the deployed architecture and adds no inference computation. Code will be publicly released.

---


### 148. [Geometric knowledge spaces, Attention pairing and Architectures](https://arxiv.org/abs/2610.29526)

**<font color=#1a73e8>作者：</font>** Shang Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose a geometric approach to deriving attention mechanisms and exploring potential new transformer architectures. We begin by formalizing the notions of knowledge worlds and attention pairings, then demonstrate how this framework naturally leads to the architectures of standard attention, causal attention, linear attention, tensor attention, and recurrent neural networks. Finally, we introduce several new geometric spaces that may inspire novel neural network architectures.

---


### 149. [Are Joint-Embedding Predictive Objectives Effective for Longitudinal EHRs?](https://arxiv.org/abs/2610.29528)

**<font color=#1a73e8>作者：</font>** Ashvin Gupta, Brendan Delaney, Alessandra Russo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked language modelling (MLM) is the dominant pretraining objective for transformer encoders applied to longitudinal electronic health records (EHRs). However, reconstructing individual events may overemphasise noisy or weakly informative observations and does not explicitly encourage learning higher-level patient states. Joint-Embedding Predictive Architectures (JEPAs) instead learn by predicting representations in latent space and have shown strong performance in a variety of domains. In this paper, we investigate to what extent JEPA can be adapted to EHR sequence representation. Our empirical investigation using MIMIC-IV shows that although all three of our JEPA formulations train stably without representational collapse, they consistently underperform standard MLM. We find that target size, not target heterogeneity, increases prediction error, yet reducing the target size does not recover downstream performance. This suggests that stable latent prediction alone is insufficient for competitive EHR representation learning and highlights the challenge of defining clinically meaningful latent targets for EHR.

---


### 150. [Phase Transitions in Learning Driven by Extremal Data](https://arxiv.org/abs/2610.29531)

**<font color=#1a73e8>作者：</font>** Ethan Levien, Trevor GrandPre  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study an extremal regression problem, an example of multiple instance learning (MIL), where the predictors are given as multisets, called bags. The bag elements (called instances) possess hidden labels which are pooled to produce an observed bag-level label. Max pooling is common in MIL applications, but gives rise to vanishing gradients. To handle this, modern MIL pipelines approximate the max with a softmax, treating the sharpness as a learnable parameter, denoted $\lambda$. When the max pooling model is the true data generating process, learning will be successful when $\lambda$ is increased during gradient descent, thereby driving the dynamics into regions of parameter space with vanishing gradients. To understand the conditions under which gradient descent breaks down, we study a minimal model and derive a low dimensional projection of the gradient flow in the joint limit of large bags $n$ and high dimension $d$ with $\alpha=\ln n/d$ fixed. The flow has two distinct phase transitions: an intrinsic freezing transition related to the random energy model of disordered systems, and a retrieval transition occurring in modern Hopfield networks. Numerical simulation confirms both the phase diagram and the convergence of the finite-size training gradient to its predicted asymptotic form.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-232](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
