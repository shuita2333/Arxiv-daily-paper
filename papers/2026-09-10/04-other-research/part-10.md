# 📦 其他研究 | 2026年09月10日

> 本类共 **542** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-542](./part-11.md)

---

### 451. [MLIP Detective: Active Failure Mode Discovery Beyond Benchmark Scores for Machine-Learning Interatomic Potentials](https://arxiv.org/abs/2609.08399)

**<font color=#1a73e8>作者：</font>** Ryuhei Okuno, Nontawat Charoenphakdee, Kaoru Hisama 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Universal machine-learning interatomic potentials (u-MLIPs) aim to generalize across diverse configurations. Benchmarks enable reproducible evaluation but may not expose failures outside their predefined scope. Here, we show that physics-informed search can complement benchmark-based evaluation by uncovering hidden failure modes. We introduce MLIP Detective, an agentic framework for active failure mode discovery. Starting from benchmark evidence, MLIP Detective generates falsifiable, physics-informed failure hypotheses, screens them with inexpensive simulations, and escalates only the most suspicious cases to human experts together with proposed verification protocols. Without issue-specific prompting, MLIP Detective identified and characterized a systematic anomaly in MACE-MPA-0: the model predicted some relaxed adsorbate-surface systems involving O- or F-containing adsorbates to be higher in energy than their corresponding separated fragments. Using cross-model comparisons, MLIP Detective further inferred a likely training-data origin for the anomaly, consistent with recent reports.

---


### 452. [Stochastically Perturbed Weights: Ensembles from Deterministic Machine-Learning Weather Models](https://arxiv.org/abs/2609.08412)

**<font color=#1a73e8>作者：</font>** Simon Adamov, Oliver Fuhrer, Reto Knutti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learning weather models (MLWMs) now match or outperform operational numerical weather prediction (NWP) at global medium-range forecasting, at far lower inference cost. Many deployed MLWMs are deterministic, producing a single forecast with no estimate of its own uncertainty, whereas a growing family of trained-probabilistic models generate calibrated ensembles directly, at the price of a dedicated training run. We ask instead how much uncertainty can be extracted from a deterministic checkpoint that already exists, without retraining it. Where physical ensembles represent model uncertainty by stochastically perturbing parametrisation tendencies, we perturb the network's raw weight tensors at inference time, a scheme we call stochastically perturbed weights (SPW). We also ask whether it works, where and on which scales to inject the noise, and where it fails. A three-phase ablation across four deterministic backbones, Aurora, GraphCast, SFNO, and AIFS, selects one production baseline per model, benchmarked against the trained-probabilistic AIFS-ENS, FourCastNet 3 and Atlas as well as the operational ECMWF ensemble (IFS-ENS) over 112 initialisation times. At a 240 h (10-day) lead time the SPW ensembles reach continuous ranked probability skill scores (CRPSS) between 0.04 and 0.13 below the best trained-probabilistic baseline, at zero marginal training cost. No injection site works across models: the productive tensor group is architecture-specific, so SPW is at present a tuning procedure rather than a plug-and-play recipe. Its main failure mode is a coherent whole-field offset that overdisperses the domain mean, and restricting the noise to coarse scales or perturbing the initial conditions each repair part of it.

---


### 453. [Feyospace-v1: How the Cyber Mercury Seven Trained Frontier Cyber Models](https://arxiv.org/abs/2609.08418)

**<font color=#1a73e8>作者：</font>** Zongjie Li, Alan Z. W, John Nicolas J 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Training capable cyber agents is often treated primarily as a problem of model scale, yet open-weight post-training is constrained more directly by the cost of executable environments, reliable multi-turn supervision, and access to strong teachers. We present a data-centric framework that addresses these bottlenecks through five complementary systems: Choulea analyzes hidden reasoning signatures, SkyReal reduces teacher-sampling cost, Hongzwang bypasses API restrictions on teacher execution, PSBreakup restores capabilities weakened by model merging, and Kreator converts expert interventions into trainable reasoning. Our data engine constructs resettable coding, vulnerability, CTF, kernel-history, full-exploit, firmware, and device-backed environments. Candidate trajectories are retained only after execution verification and evidence auditing, yielding 164,269 trajectories for long-context supervised fine-tuning. The three checkpoints improve over their starting models by an average of 23.76% on the full CyberGym suite and 10.49% across the pooled CTF suites. As of September 1, 2026, Feyospace-s1 achieves a verified success rate of 63.24% and ranks 10th on the official CyberGym leaderboard, while all three checkpoints rank 1st among models at comparable parameter scales. To our knowledge, this is the first end-to-end demonstration that a seven-person independent team can train open-weight models with leading agentic cyber capability.

---


### 454. [CAR-MIL: Counterfactual Attention Regularization for Multiple Instance Learning](https://arxiv.org/abs/2609.08419)

**<font color=#1a73e8>作者：</font>** Imane Chraki, Pierre Marza, Stergios Christodoulidis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multiple Instance Learning (MIL) is widely used for weakly supervised learning, particularly in digital pathology, where fine-grained annotations are costly. Most MIL methods aggregate instance features via attention mechanisms. However, attention weights do not always faithfully reflect instance importance and may focus on spuriously correlated regions. In this work, we propose CAR-MIL, a framework that explicitly guides attention learning through a counterfactual attention regularization objective inspired by counterfactual explanations. Built on a standard attention-based MIL architecture, our approach introduces a lightweight counterfactual attention branch trained to produce an alternative prediction while remaining close to the factual attention distribution. This encourages prediction changes to arise from minimal, structured redistributions of attention, leading to more informative evidence allocation. The resulting factual and counterfactual attention maps capture complementary evidence: the former highlights regions supporting the prediction, while the latter reveals regions whose reweighting would challenge it. We evaluate our method on synthetic MIL benchmarks with instance-level ground truth enabling controlled analysis of attention behavior and on five digital pathology datasets across four tasks. CAR-MIL maintains competitive classification performance, with the largest gains observed on more challenging tasks, while improving attention reliability, demonstrating the benefits of integrating counterfactual explainability reasoning into attention learning. Code is available at: this https URL.

---


### 455. [AirAnchor: Bridging Local and Global Spatial Information for Zero-Shot Aerial Vision-and-Language Navigation](https://arxiv.org/abs/2609.08442)

**<font color=#1a73e8>作者：</font>** Shanwei Fan, Bin Zhang, Zhiwei Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial Vision-and-Language Navigation requires drones to follow natural-language instructions and navigate through complex urban environments. Accurate navigation relies on both local and global spatial information, which support immediate action grounding and long-horizon path planning, respectively. However, existing zero-shot methods typically operate at a single spatial scale, relying either on local representations constructed online from current observations or on global memories built offline from historical experience. To address this limitation, we propose AirAnchor, a new paradigm that bridges local and global spatial information through spatial anchors and integrates both into a shared navigation framework, enabling comprehensive spatial grounding for decision-making. AirAnchor consists of three core components: (1) Query-Driven Spatial Anchor Grounding, which identifies decision-relevant anchors from visual observations and organizes them into local spatial representations; (2) Persistent Object Spatial Memory, which incrementally maintains an object knowledge base as persistent global spatial memory and retrieves landmark-related spatial priors; and (3) a Spatially-Informed Navigation Agent, which explicitly integrates both local and global spatial information into an agentic framework for decision-making. Extensive experiments on AerialVLN demonstrate that AirAnchor substantially outperforms existing zero-shot baselines, validating the effectiveness and efficiency of the proposed paradigm.

---


### 456. [Topological Fraud Detection in Latent Transaction Spaces](https://arxiv.org/abs/2609.08445)

**<font color=#1a73e8>作者：</font>** Avraham Bourla  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Working entirely on topologically anonymized embeddings, we perform fraud detection using iterative rounds of unsupervised filtering followed by supervised sniping. The result is an ultra-low latency privacy--preserving triage that allows institutions to flag suspicious activity without compromising Personally Identifiable Information.

---


### 457. [GSComplete: Gaussian Splat Completion with 2D Diffusion Priors](https://arxiv.org/abs/2609.08449)

**<font color=#1a73e8>作者：</font>** Elias Brugger, Philipp Erler, Stefan Ohrhallinger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian splats provide a fast, high-fidelity representation for 3D objects but are often constructed from incomplete input data in practice, leaving missing regions. Existing completion methods either do not preserve the original splats or require scarcely available 3D training data. We propose GSComplete, which combines 3D generation based on Score Distillation Sampling with a novel preservation loss that encourages the original splats to be preserved where they should be visible. This effectively completes the Gaussian splat object using only 2D diffusion priors while fully preserving existing splats and generating new splats only in missing regions, without occluding the input. To evaluate our approach, we introduce a new dataset of partial Gaussian splat objects and show that GSComplete achieves significantly more accurate preservation of the input than existing methods with comparable plausibility of the completed result. Our code and dataset will be made available upon acceptance.

---


### 458. [Detecting Authorship in Political Texts with Inductive Stylometry](https://arxiv.org/abs/2609.08459)

**<font color=#1a73e8>作者：</font>** Gennadii Iakovlev, Levente Littvay  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Political texts are rarely authored by the nominal speaker alone. Tweets, speeches, reports, and official statements are drafted, edited, or harmonized by staff, yet political science has paid limited attention to the stylistic traces these hidden authors leave behind. This paper develops and stress-tests an inductive stylometric approach for recovering latent authorship structure in political communication, combining character 3-gram features with UMAP dimensionality reduction, and Burrows' Delta. We apply the approach to six corpora that vary in length (from tweets to long documents), in mode (written and oral), and in language (English and Hungarian). The approach recovers near-disjoint analyst fingerprints in formal legal prose in both languages, sorts a politician's tweets into validated subsets while uncovering additional insights, and distinguishes scripted from improvised speech. It fails, however, to resolve individual speechwriters within scripted corpora. Frequency-based stylometry is thus a powerful tool that, depending on authorial signal strength and institutional editing, can uncover authorship traces relevant to legislative studies, political communication, and policy research.

---


### 459. [When Topology Betrays Privacy: Lattice-Based Reconstruction Attacks on Secure Aggregation in Decentralized Federated Learning](https://arxiv.org/abs/2609.08476)

**<font color=#1a73e8>作者：</font>** Wenrui Yu, Changlong Ji, Johannes Bjerva 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Secure Aggregation (SA) is widely regarded as a strong defense against model-update leakage in Federated Learning (FL), as it reveals only aggregate results while hiding individual updates. In Decentralized Federated Learning (DFL), SA is commonly instantiated as local neighborhood aggregation, where each node obtains a weighted aggregate over its neighbors. We show that this locality creates a structural leakage surface: sparse decentralized topologies provide colluding semi-honest nodes with asymmetric aggregate views, exposing multiple hidden linear combinations of honest participants' private states. Reconstructing private states from these aggregate views is fundamentally challenging, as both the private states and the aggregation coefficients are hidden. We tackle this challenge by establishing a formal connection to the Hidden Subset Sum Problem, a long-studied problem in cryptography. Building on this formulation, we design a lattice-based reconstruction approach that combines lattice reduction with structural filtering to reconstruct protected model states. We evaluate our attack on image, tabular, and text tasks under sparse DFL topologies. Our results show that colluding semi-honest nodes can recover the original local updates of honest nodes, enabling downstream reconstruction of private training data. These findings demonstrate that SA alone does not guarantee privacy in DFL when local aggregation induces asymmetric observations.

---


### 460. [An Evidence Model for Agentic Processes: Evidence Claims, Trust Assumptions, and Policy Assessment](https://arxiv.org/abs/2609.08481)

**<font color=#1a73e8>作者：</font>** Arslan Brömme  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agentic AI systems increasingly exchange messages, invoke tools, request approvals, hold structured decision sessions, and modify shared artifacts. Logs and anchors can make selected records tamper-evident, but they can also mislead if their evidentiary meaning is implicit: a hash does not establish semantic truth, a signature does not establish authorization, and an external anchor does not establish capture completeness. This paper proposes an evidence claim model for agentic processes. It distinguishes artifact integrity, temporal existence, provenance, approval evidence, declared ordering, capture claim, relevance claim, deliberation traceability, monitoring claim, anchoring authorization claim, policy assessment claim, risk treatment claim, mitigation implementation claim, and management response claim. Semantic validity is treated as a recurring limitation. The model maps these claims to mechanisms, assumptions, limitations, and threats, and situates them in an agent organization with functional CEO agent, executive, operational, evidence, and audit roles, plus a plan-do-check-act-inspired management response loop. The contribution is conceptual: it does not validate a particular implementation, prevent all failures, or automate legal compliance. It provides a vocabulary for stating which claims an agentic black box can support, which claims it cannot establish, and which controls are required around it.

---


### 461. [Enhancing Communication in Speech Therapy: Exploring the Cognitive Synergy Between Gesture and Speech](https://arxiv.org/abs/2609.08486)

**<font color=#1a73e8>作者：</font>** Paul-Peter Arslan, Xiao Xiao  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper examines the adaptation of a rhythm-based interface, originally designed for manual dexterity rehabilitation, for use in speech therapy. The interface allows users to control synthesized vocal phrases through finger tapping, leveraging the cognitive link between gesture and speech. Through interviews with four therapists and pilot tests with one speech therapist and eight children with speech impairments (autism, Down syndrome, verbal apraxia, dyslexia), we found that the interface improves motivation and therapeutic outcomes by facilitating more interactions between verbally challenged patients and the therapist. Our findings suggest that rhythmic gestures can enhance verbal communication, offering potential for broader therapeutic and educational applications.

---


### 462. [SignRefine: Adapting Foundational Video Models for Sign Language Generation](https://arxiv.org/abs/2609.08496)

**<font color=#1a73e8>作者：</font>** Anton Pelykh, Edward Fish, Ozge Mercanoglu Sincan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign language video generation demands precise hand and facial articulation, yet modern video diffusion models, trained predominantly on spoken-language video, produce artifacts that render signing unintelligible. We propose SignRefine, a sign language video generation model that produces comprehensible signing from 2D keypoint conditioning alone, generalizing across appearances and visual conditions. Our approach builds on a pretrained video diffusion transformer and introduces local adapters with spatial grounding to selectively refine hand and face regions, steering the strong base model's prior toward accurate articulation. To enable this work and support broader sign language research, we present NVSign, a large-scale dataset of video content natively produced in sign language, offering diverse signer appearances, environments, and natural conversational settings. Trained on this data, our model shows up to 30% improvement in hand pose precision metrics over the strongest baseline and is preferred by sign language users for visual quality and comprehensibility in more than 80% of comparisons.

---


### 463. [Temporal State Transport in Video Generation: Diagnosing and Correcting Spectral Imbalance](https://arxiv.org/abs/2609.08505)

**<font color=#1a73e8>作者：</font>** Luyao Tang, Bingjun Luo, Dong Yi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable video generation requires more than high-quality frames to form a coherent story: a model must maintain a persistent state, transporting visual attributes such as identity, scene layout, motion, and fine details across time. Existing training-free methods mainly strengthen cross-frame attention or analyze local attention entropy, but these views do not reveal whether temporal interactions stay in a healthy transport regime. In this work, we study video generation through the perspective of Temporal State Transport. We introduce Spectral Tension, a signed diagnostic that compares local attention diffuseness with global spectral diversity, and use it to identify two opposite temporal failures: fragmented transport and over-mixing hotspots. Based on this diagnosis, we propose Spectral Transport Homeostasis, a training-free regulator that softly corrects pathological temporal states while largely preserving balanced ones. Experiments on pretrained video generation models show that the original model often occupies imbalanced temporal regimes, whereas our method selectively applies larger corrections to the worst temporal hotspots and improves temporal consistency and visual quality without finetuning. Code: this https URL

---


### 464. [Visualizing Colonial Regimes: A Multi-View Approach to (Historical) Political Transformation](https://arxiv.org/abs/2609.08518)

**<font color=#1a73e8>作者：</font>** Nicole Husemann, Steffen Kailitz, Christofer Meinecke  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper takes a critical approach to visualization of colonial regimes. Drawing on critical hermeneutics and postcolonial theory, we created interactive visu- alizations revealing the constructed nature of colonial categories and exposing the hierarchies between empires and territories. Using the Varieties of Political Regimes dataset, our approach combines temporal flow visualization and geo- graphic distribution mapping. This allows us to contextualize colonial rule within broader patterns of political change. Our visualization challenges conventional, static, and isolated representations of colonial data by making the interpre- tive frameworks underlying colonial categorization visible through coordinated temporal, spatial, and relational views.

---


### 465. [Not All Variables Agree: Reliability-Aware Variable-Wise Gradient Surgery for Multivariate Time-Series Forecasting](https://arxiv.org/abs/2609.08554)

**<font color=#1a73e8>作者：</font>** Jinwoo Park, Hyeongwon Kang, Pilsung Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In data-driven training, multivariate time-series forecasting is usually optimized with a scalar loss averaged over samples, variables, and horizons. This averaging is convenient, but the optimizer sees only the aggregated gradient, which does not reveal whether the variable-wise contributions align or oppose one another. To quantify how often this disagreement arises, we measure the variable-wise gradients directly and find that 30.6% of their pairwise cosine similarities are negative on average across seven datasets. However, conflict and harm are not the same thing. Under shared training 35 of the 64 variables do worse than a full-input single-target oracle, and the harmed fraction is not reliably predicted by how often gradients conflict. We propose Per-Variable Surgery (PV-Surgery), an optimizer-side training strategy for backbones with cache-compatible layers. One backward pass builds variable-wise gradient proxies from output-side signals and keeps the pointwise forecasting loss. Reliability-aware selection targets layers whose proxy sums closely approximate their shared-gradient slices. Conditional pooling forms anchor and conflict pools without dropping variables. Common-direction surgery aligns variable or pooled gradients with their normalized mean and restores input norms to avoid reweighting. In experiments across five backbones, seven datasets, and four horizons, PV-Surgery lowers MSE by 3.61% and MAE by 2.93% on average. For multivariate forecasting, this indicates that the variable-wise structure hidden by mean-loss training is a usable optimization signal.

---


### 466. [Effects of model architecture and learning strategies on deep learning-based recognition of activated sludge microscopic images and comparison with quantitative image analysis](https://arxiv.org/abs/2609.08570)

**<font color=#1a73e8>作者：</font>** Suguru Hakoshima, Tomohiro Tobino, Fumiyuki Nakajima  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Microscopic image analysis has long been recognized as a promising approach for monitoring activated sludge. In recent years, deep learning-based image analysis has been increasingly adopted in this field because of its high performance. However, previous studies on microscopic image analysis of activated sludge have rarely explored transformer-based models or self-supervised foundation models and have instead relied on CNNs and supervised ImageNet pretraining. In addition, previous studies often downsampled image sizes, but the effects of downsampling have not been sufficiently investigated, and the relationship between downsampling strategies and image analysis performance remains unclear. Furthermore, no study has quantitatively compared deep learning performance with quantitative image analysis (QIA), which was widely used before the emergence of deep learning. In this study, to examine how model architecture and learning strategies affect performance in microscopic image analysis of activated sludge and to quantitatively determine whether deep learning outperforms QIA, we prepared three types of activated sludge samples, classified their microscopic images, and evaluated classification accuracy. Our results showed that transformer-based architectures and alternative pretraining methods were effective in terms of classification accuracy. Our downsampling analysis showed that using overly small images reduced accuracy, but increasing image size beyond a certain point did not improve it further. In addition, the analysis indicated that, to achieve high classification accuracy, maintaining the field of view was a more effective downsampling strategy than maintaining resolution. Finally, our comparison between deep learning and QIA showed that deep learning outperformed QIA in terms of accuracy.

---


### 467. [AlphaRJM: Reward-Jump Memory for Stochastic Return-Guided Alpha Discovery](https://arxiv.org/abs/2609.08581)

**<font color=#1a73e8>作者：</font>** Sayan Dhan, Selvaraju Natarajan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Formulaic alpha discovery is a pool-dependent symbolic search problem in which informative feedback is observed primarily when a complete expression is evaluated. This delayed feedback creates two coupled difficulties: the retained alpha pool does not preserve the full history of realized evaluation feedback, and the value of an intermediate construction action is uncertain because its consequence depends on the formula eventually completed. We introduce AlphaRJM, which addresses these difficulties through Reward-Jump Memory, an event-driven latent state that remains fixed during token construction and updates only at terminal evaluation events using the realized pool reward and evaluation outcome, and an action-conditioned SDE return critic that represents future discounted discovery returns with stochastic particles. The particles guide action selection through their mean and uncertainty and are learned using a distributional Bellman objective combining energy-distance matching, mean calibration, and jump regularization. Empirically, AlphaRJM delivers strong and stable gains across multiple equity universes, forecasting horizons, and random seeds, while ablations confirm the complementary roles of persistent evaluation history, stochastic return modeling, and distributional supervision.

---


### 468. [Leveraging Cardiac Imaging to Improve ECG-Based Detection of Chagas Disease in Resource-Constrained Settings](https://arxiv.org/abs/2609.08582)

**<font color=#1a73e8>作者：</font>** Laura Alvarez-Florez, Daniel Uyterlinde, Samuel Ruipérez-Campillo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chagas disease is a major cause of cardiomyopathy in Latin America. Cardiac magnetic resonance (CMR) imaging can characterize its structural abnormalities, but scanners and expert readers remain scarce in endemic regions. Electrocardiography (ECG) is inexpensive and widely available, yet structural disease must be inferred indirectly from electrical signals. We propose to transfer CMR-derived structural knowledge to ECG through contrastive pre-training. Using 63,193 paired ECG-CMR examinations from the UK Biobank, we align an ECG encoder with a clinically grounded CMR embedding space using an asymmetric InfoNCE objective. Despite seeing no Chagas cases during pre-training, the resulting representation improves ECG-based Chagas detection. Across CODE-15% and SaMi-Trop, a frozen linear probe achieves an AUROC of 0.851 and sensitivity at the top 5% of predicted risk (Top5%-TPR) of 0.427 in five-fold cross-validation, compared with 0.827 and 0.377 for an unaligned ECG-FM baseline. On the PhysioNet/CinC 2025 Challenge test set, our model obtains the highest AUROC on SaMi-Trop-3 and the best ELSA-Brasil challenge score among the three top-performing methods, indicating that imaging-supervised ECG representations can generalize to populations and settings beyond the pre-training distribution.

---


### 469. [Rescuing Performance from the Demo: Co-Designing Drum Gesture Mappings with a Percussionist](https://arxiv.org/abs/2609.08587)

**<font color=#1a73e8>作者：</font>** Jordie Shier, Teresa Pelinski, Charalampos Saitis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Augmenting instruments with sensors and neural network mappings is a well-explored digital musical instrument design approach. While augmentations can create new expressive opportunities, they also exert aesthetic influence and can constrain musicians' gestural language, which, if left unchecked, can lead to technological capture. To examine this, we conducted a study with a professional percussionist, co-developing a gesture mapping toolkit and recording a ten-track album. Drawing on the concept of productive dissonance, our study aimed to hold the musician's aesthetic in tension with technological constraints. This, along with a practice-based reflective approach, supported the development of a continuous gesture recognition method for percussive mapping and surfaced insights into the design process. We identify knowing-when as a form of tacit knowledge that supported productive dissonance, and raise an open question: absent a musician's broader social context, how do we know whether a technology's influence is genuinely supporting their practice?

---


### 470. [Multi-Level-Set-Based Physics-Driven Neural Network to Solve 3-D Inverse Scattering Problems](https://arxiv.org/abs/2609.08594)

**<font color=#1a73e8>作者：</font>** Yutong Du, Zicheng Liu, Bo Qi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a level-set-based physics-driven neural network solver (LSPDNN) for 3-D electromagnetic inverse scattering. To mitigate boundary blurring and reconstruction artifacts in voxel-wise contrast reconstruction, the proposed solver exploits the piecewise homogeneity of practical scatterers by representing unknown targets with multiple coordinate-dependent neural level-set components. Specifically, a soft-union multi-material model is proposed to separately describe the object support and material distribution. The global support is formed by the union of multiple level-set components, while the local contrast is determined by normalized component weights and learnable complex permittivity candidates. In addition, a model-consistent total variation (TV) regularization is imposed on the material-region indicators, rather than directly on the reconstructed contrast, to suppress fragmented material assignments without excessively smoothing material interfaces. An adaptive loss balancing strategy is further introduced to reduce the dependence on manually selected regularization weights. For each measurement instance, the neural level-set parameters and material candidates are optimized by minimizing a physics-consistent objective function. Numerical and experimental results demonstrate that LSPDNN can reconstruct scatterers with clear boundaries, more uniform material regions, and substantially reduced background artifacts. The results highlight the advantage of the neural level-set parameterization in challenging 3-D inverse scattering cases involving irregular shapes, closely spaced objects, multiple materials, and measurement noise.

---


### 471. [GOLF: Global Observation with Local Focus for Calibration-Aware Stereo Interaction Field Estimation](https://arxiv.org/abs/2609.08607)

**<font color=#1a73e8>作者：</font>** Minqiang Zou, Riqiang Jin, Zhi Lv 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present GOLF, the first-place solution to the SHOW3D Interaction Field Estimation Challenge at HANDS@ECCV 2026. Given synchronized egocentric stereo views, the task is to predict a 3D vector from each of 21 hand joints to the closest point on the manipulated object. GOLF combines dense global context, locally sampled hand/object evidence, and common-frame Plücker-ray geometry. We adapt DINOv3 ViT-H+/16 with LoRA and trainable LayerNorm parameters, then jointly decode both interaction fields. Our primary model achieves an official score of 27.61 and a mean ADE of 27.96 mm on the hidden test set. An equal-weight ensemble with a complementary directly fine-tuned variant improves these results to an official score of 27.47 and a mean ADE of 27.82 mm, securing first place.

---


### 472. [Why shared attention vectors fail: a case for outcome-indexed tuning](https://arxiv.org/abs/2609.08615)

**<font color=#1a73e8>作者：</font>** Lenard Dome  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dimensional attention in learning is often implemented as a globally shared attention vector, where each stimulus dimension corresponds to a single scalar. These scalars are learned by models through gradient-descent on error, where predictive features acquire more salience. We show that under multi-outcome learning, where models predict more than one outcome, this shared vector becomes unstable; it collapses to its bounds and prevents the models from learning meaningful attentional tunings for learning and generalization. We address this by introducing an outcome-indexed attentional matrix that converts globally shared attentional tuning into an outcome-indexed representation. We present an analysis of the unstable shared vectors and derive the conditions under which it holds. Empirically, three synthetic experiments benchmark the proposed attention matrices and show that they converge to meaningful representations, something shared attention vectors fail to do. These results suggest that outcome-indexed attentional matrices are a general fix for gradient-based attentional processes, which improves models of learning under multi-outcome conditions.

---


### 473. [Leveraging contextual events on structure-aware next activity prediction](https://arxiv.org/abs/2609.08622)

**<font color=#1a73e8>作者：</font>** Alessandro Mele, Claudia Diamantini, Domenico Potena  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive process monitoring aims at forecasting various aspects of running processes. Among the different tasks, next activity prediction represents the most extensively investigated. However, only a limited number of existing approaches explicitly encode contextual information, i.e., the environmental conditions in which the process is executed, typically modeled through event log attributes or aggregated measures. In this paper, an approach based on the concept of Instance Graphs is introduced. To incorporate contextual process instances, several encoding strategies are proposed and evaluated by measuring their impact on prediction performance. For each encoding strategy, a set of prefix-Instance Graphs is generated and subsequently provided as input to a Graph Neural Network for the classification task. The proposed approach is evaluated on multiple real-world event logs, and the experimental results demonstrate that incorporating contextual process instances benefits prediction performance.

---


### 474. [Navigating the Latent Manifold: Proactive Concept Drift Adaptation for Resilient NIDS](https://arxiv.org/abs/2609.08623)

**<font color=#1a73e8>作者：</font>** Chao Zha, Zifeng Kang, Tian Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Network intrusion detection systems (NIDS) are critical for cybersecurity, safeguarding services and data from potential attacks. However, existing AI-based NIDS often assume static data distributions and fail to handle concept drift, leading to degraded performance and increased false positives in dynamic network environments. To address this issue, we propose DriftXpert, a novel NIDS for drift-adaptive detection. Specifically, we propose a decoupled two-stage offline adaptive framework. In Phase 1, we introduce an unsupervised anomaly metric based on latent manifold deviation. By performing outlier analysis within the latent space, the framework achieves high-sensitivity detection of network traffic concept drift. In Phase 2, to mitigate catastrophic forgetting under non-stationary distributions, we design a representation consistency alignment strategy. This strategy constrains the feature mapping between the legacy model and the drifted distribution, ensuring the model captures emerging attack characteristics while retaining discriminative power over known patterns. Furthermore, we incorporate cross-epoch neuron weight aggregation and selective freezing mechanisms to enable fine-grained knowledge transfer in the parameter space, effectively balancing model plasticity and stability. Extensive experiments on public datasets demonstrate that DriftXpert effectively adapts to drifted data without catastrophic forgetting. Furthermore, real-world evaluations on enterprise network further confirm its robustness and practical applicability, contributing to improved security protection for millions of users.

---


### 475. [SynthRCT: Scalable Conditional Deformation Synthesis for Synthetic Repeat CT Generation](https://arxiv.org/abs/2609.08627)

**<font color=#1a73e8>作者：</font>** Tomas Guija-Valiente, Blanca Rodriguez-Gonzalez, Norberto Malpica  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In proton therapy, plans are typically optimized on a single planning CT, making robustness evaluation essential under anatomical changes. However, current scenarios often rely on simplified perturbations that poorly capture complex, patient-specific variability. We propose SynthRCT, a scalable conditional generative framework for 3D anatomical deformation synthesis. Based on a conditional variational autoencoder, SynthRCT learns a latent deformation space and decodes sampled latent codes into local stationary velocity fields conditioned on an input anatomy. Local fields are assembled into coherent full-volume transformations, enabling memory-scalable generation for large field-of-view CT data. We validate the approach on respiratory 4DCT data with multiple breathing-phase anatomies per subject. SynthRCT enables patient-specific sampling of plausible anatomical transformations beyond predefined robustness scenarios. Code available at: this https URL.

---


### 476. [From Where to How: Continuous 4D Interaction Forecasting from Egocentric Video](https://arxiv.org/abs/2609.08636)

**<font color=#1a73e8>作者：</font>** Qiaohui Chu, Haoyu Zhang, Meng Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric 4D interaction forecasting aims to anticipate both where future interactions will occur in 3D and how the human body will move to realize them, providing an important capability for assistive robotics and human-computer interaction. Existing methods struggle to translate semantic understanding into precise continuous 3D localization and to balance motion diversity with structural consistency in pose forecasting. More fundamentally, these tasks are often modeled separately, leaving the continuous geometric and temporal correspondence between interaction locations and body motion insufficiently captured. To address these challenges, we introduce Coherent4D, a large-scale egocentric dataset for continuous 4D interaction forecasting, comprising approximately 233K samples across three domains. Each sample pairs a sequence of future 3D interaction locations with corresponding full-body poses, aligned in time and expressed in a shared coordinate system. We also provide evaluation metrics in continuous space. Building on this formulation, we propose HIGFlow, a Hand Interaction Guided Residual Flow framework that models forecasting as a cascaded where-to-how process. HIGFlow first forecasts continuous future interaction locations by combining semantic grounding with short-horizon visual dynamics, and then uses the predicted location sequence to condition a deterministic motion anchor and residual Flow Matching for diverse yet structurally consistent full-body motion forecasting. Extensive experiments across all three domains demonstrate consistent improvements over representative baselines on both location and pose forecasting, while ablations validate the contributions of the proposed components. The project page is available at this https URL.

---


### 477. [SUN: Reaching for Novelty in Reinforcement Learning](https://arxiv.org/abs/2609.08642)

**<font color=#1a73e8>作者：</font>** Wenyan Yang, Arsenii Mustafin, Dominik Baumann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exploration in reinforcement learning (RL) remains a fundamental challenge. Recent goal-conditioned RL strategies (which select goals to encourage broader state coverage) have shown promising results, but none scores a goal by novelty and reachability jointly: the two signals are traded off by hand, applied in sequence, or one is neglected outright. In this paper, we introduce a reachability-aware goal-selection framework that explicitly integrates these two aspects, and that can be seamlessly incorporated into any off-policy RL algorithm. To this aim, we propose SUccessor-to-Novelty (SUN), an indicator derived from successor value functions to identify goals that are both novel and reachable. We prove that SUN recovers count-based bonuses in the limit, bounds short-horizon hitting probabilities, and provably rejects unreachable goals. We further present an adaptive goal-selection strategy that leverages these properties, and an accurate yet lightweight pseudocount to avoid the overhead of classic methods. We back up all our claims with thorough benchmarks: SUN consistently outperforms state-of-the-art methods in standard and novel environments with unreachable or hard-to-reach states, irreversible transitions, obstacles, mazes, and unbounded spaces.

---


### 478. [TriCCOT: Tri-part Convolutional Conformal Transformer for Onboard Space Object Detection](https://arxiv.org/abs/2609.08659)

**<font color=#1a73e8>作者：</font>** Adrien Dorise, Marjorie Bellizzi, Julia Cohen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Onboard object detection in Earth observation is constrained by limited computational resources and the absence of fully corrected imagery. While convolutional detectors are hardware-efficient, they often struggle to extract robust representations from raw and noisy data. Conversely, transformer-based models provide stronger global reasoning capabilities but remain difficult to deploy on FPGA accelerators due to quadratic attention complexity and non-compatible operations.
We introduce TriCCOT, a tri-part architecture for robust and deployable onboard object detection. TriCCOT combines a convolutional region proposal network, a conformal prediction stage, and Aper-GATES, our hardware-friendly attention-based classifier. The region proposal network generates candidate bounding boxes, which are subsequently enlarged via conformal prediction, providing a distribution-free probabilistic coverage guarantee. The resulting crops are processed by Aper-GATES, which reformulates self-attention through convolutional projections, global channel statistics, and hardware-friendly gating operations, avoiding standard transformer operations that are poorly suited to CNN-oriented accelerators.
Experiments on the DIOR and VDVRaw datasets demonstrate competitive detection performance and improved robustness to spatial blur and signal-dependent noise when compared to FPGA-compatible architectures. Finally, we report full deployment on a Xilinx Versal VCK190 FPGA without modifying the underlying DPU architecture, enabling unified CNN-Transformer inference for spaceborne embedded applications.

---


### 479. [CoordFormer: Give Me Any Coordinates and I Will Give You Labels](https://arxiv.org/abs/2609.08660)

**<font color=#1a73e8>作者：</font>** Iacopo Curti, Pierluigi Zama Ramirez, Alioscia Petrelli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation on very-high-resolution images remains challenging due to the high computational cost and the difficulty of capturing fine-grained details. We propose CoordFormer, a novel coordinate-based architecture for semantic segmentation that predicts labels at arbitrary spatial locations through a Coordinate Decoder equipped with a Localized Cross-Attention mechanism. The decoder combines coordinate embeddings with high-resolution local patch features and interacts with global tokens extracted from a downsampled image processed by a ViT foundation encoder, enabling rich semantic context while preserving pixel-level precision. This design enables flexible inference at arbitrary resolutions while keeping memory low on very-high-resolution inputs, and supports an efficient semantic-edge-focused strategy that concentrates computation along boundaries, maintaining fine-grained accuracy while reducing latency and computational cost. CoordFormer achieves state-of-the-art performance on MaSS13K and outperforms comparably sized and higher-parameter methods on DIS5K and KPIs, demonstrating its effectiveness for high-quality, very-high-resolution semantic segmentation.

---


### 480. [Neither Adversarial Training Nor Purification: Emergent Adversarial Robustness from Oscillatory Predictive Learning](https://arxiv.org/abs/2609.08683)

**<font color=#1a73e8>作者：</font>** Mohammed-Yassine Habibi, Klea Ziu, Martin Takáč 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial robustness in computer vision is still largely achieved through adversarial training or test-time adversarial purification, both of which introduce significant computational overhead by generating adversarial examples during training or performing iterative denoising at test time. We study whether empirical robustness can instead emerge from architectural and representation-learning inductive biases. We introduce Oscillatory Predictive Learning (OPL), a two-stage framework that combines Artificial Kuramoto Oscillatory Neurons (AKOrN) with predictive self-supervised pretraining using X-PhiNet. Because our default checkpoint uses randomized initial oscillator states, we compare it with other randomized adversarial defense methods that provide precise, reproducible, and strong attack protocols. Experiments on CIFAR-10 and CIFAR-100, with additional corruption evaluation on CIFAR-10-C, demonstrate that our method achieves competitive results under the AutoAttack-rand evaluation protocol. On CIFAR-10 and CIFAR-100, OPL attains 76.63$\pm$0.76$\%$ and 50.44$\%$ robust accuracy, respectively, under $\ell_\infty$, $\epsilon=8/255$, AutoAttack-rand with EoT $K=20$.

---


### 481. [HOPE: Heterophily-Aware Open-Set Node Classification with Pseudo-Extrapolation](https://arxiv.org/abs/2609.08685)

**<font color=#1a73e8>作者：</font>** Yumeng Dai, Yue Tan, Yixin Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard open-set node classification methods rely on the homophily assumption, where connected nodes share labels. However, real-world graphs are often heterophilic, exposing the limitations of current methods and posing new challenges to open-set node classification. On the one hand, cross-class connectivity causes representations from different known or unknown classes to become intertwined after aggregation, undermining their discriminative capacity. On the other hand, structural mixture invalidates threshold-based open-set methods and cross-class feature interpolation, leading to unreliable unknown-class rejection. To address these challenges, we propose HOPE, a Heterophily-aware Open-set node classification method with Pseudo-Extrapolation. To adapt open-set graph neural networks (GNNs) to heterophilic scenarios, HOPE uses a structure-augmented feature initialization layer to capture multi-hop structural patterns. Meanwhile, we design a trustworthy neighborhood aggregation mechanism for standard GNNs to dynamically filter noisy cross-class neighbors. To enhance unknown-class rejection, we introduce a heterophily-guided pseudo-extrapolation strategy. It dynamically maintains known-class centers and extrapolates along cross-class neighborhood displacement directions, synthesizing pseudo-unknown proxies near structurally ambiguous regions. Finally, we optimize the network with joint classification and logit margin regularization, routing synthetic proxies into a dedicated rejection slot without imposing geometric margin constraints in the representation space. Extensive experiments on multiple datasets show that HOPE consistently outperforms state-of-the-art models, validating its effectiveness, robustness, and efficiency.

---


### 482. [Global Divergence, Local Convergence: Representation Geometry in SSMs and Transformers](https://arxiv.org/abs/2609.08692)

**<font color=#1a73e8>作者：</font>** Amit Ben-Artzy, Roy Schwartz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent state-space models (SSMs) such as Mamba achieve language modeling performance comparable to transformers despite relying on fundamentally different architectures. This raises an important question: how do these structural differences influence the geometry and functional nature of their internal representations? We study this question through a multi-scale analysis of representations in transformers, SSMs, and hybrid architecture. First, we find that SSMs distribute their representational information evenly across all dimensions, whereas transformer representations are heavily dominated by a single principal direction. By evaluating hybrid architectures, we observe that the representation space becomes increasingly skewed toward a single dominant direction after each attention layer. Next, we explore how the different geometric spread of representations impacts representational capacity through compressibility. Surprisingly, we find that despite their contrasting geometric structures, both architectures exhibit tightly matched effective capacities. We further investigate whether this skewed geometry affects how concepts are encoded. Using rank-constrained probes, we demonstrate that both architectures encode concepts in subspaces of surprisingly similar dimensionality. Furthermore, we demonstrate that the transformers' dominant principal direction does not inherently encode more conceptual information. Finally, we zoom in and examine the alignment between manifolds, either by analyzing representations of specific topics or by looking at the nearest neighborhoods of tokens, and find that they are highly aligned. Ultimately, our analysis suggests that while transformers and SSMs induce different usage of latent space, they display a striking functional convergence at the level of local semantic manifolds.

---


### 483. [Enhancing Table Structure Recognition via Bounding Box Guidance](https://arxiv.org/abs/2609.08705)

**<font color=#1a73e8>作者：</font>** Lei Hu, Shuangping Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Table Structure Recognition (TSR) aims to extract the bounding boxes of cells and table structure (e.g., HTML) from table images. Although current approaches have made significant progress, the latest image-to-sequence methods overlook the explicit utilization of the bounding box information when predicting HTML sequences, leading to error predictions in complex scenes. In this paper, we introduce a novel framework BGTR (Bounding Box-Guided Table Recognizer). To more effectively utilize bounding box information, we first predict the bounding boxes of cells and then use this information to guide the generation of HTML sequences. While utilizing bounding box information can enhance the accuracy of HTML sequences, for natural scene tables, the data volume is too small to allow for sufficient training of bbox-guided HTML generation. In response, we adopt a progressive training method for natural scene tables and introduce SNSTab, a synthetically generated natural scene table dataset. Our experiments on five benchmark datasets demonstrate SOTA performance.

---


### 484. [GoAnt: Quality-Diversity Multi-Agent Search for Alpha Factor Discovery in Market Microstructure Data](https://arxiv.org/abs/2609.08719)

**<font color=#1a73e8>作者：</font>** Stella Zhao, Tommy Sha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated alpha factor discovery searches symbolic trading signals from price-volume panels and order-book data under a fixed evaluation budget. Existing single- and multi-agent program-search systems can overfit predictive proxies that fail after execution costs and repeatedly explore redundant factor families, limiting execution robustness and behavioral diversity. We introduce GoAnt, a quality-diversity multi-agent search framework that combines non-communicating Explorer, Exploiter and Connector workers with a shared adaptive Mental Map and a compact Queen dispatcher. The Mental Map organizes candidates by leakage-free execution profiles and retains one elite per niche, while the Queen reallocates the evaluation budget from explicit search-state summaries. We also define a map-independent effective-yield protocol that counts high-quality, mutually nonredundant factors directly from each method's evaluation records, giving archive-based and map-free systems the same ruler. On real A-share microstructure data spanning 2023--2026, GoAnt reaches quality-weighted yields of 41.8 and 47.6 in price-volume and order-book settings, improving the strongest baseline by 57% and 97% under matched budgets. Its locked populations retain 0.64 and 0.67 of in-sample quality out of sample, compared with 0.61 and 0.63 for a static map.

---


### 485. [BAFF: Bid-Aware Filter Family for Mitigating Training Data Interference in RTB A/B Tests](https://arxiv.org/abs/2609.08725)

**<font color=#1a73e8>作者：</font>** Jeonglyul Oh, Ikkyu Choi, Inseop Youn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In online A/B tests for real-time bidding (RTB), control and treatment models are typically trained on a shared serving log that includes data generated by the counterpart model. This shared-log training biases each model's training data through two channels: the counterpart model may have selected a different ad from the ad-candidate pool (ad-ranking disagreement) and may have bid a different price (bid-pricing disagreement), potentially distorting the A/B test outcome. Log-splitting eliminates the bias but sacrifices training data; log-sharing retains all data but leaves the bias unaddressed. We formalize the Bid-Aware Filter Family (BAFF), a class of (k,l)-parameterized hard filters that controls tolerance to each channel independently, providing a structured search space between these two extremes. We further propose a three-stage online measurement protocol that enables evaluating data-sharing strategies by their deviation from an interference-free reference model in production. In offline simulation, a (k,l) sweep surfaces operating points with smaller deviation from the interference-free reference model than both log-sharing and log-splitting. In a live RTB deployment on a demand-side platform (DSP), filter-based variants preserve the reference model's business metrics (e.g., CPC, CTR) more closely than both baselines. The best operating point is setting-dependent, underscoring the practical value of the search space itself.

---


### 486. [Application of curiosity driven exploration methods for hardware interference identification](https://arxiv.org/abs/2609.08729)

**<font color=#1a73e8>作者：</font>** Ludovic Matar, Clement Moulin-Frier, Pierre-Yves Oudeyer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The transition from single-core to multi-core architectures in safety-critical embedded systems introduces significant challenges due to inter-core interference caused by contention for shared hardware resources. Such interference affects execution times and complicates the verification of strict temporal requirements, particularly in domains such as avionics where standards require comprehensive identification of interference sources. Existing interference analysis approaches, whether manual or model-based, struggle to capture the full range of behaviors arising from the complex interactions among micro-architectural components. In this paper, we frame multi-core interference analysis as the exploration of a complex system behavior space. We propose the use of curiosity-driven exploration algorithms from artificial intelligence to systematically and efficiently cover the space of possible interference behaviors. Using a simulator-based environment, we show that the proposed approach achieves broader and more uniform behavioral coverage within a limited experimental budget compared to traditional pseudo-random program generation methods.

---


### 487. [CVT-GS: Learning to Simplify 3D Gaussian Splatting with Centroidal Voronoi Tessellation](https://arxiv.org/abs/2609.08730)

**<font color=#1a73e8>作者：</font>** Bingxian Li, Yilong Li, Jingliang Peng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While 3D Gaussian Splatting (3DGS) has emerged as a powerful representation for real-time novel view synthesis, rendering high-fidelity scenes often relies on a massive number of Gaussian primitives, incurring substantial storage and computational overhead. Existing simplification techniques are largely intrusive, requiring training-time pruning, architectural modifications, or computationally expensive per-scene fine-tuning. These drawbacks limit their deployment on off-the-shelf pretrained models. In this paper, we propose CVT-GS, a novel optimization-free post-hoc simplification framework that directly compresses trained 3DGS scenes without sacrificing visual fidelity. Our approach first constructs spatially coherent cells over Gaussian centers via a geometry-aware Centroidal Voronoi Tessellation (CVT). Subsequently, a lightweight neural cell merger predicts the geometry and appearance of a single, highly representative Gaussian primitive for each cell under differentiable rendering supervision. By formulating simplification as a rendering-aware many-to-one merging process rather than naive primitive pruning, CVT-GS outputs a standard 3DGS scene that is seamlessly compatible with existing renderers. Experiments on various datasets demonstrate the superiority of our method. Notably, when achieving a 100-fold reduction in Gaussian points, our method operates 12 times faster than state-of-the-art methods while improving the PSNR by 1.3 dB.

---


### 488. [When Can One Obtain Certificates of Optimality Using Positivstellensaetze?](https://arxiv.org/abs/2609.08736)

**<font color=#1a73e8>作者：</font>** Nayoon Kim, Allen Gehret, Shenyuan Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study certificates of positivity and optimality for learning problems whose objectives and constraints need not be polynomial. We isolate an axiomatic core of Fischer's constructive strict and weak Positivstellensätze and prove the resulting theorems for abstract function algebras over ordered fields. The framework separates two roles that can otherwise be conflated: objective and constraint functions may be built from broad classes of continuous or definable operations, while the auxiliary primitives used to construct a certificate satisfy explicit scalar and closure axioms. We give instances over continuous and definable function algebras, including ordered fields not closed under square roots, derive lower-bound and global-optimality certificates, and analyze both expanded term length and shared computation-graph complexity.

---


### 489. [PAC-Bayesian Bounds for Learning Partially Observed Stochastic Linear Time-Invariant State-Space Systems with Inputs and Sub-Gaussian Noise](https://arxiv.org/abs/2609.08740)

**<font color=#1a73e8>作者：</font>** Mihaly Petreczky, Mohamad Al Ahdab, John Leth  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper we derive a Probably Approximately Correct (PAC)-Bayesian error bound for partially observed linear time-invariant (LTI) stochastic dynamical systems in state-space form with inputs and sub-Gaussian noise. Such bounds are widespread in machine learning, and they are useful for characterizing the predictive power of models learned from finitely many data points. The bound derived in this paper relates the expectation of prediction errors with the prediction error generated by the model on the data used for learning. In addition, we show that it can also be used to derive bounds for the parameter estimation error. In turn, this allows us to provide finite-sample error bounds for the prediction error and parameter estimation error for a wide class of system identification algorithms. Furthermore, as LTI systems are a sub-class of recurrent neural networks (RNNs), these error bounds could be a first step towards PAC-Bayesian bounds for RNNs.

---


### 490. [Kairos: A Dataset for Fine-Grained Video-Language Modeling over Space, Time, and Dynamics](https://arxiv.org/abs/2609.08755)

**<font color=#1a73e8>作者：</font>** Ruibo Ming, Lei Sun, Deheng Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many emerging video language modeling tasks require systems to move beyond clip-level abstraction and model visual content as it unfolds over extended time horizons. However, most existing video datasets rely on coarse or sparsely aligned supervision, which compresses temporal variation and limits the ability of models to learn reusable representations of continuous visual dynamics. We introduce Kairos, a video dataset for video-language modeling with time-resolved annotations. Kairos consists of long-duration videos, ranging from ten minutes to half an hour, annotated with fine-grained temporal alignment. The annotations capture ongoing actions, entity appearances and attributes, interactions, and evolving contextual cues along the video timeline. This time-resolved structure supports fine-grained evaluation, long-range modeling and reasoning, instruction data construction, representation learning, and video generation. Kairos provides a general-purpose foundation for modeling visual experiences over time.

---


### 491. [ZK-Trace: Certified Collusion Tracing with Zero-Knowledge Credentials for Federated GNSS Interference Monitoring](https://arxiv.org/abs/2609.08763)

**<font color=#1a73e8>作者：</font>** Redwanul Karim, Nisha L. Raichur, Lucas Heublein 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated global navigation satellite system (GNSS) monitoring distributes a proprietary classifier to partly trusted stations, any of which may leak its copy. ZK-Trace combines public identity marks, recipient-specific Tardos fingerprints, and zero-knowledge credential verification. The registry supports offline tracing without the leaker's cooperation. We establish conditional false-accusation bounds for arbitrary recovered bit patterns, a finite completeness bound under a hidden-bias residual channel, and a deterministic tracing-score bound for correlated feature-distillation errors. An interval-arithmetic checker makes the conditional bound executable and allocates a common budget across accusation and tamper decisions. Under innocent-row independence, the certificate-based evaluation uses a false-naming budget of 0.001 per investigation. It isolates all 160 single-owner copies and traces 712 of 720 two-owner mixtures without naming an innocent. Experiments use a simulated GNSS federation and CIFAR-10. Feature matching preserves the feature mark in 20/20 runs and cross-architecture transfer in 19/20, at copy-accuracy costs of 4.8 and 6.1 percentage points on GNSS and CIFAR-10. Function-only distillation erases the feature mark, and distillation also removes weight-space marks. These results support verifiable tracing under explicit statistical and cryptographic assumptions. Credential knowledge and recipient evidence serve distinct roles.

---


### 492. [Compensating for Scarce Historical Images in Cross-Domain Cultural Heritage Retrieval Using Synthetic Aging](https://arxiv.org/abs/2609.08766)

**<font color=#1a73e8>作者：</font>** Marcin Iwanowski, Adam Mazgaj, Ferdynand Gorski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cultural heritage collections often contain contemporary and historical visual records of the same physical object. Linking these records is difficult because corresponding images may differ in viewpoint, acquisition conditions, color reproduction, framing, resolution, and degradation, while genuine historical images are frequently scarce. This study investigates whether synthetically aged contemporary images can replace or complement missing historical training data in bidirectional instance-level retrieval. Synthetic old-domain images are generated using degradation-oriented transformations. An EfficientNetV2-M model is evaluated on identity-disjoint training, validation, and test sets across three dataset partitions and three training seeds. Mixed real-synthetic training is compared with real-only baselines using proportionally scaled and fixed 300-batch-per-epoch schedules. Complete replacement of genuine historical images reduced bidirectional mean R@1 from 86.56% to 81.27%, showing that synthetic aging does not reproduce the full genuine old-domain variability. Increasing the number of independently generated synthetic variants provided no consistent improvement. Under controlled scarcity, however, synthetic completion improved mean R@1 by 3.69 percentage points at 25% genuine historical coverage and by 2.92 points at 50%, relative to the proportionally scaled real-only baselines. At 75%, the gain decreased to 2.00 points, while performance remained comparable to the complete-real-data reference. Fixed-schedule real-only controls did not reproduce these improvements. The results indicate that genuine and synthetic observations are complementary. Synthetic completion primarily benefits retrieval by extending cross-domain identity coverage rather than by increasing training exposure, with its contribution gradually decreasing as genuine historical coverage increases.

---


### 493. [AXS-Net: Interpretable Deep Unfolding for Hyperspectral Image Denoising via Spectral Basis Unmixing and Structured Noise Refinement](https://arxiv.org/abs/2609.08777)

**<font color=#1a73e8>作者：</font>** Ziyi Guan, Jianping Zhang, Zheng Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral images (HSIs) are often degraded by mixed noise, including band-dependent Gaussian perturbations and structured artifacts such as stripes, dead-lines, and impulse noise. Most deep denoisers regress the clean image directly, entangling signal and structured noise. We instead model HSI denoising as $\Y=\A\X+\Snoise+\Nnoise$, where $\A\X$ is a low-rank spectral-subspace (unmixing) reconstruction, $\Snoise$ is structured sparse noise and $\Nnoise$ is residual Gaussian noise. The resulting regularized optimization problem is unrolled into AXS-Net, a $K$-stage alternating proximal-point framework. Each stage combines an analytic spectral-basis gradient step, an SSX-Block proximal operator for abundance coefficients, and an SBlock proximal operator for the structured residual with column-consistent and sparse priors. This optimization correspondence exposes interpretable endmembers, abundance maps, and structured-noise estimates. Across ICVL, CAVE, and Harvard datasets and five noise configurations, the proposed AXS-Net achieves strong in-domain accuracy and competitive zero-shot transfer, with consistent gains across all five noise regimes on ICVL and Harvard. The recovered structured-noise closely follows the synthetic reference, and the recovered spectral basis is smooth and band-ordered rather than an arbitrary set of latent channels.

---


### 494. [Improving Term Evaluation in Machine Translation: Variation Matters](https://arxiv.org/abs/2609.08779)

**<font color=#1a73e8>作者：</font>** Nicolas Dahan, Ziqian Peng, François Yvon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Terminology evaluation in machine translation (MT) usually assumes a single correct target form per source term. However, human translators routinely introduce variation that current metrics penalize as inconsistency. We examine how to account for this variation in document-level MT evaluation of English-French scientific translation, combining glossary-based accuracy, translation consistency, and a new cross-term variation (CTV) diagnostic measure that tests whether variation relationships are preserved across languages. Based on analyses of two parallel corpora, translated by four MT systems, we find that (1) MT systems generate less target-side variation than human translators; (2) transfer patterns strongly depend on the variation type; (3) consistency rankings vary with the choice of metric; and (4) constraining MT with a glossary improves accuracy and consistency but degrades CTV by suppressing valid variation. We argue for variation-aware evaluation that conditions consistency penalties on whether target-side variation mirrors source-side variation.

---


### 495. [Interpretable Hyperspectral Unmixing Framework with Fixed Endmember Prior and Structured Residual Refinement](https://arxiv.org/abs/2609.08786)

**<font color=#1a73e8>作者：</font>** Ziyi Guan, Jianping Zhang, Qian Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral unmixing decomposes mixed pixels into material endmembers and their abundances from contiguous spectral observations. In modular sensing pipelines, endmembers are often first identified and then treated as fixed during abundance estimation. When this fixed endmember prior is inaccurate, spatially structured mismatch arising from illumination changes, sensor artifacts, or material boundaries may be incorrectly captured by the abundance variables, leading to unstable decompositions. This study presents an interpretable stage-wise hyperspectral unmixing framework (I-HyperSU) under fixed endmember priors, which is explicitly decomposed into a fixed endmember matrix $\mathbf{A}$, an abundance block $\mathbf{X}$, and a structural residual refinement block $\mathbf{S}$. The X-block estimates abundances using FISTA with nonnegativity and sparsity enhancement, and a soft penalty that approximately enforces sum-to-one constraints. The S-block jointly applies low-rank SVD structural regularization and a lightweight deep image prior (DIP) to refine structured residuals. This staged design makes the interaction between abundance and residual components transparent and interpretable. Experiments on Samson, Urban, and Jasper Ridge datasets demonstrate that, under fixed and imperfect endmember priors, soft abundance relaxation consistently outperforms hard simplex projection. Under the default N-FINDR endmember prior, the proposed framework reduces the joint reconstruction error by 61.7\%--69.5\% compared with a fixed-$\mathbf{A}$ UCLS baseline, while keeping the abundance RMSE nearly unchanged, indicating that the residual refinement branch accounts for structured model mismatch without degrading the abundance estimates. For example, on Urban, the reconstruction SAM decreases from $5.99^\circ$ for the X-only model to $1.92^\circ$ for the full model.

---


### 496. [Adaptive Anisotropic Attention for Axis-Structured Signals](https://arxiv.org/abs/2609.08788)

**<font color=#1a73e8>作者：</font>** Mahir Jain, Parshva Runwal, Aditya Ray Mishra 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dense self-attention treats all token pairs as equally plausible before learning, an interaction-isotropic prior that can be mismatched to structured signals. For structured, low signal-to-noise ratio (SNR) signals such as EEG, dependencies are organized along the electrode and time axes, and this uniform prior exposes each token to many irrelevant interactions. We introduce Adaptive Anisotropic Attention (AAA), which splits attention into two paths: a temporal path, where each token attends to the tokens of its own electrode across time, and a spatial path, where it attends to the tokens of the other electrodes at the same time step. A small gate predicts, for every token, a convex combination of the two path outputs: two non-negative weights that sum to one. On six EEG downstream tasks, the resulting model, AXON (AXis-factorized Operator Network), improves mean balanced accuracy over a dense baseline under both linear probing and full fine-tuning. We show that both paths (temporal and spatial) are necessary and that the weighted sum beats a hard choice of one path; most of the benefit comes from the gate learning a different temporal/spatial balance at each layer of the network. Controlled audio spectrogram experiments show that axis factorization transfers beyond EEG. These results suggest that aligning attention with the natural axes of structured signals provides a useful inductive bias.

---


### 497. [Hi-FLoop: Hierarchical State-Feedback Loops for Multi-Timescale World Modeling](https://arxiv.org/abs/2609.08796)

**<font color=#1a73e8>作者：</font>** Rx Fan, Zhan H  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-agent traffic simulation seeks diverse, coordinated, and physically realistic futures from maps and observed history. Long-horizon closed-loop generation must reconcile multiple decision time scales while its context evolves with generated states. Existing methods often unfold long futures from the initial scene and resolve intent, interaction, and motion monolithically, weakening cross-scale consistency and adaptation. We present HI-FLOOP, a branch-consistent multi-timescale state-feedback framework. Eight scene-level Worlds represent joint hypotheses, and all agents share the selected World identity throughout an 8-second rollout. Within the branch, an 8-second Goal anchors intent, a 2-second Preview coordinates interactions, and 1-second Control produces physical motion. Every 0.5-second commit feeds back only its executed prefix as new facts, while unexecuted hypotheses never enter factual memory. Joint Preview Interaction (JPI) induces a sparse directed future graph from Preview and uses conflict probabilities and signed arrival-time differences to gate interaction refinement. For generated-state recovery, a prefix-frozen A-to-B cascade lets frozen Model A generate 0-1 seconds, then transfers typed physical state, admissible context, and the branch index, but no latent state, to an independent Model B for re-encoding and 1-2-second recovery. On the full H-D public-validation split of 955 scenarios, one complete S1 run yields an Overall score of 0.689987 with the official evaluator. Under agent-centric oracle evaluation, HI-FLOOP achieves oracle-minADE@8 of 1.196636 m over the 8-second horizon and 0.526 m over the 6-second horizon.

---


### 498. [Eliciting Weak-to-Strong Generalization with On-Policy Reverse Distillation](https://arxiv.org/abs/2609.08798)

**<font color=#1a73e8>作者：</font>** Youngrok Park, Sangmin Bae, Hojung Jung 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weak-to-strong generalization asks whether stronger models can learn from weaker supervisors and surpass them. This question is particularly important for successive model generations and multi-domain consolidation, where repeating frontier-scale post-training from scratch can be prohibitively expensive. Yet conventional distillation treats the weak teacher as an optimization target, potentially imposing its capacity ceiling on the student. We introduce On-Policy Reverse Distillation (OPRD), which evaluates the teacher's policy shift relative to its reference policy on student rollouts and amplifies the component of the student's verifier-driven policy gradient along that direction. By rescaling only verifier-supported updates, OPRD preserves the stationary points of policy optimization while accelerating learning beyond the teacher. In both successive model transfer and multi-teacher distillation, OPRD achieves higher performance with fewer student updates than existing RL and distillation approaches. Response-style analysis shows that OPRD students remain closer to models trained with verifier-based RL alone than to their weak teachers, suggesting that teacher guidance accelerates rather than redirects the student's own optimization. Results in conventional strong-to-weak distillation further demonstrate that OPRD effectively combines verifier-driven policy optimization with teacher guidance regardless of capacity ordering.

---


### 499. [Evaluation Principles for MRI-MRA Registration in Trigeminal Neuralgia: An ROI-Centered Neurovascular Benchmark](https://arxiv.org/abs/2609.08805)

**<font color=#1a73e8>作者：</font>** Xupeng Zhang, Xihang Wang, Michael Xie 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Preoperative evaluation of trigeminal neuralgia (TN) often requires joint interpretation of structural MRI, which depicts the trigeminal nerve and surrounding cisternal anatomy, and time-of-flight MRA, which highlights vascular structures. Although MRI-MRA fusion is clinically attractive for visualizing neurovascular compression, this task is poorly captured by conventional whole-brain registration evaluation because the clinically relevant target is a small trigeminal ROI, vessel annotations are partial and clinically focused, local TOF-MRA contrast is variable, and field-of-view mismatch can limit deformable alignment. We formulate TN MRI-MRA fusion as an ROI-centered neurovascular registration-evaluation problem and construct a benchmark from 149 patients with clinician-annotated bilateral trigeminal ROIs. Six representative registration pipelines were evaluated using local image-based metrics, segmentation-derived vessel-localization metrics, prediction-volume analysis, and contrast- and FOV-stratified comparisons. Conventional evaluation summaries were often misleading: local image similarity, vessel-background separability, and downstream vessel localization did not co-rank methods; one-sided vessel distances were strongly affected by predicted vessel extent under partial annotations; and local MRA contrast determined when vessel-separability metrics were informative. Deformable refinement provided only a small, FOV-dependent benefit over affine alignment, while reader review showed that locally favorable vessel distances could coexist with globally implausible registrations. These findings indicate that TN MRI-MRA registration should be evaluated as a local, vessel-aware, contrast-sensitive, and FOV-aware visualization task rather than as generic multimodal brain registration. Our code is publicly available at this https URL.

---


### 500. [ArmPoser: Real-Time, Calibration-Free Arm Pose Estimation from Smartwatch IMU](https://arxiv.org/abs/2609.08806)

**<font color=#1a73e8>作者：</font>** Bishnu Dev, Vasco Xu, Xi-Aan Loh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Arm pose estimation enables applications in fitness, extended reality input, rehabilitation, and life logging. Prior smartwatch-based approaches rely on calibration poses and preprocessing pipelines that transform raw IMU measurements into standardized training formats. These steps hinder deployment in everyday settings and introduce errors due to imperfect calibration and sensor drift. We present ArmPoser, a calibration-free arm pose estimation system using a single smartwatch IMU. Our central contribution is training models directly in the reference frame native to consumer smartwatches, aligning learning with how IMU data is produced by deployed devices. By operating on device-native axes, ArmPoser removes the need for coordinate transformations, explicit alignment, and bone-offset calibration used in prior work. We further augment training with physically grounded variations in watch placement and arm morphology to account for user-specific variability. ArmPoser also includes a wear-configuration module that infers anterior or posterior forearm placement and crown orientation. We evaluate pose estimation on public benchmarks and on a 10-participant, 30-activity study using watchOS and Android smartwatches, where ArmPoser matches or exceeds calibrated baselines without any user calibration.

---


> [!TIP]
> 当前位于：**451-500**（第 10/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | **451-500** | [501-542](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
