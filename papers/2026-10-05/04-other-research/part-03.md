# 📦 其他研究 | 2026年10月05日

> 本类共 **385** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-385](./part-08.md)

---

### 101. [Sensing Instability, Adapting the Scene: A Real-Time Movement-Smoothing Design Framework for Stable VR Locomotion](https://arxiv.org/abs/2610.00643)

**<font color=#1a73e8>作者：</font>** Ramisa Fariha Joyee, M. Rasel Mahmud  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Users experience different balance challenges while standing, walking, and turning in virtual reality (VR), yet most locomotion techniques apply the same visual behavior regardless of movement state. We present a real-time movement-smoothing design framework in this paper that organizes visual adaptations according to movement-specific balance demands. The framework introduces three design strategies targeting standing, walking, and turning, illustrating how state-aware visual adaptations can support postural stability during locomotion. This paper focuses on the framework design and implementation, while a user study is planned as future work. Our work guides the development of future context-aware VR locomotion systems that better support safe and comfortable navigation.

---


### 102. [A Simple Doxastic Deontic Logic for Norm-Guided Decision Making](https://arxiv.org/abs/2610.00668)

**<font color=#1a73e8>作者：</font>** Thorsten Engesser, Agata Ciabattoni  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Making decisions despite conflicting norms and incomplete or unreliable information is a fundamental challenge for autonomous systems. We introduce a simple doxastic deontic logic for this setting: a classically reducible fragment of Chellas' Minimal Deontic Logic, extended with explicit conditional norms and combined with multi-agent KD45, so that norms can depend on agents' beliefs about both facts and norms. On this logic we define the Doxastic Norm Compliance Optimization Problem, where an agent chooses a decision minimizing weighted norm violations. We distinguish subjective optimization (relative to the agent's beliefs) from objective optimization (relative to the actual facts). We give conditions under which (i) the two coincide and (ii) optimal decision-making can be reduced to weighted partial MaxSAT in polynomial time.

---


### 103. [ORBIT-FMIB: Tracking Order-Resolved Epistatic Information Through ESM-2](https://arxiv.org/abs/2610.00672)

**<font color=#1a73e8>作者：</font>** Maryam Rahimimovassagh, Ivan Garibay, Niloofar Yousefi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Protein foundation models support mutation-effect and structural prediction, but predictive performance alone does not reveal which forms of biological interaction information remain accessible through model depth. We ask whether ESM-2 retains higher-order epistatic information as strongly as first- and second-order information across its representation hierarchy, introducing ORBIT-FMIB, a diagnostic framework combining Walsh-based interaction decomposition with subset-conditioned neural dependence estimation. The method is validated on synthetic landscapes with known interaction structure before being applied to the dense four-site GB1 fitness landscape using frozen ESM-2 representations.
An initial production run suggested ESM-2 retains higher-order epistatic information less well than lower-order information ($\Delta_{\mathrm{HO-LO}}=-0.107$). An independent replication of the complete measurement grid, under matched GPU hardware and identical critic seeds, substantially reduced this contrast ($\Delta_{\mathrm{HO-LO}}=-0.017$), and its sign was unstable across otherwise-defensible evaluation-pairing choices applied to the same trained critics ($-0.011$ to $+0.015$). We therefore do not currently have robust evidence that ESM-2 selectively loses higher-order epistatic information, nor that retention is equal across orders; the directional question remains open. The measurement protocol itself, including its documented removal of a positional-subset shortcut in pooled critics, remains validated and is unaffected by this finding. ORBIT-FMIB is offered as a diagnostic framework for probing interaction structure in protein foundation models; this study's own replication result illustrates why such probing requires adequately-powered reproducibility checks before its output is treated as a biological finding.

---


### 104. [Learning Transferable Skills using Goal-Conditioned Bisimulation](https://arxiv.org/abs/2610.00676)

**<font color=#1a73e8>作者：</font>** Mohammad Amin Abbasfar, Farbod Azimmohseni, Mohammad Hossein Rohban  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised skill discovery has emerged as a promising approach for leveraging reward-free datasets to pretrain general-purpose policies. However, current skill discovery methods either require access to expert data or exhibit limited generalization, failing to transfer effectively to previously unseen layouts. A key challenge is to learn representations that capture the temporal structure of the environment while remaining robust to variations across layouts. To address this issue, we present an objective for learning action-aware temporal representations that satisfy the functional equivariance property while preserving the local temporal structure of the environment. Building upon this embedding, we further propose unsupervised skill discovery using bisimulation, which learns transferable skills by conditioning the behavior of skills exclusively on the subset of state features that directly affect their execution. This enforces invariant behavior across different layouts, enabling skills to transfer effectively to other configurations. Finally, through comprehensive empirical evaluations, we show that skills learned in a given environment can be effectively applied to solve downstream tasks in various environment layouts, demonstrating strong out-of-distribution generalization.

---


### 105. [Curvature Under Attack in hZACH-ViT: Gauge Symmetry, Boundary Saturation, and Adversarial Failure](https://arxiv.org/abs/2610.00680)

**<font color=#1a73e8>作者：</font>** Athanasios Angelakis, Marta Gomez-Barrero  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Curvature is often treated as an intrinsic property of a representation, although its empirical effect also depends on coordinate scale, learned logit temperature, and numerical safeguards. We study this interaction in hZACH-ViT, a compact Vision Transformer with Euclidean, Poincare, and spherical prototype heads. The backbone architecture, seed-specific initialization, 50-per-class training subset, and optimization protocol are matched across three MedMNIST datasets and five seeds. At the fixed comparison curvature $c=1$, Poincare has the lowest class-macro PGD attack-success rate in all 12 dataset-budget cells and under a stronger CE+DLR multi-restart attack on all three datasets, but it also has the lowest clean MacroF1. An end-to-end curvature intervention changes the interpretation. Reducing Poincare curvature to $c=0.1$ improves clean MacroF1 in every one of the 15 paired seed-dataset comparisons and removes hard boundary clipping, yet on OrganAMNIST it increases strong attack success from $89.7\%$ to $99.3\%$ (paired difference $+9.57$ points; 95\% hierarchical bootstrap CI $[+5.52,+14.03]$). At $c=1$, $40$-$47\%$ of clean Poincare features are hard-clipped, the radial Jacobian of the inherited map is nearly zero, and dimensionless attack trajectories are unusually long and inefficient. The spherical head provides a control: its curvature change is an exact scale gauge to floating-point precision and produces much smaller attack differences. These results do not establish intrinsic hyperbolic robustness. They identify an implementation-sensitive regime in which curvature, scale, and proximity to the Poincare boundary jointly organize clean recognition and adversarial representation motion.

---


### 106. [Grand Canonical Generators](https://arxiv.org/abs/2610.00683)

**<font color=#1a73e8>作者：</font>** Andreas Burger, Malte Franke, Luka Mucko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Grand Canonical Generators (GCG), a generative framework that extends Boltzmann generators to the grand canonical ensemble. We present two designs. The first conditions a variable-size generative model on the chemical potential, sampling particle number and configuration jointly. The second factorizes the grand canonical distribution into a particle-number distribution and the corresponding canonical Boltzmann density. This factorized formulation can use any existing Boltzmann generator for the canonical component, encodes the known linear chemical-potential dependence analytically, and yields a tractable likelihood that supports self-normalized importance sampling (SNIS). Empirically, GCG accurately reproduces grand canonical observables on a Lennard--Jones fluid and methane adsorption in a zeolite, demonstrating generalization across chemical potentials and correction via SNIS and grand canonical Monte Carlo.

---


### 107. [SemanTok: Predictable Semantic Tokens for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2610.00686)

**<font color=#1a73e8>作者：</font>** Mikhail Dereviannykh, Vikram Voleti, Simon Donne 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video-based world models pair the scalability of autoregressive (AR) prediction with the visual quality of diffusion models. The choice of scene tokenizer is paramount for the optimal performance of each of these, both in terms of fidelity and semantics. Flexible-length, coarse-to-fine tokenizers yield exactly that: the first coarse tokens carry the clip's global semantics while later tokens further specify details. Existing flexible tokenizers only apply a representation-alignment (REPA) loss on early decoder hidden states, a target the decoder can partly meet from its noised input instead. We introduce SemanTok, a flexible video tokenizer that feeds frozen DINO features into its encoder and adds lightweight heads that reconstruct them from each retained token prefix alone. SemanTok achieves high semantic alignment and video fidelity at every AR model size: a 201M SemanTok AR model matches or beats a VideoFlexTok AR model $3.4\times$ its size, and larger SemanTok AR models further improve fidelity. It keeps semantic alignment on out-of-distribution classes and gives the decoder higher semantic alignment at every noise level, including pure noise. It performs well in both reconstruction and generation, and its short token prefixes are cheaper to predict and give better generation fidelity, with pixel detail deferred to later tokens.

---


### 108. [Soundwich: Video Generation with Layered and Controllable Audio](https://arxiv.org/abs/2610.00691)

**<font color=#1a73e8>作者：</font>** Zhuo Ning, AmirHossein Naghi Razlighi, Sagi Polaczek 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent joint audio-video generative models can synthesize realistic videos with synchronized sound, but typically generate audio as a single mixed track. This limits source-level control and differs from practical audiovisual workflows, where speech, music, sound effects, and ambient sounds are represented as separate editable tracks. We introduce Soundwich, a training-free framework that transforms a frozen joint audio-video flow-matching model into a generator of multiple synchronized, independently editable audio stems coupled to a shared video. Soundwich generates separate audio stems with explicit control over their temporal activity. To keep separately generated sounds coherent, we introduce a shared scene representation that communicates global audiovisual context across stems while preserving their source-level separation. We further route cross-modal interactions between each audio stem and its corresponding visual source, improving audiovisual consistency. The resulting stems remain synchronized with the video and can be independently retimed, muted, replaced, or remixed. Experiments and human evaluations show improved temporal control, source separation, and naturalness, while enabling flexible source-level editing within coherent audiovisual generation. Code is available at this https URL.

---


### 109. [FedMAD: Modulation-Aware Directional Aggregation for Federated Learning in Remote Sensing Image Classification](https://arxiv.org/abs/2610.00693)

**<font color=#1a73e8>作者：</font>** Barış Büyüktaş, Begüm Demir  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) has recently attracted increasing attention in remote sensing (RS) since it enables collaborative model training across decentralized RS image archives without requiring direct access to local data. However, FL performance significantly degrades when the data distributions between clients are heterogeneous, which often occurs due to geographical differences, seasonal changes, and varying image acquisition and atmospheric conditions. To address this challenge, in this letter, we propose a novel personalized FL framework (denoted as FedMAD) for RS image classification problems. The proposed framework separates globally shared representation parameters from client-specific adaptation parameters to preserve client-specific features while maintaining globally transferable representations. This is achieved by integrating lightweight modulation modules and local batch normalization layers into the backbone network. Although globally shared parameters are collaboratively optimized between clients, client-specific parameters remain local to preserve domain-specific feature characteristics. In addition, FedMAD introduces a modulation-aware directional aggregation strategy that dynamically adjusts the importance of aggregation for each client according to the alignment of local modulation updates. This allows the global optimization process to suppress conflicting client updates originating from heterogeneous data distributions while enhancing the contribution of clients with consistent adaptation behaviors. The experimental results obtained on the BigEarthNet-S2 and EuroSAT datasets demonstrate the effectiveness of FedMAD compared to state-of-the-art FL algorithms under heterogeneous RS data distributions. The code of the proposed framework will be publicly available at this https URL.

---


### 110. [Progressive-Resolution Secure Aggregation for Federated Learning](https://arxiv.org/abs/2610.00695)

**<font color=#1a73e8>作者：</font>** Seyed Mohammad Azimi-Abarghouyi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Secure aggregation lets a server recover an aggregate of client updates without observing any individual update, but conventional protocols fix the aggregate precision when clients upload. We introduce and formulate a new progressive-resolution secure-aggregation functionality in which clients upload once and successively finer resolutions of the same aggregate can later be authorized without renewed client participation. To realize this functionality, we propose progressive-resolution secure aggregation (PSA): each clipped, dithered update is represented by compatible nested-lattice digits; separately releasable layers are protected by secure aggregation and an additional aggregate pad that remains unavailable to the server until a non-colluding release controller authorizes that layer.

---


### 111. [Meta-Multi-Agent Reinforcement Learning for Fast Adaptation of Interactive Policies with Applications to Autonomous Driving](https://arxiv.org/abs/2610.00705)

**<font color=#1a73e8>作者：</font>** Huiwen Yan, Kyriakos G. Vamvoudakis, Mushuang Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper develops a meta-multi-agent reinforcement learning (meta-MARL) framework to enable fast adaptation of interactive policies in a multi-agent system (MAS). Meta-reinforcement learning (meta-RL) enables agents to rapidly adapt to new tasks/environments using a bi-level optimization mechanism. However, existing meta-RL generally focuses on single-agent systems. Extending these frameworks and algorithms to multi-agent systems poses additional challenges, as tasks are characterized by not only the environment but also agents' strategic interactions. To address these challenges, we model multi-agent reinforcement learning (MARL) problems as Markov games (MGs) and develop a meta-MARL framework for rapid interactive policy adaptation across a distribution of MGs. A new concept, called meta-NE, is defined to describe the desired solution concept in a meta-MARL problem. Sufficient conditions for the equivalence between a meta-NE and a stationary point of the gradient-play-based meta-MARL algorithm are established. Our evaluation on autonomous-driving tasks demonstrates that the proposed meta-MARL method achieves faster adaptation than pretrained MARL baselines, validating the effectiveness of our framework.

---


### 112. [Beyond Unimodal Bases: Pullback Geometry for Multimodal Data](https://arxiv.org/abs/2610.00708)

**<font color=#1a73e8>作者：</font>** Honglei Brinkmann, Lucas Ng, Georgios Batzolis 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven Riemannian geometry provides nonlinear interpolation and geometric representations of high-dimensional data. For these operations to be statistically meaningful, paths between observations should preferentially traverse high-likelihood regions. Existing scalable pullback constructions typically use a unimodal Gaussian latent distribution, assuming that the data reside close to a single manifold. For multimodal data, mapping separated modes or local structures into one Gaussian region can require substantial transport deformation and compromise the resulting geometry.
We introduce a pullback geometry for data supported on mixtures of manifolds. Using a latent Gaussian mixture, we define its Riemannian metric as the matrix square of the responsibility-weighted expected component precision. The metric is smooth and positive definite and recovers the existing Gaussian construction in the single-component limit. For structured overlapping mixtures, we establish conditions under which the log-density is concave along geodesics, providing a formal connection between the proposed geometry and paths through high-likelihood regions, and derive the corresponding local curvature relations.
We instantiate this geometry in a normalizing flow with adaptive mixture learning, allowing the number of active components to emerge from the data and supporting component-wise reconstruction and local effective-dimension estimation. Experiments on synthetic geometric data, a controlled multi-view image setting with a known reference trajectory, and MNIST show reduced transport distortion, competitive path support, close reference-trajectory recovery, and improved interpolation realism. These results extend scalable pullback geometry beyond datasets that reside close to a single manifold while retaining tractable and interpretable local structure.

---


### 113. [WOMBAT: Whitebox Oracle for Molecular Benchmarking and Attribution Testing](https://arxiv.org/abs/2610.00713)

**<font color=#1a73e8>作者：</font>** Dominik Matuszek, Bartosz Zieliński, Tomasz Danel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a graph neural network (GNN) explainer produces an unexpected attribution on a molecule, the attribution alone cannot reveal whether the explainer has failed or the model has learned a shortcut. We introduce WOMBAT, a benchmark of 14 whitebox GNNs, each with message-passing weights set by hand to detect a specific SMARTS motif. Each model's decision rule is known by construction, providing attribution ground truth against which explainer errors can be identified and studied. We validate the models on millions of PubChem molecules and evaluate post-hoc explainers including GNNExplainer, PGExplainer, and Integrated Gradients. Guided by our qualitative analysis, we construct a model that causes Integrated Gradients to spread attribution across the graph, even though the model reliably detects the intended motif. We release the dataset, models, and evaluation code to help researchers in the development of newer XAI tools for GNNs.

---


### 114. [JEPA-TTT: Persistent Test-Time Training of Latent World Models for Planning under Dynamics Shifts](https://arxiv.org/abs/2610.00722)

**<font color=#1a73e8>作者：</font>** Zheyuan Zhang, Suyu Ye, Nakul Agarwal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models enable agents to plan by predicting future states of the environment, but their predictions can become unreliable when test-time dynamics differ from those seen during training. We present JEPA-TTT, which adapts the latent dynamics predictor of a pretrained action-conditioned Joint-Embedding Predictive Architecture world model throughout test time. Self-supervised updates accumulate across episodes, while the visual encoder and reward head remain fixed, preserving the pretrained representation and task objective. Planning requires neither a goal image nor online environment reward. JEPA-TTT uses dense replay, which forms prediction windows at every temporal offset, retains them in a growing buffer, and samples minibatches from that buffer for predictor updates. Across eight dynamics shifts in four continuous-control environments, JEPA-TTT improves planning on every shift. After 500 test-time episodes, it reduces autoregressive latent prediction error by 83% on average and improves planning performance by 153% over the frozen JEPA world model. These results show that persistent self-supervised test-time training can adapt a pretrained latent world model under changed dynamics.

---


### 115. [Reward as Observation: Learning Reward-Based Policies for Rapid Adaptation](https://arxiv.org/abs/2610.00729)

**<font color=#1a73e8>作者：</font>** Morgan Byrd, Maks Sorokin, Robert Wright 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper explores a reward-based policy to achieve zero-shot transfer between source and target environments with completely different observation spaces. While humans can demonstrate impressive adaptation capabilities, deep neural network policies often struggle to adapt to a new environment and require a considerable amount of samples for successful transfer. Instead, we propose a novel reward-based policy only conditioned on rewards and actions, enabling zero-shot adaptation to new environments with completely different observations. We discuss the challenges and feasibility of a reward-based policy and then propose a practical algorithm for training. We demonstrate that a reward policy can be trained within three different environments, Pointmass, Cartpole, and 2D Car Racing, and transferred to completely different observations, such as different color palettes or 3D rendering, or Stretch robot navigation in Habitat-Sim, in a zero-shot manner. We also demonstrate that a reward-based policy can further guide the training of an observation-based policy in the target environment.

---


### 116. [Reformulation-Contrastive Learning for Mixed Integer Programs](https://arxiv.org/abs/2610.00730)

**<font color=#1a73e8>作者：</font>** Ousema Bouaneni, Mathis Le Bail, Clément Elliker 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixed-integer linear programs (MILP) model many real-world decision problems, motivating machine-learning methods that exploit recurring structure to accelerate MILP solving. MILPs can admit many equivalent formulations: integrality-preserving changes of variables and the addition of redundant constraints can alter their formulations while preserving the optimization problem. We leverage these reformulations as a source of self-supervision for learning general-purpose representations of MILP variables and constraints. We characterize the affine reformulations that are valid for every input instance, and distinguish re-descriptions, which leave variables unchanged, from substitutions, which transform them predictably. Building on equivariant self-supervised learning, we introduce ReMILP (reformulation-contrastive MILP representation learning), which jointly trains a graph neural network and a hypernetwork to predict how variable embeddings transform under changes of variables. Without solver-derived labels, ReMILP learns representations that exhibit the intended invariance and equivariance on unseen problem classes. Across binary solution, constraint activity and integrality gap prediction, these representations carry task-relevant information when frozen and provide a useful initialization for fine-tuning.

---


### 117. [Personalized Image Generation with Reasoning and Reflection](https://arxiv.org/abs/2610.00737)

**<font color=#1a73e8>作者：</font>** Bo Ni, Ngoc N. Tran, Qinwen Ge 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalized image generation has remained narrowly focused on conditional synthesis from curated visual exemplars, rather than capturing who a user is. In practice, however, a user's personal context is much richer, comprising reviews, posts, images, captions, and metadata accumulated over time. A truly personalized generator should leverage this history to produce images aligned with the user's lifestyle and aesthetic preferences. To this end, we introduce the first unified benchmark for personalized image generation from user histories. The benchmark comprises two complementary tasks and a multi-axis evaluation protocol that assesses target fidelity, visual quality, user distinguishability, semantic alignment with the user's history, and task-specific utility. Grounded in real-world e-commerce and social media settings, the benchmark includes: (1) Personalized Scene Generation, which places a given object in a scene that reflects a user's preferences and lifestyle, motivated by personalized product presentation; and (2) Personalized Creative Generation, which generates a novel image on a specified topic that is faithful to a user's aesthetic and visual identity, motivated by social media content creation. We further propose PEARL, which couples a multimodal reasoner with a frozen image generator in an interleaved reason-reflect loop optimized with differential data reward. Across both tasks, PEARL outperforms strong baselines, achieving an average improvement of 15% across personalization metrics.

---


### 118. [What Builds the Scene? Luminance Dominates Geometry Formation in 3D Gaussian Splatting](https://arxiv.org/abs/2610.00749)

**<font color=#1a73e8>作者：</font>** Rezvan Joshaghani, Steven Cutchin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard 3D Gaussian Splatting (3DGS) learns geometry and appearance jointly from RGB supervision, making it difficult to isolate how luminance and chroma contribute to the learned representation. We study this by training models under different channel supervision, freezing their non-appearance parameters (position, scale, rotation, and opacity), and re-estimating appearance with the same solver before comparing held-out reconstruction. Across eleven benchmark scenes with four independent runs each, geometry learned from luminance alone supports held-out reconstruction 0.085 dB below RGB-trained geometry on average. If chroma is deleted from a trained model, a sufficiently expressive solver can re-fit it on the frozen geometry to the original quality or slightly better. Higher-order spherical harmonics contribute much more reconstruction quality to luminance than to chroma, improving PSNR by 1.44 dB versus 0.19 dB on average, although on mirror-like surfaces hue does still change with viewpoint. The luminance advantage is even larger when geometry is being formed. Chroma-only supervision produces geometry 3.9-5.5 dB worse than luminance-only supervision after the same appearance solve; densification explains part of this gap. Overall, geometry formation in standard 3DGS is strongly luminance-dominated but not luminance-exclusive, and much of the chromatic appearance can be recovered after spatial support has formed.

---


### 119. [Signal-Noise Factorization Isolates Nuisance Variation into Removable Subspaces](https://arxiv.org/abs/2610.00751)

**<font color=#1a73e8>作者：</font>** Sakin Kirti, Joel Zylberberg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent theoretical work identified fundamental properties of representation geometry that shape inference ability of deep neural networks. These include signal-noise factorization (SNF), the ability to segregate signal from noise, and signal-signal factorization (SSF), the ability to segregate task-specific and task-irrelevant signals. Here, we built regularizers that reinforce these two properties during training. We compared networks trained with these regularizers to $L_2$-regularized baseline networks on the CIFAR-100 classification task to understand how our regularizers shape representation geometry and impact performance on a well-known computer vision baseline. Enhancing SNF via regularization improved model performance but enhancing SSF did not. Motivated by biomedical applications, we investigated how our regularizers affected performance on the BloodMNIST dataset treated with MedMNIST-C corruptions at five severity levels, and found even larger performance gains using the SNF regularizer. To understand the mechanism by which SNF-regularization produces improved performance, we analyzed the nuisance subspaces across regularization regimes, finding that the SNF-regularized models represent noise in distinct subspaces, separate from class-relevant signal. Because this geometry is explicit, the dominant corruption-induced directions can be estimated on held-out data and projected out of the representations. This manipulation led to a substantial gain in accuracy. These results show that regularizers that enforce signal-noise factorization can produce substantial improvements on computer vision tasks that contain out-of-distribution image distortions at inference time. They also highlight how shaping representations affects model performance: isolating nuisance variables from categorical ones is more important than maintaining factorized representations of categorical variables.

---


### 120. [Increasing Width Allows Greedy Layer-wise Training to Rival End-to-End Backpropagation in Self-Supervised Learning](https://arxiv.org/abs/2610.00753)

**<font color=#1a73e8>作者：</font>** Syon Mansur, Joel Zylberberg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> End-to-end backpropagation has been the dominant mode of training in deep learning, allowing for the coordination of parameter updates across layers of a neural network. Prior studies have explored alternative -- and, in some cases, simpler -- training mechanisms, showing that they can sometimes achieve performance similar to backpropagation. However, the architectural conditions under which locally optimized networks, which avoid end-to-end backpropagation of error, can learn representations comparable to those learned through end-to-end training remain unclear. We aim to answer this question in the context of self-supervised learning, an important framework for large-scale pretraining in artificial intelligence. Here, we investigate how network width and depth affect the efficacy of greedy layer-wise and end-to-end self-supervised training in convolutional networks. We find that in wider networks, the benefits of end-to-end backpropagation over greedy layer-wise training shrink: in relatively shallow and very wide networks, we even observed higher performance in models trained with greedy layer-wise training. Subsequent analysis of the representations formed by these networks shows that very wide greedy-trained networks exhibit more favorable representational geometry than do networks trained end-to-end with backpropagation. This work shows that width can compensate for restricted credit assignment and identifies differences in representational geometry as a potential mechanism for their improved performance.

---


### 121. [Scalable Multi-Task Inverse Reinforcement Learning](https://arxiv.org/abs/2610.00758)

**<font color=#1a73e8>作者：</font>** Allen Tran, Jia Wan, Nathan Kallus 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> By learning transferable rewards, inverse reinforcement learning (IRL) enables counterfactual evaluation of agents under modified environments. Such transfer places strict requirements on coverage since target environments affect agents' state occupancy. We propose a multi-task IRL method that pools data across multiple agents with different rewards in the same environment under a low-rank assumption. In addition to alleviating coverage requirements, so each task need not visit every state as long as others do, the method offers scalable evaluation of multiple tasks under new environments as computationally intensive planning scales with rank rather than the number of tasks. We provide finite sample guarantees on reward recovery and on policy learning in new environments. Experiments show our method is robust to limited coverage, recovers rewards on and off of each task's support, transfers to target environments at lower regret than baselines, with its computational advantage over per-task methods widening as tasks grow.

---


### 122. [Crossing the Cyber Divide: Sim-to-Sim and Sim-to-Real Transfer for RL Agents](https://arxiv.org/abs/2610.00759)

**<font color=#1a73e8>作者：</font>** Sabrina Saika, Yinuo Du, Aritran Piplai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber attack agents are typically trained and evaluated within a single simulator, making it unclear whether learned policies transfer beyond the environments in which they were developed. This limitation hinders both deployment and fair comparison, as cyber simulators differ substantially in their state representations, observation models, and action spaces. In this paper, we study policy transfer across cyber environments and argue that simulator-to-simulator and simulator-to-real transfer can be viewed as instances of the same underlying alignment problem. We propose a framework that separates state alignment from action translation, enabling a policy trained in one environment to operate in another without retraining. We evaluate transfer across four cyber platforms, CyberBattleSim, NetSecGame, CyberWheel, and NASim, including emulated deployments in NASim. Our experiments show that zero-shot transfer is feasible, fully preserving source-policy performance in closely aligned environments and achieving 45.2% win rates when transferring policies whose source performance is 60.5%. In emulated virtual machine environments, transferred policies exhibit a Jensen-Shannon divergence of 0.085 from native policies, indicating strong behavioral similarity. Code and benchmarks are available at: this https URL.

---


### 123. [Pre-training interventions, ex post facto: Grafting model beliefs across checkpoints](https://arxiv.org/abs/2610.00767)

**<font color=#1a73e8>作者：</font>** Peter Nutter, Dani Roytburg, Clément Dumas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-training interventions are critical to alignment research, since beliefs formed during pre-training shape how a model generalizes from later training. One recently popular technique for such interventions is synthetic document fine-tuning (SDF), which aims to alter what the model believes. Ideally, synthetic documents would be mixed into pre- or mid-training, but every change to a pre-training corpus must be followed by a full post-training run before its effect can be measured, making iteration slow and expensive. Common practice instead applies SDF to an already post-trained model. This is known to leave artifacts and degrade capabilities, and, as we show, it makes the model treat fabricated entities unrelated to the documents as real, a failure we call reality drift. We propose grafting: train the SDF adapter on the pre-trained checkpoint, then add the learned weight update to the post-trained model, which approximates the faithful approach while reusing the existing post-training. We demonstrate this by installing false facts, training misaligned model organisms and applying a constitutional mid-training intervention, across model families up to 284B parameters. Grafting installs the target belief as strongly as SDF on the post-trained model while reducing both reality drift and the loss of preference coherence by more than half on average, and it stays closer to a faithful mid-training run. Because grafting requires no post-training, the same adapter can be applied to any later checkpoint, enabling researchers to iterate quickly on pre-training interventions at the cost of a single fine-tuning run.

---


### 124. [Localizing Transfer Between Memorization Tasks](https://arxiv.org/abs/2610.00771)

**<font color=#1a73e8>作者：</font>** Yimiao Yu, Florentin Guth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central puzzle in transfer learning is why pre-training on one task can accelerate training or improve performance on another task, and what mechanisms underlie this transfer. In this work, we examine the transfer between memorization tasks of random input-output mappings. We find two surprising transfer patterns: equivalent transfer, where each additional pre-training epoch saves approximately one downstream fine-tuning epoch; and non-equivalent transfer, where pre-training on a mismatched task can be even more efficient than directly training on the downstream task itself. Through ablation experiments, we decompose and localize the transfer into two separate effects: a "trivial" magnitude-driven transfer in the last layer, and a "non-trivial" structure-driven transfer, partially attributable to the covariance of the other layers. These results advance our understanding of the underlying mechanisms of transfer learning and have the potential to lead to principled pre-training strategies.

---


### 125. [Learning Goal-Reaching Quasimetric Geometry From Finite-Time Reachability](https://arxiv.org/abs/2610.00778)

**<font color=#1a73e8>作者：</font>** Daisuke Yamada, Travis Pence, Vikas Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In goal-conditioned reinforcement learning (GCRL), quasimetric learning models goal-reaching costs as quasimetric distances, connecting local constraints to global value geometry. Its local constraints, however, should reflect the direction- dependent effects of control composition over a finite horizon together with environmental feasibility. We propose ReQRL, which constrains the critic's value gradients through finite-horizon reachability. Drawing on state-constrained optimal control, we decouple dynamical reachability from boundary geometry, estimating both from data. On OGBench, our method outperforms or rivals existing quasimetric approaches and other offline GCRL methods.

---


### 126. [Made to Measure: Designing Image Watermarks to Specification](https://arxiv.org/abs/2610.00780)

**<font color=#1a73e8>作者：</font>** Mingzhe Li, Yuefeng Peng, Kejing Xia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Image watermarking supports provenance and attribution by embedding verifiable identity information into images. Practical deployments, however, must jointly satisfy requirements for attack resistance, false-positive rate (FPR), image quality, and latency. Existing watermarking methods are robust to different classes of transformations, so combining complementary methods can provide broader protection than any single watermark. Such composition is challenging, as additional fragments increase distortion and decoding cost and must share the same FPR budget. Therefore, we propose **TAILOR**, a request-conditioned watermark composition framework with three stages: (1) *offline characterization* measures fragment recovery, distortion, and runtime as response curves over embedding strength; (2) *joint configuration selection* encodes the request as an SMT model over these curves and solves for the lowest-distortion composition of fragments, strengths, order, and geometric recovery; and (3) *live calibration* validates the selected configuration on the user's images and refines predictions that fail to transfer. Experimental results across 7,321 distinct requests spanning five scenarios and 20 attack settings show that **TAILOR** achieves **96.21%** scenario-averaged request satisfaction with a mean PSNR of **41.02 dB**, outperforming existing methods in robustness while achieving consistently better image quality. Code is available at [this https URL](this https URL).

---


### 127. [VTV-FM: Flow Matching through Variational Terminal-Velocity Closure](https://arxiv.org/abs/2610.00785)

**<font color=#1a73e8>作者：</font>** Haoyang Jiang, Yuheng Li, Di Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow matching (FM) learns generative transport by fitting continuous-time motion from a simple source distribution to the data distribution. Most existing methods use first-order bridges: once a source and a target sample are paired, the path is a straight motion with constant velocity. FM with optimal transport (OT) improves the pairing, but the bridge itself remains linear, limiting its ability to model curved motion, acceleration, and changing directions. A natural remedy is to use second-order phase-space dynamics; however, learning the bridge requires target-side terminal-velocity information that static datasets do not provide. We propose Variational Terminal-Velocity Flow Matching (VTV-FM), a second-order FM framework that derives the missing velocity by minimizing acceleration energy, yielding a closed-form closure for static data. The same minimum-acceleration variational construction also defines the OT pairing cost and the acceleration targets used for training. Experiments on low-dimensional datasets, PDE-governed physical fields, and CIFAR-10 show that VTV-FM improves transport geometry and generation quality over first-order and high-order FM baselines.

---


### 128. [Enterprise Representation Simplification (ERS): Reducing Representational Complexity for Enterprise AI](https://arxiv.org/abs/2610.00791)

**<font color=#1a73e8>作者：</font>** Terry Dorsey, Kevin Huggins  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise information is represented through artifacts shaped by applications, projects, technologies, organizational boundaries, and local requirements. These structures accumulate over time, creating representational complexity that must be maintained by the enterprise and interpreted by information consumers and AI systems. This paper introduces Enterprise Representation Simplification (ERS) as reducing unnecessary representational complexity while preserving required information within a defined scope, and Enterprise Representation Complexity (ERC), a representation-neutral model for comparing complexity across representation states.
ERC characterizes representational extent through four dimensions: Representation Objects, Interactions, Behaviors, and Supporting Sources. Objects, Interactions, and Behaviors form dependent categories, while Supporting Sources characterize representation exposure. ERC is defined at representation and task levels, enabling comparison and distinguishing architectural simplification from retrieval optimization.
The paper develops two consequences of ERS. First, representational structures create lifecycle obligations for maintenance, governance, dependencies, change, enhancement, and operation. An economic model distinguishes recurring global representation cost, recurring task-level cost, and one-time transformation cost, enabling evaluation over a defined time horizon. Second, reductions in task-level ERC reduce the representational extent an AI system must identify, relate, and interpret. Text-to-SQL research provides evidence that reduced schema and reasoning complexity can improve reasoning accuracy.
ERC is not a universal complexity, performance, or cost metric. It provides measurable architectural variables for comparing representational alternatives, transformation effects, economic outcomes, and AI reasoning performance.

---


### 129. [Sapien: A Stateful Policy Engine for Autonomous AI Agents](https://arxiv.org/abs/2610.00797)

**<font color=#1a73e8>作者：</font>** Corinn Tiffany, Wen Zhang, Eugene Bagdasarian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Contextual security defenses prevent AI agents from taking rogue actions by synthesizing a task-specific policy and enforcing it on the agent's tool calls. In multi-step tasks, however, which actions are valid often depends on what the agent has already done and learned. We present Sapien, a policy engine for enforcing stateful contextual policies. A Sapien policy specifies permitted tool-call sequences using a regular expression extended with stateful predicates, deferred policy generation, and scoped semantic checks. We show that Sapien stays within a few percent of an unconstrained agent's utility. Even if the agent is fully hijacked, Sapien's policies rule out 93-95% of attacks on AgentDojo and 62-85% on Toolathlon (twice as many as tool allowlists on long-horizon tasks).

---


### 130. [Video Generation Models: A Survey of Post-Training and Alignment](https://arxiv.org/abs/2610.00812)

**<font color=#1a73e8>作者：</font>** Chaoyu Li, Xiaoyi Gu, Yogesh Kulkarni 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation has rapidly progressed from short, low-quality clips to high-resolution, long-duration sequences with complex spatiotemporal dynamics. Despite strong generative priors learned through large-scale pretraining, pretrained video models often fail to reliably follow human intent, maintain temporal coherence, or satisfy physical and safety constraints. Compared with image and text generation, alignment in video generation presents unique challenges, including error accumulation over time, motion-appearance coupling, multi-objective trade-offs, and limited supervision for temporal properties. These challenges motivate systematic post-training strategies that adapt pretrained models without retraining them from scratch. In this survey, we present the first comprehensive review of post-training and alignment in video generation models. We frame post-training as a unifying framework and distinguish between implicit alignment and explicit alignment based on how alignment signals are enforced. From this perspective, we organize existing approaches into four broad categories: supervised fine-tuning methods, self-training and distillation methods, preference- and reward-based methods, and inference-time methods. This taxonomy provides a coherent view of how alignment signals shape model behavior across both training and deployment. Beyond methodological advances, we review commonly used datasets, benchmarks, and evaluation practices, and discuss open challenges such as scalable reward design, long-horizon temporal consistency, stability-expressiveness trade-offs, and safety-aware generation. This survey aims to provide a structured conceptual foundation and practical guidance for advancing controllable and reliable video generation models.

---


### 131. [Quantifying the Impact of Ambulance Ramping: A Multi-Year Analysis of Victorian Emergency Medical Services Cases](https://arxiv.org/abs/2610.00818)

**<font color=#1a73e8>作者：</font>** Ayesha Tanveer, Khandakar Ahmed, Assefa Teshome 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ambulance ramping, the delay between hospital arrival and patient handover, is a critical operational bottleneck in Emergency Medical Services (EMS), yet its systemic magnitude and dynamics remain inadequately characterised at scale. This paper quantifies the scale, trajectory, and operational correlates of ramping across an entire statewide EMS system, analysing 2,850,575 ambulance attendances in Victoria, Australia from January 2020 to March 2024 using an Exploratory Data Analysis (EDA). After systematic preprocessing, an analytical cohort of 2,026,569 Emergency Department (ED) transports across 59 hospitals with ED and 79 Local Government Areas (LGA) was examined through interval decomposition, Pareto concentration, hourly cross-correlation, hospital arrival concurrency and priority-stratified operational comparisons. Cumulative Ambulance Hours Lost (AHL) totalled 1,491,127 hours, equivalent to approximately 96 ten-hour ambulance shift lost every day of the study window. Ten of 59 hospitals account for 57.8% of lost hours from 50.9% of cases. Annual losses rose 57% to a 2022 peak while transported demand fell 3.7%, indicating deterioration in per-case handover rather than growth in demand. Handover duration varies little with patient acuity, but rises monotonically with the number of ambulances arriving at the same hospital in the preceding hour, an effect persisting within every hour of the day. Hourly demand is moderately associated with ramping two to four hours later (r = 0.365). These findings establish the empirical preconditions for hospital-state aware ambulance routing.

---


### 132. [On-the-fly Weight Generation: A Hypernetwork Proof of Concept on ARC-1D](https://arxiv.org/abs/2610.00820)

**<font color=#1a73e8>作者：</font>** Fabio J. Fehr, Philip Torr  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> General-purpose models can adapt to many tasks from context, while specialised models can execute individual functions with less capacity. Yet obtaining such specialists requires task-specific training or adaptation. We ask whether they can instead be generated directly from a few demonstrations. Using ARC-1D as a controlled testbed, we show that individual transformations can be represented by tiny specialist models, and that a hypernetwork can generate their parameters from context. The generated parameters form a structured weight space, while the resulting specialists show partial compositional generalisation and generalisation to transformations not seen during training. In both settings, removing explicit task identifiers improves generalisation beyond the training transformations. Together, these results provide a proof of concept that few-shot task context can be compiled on-the-fly into compact executable model parameters, and that the resulting weight space can support reuse and generalisation beyond known functions.

---


### 133. [TrueMuse: A Benchmark for Data Attribution in Text-to-Music Models](https://arxiv.org/abs/2610.00835)

**<font color=#1a73e8>作者：</font>** Jiawei Yu, Jian Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-to-music generation models are trained on massive music collections, creating a growing need for data attribution methods that can quantify the contribution of individual training samples. However, existing attribution methods are difficult to rigorously evaluate due to the lack of reliable ground truth, making it challenging to reliably assess their actual effectiveness. To address this gap, we introduce TrueMuse, a controlled dataset and benchmark for text-to-music data attribution. TrueMuse is constructed by fine-tuning three diffusion-based text-to-music models on carefully curated attribution samples, whose known inclusion in fine-tuning provides controlled attribution targets for evaluation. The benchmark covers four attribution settings, spanning melodic structure, timbral characteristics, artist-level stylistic signatures, and genre-level shared patterns, and includes 133 attributes, 648 fine-tuned models, and 95,456 generated samples across two prompt types. Using TrueMuse, we systematically evaluate existing black-box attribution methods along four dimensions: fine-tuning improvement, prompt-type difficulty, multi-task training, and fine-tuning data size. Our results show that attribution remains challenging, with existing methods exhibiting substantial variation across evaluation settings, highlighting the need for more reliable and generalizable attribution methods for text-to-music generation. Code and Dataset will be released upon acceptance.

---


### 134. [Learning Multiple Timescales for Goal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2610.00849)

**<font color=#1a73e8>作者：</font>** Pedro Robles Dutenhefner, Dikshant Shehmar, Wagner Meira Jr. 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing approaches to offline goal-conditioned reinforcement learning (GCRL) struggle with long-horizon tasks. Discounting shrinks value differences between distant states until they fall below the function approximation error, leaving the agent with no signal for ranking states. Temporal abstraction, which treats k environment steps as a single transition, restores this signal at long range, but no single fixed k suits all state-goal distances: large k preserves value differences across long temporal distances while collapsing distinctions between nearby states, and small k does the reverse. We make this trade-off explicit and introduce Generalized Implicit Temporal Abstraction (GITA), which conditions a single value function on k. GITA trains one policy by aggregating advantage-weighted supervision across multiple k values, so scales assigning larger positive advantages to a state-goal pair contribute more strongly to its update. GITA does not need to choose between local resolution and long-range signal; it retains both without committing to a single k. On OGBench, GITA outperforms a broad range of offline GCRL baselines, raising average success rate across all tasks by 25 percentage points (73% relative improvement) over HIQL. It also improves over the strongest fixed-k method, OTA, by 7 percentage points (14% relative).

---


### 135. [SmoothOperator: Enhancing Representations for Fine-grained Open-set Recognition via Modulated Label Smoothing](https://arxiv.org/abs/2610.00851)

**<font color=#1a73e8>作者：</font>** Thiru Thillai Nadarasar Bahavan, Yu Xia, Sachith Seneviratne 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open Set Recognition (OSR) aims to enable models to accurately classify known classes while rejecting samples from unseen classes. A key challenge in OSR lies in the inability to model the unbounded distribution of unknown classes during training, often leading to the misclassification of samples from these classes. Rather than modeling unknowns, recent work shapes the feature space so that known classes are compact and well separated, and spherical representation learning methods have achieved strong results this way. Label smoothing has been identified as one of the key drivers of this success, yet it applies the same coefficient to every training sample, regardless of how well each sample is already embedded. We show that the spherical representation learning objectives used in OSR share a single alignment--uniformity structure in which labels enter only through the alignment term. Label smoothing therefore acts as an alignment dial, and a fixed coefficient sets this dial to the same value for every sample. We propose a plug-in, SmoothOperator (SmoothOP), which sets the smoothing coefficient of each sample from its \textbf{prominence}, an embedding-space signal measuring how clearly the sample's own class stands out against its strongest competing class. Our method integrates into four existing spherical representation learning methods at minimal training overhead. SmoothOP assigns strong smoothing to samples with high prominence, which reduces their alignment and relaxes their pull. On the Semantic Shift Benchmark, SmoothOP-augmented variants generally outperform their base objectives across datasets, degrees of semantic shift, and OSR post-processors, with gains of up to 4.7\% in AUROC, OSCR, and closed-set accuracy.

---


### 136. [Child-Adapted Structured Phonological Representations for Interpretable Speech Sound Analysis](https://arxiv.org/abs/2610.00852)

**<font color=#1a73e8>作者：</font>** Abner Hernandez, Tomás Arias Vergara, Andreas Maier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structured phonological representations provide an interpretable alternative to generic speech embeddings, but existing models are largely trained on adult speech. We adapt PhonoQ-2.0 to child speech using CHILDES-Aligned data and compare three alignment-supervision conditions (Adult, Adult+Child, and Child-only) across two initialization strategies (Adult PhonoQ and scratch). Generalization is evaluated against manual child-speech annotations. On 1,352 consonant targets from 58 typically developing children, child-speech adaptation improves voicing recognition across all supervision conditions, from 0.922 macro-F1 for Adult PhonoQ to 0.972--0.987 after adaptation. Manner is more sensitive to alignment supervision: Adult+Child MFA reaches 0.804 and 0.796, compared to approximately 0.70 under Adult MFA supervision. Place remains comparatively strong across systems (0.871--0.902), although per-class performance varies substantially. The velar-fronting contrast is preserved across all seven model variants. Longitudinal UltraPhonix analysis further reveals speaker-specific velar and post-alveolar changes that are largely preserved across models and broadly consistent with reported clinical progress.

---


### 137. [Fixing a Model That Learned Worse Cancer Means Lower Risk: Monotonic Constraints in Bladder Cancer Recurrence Prediction](https://arxiv.org/abs/2610.00858)

**<font color=#1a73e8>作者：</font>** Saram Abbas, David Thomas, Naeem Soomro 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background and Objective: Clinicians expect recurrence risk to climb with cancer severity. In a UK multicentre trial, an unconstrained XGBoost model learnt that higher tumour stage and carcinoma in situ predicted lower recurrence risk, and discrimination, calibration, and SHAP were all blind to it. We developed a counterfactual testing framework to detect this inversion and a monotonic-constraint framework to remove it without hurting performance. Methods: BOXIT enrolled 472 patients with protocol-mandated cystoscopy across 51 UK sites (2007-2012); 435 had at least two years' follow-up (153 recurrences, 35.2%). We developed a counterfactual direction test and a monotonic-constraint correction, with constraint directions drawn from the EORTC and EAU risk systems, and evaluated both against unconstrained XGBoost and logistic regression on 18 predictors (seven directed) over 50 cross-validation folds. The test worsened each patient on one directed feature at a time to check whether risk fell; SHAP direction and calibration were also assessed. Key Findings and Limitations: Tumour stage and carcinoma in situ were associated with lower recurrence, opposite to medical intuition; the unconstrained model reversed carcinoma in situ counterfactuals in 90.2% of cases and stage in 74.3%. Discrimination ($\Delta$AUC 0.005, p=0.47), calibration, and SHAP magnitude were all blind to the inversion. Monotonic constraints eliminated every violation at no cost to discrimination (0.723 vs 0.718) and outperformed EORTC (p=8.9e-16). Limitations: single trial, internal-external validation only. Conclusions and Clinical Implications: A model that had learned this inversion passed every conventional check. A counterfactual direction test, run as a single refit with pre-specified monotonic constraints, catches this failure at no cost to performance and should be routine before clinical deployment.

---


### 138. [CtrlWAM: Controllable World Action Models with Aligned Intent and Foresight](https://arxiv.org/abs/2610.00859)

**<font color=#1a73e8>作者：</font>** Chensheng Peng, Wenhao Ding, Ran Tian 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World action models (WAMs) jointly predict actions (intent) and visual future (foresight). Standard training adds noise to recorded actions and video simultaneously, but such training paradigms introduce a mismatch: perturbed actions imply counterfactual future visual, while the noised video remains tied to the GT recording. In low-noise regime, the scene geometry and even the dynamic behavior remain clearly visible from the noisy future frames despite the added noise. We present CtrlWAM, which executes perturbed actions in a simulator and pairs them with their noised visual consequences for joint WAM learning. To accommodate the different denoising requirements of video and actions, we introduce warped video--action noise schedules that aim to keep visual layout responsive as action predictions evolve. We further extend the action interface from ego-only control to a variable number of agent streams, allowing a unified model to represent predicted or commanded futures for multiple agents. Driving experiments show more accurate action forecasts, closer agreement between generated video and actions, and better following of supplied commands; robotics experiments show stronger motion fidelity and controllability. Matched controls support the benefit of off-path renders for command following and manipulation fidelity. Together, these findings contribute to a more controllable world action model. Project page: this https URL

---


### 139. [Don't Waste the Noise: Importance-Guided Perturbation Allocation under Joint Global and Local Constraints](https://arxiv.org/abs/2610.00861)

**<font color=#1a73e8>作者：</font>** Melika Shirian, Kianoosh Vadaei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial optimization under a shared $\ell_1$ budget requires deciding not only how much perturbation to use, but also where that limited budget should be spent. This allocation problem becomes particularly important when individual input coordinates are subject to local magnitude constraints, which restrict the extent to which perturbation can be concentrated on a small number of locations. We introduce an importance-guided allocation mechanism that uses a fixed clean-gradient prior to steer perturbation toward model-sensitive regions while leaving the feasible perturbation set unchanged. A centered allocation objective encourages perturbation at above-average importance locations and discourages unnecessary expenditure elsewhere, thereby redistributing rather than enlarging the available budget. Across ten robust model--dataset configurations under a common capacity-limited threat setting, the proposed method improves attack success over matched APGD- and PMA-based baselines by $2.52$ to $17.70$ percentage points. Allocation analysis shows that these gains are accompanied by substantially greater perturbation mass in high-importance regions without increased global $\ell_1$ consumption. Mechanism ablations further show that centered non-uniform redistribution provides part of the benefit, while model-derived importance yields an additional improvement. These results identify perturbation allocation as a distinct and practically relevant dimension of adversarial optimization under shared-budget, locally constrained threat models.

---


### 140. [Rethinking Data Augmentation under Covariate Shift: Invariant-Guided Diffusion and Prototype Reweighting](https://arxiv.org/abs/2610.00873)

**<font color=#1a73e8>作者：</font>** Hongyu Cao, Xinyuan Wang, Arun Vignesh Malarkkan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many industrial applications, 1) tabular data is scarce and imbalanced and thus requires synthetic expansion; 2) input distributions drift between training and deployment (covariate shift); 3) validation sets often diverge from unseen test environments; or 4) standard generative models simply mimic outdated source distributions. This learning setting limits the stability of standard augmentation and adaptation pipelines. We generalize the task under such setting as the Augmented and Weighted Learning under Covariate Shift problem (AWL-CS). AWL-CS imposes two critical challenges on existing methods: 1) misleading generative guidance where models optimize for source similarity rather than downstream task relevance, and 2) structural instability of distributional density where reweighting mechanisms overfit to noisy validation signals. To tackle these challenges, we propose IGDPR (Invariant-Guided Diffusion with Prototype Reweighting), a unified framework that synergizes stable synthesis and structural adaptation: i) To achieve task-relevant generation, we steer the diffusion sampling process using invariant potentials to ensure synthetic samples align with stable decision boundaries rather than outdated correlations. ii) To ensure stable adaptation, we develop a prototype-based reweighting strategy that assesses sample reliability through structural clusters instead of isolated points, effectively filtering validation noise. Extensive experiments on real data demonstrate our method improves data quality by augmenting the most beneficial data for robust learning.

---


### 141. [Machine Translation for Sign Languages](https://arxiv.org/abs/2610.00881)

**<font color=#1a73e8>作者：</font>** Ozge Mercanoglu Sincan, Anton Pelykh, Edward Fish 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign language machine translation has progressed substantially over the past decade, evolving from isolated sign recognition to end-to-end translation systems. Advances in pose estimation, transformer architectures, and large-scale dataset collection have driven progress, yet challenges remain. Datasets are limited compared to spoken-language resources; evaluation metrics inadequately capture the linguistic quality of output; and models must capture the simultaneous, multi-layered, and three-dimensional structure of sign languages. This manuscript provides a comprehensive review that seeks to balance technical challenges with stakeholder considerations. We examine the linguistic properties that make sign languages computationally unique, trace the evolution of recognition, translation, and production systems, and analyze ongoing technical challenges. Crucially, we address ethical considerations around data governance, community involvement, and appropriate use. Drawing on interdisciplinary perspectives spanning computer vision, sign language linguistics, and deaf studies, our analysis emphasizes that continued progress requires sustained collaboration across these fields and with deaf communities.

---


### 142. [DeBERTa-ConPara: Attack-Aware and Deployment-Realistic Detection of AI-Generated Text](https://arxiv.org/abs/2610.00883)

**<font color=#1a73e8>作者：</font>** Mohamed Mady, Yupei Li, Johannes Reschke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Robust detection of AI-generated text under deployment conditions is challenging: distribution shifts across domains and generators, adversarial perturbations of the input surface, and the absence of target-domain labels for threshold calibration all degrade detectors that perform well in-domain. We present DeBERTa-ConPara, a deployment-oriented detector combining attack-aware Unicode preprocessing with a contextual transformer encoder trained over HC3 Plus, M4, MAGE and RAID. Our central finding is that preprocessing acts in opposite directions depending on where it is applied: normalising the training corpus deduplicates it, collapsing 35.4% of RAID rows into copies of their clean siblings and deleting the adversarial supervision, whereas normalising at inference is an effective defence. A factorial varying the two placements independently identifies raw training with normalised inference as the best configuration, reaching 99.61% AUROC, 99.01% TPR@5% FPR and 96.57% TPR@1% FPR on the official RAID hidden test, alongside 93.14% average balanced accuracy across HC3 Plus and MAGE under a fixed threshold. The gain is confined to two of twelve attack classes: homoglyph and zero-width-space insertion rise from 11.05% and 1.12% to 96.98%. The same signature reproduces in a zero-shot detector of different architecture, showing the effect belongs to the attacks rather than to our model. We additionally report two negative results: semantic-invariance augmentation through paraphrasing and supervised contrastive learning (ConPara) does not improve the best configuration, and the handcrafted feature-fusion branch is inert in distribution and harmful outside it.

---


### 143. [In CEM, a World Model Is Also a Proposal Mechanism](https://arxiv.org/abs/2610.00921)

**<font color=#1a73e8>作者：</font>** Oliver Obst, Frieder Stolzenburg  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The cross-entropy method (CEM) uses world-model scores to select action sequences and fit the distribution sampled in its next iteration. A scoring error can therefore change both the present decision and the candidates considered later. We evaluate these two roles separately. Four types of predictive model generate CEM traces, and every model rescores every saved candidate pool. Executing the same candidates in the environment provides a reference elite set and proposal update.
Across twelve independently trained task-seed units on Walker and Cheetah, the pre-specified proposal distance falls from the first to the final CEM iteration in every unit. Proposal widths contract and fitted means separate relative to the remaining search width. Pairwise ranking agreement stays near chance on Walker and declines on Cheetah; elite-set agreement does not improve. This comparison shows greater variation between scorers than between pool sources on Cheetah; Walker has variation in both and in their pairings. We use the original six units to select Random nonlinear for a one-update intervention, without inspecting intervention outcomes. Replacing its first model-ranked update with an environment-ranked update lowers final realised selected-sequence cost in those six units and in six further units held out from the selection.

---


### 144. [EyeTAG: Eye Trajectory-Aware Gaze Estimation](https://arxiv.org/abs/2610.00922)

**<font color=#1a73e8>作者：</font>** Jungmin Lee, Niamat Ullah, Yoseob Han  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaze estimation under natural head-eye motion underpins applications from driver monitoring to human-computer interaction. Single-frame methods predict each frame independently, so consecutive outputs fluctuate as jitter. Multi-frame methods reduce this, but they learn motion implicitly inside appearance features, so the gaze trajectory is never an explicit variable. We propose EyeTAG (Eye Trajectory-Aware Gaze Estimation), a causal multi-frame framework built around an explicit first-order gaze prior: at each step it differentiates its own recent predictions and feeds the resulting trajectory back as a compact kinematic token. Because differencing is translation-invariant in gaze space, this token carries subject-invariant motion rather than personal gaze offsets. Face and eye streams supply visual evidence, fused by cross-attention and a causal Transformer decoder. EyeTAG reduces the mean angular error by about 1.0$^\circ$ on Gaze360 and performs on par with the strongest baseline on EVE (2.56$^\circ$ vs. 2.58$^\circ$). Within-model ablations, which keep the encoder and the rest of the architecture fixed and vary only the gaze history, show that the differential formulation, rather than temporal context alone, removes the systematic saccade bias that persists even with an absolute gaze-history prior. Our code is available at this https URL.

---


### 145. [Rate-Optimal Algorithm for Adversarial Linear CMDPs](https://arxiv.org/abs/2610.00927)

**<font color=#1a73e8>作者：</font>** Kihyun Yu, Honghao Wei, Dabeen Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study episodic adversarial linear constrained Markov decision processes (CMDPs) with unknown transitions, where both the loss and constraint functions may vary adversarially across episodes. The best previous algorithm achieves $\widetilde{\mathcal{O}}(K^{3/4})$ regret and cumulative constraint violation, leaving a gap to the optimal $\widetilde{\mathcal{O}}(\sqrt{K})$ dependence on the number of episodes $K$. We close this gap by proposing a new primal dual algorithm that achieves $\widetilde{\mathcal{O}}(\sqrt{K})$ regret and cumulative constraint violation without assuming Slater's condition. The main challenge is that learning linear CMDPs requires uniform concentration over a value function class with a controlled covering number, whereas standard techniques in constrained online learning, such as policy mixing, can make this class more complex. Our algorithm combines adaptive Follow the Regularized Leader (FTRL), contracted value estimation, and an exponential Lyapunov function. An adaptive dual regularizer offsets the dependence on the dual weights in the primal regret bound, removing the need for policy mixing. We further show that the normalization in the FTRL update bounds the policy parameters independently of the magnitudes of the dual weights, which explains why the resulting policy class remains compatible with uniform concentration. Under feature access, the computational complexity is independent of the size of the state space.

---


### 146. [Platonic Task Arithmetic](https://arxiv.org/abs/2610.00929)

**<font color=#1a73e8>作者：</font>** Junghwan Park, Woojin Cho  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Models specialized for the same task converge to similar behavior, yet the parameter updates that produce it share no common coordinate system, so weight-space task arithmetic stays confined to a single model and cannot cross architectures without a structural correspondence. Drawing on Plato's allegory of the cave, we hypothesize that these model-specific updates are shadows of one shared, model-agnostic object, which we call the platonic task vector. To make it operational for models that pair an image or audio encoder with a text encoder, we introduce Universal Task Descriptors: matrices whose shape is independent of architecture and embedding dimension, which record a task's functional effect and support addition and negation as matrix operations. Transferring a descriptor into a target means editing the target until it reproduces the descriptor on the task's unlabeled probe images and class-name prompts, requiring no per-image labels. We realize this edit in two ways. First, the descriptor factorizes into a shift field on image embeddings, so a single least-squares solve yields a linear operator that folds into the target's last layer as a weight edit; by linearity, a bank of such operators admits any composition at any strength as a signed sum. Second, a low-rank adapter trained on the same objective reaches every layer and fits compositions jointly, at the cost of one optimization per edit. Heterogeneous models share this object only partially, with a model-specific residual comparable in norm to the shared component, yet cross-model transfer still retains 74-80 percent of the gain of the target's own descriptors. Experiments across six model families, eight classification tasks, and an audio-text setting show that task knowledge transfers and composes across heterogeneous models under both realizations.

---


### 147. [Joint Branch-Space Transform Coding for Diffusion Activation Quantization with Classifier-Free Guidance](https://arxiv.org/abs/2610.00930)

**<font color=#1a73e8>作者：</font>** Mingrun Jiang, Yuejia Liu, Zishan Shao 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-training quantization for diffusion models increasingly exploits timestep, feature, and layer structure. While recent work has begun incorporating CFG structure into diffusion quantization, activation quantization still operates independently across conditional and unconditional coordinates, leaving cross-activation structure unexploited. We show that matched CFG activations form a strongly correlated two-dimensional source and that, under a fixed bit budget, the choice of branch coding basis materially affects quantization fidelity. Motivated by this observation, we introduce branch-space transform coding, which rotates matched CFG branches via an offline derived 2x2 orthogonal matrix, requiring minimal modifications to model parameters or the quantization pipeline. We further derive the Guidance-Correlation Branch Transform (GCBT), which jointly incorporates the CFG guidance direction and cross-branch second moments. Under an equal-rate quantization-noise surrogate, GCBT admits a closed-form per-layer solution without gradient optimization or angle search. Applied on top of existing diffusion PTQ methods, GCBT yields statistically significant fidelity gains in most evaluated comparisons with no statistically significant degradation, while leaving the underlying host quantization pipeline unchanged.

---


### 148. [Cybernetic and Epistemic: A Missing Vocabulary for Trustworthy Agentic Delegation](https://arxiv.org/abs/2610.00961)

**<font color=#1a73e8>作者：</font>** Jérémie Lumbroso  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As code generation is increasingly delegated to AI systems, the bottleneck is shifting from writing code to supervising the systems that write it --- a shift CS-education researchers have begun to name. This shift exposes a vocabulary gap: the field asks for "human oversight" without a working distinction between the two things language does in a delegation channel --- coordinate action (cybernetic: words succeed when the world comes to match them) and coordinate understanding (epistemic: they succeed when they answer to the world and a hearer can check that they do). The failure this names is not cybernetic language but epistemic-form language doing cybernetic work: explanation-shaped output calibrated for approval rather than truth. Oversight that checks only whether an output was approved is satisfiable by rubber-stamping; oversight that holds an agent accountable requires the reasoning behind its work be retrievable and checkable. We present three delegation episodes --- illustrations, not controlled evidence --- in which epistemic engagement proved practicable while remaining auditable, one public record where a recommendation was withdrawn on its own stated terms, and one failure case illustrating oversight that requires no reasons for its discretionary choices. We propose a criterion for agentic-system governance, alongside existing technical trust properties: every consequential choice should carry the condition under which it would have gone otherwise, in a form a third party can test. Without such a condition, a third party cannot distinguish a decision from a rubber stamp. We give the criterion an operational form --- a two-part reconstruction test scoring a delegation record by whether a second reader can predict what the agent does under a perturbation --- and a deliberation-recording convention, ORRCF, that makes the condition a required component of every recorded choice.

---


### 149. [Structure-agnostic Causal Representation Learning](https://arxiv.org/abs/2610.00968)

**<font color=#1a73e8>作者：</font>** Arman Behnam, Binghui Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal representation learning aims to discover robust features by exploiting the causal structure underlying data generation. Existing methods require specifying the causal structure a priori, yet different structures demand fundamentally incompatible invariance constraints, and misspecification leads to representations that discard predictive information. We introduce SaCRL, a framework that jointly identifies the causal structure and learns the corresponding invariant representation without prior structural knowledge. Our approach formulates structure selection as a soft optimization over candidate invariances using HSIC-based violation metrics, with adaptive weights that automatically concentrate on the achievable structure. We provide theoretical guarantees for structure identification, including under random-feature approximation, invariance satisfaction, and out-of-distribution generalization. Empirically, SaCRL recovers the true structure on synthetic and semi-synthetic Bayesian-network benchmarks, outperforms fixed-invariance baselines on Colored MNIST, achieves state-of-the-art accuracy on three DomainBed benchmarks (PACS, VLCS, OfficeHome), and degrades gracefully under structural misspecification and limited environment diversity. Code is available at: this https URL.

---


### 150. [Variational Streaming Flow: Probabilistic Forecasting in Physical Time](https://arxiv.org/abs/2610.00976)

**<font color=#1a73e8>作者：</font>** Hans Hao-Hsun Hsu, Minseon Gwak, Soon Hoe Lim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic forecasting is important for predicting complex dynamical systems because intrinsic randomness and incomplete observations can cause the same observed state to evolve into multiple plausible futures. While flow matching is a flexible approach for probabilistic forecasting, it is computationally expensive. Streaming flow (SF) reformulates this approach to model temporal evolution efficiently by learning a continuous velocity field directly in physical time. However, SF learns a deterministic velocity field. Thus, it provides only a single future trajectory for a given fixed initial state and observation history. To overcome this limitation, we introduce Variational Streaming Flow (VSF). Our approach learns a latent distribution that is conditioned on the dynamics of interest. In turn, this enables probabilistic forecasting. Importantly, we retain the computational efficiency of SF by generating in physical time. Across deterministic and stochastic dynamical systems, VSF demonstrates superior predictive accuracy and distributional fidelity. We demonstrate the advantage for both long-horizon rollouts exceeding 1,000 steps, and settings with bifurcating dynamics. Moreover, VSF can be integrated into existing Joint-Embedding Predictive Architecture (JEPA)-based world models as a plug-and-play predictor to improve temporal dynamics and goal-directed success rate in navigation, motion planning, and manipulation.

---


> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-385](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
