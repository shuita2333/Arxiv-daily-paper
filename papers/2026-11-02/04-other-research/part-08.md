# 📦 其他研究 | 2026年11月02日

> 本类共 **432** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-432](./part-09.md)

---

### 351. [Cheap Retrieval and Observation Credit Assignment from One Quantity: The Value of Information](https://arxiv.org/abs/2610.40030)

**<font color=#1a73e8>作者：</font>** Daniel Strauss, Nikolaos Sotirakis, Zhenshan Bing 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory in reinforcement learning raises two problems. Attention finds the relevant item by scoring the whole store, which is costly for robots under latency and energy limits. When a retrieved memory pays off, credit for acquiring it must cross the whole sequence. We argue that both are governed by one quantity, the value of information, and propose to estimate it from archived rollouts with a learned world model. We obtain that, when read at the observation, it yields a provable lower bound on the optimal value of the acquiring action, which floors its TD target and attributes this floor to the observation that earned it. Read at the decision, it defines the optimal retrieval set. A pilot retrieval system, to be trained and improved with this signal, solves a memory task with reduced context.

---


### 352. [EPC-RawDC: Equivariant Physics Constrained 3D Diffusion with Raw Data Consistency for CBCT to CT Image Synthesis](https://arxiv.org/abs/2610.40046)

**<font color=#1a73e8>作者：</font>** Alzahra Altalib, Chunhui Li, Alessandro Perelli  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cone beam computed tomography (CBCT) is widely used for image guided and adaptive radiotherapy, but scatter, noise, reconstruction artifacts, and inaccurate Hounsfield units limit its quantitative use. Recent diffusion approaches for CBCT to CT synthesis remain largely image driven, with limited use of the underlying acquisition physics. We propose EPC-RawDC, a conditional 3D latent diffusion framework that combines volumetric generative modeling with two complementary constraints derived from the same scanner specific CBCT forward model. First, geometry equivariant projection constraint exploits the rotational equivariance of the CBCT forward operator by supervising the synthesized CT through correspondingly transformed reference projections. Second, raw data consistency uses noisy projection measurements of the individual acquisition as scan specific supervision during training. The framework was evaluated on two independent clinical cohorts with distinct scanner geometries and projection sources. For JUST, the physics constraints used measured clinical raw CBCT projections acquired with an Elekta system, whereas for SynthRAD2025 the projection data were simulated from the reference CT using a Varian geometry with Poisson photon statistics. EPC-RawDC achieved an SSIM of 0.97 in both cohorts and improved PSNR over DDPM by 2.66 dB on SynthRAD2025 and 2.10 dB on JUST, while reducing mean MAE by 20.3% and 19.0%, respectively. On SynthRAD2025, projection consistency and equivariant errors were reduced by 55.0% and 41.4% relative to DDPM. These results demonstrate that combining a volumetric diffusion prior with scanner geometry and scan specific projection measurements improves quantitative CBCT to CT synthesis across both simulated and measured projection domains. Code available after publication at this https URL.

---


### 353. [Localizing Concepts in Visual Autoregressive Models](https://arxiv.org/abs/2610.40061)

**<font color=#1a73e8>作者：</font>** Nanxiang Jiang, Yang Liu, Yuanhao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding the internal routing of visual concepts is crucial for the safe and controllable adaptation of generative models. While concept localization has been widely studied in diffusion models, the emerging paradigm of next-scale visual autoregressive models remains largely unexplored. In this paper, we introduce LoCo, the first model-agnostic framework to localize where and when specific concepts emerge within autoregressive models. Driven by the native coarse-to-fine nature of next-scale generation, our method precisely maps conceptual knowledge across three distinct dimensions: Layer, Scale, and Position. To systematically localize and evaluate concept routing without context bias, we propose LoCoBench, a comprehensive dataset spanning 10 diverse categories. Extensive probing on image and video autoregressive models like Infinity, HunyuanImage-3.0, and InfinityStar shows that the localized positions are both interpretable and causally related to concept emergence. Building on these insights, we apply our localization method to three key applications: concept erasure, model personalization, and adversarial concept injection. Experiments demonstrate that our targeted intervention achieves state-of-the-art performance, substantially reducing computational overhead while preserving benign utility. Overall, our findings offer insights into how conceptual knowledge is routed during autoregressive generation, introducing a practical pathway for more interpretable, efficient, and secure adaptation.

---


### 354. [BRACHIO: Broad Representations Across Centres for Head-and-neck Imaging Oncology (HECKTOR 2026)](https://arxiv.org/abs/2610.40068)

**<font color=#1a73e8>作者：</font>** Roxanne De Maeyer, Ine Dirks, Yannick Brackenier 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The HECKTOR 2026 challenge benchmarks machine learning for head and neck cancer, where teams delineate primary and nodal tumour volumes, perform TN staging, and predict recurrence-free survival (RFS). This report describes the submissions for the HECKTOR challenge of team nucli. As the three tasks span both dense and global information from multicentric PET/CT scans, we utilise self-supervised pre-trained encoders, training a 2D DINOv2 encoder (PET-DINOv2-MIPs) on HECKTOR 2026's PET scans. Our final test submission ensembles a DynUNet trained from scratch with a SwinUNETR whose Swin trunk was initialised from a SimMIM-pre-trained checkpoint for segmentation, reaching a mean Dice of 0.5409. For TN staging, GTVp/GTVn geometric features from the segmentation masks are fit to stage probabilities by logistic regression (LR) and fused with PET-DINOv2-MIPs deep features (PCA + LR) via a second-level LR, reaching balanced accuracies of 0.3962 (T-stage) and 0.6432 (N-stage). For the RFS prognosis task, we fine-tune the last two blocks of the PET-DINOv2-MIPs ViT-S encoder jointly with an MLP head under a CoxPH loss, concatenating clinical covariates with the imaging features, reaching a test Harrell's C-index of 0.6577 and a weighted challenge score of 0.5802. The prognosis result is comparable to the best entry of the previous edition and consistent with our internal cross-validation, while our segmentation result is well below it and limits the staging results that depend on it.

---


### 355. [Agentic process evidence](https://arxiv.org/abs/2610.40071)

**<font color=#1a73e8>作者：</font>** Yuval Kainan, Carmit Hershman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The way software gets built is changing dramatically. AI agents now create pull requests, select dependencies, refactor codebases, interpret test failures, and execute infrastructure changes across the entire Software Development Life Cycle (SDLC). AI agents are autonomous team members, but unlike human engineers, they are ephemeral - their reasoning, decisions, and tool calls vanish the moment the session ends. Modern Security incidents involving intent mismatch or injection are becoming increasingly common - forcing us to address AI Agents as an insider threat. No widely adopted standard yet enables agentic provenance and governance and its obvious that you can't hold an ephemeral process accountable. The git log was designed for human commits. It shows what changed. It does not show what an AI agent did, which model it used, which tools it called, or whether anyone was accountable for the outcome. Every governance framework, every audit trail, every compliance control in the SDLC was built around one assumption: a human made the decision. That assumption no longer holds. This shift introduces 3 main procedural problems (not addressing scale) - Supply-chain vector - The agentic coder is software, so it is a supply-chain security risk. Policy guardrails - How to ensure the agentic coder is compliant with the policies of the organization. Task-alignment - How to align the agentic coder on its tasks and goals. We introduce Agentic Process Evidence (APE), a signed, tamper-evident, machine-readable attestation of agentic processes, linking the sessions to their outcome (process-aware logging). APE enables Policy-as-Code control over the agentic processes, allowing for human in the loop only when it's needed. We support the in-toto style attestation framework, and the protocol is aligned with the relevant regulations

---


### 356. [Uncertainty-aware Coarse-to-Fine Main Pancreatic Duct Segmentation for Width Measurement in 3D MRCP](https://arxiv.org/abs/2610.40073)

**<font color=#1a73e8>作者：</font>** Zipei Zhang, Jaakko Sahlsten, Mikko Saukkoriipi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Assessment of the main pancreatic duct (MPD) from volumetric magnetic resonance cholangiopancreatography (MRCP) scans is an essential task for ductal dilatation diagnosis and pancreatic cancer analysis. However, manual assessment is affected by reader variability in which automated analysis may assist. Nevertheless, fully automated and uncertainty-aware MPD analysis from volumetric MRCP remains underexplored area of research. In this study, we propose an automatic and uncertainty-aware deep learning-based pipeline for MPD segmentation and maximum-width analysis from MRCP scans. A coarse localisation model first identifies the ductal region-of-interest, followed by a fine model that segments the MPD within the region. The dataset consists of 256 MPD-segmented MRCP scans from 69 patients. A randomly selected holdout test subset of 14 patients with 55 MRCP volumes was used for evaluation. We employed a five-model cross-validation ensemble for improved performance and uncertainty estimation. The best MPD segmentation performance was 0.634 DSC, 0.744 precision, and 0.593 recall. The mean absolute error for maximum MPD width prediction was 0.355~mm and dilated MPD ($\geq 5$~mm) was detected with 75.0\% sensitivity and 74.4\% specificity. These novel results suggest that automated MPD segmentation can be used to aid MRCP-based duct measurements.

---


### 357. [Morphology-Aware Channel-Decoupled Mamba Network for Medical Image Segmentation](https://arxiv.org/abs/2610.40085)

**<font color=#1a73e8>作者：</font>** Chenchen Wang, You Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate multi-organ segmentation in computed tomography (CT) is essential for computer-aided diagnosis, treatment planning, and disease monitoring. However, substantial variations in organ shape and size, together with low tissue contrast and ambiguous boundaries, complicate the modeling of heterogeneous anatomical structures. To address these challenges, we propose a Morphology-Aware Channel-Decoupled Mamba Network (MCDNet), which integrates adaptive local structural enhancement with channel-decoupled long-range modeling. Specifically, we introduce a Morphology-Aware Channel-Decoupled State-Space (MCSS) block that divides feature channels into separate processing groups, allowing differentiated structural representations to be learned within an efficient state-space framework. Within each group, a Morphology-Aware Enhancement Module (MAEM) combines deformable convolutions with channel attention to adapt local feature extraction to anatomical shape variations. Group-wise state-space modeling then captures long-range spatial dependencies, and channel gating adaptively integrates the resulting features. Experiments on the Synapse abdominal CT dataset demonstrate the effectiveness of MCDNet, achieving an average Dice Similarity Coefficient of 81.61% for multi-organ segmentation.

---


### 358. [Neural Blind Deconvolution for Image Scanning Microscopy](https://arxiv.org/abs/2610.40088)

**<font color=#1a73e8>作者：</font>** Eliot Guez, Nathan Buskulic, Lisa Cuneo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image scanning microscopy (ISM) acquires one scanned image per detector element, which are then fused into a single image by multi-image deconvolution to obtain a super-resolved image. Its accuracy, however, depends on point spread function (PSF) models that sample- and system-induced aberrations often invalidate. Since differences between the scanned images encode aberration information, we propose a training-free blind Deep Image Prior (DIP) framework that jointly estimates the specimen and the detector-dependent PSFs. The PSFs are parametrised through the detector geometry and shared excitation and emission PSFs, reducing the unknowns while preserving the physical ISM model, and a Gaussian pre-initialisation stabilises the blind optimisation. On experimental tubulin data, blind DIP recovers finer filamentous structures than multi-image deconvolution and DIP with fixed theoretical PSFs, while adapting the PSFs to the measurements.

---


### 359. [Reward-Adaptive Co-Evolution of Policy and Rubric](https://arxiv.org/abs/2610.40096)

**<font color=#1a73e8>作者：</font>** Yizhu Chen, Jianguang Jiang, Jiameng Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rubric-based rewards provide fine-grained, interpretable supervision for open-ended reinforcement learning, where holistic scalar rewards struggle to capture multidimensional response quality. Static rubrics can lose discriminative power as the policy distribution evolves, while existing policy--rubric co-evolution methods rely on globally prescribed update schedules that ignore heterogeneous reward informativeness. We introduce RACE, a Reward-Adaptive Co-Evolution framework. At the group level, per-rollout-group training-signal routing classifies groups as informative, diversity-collapsed, or rubric-failed, updating the policy only with informative groups while caching rubric failures. At the phase level, event-triggered phase switching enters rubric optimization upon persistent reward saturation and returns when rubric-reward improvement plateaus. Rubric phases train the generator on cached pairs using a frozen judge and a scale-normalized pairwise-margin reward. Across both levels, online threshold adaptation adjusts routing and switching thresholds through proportional control. Under a unified evaluation protocol, RACE achieves the highest average performance and outperforms the strongest fixed-alternation baseline on all eight tasks, while improving rubric discrimination.

---


### 360. [Apple Vision Pro: The good, the bad, the ugly](https://arxiv.org/abs/2610.40108)

**<font color=#1a73e8>作者：</font>** Santiago Berrezueta-Guzman, Andrei Koshelev, Habiba-Loai Khalil 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Apple Vision Pro (AVP), the headset Apple introduced as its first ``spatial computer,'' built by a single, vertically integrated vendor, entered the market in February 2024 and has since accumulated a fast-growing body of primary research spanning surgery, education, accessibility, design, and human-computer interaction. In this paper, we adopt the tripartite structure of Leone's 1966 film to organize a systematic review of this literature: we cataloged the validated, working applications of AVP (the good), the persistent technical and ergonomic limitations of a still-early-generation headset (the bad), and the ethical concerns and structural harms that follow from deliberate design, marketing, and deployment choices (the ugly). The review is built from a Scopus export of 218 records mentioning AVP, which we narrowed to 104 papers (2024--2026) with a primary focus on AVP, using explicit inclusion/exclusion criteria that we report in full, alongside a PRISMA-informed flow diagram of the screening process. We find the corpus heavily skewed toward validating benefits (medicine and surgery, education, and software tooling account for over half of the included papers) and comparatively thin on documented risks or misuse, a pattern we treat as a finding in its own right rather than a limitation to be explained away. We further show that several recurring issues, namely price, simulated social presence, and the gaze-tracking privacy architecture, resist a clean separation into ``bad'' or ``ugly'' using the published evidence alone, since both readings remain compatible with the same data. We close by identifying where the evidence base most needs to grow: independent risk and ethics research, bystander- and equity-focused study designs, and disclosure that would let researchers distinguish an engineering backlog from a structural choice.

---


### 361. [Coupled Guidance for Flow Matching](https://arxiv.org/abs/2610.40109)

**<font color=#1a73e8>作者：</font>** Mateo Clémente, Léo Maxime Brunswic, Rui Heng Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Guidance methods are essential tools for steering the generation process in diffusion models, improving the generalizability of stochastic robotic controllers and enabling high-quality controlled image synthesis. Despite strong parallels between flow-matching and diffusion, integrating guidance into flow-matching models remains quite challenging. Recent work has proposed general guidance frameworks for flow-matching, however, they are direct adaptations of diffusion guidance methods and can prove unstable. In this work, we conduct a theoretical analysis of guidance in flow-matching and show that a naive translation of diffusion-based guidance to flow-matching breaks the coupling distribution used during training, resulting in weaker control over sampling accuracy. Building on this insight, we propose Coupled Guidance, a flow-matching-specific guidance mechanism derived from a geometric perspective that leverages the coupling structure inherent to flow-matching training. To validate the effectiveness of our approach, we conduct extensive experimentation on a custom robotic collision avoidance task using ManiSkill3, four robotic dexterous manipulation tasks from the Adroit benchmark, and three image generation tasks, namely inpainting, super-resolution, and deblurring, using the ImageNet-128 and CelebA-HQ-256 datasets. Our findings show that our framework improves sample quality and guidance stability across all tasks, without imposing any additional overhead.

---


### 362. [D-MOD: Diffusion mode estimation for accelerated MRI](https://arxiv.org/abs/2610.40110)

**<font color=#1a73e8>作者：</font>** Md Kawsar Ahmed, Mathews Jacob  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models are powerful priors for accelerated MRI reconstruction, but most current methods are posterior samplers, which return a random draw from the posterior. A reproducible and high-quality reconstruction often requires averaging many samples, resulting in a high computational cost. We introduce D-MOD, a fast algorithm that instead provides a posterior mode. It uses a minorize-maximize algorithm on a lower bound of the smoothed log-posterior, which provably increases the objective. Each iteration draws S noisy samples of the current estimate at the current noise level, denoises them with a pretrained diffusion model, and combines their average with the measured k-space through a conjugate-gradient (CG) solve. We anneal the noise levels, as the distance between the bound and its target decays quadratically with noise. On fastMRI brain (T1, T2, FLAIR), a single D-MOD reconstruction exceeds, in PSNR, the 10-sample finite-MMSE estimates of DPS, DAPS and SNORE-P and stays within 0.31 dB of the strongest baselines (DiffPIR, DDS). This approach thus provides a fast deterministic reconstruction algorithm (11-73 times faster than MMSE estimates), which is useful in a clinical setting.

---


### 363. [SynthFaces: Balanced Large Scale Human Dataset](https://arxiv.org/abs/2610.40119)

**<font color=#1a73e8>作者：</font>** Sergey Karpukhin, Denis Bobkov, Kirill Morozov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The pursuit of fair and equitable AI in human-centric tasks is critically hindered by the inherent biases and privacy risks of real-world datasets, which offer imbalanced representations of identity and often contain sensitive personal information. Consequently, state-of-the-art generative models trained on this skewed data exhibit unfair performance, particularly in identity-preserving generation. In this work we propose a pipeline for controllable generation of dataset with diverse faces for generative models training and finetuning. We achieve this by expanding foundational Arc2Face diffusion model with a flow matching generative model in the manifold of identity embeddings. We demonstrate that such approach achieves both goals of generative fidelity and label diversity not present in real human-centric datasets. As a result we collect and further contextualize a highly balanced identity-centric dataset of humans named SynthFaces. By design, our released images and identities are synthetic, reducing direct reliance on real personal images; we empirically check identity separation with a nearest-neighbor non-leakage metric. We purpose it for training and tuning of fair models for various downstream tasks, and showcase its usability in finetuning an existing adapter-based method for personalized generation.

---


### 364. [Learning a Motion Manifold to Constrain Ambiguity in Unsupervised 4D Medical Image Interpolation](https://arxiv.org/abs/2610.40121)

**<font color=#1a73e8>作者：</font>** Haojin Li, Huazhu Fu, Heng Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised 4D medical image interpolation reconstructs intermediate anatomical states from temporally sparse observations without intermediate supervision. Distinct motion fields may attain comparable endpoint agreement while producing different intermediate anatomy, giving rise to motion ambiguity. This ambiguity is difficult to constrain when many independently adjustable motion variables must be estimated from the observed endpoints. We develop a framework that learns a motion manifold to restrict candidate motion fields while retaining sample-specific variation. Cross-Sample Spectral Basis Learning extracts recurring motion structure from endpoint-derived dense estimates and encodes it in a shared spectral basis. Sample-Conditioned Cayley Basis Reorientation uses predicted motion coordinates to rotate the effective motion directions for each endpoint pair without increasing the number of independent coordinates. Their composition defines a nonlinear family of complete velocity fields across endpoint pairs, accommodating anatomical and motion-state differences within a restricted representation. Integrating each predicted field supports bidirectional reconstruction at arbitrary intermediate times. Theoretical analysis establishes sufficient conditions under which endpoint observations distinguish nearby motions within the learned family. Experiments on ACDC and 4D-Lung demonstrate state-of-the-art performance among the evaluated methods trained without intermediate volumes and competitive results against methods using intermediate supervision.

---


### 365. [Does System Size Matter in Uncertainty Quantification for Machine Learning Interatomic Potentials?](https://arxiv.org/abs/2610.40126)

**<font color=#1a73e8>作者：</font>** Chayaphol Lortaraprasert, Nontawat Charoenphakdee, Wenwen Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learning interatomic potentials (MLIPs) commonly use uncertainty estimates to flag out-of-distribution (OOD) configurations and select structures for active learning. A key question is whether the resulting structure-level uncertainty scores remain comparable across different system sizes. A common practice is to aggregate per-atom uncertainties by their mean or maximum and compare the resulting score against a fixed threshold, implicitly assuming such comparability. We test this assumption across several in-distribution (ID)/OOD pairs by characterizing both aggregations as a function of atom count. The two aggregations exhibit distinct size dependencies. Mean aggregation remains size-independent for homogeneous systems but loses sensitivity to defects in large cells. In contrast, maximum aggregation grows with system size for ID systems while remaining approximately flat for defect-containing systems, narrowing the ID-OOD gap in a manner consistent with extreme-value statistics. Although highly uncertain atoms in large structures may indicate novel local environments, retraining on these structures yields little improvement, in contrast to retraining on OOD structures constructed to lie outside the training distribution. Our results reveal a practical limitation of size-unaware uncertainty criteria and motivate size-aware calibration for more reliable OOD detection in large-scale atomistic simulations.

---


### 366. [Escaping Path Mirages in Offline Goal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2610.40130)

**<font color=#1a73e8>作者：</font>** Junhyeon Bae, Jaebak Hwang, Gwanwoo Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline goal-conditioned reinforcement learning remains challenging in stochastic long-horizon settings, where compounding value estimation errors hinder reliable goal reaching. While prior methods have sought to address this challenge through various approaches, a key challenge remains path mirage, where agents overcommit to spuriously successful trajectories in offline datasets induced by stochasticity, often leading to failure on difficult tasks. To address this issue, we propose Branch-aware Graph Planning (BGP), which captures stochastic branching structures by identifying high-variability points as graph nodes and designing goal-conditioned edges with segmented learning to avoid unreliable branches and reduce unnecessary stochasticity along paths. As a result, BGP enables reliable goal reaching even in highly stochastic long-horizon environments, and experiments on diverse OGBench tasks show that it substantially outperforms prior state-of-the-art offline goal-conditioned RL methods. Our implementation is available at this https URL.

---


### 367. [DynaRev: Benchmarking Web Agents under Dynamic Goal Revision](https://arxiv.org/abs/2610.40133)

**<font color=#1a73e8>作者：</font>** Shiqi Zhang, Guochen Zhou, Zesheng Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Web agents are typically evaluated with goals fully specified before execution and fixed thereafter, whereas real users often revise their requirements during interaction. To study such interactions, we introduce DynaRev, a benchmark of 181 tasks to evaluate web agents under dynamic goal revision. DynaRev uses semantic milestones to deliver revisions at task-defined stages, covers additive revisions, unconditional overrides, and runtime-conditioned overrides, and evaluates correctness, responsiveness, and efficiency through trajectory-grounded evaluation. Five-model evaluations show that agents often satisfy only part of the task requirements, with performance varying across task sources, revision types, and models. Further analyses reveal varied milestone timing, mixed effects of dynamic delivery, and contrasting revision-handling outcomes, with gains from instruction rewriting while preserving browser state and losses from browser resets. DynaRev provides a testbed for studying how web agents adapt to evolving user goals. The code and data are available at this https URL.

---


### 368. [NeurEO: dissecting Earth observation embeddings with computational neuroscience](https://arxiv.org/abs/2610.40137)

**<font color=#1a73e8>作者：</font>** Thijs L van der Plas, Jacob JW Bakermans, Ioannis N Athanasiadis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Earth embeddings are compressed representations of rich Earth observation data that enable downstream models to tackle a wide range of complex geospatial tasks. Yet, this increase in performance comes at the cost of decreased interpretability, as the semantic meaning of Earth embeddings is unknown. To address this challenge, we borrow methods from the field of computational neuroscience, which aim to interpret activity in (biological) neurons. Here, we adapt and apply these methods to assign meaning to AlphaEarth embeddings. We analyse embedding features both as stand-alone data, equivalent to spontaneous neural activity, and in relation to land cover and elevation correlates, equivalent to stimulus-response neural activity. We demonstrate correlational and multi-scale structure in the embedding features. Embedding features can display highly specific and directional tuning to land cover and elevation, such as a `North vs South woodland edge' response. When we remove the main trends of combined land cover responses (like water versus land tuning), we discover fine-grained representational details with increased effective dimensionality. Together, our analyses start to unravel what these Earth embeddings represent, which is critical for developing trustworthy downstream applications.

---


### 369. [A Deep Learning Framework for Quantile Demand Forecasting in E-commerce with Doubly Censored Data](https://arxiv.org/abs/2610.40138)

**<font color=#1a73e8>作者：</font>** Ziwen Ye, Jiawen Wei, Teng Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, a growing number of online retail companies have embraced deep learning models for demand forecasting, leveraging their scalability in processing large-scale datasets. Accurate demand forecasts enable improved planning and allow operational flexibility to adjust sales accordingly. Moreover, quantile estimation has gained widespread application as it offers valuable uncertainty quantification, thereby enhancing the robustness of decision-making processes. However, limited research has addressed the effective quantification of uncertainty when target labels are ambiguous. In retail, actual sales can be capped by stock and boosted by temporary promotions, whereas the target is underlying demand. Such scenarios are characterized by double censoring and no deep-learning pipeline yet exists for such data. In this paper, we introduce a straightforward framework for learning quantiles from doubly-censored observations and propose a tailored evaluation metric. Our approach is supported by theoretical guarantees, and we empirically demonstrate that our metric correlates well with the oracle calibration measure. Experimental results show that our estimator surpasses existing baselines. Finally, inventory simulations and real-world applications confirm the practical utility of our method in retail operations.

---


### 370. [FARE: Factor-Aware Retrieval with Error-Guided Fusion for Retail Forecasting](https://arxiv.org/abs/2610.40160)

**<font color=#1a73e8>作者：</font>** Chenghao Gu, Zhuokang Shen, Shenghao Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retail sales forecasting underpins inventory planning, yet promotions and calendar events reshape short-term demand. Although each factor usually has historical occurrences, the complete factor combination of a target week often has few precedents. The challenge is therefore to retrieve informative partial matches and weight them by their reliability, which varies across series. We propose FARE(Factor-Aware Retrieval with Error-Guided Fusion), which ranks historical weeks separately for each known target-week factor and merges the selected weeks into a factor reference under a fixed budget. Guided by shrunk errors from completed development weeks and the current disagreement among candidates, a first gate mixes this factor reference with a shape reference from similar sales histories, and a second gate controls how strongly the mixture corrects a backbone forecast. Both gates remain fixed during testing. On Favorita, M5, Rossmann, and Rohlik, FARE reduces the weighted absolute percentage error (WAPE) of five backbones by 11.46%, 4.06%, 14.63%, and 10.16% on average. With Chronos-2 frozen, FARE also outperforms conventional and existing enhancement methods, including supervised residual correction and retrieval augmentation. Code is available at this https URL .

---


### 371. [Closing the Log Gap: Minimax-Optimal Regret for Episodic RL](https://arxiv.org/abs/2610.40165)

**<font color=#1a73e8>作者：</font>** Guy Zamir, Victor Boone, Matthew Zurek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we study the regret minimization problem in episodic tabular MDPs. Our algorithm achieves the first expected regret bound scaling as $\sqrt{H^3 S A K}$ for sufficiently large $K$, where $H$ is the episode length, $K$ is the number of episodes, and $S$ and $A$ are the numbers of states and actions, respectively. Our method is the first to match the minimax lower bound \emph{without extra polylog factors}. We introduce a variant of UCBVI which does not maintain strictly optimistic estimates, and uses MOSS-style exploration bonuses whose logarithmic terms adapt to both visit counts and estimated variances. A key challenge is controlling the propagation of errors caused by under-optimism, which we accomplish in an occupancy-weighted way, avoiding logarithmic overhead that would be incurred by uniform-over-rows concentration. Our analysis develops time-uniform and variance-aware concentration bounds that may be of independent interest. As a corollary we also develop an algorithm for $(\varepsilon, \delta)$-PAC best-policy identification, which is the first to match the $\Omega\big(H^3 SA\log(\frac{1}{\delta})\varepsilon^{-2}\big)$ minimax lower bound up to constants in some regimes.

---


### 372. [EventSeeColor: Learning to Reconstruct Color from Monochrome Events](https://arxiv.org/abs/2610.40166)

**<font color=#1a73e8>作者：</font>** Chuanzhi Xu, Langyi Chen, Haoxian Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras capture visual brightness changes under challenging lighting conditions. However, traditional event-based image reconstruction targets grayscale intensity and produces images without scene color. Color distinguishes surfaces with similar intensity. Reconstructing color from events can reveal appearance differences that reconstructed grayscale images cannot express. Although monochrome event cameras do not directly measure color, their event-triggering patterns depend on surface reflectance, illumination, and the sensor's spectral response. These patterns may contain cues that support color reconstruction. In this paper, we present EventSeeColor, which uses event-reconstructed grayscale and aligned events to jointly guide a diffusion colorizer. Grayscale-derived semantic context supports color inference, while region-balanced chroma supervision and local RGB refinement improve color distribution, brightness, and texture. In the combined evaluation on two real event datasets, EventSeeColor achieves the best structural similarity, learned perceptual scores, and chromatic-region color difference among the external methods.

---


### 373. [Beyond CCT: Multi-channel SPD recovery for per-shot camera color correction](https://arxiv.org/abs/2610.40175)

**<font color=#1a73e8>作者：</font>** Shuwei Yue, Hongke Wei, Qiao Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern cameras correct color via two or three pre-calibrated 3x3 matrices interpolated by Correlated Color Temperature (CCT). This collapses the illuminant SPD to a scalar. LEDs, fluorescents, and mixed sources sit off the Planckian locus, and metameric illuminants with the same chromaticity demand different optimal CCMs that a CCT pipeline cannot distinguish. We recover the illuminant SPD instead using non-negative least squares against a basis dictionary, conditioned on the camera white point and a multi-channel ambient-light sensor (ALS). A closed-form 3x3 CCM is then fit per shot. On a synthetic benchmark of 300 illuminants and 3,100 reflectances, mean angular error drops from 1.89 to 1.20 degrees, with a 1.7x tail reduction on the LED-like off-Planckian group (n=45) where metameric ambiguity is tangible. The gain holds under realistic ALS imperfections and observation noise, and the same off-Planckian advantage carries over to 1,684 real measured SPDs.

---


### 374. [Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement](https://arxiv.org/abs/2610.40191)

**<font color=#1a73e8>作者：</font>** Liaoyuan Fan, Yuhao Zheng, Dongxing Mao 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation is shifting from end-to-end synthesis toward agentic generation, where planning, tool use, and feedback enable coherent, controllable multi-shot videos. In parallel, video world models provide action-conditioned observations and predicted futures, serving as interactive environments for agents. We study their intersection through the agent harness: an executable runtime that constructs context, exposes tools, maintains state, routes feedback, and manages budgets around video models. This report examines three directions. First, agentic video generation, where harnesses coordinate scripting, shot planning, asset management, production, and editing, alongside the evaluation challenges of these systems. Second, agentic world modeling, where harnesses mediate observation, control, execution, and state. We discuss hybrid designs in which game engines or agent-written programs maintain world state while video models render observations, and how agents and world models can mutually evaluate and improve one another. Third, recursive self-improvement (RSI) in video model development, distinguishing output revisions, updates to harness state, generator parameters, and evaluators, and changes to the improvement procedure itself. We identify how these improvements feed back into subsequent development. Across these directions, we analyze essential agent capabilities, including audiovisual perception, long-horizon planning, memory, code-based interaction, feedback-guided control, skill reuse, and multi-agent coordination. We conclude with challenges in autonomous video production, lifelong memory, programmable hybrid control, autonomous model development, provenance, cost accounting, and evaluation linking video quality and task performance to sustained improvements in models and harnesses.

---


### 375. [Attack-Resilient Multi-Bit Image Watermarking Framework via Latent Coordinate Sign Clamping](https://arxiv.org/abs/2610.40204)

**<font color=#1a73e8>作者：</font>** Marjan Beheshti, Ronghua Xu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Watermarking is essential for image copyright protection and attribution, yet existing methods suffer from fundamental trade-offs among post-hoc applicability to pre-existing images, multi-bit capacity, training-free deployment, and adversarial resilience. To address these limitations, we propose a training-free watermarking framework that exploits the overcompleteness of diffusion latent spaces to embed multi-bit payloads into arbitrary images while preserving high visual quality. Additionally, we develop a three-layer decoding pipeline that combines magnitude-weighted majority voting, BCH, and Chase decoding to maximize message-extraction accuracy in the presence of channel noise. To counter active adversaries, our framework integrates a steganalysis-resistant noise camouflage layer and a dual-layer forgery defense that combines perceptual hashing with a Reed-Solomon fuzzy commitment scheme over CLIP features. Empirical evaluations demonstrate that our method applies to both natural and AI-generated images with a scalable $32\text{--}128$-bit capacity. Furthermore, it effectively mitigates advanced removal vectors ($94.6\%$ decode rate against CtrlRegen+ regeneration attacks) and secures robust forgery detection ($98.8\%$ accuracy via joint CLIP and RS fuzzy commitment mechanism).

---


### 376. [DYNAS: A Dynamic Network Penetration Testing Framework Using Deep Hierarchical Reinforcement Learning](https://arxiv.org/abs/2610.40214)

**<font color=#1a73e8>作者：</font>** Md. Rakibul Hassan, Majedul Islam, Md. Ashraful Alam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As network scale and uncertainty complicate automated penetration testing, reinforcement learning (RL) environments must support controlled evaluation under defensive and non-stationary conditions. We present DYNAS (Dynamic Network Attack Simulator), which combines parameterized large-scale scenario generation with stateful intrusion detection responses, explicit scan false-positive and false-negative noise, temporary service unavailability, and duration-based action timeouts. We further introduce Pen-DHRL, a recurrent manager--worker policy that selects persistent subgoals using IDS-conditioned global context. We compare Pen-DHRL with GNN, Invariant, and Attention baselines across four scenario variants and multiple training regimes. Under IDS-disabled training followed by IDS-enabled evaluation, Pen-DHRL obtains approximately 64\% and 24\% higher reward per step on Bridge and Dynamic, respectively, and approximately 26\% and 30\% more captured hosts on VarA and VarB than the next-best baseline. With all defensive dynamics active from the beginning of training, Pen-DHRL achieves positive mean episode returns in all four scenarios, whereas the flat baselines produce negative mean returns in all 12 architecture--scenario combinations; staged curriculum training produces positive mean returns across all 16 evaluated combinations.

---


### 377. ["It Feels Weird to Just Rely on AI": How Experienced Healthcare Professionals Work With Decision Support Systems in Clinical Practice](https://arxiv.org/abs/2610.40224)

**<font color=#1a73e8>作者：</font>** Simon W.S. Fischer, Hanna Schraffenberger, Miranda L. van Hooff 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Decision support systems (DSS) assist with clinical decision-making. Little is known, however, about the decision-making process with DSS in clinical practice and the extent to which clinicians consider or rely on the predictions. Studies on human-AI decision-making usually focus on laypeople, simplified decision tasks, or one-shot interactions with prototypes that are not integrated into existing workflows. To gain insights from real-world practice, we conducted an online survey (n=12) and semi-structured interviews (n=10) with clinicians from two different medical cohorts each working with a DSS. Findings show, amongst other things, that the interaction with DSS changes as experience increases, the predictions become more important in complex cases, that decisions are discussed with colleagues, and that workflow integration affects decision-making. Our findings on human, technical, contextual, and organisational factors contribute to a socio-technical perspective on DSS reliance behaviour. We conclude by discussing the implications of our findings for the design of DSS.

---


### 378. [Reaction precedents extend retrosynthetic prediction beyond training coverage](https://arxiv.org/abs/2610.40249)

**<font color=#1a73e8>作者：</font>** Jiaxing Sun, Xuli Shen, Jiang Wu 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reaction precedents guide retrosynthesis, but how far they can compensate for gaps in task-specific training coverage remains unclear. Using 2.71 million reactions, we restricted training and retrieval coverage by transformation or time, then expanded only the retrieval corpus with model parameters fixed. For transformations excluded from training, mean Top-1 accuracy increased from 13.0% to 58.0% on a historical test set and from 4.9% to 23.1% on a temporally held-out test set. For temporal coverage gaps, retrieval expansion enabled a model trained on records before 2017 to match or exceed a non-retrieval model trained on records before 2025 on both test sets. Without task-specific fine-tuning, precedents improved all 14 representative general-purpose models on both test sets and USPTO-50K; the strongest with precedents surpassed all eight representative specialized models. These findings show that inference-time reaction precedents can extend retrosynthetic prediction beyond task-specific training coverage without parameter updates.

---


### 379. [Learned Terminal Costs for Short-Horizon Model Predictive Control of Autonomous Trucks in Interactive Highway Traffic](https://arxiv.org/abs/2610.40257)

**<font color=#1a73e8>作者：</font>** Hooman Hamze, Benjamin Houshmand, Deepthi Pathare 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous highway driving for heavy-duty trucks is a challenging control problem. The greater mass, dimensions and intricate dynamics increase the requirements for cooperation from surrounding traffic in critical maneuvers, requiring a careful balance between safety constraints and efficient long-horizon decision making. Model Predictive Control (MPC) provides rigorous constraint satisfaction but relies on terminal cost which can limit its effectiveness at short, computationally affordable horizons. Reinforcement Learning (RL) captures long-term driving behavior but offers no constraint guarantees and tends toward overly conservative policies when trained under sparse collision penalties. In this paper, we propose a hybrid MPC and RL framework for highway driving in autonomous trucks, where a finite-horizon MPC, solved via dynamic programming, uses a pre-trained RL model for terminal cost estimation. We evaluate the framework in a simulation environment with reactive surrounding traffic and compare it against pure MPC with zero terminal cost, rollout with terminal cost estimation using a base policy, and pure RL. Results show that the hybrid approach achieves zero collisions with the lowest cost of any configuration.

---


### 380. [From MS/MS evidence to adaptive spectroscopic characterization: Reinforcement learning guided by candidate molecular structures](https://arxiv.org/abs/2610.40264)

**<font color=#1a73e8>作者：</font>** Bowen Gao, Lei Zhu, Yiying Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small-molecule identification from tandem mass spectrometry (MS/MS) may require complementary measurements. Herein, we propose a structure-informed deep Q-network (SI-DQN) that uses existing MS/MS evidence to decide whether further characterization is needed, which measurement to request, and when to stop. The policy combines spectral representations and candidate rankings with score-weighted descriptors of the candidates' chemical features and structural differences. The policy was evaluated on 79,462 held-out samples with simulated MS/MS, infrared (IR), and nuclear magnetic resonance (NMR) spectra from the Multimodal Spectroscopic Dataset. Evaluation used fixed hard candidate sets containing the correct structure and equal normalized acquisition costs. Averaged across three training runs, SI-DQN increased Top-1 accuracy from 80.10% to 93.78% for positive-ion MS/MS starts and from 70.44% to 93.31% for negative-ion starts. The corresponding mean additional measurement counts were only 0.227 and 0.340 per sample, respectively. Complete acquisition achieved 97.72% accuracy with four additions, whereas SI-DQN reduced the additional measurement count by 94.3% and 91.5%. Relative to a rule-based policy, SI-DQN reduced the composite loss combining terminal ranking error and acquisition cost by 19.3% and 25.5%. Adding structural information to DQN further improved accuracy while reducing requests across all three training runs. At comparable ranking uncertainty, SI-DQN increased request rates relative to DQN more strongly in groups with high structural disagreement, where larger reductions in composite loss were also observed. Together, these results support using the ambiguity among candidate structures after MS/MS analysis to guide further characterization, providing a quantitative basis for balancing identification performance against subsequent measurement effort.

---


### 381. [Latent Prediction Yields Cross-Subject Alignable Representations in Sensory-Evoked fMRI](https://arxiv.org/abs/2610.40280)

**<font color=#1a73e8>作者：</font>** Serwan Jassim, Victoria Bosch, Daniel Anthes 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decoding sensory-evoked functional magnetic resonance imaging (fMRI) data is a central analytical tool in cognitive neuroscience. Here we ask whether self-supervised learning (SSL), which has been scarcely explored in this domain, can yield representations that support strong downstream performance. To do so, we adapt a joint embedding predictive architecture (JEPA) to train participant-specific encoders on brain data alone. The encoders never see the stimulus images or any representation derived from them. Applied to the Natural Scenes Dataset (NSD), we evaluate our learned brain embeddings on the downstream tasks of brain captioning and image reconstruction, as well as cross-participant generalization. Our self-supervised approach achieves competitive performance with parameter-rich supervised pipelines that are trained end-to-end with access to image and language data. We further find that encoders trained independently for different participants can be aligned fully unsupervised, using neither images nor stimuli shared between them. After alignment, a neural decoding head trained on one participant can be applied to another without fine-tuning and retains most of its within-subject performance on image reconstruction and brain captioning. By removing the need for images and shared stimuli, our approach is a step towards pooling fMRI data across participants and, eventually, across datasets.

---


### 382. [LoRe-MIM: Lost-or-Replaced Masked Image Modeling for Self-Supervised Representation Learning in Whole-Body PET/CT](https://arxiv.org/abs/2610.40284)

**<font color=#1a73e8>作者：</font>** Amartya Bhattacharya, Bashirul Azam Biswas, Biratal Raj Wagle 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models for whole-body positron emission tomography/computed tomography (PET/CT) hold significant clinical potential for disease detection, treatment planning, and response assessment. However, the time and cost associated with expert annotations remain major bottlenecks in developing robust and generalizable models. Although self-supervised learning (SSL) has emerged as a promising approach to mitigating annotation scarcity, its application to whole-body PET/CT remains relatively underexplored due to the limited availability of large-scale datasets and the challenges associated with learning complementary cross-modal representations. To address these limitations, we curate a heterogeneous, multi-tracer, multi-institutional cohort comprising 6,531 whole-body PET/CT scans and propose LoRe-MIM (Lost-Or-Replaced Masked Image Modelling), a novel self-supervised framework designed to learn multimodal representations through masked image reconstruction. Specifically, LoRe-MIM introduces a masking strategy in which image regions are either replaced with zeros (Lost) or substituted with corresponding complementary imaging modality (Replaced), encouraging the model to capture both modality-specific characteristics and cross-modal relationships. We evaluate the learned representations across multiple downstream tasks, including multimodal PET/CT image reconstruction, patch-based classification into cancer vs. non-cancer, whole-body lesion segmentation, label-efficient training, and robustness assessment. Experimental results demonstrate that LoRe-MIM consistently outperforms the corresponding state-of-the-art baselines across these tasks, highlighting its potential as a scalable and generalizable self-supervised learning framework for whole-body PET/CT analysis.

---


### 383. [Self-training for cross-centre coronary vessel segmentation in X-ray angiography using pre-contrast frame subtraction](https://arxiv.org/abs/2610.40302)

**<font color=#1a73e8>作者：</font>** Danial Moafi, Aida Moafi, Mostafa Aryafar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models for coronary vessel segmentation in X-ray angiography often perform poorly on data from centres that were not represented in training. Apart from differences in equipment, the labels of the largest public dataset (ARCADE) are incomplete, as only the segments defined in the SYNTAX score are annotated. In this study, we evaluated whether self-training with pseudo-labels can improve performance on external data without additional manual annotation. Pseudo-labels were generated from two sources, namely the predictions of an nnU-Net model trained on ARCADE and a contrast map obtained by subtracting a pre-contrast frame from the same sequence. The nnU-Net predictions were extended along the contrast map, and pixels detected only in the subtraction image were assigned an ignore label and excluded from the loss. Six models were trained and tested on ARCADE and on two external datasets (XCAD and XACV). All first-round models initialised with the baseline predictions performed better than both the baseline and a control model fine-tuned for the same number of epochs. The model trained on the XCAD pool improved the macro-averaged Dice score by 2.7 points (95% CI 2.3-3.2), while the control decreased it by 0.6 points. A second round of self-training did not lead to further improvement. When an external model trained on 50 fully annotated images was used to generate the initial labels, the XCAD Dice score increased from 0.623 to 0.745 without any XCAD labels, although performance on XACV did not improve because large main vessels were missed. These results suggest that the benefit of self-training depends largely on the sensitivity of the model used to generate the initial pseudo-labels.

---


### 384. [Causal-prior-constrained deep learning for rapid-intensification warning of western North Pacific tropical cyclones](https://arxiv.org/abs/2610.40304)

**<font color=#1a73e8>作者：</font>** Xinrui Li, Yijun Jin, Yifan Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rapid intensification (RI) is one of the most dangerous and unpredictable phases of tropical cyclones, and its environmental and structural drivers are difficult to identify and separate in observations. Here we introduce CausalVisionRI, a causal-prior-constrained deep-learning system for 24-h RI warning in the western North Pacific. It integrates infrared remote sensing imagery, atmospheric and oceanic fields, and an observationally discovered causal graph into a unified model. The graph and eight sign-verified effects on 24-h intensity change provide an auditable causal prior for training. Discovered from 522 cyclones in 2000-2017, it identifies causal pathways linking atmospheric and oceanic conditions, the cyclone's dynamical and structural state, and its 24-h intensity change. On a forward holdout covering 2020-2024 and 3,004 records, the five-member ensemble achieves a Brier skill score (BSS) of 0.259 relative to a fixed development climatology, significantly exceeding four reference systems; the three LDA baselines reach at most 0.105. It also attains higher detection rates than a published knowledge-block scheme and a reconstructed contrastive-learning scheme at matched false-detection rates under our USA 30-kt standard and the published RITCF standard. Ablations show that the graph pathway adds 0.032 BSS across the holdout and 0.063 over 2020-2021, with a significant contribution in one ensemble member. A deep-learning model constrained by observationally discovered causal structure thus offers a new route to physically informed RI warning.

---


### 385. [Crowds Believe in You: Online Prediction Markets Overestimate How Often People Achieve Their Own Goals](https://arxiv.org/abs/2610.40324)

**<font color=#1a73e8>作者：</font>** Zihan Chen, Lei Nico Zheng, Di Zhu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People increasingly share personal goals online and invite others to forecast them. Research on the planning fallacy finds that observers predict a person's behavior less optimistically than the person does, and prediction markets aggregate such judgments, harnessing the wisdom of crowds. We study 6,150 prediction markets on Manifold in which 1,660 users asked about their own futures ("Will I ...?"), reconstruct every order and execution, and compare these self-markets with markets about external events. Self-markets resolved YES 4.4 percentage points less often than their final prices implied, whereas external markets were nearly calibrated (0.9 points); the difference was 2.2 points at the same price level and 1.9 points within creators who made both kinds of market. Absent when markets opened, the overstatement emerged within a day of trading, even where the person never traded, and peaked in the week before close. In a market's first day, observers moved external-market prices down toward the base rate, but moved self-market prices 3.6 points further toward YES, except in markets naming an outcome the person would not want, which were not overpriced. The correction came late and largely from the person, whose orders supplied 38% of the eventual movement toward the outcome in self-markets, against 9% in external markets. Because self-market prices mainly failed to separate successes from failures, a recalibration learned from earlier markets improved later forecasts by only 1.5%. Crowds believe in the futures people pose for themselves, and the information that would correct them lies with the person.

---


### 386. [How to Loop Your Transformer: Loop Scaling, Specialization, and Parallel Inference](https://arxiv.org/abs/2610.40325)

**<font color=#1a73e8>作者：</font>** Chanakya Ekbote, Artidoro Pagnoni, Devendra Singh Sachan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looping in transformer models reuses weights by repeatedly applying the same transformer, or parts of it, making the model deeper without increasing its parameter count. Whether looping is useful depends on which constraint dominates: model size, training compute, or autoregressive inference efficiency. We study these trade-offs jointly in dense decoder-only transformers trained from scratch, varying which parts of the model are looped, how many loops are applied, and how information is passed between loops. Our experiments span models with up to 1B parameters, trained on up to 155B tokens with up to $1.07\times10^{21}$ FLOPs and 32 loops. We find that looping the full transformer generally gives the strongest quality at a fixed parameter budget, whereas looping a middle block of layers gives a better return when training FLOPs are constrained. Adding loops is not uniformly beneficial: gains eventually saturate, reverse, or become unstable. This motivates asking whether forcing every loop to use the same weights limits the benefit of deeper looping. We address this by adding small loop-specific low-rank adapters that improve quality, with larger gains as more loops are added. Looped transformers also suffer a decoding slowdown proportional to the number of loops. Parallel Loop Transformers address this by passing hidden states between loops across adjacent token positions, allowing loop stages to run concurrently. However, in our experiments the original formulation does not consistently retain the quality gains of ordinary looping. We find that preserving the current-token embedding and separately normalizing it and the previous-token hidden state before combining them recovers strong performance across model scales and training budgets. Together, these results show that effective looping requires matching the design to the resource constraint and inference setting.

---


### 387. [Multistep and Multivariate Time Series Explainability with GradientSHAP: A Wind Power Case Study](https://arxiv.org/abs/2610.40330)

**<font color=#1a73e8>作者：</font>** Robbie Southam, Zhong Fan, Ke Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As the effects of climate change become increasingly apparent, the demand for renewable energy sources such as wind power continues to grow. However, renewables' variable and intermittent nature presents significant challenges in their integration into energy grids. Artificial intelligence (AI) has emerged as a powerful tool to address these issues. Still, its adoption in the energy sector has been hindered by the opacity of many AI models, which often function as black boxes. This paper introduces a carefully adapted GradientSHAP approach to provide interpretability for multivariate, multistep wind power forecasting -- a largely underexplored area. This capability is critical for day-ahead grid management and, to the best of our knowledge, this is the first study to apply GradientSHAP in the context of wind power forecasting. To address the inherent dimensionality, we developed novel visualizations that deliver both local and global explanations, uncovering intricate relationships between environmental factors, site-specific conditions, and temporal dynamics. While GradientSHAP is not an out-of-the-box solution, our findings demonstrate that, with thoughtful handling of SHAP values and domain expertise, it can offer valuable insights into model behaviour, supporting more informed and trustworthy decision-making. Nevertheless, its complexity poses challenges for practical implementation. Future research should focus on streamlining these interpretability methods to make them more actionable for routine deployment in critical energy applications.

---


### 388. [RFW-A: Agentic Procedural Generation of 400K Articulated Assets over 500 Categories](https://arxiv.org/abs/2610.40333)

**<font color=#1a73e8>作者：</font>** Yuanbo Lyu, Changjian Pan, Saining Zhang 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality articulated assets are essential for embodied perception, simulation, and manipulation, yet constructing them at scale remains difficult. Manual annotation and procedural modeling require substantial human effort. Recent agentic systems automate asset construction through program synthesis, but repeat costly reasoning and refinement for every new asset. Our key observation is that assets within a category can share construction logic despite variations in structure and appearance. Agentic synthesis and procedural generation are therefore complementary: agents can construct reusable programs, while procedural execution reuses the resulting logic across many samples. We therefore present RFW-A, which combines the two in a new articulated-asset generation paradigm. Starting from existing articulated programs, RFW-A organizes reusable components and their dependencies into category-level generators. Agents test and refine these generators across sampled configurations and motion states. Once constructed and validated, the generators produce diverse assets through procedural execution with no further model calls or token charges. The estimated API cost of generator authoring averages $10.62, amortizing to $0.05 per asset over 200 assets, versus $1.24 for the sampled per-asset agentic synthesis baseline. Using RFW-A, we built RFW-A-400K, containing over 400K sim-ready articulated assets across more than 500 categories. Experiments show high structural and kinematic validity and stable execution across physics simulators. Beyond asset validity, training with RFW-A-400K improves part-level articulation estimation on seen and unseen categories, while policies trained in simulation with retrieved and program-edited assets transfer zero-shot to real articulated objects.

---


### 389. [Wizard: Manipulate Any World in Real Time via Agentic Control](https://arxiv.org/abs/2610.40339)

**<font color=#1a73e8>作者：</font>** Yuzhe Wu, Zijun Lin, Yeying Jin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video world models have enabled the generation of increasingly realistic and interactive virtual environments, opening new possibilities for player-customizable gameplay. Agentic frameworks further advance this direction by decoupling explicit game logic and controllable world representations from visual generation. However, existing approaches support only simple game settings and predefined motion patterns, generalize poorly to unseen environments and characters, and offer limited real-time interactivity. In this paper, we introduce Wizard, an agentic game world model that enables real-time, precise control over character motions while generalizing zero-shot across novel scenes, characters, and actions. To achieve this, we construct a diverse dataset spanning 750 scenes and 178 characters, incorporating skeleton and geometry information as structured representations. We leverage these representations as intermediate proxies to condition a video generation model, together with an adaptive masking mechanism that improves alignment between the conditioning signals and generated video rollouts. Furthermore, we introduce an agentic framework that explicitly maintains and updates game states, allowing players to freely configure their virtual worlds and exercise fine-grained control over character motions while preserving visual quality and gameplay consistency. By combining agentic control with structured proxy-based generation, our framework unlocks new possibilities for player-driven game creation with real-time, generalizable, and mechanically consistent world simulation.

---


### 390. [Is It the Curriculum or Just the Easy Start? Benchmarking Unsupervised Environment Design on Quadrupeds](https://arxiv.org/abs/2610.40364)

**<font color=#1a73e8>作者：</font>** Jakub Gilewicz, Dominik Galus, Piotr Wojdas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unsupervised environment design (UED) methods such as PLR, ACCEL, SFL and PAIRED are compared mostly on 2D mazes, grid worlds and BipedalWalker, while terrain curricula for legged robots are hand-designed and evaluated against a few baselines. We present a benchmark that runs fourteen UED, domain-randomisation and robotics curricula under one protocol on five 3D quadrupeds in MuJoCo MJX: the closed-chain W01-TEK and the open-chain Unitree Go1 and Go2, Google Barkour vB and Boston Dynamics Spot. Levels are vectors of eight interpretable terrain parameters, and all curricula drive the same PPO student at matched environment-step budgets. The evaluation reports success on random and held-out structured terrains, interquartile means with stratified bootstrap intervals, capability envelopes and a level-by-level domination comparison. We compare methods within each robot and report, per level set, the top group of methods not significantly below the best. No method is in the top group on every robot and level set. Methods with easy or low-difficulty training levels, curated or not, fill the top groups on in-distribution random levels of Go1 and Barkour, and of W01-TEK apart from PAIRED+BiBC. The success-driven terrain curriculum from legged-robot practice is in a top group most often, domain randomisation on uniform levels in none, and PAIRED in none outside Spot, where the fourteen methods lie within 3.8 points on random levels of difficulty 0.25. On three robots the leader on in-distribution random levels is not the leader on held-out terrain. We collect the results into a per-robot guide to choosing a curriculum.

---


### 391. [Composing and Steering Diffusion Models with Generalized Feynman-Kac Correctors](https://arxiv.org/abs/2610.40383)

**<font color=#1a73e8>作者：</font>** Wael Mattar, Daniel Freedman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have become the leading paradigm in generative modeling, yet many applications require sampling from distributions that are not those of any single pretrained model, but are instead defined through combinations of several models, possibly tilted toward high values of a downstream reward. Naively combining the scores of the models yields incorrect samples, while existing corrections are restricted to specific families of targets. In this work, we introduce the generalized Feynman-Kac correctors (GFKC), a principled framework for sampling from an arbitrary target function of several pretrained diffusion models. We show that the geometric interpolation between an arbitrary initial function and the target function of the models satisfies a Feynman--Kac partial differential equation, and derive its potential in closed form. To evaluate this potential during generation, we further generalize the log-probability ODE to track the density of each model along trajectories driven by a different velocity field. The resulting algorithm operates entirely in the log domain, incorporates reward-based steering at no additional conceptual cost, and corrects the generation on the fly, without retraining or fine-tuning the models. We validate the method on analytic Gaussian models, where it closely matches the ground-truth targets, and on diffusion models trained on MNIST, where it samples from non-trivial combinations of the models and enables effective steering.

---


### 392. [Deep Learning Based Behavioral Drift Modeling for Continuous Biometric Authentication](https://arxiv.org/abs/2610.40398)

**<font color=#1a73e8>作者：</font>** Suprava Saha Dibya, Minar, Abdulla Al Noman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This research proposes a two-level keystroke dynamics authentication system that provides defense-in-depth security through continuous behavioral drift monitoring. Level 1 employs fixed-text password authentication using Temporal Convolutional Networks (TCN) with contrastive learning and population-based training (PBT), achieving 3.77% EER for high-security login verification. Upon successful authentication, Level 2 continuously monitors user typing during natural free-text sessions using a 4-Model Deep Learning Ensemble. If suspicious behavioral drift is detected during monitoring, the system re-authenticates the user by returning to Level 1, providing a feedback loop against session hijacking and behavioral anomalies. The system explicitly models long-term behavioral drift through the fixed-text component's PBT mechanism, which adapts to temporal variations in password typing patterns. This research leverages free-text (Buffalo dataset) and fixed-text (GREYC dataset) keystroke dynamics datasets, extracting temporal and spatial features including hold times, up-down latencies, down-down intervals, and trigram patterns. The final system achieves 96%+ accuracy for fixed-text authentication (3.77% EER) and 83.53% True Acceptance Rate (TAR) at 5% False Acceptance Rate (FAR) for free-text continuous authentication (10.05% EER), demonstrating superior performance and strong resistance to impostor attacks through continuous behavioral monitoring.

---


### 393. [IMPACT: Inverter-Informed Multimodal Learning for Photovoltaic Generation Forecasting](https://arxiv.org/abs/2610.40418)

**<font color=#1a73e8>作者：</font>** Anushka Katiyar, Cong Feng, Jing Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work develops a physics-informed multimodal deep learning framework for 10- to 110-minute-ahead probabilistic photovoltaic power forecasting. The forecasting model is built on a four-branch architecture that separately encodes plant-level temporal history and inverter-level spatial cloud dynamics through a graph attention encoder with a learned adjacency, known-future solar geometry, and the current meteorological state, fused through gated cross-attention. The geometry branch adds two forward-looking physical signals, spatial cloud heterogeneity and inverter ramp-down activity, each empirically weighted toward the horizon where it is most predictive. The decoder anchors its prediction to a smart persistence baseline, learning a horizon-conditioned correction, and the resulting quantile forecasts are calibrated online through a kernel-weighted adaptive conformal calibration step. The proposed model outperforms all 14 baselines, achieving a forecast skill score (FSS) of 0.2950, 0.099 above the next-best model. A branch-composition ablation shows that every branch contributes positively and the model retains substantial skill in challenging overcast and variable sky conditions (FSS 0.198 and 0.255).

---


### 394. [NECA: Neighbor Event Curve Augmentation for Multi-Horizon ICU Deterioration Prediction](https://arxiv.org/abs/2610.40420)

**<font color=#1a73e8>作者：</font>** Chenyang Wang, Jiawei Theresa Tang, Xinran Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Early prediction of ICU organ dysfunction events supports timely clinical monitoring and intervention, but estimating short-term organ-specific risk from early ICU records remains challenging due to irregular measurements, heterogeneous clinical variables, and the need to predict risk across multiple future horizons. Existing supervised models usually treat each patient as an isolated sample and do not explicitly use the observed event timing of similar historical patients. We propose Neighbor Event-Curve Augmentation (NECA), a model-agnostic method that retrieves training-set patients with similar early-window profiles and converts their subsequent organ dysfunction event onset times into cumulative event-curve features over 6h, 12h, 24h, and 42h. These features are concatenated with the original patient representation and used by standard downstream predictors. On PhysioNet 2012 and a 4,000-stay MIMIC-IV subset, NECA improves average PR-AUC and ROC-AUC across four organ dysfunction event tasks and seven supervised learners. The largest gain appears for neurological dysfunction events, where task-level average PR-AUC increases from 0.461 to 0.557 on PhysioNet 2012. Ablations show that clinically meaningful retrieval and horizon-specific neighbor risk drive most of the improvement, while the full cumulative curve adds task-dependent temporal context. These results support similar-patient event timing as a structured temporal risk signal for ICU organ dysfunction event prediction. The source code will be publicly released upon acceptance of this paper.

---


### 395. [Uncertainty-aware Feedback Loop Diagnosis: integrating reinforcement learning and conformal prediction for reliable wafer defect classification](https://arxiv.org/abs/2610.40421)

**<font color=#1a73e8>作者：</font>** Aleksandr Dekhovich, Carlas Smith, Oleg Soloviev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semiconductor manufacturing is a complex, multi-step process that requires both high precision and low operating costs. Therefore, detecting defects in a high-volume setting is an important component of wafer map analysis for reliable production. However, most state-of-the-art deep learning approaches require a full scan of the surface, which hinders the development of high-throughput inspection systems. To address this problem, we propose Uncertainty-aware Feedback Loop Diagnosis (UFLD), a novel algorithm that employs reinforcement learning for adaptive measurement acquisition and provides a prediction uncertainty level after each step, stopping the process once sufficient information is obtained. Unlike existing methods that rely on ensemble models or auxiliary confidence estimation deep learning models, UFLD utilizes a more parameter-efficient conformal prediction framework to determine the optimal stopping time. The proposed UFLD reduces acquisition time by about $40\%$ and achieves $98.4\%$ inspection accuracy, without requiring an additional learned confidence-estimation network. We validated our approach on the MixedWM38 dataset, demonstrating its advantages over existing adaptive acquisition procedures and standard convolutional neural networks.

---


### 396. [Soil Moisture Estimation in Precision Agriculture: A Knowledge Distillation Approach](https://arxiv.org/abs/2610.40432)

**<font color=#1a73e8>作者：</font>** Mohammed Rakib, Vrinda Nagula, Arunkumar Bagavathi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate soil moisture estimation is critical for precision agriculture, influencing irrigation, fertilization, and harvesting strategies. Traditional methods primarily rely on meteorological and soil property data, while recent approaches incorporate visual modalities such as aerial and geospatial imagery. However, these high-resolution images are expensive and computationally demanding to analyze. In this work, we propose Soil Moisture Distillation (SMD), a Knowledge Distillation (KD)-based multimodal learning framework that leverages unimodal teachers to enhance multimodal soil moisture estimation. SMD surpasses not only traditional multimodal fusion techniques, including MIS-ME, but also outperforms unimodal models, demonstrating the benefits of guided unimodal knowledge transfer. Additionally, we conduct a comparative analysis of soil patches and crop images, showing that crop images provide superior visual cues, leading to improved prediction accuracy. SMD achieves a 2% improvement in MAPE for soil patches and 1.2% for crops over state-of-the-art baselines, highlighting the effectiveness of leveraging both meteorological and visual data through knowledge distillation for enhanced soil moisture forecasting.

---


### 397. [A Pretrained Model for Bayesian Filtering in Heterogeneous Dynamical Systems](https://arxiv.org/abs/2610.40437)

**<font color=#1a73e8>作者：</font>** Ke Fan, Wen Wu, Haitao Su 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Filtering has not yet had its foundation-model moment: state estimation is still dominated either by online Bayesian filtering algorithms that require known dy- namics as inputs, or by learning-based neural filters trained from scratch for a single system or parametric family. The core challenge is structural heterogene- ity: dynamical systems differ in their governing dynamics, physical scales, and noise levels, precluding a shared representation space for a reusable filter. To bridge this gap, we introduce FilterFM, the first pretrained model for Bayesian filtering that estimates latent states across heterogeneous dynamical systems with a single checkpoint. FilterFM employs a hierarchical two-level observation se- quence encoder and a prior-to-posterior state-reconstruction module that together handle varying observation and state dimensions across heterogeneous systems, while modeling state uncertainty via quantile prediction. Trained on a mixture of heterogeneous filtering tasks, FilterFM exhibits superior in-domain performance, delivering significant gains in estimation accuracy, runtime efficiency, and noise robustness compared to existing baselines. Beyond in-domain performance, it marks the first model to successfully enable zero-shot filtering on unseen dynamics, bridging the generalization gap in state estimation. Furthermore, we uncover clear scaling behaviors in foundation-model-based Bayesian filtering, which combined with comprehensive component ablation studies, validate the structural optimality of our design and broaden the generalization scope for this research field.

---


### 398. [Framework-Conditional Open Materials Generation](https://arxiv.org/abs/2610.40443)

**<font color=#1a73e8>作者：</font>** Maya M. Martirossyan, Hillary Pan, Philipp Höllmer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Theoretical predictions of novel materials rely on a variety of techniques, from data-mining-based ion substitution methods to fully de novo generative models. Each approach imposes specific constraints and encounters unique challenges when extrapolating beyond the distribution of known materials to discover new ones. The foremost goal of materials generation is to produce stable, unique, and novel (S.U.N.) structures. Predicted structures that meet these criteria, however, typically result from novel chemical compositions mapped onto known structural prototypes or frameworks. We leverage this heuristic insight to present a new generative paradigm for the de novo prediction of inorganic crystalline materials constrained by their structural framework---i.e., the unit cell shapes and respective particle positions. Our method, termed OMatG-FC (Open Materials Framework-Conditional Generation), learns via a combination of discrete flow matching on the atomic species and stochastic interpolants for the volume scaling of the unit cell lattice, while fixing in-place the fractional coordinates and the unit-volume lattice vectors, dramatically reducing the dimensionality of the problem compared to unconstrained (framework-free) generation. Our method is more flexible than existing prototype-constrained methods, demonstrating capability for discovery of unseen, stable prototypes derived from known structural frameworks. We also investigate the number of unique frameworks in the MP-20 dataset, demonstrating the propensity of duplicate frameworks within the dataset and providing a framework-split version. We benchmark the performance of our model using the LeMat-GenBench suite using three ML interatomic potentials and achieve state-of-the-art S.U.N. rate below the convex hull, eschewing the need to learn atomic packings for materials discovery.

---


### 399. [Reinforcement learning for control of partial differential equations](https://arxiv.org/abs/2610.40449)

**<font color=#1a73e8>作者：</font>** Nicolò Botteghi, Matteo Tomasetto, Andrea Manzoni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Controlling dynamical systems governed by partial differential equations (PDEs) remains a challenging task in scientific computing, owing to high-dimensional state spaces, distributed actuation, nonlinear dynamics, and stringent real-time constraints. Reinforcement learning (RL) has emerged as a promising paradigm for synthesizing feedback controllers that adapt to varying operating conditions and can be deployed efficiently in real-time. This review provides a unified perspective on RL and PDE-constrained optimization, and surveys model-free, model-based, and multi-agent RL approaches to PDE control, with particular emphasis on sample efficiency, generalization across parametric variations, and scalability to high-dimensional problems. Two demonstrative examples, the stabilization of a chaotic system and a flow control problem, illustrate the performance and pitfalls of RL agents in practice. Finally, we discuss evaluation and benchmarking practices, current limitations, and open research directions toward reliable, data-efficient, and scalable RL for scientific computing.

---


### 400. [PhysInsert: Physically Plausible Object Insertion with Geometric Priors and Bidirectional Object-Scene Interactions](https://arxiv.org/abs/2610.40453)

**<font color=#1a73e8>作者：</font>** Yue Gong, Le Zhang, Rui Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present PhysInsert, a framework for physically plausible reference-based object insertion that jointly adapts objects and their surrounding scenes. Existing methods often rely on masked inputs, generation-based pairs, or training pairs with limited viewpoint variation, leaving pose and illumination adaptation and bidirectional object-scene interactions insufficiently constrained. We construct the Insert World dataset with strictly aligned Blender-rendered counterfactual pairs and object references across viewpoints and lighting conditions. Building on these data, Geometry-Guided Adaptation couples a VGGT geometry stream with image and text streams under target-scene feature supervision to guide spatially consistent insertion. Complementary 2D Object-Scene Spatial Supervision jointly supervises object occupancy and environmental changes while grounding spatial instructions in object regions through image-text attention. We introduce PhysInsert-Bench with dedicated cross-environment and cross-view cases requiring illumination and pose adaptation beyond appearance copying. Experiments on PhysInsert-Bench and DreamBooth demonstrate improved image fidelity; a user study further shows more accurate placement and improved lighting integration, perspective, and pose plausibility.

---


> [!TIP]
> 当前位于：**351-400**（第 8/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-432](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
