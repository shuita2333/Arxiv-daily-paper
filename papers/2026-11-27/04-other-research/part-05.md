# 📦 其他研究 | 2026年11月27日

> 本类共 **314** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-314](./part-07.md)

---

### 201. [AnyCam4D: Ray-Based 4D Gaussian Rendering for Arbitrary Camera Models](https://arxiv.org/abs/2611.34223)

**<font color=#1a73e8>作者：</font>** Sascha Kirch, Rafael Pagés, Jan Ondřej 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real cameras are not pinholes, yet most dynamic Gaussian splatting assumes they are. Footage is therefore undistorted first, losing field of view or detail, especially with wide-angle and fisheye cameras. Static Gaussian splatting has largely solved this with ray-based rendering, which suits any camera. Native 4D Gaussians, which model motion in space-time, cannot use it directly: each Gaussian's orientation and size cannot be recovered reliably from its covariance. We present AnyCam4D, which trains native 4D Gaussians on original footage by ray-based rasterization, preserving field of view and resolution at about the per-step cost of standard projection. Our key contribution is a numerically stable way to obtain orientation and size: we condition a square root of the 4D covariance. Trained models render through other cameras, with rolling shutter, depth of field or chromatic aberration. With a synthetic 170-degree fisheye camera, training on original images improves peak signal-to-noise ratio (PSNR) by 3.0-8.1 dB. On real footage, AnyCam4D has lower perceptual error than the standard projection adapted to each camera, at comparable PSNR and without camera-specific derivations. With the synthetic camera rotated 60-80 degrees away from the capture rig's view, it leads by 6.2 dB against ground truth.

---


### 202. [EgoMyo: Physical Hand State Estimation from Egocentric Video and Wrist Electromyography](https://arxiv.org/abs/2611.34224)

**<font color=#1a73e8>作者：</font>** Guanglong Sun, Kanglei Zhou, Ziteng Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical hand interaction depends on configuration, contact, and force, yet nearly identical appearances can conceal different contact states and exerted forces. We therefore formulate physical hand state estimation from egocentric video and wrist surface electromyography (sEMG), combining visual geometry with neuromuscular evidence to jointly recover these coupled components. To support this task, we introduce EgoMyo, a benchmark spanning 5.75M video frames, 50 participants, 34 contact configurations, and repeated donnings, synchronizing these inputs with 3D hand pose and with contact and normal force registered onto the hand surface from bare-hand pressure. Controlled analysis reveals that vision resolves spatial structure while sEMG better estimates force magnitude, that sEMG's gains concentrate in regions where vision is least reliable, and that contact localization limits force accuracy. Guided by these findings, we propose MyoBridge, which makes the hand region the unit of vision-sEMG fusion, lets each region gate its own share of sEMG, and distributes regional force magnitudes only over predicted contact vertices at inference. On held-out trials, MyoBridge reduces pose and force error by 39.8% and 18.5% over the strongest baseline and achieves the lowest pose error on unseen sessions and subjects.

---


### 203. [LiveRelight: Sub-Second Global Illumination Editing for Gaussian Interiors](https://arxiv.org/abs/2611.34226)

**<font color=#1a73e8>作者：</font>** Noah Rothenberger, Dor Verbin, Serge Belongie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Relighting reconstructed 3D scenes remains challenging due to the complex nature of light transport: slow or approximate visual feedback restricts the editor's ability to fine-tune the results to satisfaction. We present a hybrid relighting approach that enables interactive, high-fidelity updates of direct and indirect indoor illumination without per-edit optimization. Our approach permits the editor to make a wide range of relighting edits at room-scale, with near-instant feedback. Our key insight is to precompute geometric light exchange rather than illumination responses, retaining an inexpensive transport solve that accommodates changes in emission and surface reflectance. We evaluate direct illumination on reconstructed 2D Gaussians using visibility-aware sampling of one-sided emitters, while propagating diffuse interreflection through sparse radiosity on a triangle proxy. A sparse projection fitted through Gaussian alpha compositing transfers the proxy solution to the reconstruction. Our formulation further supports fast fixture transformations and emitter insertion by recomputing light source injection. Across eight relighting conditions of our synthetic test suite, our sub-second edits improve relighting fidelity over prior path-traced editing by an average of 5\,dB PSNR, while reducing editing latency by up to three orders of magnitude. Qualitative results further demonstrate realistic, interactive relighting of real-world captures.

---


### 204. [Change Point Detection with Generative Models](https://arxiv.org/abs/2611.34228)

**<font color=#1a73e8>作者：</font>** Tigran Ramazyan, Denis Derkach, Mikhail Hushchyn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Change point detection (CPD) methods aim to identify abrupt changes in the properties of time series, which is a key problem in numerous fields. A major class of CPD approaches relies on computing a CPD score, which is either a discrepancy or divergence between two subsequent samples, called windows. A fundamental limitation of window-based CPD is the 'sample size bottleneck.' To ensure temporal precision, windows must be small; however, small samples provide insufficient statistical evidence for the classifiers and deep-learning models currently used to compute CPD scores. This leads to high variance in the scores and frequent mispredictions. Our study tackles this issue by exploring generative models for window augmentation, effectively expanding available data to improve CPD quality. Experiments on synthetic and real data demonstrate that the proposed approach significantly enhances CPD. Specifically, we show that this approach allows simple classifiers to outperform complex deep-learning baselines by stabilizing the CPD score distribution.

---


### 205. [Evaluating Post-Quantum and Hybrid Signatures for Blockchains: Performance, Storage and Ledger Growth](https://arxiv.org/abs/2611.34229)

**<font color=#1a73e8>作者：</font>** Anthony Mikhaiel, Essam Ghadafi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Advances in quantum computing pose a long-term threat to blockchain systems that rely on classical digital signature schemes such as ECDSA. Migrating these systems to post-quantum cryptography introduces practical costs beyond cryptographic security, including larger transactions, higher computational costs and faster ledger growth. We present an empirical evaluation of 13 signature configurations in a common simulated blockchain framework: ECDSA, ML-DSA-44/65/87, Falcon-512/1024, SLH-DSA-SHA2-128s, and six hybrids combining ECDSA with each post-quantum scheme. We measure signing and verification costs, transaction-processing throughput, and signature and public-key sizes, and project the measured overheads onto five public blockchains: Bitcoin, Ethereum, Solana, BNB Smart Chain and TRON. Verification remains inexpensive for the evaluated lattice-based schemes, with Falcon-512 achieving a verification time comparable to ECDSA (30.1 versus 32.8 $\mu$s). Storage overheads, however, are substantial. Under our modelling assumptions, had the recorded transaction histories used Falcon-512, the most compact post-quantum scheme evaluated, ledger sizes would have been 79--229% larger, depending on the blockchain. Hybrid configurations introduce relatively modest additional storage overhead compared with their standalone post-quantum counterparts, while ECDSA+Falcon-512 approximately doubles the verification cost of standalone Falcon-512. Existing transaction- and script-size limits also present obstacles to straightforward migration in Bitcoin and Solana. Overall, our findings suggest that storage overhead may pose a greater challenge than signature verification costs when migrating blockchain systems to post-quantum cryptography.

---


### 206. [EXPOSURE: Explaining Sources of Uncertainty in Reinforcement Learning](https://arxiv.org/abs/2611.34248)

**<font color=#1a73e8>作者：</font>** Kiana Farhadyar, Yannick Vogt, Philipp Laur 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Shapley values in reinforcement learning are used to explain which observation features drive an agent's behavior and expected return, but not its certainty. Explaining certainty requires understanding how observation features influence different sources of return uncertainty, and Shapley values need the agent's prediction for every subset of visible features. We propose EXPOSURE, which uses one mask-aware belief network for both action selection and Shapley explanations. It explains the variance of the return, split into an observational part due to missing features and an inherent part due to the environment's own randomness, and the entropy of its belief over the masked features. In tic-tac-toe and Minesweeper, where exact Shapley values are computable, EXPOSURE gives more accurate explanations of expected return and its uncertainty, while uniquely explaining belief uncertainty.

---


### 207. [Detector Operating Behavior Inference via Data-Space Sampling](https://arxiv.org/abs/2611.34252)

**<font color=#1a73e8>作者：</font>** Stefan Becker, Simon Weiss, Wolfgang Hübner  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A detector scores candidate detections, but the recall and false alarms at a given confidence threshold depend on the input distribution. We introduce Detector Operating Behavior Inference (DOBI), a second-level inference task: estimating a fixed detector's threshold-dependent, distribution-level operating response from the internal evidence of a single unlabeled image. DOBI treats the detector's threshold response, i.e. recall, false positives, and precision across thresholds, as a latent behavioral state under the current data condition. Controlled data-space sampling probes this state space offline, and a lightweight monitor learns the inverse map from one image to this state, whose single functional output supports multiple operating policies. In a controlled proof of concept with a fixed YOLOv10-Nano person detector and COCO-derived degradations, predicted PR behavior reduces mean absolute deviation from 0.128 for an image-independent mean-behavior prior to 0.054, and predicted functional distances track empirical regime distances (Spearman 0.96). From one unlabeled image, the inferred behavior selects operating points as well as a non-deployable lookup that knows the true regime (macro-regime $F_1$ 0.6604 for both, versus 0.6407 under pristine calibration; oracle 0.6620). On this discrete benchmark, regime-supervised curve lookups are strong controls. Pre-specified continuous and compositional probing shows where functional inference matters: on unseen combinations, the functional decoder has a lower mean curve error than a template lookup, increasingly with distance from the training conditions, whereas the lookup is more accurate for interpolation. These results establish the feasibility of single-image inference of distribution-level detector behavior over the probed conditions. Source code is available at this https URL

---


### 208. [TORE: Token-Wise Taylor Order Selection via Decomposed Residual Error Estimation for Diffusion Acceleration](https://arxiv.org/abs/2611.34261)

**<font color=#1a73e8>作者：</font>** Lei Tang, Baoquan Zhang, Yakun Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models excel at image and video generation, but iterative denoising incurs substantial inference latency. Recent token-adaptive acceleration methods select Taylor prediction orders for the full-model residual using shallow-layer proxy scores. However, candidate orders are evaluated on these proxy features but used to predict the full-model residual, creating a proxy--target mismatch: the proxy-preferred order may not minimize residual prediction error. To address this mismatch, we propose \textbf{TORE} (\textbf{T}aylor \textbf{O}rder selection via \textbf{R}esidual \textbf{E}rror estimation), which selects token-wise Taylor orders based on estimated prediction errors for the full-model residual. Yet direct error evaluation requires future ground-truth residuals, which are unavailable during order selection. TORE therefore estimates prediction error by analyzing how errors arise in Taylor extrapolation. Specifically, it decomposes prediction error into truncation error and finite-difference derivative error, then estimates both contributions from cached residuals to preselect token-wise orders for upcoming skip steps. Extensive experiments show that TORE achieves $4.31\times$ speedup on FLUX.1-dev and $4.18\times$ on Wan2.1 while maintaining high generation quality and fidelity.

---


### 209. [LatentCP-DPO: Conformal Pessimism for DPO with Finite-Sample Guarantees](https://arxiv.org/abs/2611.34275)

**<font color=#1a73e8>作者：</font>** Hongwei Xu, Jingyi Liu, Vincent Y. F. Tan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Direct Preference Optimization (DPO) learns a response policy from human preference data, but with a limited dataset it can overfit to noisy or weakly informative preference labels. We introduce LatentCP-DPO, a framework that combines conformal prediction with pessimistic preference optimization for Bradley-Terry (BT) pairwise feedback and Plackett-Luce (PL) ranking feedback. Building on LatentCP's construction of uncertainty sets for unobserved model parameters, we address how to incorporate this uncertainty into preference optimization and characterize its effect on policy performance. Under exchangeability and a correctly specified preference model, we construct uncertainty sets for latent relative rewards with finite-sample marginal coverage from conformal prediction sets for observable preferences. We then learn a response policy by maximizing the worst-case expected preference log-likelihood over these uncertainty sets, using an independent collection of prompts and candidate responses without preference labels. Under suitable assumptions, we establish finite-sample upper bounds on regularized policy suboptimality that separate policy-class approximation error, conformal uncertainty, and statistical estimation error. For BT feedback, we further establish a worst-case lower bound for LatentCP-DPO that matches the upper bound's reciprocal dependence on the number of unlabeled optimization examples. The lower bound also shows that the uncertainty sets can induce a bias that persists as the optimization sample grows. Together, these results characterize both the statistical accuracy and potential limitations of preference optimization using conformal uncertainty sets. Experiments support the benefits of the proposed framework in finite preference datasets.

---


### 210. [Semantic State Reading for Joint Image-Semantic Diffusion Transformers](https://arxiv.org/abs/2611.34279)

**<font color=#1a73e8>作者：</font>** Guanxi Lai, Zixuan Li, Zhiwei Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained visual representations improve diffusion-transformer training, yet exploiting both global context and local spatial structure requires deciding which semantic states to model and how to access them. We introduce Semantic State Reading (SSR), which jointly denoises image latents, a global CLS token encoding image-level context, and a compact patch state preserving spatial correspondence. SSR couples this global-local modeling with distinct reading paths: local states are fused with corresponding image tokens at the input, while independent projections inject the current global state into every transformer block. Both semantic scopes thus remain accessible throughout denoising. Ablations show complementary benefits from local-state modeling and repeated global reading, and semantic-trajectory interventions alter image layout under a fixed class label. On ImageNet $256 \times 256$, SiT-XL/2 with SSR reaches or surpasses the reference FIDs of SiT, REPA, and Representation Entanglement for Generation (REG) with $100\times$, $40\times$, and $2\times$ fewer training iterations, respectively. SSR achieves unguided FID 1.78 at 2M iterations and FID 1.34 with classifier-free guidance alone. Combining classifier-free guidance with autoguidance yields FID 1.31 at 1M iterations, achieving the best FID in our main comparison table.

---


### 211. [ReMeDi: Single-Image PBR Material Estimation via Reparameterization between Metal and Dielectric Hypotheses](https://arxiv.org/abs/2611.34284)

**<font color=#1a73e8>作者：</font>** Fan Fei, Xin Huang, Yixin Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physically based rendering (PBR) material estimation facilitates relighting, material editing, and 3D content creation. As the reflectance of a surface heavily depends on whether it is a metal or a dielectric, producing any map that determines albedo involves a decision on metalness, which we call the "intended metalness" of the map. Rendering maps with mismatched intended metalness yields physically implausible or misinterpreted materials. The metallic--roughness workflow makes metalness explicit and thus encourages base color to match it, but does not enforce this match, especially for automated methods directly predicting each map. Therefore, we propose ReMeDi, which enforces the match through two components. First, we reparameterize base color as a metalness-weighted blend of its two variants, estimated under the all-metal and all-dielectric hypothesis, respectively. Second, as available supervision cannot teach a single network both hypotheses at every pixel, we restrict each of two separate networks to one hypothesis, so that each variant is ensured to follow its hypothesis. Besides enforcing the match, this also improves each estimated material map. Experiments show that ReMeDi outperforms state-of-the-art methods in both material accuracy and relighting fidelity.

---


### 212. [Energy-Aware Distributed Task Allocation via Local Submodular Maximization](https://arxiv.org/abs/2611.34293)

**<font color=#1a73e8>作者：</font>** Jing Liu, Fangfei Li, Xin Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This paper studies distributed task allocation under time-varying agent sets, task sets, and communication graphs. At each decision epoch, the stage allocation problem is formulated as monotone submodular maximization over a time-varying, energy-filtered admissible ground set subject to a partition-matroid constraint. We develop a Distributed Adaptive Greedy Bidding Algorithm (DAGBA) that combines local admissible-set construction, conditional marginal bidding, and neighbor-based conflict resolution under limited communication. We prove that DAGBA guarantees per-epoch feasibility, finite-round convergence, and residual-energy safety. Theoretically, we identify a sequential-greedy regime where DAGBA recovers the classical $1/2$-approximation guarantee. For general executions with partial information, we derive a local-information-factor approximation bound and conservative bounds computable from the execution trace that quantify the degradation caused by local estimates and parallel fixing. Simulations on cooperative observation missions demonstrate that DAGBA achieves task-completion progress and utility close to centralized and complete-communication references, while improving communication efficiency and maintaining strict energy feasibility.

---


### 213. [Interpretable identification of constitutive parameter field for three-dimensional heterogeneous and graded hyperelastic materials from full-field displacements](https://arxiv.org/abs/2611.34310)

**<font color=#1a73e8>作者：</font>** Kanhaiya Lal Chaurasiya, Vaskar Halder, Prajyot Patil 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The inverse problem of identifying spatially varying material properties of heterogeneous solids using experimentally available displacement fields and boundary reaction forces alone remains challenging. Being able to characterize heterogeneous and graded solids would be advantageous in the design and manufacturing of functionally graded materials and composites. Additionally, an efficient technique for identifying heterogeneous material properties from in vivo measurements would be useful in biomedical contexts to characterize heterogeneous biological tissues. Although several techniques developed over the past two decades have addressed inverse identification for homogeneous materials, including linear elastic, hyperelastic, viscoelastic, and elastoplastic solids, comparatively fewer studies have considered heterogeneous and graded materials. Furthermore, several recent approaches to characterizing heterogeneous and graded materials employ parameter-heavy, deep learning-based frameworks trained to enforce force equilibrium at specified collocation points within the material. In this work, we propose an interpretable and time-efficient framework that predicts the three-dimensional relative spatial variation of a constitutive parameter field for multiple parameters of a heterogeneous hyperelastic material, using only displacement-field data. In this work, we validate our framework on 3D synthetic and 2D experimental benchmarks involving heterogeneous, graded, and anisotropic hyperelastic materials. By leveraging the linear nature of the inverse problem for hyperelastic materials and directly optimizing for the constitutive parameters at the finite-element level, we achieve acceptable prediction accuracy with significantly lower computational time compared to recently reported deep-learning-based frameworks.

---


### 214. [Poisoning Attacks to Local Differential Privacy Protocols for Dynamic Graphs](https://arxiv.org/abs/2611.34340)

**<font color=#1a73e8>作者：</font>** Shang Liu, Yuhan Bao, Hongbin Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the increasing adoption of privacy-preserving techniques in dynamic graph analysis, local differential privacy (LDP) has become a fundamental paradigm for protecting user data in decentralized environments. However, despite its strong privacy guarantees, LDP-based dynamic graph protocols remain vulnerable to data poisoning attacks through malicious data injection. In this paper, we present the first systematic study of data poisoning attacks against privacy-preserving dynamic graphs under the LDP framework. Considering the temporal evolution of dynamic graphs, we identify key challenges in attack design and evaluation, including how to schedule attack resources across time and how to measure cumulative attack impact. To address these challenges, we introduce an absolute gain metric to quantify the overall deviation of graph statistical metrics before and after attacks across time. Based on this metric, we further propose a unified poisoning attack framework for dynamic graphs, which consists of target node selection, dynamic fake node scale scheduling, and fake edge injection. Within this framework, we design a temporal enhanced attack (TEA) strategy that dynamically schedules attack resources to maximize attack effectiveness, along with two baseline strategies, equal-scale attack (ESA) and random-scale attack (RSA), for comparison. Extensive experiments on real-world and synthetic datasets demonstrate that the proposed attacks can significantly degrade the accuracy of graph metric estimation for target nodes.

---


### 215. [SPARC: Semantic Calibration with Latent Multimodal Knowledge for Robust Image-Text Retrieval](https://arxiv.org/abs/2611.34344)

**<font color=#1a73e8>作者：</font>** Zhongkuan Mao, Wenzhuo Zhao, Haidong Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust image-text retrieval aims to maintain accurate cross-modal matching when image or text queries are incomplete, supporting reliable information access in real-world applications. However, existing methods typically focus on adapting to distribution shifts, without adequately addressing candidate discrimination for incomplete queries and ranking instability. To this end, we propose semantic projection and alignment with relational constraints (SPARC), which elicits latent multimodal knowledge from frozen encoders to improve candidate discrimination and ranking stability. Specifically, we first devise a semantic calibration module on a product of spheres that refines incomplete visual and textual features through tangent-space updates, maintaining the unit-sphere structure used for cosine similarity. Second, we introduce a robust semantic guidance module that combines latent multimodal knowledge encoded in complete image-text features with cross-modal semantic anchors to promote semantic alignment of the calibrated features. Finally, we introduce a matching relation constraint module that fuses original query features with their calibrated counterparts and applies a soft ranking constraint to penalize reductions in initially positive matching margins, thereby limiting ranking perturbations. Extensive experiments on Flickr30K and COCO demonstrate that SPARC outperforms competing methods under various image occlusion and word deletion settings, while achieving consistent gains across different pretrained backbones.

---


### 216. [Inverse Reinforcement Learning with State-Dependent Foresight for Human Decision-Making](https://arxiv.org/abs/2611.34351)

**<font color=#1a73e8>作者：</font>** Jinil Kim, Jinwoo Jeong, Hyeongjun Yun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computational modeling of behavior represents individuals with a model fitted to their observed behavior and characterizes them through its parameters. Naturalistic tasks incorporate the complexity of real environments and yield high-dimensional behavioral trajectories. Inverse reinforcement learning (IRL) infers the latent reward function underlying these trajectories. Standard IRL, however, assumes effectively infinite-horizon planning, whereas human foresight is both bounded and state-dependent. Here we introduce SC-AIRL (State-Conditional Adversarial IRL), which builds these two cognitive properties into the planner. Per-depth policies share one reward but differ in how far ahead they sum it explicitly. A state-conditional router mixes them according to the current state. Across held-out episodes in pedestrian crossing and highway overtaking tasks, SC-AIRL improves imitation over Standard AIRL, raising top-1 accuracy from 0.549 to 0.647 and from 0.629 to 0.718, respectively, while more closely reproducing participant behavior in rollouts. Inferred planning depth correlates with self-reported anxiety and motor impulsivity. SC-AIRL thus reproduces human behavior more closely than Standard AIRL while providing an interpretable, model-derived measure of state-dependent foresight.

---


### 217. [RAWPrism: A Three-Task Dataset and a Unified Model for RAW-Domain Image Fusion](https://arxiv.org/abs/2611.34359)

**<font color=#1a73e8>作者：</font>** Tianyi Hu, Yangdong Li, Shuyan Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Research on multi-exposure fusion (MEF), multi-focus fusion (MFF), and infrared-visible image fusion (IVIF) has largely focused on rendered RGB images, while unified fusion across these tasks in the RAW domain before image signal processing (ISP) remains relatively underexplored. To support research in this setting, we introduce the RAWPrism dataset, covering all three tasks, and the RAWPrism model, a lightweight unified multi-task fusion network. The RAWPrism dataset comprises 422 usable MEF scenes and 150 registered MFF pairs from our RAW captures, together with 1,500 FMB-derived IVIF samples, in which the visible RAW inputs are reconstructed by ReRAW and their RGB counterparts rendered by CycleISP. Scene-level partitions and task-specific rendering and scoring protocols connect these resources to method development and evaluation. To our knowledge, the RAWPrism model is the first to unify MEF, MFF, and IVIF directly in the RAW domain. It combines a CFA-aware representation, task-conditioned source gating, and a shared backbone to support all three tasks with one 3.58M-parameter checkpoint. Together, the dataset and model support the study of shared fusion mechanisms across exposure, focus, and spectral complementarity.

---


### 218. [MoCA4D: Monocular 3D Bounding Box Lifting and Tracking with Camera and Object Motion](https://arxiv.org/abs/2611.34370)

**<font color=#1a73e8>作者：</font>** Changwoo Jeon, Jongyoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular 3D bounding box tracking must account for both object motion and changes in camera viewpoint. Framewise box lifting with temporal filtering leaves these motion components implicit, while static-scene fusion assumes stationary objects. We introduce MoCA4D, a framework for 3D box lifting and tracking from monocular video, associated 2D box prompts, and camera intrinsics. An observation branch estimates per-frame geometry, while a dynamic branch predicts a camera transformation shared across objects and a separate rigid transformation for each object. We propose Star Optimization to refine current depth and orientation using the observation and historical boxes propagated through these transformations. The refined box then guides subsequent propagation. Across all evaluated objects in Argoverse 2 and ADT, Star Optimization reduces center motion error by 38.1% and 38.7%, respectively, relative to Kalman filtering of the same observations. On MOVi-F, the dynamic branch achieves the lowest corner and rotation errors and the highest IoU among the evaluated methods over eight-transition motion windows. Real-data camera-only controls further link predicted object motion to improved localization on dynamic-object tracks.

---


### 219. [Plausible Is Not Proven: Testing Failure Explanations in Monocular Depth Estimation](https://arxiv.org/abs/2611.34393)

**<font color=#1a73e8>作者：</font>** Zeeshan Ali, Md Rayyan, Anshuman Chakravorty 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Failure analyses of monocular depth models often name a cause for each error, such as an occluding boundary, a thin object or a reflective surface, but such labels are rarely tested. We present the Vision Error Observatory (VEO), an audit that finds regions failing the $\delta_1$ criterion on sensor-measured pixels, labels each with a likely cause or abstains, and then subjects the labels to four tests: agreement with object annotations on data the label model never saw, agreement with blinded human raters, response to targeted image edits, and value as a training signal. We apply it to eight models on NYU Depth V2, DIODE and iBims-1, with labels also checked on Hypersim, and fix most decision rules before their results. The occluding-boundary label agrees with annotations (AUROC 0.85 on NYU, 0.81 on Hypersim, 0.69 on iBims-1), but a single depth-edge cue does as well, and most boundary failures of the strongest model vanish under a 2-pixel tolerance. The reflection label does not transfer to synthetic data, the textureless label is near chance against annotations, and only one of four edit tests, an exploratory one, supports its label. Evaluated against five blinded raters, VEO's labels matched the human consensus only at chance level (Cohen's $\kappa$ = 0.05). In addition, an increase in the weight on the diagnosed regions during fine-tuning led to an increase in the error on targeted pixels at every weight tested. The architecture-specific failure fingerprint claimed by an earlier version of this project also failed to replicate across the datasets. Plausible failure explanations, in short, need to be tested before they are trusted; we release the protocol, code, ratings and every result file.

---


### 220. [Northstar: Efficient Verifiable Negacyclic Polynomial Arithmetic with Applications to Encrypted Lattice-based Multi-Asset ERC-20 and Verifiable FHE](https://arxiv.org/abs/2611.34417)

**<font color=#1a73e8>作者：</font>** Yeoh Wei Zhu, Shaltiel Eloul, Yash Satsangi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Lattice-based cryptography can be used to construct a variety of post-quantum cryptographic schemes, ranging from standard cryptographic primitives such as digital signatures and encryption, to fully homomorphic encryption (FHE). However, the verification of correct lattice computations remains relatively expensive, particularly for computationally intensive FHE operations and for resource-constrained environments such as on-chain verification via smart contracts. We propose Northstar, an efficient technique for proving negacyclic arithmetic natively. When integrated with existing STARK proving frameworks, Northstar achieves the best overall performance across prover time, verifier time, and proof size compared to prior state-of-the-art approaches for verifiable FHE constructions. Furthermore, Northstar is used to construct the first verifiable encrypted multi-asset (~ 1000 assets) variant of ERC-20 that is efficiently verifiable by a smart contract, and is practically deployable in the current blockchain ecosystem.

---


### 221. [SPGSR: A Small Pixel-Space Generator for One-Step Super-Resolution](https://arxiv.org/abs/2611.34418)

**<font color=#1a73e8>作者：</font>** Yun Yue, Luming Liang, Yiqi Zhong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In one-step super-resolution (SR), vision-only models extract semantic cues directly from the low-resolution (LR) image, keeping those cues spatially aligned with the structures they help restore. Recent models achieve high restoration quality with generators of up to 1.4 billion parameters. Given how much structure the LR image already provides, could a much smaller generator achieve comparable quality? We introduce SPGSR, a vision-only framework that adds a learned RGB correction to the LR image. A frozen DINOv2 guides prediction, and a lightweight block refines the correction locally. SPGSR achieves higher PSNR/SSIM and lower LPIPS/DISTS than VOSR, a leading vision-only SR method, across three benchmarks. Its $31.8\mathrm{M}$-parameter generator is just $6.5\%$ the size of VOSR-0.5B's. SPGSR also achieves competitive quality against T2I-based SR methods. SPGSR's generator uses only $0.60\%$ of the HR pixels used to train and distill VOSR's generator. For $512\times512$ outputs, SPGSR achieves $2.80\times$ and $3.35\times$ GPU-pipeline speedups over VOSR-0.5B and VOSR-1.4B, respectively.

---


### 222. [Can Visual World Models See Force?](https://arxiv.org/abs/2611.34422)

**<font color=#1a73e8>作者：</font>** Felix Tristram, Benjamin D. Killeen, Nassir Navab  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models and vision-language-action policy models are increasingly proposed as foundations for robot manipulation. They predict how scenes evolve and which actions to take, yet successful manipulation depends not solely on following observable trajectories but also on the hidden variable of interaction force. Neurophysiology has shown that humans possess a visual prior for this hidden variable, motivating us to ask the question: Do the representations of visual foundation models also capture the forces involved in an interaction? We define force awareness as the ability of representations to (1) indicate when contact force is applied, (2) track how it changes during an interaction, and (3) reflect how large it is. We probe frozen image, video, world- and policy model representations with a lightweight readout trained on synchronized video and force measurements from two manipulation datasets. Our experiments show that most models capture when contact occurs but not how much force is being applied. Surprisingly, robot post-training does not improve this either, highlighting an important gap in current models capabilities.

---


### 223. [One Representation to Rule Them All -- Open-Vocabulary Change Detection from Text or Visual Examples](https://arxiv.org/abs/2611.34430)

**<font color=#1a73e8>作者：</font>** Blaž Rolih, Matic Fučka, Filip Wolf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary change detection (OVCD) aims to localise user-specified changes without retraining for predefined categories. Existing approaches typically rely on textual descriptions and combine separate models for region proposal, semantic recognition, and temporal comparison. This limits how target concepts can be expressed and makes detection dependent on several intermediate predictions. We introduce OVTSID3, a training-free framework that unifies region grouping, concept identification, and temporal comparison in the representation space of DINOv3. OVTSID3 supports two complementary modes of concept specification: zero-shot textual queries or one-shot visual prompting through a masked reference pair. OVTSID3 outperforms all prior training-free OVCD methods on two building and two natural-disaster benchmarks, raising the average F1 by 8.9 points. OVTSID3 also supports semantic change detection and achieves state-of-the-art on SECOND. These results demonstrate the flexibility of a unified representation for text- or example-guided change detection without task-specific model training.

---


### 224. [Most of the Way There: Turning a Strong Video Prior into an Action-Conditioned World Model](https://arxiv.org/abs/2611.34435)

**<font color=#1a73e8>作者：</font>** Zanyi Wang, Xia Chen, Liu Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern video generators excel at producing visually plausible futures guided by text and image prompts. Yet their emphasis on semantic plausibility does not guarantee fidelity to the physical consequences of specific actions. Action-conditioned world models (ACWMs), in contrast, aim to simulate how the world responds to robot actions, enabling scalable policy evaluation and improvement without costly real-world rollouts. The challenge is not merely to generate a plausible future, but to predict what follows from a specific physical action. As video priors grow stronger, we ask how little adaptation is truly needed to bridge this gap. We introduce Dianjing, a minimal recipe that preserves and unlocks the capabilities of strong video priors through unified physical action conditioning, training concentrated at the high noise levels where motion and layout, and thus the consequences of actions, are decided, and native history conditioning. Built upon MiniMax H3, a 33B video foundation model, Dianjing freezes the pretrained backbone and trains only 0.34% of its parameters using approximately 65 hours of robot video across two embodiments, without additional robot-specific pretraining or camera calibration. Controlled ablations show that where training is allocated across noise levels matters more than how actions enter the network. On WorldOracle, which evaluates predictions against paired real-world executions, Dianjing achieves the best scores on four of the five evaluation tracks and ranks second on AgiBot-Long. Our findings suggest that strong video priors already bring us most of the way to world modeling; lightweight physical action grounding can unlock their potential for real-world prediction.

---


### 225. [PreserveReward: Reliable Consistency Reward Modeling for Image Editing via Dual-Teacher On-Policy Self-Distillation](https://arxiv.org/abs/2611.34446)

**<font color=#1a73e8>作者：</font>** Xueheng Li, Yong Liu, Wen Xue 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-guided image editing has a wide range of applications, yet existing models may inadvertently alter content that should remain unchanged. Reliable consistency evaluation is therefore essential for assessing content preservation and providing reward signals for Reinforcement Learning (RL). However, existing reward models may overlook subtle visual changes or fail to distinguish necessary modifications from unintended alterations, limiting the reliability of consistency assessment. To address this challenge, we propose PreserveReward, a consistency reward model for image editing that integrates visual On-Policy Self-Distillation (OPSD) to enhance fine-grained visual perception and consistency assessment. PreserveReward learns from reference preservation scores through a regression-based scoring loss and employs two complementary teacher views for self-distillation. The local teacher uses matched crops to identify subtle visual changes, while the joint teacher combines local details with global context to determine whether these changes align with the editing intent. To improve the reliability of distillation supervision, we calibrate teacher score distributions via minimum-KL projection under reference-score error constraints and adaptively select teacher process supervision based on gradient alignment with the scoring objective, mitigating scoring bias and optimization conflicts. Extensive experiments across multiple benchmarks demonstrate that PreserveReward achieves strong alignment with human preference on non-edited content preservation and generalizes well across diverse editing scenarios.

---


### 226. [Decision-Aligned Value Learning for Selective Adoption of EEG Fusion in Human-Robot Collaboration](https://arxiv.org/abs/2611.34451)

**<font color=#1a73e8>作者：</font>** Xinjia Yu, Jing Yang, Yang Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) captures neural activity associated with human perception and decision-making. It provides human-robot collaboration (HRC) systems with measurable evidence for event recognition, situation assessment, and action preparation. External sensing cannot easily provide such evidence. However, the quality and complementarity of this evidence vary across samples, and existing EEG fusion methods do not explicitly determine when EEG improves a prediction. We therefore framed selective EEG use as a sample-wise incremental-value estimation problem and proposed Value Estimation and Constraint-Aware Triage for Adoption (VECTA). VECTA separates the generation of an EEG-informed Fusion prediction from the decision about whether it should replace the existing Base prediction. The framework uses system gain to quantify the loss reduction from Base to Fusion and matching gain to assess whether benefits arise from sample-matched EEG. A signed-value learner estimates system gain from decision-time evidence and prioritizes high-value Fusion outputs under budget constraints. Cross-subject evaluations on three HRC datasets showed that matched Fusion outperformed shuffled controls. Estimated gains tracked realized gains, with Spearman correlations of 0.347-0.612 and positive-gain areas under the receiver operating characteristic curve (AUROCs) of 0.708-0.842. Under budget constraints, VECTA reduced Brier loss and harmful Fusion adoption and achieved the highest mean normalized AUBC across three datasets among the selective-decision methods evaluated. Validation on three external multi-modal datasets showed that VECTA could be applied directly as a post-hoc decision layer to task-specific predictors without retraining. These results show that selective Fusion adoption can translate the uneven utility of EEG into system-level gains.

---


### 227. [ProxyGenBench: Benchmarking Proxy-Guided Video Generation](https://arxiv.org/abs/2611.34457)

**<font color=#1a73e8>作者：</font>** Zhenchen Tang, Haolin Lu, Songlin Yang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video generators produce realistic videos, yet controlling how scenes unfold remains challenging. Structural proxies, such as animated 3D blockouts, guide generation by specifying scene layout, motion, camera behavior, and event order. However, these coarse inputs leave details unspecified and may contain artifacts that should not be reproduced. Successful proxy-guided generation must therefore Preserve intended structure, Complete missing content and correct proxy artifacts, and Bind text, image, and audio conditions to the right entities and events. We introduce ProxyGenBench to study these interacting requirements, with 312 evaluation cases from 60 scenes across three scene tasks and controlled variations in proxy fidelity, text detail, and multimodal inputs. We evaluate five video generators using verified, case-specific checklists. Experiments show that proxies improve spatiotemporal control, but greater proxy detail can coincide with poorer completion, while strong structural adherence does not ensure correct binding.

---


### 228. [SceneDesigner++: A Unified 9-DoF Pose Control Framework for T2I and T2V Generation](https://arxiv.org/abs/2611.34461)

**<font color=#1a73e8>作者：</font>** Xincheng Shuai, Zhenyuan Qin, Henghui Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise 9-DoF pose control is essential for visual content generation, enabling users to specify object location, size, and orientation in 3D space. However, existing methods typically focus on either text-to-image (T2I) or text-to-video (T2V) generation, with limitations in pose controllability and temporal coherence. We present SceneDesigner++, a unified framework for 9-DoF pose control across both T2I and T2V generation. We construct ObjectPose9D++, a dataset containing high-quality images and videos with accurate pose annotations. Trained on ObjectPose9D++, SceneDesigner++ combines absolute and relative pose encoding strategies to decouple frame-wise spatial grounding from inter-frame motion modeling. Specifically, absolute pose encoding leverages CNOCS map sequences to provide explicit, frame-wise 9-DoF pose guidance. Meanwhile, our relative pose encoding, termed VPRoPE, incorporates relative pose information into rotary position embeddings to explicitly model inter-frame pose transitions, thereby promoting temporally coherent object motion. A learnable orthogonal transformation is further introduced for each attention head, allowing different heads to capture complementary geometric relationships while preserving input feature norms to promote training stability. We further adopt a two-stage training strategy to learn the absolute and relative pose encoding mechanisms separately. Benefiting from this lightweight and decoupled design, SceneDesigner++ also supports integration with an independently trained camera-control module, enabling separate or joint control over object and camera motion. Finally, we introduce T2IVPoseEval, a benchmark for evaluating diverse object poses and motion patterns in both T2I and T2V tasks. Extensive experiments demonstrate that SceneDesigner++ consistently outperforms same-backbone baselines in pose fidelity and motion quality.

---


### 229. [Fuel as Identity: Authenticating Inter-Satellite Laser Links after Total Key Compromise](https://arxiv.org/abs/2611.34470)

**<font color=#1a73e8>作者：</font>** Leon Birkel, Mohammad Hamad, Sebastian Steinhorst  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Optical inter-satellite links form the backbone of entire constellations in low Earth orbit, yet their security rests on keys alone. When an attacker obtains every key of a satellite, no secret is left to authenticate it again. Existing fixes fail, since ground rekeying encrypts new keys under the leaked ones, and post-compromise protocols assume an authenticated start. As a remedy, the satellite's orbit can take over as the trust anchor. The attacker then needs an impostor satellite that blocks and retransmits the beam, a chord beneath the curved orbit. Hence, the blocking point lies off free fall and costs the impostor continuous thrust. We formalize this position-gated adversary and prove, for satellites on a shared circular orbit, a tight lower bound on the propellant cost in delta-v of a point-mass craft that keeps blocking, however it moves. We present OrbitLock, a history-chained protocol that combines this position gate with ML-KEM. Each link authenticates on its own, and we sketch how combining links forces an impostor onto every link. Once the chain outlasts an impostor's propellant, every key back to the first is authenticated retroactively. A satellite thus needs no crosslink key before launch, so none can leak in the supply chain. The same mechanism heals the link after total key compromise, even without compromise awareness. A passive attacker is shut out at the next round, whereas an active one splits the chains and is exposed once its propellant runs out. The chain can then heal after an operator reset. As a result, every Starlink satellite has a partner on whose link a CubeSat-class impostor runs out of propellant in about two days. This holds against one rigid craft per link running the best attack we know, if each terminal enforces a 1 km exclusion zone, while the protocol only uses under 0.02% of the link.

---


### 230. [DiversePlace: Diversity-Seeking Curriculum Reinforcement Learning for Macro Placement](https://arxiv.org/abs/2611.34472)

**<font color=#1a73e8>作者：</font>** Wenrui Zhou, Jiashun Liu, Wenji Fang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Macro placement is a critical early-stage decision in physical design because macro locations strongly constrain subsequent implementation stages. The task is difficult because these high-impact discrete decisions must be made before downstream quality can be measured accurately, forcing training to rely on fast but imperfect training-time oracles such as half-perimeter wirelength (HPWL). Existing RL-based placers therefore mostly optimize single HPWL-driven solutions, and their long sequential horizons often require heavy search assistance or offline expert data while leaving little room to preserve multiple competitive layouts. We address this gap by making quality-controlled diversity an explicit objective for macro placement. Instead of relying on a single proxy-optimal solution, we maintain a compact archive of HPWL-competitive yet meaningfully different placements for downstream selection. We realize this idea in DiversePlace, a curriculum proximal policy optimization (PPO) framework that combines a quality-gated diversity reward with an expanding placement horizon, enabling from-scratch RL optimization while keeping exploration inside competitive HPWL regions. On the ISPD2005 benchmarks, DiversePlace consistently improves top-5, top-10, and top-20 archive diversity and achieves lower or virtually identical HPWL on all eight designs with better efficiency. Code: this https URL.

---


### 231. [TACC: Target-Aware Carrier Compression for Dense-Context Novel View Synthesis](https://arxiv.org/abs/2611.34476)

**<font color=#1a73e8>作者：</font>** Yiming Fan, Yijia Guo, Zewen Guo 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent feed-forward approaches mark a paradigm shift in novel view synthesis by eliminating the reliance on per-scene optimization, directly inferring 3D representations from input views. However, their reliance on global scene-token context incurs substantial memory and latency overhead, constraining their ability to handle increasingly dense source-view contexts. Compressing source representations offers an intuitive way to limit this token budget. Prior general-purpose compression methods are not tailored for novel view synthesis, as their fixed, target-agnostic nature fails to adapt evidence allocation to individual target views. To overcome this, we introduce TACC, a target-aware compression module tailored for feed-forward latent NVS. Specifically, TACC organizes each source view into a progressive carrier hierarchy. Driven by source-target geometric relevance, it adaptively retrieves tokens to dynamically allocate exact computational quotas. This selective retrieval directly yields a compact, target-conditioned representation. Extensive experiments on the RE10K demonstrate that under dense input settings, TACC achieves $9.23\times$ and $64\times$ higher Effective FPS than Full Context on LagerNVS and LVSM, respectively. Effective FPS excludes one-time source encoding and Carrier construction.

---


### 232. [Feed-Forward Adaptive Gaussian Splatting for Interactive Medical Volume Rendering](https://arxiv.org/abs/2611.34478)

**<font color=#1a73e8>作者：</font>** Zhongpai Gao, Benjamin Planche, Meng Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Path-traced rendering shows CT and MR volumes with realistic lighting, but it restarts after every change of view, clipping plane or transfer function (TF), the map from voxel intensity to colour and opacity, which limits the frame rate. Feed-forward Gaussian splatting models such as RenderFM predict the Gaussians directly from the volume instead of fitting them to each scan, and are fast. RenderFM, however, handles only CT, runs its network again after every TF edit, has no clipping operator, and places its Gaussians on a uniform 3-mm grid that blurs organ boundaries and cut faces. We present RenderFM-Next, a feed-forward model that addresses these limits. One network handles both CT and MR. Its Gaussians are predicted once per volume: a new TF needs no pass of this network, and a clipping plane cuts them exactly, using operators from prior work. The model predicts coarse 3-mm Gaussians for the whole volume and refines them to 1.5 mm only where refinement improves the image. A small score head ranks the coarse Gaussians by how much refining them would reduce the rendering error; at render time the user chooses how many are refined, and those next to a clipping plane are always refined, which sharpens cut faces. We build a benchmark of about 2,000 CT and MR scans with path-traced references under clinical presets, TF edits and clipping. Our RenderFM-Next improves over RenderFM retrained on this benchmark by 2.8 dB on CT and 2.4 dB on MR and renders a 1600x1600 view in 4-6 ms. Refinement adds 0.30 / 0.69 dB over the same model trained without it (0.51 / 1.17 dB on cut faces), and refining a learned 10% of the coarse Gaussians matches a random 50% with 2.4x fewer Gaussians. Project page: this https URL

---


### 233. [ProManO: Beyond Sim(3) for Metric Upgrade of Feed-Forward Geometry with Visual-Inertial Anchors](https://arxiv.org/abs/2611.34480)

**<font color=#1a73e8>作者：</font>** Lingxiang Hu, Zhenjun Zhao, Qi Shao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Upgrading feed-forward geometry to metric scale with visual-inertial odometry (VIO) raises the question of which correction should align dense feed-forward prediction with sparse metric VIO anchors. Existing methods use either a similarity transformation, which cannot represent depth-dependent distortion, or a projective transformation, which alters pre-calibrated intrinsics. We prove that the transformations compatible with pre-calibrated intrinsics form a ten-dimensional manifold. Beyond Sim(3), this manifold contains three degrees of freedom (DoF) that locate the plane at infinity and leave residuals growing quadratically with depth range after any similarity alignment. These DoF are invisible in the image and can be resolved only by metric depth along viewing rays or by multi-view constraints. To estimate them, we propose ProManO, a probabilistic manifold optimization framework in which every anchor is weighted by its along-ray uncertainty and inlier probability within a single expectation-maximization (EM) procedure. ProManO certifies the similarity synchronization and refines the plane at infinity only where it is observable, which guarantees an objective value no worse than that of the optimal similarity alignment. Experiments on EuRoC, CID-SIMS, Oxford Spires, and KITTI-360 demonstrate that ProManO achieves the highest mean F1 and outperforms Sim(3) alignment on all four datasets. The project page is available at this https URL.

---


### 234. [Where Does the Asymmetry Enter? Staging a Fairness Audit Across a Fused Multimodal Moderation Pipeline](https://arxiv.org/abs/2611.34491)

**<font color=#1a73e8>作者：</font>** Kardelen Subasi, Jarosław A. Chudziak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Almost every short-video upload now passes through a classifier that fuses video, speech, and on-screen text into one decision about whether it may be seen. It moderates every language community on the platform at once, and fairness across them is judged, if at all, from one accuracy score. That score is compatible with error falling almost entirely on one language group. An audit that goes looking reads the model's decisions, the last stage of a long pipeline and the one whose test has the fewest items. We ask where in a fused pipeline a subgroup asymmetry can be detected at all: in what the classifier may read, in what its branches encode, or in what it decides. We answer this with a post-hoc audit of a published TikTok classifier, holding all three stages to one significance standard using only its logged decisions, labels, and pre-fusion features, with source language as the subgroup axis. The asymmetry is significant at the stage deciding what the model may read, and again in what the text branch encodes. At the earlier stage, a language-blind cap admits less of a Vietnamese clip than an English one, for reasons of segmentation, not verbosity. The asymmetry is undetectable at the decision, where the smallest subgroup leaves twelve items to test. An audit reading only decisions looks where its evidence is thinnest; the same test staged upstream recovers a disparity the decision-level view returns as noise.

---


### 235. [Auditing Identity and Timing Signals in Operational Logs](https://arxiv.org/abs/2611.34493)

**<font color=#1a73e8>作者：</font>** Andrew Hendel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Models that predict events from operational logs, such as sepsis in ICU records or failures in hard drives, can score well by recognizing which patient or drive a record came from, or when it was recorded, instead of predicting the event. I introduce two simple audits that measure how much of this information a dataset carries before any event-prediction model is trained, and apply them to seven public datasets in six domains. One asks whether a classifier can tell that two records came from the same unit; the other asks which of two records from the same unit came later. Under the stated nulls, both have expected AUC 0.5. In ICU data, the identity audit flags a common preprocessing step: carrying the last measurement forward raises identity AUC from 0.916 to 0.993. On a 12-hour sepsis forecasting task, carrying forward makes a model look 0.163 AUC better than raw values when a patient's hours are split between training and test, but only 0.046 better when patients are held out. The exaggeration under patient overlap also appears in a second ICU dataset with mortality as the outcome. On the sepsis task, a chronological control with complete follow-up, in which training sees only a patient's earlier, resolved hours, shows no positive mean overlap gap. Timing is a strong predictor: with complete follow-up, hour of stay and measurement counts alone, with no clinical value, score 0.761 on held-out patients, and adding the raw clinical values changes that by +0.018. Outside the ICU, 95% of drives and 75% of loans have records on both sides of a calendar cut, and the overlap gap persists under a calendar split. The audits show which features and preprocessing choices to check; the evaluation protocol decides the consequences. I release the code, a library that runs the audits on any table with a unit column and a time column, and a guide to using the audits.

---


### 236. [Angular Interpolation in Sparse-View Low-Dose CT Reconstruction: Placement Effects and Data-Consistency Step-Size Scaling](https://arxiv.org/abs/2611.34508)

**<font color=#1a73e8>作者：</font>** Yitian Tang, Yuncheng Zhang, Hualiang Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dual-domain networks combine projection and image processing for sparse-view low-dose computed tomography (CT). We quantify the contribution of angular interpolation before learning and distinguish its roles in sinogram initialisation and the image residual base. On synthetic parallel-beam data, parameter-free interpolation reduces noise-free missing-view mean absolute error by 99.7% relative to zero filling at 60 views. Full-view filtered back-projection (FBP) of the jointly learned completed sinogram adds 1.27 dB of peak signal-to-noise ratio (PSNR) over interpolated FBP. In a data-consistency dual-domain network (DC-DuNet), a 2x2 configuration ablation controls branch width, depth and training schedule while varying these placements and their associated input channels. After 20 epochs, the PSNR contrasts are +1.98 dB for sinogram initialisation and -2.16 dB for the interpolated image base; the image-base ranking also reverses during training. The sinogram-initialised variant exceeds an image-only U-Net by 0.96 dB at 60 views and 10% dose, and by 1.28 dB on independently generated synthetic data. The U-Net leads at higher view counts and with a shared interpolated image base. Without retraining, the variant retains a 0.12 dB advantage on held-out CHAOS abdominal CT under simulated degradation; the image-base contrast rounds to zero. The implemented projection/backprojection pair has empirical dominant gain of approximately 0.85NK, where N is image-grid width and K acquired view count. These results distinguish interpolation placement from network architecture and support NK normalisation for step calibration.

---


### 237. [SMOTE 25 Years of Magic: What Has Been Done, What the Evidence Shows, and Whom It Reached](https://arxiv.org/abs/2611.34511)

**<font color=#1a73e8>作者：</font>** Thanapong Intharah, Pharamut Makjaroen, Kanvara Thawarorit 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background. SMOTE was published in this journal in 2002 and reviewed here at its fifteenth anniversary in 2018. At twenty-five it is cited by more than 34,000 indexed works, half of them outside computer science. Objectives. To establish what the methods built on SMOTE change, how strong the evidence for them is, and whom the technique has reached. Methods. We audited a curated corpus of 76 papers, 37 of which propose a SMOTE-family generator, and tested its coverage with a systematic search of 22,426 records in the PRISMA 2020 format. From the corpus we collected 1,756 dataset entries, 1,511 published comparisons with SMOTE and the evaluation design of 71 studies; from the search we drew 300 applications of SMOTE at random. We used an agentic AI approach to extract, screen and code under our written rules, and we report how each step was checked. Results. Every variant re-decides some of the six decisions of the SMOTE rule, and 24 of the 37 are only ever run on two classes. In their own papers, proposed methods beat SMOTE in 79.0% of the decided comparisons, but independent studies find that the gains shrink with strong learners and tuned thresholds, and that resampling damages calibration. The corpus holds 52 of the 3,097 records that pass the screen and covers the early years closely, the recent ones thinly. The reach is very wide, but a benefit at the level of outcomes is undemonstrated, four harms are documented, and an estimated 37% of applications resample the whole data set before splitting it. Conclusions. For tabular classification, a new SMOTE variant should no longer count as a contribution in itself: a new generator should be tested one decision at a time against class weighting and a tuned threshold with a strong learner, with calibration reported. We close with a selection guide, a reporting checklist of fifteen items and a research agenda.

---


### 238. [Rank Before You Encode: Reading a Few Percent of a Whole-Slide Image](https://arxiv.org/abs/2611.34523)

**<font color=#1a73e8>作者：</font>** Haoyu He, Mahdi S. Hosseini  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Classifying a whole-slide image requires encoding thousands of high-resolution tiles with a pathology foundation model, which accounts for most of the inference cost. Existing efficient methods reduce this cost by selecting fewer tiles, but typically train a new model around their selection strategy. A largely unexplored alternative is to keep an existing full-bag model frozen and run it on selected tiles at the same encoder cost. We introduce this comparison, alongside random tile sampling at matched cost. To select tiles, we fit a lightweight selector with 3.3K parameters to the attention of a frozen model, without additional slide labels. The selector ranks regions from a slide thumbnail, encodes the top K regions at 5x magnification, and selects b for processing at 20x. We evaluate seven frozen MIL aggregators on six tasks and compare them with nine efficient methods trained on the same features and splits. At a budget of (K,b)=(1000,10), encoding costs about 6.6% of the full bag and is 10-14x faster, excluding tiling. The AUROC drop is no more than 0.005 in 33 of 36 aggregator-task pairs. At (500,10), the cost falls to about 4% and inference is 13-22x faster, but AUROC drops by up to 0.035 on CAMELYON17, where small metastases are easily missed. Selection improves over random sampling by about 0.10 AUROC on tasks with focal lesions, while random sampling performs well on diffuse tasks. In our comparisons, the frozen model at (500,10) is ahead of nine efficient methods in 55 of 60 paired comparisons. Giving an existing WSI model fewer tiles is thus a baseline that a new efficient model should be compared with at matched encoder cost.

---


### 239. [Resilience Analysis Through Automated Stage Identification and Quantitative Assessment](https://arxiv.org/abs/2611.34527)

**<font color=#1a73e8>作者：</font>** Anna Strzoda, Krzysztof Grochla, Rafael Munoz-Carpena  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduced an ML-based approach, designed to be domain- and threat-agnostic, for automated recognition of PARA (Plan/Prepare, Absorb, Recover, Adapt) resilience stages in system-performance time series, enabling subsequent quantitative resilience analysis across different systems. We investigate four ML models for resilience stage recognition: Random Forest (RF), Support Vector Machine (SVM), Light Gradient Boosting Machine (LightGBM), and Extreme Gradient Boosting (XGBoost). We then use the ML models' predictions to quantify system resilience by computing corresponding resilience metrics from system-performance data observed before, during, and after disruptive events. We evaluate the proposed approach using datasets from two distinct operational domain network systems and an airport transportation system, demonstrating its domain-agnostic applicability to resilience assessment. The results demonstrate the effectiveness of resilience stage classification, with the best F1-scores ranging from 74.3% to 99.4% across all resilience stages. The overall resilience metrics R_t and RL are estimated, with the best models' MAPE ranging from 0.35-0.82% on IEEE 802.11 and LTE to 1.65-9.56% for the airport. These results provide a basis for threat-agnostic resilience analysis of complex engineering systems, enabling further assessment of how effectively a system withstands, absorbs, and recovers from disruptive events and stress conditions.

---


### 240. [Kant-Q: A Q-Learning Algorithm for Kantian Equilibrium in Symmetric Markov Games](https://arxiv.org/abs/2611.34536)

**<font color=#1a73e8>作者：</font>** Rishi Bharadwaj, Sujit Gujar, Yadati Narahari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly interact with one another, and many of these interactions are mixed-motive games, which have posed a persistent challenge for learning algorithms. Most multi-agent reinforcement learning (MARL) algorithms are designed to reach Nash equilibria, yet in many such games these equilibria are Pareto-inefficient. We instead study Kantian equilibria, an economic solution concept in which each agent plays the action it would want all agents to adopt. In symmetric games, this corresponds to an optimal common policy. We propose Kant-Q, a Q-learning algorithm in which each agent learns action profiles where all agents play the same action. Each update is then a sample from a single-agent MDP, so Kant-Q inherits the convergence guarantees of standard Q-learning. We show that every symmetric Markov game has a pure Kantian equilibrium. We also prove that all agents' Q-tables converge to the same limit, whose greedy policy is such an equilibrium, and that greedy play converges whenever the optimal common action is unique at every state. We further show that in a subclass of symmetric monotone games, the Kantian equilibrium is Pareto-efficient among pure strategy profiles and strictly individually rational. Empirically, on the iterated Prisoner's Dilemma and the GovSim fishery with up to 200 agents, Kant-Q learns the Kantian equilibrium, while the baselines underperform. Since copies of the same AI system naturally face one another in symmetric games, these results suggest universalization as a design principle for cooperative AI-AI interaction.

---


### 241. [CADENCE: Sensor-GroundedWorld-Consistent Gaussian SLAM for Collaborative Mobile Reconstruction](https://arxiv.org/abs/2611.34549)

**<font color=#1a73e8>作者：</font>** Reshad Ul Karim, Abrar Samin, Md Rashad Al Hasan Rony  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Collaborative reconstruction with consumer phones promises faster and more complete indoor maps. However, heterogeneous devices introduce degraded observations and unreliable cross-device associations, so a single poor contributor or incorrect match can corrupt the shared Gaussian map. To address this, we propose \textbf{CADENCE}, a collaborative Gaussian simultaneous localization and mapping (SLAM) system that separates finding cross-device matches from deciding whether and how peer observations update the map. To find matches, a sensor-grounded regional memory summarizes committed observations and ranks candidate peer regions using appearance, relative pose, gravity, barometric altitude, and observation quality. Deterministic geometric verification and optional physical checks then decide which of the proposed matches are accepted. Once a match is accepted, separate cue-based confidences control how its observations contribute to pose constraints, geometry, appearance, and memory. As a result, useful depth can still contribute even when color is unreliable. Throughout this process, local tracking remains isolated from mapping, verification, and networking. We evaluate CADENCE on eight Matterport3D houses that were not used to train the memory. On these houses, regional memory achieves an area under the receiver operating characteristic curve (AUROC) of $0.95$ to $0.97$ and thus outperforms appearance retrieval, while verification keeps false-link rates below $0.5\,\%$. Furthermore, soft confidence weighting reduces the mean receiver peak signal-to-noise ratio (PSNR) loss from $2.66$ to $1.05$\,dB across eight degradations while retaining useful peer depth. Finally, using inertial and platform motion, CADENCE tracks all twelve held-out iPhone scans with a mean absolute trajectory error of $6.98$\,cm, and its refined maps achieve better average rendering quality than the baselines.

---


### 242. [On Utilization of Edge-AI for condition monitoring towards predictive maintenance: A use case in dairy processing using explainable AI](https://arxiv.org/abs/2611.34563)

**<font color=#1a73e8>作者：</font>** Rahul Umesh Mhapsekar, Norah O'Shea, Omer Ali 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Industrial Internet of Things (IIoT) and Artificial Intelligence (AI) are driving Industry 4.0, enhancing productivity, automation, and efficiency in manufacturing systems. This study develops an Edge-AI-based condition monitoring framework, as a step towards predictive maintenance, for a rotary valve in a dairy processing pilot plant, using vibration data collected via a low-power IIoT sensor node and processed on an edge device.

---


### 243. [Score-based Black-box Attack via Adversarial Condition Guided Diffusion Model](https://arxiv.org/abs/2611.34564)

**<font color=#1a73e8>作者：</font>** Yuhang Chen, Chih-Hong Cheng, Kurt Debattista 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models enable unrestricted adversarial attacks that aim to fool classifiers while preserving the natural appearance and semantics of the original image. However, existing diffusion-based black-box attacks largely rely on transferability from surrogates, making their effectiveness sensitive to differences between surrogate and victim. Improving transferability can also distort semantic content and degrade image quality. Moreover, retaining the original prompt to preserve fidelity leaves the diffusion model's conditional prior underused for adversarial guidance. We address these limitations by adapting score-based black-box attacks to reverse diffusion, using the victim's output probabilities to guide latent updates without accessing its gradients. We further introduce adaptive-target guidance, which uses the victim's current runner-up class as an adversarial condition to steer denoising towards the decision boundary. Because such guidance can introduce unwanted semantic changes, we also propose target-search guidance, which searches for a small perturbation of the original condition embedding using a score-based attack. This achieves comparable attack effectiveness with better image quality than runner-up guidance. Experiments on the ImageNet-Compatible dataset show that our framework outperforms transfer-based baselines in both attack effectiveness and image quality.

---


### 244. [Physics-Guided Generative Modelling of Oxy-Combustion Flame Images: From Conditional LSGANs to Denoising Diffusion Models](https://arxiv.org/abs/2611.34568)

**<font color=#1a73e8>作者：</font>** Imane Er-rabhi, Gorkem Oztarlik, Jean Caudal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Validating industrial oxy-combustion burner designs traditionally requires costly experimental campaigns in which each operating condition is physically reproduced on an instrumented rig and imaged via OH* chemiluminescence, rendering iterative design exploration prohibitively slow. This work develops deep generative surrogate models that map a 15-dimensional vector of continuous operating parameters (thermal power, swirl numbers, momentum ratios, mixture fractions, etc.) directly to a $512\times64$ heat-release flame image, trained on 1,609 experimental samples from the OXYTEC dual-swirl non-premixed oxy-combustion database. Two complementary generative paradigms are investigated, as they offer opposite strengths for surrogate modelling: a custom spatially-anchored conditional least-squares GAN (cLSGAN-L1-CBN), whose single-pass generation enables near-instantaneous inference, and a custom physics-guided denoising diffusion probabilistic model (DDPM), whose iterative sampling favours the smooth, continuous heat-release gradients of fluid flows. Both are validated through ablation on a stratified held-out test set. The optimized cLSGAN reaches RMSE 0.022 and FID 20.68 and generates an image in about 20 ms on a mobile workstation GPU, though extended training leaves its texture realism unchanged; the DDPM improves steadily over long training horizons, reaching RMSE 0.019 and FID 20.29 at 40,000 epochs, at the cost of roughly thirty seconds per image on the same hardware --- three orders of magnitude slower than the adversarial surrogate. A nearest-neighbour analysis traces the persistent worst-case errors to sparsely sampled regions of the parameter space, and a parameter-sensitivity study confirms smooth, physically consistent responses to perturbed inputs. These results demonstrate that carefully guided generative models can act as reliable visual surrogates for combustion experiments.

---


### 245. [Investigating the efficacy of vortex beam speckle patterns for the recognition of atmospheric turbulence and fractional topological charge with a deep learning model](https://arxiv.org/abs/2611.34573)

**<font color=#1a73e8>作者：</font>** Ratikanta Swain, Allarakha Shikder, Naseem Babu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fractional topological charge (TC) enlarges the usable mode set of orbital angular momentum (OAM) links, but reading it reliably after atmospheric turbulence remains difficult. Interferometric and diffractive methods need an undistorted beam and a careful alignment, while most learned approaches treat integer or coarsely spaced charges and do not include turbulence. Here we ask whether the charge of a scalar vortex beam can be regressed directly from a single speckle image, and at which turbulence strength this stops working. We propagate vortex beams over 1500~m through 150 von Kármán phase screens, scatter them with a fixed random diffuser, and record $256\times256$, 16-bit speckle images for TC from 0 to 10 in steps of 0.01 and turbulence strengths $D/r_0$ from 0 to 50; the results reported here use a subset of 20\,000 images, and a data set of $10^{6}$ images is in preparation. A convolutional neural network estimates the TC and, through an auxiliary head, the turbulence category. On charges withheld from training, the mean absolute error is 0.031 without turbulence (with a common intensity scale) and rises to 0.78 at $D/r_0=10$ and 1.85 at $D/r_0=50$, against 2.5 for a constant prediction, and the turbulence category is identified correctly in 78\% of the images. The results show that, at the present training size, the charge is read accurately only without turbulence, and that the charge and the turbulence oth act on the speckle grain size, which may limit the readout. Experimental validation and the extension to vector vortex beams are left for future work.

---


### 246. [ChemoMAE: Self-Supervised Spectral Representation Learning Reveals Chemical Heterogeneity in Historical Wood](https://arxiv.org/abs/2611.34581)

**<font color=#1a73e8>作者：</font>** Ryuji Yamaguchi, Miyuki Matsuo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In historical timber buildings, multiple environmental factors act over centuries on wood whose chemical composition varies across anatomical regions, producing complex patterns of degradation. Understanding how timber members degrade is important for the effective conservation and restoration of historical buildings, yet the mechanisms underlying these patterns remain unclear. To investigate these mechanisms, we used self-supervised learning to establish a common basis for comparing specimens from timber members that differ in wood species and service history. We examined transverse sections of 49 wood specimens from several historical buildings in Japan using near-infrared hyperspectral imaging. ChemoMAE, a self-supervised Transformer, learns pixelwise spectral representations through masked denoising that exploits multicollinearity among spectral variables. Clustering these representations yields spatial maps without predefined chemical-state categories. Because anatomy and degradation can produce spatially continuous regions, we formulated Local Label Agreement (LLA) to quantify agreement among labels assigned to neighboring pixels. Using spectra alone, ChemoMAE yielded higher mean LLA than baseline methods on validation specimens. We then trained ChemoMAE anew and fitted cluster centers across all specimens. Spatial structures consistent with wood anatomy and the expected effects of surface exposure emerged in the resulting maps. By cross-referencing regional spectra and spatial distributions across specimens in light of wood anatomy, service histories, and prior studies, we proposed models of internal and surface degradation as mechanistic hypotheses. This exploratory AI for Science framework gives researchers a basis for linking latent patterns learned through self-supervision with domain knowledge when investigating how material states form.

---


### 247. [Learning from Crowds with Unsupervised Item Response Models](https://arxiv.org/abs/2611.34602)

**<font color=#1a73e8>作者：</font>** Pascal Wullschleger, Majid Zarharan, Donnacha Daly 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Item Response Theory (IRT) is the study of tests, including the properties of both test items and test takers. Crowdsourced labelling can be cast as an unsupervised IRT problem: annotators play the role of test takers with varying ability, and annotation tasks play the role of items with varying difficulty. We evaluate unsupervised variants of standard logistic IRT models for latent trait recovery and label inference on six datasets with crowdsourced labels and known ground truths. Unsupervised IRT models can recover annotator and item traits (e.g., ability, difficulty and discrimination) reliably across most datasets when compared to supervised variants trained on the ground truth. IRT models seem to be more stable in label inference compared to most baselines, but might not be the best possible choice depending on the dataset. We further propose to use IRT models to inform classifiers during training and compare against existing crowd-learning methods. We find that crowd-learning methods can improve F1 over majority-vote baselines, but no method significantly improves both F1 and calibration. IRT-informed curriculum methods seem to preserve calibration better than other crowd-learning methods, but are not at the frontier regarding F1, and the best crowd-learning methods in terms of F1 seem to be miscalibrated.

---


### 248. [DuCo: Exploiting Dual Cross-Layer Consistency for Sparse Geometric Attention](https://arxiv.org/abs/2611.34608)

**<font color=#1a73e8>作者：</font>** Liangyu Xiang, Junyu Gao, Xiaofeng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense global attention is crucial for capturing cross-view geometry in visual geometry foundation models, yet its quadratic complexity limits efficient inference on long image sequences. Existing sparse attention methods primarily select entries of the global attention matrix based on attention probabilities and construct masks independently across layers, overlooking value redundancy and cross-layer information reuse. By analyzing attention distributions and clustering value representations across layers, we reveal two forms of \emph{cross-layer consistency}, characterized by highly similar attention probability distributions and localized changes in value redundancy structures. Building on these observations, we propose \textbf{DuCo}, a training-free sparse attention framework that exploits historical attention information and value redundancy for efficient geometric inference. Specifically, DuCo leverages historical attention information to estimate current-layer dense attention probabilities and introduces value clustering to exploit redundancy, with clusters efficiently refined through local updates across layers. Both factors are integrated through probability-weighted value distortion to jointly optimize four cluster representation states under an attention budget for sparse mask construction. Experiments across three visual geometry foundation models and five benchmarks demonstrate favorable accuracy--efficiency trade-offs.

---


### 249. [Automated Batch-Variable Selection for ComBat-Based Radiomic Harmonization](https://arxiv.org/abs/2611.34618)

**<font color=#1a73e8>作者：</font>** Jose Lozano-Montoya, Gemma Urbanos, Carmen Prieto-de-la-Lastra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> ComBat harmonizes multicentre radiomic features, but batch variables are usually chosen manually, without a standardized criterion across image acquisition parameters. We propose ParsiComBat, which selects acquisition parameters for ComBat, balancing batch-effect removal against feature-structure preservation and abstaining when technical variation is negligible.
ParsiComBat ranks candidate acquisition parameters by batch effect, filters redundancy, and scores sequential ComBat corrections. We evaluated it in three experiments: in simulations, testing whether it recovered a known batch variable and abstained without one; in CT (NSCLC-Radiomics) and MRI (MAMA-MIA) cohorts, comparing batch-effect removal against manufacturer (manual), every feasible parameter (greedy) and AutoCombat; and in clinical prediction, internally and externally.
In simulations, ParsiComBat identified the true batch variable in 92.9% of positive trials and abstained in 99.2% of null controls. In CT, correcting for reconstruction kernel reduced mean k-nearest neighbour batch-effect test from 0.276 to 0.032, almost matching greedy correction of six variables. In MRI, correcting for slice thickness and manufacturer reduced it from 0.680 to 0.325, slightly more than manual selection but less than greedy correction of seven variables. Removing technical variation did not improve clinical discrimination: no strategy, including raw features, differed significantly from ParsiComBat in area under the curve.
ParsiComBat provides a data-driven framework that removes technical batch effects using minimal acquisition parameters, preserving feature structure and clinical discrimination. It selects variables verifiable against the acquisition protocol and abstains when no correction is needed, supporting transparent, reproducible multicentre radiomics.

---


### 250. [Beyond Pose Control: Anatomically Consistent Ultrasound Video Generation](https://arxiv.org/abs/2611.34622)

**<font color=#1a73e8>作者：</font>** Yue Zhou, Fangxu Han, Tony Danjun Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-controlled video generation anticipates how a scene appears from new viewpoints by relying on a prior learned implicitly from large-scale data. Ultrasound poses the same problem, with the probe pose as the viewpoint, but under opposite conditions: anatomy offers an explicit prior that every sonographer relies on, whereas tracked scans are too scarce to learn it implicitly. As a result, pose control alone is not enough, and pose-conditioned ultrasound generators produce implausible anatomy in unscanned regions and inconsistent anatomy on revisits. We go beyond pose control and give the generator the two kinds of knowledge that make up a sonographer's mental model. An anatomical prior, built from a population of subjects, guides generation where nothing has been scanned, and is refined online by every generated chunk towards the scanned subject. A 3D latent memory, designed around the cross-sectional physics of ultrasound, compounds the generated slices into a volume of the patient and reslices it at new poses, keeping revisited anatomy consistent. The fine-grained memory enters the generator at the input, while the coarse anatomy prior guides the layout across transformer blocks. Experiments on thyroid, kidney, and lumbar spine show improved visual fidelity, pose following, and anatomical consistency over pose-conditioned and memory-augmented baselines.

---


> [!TIP]
> 当前位于：**201-250**（第 5/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-314](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
