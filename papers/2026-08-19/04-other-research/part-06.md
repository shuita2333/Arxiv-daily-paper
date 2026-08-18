# 📦 其他研究 | 2026年08月19日

> 本类共 **435** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-435](./part-09.md)

---

### 251. [Pricing the Risk of Runtime Compression: Anytime-Valid Admission and a Served-Output Law for Compressed Serving State](https://arxiv.org/abs/2608.15810)

**<font color=#1a73e8>作者：</font>** Fanzhe Wei, Li Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Runtime compression of serving state trades quality for capacity with no priced guarantee: systems adapt precision on load signals with no soundness statement, and certified approaches budget request-level risk by a union bound over a pre-declared event count. We show the union budget exhausts on every long request in a production serving stack (100% of requests), and replace it with an anytime-valid, physically accounted ledger whose bound holds at every one of 352,333 admission calls on live traffic and which, in a pre-registered held-out confirmatory round, halves the exact-fallback rate at matched risk (0.30 -> 0.14) -- coverage is bought at a price the account states. We then price the remaining distance from the certified witness to what a user experiences: a machine-checked design law (TV <= tanh(a_q w_thr)) turns the served-TV target into a threshold knob, and a three-layer audit of its instantiation -- an operator-norm query envelope measured 1.5x from tight, a measured-ellipsoid replacement for the Cauchy-Schwarz ball that buys nothing (0.89x, held-out sound), and the gate's operating point (~700x) -- localizes the entire 1064x gap to the operating point, a price the law now states rather than an unknown. A priced bound is worth nothing on a request one has not seen, so the third link is the quantifier: exchangeable extrapolation across 80 serving histories replaces binary conformal prediction's vacuous certificates with order-statistic bounds that discriminate (0.41 against 0.51 calibration risk). All probabilistic kernels are Lean 4-checked (228 exported theorems, no sorry); which object deserves this machinery at all is settled empirically in a companion paper that adjudicates -- and rejects -- the natural alternative of certifying routing. What ships is an account: risk you can spend, a gap you can read off a law, and a bound that survives the request you have not seen.

---


### 252. [From Generation to Matching: A Development Report on Personalized Chinese Handwriting](https://arxiv.org/abs/2608.15812)

**<font color=#1a73e8>作者：</font>** Yiwei Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper documents a frozen engineering project on personalized Chinese handwriting. The project started from approximately 200 real handwriting images from one user, covering 197 unique Chinese characters, and was initially formulated as few-shot generation of unseen characters. A sequence of canonical-centered personalization routes repeatedly exposed the same conflict: increasing structural pressure made outputs more canonical, while increasing personalization could damage identity-defining strokes. The project was therefore reset around real-human character equivalence classes. A multi-writer CASIA candidate pool showed that a USER-compatible realization often already existed among valid human samples. The task consequently changed from synthesis to character-wise matching, followed by cross-writer composition into a virtual writer. The frozen system uses real-ink features, character-specific human population percentiles, top-20 candidate pruning, and greedy hardest-first whole-row selection. On the covered target set, all 197 USER characters had real-human candidates, and the 100-character evaluation subset was covered 100/100. Knowncharacter held-out comparisons included a row judged visually almost indistinguishable from genuine USER handwriting. A 60- episode stability audit placed every episode in a predefined A-like machine-proxy region, but these were not independent human A-level judgments. The final evidence supports stable practical B-level quality, with many outputs approaching A-level under the USER-defined criterion. The report records why generation became unnecessary for this case without claiming unrestricted or universal handwriting synthesis.

---


### 253. [KOALA: Koopman Operator Learning for WiFi-Based Anticipatory Hum](https://arxiv.org/abs/2608.15815)

**<font color=#1a73e8>作者：</font>** Quang-Anh N. D., Duc Pham Minh, Thao Phuong Pham 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> WiFi Channel State Information (CSI) has emerged as a privacy-preserving alternative to cameras for human pose estimation. However, existing approaches treat pose inference as an instantaneous regression problem and do not model temporal dynamics, making future motion prediction infeasible. Naively applying vision-based prediction methods compounds the estimation noise already present in CSI-derived poses, as autoregressive rollouts amplify errors at every step. We propose KOALA, the framework for human motion prediction directly from WiFi CSI, by lifting noisy CSI-derived pose sequences into a learned Koopman latent space where nonlinear dynamics become linear, enabling multi-horizon prediction via simple matrix-vector products without autoregressive iteration or error accumulation. A residual CSI-conditioned operator resolves the identity attractor problem inherent from Koopman formulations, and an anchor-delta prediction head eliminates the degenerate shortcut of copying the current pose across all horizons. To regularise the lifting and operator jointly, we introduce a Koopman Anchored Latent (KAL) loss that operates in the temporal-encoder feature space, enforcing dynamical consistency across prediction horizons without requiring contrastive, spectral, or auxiliary losses. Experiments on MM-Fi and WiPose show that KOALA achieves robust, consistent performance across both short- and long-term prediction horizons, outperforming all baselines by a substantial margin.

---


### 254. [FlowDance: Music-Driven Dance Video Generation with Parallel Pose and RGB Streams](https://arxiv.org/abs/2608.15818)

**<font color=#1a73e8>作者：</font>** Genying Li, Boda Lin, Jiachen Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Music-driven dance video synthesis aims to animate a reference person according to a given music clip. The task is challenging because it requires a model to jointly learn music-to-motion correspondence, identity-preserving human animation, temporal coherence, and visually realistic video generation. We present FlowDance, a music-driven dance video generation framework that integrates explicit motion modeling with reference-preserving visual synthesis through parallel pose and RGB streams. We further introduce timestep-aware pose injection to adapt structural guidance across denoising steps and persistent identity injection to preserve the reference appearance over long video. To support this task, we further build a popularity-curated, high-resolution in-the-wild dance video dataset with synchronized music, RGB videos, 3D body motion, camera parameters, and projected 2D pose annotations. Extensive experiments show that FlowDance achieves strong performance in both dance motion generation and music-driven dance video synthesis.

---


### 255. [QuantumPhaseNet: A Gauge-Covariant Geometric and Quantum-Spectral Theory of Semantic Concept Hierarchies with Prototype Validation of a Classical Quantum-Inspired Model](https://arxiv.org/abs/2608.15820)

**<font color=#1a73e8>作者：</font>** Kiyotaka Kasubuchi, Kazuo Fukiya  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present QuantumPhaseNet, a gauge-covariant geometric and quantum-spectral extension of Transformer representations. Context-dependent semantic states are modeled as complex amplitudes; a covariant phase rate induces a semantic wavelength used as a proxy for conceptual scale; and low-frequency graph modes define a document-level discourse direction. The theoretical part establishes local gauge invariance, unitarity of the quantum block, boundedness and conditional stability of WavePhase Attention, and a calibratable hallucination-risk formulation. We also implemented a fully offline Validation Studio for the classical quantum-inspired pipeline in Section 14.1 and evaluated the five research questions in Section 16.1 on its built-in synthetic setting (n=240, observation noise 0.22, circuit noise 0.08, five seeds). RQ1 yielded a wavelength-hierarchy Spearman correlation of 0.852 versus 0.707 for the baseline, 87.3% direction accuracy, and AUC 0.953. RQ2 achieved discourse alignment 0.933 versus 0.589 and 41.2 versus 16.2 paragraphs before drift. RQ3 achieved AUROC 0.881 versus cosine 0.765 and phase-shuffle 0.536. RQ4 achieved error-detection AUROC 0.854 versus entropy 0.634, with Brier 0.150 and ECE 0.098. RQ5 did not show quantum advantage: target probability and end-to-end cost efficiency were 25.5% and 0.107, compared with 70.7% and 0.707 for the Chebyshev classical approximation. These results provide initial synthetic evidence for the classical quantum-inspired components, but not external validity or unconditional quantum speedup.

---


### 256. [Second-Moment Memory in Coordinatewise Adam](https://arxiv.org/abs/2608.15824)

**<font color=#1a73e8>作者：</font>** Jeonseong Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adam retains a moving average of past squared gradients in its denominator, but the optimization cost of this memory is not well understood. We show that second-moment memory can itself suppress progress toward the optimum even under finite-variance stochastic gradients. For a simple two-point oracle, the expected positive normalized update is $O(M_2^{-1/2})$ after an initialization transient, where $M_2=(1-\beta_2)^{-1}$ is the second-moment memory length. We convert this directional bound, under the stated memory and stepsize scaling, into an average-stationarity lower bound of the same order on a smooth convex problem with normalized gap, smoothness, and variance. Long second-moment memory can slow optimization even when the gradient noise has finite variance.

---


### 257. [A Cognitively Motivated Multidimensional Framework for Evaluating Metaphor Explanations](https://arxiv.org/abs/2608.15828)

**<font color=#1a73e8>作者：</font>** Ana Naveriani, Jakob Suchan, Stefano Zoia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current evaluation of metaphor explanations relies mainly on holistic quality ratings, revealing little about how explanation quality is structured or where human judgments agree and diverge. We introduce a cognitively motivated framework that decomposes metaphor explanation quality into six theoretically grounded dimensions. In a dense annotation study (11,200 ratings), we find that: {\bfseries(i)} explanation quality is genuinely multidimensional; {\bfseries(ii)} annotator disagreement is systematic rather than random; and {\bfseries(iii)} the six dimensions collapse into a shared cluster and two independent axes of judgment. An exploratory feasibility study further shows that a standard automatic evaluation pipeline can recover parts of this structure, predicting the most discriminative dimensions well while its errors correlate human (dis)agreement. Together, these results suggest that multidimensional evaluation offers richer diagnostic insight than holistic ratings, and that automatic evaluators for open-ended generation tasks should be judged on how well they preserve the structure of human judgment.

---


### 258. [MITE-Net: SWaP-Optimized 4K Video Tiny Target Perception for Embodied Edge SAR](https://arxiv.org/abs/2608.15830)

**<font color=#1a73e8>作者：</font>** Mingshuo Xu, Mu Hua, Jigen Peng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time tiny target perception in high-resolution imagery is critical for embodied Search-and-Rescue (SAR) missions. However, strict Size, Weight, and Power (SWaP) constraints on edge devices like UAVs create a bottleneck: traditional image downsampling causes severe feature loss, while slice-based processing incurs prohibitive latency. To address this gap, this paper introduces a comprehensive framework encompassing a novel architecture, specialized datasets, and hardware-level benchmarks. First, we propose MITE-Net, a SWaP-optimized cascaded architecture, which couples a bio-inspired, learning-free Tiny Target Motion-Based Region Proposal Network (TTM-RPN) with a sub-0.14M-parameter R-CNN-like head. Second, to standardize 4K tiny target evaluation, we construct the SAR-Tiny Datasets by relabeling two challenging UAV datasets: SeaDroneSee-Tiny (dynamic maritime scenes, tiny targets predominantly of 64-256 pixels ) and UAVID-Tiny (cluttered urban scenes, extremely tiny targets, less than 64 pixels). Third, we benchmark against state-of-the-art YOLO models on an edge device, NVIDIA Jetson AGX Xavier, where MITE-Net directly processes 4K maritime imagery, achieving a 100\% search success rate at 30.33 FPS. Consuming merely 3.19 W (9.51 FPS/W), MITE-Net vastly outperforms YOLO baselines in target recall and energy efficiency. Conversely, UAVID-Tiny evaluations expose a compound structural limitation: the learning-free bionic front-end struggles against urban backgrounds, while the ultra-lightweight head lacks representational capacity for complex features. Ultimately, this work delivers an efficient onboard perception paradigm and a rigorous baseline guiding future end-to-end SAR architectures.

---


### 259. [CardiacMamba: Fair and Robust RGB-RF Fusion for Remote Heart Rate Estimation via State Space Modeling](https://arxiv.org/abs/2608.15831)

**<font color=#1a73e8>作者：</font>** Bo Zhao, Zheng Wu, Yiping Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote photoplethysmography (rPPG) enables non-contact heart rate (HR) monitoring from facial videos, but RGB-only methods are vulnerable to illumination changes, motion artifacts, and skin-tone-dependent optical reflectance. We propose CardiacMamba, a fair and robust RGB-RF fusion framework that integrates optical facial cues and radio-frequency cardiac motion cues through state space modeling. CardiacMamba introduces a Temporal Difference Mamba Module (TDMM) to enhance subtle RF temporal variations, a bidirectional SSM-based interaction mechanism to align heterogeneous RGB-RF dynamics, and a Channel-wise Fast Fourier Transform (CFFT) module for channel-domain spectral refinement. On the EquiPleth dataset, CardiacMamba achieves state-of-the-art performance with 0.96 bpm MAE, 3.06 bpm RMSE, and 0.97 Pearson correlation, while reducing the observed light-dark skin-tone MAE gap to 0.26 bpm and maintaining robustness under RGB degradation and RF-missing conditions

---


### 260. [The Authority Resolution Framework: A Five-Domain Ontology for Governing Who and What Decides, at Scale](https://arxiv.org/abs/2608.15832)

**<font color=#1a73e8>作者：</font>** Parviz Shariff  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI systems become increasingly capable of autonomous action, determining whether an agent is technically capable of performing an action is insufficient: the system must also determine whether the action is authorised in its context.
This paper introduces the Authority Resolution Framework (ARF), a five-domain ontology for representing and resolving authority across organisational roles and informal influence, business concepts, codified processes, machine-readable permissions and executable systems, and external real-world context. ARF defines the Authority Relation (AR) as a cross-domain primitive binding an actor, action, object, bounded context, justification chain, and a calibration measure termed the DNA-Coefficient, which captures divergence between documented authority structures and authority as practiced.
The framework provides a machine-interpretable representation of authority provenance and scope, with JSON-LD representations and knowledge-graph query patterns for authority resolution. ARF is designed to support AI agents in determining the provenance, scope and contextual validity of authority before executing consequential actions. The framework positions authority resolution as a knowledge-representation and reasoning problem at the intersection of ontology engineering, semantic AI, agentic AI and AI governance.

---


### 261. [PersonaEval: Persona-Based User Simulation for Evaluating Interactive Applications](https://arxiv.org/abs/2608.15838)

**<font color=#1a73e8>作者：</font>** Yifan Simon Liu, Qianfeng Wen, Yilan Fan 等 43 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Real user studies are important for understanding how people interact with systems under test or already deployed. In practice, however, they are often costly, time-consuming, and difficult to scale. To address these challenges, we introduce PersonaEval, a persona-based user simulation framework that approximates real-user behavior across diverse interactive settings. PersonaEval connects simulated users drawn from existing persona datasets to task-specific application interfaces and collects the interaction trajectories and outcomes. PersonaEval provides a plug-and-play evaluation workflow in which the application being evaluated can be easily changed. In this demo, we present PersonaEval on three forms of interactive applications: surveys, chatbots, and web applications. Together, these examples show that PersonaEval can support repeatable, parallelizable, and scalable evaluation across different interaction settings, while producing user-oriented feedback and task-specific behavior.

---


### 262. [Self-Supervised Auxiliary Task Discovery for Stable Reinforcement Learning in Stock Trading](https://arxiv.org/abs/2608.15841)

**<font color=#1a73e8>作者：</font>** Arishi Orra, Himanshu Choudhary, Manoj Thakur  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has gained increasing attention as a data-driven approach for stock trading. However, learning a policy that is both profitable and stable remains challenging due to non-stationary market behaviour and noisy reward signals. Auxiliary tasks are often used to improve representation learning and stabilize training, yet they are usually designed manually and depend heavily on prior assumptions about targets and prediction horizons. Such fixed designs may not remain suitable across changing market regimes. In this work, we propose a self-supervised framework that automatically discovers auxiliary tasks to support reinforcement learning for stock trading. The auxiliary tasks are formulated as General Value Functions so that their predictions enrich the learned state representation and assist policy optimization. The framework consists of two networks. The main network learns the trading policy along with the auxiliary predictions, while the secondary network generates the definitions of auxiliary tasks through learned cumulants and discount factors. These tasks are updated using a meta gradient mechanism that accounts for their long-term impact on trading performance and improves training stability. We evaluate the proposed approach across four major equity indices: DJI, FTSE, Sensex, and TAIEX. The empirical results demonstrate that automatically discovered auxiliary tasks lead to more robust learning and improved trading performance compared to existing baselines.

---


### 263. [Geometry of Forgetting: Representation Flux in Continual Learning](https://arxiv.org/abs/2608.15854)

**<font color=#1a73e8>作者：</font>** Maksim A. Kazanskii  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Catastrophic forgetting remains a fundamental obstacle to continual learning, where neural networks lose previously acquired knowledge while learning new tasks. Existing methods primarily mitigate forgetting through parameter regularization or experience replay, while the representation-space dynamics associated with forgetting remain less understood. We investigate latent representation evolution during sequential learning and introduce representation flux, a geometric measure of sample-level representation displacement across training. We show that representation flux is strongly associated with catastrophic forgetting across multiple benchmarks, with temporal analyses indicating that elevated flux can precede subsequent performance degradation. Representation displacement is also associated with confidence degradation, while complementary geometric properties provide additional information about sample-level forgetting. Motivated by these observations, we propose FlowLess-R, a representation-space regularization method that constrains replay representations relative to stored references while allowing continued learning. FlowLess-R is architecture-agnostic and integrates into replay-based methods through a representation-matching term. Experiments on SplitMNIST, SplitFashionMNIST, SplitCIFAR10, and SplitTinyImageNet show improved final average accuracy and reduced forgetting with ER, DER++, and ER-ACE. Our results identify representation flux as an informative geometric marker of forgetting and show that stabilizing latent representations provides a simple strategy for mitigating catastrophic forgetting.

---


### 264. [TransfHAR: Self-Supervised Wrist Representations for On-Demand Activity Recognition](https://arxiv.org/abs/2608.15861)

**<font color=#1a73e8>作者：</font>** Aidan Bradshaw, Riku Arakawa, Xin Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-grained wrist activity recognition can support applications such as procedural step guidance and context-aware assistance, yet acquiring labeled data for every new task, user, and activity granularity remains a bottleneck. We present TransfHAR, a self-supervised wrist IMU framework for on-demand, fine-grained activity recognition by learning transferable motion priors from global, unlabeled activities. We show that self-supervised pretraining on coarse wrist IMU activities (e.g., sitting, walking, exercise) learns motion structure rich enough to transfer to fine-grained manipulative, gestural, and procedural activities (e.g., snapping, stirring, waving) that are absent from pretraining. We implement TransfHAR as a real-time smartwatch application that lets users define and expand their own activity set for personalized recognition from only a few demonstrations. Across three offline cross-dataset evaluations, TransfHAR matches or exceeds fully supervised baselines that use complete label sets with equal or additional sensor channels, by 6.2 balanced-accuracy points on average. In an in-lab study with 10 participants each performing seven novel wrist activities, TransfHAR reaches 86.7% balanced accuracy across participants with five examples per class and 90.4% when updated from a single one-minute recording per class. These results indicate that broad self-supervised wrist pretraining provides an effective foundation for on-demand fine-grained activity recognition.

---


### 265. [Feasible and Novel Synthetic Population Generation with Tabular and Sequential Travel Attributes](https://arxiv.org/abs/2608.15867)

**<font color=#1a73e8>作者：</font>** Farbod Abbasi, Zachary Patterson, Bilal Farooq  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic populations are critical inputs for activity-based travel demand models, yet generating realistic populations from limited survey data remains challenging. Small samples miss valid attribute combinations, known as sampling zeros, and generative models may also produce infeasible structural zeros. Moreover, realistic synthetic populations must capture both static socio-demographic attributes and sequential travel behaviour, such as trip chains. This paper proposes a regularized two-stage generative framework to address these challenges, where regularization refers to additional loss terms that guide the generator toward broader valid coverage and fewer infeasible samples. In Stage 1, a Wasserstein GAN with gradient penalty is augmented with three regularization terms, IGP, LDR, and CLAP, to improve feasibility, diversity, and novelty in tabular population synthesis. In Stage 2, Transformer and LSTM-Attention models generate sequential travel attributes, including departure time, trip purpose, and travel mode, conditioned on the synthesized tabular profiles. We also introduce novelty and count-aware metrics to evaluate whether valid unseen combinations are recovered and generated in realistic proportions. Results show that regularized models outperform the vanilla WGAN-GP across feasibility, diversity, and novelty. Regularization increases feasibility by 2.1 to 3.7 percentage points and novelty by 6.6 to 10.0 percentage points, improving sampling-zero recovery without sacrificing feasibility. The F1 score improves by 6.3 to 8.6 percentage points. For sequential attributes, LSTM-Attention best matches the trip-length distribution, while Transformer achieves higher overall sequential F1, 90.6\% versus 89.1\%. Cross-stage validation confirms strong consistency between generated mobility status and generated trip chains.

---


### 266. [CoupVisor: Strategy Optimization by Round and Challenge Decision Support](https://arxiv.org/abs/2608.15868)

**<font color=#1a73e8>作者：</font>** Cris Huynh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents CoupVisor, a decision-support system for the hidden-information card game Coup. It addresses two questions: what a player should do on each turn, and when a player should challenge an opponent's claim. The system is built around a single description of game events, which is shared across manual play, replay of recorded games, simulation, belief tracking, advisor recommendations, and learning-based policies. CoupVisor estimates the chance that a claim is truthful by combining how likely each role is with how many cards the claimant still holds, which corrects a case where the very first claim of a game was flagged as suspicious despite no evidence. We compare a rule-following advisor and several learned and heuristic players across many simulated games and different opponent styles. Our main finding is that the choice of reward, whether it rewards short-term gains or ultimately winning the game, decides which learning approach performs best, and that a win-oriented reward produces a policy that outperforms all baselines.

---


### 267. [Layers Matter: Why Continual Learning Regularization Should Be Layer-Adaptive](https://arxiv.org/abs/2608.15901)

**<font color=#1a73e8>作者：</font>** Brian B. Moser, Ahmed Anwar, Tobias Christian Nauen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning regularizers like EWC fight forgetting by penalizing changes from previous-task parameters with per-parameter importance, typically diagonal Fisher values. Per-parameter looks more flexible than per-layer, but each layer's diagonal Fisher is a weak summary of its actual curvature, missing the top-eigenvalue information that controls forgetting. Adversarial bit-flip attacks and Hessian-spectrum studies show that this missing per-layer sensitivity spans orders of magnitude in neural networks. Under a block-diagonal Hessian assumption, the layer-level analogue of EWC's existing diagonal assumption, we prove three things. Forgetting decomposes as a sum of per-layer terms weighted by each layer's top Hessian eigenvalue. Diagonal-Fisher weights cannot recover this eigenvalue. For instance, two layers with identical Fisher averages can have top eigenvalues differing by a factor as large as the layer width. For the same level of forgetting, uniform regularization loses new-task performance by an amount scaling with the layer condition number. Our theoretical analysis leads to a simple recipe: protect early layers strongly, let deeper layers move. We apply this recipe to EWC and SLCA and show clear improvements in average performance and forgetting metrics.

---


### 268. [Comprehensive Benchmarking of Deep Learning Architectures for Lung Cancer Histopathology](https://arxiv.org/abs/2608.15915)

**<font color=#1a73e8>作者：</font>** Hadi Hasan, Safaa Salman, Lama Sleem 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lung cancer remains the leading cause of cancer-related mortality worldwide, while histopathological diagnosis is often affected by inter-observer variability and the substantial workload associated with manual slide examination. Although deep learning has shown considerable potential in computational pathology, comprehensive benchmarks that integrate tissue classification and region segmentation within a unified analytical framework remain limited. This study presents a two-stage deep learning framework for multi-class tissue classification and pixel-level histopathological region segmentation, accompanied by a systematic comparison of state-of-the-art architectures at each stage. For tissue classification, six models, a custom convolutional neural network, VGG16, DenseNet, MobileNetV3, a custom Vision Transformer, and YOLO11, are evaluated on a combined dataset of 39,000 images derived from LC25000 and LungHist700. The models distinguish between adenocarcinoma, squamous cell carcinoma, and normal lung tissue. YOLO11 achieves the best classification performance, with an accuracy of 98.38%, a five-fold cross-validation accuracy of 98.21 +/- 0.35%, and a macro F1-score of 0.98. For region segmentation, U-Net, ResNet-encoder U-Net, DeepLabV3+, and YOLO11-seg are evaluated using the GlaS gland segmentation benchmark. DeepLabV3+ obtains the highest Intersection over Union of 0.80 and a Dice score of 0.89, while YOLO11-seg achieves a comparable Intersection over Union of 0.79 using approximately 14x fewer parameters. The best-performing classification and segmentation models are subsequently integrated into an end-to-end framework, providing an accurate, computationally efficient, and reproducible baseline for automated histopathological image analysis.

---


### 269. [Information Geometry of Message Passing](https://arxiv.org/abs/2608.15922)

**<font color=#1a73e8>作者：</font>** Mykola Lukashchuk, Kyrylo Yemets, Alex Ledbetter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that the natural-gradient stationary condition of variational inference has an edge-local form on a Forney-style factor graph. We start from the Bethe free energy and constrain a selected edge marginal to an exponential family. At a stationary point, the natural parameter of that edge equals the sum of two projected messages, one from each incident factor. Each projected message is the natural-gradient projection of the exact belief-propagation log-message at the current receiving marginal, or equivalently, the gradient of its expectation in the so-called mean coordinates. We call the resulting scheme natural-gradient message passing (NGMP). The rule is local; each edge may carry its own exponential family, and the message a factor sends depends on the marginal that receives it. Compared with variational message passing, NGMP keeps the part of the exact message that the receiving family can represent instead of averaging the factor under the neighboring beliefs. The two coincide when the uncertainty on the edges entering a non-conjugate factor vanishes, and NGMP is more accurate when that uncertainty persists, for example, along a partially observed latent chain or when parameters are filtered through successive data batches. Experiments on Poisson smoothing, heteroskedastic regression, and hourly ETTh forecasting confirm this and show that the gain appears mainly in uncertainty calibration.

---


### 270. [Unified Pedestrian Path Prediction Using Inverse Reinforcement Learning](https://arxiv.org/abs/2608.15929)

**<font color=#1a73e8>作者：</font>** Šimon Sukup, Ariyan Bighashdel, Pavol Jancura  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pedestrian path prediction is crucial for enhancing the safety of autonomous vehicles and advanced driver-assistance systems. Previous studies explored different learning-task formulations for pedestrian path prediction and compared these formulations using shallow neural networks, but did not extend this analysis to more complex deep-learning models. This paper adapts the Spatial-Temporal Graph Attention Network (STGAT) to a unified pedestrian path prediction framework and introduces state and action definitions specific to STGAT. The resulting formulations support deterministic and stochastic policies, one-time and sequential decision-making, and reinforcement-learning algorithms including REINFORCE and proximal policy optimization. The proposed learning-task formulations improve prediction performance across the selected benchmark datasets compared with the standard supervised-learning formulation. These results demonstrate that reformulating the decision process and training objective can improve an advanced pedestrian trajectory prediction architecture and may provide a path toward improving other graph-based prediction models.

---


### 271. [The Null Token Knows: Reducing Message-Free Hallucination in ASR and NMT](https://arxiv.org/abs/2608.15940)

**<font color=#1a73e8>作者：</font>** Kirill Borodin, Vasiliy Kudryavtsev, Ivan Viakhirev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern encoder-decoder systems can produce fluent text even when their input contains no recoverable message. We study this failure in ASR and NMT through the models' reserved null tokens, asking whether the score for ending generation already carries a usable abstention signal. Across speech recognizers and translation models, we audit native null-token scores and scalar logit shifts. In Whisper, we additionally probe decoder states and compare supervised row edits with conventional external gates. The evaluated models often expose a useful abstention signal, but stock decoding does not reliably act on it. Raising the null-token score can sharply suppress fabrication, but aggressive intervention also deletes valid speech or shortens legitimate translations. These findings turn the null token into a diagnostic lens on hallucination and motivate evaluating abstention methods by both suppression and deletion costs, rather than by hallucination reduction alone.

---


### 272. [ReliaGate: Reliability Routing for Low-Stakes Wearable Stress Prediction](https://arxiv.org/abs/2608.15951)

**<font color=#1a73e8>作者：</font>** Jaden Moon, Yu Wu, Arvind Pillai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study when a wearable stress system should surface a prediction rather than change it. In low-stakes reflection and summary settings, aggregate accuracy is insufficient because withholding can reduce error while leaving some people with little or no information. We formulate fixed-label reliability routing: after a locked classifier emits a protocol-defined stress/non-stress label, a post-hoc gate surfaces that unchanged label or withholds it as unavailable. ReliaGate assembles established confidence, signal-quality/trust, agreement, train-standardized atypicality, and train-fitted geometry cues into a post-hoc correctness score. We evaluate four wearable datasets using subject-disjoint folds, validation-selected routing, paired held-out-subject intervals, and pooled and per-subject analyses. WESAD point estimates favored ReliaGate, UBFC-Phys primary coverage/risk intervals favored ReliaGate, and E4 checks were mixed. ReliaGate provides an operational framework for studying surfaced-label error, output availability, and accepted-output distribution across subjects, without revising labels or providing clinical or finite-sample risk guarantees.

---


### 273. [Solvable Sokoban Without a Solver via Diffusion](https://arxiv.org/abs/2608.15958)

**<font color=#1a73e8>作者：</font>** Sina Baghal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deciding whether a Sokoban puzzle is solvable is PSPACE-complete (Culberson, 1997): solutions can be exponentially long and there is no short certificate to check. Solvability is also a fragile property, since even a single misplaced wall can silently render an entire puzzle unsolvable.
In this work, we show that a transformer-based discrete diffusion model trained purely on tile completion, with no access to solvers, rewards, or solvability labels, achieves a solvability rate of 77.4%, with 94.5% of the remaining failures rendered solvable by removing a single wall. In other words, a global, search-heavy property follows from a local training objective: trained only to fill in masked cells, the model inherits solvability it was never trained on.
An autoregressive model factorizes as $p(c_k \mid c_1 \dots c_{k-1})$, meaning a fixed order, always conditioned on a prefix. Masked diffusion does not: it hides a random subset of cells and learns $p(c_k \mid \text{any subset})$, so at generation time it can reveal cells in any order, each one conditioned on everything already placed, wherever it sits on the board. A puzzle's difficulty comes from exactly this kind of non-local interaction, a decision in one part of the grid constraining what will work somewhere else entirely. A generator that is not locked into a single fixed order is therefore a better structural match for the problem than one that is.
The training pipeline is adapted from MD4 (Shi et al., 2024) and the dataset is DeepMind's Boxoban (Guez et al., 2019). The trained model and instructions for generating puzzles are publicly available.

---


### 274. [Beat the Counter First: A Baseline for Temporal-Graph Anomaly Detectors](https://arxiv.org/abs/2608.15965)

**<font color=#1a73e8>作者：</font>** Omair Shafi Ahmed, Zohair Shafi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Progress in streaming, edge-level graph anomaly detection (GAD) has been marked by increasingly elaborate architectures, from count-min-sketch chi square tests to memory-augmented attention networks. Yet the empirical gains attributable to this added complexity have not been systematically evaluated. We propose SimpleCount, a reference with no parameter fitting that selects one scalar feature per dataset from a fixed pool of counts, recencies, first-occurrence indicators, and count-derived transforms. We compare SimpleCount with two temporal-graph detector models and an IsoForest control fitted to the complete feature vector across five public datasets and one synthetic dataset. SimpleCount matches or exceeds SLADE on three of six datasets and exceeds IsoForest on all six. We report paired statistical tests and five-seed SLADE evaluations. SLADE requires 23 to 133x more wall-clock time than SimpleCount. On Synth-Triangle and an additional Synth-Quad probe, pre-event structural scores recover the planted signal at AUC up to 0.955, while all evaluated detector models remain near random. The benefit of complexity is dataset-dependent, and every claimed gain should be reported against a strong one-feature reference together with its compute cost.

---


### 275. [A Banach-Space Theory of Markovian Halpern Iteration for Non-Expansive Maps](https://arxiv.org/abs/2608.15966)

**<font color=#1a73e8>作者：</font>** Ege C. Kaya, Arda Fazla, M. Berk Sahin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study stochastic approximation of fixed points of a non-expansive operator when the oracle samples originate from a continuing Markovian trajectory. A direct block-minibatch implementation of Halpern iteration attains an expected last-iterate residual of order $O(\log N/N)$, but accrues a substantive complexity of $\tilde O(\epsilon^{-5})$ Markovian samples. We therefore introduce a variance-reduced Markovian PAGE-Halpern method whose refresh and same-state difference blocks are analyzed through the Poisson equation. In Hilbert spaces, the cocoercivity of $I-T$ results in an $O(\epsilon^{-3})$ sample complexity. Our main result extends this construction to a general finite-dimensional Banach space. A displacement-level Halpern bound replaces the Hilbert-space potential and yields $\tilde O(\epsilon^{-3})$ sample complexity in the original non-expansiveness norm. We also establish a high-probability guarantee with the same leading accuracy dependence by measuring the estimator in an auxiliary smooth norm. Non-smooth sup and block-sup geometries are covered through norm smoothing.

---


### 276. [BagShift: Measuring How Patch Selection Changes the Evidence Seen by Whole-Slide MIL](https://arxiv.org/abs/2608.15970)

**<font color=#1a73e8>作者：</font>** Ruicheng Yuan, Zhenxuan Zhang, Liwei Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-slide multiple-instance learning (MIL) observes only the patches admitted by its selector. Deployment can alter this selector through compute limits, tissue masking, or regional workflows, even when the patch count is unchanged. We introduce BagShift, a paired protocol that changes the selector for the same case while holding its features and predictor fixed, thereby isolating selector response from case mix. With equal 128-patch budgets, sampling across the tissue or concentrating around one coordinate exposes markedly different evidence: on PANDA, the two views reduce quadratic weighted kappa by 1.57 and 17.96 points, respectively (QWK reported on the $\times100$ scale). On CAMELYON16, lesion annotations withheld from model development show that localized views retain tumor in only 10.0\% of micrometastatic observations, and matched exposure does not consistently recover the loss. The same fixed-count stressor produces a much smaller response on external lung subtyping, although differences in relative coverage make cross-task severity descriptive. When repeated localized observations are available, unioning their patches before one nonlinear MIL pass improves PANDA QWK by 7.87 points over averaging regional predictions. Patch count specifies computation, not observed evidence; deployment evaluations should report both what a selector preserves and how repeated observations are aggregated.

---


### 277. [The Limits of Binding in Dual Encoders](https://arxiv.org/abs/2608.15971)

**<font color=#1a73e8>作者：</font>** Kin Ian Lo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dual-encoder models such as CLIP score an image-caption pair by a single inner product of two independently computed unit vectors, and fail at binding, often scoring near chance when asked to distinguish "a red car and a blue dog" from "a blue car and a red dog". We give a mathematical account of when this failure is necessary and when it is contingent. Working within the ideal-encoder framework proposed by Kang et al., we first show the relevant axioms are satisfiable, so every impossibility must enter through an added, checkable hypothesis. We then prove three such obstructions. Depth: for recursive role-binding codes the swap margin obeys an exact law $m(D) = 2b^{-D}$ in the nesting depth D, with a finite-dimension version holding up to one explicitly flagged concentration estimate; the resolvable depth grows only logarithmically in the dimension and is single-digit at CLIP scale, the nesting depth of ordinary language. Objective: architecture-free throttle theorems showing that the contrastive objective's entire reward for binding is bounded by the rate at which training contrasts a caption against its own swap, a rate that vanishes at web scale, and that exactly reversed binding costs only that rate times the mean binding margin; both are verified in simulation. Geometry: a tight smoothness-binding frontier: the closer the two swap-related captions must embed to a shared paraphrase anchor, the smaller the binding margin can be, with an exact constant. Measuring its text-only diagnostic across 18 deployed text encoders, every model sits at roughly 25-35% of its ceiling, and the induced per-item ceiling tracks SugarCrepe's subset difficulty at r = 0.99. Binding failure in deployed dual encoders is thus not a dimension or smoothness limit today, but an incentive and code-structure limit, with a proved depth ceiling that remains once those are fixed.

---


### 278. [CM-MAE: A Physics-Guided Cross-Modal Self-Supervised Learning Framework for Vision-Wireless Applications](https://arxiv.org/abs/2608.15972)

**<font color=#1a73e8>作者：</font>** Yubo Zhang, Yiyao Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synchronized camera and wireless measurements observe the same scene through different physical channels. The central difficulty is that a representation learned in one deployment can fail when viewpoint, traffic, illumination, and propagation geometry change. This paper presents CM-MAE, a self-supervised vision--wireless pretraining framework for cross-scenario representation transfer. The evaluated real-data model uses only RGB frames and the measured 64-beam received-power vector available in DeepSense 6G; it does not use ray-traced paths, calibrated depth, or beam-index labels during pretraining. Its central pretraining term is a \emph{soft contrastive alignment loss}. Instead of making the synchronized image--wireless pair the only positive pair, this loss builds a target distribution from similarities between measured beam-power profiles, so nonidentical samples with similar directional responses are not forced apart as false negatives. A masked joint decoder provides the complementary local objective by reconstructing hidden visual patches and wireless angular clusters under modality dropout. After pretraining, a differential-rate fine-tuning rule lets a new fusion head adapt quickly while the encoders move slowly. Under a sequence-disjoint DeepSense 6G protocol, adding the soft alignment loss improves a matched linear-probe transfer average from 24.88\% to 29.49\%. Mild fusion fine-tuning reaches 77.38\% Top-1 accuracy on unseen Scenarios 6--8, and optional transductive normalization adaptation reaches 78.69\%. Since the fusion setting uses the contemporaneous 64-beam power vector at inference, these results should be read as representation-transfer diagnostics, not as proactive beam-prediction or reduced-sweeping claims.

---


### 279. [Operator-Theoretic Generalization Bounds for Multitask Deep Learning](https://arxiv.org/abs/2608.15982)

**<font color=#1a73e8>作者：</font>** Mahdi Mohammadigohari, Thomas Borsani, Giuseppe Di Fatta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop operator-theoretic generalization bounds for deep multi-output function classes by representing network layers as Koopman composition operators on vector-valued reproducing kernel Hilbert spaces. In vector-valued Sobolev RKHSs, we derive Rademacher complexity bounds for invertible and width-expanding injective architectures. The estimates separate the output-coupling contribution, represented by the trace of the task matrix, from the layerwise operator norms, Sobolev symbol ratios, determinant factors, and restriction constants generated by the linear maps. We then analyze a distinct one-dimensional Brownian/Cameron--Martin regime. Using the exact anchored derivative-norm characterization of the vector-valued Brownian RKHS, we obtain layerwise bounds for domain-preserving scalar linear maps and anchored diffeomorphic activations; the corresponding factors scale as $|W_l|^{1/2}$ and $\|\sigma_l'\|_\infty^{1/2}$, respectively, and do not involve Sobolev smoothness exponents. Because the Sobolev and Brownian results concern different hypothesis spaces, neither is asserted to dominate the other uniformly. We additionally formulate shared operator learning across tasks, prove a finite-rank representer theorem, derive the exact finite-dimensional problem for squared loss, and establish a target-transfer bound when the learned operator is obtained independently of the target sample. Synthetic and MNIST studies examine stabilized Sobolev-inspired and Brownian-inspired complexity proxies; these empirical proxies are not evaluations of the proved bounds for rank-deficient architectures.

---


### 280. [Toward Optimal Second-Order Path-Length Guarantee for Adversarial Multi-Armed Bandits](https://arxiv.org/abs/2608.15996)

**<font color=#1a73e8>作者：</font>** Mengxiao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study second-order path-length regret in adversarial $K$-armed bandits against oblivious loss sequences. Bubeck et al. [2019] designed an algorithm that achieves $\widetilde{\mathcal{O}}(K+\sqrt{KQ_{\infty,1}})$ regret, where $Q_{\infty,1}$ is the first-order path length, and left open whether $\widetilde{\mathcal{O}}(\text{poly}(K)\sqrt{1+Q_{\infty,2}})$ regret is achievable under bandit feedback, where $Q_{\infty,2}$ is the second-order path length. Somewhat surprisingly, we resolve this question positively by showing that with a more involved analysis, the exact same algorithm of Bubeck et al. [2019] achieves $\mathcal{O}\left(K\log(KT)+\sqrt{K\log(KT)\bigl(1+Q_{\infty,2}\bigr)}\right)$ expected regret when $Q_{\infty,2}$ is known, where $T$ is the horizon. This matches the $\Omega(\sqrt{KQ_{\infty,2}})$ lower bound up to logarithmic factors and additive terms. We further remove the knowledge of $Q_{\infty,2}$ using an adaptive restart scheme whose path-length estimator has uniformly bounded increments.

---


### 281. [MUPA$^{2}$E: Multimodal Unified Perception with Asymmetric Attention for Emotion Assessment](https://arxiv.org/abs/2608.15999)

**<font color=#1a73e8>作者：</font>** Stefanos Gkikas, Eric Nichols, Christian Arzate Cruz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic emotion assessment can benefit from combining neural and behavioral signals, but many multimodal approaches rely on separate, modality-specific feature-extraction pipelines before fusion. This paper presents MUPA\textsuperscript{2}E, a unified perception framework that processes facial video and electroencephalography (EEG) through a single shared asymmetric-attention backbone. Facial video is represented through axis-folded frame tokens, while EEG is processed either as a raw multichannel waveform or projected into the spatial domain for multimodal fusion. The framework is evaluated on the DMER dataset under a stratified subject-independent protocol, comparing unimodal video, unimodal EEG, and fused video--EEG configurations with per-channel and merged EEG projections. Using the original recordings, with shorter trials zero-padded to match the longest duration, merged fusion at stride~$30$ achieves the highest validation performance and a test accuracy of $70.07\%$. Further analysis revealed that recording duration is unevenly distributed across the affective classes, making the padding pattern a potential classification cue. Controlling for this factor by cropping all recordings to a common duration of $20$ seconds yielded a test accuracy of $62.71\%$, providing a stricter duration-controlled assessment of the framework in which differences in recording length are removed as a potential classification cue. These findings demonstrate the feasibility of processing structurally different neural and visual signals within a compact unified architecture while highlighting the importance of controlling duration-related cues in affective datasets.

---


### 282. [Retrieval-guided Twin Fusion with Similarity-aware Contrast for Molecule-Text Alignment](https://arxiv.org/abs/2608.16005)

**<font color=#1a73e8>作者：</font>** Shunshun Gu, Shengqi Qiu, Hang Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper studies the problem of molecule-text alignment, which aims to project molecules and their textual descriptions into a joint latent space for downstream tasks including molecule search and molecular property prediction. Previous approaches typically combine graph structure mining with contrastive learning to enhance joint representation learning. However, they typically neglect fine-grained semantic relationships between substructures and texts, leading to suboptimal performance on downstream tasks. Towards this end, we propose a novel approach named Retrieval-guided Twin Fusion with Similarity-aware Contrast (RISEN) for molecule-text alignment. The core idea of RISEN is to construct a latent twin molecule for each substructure with cross-modal retrieval for semantic enhancement. In particular, for each substructure query, we retrieve relevant textual descriptions and sample several molecules that share similar descriptions of substructures. Then, we aggregate their representations via attention pooling for a twin latent representation, which would be further fused with the original substructure for representation enrichment. In addition, we measure the similarity across substructures and texts, which would further guide cross-modal contrastive learning with soft thresholding. Extensive experiments on benchmark datasets validate the superiority of the proposed RISEN in comparison with existing baselines.

---


### 283. [Spatial Temporal Synergy: Balancing Change and Invariance in Text Driven 3D Human Motion Editing](https://arxiv.org/abs/2608.16008)

**<font color=#1a73e8>作者：</font>** Shaohui Lin, Zhenwu Shi, Jingyu Gong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-driven human motion editing aims to modify existing motion sequences according to natural language instructions while maintaining the structural consistency of the original motion. Existing diffusion-based approaches struggle to balance text-responsive "change" and inertial "invariance". They often rely on coarse spatial constraints and rigid uniform time assumptions, leading to spatial motion distortions and the destruction of intrinsic physical rhythms during variable-length editing. To handle these challenges, we propose Change and Invariance Motion Editing (CIME), a unified framework that comprehensively decouples change and invariance into spatial pose and temporal rhythm dimensions. For spatial poses, our method integrates an omni-supervised positive-negative learning mechanism comprising hierarchical retrospective feature supervision, subtle motion preservation, and triplet-based semantic alignment. For temporal rhythms, we introduce the Riemannian Non-uniform Integral Manifold Mapping (RNIMM) module, which achieves high-fidelity reproduction of physical beats in the edited text via kinematics-aware non-uniform timestamps. Extensive experiments on the MotionFix and STANCE Adjustment datasets demonstrate that CIME achieves state-of-the-art performance in editing alignment and structural fidelity, validating the effectiveness of our unified architecture. Our source codes and models have been released at: this http URL

---


### 284. [Breaking the Compression Barrier: Cross-Architecture Compression Boundary Learning via Reverse Regrowth](https://arxiv.org/abs/2608.16010)

**<font color=#1a73e8>作者：</font>** Zhaocen Liu, Satvik Praveen, Yi Sheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model compression is critical for deploying networks on resource-constrained edge devices. While pruning-based methods can significantly reduce model size, they often suffer from abrupt performance collapse beyond a sparsity thresh-old, making it difficult to identify the feasible compression limit of the model. To address this challenge, we propose a boundary-Learning reverse regrowth framework, BRIDGE, that reformulates compression as a constructive boundary-search problem. Unlike forward pruning, our method first drives the model to an extremely sparse state to expose the collapse region, and then selectively regenerates the critical structure to restore performance. The proposed framework employs a hierarchical regeneration strategy, including coarse-grained layer selection and fine-grained regeneration parameter selection, to accurately identify which parameters require recovery. Experiments show that our method can recover models from the brink of collapse on both CNNs and Transformer architectures, demonstrating its architecture in-dependence. BRIDGE achieves a performance improvement of up to 1.49% in unstructured pruning and up to 4.77% in structured pruning. These results demonstrate that reverse regeneration can effectively extend the compression limit while maintaining stable performance. The source code is available at this https URL.

---


### 285. [Depth-guided Multi-view Exposure Bracketing for HDR Robot Vision](https://arxiv.org/abs/2608.16014)

**<font color=#1a73e8>作者：</font>** Jinnyeong Kim, Juhyung Choi, Woohyeok Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving reliable single-shot high dynamic range (HDR) imaging under extreme illumination conditions remains a long-standing challenge, yet no comprehensive benchmark exist for evaluating HDR perception in multi-sensor robotic systems. To fill this gap, we introduce a large-scale dataset collected via a custom robotic vision platform and an iPhone 13 Pro: 121 real-world scenes spanning modest and ultra-high dynamic range conditions, alongside 20 synthetic video sequences from the CARLA simulator. As a reference pipeline for this dataset, we propose Depth-guided Multi-view Exposure Bracketing (DMEB), a single-shot HDR method that distributes drastically different exposures across multi-view low-bit-depth cameras and fuses them via depth-guided confidence-aware fusion. Evaluations on our dataset show that DMEB establishes a strong reference point and highlight the promise of this sensor configuration for robust HDR perception in diverse multi-camera and depth sensor system.

---


### 286. [Multi-scale Decomposed Convolution Refinement Network for Visible-Infrared Person Re-Identification](https://arxiv.org/abs/2608.16015)

**<font color=#1a73e8>作者：</font>** Mingsheng Zheng, Zirui Jiang, Bo Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visible-infrared person re-identification (VI-ReID) suffers from cross-modal discrepancies and limited discriminative capabilities, leading to suboptimal recognition performance. Current approaches exhibit limitations in semantic mining, cross-modal fusion and feature constraints. To tackle these challenges, we propose MDCRNet, a Multi-scale Decomposed Convolution Refinement Network that enhances cross-modal feature learning and discriminative metric learning. Specifically, we introduce a Hierarchical Learning Module (HLM) containing four Hierarchical Decomposed Convolution Attention (HDCA) modules, each equipped with lightweight channel attention and multi-scale spatial perception blocks to capture multi-scale spatial dependencies. Moreover, we develop a Joint Discriminative Metric Loss (JDML) incorporating a novel Granularity Discriminative Loss (GDL) that simultaneously optimizes intra-identity compactness and inter-identity separability across modalities. Extensive experiments on SYSU-MM01 and RegDB datasets demonstrate that MDCRNet achieves state-of-the-art performance on both benchmarks. Code is available at this https URL.

---


### 287. [Dynamic Evidence Collection Ecosystem for Assessment Integrity and Authentic Competence](https://arxiv.org/abs/2608.16016)

**<font color=#1a73e8>作者：</font>** Rajan Kadel, Bellal Hossain, Samar Shailendra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative Artificial Intelligence (GenAI) can produce high-quality essays, code, and design artefacts, challenging the validity of conventional assessments that rely on single-point submissions and product-only grading. This paper proposes a design framework called "Dynamic Evidence Collection Ecosystem" that shifts assessment toward continuous, authentic, multi-source evidence of student learning over time. The framework collects process evidence through iterative artefacts, design logs, activity rounds, self-reflection, and peer collaboration, supported by an AI-enabled layer for learning analytics, formative feedback, and transparency. The approach is grounded in recent assessment-redesign scholarship in AI-rich contexts and aligned with contemporary views of authenticity in assessment. This paper builds on the hypothesis that academic integrity is strengthened when it is treated as an assessment design rather than as an AI detection problem. The tools have limitations and risks of use that carry academic penalties. This paper presents an implementation scenario to support institutional adoption.

---


### 288. [RagGAD: Rationale-Aware Conditional Gaussian Mixture Normalizing Flow for Unsupervised Graph Anomaly Detection](https://arxiv.org/abs/2608.16018)

**<font color=#1a73e8>作者：</font>** Junxin Lu, Jing Zhao, Shiliang Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph anomaly detection aims to identify nodes that deviate from normal behavioral patterns within graphs. However, existing methods largely rely on the homophily assumption, which makes it difficult to distinguish spurious affinities and to capture the diverse behaviors of normal nodes,limiting their robustness in complex real-world scenarios. To address this problem, we propose RagGAD, an unsupervised graph anomaly detection framework based on rationale-aware conditional Gaussian mixture normalizing flow. RagGAD introduces an adaptive rationale disentangler to disentangle stable rationales from spurious correlations within node interrelationships, and further decomposes stable rationales into robust and fragile components. The learned rationales capture underlying interaction patterns that characterize normal behaviors under varying conditions, while anomalies emerge as deviations associated with unstable or spurious correlations. To model the intricate distributions of normal and abnormal nodes, RagGAD integrates rationale-non-rationale Gaussian mixture modeling with a robust-fragile rationale mixture learning strategy. By mitigating spurious homophilic correlations and embracing the heterogeneity of normal patterns, RagGAD identifies anomalies as low-density regions within a structure-aware distribution space. Extensive experiments on multiple benchmark datasets demonstrate that RagGAD outperforms state-of-the-art methods.

---


### 289. [Group ICA 2.0: Closing the Gap Between Subjects and Group Latent Decomposition with Copula-Linked Group ICA (CoLiG-ICA)](https://arxiv.org/abs/2608.16029)

**<font color=#1a73e8>作者：</font>** Oktay Agcaoglu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Independent Component Analysis (gICA) is widely used to decompose high-dimensional functional MRI data into interpretable brain networks. However, conventional gICA primarily identifies components shared across subjects. This group-level assumption can limit the recovery of networks present only in individuals or subject subsets, reducing sensitivity to intersubject heterogeneity in clinical neuroimaging datasets. We introduce Copula-Linked Group ICA (CoLiG-ICA), an algorithm in the Group ICA 2.0 framework that jointly estimates template-linked, cohort-only, and subject-only brain networks within a unified model. CoLiG-ICA combines ICA-based spatial decomposition, copula-based dependence modeling, and deep learning optimization to preserve the consistency and interpretability of template-constrained ICA while enabling free components beyond the reference networks. By linking subject decompositions to shared templates and jointly estimating cohort-only and subject-only sources, CoLiG-ICA represents individual variability not captured by conventional group priors. We evaluate CoLiG-ICA using resting-state fMRI data from the UCLA-CNP dataset and compare it with conventional constrained ICA in estimating template-linked components, discovering additional free components, improving component independence, and capturing subject-level variability beyond the shared group prior. Compared with MOO-ICAR, CoLiG-ICA showed significantly lower intercomponent spatial dependence, indicating improved subject-level component independence, and significantly reduced motion-related variance in the template-linked components. Additionally, in a schizophrenia-only group analysis, CoLiG-ICA identified three additional resting-state networks beyond the 53 template-linked NeuroMark components: one sensorimotor and two visual networks.

---


### 290. [AdROD: HyperNetwork-based Adversarially Robust Object Detection for Autonomous Driving](https://arxiv.org/abs/2608.16031)

**<font color=#1a73e8>作者：</font>** Yuting Wu, Dongfang Guo, Xiangzhong Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Camera-based object detectors are vulnerable to physical adversarial attacks designed to suppress detections. While adversarial training and input purification offer some protection, they often overfit to specific attack distributions and fail on adaptive adversaries. This paper presents AdROD, an embedded, stochastic ensemble defense software designed for autonomous driving. AdROD employs {\em low-rank HyperNetworks}, which require only 1.6\% of the parameter footprint of standard HyperNetworks, to generate diverse detectors at a per-frame rate, making it impractical for attackers to obtain the deployed detectors in time. To further improve adversarial robustness, AdROD incorporates a novel \emph{functional diversity} mechanism, which couples stochastic weight updates with unique input-space transformations. We design two serving modes of AdROD that strike different trade-offs between robustness and runtime overhead: AdROD-I, a continuous protection mode for maximum resilience that leverages inter-detector disagreement to recover compromised detections, and AdROD-II, an on-demand mode triggered by kinematic discontinuities in object tracking. Through comprehensive evaluation with synthetic benchmarks, physically deployed adversarial patches, and end-to-end safety tests in the OpenCDA co-simulator, AdROD outperforms five baseline defenses and exhibits superior generalizability compared with the evaluated adversarial-training baselines, while maintaining real-time performance for safely stopping the vehicle at a stop sign instrumented with adversarial patches.

---


### 291. [NICE: Scale-Stable Perturbations for Graph Neural Network Explanations via Noise Corruption](https://arxiv.org/abs/2608.16038)

**<font color=#1a73e8>作者：</font>** Ziluowen Luo, Jun Yin, Ruochen Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc Graph Neural Network (GNN) explainers commonly follow a Perturb-Query paradigm, inferring the importance of graph elements based on queried predictions to perturbed inputs. However, such perturbations often introduce substantial distribution shift, undermining the reliability of the queried predictions used to derive explanations. While existing efforts mainly improve perturbed graphs or stabilize model predictions on them, we revisit the perturbation mechanism itself. We show that the widely used Element-wise Masking(EM) suppresses edge-induced messages toward zero, causing deterministic scale contraction that accumulates across message-passing layers, a phenomenon we term Scale Drift. Consequently, prediction changes under EM may conflate information corruption with deviations in propagation scale. As a scale-stable alternative to EM, we introduce Noise Corruption (NC), which perturbs each message through matched-norm random-direction corruption while preserving the expected squared message norm. Building on NC, we propose NICE, a Noise Corruption-based explanation framework, which learns a Stochastic Restoration Boundary (SRB) under NC-induced uncertainty, balancing target-prediction restoration against compactness. Furthermore, Boundary-Integrated Gradient (BIG) converts this boundary into edge attributions by accumulating each edge's contribution to reducing restoration risk along the restoration path. Experiments across multiple benchmarks demonstrate stronger explanation performance and model faithfulness while confirming that NC substantially reduces the Scale Drift induced by masking.

---


### 292. [TR-GS: High-Fidelity Sparse-View CT Volumetric Rendering via t-Distribution Gaussian Splatting and Ray-Confidence Modeling](https://arxiv.org/abs/2608.16042)

**<font color=#1a73e8>作者：</font>** Zedong Xiao, Yiren Wang, Zhou Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity 3D medical visualization supports applications such as clinical assessment and surgical planning. Sparse-view computed tomography (CT) can reduce projection requirements and associated radiation exposure, but limited observations may introduce structural artifacts and reconstruction uncertainty. Although 3D Gaussian Splatting (3DGS) provides an efficient explicit representation for volumetric rendering, existing CT methods based on standard Gaussian primitives may be sensitive to unreliable observations under sparse-view acquisition. We present TR-GS, a Gaussian-splatting framework for sparse view CT volumetric rendering. TR-GS replaces standard Gaussian primitives with projectable Student's t-distribution primitives and introduces a ray-confidence model that regulates their degrees of freedom according to local ray observability. Confidence-guided 3D wavelet regularization is further used to balance high-frequency detail preservation and noise suppression. This work is licensed under a Creative Commons Attribution 4.0 International License. Experiments on synthetic and real-world datasets show that TR-GS improves over representative baselines in most evaluated settings and remains competitive in the remaining cases. The resulting volumetric representations may support downstream medical multimedia applications, including XR-based visualization and interactive clinical rendering.

---


### 293. [Pluralistic Human-Robot Interaction: Designing for Robot Interaction with Diverse Communities](https://arxiv.org/abs/2608.16049)

**<font color=#1a73e8>作者：</font>** Raj Korpan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Social robots are being developed for homes, schools, and other environments where they will interact with diverse users. While Human-Robot Interaction (HRI) research often emphasizes natural communication, engagement, personalization, and task success, these goals do not fully address the social complexity of real-world deployment. This paper proposes \emph{Pluralistic HRI}, a framework for designing social robots that treat human diversity as a foundational design concern. The framework brings together pluralism, civic dialogue, perspective-taking, empathy, intercultural competence, cultural humility, and moral imagination to guide inclusive, adaptive, and ethically grounded interaction. We outline how pluralistic HRI can inform design, evaluation, and deployment in diverse human communities.

---


### 294. [OceanLight: Efficient Global Ocean Forecasting via Geometry-Adaptive Unstructured Mesh Representation](https://arxiv.org/abs/2608.16070)

**<font color=#1a73e8>作者：</font>** Wei Wu, Xiang Wang, Hongze Leng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable global ocean forecasting is critical for climate monitoring, marine navigation, and extreme event early warning. Physics-based ocean forecasting models impose prohibitive computational costs, while existing deep learning approaches predominantly rely on structured-grid architectures, incurring unnecessary computation on masked land cells and enforcing uniform resolution across dynamically heterogeneous ocean regions regardless of local flow complexity. Here we present OceanLight, an efficient global ocean forecasting framework innovatively combining geometry-adaptive unstructured mesh tokenization with a graph neural network (GNN) backbone. OceanLight achieves pointwise forecast accuracy and kinetic energy spectral fidelity exceeding both operational numerical analyses and state-of-the-art AI-based models, while surpassing all AI-based ocean models in geostrophic balance consistency. Furthermore, OceanLight demonstrates reliable mesoscale eddy representation, capturing coherent ocean structures beyond pointwise statistical optimization. These capabilities are delivered with a 62% reduction in GPU memory consumption and 70\% reduction in FLOPs relative to structured-grid baselines. Our unstructured mesh representation establishes a generalizable paradigm for scalable data-driven oceanography.

---


### 295. [DeepOHeat-v2: Self-Improving Operator Learning for Fast and Trustworthy Thermal Optimization in 3D-IC Design](https://arxiv.org/abs/2608.16080)

**<font color=#1a73e8>作者：</font>** Xinling Yu, Yixing Li, Ziyue Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Thermal-aware optimization of multi-die 3D integrated circuits evaluates many designs, each a costly heat-equation solve. Operator-learning surrogates replace this solve with a fast forward pass, ideally trained from physics alone, without labeled data. DeepOHeat-v1 made such surrogates fast and trustworthy, but only on low-contrast geometries. High-contrast multi-die stacks break it in two ways: discontinuous conductivities make the continuous physics loss ill-defined at material interfaces, and ill-conditioning ($\kappa_2(A_h) \approx 6 \times 10^4$) puts the discretized strong-form loss beyond first-order optimization. We propose DeepOHeat-v2 to overcome both. First, we train on a discretized physics loss that handles the discontinuities natively; its energy form reduces the prediction-space loss-Hessian conditioning from $\kappa^2$ to $\kappa$, and a matrix-preconditioned optimizer cuts the mean peak temperature error from over 30 K to 0.55 K. Second, because optimization leaves the training distribution, we propose a self-improving framework: a hotspot trust gate sends flagged placements to a reference solver, and the surrogate incrementally retrains on the refined solutions, keeping an update only when it improves held-out validation error. On a multi-die benchmark, the surrogate-true peak gap on the returned design falls from 1.12 K to 0.11 K, matching a solve-at-every-step optimizer while running $56\times$ faster.

---


### 296. [Towards Reasonable Molecular Structure Elucidation from Infrared Spectroscopy with Chemical Feedback](https://arxiv.org/abs/2608.16082)

**<font color=#1a73e8>作者：</font>** Yusen Tan, Hongyu Zhan, Hai-tao Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Infrared (IR) spectra provide characteristic signals of molecular structure, which are often interpreted by experts via functional-group identification or library matching, making the process time-consuming and ambiguous. Recent machine learning methods have made progress in molecular structure elucidation using molecular formulas and IR spectra. However, these models often infer unreasonable candidate molecular structures, including top-ranked predictions. More specifically, the molecular formula implied by a candidate structure often fails to match the input molecular formula, and the candidate's theoretical IR spectrum is often inconsistent with the observed IR spectrum. To address these issues, we propose Formula- and IR-Matched Preference Optimization (FIRMPO), a general and plug-and-play chemical feedback-driven preference optimization framework for molecular structure elucidation. FIRMPO incorporates chemical feedback as preference signals based on exact molecular formula matching and IR spectral consistency to guide reasonable structure predictions. Unlike generic preference optimization methods, FIRMPO is tailored to molecular structure elucidation while remaining model-agnostic, enabling it to be readily integrated with different structure prediction models in this class. This encourages models to prioritize structures that satisfy the chemical feedback, leading to a substantial improvement in the accuracy of top-ranked predictions. Extensive experiments on three widely used IR datasets show that FIRMPO significantly improves molecular structure elucidation accuracy over existing baselines.

---


### 297. [Eigenanalysis framework for autoregressive neural emulators of multi-scale chaotic dynamics](https://arxiv.org/abs/2608.16084)

**<font color=#1a73e8>作者：</font>** Conrad Ainslie, Pedram Hassanzadeh, Michael W. Mahoney 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural autoregressive models have rapidly emerged as powerful emulators of high-dimensional chaotic systems, yet their long-term instability and error growth remain poorly understood, leading to ad-hoc solutions. Here, we develop an eigenanalysis framework that reveals the dynamical origin of this error growth. By analyzing the Jacobian of the learned one-step update map with respect to the state, we show how inference-time error growth, and thus model stability, is governed by its spectral radius. Direct-step architectures (models that predict the next state from the previous one) generically admit unstable eigenvalues with magnitudes exceeding one, explaining the rapid divergence of these widely used models. In contrast, integration-constrained models (where the time derivative is estimated and integrated with a higher-order integrator) collapse their eigenspectrum onto the unit circle, yielding neutral stability and a universal linear error-scaling law. The largest eigenvalue of this Jacobian provides an architecture-agnostic, a priori diagnostic of short-term skill, long-term stability, and spectral bias, without requiring an expensive rollout. Leveraging this theory, we introduce a stability-promoting loss that explicitly regularizes Jacobian-driven error amplification, improving both forecast accuracy and dynamical robustness. Demonstrated across $29$ models spanning two architectures, several explicit and implicit integrators, and multiple loss functions on the Kuramoto-Sivashinsky system, our results establish a theoretical foundation for the design and evaluation of neural emulators of chaotic multi-scale dynamics. More broadly, our framework is a step toward the kind of a priori stability analysis that numerical analysis provides for discretizations of differential equations and that scientific machine learning currently lacks.

---


### 298. [Behaviour Is an Incomplete Measure of Reasoning Development: Cross-surface pre-arrival accessibility and the limits of developmental inference in a recurrent-depth reasoner](https://arxiv.org/abs/2608.16085)

**<font color=#1a73e8>作者：</font>** Simon Lam-Muir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Capability development is routinely inferred from behavioural thresholds, from final checkpoints, or from what a decoder can read out of a hidden state. These quantities need not identify the same event. We study a 30M-parameter recurrent-depth relational reasoner in a closed, oracle-defined world, using dense behavioural trajectories, two training surfaces, preregistered pre-arrival hidden-state probes, prospectively checked evaluability, and explicit untrained and negative controls, holding the training-time and inference-time axes separate throughout. Behaviour first: under one frozen acquisition criterion, three-hop competence cost 70 logical epochs on the symbolic surface and 13,055 on the verbal surface, a 186.5-fold contrast, after which verbal four-hop competence cleared in 8 logical epochs. Across the 13,055-epoch grind, four-hop held-out behaviour never exceeded 3/40 and ended at 0/40. Internal measurement next: on the verbal surface a linear probe recovered future-answer identity before behavioural arrival at 0.056159 against uniform chance 0.025, an untrained control of 0.024758 and a population frequency baseline of 0.048309 (p = 0.012987; 16/40 answer classes contributing). Analogous pre-arrival accessibility survived the surface change, reaching 0.1020 against a zero-step control of 0.0460 (p = 0.000999) at the upstream structural position and 0.0618 at the readout comparator (p = 0.004), with 21/40 classes contributing. Finally, the natural attempt to track that accessibility across training was not cleanly evaluable: probe eligibility is defined by behavioural arrival, so the measured population changes with the measurand. Behavioural competence, internal accessibility, and training-time development are distinct observables, and neither behaviour nor decoder accessibility identifies the computation training acquired; causal intervention is the necessary next step.

---


### 299. [Representation Is Not Enough: Body-Localized Thermal Evidence for Contactless Stress and Craving Sensing in Opioid Use Disorder](https://arxiv.org/abs/2608.16087)

**<font color=#1a73e8>作者：</font>** Sachin Deb, Harshit Sharma, Asif Salekin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Removing wearables from physiological monitoring also removes their supervision: the signal indicating where and when a stress response occurred. Contactless stress sensing therefore becomes a weakly supervised evidence-localization problem, where a clip-level label must be traced to the body regions and moments that produced it. We address this with FABLE-Therm, a weakly supervised architecture that preserves localized evidence across body regions, time, and encoder-specific representations until the final decision. FABLE-Therm fuses frozen foundation-model encoders at the embedding level, with theory explaining why localized fusion can outperform feature concatenation and prediction averaging. We study this problem in opioid use disorder (OUD), where stress is a major relapse trigger and sustained wearable use can be difficult during early recovery. Using fixed thermal video, FABLE-Therm achieves 0.938 AUROC on held-out participants, and its learned representation transfers to self-reported craving, providing, to our knowledge, the first evidence that craving can be recovered from contactless thermal video. Localized evidence also enables participant-level analysis of deployment failure. We find that improving representation alone is insufficient for equitable deployment: additional data from the underserved group would recover only about half of the cohort gap, while the remainder reflects person-to-person heterogeneity. This modality-agnostic decomposition applies to models with identifiable subpopulations. Together with the first cohort-structured contactless thermal OUD benchmark, our results show that preserving localized evidence supports both accurate sensing and principled analysis of who a model fails and why.

---


### 300. [Protein Structure Prediction: From Evolutionary Constraints to Generative Modeling](https://arxiv.org/abs/2608.16094)

**<font color=#1a73e8>作者：</font>** Wengan He, Yongsheng Luo, Lihong Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate protein structure prediction is fundamental to structural biology because protein structure underlies molecular function and provides a basis for mechanistic interpretation. Recent advances in deep learning have transformed the field from multiple sequence alignment (MSA)-driven monomer folding into broader frameworks capable of modeling protein complexes and increasingly heterogeneous molecular systems. Existing reviews have summarized this progress from the perspectives of representative models, application domains, and protein design. Building on these efforts, this review focuses on the methodological evolution of the field itself. It examines recent developments through three closely related dimensions: representations and data, architectures and learning strategies, and confidence and evaluation. Within this perspective, the field is organized into four methodological phases and three cross-cutting transitions: from explicit evolutionary coupling features and early contact prediction to learned sequence representations in AlphaFold2, RoseTTAFold, and ESMFold; from protein-only monomer folding to increasingly integrated modeling of heterogeneous molecular systems in AlphaFold-Multimer, RoseTTAFoldNA, and AlphaFold3; and, more recently, from prediction-oriented structure inference to design-oriented generative modeling in RFdiffusion and related frameworks. This framework provides a clearer understanding of how methodological shifts have shaped the capabilities, limitations, and practical roles of recent models.

---


> [!TIP]
> 当前位于：**251-300**（第 6/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-435](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
