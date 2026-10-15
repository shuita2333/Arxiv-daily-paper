# 📦 其他研究 | 2026年10月16日

> 本类共 **264** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-264](./part-06.md)

---

### 101. [AWARE-RG: Abstraction Aware Explanation of Resiliency Graphs for Cyber Physical Systems](https://arxiv.org/abs/2610.19650)

**<font color=#1a73e8>作者：</font>** Shadaab Kawnain Bashir, Rakesh Podder, Philip D. Hopkins 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Understanding the security posture of cyber physical systems (CPS) requires reasoning across both information technology (IT) and operational technology (OT). However, a security analyst often holds an incomplete, role-specific view of the underlying system which has most likely resulted from their knowledge limited by a need-to-know framework. Such an incomplete view can potentially lead them to incorrectly assess if a cyber attack produces an untoward physical consequence resulting in making uninformed decisions about system resilience. In this work, we present AWARE-RG (Abstraction Aware Explanation of Resiliency Graphs), a semi-automated, human-in-the-loop framework that provides an analyst with a role-bounded, need-to-know explanations of resiliency paths in a CPS. The AWARE-RG abstraction structure is derived using Formal Concept Analysis over MITRE ATT&CK for ICS tactics, ordered by the ICS Cyber Kill Chain. For valid attack-fault queries, plan repair and backward means-end analysis identify the missing dependencies, explain why the physical hazard is reachable, and suggest defensive strategies. For invalid attack-fault queries, AWARE-RG localizes the first abstraction level at which the path fails, and reports confirmed blocking conditions as hardening pointers.

---


### 102. [On Global Joint Lower Bounds in Zeroth-Order Nonconvex Optimization](https://arxiv.org/abs/2610.19652)

**<font color=#1a73e8>作者：</font>** Yuxuan Xia, Xiao-Tong Yuan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has sought to transfer first-order nonconvex optimization guarantees to zeroth-order methods through gradient estimators, typically incurring a factor linear in $d$. \citet{kornowski2024} obtained an $\mathcal{O}(d\delta^{-1}\epsilon^{-3})$ oracle complexity for nonsmooth nonconvex optimization and asked whether its dependence on all three parameters is jointly optimal. Although the dimension dependence and the first-order dependence on $(\delta,\epsilon)$ are separately known to be unavoidable, a matching zeroth-order lower bound has remained open. We answer this question in the unrestricted full-space setting. For smooth stochastic nonconvex optimization, we establish a scalar-oracle lower bound of $\Omega\!\left(dL_0^2\min\{\Delta H,L_0^2\}/\epsilon^4\right)$ assuming a smooth, globally lower-bounded population objective and a second-moment bound on sample Lipschitz constants. A smooth reduction then yields a lower bound for Goldstein stationarity, proving the joint minimax optimality of the dependence on $(d,\delta,\epsilon)$ under explicit high-dimensional and small-accuracy conditions. Crucially, our results allow algorithms to query arbitrary points in $\mathbb{R}^d$, adaptively select sample-function labels, reuse the same sampled function at any number of locations, and output points without spatial restrictions. Thus, unlike lower bounds based on bounded query regions or fresh evaluation noise, our guarantees apply to a fully adaptive, reusable-sample scalar oracle. We also establish a separate noiseless exact-value lower bound against randomized algorithms, and hence also against deterministic methods. Our proof combines a globally defined sequential nonconvex construction with an exact Gaussian scalar channel, multistage random-field estimates, and an antithetic finite-sample realization that preserves information hardness under adaptive reuse.

---


### 103. [Remember, Revisit, Revise: Scaffold Memory for Long-Horizon 3D Geometry](https://arxiv.org/abs/2610.19674)

**<font color=#1a73e8>作者：</font>** Soumick Sarker, Mengmi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometry foundation models estimate camera poses and 3D scene structure from video sequences, but maintaining consistent reconstructions over long horizons remains challenging. Feed-forward models process long sequences as independent, fixed-length frame windows and align their predictions, causing pose and reconstruction errors to accumulate across windows. Streaming models retain information from past frames to inform future predictions, but cannot revise earlier estimates when later observations reveal errors. To address this, we introduce Scaffold MemOry for Revision (SMORE), a framework equipping frozen geometry foundation models with a revisable external memory for long-horizon inference. Inspired by hippocampal associative memory in biological brains, which links spatial context with sensory experience, SMORE associates where an observer is with what it observes, enabling past observations to be stored, retrieved, verified against new evidence, and revised when inconsistencies are detected. We evaluate SMORE with eight competitive geometry models on five datasets spanning camera pose estimation, multi-view depth estimation, 3D point-cloud reconstruction, simultaneous localization and mapping (SLAM), and novel view synthesis. Across all evaluated models, SMORE consistently improves long-sequence pose estimation, reduces multi-view depth error by up to 58%, reduces Chamfer distance for 3D point-cloud reconstruction by up to 43%, and achieves average trajectory error as low as 2.9 cm in long-horizon SLAM. By retaining corrected poses and observations, SMORE further improves the fidelity and spatial consistency of large-scale 3D scene reconstruction. These results establish revisable external memory as a flexible interface for extending pretrained geometry models beyond fixed-context prediction toward iterative, error-correcting inference over long visual sequences.

---


### 104. [MicroSDF: Microfacet-Driven Hybrid Neural SDFs for Mixed-Reflectance Surface Reconstruction](https://arxiv.org/abs/2610.19681)

**<font color=#1a73e8>作者：</font>** Lejia Ye, Yuhua Xu, Yulan Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D reconstruction in real-world environments remains a significant challenge due to the coexistence of reflective and non-reflective surfaces, which pose distinct modeling demands. Existing methods often treat these surface types separately, limiting their generalizability and physical plausibility. To bridge this gap, we propose MicroSDF, a novel neural implicit framework that facilitates geometry and reflectance modeling through microfacet theory. Our approach incorporates three core innovations: (i) a microfacet-guided geometry model that extracts multi-scale surface normals (macroscopic and microfacet) from a signed distance field (SDF), regularized by a proposed microfacet normal consistency loss to enforce physically plausible surface orientations; (ii) an enhanced dual-branch color model, where the specular branch leverages the microfacet normals to model high-frequency reflectance, and the vanilla branch, unlike prior works, uses reflection direction (instead of viewing direction) to better model diffuse and low-frequency specular components; and (iii) a detection-guided color blending strategy that adaptively fuses the color outputs based on reflection priors, providing more physically intuitive blending than implicitly learned blending weights. Combined with a tailored multi-stage optimization scheme, the proposed MicroSDF achieves robust and high-fidelity reconstruction across reflective and non-reflective surfaces. Extensive experiments on DTU, Shiny Blender, Ref-NeRF, and DeepVoxels datasets demonstrate state-of-the-art performance, establishing a new direction for physically grounded neural reconstruction.

---


### 105. [Enhancing Latent World Models with Associative Memory](https://arxiv.org/abs/2610.19683)

**<font color=#1a73e8>作者：</font>** Yuwei Sun, Siyu Zhu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models trained via latent dynamics offer a scalable path for embodied planning, yet existing methods suffer from representational collapse, computational overhead, and limited long-horizon capability. We introduce a memory-enhanced latent world model that augments JEPA-style prediction with a content-addressable memory bank. Our approach learns high-level representations directly from observations, operating at multiple temporal scales within a shared latent space, and conditions predictions via adaptive layer normalization. To prevent collapse and ensure effective memory usage, we design two complementary losses that encourage slot diversity and balanced temporal utilization. Experiments on PushT, Tworoom, Reacher, and OGBCube demonstrate that our method achieves state-of-the-art performance with a lightweight architecture, outperforming conventional latent world models on long-horizon planning tasks.

---


### 106. [Annealed Lévy Diffusion via Gaussian Surrogate Reverse Dynamics](https://arxiv.org/abs/2610.19692)

**<font color=#1a73e8>作者：</font>** Yuling Jiao, Lican Kang, Jerry Zhijian Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gaussian diffusion models offer a practical framework for generative modeling. Denoising Lévy Probabilistic Models (DLPM) introduce heavy-tailed perturbations with a fixed tail index throughout denoising. We introduce Annealed Lévy Diffusion (ALD). ALD varies the stability index $\alpha(t)$ to combine heavy-tailed exploration with Gaussian refinement. Our marginal-first formulation represents stable noise as a scalar Gaussian scale mixture. This formulation enables standard Gaussian noise-prediction training with one additional scale input. We study two sampling processes. ALD-renoise estimates the clean sample and injects fresh marginal noise. ALD-posterior preserves dependence between successive states through an accumulated conditional variance and a Gaussian bridge update. Both samplers reuse the same trained predictor with different scalar inputs. We evaluate ALD on four 2D benchmarks and an imbalanced nine-mode mixture. We also examine training efficiency and the effects of prediction perturbations on clipped Holtsmark data. Additional experiments evaluate MNIST and CelebA64 generation and CIFAR-10LT augmentation. ALD preserves local geometry on the evaluated light-tailed and manifold-structured targets.

---


### 107. [ReGRA: Residual-Gradient Adaptation for Complementary Low-Rank Fine-Tuning](https://arxiv.org/abs/2610.19700)

**<font color=#1a73e8>作者：</font>** Fanyao Li, Yuxi Liu, Xiaohao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) enables parameter-efficient fine-tuning by learning low-rank weight updates. Increasing rank expands adaptation capacity, but does not guarantee that all learned directions improve downstream performance. In a diagnostic experiment with rank-16 LoRA, we show that retaining only the top singular components achieves the best performance, whereas adding further components degrades it. Motivated by this, we propose Residual-Gradient Adaptation (ReGRA), a two-stage method for making more effective use of a fixed rank budget. After the first stage, ReGRA estimates task gradients on a calibration set and removes their projections onto the two-sided subspace induced by the first-stage update. It then aggregates the residual-gradient directions to initialize a second-stage adapter without changing the first-stage update. An orthogonality regularizer encourages the two updates to capture complementary directions. Both updates can be merged into the pretrained weights, incurring no additional inference overhead. Across diverse benchmark sets, ReGRA achieves stronger performance than alternatives with the same total rank and even matches LoRA adapters with twice the rank. Ablation studies and further analysis support the contribution of its core design choices. Code is available at this https URL.

---


### 108. [Runtime Monitoring of Supermartingale Certificates](https://arxiv.org/abs/2610.19701)

**<font color=#1a73e8>作者：</font>** Mirco Giacobbe, Thomas A. Henzinger, Konstantin Kueffner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Supermartingale certificates formally guarantee temporal properties of discrete and continuous-time stochastic dynamical systems. However, these guarantees rely on a mathematical model of the world, leaving a sim-to-real gap that can invalidate them for the deployed system. We formulate the runtime monitoring problem for supermartingale certificates, in which a monitor observes a single system trajectory and raises an alarm when there is sufficient statistical evidence that the supermartingale certificate has been violated during execution. We present an algorithm to automatically construct a monitor using betting-based sequential tests that bound the probability of ever raising a false alarm at a user-specified level. Within this betting framework, we formulate strategies that allow the monitor to exploit spatial regularity to improve detection power while preserving this statistical guarantee. We demonstrate the efficacy of our approach on supermartingale certificate benchmarks from the literature.

---


### 109. [SceneAE: Scene Generation and Reconstruction in Queryable 3D-Anchored Latent Space](https://arxiv.org/abs/2610.19708)

**<font color=#1a73e8>作者：</font>** Shuofeng Sun, Wenzhao Zheng, Yunpeng Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video world models have increasingly adopted 3D memory mechanisms to integrate historical observations into a lightweight and persistent scene representation. This naturally raises a complementary question: if 3D representations can serve as an effective mechanism for memorizing observed scenes, can they also be directly used as the latent space for reconstructing and generating scenes? Motivated by this idea, we represent a scene as a compact and unstructured 3D-anchored latent space (\textbf{SceneAE}). Each latent combines an
explicit 3D position with an implicit content feature and is spatially grounded to describe its local scene region, forming a
sparse latent point cloud. Unlike conventional video-VAE latents that describe how a scene appears from particular viewpoints, our
representation directly describes the scene itself, making it naturally applicable to both reconstruction and generation. For
reconstruction, once the scene has been generated, our persistent 3D representation can be projected and decoded into RGB-D observations by different target cameras, without the need to regenerate a video for each new camera trajectory.
For generation, we leverage the geometry-content separation to first generate camera-controlled 3D geometry and
then synthesize content conditioned on it, reducing camera-appearance entanglement and improving camera
controllability. Experiments show that this 3D latent achieves superior generation quality, computational cost, and camera controllability.

---


### 110. [Beyond State Capacity: Why Retrieval Breaks in Mamba](https://arxiv.org/abs/2610.19709)

**<font color=#1a73e8>作者：</font>** Nir Yarden, Amit Ben-Artzy, Roy Schwartz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mamba models underperform Transformers on in-context retrieval. This gap is usually attributed to Mamba's fixed-size recurrent state, which loses information as the context grows. We challenge this assumption by focusing on query-first retrieval, a setup in which the query precedes the context and state capacity should not be the binding constraint. We show that even in this setting Mamba lags substantially behind Transformers, despite its selection mechanism, which was designed to distinguish relevant content from distractors. We then demonstrate that the Mamba selection gates have sufficient control over the state updates to influence the model output: intervening on specific gates alone can swing accuracy between extremes. However, as gates are input-dependent, they require the incoming token's representation to encode its relevance to the query. We therefore probe token representations across layers, and find that the relevance signal emerges only gradually with model depth, and that the gates begin to reflect it only several layers deeper. Crucially, we find that gates in retrieval-critical layers are not yet aligned with relevance. The selection mechanism is thus expressive enough to solve the task, but it commonly operates on a relevance signal that has not yet arrived. Mamba's retrieval bottleneck therefore extends beyond state capacity: even when capacity is sufficient, the delayed emergence of relevance information across depth often prevents successful retrieval.

---


### 111. [No Way To Steal My Face: Proactive Defense Against Identity-Preserving Personalized Generation](https://arxiv.org/abs/2610.19717)

**<font color=#1a73e8>作者：</font>** Lizhi Xiong, Jun Li, Ziqiang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in diffusion models have enabled high-fidelity, identity-preserving image generation for personalized applications such as digital avatars and virtual try-on systems. However, their reliance on sensitive facial reference images raises growing privacy concerns. Existing defense mechanisms are primarily designed for training-based personalization and struggle to generalize to emerging training-free approaches, due to fundamental differences in their identity integration paradigms. To bridge this gap, we propose IDGuardian-the first generalizable and model-agnostic identity protection framework capable of defending against both training-based and training-free personalization methods. IDGuardian abstracts the personalization process into two critical stages: identity extraction and identity injection. It then introduces crafted adversarial perturbations to simultaneously disrupt both stages. Specifically, it degrades the identity features extracted by external encoders and establishes an adversarial conceptual bridge that misdirects the generative trajectory away from the target identity. Extensive experiments show that IDGuardian effectively protects identity across various personalization pipelines and model architectures, while remaining robust to post-processing, adaptive attacks, and cross-dataset generalization. Our code is available at this https URL.

---


### 112. [Learning Individual Scientific Taste with Privileged Hindsight Distillation](https://arxiv.org/abs/2610.19719)

**<font color=#1a73e8>作者：</font>** Hanwei Fan, Yanqiao Wang, Yiqi Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific taste shapes which research directions researchers pursue, and it varies across individuals. Existing work evaluates research directions along multiple evaluation criteria or models scientific taste using community feedback signals such as citations and reviews, but neither directly captures how individuals translate assessments under the same criteria into different preferences. We model scientific taste as a researcher-specific mapping from criterion-level assessments in a shared, evidence-grounded evaluation space with proposal-visible evidence, to relative preferences. A population-level mapping learned from retrospective supervision provides a cold start when individual feedback is scarce. We introduce Privileged Hindsight Distillation (PHD), which uses later-emerging scientific evidence during training to improve proposal-time criterion assessment and the population mapping, while exposing only proposal-visible information at inference. We evaluate our approach primarily in quantum research, where structured public reviews are largely unavailable, and use pairwise proposal comparison as a direct interface for observing individual taste. With only 15 comparisons per researcher, our method captures sharply different tastes, including opposing preferences over the same research-direction pairs when they trade off across evaluation criteria. In an interactive study, personalized rankings also surface proposals associated with greater subsequent user engagement, connecting learned taste to downstream research exploration.

---


### 113. [Generative World Simulation with DAO and JING](https://arxiv.org/abs/2610.19726)

**<font color=#1a73e8>作者：</font>** XGEN Team, Guohao Cai, Haoxuan Che 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a Generative World Simulation framework that couples persistent shared world state with continuous first-person audiovisual generation. The framework integrates DAO, a computable world engine, and JING, an Egocentric Interactive Experience Model, to support sustained interaction for humans and agents. DAO maintains the states of characters, objects, and spaces and their relationships, advancing the world according to interaction rules and world time while preserving the consequences of past actions. From this evolving state, DAO derives observer-specific conditions for JING, which combines these conditions with character, object, and scene references, observation history, and current actions to generate each observer's audiovisual experience. Users can explore environments, manipulate objects, and communicate with characters through viewpoint control and text instructions, with their actions shaping both the shared state and subsequent experiences. By connecting world-state evolution with experience generation in a continuous interaction loop, the framework offers an approach to building interactive worlds that retain their history, evolve through action, and persist beyond any individual observer.

---


### 114. [A Diagnostic Study of World-Space Human Recovery Under High Camera Dynamics](https://arxiv.org/abs/2610.19729)

**<font color=#1a73e8>作者：</font>** Hao-Jen Chien, Wei-Lun Chao, Yu-Lun Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular world-space human recovery methods excel on current benchmarks, but these rarely include fast camera motion. We introduce the K-Pop stress test, broadcast dance videos that combine fast, large camera motion with dense multi-person choreography. Leading methods produce plausible per-frame meshes on these videos, yet their world-space trajectories drift far from the performers' stage positions. Through a systematic diagnosis, we show that the camera and human estimates each remain self-consistent, and that the drift appears when they are combined at mismatched scales. Each is recovered at its own scale, so a mismatch between the two can turn camera motion into human drift that grows with camera displacement and becomes severe in broadcast dance videos. We derive a closed-form correction that estimates this mismatch and applies one scale to all performers, removing the drift while keeping their relative positions in one shared world frame. It requires no retraining and works with existing backends. Combined with physical constraints, the correction yields stable world-space reconstruction for choreography modeling, scene editing, data generation, and virtual reshooting.

---


### 115. [What Happens to the Goal? Distinct Failures of Policy Alignment in Goal Misgeneralization](https://arxiv.org/abs/2610.19731)

**<font color=#1a73e8>作者：</font>** Julia Barth, Armin Sommer, Kunvar Thaman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Goal misgeneralization is a common failure mode in which an agent behaves competently out of distribution but does not pursue the intended goal. However, we still have a weak understanding of what happens to the intended goal in misgeneralizing agents. Across three Procgen environments and five robot tasks, we find three distinct forms of policy-goal misalignment: (1) functional target substitution, where behavior follows an alternative goal, (2) a policy shortcut, where behavior follows a learned action strategy, and (3) cue competition between intended and proxy goal cues. We distinguish these regimes by tracing where goal information remains available internally, how strongly it influences the policy, and what role it plays in action selection, and find that the goal is lost at different depths. Where the goal reaches the decision, as in cue competition, steering redirects the policy to the goal's location, raising intended-goal reach from 16.0% to 95.3%. Where it reaches the policy but not the decision, only new downstream wiring recovers goal reach, from 31.6% to 84.3% in the environment with the action shortcut. Where it is inert, neither works. Our results show that goal misgeneralization is not a single failure of goal representation, but distinct failures of policy alignment at different depths, tightly connected to which recovery works.

---


### 116. [Exact Cut Complexity of Equal-Length Proportional Cake Cutting](https://arxiv.org/abs/2610.19733)

**<font color=#1a73e8>作者：</font>** Yasushi Kawase, Bodhayan Roy, Mohammad Azharuddin Sanpui  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We study proportional cake cutting under an equal-length constraint, where each of $n$ agents must receive a bundle of length exactly $1/n$ that is worth at least $1/n$ to that agent. Our main result determines the exact worst-case number of cuts needed to guarantee such an allocation, namely $2n-2$ for every $n$. This improves on the previously known quadratic upper bound. The proof combines the constrained necklace-splitting theorem with a recursive assignment argument based on Hall's theorem. The same bound extends to the stronger requirement of envy-freeness when $n$ is a prime power, and an $O(n^{1.525})$ upper bound holds for arbitrary $n$. We then ask whether such allocations can be computed. We first show that no deterministic protocol in the Robertson--Webb model terminates after finitely many queries on every instance and always returns an exact equal-length proportional allocation, even for two agents with identical valuations. For every $\varepsilon>0$, however, $O(n^2/\varepsilon)$ queries suffice to produce an allocation in which every agent receives a bundle of length exactly $1/n$ and value at least $1/n-\varepsilon$, again using at most $2n-2$ cuts. Finally, we augment the Robertson--Webb model with two-knife queries. We show that recursive balanced halving attains the optimal bound of $2n-2$ cuts when $n$ is a power of two. For arbitrary $n$, we give a procedure using $O(n\log n)$ cuts.

---


### 117. [Object Pose from 2-D to 3-D Point and Line Correspondences](https://arxiv.org/abs/2610.19734)

**<font color=#1a73e8>作者：</font>** Thai Quynh Phong, Radu Horaud, Adnan Yassine 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper we present a method for optimally estimating the rotation and translation between a camera and a 3-D object from point and/or line correspondences. First we devise an error function and second we show how to minimize this error function. The quadratic nature of this function is made possible by representing rotation and translation with a dual number quaternion. We provide a detailed account of the computational aspects of a trust-region optimization method. This method compares favourably with Newton's method which has extensively been used to solve the problem at hand, with Faugeras-Toscani linear method [6] for calibrating a camera, and with the Levenberg-Marquardt non-linear optimization method. Finally we present some experimental results which demonstrate the robustness of our method with respect to image noise and matching errors.

---


### 118. [MakSafe: A Spatiotemporal Semantic Framework for Formal Specification and Compliance Checking of Road Vehicle Safety Rules](https://arxiv.org/abs/2610.19735)

**<font color=#1a73e8>作者：</font>** Maksym Labzhaniia, Julien Deantoni, Marie-Agn{è}s Peraldi-Frati 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scenario-based validation is essential for automated road vehicles but cannot cover the full variability of openworld traffic. We present MakSafe, a formal spatiotemporal framework for specifying and checking road vehicle safety rules through semantic zones, action-based forecasting, and trace-tree reasoning, avoiding uniform time discretization. We formalize the road network, vehicle states, and occupancy zones, then build executable rules for front-vehicle identification and timeto-collision (TTC) verification. The evaluation combines a tracedependent case study with a scalability benchmark over traffic density (N ), horizon (H), and branch factor (B). MakSafe yields branch-specific verdicts, deriving safe and unsafe outcomes from the same initial scene, and re-evaluates a scenario after a control update. A single rule check stays well below a millisecond across the reported sweep, and longer horizons slow the TTC check.

---


### 119. [HyperLoop: Hyperspectral-Assisted Loop Closure Detection in 3D-SLAM for Planetary Exploration](https://arxiv.org/abs/2610.19742)

**<font color=#1a73e8>作者：</font>** Annie Bhalla, Dennis Rotondi, Riccardo Giubilato 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous navigation of planetary rovers is challenged by visually repetitive, featureless terrain. SLAM systems based on 3D Gaussian Splatting (3DGS) offer dense mapping but rely on RGB appearance descriptors that degrade under perceptual aliasing - a common failure mode in extraterrestrial environments where physically distinct locations appear visually identical. This paper presents HyperLoop, the first framework integrating hyperspectral imaging (HSI) into the loop closure module of a 3DGS-based SLAM system. Hyperspectral descriptors encode material-level spectral signatures complementing RGB features, providing robustness to illumination changes and visual repetitiveness. Two HSI descriptor families are introduced: Bag-of-Spectral-Words (BoSW), encoding spectral material distributions via TF-IDF weighted histograms, and PCA-K VLAD (PCAK-VLAD), capturing first-order residual statistics of PCA-compressed spectral signatures. Both are evaluated with SIFT-VLAD and NetVLAD RGB descriptors under Strict-AND and Weighted fusion strategies on a custom dataset from the Moon-Mars Outdoor Test Site (MMOTS) at DLR, comprising synchronized RGB-D and hyperspectral sequences across four planetary analog traverses (65.5 m total). A key finding is that the sensor's Red-NIR range (600-860 nm) provides limited discriminability for rock terrain: the best HSI fusion (SIFT-VLAD + BoSW, Strict-AND) achieves 5.04 cm ATE RMSE, within 1.8% of SIFT-VLAD alone (4.95 cm). The gain over NetVLAD (8.81 cm) is attributable to SIFT-VLAD, not HSI fusion. This motivates future adoption of SWIR sensors capturing diagnostic mineral absorption features absent from the 600-860 nm range for planetary SLAM missions.

---


### 120. [Discriminative Score Function: Turning Pretrained Models into Functional Generative Priors](https://arxiv.org/abs/2610.19743)

**<font color=#1a73e8>作者：</font>** Junhoo Lee, Hyeonjin Kim, Sangbum Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Discriminative models are trained with task-specific objectives such as classification, detection, or representation learning, yet their practical utility depends on generalizing beyond the training task to unseen samples from the same domain. This suggests that a discriminative model may retain an implicit trace of the data manifold beyond its task labels. We ask whether this trace can be exposed as a generative signal without task-specific guidance. We introduce the Discriminative Score Function (DSF), which extracts an image-space generative field from the loss-gradient geometry of a pretrained discriminative model. DSF provides a training-free update rule that moves images toward model-consistent visual regions without retraining or task-specific targets. We apply DSF to diverse pretrained discriminative models, including ResNet classifiers, DETR detectors, and DINOv2 ViT encoders. DSF generates unconditional images from noise and supports conditional guidance, editing, inpainting, and explanation through the same field. DSF-generated samples also provide effective zero-shot quantization calibration when real images or labels are unavailable, preserving feature geometry better than data-free calibration baselines. These results show that discriminative training leaves a generative functional signal for synthesis and calibration. Project page: this https URL.

---


### 121. [Beyond Reachability: A Relation-Semantic Reasoning Framework for Biomedical Multi-hop QA](https://arxiv.org/abs/2610.19754)

**<font color=#1a73e8>作者：</font>** Ziyang Ling, Ziyi Chen, Ronald X.Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical multi-hop reasoning over knowledge graphs requires identifying a semantically valid relation sequence that supports the answer. Existing methods can retrieve correct answers, yet often rank them poorly within a large pool of seemingly relevant candidates. Even when a correct answer is retrieved, its associated evidence and reasoning path may fail to support the relation composition required by the question. We term this disconnect between answer reachability and evidential validity the reachable-but-invalid problem. We present ReSemReason, which shares a question-induced distribution over typed, directed relation schemas between candidate discovery and evidence selection. Schema compatibility guides graph search; ReSemAttn then uses relation-conditioned key/value projections and an uncertainty-weighted path prior to attend to candidate-specific evidence. A separate absolute-support score complements normalized attention when all retrieved paths are weak. The reported experiments on BioHopR, PrimeKGQA, and MedReason show improvements in answer ranking and answer-set quality. Path-discrimination analyses examine the distinction between endpoint correctness and evidential support. We also specify matched controls for search, attention, and schema uncertainty.

---


### 122. [Physics-Shaped, Not Physical: Auditing Physics-Guided Underwater Image Restoration](https://arxiv.org/abs/2610.19763)

**<font color=#1a73e8>作者：</font>** Mochamad Rizal Fauzan, Irgi Surya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physics-guided networks for underwater image restoration predict transmission and backscatter and invert the image-formation model, yet rarely test whether this physics does any work. We audit one representative design, PhysGuide-Net, with four controlled experiments: five-seed ablations on UIEB with zero-shot evaluation on the complete LSUI (4279 pairs) and AUIED3K (3000 pairs) sets; a data-efficiency study with a capacity-matched control that removes the formation model; and a validation of the predicted maps against measured range on Sea-thru. With all 800 training images the physics module gives no zero-shot gain (mean PSNR differences of at most 0.16 dB; all 95% intervals include zero) at 3.4x the FLOPs. With 80 images it helps more (+0.65 dB on UIEB, +1.48 dB on AUIED3K; seed-to-seed s.d. on AUIED3K from 1.3 to 0.5 dB), although not individually significant after correction, and the control does not reproduce this (0.8-1.0 dB lower). Yet the predicted transmission does not behave like a physical quantity: its correlation with range is no stronger than for the range map of a different image (pooled difference +0.02, versus -0.06 for the dark-channel prior), and a Beer-Lambert fit explains 0.4% of its variance. The effect of the module also changes sign with degradation severity between datasets. The benefit thus comes from a physics-shaped inductive bias, not from physics. We further show that single-run ablations can reverse sign and document implementation defects that invalidate loss ablations.

---


### 123. [Analyzing and Mitigating Poisoning Attacks on Flow-Based Intrusion Detection](https://arxiv.org/abs/2610.19766)

**<font color=#1a73e8>作者：</font>** Florian Spelter, Johannes F. Loevenich, Tobias Hürten 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Although Artificial Intelligence (AI)-based Intrusion Detection Systems (IDSs) are increasingly deployed in operational networks, their dependence on large-scale training data introduces a critical vulnerability to stealthy poisoning attacks. We demonstrate that latent backdoors can be successfully implanted in flow-based IDS models by poisoning as little as 0.001% of the training data, maintaining near-nominal performance on clean inputs while ensuring high attack success rates. To address this threat, we propose a diagnostic-first methodology that localizes trigger-relevant features through constrained perturbation analysis and detects poisoning-induced behavioral drift by comparison with a distilled baseline model. The proposed methodology further enables targeted mitigation via automated data sanitization or neuron pruning. Our findings expose the operational risks of near-undetectable backdoors and provide a scalable approach to analyzing, quantifying, and mitigating backdoor exposure in AI-based IDS.

---


### 124. [Learning to Compute Is Not Learning to Retain or Reuse in Looped Transformers](https://arxiv.org/abs/2610.19768)

**<font color=#1a73e8>作者：</font>** Peilong Zhou, Hongtao Zhang, Yulong Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped transformers compute by applying one block repeatedly, so they can run for more loops than they were trained with. Recurrent reasoners are known to overthink: iterating past the trained depth can turn a correct answer into a wrong one. Such a late error can reflect failed computation, loss of retention, or a state that later computation cannot reuse. We separate these cases in in-context Mealy-machine execution, where a simulator supplies intermediate targets and exact counterfactuals for hidden-state interventions. Models trained to answer at loop 32 are fully correct there but keep only 22% of these answers at loop 64. Retention depends on what training asks for: supervising one randomly chosen position per example, instead of always the last, keeps 99.8%, and randomizing the number of training loops also helps; truncating gradients, as in progressive training against overthinking, does not. The computation itself is exact: position $k$ is computed at loop $k$, and swapping its loop-$k$ hidden vector for the one from another input redirects every later position to that input's exact continuation (237/237 pairs in each of ten models). Retention, however, is not reuse. Even in models that keep nearly all answers, holding each position $k$ fixed from loop $k$ drops accuracy to 4--6%, whereas holding it from loop $k+4$ is harmless. A released recurrent maze network trained to avoid overthinking behaves the same way. Learning to compute is thus not learning to retain, and avoiding overthinking does not make a state reusable when its answer first appears.

---


### 125. [From Global to Tail Convergence: Dynamics of $α$-Stable Score-Based Generative Models](https://arxiv.org/abs/2610.19773)

**<font color=#1a73e8>作者：</font>** Ianis Hammani, Claire Boyer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Score-based generative models driven by $\alpha$-stable L{é}vy processes have been proposed as an alternative to Brownian diffusion models, with empirical evidence suggesting improved sampling and better modeling of heavy-tailed data. Yet theoretical guarantees for these models remain limited. We develop a non-asymptotic convergence analysis for scale-preserving $\alpha$-stable generative dynamics, covering both compactly supported and power-law targets. In p-Wasserstein distance, we quantify the effects of early stopping, initialization, score approximation, and time discretization, and show exponential decay of the initialization error. A comparison with Brownian dynamics reveals that global Wasserstein convergence alone does not fundamentally distinguish the two models: both initialization errors decay exponentially with the forward horizon on the common class of heavy-tailed targets. A sharp separation emerges instead in the tails. At any positive generation time, stable dynamics produces power-law tails with index $\alpha$, whereas Brownian dynamics remains light-tailed. For a target with tail index $\nu$, asymptotically correct extreme-quantile scaling is possible precisely when $\alpha$=$\nu$. These results identify tail-index matching as a principled mechanism behind the ability of stable generative models to capture extreme events.

---


### 126. [LabOPBench: A Multimodal Benchmark for Evidence-Grounded Laboratory Decision Making](https://arxiv.org/abs/2610.19780)

**<font color=#1a73e8>作者：</font>** Jingyuan Li, Yujie Liu, Yijie Dai 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Laboratory experiments involve more than following predefined protocols; they require adaptive decision-making as the experimental state changes. Existing scientific benchmarks rarely assess such evidence-based decisions in laboratory settings. Here we present LabOPBench, a multimodal benchmark of 756 expert-authored, independently reviewed questions in organic synthesis and materials science. Each item pairs laboratory evidence with procedural context and an open-ended judgment, evaluated using a question-specific scoring rubric. Eight multimodal models obtain overall normalized scores of 28.8-45.8%, leaving substantial room for improvement. On a controlled 100-question subset, the strongest models outperform undergraduate participants on average but remain below the average performance of PhD participants. Expert analysis of responses from the three leading models identifies Evidence Misreading and Evidence-Decision Conflict as the dominant error patterns. These results reveal that current models still struggle to turn multimodal perception into reliable laboratory decision-making.

---


### 127. [Learning Who Benefits Most: Multi-Treatment Causal Ranking for Population Health Stratification](https://arxiv.org/abs/2610.19782)

**<font color=#1a73e8>作者：</font>** Rocco Zaccagnino, Martina Girolamo, Alberto Lombardi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Population health stratification frameworks, such as the Italian DM77, organize patients by clinical need and care pathways but offer limited guidance on which care changes to prioritize under constrained resources.
We present PROMETHEUS (Proactive Resource Optimization through Multi-treatment Effect-based Targeting in Healthcare Environments Using Stratification), a framework that formulates population health stratification as a multi-treatment causal ranking problem. Its objective is to order eligible patient-treatment opportunities by expected incremental benefit rather than obtain perfectly calibrated individual treatment-effect estimates.
Each clinically admissible care intensification is compared with maintaining the patient's current pathway. Treatments are learned jointly to produce a globally comparable ranking across patients and care profiles, within domains sharing a reference condition, outcome, follow-up horizon, and benefit scale. This separates clinical need, treatment benefit, and resource-constrained allocation.
PROMETHEUS combines doubly robust causal signals with a Siamese neural ranking model and contrastive representation pretraining. The shared representation captures similarities across care transitions, supporting prioritization under capacity constraints.
Synthetic experiments and semi-synthetic experiments using real administrative covariates from ASL Benevento evaluate ranking quality, allocation value, robustness, and failure modes. The results support the framework's ability to recover generated benefit orderings and prioritize care opportunities in the evaluated settings. PROMETHEUS provides a preclinical approach to actionable stratification; validation with observed treatment-outcome data is required before clinical use.

---


### 128. [Reinforcement Learning via Advantage Guidance](https://arxiv.org/abs/2610.19783)

**<font color=#1a73e8>作者：</font>** Zhiyuan Zhou, Sergey Levine  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) holds the promise of learning a policy that can outperform what is shown in the data. However, in practice, such systems suffer from instability and hyperparameter sensitivity. In contrast, supervised learning provides a stable and scalable training objective, but is fundamentally limited by the quality of the demonstrated behavior. In this paper, we ask whether we can perform policy optimization with something as simple and stable as supervised learning but as performant as RL. Unfortunately, naively training the policy with supervised learning and conditioning on future rewards or advantages typically underperform dedicated RL methods. We introduce a new policy extraction method, Advantage Guidance, that retains the simple supervised learning structure with advantage conditioning while outperforming prior RL methods through effective conditional training and contrastive diffusion guidance during sampling. We show that Advantage Guidance can significantly improve a model's ability to respond to conditional advantage signals, and the contrastive guidance during sampling can use the learned advantage-conditioned policy to target the KL-regularized optimal policy. Empirically, we find that Advantage Guidance significantly outperforms prior state-of-the-art RL methods on 26 long-horizon, sparse reward tasks across datasets with varying degrees of optimality.

---


### 129. [FPV-CRASH: A Dataset for Offline Crash Moment Localization in Drone First-Person-View Videos](https://arxiv.org/abs/2610.19785)

**<font color=#1a73e8>作者：</font>** Jifan Zhang, Tingyu Wang, Qian Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Crash Moment Localization aims to localize the major physical impact that interrupts controlled flight in an onboard first-person-view (FPV) video recorded by a drone, thereby providing a temporal reference for retrospective crash analysis in aerial robotics. However, existing crash-video datasets predominantly target surveillance or dash-camera footage, and their annotation schemes and task formulations are not designed for temporal localization of the major physical impact in UAV onboard FPV videos. To address this gap, we present FPV-CRASH, a dataset and fixed-protocol reference evaluation for offline Crash Moment Localization in drone FPV videos. FPV-CRASH contains 1,052 drone FPV clips (526 Crash and 526 Normal); each Crash clip has a single-frame reference annotation for the Crash Moment, and every clip is paired with four English captions automatically generated from sampled frames and the known Crash/Normal label. Normal clips carry no timestamp target and provide training-time background supervision. The captions support an auxiliary Text-to-Video Retrieval task, whereas localization inference remains video-only. We further provide a heatmap-based reference model that estimates a continuous Crash Moment timestamp from sparsely sampled frames. Under the fixed, non-source-disjoint clip-level protocol, the reference model reduces MAE from 1.12 s for the strongest fixed timing-prior baseline to 0.56 s (a 50% relative reduction) and achieves a median absolute error (MedAE) of 0.33 s; the fraction of clips localized within 0.5 s rises from 37.14% to 65.71%. The release includes annotations, available source video identifiers and URLs, clipping metadata, fixed split lists, and preprocessing code so that the reportable portion can be reconstructed without redistributing source footage. At submission time, all source-compilation URLs remained accessible.

---


### 130. [LiFi: LiDAR Generation from Multi-View Images via Geometric and Semantic Collaborative Guidance](https://arxiv.org/abs/2610.19786)

**<font color=#1a73e8>作者：</font>** Sizhuo Zhou, Xiaosong Jia, Fanrui Zhang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating LiDAR point clouds from multi-view camera images is a valuable task with applications in controllable data synthesis, cross-modal simulation and various perception tasks. However, most existing methods are not specifically designed for this task, and the quality of their generated LiDAR remains limited. Moreover, these methods typically focus only on semantic cues in images or generate LiDAR from a monocular camera image. In this work, we introduce LiFi (LiDAR From images), a dedicated framework for generating visually and geometrically aligned LiDAR scenes from multi-view camera images. LiFi guides the latent diffusion process through two complementary branches: geometry and semantics. The geometry branch constructs scene features from images through a reverse sampling algorithm and an uncertainty-aware geometric encoder combined with DepthAnything3, whereas the semantic branch provides high-level semantic representations via a cross-view interaction module. We further introduce a dual-branch balanced classifier-free guidance (CFG) strategy, which enhances the model's conditional generation capability while preserving the independent learning and collaborative controllability of the two branches. Extensive experiments demonstrate that LiFi outperforms state-of-the-art methods in generating high-fidelity LiDAR scenes. The code will be publicly available at: this https URL.

---


### 131. [One Agent per Zone: Decentralised Active Inference under Partial Observability for Multi-Zone HVAC Control on Edge Hardware](https://arxiv.org/abs/2610.19790)

**<font color=#1a73e8>作者：</font>** Panagiotis Kasnesis, Lazaros Toumanidis, Christos Chatzigeorgiou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-zone HVAC control is a shared-resource problem: zones on a floor share one fan and cooling coil, so each zone's demand affects its neighbours and the building's peak power. One controller per zone scales well and isolates faults, but each controller then observes only its own zone, not the shared air loop. In this work, we present a decentralised controller that assigns each zone an independent active-inference agent, which plans by minimising expected free energy and learns its zone dynamics online. The agents exchange no messages, so none depends on peers or a coordinator; each accounts for the unobserved coupling through a latent disturbance and a congestion signal derived from the metered power of the other floors. Fifteen agents are evaluated in EnergyPlus on a Sinergym office building against three rule-based controllers and three MADDPG fleets, one given the same floor meters. On five noisy weather years unseen during training, the fleet attains the lowest mean building peak (88.3 kW, 3 to 17 % below the baselines) and staggers the floor peaks better than any baseline, with a coincidence factor (building peak over the sum of the floor peaks) of 0.929 versus 0.936 to 0.994. Compared with a reactive rule at similar comfort (0.912 versus 0.916), it lowers the sum of monthly peaks, on which demand charges are billed, by 33 kW (4 %) in every year, at the cost of about 10 % more energy. It costs 9% less per year than the proactive rule (at lower comfort) and 1% less than the MADDPG fleet given the same floor meters, in every test year. The whole fleet runs on a single low-cost Raspberry Pi 5, closing the observation-to-action loop over MQTT in 442 ms at p95, far below the 15-minute control step.

---


### 132. [JetSpec++: Foresight Parallel Drafting with Self Refinements](https://arxiv.org/abs/2610.19792)

**<font color=#1a73e8>作者：</font>** Zhaoxiang Feng, Lanxiang Hu, Haoran Yuan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding's effectiveness is governed by two quantities: the acceptance rate of drafted tokens and the cost of producing them. We show the two objectives can be co-optimized with algorithm-system co-design, and present JetSpec++, which retains a strong learned draft model while hiding its cost almost entirely. JetSpec++ combines three components: intra-block self refinement, which trains the draft model to iteratively correct its own parallel predictions within a block of tokens; inter-block foresight drafting, which begins the next block before the current one is verified; and pipelined drafting and verification, which overlaps the two stages so drafting's marginal wall-clock cost approaches zero. In comparison with state-of-the-art speculative decoding methods, JetSpec++ attains a wall-clock speedup of up to $7.45\times$ over autoregressive (AR) decoding and $1.54\times$ over DSpark, with up to 1,361 tokens per second for a single request on GB200, and an average acceptance length of 8.94 across seven benchmarks, while preserving the target model's output distribution. Our code and models are available at this https URL.

---


### 133. [Asymptotically Exact Negative Guidance of Diffusion Models via Positive-Unlabeled Learning](https://arxiv.org/abs/2610.19802)

**<font color=#1a73e8>作者：</font>** Hirohane Takagi, Masashi Sugiyama  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Negative guidance of diffusion models generates samples that avoid an undesired condition, specified either by reference samples or by a conditional score alongside an unconditional model. Existing methods inject repulsive terms derived from local information at each sample, so the resulting sampler does not target an explicit density, and its bias cannot be systematically reduced by increasing computation. We instead present a negative-guidance method that samples from an explicit target density, which uniformly handles both reference-sample and score-based specifications and suppresses probability mass near the undesired condition with an avoidance strength that parametrizes the target density itself. Realizing this target requires estimating, at each diffusion timestep, how likely each sample is to belong to the undesired condition. We cast this estimation as a Positive-Unlabeled learning problem that admits lightweight online training along the diffusion trajectory, using condition samples as positives and diffusion particles as unlabeled data. Because the guided particles drift from the unconditional marginal, we further correct the residual mismatch via Sequential Monte Carlo, yielding a sampler that is asymptotically exact in the particle limit and that turns any existing negative-guidance method into its proposal kernel. Empirically, our method approaches the ground-truth target on Gaussian mixtures and Pareto-dominates existing methods on trade-offs between avoidance and generation quality, distributional bias, and diversity, including in an image-generation setting with a pretrained score network.

---


### 134. [Improving Category-Aware Active Domain Adaptation via Uncertainty-Guided Region Coverage](https://arxiv.org/abs/2610.19803)

**<font color=#1a73e8>作者：</font>** My Tra Nguyen Huynh, Viet Cuong Ta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Active domain adaptation researches focus on alleviating the annotation cost, which comprises source data and target data labelling, as well as enhancing the performance of unsupervised domain adaptation. However, optimizing the adaptation model based on the average accuracy can lead to the drop in performance of some difficult categories. To overcome this issue, a point-wise selection strategy built upon the influence function can be used to improve domain adaptation performance. In our work, we first address the sensitive and redundant aspects of point-wise selection, which can lead to overfitting of the acquisition function. We thus introduce a region-based approach that ensures the improvement of the adaptation model by maximizing a positive manifold coverage. An uncertainty score is further introduced to the selection mechanism to learn a better decision boundary for the target domain. In comprehensive experiments, our proposed method surpasses the first category-aware active domain adaptation baseline as well as existing active domain adaptation methods across multiple domain adaptation benchmarks. Our implementation is available at: this https URL IS NEXT.

---


### 135. [Adaptive and Proximal Federated Optimization for Transferable Network Intrusion Detection](https://arxiv.org/abs/2610.19808)

**<font color=#1a73e8>作者：</font>** Rezwan Islam Salvi, MD Rafin Jawad Hafiz, Abeer Mahmood Kalam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Network Intrusion Detection Systems (NIDS) based on deep learning often fail to detect attack classes that are absent from training data, limiting their robustness against zero-day threats. This property called transferability across attack classes, remains underexplored especially in federated learning (FL) settings where data heterogeneity and client drift pose additional challenges. Prior work (TabFIDS) showed that FedAvg combined with bootstrapping and temporal averaging improves transferability for cross-device NIDS. In this paper, we explore whether other federated optimizers can do better. We compare two optimizers inspired by FedAdam and FedProx against the FedAvg baseline on the CIC-IDS 2017 dataset using an 11-client federated setup, sweep 10 hyperparameter configurations, and contrast two data-balancing strategies: bootstrapping and SMOTE. Using the count of client pairs whose transferred-model accuracy exceeds 70% as our primary metric (following TabFIDS), the proximal optimizer with a strong regularization term yields 48 transferable pairs versus 42 for FedAvg, while the adaptive optimizer with an aggressive server learning rate yields 46 pairs. SMOTE improves per-pair accuracy over bootstrapping but reduces breadth, revealing a depth-vs-breadth trade-off: high accuracy on a few client pairs versus moderate accuracy across most. These results indicate that the choice of federated optimizer, the rule by which client updates are regularized and aggregated into the global model, is very important for federated NIDS.

---


### 136. [VaryST: Generalizable Spatio-Temporal Forecasting Beyond the Closed-World Setting](https://arxiv.org/abs/2610.19813)

**<font color=#1a73e8>作者：</font>** Shengnan Guo, Jinjun Cheng, Xiaowei Mao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal forecasting is fundamental to many real-world systems, yet deployment environments are inherently varying: temporal distributions may evolve, spatial domains may change, and observation availability may shift from training conditions. Existing models are often tightly coupled to their training environments through node-specific representations, predefined spatial support sets, and reliance on consistently available observations, limiting generalization to changing environments. To this end, we propose VaryST, a compact spatio-temporal forecasting model trained from scratch that achieves strong generalization by dynamically constructing predictive context from available long-term observations. To accommodate temporal changes, VaryST derives node representations from long-term histories, capturing current behavior in the context of longer-term patterns. To adapt to spatial changes, it dynamically selects functionally relevant support nodes beyond predefined neighborhoods and integrates their information with recent and long-term target states and global context. To handle varying observation availability, VaryST selectively masks historical patches on which the model relies most during training, encouraging it to exploit alternative temporal and spatial dependencies for accurate forecasting when key observations become unavailable. Extensive experiments on six real-world datasets against seventeen baselines show that VaryST achieves strong in-domain forecasting accuracy, substantially improves zero- and few-shot generalization under spatial and temporal changes, and remains robust to varying observation availability.

---


### 137. [CTIA-ODE: Continuous-Time Inter-Variable Attention for Long-Term Time Series Forecasting](https://arxiv.org/abs/2610.19831)

**<font color=#1a73e8>作者：</font>** Chengyi Pan, Huangqimei Zheng, Hao Xue  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Although multivariate time series forecasting has broad application prospects, effectively incorporating exogenous variables remains challenging. Prevailing discrete-time architectures often impose rigid temporal alignment across heterogeneous variables, which may limit their ability to capture continuously evolving external effects. To address this limitation, we introduce CTIA-ODE, a continuous-time forecasting framework centered on Continuous-Time Inter-Variable Attention (CTIA). Specifically, CTIA is embedded within an ordinary differential equation (ODE) solver, enabling the continuously evolving endogenous trajectory to dynamically query a static exogenous context along the integration path without requiring explicit temporal alignment. To improve the stability of the continuous latent dynamics, we further introduce a dual-stabilization strategy: architecturally, a Linear Residual Augmentation (LRA) module provides a macroscopic trend anchor, while an Outlier-Robust Hybrid Loss (ORHL) mitigates the influence of heavy-tailed anomalies during optimization. Extensive experiments across eight real-world datasets demonstrate that CTIA-ODE achieves state-of-the-art forecasting performance across diverse datasets and prediction horizons, while maintaining a favorable accuracy-efficiency trade-off with a compact memory footprint and low inference latency, particularly under long-horizon forecasting settings. Anonymous code is available at this https URL.

---


### 138. [Teaching Agents in their Own Style: Blackbox Teacher Distillation for Web Agents](https://arxiv.org/abs/2610.19834)

**<font color=#1a73e8>作者：</font>** Md Farhan Ishmam, Kenneth Marino  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier web agents using closed models have high inference and computational costs. Smaller open models can be an alternative, but to be performant, they require training supervision from a human or teacher model. Token-level teacher distillation is not an option for closed teachers as it needs access to the model's logits. The standard approach is to imitate teacher demonstrations offline, but it trains the student on states it has never visited, and in a style it does not write in. We introduce WebKD, where the teacher is the editor of the student's failures. Given a failed episode, the teacher finds the first point of mistake, and rewrites the student's reasoning traces, harness states, and actions from that point onward. The editing reveals that the teacher's corrections can be more surprising to the student than the student's own text. WebKD instead aims to edit minimally. In the data space, the teacher writes each correction in the student's style. In the objective space, the reasoning is weighted by its contribution to the action. A role-asymmetric KL anchor allows the corrected action to move freely while keeping the reasoning near the student's prior. On the TimeWarp benchmark, WebKD students gain about 5.5-10.7 pp over behavior cloning, outcome-reward RL, and teacher editing baselines. The performance transfers to unseen versions and to the live web in the OnlineMind2Web benchmark. WebKD opens a new way of distilling black-box models to improve the capabilities of open-weight web agents.

---


### 139. [VisibilitySplat: Ray-Traced Occlusion for Relighting with 3D Gaussian Splatting](https://arxiv.org/abs/2610.19847)

**<font color=#1a73e8>作者：</font>** Sven Kluge, Oliver Staadt  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address inverse rendering with 3D Gaussian Splatting (3DGS) by introducing explicit visibility modeling for relighting as well as material and light decomposition. Our approach augments the standard rasterized 3DGS pipeline with a sparse visibility oracle that estimates transmittance-weighted occlusion for Gaussian primitives from sampled lighting directions. This oracle is implemented using a point-based ray tracer accelerated by a bounding volume hierarchy (BVH) and queried sparsely within the inverse-rendering objectives, while the original 3DGS loop is retained for training efficiency, interactive visualization, and tooling compatibility. Shading follows a physically based rendering (PBR) formulation with a principled microfacet bidirectional reflectance distribution function (BRDF) and low-resolution high-dynamic-range (HDR) environment maps. We evaluate our method on the TensoIR synthetic dataset against baselines based on neural radiance fields (NeRFs), tensor representations, and 3DGS. The results show competitive performance and improvements over several earlier baselines for novel-view synthesis (NVS), albedo reconstruction, and relighting. Ablations indicate that explicit visibility modeling is an important contributor to relighting and material-illumination disentanglement, while pure PBR supervision can favor appearance fitting in NVS. Overall, the findings suggest that sparse, point-based visibility queries effectively complement rasterized splatting for inverse rendering while preserving the practical advantages of the 3DGS ecosystem.

---


### 140. [DeltaStreamer: Towards Human-Like Agentic Streaming Video Understanding](https://arxiv.org/abs/2610.19849)

**<font color=#1a73e8>作者：</font>** Boyuan Sun, Deshui Miao, Wenzhao Gao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose DeltaStreamer, a novel agentic framework for streaming video understanding inspired by how humans observe, remember, and investigate. Streaming video understanding requires a system to retain evidence before knowing which details future queries will need. Existing approaches often obscure event transitions and omit relevant details when compressing video history, and cannot recover missing visual evidence. DeltaStreamer addresses these limitations by combining change-aware memory with query-driven planning and targeted evidence gathering with replay. Before a query arrives, it continuously observes the stream and explicitly records visual changes in structured memory, preserving how events unfold rather than only what is present. When a query arrives, a query-driven planner identifies the required evidence and guides memory retrieval and targeted replay. By revisiting historical frames, the agent can recover visual details omitted during observation and ground its answer in evidence beyond the retained descriptions. This connects continuous observation with active investigation tailored to each question. Experiments on OVO-Bench and StreamingBench demonstrate improvements over representative streaming video understanding methods, with overall scores of 66.07% and 59.53%, respectively.
Project page: this https URL

---


### 141. [Lost in the Fallback: How Reliably Do Typed Decision Models Use Fallback Options?](https://arxiv.org/abs/2610.19856)

**<font color=#1a73e8>作者：</font>** Yuanbo Xie, Mingli Zhu, Tianyun Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Typed decision models (TDMs) are increasingly used in applications such as request routing and model selection, making reliable decisions critical to system performance. Fallback options accommodate categories outside regular choices, enabling deferral to human experts or more capable models. While recent works have examined adversarial vulnerabilities in TDMs, their ability to follow fallback rules in non-adversarial settings remains underexplored. We introduce the Paired Fallback Robustness (PFR) Test to evaluate two aspects of fallback reliability: whether models correctly switch between regular and fallback options, and whether they make consistent decisions under logically equivalent definitions of the same rule. We evaluate open-source decision models on three benchmarks, with controlled comparisons across architectures and parameter counts. We find that correct recognition does not reliably transfer to correct fallback options, and errors persist even when the correct category is explicitly this http URL, logically equivalent formulations of the same fallback rule can also produce substantial disagreement in model decisions. These findings reveal a crucial reliability gap in current TDMs: fallback mechanisms designed to improve reliability can instead introduce errors. It highlights faithful execution of fallback rules and consistency under equivalent definitions as essential requirements for reliable typed decision-making.

---


### 142. [OmniPoser: Flexible Human Motion Recovery in the Wild with Masked Flow Matching](https://arxiv.org/abs/2610.19857)

**<font color=#1a73e8>作者：</font>** Minghao Liu, Tutian Tang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering 3D human motion from sparse wearable sensors is challenging due to the inherent noise, occlusion, and instability of real-world tracking signals. Existing approaches are restricted to fixed sensor configurations and, when built on diffusion models, are computationally prohibitive for real-time deployment. We propose OmniPoser, a universal framework that recovers full-body SMPL motion from a flexible combination of heterogeneous inputs, such as 3D keypoints, sparse IMU rotations, head-mounted 6-DoF poses, or any subset thereof, within a single model. OmniPoser introduces a cross-modal masking mechanism paired with a Masked Conditioning Encoder, enabling one architecture to incorporate diverse sensor configurations through a masked design. A decoupled dual-stream generative backbone generates complete motion via Conditional Flow Matching, requiring only a single ODE integration step at inference. Across three settings and seven benchmarks, including in-the-wild Nymeria and Ego-Exo4D datasets, OmniPoser performs on par with state-of-the-art methods while running at over 700 FPS. The project page is available at this https URL.

---


### 143. [SPARS: A Stability-Plasticity-Aware Region Selection Framework for Continual Learning](https://arxiv.org/abs/2610.19876)

**<font color=#1a73e8>作者：</font>** Teif Aldaajani, Huda Hakami, Maha A. Thafar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning aims to acquire new knowledge while retaining previously learned knowledge. However, updating shared parameters when learning new tasks often overwrites existing knowledge, causing catastrophic forgetting. Memory replay methods mitigate catastrophic forgetting but rely on previous samples, raising privacy, memory, and scalability concerns. On the other hand, parameter isolation-based methods preserve learned knowledge but may limit knowledge transfer, whereas regularization promotes adaptability but remains susceptible to interference between old and new tasks. To maintain the stability-plasticity trade-off, this paper proposes Stability-Plasticity-Aware Region Selection (SPARS), a replay-free hybrid framework combining global parameter isolation with localized parameter regularization. SPARS estimates parameter importance using either the Fisher Information Matrix (FIM) or a novel Confidence Score (CS) estimator that leverages logit sensitivity and achieves comparable performance to FIM without requiring labelled data. Based on parameter importance, SPARS partitions parameters into three importance-aware regions namely, winning, neighboring, and non-important parameter regions. Each region receives a different adaptation strategy: selective freezing, soft regularization, or unrestricted learning based on its role in the stability-plasticity trade-off. To mitigate classifier bias in class-incremental learning, we employ Quadratic Discriminant Analysis to improve performance on previously learned classes .Experiments on CIFAR-10 and TinyImageNet demonstrate consistent improvement in average incremental accuracy over existing isolation- and regularization-based methods across task- and class-incremental learning. On TinyImageNet, SPARS achieves the best performance with 6% improvement for class-incremental learning while retaining over 60% of parameters for future tasks.

---


### 144. [Neural Wasserstein Splines: Representation-Invariant Second-Order Priors for Trajectory Inference](https://arxiv.org/abs/2610.19878)

**<font color=#1a73e8>作者：</font>** Amartya Banerjee, Harlin Lee, Caroline Moosmüller  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Population dynamics are often observed only as unpaired snapshots, which leave the evolution between measurements underdetermined. Second-order regularization can constrain it, but a penalty on the accelerations of sampled particles is a prior on joint particle paths, and different particle representations of the same marginal curve can have different acceleration costs. We therefore introduce Neural Wasserstein Splines (NWSP), a sample-based method that learns a continuous population curve under a Wasserstein smoothness prior. A neural network maps latent variables to the control points of a cubic spline in time, so samples at any time come from the spline basis without numerical integration. We project the generator's velocity onto gradients of a finite dictionary of scalar potentials and differentiate this measure-dependent projection in time, obtaining a finite-dimensional surrogate for the intrinsic Wasserstein acceleration, trained jointly with distributional fit losses. For a fixed dictionary and ridge parameter, we prove that the population penalty depends only on the marginal curve and bound its sensitivity to moment-estimation errors. Learned potentials (NWSP-N) sharpen acceleration estimates. On various synthetic and single-cell benchmarks, NWSP is highly competitive with transport and flow-based methods, ranking in the top two in 11 of 16 settings. The penalty improves on an unregularized spline in 13 of 16 settings and, while competitive with a particle-acceleration penalty, adds provable representation invariance.

---


### 145. [CoDy: Codec Dynamics as Complementary Priors for Unsupervised Temporal Action Localization](https://arxiv.org/abs/2610.19880)

**<font color=#1a73e8>作者：</font>** Tianyu Yan, Qingyi Yang, Qin Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised temporal action localization (UTAL) aims to identify action categories and localize their temporal boundaries without annotation supervision. Existing methods typically derive supervision for both tasks solely from RGB and optical-flow representations, often resulting in noisy category assignments and inaccurate temporal boundaries. In this work, we reveal an overlooked property of video codecs: group-of-pictures quantization patterns preserve category-discriminative dynamics, while motion-vector and residual variations exhibit pronounced responses around action transitions. Based on this insight, we propose CoDy, a codec dynamics-guided framework that exploits the codec as complementary information to the visual view for UTAL. CoDy integrates a codec-enhanced view with RGB and flow through confidence-aware consensus clustering, producing reliable soft pseudo-labels. It further converts codec dynamics into a class-agnostic boundary prior, which supervises visual boundary learning and guides proposal initialization and iterative refinement. The codec branches are only used during the training stage and introduce no extra codec-side computation at inference. Extensive experiments on THUMOS14 and ActivityNet v1.3 demonstrate that CoDy consistently outperforms existing UTAL methods and achieves state-of-the-art localization performance. These results establish codec signals as effective annotation-free priors for jointly inferring which actions occur and when they occur.

---


### 146. [Occupancy Modeling via Drifting: One-Step Generation Enables Direct Policy Extraction](https://arxiv.org/abs/2610.19883)

**<font color=#1a73e8>作者：</font>** Robin Uhrich, Marco Bagatella, Núria Armengol Urpí 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The growing interest in behavior foundation models, combined with recent advancements in generative modeling, has led to an appealing recipe for reinforcement learning from unlabeled data: pre-train a generative model to model occupancies, i.e., discounted state visitations, on reward-free trajectories, such that a policy can be easily extracted once a small reward-labeled dataset becomes available. We decompose this recipe along three axes: (i) the degree to which the multi-modal structure of occupancies must be captured, (ii) the class of generative model, and (iii) the method used for policy extraction. Along each axis, we consider existing choices, propose simpler alternatives, and validate each decision experimentally. This analysis culminates in a novel, streamlined method that leverages drifting, a modern one-step generative sampler, to model the occupancy. We show that this enables policy extraction via direct differentiation through the occupancy model, and bypasses the need for critic distillation. Overall, we observe that this nimble setup leads to improvements in performance on standard benchmarks.

---


### 147. [Bilinear Compressive Security with Finitely Many Samples](https://arxiv.org/abs/2610.19898)

**<font color=#1a73e8>作者：</font>** Axel Flinth, Semira Einsele, Matilda Kylberg 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Bilinear Compressive Security (BCS) is a lightweight encryption scheme that combines compressed sensing with a fresh random convolution filter to improve resistance against key-recovery attacks under key reuse. Previous work derived information-theoretic guarantees for BCS by relating key identifiability to phase retrieval under the assumption that an adversary has access to the full ciphertext distribution induced by the random filter. In practice, however, an adversary only observes finitely many encryptions, leaving the security of BCS in the finite-sample regime largely unexplored.
In this paper, we study key recovery from only finitely many observations. We first develop a covariance-based attack that estimates the linear measurements from repeated encryptions of the same plaintext and subsequently recovers the secret measurement matrix. We analyze the estimation procedure and derive finite-sample guarantees together with corresponding sample-complexity bounds. We further investigate the complete attack experimentally and compare its observed recovery behavior with the previously established information-theoretic identifiability results.
Our experiments show two qualitatively different recovery regimes on the structure of the measurement matrix. For dense matrices, including Gaussian matrices, the number of measurements required for successful recovery appears to grow linearly with the signal dimension. This differs from the worst-case behavior suggested by information theory. In contrast, for matrices with sparse rows, we observe a quadratic growth consistent with the theoretical bound.
These results suggest that the sparsity structure of the measurement matrix plays an important role in the security of BCS and should be taken into account when selecting parameters and designing practical instances of the scheme.

---


### 148. [Universal Sample-Based Embeddings of Higher-Order Objects](https://arxiv.org/abs/2610.19899)

**<font color=#1a73e8>作者：</font>** Radovan Haluška, Christopher Solinas, Nathan R. Sturtevant 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks operate naturally on finite-dimensional vectors, yet many problems require reasoning about higher-order objects such as distributions, functions, and graphs. Such objects capture relationships within a ground set and rarely admit an explicit compact representation. Moreover, we typically want a compact representation not of a single higher-order object but of an entire family of such objects, including members unseen during training. While a few approaches exist for particular object types, none is designed to work across object types. We propose a unified framework that represents any higher-order object as a fixed-size embedding vector learned over a family of such objects. An encoder maps an object, seen only through a finite set of samples, to an embedding, and a domain-specific decoder supplies the training signal by modeling the object conditioned on that embedding. Since the encoder works only from samples, one architecture serves different object types. Because the decoder is a model already suited to single instances of the object type, the framework inherits that model's native operations and inductive biases. We instantiate the framework on distributions, functions, and graphs. In each case we show that a single trained model represents an entire family and generalizes to members unseen during training. Furthermore, we demonstrate the downstream utility of these embeddings: interpolating distributions in embedding space, solving differential equations in embedding space, and predicting unseen edges from a graph's embedding.

---


### 149. [CARD: Closing the Teacher-Student Loop for Adversarial Robustness Distillation](https://arxiv.org/abs/2610.19911)

**<font color=#1a73e8>作者：</font>** Zhi Li, Haowei Liu, Hongchen Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial robustness distillation typically treats a robust teacher as a fixed knowledge source and transfers robustness to a compact student in a one-way manner. This paradigm terminates teacher-student interaction once the student is distilled, thereby discarding potentially useful feedback from the distilled student. However, exploiting such feedback is nontrivial because indiscriminate weak-to-strong transfer may propagate student errors to the teacher. To address this issue, we propose Cyclic Adversarial Robustness Distillation (CARD), a closed-loop framework that turns the distilled student into a feedback source for refining the robust teacher and subsequently transfers the teacher gains back to the same student. CARD first performs strong-to-weak adversarial distillation and then uses reliability-enhanced student feedback to refine the robust teacher. The refinement combines inverse adversarial student feedback with teacher-student discrepancy maximization, after which the refined teacher is used to continue training the same student under the unchanged base distillation objective. We further establish a sample-level sufficient condition for reliable weak-to-strong feedback transfer and derive a distribution-level upper bound on the refined teacher's risk. Experiments on CIFAR-10, CIFAR-100, and TinyImageNet-10 across multiple teacher-student architectures and base distillation methods show that CARD improves adversarial robustness in most evaluated settings while generally preserving clean accuracy. These results show that the distilled student can provide useful feedback to the teacher, enabling robustness transfer to proceed beyond the conventional one-way teacher-to-student paradigm.

---


### 150. [Quantifying Annotation Agreement in Object Detection with Optimal Transport](https://arxiv.org/abs/2610.19912)

**<font color=#1a73e8>作者：</font>** Kirill Prokhorov, Alexandr A. Kalinin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable validation of machine learning models is a crucial step in designing robust and trustworthy systems. Yet validation relies on annotated test sets treated as ground truth, even though annotations can be noisy or ambiguous. In object detection, sources may disagree on object presence, box location, or class label. Standard agreement metrics usually binarize box overlap before computing a summary score, obscuring the degree and structure of disagreement between annotation sets. Here, we study an Optimal Transport (OT)-based metric for measuring agreement between object detection annotations. Instead of binarizing bounding box overlap, this metric assigns graded costs to matched and unmatched labeled boxes. Through theoretical analysis and experiments on real and synthetically perturbed annotations, we show that OT captures graded changes in agreement and distinguishes annotation pairs that thresholded metrics score identically. Our results suggest that OT provides a richer measure of annotation agreement in object detection, especially for domains with many small or ambiguous objects. Such agreement estimates can support more reliable validation when labels are noisy or conflicting.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-264](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
