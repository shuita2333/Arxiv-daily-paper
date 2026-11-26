# 📦 其他研究 | 2026年11月27日

> 本类共 **314** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-314](./part-07.md)

---

### 101. [Show Me the Change You Want: Visual Example-Guided Change Detection](https://arxiv.org/abs/2611.33756)

**<font color=#1a73e8>作者：</font>** Yuan Qian, Jiaqi Cui, Jie Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Change detection identifies where images differ, but in practice users often seek only a particular kind of change. Existing referring change detection methods rely on predefined categories, textual descriptions, or annotated masks, limiting flexibility or requiring additional annotation. In this paper, we propose a new way to perform change detection, where an unannotated before-and-after image pair serves as a visual example to guide change localization in another pair. Our framework, Visual Example-Guided Change Detection (VECD), learns comparable attribute states from single images and introduces an example-conditioned readout to match changes across different objects and scenes. The example itself defines the request, without text, example masks, or test-time fine-tuning. We evaluate VECD on four datasets spanning rendered scenes and natural image edits: EditCLEVR, MagicBrush, HumanEdit, and MaskEdit. Experiments demonstrate cross-dataset generalization without fine-tuning: a single fixed example pair guides change detection across multiple scenes, even when examples and queries originate from different datasets. VECD selects matching changes in scenes with multiple simultaneous changes and returns an empty mask when the requested change is absent. It further generalizes to attribute families withheld from paired training, achieving 74.54\% to 93.38\% mIoU across four holdout settings. Code is available at this https URL

---


### 102. [GlassGround: GUI Grounding Beyond Native Screenshots with Egocentric Wearable Vision](https://arxiv.org/abs/2611.33760)

**<font color=#1a73e8>作者：</font>** Yun Wang, Siyue Sun, Jiaying Du 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wearable assistants must localize interface elements from camera observations when direct screenshot access is unavailable, yet existing GUI grounding benchmarks primarily evaluate native screenshots. We introduce GlassGround, a new benchmark that pairs native screenshots with wearable camera observations while holding GUI states, instructions, and targets fixed. GlassGround contains 3,250 tasks across Android and iOS, captured using four wearable devices under four viewing conditions. Across ten open-source models, mean grounding accuracy drops from 94.8% on screenshots to 48.5% on camera images. Further analysis reveals that changes in target scale, screen geometry, and background cannot fully explain this performance degradation. We then study two ways to narrow this gap. At inference time, local zooming and screen rectification help but leave most of the gap. For training-time adaptation, we build on GlassGround's paired-view design and introduce PairDistill, a baseline that aligns target representations across views alongside coordinate supervision. Trained on independently collected data and using no screenshots at inference, it improves camera-image accuracy by 9.4 and 12.2 points on two backbones and transfers to unseen devices and operating systems. Combined with local zooming, it reaches 69.6% and 64.4%, but does not close the gap. The GlassGround dataset and code are available at this https URL.

---


### 103. [Improving Building Energy Efficiency with an Indoor Environmental World Model and Counterfactual Adaptive Learning](https://arxiv.org/abs/2611.33764)

**<font color=#1a73e8>作者：</font>** Xu Yang, Kailai Sun, Dianyu Zhong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Optimizing indoor climate systems plays a critical role in achieving the United Nations' Sustainable Development Goals 11 and 13. However, indoor delayed thermodynamic responses and partial observability severely hinder existing reinforcement learning (RL) methods, which are primarily limited by implicit thermal inertia, occupancy dynamic prediction, and cumulative prediction errors during long-horizon rollouts. Thus, we propose a novel occupant-centric indoor climate control framework. It develops indoor environmental world models to predict future physical thermal baselines and dynamic occupancy, explicitly capturing latent thermal inertia. By formulating adaptive regulation as counterfactual advantage learning against future environments via a Branching Dueling Q-Network, and integrating a Held-Action TD-{\lambda} target, it effectively mitigates delayed credit assignment. Additionally, a proposed physics-aligned smoothness regularization suppresses high-frequency actuator fluctuations, potentially extending equipment service life. Experiments on SemiBuildingSim and Sinergym demonstrate that our method achieves a superior multi-objective trade-off. Compared to the best-performing methods, it further reduces energy consumption by 11.2%, occupant discomfort by 44.2%, and action fluctuation by 47.3%, achieving better sample efficiency and cross-region effectiveness. This interdisciplinary study offers an energy-efficient, occupant-centric AI solution for control science, building science, and energy sustainability.

---


### 104. [Don't Waste the Population: Post-Anneal Refinement for Combinatorial Optimization](https://arxiv.org/abs/2611.33766)

**<font color=#1a73e8>作者：</font>** Yuma Ichikawa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parallel annealers generate diverse candidate solutions; yet, conventional post-processing typically refines only the best, leaving much of the population's potential untapped. We introduce Iterative Path-Relinking Polish (I-PRP), a deterministic, training-free method that exploits this diversity to discover better solutions without modifying the underlying annealing process. I-PRP selects promising candidates, explores cost-guided paths between locally optimized solutions, and refines intermediate states to uncover better local minima. Newly discovered improvements are iteratively incorporated into the population, enabling further exploration. We theoretically guarantee that I-PRP never degrades solution quality relative to conventional single-candidate polishing on the same population and converges in finitely many iterations. Experiments across challenging combinatorial optimization benchmarks, including MaxCut, MaxClique, and graph coloring, demonstrate substantial improvements in several instances. Paired evaluations confirm non-degradation, while matched-runtime comparisons show that exploiting existing population diversity can outperform additional annealing. These results establish I-PRP as an effective and reliable refinement strategy for parallel annealing.

---


### 105. [DuoWM:Integrating Dual 6-DoF Visual Flows into Action-Conditioned Drone World Model](https://arxiv.org/abs/2611.33779)

**<font color=#1a73e8>作者：</font>** Zixuan Li, Kangyao Huang, Meng Xu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action-conditioned video world models generate future observations from an initial frame and a camera trajectory, but often fail to align camera commands with visual dynamics or represent full 6-DoF scene transformations. We present DuoWM, a first-person drone video world model with two complementary visual conditions. Action flow projects future camera positions and orientations into each target frame, while Object flow forward-warps the initial observation and overlays local 6-DoF transformations to ground the induced scene motion. We further introduce transform-aware pretraining, which pairs object appearance with explicit transformation axes before standard RGB video training. On Sekai-drone dataset, DuoWM achieves the best results across video quality, 3D consistency, and trajectory following. Compared with Captain Safari, the state-of-the-art method, our approach reduces real-domain FVD and LPIPS by 17.2\% and 21.6\%, respectively, while improving game-domain AUC@30 from 0.5003 to 0.5719 and AUC@15 from 0.3088 to 0.3747.

---


### 106. [Bridging Transferability and Discriminability via Positive-Unlabeled Domain Adaptation for Building Damage Mapping Across Disaster Events](https://arxiv.org/abs/2611.33790)

**<font color=#1a73e8>作者：</font>** Qirui Wang, Hengwei Zhao, Xiaoshu Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mapping the damage to buildings following natural and human-caused disasters is essential for disaster response and humanitarian assistance. However, differences in hazard types, geographic environments, building characteristics, and imaging conditions cause cross-event distribution shifts that limit the generalization of deep learning models to new disaster events, even for geospatial foundation models (GFMs) pretrained on extensive Earth observation data. Unsupervised domain adaptation (UDA) can mitigate these shifts, but adaptation remains challenging when damage-proportion and damage-appearance shifts coexist and interact. We identify enhancing target-domain discriminability as key to addressing this challenge. To this end, inspired by positive-unlabeled (PU) learning, we introduce positive-unlabeled domain adaptation, a paradigm that incorporates PU weak supervision to enhance target-domain discriminability, requiring only a few labeled damaged buildings in the target domain. Building upon this straightforward intuition, we develop Positive-ANchored Domain Adaptation (PANDA), comprising two complementary and mutually reinforcing components: Pairwise Alignment with Intra-class Robustness (PAIR) for discriminative representation learning and Refine Gate and Verifier (RAV) for supervision refinement. On a global-scale multi-disaster benchmark, PANDA generally outperforms representative domain adaptation and PU learning methods. Results on the 2025 Los Angeles wildfires show its effectiveness in new disaster scenarios with few labeled damaged buildings. Further experiments demonstrate the potential of integrating PANDA with GFMs for cross-event adaptation. These findings highlight PANDA's practical potential for rapid, reliable, and cross-event building damage mapping.

---


### 107. [Spatial Transcriptomics Prediction from Histology via Topology-Informed Graph Attention and Gene-Semantics Conditioning](https://arxiv.org/abs/2611.33792)

**<font color=#1a73e8>作者：</font>** Yuqi Cheng, Boshuai Zhang, Ziqi Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics (ST) profiles gene expression with spatial context but remains costly, motivating models that infer expression from H&E images. Existing approaches face three key limitations: (i) a single patch embedding is often insufficient: morphologically similar regions can exhibit distinct expression due to spatial context, while naive neighborhood aggregation can over-smooth boundaries; (ii) conventional fixed, gene-indexed output heads treat genes independently and cannot directly support strict zero-shot prediction for unseen genes; and (iii) common metrics under-measure spatial pattern fidelity and boundary resolution. To address these challenges, we propose TIGEM, a topology-informed, gene-conditioned framework for histology-to-ST inference. TIGEM learns topology-aware spot representations by regularizing graph attention with tissue-level topology and morphology cues to avoid cross-compartment smoothing, and uses gene semantic modulation to replace gene-indexed heads, enabling zero-shot prediction for unseen genes. We also introduce Graph Spectral Correlation (GSC) to evaluate spatial pattern fidelity and boundary resolution complement to PCC/MSE. Across three large-scale ST datasets, TIGEM achieves overall state-of-the-art performance and significantly improved boundary prediction resolution, and further demonstrates the ability to predict expression patterns for genes unseen during training, extending prior zero-shot histology-to-ST efforts with topology-aware spatial propagation and PLM-based gene conditioning.

---


### 108. [SprintGS: Eliminating Redundancy for Fast 3D Gaussian Splatting Training](https://arxiv.org/abs/2611.33796)

**<font color=#1a73e8>作者：</font>** Ryosuke Watanabe, Tomoaki Konno  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) renders photorealistic novel views in real time, but its per-scene training (optimization) remains slow. Recent fast training methods such as FastGS shorten training to a few minutes by reducing the number of Gaussians. Profiling FastGS, we find two costs that remain even in its compact model. First, rasterization is still the largest cost, and redundant work remains in it. Second, the loss computation does not shrink with the number of Gaussians, so its share of the training time grows as the model becomes compact. We present SprintGS, a training framework built on FastGS that keeps the model compact and reduces both costs. For rasterization, scheduled tile culling limits each Gaussian to the tiles where it matters, using a coarse footprint that is annealed to the exact one before training ends; convergence-aware pruning removes converged, nearly transparent Gaussians; and a shuffle-efficient backward pass reduces the data exchanged between GPU threads. For the loss, a fused loss computes the loss and its image gradient in the forward pass without a loss map, removing most of its cost. SprintGS trains 2.15x faster than FastGS at comparable quality, and 1.81x faster in its high-quality setting. It also accelerates other fast training methods and dynamic, sparse-view, and surface reconstruction.

---


### 109. [DriftWAM: Faster World-Action Models via Action-Aware Video Drifting](https://arxiv.org/abs/2611.33797)

**<font color=#1a73e8>作者：</font>** Minyang Li, Siyu Xu, Yunke Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World-action models (WAMs) unify future video prediction and action generation for robotic control, but their reliance on iterative denoising incurs substantial inference costs. Distilling these models into few-step generators offers a promising route to efficient deployment, yet maintaining task performance under aggressive step reduction remains challenging. Existing methods rely on point-wise trajectory consistency distillation, which pursues high visual fidelity while leaving downstream action information unexploited in optimizing video generation, and also lacks explicit distribution-level alignment. To address this, we propose DriftWAM, a few-step WAM distillation framework that incorporates the actions induced by predicted videos into video learning. Specifically, DriftWAM integrates action-aware video drifting, which performs video distribution matching through a joint visual--action similarity kernel to steer sample evolution under the guidance of these induced actions, with action-guided video regularization, which leverages the compatible teacher--student matches identified by the joint kernel to backpropagate action-level gradients directly into the video generator. Evaluations on the RoboTwin 2.0 and LIBERO benchmarks, as well as in real-world robotic manipulation tasks, show that DriftWAM consistently outperforms prior consistency distillation methods across few-step settings at the same inference speed.

---


### 110. [Dynamic Forcing: Learning Action-Grounded Sparse Dynamic Representations with Dense Future Guidance for World Action Models](https://arxiv.org/abs/2611.33799)

**<font color=#1a73e8>作者：</font>** Ziqiang Li, Shisheng Chen, Yunnan Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World action models (WAMs) support robot control through visual prediction, but dense future modeling repeatedly encodes static context already available in the current observation, while action-relevant changes are often spatially sparse. We study sparse dynamic representation learning, retaining the current observation as a contextual anchor and using a small set of compact dynamic tokens to represent anticipated changes. We develop CompactWAM, a sparse-dense joint predictive framework that enables sparse representation learning within a video-supervised shared backbone, without requiring a reconstruction objective for the sparse pathway. Since a limited token budget alone does not specify which information to retain, we introduce Dynamic Forcing, which pairs direct action supervision with privileged dense future guidance to promote action relevance and dynamic fidelity. While action prediction gradients directly drive compact tokens to capture control-relevant cues, dense future guidance further shapes them via action functional guidance that matches sparse and dense contributions to the action expert, and dynamics-aware distribution matching, which aligns temporal relational changes relative to a static reference. At inference, a single visual forward pass encodes current observations and compact dynamic tokens for action generation, eliminating dense future modeling. CompactWAM achieves 98.4\% success on LIBERO and 77.9\% on LIBERO-Plus, retaining respective success rates of 98.3\% and 76.6\% with only 9.2\% of the dense future token budget. Evaluations on RoboTwin~2.0 and real-world manipulation further demonstrate the effectiveness of the learned sparse predictive representations.

---


### 111. [EvoVAU: Tool Evolution for Video Anomaly Understanding](https://arxiv.org/abs/2611.33808)

**<font color=#1a73e8>作者：</font>** Benfeng Wang, Chao Huang, Yudong Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video anomaly understanding (VAU) requires reasoning about event progression, interactions, and the contextual conditions that distinguish abnormal behavior from common activity across diverse scenes. Although video agents enable multi-round analysis, the predefined analytical operations may not adequately satisfy these diverse reasoning demands. In this paper, we present EvoVAU, a framework that evolves a reusable tool library for a frozen video solver. Guided by task outcomes and execution trajectories, an external proposer identifies potential limitations in the library and refines it, retaining task experience as analytical operations that can be reused across questions. Specifically, Cross-Version Contrastive Feedback guides tool refinement by combining current errors with paired execution trajectories from historical corrections and regressions. Adoption-Aware Selection accepts a candidate library only when overall development-set accuracy improves and corrections outnumber regressions among questions on which the solver invokes new or modified tools. Using a small development set, EvoVAU alternates tool refinement with candidate evaluation and selection. At test time, the evolved library remains fixed, with no further involvement from the proposer. Experiments on several VAU benchmarks demonstrate strong performance and the flexibility of the evolved library across anomaly domains.

---


### 112. [Probabilistic Monocular Biomechanical Reconstruction via Guided Flow Matching](https://arxiv.org/abs/2611.33809)

**<font color=#1a73e8>作者：</font>** R. James Cotton, Fabian Sinz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing 3D joint kinematics from a single video is ill-posed due to depth and stature ambiguity, limb occlusion, and missing uncertainty estimates. We introduce the Biomechanical Flow Model (BFM), a continuous-time flow-matching prior over subject anthropometry, anatomical joint-angle trajectories, and virtual markers, trained on multi-camera clinical recordings from 565 participants and steered toward monocular 2D keypoints at test time without paired video training. In a head-to-head comparison on the same clinical trials against a state-of-the-art deterministic trajectory optimizer fitting the identical skeleton, BFM achieves comparable joint-angle accuracy across walking and timed-up-and-go (TUG). Across held-out control, prosthetic, and neurologic participants, BFM reaches 3.91 deg and 4.97 deg mean absolute joint-angle error on walking and TUG while providing credible intervals that bridge temporal and whole-limb occlusions. Where keypoints are hidden, the intervals widen with the error and keep their coverage near nominal. Supplying individual anthropometric calibration removes most monocular pelvis depth error, whereas testing on out-of-distribution pediatric crouch gait produces biased, overconfident extension predictions, highlighting the need for pathologically diverse movement priors.

---


### 113. [Ensuring Deployment-Time Safety of Neural Network Controlled Systems via Localized Certificate Repair](https://arxiv.org/abs/2611.33813)

**<font color=#1a73e8>作者：</font>** Xiaoyang Lv, Peixin Wang, Jianhao Bai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Barrier certificates provide formal safety guarantees for neural network controlled systems by ensuring that system trajectories avoid unsafe regions over time. However, after deployment, previously unseen obstacles or constraint changes may introduce new unsafe regions, invalidating the original certificate and potentially leading to unsafe behavior. We address this setting with adaptive piecewise barrier certificates, which preserve the original certificate and policy in unchanged regions while introducing localized updates around newly emerged unsafe regions. The central question is how to perform such updates efficiently during system execution without retraining from scratch. Our key idea is to cast deployment-time adaptation as a localized certificate repair problem and reduce it to an optimization task that leverages the learned structure of previous barrier certificates, enabling fast updates without global retraining. We further design a staged repair framework that progressively transitions from localized repair to joint policy-certificate updates and, when necessary, localized retraining. Empirical results on four benchmarks with five new obstacles show that our method succeeds in all cases and completes within tens of seconds on average, whereas retraining from scratch fails in most cases. On instances where retraining succeeds, our method is 17.3$\times$ faster on average. It incurs only 16.2% performance degradation relative to the original policy.

---


### 114. [Spectral Optimal Transport for Dynamics-Aware Sign Language Generation](https://arxiv.org/abs/2611.33818)

**<font color=#1a73e8>作者：</font>** Nabeela Khan, Bowen Wu, Runwu Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sign language generation (SLG) translates spoken-language text into pose sequences that convey its meaning. Recently, flow-based models with optimal transport (OT) have become a strong SLG baseline by handling the one-to-many nature of text-to-sign. While classifier-free guidance (CFG) could be applied to further strengthen the semantic alignment theoretically, its training involves conditional and unconditional training, which may contradict the pose-space OT, thus reducing the generation quality. Under the condition dropout, one noise sample can be paired with target motions exhibiting incompatible motion dynamics, interfering with the semantic guidance when the text condition is present. To address this issue, we propose Spectral Optimal Transport (SOT), which augments the pose-space cost with a spectral feature distance, reweighting the coupling toward the temporal-frequency structure of the target motions, thereby improving the performance when using CFG. The quantitative and qualitative experiments demonstrate the effectiveness of the proposed method.

---


### 115. [MMotion: Collaborative Cross-Scale Memory for Text-to-Motion Generation](https://arxiv.org/abs/2611.33819)

**<font color=#1a73e8>作者：</font>** Zhaoxin Fan, Qingchen Yu, Kejian Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-motion generation aims to synthesize realistic human motions from natural-language descriptions, enabling applications in animation, virtual avatars, and embodied agents. Despite recent progress, existing methods either retrieve motion exemplars or retain long-range context, but rarely exploit memory to jointly reason about semantics, dynamics, and generation history. In this paper, we propose MMotion, a collaborative multi-scale memory framework that unifies scale-conditioned semantic retrieval, latent dynamics modeling, and causal working memory. Specifically, semantic memory provides motion priors at different generation scales, dynamics memory captures latent state transitions, and working memory preserves causal context from previously generated motions. A collaborative fusion mechanism integrates these complementary memories to determine what motion to generate, how it should evolve, and how it should remain consistent with its history. MMotion is architecture-agnostic and can be readily integrated into both diffusion-based and next scale autoregressive models. Extensive experiments across standard benchmarks and diverse backbones demonstrate consistent improvements over strong baselines.

---


### 116. [Revisiting Monocular In-Hand Object Scanning: Dataset, Pose Estimation, and Surface Reconstruction](https://arxiv.org/abs/2611.33824)

**<font color=#1a73e8>作者：</font>** Di Wu, Jeeeun Kim, Shu Kong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In-Hand Object Scanning (IHOS) from monocular video captured by a commodity smartphone holds immense potential to democratize 3D digitization for non-expert users, facilitating applications in digital archiving, augmented reality, and custom fabrication. Yet, IHOS remains largely understudied due to a lack of realistic datasets and systematic benchmarks. To bridge this gap, we introduce ToysRUs, a high-quality dataset featuring diverse figurines captured by 4K Ultra High-Definition (UHD) monocular videos. Studying IHOS from first principles, we examine structure-from-motion (SfM) for camera pose estimation, which is key to IHOS. We identify two key challenges: small baselines between consecutive frames, and sparse feature matches across large-view, long-range frames, further exacerbated by dynamic hand occlusions. Guided by these insights, we propose performing SfM on video sub-sequences sampled at sufficient angular intervals, and iteratively stitches the corresponding sub-trajectories into a unified global trajectory. Furthermore, for high-fidelity surface reconstruction, we introduce occlusion-aware 2D Gaussian Splatting, which incorporates opacity rendering and omits the opacity loss on hand regions. Quantitative and qualitative evaluations demonstrate that our framework significantly outperforms existing approaches, including neural implicit representations and 3D foundation models, in both geometric accuracy and photometric fidelity.

---


### 117. [On Grokking and the Dynamics of Generalization](https://arxiv.org/abs/2611.33825)

**<font color=#1a73e8>作者：</font>** Malik Amir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We extend the signal-channel theory of grokking introduced by Litman and Guo by relating training dissipation and evaluation transfer to population risk. For preconditioned gradient flows with time-dependent kernels, we distinguish two sources of limited evaluation visibility, namely small cumulative dissipation and weak transfer. We obtain quantitative bounds for task visibility and establish their stability under signal filtering and changes of evaluation distribution. We describe how task directions enter the effective signal channel through spectral activation or transport. We establish necessary and sufficient conditions for the transferred signal to decrease squared population risk and derive classification error bounds under margin assumptions. These results yield sufficient conditions for the same training trajectory to generalize under one evaluation distribution while failing under another. We show that differences in spectral learning rates can produce arbitrarily long delays between low training loss and low population risk. By relating classification accuracy to the distribution of margin crossing times, we construct a family of gradient flows in which the generalization delay tends to infinity, while both the duration of the transition from zero to full accuracy and the corresponding variation of population risk tend to zero. These phenomena occur without feature evolution during training. Finally, we prove that the occurrence and timing of generalization cannot generally be inferred from training dynamics alone, but depend on the geometry of evaluation transfer and its relation to the target.

---


### 118. [MotionODE: Enhancing Autoregressive Text-to-Motion Generation with Continuous-Depth Modeling](https://arxiv.org/abs/2611.33826)

**<font color=#1a73e8>作者：</font>** Zhaoxin Fan, Jian Yang, Kejian Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive text-to-motion generation requires local motion predictions to reconcile cross-temporal textual requirements with the available motion context. While existing methods primarily improve motion representations and generation order, the internal formation of conditioned motion representations remains less explored. We introduce MotionODE, a continuous-depth post-training framework that refines hidden-state evolution in pretrained autoregressive generators. MotionODE reinterprets selected Transformer residual branches as local vector fields and replaces their original updates with midpoint Runge--Kutta (RK2) integration, while preserving the motion representation and outer generation mechanism. To address the mismatch between pretrained update paths and newly introduced intermediate states, we propose mixed one-step/two-step RK2 post-training under motion-token supervision, with optional distillation and update-map constraints to preserve pretrained behavior. This minimally invasive framework supports both next-token and next-scale generation without training the generator from scratch. Extensive experiments on HumanML3D demonstrate consistent improvements in text--motion alignment across MoScale, BAMM and LMR, highlighting internal representation updates as a complementary direction for improving autoregressive motion generation.

---


### 119. [Teaching a Multilingual Translation Model Regional Varieties: Castilian and Latin American Spanish, Asturian, Aragonese and Aranese with MADLAD-400-3B-MT](https://arxiv.org/abs/2611.33831)

**<font color=#1a73e8>作者：</font>** Nerea de la Torre Veguillas, Pol Gerdt, Raul Quijada 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Massively multilingual translation models usually have one tag per language and no control over regional varieties, and they cover a region's smaller languages poorly or not at all. We report three fine-tunes of MADLAD-400-3B-MT, each adding target tags with low-rank adaptation (LoRA), back-translation of monolingual text and replay of the base model's own translations: <2es_ES> for Spanish as written in Spain, <2es_419> for Latin American Spanish, and one model for three Romance languages of the Iberian Peninsula, Asturian (<2ast>), Aragonese (<2an>) and Aranese (<2oc_aranes>). For the Spanish varieties we annotate the 250.9M documents of MADLAD-400's Spanish split with a domain-supervised Spain vs. Latin America classifier and select variety text with a rule that admitted no Latin American document in a 340-document reference set. The Castilian model chooses Spain's everyday vocabulary in 97% of a targeted test (base model 62%) and vosotros for informal plural address in 70% (10%), while improving chrF++ on human references. A first finding is tag collapse: with a new tag initialised from <2es>, the parent tag drifts to the new variety (84-87% identical outputs). In the Iberian model, contrastive pairs and a separate learning rate for the tag embeddings keep each tag in its own language. Trained only on publicly available data, mostly the TAN-IBE Wikipedia corpora, the Iberian model matches or beats the TAN-IBE Marian systems in four of six Spanish directions on FLORES+, is 1.9 BLEU behind in Spanish->Aranese, and is second only to SalamandraTA-7B in most directions. The exception, Spanish->Aragonese, reflects a difference of written variety between Aragonese Wikipedia and the FLORES+ reference, not model quality. All three fine-tunes lose 0.6-0.7 chrF++ on average in thirteen other FLORES-200 directions. We release the models, data and variety classifier under open licences

---


### 120. [Continuous Foundation-Guided Pseudo-Label Weighting for Breast Ultrasound Domain Adaptation](https://arxiv.org/abs/2611.33843)

**<font color=#1a73e8>作者：</font>** Xinyu Fan, Xinyi Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Breast ultrasound segmentation models often generalize poorly across scanners, institutions, and patient populations. We investigate continuous foundation-guided pseudo-label weighting for unsupervised domain adaptation (UDA). An exponential-moving-average (EMA) teacher generates target-domain pseudo-labels, while a frozen ultrasound segmentation model (AutoSAMUS) modulates their contribution using a bounded weight that combines the prior's certainty with its probabilistic agreement with the teacher. In contrast to our earlier selective BiRP rule, the proposed formulation supervises every target pixel with a weight in [0.5, 1] and requires no foundation-model inference at test time. We evaluate the method on five public breast ultrasound datasets, spanning three source domains and eleven source-target directions. Under the TransUNet protocol, continuous weighting outperforms both all-pixel EMA and original BiRP on all four BUSI-source targets, and achieves the highest mean Dice and lowest HD95 among the compared methods on all four BUS-BRA-source targets. Results with BrEaST as the source are mixed: continuous weighting performs best on BUSI and comparably to original BiRP on OASBUD, whereas none of the adaptation methods surpasses source-only training on BUS-UCLM. In a separate U-Net pipeline, agreement-only weighting performs comparably to the full formulation, leaving the incremental value of prior certainty unresolved. Because the weighting rule was developed after some target-test results had been examined, we treat the study as exploratory and report adverse as well as favorable outcomes.

---


### 121. [Mitigating Overgeneralization in RND via Spectral Target Design](https://arxiv.org/abs/2611.33850)

**<font color=#1a73e8>作者：</font>** Minseok Jeong, Yechan Lee, Hyewon Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Random Network Distillation (RND) is a scalable novelty signal for RL based on a fixed random target network and a trained predictor. However, it can overgeneralize: the predictor extrapolates the random target off the data manifold, causing novelty scores to collapse on unfamiliar inputs. This paper analyzes this failure through a kernel-theoretic lens. Under a GP target model and an NTK-regime predictor, we show that the RND novelty score is a cross-kernel residual variance: it is governed jointly by the target covariance kernel and the predictor NTK, rather than by either one alone. This identifies overgeneralization as spectral under-excitation. Motivated by this view, we formulate spectral target design as a principle for shaping RND novelty geometry. As a concrete instance, we replace the implicit random-network target with a bandwidth-controlled Random Fourier Feature (RFF) target, redistributing residual signal toward modes less attenuated by the predictor. Experiments on offline D4RL, online Atari, and Fetch manipulation benchmarks show improved novelty discrimination and downstream RL performance. The code for the RL implementation is available at this https URL.

---


### 122. [Structured Noise Diffusion for Echocardiography Haze Removal](https://arxiv.org/abs/2611.33860)

**<font color=#1a73e8>作者：</font>** Zike Luo, Hao Li, Mengxiao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Echocardiographic images are frequently degraded by spatially structured haze artifacts that obscure anatomical boundaries and hinder clinical analysis. Conventional diffusion models typically employ pixel-independent Gaussian noise, limiting their ability to represent localized ultrasound haze. In this study, we propose a structure-informed diffusion framework that explicitly models ultrasound haze as an accumulation of localized Gaussian components constrained by the ultrasound fan geometry. The forward process generates spatially correlated corruption by sampling component locations and scales, providing a formulation that better reflects the spatial characteristics of real echo artifacts. During reverse restoration, a dual-head network predicts an anchor probability map and Gaussian scale parameters to progressively remove structured artifacts while reducing the center bias associated with direct coordinate regression. We evaluated the framework on the public DehazingEcho2025 benchmark and two private clinical datasets, without retraining or fine-tuning on either private cohort. Our method achieved the highest mean generalized contrast-to-noise ratio across all three datasets, reaching $0.715 \pm 0.090$ on the public benchmark while preserving tissue edges.

---


### 123. [MAFNet-UR$^3$: Mask-Aware Fusion Network for Unified Raindrop and Reflection Removal](https://arxiv.org/abs/2611.33866)

**<font color=#1a73e8>作者：</font>** Yeongjin Jeong, Hyunjin Cho, Minsang Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Raindrops and reflections frequently co-occur on windshields and jointly obscure scene content, making their unified removal, referred to as UR$^3$, a highly ill-posed problem. Existing approaches are mainly based on diffusion models and thus can produce visually plausible restorations. However, they may generate scene-inconsistent structures in severely corrupted regions. To address this limitation, we propose MAFNet-UR$^3$, which adopts a three-stage framework to exploit multiple observations for scene-consistent unified raindrop and reflection removal. Specifically, Stage I suppresses raindrops while preserving the reflection layer, and Stage II performs prior-guided reflection removal followed by image-space refinement. Stage III estimates degradation masks from intermediate restoration results to provide degradation cues and performs mask-aware multi-scale fusion across observations to preserve scene structure and fine details. As a result, our proposed MAFNet-UR$^3$-L achieves state-of-the-art performance on the RDRF-testing benchmark, outperforming DiffUR$^3$ by 2.33 dB in PSNR and 2.7634 in the challenge score. Our method ranked third in the LoViF 2026 UR$^3$ Challenge, achieving a final score of 41.1416.

---


### 124. [Concept Generalization in Visual Brain Decoding via Encoder-Generated fMRI](https://arxiv.org/abs/2611.33870)

**<font color=#1a73e8>作者：</font>** Peter Yongho Kim, Juhyeon Park, Dongsheng Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual brain decoders are typically trained and evaluated on stimuli drawn from similar semantic distributions, leaving their ability to reconstruct unseen concepts poorly understood. We study this concept generalization problem by withholding semantic concepts from a target subject's training data. We find that three recent fMRI-to-image decoders degrade substantially for the held-out concepts, even when the concept remains available for multi-subject models. In contrast, brain encoders that map a pretrained visual representation directly to voxels are markedly more robust to the same semantic holdout. Motivated by this asymmetry, we use such an encoder to generate synthetic fMRI responses for new images and add the resulting image-fMRI pairs to decoder training. Across three decoders, four subjects, and twelve semantic concepts, synthetic data recovers a substantial fraction of the performance lost on unseen concepts without requiring additional, time-consuming fMRI acquisition. We further show that the same approach improves general decoding performance across a wide range of data budgets. Analyses of encoder training conditions, encoder designs, and synthetic-data controls show that the gains depend on both encoder generalization and the semantic content of the synthetic supervision, rather than merely increasing the amount of training data. Together, our results show that encoder-generated fMRI can transfer semantic generalization to decoders.

---


### 125. [Normalizing Flows are Capable World Models](https://arxiv.org/abs/2611.33872)

**<font color=#1a73e8>作者：</font>** Zijia Li, Yong-Hyun Park, Shusheng Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A world model lets an agent anticipate the consequences of its actions and use imagined futures to make decisions. We introduce Normalizing-Flow World Model (NFWM), which pairs an invertible observation encoder with an action-conditioned probabilistic predictor. Because the encoder is invertible, the predicted distribution over latent states defines a distribution over future observations. Maximizing the exact conditional likelihood of those observations therefore trains the representation and dynamics jointly. An agent can plan directly in the learned latent space and decode sampled trajectories to inspect possible futures. On Teleport, these samples capture the two possible outcomes of the same action. In Flappy Bird, a world model trained by likelihood alone supports reward-based planning that reaches 100 pipes in all ten evaluated games. For goal-conditioned control, an auxiliary inverse-dynamics objective shapes the coordinates used to compare predicted states with a goal. On LIBERO, NFWM uses this distance to select successful action sequences more often than LeWM and SMWM. In Atari Boxing, training on imagined trajectories improves a policy beyond its behavior-cloned initialization. Together, these results establish normalizing flows as capable world models.

---


### 126. [X-Matte: VAE-Free Pixel-Space Flow Matching for Single-Step Image Matting](https://arxiv.org/abs/2611.33874)

**<font color=#1a73e8>作者：</font>** Zanyi Wang, Jiaang Li, Dengyang Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pre-trained generative models offer rich visual priors for image matting, but their adaptation often relies on variational autoencoders (VAEs), whose spatial compression can degrade fine alpha details and introduce additional inference overhead. To address these limitations, we propose X-Matte, a VAE-free pixel-space flow matching framework for single-step image matting. By eliminating latent compression, X-Matte formulates the RGB-to-alpha transition as a continuous flow directly in pixel space. We adopt trajectory-wide x-prediction with transition-aware alpha supervision, enabling the model to learn from intermediate states while directly predicting the target alpha matte in a single forward pass. This design avoids both VAE encoding and decoding and iterative sampling. Extensive experiments demonstrate performance competitive with state-of-the-art trimap-free matting methods on P3M benchmarks, together with promising zero-shot generalization to RWP-636 and AIM-500. Moreover, X-Matte achieves up to a 9.4x inference speedup over a constructed single-step latent counterpart at high resolution, demonstrating the effectiveness of VAE-free pixel-space modeling for accurate and efficient image matting.

---


### 127. [Random Voronoi Networks](https://arxiv.org/abs/2611.33875)

**<font color=#1a73e8>作者：</font>** Ray Verma, Pau Mateo-Bernardó, Daniel Mas Montserrat 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nearest-neighbor methods are local, simple, and interpretable, but their non-parametric form makes them memory-intensive, expensive at inference, and difficult to integrate into differentiable neural architectures. We introduce Random Voronoi Networks (RVNs), a family of structured three-layer MLPs that express nearest-neighbor geometry through sampled Voronoi comparisons. The first layer computes Random Voronoi Features (RVF) from affine pairwise separators between selected training samples, the second layer aggregates these comparisons into Voronoi cells or top-k neighborhood scores, and the readout layer produces classification or regression predictions. We show that, when all samples and pairwise comparisons are included, step RVNs recover exact Euclidean k-NN, while ReLU RVNs provide a violation-score realization for 1-NN that can be relaxed into a differentiable soft weighting. Subsampling yields approximate RVNs with explicit control over the number of cells and features. We study several unsupervised sampling methods that trade off random coverage, directional diversity, coordinate sparsity, and empirical feature variance. Empirically, RVFs produce a highly effective data encoding strategy, providing performance boosts to downstream methods ranging from linear to modern tabular deep learning models. Finally, we showcase that RVF provides an interpretable feature map due to its k-NN based construction and ties to pairwise local directions. These results position our Random Voronoi formulation as a bridge between nearest-neighbor rules, random features, and modern tabular models.

---


### 128. [LayoutRecall: Preserving Appearance in Multi-Round 3D Layout-Controlled Image Editing](https://arxiv.org/abs/2611.33885)

**<font color=#1a73e8>作者：</font>** Yankuan Chi, Xin Lin, Baihan Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D layout-controlled image editing gives users explicit control over object placement and camera viewpoint. In a sequence of edits, however, the latest image can lose the appearance of an object when it is occluded or leaves view. The target layout specifies where the object should reappear, while its appearance must be recovered from earlier observations. We introduce LayoutRecall, a multi-round editor that stores and reuses appearance in the local coordinate systems of 3D boxes. Box-Surface Latent Memory retains image latents on box faces and retrieves them along rays in the target view. Geometry-Aligned Memory Conditioning supplies the retrieved tokens to a FLUX.2 editor using target-view positions, shared box-local embeddings, and object-wise attention. A correspondence loss encourages the editor to attend to matching observations during denoising. We also introduce LayoutLoop, a multi-round 3D layout-controlled image editing benchmark with calibrated layouts and designed revisits. We conduct extensive experiments on LayoutLoop and real-scene data to verify the ability of our method. The project page is at this https URL.

---


### 129. [DeltaRAE: Derivative Tokenization for Long Video Generation](https://arxiv.org/abs/2611.33886)

**<font color=#1a73e8>作者：</font>** Mingzhuo Yu, Shengcao Cao, Chengzhi Mao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent video generators are trained on clips of a few seconds, and much of this limit lies in their tokenizers, which spend as many tokens on a static frame as on a moving one and need future frames that do not exist during generation. We introduce DeltaRAE, a causal representation autoencoder for video. Its derivative tokenization encodes periodic anchor frames in full and all remaining frames with a few tokens each, and its causal encoder and decoder read a frozen pretrained image encoder. On UCF-101 and Kinetics-600, a standard diffusion transformer trained on DeltaRAE latents is competitive with state-of-the-art video tokenizers. DeltaRAE halves the tokenizer GFLOPs on 16-frame clips relative to keeping the same number of patch tokens for every frame, and it represents a minute of video with 18.8x fewer tokens. The tokenizer trains end to end on one-minute videos, and in video prediction a generator on its latents produces a full minute of video. The same generator collapses within 15 seconds in most videos when the tokenizer has the same token budget but no pretrained encoder.

---


### 130. [On the Learnability of Model Reprogramming: A Reachability and Relabeling Perspective](https://arxiv.org/abs/2611.33889)

**<font color=#1a73e8>作者：</font>** Zesheneg Ye, Pin-Yu Chen, Feng Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model reprogramming adapts a frozen source model to a target task by wrapping it in a learnable input transformation from target input to the source-model input space, and an output mapping from source-model outputs to target predictions. Despite extensive empirical progress, the finite-sample learnability of the induced wrapper hypothesis class $\mathcal{F}_{\rm MR}$ remains underexplored. We address this for source models that expose hard source labels and analyze it through the wrapper structure: on any target samples, the input transformation selects reachable source labels that the output mapping relabels. Through this lens, we answer two questions: (1) how many target samples are needed to approach the best predictor in $\mathcal{F}_{\rm MR}$, and (2) what gap remains between the optimum over $\mathcal{F}_{\rm MR}$ and the target Bayes risk. For (1), the wrapper structure factorizes the sample-wise complexity of $\mathcal{F}_{\rm MR}$ into a reachability term counting reachable source-label patterns, and a conditional relabeling term counting their relabelings. This yields an agnostic-PAC bound on the estimation error, with sample complexity scaling additively in the two terms; this bound becomes closed-form on additive input transformations and is matched by a lower bound on an explicit binary classification construction. For (2), the same structure decomposes the approximation error exactly into the source-label information loss and output-mapping restriction with a source-conditional upper bound on this gap. We extend the approximation analysis to logit-exposing source models, where the upper bound is empirically estimable. The wrapper-side analysis localizes both errors to specific components, giving a structural view of reprogramming practice.

---


### 131. [SIA: Selective Image Analogy](https://arxiv.org/abs/2611.33894)

**<font color=#1a73e8>作者：</font>** Amirhossein Alimohammadi, Kian Izadpanah, Bardiya Kariminia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image analogy transfers a demonstrated transformation from a before/after pair (A, A') to a new query image B. Existing methods assume all changes in (A, A') should be fully transferred, limiting flexibility when users want only a subset of the demonstrated edits. We introduce Selective Image Analogy (SIA), a new setting where a single demonstration pair encodes multiple edits, and the user selects at inference time which edits to apply to B. To support this, we curate a multi-edit analogy dataset with full-edit and partial-edit targets. We then train a model that first learns to transfer the complete demonstrated transformation, and then gains selective control through a mask-aligned suppression mechanism: a token-gated LoRA that restricts adapter updates to suppressed edit tokens during denoising, paired with a concept suppression vector that weakens the selected tokens in the text embeddings before denoising. Together, these components allow SIA to suppress unwanted edits that remain visible in A', while preserving the user-selected ones, all without requiring a new demonstration pair for each edit combination. We perform extensive quantitative and qualitative evaluations along with user studies to demonstrate the efficacy of our approach.

---


### 132. [TWIST: Teacher-Weighted Initial-Noise Spherical Transform for Quality-Preserving Diversity in Distilled Diffusion Models](https://arxiv.org/abs/2611.33895)

**<font color=#1a73e8>作者：</font>** Shayan Baghayi-Nejad, Jeongsol Kim, Jong Chul Ye  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Timestep-distilled diffusion models generate high-quality images in one or a few steps, but often suffer from reduced mode coverage and limited diversity. Recent methods improve diversity by optimizing the initial noise at inference time, requiring costly backpropagation through the denoiser. Moreover, their diversity objectives typically repel generated samples without accounting for how the corresponding teacher model distributes its outputs. We introduce Teacher-Weighted Initial-noise Spherical Transform (TWIST), a lightweight network that transforms the low-frequency components of initial noise to improve diversity without inference-time optimization. TWIST uses a teacher-guided determinantal point process (DPP) objective to align the feature-space diversity of student samples with that of the teacher. By amortizing noise optimization into a single network, TWIST eliminates inference-time backpropagation while preserving the efficiency of few-step generation. On SDXL-Turbo, TWIST matches the diversity of MoNO at less than 25% of its inference cost, while achieving higher recall and better PickScore, ImageReward, and CLIPScore under matched compute budgets. On SDXL-Lightning, it achieves comparable recall at lower cost without the ImageReward degradation observed with MoNO.

---


### 133. [Correlation-Aware Evidential Fusion for Trusted Multi-View Classification](https://arxiv.org/abs/2611.33900)

**<font color=#1a73e8>作者：</font>** Tianyang Wang, Mengchi Zuo, Cai Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trusted multi-view classification aims to make accurate and reliable predictions by integrating information from multiple views. Existing methods typically estimate class evidence and uncertainty for each view and combine the resulting opinions through aggregation rules. However, they generally treat different views as independent information sources, overlooking the correlations among them. Highly correlated views tend to produce similar evidence, and treating them as independent sources may repeatedly count consistent information and give it disproportionate influence, while weakening complementary evidence that provides additional information. Consequently, such correlation-unaware fusion may not only limit classification performance but also produce miscalibrated uncertainty estimates. To address this issue, we propose Correlation-Aware Fusion of Evidence (CAFE), a framework for trusted multi-view classification. CAFE applies complementarity-based trust discounting to the evidence produced by view-private experts and introduces a correlation-aware constraint to reduce the repeated contribution of similar evidence. It then learns sample-specific weights from the global multi-view context to adaptively combine the correlation-adjusted private evidence with cross-view collaborative evidence. Extensive experiments on six real-world datasets demonstrate that CAFE consistently improves classification and calibration performance in general settings, with particularly significant gains when strong correlations exist among views.

---


### 134. [RelPRM: Grounding Visual Process Reward Models in Relational Evidence](https://arxiv.org/abs/2611.33903)

**<font color=#1a73e8>作者：</font>** Zhaoxing Zhang, Ziqiu Gui, Cheng Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual process reward models (PRMs) can detect calculation errors yet assign high scores to steps that misread visual relations. Supervision based on subsequent answer success does not directly establish whether a step's relational claim holds. To strengthen visual-relation verification, we first build an automated pipeline that programmatically verifies each claim and identifies the required objects, relations, and image regions. It produces RelProcessTrain and RelProcessBench (RPB), which tests whether scores respond appropriately to relational evidence through controlled image edits and step rephrasings. Building on this pipeline, we further introduce RelPRM, a visual-relation-oriented method for process reward modeling with two training mechanisms. Relation-evidence self-distillation constructs views preserving necessary objects, relations, and dependencies, reducing the burden of finding decisive evidence in complex scenes and transferring reliable evidence-assisted judgments to full images. Relation-evidence-driven consistency training encourages appropriate score changes when relation edits reverse a step's truth, stability under irrelevant edits, and similar score changes across paraphrases. At inference, RelPRM directly scores the current step using only the original image and reasoning context. RelPRM achieves 66.2% on VisualProcessBench (VPB) and 68.4% on RPB, gains of 4.2 and 9.9 percentage points over VisualPRM-8B. These results show that training for visual relations improves both relational verification and step assessment across broader multimodal reasoning tasks.

---


### 135. [Tortho-Gaussian++: Suppressing Geometric Drift and Floaters for Robust Gravity-Aligned TDOM Generation in Large-Scale Aerial Scenes](https://arxiv.org/abs/2611.33905)

**<font color=#1a73e8>作者：</font>** Xiang Wang, Xin Wang, Zongqian Zhan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has demonstrated remarkable performance in aerial scene reconstruction, motivating its recent extension to true digital orthophoto maps (TDOMs) generation. We propose Tortho-Gaussian++, a novel 3DGS training framework that suppresses geometric drift and floaters and automatically prunes unreliable peripheral regions, coupled with a robust gravity-aligned TDOM rendering solution. First, we explore geometric support via viewing-ray-based geometric observability analysis, quantitatively characterizing the reliability for each Gaussian and subsequently pruning peripheral regions with particularly weak geometric support. Second, the optimizer state initialization is refined for newly created Gaussians during densification, intrinsically suppressing drift and floaters without external priors. Lastly, a robust gravity direction estimation solution is designed, combining image-derived gravity cues, camera-distribution priors and nadir views, to achieve a gravity-aligned orthogonal projection reference for TDOM rendering. Extensive experiments on multiple large-scale UAV (Unmanned Aerial Vehicle) datasets demonstrate that our Tortho-Gaussian++ outperforms vanilla 3DGS by 0.5-3.5 dB in average PSNR and yields comparable or superior performance to prior-guided 3DGS methods. Notably, it reduces the training time, VRAM and Gaussian number by 45.5%, 47.2%, and 58.6%, respectively. Qualitative evaluations confirm that our method effectively suppresses drift and floaters, while robust gravity direction estimation reduces tilt-induced facade artifacts in TDOMs.

---


### 136. [EGSE: Evidence-Grounded Skill Evolution for Medical Reasoning Agents](https://arxiv.org/abs/2611.33909)

**<font color=#1a73e8>作者：</font>** Mingyuan Li, Tong Jia, Ziyuan Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical reasoning agents combine foundation models with specialized tools to interpret medical images, yet reusing their historical experience remains challenging. A correct final answer can conceal flawed reasoning or tool use, synthesized advice may lack source support, and superficially similar cases may require different diagnostic procedures. In this paper, we propose EGSE, an evidence-grounded skill evolution framework that distills historical dialogues from similar cases into reusable conditional workflows and progressively refines a multi-faceted skill library through supported and validated updates to improve medical agents. EGSE evaluates intermediate reasoning and tool use and contrasts repeated successful and failed rollouts to extract useful practices and evidence-supported avoidance guidance. These experiences are synthesized into workflows with applicability conditions and checks traceable to source dialogues. Library additions and merges require source-grounded review and execution validation. At inference time, EGSE routes queries to skill nodes organized by imaging modality, question task type, and disease category, then retrieves and selects applicable workflows based on their conditions, the current images, and the question to guide evidence acquisition and interpretation. Experiments across four chest X-ray benchmarks show that EGSE outperforms representative medical agents and skill evolution methods in reasoning accuracy while reducing tool calls. It also delivers consistent accuracy gains across seven foundation models and supports skill transfer across datasets.

---


### 137. [Event-WAM: Learning to Act with Event-Derived Futures](https://arxiv.org/abs/2611.33917)

**<font color=#1a73e8>作者：</font>** Jongseong Bae, Hyunwoo Kim, Yeongin Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) leverage future visual modeling for robotic action learning, with recent studies exploring alternative or complementary objectives beyond conventional RGB prediction. We introduce Event-WAM, which incorporates event-derived visual changes as auxiliary future supervision alongside RGB. Event-WAM constructs temporally structured event representations from RGB demonstrations and encodes them using a frozen pretrained RGB video VAE, without training an event-specific VAE. Joint RGB--Event latent flow matching provides appearance- and change-oriented supervision without requiring event observations or explicit future generation at inference. Across simulated benchmarks, Event-WAM maintains comparable performance under standard conditions, while robustness gains under perturbations are benchmark-dependent, including improvements on LIBERO-Plus. Real-world evaluations further demonstrate improved manipulation success under both standard and unseen perturbation conditions. Further analyses show that policy improvements are not consistently accompanied by higher future prediction fidelity, suggesting the potential of change-oriented supervision for action learning.

---


### 138. [UPP-Gauss: Ultrasound Propagation Physics-informed Gaussian Splatting for B-mode Novel-View Synthesis](https://arxiv.org/abs/2611.33920)

**<font color=#1a73e8>作者：</font>** Guil Jung, Seok-Hwan Oh, Myeong-Gee Kim 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate novel-view synthesis of B-mode ultrasound images requires modeling acoustic propagation through tissue and the resulting appearance variations across probe poses. We propose Ultrasound Propagation Physics-informed Gaussian Splatting (UPP-Gauss), which integrates these acoustic interactions into an explicit Gaussian representation. UPP-Gauss constructs acoustic maps by sampling three 3D Gaussian fields using the probe pose and acoustic beam propagation direction, then combines these maps according to ultrasound propagation to synthesize B-mode images. Across three acoustically diverse datasets, UPP-Gauss achieves the best reconstruction quality with efficient rendering, improving PSNR over the best baseline on each dataset by 1.43 dB on average. These results demonstrate accurate and efficient B-mode novel-view synthesis through explicit Gaussian modeling of ultrasound propagation.

---


### 139. [CondUQ: Calibrated Conditional Uncertainty Quantification Using Distribution Matching](https://arxiv.org/abs/2611.33939)

**<font color=#1a73e8>作者：</font>** Shizhuang Wang, Tianhao Wang, Xingqun Zhan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many applications, especially reliability- and safety-critical ones, require accurate uncertainty quantification for the outputs of model- or learning-based measurement, estimation, and prediction systems. The errors of such systems often vary with factors such as input quality and operating conditions, and thus cannot be accurately described by a single Gaussian model. Although Gaussian mixture models and calibrated quantiles can approximate such error distributions, their unconditional forms do not capture how the error behavior depends on these factors. Hence, we propose condUQ, an approach that conditions error models on observable factors for enabling accurate and reliable uncertainty quantification. condUQ is built on top of an existing system without modifying it and applies even when the system is a black box. First, condUQ maps the observable factors to a latent quality index (QI) such that errors sharing the same QI follow a common, approximately Gaussian conditional distribution. The QI predictor is trained end-to-end with a distribution-matching objective, without requiring quality labels. Second, for each QI, a Gaussian error model is then fitted and calibrated on a large held-out dataset. condUQ is demonstrated on three examples: (a) GPS multipath errors conditioned on satellite elevation and signal strength, (b) relative attitude errors of a transformer-based visual relative pose regression model conditioned on its internal features of the image pairs, and (c) prediction errors of a world model conditioned on the input observations and actions. In all three examples, condUQ substantially reduces the discrepancy between the modeled and empirical error distributions compared with a single global model. Moreover, the learned QIs reveal how the underlying factors affect the error characteristics in a manner consistent with physical principles.

---


### 140. [TAT-Det: A Dataset for Testicular Appendage Torsion Detection and Segmentation in Ultrasound Images](https://arxiv.org/abs/2611.33940)

**<font color=#1a73e8>作者：</font>** Ying Jiang, Juntao Jiang, Linxuan Fan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background: Testicular appendage torsion (TAT) is the leading cause of acute scrotal pain in prepubertal children. Yet, its diagnosis remains challenging due to nonspecific clinical manifestations and the absence of standardized datasets for pediatric acute scrotal emergencies.
Results: We present TAT-Det, an expert-annotated ultrasound dataset specifically designed for TAT. TAT-Det comprises 2,600 ultrasound images from 1,203 patients collected at the Children's Hospital, Zhejiang University School of Medicine. Each TAT-positive image is accompanied by lesion-level bounding boxes for detection and pixel-level segmentation masks for fine-grained delineation. Annotations were produced through a multi-stage workflow involving independent annotation by board-certified pediatric sonographers, consensus review, and refinement. Baseline benchmarks for object detection and semantic segmentation using representative deep learning models are further provided, with YOLO11m achieving the best detection performance and RWKV-UNet the best segmentation performance.
Conclusions: TAT-Det addresses the lack of publicly available resources for pediatric emergency ultrasound and establishes a foundation for developing and evaluating artificial intelligence methods for automated TAT analysis.

---


### 141. [Should Service Requirements Be Scalarized or Constrained When Minimizing Costs? A Case Study on HVAC Control](https://arxiv.org/abs/2611.33946)

**<font color=#1a73e8>作者：</font>** Tai-You Chen, Mihael Mohorcic, Blaz Bertalanic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated decision systems, from learned policies to model-based optimizers, often minimize costs such as energy or resource use while meeting a service requirement, for example the quality of service (QoS) specified in a service level agreement (SLA), a comfort band, or a safety margin. The requirement can be scalarized with the costs into a single objective, with a fixed or an adaptively tuned (Lagrangian) weight, or it can be imposed as a constraint. We study this choice in the Smart Buildings Challenge, in which a single policy controls the heating, ventilation and air conditioning (HVAC) of previously unseen buildings and is evaluated by a weighted sum of comfort, energy cost and carbon emissions. With all other components fixed, we compare the two treatments in model-based optimization, represented by model predictive control (MPC) with the requirement as a hard or a soft (l1-penalized) constraint, and in learned policies, represented by proximal policy optimization (PPO) with a fixed or a Lagrangian penalty in the reward or a projection layer on the action. In MPC, the soft constraint reproduces the hard one once its weight exceeds the requirement's shadow price, which the challenge's comfort weight exceeds approximately fourfold; below this weight, comfort is sacrificed, and under a metric that values comfort below its shadow price the soft constraint outperforms the hard one by up to 28%. A weight tuned on the training buildings is 3.9% worse than the hard constraint on 48 unseen buildings, because the shadow price varies across buildings. In PPO, the projected policy satisfies the requirement from the outset and leads early in training; with longer training, the Lagrangian policy overtakes it while the projected policy deteriorates, and the fixed penalty does not learn to satisfy the requirement.

---


### 142. [A Computational Model of Continuous Recognition Memory for Natural Images](https://arxiv.org/abs/2611.33947)

**<font color=#1a73e8>作者：</font>** Sheng Zhao, Yijin Wang, Bei Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recognizing an image we have seen before is a basic function of human visual memory. Understanding human continuous recognition memory (CRM) can help machine vision systems predict which images people are likely to remember and generate more memorable images. It can also inform the diagnosis of memory impairments and the development of interventions to improve memory. This paper proposes the first computational model for CRM. The model captures three key components of continuous recognition memory (CRM): image encoding, memory decay, and decision making. It encodes each image as a distinct random variable in a perceptual space. As the memory of an image fades, the distribution of its random variable drifts within that space. To decide whether the current image has been seen before, the observer retrieves samples from the distributions associated with previously encoded images and compares them with the current image. Our model predicts human observers' trial-by-trial responses in CRM tasks within the variability observed across human participants. Our model is parameter efficient, requiring only four shared parameters and two parameters per observer. It can accurately predict the memorability of an image no worse than prior methods that require millions of parameters.

---


### 143. [Where to Approximate: Understanding and Accelerating Looped Multi-View Reconstruction](https://arxiv.org/abs/2611.33948)

**<font color=#1a73e8>作者：</font>** Siyuan Zhang, Yuhan Chen, Yangyang Ning 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Looped multi-view reconstruction refines scene features by repeatedly applying a shared transformer block. Making these updates cheaper requires knowing how an approximation at one step affects the rest of the refinement. We study this with paired interventions in Déjà View and stacked reconstruction transformers, separating the error an approximation injects, how that error propagates, and how it affects the output. In Déjà View, approximation errors are attenuated more strongly than matched random perturbations under a scale-adjusted state-error measure, and a local Jacobian decomposition separates the contribution of channel gating from the response to spatial error structure. Spatial approximations made early benefit from subsequent refinement, whereas cross-step reuse depends on which quantity is cached and how reuse steps are spaced. At equal final norm, approximation errors change the predicted rotations 1.55 times as much as random errors. These findings guide our proposed method, which reduces spatial resolution and pools keys and values early in refinement, then interleaves attention-output reuse with full attention, and is adapted through lightweight self-distillation. Across five reconstruction benchmarks, the balanced configuration runs $1.63\times$ faster than the official 16-step Déjà View model with a 1.86-point reduction in average pose AUC@$3^\circ$. At matched latency, it exceeds the interpolated curve of a trained baseline using full refinement blocks by 4.73 points in AUC@$3^\circ$ and improves the corresponding geometry metrics.

---


### 144. [BReD: Block Replay Dithering for Stable Low-Bit EMA Optimizer States](https://arxiv.org/abs/2611.33951)

**<font color=#1a73e8>作者：</font>** Heshen Zhan, Youhan Huang, Yunke Peng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-bit storage of optimizer states can substantially reduce the memory footprint of large-scale training. In practice, however, these states are not quantized once: at every training step, they are dequantized, updated, requantized, and written back. This iterative quantization pipeline can destabilize training. We identify a failure mode behind this instability: for states updated via exponential moving averages (EMAs), quantization errors are recursively fed into subsequent updates. As a result, biased errors accumulate over time while high-variance errors are amplified, particularly when the EMA decay factor is close to 1. To address this error accumulation, we propose BReD (Block Replay Dithering), a method that reduces rounding bias and controls rounding variance during quantization. BReD adapts classical subtractive dithering to optimizer-state quantization by combining deterministic seed replay with block-wise shared dither values, avoiding auxiliary random-tensor storage and per-element dither values generation. Across the default pretraining settings (five optimizers at 120M; AdamW and Muon at 1.1B and 3.4B model) and supervised fine-tuning (AdamW and Muon at 7B model), 4-bit BReD closely matches training with full-precision optimizer states, with PPL shifts $\leq0.5$ in pretraining and $\leq0.2$ in fine-tuning and average downstream performance changes within 0.7 points. Moreover, 3-bit BReD preserves stable convergence in the evaluated settings, offering a more aggressive alternative. Our implementation of BReD is available at: this https URL

---


### 145. [PINN-Slicer: Exploiting Rotational Symmetry to Solve the Photon Orbit Equation Around a Black Hole](https://arxiv.org/abs/2611.33953)

**<font color=#1a73e8>作者：</font>** Claire David, Tlotlo Oepeng, Harrison B. Prosper  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) typically struggle with long-horizon domains, often requiring the network to be retrained as the domain grows. We present PINN-Slicer, a method for second-order autonomous ordinary differential equations, $\ddot{u} = G(u, \dot{u})$, which exploits the invariance of this class of equations under translations of the independent variable. A single PINN, embedded within a solution ansatz that enforces the initial conditions explicitly, is trained on a thin slice of the independent variable using Sobol-sampled initial conditions. The PINN is then deployed recursively, slice-by-slice, across the full domain. We demonstrate PINN-Slicer on the nonlinear equation that describes photon orbits around a black hole, and reach a point-by-point root-mean-square error (RMSE) below $10^{-3}$ in $u = r_s/r$ (the inverse radial coordinate in units of the Schwarzschild radius) relative to a finite-difference reference solution. A key advantage of PINN-Slicer is that a single trained network generalizes to any orbital initial condition within the training range, without retraining. In addition, PINN-Slicer can cope with solution domains that may not be known a priori.

---


### 146. [RefMix: Expanding Endpoint Proposals for Diversity-Preserving Reward Fine-Tuning](https://arxiv.org/abs/2611.33957)

**<font color=#1a73e8>作者：</font>** Jaemin Kim, Christian Simon, Dongseok Shim 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online forward matching aligns flow-based generative models by repeatedly generating, rewarding, and fitting model-produced endpoints. However, this behavior creates an on-policy feedback loop: as high-reward modes become increasingly favored, alternative modes become less likely to appear in subsequent training pools, progressively reducing visual diversity. We introduce RefMix, a reference-assisted endpoint proposal strategy that addresses this limitation by injecting alternative candidates into the training pool while retaining the original task reward and forward matching objective. In particular, RefMix uses a reference model during early high-noise steps to expose alternative visual modes, followed by the current reward-tuned model for endpoint completion. Across state-of-the-art online forward matching methods, RefMix consistently improves visual diversity while preserving task reward performance. Controlled inference experiments further demonstrate that training-time endpoint exposure is critical to improve reward--diversity trade-offs, beyond the impact of reference-assisted inference. By rethinking how training endpoints are proposed, RefMix achieves up to 44% higher diversity over forward matching baselines at comparable reward levels.

---


### 147. [Where Does Free-Text 3D Grounding Fail? An Error Analysis of Report-Sentence Segmentation in Chest CT](https://arxiv.org/abs/2611.33958)

**<font color=#1a73e8>作者：</font>** Abdullah Arif Sheikh, Kamalaker Dadi, Raju S. Bapi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Free-text 3D grounding, segmenting in a CT volume the region described by one sentence of the radiology report, could link reports to images at scale, but it is unclear where current models fail. We analyse the publicly released VoxTell model on all 381 findings of the 200-scan ReXGroundingCT validation set, where it grounds 53.5% of findings. Its failures are rarely about which lesion or side is meant. No miss lies on the side opposite to the one named, and findings are almost never confused with one another. Instead, predictions are too large, land on a neighbouring lesion on the correct side, or are missing for small findings, and diffuse findings are rarely grounded. Removing location words halves performance, to the level of label-only prompting, and anatomical rules derived from the sentence never improve the full-sentence output. The same pattern holds on the hidden 300-scan test set. Further progress therefore depends on extent estimation and small-lesion sensitivity rather than on anatomical post-processing.

---


### 148. [Embodied-VGGT: Preserving Reliable Local Geometry for Long-Sequence Reconstruction](https://arxiv.org/abs/2611.33964)

**<font color=#1a73e8>作者：</font>** Yiheng Han, Ziang Chen, Zhuyong Fu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long sequence reconstruction must correct accumulated drift while preserving locally consistent geometry. In robotics and autonomous driving, embodied acquisition provides recurring platform- environment geometry and repeated observations of scene structure and platform motion. We present Embodied-VGGT, which exploits these cues to establish reliable local relationships and selectively preserve them during global refinement. Memory-Augmented Grounded Chunks (MAGC) builds on Scal3R's global context memory and uses relative scale references derived from predicted ground geometry to regularize test-time memory updates, encouraging cross-chunk consistency while limiting changes to reliable local geometry. Superpoint Alignment (SA) and Cross-Loop Optimization (CL) jointly address the robust establishment and preservation of geometric relationships. SA balances ground and non-ground evidence across spatial regions to estimate inter-chunk translation. CL uses geometric and motion consistency across interleaved windows to select coherent chunk groups, each receiving a shared Sim(3) correction that preserves its internal relative transformations during global optimization. Experiments on five public driving benchmarks demonstrate consistent and substantial improvements in long sequence reconstruction. On KITTI Odometry, Embodied-VGGT achieves a mean absolute trajectory error of 7.30 m and a Chamfer distance of 2.67 m, reducing these errors by 46.8% and 23.3% compared with the state-of-the-art baseline under same evaluation protocol. To facilitate reproducibility, we released our code: this https URL.

---


### 149. [FasterGRN: Reducing the Refinement Redundancy for Accelerating Generative Refinement Networks](https://arxiv.org/abs/2611.33982)

**<font color=#1a73e8>作者：</font>** Ziqian Zhang, Pengcheng Wang, Yulong Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Departing from the paradigm of diffusion and autoregressive models, Generative Refinement Networks (GRN) enables high-quality image generation through iterative refinements. However, this repeated processing over the entire visual representations results in substantial computation overhead. Furthermore, the binary representations and global refinement mechanism in GRN disable the direct application of acceleration strategies developed for other generative models. To accelerate GRN model, we first observe several key properties by analyzing the entire generative process. That includes the stage characteristic, dual branch similarity and more importantly, the $\textbf{refinement redundancy}$. Motivated by the observations, we present $\textbf{FasterGRN}$, a training-free acceleration method for the Generative Refinement Network. $\textbf{FasterGRN}$ first divides the GRN into the semantic establishment stage and detail refinement stage according to its semantic establishment. For alleviating the refinement redundancy mainly resulting from the detail refinement stage, we propose Adaptive Retention Expansion ($\textbf{ARE}$) and Selective Token Freezing ($\textbf{STF}$) to shrink refinement steps and reduce token computations, respectively. In the experiments on GenEval and DPG-Bench benchmarks, our method $\textbf{FasterGRN}$ achieves a $2.03\times$ sampling speedup while largely preserving image generation performance. Our evaluation on COCO datasets additionally demonstrates that $\textbf{FasterGRN}$ even outperforms the original GRN in image fidelity.

---


### 150. [MolGPAO: Molecular Generative Pre-trained Autoregressive Octree with Speculative Decoding and Sub-Millisecond Seam Healing for 3D Molecules](https://arxiv.org/abs/2611.33985)

**<font color=#1a73e8>作者：</font>** Shangqian Chen, Guojiang Zhao, Zheng Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive generation over adaptive 3D octrees (Uni-3DAR) offers an intrinsic $O(N \log N)$ sparsity advantage over dense $O(N^2)$ equivariant diffusion and flow models on large drug-like molecules, yet lags in geometric equilibrium, closed-shell valence stability, and property fidelity due to Morton-seam coordinate jumps, leaf-heavy compute with root-count trapping, and target-shortcut collapse in internal critics. We introduce MolGPAO (Molecular Generative Pre-trained Autoregressive Octree), a standalone 3D octree architecture and single-output speculative tree-decoding engine using zero external surrogates, zero reinforcement learning, and zero inference-time MLIP relaxation. MolGPAO unifies: (1) non-trapping 6-D ScaleFreeBudgetEmbedding with L5-to-L1 covalent packing priors; (2) a FlashAttention-2 pause-and-gather speculative octree funnel ($m_{s1} \to m_{s2} \to 1$, $M_{\mathrm{out}} = 1$); (3) an anti-shortcut ground-truth TwoStageOctreeProcessCritic with 64-RBF covalent edge gating and $SO(3)$-invariant 12-channel multipole norms (blind QM9 $r = 0.9867$--$0.9989$); (4) a $<0.5$ ms 4-layer $SE(3)$ PostTreeGraphRefiner for Morton-seam healing, expected-XYZ bonded supervision, selective CFG, and zero-heavy-displacement valence reconciliation; and (5) bubble-free stride-2 GPU leaf decoding. Across GEOM-Drugs (0.49 GPU-h), disjoint 50k/50k QM9 (0.43 GPU-h), and PBE0/def2-TZVP-verified OE62 (0.56 GPU-h), MolGPAO lifts drug-scale valid-connected yield 6.78x (12.7% to 86.2%, 99.83% atom stability), runs 7.3x faster (or 1.65x faster at 2.0x yield) than 100-step FlowMol at $N=100$, beats 156 GPU-h PropMolFlow on QM9 HOMO (-12.7%) and dipole (-21.0%) at 362x lower compute, and doubles live DFT hit rate on OE62 (33.3% vs. 16.7%) at 92.8x lower compute.

---


> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-314](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
