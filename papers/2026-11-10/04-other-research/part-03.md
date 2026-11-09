# 📦 其他研究 | 2026年11月10日

> 本类共 **222** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-222](./part-05.md)

---

### 101. [Deep Learning Theory through the Lens of Statistical Physics: A Topical Review](https://arxiv.org/abs/2611.09138)

**<font color=#1a73e8>作者：</font>** Wei Huang, Youjin Deng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The recent success of foundation models and deep learning has far outpaced our theoretical understanding of how large-scale neural networks learn and generalize. Statistical physics provides a natural language for describing such high-dimensional, nonlinear, and strongly coupled systems, offering concepts such as mean-field theory, phase transitions, energy landscapes, and stochastic dynamics. In this topical review, we adopt a statistical-physics way of thinking -- from concepts including phases and criticality, and free-energy viewpoints, to methods such as kernel and Gaussian-process limits, mean-field and dynamical mean-field theories, random-matrix tools, and Fokker-Planck formalisms, and to a mindset emphasizing universality, scaling, and tractable limits with explicit validity regimes. We survey recent progress on understanding modern deep learning through this lens, including mean-field analyses of wide networks, spectral and geometric perspectives on loss landscapes, stochastic-gradient-based training viewed as a dynamical process, and phase-transition analogies that organize phenomena such as overparameterization, generalization, and representation change. Our goal is to synthesize these threads into a coherent framework that clarifies what each approximation explains, when it is expected to hold, and how apparently competing narratives relate or diverge. Together, these perspectives form a unified physical framework that views representation learning as a collective phenomenon in high-dimensional systems, bridging deterministic and stochastic regimes of gradient-based optimization.

---


### 102. [CARGO: Causal Attribution and Responsibility-Guided Preventive Safe Multi-Agent Reinforcement Learning for Cooperative Driving](https://arxiv.org/abs/2611.09139)

**<font color=#1a73e8>作者：</font>** Jingjia Teng, Yang Li, Wenjie Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study presents Causal Attribution and Responsibility-Guided Optimization (CARGO), a multi-agent reinforcement learning framework for cooperative on-ramp merging in mixed traffic. A shared latent-context posterior and an action-conditioned response model estimate directed behavioral influence, with posterior uncertainty propagated into interaction-edge selection. Complementary attribution mechanisms couple signed influence with marginal team utility for cooperative reward shaping and assign responsibility from positive excess tail risk relative to a safe reference policy. Conditional diffusion generates future responses for action-dependent risk estimation. Responsibility-guided preventive optimization calibrates agent-specific risk-reduction requirements to local capacity within a policy trust region, using reserved safety margins, adaptive requirement scaling, and joint feasibility verification. Theoretical analysis establishes risk monotonicity and sufficient local conditions for non-decreasing environmental return under explicit assumptions. Experiments in highway-env across three traffic densities, together with controlled graph-recovery and attribution studies, support the effectiveness of the framework. Under high-density traffic, CARGO increases the success rate by 66.04\% and reduces the crash rate by 56.23\% relative to the best evaluated baseline for each metric.

---


### 103. [Learning Generative Dynamics for 3D Molecule Generation via Sequential Neuro-Symbolic Constraints](https://arxiv.org/abs/2611.09142)

**<font color=#1a73e8>作者：</font>** Zhuoran Li, Xu Sun, Chang Wen Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have recently emerged as a powerful paradigm for generating 3D molecules. Despite showing remarkable promise, they learn atomic distributions implicitly from data, without explicitly encoding physicochemical rules into their generative dynamics. Consequently, generated samples can be statistically plausible yet chemically invalid. To address this problem, we propose Sequential Neuro-Symbolic Constrained Diffusion (SensDiff), a framework that integrates symbolic rules into generative modeling, enabling the model to internalize scientific priors during training. Central to SensDiff is the observation that the diffusion trajectory of 3D molecule generation exhibits a coarse-to-fine evolution: valid molecules arise by first mitigating macroscopic geometric conflicts and then refining structures toward microscopic chemical consistency through iterative denoising. Accordingly, SensDiff mirrors this dynamic by sequentially enforcing constraints with adaptive weighting during training, progressively steering generation toward valid molecular geometries. Moreover, SensDiff translates domain knowledge into interpretable generative controls, grounding opaque neural denoising in scientific principles. Experiments on molecular benchmarks and real-world constrained generation tasks confirm that SensDiff consistently improves chemical validity while adhering to physicochemical rules and user-specified targets. The code is publicly available at this https URL.

---


### 104. [Augmentron: Scalable Multi-View Visual Augmentation for Robot Learning](https://arxiv.org/abs/2611.09145)

**<font color=#1a73e8>作者：</font>** Tanay Tandon, Aseem Doriwala, Jade Choghari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robot policies trained on visually narrow demonstrations can become sensitive to environmental features that are unrelated to the task. Existing generative augmentation methods can introduce visual diversity, but processing every frame and camera view independently is computationally expensive and may produce inconsistent observations across cameras and timestamps. We introduce Augmentron, a geometry-aware pipeline that generates reusable scene representations and renders them through recorded camera poses. This produces temporally and multi-view consistent environ- ment and workspace variations while preserving the robot, task objects, actions, and annotations. Across three physical manipulation tasks, replacing half of the real world training dataset with Augmentron data improves model success across three tasks for both in out-of-distribution distractor objects, and out-of-distribution workspace variation evaluations. In a separate comparison against alternate augmentation techniques, Augmentron achieves the highest pooled success in all three conditions. The results show that introducing augmented data to a data training recipe can help policies generalize to dynamic real-world settings.

---


### 105. [Evaluation of a Multi-Link Machine Learning Approach for Rainfall Detection Using Satellite Microwave Links](https://arxiv.org/abs/2611.09156)

**<font color=#1a73e8>作者：</font>** Mostafa Ftouni, Margherita Spalla, Matteo Colli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The impacts of climate change have increased the need for reliable real-time rainfall monitoring systems. This study investigates rainfall detection using a network of opportunistic sensors based on satellite microwave links (SMLs) combined with machine learning (ML) classifiers. Two models, a random forest (RF) and a convolutional neural network (CNN), were trained on aggregated SML data, including information from neighboring links. The results demonstrate that leveraging information from multiple links substantially enhances the detection of both wet and dry periods compared to single-link approaches. Moreover, the RF model consistently provides a more stable and reliable trade-off than CNN, improving rainfall detection and reducing misclassifications overall, with particularly strong performance during harsh weather conditions. The study spanned up to 32 rainy days between 2021 and 2024.

---


### 106. [Beyond the Grid: Continuous Dictionary Pursuit for Interpretable Signal Decomposition](https://arxiv.org/abs/2611.09163)

**<font color=#1a73e8>作者：</font>** Nick Janssen, Melanie Schaller, Bodo Rosenhahn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models achieve high accuracy in signal processing but remain difficult to interpret. Classical matching pursuit and sparse coding offer better transparency but suffer from spectral leakage and grid mismatch when signal frequencies do not align with discrete dictionary atoms. We introduce Continuous Dictionary Pursuit (CDP), a framework for interpretable signal decomposition that learns the parameters of closed-form functions directly from data. CDP optimizes over a continuous manifold of differentiable atoms and, unlike prior continuous pursuit methods that operate on a single analytic family, searches a heterogeneous library spanning periodic, trend, transient, and discontinuous structures. The algorithm employs a greedy iterative strategy using data-driven priors and gradient-based optimization to isolate individual signal components, with discontinuous waveforms made differentiable through spectral sharpness annealing. To ensure a sparse atom set for reconstruction, the framework utilizes a stopping criterion based on a predefined atom budget and residual error convergence. Evaluations on synthetic and real-world datasets show that CDP removes the grid discretization error for atom families contained in its library, recovers generative parameters to within $1\%$ on stationary synthetic signals expressible in that library, and achieves the best sparsity-accuracy trade-off among classical, continuous-pursuit, and neural baselines in the sparse regime. Beyond decomposition, we demonstrate that the extracted atoms can serve as structured curriculum targets for training sequence models, improving forecasting accuracy over standard end-to-end training on most evaluated datasets. The method offers a glass-box alternative for signal decomposition by providing high reconstruction fidelity alongside direct physical interpretability.

---


### 107. [FIND: Frequency Invariance Disentanglement for Test-Time Adaptation in LiDAR 3D Detection](https://arxiv.org/abs/2611.09170)

**<font color=#1a73e8>作者：</font>** Dongxiao Li, Zixuan Hu, Ling-Yu Duan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR-based 3D Object Detection (L3OD) is a fundamental 3D perception task, yet its performance is often compromised by domain shifts arising from diverse sensor configurations and environmental conditions. Existing Test-Time Adaptation (TTA) methods primarily leverage self-supervision in the spatial domain, yet they frequently confound semantic content with domain style due to the sparse, non-Euclidean nature of point clouds. To overcome this limitation, we propose FIND (Frequency INvariance Disentanglement), a novel TTA framework that precisely disentangles domain-invariant content from domain-specific interference within the frequency domain. Our methodology utilizes B-Spline fitting to construct locally adaptive filters integrated into a dual-stream architecture: an Invariant Stream extracts robust features to guide pseudo-labeling, while a Specific Stream enforces consistency against domain perturbations. By combining invariance-driven alignment with stability-guided regularization, our approach dynamically extracts robust domain-invariant features while suppressing domain-specific interference. Extensive experiments on cross-dataset adaptation and robust corruption benchmarks demonstrate that FIND significantly outperforms state-of-the-art methods. The source code is publicly available at this https URL.

---


### 108. [TOFS: Feature Selection with Swap Supervision for Semantic Communication over Fading Channels](https://arxiv.org/abs/2611.09173)

**<font color=#1a73e8>作者：</font>** Zhiyi Zhu, Eiji Takimoto, Patrick Finnerty 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Task-oriented semantic communication transmits task-relevant features to support receiver inference under limited communication resources and adverse channel conditions. For image classification, the usefulness of a feature depends on the other transmitted features and the distortion introduced by the wireless channel. Effective feature prioritization should therefore account for classification performance after transmission of the selected features. This paper proposes a Task-Oriented Feature Selection (\textit{TOFS}) framework and method, which evaluates feature replacements using receiver classification loss. Loss differences confirmed under independent transmission samples provide pairwise ranking supervision for a selector network. The trained selector predicts priorities in a single forward pass. CIFAR-10 simulations demonstrate improved classification accuracy over an importance-based feature selection baseline at the same transmitted feature count and average transmit power. The proposed \textit{TOFS} framework shows 84\% accuracy performance under Rayleigh fading and Gaussian noise, compared with the 68\% performance of a SOTA method.

---


### 109. [SIFR: Stable Signed Flow Reinforcement](https://arxiv.org/abs/2611.09175)

**<font color=#1a73e8>作者：</font>** Runlong Liao, Xingqian Xu, Lizhang Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward-based fine-tuning of flow models requires effectively promoting high-reward and suppressing low-reward samples, while maintaining training stability over many rounds of iterative updates. Iterative reward fine-tuning provides a simple starting point, but the positive reward weights give no explicit unfitting signal, and repeated reweighting concentrates the distribution and causes collapse. We propose Stable Signed Flow Reinforcement (SIFR), which replaces the reward weights by signed advantages to supply the missing unfitting signal, and constrains the velocity drift from a reference model to stabilize the updates, with a Lagrange multiplier that adapts the regularization strength to a prescribed drift budget. We further show that existing flow RL methods fall within this framework: they implicitly minimize the signed loss, differing in their regularization choices. We validate SIFR on SD3.5 Medium (2.5B) and FLUX.2 Klein (9B) and scale it to Cosmos 3 Super Text2Image (64B): across all 12 backbone--reward pairs with preference and rule-based rewards, it matches or exceeds existing methods, reaches their peak rewards much faster, and keeps improving over long training where they plateau or collapse.

---


### 110. [A Taxonomy-Driven Synthetic Dataset for Retrieval Effectiveness and Fairness Evaluation in Hiring](https://arxiv.org/abs/2611.09178)

**<font color=#1a73e8>作者：</font>** Warren Jouanneau, Morgane Hoffmann, Emma Jouffroy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While machine learning hiring tools are ubiquitous, the need for privacy regulations and commercial sensitivity makes public benchmarking legally complex. We address this challenge by introducing a taxonomy-driven, fully synthetic HR dataset and benchmark to simultaneously evaluate retrieval effectiveness and algorithmic fairness. Grounded in 660K real freelancer profiles, our multilingual corpus features candidate profiles, project briefs, and counterfactual demographic twins. Auditing state-of-the-art embedding models reveals performance divergence from general MTEB scores, alongside fairness disparities in grammatically gendered languages. This demonstrates that general benchmarks are insufficient for HR, requiring tailored evaluations to identify Pareto-optimal models that balance semantic accuracy and fairness.

---


### 111. [RoleWalk: training-free structural embeddings for directed graphs that transfer across graphs](https://arxiv.org/abs/2611.09189)

**<font color=#1a73e8>作者：</font>** Maixent Chenebaux  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structural role embeddings describe a node by its position in a graph - hub, bridge, periphery, member of a dense core - rather than by who its neighbours are. Existing methods either learn coordinates specific to one graph (struc2vec, Role2Vec, RESD) or read scales and normalisations from the whole graph (GraphWave, Digraphwave), so the same neighbourhood can receive different coordinates in two graphs; few read edge directions. We present RoleWalk, a training-free embedding that follows a short lazy random walk from each node and records, at each step, two distributions: that of the transition probabilities, through its characteristic function at a fixed grid of frequencies, and that of the walker's distance to its starting node. On directed graphs, walks that go forward then backward add who shares a node's targets or sources. The embedding depends only on a node's neighbourhood within a fixed radius, so its coordinates mean the same thing in every graph. We show that, without curvature, it is the kernel mean embedding of the walk's footprint, that it separates graphs that the Weisfeiler-Leman test cannot, and that pruning small probabilities comes with a per-node error certificate. Empirically, RoleWalk is competitive with the best role embeddings on five classification benchmarks at a fraction of their cost, has the highest scores on real directed roles in Wikipedia adminship, exceeds the published accuracy of Digraphwave at every noise level of its own Enron network-alignment benchmark, transfers centrality predictors to graphs four times larger better than existing inductive embeddings, hand-made features and a trained GIN, and embeds a million nodes in 20 s to 3 min on one CPU core. The code is open source (BSD license): this https URL

---


### 112. [Bootstrap Your Own AV-Proxies: Adaptive Contrastive and Prototype Learning for Audio-Visual Segmentation](https://arxiv.org/abs/2611.09191)

**<font color=#1a73e8>作者：</font>** Junbo Zhang, Hang Su, Zhaofan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-Visual Segmentation (AVS) aims to accurately segment sounding objects in video frames by leveraging audio-visual correspondence cues. However, it remains challenging due to the intrinsic semantic incompleteness within a single modality and the semantic gap between audio and visual representations. Traditional feature-fusion decoding approaches struggle to suppress fusion noise effectively, while recent methods that incorporate data-dependent priors often increase the complexity of modeling audio-visual correlations, leading to poor cross-domain generalization. To address these issues, we propose a novel adaptive contrastive and prototype learning framework, BYOAVP, for AVS. Specifically, we design a Self-Supervised Audio Enhancement (SSAE) module that introduces contrastive learning to adaptively align audio representations with gradient-blocked visual embeddings, thus narrowing the semantic gap between modalities. Furthermore, a Dynamic Prototype Constraint (DPC) module is developed to refine pixel-wise category perception via momentum-based prototype updating, while enhancing localization of sounding regions through cross-modal interaction. Extensive experiments demonstrate that our method achieves SOTA performance across two AVS benchmarks and six sub-tasks, exhibiting strong robustness and generalization ability.

---


### 113. [InstantHMR : Real-Time Human Mesh Recovery on Your Phone](https://arxiv.org/abs/2611.09195)

**<font color=#1a73e8>作者：</font>** Mohamed Adjel, Kahina Chalabi, Vincent Bonnet  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time 3D human mesh recovery from a single image on mobile devices is a challenging problem with many applications, including robotics, biomechanics, AR/VR, and exergames. Current state-of-the-art models are either too slow to run efficiently on mobile devices or sacrifice accuracy for speed. We present InstantHMR, a family of open-source single-image regressors suited for mobile inference, based on the Momentum Human Rig (MHR) parametric model and trained exclusively on publicly available annotations from the SAM 3D Body dataset. Our approach achieves remarkable performance on a Samsung Galaxy S23 NPU, recovering a 6,890-vertex body mesh in 5.5 ms per person, and 0.98 ms on an NVIDIA RTX 4070 GPU. This speed surpasses all existing methods we evaluated. On mobile, it is 12x faster than the single mobile-compatible method that slightly outperforms ours in accuracy, while achieving competitive accuracy with 40.0 mm PA-MPJPE on 3DPW, 48.8 mm on EMDB and 41.7 mm on RICH. To ensure fair comparisons, we re-evaluate 11 state-of-the-art methods under a unified protocol aligned with the closest MHR-based competitors, including Meta's official MHR-to-SMPL conversion, and report their reproduction results. Additionally, we measure latency across eight different targets, ranging from desktop TensorRT to two phone NPUs. Code and models are available at this https URL.

---


### 114. [Calibrated concept profiles: making the reading of a model's neurons a measurement](https://arxiv.org/abs/2611.09196)

**<font color=#1a73e8>作者：</font>** Piotr Wilam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Interpretability has largely moved from reading a model's neurons directly to reading a second model trained on the first: a probe, a sparse autoencoder, a crosscoder. The move answered real faults -- mixed meanings, thresholds without a unit, readings that did not transfer from one study to the next -- but gave up what a direct reading alone provides: nothing trained in between, the neurons themselves named, and a reading that can be repeated and compared. Here the direct reading is made a measurement.
A neuron's activation varies with the prompt, so its reading is a distribution over a population of stimuli. We declare that population: every factor around a target construct is drawn at its rate in a reference corpus and logged.
From the declared distribution we generate a battery of prompts, and draw it twice. From the battery we compute the calibrated concept profile, one number per neuron, stated in units of the neuron's own spread on ordinary input; the two draws give every number a noise unit. Before the profile is read, a fixed set of checks licenses the battery on the model, and the smallest change the profile can resolve across training checkpoints is measured.
Realised for Python on OpenCoder-1.5B and followed across checkpoints spanning two trillion training tokens, the profile gives what the alternatives do not report: a unit on every number, a chance level for every comparison, and which neurons carry a construct at every checkpoint.
The battery, the code and the data behind every result are released.

---


### 115. [Safe Reinforcement Learning via Probabilistic Option Shielding](https://arxiv.org/abs/2611.09197)

**<font color=#1a73e8>作者：</font>** Gian Luca Ascari, Isidoro Tamassia, Ying Jiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Shielding is a safe reinforcement learning technique that provides safety guarantees while learning, by blocking unsafe actions. Traditional shielding relies on a complete model of the environment to provide long-term guarantees. Probabilistic logic shielding (PLS) lifts the requirement of having such model, but only considers safety in the short term, typically looking only one or few steps ahead. We propose Probabilistic Option Shielding (POS), which extends PLS to the option level, recovering long-horizon safety without reintroducing the need for a complete environment model. POS learns a model-free critic directly from one-step PLS signals, to estimate the probability that an entire option will complete safely under uncertainty. We evaluate POS on safe navigation tasks in the LogiCity environment, and show that it achieves considerably safer training while matching the task performance of standard step-level PLS and other safety related reinforcement learning baselines.

---


### 116. [Representational drift in a code model: behaviour settles, which neurons carry it does not](https://arxiv.org/abs/2611.09204)

**<font color=#1a73e8>作者：</font>** Piotr Wilam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In neuroscience, representational drift is a change in which neurons carry a representation while behaviour stays the same; we measure its analogue in OpenCoder-1.5B during pretraining, for 169 Python constructs over two trillion tokens at a constant learning rate, with a noise unit on every change, at checkpoints as close as 1,000 training steps. For 16 of the 169, those whose grammar fixes a next token, the loss at those positions reaches its floor within the first 4% of training, while the model's reliance on the neurons carrying them grows to the end: removing them costs 0.06, 0.25 and 0.40 nats more than removing a random set, at 4 billion, 84 billion and 2 trillion tokens. Which neurons carry a construct never settles: for all 169 the carrier set is still changing at the last checkpoint, and an abrupt settling at any date from 84 billion to 1.5 trillion tokens, or a gradual one before 500 billion, would have been detected in 99% of injected cases. The set measured at 84 billion tokens, removed at the end, cannot be separated from a random set, so the function is carried by whichever neurons are current. Up close the change is a persisting pool and a changing sample: a neuron that leaves a construct's set returns at three times the rate of a matched neuron, and no set reassembles. The hypothesis we fixed in advance, that the carriers settle, is refuted; we discuss candidate causes and name the experiment that would separate them.

---


### 117. [Provable State Estimation with Recurrent Models](https://arxiv.org/abs/2611.09217)

**<font color=#1a73e8>作者：</font>** Vincent Andrieu, Pauline Bernard, Lucas Brivadis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating the state of a dynamical system from observations is a crucial task in robotics and control. Despite their empirical success, recurrent models often lack formal guarantees on convergence and robustness. We bridge this gap by analyzing these architectures from the perspective of nonlinear observer theory. By framing RNNs as a time-discretization of continuous latent dynamical systems (Neural ODEs), we demonstrate that enforcing a contraction condition on the latent flow guarantees the existence of a smooth, injective map of the true physical state into the latent space. We prove that this architecture acts as a tunable observer: by increasing a single scalar gain that scales the latent vector field, the estimation error can be driven to an arbitrarily small neighborhood of zero at an exponentially fast rate. We further establish quantitative bounds on the MLP complexity required to decode this latent state, and extend our formal guarantees to the discrete-time residual RNN implementation. We validate the theory on a real mobile robotic task, where a provably contracting model outperforms a vanilla GRU with substantially more stable training. We also report that unconstrained GRUs converge to contracting dynamics on this task, suggesting that contraction is an emergent property of well-trained sequence models.

---


### 118. [HMMF-Net: A Lightweight Hierarchical Multi-Frame Multimodal Fusion Network for Accurate Fish Feeding Intensity Assessment](https://arxiv.org/abs/2611.09224)

**<font color=#1a73e8>作者：</font>** Phi-Hung Hoang, Van-Manh Tran, Nam-Thuan Trinh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated fish feeding intensity assessment (FFIA) is important for precision aquaculture and feed cost optimization. However, unimodal methods are vulnerable to acoustic noise and visual disturbances, while existing multimodal frameworks often rely on computationally intensive 3D convolutions or Transformers, limiting their use on edge devices. To address these limitations, we propose HMMF-Net, a lightweight multimodal architecture that combines early multi-frame visual encoding and multi-axis acoustic modeling through a hierarchical bidirectional messenger cross-modal fusion (BMCF) mechanism. The visual branch captures temporal variations in feeding behavior by stacking temporally distant frames as a multi-channel input to an adapted 2D EfficientNetB0 backbone. The acoustic branch employs adaptive multi-axis residual units (AMARU) to extract temporal, frequency, and local time-frequency representations from log-mel spectrograms. BMCF progressively exchanges information between the two modalities at intermediate representation levels through compact messenger tokens, reducing the computational overhead of dense cross-modal attention. Evaluated on the AV-FFIA dataset using five-fold cross-validation, HMMF-Net achieves 96.77% accuracy and 96.88% F1-score on the held-out test folds, with 3.987M parameters and 1.002 GFLOPs. Compared with the best-performing visual configuration (95.49% accuracy), HMMF-Net reduces the classification error by 28.38%. Deployment on an NVIDIA Jetson Orin Nano using TensorRT with FP32 precision maintains comparable accuracy, with an inference time of 11.54 ms per 2-second sample and a model size of 18.81 MB. These results demonstrate that HMMF-Net combines effective multimodal representation learning with computational efficiency, enabling accurate and practical FFIA on resource-constrained edge platforms.

---


### 119. [Fused-Softmax for efficient quantized attention](https://arxiv.org/abs/2611.09225)

**<font color=#1a73e8>作者：</font>** Tianxing Wu, Juuso Korhonen, Jesus Carabano Bravo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Low-precision matrix throughput on modern GPUs is growing far faster than vector-arithmetic throughput. Attention therefore cannot realize the available GEMM performance because softmax has become the pipeline bottleneck. We introduce Fused-Softmax Attention, a training-free algorithm that reformulates and approximates softmax to fold its dominant operations into the attention GEMMs, moving work from vector units to matrix cores. Implemented for the AMD CDNA 4 architecture, our MXFP8, MXFP6 and MXFP4 kernels reach approximately 3.0, 4.0 and 4.6 PFLOP/s on an AMD Instinct MI355X GPU, yielding speedups of $2.1\times$, $2.8\times$ and $3.2\times$ over the BF16 attention. Importantly, the additional error introduced by Fused-Softmax remains below the error floor set by quantizing the GEMM operands. On Wan2.2-T2V-A14B, a hybrid MXFP6/4 schedule delivers up to $2.05\times$ end-to-end speedup while preserving the visual quality of the outputs. The kernels ship in AMD's open-source AITER library, and they powered AMD's MLPerf Inference v6.1 Wan2.2 submission, which ran $1.7\times$ faster than AMD's previous-round result on the same hardware. Our results show that redesigning softmax to utilize the matrix pipeline enables attention to capitalize on continued growth in low-precision matrix throughput.

---


### 120. [Rhythmic Fitness Beat 'Em All using Real-Time Monocular Human Pose Estimation](https://arxiv.org/abs/2611.09228)

**<font color=#1a73e8>作者：</font>** Yanis Zaoui, Valentin Bégel, Mohamed Adjel  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Short and frequent physical activity exercices mitigate the health risks of sedentary behavior. Yet, the lack of motivation remains a critical barrier to adoption. Exergames gamify physical activity, but most rely on dedicated hardware, and outside dance and rhythm games they rarely use the musical beat. We present a work-in-progress beat 'em up exergame played with the whole body in front of a single smartphone, which runs the entire pipeline: an off-the-shelf real-time 3D human mesh recovery model on the phone's neural processing unit, gesture recognition, and the game, shown on any TV through a USB-C to HDMI cable. Our contributions are (1) a 3D recognition of five shadow-boxing moves (guard, punch, slip, squat, jump), each defined by one metric measure in a body frame aligned with gravity and one threshold with hysteresis, personalised during a tutorial; (2) a rhythm stage whose discrete cues are placed on the song's kick drum and judged on the movement's capture time, with a delay learned for each player; and (3) a phone-only architecture, running at 30 frames per second, that turns a phone and an HDMI cable into an exergame console.

---


### 121. [MM-DyGraph: A Dataset, Benchmark, and Model for Multimodal Dynamic Graphs](https://arxiv.org/abs/2611.09240)

**<font color=#1a73e8>作者：</font>** Zongyuan Wu, Pengjie Wang, Lingshan Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal dynamic graphs are pervasive in real-world applications, where nodes and edges are accompanied by multimodal signals, including text and images. Despite their practical importance, benchmarks and methods that explicitly study multimodal learning in dynamic graphs remain scarce, hindering the full understanding and effective utilization of multimodal information for downstream tasks. To address this gap, we introduce MM-DyGraph, to the best of our knowledge, the first benchmark for multimodal dynamic graph learning, consisting of diverse real-world datasets with fine-grained temporal graph evolution and rich multimodal attributes. MM-DyGraph provides three evaluation tasks to comprehensively assess model performance in dynamic settings. We benchmark representative state-of-the-art dynamic graph methods and reveal that naive feature concatenation yields target-level inconsistencies: multimodal inputs benefit certain prediction targets while harming others. This observation indicates that the modality informativeness depends on the specific prediction target over time. Building on these observations, we propose a Target-aware Spatial-Temporal Multimodal Fusion (TST-MF) framework, which jointly conditions multimodal fusion on the prediction target and spatial-temporal relations, enabling context-adaptive cross-modal interplay for target-specific representations. Extensive experiments over diverse datasets and tasks show that TST-MF delivers robust and competitive performance, achieving clear gains in multimodal settings.

---


### 122. [Practical Non-Stationary Graph Gaussian Processes](https://arxiv.org/abs/2611.09247)

**<font color=#1a73e8>作者：</font>** K. S. Sesh Kumar, Viacheslav Borovitskiy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gaussian processes on graphs provide a principled framework for prediction and uncertainty estimation, but modelling heterogeneous networks often requires balancing flexibility against parameter complexity. Variability at a node may reflect useful signal that should propagate through the network, unreliable measurements whose influence should be suppressed, or a mixture of both. We introduce Variance-Coupled Gaussian Processes (VCGPs), which use a positive auxiliary signal to modulate graph interactions through a single learned coupling exponent. The exponent controls how strongly high-variability nodes propagate or attenuate information, while a cluster-wise extension accommodates different regimes within the same graph. Under stated structural assumptions, we characterize the unique stationary-rescaling point of the basic family, where correlations match those of a stationary graph kernel while node-dependent variances remain. Experiments on traffic, air-quality and weather datasets show competitive prediction and uncertainty estimation relative to stationary and per-node non-stationary baselines, with the largest gains on networks requiring multiple coupling regimes. Stationary correlations after variance rescaling remain sufficient on some data, and performance depends on the auxiliary signal and model selection.

---


### 123. [Topology as a Design Variable: Joint Architecture-Sizing Optimization for SRAM](https://arxiv.org/abs/2611.09248)

**<font color=#1a73e8>作者：</font>** Can Wang, Junhao Ma, Yikai Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> SRAM's power-performance-area-stability trade-off depends on bitcell topology, a discrete architectural choice that interacts non-separably with continuous transistor sizing. However, no open-source SRAM tool treats topology as an optimizable variable. OpenRAM generates SRAM layouts but performs no optimization, while OpenYield supports high-fidelity evaluation but restricts optimization to scalar sizing of a fixed 6T cell. OpenYieldV2 closes this gap through three integrated contributions. First, a fully parameterized compiler generates complete 6T and 10T SRAM macros with peripheral circuits and replica-bitline self-timing, enabling topology comparison under identical simulation conditions. Second, a few-shot TabPFN surrogate learns topology-dependent PPA responses with limited full-macro SPICE samples. Third, a coarse-to-refined multi-objective optimizer combines global exploration of discrete architectural choices with local refinement of continuous transistor sizes. Experiments across varying design conditions reveal a topology decision boundary that shifts with operating constraints rather than following a fixed design rule. Jointly optimizing across this boundary improves hypervolume by up to 17.3\% over the strongest single-topology baseline. OpenYieldV2 is open-source to support reproducible SRAM design research.

---


### 124. [Zero-Query Transferable Pretend Benign Attacks with Amortized Online Generation for Cooperative Perception](https://arxiv.org/abs/2611.09256)

**<font color=#1a73e8>作者：</font>** Hongwei Lin, Xun Huang, Chenglu Wen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cooperative perception enables an ego agent to acquire information from collaborators beyond its own sensors' reach. Yet, the most beneficial messages are often the hardest to verify from local observations. Pretend Benign (PB) exploits this asymmetry by targeting regions with weak local verifiability and applying multi-objective perturbations, making harmful feature changes appear to be benign assistance. However, PB is victim-dependent: selecting regions and optimizing perturbations require the victim model's architecture, parameters, and gradients, limiting transfer to unseen victims. A transferable attack must capture properties shared across cooperative detection models rather than those specific to one network. We address this by building a victim-agnostic attack from a heterogeneous ensemble of surrogate models and encoding its capabilities in a reusable dictionary to reduce per-message generation cost. Specifically, Transferable Pretend Benign (TrPB) transfers PB's region selection criterion and multi-objective perturbation strategy across heterogeneous surrogates to construct an offline attack. We further propose RT-TrPB, which encodes transferable regions and perturbation patterns into a region predictor and reusable perturbation dictionary, amortizing per-message attack generation. Experiments on widely used cooperative perception benchmarks show that RT-TrPB bypasses the consensus-based defenses ROBOSAC and FLD with success rates approaching 100% and generates each perturbation in under 56 ms. To counter PB-style attacks masquerading as benign collaboration, we also propose STTrust, which verifies received messages using spatial and temporal consistency and incorporates identity-level trust. STTrust detects over 90% of PB-style attacks and restores perception performance to near the attack-free level.

---


### 125. [Forecasting cumulative intraoperative hypotension burden: patient-disjoint evaluation of quantile boosting and alert policies](https://arxiv.org/abs/2611.09259)

**<font color=#1a73e8>作者：</font>** Yunfan Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Background: Binary hypotension forecasts do not describe the depth and duration of future low pressure. Burden forecasts may support graded early warning, but better forecast scores need not yield more useful alerts.
Objective: To evaluate conditional quantiles of the next 15-minute mean arterial pressure (MAP) deficit below 65 mmHg and distinguish forecasting performance from episode-warning performance.
Methods: Public VitalDB numeric arterial MAP was reduced to 10-second medians without forward filling. Subject-disjoint training, validation and test splits included 70,402, 14,270 and 15,575 labeled windows. We compared climatology, calibrated persistence, last-MAP-only boosting, and direct and residual quantile boosting, with and without additional MAP-history features. Patient-weighted pinball loss and subject-bootstrap intervals evaluated forecasting. Validation selected alert thresholds before a hash-recorded test evaluation.
Results: In the test split, the prespecified residual-versus-persistence comparison at the 90th percentile yielded losses of 2.256 and 2.900 mmHg-min, respectively (difference -0.644; 95% interval -0.814 to -0.487). Direct prediction achieved 2.196, and direct prediction with additional MAP features achieved 2.193. Episode-warning results were sensitive to the alert rule and operating threshold.
Conclusions: This retrospective benchmark separates burden-forecast skill from warning-policy performance. Findings support further study of direct burden estimation; they do not establish patient benefit, prospective reliability or transportability beyond the source hospital.

---


### 126. [Model-based learning for DoA estimation and array calibration via continuous sparse recovery](https://arxiv.org/abs/2611.09263)

**<font color=#1a73e8>作者：</font>** Baptiste Chatelier, José Miguel Mateos-Ramos, Vincent Corlay 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Direction of arrival (DoA) estimation, a classical signal processing problem, has experienced renewed interest with the advent of integrated sensing and communication (ISAC). While decades of research have yielded highly accurate DoA estimators, hardware impairments have frequently been neglected, despite degrading both DoA estimation accuracy and downstream communication performance in ISAC systems. This work introduces a joint array calibration and DoA estimation method based on the simultaneous orthogonal matching pursuit (SOMP) algorithm, following the model-based machine learning paradigm. The proposed method enables the calibration of antenna arrays subject to severe gain-phase and antenna location impairments through projected gradient descent (PGD), with either supervised or unsupervised objectives. Additionally, DoA estimation is enhanced by extending SOMP to continuous dictionaries via PGD refinement steps. Simulation results demonstrate that the proposed method enables efficient hardware impairment compensation, even without labeled samples, while outperforming conventional sparse recovery and subspace-based DoA estimation baselines.

---


### 127. [PHISHREV+: An ASP-Based Post-Hoc Defeasible Machine Learning Framework for Phishing Detection](https://arxiv.org/abs/2611.09273)

**<font color=#1a73e8>作者：</font>** Mainak Sen, Kumar Sanka Ray, Amlan Chakrabarti  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Phishing website detection remains a critical cybersecurity challenge. Although machine learning classifiers achieve high accuracy on benchmark datasets, they suffer from a fundamental limitation: once trained, their decision boundaries are fixed and cannot incorporate new contextual evidence without retraining the model. This work presents \textbf{PHISHREV+}, a hybrid framework that instantiates the notion of \textit{post-hoc defeasible machine learning}. This framework does not replace the classifier. It treats the initial classifier predictions as defeasible beliefs and revises them through an Answer Set Programming based non-monotonic reasoning(NMR) layer. The framework operates in two phases. In the machine learning phase, four classifiers (SVM, KNN, DT and RF) are trained on the 87 feature benchmark dataset. In the post-hoc NMR phase, four defeasible rules derived from exploratory data analysis of the training set, and validated through Chi-square and Mann-Whitney U tests, formally revise initial predictions. The proposed framework achieves consistent false positive reduction across all our classifiers SVM (41$\rightarrow$39), KNN (47$\rightarrow$46), DT (62$\rightarrow$61), and RF (52$\rightarrow$51) while maintaining complete false negative parity with zero increase overhead. A comprehensive ablation studies across seven rule configurations confirms that the hierarchical combination of all four defeasible rules is necessary to achieve this optimal balance. Instance level explainability is provided through eXplainable ASP (XASP), which generates formal derivation graphs showing which defeasible rules fired and why the initial belief was retracted, a capability absent from all existing phishing detection approaches.

---


### 128. [Federated Forensics: Jurisdictional constraints as a design driver for multi-agency federated learning](https://arxiv.org/abs/2611.09277)

**<font color=#1a73e8>作者：</font>** Aruna Withanage, Jessica Herrmann, Hudan Studiawan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Digital forensic investigations increasingly cross borders, and law enforcement agencies need to build analytical models together without centralizing their data. Federated Learning (FL) keeps data local, yet neither FL nor its frameworks enforce the jurisdictional, governance, and accountability rules that multi-agency forensic work requires. This paper takes a design-first approach to that gap. First, we derive seven requirements that a federated learning system must meet in a forensic setting. Second, we propose Federated Forensics, a three-layer reference architecture whose middle layer, unlike in existing hierarchical FL designs, sits at a jurisdictional border and can use a model update locally while blocking it from crossing that border. Third, we build a prototype of the architecture and test it on a malware-family classification task. In a prototype evaluation, the policy gate blocked every restricted update at the border with zero violations, and restricted-class accuracy rose from 0% under today's compliant alternative to 93.0%, only 4.4 points below ignoring the restriction.

---


### 129. [Diversity-Aware Client Selection for Communication-Efficient Federated Learning](https://arxiv.org/abs/2611.09278)

**<font color=#1a73e8>作者：</font>** Max Halleryd, Sima Sinaei, Viktor Valadi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables collaborative model training across distributed clients without sharing raw data, making it attractive for privacy-sensitive and bandwidth-constrained applications. A practical challenge in deploying FL is reducing communication overhead while maintaining model performance under heterogeneous, non-IID data distributions. Selecting which subset of clients participates in each training round offers a principled way to address both challenges simultaneously, yet its impact on data diversity and representativeness remains underexplored. In this paper, we investigate three client selection strategies, Power-of-Choice, Fisher information, and Centered Kernel Alignment, evaluating them not only by accuracy and convergence, but through the lens of participation diversity using the Gini coefficient and KL divergence. Under non-IID conditions, restricting participation to 15% of clients per round achieves significant communication savings, and when selection promotes diverse and balanced contributions, it also improves generalization over biased alternatives. This work provides a systematic and reproducible analysis demonstrating that diversity-focused client selection renders communication efficiency and model quality complementary rather than competing objectives.

---


### 130. [Safety-Focused Reinforcement Learning Using Risk-Sensitive Coupled Control](https://arxiv.org/abs/2611.09290)

**<font color=#1a73e8>作者：</font>** Jiabin Lin, Shana Moothedath, Vivek S. Borkar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper investigates the coupled control problem within safety-focused reinforcement learning, addressing the essential challenge of achieving optimal performance while ensuring safety in systems operating within complex environments. We define safety as the requirement to prevent the system from reaching undesirable or hazardous states. We propose a coupled control approach that prioritizes safety by employing effective methods to prevent the system from entering unsafe states while optimizing the performance metric, defined as the average cost. We propose a novel problem transformation that reformulates it into a risk-sensitive problem combined with an average reward criterion. We present a two-timescale Q-learning algorithm where in the faster timescale, the algorithm solves a risk-sensitive control problem to ensure safety, while on a slower timescale, the algorithm focuses on average cost control. We provide theoretical guarantees for the convergence of our algorithms, establishing their significance in ensuring safe, optimal control in dynamic environments. We validated the performance of our approach using GridWorld and CarGoal task in Safety Gymnasium.

---


### 131. [Multilingual Artificial Datasets for AI-Driven Cardiology: the CliTe and ParaCliTe corpora](https://arxiv.org/abs/2611.09296)

**<font color=#1a73e8>作者：</font>** Lorenzo Pratesi, Eulalia Farre-Maduell, Machteld Boonstra 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background and Aims. Comparable, multilingual, validated cardiology corpora are critical to advance trustworthy natural language processing (NLP) models for cardiology but such resources are scarce due to privacy concerns. This study aimed to cover this gap by presenting suitable artificial corpus creation guidelines and by releasing 3 multilanguage corpora. Methods. Following purpose-specific publicly-available corpus construction guidelines, cardiologists from 7 European hospitals generated artificial clinical records in Czech, Dutch, English, Italian, Romanian, Spanish and Swedish, ensuring clinical diversity and sex balance, resulting in the CliTe corpus. A CliTe subset underwent a multi-stage manual translation into the other 6 languages, resulting in the parallel ParaCliTe corpus, while the remaining reports were automatically translated, constituting ParaCliTe Silver. Results. CliTe is a collection of 699 artificial cardiology reports, mostly outpatient notes (340 documents), discharge reports (263), and inpatient notes (89), describing fictional patients with ischaemic heart disease (199 patients), heart failure (188), and valvular disease (79), among others. ParaCliTe contains reports from 94 fictitious patients, each available in seven languages with sentence-level alignment, resulting in 658 documents. The corpus mainly comprises discharge reports (322 documents), and outpatient (196) and inpatient (140) notes, describing patients with heart failure (399 documents), ischaemic heart disease (287), and valvular disease (238). Empirical results illustrate the utility of ParaCliTe and highlight the limitations of state-of-the-art NLP models adapted to the cardiology domain. Conclusions. The creation of multilingual, equitable and realistic corpora of artificial patients capable of strengthening NLP performance for cardiology is feasible when supported by detailed guidelines.

---


### 132. [A Stochastic Latent Variable Generalization of Joint-Embedding Predictive Architectures](https://arxiv.org/abs/2611.09302)

**<font color=#1a73e8>作者：</font>** Nikos Giakoumoglou, Paschalis Giakoumoglou, Tania Stathaki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-Embedding Predictive Architectures (JEPAs) predict the latent embedding of a target signal from a context signal, with an auxiliary variable z conditioning the predictor. Despite its prominent role in the original JEPA blueprint, the content of z has been carried by a fixed deterministic token in every prior instantiation, collapsing the genuinely multi-modal distribution over plausible completions to a point estimate. We present S-JEPA, which realises z as a proper stochastic latent variable for masked image prediction: a learned posterior infers z from context and target during training, while a learned context-conditioned prior approximates the distribution of plausible completions at inference, with no decoders and no reconstruction. In its deterministic limit the objective reduces to the I-JEPA loss in functional form, generalising that objective rather than strictly containing the I-JEPA model. Our central finding is that stochasticity adds capabilities, error-correlated predictive uncertainty and diverse completions, at no cost to representation quality: under matched architectures and schedules S-JEPA improves over the deterministic I-JEPA baseline and exceeds LeJEPA at matched architecture, while additionally producing spatially structured uncertainty maps and semantically diverse completions, neither of which the deterministic predictor produces.

---


### 133. [Interpretable Context-Aware Multi-Label Retinal Classification with Dual-Hub Heterogeneous Graph Neural Network](https://arxiv.org/abs/2611.09309)

**<font color=#1a73e8>作者：</font>** Proshanto Chanda, Munib Mesinovic, Tingting Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-label retinal screening requires capturing co-occurring pathologies and clinical context, yet standard multimodal fusion remains opaque. We propose a dual-hub heterogeneous graph neural network (GNN) that couples spatial fundus features and structured clinical covariates through cross-modal message passing while providing inherent interpretability. Rather than relying on post-hoc saliency approximations, our architecture exposes multi-level decision pathways during forward aggregation: spatially biased self-attention captures lesion-level patch interactions, while modality-specific graph attention coefficients explicitly quantify the contribution of visual regions and clinical risk factors to each disease node. Evaluated on the BRSET dataset (16,266 photographs from 8,524 patients), the proposed model achieves 76.1% Macro-AUPRC across seven conditions, matching or exceeding image-only (75.9%) and ResNet-50+MLP fusion (75.9%) baselines, with largest contextual gains in macular edema (+3.5%) and diabetic retinopathy (+2.1%). Codebase is available at: this https URL.

---


### 134. [Asymmetric Correspondence Learning for Lexical and Style Embeddings: Interpreting Latent Space via Acoustic Features](https://arxiv.org/abs/2611.09313)

**<font color=#1a73e8>作者：</font>** Michael Whealing, Robert Gaizauskas, Thomas Hain  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-supervised speech embeddings jointly encode lexical, speaker, and prosodic information, complicating feature isolation. We introduce Asymmetric Correspondence Learning (ACL), distilling HuBERT features into separate Acoustic Word Embeddings (AWEs) and Acoustic Style Embeddings (ASEs) via a split-latent correspondence bottleneck. Through probing and clustering evaluations on single-word utterances, we demonstrate that substantial variance from extrinsic sources remains encoded within each latent space, despite linear probing indicating the information has been stripped. Whilst the AWE space exhibits cohesive lexical clustering (AP$\approx$0.90, Fisher$\approx$6.28), linear probing on the ASE space achieves 97.9\% speaker accuracy across a diffuse topology (Fisher$\approx$1.01), yet preserves substantial lexical variance (Fisher$\approx$0.86) that remains linearly unrecoverable (0.17\%). To explain these findings, we apply group-level permutation feature importance over eGeMAPS acoustic features, finding that AWEs partition by vocal tract filters and ASEs by $F_0$ dynamics. These findings suggest that standard diagnostic benchmarks may be insufficient for verifying feature isolation, as substantial speech structure can be retained even when it remains entirely hidden from probes.

---


### 135. [Verification of Security Properties of Cryptographic Protocols](https://arxiv.org/abs/2611.09315)

**<font color=#1a73e8>作者：</font>** Simona Bernardi, Joaquín Ezpeleta  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Developing cryptographic protocols that are free from vulnerabilities is very challenging, as evidenced by numerous design flaws and implementation bugs in widely used protocols. Recent work has leveraged model checking to generate negative test cases, that is test cases that include the behavior of Dolev-Yao attacker. In this paper, we address the problem of analyzing execution traces produced by testing protocol implementations with such negative test cases. We propose a method for detecting violations of security properties by model-checking execution traces. Our approach employs a model checker based on DLTL, a Linear Temporal Logic with freeze operators, and supports automation of the testing process through pre- and post-processing steps. These steps, respectively, bridge the gap between different levels of abstraction and synthesize the results produced by the model this http URL present experimental results as a proof of concept for the feasibility of the proposed method.

---


### 136. [Keyline Detection with YOLO: Runway Perception for Vision-Based Aircraft Landing](https://arxiv.org/abs/2611.09316)

**<font color=#1a73e8>作者：</font>** Leander Fritsch, David Rügamer, Alexej Klushyn  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern object detectors can predict keypoints as per-object geometric features, but keypoints are inherently vulnerable to occlusion and truncation. Object edges can provide complementary information, often remaining observable even when partially occluded or when their defining endpoints leave the field of view. We therefore introduce object keyline detection, the task of predicting a fixed, semantically ordered set of infinite lines per object instance. Unlike the outputs of general line-segment detectors, each keyline is associated with an object instance and identified by a semantic index, providing a line-level analog of keypoints. To solve this task, we extend YOLO with keyline prediction parameterized in continuous Hesse-normal form $[\rho,\cos\theta,\sin\theta]$, and introduce Object Keyline Similarity (OKLS), which serves as an evaluation metric, target assignment signal, and regression loss. We instantiate this formulation on runway perception in vision-based landing, a motivating example containing semantic linear features that remain partially observable throughout the approach. Experiments show that our representation achieves the highest detection accuracy among four evaluated line parameterizations, and keylines integrate directly into standard YOLO heads as additional output channels without degrading keypoint performance or adding meaningful latency.

---


### 137. [Stable probabilistic emulation of partially observed dynamical systems](https://arxiv.org/abs/2611.09317)

**<font color=#1a73e8>作者：</font>** Mario Massy, Sara Shamekh, Fabrizio Falasca 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting the long-term behavior of partially observed dynamical systems such as the coupled atmosphere-ocean system is central to societal decision-making. Motivated by the success of deep learning emulators in weather forecasting, data-driven climate models represent a promising approach. However, climate emulation poses distinct challenges: models must account for unresolved fast variables introduced by unavoidable coarse-graining, reproduce long-term statistics, and remain stable over arbitrarily long rollouts and under external perturbations. These requirements motivate stochastic data-driven emulators, but modern generative models lack stability guarantees. We introduce forced-dissipative stochastic interpolants, a generative framework for learning stochastic reduced dynamics. Its architecture uses structural constraints inspired by turbulent dynamics, which provide stability by design while retaining the flexibility of stochastic interpolants to represent complex probabilistic dynamics. Building on the theory of Markov-chain stability, we establish a Foster--Lyapunov drift condition and prove geometric ergodicity for our emulator, together with stability under steady external forcing. We evaluate the framework on the two-timescale Lorenz-96 system, a prototype of partially observed multiscale turbulence. The resulting emulator remains stable over long integrations and under finite-amplitude forcing, with accurate prediction of forced responses of both the mean and variance.

---


### 138. [Recursively Self-Improving Electromagnetic Spectrum Agents: Architecture and Operation](https://arxiv.org/abs/2611.09318)

**<font color=#1a73e8>作者：</font>** Baolin Chong, Dongfang Xu, Qiaosi Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Electromagnetic spectrum agents (ESAs) must contend with changing environments and task requirements during sustained autonomous operation, yet their existing capabilities may not remain suitable for new operating conditions. This article proposes recursively self-improving electromagnetic spectrum agents (RSI-ESAs) that use operational feedback to update their capabilities and build on prior improvements. We present their architecture and editable components, and describe a self-improvement process encompassing problem diagnosis, candidate generation, validation, and inheritance. By retaining effective task versions and using modification records and diagnostic knowledge to guide subsequent updates, RSI-ESAs can accumulate task capabilities and improvement experience across successive rounds. A shared-spectrum scheduling case study illustrates improved task performance and capability accumulation over multiple improvement rounds under the tested conditions. Finally, we discuss open challenges for broader tasks and long-term operation, outlining research directions for the continued capability development of ESAs.

---


### 139. [DiffusionRef-IMU: Guide-Anchored Residual Diffusion for Cross-Location Inertial Measurement Unit Translation](https://arxiv.org/abs/2611.09323)

**<font color=#1a73e8>作者：</font>** M. M. Golam Hafiz, Safia Akter Simi, Md. Rakibul Islam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-location variation in wearable inertial measurement unit (IMU) signals complicates learning when measurements from a desired target body location are unavailable. This study proposes DiffusionRef-IMU, a two-stage cross-location translation framework in which a deterministic Direct network first estimates the target signal and a guide-anchored residual diffusion model refines only the remaining target discrepancy. The evaluation comprises five subject-disjoint activity-location composition-held-out folds, capacity-matched deterministic and flow-based residual baselines, source-only activity conditioning, computational ablation, and true zero-shot evaluation on two independent datasets. DiffusionRef-IMU with 16-step deterministic DDIM achieved a mean nRMSE of 0.087538 +/- 0.004922, compared with 0.090262 for Direct, 0.088847 for deterministic residual refinement, and 0.088417 for eight-step CompFlow, and outperformed each baseline in all five folds. Four-step DDIM retained a mean nRMSE of 0.087820 at 47.62 ms per window, providing a favourable quality-computation trade-off. Replacing ground-truth activity conditioning with a source-only activity predictor (macro-F1 0.8473) increased 16-step DiffusionRef nRMSE only to 0.088190. True zero-shot evaluation produced mixed results: DiffusionRef was marginally favourable on Grouvel2025 but remained worse than Direct on Saldaña2025. Overall, guide-anchored residual diffusion improves controlled cross-location reconstruction while revealing clear limits in zero-shot external transfer.

---


### 140. [Robust Deep Prototype Classifiers via Lipschitz Training](https://arxiv.org/abs/2611.09327)

**<font color=#1a73e8>作者：</font>** Adia Khalid Khan, Lukas Gehring, Benjamin Paaßen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Robustness and interpretability are interrelated and desirable properties of machine learning models. A model that changes its prediction under imperceptible perturbations behaves inconsistently with human-recognizable features and, hence, is not interpretable. Prototype-based classifiers such as Generalized Learning Vector Quantization address both at once. They are interpretable by construction because they make the decision by comparing the input to the prototypical example; and their hypothesis margin yields a closed form robustness certificate. However, on high-dimensional data, these shallow models need deep embedding networks to achieve high accuracy, and this voids the robustness certificate. The margin is a statement about distances in the embedding space, and an unconstrained network can map an arbitrarily small input perturbation to arbitrarily large attacks in the embedding space. We close this gap with a theorem: if the embedding network is locally L-Lipschitz around a point, and the classifier is {\epsilon}-robust around its embedding, then the full model is {\epsilon}/L-robust in the input space. Based on this, we propose a Lipschitz training scheme to achieve L-Lipschitz properties for embedding networks. We evaluate three classification heads (linear, linear Support Vector Machine, and GLVQ) crossed with two embedding networks (standard and Lipschitz-constrained) on MNIST, CIFAR-10, and Imagenette-160, under FGS, PGD and C\&W attacks. The evaluation results show that combining a prototype-based head with a Lipschitz-constrained embedding provides the strongest robustness. This suggests that the Lipschitz constraint provides an additional robustness benefit in addition to the advantage provided by the prototype-based head. Since the Lipschitz constraint is enforced by sampling rather than by construction, the reported robustness is empirical rather than certified.

---


### 141. [RegNC-Mamba3: Shared Structural Feature Learning Using Non-Causal State Space Principles for Multi-Modal Image Registration](https://arxiv.org/abs/2611.09336)

**<font color=#1a73e8>作者：</font>** Zhikang Li, Yan Wu, Xin Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The main challenge of multi-modal image registration is shared structural feature extraction with higher accuracy and lower computational complexity. Compared with a State Space Model (SSM), the State Space Principles (SSP) formulation of Mamba-3 uses a more accurate discretization with lower truncation error while maintaining linear complexity. However, vanilla SSP is designed for natural language processing (NLP) and is not directly suitable for images. To address this issue, we propose a novel non-causal SSP (NC-SSP) with shared structure awareness and develop a coarse-to-fine registration method named RegNC-Mamba3. First, NC-SSP is designed to eliminate the dependence of the integral computation on the scanning path. By combining relative-weight normalization with aggregation over all circular scan paths, NC-SSP constructs a globally hidden state without long-range decay, which provides a wider receptive field and higher efficiency than the original Mamba-3. Second, NC-SSP is modified to strengthen the extraction of cross-modal structural features. When computing hidden states and feature interactions, we construct complex-valued sequences in NC-SSP by applying learnable Log-Gabor kernels, with different orientations to each head for frequency-domain modulation. This improves the perception of shared structural information across modalities and increases both registration accuracy and quality. Experiments on VIS-SAR and VIS-IR demonstrate that RegNC-Mamba3 outperforms the compared detector-based and semi-dense multi-modal registration methods.

---


### 142. [Syn2DRE: Synergistic Dual Teacher-Student Framework for Document-level Relation Extraction](https://arxiv.org/abs/2611.09342)

**<font color=#1a73e8>作者：</font>** Khai Phan Tran, Xue Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Document-level Relation Extraction (DocRE) aims to identify relations between entities across a document but typically relies on costly large-scale annotations. While pseudo-labelling enables the use of low-quality data, existing methods often suffer from inefficiency and confirmation bias. To address these challenges, we propose Syn2DRE, a semi-supervised framework that combines self-supervised learning with cross-supervision in a lightweight teacher-student architecture to produce more reliable pseudo-labels. Additionally, we introduce a unified end-to-end training strategy to further improve efficiency of the framework. Experiments on multiple benchmarks show that Syn2DRE consistently outperforms prior state-of-the-art semi-supervised DocRE methods.

---


### 143. [Probably Safe Sim-to-Real Transfer with Lifetime Validity](https://arxiv.org/abs/2611.09344)

**<font color=#1a73e8>作者：</font>** Rohan Tangri, Jan-Peter Calliess  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present Dejavu, a method that makes sim-to-real transfer of reinforcement learning policies in constrained Markov decision processes probably safe over an unbounded sequence of policy updates. An anytime valid test using per-decision importance sampling and a betting confidence sequence certifies each candidate trained in simulation before deployment using only trajectories collected by a safe baseline policy operating in production. Simulation quality does not affect the safety guarantee, only the production sample efficiency of the method. Finally, a summable per-test failure probability yields the lifetime valid property. Empirical results across three sim-to-real benchmarks support the theoretical work.

---


### 144. [Reliable Prerequisite-Aware Learning Path Recommendation under Uncertain Knowledge Structures: Long-Horizon Evaluation and Cross-Dataset Validation](https://arxiv.org/abs/2611.09345)

**<font color=#1a73e8>作者：</font>** M. M. Golam Hafiz, A.K.M. Shahriar Emtiaz, Safia Akter Simi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning-path recommendation often depends on knowledge and prerequisite structures whose reliability is uncertain, while high accuracy in predicting the next resource does not necessarily establish reliable long-horizon path behaviour. This study develops a reliability-oriented prerequisite-aware framework that jointly examines immediate next-resource ranking, uncertain prerequisite structures, hard, soft and hybrid constraint semantics, graph robustness, and autoregressive path generation under course-level confirmatory evaluation and independent cross-dataset validation. Development used 3,187 MOOCCubeX courses, followed by a frozen confirmatory evaluation on 541 held-out courses and 37,747 transitions. The primary MOOCCubeX task is structural and course-prefix-conditioned rather than learner-personalised. Junyi provides independent structure-/hierarchy-aware external validation, uses hierarchy metadata rather than an explicit prerequisite graph and is not a zero-shot transfer setting. On the frozen MOOCCubeX evaluation, XGBoost pairwise was the strongest observed immediate ranker, with mean reciprocal rank (MRR) of 0.9048, whereas the proposed prerequisite-aware graph model achieved 0.7707. In the controlled graph-variant development ablation, the no-graph condition produced the strongest immediate ranking result, and immediate prediction showed strong dependence on permitted title/path-similarity information. Autoregressive evaluation exposed path properties not captured by one-step ranking. On Junyi, Markov achieved the strongest observed MRR of 0.4453, compared with 0.3954 for the proposed graph model, with metric-specific differences across ranking measures. Overall, immediate predictive accuracy, prerequisite-structure reliability, and long-horizon path quality should be treated as complementary rather than interchangeable evaluation dimensions in educational recommendation.

---


### 145. [When Feedback Becomes a Backdoor: Tracing Backdoor Skill Formation in Text-Space Skill Optimization](https://arxiv.org/abs/2611.09348)

**<font color=#1a73e8>作者：</font>** Louise Nayeong Koh, Yaechan Lee, Myeongjong Lee 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reference answers are a supervision channel in text-space Skill optimization, which produces reusable text artifacts called Skills that guide future agent behavior. Poisoning those answers can induce a persistent trigger-conditioned rule without giving the attacker access to the model, optimizer, or Skill file. We study this reference-feedback poisoning in SkillOpt by tracing an attacker-supplied trigger--payload mapping from reflection to held-out activation. In SearchQA, where the payload replaces a short answer, the natural attack retains an exact rule in all three seeds; each final Skill emits the payload on 200/200 triggered questions and 0/200 clean questions. In seed 42, removing the rule eliminates activation, and an in-run comparison shows similar clean accuracy to benign SkillOpt (169/200 versus 171/200). In SpreadsheetBench, where the payload requires an additional workbook edit, no natural run retains an exact rule across three seeds. Diagnostic interventions locate two successive bottlenecks: the Analyst abstracts away required literals, and, once literal preservation is enabled, edit-budget ranking can remove exact edits before candidate construction. Poisoned references can therefore create persistent backdoors, but exposure alone does not ensure that the induced rule is formed, selected, and retained.

---


### 146. [Open-world Reconstruction-based Classifier with Concept Drift Adaptation](https://arxiv.org/abs/2611.09350)

**<font color=#1a73e8>作者：</font>** Joanna Komorniczak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data stream processing has become central to modern machine learning applications, with concept drifts and novel class appearances posing the primary challenges faced by recognition methods. Adapting to concept drifts while also being able to detect novel classes and distinguish groups of unknown observations can be seen as a step towards effective method employment in an open-world setting. This work proposes a classification method that can detect and learn the distributions of new, unknown classes, as well as adapt to concept drifts once the distribution of known classes shifts. The proposed method uses the autoencoders' reconstruction errors and the KDE that models their distribution. The autoencoders incrementally adapt to the changing distributions of known classes via weight fine-tuning, resulting in continuous adjustment to evolving concepts. Conducted experiments used a diverse set of synthetic data streams, embeddings of a real-world static CIFAR dataset arranged into a stream to simulate concept drifts and the emergence of unknowns, as well as real-world datasets where novelty is observed. The methodology was compared with state-of-the-art approaches with three-criterion recognition quality assessment and resource consumption evaluation. The results indicate that the proposed method is competitive with reference approaches in stationary environments and performs best when concept drifts occur.

---


### 147. [AUTEUR: Acoustic Plan Learning for Red-Teaming Text-to-Audio Models](https://arxiv.org/abs/2611.09351)

**<font color=#1a73e8>作者：</font>** Jiashu Zhang, Jiaming He, Zheming Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated red-teaming of text-to-audio models requires test prompts that pass textual screening and expose harmful acoustic content. The central challenge is to connect the sounds produced by the target model to both reusable test generation and prompt revision. Our key idea is to represent test descriptions as structured acoustic plans that organize foreground sounds, context, and vocal attributes. To this end, we propose acoustic plan learning, a framework that learns and refines these plans using waveform feedback. We train the plan generator through supervised fine-tuning followed by reinforcement learning with audio feedback while keeping the target audio model fixed. At inference time, the same trained model generates initial plans and uses feedback to revise their context and vocal attributes while preserving the foreground. Experiments across four target systems show attack success rates of 79.4% on TangoFlux and 95.6% on Kling. The resulting test prompts also transfer across open-source and closed-source models, indicating shared acoustic vulnerabilities.

---


### 148. [Challenges, Opportunities, and Misconceptions in Neurosymbolic AI](https://arxiv.org/abs/2611.09356)

**<font color=#1a73e8>作者：</font>** Giuseppe Marra, Pierre Genevès, Meghyn Bienvenu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We examine opportunities for neurosymbolic AI alongside increasingly powerful neural models, particularly with regards to efficiency, safety and interpretability. We identify two major challenges: ensuring semantic alignment between neural and symbolic components, and managing the computational cost of symbolic inference and learning. We discuss representative methodological approaches to these challenges and address several common misconceptions concerning differentiability, independence assumptions, and scalability. This paper synthesizes perspectives developed through discussions in the Neurosymbolic Programming and Reasoning (NPR) working group at the 2026 CNRS workshop Neurosymbolic Methods and Their Applications in Data Science, rather than providing an exhaustive survey.

---


### 149. [Mitigating Covariate Shift in Behavioral Cloning via Robust Stationary Distribution Correction](https://arxiv.org/abs/2611.09371)

**<font color=#1a73e8>作者：</font>** Seokin Seo, Byung-Jun Lee, Jongmin Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider offline imitation learning (IL), which aims to train an agent to imitate from the dataset of expert demonstrations without online interaction with the environment. Behavioral Cloning (BC) has been a simple yet effective approach to offline IL, but it is also well-known to be vulnerable to the covariate shift resulting from the mismatch between the state distributions induced by the learned policy and the expert policy. Moreover, as often occurs in practice, when expert datasets are collected from an arbitrary state distribution instead of a stationary one, these shifts become more pronounced, potentially leading to substantial failures in existing IL methods. Specifically, we focus on covariate shift resulting from arbitrary state data distributions, such as biased data collection or incomplete trajectories, rather than shifts induced by changes in dynamics or noisy expert actions. In this paper, to mitigate the effect of the covariate shifts in BC, we propose DrilDICE, which utilizes a distributionally robust BC objective by employing a stationary distribution correction ratio estimation (DICE) to derive a feasible solution. We evaluate the effectiveness of our method through an extensive set of experiments covering diverse covariate shift scenarios. The results demonstrate the efficacy of the proposed approach in improving the robustness against the shifts, outperforming existing offline IL methods in such scenarios.

---


### 150. [Calibrated Uncertainty Quantification on TDC ADMET: What Can Be Resolved Across 22 Datasets?](https://arxiv.org/abs/2611.09373)

**<font color=#1a73e8>作者：</font>** Laurits Fredsgaard, Michael Riis Andersen, Mikkel N. Schmidt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Absorption, distribution, metabolism, excretion, and toxicity (ADMET) models often rely on small, heterogeneous datasets, yet their predictions may determine which compounds proceed to experimental testing. Useful evaluations must therefore assess both predictive performance and the quality of reported probabilities or intervals. We ask which common uncertainty-quantification methods perform best on the 22 Therapeutics Data Commons (TDC) ADMET datasets and what this benchmark can resolve. We compare eleven calibrated pipelines using nested five-fold cross-validation across ten chemical partitions and five model seeds. Ensemble Monte Carlo (MC) dropout has the best average rank for TDC performance, Brier score, and 90% interval score. For TDC performance, however, it is not separated from the other ensemble pipelines; for Brier and interval score, LightGBM is also not ruled out as best. LightGBM wins more individual datasets than any other method for TDC performance and Brier score, but performs poorly on several endpoints. Smaller evaluations can identify a different leader and often fail to recover the broader comparison. These results make LightGBM and an ensemble neural model complementary baselines. Comparative claims should be checked across multiple chemical partitions using statistical analyses matched to the question being asked.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-222](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
