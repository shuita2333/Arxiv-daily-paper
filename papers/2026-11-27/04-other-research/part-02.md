# 📦 其他研究 | 2026年11月27日

> 本类共 **314** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-314](./part-07.md)

---

### 51. [Recovering What Matters, Transferring Only What Is Reliable: Toward Precise Reference-Based Super-Resolution](https://arxiv.org/abs/2611.33455)

**<font color=#1a73e8>作者：</font>** Sihan Ji, Wenxin Chen, Yue Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference-based super-resolution (RefSR) aims to recover missing details from high-quality references. However, existing methods face two fundamental challenges. First, perceptual plausibility does not guarantee content fidelity. Existing methods often produce visually convincing details without faithfully recovering reference-specific information, such as text, codes, and identity cues. Second, faithful reference reading does not guarantee reliable information transfer. Increasing reference utilization also exposes the restoration process to misleading content, as global semantic relevance does not necessarily imply local correspondence consistency. To address these challenges, we propose PreciseRef, a reference-aware generative framework for faithful and reliable RefSR. At its core, Asymmetric Twin-Attention (ATA) allows target and reference images to participate in a unified attention space while the reference keeps its own shape. By letting their image tokens interact directly through joint attention, ATA facilitates fine-grained reference information retrieval without explicit image alignment. To ensure reliable information transfer, we introduce Dual-Scale Reference Gating (DRG), which combines Semantic Relevance Gating (SRG) to filter globally irrelevant reference context and Bidirectional Consistency Gating (BCG) to suppress unreliable local correspondences. Furthermore, we establish VeriRef, a benchmark evaluating exact reference-dependent content recovery and robustness to mismatched references. Extensive experiments show that our method achieves 85.6% character accuracy and 76.3% exact code decoding, compared with 17.4% and 0% for existing methods, while effectively suppressing erroneous reference transfer. It also achieves state-of-the-art perceptual quality on CUFED5 and WR-SR.

---


### 52. [Fast Muscle-Driven Whole-Body Motion Tracking with a Differentiable World Model](https://arxiv.org/abs/2611.33460)

**<font color=#1a73e8>作者：</font>** Kaibo He, Maciej Bakowicz, Shihe Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tracking motion capture with a whole-body musculoskeletal model means coordinating hundreds of muscles through contact, and current controllers take hours to days of GPU time to train, so every tuning decision is expensive. SuperMimic trains a tracking policy by backpropagating through the rollouts of a learned world model. We extend it to MS-Human-700 (700 muscles) and MyoFullBody (354 muscles), with MuJoCo's activation dynamics inside the world model. To make its training fast, our recipe takes the speedups developed for the Unitree G1, replaces three of their settings that fail on muscles, and adds four changes of our own: observations without muscle geometry, data collection concurrent with the updates, Beta exploration noise that keeps every excitation in $[0,1]$, and 50 Hz control. On one RTX 5090 it trains MS-Human-700 in 6.3 minutes to the held-out return that SuperMimic's published hyperparameters reach in 3.9 hours, 37$\times$ sooner, and in 20 minutes to lower tracking errors than theirs after 10 hours. It trains MyoFullBody 34$\times$ sooner without retuning. Ablations show what is specific to muscles: a higher policy learning rate stalls half of the runs, and clipped Gaussian noise adds a tonic co-contraction that Beta noise avoids. Finally, refining the policy's actions through the world model at test time lowers the position error by a further 26% with no held-out clip failing, and reaches the same return after 5.1 instead of 6.3 minutes of training. Code, the training recipe and videos are on the project page this https URL.

---


### 53. [FoamSurf: A Voronoi-Surfel Representation for Differentiable Rendering](https://arxiv.org/abs/2611.33462)

**<font color=#1a73e8>作者：</font>** Grzegorz Wilczyński, Julia Farganus, Krzysztof Byrski 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scenes inside a scattering medium contain solid surfaces, such as the seabed or rocks, and a semi-transparent medium, such as water, fog, or smoke. Recent Gaussian-based methods produce realistic images of scenes in scattering media, but traces of the medium can remain visible in surface-only renders. Neural fields separate surfaces and medium more accurately, but they are slow to train and difficult to edit. Both approaches evaluate the medium only along camera rays, so its effects along reflected and refracted rays are not modeled. These limitations prevent reliable surface recovery, independent editing of surfaces and the medium, and consistent rendering of inserted objects. We present FoamSurf, a hybrid representation that models surfaces with planar Gaussian surfels and the medium with space-filling Voronoi cells. A single differentiable ray tracer composites both along arbitrary rays, while training priors keep them separate without segmentation masks. Across real underwater scenes, synthetic scenes, and dense fog, FoamSurf achieves image quality on par with the state of the art and the most accurate surface-medium separation among the compared methods. The recovered components can be removed, edited, or stylized independently, and the same reconstruction supports inserted mesh objects with attenuation and scattering along both direct and reflected or refracted rays. Together, these capabilities enable scene restoration, editing, and composition within a single reconstructed model.
Project page: this https URL

---


### 54. [OrdiHand-GS: Ordinal-Guided Tracking and Hand-Refined Gaussian Avatars for Digital Signers](https://arxiv.org/abs/2611.33465)

**<font color=#1a73e8>作者：</font>** Mingxuan Ma, Ronglai Zuo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital signers, also known as signing avatars, convey sign language through animated virtual humans, where visual fidelity and linguistic intelligibility hinge primarily on the hands. When one hand crosses over the other, two failure modes dominate. First, monocular expressive-human tracking suffers from ordinal depth ambiguity: either hand can satisfy the same 2D landmarks, and the baseline tracker orders wrists at chance level on 365 annotated overlapping frames from How2Sign. Second, hand appearance remains blurred in neural rendering even after geometry is corrected. We propose OrdiHand-GS to address these errors separately. Relative depth from a video depth estimator and apparent hand size vote, with confidence weighting and abstention, for a front-back relation, which enters expressive-human tracking as a hinge on median hand-surface depth. A source-conditioned residual head then refines the local positions of hand-associated UV Gaussians with the avatar backbone and renderer frozen. We instantiate the framework with GUAVA. Against matched unconstrained refinement, wrist-order accuracy rises from 32.9% to 77.3% at a cost of 0.39 pixels of reprojection error, while a random-sign placebo gives no balanced-accuracy gain. A 2x2 factorial evaluation attributes most of the interaction-rendering improvement to tracking-stage refinement, with a smaller additional benefit from the residual.

---


### 55. [SplatWAM: Splatting World Action Models for Real-Time 3D Imagination](https://arxiv.org/abs/2611.33467)

**<font color=#1a73e8>作者：</font>** Frank Tsu-Fang Lu, Karthik Sundar Senthilkumar, Christopher Thirgood 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World models typically predict future observations in pixel or latent space, limiting their ability to directly represent true 3D scene evolution. We present SplatWAM (Splatting World Action Model), a generative world model that learns action-conditioned dynamics directly over compact 3D Gaussian primitives. A tokenizer SplatWAM-T first encodes a variable number of unposed views into a fixed budget of Gaussian tokens. A dynamics model SplatWAM-D then predicts future Gaussian states in a single forward pass per action, using log-Euclidean covariance coordinates and differentiable rendering supervision to facilitate learning in an explicit 3D space. Each predicted state can be rasterized from arbitrary viewpoints, enforcing a shared 3D representation across views by construction. On OGBench Scene, SplatWAM renders novel views 12x faster than video world models (~80 FPS on an RTX 5090) with up to 2.0 dB higher PSNR. We further introduce SplatWAM-P, a lightweight flow-matching policy head jointly trained with the dynamics model. Across 8 task suites, model-free Gaussian-token policies outperform pixel-based counterparts by up to 24.8 percentage points. SplatWAM-P improves over Latent Particle World Model (LPWM) by 12 percentage points and matches HIQL without a learned value function. On LIBERO, our ~1B model outperforms WorldVLA (~7B) and the robot-pretrained OpenVLA (~7B), while matching OpenVLA-OFT when both are trained without large-scale robot pretraining. Code and checkpoints will be released.

---


### 56. [Differentially Private Policy Optimization in Linear MDPs with Adversarial Rewards](https://arxiv.org/abs/2611.33469)

**<font color=#1a73e8>作者：</font>** Yi He  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) in personalized services often relies on sensitive interaction data. Motivated by the need to protect these data, we study differentially private (DP) policy optimization in episodic linear Markov decision processes (MDPs) with unknown transitions and adaptive adversarial linear rewards under full-information feedback. This setting poses two key challenges: past trajectories are repeatedly reused for policy evaluation, and reward choices may depend on previously released private statistics. The proposed algorithm combines batched proximal policy optimization (PPO) updates with optimistic policy evaluation, using private regression statistics and reward estimates to protect both trajectories and reward functions under joint differential privacy (JDP). With all other parameters fixed, our high-probability regret bound retains the same leading $\widetilde{O}\left(K^{3/4}\right)$ dependence on the number of episodes $K$ as the corresponding non-private bound for batched optimistic PPO. The additional privacy terms scale as $\widetilde{O} \left(K^{5/8}\right)$ and $\widetilde{O} \left(K^{1/2}\right)$. Thus, privacy incurs only lower-order additive costs in $K$, even under adaptive adversarial rewards.

---


### 57. [Memory as the Backbone: A Dual-Store Associative Memory Architecture for Visual Recognition](https://arxiv.org/abs/2611.33475)

**<font color=#1a73e8>作者：</font>** Ruizhi Wang, Xiangtao Wang, Bayar Menzat 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We investigate whether explicit memory can serve as the organizing principle of a general-purpose visual backbone. Inspired by the interaction between working and long-term memory in human cognition, we introduce DuSAM (Dual-Store Associative Memory), a hierarchical memory-native visual backbone coupling image-local working memory (WM) with a fixed-capacity persistent semantic memory (PM). WM organizes local visual evidence into compact, spatially anchored states that are updated and transported across stages, then read back to refine dense features. PM consolidates semantic evidence from training images and annotated regions into prototypes, whose retrieved content enriches the same working states. With these memory operations in place of self-attention or state-space blocks, DuSAM achieves competitive performance relative to representative, similarly sized backbones on ImageNet-1K classification, ADE20K semantic segmentation, and COCO object detection and instance segmentation. Ablations show contributions from both stores, with PM particularly benefiting class groups with fewer annotated training pixels. At $2048\times2048$, the complete DuSAM-based UPerNet segmentor achieves $2.36\times$ the throughput of the evaluated DeiT-S/16 counterpart while using $59.5\%$ less GPU memory, and $1.24\times$ the throughput of the linear-complexity VMamba-T. Memory analyses reveal spatially selective WM access and semantic associations between retrieved prototypes and training regions. Class-targeted removal and restoration further demonstrate that category-specific experience can be replenished through state updates without changing network parameters. These results establish explicit memory as a viable organizing principle for visual backbones and provide a foundation for jointly designing contextual computation and addressable semantic memory.

---


### 58. [The Geometry Is the Memory: Task-Density Routing for Continual LoRA](https://arxiv.org/abs/2611.33487)

**<font color=#1a73e8>作者：</font>** Alireza Heidari, Thomas Veasey, Mariano Tepper  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Freezing older adapters does not ensure that a continual learner will select and use them properly at inference time. When multiple adapters exist, routing among them and identifying the adapter whose representation space matches the query's answer can be difficult. We propose CONTLORA, which replaces stored examples with compact class statistics for adapter selection and classification. Gaussian class models in a frozen representation select LoRA adapters, while accumulated feature moments exactly recover a class-balanced ridge classifier for fixed training features. Trained without retaining images or feature vectors, CONTLORA reaches 88.55% accuracy on 20-task CIFAR-100 and 86.99% on CUB-200. Across three benchmarks in the matched component study, its mean final accuracy differs from an independently trained stored-feature counterpart by at most 0.07 percentage points. Ablations show that improved task coverage need not improve classification and adapter composition also matters. On held-out classes, competitor-centered likelihood scores improve novelty AUROC over raw likelihood without altering routing ranks. These results support statistical memory as an alternative to example-retention approaches in the evaluated settings, while identifying task ambiguity as an ongoing limitation.

---


### 59. [A 3D Simulator for Passive SPAD Imaging](https://arxiv.org/abs/2611.33498)

**<font color=#1a73e8>作者：</font>** Elia Mergaert, Rong Zou, Roberto Pellerito 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Passive single-photon avalanche diode (SPAD) cameras provide short-exposure observations for low-light perception, but collecting task annotations for these sensors remains difficult, and annotated datasets are scarce. We present a 3D simulation pipeline that generates realistic photon detections together with camera-motion and semantic labels, enabling perception models to be trained on synthetic SPAD observations and applied directly to real-world data. The pipeline couples controllable scene geometry and motion with a sensor-informed observation model that accounts for photon shot noise, dark counts, and spatial crosstalk. We evaluate the pipeline through calibrated photon-count comparisons and zero-shot sim-to-real transfer across three downstream perception tasks. We show that classifiers trained only on synthetic SPAD data achieve high accuracy on real low-light recordings at illumination levels less than 2 lux, without real-data fine-tuning. Similarly, we apply models trained entirely on simulated camera sweeps to real-world camera-rotation estimation and achieve mean absolute rotation errors of less than 1 degree on real 20-degree and 30-degree sweeps at 0.5 and 5.0 lux, when deployed zero-shot. We additionally train semantic segmentation models on synthetic data with automatically generated dense labels and perform direct inference on real-world low-light recordings; the results further demonstrate the usefulness of synthetic dense supervision for real low-light perception. Our simulator thus provides a practical source of annotated training data for real SPAD perception.

---


### 60. [Separating Environment and Sensor Shift from Acquisition Protocol in Physical Vision Benchmarks](https://arxiv.org/abs/2611.33507)

**<font color=#1a73e8>作者：</font>** Yuyang Yuan, Jason Wu, Mohammadali Khodabandehlou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In real-world deployments, vision systems must operate under varying environmental conditions, such as illumination changes. Recent work has explored adaptive sensing strategies that select camera parameters according to the current environment and downstream task to improve task performance. Reliable physical benchmarks are therefore essential for evaluating such strategies. We study ImageNet-ES-Diverse, a physical benchmark that evaluates the adaptive exposure control strategy Lens by recapturing printed ImageNet images under varying illumination conditions. We construct four controlled acquisition pipelines that vary printed-image scale and camera zoom, and conduct a pilot study with directly captured physical objects. We find that the acquisition choices substantially change benchmark difficulty on all downstream baselines. Moreover, the average classification-accuracy advantage of Lens over auto exposure observed on the original benchmark does not persist in either our collected pipelines or real-object pilot study. Oracle exposure selection nevertheless retains substantial gains, indicating remaining potential for sensor control. These findings highlight acquisition protocol as an important factor in physical benchmark evaluation and motivate explicit protocol reporting and evaluation across multiple acquisition setups when assessing adaptive-sensing benefits.

---


### 61. [Merkle Trees Minimize Verifier Complexity in the ROM](https://arxiv.org/abs/2611.33508)

**<font color=#1a73e8>作者：</font>** Miranda Christ, Oliver Korten, Tal Malkin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Nearly five decades after their introduction, Merkle trees remain the most efficient hash-based vector commitments. They compress a vector $x \in \{0,1\}^n$ into a commitment whose size is independent of $n$, such that a verifier can open any bit $x_i$ using $\log n$ hash evaluations. The security of the scheme (intractability of finding two distinct openings for a given bit using the same commitment) follows from the collision resistance of the hash function. The verifier's runtime complexity is a bottleneck in many key applications of vector commitments, including SNARKs, credentials, and authenticated dictionaries. As such, a longstanding open question has been whether it is possible to construct hash-based vector commitments where the verifier makes a sublogarithmic number of hash evaluations.
We prove that sublogarithmic verifier complexity is impossible to achieve through black-box use of a hash function; we not only rule out constructions from collision resistant hash functions, but in fact show that commitment schemes with sublogarithmic verifier complexity are unachievable in the random oracle model. In particular, any vector commitment with deterministic verifiers has verifier query complexity $\Omega_{\theta}(\log n)$, where $\theta$ is the input length of the random oracle. This bound is matched up to constant factors by high-arity Merkle trees. The key technical lemma in our proof is a disjoint product lemma, which can be viewed as a computational analog of the van den Berg-Kesten-Reimer (BKR) inequality. We believe this lemma is of independent interest, and in particular may be useful for showing other lower bounds and separations in the random oracle model.

---


### 62. [ArtLang-4D: Articulation-Aware Dynamic Language Fields from Monocular Videos](https://arxiv.org/abs/2611.33511)

**<font color=#1a73e8>作者：</font>** Sylvia Yuan, Dan Wang, Ravi Ramamoorthi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language that describes an articulated object is often about its state: the drawer pulled out the furthest, the door opened halfway, push the drawer all the way in. Existing 3D language fields attach one feature to each point and cannot tell these descriptions apart, and 4D language fields condition on video time, which has no kinematic meaning and cannot be set by a user. We present ArtLang-4D, which reconstructs an articulated object from a single monocular RGB-D video and equips it with a dynamic language field indexed by articulation time t, the normalized state of its joints, instead of video time. The geometry is a canonical triangle field whose triangles follow typed screw joints, discovered from the video without any joint initialization. The language field is supervised by a t-tagged caption bank that describes each part with comparative state phrases in a whitened open-vocabulary text space. A free-form query is answered by maximizing part relevance jointly over parts and states, which returns both the part and the articulation state it describes; a command is then executed by moving only that part along its recovered joint. On the 100 objects of Articulate-100, ArtLang-4D recovers more accurate joints and part geometry than reconstruction and articulation baselines, retrieves the queried state far more reliably than a state-agnostic language field, and executes language commands with lower motion error.

---


### 63. [Learning to Reason in Real-Time](https://arxiv.org/abs/2611.33513)

**<font color=#1a73e8>作者：</font>** Xavier Schneider, Benjamin Schneider, Sun Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents that operate in the real world must reason correctly and on-time, yet they currently do not account for how time should alter their reasoning. Modern agents learn to do tasks in environments that are entirely synchronous: where the world waits for the agent to act before changing. A real-time environment, by contrast, changes independent of the agent. Existing approaches try to bridge this gap by imposing a ratio of thinking to acting. However, for an agent to succeed in real-time it must learn to act quickly when delay is costly and to reason longer when the benefit outweighs the missed opportunities. To this end, we introduce real-time reasoning training (RRT) as the class of training techniques for real-time reasoning agents. We develop three standard RRT techniques: (1) using real-time data, (2) decoupling acting and observing, and (3) curriculum learning in time. Together, these simple techniques substantially outperform strong baselines. Across time pressures, we outperform the strongest non-RRT baseline by an average of 33% reward on in-distribution and 55% reward on out-of-distribution tasks in two real-time environments: Frogger and Snake. These results demonstrate that we can teach agents to balance reasoning and responsiveness under real-time constraints, and that RRT opens a broad, new set of capabilities for real-time agents.

---


### 64. [A Perturbation-Driven Framework for Sensitivity Analysis of Dimensionality Reduction](https://arxiv.org/abs/2611.33523)

**<font color=#1a73e8>作者：</font>** Md Afridi Hasan, Jaemin Jo, Takanori Fujiwara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-dimensional representations produced by dimensionality reduction (DR) are commonly evaluated using distortion measures such as trustworthiness and continuity. In this paper, we study the sensitivity of DR methods to plausible input variations by quantifying changes in structural preservation and visually diagnosing how these changes manifest in the resulting representations. This perspective reflects the fact that real-world datasets are finite, noisy samples of an underlying distribution, and DR should not produce substantially different structures under small data changes. We introduce a model-agnostic, perturbation-driven sensitivity evaluation framework that treats perturbations as controlled probes of plausible data variation. Across multiple perturbation families and strength levels, we repeatedly perturb the input, apply a DR method, and evaluate the resulting low-dimensional representations using a set of distortion measures to derive sensitivity profiles for each DR method. We demonstrate the utility of our framework through case studies on DR method comparison, behavior analysis, and robustness improvement. We find that methods performing well according to conventional distortion measures (e.g., t-SNE) can still exhibit substantial sensitivity, leading to instability in visually salient structures such as trajectories and clusters, while certain methods (e.g., multidimensional scaling) may exhibit improved structural preservation under specific perturbations. These results highlight the importance of sensitivity analysis for comparing DR methods, diagnosing perturbation-sensitive visual patterns, and guiding the development of more robust DR methods toward trustworthy visual analytics.

---


### 65. [Casper: A Projection-Based Neurosymbolic Layer for Scalable & Guaranteed Constraint Satisfaction](https://arxiv.org/abs/2611.33527)

**<font color=#1a73e8>作者：</font>** Lohith Konathala, Luca Andolfi, Eleonora Giunchiglia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many real-world problems demand exact constraint satisfaction to be meaningfully solved, yet existing neurosymbolic methods face a stark trade-off: those that guarantee satisfaction fail to scale, while those that scale must resort to approximation. Meanwhile, traditional deep learning approaches offer no satisfaction guarantees at all. In this paper, we propose Casper, a neurosymbolic layer that simultaneously (i) guarantees constraint satisfaction, (ii) scales at inference time, (iii) is fully automated, requiring no problem-specific engineering, and (iv) is fully differentiable, making it composable with any neural predictor both at training and at inference time. Casper casts constraint satisfaction as a closed-form Euclidean projection onto the constraint-feasible region, computable in a single forward pass. Experiments across MNIST arithmetic (up to 1024 digits), Sudoku solving, and Warcraft pathfinding show that Casper is the only method that produces guaranteed-valid outputs at scale: on $30\times30$ Warcraft grids, exact baselines time out and approximate ones produce valid paths less than 7% of the time, while Casper produces them 100% of the time.

---


### 66. [Frame geometry, fascicle extrapolation and leaderboard overfitting in muscle ultrasound](https://arxiv.org/abs/2611.33539)

**<font color=#1a73e8>作者：</font>** Soheil Kooklan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated readings of pennation angle, fascicle length and muscle thickness from B-mode ultrasound depend on the geometry of the stored frame and on how fascicles that leave the image are extended, and challenge entries add settings chosen on a small public leaderboard. This study measures all three in one entry of the UMUD Challenge, which scored 309 frames from six screen layouts, 103 on a public and 206 on a private leaderboard. The pipeline applies layout-specific values of scale and pixel aspect, resamples each frame to square pixels, segments aponeuroses and fascicle fragments with U-Nets and measures the three readings geometrically; the submitted entry blended its angle and length with public notebooks. Because the score is additive, 65 single-change contrasts from 13 base entries measured each decision on both splits. The primary selected entry scored 0.27608 on the private split, the 69th reported position of 690 teams. Reading every frame with square pixels cost 0.029 public and 0.037 private. Of 20 late-stage corrections, 9 kept the sign of their effect on the private split. An audit of the UMUD expert benchmark found that 26 of its 35 frames share their tissue with training images of both DL_Track_US and the challenge. On the 9 frames with no detected match in either set or orientation, the recipe scored 0.213, two experts against two others 0.218 and DL_Track_US 0.263 (0.209, 0.196 and 0.259 when both raters of a reference pair are required), with no difference established. Frame geometry and the extension rule moved readings as much as the choice of model, and small corrections tuned on about 100 public frames did not carry over.

---


### 67. [PeerReveal: Learning to Generalize in AI Peer Review Detection](https://arxiv.org/abs/2611.33555)

**<font color=#1a73e8>作者：</font>** Zi Li, André V. Duarte, Lei Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can we distinguish fully AI-generated reviews from those using AI only to rewrite human judgement? Furthermore, can we do so reliably when reviews are generated from diverse AI models and workflows across scientific domains? To this end, we introduce PeerReveal, a new detector that grounds its decisions in learned relationships between a review's claims and reference claims drawn from AI-generated reviews of the same paper, complemented by review-level textual signals. We evaluate PeerReveal on PeerShift, a new, challenging test set of 5,430 reviews spanning multiple domains, including machine learning, life sciences, and social sciences, combining variation in disciplinary review conventions with diverse AI review-production mechanisms. With regular training, PeerReveal achieves 70.52% pooled Macro-F1 on this benchmark, improving over the strongest baseline by 11.48 points. We develop an effective and practical adversarial training framework that further improves the detector's generalization using a small local generator optimized to produce challenging reviews, raising pooled Macro-F1 from 70.52% to 82.40%. These results show that robust AI-review detection benefits from richer review-level evidence and adversarial training on more challenging generation processes.

---


### 68. [DiffER$^2$: Diffusion Ensembles for Retrosynthesis Prediction with SMILES Adapted Particle Guidance](https://arxiv.org/abs/2611.33557)

**<font color=#1a73e8>作者：</font>** Sean Current, Daniel Adu-Ampratwum, Xia Ning 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computational retrosynthesis prediction has the potential to reduce development time for newly discovered drugs by automatically generating potential reactions for a target product. Data-driven approaches commonly treat this as a sequence-to-sequence generation task on SMILES strings. In this work, we construct ensembles of discrete-time and continuous-time diffusion models for molecular generation and incorporate guidance mechanisms for improved output diversity. We propose an adaptation of particle guidance to SMILES sequence generation which significantly improves the number of unique molecules generated by diffusion ensembles while increasing top-k accuracy. These results further expand the efficacy of discrete diffusion for SMILES generation, and our empirical analyses offer new insights into the capabilities of diffusion models for chemical retrosynthesis.

---


### 69. [EgoCARBS: Egocentric Video Meets Active Acoustics for Kitchen Action Understanding](https://arxiv.org/abs/2611.33565)

**<font color=#1a73e8>作者：</font>** Saif Mahmud, Vineet Parikh, Bharath Hariharan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric video records what a person looks at, but often misses what their body does: the hands leave the frame, and arm motion goes unseen. An exocentric camera recovers this context, but it must be installed wherever the activity happens. Active acoustic sensing can recover it from the wearables themselves: a device's speaker emits inaudible chirps, and its microphone senses the motion of the hands, arms, and nearby objects from their echoes. Yet no public dataset pairs it with egocentric video. We present EgoCARBS, with two deliverables. The first is a multimodal dataset and benchmark: 15 participants cook unscripted meals in their own kitchens wearing camera glasses and an off-the-shelf smartwatch that both sense with active acoustics, synchronized with egocentric and exocentric video and the watch's audio and IMU, with 4,019 verb-noun action annotations in 11.4 hours. The second is a study of what the wearables add to egocentric video. On verb recognition, they add at least as much as an exocentric camera for participants seen in training, and even more for new participants, for whom the exocentric camera does not help. Active acoustics alone provides most of this gain, and helps most where the camera does not see the hands. Trimmed action recognition, detection, and anticipation remain open. We will release the data, our data collection and annotation tools, and pre-trained models.

---


### 70. [ProPolar: Progressive Polar Decomposition for Implicit Neural Representations](https://arxiv.org/abs/2611.33567)

**<font color=#1a73e8>作者：</font>** Pureum Kim, Younggeon Ryu, Dongyoon Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit neural representations (INRs) capture global low-frequency structure during the early stage of training and then refine localized high-frequency details, afterwards. However, standard optimizers are agnostic to the coarse-to-fine learning behavior of INRs. Such optimizers accumulate a gradient matrix in momentum buffer and retain components misaligned with the dominant low-frequency directions in the early stage. We propose a progressively growing rank scheduler and a rank-aware learning-rate scheduler for enhancing a subspace-based momentum optimization, where a momentum matrix is updated within a low-rank subspace. The rank schedule expands the subspace during training, and the scheduler holds the peak learning rate through rank growth so that the added subspace contributes to fine-detail recovery. Experiments on image fitting, single-image super-resolution (SISR), and neural radiance field optimization show that the proposed method improves convergence and peak reconstruction quality over competitive optimizers. The largest gains appear in the high-frequency refinement stage, mirroring the coarse-to-fine progression that the rank schedule targets. A significant study on hyperparameter optimization (HPO) on NeRF further confirms that these gains persist under matched search budgets.

---


### 71. [Trigger-Invariant Contrastive Unlearning for Backdoor Removal](https://arxiv.org/abs/2611.33571)

**<font color=#1a73e8>作者：</font>** Santosh Chapagain, Shah Muhammad Hamdi, Soukaina Filali Boubrahimi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Backdoor attacks pose a severe threat to modern NLP models by embedding hidden triggers that induce malicious behavior at inference time. Recent unlearning methods such as gradient ascent (GA) attempt to remove backdoors by maximizing the loss on poisoned samples; however, these methods can suffer from a critical limitation: they may shift the trigger's influence to other classes rather than eliminating it. In this work, we propose Trigger-Invariant Contrastive Unlearning (TICU), a framework for mitigating textual backdoor behavior by enforcing prediction and representation invariance to trigger insertion. TICU constructs clean and trigger-inserted counterfactual pairs, then fine-tunes the model so that both inputs produce consistent output distributions and aligned hidden representations. To preserve clean-task performance, TICU also retains the supervised classification loss on clean data and constrains parameter drift from the original model. Extensive experiments across multiple datasets, model architectures, and attack settings show that TICU improves triggered accuracy and reduces trigger-induced prediction shifts compared with existing baselines, while maintaining competitive label-flipping performance and limiting clean-task degradation.

---


### 72. [DoseSteer: Steering diffusion-based dose prediction models towards clinical targets via Dual-Response Guidance](https://arxiv.org/abs/2611.33577)

**<font color=#1a73e8>作者：</font>** Shupeng Cheng, Jing Jia, Jincheng Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI dose-prediction models generate patient-specific 3D dose distributions from patient anatomy. Yet these predictions can still miss structure-level clinical dose targets. Once deployed, most existing predictors offer no direct mechanism to correct such deviations, deferring target enforcement to downstream plan optimization. We introduce DoseSteer, an inference-time framework that steers frozen diffusion-based dose prediction models towards specified clinical targets without retraining. To meet clinical targets while preserving overall dose prediction quality, we propose Dual-Response Guidance (DRG), a structure-centric algorithm that probes the model's responses to perturbations in each structure's noisy dose and context and jointly solves for per-structure steering strengths. Across five dataset-model configurations spanning three diffusion architectures and three datasets, DRG outperforms 12 training-free baselines under identical reference-derived target proxies, removing at least 97% of the target error, reducing the official dose error by 7.8% on average, and improving dose fidelity outside the steered structures. DoseSteer reconciles learned anatomical dose priors with explicit structure-level targets at test time, establishing a principled, training-free mechanism to refine AI dose predictions prior to plan optimization. Code is available at this https URL.

---


### 73. [Evaluating Strategies for Multimodal Bidirectional Interactions between Pedestrians and AVs](https://arxiv.org/abs/2611.33581)

**<font color=#1a73e8>作者：</font>** André Clérigo, Maximilian Schrapel, Pedro Rito 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Autonomous Vehicles (AVs) share spaces with Vulnerable Road Users (VRUs) in encounters where driver cues are absent. This can leave people uncertain whether the vehicle has noticed them and understood their request. Existing research has studied how AVs communicate with pedestrians through external human-machine interfaces. This work investigates bidirectional multimodal VRU-AV interactions combining Augmented Reality (AR), speech, and gestures. The study follows four stages: literature synthesis of interactions, a survey with 124 participants, interaction loop implementation, and feasibility evaluation. Participants preferred AR cues that made vehicle motion or warnings explicit, high-level voice commands, and conventional gestures. Prototype measurements revealed a trade-off between faster local processing and more accurate infrastructure-assisted processing. The demonstration shows bidirectional interaction using AR wearables and vehicular communications, while leaving decision-making to the AV. Together, the results support treating AV-VRU interaction as a closed loop of intent expression, recognition, vehicle decision, and feedback.

---


### 74. [VivaWorld: Long-Horizon Video World Model With Compositional 3D Priors](https://arxiv.org/abs/2611.33591)

**<font color=#1a73e8>作者：</font>** Ying Jiang, Donglai Xiang, Anita Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon video generation is key to interactive world modeling, physical intelligence, and spatial reasoning, yet maintaining geometric consistency and accurate camera control remains challenging without 3D grounding. We introduce \textbf{VivaWorld}, a framework for generating geometry- and view-consistent long videos from an image. We first construct a compositional hybrid 3D representation that combines reconstructed point clouds, which preserve observed scene geometry and appearance, with generated textured meshes, which provide complete object geometry across $360^\circ$ novel views. We also introduce a connected-region filter removing inconsistent floating components for robust cross-view reconstruction and propose a hybrid camera embedding that combines global and object-anchored Plücker rays to capture both scene-level camera motion and camera-object relationships, and inject it together with the visual guidance into a video generation model via a control adapter. Extensive experiments show VivaWorld achieves state-of-the-art visual quality and camera control, while supporting controllable novel-view synthesis, long-horizon scene exploration, and physical AI. Project page is available at: this https URL

---


### 75. [Aligned Machine: A Benchmark for Evaluating Multimodal Embedding Similarity via Human Comparative Judgements](https://arxiv.org/abs/2611.33594)

**<font color=#1a73e8>作者：</font>** Jiechen Li, Hannah Groos, Brinnae Bent  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embedding models increasingly inform how people search, recommend, and retrieve information, yet we lack credible ways to test whether these similarity judgments reflect how humans understand meaning. Existing benchmarks typically rely on static, expert-labeled pairs with coarse Likert-style annotations, limiting scalability and making it difficult to obtain consistent, high-confidence annotations. We introduce Aligned Machine, an interactive, public-facing platform that transforms broad participation into a continuously growing Human-Aligned Similarity Benchmark (HASB) for evaluating semantic alignment in embedding-based systems. Participants complete a cognitively-natural, forced-choice task, comparing two pairs of items (text or images) and selecting which pair is more similar. This comparative design is accessible to non-experts, yields clean preference data, and supports robust aggregation. We report results from an initial deployment with 115 participants contributing 2,875 total labeled pairs and 872 unique pairs. Using HASB, we evaluated 12 widely used embedding models and found only partial alignment between embedding similarity and human judgments. Text-only models consistently achieve higher overall agreement than multimodal models, while multimodal performance varies systematically by task type: alignment is strongest for image-image comparisons, weaker for image-text comparisons, and lowest for text-text comparisons. Aligned Machine is designed to evolve over time as participation grows, supporting longitudinal analysis, domain-specific studies, bias detection, and measurement of concept drift across model versions. By combining accessible public participation with rigorous comparative evaluation, HASB provides a scalable and accountable framework for auditing semantic alignment in embedding models.

---


### 76. [Small Leaks Sink Great Ships: Automated Analysis of Protocols That Tolerate Low-Entropy Keys](https://arxiv.org/abs/2611.33595)

**<font color=#1a73e8>作者：</font>** Yongkang Xiao, Jing Chen, Min Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern cryptographic protocols such as WPA2-PSK, Bluetooth Low Energy (BLE), and Bluetooth Classic (BC) tolerate low-entropy keys for user-friendliness, backward compatibility, or resource-constrained deployment, yet existing symbolic protocol verifiers rely on the perfect-encryption assumption and therefore cannot reason about brute-force attackers. Prior work addresses this gap only through protocol-specific, manually encoded reveal rules, which neither generalize across protocols nor systematically explore compound-key decomposition. We introduce the first protocol-agnostic, automated symbolic methodology for low-entropy keys, built on three abstractions: the message-derivation fact MDerive, which captures brute-force prerequisites independently of concrete function symbols; a three-tier breaking-oracle design (value-breaking, relationship-breaking, message-derivation) that composes with the standard Dolev-Yao attacker; and a graded bit-level attacker model that bounds the key length an attacker is allowed to exhaust. We realize the methodology as EntropyVerif, a syntax-sugar extension of Tamarin that requires no kernel modification. Using EntropyVerif we automatically rediscover the PMKID, KNOB, and Method Confusion attacks, and uncover a new attack on BC which we call the Unilateral Multi-Downgrade (UMD) attack: by repeatedly downgrading one side of a BC session and recombining the recovered key fragments, an attacker reduces session-key recovery against devices using the maximum 128-bit key from $2^{128}$ to $n \cdot 2^{128/n}$, bottoming out at $2^{12}$ for $n=16$---a factor of $2^{116}$ reduction that has been responsibly disclosed to the Bluetooth SIG. Across three real-world protocols and six BC device configurations, our results show that entropy-aware symbolic analysis is both feasible and necessary.

---


### 77. [Controllable CAD Generation and Interactive Editing of Fluid Rotors](https://arxiv.org/abs/2611.33617)

**<font color=#1a73e8>作者：</font>** Shen Chen, Lei Li, Jiajun Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-aided design (CAD) provides the geometric foundation for rotors in fluid rotating machinery. However, creating models for different rotors requires different modeling processes, making it difficult to control geometry through design intent and reuse existing models. We introduce VaneCraft, an agent-driven framework for rotor generation, inverse recovery, and editing through a unified analytical representation. The agent interprets design requests and invokes geometric modeling operations. The representation defines geometric controls through meridional geometry and independent boundary angle laws. An anisotropic partial differential equation (PDE) maps these controls to the blade surfaces. Geometric parameter correction (GPC) uses a joint geometric encoder and a parameter decoder to refine controls initialized from rotor category and dimensions. Inverse recovery maps existing CAD to the same geometric controls for reconstruction and continued editing. Experiments demonstrate that VaneCraft supports anisotropy control and parameter editing and outperforms representative baselines in rotor CAD generation tasks. Project page is available on \href{this https URL}{GitHub}.

---


### 78. [Before They Were Cool: Do Early Fans Abandon Artists Who Suddenly Become Popular? Evidence from Online Music Listening](https://arxiv.org/abs/2611.33619)

**<font color=#1a73e8>作者：</font>** Zihan Chen, Lei Nico Zheng, Di Zhu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Identity-signalling theory, echoed in the hipster's "I liked them before they were cool", expects an artist's first fans to pull away once the artist becomes popular, by leaving or by avoiding what the newcomers play. A rival account expects the event that brings the crowd to renew existing listeners' attention to the artist. We test both in the this http URL listening histories of 594,415 users (21.1 billion plays, 2005-2013), where every play appears on the user's profile. Study 1 detects 78 crowd arrivals: months in which the number of people discovering an artist tripled without a new album, single or EP, for example after a song appeared in a film. Study 2 compares Grammy and Mercury Prize winners with nominees who won nothing. We compare listeners who had played the artist before the crowd arrived (early fans) with early fans of comparison artists. Early fans did not withdraw. Those still listening stopped less often (25.8% vs. 29.1% over six months), and those who had drifted away returned more often (29.6% vs. 25.0%). Those who kept listening converged on the crowd: the song most newcomers played took a larger share of their plays, with no turn to deep cuts. More lapsed fans returned after larger surges, and neither fans with the most distinctive tastes nor fans facing a more mainstream crowd quit more. Award wins brought few new listeners and no clear change. Where listening is displayed by default, early fans moved towards the crowd after sudden popularity, not away from it.

---


### 79. [Welfare-Enhancing Mechanism Design for Agent Ecosystems](https://arxiv.org/abs/2611.33627)

**<font color=#1a73e8>作者：</font>** Zitian Guo, Chen Xu, Beibei Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The emerging Agentic Web forms a multi-agent ecosystem: a decentralized service market where the user agent selects which content agents to query from their submitted profiles, before seeing any documents. Profiles therefore become a new target of optimization. Existing Generative Engine Optimization studies how a single supplier rewrites documents the engine can already retrieve, to improve their citation. In the Agentic Web, multiple content agents optimize profiles to compete for limited opportunities to deliver documents. To study this repeated interaction, we build WildRegistry, a simulation framework and benchmark based on a real agentic-search request stream, and model it as a dynamic game under private monitoring. Long-horizon experiments show that this competition lowers website-selection quality and settles at a harmful stable point, which our empirical criterion identifies as an approximate rewriting equilibrium. We therefore design a welfare-enhancing mechanism, DEC (Delivery-Evidence Credit), a platform-side policy that uses recorded delivery outcomes to reallocate later opportunities and reduce information asymmetry. DEC improves this endpoint, raising website-selection quality while preserving most of providers' exposure gains, for a Welfare Gain of +2.01 points and a healthier long-horizon outcome. More broadly, our findings highlight the importance of mechanism design in agent ecosystems: turning recorded delivery outcomes into evidence that endogenously shapes later user-agent selection and content-agent adaptation can steer long-horizon adaptation toward delivered capabilities.

---


### 80. [What Is Redundant at High Resolution? Efficient Attention and Feed-Forward Design for All-in-One Image Restoration](https://arxiv.org/abs/2611.33636)

**<font color=#1a73e8>作者：</font>** Dongheon Lee, DongJae Lee, Sewhan Chun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-scale architectures are widely adopted in all-in-one image restoration (AIO-IR) to capture larger-scale context at low-resolution stages and refine details at high-resolution (HR) stages. However, processing spatially large feature maps at HR stages incurs substantial computational costs and memory traffic, making efficient HR processing challenging. To address this challenge, we propose High-resolution Global-Local Restoration (HiGLR), an efficient multi-scale AIO-IR network grounded in an analysis of spatial redundancy in self-attention and convolutional feed-forward networks (ConvFFNs). Specifically, this analysis identifies three key redundancies: per-query readout at the finest-scale stage, key routing across neighboring queries at intermediate stages, and spatial mixing in the expanded feature spaces of ConvFFNs. Accordingly, HiGLR replaces costly self-attention at the finest-scale stage with a learned input-independent kernel. At intermediate stages, we propose a Block-Routed Hybrid Attention, which combines coarse-scale dense attention with fine-scale block-sparse attention over value residuals relative to coarse summaries, and shares routing indices across neighboring queries. We further introduce a Dual-Space FFN that performs spatial mixing in a compact space and pointwise nonlinear transformation in an expanded space, enabling efficient kernel fusion. Combining these designs, HiGLR achieves state-of-the-art performance while delivering up to a $4.24\times$ inference speedup over existing methods.

---


### 81. [Pretraining for Forecasting in Relational Databases](https://arxiv.org/abs/2611.33645)

**<font color=#1a73e8>作者：</font>** Ziyue Lin, Sebastian Regalado Lozano, Michael Guerzhoy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world forecasting increasingly relies on asynchronous transaction logs in relational databases rather than uniformly sampled arrays. While relational deep learning (RDL) models can forecast from these complex histories, they are typically trained separately for each specific target and root entity type. We introduce Query-Conditioned Relational pretraining (QCRP), a self-supervised framework that enables a standard RDL backbone to act as a universal forecaster across a database. QCRP generates diverse forecasting objectives using a structured temporal query grammar and interleaves them through a shared conditional predictor. This produces a robust, frozen encoder reusable for downstream tasks via lightweight predictors or a zero-shot interface. Evaluated on large-scale RelBench databases, QCRP learns frozen representations that support competitive forecasting across tasks and entity types. Furthermore, a single unified QCRP model checkpoint is competitive with isolated, entity-specific specialists. We demonstrate promising results for reusing the learned representations from standard RDL backbones for forecasting tasks in relational databases.

---


### 82. [The Danger of Double Precision: Working Precision as a Hidden Constraint in Gaussian Process Maximum Likelihood](https://arxiv.org/abs/2611.33647)

**<font color=#1a73e8>作者：</font>** Thomas A. Scott  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gaussian process (GP) hyperparameters are routinely fitted by maximizing the marginal likelihood in IEEE double precision, although for smooth kernels and noiseless data the covariance matrix is often more ill conditioned than double precision can resolve. For a squared-exponential kernel on a design with a Bayesian-optimization cluster, refits over a range of significand widths, judged against a high-precision reference, show that the double-precision fit is a different model and that fits converge only once the width exceeds the base-2 logarithm of the covariance condition number, about 70 bits. Cholesky failure acts as an implicit conditioning constraint, caused mostly by rounding of the kernel entries; the constrained solution predicted from the working precision alone is within 20% of the best Powell fits at five of the six precisions from 40 to 64 bits, with a local expansion proved for the idealized problem. Across 43 kernels, designs and problem settings, including negative controls that double precision already resolves, the bits needed follow the log condition number at the reference optimum plus a tolerance-dependent offset, and at the loosest tolerance double precision suffices for the Matern 1.5 kernel but not for the squared-exponential kernel on clustered designs. Double-precision hyperparameters overstate the posterior standard deviation near the design cluster and, on a quadratic objective whose likelihood heads to the flat limit, stall closed-loop active learning. Promoting the whole likelihood to 80 significand bits recovers the reference accuracy on every fixed design tested, whereas a fixed jitter trades failures for a posterior bias.

---


### 83. [PRIOR: Pre-Call Reasoning in SFT and Its Influence on Tool-Use Retention under RL](https://arxiv.org/abs/2611.33648)

**<font color=#1a73e8>作者：</font>** Kaiwen Hu, Hyunin Lee, Joseph Suh 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool use learned during supervised fine-tuning (SFT) is not always retained during reinforcement learning (RL). We study how properties of SFT data may affect this retention by constructing Low, Medium, and High SFT datasets with approximately matched token budgets but different tool-call depths. Under the same RL recipe, the three initializations reach similar RL training accuracy yet exhibit markedly different tool-use dynamics: tool initiation increases in Low, declines in Medium, and collapses in High. We observe that these datasets also differ substantially in the amount of reasoning preceding each tool call. In particular, High trajectories contain considerably less pre-call reasoning, motivating the hypothesis that pre-call reasoning may affect how well tool use is calibrated and, consequently, whether the corresponding behaviors are retained during RL. An idealized theoretical analysis provides a selective-retention view of this process: advantages in overall and tool-conditioned accuracy can be preserved under outcome-only optimization, while tool initiation increases only when tool-using trajectories are more successful than the tool-free alternative. Guided by this analysis, we rank the original High trajectories by average pre-call reasoning length and retain the highest-ranked examples while approximately matching cumulative SFT token exposure. This simple filtering strategy improves post-RL accuracy and tool-conditioned final-answer success without consistently increasing tool initiation across multiple benchmarks. These results suggest that pre-call reasoning is a useful dimension of SFT supervision for understanding and improving tool-use retention under downstream RL.

---


### 84. [Linear-Time Online Visual Geometry Transformer with Hybrid Architecture](https://arxiv.org/abs/2611.33650)

**<font color=#1a73e8>作者：</font>** Haoyu Kang, Pingzhi Li, Ruichen Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformer-based 3D reconstruction models such as VGGT and $\pi^3$ predict cameras, depth and point maps directly from many input views. Causal attention models such as StreamVGGT extend them to online video but cache all past tokens, so their total compute grows quadratically with the stream length. Recurrent models such as CUT3R and TTT3R keep a fixed-size state at constant cost, but they progressively forget early geometry. We present LinearVGGT, a hybrid model distilled from StreamVGGT, which uses Mamba2 layers for efficient sequence modeling in three of every four global layers. The remaining layers use register-guided sparse attention to retrieve a few relevant past frames, compensating for the limited exact long-range recall of Mamba2. Our distillation needs only 9\% of the GPU hours and 31\% of the training frames that StreamVGGT uses to learn from VGGT. LinearVGGT keeps an almost constant latency of 27 ms per frame over 1,024 frames and is on average $12 \times$ faster than StreamVGGT. It outperforms its teacher and is competitive with the state-of-the-art streaming model LingBot-Map, while running $2.5\times$ faster and using $2.7\times$ less memory.

---


### 85. [Self-supervised Clipped-objective Reinforcement Leaning Framework for Risk-aware Portfolio Management](https://arxiv.org/abs/2611.33652)

**<font color=#1a73e8>作者：</font>** Zongshen Mu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Portfolio management involves balancing diverse financial assets, a critical yet challenging task in quantitative trading. Although deep reinforcement learning has emerged as an active research domain for solving complex sequential decision-making problems over the past decade, deploying reinforcement learning frameworks in non-stationary financial markets raises formidable difficulties. Most existing reinforcement learning-based portfolio management models fail to account for tick-level intraday market dynamics (e.g., order flow imbalances and liquidity fluctuations), which reflect rapid capital movements. Simultaneously, these models suffer from unstable learning processes due to reinforcement learning's inherent high variance. This paper presents a Self-supervised Clipped-objective Portfolio management framework (SCP), which addresses these limitations through a two-phase architecture. Market feature integration phase (application contribution) integrates micro-level market microstructure patterns with macro-level financial indicators to enhance sensitivity to intraday asset trend dynamics. Policy optimization Phase (AI contribution) employs intermediate asset state representations to derive optimal portfolio allocations via a self-supervised clipped-objective policy-learner, ensuring both effectiveness and computational efficiency. Extensive evaluations on three major index datasets from China's A-share market demonstrate that SCP's superior performance in balancing risk-return trade-offs compared to state-of-the-art baselines. Exploratory and ablation studies further validate the contributions of SCP's key components.

---


### 86. [Recall4D: Forgetting, Not Misalignment, Limits Long-Horizon Feed-Forward 4D Reconstruction](https://arxiv.org/abs/2611.33655)

**<font color=#1a73e8>作者：</font>** Tianle Lyu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 4D trackers recover camera motion, depth, and point trajectories from short video clips, but chaining windows over long videos degrades their accuracy. We find that replacing inter-window alignment with ground-truth transforms leaves tracking error essentially unchanged. Static-point error instead grows with time since last observation: repeatedly predicting a static point from windows that no longer observe it corrupts previously recovered geometry. We call this failure forgetting. Merely retaining the last observed positions of unseen points reduces error by 26% on PointOdyssey without modifying the tracker. We introduce Recall4D, a training-free framework that augments a frozen tracker with a persistent world state and sparse motion anchors. Static points retain their world-space positions outside the camera view and are refined by averaging observations decoded at sparse keyframes while in view. For dynamic objects, the tracker decodes sparse representative anchors, while geometric skinning propagates their displacements to dense queries. Across two long-horizon benchmarks, Recall4D improves the accuracy of its backbone while running 7.6-9.0$\times$ faster, and its accuracy gains carry over to five further backbones and three other long-sequence tasks, demonstrating its generality.

---


### 87. [SlicePlanner: Logic-Guided Agentic AI for Online QoS-Aware Network Slicing in Open RAN](https://arxiv.org/abs/2611.33664)

**<font color=#1a73e8>作者：</font>** Adhwaa Al-Chaab, Ayman Younis, Dario Pompili  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adaptive network slicing in Open Radio Access Network (O-RAN) demands reconfiguration decisions that respond to live traffic conditions while remaining safe with respect to Service Level Agreement (SLA) constraints, a combination that purely data-driven controllers cannot reliably guarantee without continuous retraining. We present SlicePlanner, a logic-guided closed-loop framework that treats each RAN reconfiguration as a controlled hypothesis: proposed from live and historical KeyPerformance Indicator (KPI) evidence, filtered through explicit SLA constraints and mined RAN control rules, and committed only when post-action measurements confirm improvement. SlicePlanner comprises two cooperating agents: SliceSense, which monitors live KPIs, retrieves context-conditioned evidence, and ranks candidate RAN actions through a surrogate-guided admissibility filter; and SliceGuard, which validates post-action KPI responses, rolls back harmful configurations, and refreshes rules under distribution drift. Validated over the air using OpenAirInterface, FlexRIC, and commercial Sierra Wireless 5G devices, SlicePlanner reduces SLA latency violations by up to 86% over static slicing and 50% over Deep Reinforcement Learning (DRL)-based slicing, while maintaining comparable cell throughput and auditable decisions without online retraining.

---


### 88. [Bounding the security of the FALCON signature scheme in the quantum random oracle model](https://arxiv.org/abs/2611.33666)

**<font color=#1a73e8>作者：</font>** Kelsey A. Jackson, Carl A. Miller  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In 2016, the National Institute of Standards and Technology (NIST) announced their invitation for proposals of public key encryption and signature schemes that are resistant to attacks by quantum computers. Since then, several rounds of proposals and revisions have occurred resulting in the 2022 announcement that three signature schemes - CRYSTALS-Dilithium, FALCON, and SPHINCS+ - would be standardized. However, in 2024, work by Fouque et al. noted an oversight in the published security for FALCON, which they were only able to remedy in a classical computing setting, namely the random oracle model (ROM). In this paper, we provide the first complete security proof for FALCON in the quantum random oracle model (QROM). Specifically, we will prove a reduction to the security of FALCON from the ring inhomogeneous short integer solution (RISIS) problem and the NTRU learning problem utilizing known quantum reprogramming results. We then provide parameter sets which meet the security levels required by NIST under our reduction.

---


### 89. [Look at What Matters: Learning Lesion Prototypes from Severity Labels for Domain-Generalized Diabetic Retinopathy Grading](https://arxiv.org/abs/2611.33671)

**<font color=#1a73e8>作者：</font>** Ziyang Zhang, Juming Xiong, Yanfan Zhu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models for diabetic retinopathy (DR) grading often generalize poorly to unseen imaging domains, in part because predictions may exploit correlations specific to source datasets rather than retinal pathology. We address this challenge by constructing grading decisions from lesion evidence learned using only image severity labels. Clinical implications of DR grades provide multiple instance constraints that guide competitive learning of lesion and background prototypes at multiple scales. An additive ordinal scoring model then predicts severity exclusively from individual lesion prototype responses, explicitly connecting learned evidence with grading decisions without a global feature classification pathway. To improve the reliability of this evidence, we introduce teacher guided preservation under image degradations and spatial regularization against persistent coordinate preferences. Across six public DR datasets under a leave one domain out protocol, our method attains a mean quadratic weighted kappa of 0.761, outperforming the strongest competing method by 0.036. Localization and prototype removal analyses show that the learned responses align with retinal lesions and contribute to grading decisions. Experiments across five other prototype architectures and under image degradations further demonstrate the generality and robustness of the approach.

---


### 90. [Node Differential Privacy via Node-Stable Graph Projections](https://arxiv.org/abs/2611.33672)

**<font color=#1a73e8>作者：</font>** Ishaq Aden-Ali, Adam Sealfon, Adam Smith 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Node-differentially private algorithms enable learning on network-structured datasets in which records reflect interactions among individuals. They protect the privacy of each individual's information, including all their associated records. A key challenge in the design of such algorithms is to exploit the structure of realistic graphs---where most nodes have low degree---to achieve high accuracy, without compromising on the worst-case privacy guarantee.
In this work we give two new tools for designing accurate, computationally efficient node-differentially private algorithms. First, we give a nearly linear time, randomized, node-stable graph projection: the projection leaves graphs of maximum degree $D$ unchanged, maps arbitrary graphs to subgraphs of maximum degree $\hat D \approx D$, and ensures that changing one node of the input graph has only a small effect on the distribution of the edges selected among the remaining vertices. Unlike prior approaches, which abstain when the input violates the degree bound, our projection acts as degree clipping: even when $D$ is set well below the true maximum degree (trading truncation bias at high-degree outliers for lower privacy noise), it retains at least as many edges as a maximal $D$-bounded subgraph.
Second, for graphs with bounded edge weights, we give a deterministic nearly linear time Lipschitz extension for the total edge weight that agrees with the original sum on graphs of maximum degree $D$ yet is $D$-Lipschitz on all graphs.
Finally, we show how to apply these methods to design node-private algorithms for high-dimensional vector summation and gradient descent on datasets where records are associated with graph edges, such as email threads.

---


### 91. [MOVR-SAR: A Multi-resolution SAR Registration Dataset under Orbit-crossing and View-variant Imaging Differences](https://arxiv.org/abs/2611.33673)

**<font color=#1a73e8>作者：</font>** Yuchi Pu, Bosong Qi, Pengcheng Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic aperture radar (SAR) image registration under varying acquisition geometries is challenging because orbit direction, look side, and incidence angle affect backscatter, terrain-induced distortion, and feature visibility. However, large-scale geometry-aware benchmarks remain scarce. This paper presents MOVR-SAR, a multi-resolution dataset of 450,845 registered and quality-screened tile pairs derived from 2774 scene pairs from Capella, Umbra, Sentinel-1, and NISAR. It covers X, C, and L bands, ground sampling distances of 0.25-20 m, and diverse regions and land-cover types. A unified framework defines four imaging-geometry pair categories from orbit direction and look side, plus viewing-angle-separation labels for Capella and Umbra, enabling stratified evaluation under same- and opposite-direction illumination. Systematic evaluation of representative matching methods shows that official and cross-modal pretrained weights perform poorly on high-resolution X-band imagery. Fine-tuning on MOVR-SAR improves accuracy and reduces disparities across platforms, imaging-geometry pair categories, and viewing-angle separations. For example, fine-tuning increases FlexGlue AUC@5 from 3.06% to 89.79% on Capella and from 1.79% to 89.03% on Umbra, reaching 93.41% and 94.77% on Sentinel-1 and NISAR, respectively. Fine-tuning substantially reduces the official-weight same-orbit, same-look-side advantage and reverses the three-method average category ranking on Capella, suggesting that this bias reflects training-data coverage rather than an invariant limitation of cross-geometry matching. Land-cover effects remain platform- and method-dependent. MOVR-SAR provides a training resource and geometry-aware benchmark for robust SAR-SAR registration. The dataset and model weights will be released at this https URL.

---


### 92. [GeoTex: Geometry-as-Texture Encoding and History-Grounded 4D Occupancy Forecasting](https://arxiv.org/abs/2611.33693)

**<font color=#1a73e8>作者：</font>** Shijun Guo, Yaming Yang, Haoran Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D occupancy forecasting models 3D scene evolution to support future prediction and scenario generation in autonomous-driving world models. Semantic occupancy abstracts image color and texture into discrete labels, leaving 3D voxel arrangements as the primary cues for distinguishing local shapes within each class. Existing methods borrow image-encoding frameworks to obtain compact latent representations through height channelization or plane factorization, but do not sufficiently model within-column height patterns and cross-column relations jointly before compression, weakening these geometric cues. Forecasting also underutilizes complementary history and struggles to retain reliable observation evidence. We therefore propose GeoTex, an occupancy world model combining geometry-as-texture encoding with history-grounded forecasting. GeoTex Representation jointly encodes within-column height patterns and cross-column relations into compact continuous latent representations and restores 3D structure through content-dependent height unfolding and geometric interaction. GeoTex Prediction retains initial evidence throughout rollout in fixed cross-observation relational memory and incorporates complementary recent history through target-referenced residual updates. After prediction training, decoder-only adaptation improves semantic decoding of predicted states. GeoTex improves average forecasting mIoU and IoU by 9.79% and 11.91% relative to GenieDrive while reducing parameters from 3.47M to 2.33M, with gains increasing at longer horizons. Code is included in the supplementary material.

---


### 93. [Efficient Scene-Distribution-Aware Second-Order Optimization for 3D Gaussian Splatting](https://arxiv.org/abs/2611.33698)

**<font color=#1a73e8>作者：</font>** Hyunseung Son, Young Sun Choi, Youngsik Yun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) optimization updates the Gaussian parameters one training view at a time, tens of thousands of times. Unlike such single-view updates, multi-view batches reduce dependence on individual training views, and second-order optimization reduces the number of updates with larger, structured parameter changes. Because fewer updates leave fewer chances to correct a change that fits only the views used in one update, scene coverage becomes more important for each second-order update. Multi-view second-order updates, however, are expensive. Pixel sampling reduces this cost, but two issues remain. First, selecting views without considering overlap leaves some views redundant. To address this, we propose a view selection strategy that reduces this redundancy. Second, existing work processes the sampled pixels of each view in a separate pass and recomputes alpha compositing for these pixels from scratch. We introduce two implementation strategies that reduce both overheads by processing the sampled pixels of multiple views in joint passes and reusing the transmittance and accumulated color cached during rendering. On three datasets, our method reaches higher PSNR than the sampled second-order baseline in less than half its optimization time, with competitive SSIM and LPIPS.

---


### 94. [P-FedSkill: A Personalized Federated Skill Learning Framework under Task Heterogeneity](https://arxiv.org/abs/2611.33707)

**<font color=#1a73e8>作者：</font>** Zehang Lin, Jiayi Ji, Rongrong Ji  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skill learning has become an important way to improve agent performance. However, agent trajectories often contain sensitive information and cannot be shared across clients, hindering collaborative skill learning. To tackle this issue, federated skill learning (FSL) has emerged as a solution by distilling trajectories into compact skill representations and uploading them to a central server for sharing. However, existing FSL methods typically share skills based on skill similarity without considering their contributions to heterogeneous tasks across clients, thereby degrading agent performance. To address this challenge, we propose P-FedSkill, a personalized FSL framework that comprises three key components: local skill extraction (LSE), personalized skill selection (PSS), and task-aware skill routing (TASR). Specifically, LSE first extracts skill patches (i.e., task applicability conditions and execution strategies) and task execution outcomes from trajectories. PSS then uses these outcomes to evaluate each skill patch's performance on client tasks and incorporates its task applicability condition to construct a personalized skill set for each client. Finally, TASR adaptively selects a task-relevant subset of skill patches based on their applicability conditions to guide agent execution. We further provide a theoretical guarantee for personalized skill selection in P-FedSkill, and extensive experiments also demonstrate its effectiveness.

---


### 95. [Nepali Currency Denomination Classification Using Convolutional Neural Networks (CNNs) and MobileNetV2: An Experimental Comparison](https://arxiv.org/abs/2611.33713)

**<font color=#1a73e8>作者：</font>** Sakar Lamichhane, Sandesh Bhatta, Aayush Adhikari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated currency denomination recognition is a computer vision task with applications in cash handling, financial technology, and assistive systems. This study classifies seven Nepali currency denominations (Rs. 5, 10, 20, 50, 100, 500, and 1,000) using three configurations: a conventional convolutional neural network (CNN), MobileNetV2 with transfer learning, and MobileNetV2 with hyperparameter tuning. A compiled dataset of 16,249 images was used, comprising 10,500 training, 3,500 validation, and 2,249 independent test images. Images were resized to 128 x 128 pixels, normalized, and augmented to vary orientation, scale, illumination, and appearance. Models were evaluated using accuracy, precision, recall, F1-score, and precision-recall and ROC analysis. The hyperparameter-tuned MobileNetV2 achieved the highest validation accuracy (95\%), with precision, recall, and F1-score of 0.93, 0.91, and 0.92, but reached only 84\% accuracy on the held-out test set. MobileNetV2 with transfer learning but no additional tuning achieved 89\% test accuracy, and the conventional CNN achieved 85\%. Transfer learning therefore provided a competitive approach under the evaluated conditions, while higher validation accuracy from tuning did not yield higher test accuracy. To demonstrate practical deployment, a Flask-based web prototype using TensorFlow Lite was developed, supporting image upload and live webcam recognition with both visual and voice output. The study shows the feasibility of combining lightweight deep learning with a voice-assisted web interface for Nepali currency recognition, and highlights the need for more diverse datasets, greater robustness under uncontrolled imaging conditions, and broader real-world evaluation.

---


### 96. [KeyDeck: Multi-Paper-to-Slide Generation via Cross-Paper Synthesis and Reference-Guided Personalization](https://arxiv.org/abs/2611.33715)

**<font color=#1a73e8>作者：</font>** Tarik Can Ozden, Sachidanand VS, Ram Prakash Reddy Motati 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-paper-to-slide generation (multi-PTSG) is the task of constructing a unified presentation from multiple research papers by selecting, organizing, and synthesizing information across sources. This task introduces two main challenges: (i) combining multiple sources into a coherent narrative requires identifying cross-paper relationships and synthesizing their content, and (ii) the desired organization and emphasis varies substantially across presenters, making personalization essential for user satisfaction. Motivated by these challenges, we propose KeyDeck, the first multi-PTSG framework that integrates per-paper and cross-paper analysis to identify relationships among sources and synthesize their contributions into a coherent narrative, and reference-guided personalization to infer presenters' narrative, content, textual, and visual preferences and adapt slide generation accordingly. To evaluate generation quality, personalization adherence, and conversational goal satisfaction, we introduce KeyBench, a benchmark of 100 expert-authored multi-paper presentations, together with a comprehensive evaluation framework. Our results demonstrate that KeyDeck outperforms existing approaches in multi-PTSG quality, personalization adherence, and conversational goal satisfaction.

---


### 97. [Flipping the Coins: Training Physical Simulators through Hard Switches](https://arxiv.org/abs/2611.33716)

**<font color=#1a73e8>作者：</font>** Tianrun Gao, Ruiqi Feng, Haomin Wen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid simulators embed learnable components such as neural networks in physical solvers and train them on reference trajectories. Many scientific solvers feature hard switches, such as a tripping power line, an igniting grid cell, or depolarizing brain tissue, where the loss exhibits discrete jumps across switch flips, leaving standard automatic differentiation to capture only its smooth part. Existing training paradigms face a fundamentally challenging trade-off, as gradient-based relaxations smooth the switches and introduce bias across jumps, whereas derivative-free methods treat the solver as a black box and discard path gradients of the continuous dynamics. Here we introduce EventFlip, which flips a near-threshold switch from a stored state, replays the original solver, and measures the loss difference between the two runs, in effect a finite difference across the switch. By perturbing every threshold with small Gaussian noise, we cast each switch as a stochastic binary decision and derive an unbiased gradient estimator that combines the continuous path gradient with a jump term constructed from these counterfactual rollouts. EventFlip-Rand optimizes this noise-averaged objective, whereas EventFlip-Hard operates on the deterministic hard-switch simulator used at deployment and provably targets the complete discontinuous loss. Under an identical forward evaluation budget, we benchmark EventFlip against twelve baselines across a power-grid cascade, a detonation wave, and cortical spreading depolarization, achieving the lowest error on every task and reducing the strongest baseline's error by factors of 1.5, 1.4, and 1.4, respectively.

---


### 98. [Understanding Mode Collapse in Diffusion Models under Classifier-Free Guidance](https://arxiv.org/abs/2611.33719)

**<font color=#1a73e8>作者：</font>** Daniel Pfrommer, Chenyang Yuan, Frank Permenter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The use of classifier-free guidance in diffusion and flow models has proven critical to their empirical success, as it allows for the controllable generation of lower-temperature and higher-fidelity samples. Despite its widespread use, classifier-free guidance remains both empirically and theoretically poorly understood, owing to the difficulty of solving the associated transport equations for arbitrary normalizing flows. In this paper, we observe that the effects of classifier-free guidance arise from a mismatch between the representation capabilities of the conditional and unconditional distributions, wherein the conditional distribution exhibits higher complexity and fidelity. We propose an analytical model to capture this observation: the conditional distribution is a Gaussian mixture whose means lie on an ellipsoid, and the unconditional distribution is a single Gaussian approximating the mixture. The flows arising from this mixture are closed under scaling, enabling us to derive analytic closed-form solutions for the guided distribution at all noise scales and guidance levels. Our analytic solution shows that classifier-free guidance induces (a) a shift along a mean-axis direction and (b) a persistent skew toward, and concentration around, a singular point corresponding to the conditional sample starting from zero noise. We validate our theoretical predictions on pretrained, large-scale image diffusion models.

---


### 99. [DualCast: Dual-Image Conditioned Diffusion Transformers for Digital Human E-Commerce Video Generation](https://arxiv.org/abs/2611.33734)

**<font color=#1a73e8>作者：</font>** Lifan Jiang, Yifan Huang, Jixuan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in world models for game interaction and control have increased the demand for large-scale gameplay videos paired with camera trajectories. However, capturing synchronized camera trajectories often requires game-specific pipelines, limiting scalability. We therefore propose GameWeaver, a unified diffusion framework that automatically produces paired video--camera data through three complementary tasks: camera pose estimation from observed video, video generation along a prescribed camera trajectory, and joint video--camera generation from a reference image and text. First, each tipxel stores the normalized 3D coordinates of a pixel ray's endpoint in a reference coordinate frame. The resulting three-channel tipxel fields and RGB frames share the pretrained video model's VAE. Next, a fully trainable dual-stream Transformer exchanges appearance and geometry features through bidirectional gated attention and conditions both streams on shared text features. Finally, deterministic fitting recovers camera intrinsics and normalized trajectories from generated tipxel fields. In our evaluation tasks, GameWeaver achieves a normalized translation MSE of 0.0029 for camera control; for joint generation, it scores 85.48 out of 100 on instruction adherence versus 64.71 for the best cascade on that metric, validating the feasibility of the proposed approach.

---


### 100. [WhatIf: Counterfactual World Models over Action-Grounded Causal Graphs for Robotic Manipulation](https://arxiv.org/abs/2611.33745)

**<font color=#1a73e8>作者：</font>** Xu Yang, Kailai Sun, Qianchuan Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World models predict what happens under an action, but choosing between actions requires comparing their outcomes in the same physical situation. Factual transitions alone determine action-wise marginal futures and average effects, but not individual effects or the probability that switching actions causes harm. We introduce WhatIf, a counterfactual world model for manipulation that couples candidate futures through shared latent physics and transition noise inferred from factual history. Each candidate action induces a sparse object-factor causal graph describing the physical pathways it activates. Rolling out these graphs under the shared situation anchors predictions to observed outcomes and confines action contrasts to the objects each action reaches. Shared type-conditioned functions support varying numbers of objects, while a round-trip loss enforces action-invariant abduction without counterfactual labels. We show that replacing an individual effect with its conditional mean incurs mean-squared error equal to its conditional variance, motivating comparisons between coupled futures. Building on these comparisons, Counterfactual Advantage Planning (CAP) ranks plans by their advantage over an incumbent within shared situations and constrains the probability of harm. Paired advantages reduce estimator variance by a factor of $1-\rho$, where $\rho$ is the correlation between branch outcomes, and cancel model errors shared by both branches. Each executed transition provides hindsight advantages to update the physics posterior, the next plan, and an amortized policy without a learned critic. We further establish when observational transitions identify interventional dynamics. Paired simulator interventions evaluate counterfactual accuracy, graph recovery, compositional generalization, and decision quality.

---


> [!TIP]
> 当前位于：**51-100**（第 2/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-314](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
