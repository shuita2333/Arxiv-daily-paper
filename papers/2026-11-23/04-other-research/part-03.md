# 📦 其他研究 | 2026年11月23日

> 本类共 **265** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-265](./part-06.md)

---

### 101. [NIMIS: A Structure-Agnostic, Chemically Informed Slot-Attention Framework for Demixing 1D $^1$H-NMR Mixture Spectra](https://arxiv.org/abs/2611.25629)

**<font color=#1a73e8>作者：</font>** Anna Marija Sumrova, Jonathan M. Goodman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The products of chemical reactions are usually complex mixtures that must be separated into their components before interpretable $^1$H-NMR spectra can be obtained. Direct analysis of the spectra of crude mixtures would accelerate reaction analysis and facilitate the exploration of new chemical space. We present NIMIS, a structure-agnostic, attention-based deep learning framework that groups the peaks of a 1D $^1$H-NMR mixture spectrum according to the component from which they originate. J-coupling information is introduced directly into the attention mechanism of a multi-head Transformer encoder, and the resulting contextualised peak embeddings are separated into components by slot attention. NIMIS was trained on 158,005 synthetic mixtures constructed from experimental spectra in the NMRexp database, covering molecules of up to 20 heavy atoms composed of C, H, N, O, S, F, Cl, Br and I. On held-out molecules it reaches a peak-to-component assignment accuracy of 82.28% for noise-free input and 77.34% with 10% integral noise, with a mean NIMIS score of 0.83 for correct assignments. NIMIS outperforms a conventional Transformer and simple baselines, and its performance carries over to a scaffold-disjoint evaluation. By grouping peaks into component-level sets, NIMIS provides a foundation for more robust mixture analysis methods, including methods capable of handling overlapping signals.

---


### 102. [What One Sample Cannot See: Why Fewer Denoising Steps Can Score Higher on Physics Benchmarks](https://arxiv.org/abs/2611.25632)

**<font color=#1a73e8>作者：</font>** Yutao Li, Chen Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When a storm can head north or south, a forecast down the middle may score better under squared error than either plausible path. The same paradox appears when video generators are tested as world models: fewer denoising steps can raise physics scores even as videos blur or stop moving early. Why? Physics-IQ compares each generated video with one recording, although a scene can have multiple valid futures. An exact decomposition shows its scores can reward reduced variation among generated futures, even when their distribution becomes less accurate. We introduce Kernel Physics-IQ to remove this incentive in expectation, needing only two independent samples per condition. Two-step sampling lowers Kernel Physics-IQ in all five image-to-video models. For CogVideoX, the official score rises by 0.055 while ours falls by 0.131. Changing the sampling schedule reveals further differences official scores miss. In controlled physical systems with known outcome probabilities, our metric favors the true distribution over collapsed predictions. In short, a world model should be judged not only by how closely one video matches what happened, but by how faithfully its predictions represent what could have happened.

---


### 103. [AesDistill: Distilling Generative Aesthetics for Image Color Enhancement](https://arxiv.org/abs/2611.25635)

**<font color=#1a73e8>作者：</font>** Chuanzhi Xu, Chengkun Yue, Huiqi Liang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image color enhancement aims to improve visual appeal, but previous methods often learn to reproduce ground-truth expert targets. These targets reflect the preferences of a few experts and cover a limited range of aesthetic choices. Matching them does not ensure stronger aesthetic quality across different tastes and scenes. By contrast, large generative models learn rich visual knowledge from large image collections and often produce vivid, appealing image edits. However, direct generation can change the source image's semantic structure along with its colors. In this paper, we introduce AesDistill, a framework for distilling generative aesthetics into image color enhancement. We use 4 leading open-source large generative models to produce 64,644 edited images as teacher targets at a cost of about 3,360 H100 GPU-hours, forming the AesDistill Dataset. AesDistill also includes AesDistill Student, a 1.13M-parameter model that learns teacher color changes through confidence-weighted supervision while preserving the source image's semantic structure. We evaluate AesDistill with 12 aesthetic and 4 image-quality assessment models. Every teacher's targets rank above the FiveK and PPR10K expert target means in the joint assessment. Across both datasets, AesDistill Student outperforms all 20 baseline methods and ranks directly behind the 4 teachers. These results demonstrate that distilling aesthetics from generative models enables a compact student to outperform methods trained on expert targets.

---


### 104. [MambaLIFT: Reference-Based Mechanism-Aware Attribution for VMamba](https://arxiv.org/abs/2611.25644)

**<font color=#1a73e8>作者：</font>** Jintu Kakati, Niladri B. Puhan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Attributing predictions of visual state-space models remains challenging because input-dependent selective dynamics couple feature selection, recurrent state propagation, and shared computational pathways. We introduce MambaLIFT, a reference-based, multiplier-first attribution framework for VMamba that propagates contributions through its computational graph using interaction-aware rules for selective-scan injection, recurrent memory, LayerNorm, and shared pathways. MambaLIFT decomposes the reference-relative class-logit difference, \(f_c(x)-f_c(x^0)\), by spatial position, VSS block, scan direction, and computational mechanism. Experiments on ImageNet-1K evaluate VMamba-T and VMamba-B, with hyperparameters selected on a calibration set and faithfulness assessed on a disjoint held-out evaluation set. MambaLIFT achieves numerical conservation to floating-point precision across audited attribution interfaces in both configurations. Under mean-colour pixel flipping, it achieves significantly higher mean faithfulness scores than MambaLRP on both configurations and the highest scores among the evaluated methods, including Integrated Gradients with matched references. Under blurred replacement, MambaLIFT is non-inferior to MambaLRP on VMamba-T and equivalent on VMamba-B, indicating that its advantage depends on the replacement protocol. Ablations on VMamba-T show that interaction allocation, temporal propagation, and pathway composition affect attribution maps. Mechanism-level analyses further show that exact relevance conservation does not imply additive effects under finite interventions: the mechanism decomposition accounts for the reference-relative logit difference but does not estimate intervention effects or establish causal validity.

---


### 105. [TRACE: Attribute Execution for Sequential Image Editing](https://arxiv.org/abs/2611.25648)

**<font color=#1a73e8>作者：</font>** Xiyang Zhang, Yuanhe Tian, Hongzhi Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Given an image and successive user instructions, sequential image editing should return an updated image that satisfies each new request and preserves earlier requirements that remain active. This lets users develop a result without repeatedly restating or repairing their decisions. The difficulty is that a retrieved image can contain a valid color on an obsolete surface, while the current image may lack the newly requested material. Neither reference selection nor a precise object mask alone specifies how to reconcile attributes occupying the same region. We present TRACE, which separates the continuing attribute from its visual carrier and prioritizes local appearance operations under complete-request checks. Active-goal binding identifies what should persist, carrier selection supplies suitable current or newly generated pixels, and tonal calibration reduces tinting near highlights and shadows. Experiments across frozen editors, independent visual readers, new source images, and complete sequential benchmarks support joint color-material recovery and show how local execution preserves the surrounding scene.

---


### 106. [Extending Rademacher Complexity-Based Generalization Theory to Domain Generalization](https://arxiv.org/abs/2611.25650)

**<font color=#1a73e8>作者：</font>** Xi Wang, Liang Bai, Xian Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Domain generalization (DG) aims to train models on multiple source domains with distinct distributions to ensure robust performance on unseen target domains. In doing so, it elevates the concept of generalization from the traditional sample level to the distribution level. Existing theoretical frameworks introduce a domain space endowed with a meta-distribution to extend classical generalization analysis to this new setting. However, these approaches typically treat the domain space as devoid of geometry. In reality, the domain space is an inherently infinite-dimensional, nonlinear abstract space composed of probability distributions, and its complex geometric properties fundamentally determine generalization behavior. Consequently, existing geometry-free theories of domain generalization have a fundamental limitation. They lack a formal characterization of what distinguishes distribution-level generalization from sample-level generalization, leaving the inherent difficulty of generalizing across domains largely unexplained. To bridge this gap, we formalize the domain space as the Wasserstein space over the representation space. Building on the geometric properties of this space (specifically the $\mathrm{CD}(K,\infty)$ curvature theory) we derive a novel, geometry-dependent DG error bound. By introducing an additional curvature-dependent confidence term, this bound formally disentangles the two levels of generalization effects and reveals the essential nature that domain generalization is affected by both the invariance and the curvature of the representation space. Finally, we experimentally validate the effect of curvature on domain generalization.

---


### 107. [Multiple Criteria Decision Making Under XORness](https://arxiv.org/abs/2611.25652)

**<font color=#1a73e8>作者：</font>** Amin Hocine  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How should we make decisions under XORness? XORness is a class of uncertainty arising from indeterminacy, exclusivity, and hesitancy. We develop a multiple criteria decision making framework that preserves XORness throughout the decision process. We define XOR numbers and prove their fundamental arithmetic and algebraic properties. Building on these results, we extend the deterministic decision matrix to an XOR decision matrix and introduce a compatible normalization procedure. Further, we propose an additive XOR aggregation operator, which preserves indeterminacy, exclusivity, and hesitancy inherent in evaluations. In addition, we introduce an axiomatic XORness measure that quantifies the degree of uncertainty associated with global performance scores and develop a performance--XORness index to rank alternatives. We prove that this index induces a total preorder over the set of alternatives and identify the conditions for preserving dominance. The applicability of the developed framework is demonstrated through the risk assessment of cyberthreat scenarios in energy systems, and recommendations are derived using the XOR--weighted sum method.

---


### 108. [Correctable Enrollment and One-Transaction Seed Proofs for Ethereum's Post-Quantum Transition](https://arxiv.org/abs/2611.25663)

**<font color=#1a73e8>作者：</font>** Xin Jin, Maximillian Liao, Handong Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A quantum computer running Shor's algorithm can extract the private key of every Ethereum account whose public key is published, and accounts exposed by their own transactions hold 54.6% of execution-layer ETH. As the first such machine may stay secret, a migration cannot wait for visible thefts, and once keys are extractable, legacy signatures no longer tell owners from attackers. We design a migration in which owners enroll post-quantum keys cheaply with their existing signatures before ECDSA is retired at a scheduled time, while a zero-knowledge proof of the wallet's BIP-39 seed can correct any such enrollment until a common deadline afterward; an account nobody enrolled stays frozen and recoverable by seed proof without a deadline. Each proof binds the new key, a nonce and a fee cap, so neither a paying sponsor nor a reordering block builder can redirect or replay it. Validators switch to hash-based keys first, at a finalized checkpoint and under a stated bound on the attacker's voting power. We prove the account guarantees under explicit assumptions, model-check the rules, and implement the design in go-ethereum and a Lean consensus client. A three-layer recursive hash-based STARK yields a seed proof of about 190 KB that fits one transaction, verifies in 38 ms and takes a median of 111 s to generate on a laptop; four proofs aggregate into one. In a ten-node simulation with mainnet-derived accounts and fee demand, block space rather than proving sets the duration: the 4.45 million accounts with at least 0.1 ETH would migrate in 29.4 days if all enroll before ECDSA is retired and in 235 days if all recover after it in batches of four. In a mass enrollment, an enrollment waits a median of 19.1 minutes in the public mempool, longer than published estimates for a fast quantum computer to extract its key, so owners with a seed and an unexposed key should migrate by seed proof.

---


### 109. [GPU-Accelerated Secure Inference for Drug--Target Interaction Prediction](https://arxiv.org/abs/2611.25664)

**<font color=#1a73e8>作者：</font>** Sikha Pentyala, Steven Golob, Daniil Filienko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep learning models that predict drug--target interactions (DTI) can speed up drug discovery, but the candidate drugs they score are valuable intellectual property that their owners cannot reveal. Secure multiparty computation (MPC) lets two servers compute a prediction on a secret-shared drug, without either server learning the drug. However, secure inference of deep models is slow. Non-linear operations require communication between the servers, and MPC arithmetic does not map naturally to GPUs. In this paper, we present our solution to Track~III of the iDASH 2026 privacy and security competition, which asked for fast two-party secure DTI inference on GPUs. Our solution is built on the co-design of MPC-friendly models and MPC protocols. On the model side, we design SlimDTA, a DTI model that reduces the operations on the secret drug, and in particular the non-linear operations that require communication. On the protocol side, we build a GPU framework that evaluates the linear layers with additive secret sharing and the non-linear layers with function secret sharing, including a custom CUDA kernel for the comparisons. Our solution won first place in the competition, at under 10,ms per prediction on average, and its secure predictions match the plaintext model to within 0.02%.

---


### 110. [LATER: Learning Action-Conditioned Temporal Evidence Retrieval for Predictive World Models](https://arxiv.org/abs/2611.25671)

**<font color=#1a73e8>作者：</font>** Zihan Zhou, Wenxi Xu, Qilin Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Early interactions can reveal physical properties that later observations no longer show. These properties can still gov- ern the effects of future actions. Inspired by the distinction between retention and selective readout in working mem- ory and cognitive science, we introduce LATER, an action- conditioned world model built on CF-JEPA. LATER stores completed real transitions in partitioned memories that remain fixed during candidate rollouts. A response bridge queries these memories using the current state and candidate action, while multi-cut auxiliary supervision trains the memory writ- ers. On distracted Two-Stage PushT, LATER raises terminal success from 15.5% to 25.0% over reconstructed CF-JEPA. In a separate comparison across six models and two scratch- training seeds, LATER achieves the lowest mean physical readout error in both clean and distracted views, reducing along-push mean absolute error (MAE) under distractors by 20.2% relative to CF-JEPA. Controlled history interventions show that later predictions depend on earlier physical evi- dence even when query observations and actions are fixed, with larger effects during pushing than waiting.

---


### 111. [Minimal Memory for Correctable Visual Continuation](https://arxiv.org/abs/2611.25675)

**<font color=#1a73e8>作者：</font>** Xiyang Zhang, Yuanhe Tian, Hongzhi Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Given past images and known actions, visual continuation generates future frames from one evolving scene state. Keeping this state revisable matters when an object reappears or a later view changes an earlier interpretation. Once past images cannot be replayed, a summary sufficient for current rendering can lose candidates needed after correction. We establish matching sparse and dense bounds on the bits needed for later correction under stable observations and bounded disagreement. For static streams at the stated smoothness and margin scales, correction incurs at least logarithmic overhead in one dimension and polynomial overhead in higher dimensions. Coherent Archive Memory (CAM) stores geometric summaries with exact updates under clipped expansion and coordinate assignments, then uses historical existence constraints to select one state for all requested frames. Exhaustive photographic tests show strict worst-truth image-risk gains from joint witnesses, while controlled neural continuations recover positions hidden in the current view.

---


### 112. [Explainability of genotype embedding models through observed cohort paths](https://arxiv.org/abs/2611.25681)

**<font color=#1a73e8>作者：</font>** Amashi Niwarthana, Aloysius Tan, Jagath C. Rajapakse  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models that combine genotypes with neuroimaging predict neurological diseases more accurately than either modality alone. Their clinical use, however, requires identifying which genetic variants a prediction is based on. Path-based attribution methods like Integrated Gradients address this by integrating the model's gradient from a baseline to the input. These methods assume the model accepts any point along that path as a valid input. Genotype models violate this assumption. They map the three discrete allele dosages \{0,1,2\} to vectors through a learned embedding defined only at those values, so a straight line passes through fractional genotypes at which no embedding, and therefore no gradient, exists. Attribution must therefore proceed in embedding space where the choice of path can affect the resulting attribution. We show that the commonly used per-variant estimator does not generally satisfy completeness. Additive separability guarantees completeness for this estimator, but interactions between variants generally break that property. Instead, we integrate along piecewise-linear embedding-space paths connecting genotype waypoints observed in the training cohort. Each path satisfies completeness in the continuum although the interiors of its segments are not necessarily observed. Our method improves faithfulness over Integrated Gradients and discretized Integrated Gradients under both perturbation protocols, achieves the strongest results for Parkinson's disease classification under support-preserving perturbations, and is competitive with a support-background Shapley baseline under per-variant perturbations. It also shows higher seed stability and better recovery of planted non-additive effects in a synthetic benchmark.

---


### 113. [D3-Cache: Accelerating Diffusion Models with Dynamic Mode Decomposition](https://arxiv.org/abs/2611.25689)

**<font color=#1a73e8>作者：</font>** Yanbo Li, An Xiang, Xiaoxin Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers generate high-quality images and videos, but every sampling step requires a full network evaluation. Training-free caching reduces this cost by reusing or forecasting network outputs across steps, but common approaches use per-model calibrated skip criteria or maintain per-layer prediction histories. We present D3-Cache, which applies Dynamic Mode Decomposition (DMD) to Diffusion sampling: it fits DMD to a short history of exact velocities and forecasts only the velocity that the scheduler consumes. A horizon-aware gate decides when to skip: whenever the network is evaluated, its output is compared with the forecast for that step, and the larger the error, the sooner the network is evaluated again, up to a cap on consecutive skipped steps. D3-Cache requires no training or per-model offline calibration curve and adds negligible memory. It shares one history length and risk tolerance across the four evaluated models. On four state-of-the-art image and video models, D3-Cache achieves speedups of 2.6-3.8x with high fidelity to the base model output.

---


### 114. [Measurable Does Not Imply Transportable: A Prospective Audit of Model Explanations in Multi-Year Field Trials](https://arxiv.org/abs/2611.25692)

**<font color=#1a73e8>作者：</font>** Rayhaneh Shabani Nia, Ali Karkehabadi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model explanations are increasingly used as scientific evidence, yet it remains unclear what they license scientists to conclude beyond the data on which they were constructed. When a fine-grained explanation fails to replicate, the failure may be attributed to noisy measurement of its target, raising a fundamental question: does reliable measurement imply a reproducible explanation? We test this directly. We formalize prospective explanation transportability: the extent to which an explanation learned from past data is recovered in a genuinely future context. This property is distinct from feature importance and measurement reliability. Using multi-year Genomes-to-Fields maize trials, where each new year is a real future context rather than a random resample, we evaluate 16 agronomically interpretable environmental concepts across five forward splits and one prospectively locked test year. Coarse environment-level explanations transport reliably (median cosine 0.83); their locked 2024 value, 0.811, fell within a prespecified 80% bootstrap percentile interval. For grain yield, genotype-conditioned explanations have a historical median cosine of 0.30 and range from 0.006 to 0.822 across years. Reliability does not order these outcomes: the year with the highest split-half reliability had the lowest explanation transport. Within-context resampling showed that GxE explanations were reproducible within a fixed context (0.77-0.95) while exhibiting lower prospective alignment across the 2020-2023 transitions (0.01-0.36). A second phenotype transports strongly at both resolutions, and non-temporal validation inflates apparent interaction-level transport by +0.22. These results show that target reliability and within-context explanation reproducibility do not by themselves establish when a model explanation can support a reproducible scientific claim.

---


### 115. [LIFT: Lifting Language-Controlled Image Fusion to Free-Viewpoint 3D Scenes](https://arxiv.org/abs/2611.25696)

**<font color=#1a73e8>作者：</font>** Jingning Tian, Hao Zhang, Yumin Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal image fusion traditionally generates a single fused image from paired observations at a specific viewpoint, limiting comprehensive scene perception and adaptability to diverse perceptual objectives. To overcome these limitations, we present LIFT, a novel framework for our proposed language-controlled 3D image fusion (L3D-IF) paradigm that extends multimodal image fusion from 2D images to free-viewpoint 3D scenes, enabling language-guided fusion tailored to diverse perceptual objectives. First, LIFT formulates Semantic Modality Binding (SMB), which interprets language instructions to identify semantic targets and their associated modality preferences and grounds these targets in corresponding regions of a shared Gaussian scene, establishing persistent semantic-to-spatial correspondences for consistent fusion control across viewpoints. Second, Language-Conditioned Gaussian Appearance (LCGA) is developed to achieve scene-wide multimodal appearance modeling by combining adaptive multimodal blending with language- and viewpoint-conditioned appearance refinement, enabling spatially adaptive realization of diverse fusion appearances while preserving source fidelity at pure-modality endpoints. Finally, we construct a Multi-View Language-Supervision (MVLS) dataset that associates language instructions and calibrated viewpoints with modulated fused images, providing effective supervision for learning instruction-dependent fusion from finite multi-view observations. Extensive experiments demonstrate that LIFT achieves coherent multimodal fusion across continuous viewpoints, accurate semantic target localization, and consistent regional fusion control under diverse language instructions.

---


### 116. [Calibrate in Context: Efficient Data-Free Quantization from Small Synthetic Pools](https://arxiv.org/abs/2611.25711)

**<font color=#1a73e8>作者：</font>** Haowen Hua, Sen Lin, Yaokun Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We enable accurate low-bit recovery from small synthetic pools by improving both image synthesis and student preparation. A grid with lower local response error can incur greater error in the student's block context. Functional Grid Calibration (FGC) selects activation scales and integer offsets against full-precision responses constructed from the student's current block input. With weights fixed during calibration, FGC evaluates candidates only at their consuming operators, bringing block context to calibration at nearly local-scoring cost. For DeiT and ViT, progressive inversion updates the same images through increasingly deep teacher prefixes. With 1,000 images, the complete pipeline exceeds MimiQ's reported accuracy in all 18 W4A4/W5A5 settings across nine backbones. With 256 images, DeiT-S and ViT-S reach 68.20% and 66.90% ImageNet top-1 accuracy at W4A4 in 26-27 minutes on one RTX 5090. The pipeline outperforms strengthened 1K-image MimiQ by 13.03 and 24.36 percentage points at lower preparation cost and the same recovery-update count. The same low-budget checkpoints retain their advantage on ImageNetV2.

---


### 117. [SkillLens: Action-Guided Dense Visual Dynamics for Proficiency Estimation](https://arxiv.org/abs/2611.25712)

**<font color=#1a73e8>作者：</font>** Deokhyun Ahn, Hyukjin Kim, Jae-Ho Han 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human proficiency estimation is challenging because skill is a high-level and often subjective property that is not captured by action identity alone. Existing approaches leverage multimodal observations such as ego-exo video, gaze, pose, and inertial signals, but the gap between sensor-level evidence and abstract proficiency labels remains difficult to bridge. We present SkillLens, a proficiency estimation framework that uses atomic action descriptions as temporal guidance, rather than direct semantic supervision, to localize proficiency-relevant windows for dense visual-dynamics extraction. Each window is summarized into an action-dynamics feature and scored by a high-low prototype margin against higher- and lower-proficiency executions from the same activity-action category. Fusing these ego/exo PDM cues with a global ego-exo-gaze baseline through CORAL ordinal calibration, our method achieves 0.542 accuracy on Ego-Exo4D. Our project page is available at this https URL

---


### 118. [SteerTrace: Tracing How Target Attacks Steer World Action Models](https://arxiv.org/abs/2611.25719)

**<font color=#1a73e8>作者：</font>** Yukun Dai, Tianshi Wang, Fengling Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World action models (WAMs) predict future videos and actions with one backbone, and their imagined future is often seen as a safety signal. We introduce SteerTrace, a targeted universal attack on WAMs that also traces its effect inside the model. One $\ell_\infty$-bounded (4/255) perturbation per model, shared across frames, tasks, and camera views, pushes the executed action toward an attacker-chosen target. On eight WAMs from four families (FastWAM, Faster-WAM, OpenWAM and LingBot-VA) on LIBERO and RoboTwin, it drives task success close to zero and moves the attacked action toward the target. Same-budget noise and BadWAM produce little action shift in the target direction. We use the signed targeted effect to measure how much of the effect each intervention removes or reproduces. Under the standard attack, restoring future tokens removes 61-94% of the targeted effect in the five models whose action experts attend to them. When the attack is constrained to keep the predicted future close to the clean prediction, the targeted effect can become more dependent on current-frame tokens. In three of these five models, restoring current-frame tokens removes 87-99% of the effect, compared with 9-15% for future tokens. In six models, restoring just 0.36% of the FFN neurons in layers 10-29 of the video expert removes 72-96% of the targeted effect. Residual directions 2-16 hold only 11-18% of the shift energy, yet removing them cancels most of the targeted effect.

---


### 119. [MemMend: A Selective Revision Framework for Memory Question Answering](https://arxiv.org/abs/2611.25721)

**<font color=#1a73e8>作者：</font>** Sheng Shi, Geng Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Revising every answer from a long-term memory can consume substantial inference budget and damage facts that were already correct. We introduce MemMend, a modular selective revision framework that routes potentially incomplete answers to an editor, represents corrections as bounded exact-text replacements, and accepts only edits with resolvable source coordinates and valid edit operations. The editor preserves the current answer when no legal repair is proposed; accepted edits require no additional semantic-verification call. On 1,986 LoCoMo development questions, MemMend achieves 67.17 conversation-macro F1 and 88.35 mean Judge score, improving over a verified revision chain by 0.82 and 1.24 points while using 62.37% fewer revision calls. Routing uses 54.15% fewer revision calls than ungated local review, with similar F1 but a 0.67-point lower Judge score. Applied directly to native PropMem, Mem0, and SimpleMem answers, the editing interface raises F1 by 3.79, 6.44, and 0.42 points. It outperforms same-gate rewriting and saves 49.85-83.72% of editing calls relative to ungated editing, which retains higher F1 in this adaptation. A source-by-editing factorial supports local editing for F1 but leaves an independent quality benefit from source obligations unresolved. Transfer to 451 LongMemEval-V2 Small questions also favors revision efficiency, while an external PerLTQA dialogue subset reveals a completeness gap. These results support selective editing as a reusable quality-cost operating point.

---


### 120. [Verifying Before Enhancing: Target Evidence Chain Verification for Infrared Small Target Detection](https://arxiv.org/abs/2611.25724)

**<font color=#1a73e8>作者：</font>** Jiayi Zuo, Songwei Pei, Shuhuai Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared small target detection is essential for early warning, surveillance, remote sensing, and space-based target perception. However, infrared small targets are typically tiny, weakly textured, and boundary-blurred, making them difficult to distinguish from complex backgrounds. Moreover, target-like background structures can produce salient responses across multiple scales, making response strength alone insufficient for reliable target discrimination. To address this challenge, we propose VBE-UNet, a Target Evidence Chain Verification Network that assesses candidate reliability beyond response magnitude through complementary evidence cues. Specifically, counterfactual background explanation models local target evidence, while joint evidence verification integrates cross-scale support and perturbation-based contribution verification to guide feature recomposition. The resulting reliability estimates guide selective feature refinement, promoting target-relevant responses while reducing unsupported background activations. Extensive experiments on IRSTD-1K, NUDT-SIRST, and NUAA-SIRST demonstrate that VBE-UNet achieves superior detection accuracy and lower false-alarm rates compared with state-of-the-art methods. Ablation studies and evidence reliability analysis further validate the effectiveness of the proposed verification framework.

---


### 121. [What's in the box? Revealing Object Layouts Inside Opaque Boxes via Contactless Vibration Excitation and Sensing](https://arxiv.org/abs/2611.25728)

**<font color=#1a73e8>作者：</font>** Ethan Turok, Matan Kichler, Shai Bagon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can we reveal what is inside an opaque box by observing its surface vibrations? Objects inside a box alter its mechanical response, providing cues about their hidden locations. We introduce a method that uses these cues to predict a box's 2D occupancy layout entirely remotely. A nearby speaker excites vibrations, which we measure on one visible wall using a grid of laser points and a camera measuring each point's speckle-pattern shifts. Our model, WhisperBox, learns to encode these vibrations into a latent representation and decode it into an occupancy map of the box's contents. The method requires no physical contact to excite or sense vibrations. We demonstrate layout recovery across various boxes and single- and multiple-object scenes, with generalization to unseen object instances, positions, orientations, and weights, as well as changes in laser placement and excitation source. Our analysis reveals that informative frequency bands need not coincide with the box's resonances and that the learned latent space captures object placement and supports arithmetic operations. These results demonstrate the potential of remote vibration sensing to infer spatial layouts hidden from view.

---


### 122. [Towards High-Fidelity Learned Video Compression](https://arxiv.org/abs/2611.25731)

**<font color=#1a73e8>作者：</font>** Bumyoon Kim, Yongseong Kim, Inhyuk Jeong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Professional video workflows operate at qualities that learned video codecs do not reach. We measure how much of a professional quality range a codec covers, from the lowest quality of the standard test conditions, VVC at QP 37, to the highest 4:2:2 grade of the production codec ProRes. To compare inter-frame coding alone, every codec receives original frames as references at the intra positions. On 10-bit YCbCr 4:2:2 test sequences, four recent learned codecs cover 24 to 38% of this range. Their encoders are feed-forward networks with a fixed latent capacity, the number of latent values per sample, of at most 0.25, and removing their quantization raises the quality by at most 1 dB. We propose a learned inter-frame codec whose encoder searches, as the encoders of conventional codecs do. It searches block motion, which a learned network refines, and it searches among learned block transforms whose latent capacity ranges up to 1, selecting the partition, the skip decisions, and the quantized coefficients by a rate-distortion cost. Our codec reaches the upper end of the range on all six sequences. With all residual blocks fixed to 16x16, whose latent capacity is 0.25, the same codec covers 55% of the range, with or without quantization.

---


### 123. [Embodied Human-Data Interaction](https://arxiv.org/abs/2611.25744)

**<font color=#1a73e8>作者：</font>** Niklas Elmqvist  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We propose the concept of human-data interaction (HDI) as the human manipulation, analysis, and sensemaking of large, unstructured, and complex datasets. We then proceed to suggest an embodied approach to HDI to build physical reasoning environments for these difficult and polymorphic tasks. We illustrate our approach with two examples: tangible lenses for visual exploration, and an educational computer game with tangible bricks.

---


### 124. [Disentangling Monitor Hardware Artifacts and Smoothing Lag for Shift-Robust Intraoperative EEG and Hemodynamic Risk Calibration](https://arxiv.org/abs/2611.25765)

**<font color=#1a73e8>作者：</font>** Zeyu Jia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Commercial intraoperative electroencephalography (EEG) and blood pressure monitors introduce cyclic impedance pulses, smoothing delays, direct-current (DC) drift, and cuff holds that confound risk forecasting and uncertainty calibration. We developed a causal signal-conditioning and shift-robust conformal calibration framework across 5,439 public anesthesia procedures. Streaming filters blank 10.13-min 64-Hz impedance checks, apply unclipped post-notch conditioning, separate 63-s suppression-ratio lag, and distinguish three-channel cuff inflations from dropouts across propofol-remifentanil total intravenous anesthesia (TIVA; N = 3,214), volatile anesthesia (N = 2,046), European endoscopy sedation (N = 171), and DC-coupled surgery (N = 8). De-impedanced cortical tree ensembles were compared against deep sequence models, paired with patient-cluster Subgroup-Covariate-Weighted Conformal Risk Control (CRC) and lag-buffered online Conformal Proportional-Integral-Derivative (PID) tracking. Pre-filter blanking removed 97.90% and 97.60% of false flatline conflicts while preserving 99.23% and 98.96% of deep suppression. On unseen TIVA surgeries (N = 525), cortical features achieved area under the precision-recall curve (AUPRC) 0.3135 (1.94% prevalence) and 0.1627 (0.82% lag-free prevalence), with no detectable difference from deep encoders (p >= 0.36) and no cortical gain for hypotension (0.3432 vs. 0.3437, p = 0.784). Zero-retraining volatile transfer (N = 1,048) showed no detectable difference from an end-tidal gas oracle on lag-free suppression (0.0820 vs. 0.0736, p = 0.472). Subgroup-Covariate-Weighted CRC bounded all 70 TIVA shift cells at <= 4.38% (alpha = 5.0%) in 66.32 ms per 30-s epoch. Causal artifact disentangling and shift-aware conformal calibration support reliable real-time intraoperative risk bounds within explicit physiological observability limits.

---


### 125. [Driver Gaze Target Identification via Gaze Estimation and Structured Driving Scene Understanding](https://arxiv.org/abs/2611.25771)

**<font color=#1a73e8>作者：</font>** Xinze Cao, Ke Wang, Deyong Guan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identifying a driver's gaze target provides object-level information for visual attention monitoring in intelligent vehicles. Gaze-zone classification and continuous attention localization provide limited information about the identity of the attended scene target. This paper proposes a modular framework that identifies object- or region-level gaze targets from synchronized in-cabin driver images and forward-view road images. The framework comprises four components: MFGaze, which combines a Vision Transformer pretrained with a masked autoencoder (MAE) and head-pose conditioning through feature-wise linear modulation (FiLM); panoptic scene understanding, which constructs a structured candidate set; polynomial ridge regression, which maps gaze features to 2D scene-image coordinates through individualized calibration; and entropy-driven target inference, which adaptively fuses boundary-distance geometry with class-level semantic priors. Experiments evaluate the framework using three public gaze datasets, a laboratory test using Cityscapes road scenes and self-collected gaze data, and the Look Both Ways (LBW) dataset. The complete framework achieves an overall Top-1 gaze target identification accuracy of 96.27% in the laboratory experiment. After sequence-specific calibration, it achieves Top-1 accuracies of 79.92% for task-relevant objects and 85.58% for the road class on LBW. MFGaze achieves the lowest mean angular errors among the compared methods, with 4.06$^\circ$, 4.23$^\circ$, and 10.52$^\circ$ on MPIIFaceGaze, ETH-XGaze, and Gaze360, respectively, and demonstrates strong cross-dataset generalization. Sensitivity analyses show stable performance under hyperparameter perturbations. These results support the framework as a source of object-level gaze information for driver monitoring.

---


### 126. [GeoPillars: A Large-Kernel Pillar Detector for Single-Sweep LiDAR Under Point Sparsity, and a Decomposition of Its Gain](https://arxiv.org/abs/2611.25787)

**<font color=#1a73e8>作者：</font>** Chaitanya Dumbre, Shubham Sarkar, Akash Mohapatra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> GeoPillars is a pillar-based 3D detector for single-sweep LiDAR under a hard budget of eight points per 0.4 m pillar, a budget that discards 46.6% of in-range points. It adds geometric pillar features, grouped vector attention within each pillar, a learned absolute positional prior on the bird's-eye-view (BEV) grid, a large-kernel backbone, auxiliary surface-normal supervision and a full-resolution detection head. Trained on 123k synthetic CARLA scans and evaluated on cars, it reaches 81.33 BEV AP@0.7, 13.76 points above CenterPoint at the same input budget and 1.91 points above CenterPoint at its native, denser budget. These are in-distribution figures, because the validation split is per-frame rather than scene-disjoint. A rung-by-rung decomposition shows that the new components explain little of the gain. Raising the detection-head resolution alone recovers 10.19 of the 13.76 points, the joint change of encoder, backbone, neck and positional prior adds 3.37, and the normal-supervision branch adds 0.20, which is within run-to-run variation. With heading reversals folded out, orientation error is similar for all seven models, although GeoPillars reverses headings about half as often as a resolution-matched baseline. It is also the slowest of the seven models. Evaluated zero-shot on 6,743 real nuScenes keyframes, no model transfers, and each retains 3.7% to 12.2% of its CARLA accuracy. A collection defect left LiDAR intensity constant, so every model learned from geometry alone. Code and checkpoints are publicly available.

---


### 127. [When Safety Rationales Hallucinate: Diagnosing and Grounding Multimodal Safety Guards](https://arxiv.org/abs/2611.25793)

**<font color=#1a73e8>作者：</font>** Yingshuo Wang, Weixiang Zhao, Guancheng Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal safety guards increasingly generate rationales alongside safety predictions, yet whether these rationales are reliable remains largely unexplored. We systematically study *rationale hallucination* from two perspectives: visual rationale hallucination, where rationales contain unsupported visual facts, and safety attribution hallucination, where grounded content is assigned an incorrect safety interpretation. Across rationale-generation methods, multiple vision-language backbones, and safety datasets, we find that rationale hallucination is widespread and does not consistently diminish with higher classification accuracy or increased model scale. Further analysis of the Think-with-Image paradigm shows that hallucination is concentrated in fine-grained attributes and relations, while visual tools are often invoked infrequently or without sufficient spatial focus. Based on these findings, we propose *Tool-Contrastive Grounding Reinforcement Learning* (TCG-RL), which rewards tool use only when it improves rationale grounding over a tool-free reference. TCG-RL substantially reduces rationale hallucination while maintaining competitive safety prediction performance. By revealing the gap between prediction correctness and rationale reliability, our study motivates a shift in multimodal safety guarding from outcome-only evaluation toward safety decisions that are both accurate and verifiably grounded.

---


### 128. [Fast and Accurate Body Estimation in Pixels, World Space and Scenes](https://arxiv.org/abs/2611.25801)

**<font color=#1a73e8>作者：</font>** Jinkun Cao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present FAB (Fast and Accurate Body estimation), a human body estimator that jointly improves inference efficiency and body-recovery fidelity. Rather than predicting only parametric mesh-model parameters, FAB directly predicts human skeleton joints and dense surface points. In images, it predicts dense 2D and 3D body points alongside a parametric Momentum Human Rig (MHR) head, then fits SMPL in one learned pass followed by two Gauss-Newton steps. Its ViT-L student, FAB-L, distilled from a fine-tuned SAM 3D Body, runs in real time for one person on an RTX 4070 Ti SUPER, from detection to a fitted body, at 4.6x the speed of SAM 3D Body's eager-PyTorch body-only path, while improving accuracy on most camera-space benchmarks. The same network predicts heel, toe, hand, and knee contacts, which connect the body to the scene. FAB also estimates world-space motion, fuses static-scene depth around the visible person, and aligns body and scene using predicted contacts. For human-to-humanoid real-to-sim transfer, an in-model G1 head and FAB-Retarget, a motion-level retargeter that reads dense points or the fitted mesh, map motion to a Unitree G1. FAB-Retarget produces references that follow the person more closely than specialized retargeters including SOMA, GMR, UMR, and OmniRetarget, and substantially more closely than Fast SAM 3D Body retargeted with our sequence IK. Project page: this https URL.

---


### 129. [World-delta: Continually Integrating Observations for Incremental 3D Scene Generation](https://arxiv.org/abs/2611.25802)

**<font color=#1a73e8>作者：</font>** Haonan Wang, Hanyu Zhou, Xiaobin Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D generation methods synthesize visually compelling scenes from fixed inputs, yet struggle to continually expand and revise a 3D world as new observations arrive. Iterative approaches often fuse real observations and generated content into a single representation, treating generated content as established structure rather than revisable predictions. Consequently, early generation errors can persist and accumulate despite new evidence. We propose World-delta, an incremental 3D scene generation framework combining uncertainty-aware persistent world modeling with delta-guided diffusion for continual scene expansion and correction. Our framework comprises three components: 1) Visual Evidence Encoding integrates geometric and semantic cues from incoming images into unified world tokens. 2) Observation-Calibrated World Modeling maintains a persistent latent world state that distinguishes observation-supported content from provisional completion hypotheses. New evidence drives selective world deltas to revise conflicting hypotheses while preserving well-supported content. 3) Incremental World Diffusion Generation uses delta-derived masks to restrict diffusion to regions requiring updates, freezing unchanged regions. Only affected 3D chunks are decoded and integrated into the existing scene. Together, these components enable continual world expansion and revision while reducing redundant generation and preserving scene consistency. Experiments demonstrate the effectiveness of World-delta in incremental 3D scene generation, observation-driven correction, scene consistency, and update efficiency over successive scene updates.

---


### 130. [Inject Where It Matters: Objective-Dependent Feature Control in Rectified-Flow Image Editing](https://arxiv.org/abs/2611.25811)

**<font color=#1a73e8>作者：</font>** Nina Goncharova, Alexandra Ivanova, Aibek Alanov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many prompt-driven FLUX editing methods rely on injecting source features into target-conditioned generation, creating an inherent trade-off between source preservation and the desired edit. We address this problem by controlling where source features are injected and which transformer blocks are used. First, we introduce adaptive masks that spatially gate feature injection using differences between source- and target-conditioned block outputs at matched inversion states. Second, we use REINFORCE to select Top-K injection blocks under different preservation-editability objectives. The selected blocks are fixed at inference and require no online search. On PIE-Bench with FLUX.1-dev, spatial masking controls the alignment-preservation trade-off. On 60 validation examples, a learned nine-block set gives lower whole-image LPIPS than the 18-block RF-Edit set within the same masked pipeline, with slightly lower alignment. Among 50 random nine-block sets, it has the lowest LPIPS but not the highest reward. Separate objective sweeps reveal different block preferences for preservation and alignment.

---


### 131. [What Places an Action Boundary? Structure-Aware Attribution for Temporal Action Localization](https://arxiv.org/abs/2611.25815)

**<font color=#1a73e8>作者：</font>** Ruoshan Lan, Zongru Shao, Chieh Tsai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporal action localization (TAL) detectors must identify actions and estimate their temporal boundaries, but localization remains a major source of detection errors. While understanding what determines boundary placement requires faithful attribution of temporal evidence, existing attribution methods have not sufficiently addressed the temporal structure of TAL or the need to tailor attribution to boundary localization. We introduce a structure-aware attribution framework that averages contributions across random evidence-restoration orders following the Shapley-Shubik principle. We make it tractable by using the detector's receptive field to limit which time steps are ordered individually, and by approximating each order with a soft gradient path. For boundary predictions, we further introduce cell-structured restoration orders and boundary-anchored references that selectively remove adjacent evidence. We also adapt faithfulness evaluation to assess the joint effects of contiguous temporal evidence and the direction of boundary displacement. Experiments on THUMOS14 and EPIC-KITCHENS-100 with TriDet and ActionFormer demonstrate improved attribution faithfulness over existing methods. Attribution analysis and controlled interventions further reveal that class-score changes do not reliably track boundary displacement, providing input-level evidence that classification relies on content less informative about boundary placement. Code and evaluation artifacts will be publicly released.

---


### 132. [SCCV-6D: Sparse Canonical Coordinate Voting for Holistic Multi-View RGB-D 6D Pose Estimation in Robotic Bin Picking](https://arxiv.org/abs/2611.25819)

**<font color=#1a73e8>作者：</font>** Nico Leuze, Samed Dogan, Maximilian Hoh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial bin picking requires pose estimates that are accurate under clutter, partial occlusion, and the reflective, texture-less nature of manufactured parts. Most recent approaches to 6D pose estimation follow multi-stage pipelines. These achieve high accuracy, but incur memory and runtime footprints that do not cope with the operational constraints of many real-world industrial deployments. Holistic pipelines estimate poses in a single pass, with cost controlled through indiscriminate subsampling or lowered resolution. Continuing this line, we present SCCV-6D, a fully sparse multi-view RGB-D estimator. We reconstruct the 3D space at millimeter precision, prune background via a staged heatmap mechanism, and predict class, translation offset and rotation at highest resolution for an arbitrary number of objects simultaneously. Rotation is formulated as canonical coordinate voting. Points vote for their canonical object coordinates with an associated confidence, enabling closed-form pose recovery with a symmetry-aware weighted Procrustes solve. Along an in-cluster point recovery induced by offset votes, this removes time-consuming post-processing stages. We reuse the task-supervised attention priors from the heatmap formulation for a novel attention-gated distillation objective that reweights teacher-student feature alignment. On the IPD test split we report competitive 0.826 AP at 1.13 s per scene, significantly faster than the leading entries. On MV-YCB our approach reaches 96.1 ADD-S, and remains competitive even on the densely packed bins of ROBI.

---


### 133. [Signed but Unbound: The Authority Gap Between Agent Commerce Mandates and Crypto Wallet Signatures](https://arxiv.org/abs/2611.25821)

**<font color=#1a73e8>作者：</font>** Shengwei You, Aditya Joshi, Andrey Kuehlkamp 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When an artificial intelligence agent pays with a stablecoin, the commerce protocol can specify the merchant, order, amount, and facilitator. The token contract enforces the fields the wallet signs. We call the difference the authority gap, define nine constraint classes, and derive them for 12 authorization configurations, including Coinbase's deployed Commerce Payments Protocol. All 31,800 trials on local copies of deployed contract code match the derivation. A controlled comparison shows that committing the terms in the signed nonce binds the order. When the facilitator submits a payment to a merchant account without code, binding the facilitator requires a separate recipient contract. Of 26,653 sampled USD Coin authorizations redeemed on Base, 98.7% followed a path that any holder of the signature could redeem. We prove sufficient conditions for a recipient contract to enforce the signed mandate under a trusted signer and show which recipient a wallet displays. MandateLock, a minimal implementation for immediate payments, rejects all 10,800 modified mandates on deployed token code and accepts signatures from two independent signers. It uses 25% more gas than a transfer that only the recipient can submit.

---


### 134. [Limits of local curvature for constructing search subspaces in segmentation models](https://arxiv.org/abs/2611.25822)

**<font color=#1a73e8>作者：</font>** Maxim Bolshim, Alexander Kugaevskikh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We examine how well subspaces constructed from local curvature represent the change in the gradient update field after a finite step in semantic segmentation models. The local response is the action of the curvature operator on the actual input displacement. In a study of 50 images and two models, we measure the ratio of the loss increase attained in a fixed subspace to that attained in the full space. This ratio decreases as the search radius increases. On ten images from the same sample, we compare the one-dimensional subspace spanned by the initial gradient with two rank-16 subspaces for both models. The two equal-rank subspaces are assessed at the same initial states, using the same actual steps and measured vectors. Adding generalised Gauss-Newton directions to the initial gradient reduces the mean relative error in representing the field change from 0.922 to 0.874 for the first model and from 0.819 to 0.763 for the second. At the same rank, including the response direction for the initial gradient nearly eliminates the error in representing the local response. The mean error in representing the field change does not decrease. A decomposition with fixed pixel weights shows that the finite-step remainder is comparable in norm to the field change and makes the largest diagonal contribution to the squared projection error of the field after the step. Evaluation of a search subspace should measure how accurately it represents the field change and the local response.

---


### 135. [Fusing Multimodal CNN Features with Structurally-Masked Transformers for Hierarchical Sub-Pixel Tree Species Mapping](https://arxiv.org/abs/2611.25824)

**<font color=#1a73e8>作者：</font>** Mattia Ferrari, Lorenzo Bruzzone  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precise forest species mapping using spaceborne hyperspectral data is challenging due to high spectral similarity and the inherent sub-pixel heterogeneity of natural forest stands. While traditional deep learning models exploit spatial context through convolutional architectures, these approaches can introduce noise in fragmented or mixed-species forests. In this paper, we propose a hierarchy-aware, multimodal deep learning framework to resolve sub-pixel forest composition by integrating PRISMA (PRecursore IperSpettrale della Missione Applicativa) hyperspectral imagery, high-resolution panchromatic data, and digital elevation models. The architecture features a multi-branch encoder combining an EfficientNetV2-based one-dimensional convolutional neural network (CNN) for spectral signatures and twin two-dimensional CNNs for spatial and topographic features, coupled with a novel structurally-masked Transformer. By using a binary transition tensor to condition the Transformer slot embeddings and constrain inference, the model enforces taxonomic consistency between broad forest categories and fine-grained species distributions. The framework is validated across three diverse Italian biogeographical regions (the Alps and the Central and Southern Apennines) using field-surveyed plots. The proposed method consistently outperforms state-of-the-art multi-label and ranking-based paradigms, particularly in identifying subordinate species and their relative dominance. The bidirectional learning mechanism allows sub-pixel compositional features to refine macroscopic forest type predictions, while the integration of topographic priors effectively resolves spectral ambiguities in complex terrains. This knowledge-driven method supports regional-scale biodiversity monitoring and forest characterization within the evaluated PRISMA scenarios.

---


### 136. [A Sparse Low-Rank Biclique Decomposition for Graphs](https://arxiv.org/abs/2611.25826)

**<font color=#1a73e8>作者：</font>** Antoine Vialle, Sergei Gerasimov, Aref Einizade 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank plus sparse decompositions, such as robust PCA, typically model the low-rank component as dense and the sparse component as corruption. This viewpoint is poorly suited to graph adjacency matrices, where sparsity is structural and dense low-rank factors destroy the combinatorial and computational properties of the graph. We propose signed biclique decomposition (SBD), a sparse low-rank decomposition for integer-weighted graphs that represents the structured component as a sum of sparse signed binary rank-one factors, together with a sparse signed residual. The resulting representation remains discrete, interpretable, sparse, and compatible with standard linear algebra. We formulate fixed-rank and greedy SBD objectives and derive a gain-based greedy algorithm with theoretical guarantees. Empirically, SBD recovers block structure in noisy graphs, while its factorized representation enables efficient sparse matrix-matrix multiplication (SpMM). On real graphs with strong shared-neighborhood structure, SBD achieves compression factors above $10$ and SpMM speedups up to $6\times$ over cuSPARSE, suggesting a practical alternative to dense low-rank decompositions for graphs. Code is available at this https URL.

---


### 137. [Beyond Alignment: Whitening Geometry, Profile Synthesis, and Heterogeneous Ensembles for Cross-Environment WiFi Action Recognition](https://arxiv.org/abs/2611.25831)

**<font color=#1a73e8>作者：</font>** Lei Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-environment deployment is the central obstacle to practical WiFi sensing: a pipeline reaching 0.89+ top-1 in its training environments collapses to 0.408 under Leave-One-Domain-Out (LODO) evaluation with only K-shot labels. A ceiling analysis shows the collapse is not an alignment problem: the action signal is strong across seen environments (about 0.89 K10), environment identity is decodable from the encoder (0.965), and the failure concentrates in the encoder's extrapolation to the novel environment. A pre-registered falsification chain confirms that "align the domains" methods--training-time alignment, readout-level prototype alignment, adversarial confusion, and covariance/subspace alignment (CORAL -3.8pp, subspace -8.3pp)--degrade performance, and that source-domain statistics anti-correlate with cross-environment contribution. The effective levers lie elsewhere; we combine them into Dec-H: (i) closed-form source within-class whitening, provably re-geometrizing the readout's L2 regularization (+8.6pp, zero cost); (ii) profile-mixing augmentation (+1.0pp); (iii) few-shot adaptation with alternating whitening refit (+1.5pp; fixed preconditioners are 20/20 negative); (iv) heterogeneous decision ensembles (+1.7pp); homogeneous scaling and source-weighted stacking are saturated or harmful. Dec-H reaches 0.560 K10 (0.812 K40), +15.2pp over the baseline, consistent across all four environments and seeds; all thirteen configurations were pre-registered with frozen criteria.

---


### 138. [ContextRenderer: Dynamic-Context Video Generation for Interactive Game Worlds](https://arxiv.org/abs/2611.25838)

**<font color=#1a73e8>作者：</font>** Runze Wang, Fei Zha, Bing He 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive game world models separate executable world evolution from visual generation, using video models to render engine-provided scene representations into detailed observations. During sustained gameplay, however, existing generative renderers struggle to follow changing conditions while preserving visual continuity across diverse proxies and target styles. We therefore introduce ContextRenderer, an autoregressive video diffusion framework designed for both dynamic conditioning and cross-proxy generalization. It couples Dynamic-Context Learning (DCL) for chunk-level interaction supervision with Recurrent History Compression (RHC) to follow condition updates while preserving visual continuity within a bounded token budget. Across proxy representations, Cross-Representation Flow Alignment (CRFA) connects proxy reconstruction with appearance and interaction variation through a shared high-fidelity reconstruction. WorldPrism, our interaction-centric dataset constructed from agent-built worlds, AAA gameplay, and open-source videos, supplies the corresponding renderings and chunk-level annotations for these learning tasks. Experiments on GWM-Bench and Solar-Bench show improved reconstruction and visual quality, while qualitative results demonstrate minute-long interactive rendering under changing prompts and subject references. Project page: this https URL

---


### 139. [Whose Risks Count? What 1,901 AI Incidents Reveal About Corporate Disclosures](https://arxiv.org/abs/2611.25841)

**<font color=#1a73e8>作者：</font>** Simeon Allmendinger, Edyta Paulina Bogucka, Niklas Kühl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems can harm people, yet the AI actors that provide or deploy them are rarely obliged to disclose these risks. US securities regulation is an exception. Companies registered with the Securities and Exchange Commission (SEC) must disclose their material risks, including those of their AI systems, in filings that carry liability for misstatement. Materiality, however, is defined by what a reasonable investor would consider important, so harms to third parties enter disclosure only insofar as they become financial risks for the company. We test whether AI harms do so by matching 9,001 AI incidents to 18,229 SEC filings of 328 AI actors by risk type. Of the 1,901 incidents with filings before and after them, half belong to a risk type that the AI actor never disclosed, and this share varies with the kind of harm. Filings disclose the risk types of 67\% of system failures but only 2\% of social system harms, and AI actors themselves report fewer than 2\% of incidents. Securities disclosure thus records the risks that AI actors face rather than the harms that people subject to AI bear. Public authorities that hold AI actors accountable for such harms could make them financially material. We release DISC, the Disclosure--Incident Securities Corpus, to support this work.

---


### 140. [TrajCal: Trajectory-Calibrated Time Schedules for Few-Step Flow Sampling](https://arxiv.org/abs/2611.25847)

**<font color=#1a73e8>作者：</font>** Junchi Zhang, Zihan Gu, Jiangcan Jia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow matching enables high-quality image and video generation, but its iterative sampling process requires repeated evaluations of large neural networks. Existing few-step methods can distort the output and reduce its agreement with a many-step reference. We propose TrajCal, a training-free calibration framework for few-step sampling. Based on scatter search, a well-established metaheuristic for difficult optimization problems, TrajCal starts with diverse seed schedules, deforms and combines these candidates, and selects one fixed schedule by final output fidelity for reuse on new inputs. For both image and video generation, TrajCal achieves higher reference fidelity than all compared baselines at low evaluation budgets while maintaining competitive visual quality. The search is effective even with randomly generated seeds, while trajectory-based seeds further improve fidelity. For cross-style generalization, photography-calibrated schedules also improve fidelity on unseen image styles.

---


### 141. [Interpretable Prototype-Conditioned Adaptation for Weather Forecasting](https://arxiv.org/abs/2611.25848)

**<font color=#1a73e8>作者：</font>** Zhixuan Li, Hao Jiang, Chen Hui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven weather forecasting requires distinguishing local states and their temporal evolution. However, learned patterns remain implicit in neural forecasters, making their influence difficult to interpret. Failing to distinguish local evolution can lead to similar forecasts for locations that develop differently, increasing prediction error. This motivates explicit references for distinguishing and interpreting local patterns. Prototypes provide explicit pattern references, but sample- or task-level conditioning leaves open how to adapt to distinct locations and variable groups. To deal with this problem, we design ProtoCast, which uses group-specific prototype banks to adapt local features while accounting for cross-variable dependencies. Specifically, (1) we combine each group's historical features and temporal change with forecast context from cross-variable attention for evolution-aware prototype matching. (2) Sparse mixtures of prototype-specific low-rank operators tailor corrections to each group and location. A gated attention block then exchanges the corrected features across groups before prediction. Each group's correction decomposes into explicit prototype contributions before this fusion. (3) We jointly train the forecasting network and operators from scratch and refit each group's prototypes before every training epoch. Slot tracking preserves prototype-operator associations, making each prototype's contribution to local corrections more interpretable. Experiments on GlobalForecast and TyphoonTracking show improved forecasting accuracy, while prototype deletion links local feature contributions to changes in prediction error. This work advances the development of more accurate and interpretable data-driven weather forecasting models. Project page: this https URL

---


### 142. [Interlacing Committees with Edge-Expansion](https://arxiv.org/abs/2611.25852)

**<font color=#1a73e8>作者：</font>** Gili Bielous, Reshef Meir  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Approval-based committee selection has recently been studied through the lens of \emph{interlacing}, a framework for studying polarization in approval elections, in which committees induce a similarity graph over voters. The quality of committees is then evaluated through the connectivity of the resulting graph. We revisit the connectivity measures used in this framework and propose \emph{edge-expansion}, a classical graph-theoretic measure with well-established connections to polarization in networks, as the optimization objective. We provide a theoretical foundation for this proposal by relating interlacing to classical models of information diffusion and by comparing edge-expansion with previously proposed connectivity objectives, identifying qualitative differences in the structural properties they capture. Finally, we study the computational complexity of optimizing edge-expansion, showing that hardness persists even for voter-interval preferences, while the problem is polynomial-time solvable for every fixed committee size, with an improved dependence on the committee size for voter-candidate-interval preferences.

---


### 143. [X Hedging: towards an eXplainable artificial intelligence option Hedging framework](https://arxiv.org/abs/2611.25870)

**<font color=#1a73e8>作者：</font>** Bjørn André Aaslund, Johannes Berge, Ayoub Haida 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose X Hedging, an alternative to the Deep Hedging framework that addresses computational and explainability limitations of neural-network-based hedging strategies. Deep Hedging leverages neural networks to learn flexible hedging policies but relies on opaque models and typically requires large training datasets, which can complicate interpretation and limit its effectiveness in data-constrained settings. X Hedging takes a step toward addressing these limitations by replacing neural networks with tree ensemble methods, specifically LightGBM, to estimate hedging strategies. This design provides a computationally efficient alternative while preserving strong hedging performance and moving toward more user-centered explainability. To integrate LightGBM into a reinforcement-learning-style hedging framework, we introduce an optimization approach that sequentially trains tree-ensemble models while introducing stochasticity through random training orders. In controlled experiments, X Hedging achieves performance comparable to Deep Hedging while offering greater user-centered explainability, improved computational efficiency, and substantially higher robustness when training data are limited. The numerical results demonstrate that tree-ensemble methods provide an effective computational alternative to neural networks for data-driven dynamic hedging.

---


### 144. [WHU-Road3D: A dataset and benchmark towards fine-grained road surface mapping](https://arxiv.org/abs/2611.25873)

**<font color=#1a73e8>作者：</font>** Xiaoxin Mi, Zhen Cao, Chong Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurately extracting and mapping road surface elements is crucial for applications such as high-definition maps, road asset management, and intelligent transportation systems. This study first provides a comprehensive review of the benchmark datasets for extracting and mapping road elements, encompassing overhead-to-perspective data, large-to-local scales, and coarse-to-fine details. Subsequently, we thoroughly review the relevant approaches for extracting road surface elements. However, we argue that existing datasets still require enhancements in semantic richness, data modality diversity, and scenario complexity. To bridge these gaps, this paper presents WHU-Road3D, a large-scale multimodal dataset for fine-grained road surface mapping to address these shortcomings. WHU-Road3D provides approximately 100 km of diverse Chinese highways and urban streets. It features a rich combination of MLS point clouds, associated panoramic images, vehicle trajectories, detailed vectorized annotations, and pointwise instance annotations for road surface elements. The dataset carefully annotates 15 distinct categories of road elements, including common markings like road boundaries, zebra crossings, lane dividers, stop lines, as well as 10 types of direction symbols. To our knowledge, WHU-Road3D stands as the first multimodal dataset for mapping such a comprehensive range of road surface elements, designed to facilitate cutting-edge research in instance segmentation, full-element extraction and mapping on road surfaces. Beyond these immediate applications, WHU-Road3D also provides a valuable source for hierarchical road topology reasoning, map updating, and street scene generation. The dataset, along with the code for our benchmark methods, will be made publicly available at \href{this https URL}{this https URL}.

---


### 145. [Parameter-Efficient Adaptation of Self-supervised Vision Backbones Survives Distribution Shift in Radar Micro-Doppler HAR](https://arxiv.org/abs/2611.25874)

**<font color=#1a73e8>作者：</font>** Keryan Chelouche, Petr Dobias, Nistor Grozavu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Micro-Doppler radar enables contactless, privacy-preserving human activity recognition (HAR), but deployment robustness remains underexplored. We compared full fine-tuning, frozen probing, and parameter-efficient fine-tuning (PEFT) using subject-disjoint in-distribution cross-validation and few-shot cross-age, cross-orientation, and cross-dataset transfer. Full fine-tuning suffered negative cross-dataset transfer, while frozen features under-adapted on cross-orientation. Only PEFT avoided both failures. We paired DINOv3 with all-layer principal-singular-direction adaptation (PiSSA), to our knowledge the first application of a self-supervised image foundation backbone to radar micro-Doppler HAR. DINOv3-PiSSA ranked first among PEFT methods in every evaluated setting. Under our protocol, its Small variant matched the in-distribution accuracy of the prior Base-size PEFT state of the art using 4.5x fewer total parameters, with only 3% trainable. It surpassed a size-matched variant of that baseline in every evaluated setting, with transfer gains increasing with shift severity: 2.1, 6.6, and 8.9 percentage points, respectively. Ablations attributed improvements to both pretraining and adapter recipe, with the pretraining contributing most under compound shift. Code and protocol are available at this https URL.

---


### 146. [Coherent belief and opinion propagation produces more echo chambers: corrected version](https://arxiv.org/abs/2611.25879)

**<font color=#1a73e8>作者：</font>** Hiro Kataoka, J{é}r{ô}me Euzenat, Koji Hasebe  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The occurrence of echo chambers is a well-known phenomenon in social networks. Echo chambers are groups of agents satisfying three properties: homogeneity, i.e., sharing the same opinion, segregation, i.e., listening primarily to agents of the same group, and reinforcement, i.e., increasing opinion similarity over time. Opinion dynamics models have been used to explain how echo chambers occur through agents updating their opinions. However, social network users also exchange beliefs supporting their opinions. Here, we aim at identifying the effect of propagating beliefs together with opinions on the formation of echo chambers. For that purpose, we complement an existing opinion dynamics model with classical belief merge operations. Beliefs and opinions are also maintained coherent guided by values that agents share. We introduce measures, applying to either beliefs and opinions, to identify echo chambers based on the three properties. This model is used to simulate opinion and belief propagation with varying initial conditions and agent tolerance for different opinions/beliefs. Results confirm the occurrence of echo chambers observed in previous opinion dynamics studies in a different setting and with a stricter measure. They also demonstrate the occurrence of echo chambers with belief propagation. Finally, they show that connecting opinions to beliefs and maintaining their coherence increases the number of belief echo chambers, but that they involve a reduced number of agents.

---


### 147. [Trustworthy Geospatial AI Workflows: Reproducible Maritime Analytics and Forecasting on Open-Source AIS Data](https://arxiv.org/abs/2611.25884)

**<font color=#1a73e8>作者：</font>** Divya Acharya, Thomas M. Roehr, Arnaud Gotlieb  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Publicly available geospatial data provide increasing opportuni- ties for data-driven maritime analytics and predictive modelling. However, their availability does not necessarily imply that the underlying observations are equally suitable for downstream AI applications. Properties of the data source and observation pro- cess, including provenance, reporting regularity, spatial coverage, observation density, and missingness, can affect how geospatial data are interpreted, processed, and ultimately used by predictive models. At the same time, trustworthy geospatial AI requires ana- lytical workflows in which these processing decisions can be made explicit and reproduced. This paper presents a reproducible mar- itime geospatial AI workflow built around damast, an open-source data-processing and machine-learning library developed at Simula Research Laboratory. Using AIS observations from multiple public data providers as a case study, we demonstrate metadata-aware validation, reusable processing pipelines, maritime trajectory con- struction, and reproducible machine-learning experimentation. The predictive stage is model-agnostic and is instantiated in this study using a Transformer-based vessel-trajectory forecasting model. Building on these implemented capabilities, we further outline an envisioned extension toward trustworthiness-aware geospatial AI. The extension introduces explicit characterization of source- and data-level properties and their relationship with downstream model performance. This distinguishes capabilities demonstrated in the current workflow from trustworthiness-oriented components identified for future development. Overall, the study demonstrates how reproducible open-source infrastructure can provide a practi- cal foundation for developing more transparent and trustworthy geospatial AI workflows.

---


### 148. [Explainable AI for Solar PV Power Forecasting: From Model Selection to Trustworthy, Reproducible Deployment](https://arxiv.org/abs/2611.25894)

**<font color=#1a73e8>作者：</font>** Nuzhat Khan, Muhammad Paend Bakht, Ab Al-Hadi Ab Rahman 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) is now a standard tool for forecasting the output of solar photovoltaic (PV) plants, yet published accuracy figures are often hard to compare and harder to trust. Many studies validate with random splits, report no reference forecast, and present feature attributions without saying what they can and cannot show. This paper reviews the main families of ML methods for PV power forecasting and resource assessment, from tree ensembles to deep and foundation models, and sets out a reproducible workflow that combines automated model search with explainable AI. The workflow is then tested on an openly available dataset: a 16.32 kWp plant in Porto, Portugal, forecast one day ahead from a 4 km numerical weather prediction grid. Over a full test year, the best models reach a normalised root mean square error (nRMSE) of 11.6% of installed capacity, about half the error of smart persistence. The choice of input features changed accuracy far more than the choice among strong algorithms, and shuffled cross-validation was mildly optimistic. After conformal calibration, the nominal 80% prediction intervals covered 81.7% of observations, against 64.5% before. SHAP rankings stayed stable when the model was retrained on different periods but shifted when correlated inputs were removed, so attributions should be read as properties of a model rather than of the plant. The paper closes with practical lessons and open problems, including deployment on edge hardware and the effect of a changing climate.

---


### 149. [Does It Depend on the Split? Frozen Satellite Features vs. Fine-Tuned CNNs for Tree Species Mapping](https://arxiv.org/abs/2611.25902)

**<font color=#1a73e8>作者：</font>** Dharani Deivasihamani, Nandakishore Puttashamachar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised foundation models are often said to need fewer labels than supervised training. We test this on a forestry task: classifying 20 tree species classes in 0.2 m aerial images from the TreeSatAI dataset. We compare a frozen DINOv3 model pretrained on 493 million satellite images, with only a linear classifier trained on top, against an ImageNet ResNet-50 that is fine-tuned end to end. On the official split, fine-tuning wins clearly (macro F1 0.764 vs. 0.685). However, 28.8% of the official test patches overlap a training or validation patch, and copying the label of the nearest such patch is correct for 83.6% of them. We therefore build a spatial split that holds out whole 2 km squares with a 200 m buffer. On this split the comparison becomes inconclusive (0.648 vs. 0.640, paired 95% CI of the difference [-0.054, 0.016]), and the learning curves of the two models overlap at every label budget from 343 to 33,126 training patches. On the five rarest classes, the frozen model achieves a higher mean F1 (0.566 vs. 0.445), although the confidence interval for this difference includes zero ([-0.05, 0.23]). Diagnostics show that the frozen features mainly miss differences between closely related species, such as the two native oaks. Choosing the input size and layer on validation data (224 px, block 16) raises the frozen model to 0.662 on the spatial split. A comparison that looks decisive on the official split is thus inconclusive under geographically separated evaluation. We release the spatial split and our code.

---


### 150. [The Linguistic Structure of Dependency-Conditioned Embeddings](https://arxiv.org/abs/2611.25909)

**<font color=#1a73e8>作者：</font>** Bach Phan-Tat, Tung Kieu, Kris Heylen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dependency-based distributional models capture syntactically informed lexical similarities, but the geometric organisation of dependency-conditioned lexical representations remains underexplored. We investigate the global and local geometry of lemma-dependency relation embeddings using four representations trained on WikiText-103: two count-based PPMI configurations and two Skip-Gram with Negative Sampling (SGNS) configurations. At the global level, we analyse dependency-relation centroids, control for lexical identity through within-lemma centring, and examine their alignment with part-of-speech (POS) distributions. At the local level, we evaluate cross-relation geometric consistency, cross-method agreement, lexical similarity, and polysemous usages. Results show that global geometry is structured strongly by context POS across all representations. Locally, broader lexical similarity structures are partially preserved across dependency relations, while immediate neighbourhoods vary substantially, highlighting different usages. PPMI-based representations exhibit greater cross-relation consistency than SGNS-based representations, with cross-method agreement varying by relation. These findings reveal systematic linguistic organisation at multiple geometric scales and its sensitivity to representation choices.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-265](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
