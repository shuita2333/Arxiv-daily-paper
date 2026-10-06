# 📦 其他研究 | 2026年10月07日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

---

### 101. [Trust the View That Sees the Target: Mining Cross-View Conflicts for Reliability-Gated Disaster Damage Assessment](https://arxiv.org/abs/2610.04327)

**<font color=#1a73e8>作者：</font>** Yifan Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> After a disaster, building damage is assessed from overhead tiles and ground-level photographs, and most methods fuse the two views symmetrically, trusting both equally for every building. This paper focuses on the samples where that assumption fails: the conflict cases, on which two independently trained single-view models disagree. We mine such cases from three paired collections (inspection photographs from the 2025 Eaton wildfire and street-view panoramas from Hurricanes Ian and Milton, each matched to very-high-resolution overhead tiles), where they make up 10-33% of the data. On these samples an oracle that simply trusts the correct view beats every fusion method we tested by 0.37-0.41 accuracy, and the gap survives longer training, calibration, and backbone changes. We recover part of it with a visibility-conditioned reliability gate: a linear model that decides which view to trust from building-visibility features, calibrated per-view confidences, and the disagreement itself. On the wildfire data the gate is the only method that significantly beats calibrated probability averaging (+0.051 on conflicts, p=0.0001) and end-to-end fusion (+0.072, p<10^-4); on the panoramic datasets it matches them. A controlled field-of-view experiment explains why: cropping panoramas toward the building doubles the benefit of fusion, whereas random crops of the same size do not. Finally, the spatial density of conflicts predicts tile-level damage without labels (Spearman r=0.615, p=0.001). Mining conflicts turns "does fusion help?" into "which view should be trusted, where, and why?".

---


### 102. [Synthetic-to-Real ViT-Based Pose Estimation of a Noncooperative UAV](https://arxiv.org/abs/2610.04335)

**<font color=#1a73e8>作者：</font>** Krishnanujam Srinivas, Hanish Acharla, Brij Agrawal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote pose estimation of noncooperative Unmanned Aerial Vehicles (UAVs) from imagery is critical, as they cannot be influenced or instrumented in advance. Deep-learning-based approaches offer a promising solution; however, their development is constrained by the cost and difficulty of acquiring large-scale real-world datasets with accurate pose labels. Synthetic imagery provides an alternative, but models trained on synthetic data must overcome the synthetic-to-real domain gap to generalize to real-world imagery. This work investigates the inherent synthetic-to-real generalization capability of a Vision Transformer (ViT)-based model for monocular UAV pose estimation. The proposed approach employs a self-supervised DINOv2 backbone and is trained exclusively on labeled synthetic imagery while being evaluated on labeled real-world imagery. Pose ambiguity-aware strategies are incorporated during training and inference to address ambiguities arising from the projection of a three-dimensional target onto a two-dimensional image plane and from target symmetries. An $\alpha$-$\beta$ filter is further integrated during inference to improve pose estimations. To assess the model under operational requirements, it is evaluated in terms of Mean Angular Error (MAE) and inference time, both before and after filtering, using a real-world dataset containing 77,077 labeled UAV images. Before filtering, the model achieves an MAE of $19.18^{\circ}$ and an inference time of $13.25$ ms, whereas after filtering, these values are $8.74^{\circ}$ and $13.42$ ms, respectively.

---


### 103. [A differentiable Lagrangian-coupled 3D Gaussian Splatting-SPH model for forward simulation and inverse analysis in solid mechanics](https://arxiv.org/abs/2610.04336)

**<font color=#1a73e8>作者：</font>** Tian Xu, Soroush Atashi, Tianju Xue  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative world models have increased interest in digital models that reproduce both the appearance of real objects and their response to physical interaction. Three-dimensional reconstruction techniques, including 3D Gaussian Splatting, capture detailed surface geometry and appearance from images and videos. However, extending these representations beyond plausible animation to mechanically interpretable models for constitutive behavior, boundary conditions, and inverse parameter identification remains less explored. In this work, a differentiable Lagrangian-coupled 3DGS-smoothed particle hydrodynamics (SPH) model is proposed for forward simulation and inverse analysis of deformable solids. The observed object is first reconstructed from multi-view calibrated visual dataset as a 3DGS rendering model. An envelope-based procedure then generates an independent SPH support for the solid-mechanics model, avoiding the direct use of rendering primitives as mechanical particles. A reference-configuration Lagrangian transfer maps SPH deformation to Gaussian positions and covariances, thereby coupling the physical model and the image observation model while preserving a differentiable computational path. The SPH formulation supports linear elastic, hyperelastic, and Kelvin--Voigt viscoelastic responses, together with fixed, free, and Robin-type boundary conditions. Numerical studies validate the SPH response against finite-element results, assess accuracy and efficiency against a conventional model using Gaussian centers as surface SPH particles, and demonstrate forward simulations on beam, bridge, and liver-shaped examples. Inverse analyses further estimate constitutive and boundary parameters from rendered deformation observations, including noisy cases, demonstrating the feasibility of the proposed model for mechanics-based parameter identification from image data.

---


### 104. [S$^3$N: A Spherical Spiral Scanning Network for Weather Forecasting](https://arxiv.org/abs/2610.04338)

**<font color=#1a73e8>作者：</font>** Fan Yan, Chen Hui, Weisi Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning-based weather prediction (MLWP) has achieved strong performance in global weather forecasting. Recent Hierarchical Equal Area isoLatitude Pixelation (HEALPix)-based methods use the HEALPix (HP) grid to avoid area distortion near the poles of conventional latitude-longitude (LL) grids. However, existing HP-based approaches often use pointwise mapping methods and process HP pixels within separate base faces or local windows. Consequently, the mapping may introduce reconstruction errors and cross-face communication depends on handcrafted boundary handling or shifted windows. We propose the Spherical Spiral Scanning Network (S$^3$N) to address both limitations. First, L2Proj provides a bidirectional method for mapping atmospheric fields between the LL and HP grids through an $L^2$ projection of their continuous finite-element representations. Second, the Attention-Guided Quad-Spiral State-Space Scanning (AQSS) block uses cross-latitude attention to guide selective state-space updates along four global pole-to-pole spiral paths. This design enables continuous information propagation across HP base-face boundaries without additional boundary-processing mechanisms. Experiments show that S$^3$N achieves better results at 4-, 7-, and 10-day lead times, and exhibits slower error growth in long-range forecasting.

---


### 105. [Any-scale Object Detection using Arbitrary-scaled Images](https://arxiv.org/abs/2610.04346)

**<font color=#1a73e8>作者：</font>** Kazutoshi Akita, Norimichi Ukita  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper proposes any-scale object detection using arbitrary-scale super-resolution for continuously rescaling object images, while general multi-scale object detection uses discretely rescaled appearance representations. However, a naive usage of super-resolution produces many false-positive detections if many super-resolution images are independently fed into an object detector. Our method suppresses these false positives by predicting scale proposal maps, each of which represents a set of pixels appropriate for each super-resolution scale.

---


### 106. [Evidence and Intervention: A Coupled Active-Inference Extension of Rational Speech Act Models](https://arxiv.org/abs/2610.04347)

**<font color=#1a73e8>作者：</font>** Yonghyeon Gwon, Elliot Murphy, Chun Kee Chung  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Identical utterance choices can arise from different communicative causes, and identical interpretations can leave different traces in what a listener learns. Rational Speech Act (RSA) models treat interpretation as inference over speaker meaning, but standard one-shot RSA does not intrinsically distinguish these causal update targets. We develop a coupled active-inference model of dialogue in which a listener's likelihood for an utterance is the policy distribution attributed to the speaker, placing the speaker's expected free energy within the listener's variational free energy. Each utterance is therefore both evidence about and an intervention on a partner. The model separates four updates that RSA approaches typically collapse: inference about the partner's current pragmatic state; learning of partner-specific parameters; prospective evaluation of clarification or repair; and a policy prior shaped by habit and a context-sensitive price of time. Under one-step, exact-inference restrictions, the model recovers the RSA speaker and listener, with RSA as the restricted single-turn limit of the coupled process. Outside these restrictions, the updates obey distinct rules and timescales, predicting which adaptations persist, remain partner-specific, or transfer. Worked examples show audience design reversing after clarification, self-confirming misunderstanding in which both interlocutors have low free energy while disagreeing about reference, and rational closing before uncertainty is resolved. Consistent with critiques of equating natural language with communication, the model treats communication as a downstream use of linguistic structure and recasts production and interpretation as coupled inference: speaking is both an intervention on a partner and an epistemic action that samples evidence for the speaker's model of that partner.

---


### 107. [LoCoSplat: Real-Time Feed-Forward 3D Gaussian Splatting with Minimal 3D Reasoning](https://arxiv.org/abs/2610.04351)

**<font color=#1a73e8>作者：</font>** Sinan Wang, Jinjin He, Yuchen Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting (3DGS) increasingly aggregates multi-view evidence with heavy learned 3D networks. We propose LoCoSplat (Local-Context Splatting), motivated by the observation that a Gaussian is a local primitive: once depth is predicted, what the 3D stage must add (scale, rotation, opacity) depends on the point cloud around each anchor, and a fixed local average of that neighbourhood is enough to supply it, no heavy network required. LoCoSplat realises exactly this average: it splats a 16-d linear projection of the point features into a fine and a coarse grid and reads both back at each anchor with a 0.14M-parameter pointwise MLP; with no learned 3D network and no dynamic sparse computation, its whole encoder runs as one fp16 CUDA graph. On RealEstate10K, LoCoSplat outperforms every prior feed-forward method on PSNR, SSIM, and LPIPS at 6, 12, and 24 views, with a margin that widens as views densify (+3.3 PSNR over VolSplat, the prior voxel-aligned state of the art, at 24 views) and grows further under zero-shot transfer to ACID and fine-tuning on ScanNet. It reconstructs a 6-view scene in 33 ms on one NVIDIA RTX PRO 6000 GPU, the fastest of seven feed-forward methods and $4.2\times$ faster than the previous state of the art, trains $2.7\times$ faster ($5.9\times$ at 24 views), and uses $6.7\times$ less inference memory.

---


### 108. [SelectOccFlow: Selective Spatiotemporal Aggregation for 3D Occupancy and Scene Flow Prediction](https://arxiv.org/abs/2610.04356)

**<font color=#1a73e8>作者：</font>** Yuhang Wang, Kai Luo, Yuanfan Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Comprehensive 3D scene understanding for autonomous driving requires modeling geometry, semantics, and motion. However, camera-based occupancy and scene flow prediction are sensitive to unreliable spatial and temporal aggregation, caused by semantically incompatible image features, misaligned historical observations, and incomplete voxel structures. To address this issue, we propose SelectOccFlow, a selective spatiotemporal aggregation framework that progressively refines contextual evidence across image, temporal, and voxel domains. To obtain semantically compatible image evidence, we design Semantic-Guided Sampling (SGS) to regulate feature sampling with semantic priors. Since reliable image evidence alone cannot resolve temporal inconsistency, we then present State-Conditioned Temporal Aggregation (SCTA) to selectively retrieve historical evidence according to voxel states. To further enhance the structural completeness of voxel representations, we introduce Extent-Aware Spatial Aggregation (ESA), which exploits directional structural support to refine foreground geometry. Experiments on OpenOcc demonstrate that SelectOccFlow achieves a state-of-the-art OccScore of 44.9, improving the previous best by +4.2%. It also maintains competitive occupancy performance on Occ3D-nus and improves the mean OccScore under nuScenes-C corruptions by +11.1%, demonstrating improved robustness to visual corruptions. The source code will be made publicly available at this https URL.

---


### 109. [Checkable NTK Positivity and Finite-Width Gradient Descent for Scalar- and Vector-Valued PINNs with Strong-Form, Weak-Form, and Nonlocal Linear Constraints](https://arxiv.org/abs/2610.04357)

**<font color=#1a73e8>作者：</font>** Zifan Lyu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We give checkable positive-definiteness criteria for the limiting neural tangent kernel (NTK) and high-probability finite-width gradient-descent guarantees for scalar- or vector-valued physics-informed neural networks (PINNs) with linear constraints. The constraints may be strong-form differential rows of any fixed finite order, including coupled systems, with any linear initial or boundary conditions; weak-form residual and boundary functionals; or finite-measure nonlocal observations such as integral, nonlocal-diffusion, and Dirac-data rows, all in any dimension. For each class, positive definiteness of the limiting NTK is equivalent to a rank condition on a finite coefficient, functional, or moment matrix of the fixed design: a certificate computed before training that detects structural zero modes. The model hypotheses are those of an ordinary two-layer PINN, a smooth nonpolynomial activation with bounded symmetric initialization, and are met by standard choices such as $\tanh$ with uniform initialization. Given a certificate, explicit width and step-size conditions ensure, with high probability, that the empirical NTK retains at least half the limiting gap and that full-batch gradient descent decreases the training loss geometrically at every iteration. Controlled experiments check the certificates and the finite-width mechanism.

---


### 110. [TRIM-ReID: Duplication-Aware Token Reduction and Modality-Aligned Interaction for Multi-Modal Object Re-Identification](https://arxiv.org/abs/2610.04361)

**<font color=#1a73e8>作者：</font>** Wanke Xia, Ruiding Zhu, Xingguo Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal object re-identification exploits complementary RGB, near-infrared (NIR), and thermal-infrared (TIR) observations to retrieve target objects. However, existing methods commonly employ visual encoders optimized for global image-text alignment and select tokens using learned importance scores. Such designs fail to preserve fine-grained identity cues or explicitly account for token redundancy, resulting in underrepresented local evidence and duplicated tokens that lead to noisy and costly cross-modal interaction. To address this gap, we propose TRIM-ReID, a compact framework that unifies dense feature extraction, intra-modal token reduction, and inter-modal aligned interaction. Specifically, semantically rich and spatially coherent patch features are extracted by Dense Identity Representation (DIR), which leverages DINOv3 to preserve fine-grained identity information. We then introduce Token Diversity Mining (TDM) to identify complementary local evidence and construct compact modality-specific token sets by suppressing repetitive patches while preserving informative diversity. Retained tokens are subsequently fused by Modal Relational Interaction (MRI) to enable effective information exchange across modalities, while a triangular alignment loss explicitly regularizes their joint relationships to maintain cross-modal semantic consistency under independent token selection. Extensive experiments on RGBNT201, RGBNT100, and MSVR310 demonstrate that TRIM-ReID achieves state-of-the-art performance.

---


### 111. [A multi-stage probabilistic framework to estimate gas-fired generator performance during extreme winter weather](https://arxiv.org/abs/2610.04368)

**<font color=#1a73e8>作者：</font>** Sajjad Uddin Mahmud, Anamika Dubey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extreme winter weather has repeatedly disrupted gas-fired power generation in the United States, yet the plant-level data needed to systematically quantify outage risk remain proprietary. Using publicly available weather and electricity demand data together with anonymized generator contingency records from the North American Electric Reliability Corporation (NERC), we develop a three-stage Bayesian probabilistic framework for estimating winter-driven generator performance. Applied to New York State (2013--2022), the framework sequentially estimates: the hourly probability of a generator contingency event, the expected net available capacity conditioned on an event occurring, and the event duration. Colder conditions and higher electricity demand are associated with higher failure probability, lower retained capacity, and longer event duration. Under the most severe observed stress conditions, estimated mean hourly event probability reaches 24\% , while expected mean net available capacity falls to 13\% of nameplate rating. Full outage events have a median duration of 12.7 hours, while partial derating event duration increases from 2.4 to 7.1 hours with capacity loss severity. The proposed framework establishes a transferable baseline that utilities with access to plant-level records can directly extend to obtain more precise reliability estimates for operational planning and resource adequacy assessment.

---


### 112. [JASPER: Special Session on Joint Reliability And Security Assessment of SPlit Computing for Edge Robustness](https://arxiv.org/abs/2610.04396)

**<font color=#1a73e8>作者：</font>** Enrico Magliano, Giuseppe Esposito, Amir Hossein Shahdadian 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Split Computing (SC) enables efficient deployment of Deep Neural Networks (DNNs) by partitioning inference between edge devices and cloud servers. However, intermediate feature representations are simultaneously exposed to hardware faults and adversarial attacks, which are traditionally evaluated independently. This paper presents a unified framework for the joint assessment of reliability and security in Split Computing. First, reliability is characterized through neuron-level fault injection using the Mean Relative Accuracy Degradation (MRAD) while security through feature-map-aware adversarial attacks simulations using the Attack Success Rate (ASR). Based on these complementary analyses, the Joint Vulnerability Score (JVS) is introduced, along with a confidence-aware extension that jointly captures prediction errors and confidence degradation. The framework is evaluated on ten Split Computing configurations based on ResNet-50 trained on ILSVRC-2012. Experimental results show substantial differences across compression strategies, with MRAD ranging from 44.3% to 61.2% under fault injection, while adversarial attacks achieve up to 98.8% ASR. Furthermore, the proposed joint metrics reveal vulnerability trends that remain hidden when reliability and security are analyzed independently, providing a more comprehensive methodology for designing dependable Split Computing systems.

---


### 113. [XTurnix: Large-Scale Self-Supervised Turn Control through Two-State Binary Decisions](https://arxiv.org/abs/2610.04400)

**<font color=#1a73e8>作者：</font>** Zhanxun Liu, Yifan Duan, Hengtao Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> General turn-taking behavior in real-time dialogue systems requires deciding whether to keep listening or start responding while listening, and whether to continue or stop while speaking. Existing turn detectors use heterogeneous, task-specific label spaces and are often trained on limited annotations or evaluated on isolated utterances, making them difficult to use as a unified causal controller with comprehensive context. We propose XTurnix, a compact text-based model that formulates turn control as two binary decisions conditioned on the AI's current listening or speaking state and predicts a single control token from the complete dialogue history. XTurnix is pretrained on 5.5 million causal action examples automatically derived from timestamped two-speaker transcripts, then fine-tuned on synthetic multi-turn examples with a flatter distribution across the four state-action labels. We evaluate XTurnix on four public benchmarks and a balanced self-curated benchmark. Across the public benchmarks, XTurnix achieves the best results on all SemanticVAD and LiveKit splits, ties the native Smart-Turn model on Smart-Turn Bench, and achieves the highest incomplete-turn accuracy on Easy-Turn. On the self-curated benchmark, it reaches 89.06% accuracy, more than 20 percentage points above the strongest third-party baseline at 68.75%, while maintaining F1 scores between 84.21% and 90.63% across all four categories. These results demonstrate unified listening- and speaking-state turn control in a single compact model. Code is available at this https URL, with an interactive demo at this https URL.

---


### 114. [CEENs: Causality-enforced evolutional networks for solving time-dependent partial differential equations](https://arxiv.org/abs/2610.04405)

**<font color=#1a73e8>作者：</font>** Jeahan Jung, Heechang Kim, Hyomin Shin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the growing popularity of physics-informed neural networks (PINNs), their applicability in the long-time integration of partial differential equations (PDEs) remains constrained. We argue that this problem stems from the lack of consideration of temporal causality in the original PINN formulation, resulting in a bias towards satisfying governing equations at later times before learning the initial condition and hence leading to erroneous solutions. To this end, we propose a novel method that seamlessly integrates temporal causality into the training process. Drawing inspiration from classical numerical methods where the temporal causality is reflected, we divide the time domain into nonoverlapping subintervals, assign a unique neural network to each subinterval, and construct a loss function founded on the integral form of PDEs within these subintervals. The proposed networks undergo sequential training, beginning with the initial time step. Our method demonstrates significant improvement in accuracy for long-time simulations of various PDE problems where the original PINN method fails while it requires less computational cost and memory compared to the PINN method. A parallelization algorithm is provided to further enhance the computational efficiency, showing a significant speedup for solving time-dependent PDEs.

---


### 115. [Specific Algorithmic Interpretability of Neural Networks: A Case Study on Textures](https://arxiv.org/abs/2610.04413)

**<font color=#1a73e8>作者：</font>** Yanglin Zhang, Anneke von Seeger, Gilad Lerman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We develop a principled framework for constructing neural networks whose specific parameter realizations admit an explicit algorithmic interpretation. Existing algorithm-inspired architectures can explain the computational structure of a network, yet after standard training the learned parameters need not retain a clear relation to the motivating algorithm. We address this gap as follows. First, we model each data point as a sample of a class-dependent stochastic process and assume that statistics of this process can be estimated from a single sample and these statistics are sufficient to distinguish the classes. We then construct a neural network whose initial parameters exactly implement an algorithm for estimating these statistics, making the network fully interpretable. To account for mismatch between the idealized model and real data, we fine-tune this network while controlling its deviation from the algorithmic initialization. The trained network hence roughly retains the interpretation of the initial network. A PAC-Bayesian analysis yields a uniform generalization bound whose complexity term scales with the fine-tuning radius, providing a statistical motivation for our approach. We instantiate the framework for texture classification using the scattering transform to estimate the discriminative statistics.

---


### 116. [CORE-RL: Confidence-Oriented Reliability Evaluation of Black-Box Reinforcement Learning Policies](https://arxiv.org/abs/2610.04418)

**<font color=#1a73e8>作者：</font>** Santhosh GS, Ananya Ravi, Devika Jay 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The deployment of Reinforcement Learning (RL) agents in critical domains must be preceded with a pipeline to evaluate the alignment of the RL agent with complex multi-objective specifications and robustness under real-world environmental drift. However, to protect intellectual property, the RL agent may be delivered for evaluation as opaque executable or remote API, which makes traditional evaluation techniques based on the internals of the policies infeasible. To address this gap, CORE-RL: Confidence-Oriented Reliability Evaluation of black box RL policy is proposed in this paper. The CORE-RL pipeline introduces a Unified Reliability Metric that formally integrates early task termination and safety constraint violations, preventing unsafe policies from masking failures through premature episode halts. By subjecting the policy to a noise certification envelope of perceptual noise, actuation noise and change in environment dynamics, the pipeline computes the finite-sample Clopper-Pearson bounds on unified reliability metric and Hoeffdings' lower bound on reward and safety cost. The pipeline then defines safe operational design domain to report high-confidence certificates for safety and expected performance. Experiments on continuous control tasks demonstrate the CORE-RL pipeline's ability to automatically reject non-compliant policies and map the safe Operational Design Domain (ODD) of safety-aware policies. Thus CORE-RL provides an evaluation framework towards a quantitative, transparent and reproducible, statistical rationale necessary to safely evaluate, compare, and deploy black box RL solutions.

---


### 117. [MaDeL: Manifold-Decomposed Feature Losses for Generative Modeling](https://arxiv.org/abs/2610.04419)

**<font color=#1a73e8>作者：</font>** Beomsu Kim, Jong Chul Ye, Kwanyoung Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models are often trained with isotropic objectives such as mean-squared error. For data concentrated near a low-dimensional manifold, however, such losses conflate displacement along the manifold, which may represent valid variation, with displacement away from it, which produces invalid samples. This mismatch is especially problematic in sparse, highly constrained domains, where ambient-space regression can encourage off-manifold interpolation. We ask whether a generative objective can distinguish manifold-parallel variation from manifold-orthogonal deviation directly from data, without explicitly estimating the manifold. We introduce a manifold-decomposed feature loss (MaDeL) that learns complementary representations from corrupted observations: one is trained to recover the clean sample, while the other is trained to recover the corruption. We show that, under a feature bottleneck, their Jacobians align with the tangent and normal spaces, exactly for linear manifolds and locally for smooth manifolds. Together, these representations define an anisotropic objective that separately measures intrinsic variation and off-manifold deviation. Across synthetic, Earth and climate science, and torsion-angle benchmarks, MaDeL improves support recovery and average angular $W_1$ under single-step sampling; on protein backbones, it reduces steric clashes across one- and few-step sampling budgets.

---


### 118. [Measuring Effective Data Resolution in Guided Diffusion Posteriors](https://arxiv.org/abs/2610.04422)

**<font color=#1a73e8>作者：</font>** Ridham Patel, Defu Cao, Jiacheng Pang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Guided diffusion samplers are increasingly used to reconstruct physical fields from sparse observations, but standard diagnostics do not say how much of the reconstruction was actually determined by the data. We introduce effective data resolution for black-box generative posteriors: a comparison between the resolution warranted by the inverse problem, $\mathrm{dof}_{\mathrm{ref}}$, and the resolution realised by the sampler, $\mathrm{dof}_{\mathrm{samp}}$. A perturbation estimator measures $\mathrm{dof}_{\mathrm{samp}}$ and the spatial map $R(x,x)$ from sampler queries alone. We validate the estimator against exact references and use it to study guided diffusion. The resulting measurements show that guidance weight can strongly alter apparent information transfer, that mean, spread and resolution are not jointly corrected by one weight even with an exact prior and score, and that resolution fidelity does not follow reliably from the apparent principledness of a guidance rule.

---


### 119. [On the Trade-off Between Information Loss and Generalization in Sparse Attention](https://arxiv.org/abs/2610.04424)

**<font color=#1a73e8>作者：</font>** Zhongqi Fan, Zheng Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To mitigate the quadratic complexity bottleneck of the Transformer, sparse attention has emerged as a pivotal technology. Despite the extensive empirical success of sparse Transformers, the theoretical understanding of sparse attention remains fragmented. In particular, two fundamental questions remain unclear: (1) How does sparsification affect the information fidelity of attention mechanisms? (2) How does this information loss interact with the generalization behavior of the model? To bridge this gap, this paper proposes a systematic analysis of the Jensen-Shannon (JS) divergence and of the generalization gap of sparse attention mechanisms. Specifically, we first characterize the approximation error via the JS divergence. Through an order-statistics-based concentration analysis of the truncation mass alpha --- where the attention scores are assumed to be independent and identically distributed sub-Gaussian random variables with parameter sigma --- the JS divergence between the full attention distribution and the sparse attention distribution is shown to admit the closed form log 2 + ((1 - alpha)/2) log(1 - alpha) - ((2 - alpha)/2) log(2 - alpha). Subsequently, we derive a generalization bound through Rademacher complexity, quantified by O(gamma * sqrt(M/n) * (sqrt(log(3eL/M)) + sqrt(pi)/2)). Furthermore, building on a mutual-information-based generalization bound together with an entropy and covering-number analysis of the sparse hypothesis class, we obtain the sparsity-dependent generalization bound O(sqrt((M/(2n)) * (log(eL/M) + log(1 + 2/epsilon)))). Our analysis shows that sparsity reduces the complexity of the considered hypothesis class while introducing approximation error that can be quantified by the JS divergence. These findings provide a theoretical characterization of the trade-off between information fidelity and generalization in sparse Transformer architectures.

---


### 120. [UnAct: Gradient-Free Unlearning via Targeted Activation Intervention](https://arxiv.org/abs/2610.04426)

**<font color=#1a73e8>作者：</font>** Saeed Abdul Muizz, Aayat Rafiq, Iqra Altaf Gillani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning seeks to remove the influence of designated training data from a trained model without retraining from scratch. Retrain-free methods such as Selective Synaptic Dampening (SSD) and its label-free variant LFSSD avoid full retraining but still require backpropagation and parameter importance computed over the entire dataset. We ask: what happens when a deletion request arrives with only a few images of the class to be forgotten? To answer this question, we introduce UnAct, a gradient-free class-unlearning method that needs only forward passes over the forget images. UnAct scores late-layer units by their responses, attenuates the most responsive connections, and repeats this for up to 20 rounds using no gradients, no labels, and no retained data. On ResNet-18 trained with CIFAR-10, CIFAR-20, and CIFAR-100, UnAct is competitive with SSD and LFSSD when forgetting entire classes and, unlike them, never collapses the network when forget data is scarce. On ResNet-18, across all tested sizes, UnAct's retain accuracy stays within 2.5 points of retraining, while SSD and LFSSD, at their full-class operating points, lose up to 86 points on some classes. With five forget images on CIFAR-10, UnAct's distance to retraining is 0.21 points, against 67 for LFSSD and 90 for SSD, and re-selecting SSD's threshold at each size with an oracle does not close the gap. In preliminary transfer to ViT-B/16, UnAct's distance to retraining is 11.5 against 33.7 for SSD, and a request is 19x faster than SSD when SSD computes its importance at request time. The code is available at this https URL

---


### 121. [Guess My Weight: Profiled Side-Channel Recovery of Floating-Point Neural-Network Weights](https://arxiv.org/abs/2610.04436)

**<font color=#1a73e8>作者：</font>** Timon Lumír Fillo, Ján Mikulec, Anubhab Baksi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Neural-network parameters deployed on embedded devices may be exposed through physical side-channel leakage during inference. Existing side-channel attacks on floating-point neural-network parameters have often targeted reduced numerical precision, while recovering the complete IEEE-754 representation remains considerably more challenging because of the large and structured 32-bit candidate space. We present a profiled template attack for bit-exact recovery of an IEEE-754 single-precision neural-network weight from power measurements. The attack targets the floating-point multiplication between a known input and a first-layer weight. During profiling, multivariate Gaussian templates are learned from randomized network configurations using Hamming-weight classes of the multiplication result, while the remaining network parameters act as nuisance variables. To efficiently search the structured 32-bit floating-point candidate space, we use a hierarchical coarse-to-fine-to-exact procedure that progressively increases both the numerical and leakage-model resolution. Experiments on a ChipWhisperer-Lite with an Arm Cortex-M4 demonstrate recovery of the exact float32 representation of the target weight. In the evaluated setting, the attack reaches a bit-exact success rate of 99% with 171 traces and 100% from 263 traces onward. These results demonstrate that profiling can enable practical full-precision extraction of floating-point neural-network parameters from physical leakage.

---


### 122. [CRAFT: An Agentic Spreadsheet Form Filling System with Template Awareness](https://arxiv.org/abs/2610.04437)

**<font color=#1a73e8>作者：</font>** Leyao Gu, Yingjie Xiong, Zirui Tang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spreadsheet form filling requires agents to consolidate external evidence, ground values to precise cells, and preserve irregular template structure. Errors in early edits can overwrite labels or misalign fields, undermining later decisions. We propose CRAFT, a template-aware agent framework that connects reflective validation to constrained local repair. Instead of treating reflection as a free-form request to regenerate the workbook, CRAFT grounds detected errors to spreadsheet regions, restores corrupted template state when necessary, and re-grounds plausible writable slots before subsequent edits. A Rectangle-Aware Slot Grounder (RASG) proposes writable cells, while label-slot hints and protected regions constrain subsequent edits. We introduce FormFillBench, with 327 forms across Instruction-Only and Multi-File tracks. Compared with the strongest baselines, CRAFT improves pair accuracy by 8.51 and 23.38 percentage points on these tracks, respectively. Component-removal experiments support structural adjudication and slot re-grounding within the pipeline, and the framework retains its relative advantage among the methods evaluated with a second backbone. The code and benchmark FormFillBench are available at this https URL.

---


### 123. [RAGrasp: Geometry-Semantic Template Retrieval and Grasp Transfer](https://arxiv.org/abs/2610.04438)

**<font color=#1a73e8>作者：</font>** Shenzhe Zhu, Chengxiao He, Jan Harder  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present RAGrasp, a retrieval-augmented pipeline for planar parallel-jaw grasping from a compact set of locally collected, grasp-annotated RGB-D (color and depth) templates. Unlike task-specific predictors trained primarily on large public or synthetic grasp datasets, RAGrasp requires no end-to-end retraining for a new this http URL template memory is constructed from observations collected with the deployment camera, robot, and gripper in the target workspace, thereby aligning stored examples with the local sensing and embodiment conditions. The system uses self-supervised DINOv2 visual fea- tures together with appearance and depth cues to prompt the Segment Anything Model 2 (SAM2), which isolates the query object. A two-stage geometry-semantic retrieval cascade then selects a template, and a confidence gate chooses one of two grasp- transfer estimators. The transferred grasp is refined using mask- support and silhouette-contact constraints before calibrated 2D- to-3D conversion. In real-world trials, RAGrasp achieves 20/20 successful grasps on seen objects and 19/20 on unseen objects. Within the evaluated setting, the results demonstrate deployment- specific grasp adaptation from limited local annotation and tolerance to the tested viewpoint and illumination changes.

---


### 124. [CHAMP: Cayley HAshing with Matrix Products](https://arxiv.org/abs/2610.04442)

**<font color=#1a73e8>作者：</font>** Alexander Demin, Alexey Ovchinnikov, Vladimir Shpilrain  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cayley hash functions hash binary strings by representing the bits of the message as elements of a semigroup and multiplying the corresponding elements. This gives Cayley hash functions useful homomorphic properties. Here, we propose CHAMP, a Cayley hash function based on products of 2 by 2 matrices over a finite field, and discuss its security, implementation, and performance.

---


### 125. [One-Step Generation via Riemannian Wasserstein Gradient Flows](https://arxiv.org/abs/2610.04454)

**<font color=#1a73e8>作者：</font>** David Li, Chanhyuk Lee, Jaehoon Yoo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, Drifting Models and Wasserstein Gradient Flows have attracted substantial attention because they move iterative distributional refinement to training and amortize it into a generator, enabling fast inference. However, existing formulations have been developed largely for continuous Euclidean domains, such as image spaces, where particles admit unconstrained additive updates. On constrained spaces, these updates can leave the valid domain or ignore its geometry, making them unsuitable targets for training. Recent work has adapted updates to these spaces, but has focused on particular fields or offered limited empirical comparison. We derive and compare several geometry-aware fields within a common training framework for one-step generators. We test the method on data with different structures and obtain competitive one-step results in each setting. The best-performing field varies by task, showing why the choice of objective matters in practice.

---


### 126. [Multi-Crop Leaf Disease Recognition: A Unified Benchmark and Cross-Region Study](https://arxiv.org/abs/2610.04456)

**<font color=#1a73e8>作者：</font>** Rosemary Nalwanga, Sebastian Bunda, Godliver Owomugisha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models for crop leaf disease recognition routinely report near-perfect accuracy yet are typically trained and evaluated on a single dataset collected under controlled laboratory conditions, leaving their behavior under realistic cross-region domain shift poorly understood. We introduce MLD (Multi-crop Leaf Disease) dataset, a unified multi-region benchmark that combines six public crop-disease datasets from the USA, Asia, and Africa into a shared hierarchical taxonomy spanning 18 crops, 56 crop-disease classes (including one healthy class per crop) making 167,427 images. We define standardized single-source and pooled multi-source evaluation protocols that explicitly probe cross-region generalization. We also investigate whether exploiting the inherent crop-to-disease dependency via a hierarchical formulation (HiLeaD) that conditions disease prediction on the predicted crop improves recognition under cross-region shift. Under the HiLeaD, the model trained on PlantVillage achieves 99.07% in-domain disease F1 but collapses to 12.88% when tested on PlantDoc, exposing a severe cross-region domain gap. The model trained on the pooled MLD dataset partly recovers cross-region disease F1 from 12.88% to 39.64% on PlantDoc (HiLeaD), achieving a 26.76 percentage point improvement. The hierarchical formulation provides a consistent additional gain, ranging from 1.71 to 4.88 percentage points in disease F1 over the flat baseline under the MLD dataset indicating that progress in this area is currently limited more by data coverage and diversity than by model design.

---


### 127. [RPFQ-ViT: Rotated Phase-Frame Quantization for Extremely Low-Bit Weights in Vision Transformers](https://arxiv.org/abs/2610.04457)

**<font color=#1a73e8>作者：</font>** Mengyuan Fan, Bokai Huang, JiaMing Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) achieve strong performance on image recognition and mobile vision applications, but their high-dimensional linear projections and attention computations still impose substantial storage and inference costs. Extremely low-bit quantization is a promising solution, yet ViTs often suffer severe accuracy degradation because conventional real-valued scalar codebooks are poorly matched to the directional geometry of Transformer projections. We present RPFQ-ViT, a Rotated Phase-Frame Quantization method that quantizes paired channels in two-dimensional phase planes, enabling low-bit codes to better preserve projection directions while recovering magnitude with lightweight scaling. RPFQ-ViT serves as a drop-in QAT replacement for this http URL and does not modify the standard real-valued attention, normalization, or activation computation graph. On ImageNet-1K, RPFQ-ViT-B/16 reaches 79.33% Top-1 / 94.48% Top-5 under W2/A4, Swin-T reaches 79.30% Top-1 / 94.79% Top-5 under W2/A8, and DeiT-S reaches 77.41% Top-1 / 93.11% Top-5 under W2/A8. Ablations, phase-geometry analysis, and direction-preservation metrics show that channel pairing, learnable rotation, phase-anchor learning, and residual phase refinement each improve quantization quality. We further deploy RPFQ-ViT image-classification models on native iOS and Android runtime stacks; with 2-bit packed weights, model size shrinks by roughly $5.4$-$7.1\times$ relative to FP32 and end-to-end on-device latency drops by $1.4$-$1.6\times$. All ImageNet results trained in our codebase use a matched 300-epoch recipe and are reported as mean accuracies over three independent runs. These results show that RPFQ-ViT provides a favorable trade-off among accuracy, compression, and practical mobile deployment for extremely low-bit ViTs.

---


### 128. [Semantic Causal-Factor Inference from Aviation Incident Narratives Using A Variational Autoencoder with Cosine-Similarity-Based Reconstruction](https://arxiv.org/abs/2610.04472)

**<font color=#1a73e8>作者：</font>** AZIIDA NANYONGA1, HASSAN WASSWA, UGUR TURHAN 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aviation accident and incident investigations generate extensive unstructured textual information containing evidence relevant to the causes and contributing factors of safety occurrences. Automatically extracting such information is challenging because causal evidence may be distributed across long and complex investigation narratives. This study proposes a semantic causal-factor inference framework combining natural language processing with a variational autoencoder (VAE) to learn the relationship between aviation investigation narratives and expert-reported probable causes. Investigation narratives and their corresponding probable causes are transformed into numerical representations, after which the encoder maps narrative representations to a probabilistic latent space. The decoder estimates representations of the corresponding probable causes and is trained using an objective that combines Kullback-Leibler divergence with cosine-similarity-based semantic reconstruction. The framework was evaluated using 20,919 finalized U.S. National Transportation Safety Board investigation reports from 2005 to 2020. On the held-out test set, the predicted and expert-reported probable-cause representations achieved a mean cosine similarity of 0.786 (SD = 0.120). The predicted representations also yielded interpretable terms associated with causal information in the reports. The results demonstrate the potential of probabilistic latent representation learning for AI-assisted extraction of causal information from aviation safety narratives while retaining expert investigation as the basis for formal causal determination.

---


### 129. [VCLMU: Mechanism-Centric Virtual Cell World Modeling for Perturbation Response](https://arxiv.org/abs/2610.04475)

**<font color=#1a73e8>作者：</font>** Yuwei Miao, Azim Dehghani Amirabad, Scott Oloff 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predicting cellular responses to genetic perturbations is a central capability for virtual cells and a key step toward computational modeling of biological interventions. Most existing models directly map an unperturbed molecular profile and perturba- tion to the resulting observation without explicitly representing the latent cellular transition induced by the intervention. We introduce a mechanism-centric virtual cell world model that represents cellular state as a set of Latent Mechanism Units (LMUs) and treats genetic perturbations as actions on these latent states. Each LMU combines a reusable identity grounded in multimodal biological evidence with an observation-specific state, allowing a perturbation to induce mechanism- specific stochastic transitions before decoding the resulting transcriptional response. We train VCLMU through two-stage pretraining, first on around 200K pseudo-bulk perturbation profiles and then on gene-aligned single-cell perturbation data. Across six perturbation-disjoint benchmarks, VCLMU consistently improves perturbation- specific response recovery over strong baselines while maintaining competitive global response accuracy. We further analyze learned LMUs through enrichment between perturbation responses and LMU gene sets and show that they capture structured biological response programs. These results support mechanism-level latent state transition as a useful formulation for virtual cell models that aim to predict and interpret cellular responses to biological interventions.

---


### 130. [Attestable Audit: Property-Based Attestation for Proprietary Workloads without Artifact Disclosure](https://arxiv.org/abs/2610.04480)

**<font color=#1a73e8>作者：</font>** Takuma Imamura  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Trusted Execution Environments (TEEs) prove the integrity of code and data to a remote peer through remote attestation: the TEE issues an attestation report by signing, with a hardware-bound key, its configuration information, including measurements (cryptographic digests) of the code loaded inside it. A verifier appraises the report by matching these measurements against reference values. When the measured artifact is proprietary, however, the verifier cannot derive the reference values itself: it can only confirm that something with a given measurement is running inside the TEE---not that the program behaves as expected---forcing full trust in the reference value provider. We propose an architecture that closes this gap without disclosing the artifact, composing two TEE workloads: attestable build (Hugenroth et al., 2025), which binds a source code digest to a build artifact measurement, and attestable audit (proposed in this paper), which binds the same source code digest to the verdicts of automated audits---fuzzing, static analysis, AI code auditing, formal methods---executed inside a TEE. Both are instances of Confidential Computing Proofs: TEE attestation viewed as a hardware-backed zero-knowledge proof. Chaining the two certificates lets the verifier conclude that the running artifact was built from source code satisfying the audited properties, without disclosing either the source code or the build artifact. A proof-of-concept implementation on Intel SGX with the Gramine Library OS, running the Bandit security analyzer on Python code, demonstrates the practicality of the approach.

---


### 131. [Understanding Clustering in Slot Attention via Particle Dynamics](https://arxiv.org/abs/2610.04493)

**<font color=#1a73e8>作者：</font>** Vasudev Joy, Rajat Rasal, Avinash Kori 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Studying attention through the lens of interacting particle dynamics has shown how token clustering can emerge from the underlying dynamics. We extend this perspective to slot attention, a method for object-centric image segmentation and representation learning in which learned components obscure how much of the clustering behaviour is intrinsic to the attention dynamics. We therefore introduce simplified slot attention (SSA), a parameter-free variant whose dynamics are connected to soft $k$-means clustering and which provides a straightforward mechanistic explanation for the emergence of object-centric representations. On the Pascal VOC dataset, SSA achieves performance comparable to that of slot attention, demonstrating that competitive object-centric segmentation can be achieved without learned neural-network components.

---


### 132. [Emoji-Emotion Ranking System Using Twitter Data](https://arxiv.org/abs/2610.04495)

**<font color=#1a73e8>作者：</font>** Danila Khlebokazov, Nurkhan Tashimov, Pakizar Shamoi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Nowadays, emojis are often replacing words. Yet computational systems still oversimplify them. Most existing approaches treat emojis as static sentiment indicators and overlook their emotional distributions. In this study, we propose an emoji-aware emotion analysis framework based on a Twitter (X) dataset of 100,000 emoji-containing replies collected between 2020-2025. After preprocessing and text cleaning, we applied text-to-emotion classification to detect five primary emotions (Happy, Angry, Sad, Fear, and Surprise) for each message. By aggregating emotion scores across contexts in which each emoji appears, we estimate emoji-emotion association distributions and construct an emoji-emotion ranking system reflecting relative emotional dominance. Furthermore, we project emojis into the Russell valence-arousal space to enable continuous affective interpretation. Our results demonstrate that emojis exhibit probabilistic, context-sensitive emotional profiles rather than fixed sentiment polarities.

---


### 133. [Homogeneous Semantic Alignment and Hierarchical Expert Routing for Radiology Report Generation](https://arxiv.org/abs/2610.04499)

**<font color=#1a73e8>作者：</font>** Erjian Zhang, Jiayuan Ma, Liejun Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiology report generation (RRG) aims to convert medical images into diagnostic texts to assist in clinical decision-making and alleviate the workload of physicians. Although existing methods have made extensive progress in cross-modal interaction and the incorporation of external priors, the distribution shift of underlying representations and the undifferentiated rigid coupling of heterogeneous information cause weak visual abnormality cues to be easily diluted by massive text priors and generation inertia during decoding. To overcome this bottleneck, inspired by cognitive science, we propose a novel two-stage Homogeneous Semantic Alignment and Hierarchical Expert Routing (HSA-HER) framework. First, the model introduces an explicit homogeneous distribution constraint in the underlying latent space to effectively eliminate the cross-modal distribution shift between visual and textual features, thereby extracting purified visual features as semantic anchors that accurately align with diseases. Second, for heterogeneous clinical evidence composed of visual features, local entities, and global retrievals, we design a hierarchical expert routing mechanism guided by these disease semantic anchors. This mechanism abandons the undifferentiated rigid coupling paradigm. Specifically, it dynamically activates expert networks to perform targeted mining and semantic reconstruction on multi-source evidence, and adaptively allocates fusion weights. Extensive experiments on three mainstream benchmark datasets demonstrate that HSA-HER achieves state-of-the-art performance, accurately depicting complex imaging details and key diagnostic information.

---


### 134. [ManifoldCache: Training-Free Diffusion Acceleration via Constraint Manifold Caching](https://arxiv.org/abs/2610.04510)

**<font color=#1a73e8>作者：</font>** Prashant Pandey, Devineni Sri Venkatraya Chowdary, Brejesh Lall  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion models for structured scientific generation must produce samples satisfying hard geometric constraints imposed by physics, chemistry, or biology, yet inference in these settings is prohibitively slow, demanding hundreds to thousands of neural-function evaluations per sample. We unify eight state-of-the-art models spanning medical volumetrics, molecular conformations, protein backbone design, crystal structure prediction, and multi-view 3D scenes under a single abstraction, Constraint-Manifold Diffusion Models (CMDMs), in which the target distribution is supported on a manifold defined by an externally specified constraint map. All existing acceleration families fail on this class: quantization exhausts memory on high-dimensional volumetric operators; pruning breaks constraint fidelity; fast ODE solvers allow trajectories to drift off the constraint manifold; and feature-caching heuristics are blind to constraint geometry, inducing mode confusion in the high-noise regime. We introduce ManifoldCache, the first training-free, data-free accelerator designed from first principles for CMDMs. The key insight is that the conditional score decomposes orthogonally into a normal component, which enforces constraint satisfaction, and a tangential component, which navigates within the manifold. Exploiting this structure, we prove that the noise-schedule midpoint is a sharp safe-caching boundary: caching before it incurs provably bounded error, while caching after it guarantees a strictly positive fraction of trajectories suffer mode confusion, a gap that persists up to the boundary. We further prove that deeper network blocks admit provably larger certified cache strides within the safe phase, as a consequence of the score decomposition propagating through block Jacobians. The resulting schedule requires no calibration data, along with zero training overhead.

---


### 135. [Towards Credible Agent-Based Policy Simulations: Disentangling Opportunities and Preferences in a Financial Inclusion Case Study of Egypt](https://arxiv.org/abs/2610.04515)

**<font color=#1a73e8>作者：</font>** Alba Aguilera, Georgina Curto, Nardine Osman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Credibility is a central topic for agent-based models intended to support policy-making. Simulations must not only represent the target scenarios and their core dynamics but also demonstrate that their assumptions, parameters, and outputs are empirically grounded and sufficiently accurate for their intended use. This paper addresses this challenge by presenting a general modelling framework, aligned with the Capability Approach, for building credible policy simulations that rely on data and domain-expert knowledge. It then demonstrates how it can be contextualised and implemented to study the social challenge of financial inclusion in Egypt, building on an agent-based model that represents heterogeneous individuals and firms behaving according to their financial states, barriers, opportunities, and preferences. The model is fitted to real-world data in two stages, initialisation and calibration, which respectively build representative synthetic populations and estimate behavioural parameters. By fixing the feasibility parameters, which determine agents' opportunities, and calibrating preference parameters across different population groups, we are able to distinguish and analyse the role of institutional and social barriers in the system, as well as the role of agents' motivations and priorities. This calibration stage provides transparent and group-specific hypotheses about the drivers of observed financial-inclusion gaps, which can further be analysed as gaps between agents' opportunities and realised outcomes, a very relevant insight for policy-making. This paper is thus a step towards improving the credibility and usefulness of policy simulations, strengthening the relationship between the model, the real target system, and the stakeholders who will use it. The code is available at: \url{this https URL}.

---


### 136. [Length Generalization Needs Proper Regularization](https://arxiv.org/abs/2610.04518)

**<font color=#1a73e8>作者：</font>** Pavlo Vasylenko, Matthias Lindemann, André F. T. Martins 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Length generalization is the ability of sequential models to perform well on context lengths unseen during training. In this work, we show that the challenge of achieving length generalization is related not only to architectural choices such as positional encoding and the attention mechanism but also to the training procedure itself. We study how regularization affects length generalization and find that weight decay can hinder extrapolation. In contrast, dropout improves extrapolation when its placement within the architecture is reconsidered. In that regard, we show that the standard placement of dropout before layer normalization introduces a systematic distributional mismatch, and that applying dropout just before the linear projection resolves this issue. For example, a modified SmolLM3 with sliding window attention, continually pre-trained with dropout, can extrapolate perfectly to 64$\times$ on Needle-in-a-Haystack and far beyond the pre-training context size on RULER and HELMET. Mamba2 also benefits from dropout, suggesting an architecture-agnostic nature of the problem. We further propose Variance-Preserving Affine Dropout (VPAD), a new dropout strategy that substantially reduces the resulting pre-activation variance mismatch, leading to further extrapolation improvements in transformers.

---


### 137. [Proximal Causal Learning under Unmeasured Confounding](https://arxiv.org/abs/2610.04519)

**<font color=#1a73e8>作者：</font>** Ying Tang, Yi Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating treatment effects from observational data typically relies on the No Unmeasured Confounding Assumption (NUCA), which rarely holds in practice. Proximal causal learning (PCL) addresses unmeasured confounding via proxy variables, yet existing methods require the proxy variables to be pre-specified. Thus, we propose PCL-U, a framework that learns proxy variables directly from observed covariates. PCL-U uses neural encoders to decompose covariates into treatment-inducing, outcome-inducing, and shared proxies, guided by minimax mutual information objectives, and obtains causal estimates through a practical moment-based risk function. Experiments on benchmarks show that PCL-U matches or outperforms existing baselines. Besides, there are two types of synthetic datasets with varying dimensions and confounding strengths that illustrate that our method maintains stable estimation accuracy.

---


### 138. [TAME:Topology-Aware Text-Driven Motion Editing across Heterogeneous Humanoid Skeletons](https://arxiv.org/abs/2610.04529)

**<font color=#1a73e8>作者：</font>** Qichen Zheng, Siyuan Yang, Chong Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-driven motion editing modifies an existing motion sequence according to a text instruction while preserving the content of the source motion. Existing methods are typically built for a single, fixed skeletal topology, which limits their use in animation pipelines where characters differ in joint count and skeletal hierarchy. We present Topology-Aware Motion Editor (TAME), a flow-matching transformer that edits motions on humanoid skeletons of varying topology. TAME represents motion as per-joint, per-frame tokens and models interactions among joints, across frames, and with the text instruction through skeletal, temporal, and text cross-attention layers. To make the skeletal attention follow each character's hierarchy, TAME replaces full joint attention with Topology-Constrained Skeletal Propagation (TCSP), which restricts attention to one-hop kinematic neighbors in the skeleton's adjacency matrix. We further introduce Edit-Focused Representation Alignment (EFRA), a self-distilled representation alignment strategy that aligns student features with cleaner EMA-teacher features exclusively on edit-relevant joint-time tokens, making edits faithful to the instruction. To make this setting trainable and comparable, we construct TopoMotionFix, a multi-topology extension of MotionFix with seen- and unseen-topology evaluation protocols. TAME outperforms previous methods in edit alignment and source preservation on MotionFix and reliably edits motions on unseen skeletons in TopoMotionFix.

---


### 139. [Weight Decay and Neuron Condensation: A Three-Stage Analysis of Two-Layer ReLU Networks](https://arxiv.org/abs/2610.04533)

**<font color=#1a73e8>作者：</font>** Cheng Xu, Pengxiao Lin, Zhangchen Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight decay is widely used as a regularization technique in neural network training, yet its role in neuron condensation (parameter direction alignment) remains unclear. Starting from a parameter initialization in the neural tangent kernel regime, we characterize training dynamics under weight decay through three stages: rapid fitting, amplitude compression, and neuron condensation. Using a two-layer ReLU network, we analyze a residual correlation field that governs both neuron amplitudes and directions. During rapid fitting, the residual approaches a quasi-static equilibrium maintained by weight decay while the tangent kernel remains nearly unchanged. In the early stage of amplitude compression, kernel decay amplifies the residual correlation field, whose isolated attracting extrema provide candidates for condensation directions. As neuron amplitudes stabilize, we bound the drift of attracting extrema and demonstrate contraction of neuron directions around them, leading to neuron condensation. This staged analysis provides a dynamical understanding of how weight decay promotes a condensed representation, beyond reducing parameter norms.

---


### 140. [FASTER: Fast Adjoint Stochastic Transport for Endpoint Refinement in Reward-Guided Image Editing](https://arxiv.org/abs/2610.04538)

**<font color=#1a73e8>作者：</font>** Yimiao Zhou, Zejia Zhong, Jingya Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reward-guided image editing at test time seeks to improve a specified reward while preserving source content and visual plausibility. Many existing approaches optimize candidates through pretrained generation processes, making repeated adjustment depend on costly large-model execution and, in some cases, backbone backpropagation. We develop a theoretical framework that jointly accounts for reward, source preservation, and pretrained-prior preferences, allowing the desired output distribution to be specified separately from the dynamics used to realize it. Based on this framework, we introduce FASTER, which trains a small network for each source and objective to perform inexpensive editing, while pretrained and reward models provide feedback on candidate outputs. By reusing each candidate and its feedback across multiple small-network updates, FASTER reduces repeated sampling and supervision queries without placing the pretrained generative backbone inside the inner optimization loop. On SD3, FASTER leads all four target metrics and several validation metrics among the evaluated methods. Compared with the evaluated baseline that optimizes controls along pretrained generation trajectories, FASTER achieves editing-time speedups of up to \({6.91\times}\) on Stable Diffusion 3 and \({24.14\times}\) on Stable Diffusion 1.5.

---


### 141. [Action-Consequence Alignment for Reliable Planning and Self-Improving in Latent World Models](https://arxiv.org/abs/2610.04539)

**<font color=#1a73e8>作者：</font>** Jinping Wang1, Zhiqiang Gao, Xiantong Zhen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent world models learn to predict observed transitions, yet low prediction error alone does not guarantee reliable planning. Inspired by self tickling experiments in neuroscience showing that disrupting motor sensory correspondence increases prediction mismatch, we examine whether learned world models preserve an analogous action consequence this http URL results show nearby alternatives can receive lower prediction errors despite producing physical outcomes farther from the recorded target. With that future treated as a goal, this reveals a concrete prediction planning mismatch: the model assigns a lower cost to an action that achieves the target less accurately. To mitigate this gap, we introduce Action Consequence Alignment (ACA), a training objective that complements forward prediction by penalizing the prediction error advantage of locally searched alternatives over factual actions without additional model components or environment interactions during training. The same principle can also guide additional data collection for self improvement. We demonstrate that across diverse environments and evaluation settings, ACA improves planning performance and reduces real goal error, while ACA guided data collection outperforms random local sampling. These results support action consequence alignment as a practical principle for bridging predictive learning and reliable planning.

---


### 142. [Quantum Machine Learning Protection of Military Quantum Key Distribution Against Cryptographically Camouflaged Attacks](https://arxiv.org/abs/2610.04543)

**<font color=#1a73e8>作者：</font>** Muhammad Shaheer Bin Junaid  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Quantum key distribution proves its protocol secure and says nothing about the hardware beneath it, so military and government operators fielding it for command-and-control keys monitor the channel for implementation attacks, and that monitoring has a blind spot. An adversary with a kleptographic foothold in the generator of a public per-block value \(x=g^v \pmod p\) can hide attacked blocks in honest noise, gating them on a predicate of its discrete logarithm, making detection a discrete logarithm problem that defeats every efficient classical monitor yet yields to a quantum kernel recovering \(v\) through Shor's algorithm. I formalise these cryptographically camouflaged attacks, reduce their hardness to an established learning separation, prove a single-frequency fidelity kernel cannot represent an interval predicate, and test them on Ghillie, a decoy-state BB84 simulator with a positive key rate to 142 km. From 10- to 14-bit groups over two seeds, a classical monitor reads 0.458 to 0.516 on camouflaged attacks while the quantum kernel reads 1.000, and both catch overt attacks above 0.99. Finite-precision recovery under depolarising noise and a hardened predicate lower the quantum result to 0.916 through 0.983 with the classical monitor at chance, and a feasibility probe on IBM Heron processors tracks the exact kernel within 0.034. A defender can therefore discard precisely the compromised key material, although the advantage is asymptotic, awaits fault tolerance, and holds only when the feature map matches the adversary's predicate, since a low-frequency map reads 0.545 on a residue pattern and 0.982 once aligned.

---


### 143. [Nonlinear Density-Driven Optimal Control (D2OC) for Multi-Agent Spatial Coverage via Sequential Convex Programming](https://arxiv.org/abs/2610.04545)

**<font color=#1a73e8>作者：</font>** Julian Martinez, Kooktae Lee  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This paper presents a nonlinear extension of Density-Driven Optimal Control (D2OC) for multi-agent spatial coverage with prescribed density distributions. Rather than assigning individual target locations, D2OC drives the collective spatial distribution of agents toward a desired density through a Wasserstein-based objective. We extend this framework to multi-step finite-horizon control for discrete-time control-affine nonlinear systems using sequential convex programming. At each control update, the nonlinear dynamics are locally linearized over the prediction horizon, yielding a strictly convex quadratic program that preserves the Wasserstein barycentric structure while directly incorporating input constraints. We further characterize the effect of constrained control deviations and nonlinear Taylor remainders on the accuracy of the local linear prediction, establishing an explicit finite-horizon error bound and a two-step specialization for receding-horizon implementation. The resulting method retains the decentralized, distribution-driven nature of D2OC while providing a computationally efficient optimization procedure for nonlinear multi-agent systems. Simulations with unicycle and quadrotor teams show coverage performance comparable to nonlinear model predictive control, while substantially reducing computation time. These results demonstrate a tractable and theoretically characterized framework for density-driven spatial coverage under nonlinear dynamics.

---


### 144. [TMAML: Temporal Model-Agnostic Meta-Learning for Cold-Start Time Series Forecasting](https://arxiv.org/abs/2610.04547)

**<font color=#1a73e8>作者：</font>** Wannes Janssens, Matthias Bogaert, Dirk Van den Poel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cold-start forecasting, the task of forecasting a time series with little to no historical data, is a common challenge. Addressing it requires approaches that learn quickly from few datapoints and leverage information from related series, typically through static covariates, to generalize well to unseen series. While some global forecasting models can generate cold-start predictions by leveraging information shared across multiple series, they are not optimized for out-of-train-set generalization or adaptation from short histories. In this work, we formulate cold-start forecasting as a few-window learning problem and introduce Temporal Model-Agnostic Meta-Learning (TMAML), which tailors the model-agnostic meta-learning algorithm, originally developed for few-shot adaptation of neural networks, to deep time series forecasting. TMAML constructs meta-tasks as temporally consistent support-query windows and pairs them with a temporal meta-training and meta-testing procedure, yielding forecasting models that are explicitly optimized for cold-start forecasting. We instantiate TMAML on the Temporal Fusion Transformer (TFT) and present an initial empirical analysis of forecast accuracy and calibration across three cold-start scenarios: TMAML consistently outperforms or matches a standard ERM-trained TFT, yields better-calibrated forecasts than naive on two of the three scenarios, but does not consistently outperform naive on probabilistic forecast accuracy.

---


### 145. [EagleDepth: Efficient Fine-Grained Depth Estimation via Pixel Diffusion Decoder](https://arxiv.org/abs/2610.04554)

**<font color=#1a73e8>作者：</font>** Bowen Chai, Tianbao Zhang, Shuyu Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering detailed geometry from high-resolution images is critical for precise perception of the surroundings and objects. However, existing methods which use latent-space modeling and VAE reconstruction can compromise geometric details. Furthermore, decoding from latent codes introduces substantial inference overhead. To address those issues, we present EagleDepth, an efficient framework for high-resolution monocular depth estimation that combines the geometric priors of latent diffusion with fine-grained pixel-space generation. Our key idea is to retain depth-aware latent representations as guidance while generating the final depth map directly in pixel space. We train the latent and pixel components sequentially: first, we fine-tune a pretrained latent diffusion model using paired RGB--depth supervision; then, we adapt a pretrained pixel diffusion decoder, PiD, to predict depth conditioned on the learned features. Training of the pixel component starts at 1024 resolution and continues across multiple resolutions up to 4K. The latent branch processes resized, lower-resolution RGB images, while the pixel branch generates depth at the target resolution, bypassing the original VAE decoder. This design preserves learned geometric knowledge without requiring the latent backbone to operate at the output resolution. On five commonly used depth estimation datasets and the high-resolution Synth4K dataset, our framework achieves state-of-the-art depth estimation performance, with faster inference and better preservation of fine structures and object boundaries.

---


### 146. [Only Project Once: Projection-Adaptive Loss for Exact Constraint Satisfaction](https://arxiv.org/abs/2610.04572)

**<font color=#1a73e8>作者：</font>** Tim Aebersold, Soheyl Massoudi, Mark Fuge  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Precise constraint satisfaction is a prerequisite to deploying learned models in many areas, motivating methods that repair raw neural predictions with a repair procedure. Current methods unroll multiple repair steps in training and softly penalize constraint violations that remain after the unroll. This is compute- and memory-intensive, lacks robustness when the repair fails to converge, and surrenders most of the constraint satisfaction work to the repair. Our central finding is that, contrary to common practice, a single detached projection step suffices in training. We accomplish this with a Projection-Adaptive Loss (PAL), which uses the constraint residual after this single step to adaptively weigh constraint penalties on the raw prediction. In experiments, PAL is the only method that retains virtually perfect feasibility on extremely nonlinear constraints, and matches or outperforms current methods on synthetic and engineering benchmarks. Because it only requires a single detached projection step, PAL trains 2.5x faster than the canonical repair-based method (DC3) on its own ACOPF benchmark. PAL can also be trained when constraints are expensive to evaluate (e.g., via neural surrogates), a setting where current unrolled methods are memory-intractable.

---


### 147. [Frozen in a Frame: The Velocity Blind Spot in JEPA World Models](https://arxiv.org/abs/2610.04585)

**<font color=#1a73e8>作者：</font>** Tinghe Zhang, Chunyu Liu, Yu Leon Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint-embedding predictive architectures (JEPAs) for world modeling train an encoder so a predictor maps a current embedding and action to the next frame's embedding, always from a single rendered frame. This has a structural blind spot: a renderer without motion blur draws a scene from configuration alone, so a single-frame embedding carries no velocity information, for any encoder, including the official released LeWM weights. We confirm this on official checkpoints across four real benchmarks (PushT, Reacher, Cube, TwoRoom): every linear velocity probe sits at or below chance while position probes reach R^2 about 0.95. We introduce RateIdent, a three-stage diagnostic protocol, and TI-JEPA, a lightweight fix splitting the latent into a pose code and an explicit finite-difference motion code, predicted jointly. Across three physically grounded environments, TI-JEPA gives a significant, seed-robust gain on a stop-at-goal planning task over a matched-memory baseline, e.g. 55% lower final distance on Pendulum (p=3.2x10^-10) and 64% on CartPole (p=5.1x10^-15). We reproduce this at official ViT-Tiny plus AdaLN-transformer scale, then push the same recipe onto real dm_control Reacher photographs trained from scratch, where TI-JEPA's branch separation exceeds the memory-having baseline's by roughly 38x, the paper's largest margin. Against a same-footprint recurrent RSSM-style predictor, TI-JEPA matches or beats its rollout accuracy on two of three environments, stays separately probeable for pose and motion, and wins outright on the most coupled one. A checkable formal argument and six evaluated environments show single-frame targets are the wrong object to predict when velocity matters, and a small, interpretable structural change fixes it with no privileged supervision. Code, checkpoints, and the project page are linked below the title.

---


### 148. [StegoMemory: Agentic Memory Acts as Covert Steganographic Channel](https://arxiv.org/abs/2610.04589)

**<font color=#1a73e8>作者：</font>** Snehasis Mukhopadhyay, Arun Nair  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Is agentic memory robust against stealthy steganographic attacks? We carry out a large-scale red-teaming exercise to test whether agents can encode attacker-controlled strings in one session and recover them in another without triggering safety oversight. Following SHADE-Arena-style tasks, we embed malicious side tasks to encode secret strings using steganography within otherwise benign tasks and evaluate them using independent task-completion and safety oversight. We test 14,000 attack trials spanning 91 model-attack configurations, 13 models, and 7 steganographic schemes: Acrostic, Mesostic, Telestich, Word-choice, Capitalization, Position-based, and Homoglyph. 41.2% of trials successfully encode the target payload in the generated response, while 29.8% survive the memory-write step with the encoding intact. Overall, 25.4% of trials yield a recoverable payload at retrieval, and 20.1% achieve exact-match recovery, including synthetic API keys and cryptographic material never exposed to the receiver. Among the exact-match transmissions, 71.4% also pass primary task-completion scoring and are independently judged safe by the oversight model, corresponding to 14.4% of all trials in which a successful covert transmission would appear to be an ordinary, benign interaction under task-level evaluation. Our results demonstrate that agentic memory can function as a persistent cross-session covert channel. The results further show that the principal bottleneck occurs at memory persistence rather than retrieval: once a steganographic payload survives the memory-write stage, a substantial fraction remains recoverable. We therefore argue that memory integrity, information-flow control, and covert-channel detection should be explicit security requirements for agentic systems.

---


### 149. [Bounds, Decompositions and Null Behaviour of KRATOS: A Mathematical Specification of a Recognition-Comparability Diagnostic](https://arxiv.org/abs/2610.04592)

**<font color=#1a73e8>作者：</font>** Maria Dolores Gonzalez, Alberto Barbado  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> KRATOS is a group-structured bibliometric diagnostic that compares the distribution of documents (participation) with the distribution of citation weight (recognition) over a fixed, finite universe of analytical groups. This note gives its complete mathematical specification and derives the properties that govern its interpretation. Beyond bounds and equality conditions for each component, we show that the recognition-alignment score depends on citation data only through ratios of group mean citation rates to the corpus mean; that the composition ceiling of the participation--recognition factor is an affine function of the total variation distance to the uniform reference; and that the factor itself satisfies Fréchet-type bounds in terms of this ceiling and a participation-weighted recognition score. We establish an exact logarithmic decomposition of the composite index, an ordering between the primary and a reciprocal-symmetric recognition score, invariance properties, and closed-form first and second moments of the recognition ratios under global and stratified permutation nulls. These results explain why composite orderings can be sensitive to small groups, heavy-tailed citation distributions and metadata reassignment. All results are verified numerically with an accompanying script. The specification concerns measurement structure only; it does not define a measure of epistemic change or justice.

---


### 150. [Asymptotically Optimal Best Arm Identification with Fixed-Budget under Differential Privacy](https://arxiv.org/abs/2610.04600)

**<font color=#1a73e8>作者：</font>** Keqin Chen, Jie Bian, Yulian Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Best arm identification under differential privacy is a pure-exploration problem in which both statistical efficiency and privacy protection must be achieved simultaneously. We study fixed-budget best arm identification for bandits under pure $\epsilon$-differential privacy, where the learner must recommend an arm after a prescribed sampling budget while protecting the full transcript. We prove that the optimal exponential decay rate of the error probability is upper bounded by an instance-dependent privacy-aware transportation exponent that differs from the analogous quantity used to characterize the stopping time in fixed-confidence analysis by Jourdan and Azize [2025]. Guided by this exponent, we propose AO-Pri-BAI, an adaptive algorithm that maintains private running estimates through Laplace-tree mechanisms and learns a sampling design through a min--max interaction between hard alternatives and arm allocations. We prove that AO-Pri-BAI satisfies pure $\epsilon$-differential privacy. We also establish that the exponent of the failure probability of AO-Pri-BAI matches the privacy-aware benchmark. Numerical studies show that even in the non-asymptotic setting, AO-Pri-BAI outperforms benchmark algorithms on various instances, complementing the theoretical analyses.

---


> [!TIP]
> 当前位于：**101-150**（第 3/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
