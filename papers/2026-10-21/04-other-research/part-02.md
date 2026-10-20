# 📦 其他研究 | 2026年10月21日

> 本类共 **534** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-534](./part-11.md)

---

### 51. [BiNar: Bitstream Native Restorer for Bitstream-corrupted Image Restoration](https://arxiv.org/abs/2610.24094)

**<font color=#1a73e8>作者：</font>** Fangcheng Li, Zhen Yu, Kejun Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bitstream-corrupted image restoration (BCIR) aims to reconstruct faithful images from corrupted compressed bitstreams. However, corruption occurs in bitstream-domain may lead to unpredictable error propagation and distortion amplification in pixel-domain, and even result in complete undecodability by standard decoders, posing significant challenge to existing image restoration paradigms. To address this challenge, we propose Bitstream Native Restorer (BiNar), a generative restoration framework that leverages fine-grained bitstream-native semantics to guide bitstream-corrupted image restoration. In BiNar, Bitstream Semantic Modeling (BSeM) extracts robust informative semantics and models sequential bytes directly from corrupted bitstream, enabling to generate fine-grained bitstream descriptions without relying on pixel decoding. Based on the descriptions,the Corruption-adaptive Multimodal Semantic Aggregation (CMSA) further extracts adaptive visual modal cues in decoded corrupted images and aggregates to bitstream descriptions. The multimodal aggregated fine-grained descriptions can serve as coherent restoration guidance. Finally, Blind Corruption Localization (BCoL) exploits the segmentation prior of visual foundation models to identify and locate error regions that requires recovery in corrupted images. The located error regions and the fine-grained descriptions jointly serve as visual prompt and language prompt of diffusion models image restoration, respectively. Extensive experiments under diverse bitstream corruption conditions show that BiNar outperforms all State-of-the-arts image restoration models regardless of perceptual quality or objective quality. Ablation studies demonstrate the effectiveness of fine-grained bitstream-native semantics in BCIR task.

---


### 52. [BLANC: Adaptive Temporal Scheduling for Sign Language Production](https://arxiv.org/abs/2610.24109)

**<font color=#1a73e8>作者：</font>** Youngmin Kim, Seoyeong Hwang, Sujung Hong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign language production (SLP) aims to synthesize expressive signing motion from written text. Modeling signing motion presents two key temporal challenges. First, fine-grained hand articulations demand higher temporal resolution than relatively slower body movements. Second, signing events unfold over variable durations, calling for adaptive temporal scheduling during generation. To address these challenges, we first introduce a Multi-Rate Vector Quantizer (MRVQ), an articulation-decoupled motion tokenizer that represents the body and both hands as separate discrete streams at distinct temporal resolutions. Building on this representation, we propose BLANC (BLock-wise Adaptive diffusioN with Articulatory Clock), a gloss-free SLP framework that generates variable-duration motion blocks causally while denoising tokens in parallel within each block. At its core, a Latent Articulatory Clock (LAC) learns temporal structure from multi-scale motion-derived partitions to predict block durations and sequence termination during generation. We further introduce inference-time body-conditioned hand refinement to improve coordination across articulators. Extensive experiments on PHOENIX-2014T and CSL-Daily demonstrate that BLANC achieves state-of-the-art performance in sign language production.

---


### 53. [Looped GNNs Beyond Fixed Depth: Graph Size Generalization and Parameter-Efficient Adaptation](https://arxiv.org/abs/2610.24112)

**<font color=#1a73e8>作者：</font>** Zhiyang Wang, Zhishang Luo, Yusu Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generalizing from small graphs to larger ones can require computation beyond the depth of a neural model used during training. We study target tasks that admit a common local iterative computation and whose effective dependency radius grows with graph size. The central idea is to learn a local update rule through GNN pretraining, then repeatedly apply the same learned processor beyond the training depth to extend information reach on larger graphs without retraining. Calling such parameter-shared architecture a \emph{looped GNN}, we categorize six schemes for looped GNNs to separate the effects of depth extension, fine-tuning, and freeze-and-steer adaptation. Our analysis establishes fixed-depth information limits and sufficient conditions under which accurate iterative reuse overcomes them. To improve beyond unadapted reuse, we introduce \emph{Loop-Freeze-Steer} (LFS), which freezes the pretrained processor and learns a small controller to steer its repeated application, using much fewer trainable parameters than full fine-tuning. Our finite-sample analysis gives sufficient conditions for adaptation to improve performance on larger graphs. Experiments on synthetic tasks and chip placement evaluate depth extension and adaptation, highlighting LFS's accuracy--trainable-parameter trade-off for size generalization.

---


### 54. [Graph-Regularized Synthetic Control for Stable Counterfactual Estimation under Donor Redundancy](https://arxiv.org/abs/2610.24113)

**<font color=#1a73e8>作者：</font>** Yanlin Zhang, Sungyong Chung, Alireza Talebpour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic control methods estimate counterfactual outcomes by weighting untreated donor units to match a treated unit before treatment. In recent applications, however, the donor pool can be large, highly correlated, and short in pre-treatment history, yielding many near-equivalent solutions with unstable and difficult-to-interpret donor weights. We propose Graph-Regularized Synthetic Control (Graph-SC), a convex estimator that augments the classical pre-treatment matching objective with a graph Laplacian penalty. The graph encodes similarity among donor trajectories, encouraging coherent weights over structurally related donors while preserving the transparency of synthetic controls. We provide theoretical results characterizing the bias-variance tradeoff induced by graph regularization and establish efficient convergence guarantees with an accelerated proximal gradient method. Across a controlled simulation under donor redundancy, the California Proposition 99 benchmark, and observational counterfactual analyses on the Waymo Open Motion Dataset, Graph-SC improves weight stability, reduces sensitivity to redundant donor pools, and maintains competitive pre- and post-treatment accuracy relative to classical and regularized synthetic control baselines. Our results suggest that graph regularization is most valuable not as a universal accuracy booster, but as a principled mechanism for selecting stable and interpretable counterfactuals from near-equivalent synthetic controls with comparable pre-treatment fit.

---


### 55. [HAVANA: A Hierarchical Video-Action Model for Vision-Language Navigation](https://arxiv.org/abs/2610.24122)

**<font color=#1a73e8>作者：</font>** Dongzhihan Wang, Yi Du, Chen Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Navigation (VLN) requires long-horizon instruction-consistent planning and short-horizon local planning in current geometry. Video-action models (VAMs) offer a promising way to learn predictive representations for navigation. However, existing VAMs jointly predict visual futures and local trajectories in a single process, even though they operate at different paces: future prediction remains stable across multiple updates while local trajectories must react to fresh observations. To bridge this gap, we introduce HAVANA, a dual-system VAM that decouples predictive reasoning from reactive local planning. A slow system produces a compact language-conditioned latent plan from observation history, while a fast system combines the latest plan with the current observation to generate local trajectories. Their asynchronous execution enables rapid adaptation without repeated future prediction, and no future video is generated during inference. Experiments on OmniNavBench demonstrate state-of-the-art navigation performance over prior baselines, while real-world deployments further show robust generalization to unseen environments across different robot embodiments. Our code and checkpoints will be available at this https URL.

---


### 56. [On the Selectivity of Generative Models in Structure-Based Drug Design](https://arxiv.org/abs/2610.24124)

**<font color=#1a73e8>作者：</font>** Ella Miray Rajaonson, Jungyoon Lee, William Chau 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Designing small-molecule drugs that selectively bind to a target protein while avoiding unintended interactions with other proteins is essential for reducing side effects that contribute substantially to clinical attrition. Although structure-based drug design (SBDD) has advanced rapidly with deep learning, most generative models still optimize binding to a single target and disregard selectivity due to limited training data and unknown off-target interactions. Motivated by this gap, we introduce SELECTBENCH, a comprehensive benchmark assessing the selectivity of generative SBDD models. SELECTBENCH provides three curated evaluation tasks reflecting different real-world drug discovery scenarios: literature-based case studies, safety screening panels used in pharmaceutical development, and large-scale structure-based evaluation sets. We further introduce a suite of metrics to quantify selectivity and conduct a systematic evaluation of nine representative SBDD models, including methods explicitly trained for selectivity and widely-used inference-time guidance techniques. Our results show that even selectivity-trained models achieve only modest off-target discrimination and inference-time guidance provides limited gains, underscoring the need for method improvement. SELECTBENCH provides both a characterization of where current generative SBDD stands on selectivity and an open, extensible platform to accelerate progress. The benchmark is available at this https URL.

---


### 57. [Data-Driven Resource Aggregation for Scalable Digital Twin and Simulation Model Generation](https://arxiv.org/abs/2610.24126)

**<font color=#1a73e8>作者：</font>** Yucheng Wu, Alp Akcay  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As industrial digitization accelerates, the use of digital twins has become widespread. However, modern manufacturing systems are highly dynamic and frequently reconfigured, making manual model development and updates increasingly difficult. Recent research on automated simulation model generation shows that historical data such as event logs can yield simulation models automatically. However, modeling every resource at full granularity leads to unnecessary complexity and computational cost. We propose a method for automatically selecting and aggregating resources to simplify simulation modeling. Our method uses ideas from inverse reinforcement learning to learn behavioral value representations of resources from production event logs. This process identifies and aggregates resources with similar functional contributions. Experiments on manufacturing systems, using throughput and system time as performance measures, demonstrate that value-based resource aggregation performs well when the goal is to substantially reduce complexity while preserving performance accuracy.

---


### 58. [Recording-Aware Evaluation of Multimodal OT Intrusion Detection](https://arxiv.org/abs/2610.24128)

**<font color=#1a73e8>作者：</font>** Mustafa Umut Ozbek, Khalil El-Khatib, Li Yang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine-learning-based intrusion detection systems (IDSs) for operational technology (OT) are commonly evaluated on benchmark datasets in which normal and attack data are collected in separate recordings. In such settings, high performance may reflect recording-associated differences as well as attack behavior. We introduce a recording-aware evaluation procedure that compares attack windows with background from the same recording, uses prior data for model fitting and calibration, tests temporal alignment against randomized event schedules, and reports event coverage together with alarm burden. On the ProvICS multimodal dataset, cyber modalities strongly distinguish the benign and attack recordings before the first labeled attack. Same-recording evaluation reverses the apparent modality ranking across all studied window sizes: the physical view becomes the strongest individual modality, while cyber-only fusion shows the largest difference between cross-recording and same-recording AUC, reaching 0.54. Operational analysis further shows that permissive event-overlap metrics can overstate detection when a small number of long alarm episodes cover multiple actions. An external analysis on HAI shows smaller and reference-dependent recording sensitivity. These findings show that cross-recording benchmark performance should be interpreted alongside same-recording, forward, temporal, and operational evaluations.

---


### 59. [Preservation and loss of algorithmic structure in experimental diffusion of joint-action norms](https://arxiv.org/abs/2610.24150)

**<font color=#1a73e8>作者：</font>** Dhara Yu, Bill D. Thompson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Everyday norms of social interaction - e.g. norms of sharing space, taking turns, or queuing - are essential to large societies, offering structured procedures for common interactions. However, it remains unclear how the underlying algorithms of these implicit joint plans evolve as they diffuse through populations. Here we show that this process of diffusion can select against complex algorithms in the earliest stages. We conducted a large-scale study of experimental diffusion of novel social norms among human participants, leveraging advances in program synthesis to characterize the procedures people developed in independent populations. Inherited procedures became structurally simplified and lost during interactions between participants who inherited different variants of joint-action norms; however, opportunities for interactive repair offset this pressure, preserving complex algorithms despite misalignment. These results demonstrate that interactive reasoning mediates selective pressures on structural complexity during cultural evolution of procedural norms.

---


### 60. [NV-Generate-Body: 3D Latent Diffusion Model forControllable Anatomy, Tumor, and Demographic Body Mask Synthesis](https://arxiv.org/abs/2610.24153)

**<font color=#1a73e8>作者：</font>** Can Zhao, Pengfei Guo, Dong Yang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Curating large labeled CT datasets is expensive and constrained by patient privacy. We present NV-Generate-BodyMask, a 3D latent diffusion model that synthesizes whole-body CT segmentation masks with precise, joint control over organ anatomy, tumor burden, and patient demographics. The model operates in the compressed latent space of a frozen mask autoencoder, generating $256^3$ volumetric label maps conditioned on a 19-dimensional vector via Adaptive Group Normalization and cross-attention. A size-adaptive ROI loss with spatial halo weighting and a paired tumor injection pipeline enable accurate tumor size conditioning despite the scarcity of annotated tumor cases. Trained on 8,571 masks across 26 cohorts spanning 132 labels, the model achieves Spearman $\rho = 0.70$--$0.92$ for organ size, 85--100\% tumor recall for lung, pancreatic, colon, and bone lesions, and strong demographic alignment (BMI $\rho = 0.78$, sex-conditioned perfect prostate control).

---


### 61. [Budgeted Bayesian Bandits for Future Utilization](https://arxiv.org/abs/2610.24156)

**<font color=#1a73e8>作者：</font>** Sudipto Guha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The multi-armed bandit problem models the trade-off between exploration and exploitation. In this paper, we study the variant where exploration has a hard budget and precedes exploitation. Prior guarantees include a 1/3 approximation by Guha and Munagala using Lagrangian duality, and a 4/27 approximation by Ma against a primal linear programming relaxation for a more general model. We show that the analyses of both algorithms are tight, even when their relaxations are asymptotically exact. We provide a different efficient algorithm that achieves a 0.43 approximation. We then provide an efficient algorithm whose guarantee approaches 1-e^{-1} approx 0.63 for bounded exchangeable reward observations in a non-vanishing regime, which is asymptotically tight against natural linear programming relaxations. The technique also gives certificates for stopping sequential model evaluation.

---


### 62. [TorchTPU - A Hybrid Eager/Compiled Architecture for Native PyTorch Execution on TPU](https://arxiv.org/abs/2610.24161)

**<font color=#1a73e8>作者：</font>** Claudio Basile, Michael Voznesensky, Gunhyun Park 等 53 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> TorchTPU is an open-source collaboration between Google and Meta that introduces a native and principled PyTorch backend for Google TPUs. It enables seamless out-of-the-box model execution and TPU migration while delivering industry-competitive inference and training performance through eager execution optimizations, this http URL integration, and native hardware acceleration.

---


### 63. [Margin Certificates for Voting Classifiers under Mixing Dependence](https://arxiv.org/abs/2610.24166)

**<font color=#1a73e8>作者：</font>** Adria Binte Habib, Ibne Farabi Shihab  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Margin bounds explain why weighted votes generalize after training error vanishes, but dependent observations require concentration arguments that keep the dependence model and failure budget explicit. We study stationary mixing streams without treating dependence as a formal substitution of an "effective sample size." For a finite base class, we combine independent-block Rademacher theory for stationary $\beta$-mixing processes with a clipped margin loss to obtain an explicit uniform voting-margin certificate, whose dependence penalty is set by the number of approximately independent blocks and the coupling budget $4(\mu-1)\beta(a)$. A black-box transfer theorem shows that any i.i.d. voting-margin guarantee remains valid on a regularly spaced subsequence, with only an additive $\beta$-mixing failure probability. For votes fixed independently of a stationary finite-state reversible Markov stream, spectral concentration gives the cleaner $\sqrt{t_{rel}/n}$ rate, and a sticky-refresh construction shows this exponent is unavoidable. The constant is statistic-specific: the effective sample size is $n/\tau_{int}(g)$, with $\tau_{int}(g) \le 2t_{rel}-1$. When the dependence scale is unknown, a batch-means Student-t interval is valid up to an explicit remainder vanishing in the number of batches, with width governed by $\tau_{int}(g)$ rather than the worst-case $t_{rel}$. Experiments show: the learned-vote certificate is nonvacuous once the block count is large; a two-timescale construction gives a batch-means interval 8.1x narrower than the worst-case interval at nominal coverage (0.945); block-bootstrap and batch-means intervals undercover under strong dependence while the certificate stays valid; and on real, ordered UCI HAR sensor data the dependence-agnostic certificate reaches 0.95 coverage where naive intervals reach only 0.38.

---


### 64. [SERO: Semantic Prediction for Single-Step Object Removal](https://arxiv.org/abs/2610.24173)

**<font color=#1a73e8>作者：</font>** Amreen Hasheem Siraj, Alireza Javanmardi, Pragati Jaiswal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object removal and semantic inpainting of missing regions remain inherently ill-posed, as multiple plausible completions may exist for a given scene. Recent diffusion-based methods have demonstrated strong potential for high-quality object removal; however, they still face two key limitations. First, although they can synthesise sharp and high-resolution images, they often struggle to complete removed regions in a semantically consistent and contextually meaningful manner, where the generated content should agree with the surrounding scene layout and object relationships rather than merely appear visually realistic. Second, their iterative denoising process makes them computationally expensive, limiting their practicality for downstream applications. We propose SERO, a semantic prediction framework for single-step object removal. Our model predicts a hidden-region semantic prior in embedding space, which guides a latent bridge-matching generator toward plausible scene completion by providing both where to edit and what structure is likely to exist behind the removed object. This enables visually realistic and contextually coherent completions in one forward pass. Experiments on the RORD and OBER datasets show that SERO achieves competitive or state-of-the-art performance while requiring only a single generation step.

---


### 65. [Self-Improving Video-to-Action Models](https://arxiv.org/abs/2610.24177)

**<font color=#1a73e8>作者：</font>** Hyunwoo Ryu, Eric Ming Chen, Max Wilcoxson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Video generative models are an emerging tool for embodied agents: they can serve as scalable visual planners, generating videos that depict how to complete previously unseen tasks. However, executing these plans typically requires a video-to-action or "inverse dynamics" model trained on large, human-collected video-action datasets, severely limiting scalability. We introduce Mirror, a self-supervised approach that learns video-to-action mappings through environment interactions, without prior action data or hand-crafted rewards. Mirror learns by attempting to follow a visual plan by executing its best guess of the underlying actions in the environment. Mirror then trains on the resulting video-action pairs, incrementally self-improving and following the visual planner more closely. Across Atari, OGBench, and DeepMind Control, Mirror outperforms leading learning-from-observation methods with learned video plans, and achieves near-expert performance with oracle plans. On Minecraft BASALT, it outperforms methods with access to expert actions or hand-engineered task knowledge. In Minecraft survival, it is the first method to acquire an iron pickaxe through self-improvement alone, without rewards or expert action labels. In the offline setting, with expert action labels but no environment interaction, it sets a new state of the art in obtaining diamonds. Our results suggest that advances in video models can translate into increasingly capable agents without a corresponding need for hand-crafted rewards or large collections of expert action data.

---


### 66. [Precision Cotton Disease Management: Leveraging UAV Imagery and Custom YOLO Deep Learning Framework for Enhanced Detection](https://arxiv.org/abs/2610.24182)

**<font color=#1a73e8>作者：</font>** 1. Anwar Iqbal*1 aiqbal.rime23smme@student.nust.edu.pk 2. Kunwar Faraz Ahmad Khan1 kunwar.faraz@smme.nust.edu.pk 3. Shahbaz Khan1 shahbaz.khan@smme.nust.edu.pk 4. Khawaja Fahad Iqbal1 fahad.iqbal@smme.nust.edu.pk 5. Sara Ali1, 2 sara.baber@smme.nust.edu.pk 6. Saqib Nazir1 saqib.nazir@smme.nust.edu.pk 7. Muhammad Azhar Javed3 muhammadazhar6231@gmail.com 1 Department of Robotics, Artificial Intelligence 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cotton sustains the textile economies of over 80 countries with an annual yield of 113 million bales, yet 30-60% of yield losses are still attributed to viral, bacterial, and fungal diseases that remain undetected until manual field scouting. To address this critical issue, the integration of Unmanned Aerial Vehicle (UAV) imagery with deep learning offers a scalable early-warning system; however, existing models suffer from low early-stage accuracy, poor transferability, and high computational cost. In this paper, we propose Cotton-Vision, a fully convolutional single-stage detector that synergizes three lightweight architectural innovations: Ghost Bottleneck modules for a 20% parameter reduction, Efficient Channel Attention (ECA) for adaptive feature recalibration, and Cross-Stage Partial (CSP) fusion for enriched gradient flow. The network is trained on a novel dataset collected across seven cotton fields in the Punjab province of Pakistan, comprising over 2,700 high-resolution drone images. Extensive data augmentation (rotation, shear, exposure, and saturation) expands the dataset to 11,704 training samples. On a held-out test set, Cotton-Vision achieves a precision of 97.7%, a recall of 77.7%, an mAP@50 of 85.6%, and an mAP@50-95 of 76.6%. These results represent a 10-20% improvement in precision, recall, and mAP over state-of-the-art baselines, including YOLOv5, YOLOv8, YOLOv11, YOLOv12, RT-DETR, and RF-DETR. Through a comprehensive ablation study, we demonstrate that each proposed architectural enhancement contributes to the model's superior performance, yielding a 12-16% mAP improvement over the baseline architecture. Our findings confirm that this synergy of lightweight and attention-based modules provides a robust, computationally viable solution for early cotton disease detection.

---


### 67. [Bootstrap Stochastic Interpolant Tree for Inference-time Search Under Sparse Reward](https://arxiv.org/abs/2610.24185)

**<font color=#1a73e8>作者：</font>** Binglin Ji, Anindya Sarkar, Yevgeniy Vorobeychik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tree-based samplers offer a compelling alternative for scalable inference-time search, bypassing the per-step reward and gradient dependencies that introduce systematic bias into SMC-style frameworks. Despite this advantage, contemporary tree samplers fail to achieve broad exploration. Their reliance on learned, DDPM-like transitions inherently couples neighbor states in a trajectory, thereby restricting child-parent feature divergence in the tree sampler. Consequently, these samplers suffer from restricted coverage of the target marginal distribution, severely hindering the exploration critical for efficient search under sparse reward. To overcome these limitations, we introduce a simple yet effective Bootstrap Stochastic Interpolant Tree (BSIT) sampler that decouples child node generation from explicit parent dependencies. By expanding the degrees of freedom during child node sampling, BSIT encourages diverse trajectory rollouts and unlocks broader path-space diversity-the exact catalyst needed for efficient exploration. Crucially, we show that BSIT's improved exploration accelerates convergence to the target distribution while achieving broader distributional coverage than samplers that rely on DDPM-like transitions for child-node generation, all without incurring additional function evaluations or reward feedback, thereby providing a highly efficient basis for rare target search. Extensive experiments across diverse search settings, including rare-species discovery and target-aligned molecule generation tasks, demonstrate BSIT's superior search efficiency over the baselines.

---


### 68. [Over reliant and underprepared: First responder resilience to disruption of operational technology](https://arxiv.org/abs/2610.24186)

**<font color=#1a73e8>作者：</font>** James Connor, Courtney Crooks, Ryan Shandler  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The Emergency Services Sector (ESS) is responsible for taking life-saving action in the face of extreme crises. To enhance its response capabilities, the sector has spent the last two decades investing in new technology to improve their operational efficiency. This has created significant interdependencies and a culture among first responders of technical overreliance, raising questions about what would occur if those tools were suddenly disrupted. Several works have discussed the potential for terrorism to intentionally target ESS technology as part of a larger kinetic attack. Despite this, the resilience of first responder agencies to technological disruption and their preparedness for such an attack has largely remained unexplored. To bridge this gap, we implemented a novel scenario-based interview methodology involving senior officials from emergency service agencies across the United States. These interviews explored how each agency prepared for a disruption of operational technology and what factors might influence different levels of preparation between them. Participants were asked to describe their responses to a hypothetical scenario modeled after historical cyber-attacks against ESS infrastructure. The results indicate that while ESS agencies are prepared for short-term technological disruptions, they are likely to struggle with long-term or hybrid incidents. The data further revealed that agencies often lack dedicated expertise in cybersecurity, technology, and emergency management that could otherwise elevate resilience to interruptions of operational technology. These findings emphasize the need for investment in redundant analog systems, increased training for frontline personnel, and a focused effort against loss of specialized technical expertise among ESS agencies.

---


### 69. [On Reparameterizing the Score Function](https://arxiv.org/abs/2610.24188)

**<font color=#1a73e8>作者：</font>** Mohammad Hossein Amani, Leonardo Bocchieri, Maxime Peyrard 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Policy gradients for autoregressive sequence models differentiate each token's log-probability while holding the conditioning history fixed. This discards information about how earlier decisions shape later conditional distributions, creating a credit-assignment bottleneck when rewards are sparse. We introduce History-Reparameterized (HR) policy gradients, which replace the frozen prefix in the score function with a differentiable reparameterized or relaxed history, allowing gradients of downstream log-probabilities to propagate backward through the generated trajectory. The resulting history-pathwise term is generally biased when added directly, so we derive Optimal HR (OHR), a centered control-variate estimator with a closed-form coefficient that minimizes the trace of the gradient variance at the population level. The variance reduction is governed by temporal structure in the policy dynamics: random or weakly structured policies provide little benefit, while policies with learned sequential dependencies yield informative history-pathwise corrections. For discrete tokens, the choice of relaxation is crucial: embedding-level relaxation yields substantial variance reduction that grows with horizon, whereas straight-through Gumbel-Softmax yields essentially none in our diagnostics. We validate the method on a Gaussian linear Markov model, a sparse-reward T-maze with a recurrent policy, and an autoregressive Transformer model for small Traveling Salesman Problem (TSP) instances.

---


### 70. [PREEMPT: Proactive Robustness Evaluation under Editing for Media Protection Techniques](https://arxiv.org/abs/2610.24205)

**<font color=#1a73e8>作者：</font>** Qiuyu Tang, Aparna Bharati  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Proactive image protection methods aim to defend visual content against unauthorized manipulation and generative misuse by embedding protective signals into images before release. Evaluating whether these protections remain effective under image editing is therefore critical. However, existing evaluations remain largely limited to one-shot edits, providing only a static view of robustness while overlooking its evolution under realistic multi-step editing workflows. To systematically characterize robustness dynamics under sequential editing across various protection paradigms, we introduce PREEMPT, a holistic evaluation framework. It evaluates protection robustness under both one-shot and sequential editing scenarios, covering image transformations, semantic edits, homogeneous and heterogeneous edit compositions. To enable consistent analysis across protection paradigms with different underlying objectives, PREEMPT normalizes task-specific effectiveness into protection survival trajectories and summarizes long-horizon robustness through trajectory-based diagnostics. Using this framework, we reveal that degradation behaviors remain hidden under conventional one-shot evaluation. Furthermore, perturbation- and watermark-based protection methods exhibit different failure modes, and the first semantic edit largely determines subsequent degradation trajectories. PREEMPT provides a standardized protocol for studying long-horizon robustness and offers new insights into the degradation dynamics of proactive image protection.

---


### 71. [Navigating Deception on Gay Dating Apps: A Qualitative Study of Users' Experiences, Verification Strategies, and Community Knowledge in China](https://arxiv.org/abs/2610.24207)

**<font color=#1a73e8>作者：</font>** Yibo Meng, Lyumanshan Ye, Bingyi Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Gay dating applications have become essential platforms for sexual minority men to seek relationships, intimacy, and community, yet they also expose users to a range of deceptive interactions that remain underexplored in HCI and CSCW research. This study examines how gay male users in China experience, identify, and respond to deception on dating applications. Through semi-structured interviews with 22 participants who used platforms such as Blued, Aloha, Fanka, and Soul, we identify a typology of deceptive practices that users encounter, including relational misrepresentation for sexual access, sustained emotional deception, financial fraud, marketing behavior disguised as ordinary users, and false identity construction. We further analyze the verification and coping strategies that users develop through long-term platform use, such as judging relational intent through interactional pace, identifying financial risk signals, recognizing commercial promotion accounts, and progressively verifying identity authenticity. Finally, we show that risk recognition is not merely an individual capacity but a collaborative practice that gradually emerges through the circulation of experience within the community, the summarization of recurrent deceptive tactics, and the learning of shared rules. Our findings contribute to CSCW scholarship by demonstrating how users of a marginalized community collectively construct practical knowledge about deception, and by revealing that trust assessment on dating platforms operates as a layered, probabilistic, and socially distributed process rather than a binary judgment.

---


### 72. [You Already Have Me--Why Do You Still Use Blued?'' How Gay Dating Apps Shape Intimate Relationships Among Chinese Gay Men](https://arxiv.org/abs/2610.24215)

**<font color=#1a73e8>作者：</font>** Yibo Meng, Lyumanshan Ye, Bingyi Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Gay dating applications such as Blued are widely used for meeting partners, yet their role does not end once an intimate relationship is formed. When these platforms persist within an established relationship, they transform from matchmaking tools into a form of relational infrastructure that both partners must continuously manage. Building on existing CSCW and HCI research that has primarily examined how social media triggers jealousy, surveillance, or trust issues in intimate relationships, this study investigates how the persistent presence of gay dating applications shapes the dynamics of intimate relationships among Chinese gay men. Through semi-structured interviews with 23 self-identified gay men aged 19 to 55, we identify a recurring cyclical process: platform signals-such as online status, profile updates, distance indicators, and usage records-trigger suspicion and conflict; partners invest negotiation labor through intent explanation, visibility control, rule formation, or silence; and these negotiations eventually sediment into temporary governance settlements that reduce trigger frequency but remain conditionally stable. We identify four types of governance settlements: infrastructure removal, transparency governance, silence agreements, and layered/open agreements. Each settlement addresses the governance problems of platform presence, visibility distribution, and loyalty boundaries differently, yet none achieves permanent stability due to platforms' reversible entry mechanisms and continuous visibility cues. Our findings extend existing CSCW research on digital technology and intimate relationships by revealing a more complex process than previously documented: platform signals not only trigger emotional responses but prompt partners to engage in sustained relational negotiation through explanation, visibility management, rule formation, or silence.

---


### 73. [Landmark-Free and Scale-Blind Multi-View Registration of Preoperative Liver Models to Intraoperative Surfaces](https://arxiv.org/abs/2610.24218)

**<font color=#1a73e8>作者：</font>** Jiaming Feng, Gerardo Loza Galindo, Shahid Farid 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Augmented-reality guidance in laparoscopic liver resection requires aligning preoperative 3D liver models from CT/MRI with intraoperative surfaces. Monocular reconstruction in most cases cannot guarantee scale, albeit rigid-motion registration requires scale as an input. Our proposed framework ``SimCompose'' estimates the full similarity transformation $\Sim$, including scale, without relying on landmarks and applies the same transformation across multiple views with known relative geometry. However, reliable detection of registration failures remains challenging in surgical settings, where ground-truth alignment is generally unavailable. For this, we propose a geometry-based selector that evaluates candidate transformations without requiring ground truth. Large disagreement among these transformations is used to flag potentially unreliable registrations. Finally, we propose to use a non-rigid refinement based on a low-dimensional deformation model from Neo-Hookean simulations in the Simulation Open Framework Architecture (SOFA), without additional network training. SimCompose is trained exclusively on synthetic partial views. Its encoder processes point clouds normalised to a unit root-mean-square radius, without access to metric scale, and filters each view before multi-view fusion. Evaluation on unseen synthetic data (300 single-view pairs per run; 100 three-view registrations) shows that multi-view integration and candidate selection increase the success rate under stringent $\Sim$ accuracy criteria from 38.4% for a single-view, single-method configuration to 77%. Existing learning-based baselines do not satisfy these criteria even when provided with the exact scale. On five in-vivo patients with 92 keyframes, the rigid registration stage reduces surface error more than three-fold relative to learning-based baselines with external scale information.

---


### 74. [Hidden Trajectories Don't Lie: Correcting Corruption Drift for Test-Time Adaptation](https://arxiv.org/abs/2610.24220)

**<font color=#1a73e8>作者：</font>** Amirhossein Sabour, Amir Khasahmadi, Mengliu Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) adapts pretrained models to distribution shifts encountered during deployment. However, most existing methods rely on the weight representations of the final layer or signals derived from the model's output probability distribution. We study hidden trajectories: the ordered sequence of intermediate representations produced across a deep neural network. We observe that clean and corrupted trajectories become more separable as corruption severity increases. We introduce Drift-TTA, which adds zero-initialized low-rank adapters to a frozen backbone and trains them to align corrupted hidden trajectories with those from cleaner inputs. The approach supports two variants: a source-dependent version trained with clean targets, and a source-free setting that learns from corrupted images at different severities. We develop an online TTA approach that freezes the backbone and adapters while updating a scalar gate to control adaptation strength. We further cast trajectory alignment as MAP inference under a Gaussian observation model and derive a KL-based transfer bound characterizing test-time trajectory misalignment in terms of offline residual error, residual dimensionality, and distribution shift between offline and test corruptions. We evaluate Drift-TTA on CIFAR-10-C, CIFAR-100-C, and ImageNet-C using supervised ViTs and CLIP models. On CIFAR-100-C at severity 5, our source-free online approach improves accuracy over no TTA by 13.3 percentage points with ViT-B/16 and 11.6 percentage points with CLIP ViT-B/16, reaching 74.9% and 47.4%, respectively. Under the same setting, prior TTA baselines yield ECEs of 18.00% for ViT and 14.70% for CLIP, while our approach reduces them to 9.53% and 5.77%, respectively. These results demonstrate that hidden trajectory alignment provides an effective signal for both offline correction and lightweight online test-time adaptation.

---


### 75. [Trinketry: Materializing Elements to Anchor Traceable Design Histories](https://arxiv.org/abs/2610.24221)

**<font color=#1a73e8>作者：</font>** Wen-Fan Wang, Yi-Ting Chiu, You-Yi Hsieh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative tools enable visual designers to rapidly explore diverse design directions---but as flawed generated outputs proliferate, designers may lose track of promising ideas and the context of their development. We introduce trinkets: user-preserved design elements that function as reusable materials, retrieval queries, and navigational anchors for tracing how ideas emerge, transform, and recur throughout design history. We implement this concept in Trinketry, a visual exploration canvas. In a within-subjects study with 12 concept designers, Trinketry supported focused element-level exploration and greater perceived control than a simple branching image generation history baseline. A follow-up study with six returning designers examined delayed design history sensemaking, continuation of work, and reconstruction of others' processes. Compared with whole-image histories, Trinketry supported more precise reconstruction of process structure, turning points, and goals, while helping designers recover overlooked materials and continue exploration. However, opportunities remain to augment trace representations with explicit statements of design rationale.

---


### 76. [Analyzing Repetition and Interference Effects in Memory-Constrained User Simulators](https://arxiv.org/abs/2610.24232)

**<font color=#1a73e8>作者：</font>** Cara Su-Yi Leong, Nicholas Tomlin, Tal Linzen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> User simulators can help evaluate and train AI systems to interact with humans at scale. To do so, evaluation of user simulators must measure behavioral parity with people. We evaluate whether memory-constrained user simulators are sensitive to two factors known to affect human information retention: repetition of a fact and interference from competing information. We find that some simulators achieve human-like overall accuracy, and replicate the magnitude of repetition and interference effects, but none match people's accuracy on particular questions: while humans misremember facts, models forget them, leading to different error patterns. We release this data as a challenge benchmark for future work on user simulators.

---


### 77. [Usability, User Experience, and Acceptability of the Trail Making Test in Virtual Reality in Younger and Older Adults](https://arxiv.org/abs/2610.24237)

**<font color=#1a73e8>作者：</font>** Panagiotis Kourtesis, Dante O'Connor, Sarah E. MacPherson  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Immersive virtual reality (VR) adaptations of neuropsychological tests change how a test operates. Before their scores are interpreted, the individuals they are intended to assess should find them usable, acceptable and tolerable, and for older adults this evidence is usually missing. This study evaluated the experience of the Trail Making Test in Virtual Reality (TMT-VR), a head-gaze adaptation of the Trail Making Test that requires no hand-held controller, in 47 younger (20-38 years) and 44 older adults (64-81 years). After the task, participants rated usability, pragmatic and hedonic user experience, acceptability, and cybersickness. The study had three aims: to compare the two age groups on these ratings; to examine whether the ratings were associated with age group, gaming and technology experience, and whether cybersickness was associated with motion sickness susceptibility; and to examine whether the ratings were related to TMT-VR completion and error-adjusted times. Both groups rated the TMT-VR as highly usable, acceptable and pleasant to use. Older adults gave slightly lower usability and pragmatic ratings, but neither the age-group differences nor the associations with age group or previous experience were statistically significant after correction. Cybersickness was low, with 38 of the 91 participants reporting no symptoms; it did not differ between the age groups and was not associated with motion sickness susceptibility. No correlation between the ratings and TMT-VR performance survived correction. The TMT-VR with head-gaze selection is therefore usable, acceptable and well tolerated by older as well as younger adults. Because the ratings were favourable across the whole range of TMT-VR scores, slower or less accurate performance is unlikely to reflect difficulty with the interface.

---


### 78. [Ghost Attack: Using 19th-Century Illusions to Fool 21st-Century Biometrics](https://arxiv.org/abs/2610.24238)

**<font color=#1a73e8>作者：</font>** Tyler Fitzsimmons, Adam Czajka  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While the Pepper's Ghost illusion is a 19th-century optical technique, we found that this forgotten gimmick exposes vulnerabilities in modern face recognition systems. This paper introduces the 'Ghost Attack': a physical attack that repurposes this classic illusion using low-cost, free-space hardware and a transparent medium to project high-resolution facial data into physical 3D space. We show in the paper that despite relying on centuries-old optical principles, this new attack type simultaneously breaks three components of modern facial recognition systems (FRS): (a) the face matcher, (b) the presentation attack detection module, and (c) the morphing attack detection component, resulting in high impersonation success rates against state-of-the-art algorithms without triggering presentation or morphing defenses. These findings reveal a significant blind spot in current biometric systems, which fail to account for transparent projections and evolving physical attack vectors. To support further research, we are offering the dataset of face images of 100 identities, re-captured with and without 'ghost' projections as a new benchmark representing a novel attack for face recognition.

---


### 79. [Probing Ambiguity: Adversarial Intent Resolution for Robust Text-to-SQL](https://arxiv.org/abs/2610.24248)

**<font color=#1a73e8>作者：</font>** Youbing Yin, Xujun Peng, Muhammad S. Uddin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL systems typically assume a one-to-one mapping between natural-language queries and correct SQL translations. In practice, however, many queries are inherently ambiguous, admitting multiple valid interpretations that yield distinct outputs. We introduce Adversarial Intent Resolution (AIR), a multi-agent framework that actively probes and resolves such ambiguity without any task-specific training. AIR first constructs competing interpretations, verifies through SQL execution that they produce genuinely different results, and generates targeted clarification questions grounded in the observed data differences. Evaluating on leading benchmarks for ambiguous questions, AIR demonstrates strong performance, efficiency, and robust cross-benchmark transferability. On the AMBROSIA benchmark under schema-only context, a realistic production setting where exposing the full database is infeasible, AIR outperforms IntentRL, the state-of-the-art reinforcement learning model, across all metrics (e.g., F1 0.679 vs. 0.618). Crucially, AIR exhibits only ~7% performance degradation without the full database, compared to ~20% for IntentRL. On the AmbiQT benchmark, where ambiguity arises from schema design rather than linguistic structure, AIR achieves higher F1 under both context settings without any benchmark-specific adaptation.

---


### 80. [Dynamic Neural Optimal Transport for Subset Alignment](https://arxiv.org/abs/2610.24258)

**<font color=#1a73e8>作者：</font>** Austin J. Brockmeier, Bilal Riaz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study optimal transport between distributions when only a subset of the target population is relevant to the source. The goal is to map the source distribution to a reweighted target distribution whose density ratio with respect to the full target lies in $[0, c]$. This constraint enables the transported distribution to select an appropriate target subpopulation while limiting how strongly any region of the target can be emphasized. We propose a dynamic neural optimal transport framework for this setting using two neural networks. The first parameterizes a time-dependent potential whose spatial gradient defines the velocity field and whose terminal value enforces the density-ratio constraint. The second parameterizes an interpolation between the source distribution and the learned terminal distribution. Unlike prior neural dynamic optimal transport methods, which typically assume a fixed terminal distribution, our formulation learns the terminal distribution within the support of the target. We demonstrate the method on positive-unlabeled learning, unpaired domain translation, and trajectory inference, where meaningful alignments exist between source and target distributions, but direct distribution matching is inappropriate because the target contains additional or irrelevant components

---


### 81. [Modeling bilingual naming performance through laterally-connected SOMs](https://arxiv.org/abs/2610.24275)

**<font color=#1a73e8>作者：</font>** Divya Prabhakaran, Uli Grasemann, Erie Shivers 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Computational models have explanatory power to understand cognition in individuals, but there is usually not enough training data to build such models with traditional machine learning. However, alternative architectures that model neural and cognitive processes in more detail can be more easily fit to individuals and can lead to mechanistic insights into human behavior. BiLex is such a computational model of the bilingual lexicon, containing a shared semantic system and phonetic language systems represented through self-organizing maps. In this study, BiLex was extended further into biological realism with excitatory and inhibitory lateral connections. This extension makes it possible to account for response times as well as common errors such as those based on semantic concept familiarity, typicality, and specificity. The Boston Naming Test was simulated in Spanish and English, and model performance approximated naming accuracy and error types in Spanish-English bilinguals with varying primary and secondary language histories. The results indicated that the approach captures semantic-level processes in bilingual lexical access, thus modeling the semantic cognition of individual subjects. In the future, such models may serve as a foundation for modeling impairments and treatment options.

---


### 82. [Empirical Analysis of TEE-Enabled Rollup Designs](https://arxiv.org/abs/2610.24284)

**<font color=#1a73e8>作者：</font>** Claudiu-Nicu Bărbieru, Corentin Libert, Peterson Yuhala 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Layer 2 (L2) rollups have become the dominant scaling solution in Ethereum. At the core of these systems lies the rollup sequencer, a component that orders, executes, and submits L2 transaction blocks to the main Ethereum blockchain. The centralization of this sequencer introduces security risks, including censorship and malicious manipulation of transactions to extract maximum extractable value (MEV). Trusted execution environments (TEEs) provide strong hardware-enforced confidentiality and integrity guarantees for code and data. TEEs are strong candidates for strengthening security and ensuring verifiable neutrality in rollup sequencer operations, but multiple TEE-based designs are possible, offering different trade-offs among modularity, performance, and security guarantees. Among them, the separation of proposer and builder logic (PBS) into independent services is a strong contender against the monolithic approach that bundles all sequencer logic. Despite several proposed theoretical frameworks, there is a lack of experimental evaluation of the practicality and security trade-offs of integrating TEEs into rollup sequencers. This work addresses this gap through a comprehensive empirical study of TEE-enabled rollup designs under both PBS and monolithic sequencer models. Our experimental evaluations show that the impact of TEEs on rollup performance is small and that PBS does not significantly amplify it. We also show that PBS can lead to significant performance improvements by enabling more specialized, efficient builder logic implementations.

---


### 83. [ULIFLOW: Unified Latent Human-Object Interaction Flow](https://arxiv.org/abs/2610.24286)

**<font color=#1a73e8>作者：</font>** Wenqi Cai, Chunzhi Gu, Weichen Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-conditioned 3D human--object interaction (HOI) generation remains challenging because individually plausible human and object motions do not necessarily form a coherent interaction. We argue that a key limitation lies in conventional skeleton-based representations, which compactly describe body kinematics while leaving surface-level interaction geometry largely implicit, often requiring additional contact-specific regularizers. We propose ULIFlow, a framework that explicitly models continuous human--object relations within a unified latent space. To this end, we derive continuous marker--object relations from sparse body-surface markers and treat them as an explicit interaction modality alongside human motion and object dynamics. A Mixture-of-Transformers (MoT) autoencoder is then designed to jointly model these heterogeneous streams while preserving their modality-specific structures. Importantly, we let the relation stream directly participate in human and object reconstruction, encouraging the shared latent representation to preserve both individual dynamics and the interaction geometry that coordinates them. To further achieve variable-length generation, we introduce a blockwise Flow Forcing scheme with global sequence-progress conditioning, enabling progressive continuation from fixed-length training windows while maintaining consistent long-horizon dynamics. Extensive experiments demonstrate that ULIFlow consistently outperforms prior work in overall generation quality and human--object coordination, while preserving coherent interactions over requested durations beyond the training horizon.

---


### 84. [Inducing Fourier Geometry: A Smoothness Prior Imposes Approximate Translation Equivariance in Multimodal Stellar Embeddings](https://arxiv.org/abs/2610.24292)

**<font color=#1a73e8>作者：</font>** Ilay Kamai, Alex M. Bronstein, Hagai B. Perets  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned representations often contain geometric structure induced by symmetries in the underlying data. We ask whether a known continuous parameter space can instead be used to \emph{induce} such structure when the corresponding symmetry is only approximate. We introduce a graph-Laplacian smoothness prior that encourages representations to vary smoothly over a physical parameter space without specifying a representation geometry; in the continuum limit it selects Laplacian eigenfunctions and therefore predicts the Fourier-like geometry associated with translation symmetry. On multimodal stellar representations spanning six astronomical surveys, the prior induces Toeplitz Gram structure and sinusoidal modes along stellar parameters, including in modalities whose native representations lack this geometry, while modality-specific residuals preserve structure outside the imposed coordinates. Of the exact-symmetry predictions, stationarity in a recoverable warped coordinate survives; diagnostics assuming exact quantization or asymptotic rates do not. The prior also improves downstream linear-probe performance and label efficiency, suggesting a general strategy: where a meaningful continuous parameter space exists, its local geometry can serve as a data-informed prior.

---


### 85. [Constructive Universal Approximation by Infinite-Dimensional Neural Networks via Gaussian-Weighted Ridgelet Transform](https://arxiv.org/abs/2610.24293)

**<font color=#1a73e8>作者：</font>** Sho Sonoda, Luca Galimberti, Yuanchao Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks whose inputs are functions, as in operator learning, are usually shown to be universal by existence arguments, either by reduction to finite-dimensional networks or by Stone--Weierstrass-type density; these prove that approximants exist but say little about how the parameters depend on the target. We take a constructive route. We extend the ridgelet transform, an integral transform related to the Fourier, Radon, and wavelet transforms, to continuous maps on a separable infinite-dimensional Hilbert space, replacing the Lebesgue measure that is unavailable in infinite dimensions by Gaussian weights with a homogeneous mixture on the direction space. The resulting transform has a Plancherel identity and reconstruction formulas incorporating the frame operator, the correction induced by the weights, and it assigns to each target an explicit coefficient measure, one for every admissible analysis filter. From these representations we obtain uniform approximation on compact sets for all continuous non-polynomial activations of polynomial growth, including ReLU, and, by Monte Carlo sampling of the coefficient, finite-width networks with a dimension-free $O(N^{-1/2})$ error in the width $N$ for globally Lipschitz activations and coefficients with finite variation and second moments. Explicit examples include Gaussian targets and neural-operator layers. A companion Lean~4 formalization provides machine-checked proofs, with its correspondence to the manuscript documented at this https URL .

---


### 86. [CRISP: Progressive Illumination Curriculum for Recurrent Low-Light Video Enhancement with Semantic Priors](https://arxiv.org/abs/2610.24299)

**<font color=#1a73e8>作者：</font>** Ruirui Lin, Xin Yan Lim, Yini Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-light video enhancement requires the recovery of brightness, color, and fine spatial structures while preserving temporal coherence in the presence of noise and motion. Existing methods often struggle to balance these objectives, particularly in severely degraded regions. This paper presents CRISP, a recurrent framework trained using a progressive illumination curriculum. Its two-frame recurrent architecture propagates information across successive frames to exploit temporal context beyond the immediate input pair. During training, supervision progressively transitions from intermediate targets interpolated between the low-light input and the reference to the full reference, gradually increasing the required brightness and color correction. This curriculum stabilizes recurrent training without introducing additional inference cost and yields the largest performance improvement among the components evaluated in the ablation study. To further support structural reconstruction, the framework optionally incorporates frozen DINOv3 semantic features through adaptive layer normalization (AdaLN)-style modulation, without fine-tuning the foundation model. Experiments on DID and BVI-RLV demonstrate that CRISP achieves the highest PSNR on DID and the highest SSIM on BVI-RLV among the evaluated methods, while maintaining computational efficiency.

---


### 87. [Torch-DPhys: A Torch-Native, MOOSE-Compatible Framework for Differentiable Physics Simulation and Hybrid Machine Learning Integration](https://arxiv.org/abs/2610.24301)

**<font color=#1a73e8>作者：</font>** Akzhol Almukhametov, Yang Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present Torch-DPhys, a Torch-native framework implemented in PyTorch for differentiable physics simulation and hybrid physics-machine learning. It implements selected thermal-hydraulic modeling concepts and discretizations from MOOSE's Thermal Hydraulics Module and the System Analysis Module (SAM), with a preliminary extension to continuum mechanics. Native tensor residuals support CPU and GPU execution, compilation of selected numerical kernels, and sparse direct linear solves. Sensitivities are obtained by differentiating executed numerical operations or through discrete adjoints of converged residual equations. Verification combines analytical solutions, reference-code comparisons, and derivative checks. Demonstrations cover plane-strain elasticity, one- and two-loop thermal-hydraulic transients, and an axisymmetric molten-salt fast reactor. For the reactor, comparison with SAM-Lite gives a maximum normalized field discrepancy of 1.13 x 10^-5 over 200 adaptive time steps, demonstrating agreement between the tested discrete implementations. Selected transient sensitivities are assessed using tangent-linear calculations and finite differences on fixed time schedules. Two applications illustrate the framework's connection between simulation and optimization. A residual-adjoint parameter-identification calculation recovers nominal pump head and heating power with relative errors below 0.06% from noiseless synthetic MOOSE observations. A separate three-loop plant demonstration uses solver-in-the-loop training of a predictive controller by differentiating trajectory-level objectives through the thermal-hydraulic simulation. These examples illustrate a foundation for gradient-based inference, control, and coupled physics-machine learning models in nuclear engineering.

---


### 88. [Muon Operates Beyond the Edge of Stability](https://arxiv.org/abs/2610.24305)

**<font color=#1a73e8>作者：</font>** Niko Covic, Baraq Lipshitz, Alexander Padula 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the Muon optimizer using sharpness and provide the first empirical evidence that the Flat Minima Hypothesis also applies to Muon. Further, we derive Muon's implicit preconditioner to analyze its potential Edge of Stability behavior. Experiments on CIFAR-10 show sharpness strongly correlates with generalization gap within each optimizer (Pearson $r = 0.45$-$0.69$, $p \leq 10^{-4}$), confirming the hypothesis holds for Muon similarly to Adam and SGD. However, Muon operates above the classical sharpness-based Adaptive Edge of Stability threshold that bounds diagonally-preconditioned optimizers like Adam and RMSprop, yet remains stable. Our findings suggest Muon operates in a fundamentally different regime than diagonally-adaptive methods. Defining the exact stability boundary for Muon remains an open question. All code is available at this https URL.

---


### 89. [Learning Administrative Boundary-Aware Location Encoders via Reverse Geocoding](https://arxiv.org/abs/2610.24306)

**<font color=#1a73e8>作者：</font>** Lakshay Sharma, Alex Marin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Location encoders learn compact representations of latitude--longitude coordinates for downstream geospatial prediction tasks. Existing approaches are pretrained using continuous or naturally occurring supervision, such as imagery, climate variables, or species distributions, and therefore do not explicitly capture administrative boundaries or place names, despite their strong influence on many real-world geospatial phenomena. We introduce, to our knowledge, the first method for learning administrative boundary-aware location encoders, using reverse-geocoded text as a self-supervised training signal. Our approach can be applied to existing location encoder architectures and consistently improves their downstream performance. We further introduce RevGeoRQ, a custom architecture tailored to reverse-geocoding supervision, which yields additional gains and exceeds contemporary location encoders on several downstream tasks. Finally, the use of human-interpretable reverse-geocoded strings and residual-quantized semantic IDs provides a more interpretable representation of geographic location than existing approaches. Code and model weights to be released soon.

---


### 90. [Indirect Influences of Artificial Intelligence Advice on Complex Sepsis Treatment Decisions](https://arxiv.org/abs/2610.24313)

**<font color=#1a73e8>作者：</font>** Venkatesh Sivaraman, Joel Levin, Eric P. Mason 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Sepsis is a major public health concern, and many sepsis patients die due to ineffective hemodynamic management. Artificial intelligence could support hemodynamic decisions, particularly in complex cases where conflicting information and comorbidities drive uncertainty and practice variation. However, these systems' real-world value depends on not just accuracy, but how they influence the quality of clinician decisions. We first retrospectively evaluated an AI system's recommendations in 6,928 sepsis patients, finding that they improved upon the original providers' decisions overall but had significantly worse performance in complex cases. We then conducted a pre-registered experiment with 228 US critical care physicians to test their use of this imperfect advice in six complex treatment decisions, using one of three advice types designed to vary reasoning autonomy. Participants given simple model recommendations overcame poor advice, choosing optimal treatments in 56.3% of decisions compared to 31.8% if they had always followed the recommendations. They also made significantly better decisions than those receiving a less prescriptive advice type (42.9%). Physicians selectively adapted and improved weak advice, likely because it prompted them to reconsider their assessment. Our findings suggest that improving sepsis care decisions with AI may require accounting for these indirect influences resulting from human-AI collaborative reasoning.

---


### 91. [Latent State Utilization in Probabilistic Circuits](https://arxiv.org/abs/2610.24315)

**<font color=#1a73e8>作者：</font>** Zilei Shao, Anji Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic circuits (PCs) are generative models that support efficient probabilistic inference. Adding latent states to a PC increases its representational capacity, but yields diminishing gains in likelihood. We use mutual information to examine how the dependence represented by a trained PC changes with latent size. Experiments with Hidden Chow-Liu Trees (HCLTs) on ImageNet32 show that learned dependence grows slowly and remains well below both the latent-state upper bound and estimates of dependence in the data. To understand how learning uses these states, we examine how strongly each sample favors particular latent states and how broadly states are used across the dataset. Tracking these measurements during HCLT training distinguishes rapid early posterior concentration from the more gradual stabilization of sample-dependent state preferences. Early measurements also guide initialization selection in HCLTs and hidden Markov models (HMMs), as well as tree selection in HCLTs. The resulting choices improve the ultimate performance across the tested latent sizes, providing a practical benefit from our study of latent-state utilization.

---


### 92. [Morpheus-2.0: Multiscale Probabilistic Forecasting with Dual-Axis Attention](https://arxiv.org/abs/2610.24321)

**<font color=#1a73e8>作者：</font>** Aakriti, Manoj Cherukumalli, Prathamesh Patil 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A universal forecaster is trained once and applied everywhere, so it must serve tasks whose schemas, forecast horizons, and temporal resolutions all differ. The number of targets and covariates changes from dataset to dataset, horizons vary by orders of magnitude, and sampling rates range from seconds to years. Existing time-series foundation models address these only in part, since they isolate each series or visit the two grid relations in separate blocks, and they fix the horizon and resolution before training begins. We introduce Morpheus-2.0, a compact encoder-only foundation model that represents targets and covariates on a single variable-time grid. Its dual-axis attention runs both relations side by side in every layer, one across variables at a timestep and one across time within a variable; a learned gate weights the two per layer, and an axis-aware rotary encoding preserves both grid coordinates. The forecast length is sampled during training, so one set of weights spans short to long horizons at no additional inference cost. Morpheus-2.0 Multiscale extends the model to several temporal resolutions at once, weighting them according to the series being forecast. Across GIFT-Eval, which spans several domains and frequencies, the two models give complementary operating points: Morpheus-2.0 attains 0.685 relative MASE with 81M parameters, while the larger Morpheus-2.0 Multiscale attains 0.646 relative MASE and 0.455 relative CRPS, the lowest of any published system on both metrics.

---


### 93. [PAC Learning with Query Feedback](https://arxiv.org/abs/2610.24332)

**<font color=#1a73e8>作者：</font>** Chase Hutton, Adam Melrod, Han Shao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study realizable multiclass PAC learning with query feedback, where each training example provides a single binary response indicating whether its true label belongs to a chosen subset from a fixed query family. Our main contribution is the query dimension, a combinatorial parameter that captures both the structure of the hypothesis class and the ability of the available queries to distinguish labels. This parameter generalizes the bandit DS dimension, which it recovers under singleton queries. We establish a sample-complexity lower bound of $\Omega(D/\varepsilon)$ and an upper bound of $\widetilde{O}(D^2/\varepsilon)$, suppressing factors polylogarithmic in the number of labels and the failure probability. When the available queries can split every candidate set into two parts of comparable size, we improve the upper bound to $\widetilde{O}(D/\varepsilon)$, yielding a characterization up to logarithmic factors.

---


### 94. [Power-Law Correlations Without Apparent Temperature-Tuned Criticality in Fixed-Tree Hierarchical Languages](https://arxiv.org/abs/2610.24334)

**<font color=#1a73e8>作者：</font>** Marcel Kühn, Bernd Rosenow  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling temperature can substantially reshape autoregressive generation, but it is unclear when temperature changes in long-range correlations reflect a genuine phase transition rather than a smooth change in statistics. We study this question in a controlled analogue of temperature sampling: a finite-depth probabilistic context-free grammar on a fixed hierarchical tree, where exact next-token conditionals are computed by belief propagation and then rescaled by a softmax temperature before autoregressive sampling. We measure two-point mutual information between tokens as a function of separation. Across the tested temperatures and grammar ensembles, mutual information remains well described by a power-law envelope. Temperature changes the correlation magnitude and fitted exponent, but within the accessible system sizes we find no long-distance plateau characteristic of an ordered phase and no clear crossover to short-range exponential decay. An approximate mapping to an Ising model on a tree explains how exponential decay in tree distance becomes a power law in token distance, allowing power laws to persist without tuning to a special decoding temperature. This controlled baseline clarifies which temperature effects can arise from hierarchical structure alone, before adding training, approximation error, or neural architecture.

---


### 95. [Uniform convergence at optimal rate and scale](https://arxiv.org/abs/2610.24336)

**<font color=#1a73e8>作者：</font>** Noga Alon, Steve Hanneke, Shay Moran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uniform convergence asks how many random samples suffice for empirical averages to approximate expectations simultaneously over an entire class of functions. It is a central concept in probability and a foundation of statistical learning. For binary-valued classes, the Vapnik--Chervonenkis theorem characterizes uniform convergence by finiteness of the VC dimension. For dimension $d$, the sharp worst-case sample complexity for additive error $\varepsilon$ is of order $d/\varepsilon^2$. For real-valued functions, the analogous combinatorial parameter is the fat-shattering dimension, which depends on an approximation scale $\gamma$. The challenge is to achieve error $\gamma+\varepsilon$ with order $d/\varepsilon^2$ samples, matching the sample bound for binary classes, where $d$ is now the fat-shattering dimension at scale $\gamma$. Previous results achieved either the optimal scale or the optimal sample complexity, but not both. Our main result closes this gap, establishing the sharp sample complexity at the optimal scale. Along the way, we use several tools that may be of independent interest. The first concerns $\varepsilon$-nets with margin. A classical $\varepsilon$-net intersects every set of mass at least $\varepsilon$ in a prescribed family; we allow the net to intersect a slightly enlarged version of each such set. Remarkably, this relaxation permits bounds independent of the ambient dimension in natural geometric settings. Second, we derive improved covering bounds in both discrete and real-valued settings: we extend Haussler's covering lemma to partial concept classes and use this extension to obtain $\ell_2$ covers at the optimal scale for real-valued function classes. Third, we obtain a chaining bound at the optimal scale by aligning the covers so that successive approximations become increasingly close to one another.

---


### 96. [The Certification Exponent: Instance-Optimal Sequential Certification of Policy Improvement from History Dependent Logs](https://arxiv.org/abs/2610.24345)

**<font color=#1a73e8>作者：</font>** Rui Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Before a new policy replaces a deployed one, we often want a certificate, computed from logged episodes, that it is better. We ask how many episodes such a certificate needs when the logging policy is known but history-dependent, and the error probability must stay below $\delta$ in every environment consistent with the logs. The answer is an exponent $K^\star$: the smallest KL divergence from the logged law to a law with the same logged action probabilities under which the target does not improve. No sound certifier stops in fewer than $\log(1/\delta)/K^\star$ expected episodes, at any $\delta$, and whenever $0<K^\star<\infty$ a plug-in Kelly certifier attains this rate to first order as $\delta\to0$. Coverage, computed by one backward induction, decides whether certification is impossible ($K^\star=0$), possible at a finite rate, or possible in a constant number of episodes ($K^\star=\infty$). By convex duality, the optimal certificate bets on the importance-weighted advantage and also places fair bets on the logged actions, so doubly robust control variates act as hedges rather than estimators. As a consequence, no choice of off-policy estimator changes $K^\star$, a coverage ceiling explains the curse of memory, and structural assumptions can be priced in exponent units. A cushion certifier extends the approach to trees too large to enumerate. In experiments the plug-in's median stopping time is 1.13-1.43x the lower bound on memory tasks, 1.13-1.51x on Tiger ($H\le5$) and 1.17-1.64x on random trees. The best scalar betting baselines need up to 2.65x (memory) and 4.1x (Tiger) the plug-in's episodes; only on a few shallow random trees is a doubly robust bet faster, by at most 18%.

---


### 97. [Exact Risk Certificates for Pairwise-Judged Reranking](https://arxiv.org/abs/2610.24347)

**<font color=#1a73e8>作者：</font>** Xinyu Wang, Jingrui Tian, Sicheng Lyu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pairwise relevance judgments constrain both the loss numerator and the ideal-ranking denominator of nDCG. We characterize the exact worst-case loss of replacing a ranking with a fixed proposal. Binary gains attain this loss and provide an inspectable witness. Threshold verification reduces to at most $K+1$ maximum-closure problems. Our exposure-flow ablation isolates denominator coupling: on shared judge trajectories, exact verification saves 2.34 comparisons per TREC-DL development query and 1.98 per confirmation query at a budget of 32. Savings transfer to BEIR and a second proposer. Predictive gates achieve higher deployment gains, while certificates expose the worst gains still permitted by accepted comparisons.

---


### 98. [Can Agents Keep Secrets They Were Never Told? Benchmarking Latent Privacy Risks Across Sessions with MemJoin](https://arxiv.org/abs/2610.24359)

**<font color=#1a73e8>作者：</font>** Qishun Yang, Shu Yang, Difei Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> To support sustained interactions and personalized assistance, agents use long-term memory to retain and combine user information across sessions. Reusing such memories can lead an agent to state a sensitive relation while completing an ordinary task that does not require it. The relation to protect and the combination of clues that reveal it may remain hidden at memory write time, when later records and tasks are still unknown. In this paper, we introduce MemJoin, a privacy benchmark of 288 synthetic analysis cases in which the complete history entails a sensitive relation, but every individual session is insufficient. We evaluate six memory systems with the same answer-generating model, alongside full-history and no-history controls. Each system writes and updates memories in session order and later retrieves context for an ordinary task, while target annotations remain with the evaluator. We separately check which target attribute values appear in stored records and retrieved context, and whether the final answer states the complete, person-linked relation. In a separate paired test on a prespecified subset, removing shared identifiers and other connecting clues can change complete-relation output while all checked target attribute values remain visible. These findings show why checking attribute visibility alone is insufficient to evaluate what records from different sessions reveal together.

---


### 99. [Hexagonal Basis Projectors for Model-Based Iterative CT Reconstruction](https://arxiv.org/abs/2610.24363)

**<font color=#1a73e8>作者：</font>** Ke Chen, Alireza Entezari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image representation affects both the forward model and quantitative feature recovery in model-based iterative CT reconstruction. For isotropically bandlimited signals, the hexagonal lattice is the most sampling-efficient lattice in two dimensions, with greater directional isotropy and a larger alias-free bandwidth than the Cartesian grid at equal density. We develop constant and linear hexagonal projectors for two-dimensional fan-beam CT using box spline calculus. Both bases form a partition of unity on common coefficient centers; the linear tent also reproduces affine functions. We derive analytic ray footprints and effective detector-blur expressions and implement efficient GPU forward and backprojection. On simulated FORBILD data, the linear model improves on Cartesian and hexagonal pixels, with its best noisy-data accuracy at the coarser resolution. Real-world 2DeteCT comparisons use high-dose, high-resolution Cartesian reconstructions as pseudo ground truth and show competitive image and feature agreement. These results establish a practical hexagonal representation for quantitative CT.

---


### 100. [A Two-Stage Hybrid Framework for Inferring Air Trips from Mobile Location-based Service (LBS) Data under Incomplete Airport Sightings](https://arxiv.org/abs/2610.24366)

**<font color=#1a73e8>作者：</font>** Hsuan-Chih Wang, Xianfeng Terry Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mobile device location-based service (LBS) data provide large-scale spatiotemporal observations that can help airport planners understand air travelers' mobility patterns. However, airport sightings are often missing before or after flights, making strictly rule-based detection incomplete. This study develops a two-stage framework to infer U.S. domestic air trips from large-scale LBS data under incomplete airport sightings. Stage 1 uses heuristic rules to identify high-confidence air trips whose endpoints are observed at two distinct airports. Stage 2 addresses latent air trips with a probabilistic model that infers air routes using spatial proximity, temporal compatibility, and historical flight schedule information. Using January 2022 nationwide LBS data with nearly 10 million users and 131 million sightings, results are validated against T-100 Domestic Segment route benchmarks and a Stage 1 pseudo-ground-truth reference set. The framework increases air route coverage from 10.65% under Stage 1 to 50.60% and recovers nearly all top-1,000 benchmark routes. It improves Spearman rank correlation with T-100 route shares from 0.4490 to 0.7630 and reduces Jensen-Shannon divergence from 0.2808 to 0.2263. Stage 2 also recovers 92.2% of Stage 1 reference trips. This study formalizes three endpoint observation regimes for LBS-based air trip inference (airport-observed, semi-observed, and latent) and helps airport agencies identify domestic air travel patterns missed when airport sightings are incomplete.

---


> [!TIP]
> 当前位于：**51-100**（第 2/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-534](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
