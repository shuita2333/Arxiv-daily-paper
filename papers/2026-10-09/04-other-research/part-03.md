# 📦 其他研究 | 2026年10月09日

> 本类共 **324** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-324](./part-07.md)

---

### 101. [TileSkipper: Region-Adaptive Tile Pruning for 3D Gaussian Splatting](https://arxiv.org/abs/2610.09343)

**<font color=#1a73e8>作者：</font>** Jingxing Li, Yongjae Lee, Deliang Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tiled 3D Gaussian Splatting rasterizers often use one scene-wide contribution cutoff for tile enumeration, although content differs in its sensitivity to support truncation. TileSkipper selects a static per-Gaussian cutoff policy for a frozen checkpoint. Calibration renders measure candidate pair savings and an isolated-removal distortion proxy that accounts for front transmittance and background color. The method allocates cutoffs across 64 Gaussian groups and accepts policies only after complete renders on disjoint selection views. The exported policy uses one byte per Gaussian, with no parameter updates, additional kernel, or per-frame policy inference. Across 13 scenes from Mip-NeRF 360, Tanks & Temples, and Deep Blending, a fixed-policy AccuTile sweep gives dataset-macro speedups of $1.088\times$ at standard resolution and $1.238\times$ at 3840 pixels wide, with $-0.007/-0.023$ dB mean PSNR change. Six integrations with existing opacity-aware bounds yield $1.009\times$--$1.121\times$ compiler-only speedups. For four ports from $3\sigma$ rasterizers, we separately attribute the prior exact-bound transition and our incremental gain. Matched-quality ablations show modest gains over scene-global calibration and parity with per-Gaussian control; the standalone comparison with AdaGScale is regime-dependent.

---


### 102. [Many Brains, One Geometry: A Shared Visual-Semantic Space for Cross-Dataset fMRI Decoding](https://arxiv.org/abs/2610.09352)

**<font color=#1a73e8>作者：</font>** Moein Khajehnejad, Michelangelo Tronti, Forough Habibollahi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visual decoding from fMRI is typically siloed by participant and experiment, obscuring whether heterogeneous neural measurements can be organized within a common computational geometry. Here we introduce BRAID-fMRI (Brain Representation Alignment across Individuals and Datasets), a shared CLIP-supervised decoding framework. BRAID-fMRI uses a single ROI-wise Transformer with optional participant conditioning across eight visual-fMRI datasets comprising 93 dataset-specific participant entries, 430,007 single-trial responses and 162,839 unique stimuli. Regional brain activity is aligned with 512-dimensional CLIP ViT-B/32 representations using a multi-positive contrastive objective that treats repeated stimuli across participants and datasets as positives. BRAID-fMRI supports retrieval across seven evaluation datasets. On eight matched participant entries, it achieves 35.0 +/- 11.1% Top-10 accuracy, exceeding the observed mean accuracy of the two evaluated baselines - the MindEye-style pooled-CLIP decoder (27.1 +/- 5.1%) and ridge regression (21.1 +/- 9.1%) - and attaining the highest observed accuracy for seven of eight entries. In separately trained participant-agnostic models, expanding the source pool increased target-dataset holdout accuracy by up to 92.1% relative to the initial source-training condition. The learned space preserves graded semantic structure, while ablations and saliency highlight ventral and early visual cortex and category-specific motion and attentional systems. These results support scalable cross-dataset decoding into a common CLIP-aligned space, with model sensitivity concentrated in ventral and early visual inputs.

---


### 103. [Global Exponential Convergence of Two-Layer Linear Network Training](https://arxiv.org/abs/2610.09356)

**<font color=#1a73e8>作者：</font>** Stephen Y Zhang, Gabriel Peyré  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove global exponential (linear) convergence with an explicit rate in the rich scaling for wide two-layer linear networks trained with smooth Polyak-Lojasiewicz predictor losses. Gradient flow in the factors closes exactly in terms of a finite-dimensional Bures flow of the neuron law covariance, in which the predictor dynamics are preconditioned by hidden covariance blocks. Mean-field conservation laws provide uniform spectral lower bounds on the hidden preconditioning blocks when the initial covariance satisfies a spectral support gap condition. This condition encompasses positive definiteness while still allowing for singular initializations. For an initial covariance $\Sigma_0 = \sigma^2 \mathrm{Id}$, the loss converges to the global minimum with linear rate at least $4\sigma^2\kappa$, where $\kappa$ is the PL constant. We establish stability of this rate under finite-width sampling, as well as global convergence of factor gradient descent for an explicit stepsize interval depending on smoothness, the initial loss, and conserved spectral margins. Our argument extends layerwise to deep linear ResNets, subject to a residual-path bound. In the case of heavy-ball momentum, training dynamics close instead over positions and velocities in terms of a lifted phase covariance. Linear convergence holds under an explicit condition on the energy and damping, specifying a window of admissible dampings. For two-scale white initializations, this interval is nonempty for sufficiently large position scales, with a fixed initial loss gap and velocity covariance. Numerical experiments illustrate the covariance geometry and compare the predicted and observed rates.

---


### 104. [Closing the Loop on Contrail Avoidance with Satellite Verification](https://arxiv.org/abs/2610.09363)

**<font color=#1a73e8>作者：</font>** Spandan Ghose Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrails are the thin ice clouds that aircraft leave behind. They cause a large share of aviation's warming, and rerouting the few flights that produce them could avoid much of it. However, an avoided contrail only counts if a satellite can confirm that it never formed, and this check is hard: contrails are one to two pixels wide, cover only 0.18% of pixels, and look very similar to natural cirrus. We build a small diffusion model (8.4M parameters, trained on one GPU) that detects them, and we run a controlled study to find out which components matter. The model reaches 0.476 PR-AUC, compared with 0.414 for a DeepLabV3+ baseline and 0.119 for an adapted MedSegDiff. Doubling the input resolution of the CNN brings it to parity (0.499, p=0.07). Three lessons apply beyond contrails. First, check the input resolution before designing a new architecture. Second, simple flips and rotations more than double accuracy and matter more than any architectural choice we measured. Third, pretraining the model on contrail shapes is harmful: the model learns that thin strokes appear everywhere and paints them onto empty scenes. Precision collapses to 1% while recall-based metrics still rate the degraded model as excellent, and no threshold or guidance heuristic repairs this failure.

---


### 105. [Unified Multi-plane Autoregressive Diffusion for 3D Multi-contrast MRI Synthesis](https://arxiv.org/abs/2610.09376)

**<font color=#1a73e8>作者：</font>** Yejee Shin, Geonhui Son, Jinglu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Acquiring a complete set of magnetic resonance imaging (MRI) contrasts is time-intensive and uncomfortable for patients, despite the diagnostic value of multi-contrast imaging. This motivates synthesizing missing contrasts from those already acquired, which is an inherently 3D problem requiring anatomical coherence across axial, sagittal, and coronal planes. However, fully 3D generative models are often impracti- cal under computational resources that scale cubically with volume size. We propose a unified Multi-Plane Autoregressive Diffusion (MPAD), a latent diffusion framework that achieves full-volume 3D synthesis using efficient plane-wise 2D operations while preserving volumetric coherence. A 3D autoencoder first compresses MRI scans into an isotropic 3D la- tent representation. A 2D diffusion model is then trained to reconstruct masked latent slices of the target contrast, conditioned on both source- contrast slices and unmasked target-contrast slices. During inference, we introduce plane-wise autoregressive synthesis with inter-plane priors. Slices are generated autoregressively in random order within one plane orientation to maintain intra-plane continuity, then propagated as con- ditioning priors to orthogonal plane orientations to enforce inter-plane consistency. Compared to 3D latent diffusion baselines, MPAD reduces training and inference FLOPs by 7x and 3x, respectively, while also lowering inference time and peak memory consumption. Experiments on multiple datasets demonstrate that MPAD achieves superior perfor- mance, generating high-fidelity 3D volumes and supporting one-to-many translation within a single unified model.

---


### 106. [From Plausible Hierarchies to Useful Taxonomies: Evaluating Agentic Harnesses on Customer Feedback](https://arxiv.org/abs/2610.09377)

**<font color=#1a73e8>作者：</font>** Prabhath Chellingi, Raviraja G, Viraj Bagal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Taxonomies are the symbolic representations through which AI systems organize evidence, aggregate patterns, and answer questions over large document collections. Over customer feedback, the category tree decides how every record is counted and routed, which problems get seen, and which team owns them. Agentic harnesses now make it easy to generate a plausible-looking hierarchy, and such trees are checked today with generic, individually scoped checks: each name fits its description, sits under the right parent, and stays distinct from its siblings. We ask a more operational question: when is a generated hierarchy actually useful as a production taxonomy? We build six taxonomies over two proprietary feedback corpora (1,940 and 5,000 records): for each corpus, a production reference and two repeated runs of the same harness under identical inputs. All six pass every generic naming and structure check, and a deeper product-coverage check even prefers the generated trees. Yet in every generated tree at least 97.7% of leaf names merely restate an ancestor's name (13.9% and 2.9% in the references), and in one, three of every four records fall under multiple top-level categories. We introduce two families of whole-tree metrics: structural discriminators test whether a tree's shape was learned from the data or imposed by its generator; team partitionability tests whether branches split feedback into groups teams can own. Trees the generic checks rate as equally correct differ by 27 percentage points in cross-branch leakage, and only one of the two beats a random split. Surface plausibility is an insufficient measure of taxonomy quality: evaluation must measure the whole tree as well as each node.

---


### 107. [PPCAR-Net: Projection-Refined Parametric 3D Coronary Artery Reconstruction from Sparse X-ray Angiographic Views](https://arxiv.org/abs/2610.09383)

**<font color=#1a73e8>作者：</font>** Yu Ren, Hwee Kuan Lee, Tat-Jen Cham 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse-view 3D coronary reconstruction commonly relies on cross-view correspondence and triangulation, which are vulnerable to vessel overlap and foreshortening, or on volumetric prediction followed by vascular-graph extraction, which does not directly provide centrelines and radii. We introduce PPCAR-Net, a projection-refined parametric coronary artery reconstruction network that directly predicts a branch-structured centreline-and-radius representation without explicit point matching, triangulation, or an intermediate volume. Given a variable number of segmented views, a coarse predictor combines frozen VGGT features with learned branch queries to estimate branch presence, B-spline centreline trajectories, and dense radius profiles. Projection-guided geometry and radius refiners then sample local evidence from the input views and apply residual corrections learned with 3D supervision. We evaluate representation fidelity and sparse-view reconstruction quantitatively and qualitatively. On simulated angiographic masks generated from CT-derived coronary anatomy, PPCAR-Net produces better connected artery reconstructions and achieves strong centreline accuracy, particularly for RCA, while maintaining competitive volumetric overlap. Coarse-to-fine inference takes 121 ms, enabling real-time reconstruction.

---


### 108. [One Frame, Full Heartbeat: ECG-Free Cardiac Cine MRI Synthesis via Phase-Conditioned Flow Matching](https://arxiv.org/abs/2610.09397)

**<font color=#1a73e8>作者：</font>** Shiyi Wang, Ruochen Sun, Peirong Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cine cardiovascular magnetic resonance (CMR) analysis relies on multi-frame sequences capturing the full cardiac cycle. However, standard multi-frame acquisition depends heavily on electrocardiogram (ECG) gating and repeated breath-holds, posing challenges in uncooperative populations, resource-limited settings, and temporally corrupted datasets. Existing methods that synthesize full cardiac sequences either rely on explicit ECG signals to parameterize myocardium function, or employ deformable registration without physiological constraints, failing to faithfully reproduce clinically relevant dynamic metrics such as ejection fraction (EF) and ventricular contraction magnitude. We present PhaseFlow, a unified generative framework that overcomes both limitations. PhaseFlow estimates a non-linear cardiac phase signal directly from the input sequence via a segmentation-derived left-ventricular (LV) area curve, capturing the asymmetric dynamics of systole and diastole without any ECG dependency. At inference, this phase signal is provided by a pathology-specific template, informing phase-specific frame generation. A rectified flow model conditioned on the phase and slice position synthesizes the full cardiac motion trajectory in the latent space, decoded into a diffeomorphic displacement field that warps end-diastole pixel intensities directly, eliminating the reconstruction blur often accompanying the variational autoencoder. On the ACDC benchmark, PhaseFlow achieves superior physiological fidelity and image realism, with best LV volume curve $R^2$, structural similarity (SSIM) and generative quality (FID) among all baselines. Ablation studies confirm that each proposed component contributes measurably to the overall performance.

---


### 109. [Noise, Denoise, Correct: MCMC Posterior Sampling with Diffusion Priors in Three Steps](https://arxiv.org/abs/2610.09407)

**<font color=#1a73e8>作者：</font>** So Takao, Gregory David Bellchambers, Luke Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained diffusion models are powerful priors for inverse problems, but posterior sampling under nonlinear, non-differentiable forward models remain hard. We introduce diffusion waltz, an MCMC method using SDEdit-style noising-denoising as a proposal, corrected via Metropolis-Hastings for exact posterior sampling without prior evaluation. We further propose injecting observations into the proposal while preserving exactness, using a gradient-free ensemble Kalman update. On a non-differentiable Navier-Stokes initial condition recovery task, diffusion waltz outperforms existing baselines across different noise and nonlinearity regimes.

---


### 110. [Shared Geometry As A Rosetta Stone: Cross-Modal Alignment Without Paired Data](https://arxiv.org/abs/2610.09411)

**<font color=#1a73e8>作者：</font>** Dominik Schnaus, Thomas Dagès, Daniel Cremers 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal representations enable zero-shot classification and retrieval, but aligning independently trained models usually requires large amounts of paired data. Yet, the Platonic Representation Hypothesis suggests that models trained on different modalities may converge spontaneously toward a shared representation geometry. But then, do we even need paired examples for cross-modal alignment? Remarkably, we show that paired examples are unnecessary for coarse cross-modal alignment. Our simple Wasserstein Procrustes method with a coarse geometric initialization aligns two disjoint embedding sets by estimating a single orthogonal map without seeing any pairs. Across datasets, modalities, and unimodal models, we show that we can consistently align independently trained representations without pairs, and standard geometric alignment metrics accurately predict when this is possible. Nevertheless, we can naturally benefit from paired examples. In the very few-pair regime, our method substantially outperforms existing ones, while staying competitive with pair-based methods with more added examples. Finally, we demonstrate that the resulting alignments can enable text-to-image generation without paired examples. These results show that independently trained models often share enough geometry to establish cross-modal correspondence with little or no paired data.

---


### 111. [Self-Consuming Generative Models with Co-Evolving Human Preferences](https://arxiv.org/abs/2610.09415)

**<font color=#1a73e8>作者：</font>** Xiukun Wei, Tian Xie, Ding Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models are increasingly trained in self-consuming iterative loops, where users curate preferred samples from model-generated candidates and the curated samples are used to train future generations of the model. Prior work has largely assumed fixed user preferences, but in practice exposure to model outputs gradually reshapes what users perceive as desirable, creating a feedback loop in which model distributions and user preferences co-evolve. We take a first step toward understanding the long-term behavior of such coupled dynamics. We show that when training relies entirely on user-curated synthetic data, iterative curation amplifies initial biases and drives the system toward one of multiple singleton equilibria in which the instance holding an initial advantage eventually dominates. In contrast, injecting reference data into training at a sufficiently large rate fundamentally changes the dynamics and yields a unique globally attracting equilibrium. Building on this insight, we study how reference-data injection can be used to control long-term outcomes, and propose an efficient algorithm that jointly selects a reference distribution and its mixing weight to steer the coupled system toward equilibria that preserve desired attributes while minimizing data collection costs.

---


### 112. [trACT: temporal revelation Airborne Camera Trap](https://arxiv.org/abs/2610.09417)

**<font color=#1a73e8>作者：</font>** Oliver Bimber, Rakesh John Amala Arokia Nathan, Mohamed Youssef 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Effective remote monitoring and surveillance using drones are frequently impeded by severe environmental and thermal clutter, dynamic vegetation, target camouflage, and system latency. Drawing inspiration from the hunting strategies of birds of prey that hover and stabilize their vision to isolate subtle ground motion, we introduce trACT (temporal revelation Airborne Camera Trap), a lightweight, real-time aerial robotics framework designed for autonomous consumer drones. The system integrates Temporal Max Pooling (TMP), a low-level signal processing method that transforms imperceptible movement across a rolling integration window into robust value and time encodings, with self-supervised motion anomaly detection to isolate target motion from background environmental motion caused by wind gusts and drone drift. To overcome mechanical and processing delays, trACT combines motion prediction with automated gimbal-stabilized optical zoom verification and equitable multi-target verification balancing. Extensive real-world field experiments in densely forested wildlife habitats and surveillance scenarios demonstrate that trACT successfully bridges the gap between wide-area aerial monitoring and precise, autonomous target verification under challenging operational conditions.

---


### 113. [What a Reporting Convention Hides: A Matched-Budget Audit of Quantum Natural Gradient with an Exactly Computed Metric](https://arxiv.org/abs/2610.09425)

**<font color=#1a73e8>作者：</font>** Lu Wei, Yufeng Wang, Haibin Ling  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Several published comparisons of variational quantum optimizers time only runs that reach a target loss, or read the verdict at a single target. Either convention could decide whether an optimizer's costlier steps pay off. We measure how much each convention changes verdicts among Adam, simultaneous perturbation stochastic approximation (SPSA) and quantum natural gradient (QNG), on initializations held out from the selection of settings. We compute the exact metric that preconditions QNG, price every step in circuit evaluations and give every method the same budget. In a median pooled over circuit widths, cost families and a sweep of settings with common misses, SPSA needs more than twice Adam's evaluations to reach a loose target. Dropping the censored runs that miss the target hides this gap. On the global-cost family we hold fixed the settings selected for a strict target. QNG then usually reaches the loose target after Adam but the strict target first. QNG's strict-target lead disappears when the metric's simulator price, linear in the number of parameters, is replaced by an assumed hardware count quadratic in that number. We recommend charging every miss the budget and reporting verdicts across targets.

---


### 114. [RSI-Forge: From Research Papers to Environments for Recursive Self-Improvement](https://arxiv.org/abs/2610.09426)

**<font color=#1a73e8>作者：</font>** Renxiong Wang, Darvin Yi, Abril Herrlein 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Environments are the foundation of recursive self-improvement: they provide the problems agents work on and the feedback used to evaluate progress. Yet constructing challenging research environments with reliable evaluation still depends on domain experts, limiting their scale and disciplinary coverage. We introduce RSI-Forge, a multi-agent pipeline that turns published papers into executable environments for self-improvement. Three agents coordinate construction, reproduction, and review to produce tasks with automated evaluators; each paper's method is independently reimplemented to establish a baseline score. We present 210 environments across 18 fields, including 90 reviewed by independent human domain experts. Both experts and agent judges give high ratings to the potential for improving the provided starting solutions and the evaluators' ability to distinguish solution quality, whereas experts are more critical of shortcut resistance, faithfulness to the source paper, and whether a single idea can exhaust a task. To validate their use for repeated improvement, we evaluate four models over 3 successive attempts on 120 environments, with each attempt inheriting prior code and notes while model weights remain fixed. At least one model improves after the first attempt in 84% of environments. Models also outperform the reproduced paper methods in 68 of the 120 environments, demonstrating room for gains beyond these baselines. Transcript analysis identifies work beyond parameter tuning in 95% of these successful attempts. Analysis of the resulting trajectories shows that models scoring lower on these tasks explore less, more often accept gains smaller than the reported standard error, and rely more heavily on tuning to the development set. RSI-Forge provides a scalable approach to constructing research environments for training and evaluating self-improving agents.

---


### 115. [Event-Aligned Visual Action Reasoning for World Action Models](https://arxiv.org/abs/2610.09427)

**<font color=#1a73e8>作者：</font>** Xiaomeng Yang, Yushu Wu, Yi Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World-Action Models (WAMs) utilize future visual prediction as an intermediate reasoning process to guide action generation. However, existing WAMs typically structure visual imagination according to predefined temporal intervals, without explicitly accounting for the different roles of task-critical interactions and connecting transitions. We argue that effective visual foresight should align directly with task-relevant interactions and their corresponding reasoning demands. To this end, we introduce an event-aligned visual action reasoning framework that organizes visual-action prediction around interaction events. Through event-aligned visual-action supervision, WAM learns to generate event-aligned visual context in each imagined rollout, placing greater emphasis on critical state changes that inform action generation. This shapes the visual reasoning granularity according to the underlying interaction dynamics, with detailed reasoning around task-critical events and coarser progression through connecting transitions. Furthermore, we introduce an execution validity head that identifies the valid portion of each predicted action sequence, avoiding redundant actions during chunked inference. Experiments demonstrate a 10.26 percentage point improvement in DOMINO success rate over baseline and competitive performance on RoboTwin 2.0. It also transfers from DOMINO Level 1 to Levels 2 and 3 without target-level adaptation.

---


### 116. [An extended deep energy method for thermo-mechanical crack propagation](https://arxiv.org/abs/2610.09433)

**<font color=#1a73e8>作者：</font>** Han Zhang, Mehrisadat Makki Alamdari, Babak Shahbodagh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Thermo-mechanical fracture couples transient heat conduction on a cracked domain with a crack that grows as the temperature and the displacement evolve. Neural energy solvers have been proposed for phase-field fracture and later extended to represent a sharp crack through the network input, but heat conduction on the cracked domain and crack propagation under the resulting thermal stresses have not yet been treated together in these solvers. We present an extended deep energy method for thermo-mechanical crack propagation in which the crack remains a sharp polyline. Two networks represent the temperature and the displacement and receive the crack through a scalar embedding function, discontinuous across the crack and smooth elsewhere, so that both fields can jump across it without a regularization length, and the displacement is enriched near the tip by the Williams expansion with trainable amplitudes. The two fields are obtained by minimizing an incremental conduction functional and the thermoelastic potential energy in a staggered sequence, with Monte Carlo integration on points stratified over background elements, densified near the tip and redrawn during training. The stress intensity factors are extracted by the interaction integral with the area term of Wilson and Yu and checked by a sweep of the contour radius, and the crack advances at the maximum hoop stress angle when the energy release rate of the kink reaches the critical value at the crack-tip temperature. On a stationary thermal edge crack the extracted stress intensity factor agrees with the published value to 0.11%, in a functionally graded shear test initiation agrees with an independent sharp-crack finite element solution to within one load step, and on a notched cruciform specimen the crack paths follow the published solutions under mechanical, thermal and combined loading.

---


### 117. [Controllable Crowd Generation through World-Model Planning](https://arxiv.org/abs/2610.09438)

**<font color=#1a73e8>作者：</font>** JunGyu Lee, Jisu Shin, Seunghyun Shin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Crowd simulation plays a central role in robot navigation, autonomous driving, and urban planning. For these applications, realistic simulation requires crowds to adapt their behavior to environmental changes and user objectives. However, existing methods that rely on predefined control settings have limited flexibility in accommodating new user-specified objectives. To address this limitation, we propose Ctrl-CWM, a multi-agent Controllable Crowd World Model that integrates crowd generation and run-time control. Our key idea is to adapt the world-model principle of planning using imagined futures to crowd simulation. To this end, Ctrl-CWM consists of an encoder that learns a representation of human motion dynamics, an actor that proposes pedestrian displacements, a critic that evaluates imagined crowd trajectories, and a planner that selects actions. We first learn human motion dynamics through trajectory prediction on real-world pedestrian videos and then freeze the encoder to preserve them. Using this representation, the actor generates imagined crowd trajectories through repeated state updates, and the planner combines the critic's scores with user costs to select actions. Repeated planning advances the simulated crowd, while additional user costs introduce new control objectives without retraining. We extensively evaluate crowd generation under varied agent arrival conditions and run-time control across avoidance and attraction scenarios. Ctrl-CWM outperforms the state-of-the-art method on most crowd realism and collision metrics, and adapts crowd behaviors to user-specified objectives introduced during simulation. The project page is available at this https URL

---


### 118. [InscriptionOCR: A Dataset and Method for Understanding Inscriptions](https://arxiv.org/abs/2610.09439)

**<font color=#1a73e8>作者：</font>** Jaidev Sanjay Khalane, Akbar Ali, V. N. Prabhakar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ancient script image restoration is a fundamental problem in computer vision, as it directly affects the reliable analysis and interpretation of historical documents and inscriptions. Ashokan Brahmi is an ancient script extensively used during the reign of Emperor Ashoka in the 3rd century BC, primarily for inscriptions in Prakrit. These inscriptions, including major and minor rock and pillar edicts, constitute a valuable yet largely unexplored source of data for computational analysis. The degraded nature of inscription imagery and the lack of standardized digital resources pose significant challenges for automated processing.
We present an end-to-end AI-based framework for understanding ancient inscriptions that encompasses image enhancement, optical character recognition (OCR), transliteration, and neural machine translation (NMT). The proposed pipeline processes low-quality images captured directly from stone inscriptions, performs image restoration and Brahmi script character recognition, maps the recognized characters to the Roman script, and finally translates the resulting Prakrit text into English. We also introduce two new datasets: (i) InscriptionOCR Dataset: the largest publicly usable digital OCR dataset for Brahmi script to date, consisting of over 200,000 character images across about 600 classes, and (ii) a bilingual Prakrit-English parallel corpus comprising over 2,000 sentence pairs for NMT. We believe that the proposed framework and datasets will facilitate future research in ancient script analysis, low-resource OCR, and digital epigraphy.

---


### 119. [TIRA: Tumor Immune Representation Adaptation for Zero-Shot Cross-Cancer MSI and TMB Prediction](https://arxiv.org/abs/2610.09441)

**<font color=#1a73e8>作者：</font>** Dasari Naga Raju  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Microsatellite instability-high (MSI-H) and high tumor mutational burden (TMB-H) are clinically relevant biomarkers, yet their histopathological prediction remains challenging when models are transferred across morphologically distinct cancer types. Immune-associated spatial patterns can persist across cancers despite these morphological differences, but foundation-model-based predictors trained on a single cancer do not explicitly use this information, limiting cross-cancer generalization. To address this limitation, we propose TIRA (Tumor Immune Representation Adaptation), a target-free framework that refines frozen foundation-model representations using spatial immune topology, without requiring target-domain data during model development or test-time adaptation. TIRA uses a topology-supervised biology representation to condition tile-level attention while pooling only morphological features for joint MSI and TMB prediction. We train TIRA on TCGA-COAD+READ and evaluate it zero-shot on CPTAC-COAD, TCGA-STAD, TCGA-UCEC, and CPTAC-UCEC, covering cross-site, cross-cancer, and combined cross-cancer-site distribution shifts under UNI2, CONCH, and Virchow2. With UNI2, TIRA improved zero-shot AUROC on TCGA-STAD from 0.633 to 0.766 for MSI and from 0.651 to 0.772 for TMB. Source-derived spatial immune topology improved the cross-cancer robustness of frozen pathology foundation-model representations.

---


### 120. [LighTROcc: Lightweight 4D Occupancy Forecasting via Instance-Centric 3D Gaussians](https://arxiv.org/abs/2610.09444)

**<font color=#1a73e8>作者：</font>** Hwanhee Jung, SeungHyeon Kim, Inkyu Koo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forecasting future 3D occupancy from surround-view cameras is essential for autonomous driving, yet existing approaches rely on dense voxel or bird's-eye-view representations whose cost grows rapidly with spatial resolution and prediction horizon. Because these representations do not explicitly maintain object identities, they also struggle to preserve instance consistency over time. We present LighTROcc, a lightweight instance-centric framework that represents movable objects with a compact set of learned queries and predicts present and future occupancy in a single forward pass. LighTROcc localizes each query through attention-guided forward lifting, combining image-space cross-attention, query-specific depth, and camera geometry to estimate its 3D center. Each instance is modeled as a mixture of anisotropic 3D Gaussians and propagated across future steps using predicted displacements, producing continuous, temporally consistent occupancy forecasts. Experiments on nuScenes and supplemented nuScenes-Occupancy show that LighTROcc outperforms the evaluated dense and instance-wise baselines in instance-level forecasting accuracy while maintaining strong voxel-level occupancy quality. Across different model configurations, LighTROcc achieves a favorable balance between forecasting accuracy and computational efficiency, demonstrating the potential of compact instance-centric modeling for camera-based 4D occupancy forecasting.

---


### 121. [From Global Alignment to Local Grounding: Zero-Shot Chinese Character Recognition with Radical Verification](https://arxiv.org/abs/2610.09449)

**<font color=#1a73e8>作者：</font>** Yu-Heng Shih, Bing-Chen Wu, Tsz-To Wong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot Chinese character recognition (ZS-CCR) aims to recognize characters whose categories are never observed during training, and typically relies on the compositional structure shared between seen and unseen characters. Recent CLIP-style methods represent this structure with the Ideographic Description Sequence (IDS) and align it with glyph images in a shared embedding space. However, they rely on a single global image--IDS similarity that discards the spatial layout of radicals and, being learned only implicitly from seen classes, generalizes poorly to unseen ones; moreover, global matching often retrieves the correct character within the top candidates yet fails to rank it first when characters differ only in subtle local radicals. To address these issues, we propose a global-to-local two-stage framework. In the first stage, STG-CLIP augments the IDS with explicit tree-position and radical-level geometric priors, yielding a spatial-aware prototype that provides a consistent spatial description across seen and unseen categories for high-recall global retrieval. In the second stage, the Radical Verification Module (RVM) uses the radical instances of each retrieved candidate as queries to verify whether the corresponding radicals can be matched to spatially compatible regions in the input glyph. A margin-based gating rule activates the RVM only when the leading global candidates receive similar similarity scores. Experiments on the ICDAR2013 benchmark demonstrate that our method achieves state-of-the-art performance under the character-level zero-shot setting, obtaining 83.06% top-1 accuracy with 2,755 seen classes. Ablation studies further show that the explicit geometric priors and radical-level verification provide complementary improvements.

---


### 122. [DSReg: Provably Recovering Individual World Latents without Reconstruction](https://arxiv.org/abs/2610.09457)

**<font color=#1a73e8>作者：</font>** Yujia Zheng, David Klindt, Randall Balestriero 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Methods that recover individual latent variables of the world, from nonlinear ICA to dictionary learning and causal representation learning, anchor the latents to observations through reconstruction, auxiliary supervision, or distributional asymmetries such as non-Gaussianity. Methods without these anchors, including joint-embedding predictive architectures (JEPAs), identify the latent state only up to a linear transformation, so individual latents remain mixed. We close this gap: individual world latents can be provably recovered with no reconstruction, no decoder, and no labels. The key condition is Structural Diversity: different latents leave distinct dependency footprints on observations, just as no two snowflakes are alike. Building on the linear identifiability that LeJEPA provides, we prove that under Structural Diversity, DSReg (Dependency-Sparsity Regularization) recovers individual world latents up to signed permutation, without reconstruction or a decoder. It applies post hoc to any linearly identified representation, reusing trained checkpoints at no loss over joint training, and establishes the first fully identifiable JEPA that recovers every world latent. Moreover, as a condition on dependency footprints, Structural Diversity is strictly weaker than all structural conditions of prior identifiable latent variable models. Across synthetic regimes, world model probes, learned visual encoders, and external renderers, DSReg preserves dense prediction while improving individual-latent recovery and downstream use with scales.

---


### 123. [An Invariant Tangent-Angle Descriptor and a Band U-Net for 2D Fragment Adjacency Prediction](https://arxiv.org/abs/2610.09459)

**<font color=#1a73e8>作者：</font>** Guillaume Brouillette, Alain Goupil, Pierre-Olivier Parisé 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper addresses the prediction of adjacency between pairs of 2D fragments based on their contours. We improved the two-stage architecture proposed in Beaulac's thesis, in which a rotation-equivariant Siamese convolutional neural network scores pairs of local image windows along the two contours of two fragments. The scores are gathered in an adjacency matrix in which a ResNet detects the partial anti-diagonal band that reveals the adjacency of two fragments. In the current work, we keep the pipeline and replace the local score by a comparison of tangent-angle profiles of contour windows, making it, by construction, invariant to fragment rotation and agnostic to the selected contour-starting point. These adaptations may be either a training-free likelihood ratio or a small one-dimensional convolutional model trained on corresponding points. We also replaced the final classifier by a band U-Net that segments the band and classifies the pair, so that the shared arc is obtained along with the decision. In the synthetic data set of the original thesis, the tangent descriptor performs as well as or better than the image-window approach in all tested configurations. The proposed pipeline reaches an accuracy of 98%, vs 93% to 95% for the original approach once its evaluation is corrected. We tested our pipeline, with models trained only on synthetic data, on the PairingNet benchmark, and obtained an AUC of 0.93. Furthermore, under the PairingNet pair-searching protocol conditions, our learned descriptor obtains a Recall@10 of 0.82 on the real set against 0.56 from the best model of the original paper.

---


### 124. [BanglaRhet: Benchmarking Classical and Transformer Models for Rhetorical and Persuasion Detection in Bangla Political Speech](https://arxiv.org/abs/2610.09464)

**<font color=#1a73e8>作者：</font>** Rohit Kumar Sen, Anik Chowdhury  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Political discourse often uses rhetorical and persuasive language to frame narratives, influence public opinion, and mobilize audiences. While Bangla natural language processing has made progress in sentiment analysis and opinion mining, systematic benchmarking of transformer models for fine-grained rhetorical and persuasion technique detection in Bangla political speech remains largely underexplored. This paper presents a benchmark study of transformer-based models for detecting rhetorical form and persuasive intent in Bangla political discourse. Using BanglaRhet, a manually annotated corpus of 30,289 Bangla political speech segments collected from publicly available political news sources, we formulate two supervised single-label classification tasks: rhetorical technique detection (contrast, repetition, exaggeration, metaphor, rhetorical questions) and persuasion technique detection (blame assignment, call to action, unity call, moral, emotional, and logical appeals). We evaluate four transformer-based models, BanglaBERT, BanglaBERT-Base, SahajBERT, and XLM-RoBERTa-Base, against classical TF-IDF baselines. BanglaBERT achieves the highest performance, with 65.40% macro-F1 for rhetorical technique detection and 66.46% for persuasion technique detection, outperforming the best tuned classical baseline by 19.2 and 13.8 macro-F1 points, respectively. Class-level analysis indicates that errors are mainly associated with semantic overlap among labels, figurative language, and class imbalance. The results provide initial benchmark baselines for Bangla rhetorical and persuasion-aware political discourse analysis and highlight the need for context-aware and multi-label modeling.

---


### 125. [MORA: Modeling Observed Changes for Drift-Robust Time-Series Anomaly Detection](https://arxiv.org/abs/2610.09473)

**<font color=#1a73e8>作者：</font>** Xudong Mou, Tiejun Wang, Rui Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series anomaly detection (TSAD) identifies deviations from patterns learned from historical data. In non-stationary settings, distribution drift and true anomalies can cause similar local changes, making it difficult to tell whether a deviation reflects abnormality or evolving context. Existing methods typically adapt to detected shifts or learn drift-insensitive representations, but do not resolve this ambiguity. We define this problem as \emph{temporal change disambiguation}: determining whether a local deviation is explained by broader temporal evolution. We introduce MORA, a drift-robust TSAD framework that reconstructs the same local target from paired short- and long-term views. The reconstruction gap measures contextual support for a local deviation, and a data-dependent correction mechanism conservatively adjusts the primary local anomaly score. Context can only reduce the score when it improves reconstruction of the same target. MORA needs neither drift annotations nor online adaptation. Experiments on four TSAD benchmarks show strong robustness to non-stationarity while preserving sensitivity to genuine anomalies.

---


### 126. [InstanceBench: Diagnosing Referential Reasoning and Target Identity in Referring Expression Segmentation](https://arxiv.org/abs/2610.09478)

**<font color=#1a73e8>作者：</font>** Yuchen Li, Shaoyang Zhou, Yiran Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring Expression Segmentation (RES) links natural-language descriptions to pixel-level object masks. Yet standard evaluation provides limited insight into instance-level referential reasoning: it does not systematically distinguish referential logics, test target preservation across valid grounding paths, or separate target-selection from mask-generation errors. We introduce InstanceBench, an instance-centered diagnostic benchmark comprising 6,194 images, 9,264 target instances, and 25,077 human-verified expressions. Each target-centric expression set (TCES) fixes the image and target mask while pairing a minimal expression with a same-target variant that uses another valid cue or grounding path. A compact referential-logic taxonomy spans direct target evidence, same-class selection, relational and compositional grounding, and exclusion, while logic-critical construction suppresses simpler shortcuts. Identity-aware metrics measure target retention and set-level success while separating selection from mask-generation errors. Across 22 native-mask RES checkpoints from 18 model families, the strongest checkpoint reaches 67.1% mIoU but only 59.6% All@0.7. Controlled interventions confirm language sensitivity, while failure decomposition identifies target selection rather than mask decoding as the main bottleneck. On a controlled training subset, matched supervision improves identity-aware performance, showing that the diagnosed capability responds to targeted supervision. Collectively, InstanceBench supports a measure-diagnose-improve cycle: measuring target consistency across grounding paths, localizing failure sources, and evaluating targeted interventions.

---


### 127. [Gaussian Material Fields for Volumetric Multi-Energy CT Decomposition](https://arxiv.org/abs/2610.09492)

**<font color=#1a73e8>作者：</font>** Jian Lin, Jiancheng Fang, Hongming Shan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Volumetric material decomposition in multi-energy computed tomography requires a representation that organizes multiple three-dimensional material fields in a common spatial domain while retaining differences in composition and local structure. We observe that spatial primitives can be shared across materials without tying their coefficients, but their local capacity must respond to material-specific reconstruction needs. We introduce Gaussian material fields, which represent multiple material distributions with shared anisotropic 3D Gaussian primitives and independent nonnegative material coefficients. The shared geometry defines a continuous spatial basis, while the coefficients determine each primitive's contribution to the individual material fields. To reconstruct this representation from multi-energy projections, a differentiable spectral forward model combines Gaussian material path integrals with a calibrated basis matrix, enabling joint optimization of spatial geometry and material composition. Material-aware adaptive density control retains material-specific refinement evidence before aggregation and adjusts local representation capacity to accommodate both spatially extensive components and sparse details. Experiments use synthesized multi-energy projections generated from pseudo-reference material maps constructed by conventional methods from publicly available CT data. Across 15 cases, our approach improves average PSNR by 4.03 dB and SSIM by 4.96% over the strongest baseline, while reducing NRMSE by 33.45%. Material-wise comparisons and component ablations support improved recovery of localized structures, while runtime and memory measurements show favorable computational scaling. These results establish Gaussian material fields as an explicit, adaptive representation for volumetric multi-material reconstruction.

---


### 128. [Cognitive Schemas, Laws and Tasks](https://arxiv.org/abs/2610.09495)

**<font color=#1a73e8>作者：</font>** Antal Jakovác, András Telcs  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper asks how explicit representations can support reusable cognitive schemas in knowledge-based problem solving. We develop a structural framework in which schemas are organized by the information and relations required for their use, rather than introduced as unrelated primitives. The framework also distinguishes context-dependent relations from more stable structures that can be reused across different representations.
Tasks are described through the information available, the unknowns to be determined, and the constraints that admissible solutions must satisfy. This makes it possible to separate limitations of the representation from limitations of the solving procedure. In particular, we distinguish inconsistency, underdetermination, and contextual insufficiency, where the current representation lacks distinctions or relations required by the external task meaning. We also show formally when a reduction of representation preserves the task-relevant solution structure.
The resulting task--schema interface offers a structured way to describe representational conditions relevant to problem solving. It supports the reuse and stabilization of derived knowledge while remaining independent of the particular mechanism used to generate candidate solutions. This may provide a useful component for future solver architectures that combine structured knowledge, verification, and learned proposal mechanisms.

---


### 129. [Ream: Unfolding Mutual Awareness in Human-Agent Workspaces](https://arxiv.org/abs/2610.09497)

**<font color=#1a73e8>作者：</font>** Peiling Jiang, Sangho Suh, Varsha Kishore 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI agents work alongside humans in shared workspaces, a mutual awareness challenge arises: agents act at speeds that outpace human monitoring, and users' evolving interests are not always expressed in chat. This challenge is especially pressing in literature review, where both parties retrieve, read, and synthesize a growing body of papers. We present Ream, a literature review workspace that supports mutual awareness through structured artifacts, bidirectional engagement tracking, and localized visualizations. Users can see each party's activity within these documents, and agents can retrieve the same history to guide their work. In studies with eighteen researchers, participants used these traces to inspect evidence, steer agents, communicate through annotations, and reflect on their research focus. Shared histories also helped agents build on earlier work. These findings inform how engagement traces within shared documents can support transparency, personalized assistance, and coordination in human-agent knowledge work.

---


### 130. [SpatialUQ: Post-Hoc Uncertainty Quantification from Spatial Consistency in Black-Box Vision Models](https://arxiv.org/abs/2610.09498)

**<font color=#1a73e8>作者：</font>** Md Kawsher Mahbub, Milon Biswas, Mirza Niaz Morshed 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinical vision models are often deployed as frozen black boxes with no access to internals, retraining, or ground truth at inference time. We introduce \textbf{SpatialUQ}, a post-hoc uncertainty method using only output probabilities. It measures the Jensen-Shannon divergence between the global prediction and the mean of five fixed spatial crops in six deterministic forward passes. The premise is simple, trustworthy predictions are spatially consistent. On NIH ChestX-ray14 (DenseNet-121, $N{=}25{,}596$), our Multicrop Uncertainty Score (MUS) reaches $0.784$ failure-detection AUC versus $0.664$ for MC-Dropout ($p{<}10^{-6}$) at one-fifth the compute, with native calibration ($\text{SCE}{=}0.049$ vs.\ $0.127$ for $\ell_1$), the best-calibrated among methods above 0.78 AUC. A supervised fusion of MUS with entropy, confidence, and $\ell_1$ reaches $0.832$, outperforming a five-member ensemble ($0.813$). MUS scales with model quality, reaching $0.899$ with BiomedCLIP ($\rho = 0.846$), while this relationship remains meaningful in-distribution ($\rho = 0.523$) but breaks down under severe distribution shift (VinBigData, $\rho = 0.027$). MUS is well-suited to diffuse findings but is less dependable for small focal lesions such as nodules. Code and experimental materials are publicly available at this https URL.

---


### 131. [Safe on Average, Unsafe in the Tail: When Is the Episodic-Cost Tail Controllable?](https://arxiv.org/abs/2610.09508)

**<font color=#1a73e8>作者：</font>** Samuel Tetteh, Cody Fleming  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safe reinforcement learning seeks policies that maximize return while satisfying constraints on cumulative cost. Most methods impose these constraints on expected episodic cost. Consequently, standard evaluations report mean episodic cost without characterizing how cost is distributed across episodes. A policy that satisfies the mean-cost criterion may therefore remain unsafe in its worst episodes. Mean-cost reporting neither identifies this tail violation nor shows whether it can be brought within budget while preserving return. In this work, we measure the episodic-cost tail using $\mathrm{CVaR}_{0.1}$, the average cost of the worst $10\%$ of episodes. We classify a policy as tail-safe when $\mathrm{CVaR}_{0.1}$ is within the safety budget. This allows us first to identify policies that are safe on average but unsafe in the tail and then to study whether their tail violations can be controlled while preserving return. To identify tail-unsafe policies, we evaluate five standard algorithms on three Safety-Gymnasium navigation tasks. We then examine four constraint families on dense-hazard navigation and assess tail control across four navigation and four locomotion tasks.

---


### 132. [TERRA: Learning Transportable Latent Actions through Temporal Effect Representation and Relational Alignment](https://arxiv.org/abs/2610.09509)

**<font color=#1a73e8>作者：</font>** Tianxingjian Ding, Mubarak Shah, Yu Tian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent actions supervise robot policies with action-like codes inferred from visual transitions, and their usefulness hinges on two questions: what a code keeps from a transition, and whether it still means the same thing when reused in a different initial state. The first is a tension in time: an endpoint difference discards how motion unfolds, while the full sequence admits nuisance variation. The second is left open by reconstruction, which only ever observes a latent together with the state it came from. We argue that both questions can be answered in the same place. TERRA (Temporal Effect Representation and Relational Alignment) describes a transition by a compact temporal effect, its net feature change together with a low-order within-window dynamics component, and learns a continuous latent from this effect. The same effect space then serves as the reference for reuse: Effect-Anchored Transport (EAT) decodes a latent in other initial states and anchors the resulting effect to the one observed at its source, so that the latent is shaped by what it does across contexts rather than only by the transition it came from. With frozen linear readers, TERRA predicts actions more accurately than UniVLA and a LAPA-style baseline, degrades more slowly under visual distractors, and keeps transported transitions faithful to the donor action as the recipient context moves farther away; a same-budget control shows that these gains come largely from EAT. At matched pretraining scale, the complete system reaches 93.4% average success on LIBERO, compared with 91.8% for UniVLA.

---


### 133. [Physics-Informed Neural Plasticity: PDE Solvers That Reshape Themselves](https://arxiv.org/abs/2610.09510)

**<font color=#1a73e8>作者：</font>** Chun-Wun Cheng, Bingcheng Hu, Angelica I. Aviles-Rivero  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural PDE solvers adapt their parameters to satisfy governing equations, yet their representational structure typically remains fixed throughout training. This rigidity is poorly matched to PDE solutions with strongly heterogeneous complexity across space and space--time, leaving capacity insufficient where the physics is difficult and redundant where it is simple. We introduce physics-informed neural plasticity, a paradigm in which the representation itself reshapes during optimization in response to unresolved physics. We instantiate this principle with Representation Capacity Adaptation for PDEs (ReCAP), a Gaussian-localized solver that dynamically redistributes capacity through local enrichment, residual-directed splitting, gate-based pruning, and function-aware merging. ReCAP uses responsibility-weighted error indicators and the geometry of residual energy to determine where and how to refine. To limit the disturbance introduced by splitting, we introduce quiet-child refinement, which initializes new components by transporting the parent representation while controlling instantaneous functional perturbation. We further establish conditional a posteriori reliability and structural-stability guarantees linking localized physics residuals to solution error and stable refinement. Across five challenging 3D and 4D PDE benchmarks against 11 physics-informed solvers, ReCAP achieves the lowest relative $L^2$ error on every problem, reducing error by $10.7\%$--$27.5\%$ relative to the strongest competing result. These results suggest that physics-informed solvers need not merely learn their parameters---they can learn how their representational capacity should be organized.

---


### 134. [LiG-DETR: Local-in-Global Reassembly in Latent Space for Aerial Object Detection](https://arxiv.org/abs/2610.09511)

**<font color=#1a73e8>作者：</font>** Yupeng Zhang, Fangzhuo Gao, Juntao Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aerial object detection faces substantial scale and density variations. Small objects are easily degraded by downsampling and feature compression, while medium and large objects require sufficient global context. Existing methods mainly follow two paradigms: image slicing provides clearer local evidence but relies on independent crop-level prediction and post-processing, whereas feature- and query-level optimization preserves unified inference but operates on already compressed full-image representations, limiting recovery of fine-grained information. This raises a key question: can aerial detection directly acquire high-fidelity local evidence before feature degradation and integrate it into a unified end-to-end framework? To this end, we propose LiG-DETR, an Efficient Global-Local Reassembly framework that reformulates image slicing as high-fidelity local feature acquisition. A shared encoder extracts global and locally magnified features, which are projected into the detector feature space. The projected local features are reassembled according to their original spatial locations to form a globally aligned local feature level, and a single DETR decoder jointly decodes global and local features. To reduce redundant computation, Context-Preserved Selective Reassembly focuses high-resolution encoding on informative regions while preserving a dense feature layout, and Density-Aware Adaptive Query Allocation adapts the decoder query budget using encoder proposal scores. Experiments show substantial gains on small and medium objects while retaining strong large-object performance, with favorable accuracy--efficiency trade-offs and improved cross-domain generalization. The code will be released.

---


### 135. [OmniCam: Omni-Camera Trajectory Generation via Geometry-Grounded Pose Token Learning](https://arxiv.org/abs/2610.09513)

**<font color=#1a73e8>作者：</font>** Zhenyang Liu, Chenjie Cao, Yisu Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera trajectories control viewpoint changes in video generation, scene reconstruction, and robotic perception. Generating them from language requires both scene geometry and target-aware framing. We introduce OmniCam, an autoregressive model that generates camera pose sequences from a single panorama and textual trajectory descriptions. Its geometry-grounded pose token learning combines three components: a panoramic point-cloud encoder for omnidirectional geometric context; hybrid absolute-rotation and relative-translation tokenization with temporally consistent quaternion signs; and separate geometric and semantic conditioning streams with an explicit 3D target anchor. We also construct OmniCaT, containing 267,700 trajectories across four camera behaviors. On the reported OmniCaT evaluation, OmniCam reduces trajectory errors by 28--47% and collision rate by 65.8% relative to GenDoP retrained on OmniCaT. Against the best baseline for each metric, the ATE and collision reductions are 43.0% and 62.3%, respectively. Component ablations support the use of geometric and target-aware conditioning, while downstream experiments examine camera-controlled video generation and robotic active perception.

---


### 136. [STRIKE: Learning Visual State Transitions for Physical World Modeling](https://arxiv.org/abs/2610.09514)

**<font color=#1a73e8>作者：</font>** Wenbin Teng, Tianshuo Xu, Depu Meng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical world modeling requires predicting how interactions change a scene, not merely generating coherent motion. We propose STRIKE, a framework that separates visual state transition learning from dense video generation. We construct event-aligned supervision by extracting observed states from training videos and pairing them with transition descriptions and temporal offsets. An image-based transition model learns to predict the next scene configuration from the current image, a local transition specification, and elapsed time. At inference, a pretrained vision-language planner predicts time transition specifications, and recursive application of the learned transition model produces a sequence of future visual states. A separately trained dynamic model then generates the complete rollout conditioned on these states and their temporal locations. Experiments on Physics-IQ Verified, PhyGenBench, Pisa-Experiments, and RoboTwin2.0 show improvements of STRIKE over the corresponding video-backbone baselines in benchmark measures of physical consistency and manipulation-video fidelity. These results support learned visual state transitions as an effective intermediate representation for physical world modeling.

---


### 137. [ActiveLang: Active Open-Vocabulary 3D Mapping with Semantic-Uncertainty-Guided Exploration](https://arxiv.org/abs/2610.09518)

**<font color=#1a73e8>作者：</font>** Liyan Chen, Hairong Yin, Huangying Zhan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As robots increasingly assist humans with diverse tasks, they need both geometric and semantic understanding of their surroundings. Moreover, robots often operate in unfamiliar environments and take on new tasks without knowing the relevant concepts ahead of time. This motivates language-annotated 3D maps that support open-vocabulary scene understanding and human-robot interaction. We introduce ActiveLang, an autonomous system for active open-vocabulary 3D mapping with semantic-uncertainty-guided exploration. ActiveLang performs online language-feature adaptation on a compact dual-Gaussian representation to jointly reconstruct scene geometry, appearance, and open-vocabulary semantics with modest memory overhead. Its planner efficiently selects informative viewpoints, enabling effective mapping with fewer observations and lower computational cost. Experiments on Replica and ScanNet++ demonstrate substantial improvements in 2D and 3D open-vocabulary segmentation over both online and offline baselines, highlighting that actively exploring scenes builds language-annotated 3D maps more efficiently.

---


### 138. [Differential Refresh Policies for Models Trained on Lagging Data Snapshots: From a Single-Age Equivalence Limit to an Optimal Per-Segment Allocation](https://arxiv.org/abs/2610.09519)

**<font color=#1a73e8>作者：</font>** Amit Rajula  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Production machine-learning models are derived artifacts of time-bounded training snapshots: a deployed model is a materialized view over a training cut that ages the instant it is built. A common response is to replace the fixed retraining cadence with an adaptive trigger -- a weighted staleness score that retrains when accumulated source risk crosses a threshold. We show this is the wrong lever, and identify the right one. First, an equivalence limit: any refresh trigger that is a static, strictly monotone function of a single shared global training-data age is operationally equivalent to a calibrated uniform age timer, so a global staleness budget, however elaborately it weights segments, sources, and sensitivities, carries no scheduling information a clock does not. The limit also shows how to escape it: refresh segments differentially, giving each its own age and refresh interval, which is meaningful when refresh cost is separable across segments (incremental training or per-segment models). We solve the resulting budget-allocation problem. In the frequent-refresh regime each segment's optimal refresh rate is proportional to the square root of its risk $w_j \lambda_j$ (weight times change rate), and the optimal policy never costs more than the uniform timer, beating it by a closed-form Cauchy-Schwarz "price of uniformity" that is zero for homogeneous workloads and grows with heterogeneity. In a discrete-event simulation with real Poisson change events, the optimal policy lowers realized weighted stale exposure by 8-29% relative to the uniform timer at matched refresh budget, winning on 86-100% of seeds; a naive exposure-threshold policy does not, showing the allocation is what helps; and the advantage survives 50% rate-estimation noise. The leverage in model refresh is not a better score but a better action.

---


### 139. [Align Before You Combine: Reference Space Calibration for Supervision Without Ground Truth](https://arxiv.org/abs/2610.09525)

**<font color=#1a73e8>作者：</font>** Jackson Eshbaugh, Jorge Silveyra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce a calibration-first framework that produces supervision scores without access to ground-truth labels or a shared annotation space. Our framework aligns subset-specific scorers using a synthetic ordinal reference space before fusion. This reference space is constructed from ordered calibration features that represent the latent concept, providing a common scale on which otherwise incomparable scorer outputs can be aligned. Because our calibration procedure uses the reference space rather than training samples, it is independent of the training set's empirical distribution. Across three benchmark datasets, our framework consistently outperforms uncalibrated averaging and achieves higher primary-metric point estimates on the evaluation metrics than the best individual scorer. Performance relative to sample-dependent baselines varies by domain, with absolute differences below 0.02 on Ames Housing and below 0.01 on Breast Cancer Wisconsin and Wine Quality. After Bonferroni correction, differences remain significant for all three comparisons on Ames Housing and one on Breast Cancer Wisconsin. Additionally, we show that using fewer calibration levels per feature can closely approximate higher-resolution results at substantially lower computational cost. Together, these results support our framework as a viable approach to construct supervision scores when neither ground-truth labels nor a shared annotation space is available.

---


### 140. [A Comparative Study of Evaluation Metrics for Long-Document Financial Narrative Summarization with Transformers](https://arxiv.org/abs/2610.09529)

**<font color=#1a73e8>作者：</font>** Nadhem Zmandar, Mo El-Haj, Paul Rayson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> There are more than 2,000 listed companies on the UK's London Stock Exchange, divided into 11 sectors who are required to communicate their financial results at least twice in a single financial year. UK annual reports are very lengthy documents with around 80 pages on average. In this study, we aim to benchmark a variety of summarisation methods on a set of different pre-trained transformers with different extraction techniques. In addition, we considered multiple evaluation metrics in order to investigate their differing behaviour and applicability on a dataset from the Financial Narrative Summarisation (FNS 2020) shared task, which is composed of annual reports published by firms listed on the London Stock Exchange and their corresponding summaries. We hypothesise that some evaluation metrics do not reflect true summarisation ability and propose a novel BRUGEscore metric, as the harmonic mean of ROUGE-2 and BERTscore. Finally, we perform a statistical significance test on our results to verify whether they are statistically robust, alongside an adversarial analysis task with three different corruption methods.

---


### 141. [KASALv2: Fully Automatic 3D Rotational Symmetry Classification and Axis Localization](https://arxiv.org/abs/2610.09534)

**<font color=#1a73e8>作者：</font>** Mengxin Zhang, Yulin Wang, Chen Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rotational symmetry is an important prior in 6D pose estimation, improving pose accuracy and supporting symmetry-aware evaluation. However, current symmetry annotations for 3D objects remain largely manual or semi-automatic, often requiring predefined types or orders, which limits scalability. This work introduces a fully automatic, reference-free framework for symmetry-type classification, rotational-order identification, and full-axis localization across all eight canonical 3D rotational symmetry types. The method localizes a dominant high-order axis, infers its rotational order through self-consistency analysis, and reconstructs the complete symmetry structure under a hierarchy-guided formulation. A texture-aware extension further models appearance-induced reductions in rotational order while preserving axis orientations. Experiments on idealized and real-world datasets demonstrate strong accuracy and generalization, achieving 94.75% accuracy on 438 symmetric objects in GSO. Training FoundationPose with these priors improves accuracy by up to 0.9% across five BOP datasets, showing that automatically estimated rotational priors improve downstream 6D pose estimation. Code is available at this https URL.

---


### 142. [Human-AI Conversational Behaviors Predict Unassisted Task Performance](https://arxiv.org/abs/2610.09547)

**<font color=#1a73e8>作者：</font>** Li Siyan, Federico Bianchi, James Zou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Assistance from AI tools has supported and improved human performance across domains. However, recent research suggests that these immediate benefits may entail future costs, including diminished performance when AI assistance is no longer available. We study how human-AI interaction behaviors correlate with immediate and future unassisted task performance across two game-based problem-solving user studies ($n=139$ and $n=111$), using a \textit{dialogue act} framework adopted from a tutor-student dialogue taxonomy. In our studies, verbalizing thought processes correlates with higher unassisted outcomes, whereas directly requesting solutions correlates negatively. Similar to these participant-side patterns, assistant explanations of the current problem state are associated with better subsequent unassisted performance, whereas directly providing the next action is associated with worse performance. Qualitative and subtype analyses further show that ostensibly similar reasoning turns can elicit different assistance. Our findings suggest that preserving users' cognitive participation in problem-solving may support performance beyond AI-assisted interaction.

---


### 143. [CircuitGate: Logic-Consistent Circuit-Level Functional Modeling for And-Inverter Graphs](https://arxiv.org/abs/2610.09549)

**<font color=#1a73e8>作者：</font>** Qifan Zhang, Ruijie Li, Fangzhou Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> And-Inverter Graphs (AIGs) are fundamental representations for logic synthesis and verification in Electronic Design Automation (EDA). As structured representations of complex digital systems, AIGs require models to capture functional dependencies beyond local structure and remain robust to functionality-preserving transformations. In learning-based AIG representation, existing approaches are predominantly based on GNNs and rely on local gate-level message passing, limiting their ability to capture circuit-level functional context and making the learned representations sensitive to topology-specific patterns. Therefore, we propose CircuitGate, a function-aware AIG representation learning framework that advances from gate-level semantics to circuit-level functional modeling. CircuitGate explicitly encodes global primary-input (PI) support and models support-overlap-aware reconvergence between fanins, while incorporating logic-inspired Boolean constraints to encourage functionally consistent representations. We evaluate CircuitGate on the large-scale ForgeEDA benchmark and further validate it on the EPFL and ITC'99 benchmarks. Across equivalent-gate identification and signal-probability prediction tasks, CircuitGate consistently outperforms existing methods, achieving up to 21.7% and 14.2% reductions in MAE, respectively. Under direct ForgeEDA-to-OpenABC transfer without fine-tuning, CircuitGate also achieves the best equivalent-gate identification performance, demonstrating strong cross-dataset generalization. These results demonstrate the effectiveness of modeling circuit-level functional dependencies beyond local topology.

---


### 144. [A Framework for the Systematic Review of ML Assets in AI Registries](https://arxiv.org/abs/2610.09551)

**<font color=#1a73e8>作者：</font>** Alexandra González, Quim Motger, Xavier Franch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Background: Modern software systems increasingly rely on Machine Learning (ML) assets (i.e., pre-trained models, datasets, benchmarks) for building, evaluating, and integrating ML-based systems. However, current exploration, selection and reuse practices of ML assets are not supported by systematic retrieval methodologies comparable to those used in traditional evidence synthesis. Consequently, in practice, ML asset selection is often presented as a settled design decision, supported by informal justification rather than a traceable, evidence-based, and updatable selection process. Aims: This paper explores how systematic review methods can support ML asset retrieval. In doing so, we aim to make their selection transparent and reproducible, grounded in explicit evidence, and ultimately better suited to its intended use. Method: We analyze established systematic review practices from scientific literature and adapt their phases (i.e., planning, conducting, and documenting) to Artificial Intelligence (AI) registries, treating ML assets as first-class units of analysis. The resulting framework integrates registry-aware search strategies, cross-registry schema alignment, and dependency-driven ML asset exploration. Results: We conceptualize ML asset retrieval as a systematic and reproducible process rather than an ad hoc activity, and propose a framework for structured ML asset discovery. \textbf{Conclusions:} This work illustrates how systematic review principles can be extended beyond scientific literature to support evidence synthesis over evolving AI registries.

---


### 145. [UniCSI Towards a Universal Wi-Fi CSI Encoder for Ubiquitous Human Sensing](https://arxiv.org/abs/2610.09559)

**<font color=#1a73e8>作者：</font>** Daniel Eckhoff, Hua Kang, Zhitang Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wi-Fi sensing promises to turn the everyday wireless signals that already surround us into ubiquitous sensors for human sensing. However, a fundamental obstacle is that CSI is acquired under diverse device-specific configurations, including different subcarrier counts, bandwidths, and carrier bands. Consequently, the resulting CSI tensors vary in both spectral resolution and tensor shape, making heterogeneous modeling challenging. Standard architectures struggle with such heterogeneity, forcing lossy pre-processing which compromises the underlying signal. To bridge this gap, we present UniCSI, a unified foundation architecture that directly operates on heterogeneous CSI while preserving the integrity of the native waveform. UniCSI hinges on two core innovations: (1) a physics-informed RF tokenizer that encodes each frequency channel based on its fractional position within the physical spectrum rather than rigid array indices. It preserves intrinsic spectral coherence and enables seamless, frequency resolution-agnostic processing across arbitrary sensing configurations. (2) a spectral aggregator that distills variable-length channel sequences into a fixed-size spectral signature, effectively decoupling the feature dimensionality from the physical subcarrier spacing. Extensive evaluations on a large-scale corpus of 25 heterogeneous public datasets, spanning 14 to 2048 subcarriers, 20 to 160 MHz bandwidth, and the 2.4 and 5 GHz bands, demonstrate that native heterogeneous ingestion substantially improves cross-domain transfer under both supervised and self-supervised training schemes, particularly in regimes where fixed-grid architectures fail to generalize.

---


### 146. [Online Resource Allocation with an Endogenous Markov State: Fewer LP Solves Earn More](https://arxiv.org/abs/2610.09577)

**<font color=#1a73e8>作者：</font>** Zhaohua Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study finite-horizon online resource allocation with i.i.d. requests and an endogenous Markov state on a finite state space: each action affects the transition of the state that governs future rewards and resource consumption. In this problem, a transient fluid LP benchmark upper bounds the expected reward of every nonanticipating policy, while a stationary LP supplies randomized state-dependent controls. We assume that the stationary LP has a unique optimum and identify primal nondegeneracy and irreducibility of the optimal induced kernel as important regularity conditions in this framework. With a known request prior, we show that, under nondegeneracy and irreducibility, both frequent and infrequent re-solving attain $O(1)$ regret. However, under a degenerate optimum, irreducibility yields the sharp worst-case $\Theta(\sqrt{T})$ rate for infrequent re-solving, while frequent re-solving can incur $\Omega(T)$ regret. Thus, more frequent optimization can perform asymptotically worse. With an unknown request prior, we develop a three-phase U-shaped infrequent re-solving policy that coordinates learning and inventory correction with $O(\log\log T)$ LP solves. When the optimal induced kernel is irreducible and the algorithm is given the optimal target state class and a constant-cost entrance policy, it attains $O(1)$ regret under nondegeneracy and $O(\sqrt{T})$ regret under degeneracy. Without the target-class information, linear minimax regret is unavoidable. Numerical experiments further illustrate the instability of round-by-round re-solving relative to epoch-wise infrequent re-solving, show that thresholding greatly mitigates its loss, and find that infrequent schemes remain dominant under both known and estimated priors.

---


### 147. [Gradient-Based Trajectory Optimisation over Continuous Poses for Sparse-View Cone-Beam CT](https://arxiv.org/abs/2610.09579)

**<font color=#1a73e8>作者：</font>** Linda-Sophie Schneider, Simon Wittl, Gabriel Herl 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Trajectory optimisation for cone-beam computed tomography (CT) determines which information sparse-view scans acquire. Fixed candidate pools prevent off-grid refinement and require new object-specific precomputation for each acquisition manifold. We make every source pose an individual continuous variable and move all poses jointly by gradient ascent on the scanner's kinematic manifold. The objective combines soft-Tuy plane coverage, continuous View Covariance Loss, and an analytic attenuation-aware ray-bundle penalty. The same optimiser handles circular, limited C-arm, two-axis, and freesphere parametrisations. On a Defrise flange, continuous selection recovers laminar defects invisible to a circular orbit, matches discrete swap search on the free sphere at the sparser budget, and leads at the denser one, with the same objective evaluated in every arm. A moderate elevation band already recovers most of the free-sphere gain at the defects, so the same optimiser transfers to bounded scanner envelopes. Photon noise preserves the ordering on the flange and compresses it on a dense fuel nozzle. Sparseprescan planning benefits from matching prescan and planned acquisition manifolds. Selection takes seconds rather than minutes without an object-specific reconstruction basis. Prescan-planned poses were executed on a robot CT bench and reconstructed in a common frame, demonstrating feasibility but no consistent metric gain over uniform band sampling. Continuous pose optimisation incorporates attenuation and scanner constraints directly into sparse-view acquisition design.

---


### 148. [STORK: Spatio-Temporal Observation of uterine contRactions via neural networKs](https://arxiv.org/abs/2610.09598)

**<font color=#1a73e8>作者：</font>** Melissa Schween, Tristan Gottwald, Jordina Aviles Verdera 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Uterine contractions in fetal MRI are typically identified manually and discarded, limiting insights into contraction dynamics. We formalize Uterine Contractile Activity Detection (UCAD) as a weakly-supervised learning problem and introduce STORK, a multi-instance learning model trained on dynamic MRI series using only coarse, series-level labels. STORK factorizes 3D spatio-temporal convolutions into parallel branches across temporal hyperplanes to capture coherent tissue motion without the cost of full 4D convolutions. Per-frame embeddings, combining intensity and Demons-estimated displacement fields, are aggregated by a linear mean-pooling head. This ensures that frame-level contraction scores can be recovered post-hoc without frame-level training supervision. Evaluated on around 700 multi-vendor dynamic fetal MRI series, STORK achieves a series-level AUROC of 95.0% and AUPRC of 94.6%, substantially outperforming 3D ResNet and ConvNeXt baselines. Grad-CAM analysis suggests that the model draws on predictive features extending beyond the placenta into the uterine tissue, offering an automated tool for richer phenotyping of uterine behavior.

---


### 149. [Decoupled Optimization for Teacher-Student Semi-Supervised Learning via a Pioneer Student](https://arxiv.org/abs/2610.09609)

**<font color=#1a73e8>作者：</font>** Haorong Han, Jidong Yuan, Chixuan Wei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semi-supervised learning (SSL) relies on two core mechanisms: self-training under the Teacher-Student (T-S) framework and joint optimization of labeled and unlabeled losses. Despite their effectiveness, we find both mechanisms introduce distinct optimization pathologies. First, parameter coupling enforces strict synchronization between teacher and student, where strong regularization on the student degrades the teacher's fitting ability, thereby limiting the permissible generalization intensity. Second, the imbalance in gradient update consistency between labeled and unlabeled losses drives the shared parameters to prematurely converge to labeled-dominated local minima, creating a bottleneck for global optimization. To address both issues, we propose the Pioneer Student (PiS), an auxiliary branch that operates in an independent parameter space and periodically transfers accumulated knowledge back to the T-S model. Extensive experiments show that PiS is a universal plug-and-play module that consistently improves mainstream SSL methods.

---


### 150. [Sequential Pretraining Favors Large Models](https://arxiv.org/abs/2610.09611)

**<font color=#1a73e8>作者：</font>** Mohnish Harwani, Yujia Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large neural networks often acquire capabilities that small models fail to learn. Does this stem from large models learning more representative features, or from being more robust to unaccounted-for adverse effects introduced during training? We define and quantify one such adverse effect, primacy bias, as the extent to which exposure to early data distributions impairs later learning. We show that small models can allocate learning capacity inefficiently toward early distributions, whereas sufficiently overparameterized models are robust to this effect. This inefficiency is particularly consequential in pretraining, where foundation models often encounter heterogeneous data distributions sequentially rather than jointly. As a result, small foundation models can struggle to learn distributions encountered late in training, which is particularly harmful when later data emphasizes desirable capabilities such as code, mathematics, and reasoning. Motivated by these findings, we introduce Exposure Therapy (ET), a simple regularization that promotes more efficient allocation of learning capacity during sequential pretraining. We demonstrate that ET improves foundation models' performance on late data distributions as well as overall capability in models up to the billion-parameter scale. Overall, our results suggest that some benefits of large foundation models may arise from greater robustness to adverse training effects, rather than from learning more representative features, and that improved training algorithms can recover some of these advantages in smaller models.

---


> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-324](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
