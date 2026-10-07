# 📦 其他研究 | 2026年10月08日

> 本类共 **335** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-335](./part-07.md)

---

### 251. [Contextual Chain: Lightweight Continuity Authentication for Intermittently Connected Devices](https://arxiv.org/abs/2610.08262)

**<font color=#1a73e8>作者：</font>** Song-Ju Kim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Can authentication make memory, rather than computational hardness, the attacker's bottleneck? Contextual Chain is a lightweight continuity protocol for intermittently connected devices that share evolving physical or operational context. An honest device follows one realized history, updating a compact accumulator and fixed hash-based readiness lanes; outages cause pause or bounded rollback, not branch search. After the epoch is frozen, a fresh challenge selects one lane under a short deadline. An outsider that missed context may therefore need to prepare for many mature histories before learning which one will be tested. In the standard random-oracle model, a causal counting theorem lower-bounds the deadline-accessible retained state required for a target success probability against arbitrary nonlinear preselection encoding and adaptive post-selection queries, accounting for sequential depth, candidate queries, and cross-target protected information obtained online. Honest readiness memory remains fixed and independent of the number of plausible histories. Contextual Chain thus converts shared-experience uncertainty into a tunable preparation requirement without transferring combinatorial complexity to lightweight devices.

---


### 252. [Reinforcement Learning with Segment Reward Feedback under Linear Function Approximation](https://arxiv.org/abs/2610.08271)

**<font color=#1a73e8>作者：</font>** Fengxu Liu, Siwei Wang, Gal Dalal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical reinforcement learning (RL) assumes that a reward is observed for every visited state-action pair. However, in real-world applications such as autonomous driving, such fine-grained feedback can be costly or difficult to collect, whereas trajectory-level feedback may be too sparse for efficient learning. To provide a general feedback model bridging these two extremes and handle large state spaces, we study RL with segment reward feedback under linear function approximation. Our work answers how the granularity of segment feedback and the choice of segmentation influence learning. For equal-length segments with known transitions, we design algorithms $\bitssegd$ and $\edlinucbsegd$ for binary and sum feedback types, respectively. They adopt posterior sampling with planning to achieve computational efficiency and the E-optimal experimental design to attain near-optimality. Nearly matching lower bounds are established. For equal-length segments with unknown transitions, we develop a unified $\seglsvits$ framework with two instantiations for binary and sum feedback, which carefully integrates the posterior estimated reward parameters into least-squares value iteration. These results reveal a fundamental insight: under binary feedback, increasing the number of segments significantly reduces the regret through an exponential factor, while surprisingly, under sum feedback, the granularity of segments does not affect learning much. Finally, to investigate whether segmenting according to state-action features can further expedite learning, we design an algorithm $\uneqsegbitsd$ that allows arbitrary segmentations. The resulting regret bound shows that under the usual elliptical potential analysis, the influence of state-action features on the regret appears only through logarithmic factors, and equal segmentation achieves the best performance.

---


### 253. [Performative Prediction with Selective Labels](https://arxiv.org/abs/2610.08272)

**<font color=#1a73e8>作者：</font>** Giovani Valdrighi, Isabel Valera, Marcos Medeiros Raimundo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many social applications of machine learning exhibit performative effects: population behavior changes in response to deployed models. Performative prediction studies this interaction through a distribution map that relates each model to the population distribution it induces. One of the main results in this framework showed that repeated risk minimization (RRM), which updates models by retraining on the most recent data, can converge to a stable model that minimizes risk on its own induced distribution. However, existing analyses typically assume access to the complete distributions of features and labels after model deployment, ignoring the possibility of selective labels: observing labels only for the accepted subset of the population. In this work, we formalize performative prediction with selective labels and show that retraining only on observed data can misguide the retraining procedure and undermine the guarantees of convergence to a stable solution. We then propose a worst-case objective based on knowledge of a confidence interval on the probability of a positive label. Applying RRM to this objective permits us to remain within a bounded distance to the true stable point. Under a sensitivity assumption on the conditional label distribution, we further show how previously accepted data can tighten these confidence intervals over time. Experiments in a lending application with fairness regularization show that our robust optimization approach closely matches the performance of RRM with complete label access.

---


### 254. [Whose Face Is It Anyway? A Multi-Model Audit of Facial Affect Recognition on Children, and Why the Gap Is the Head, Not the Features](https://arxiv.org/abs/2610.08279)

**<font color=#1a73e8>作者：</font>** Tobias Hallmen, Robin-Nico Kampa, Elisabeth André  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial affect models are trained almost entirely on adults, yet are increasingly applied to children in education, health, and developmental research. We present a controlled, multi-model audit of five AffectNet-pretrained expression models (EmoNet, EmotiEffLib, DDAMFN++, OpenFace 3.0, LibreFace) on children, across four child image datasets, the AffectNet-8 validation set, and two spontaneous child video datasets, through one shared harness. Three findings emerge. First, the child gap is model-agnostic: every architecture degrades from posed to naturalistic faces and shares the fear$\rightarrow$surprise confusion. Second, it is concentrated and corroborated across all five models: open-mouth faces (read as surprise, correlating with the AU26 jaw drop) and South-Asian children degrade systematically, with a smaller averted-gaze penalty, while closed-mouth faces, White and Black children, and direct gaze do not; the bias tracks expression morphology and specific populations, not skin tone. Third, the gap is diagnosable: a linear probe on frozen features reaches 0.75-0.91 on unseen children versus 0.48-0.66 zero-shot, so it lies largely in the classifier head, not the representation, whereas dimensional valence/arousal regression degrades sharply under domain shift. Building on this, recalibrating only the head on a little target data recovers $+0.13$ to $+0.28$ on the two largest child sets across all five models at negligible adult cost, though the gain is in-distribution and does not transfer across child collections. We will release the harness, per-sample predictions, and analysis code; the child face data stays license-locked and is never redistributed.

---


### 255. [Event Detection in Table Tennis Videos using 2D Keypoints](https://arxiv.org/abs/2610.08286)

**<font color=#1a73e8>作者：</font>** Rainer Lienhart, Daniel Kienzle, Shin'ichi Satoh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper addresses the challenge of automatic, frame-accurate event detection in table tennis videos. Current methods for estimating 3d ball trajectories and ball spin typically require that key events, such as ball-racket contacts, have already been identified in advance. This requirement makes it difficult to apply these methods to longer, unedited video recordings. To overcome this limitation, we propose EventNet, a two-stage pipeline to detect key events: (1) 2d keypoints are extracted of the upper-body poses for both players, table corners and ball center. A small keypoint transformer combines them into a compact representation that is robust to changes in viewpoint, lighting, and background clutter. (2) The temporal sequences of these frame-based representations are processed by a transformer encoder that predicts two time-to-event values for each frame, indicating how close the current frame is to the next and previous ball-racket contact. One novelty is a new, temporal cosine-like target signal. Furthermore, we introduce viewpoint augmentation via 3D reprojection and frame-rate augmentation to improve robustness and generalization. Our extensive ablation study gives deeper insights into the importance of various architectural and training aspects. Experimental results show that the proposed approach achieves an F1 score of 91.16% and a mean frame deviation between ground truth and predicted frame of 0.42 on the Latte-MV dataset and 73.08% / 1.16 on the challenging TTHQ dataset. Overall, our work demonstrates that 2d keypoint-based temporal modeling with our EventNet architecture is a promising and practical approach for automatic event detection in table tennis videos.

---


### 256. [Scalable extraction and visualization of multi-attribute logical and functional dependencies in tabular data](https://arxiv.org/abs/2610.08287)

**<font color=#1a73e8>作者：</font>** Chaithra Umesh, Arvind Lomrore, Neethu D 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding the structural relationships among attributes in tabular data is fundamental to machine learning and pattern recognition. While functional dependency (FD) discovery has been extensively studied, scalable discovery of logical dependencies (LDs), particularly as the number of attributes and dependency order increase, remains underexplored. These dependencies capture non-deterministic, condition-specific relationships among pairwise or multiple attributes. Furthermore, existing approaches do not provide a unified framework for extracting multi-attribute LDs and FDs. To address these limitations, we propose LDTool and HLDTool for extracting and visualizing multi-attribute LDs and FDs from tabular data. LDTool extends dependency discovery beyond pairwise relationships, while HLDTool enables scalable extraction through hypergraph-guided search-space reduction. Experiments on three simulated and eleven real-world datasets demonstrate that the proposed framework extracts meaningful LDs and FDs while improving scalability. LDTool recovers the same FDs as existing FD discovery methods with lower runtime in high-dimensional feature spaces, whereas HLDTool enables dependency discovery in datasets with hundreds of features. The proposed framework provides interpretable visualizations of dependency structures and supports applications in exploratory data analysis and the quantitative evaluation of synthetic tabular data.

---


### 257. [OxiGen: Oxidation-State-Aware Crystal Generation](https://arxiv.org/abs/2610.08296)

**<font color=#1a73e8>作者：</font>** Dylan John, Kim E. Jelfs, Alex M. Ganose 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models have the potential to accelerate inorganic materials discovery by enabling inverse design, but generating experimentally realisable crystals remains challenging. Oxidation states are widely used to assess the compositional validity of crystals and guide inorganic materials discovery. While existing generative models for crystals can generate materials with charge-neutral oxidation-state assignments, they poorly reproduce the distributions of oxidation states observed in synthesised materials. To address this limitation, we propose OxiGen, an oxidation-state-aware crystal diffusion model that explicitly represents oxidation states during generation. OxiGen enforces global charge neutrality by construction using a structured output layer with exact inference over a finite-state automaton. Empirically, OxiGen substantially improves oxidation-state fidelity, generates the highest rate of stable, unique, and novel crystals among evaluated methods, and maintains high compositional validity even under property conditioning.

---


### 258. [Zeppelin: Client-Side BFV Encryption and Decryption for Helium-Powered Microcontrollers](https://arxiv.org/abs/2610.08301)

**<font color=#1a73e8>作者：</font>** Muhammad Saif ul Islam, Karar Haider, Manaal Malik 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The growth of the Internet of Things (IoT) has raised concerns over the privacy of data collected by resource-constrained sensing devices. Homomorphic encryption (HE) addresses this by letting a device encrypt its data once and an untrusted cloud server compute on the ciphertext without seeing the values. In practice, HE's memory and computational cost have kept it out of reach of microcontroller-class devices. Prior work, SEAL-Embedded, made this feasible using CKKS, but left three gaps: its arithmetic is entirely scalar, even on hardware with a vector instruction set; it never decrypts on the device, so the client cannot consume a result; and it does not explore BFV, whose encoding uses only integer arithmetic and decrypts exactly. We present Zeppelin, the first HE library to use an embedded vector instruction set, the first to support both encryption and decryption on an embedded device, and the first BFV implementation on MCU-class hardware. Zeppelin vectorizes the number-theoretic transform, HE's main bottleneck, for ARM's Helium extension, and includes a decryption procedure that avoids large-integer arithmetic and timing leakage of the secret key. A server-side adapter converts Zeppelin's ciphertexts into a format compatible with Microsoft SEAL, so the device handles encryption and decryption while the server performs all homomorphic computation. On an STM32N6 MCU with an ARM Cortex-M55, Zeppelin encodes and encrypts 4096 packed values in 4.76 ms (seeded symmetric, 128-bit security per the HE standard) and decrypts and decodes the result in 5.38 ms, using under 500 KB of RAM, with the vectorized NTT engine ${\sim}2.7\times$ faster than an equivalent scalar implementation on the same core.

---


### 259. [Hugging Suit: Pneumatically-Actuated System Design for Remote Haptic Experiences](https://arxiv.org/abs/2610.08305)

**<font color=#1a73e8>作者：</font>** Russian, Luke Hespanhol, Marius Hoggenmueller 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The COVID-19 pandemic emphasised the importance of remote emotional communication and highlighted a gap in existing technologies that lack haptic channels. While video calls maintain visual and auditory presence, they cannot convey the emotional depth of physical contact, especially hugging, a universally recognised form of intimacy and support. To explore this challenge, we developed the Hugging Suit, a pneumatically-actuated wearable system that enables users to simulate and receive remote hugs in real time. Unlike prior haptic systems that focus solely on tactile sensation, our approach integrates both technical and experiential considerations. The system integrates a programmable Air Actuator Matrix (AAM), a portable high-pressure pneumatic unit, and a fabric-based pressure sensor layer, enabling precise, wearable haptic feedback while remaining lightweight and mobile. Guided by a Research through Design (RtD) methodology, we iteratively refined the prototype to improve tactile resolution, overall usability, and user comfort, while introducing modular components to support flexible and scalable haptic configurations. In parallel, we explored how specific contextual factors, such as lighting, privacy, and the visibility of the remote partner, might shape the emotional and perceptual experience of receiving a remote hug. Preliminary feedback suggests that low-lit, private spaces, especially when users could also see their remote partner via video, improved emotional engagement and comfort during mediated haptic experiences. Our low-cost, maker-space-friendly approach contributes to affective haptics applications in long-distance relationships, emotional regulation, and remote therapeutic support.

---


### 260. [Catastrophic Forgetting in Sequential Thermal Anti-UAV Detection: The Role of Scale-Conditioned Gradient Imbalance](https://arxiv.org/abs/2610.08315)

**<font color=#1a73e8>作者：</font>** Khac Duc Giang Nguyen, Seyed Sahand Mohammadi Ziabari, Ali Mohammed Mansoor Alsahag  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Counter-UAV systems based on thermal infrared detection must stay accurate as operational datasets evolve, yet sequential fine-tuning causes catastrophic forgetting of prior tasks, a problem that remains insufficiently characterized in this domain. This continual-learning study measures the stability-plasticity trade-off in YOLOMG, a YOLOv5-based detector run as a single thermal-infrared stream with the motion channel disabled, trained sequentially across three anti-UAV benchmarks of rising scale difficulty: Anti-UAV-RGBT, Anti-UAV410, and CST Anti-UAV. Naive fine-tuning on CST yields a Forgetting Measure of -0.605 against the Stage 1 ceiling, corresponding to a 90% capability loss, with -0.572 occurring in Stage 3 alone. In contrast, knowledge distillation from a frozen teacher is associated with FM = -0.033 +/- 0.004 across three seeds, corresponding to 95% retention. Because no Stage 2 no-KD control is included, this result establishes retention under KD training rather than a causal KD effect. Per-stratum analysis shows large-target detection collapsing to near zero within the first epoch, despite an inter-stage cosine similarity of 0.987 over the gradient-updated weights, pointing to scale-conditioned gradient imbalance, rather than weight drift, as a candidate mechanism. Scale-Stratified Herding (SSH), a 300-exemplar buffer balanced across four UAV size strata, roughly halves the forgetting (FM = -0.605 to -0.311) and keeps large-target detection non-zero. An ablation attributes the gain primarily to scale stratification rather than herding: random-stratified replay performs at least as well (FM = -0.221 versus -0.311 for SSH). These replay results are single-seed and should therefore be treated as preliminary.

---


### 261. [MARCO: The Radioactive Watermark for Protein Generative Models](https://arxiv.org/abs/2610.08316)

**<font color=#1a73e8>作者：</font>** Huajie Chen, Xin Guo, Yuchen Shi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Protein Generative Models (PGMs) have revolutionized structural biology by enabling the design of complex 3D protein structures from sequence data. However, this breakthrough introduces a dual-use challenge, exposing high-value PGMs to economic risks like unauthorized model extraction and biosecurity threats such as biohazard synthesis. To mitigate these threats, we propose \textbf{MARCO} (\textsc{COnformation waterMARk}), the first radioactive watermarking framework specifically tailored for PGMs. MARCO establishes a Dual-Layer defense that simultaneously protects intellectual property and ensures the forensic traceability of potential biosecurity misuses. (i) To preserve efficiency, MARCO iteratively embeds watermarks during diffusion reverse denoising via an auxiliary encoder-decoder, allowing the original PGM parameters to remain frozen for broad compatibility. (ii) To preserve biophysical fidelity and maximize robustness, we employ specialized loss functions targeting $C_\alpha$-atom pairwise distances and torsion angles ($\psi, \phi$) within an adversarial training framework integrated with stochastic attack simulations. (iii) Crucially, MARCO exhibits ``radioactivity'' where the watermark automatically transfers to the outputs of any pirate models trained on the watermarked data, effectively countering model extraction attacks. Comprehensive experiments demonstrate that MARCO achieves superior fidelity and robustness while successfully validating watermark transferability.

---


### 262. [Structure-Aware Graph Abstention for Reliable Selective Forecasting](https://arxiv.org/abs/2610.08322)

**<font color=#1a73e8>作者：</font>** Jianxiang Xie, Belal Alsinglawi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selective forecasting abstains on high-risk test windows under a retained-coverage budget. Existing gates such as TEM (Brusokas et al., 2025) score each forecast as a whole; for multivariate outputs, trajectories can look plausible while violating dependencies among variables. We treat instance-level plausibility and relational consistency as distinct reliability axes and operationalize the latter via a learned sparse graph and a Dirichlet-style structural energy E_struct, trained with error-weighted graph regularization and score-error alignment. On seven long-horizon benchmarks and four backbones, structural gating often reduces selective MSE versus TEM at matched coverage, with the largest gains where cross-variable structure appears more informative in our benchmarks; gains are not universal, indicating a complementary abstention signal. Table 1 is a Protocol A ranking diagnostic (seed 2024); three-seed deployable Protocol B on an aligned subset is in Table 3 (full validation-to-test grids: Appendix A).

---


### 263. [An AI-Assisted Formalization of the Poincaré Conjecture](https://arxiv.org/abs/2610.08329)

**<font color=#1a73e8>作者：</font>** Zhiyuan Zhang, Axel Delaval, Leheng Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present an AI-assisted Lean 4 formalization of the Poincaré conjecture. The project began with limited reusable formal infrastructure for the geometric analysis behind the proof. To organize this work, we combined a proof blueprint prepared by mathematicians with explicit milestone statements. These milestones enabled parallel agent work and gave mathematicians clear points to locate blockers and provide effective mathematical guidance. Our analysis identifies the human interventions and organizational choices behind this workflow. The project provides a starting point toward reusable infrastructure for future formalization projects; such infrastructure, once developed, could eventually reduce the cost of verifying mathematical results in geometric analysis.

---


### 264. [Digital Twin-Driven Real2Sim2Real: Simulator-Conditioned Generation via Paired Driving-Scene Reconstruction](https://arxiv.org/abs/2610.08339)

**<font color=#1a73e8>作者：</font>** Hojun Lim, Hyeongseok Jeon, Donghyun Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-based 3D perception for autonomous driving relies heavily on large annotated datasets, and deploying such a system to a new target region typically requires data collection and annotation. Generative augmentation has been proposed to reduce this cost, but existing approaches face a fundamental trade-off: label-conditioned methods consume the very annotations they aim to replace, while simulator-conditioned methods offer free annotations but lack visual grounding to specific real environments. This work investigates the extent to which a digital-twin-driven Real2Sim2Real pipeline (DT-R2S2R) can substitute for target-region real data. By reconstructing recorded driving clips inside a georeferenced digital twin (DT-R2S), we condition a diffusion model on geometrically aligned simulator renderings, establishing a digital twin-grounded Sim2Real model (DT-S2R). As a result, DT-S2R synthesizes photorealistic driving images given low-cost yet georeferenced simulator data across both reconstructed and novel simulator scenes within digital-twin coverage. The efficacy of generated data is verified on diverse 3D detectors. DETR3D, especially, reports 93.18% of mAP obtained by a target-region real-data oracle, without employing target images for detector training. Furthermore, simple co-training with existing out-of-target real data outperforms the oracle. Thus, DT-R2S2R can substantially reduce the cost of manual on-site data collection and annotation in digital twin-available districts, providing a practical foundation for scaling 3D perception.

---


### 265. [PolarScale: A Physics-Grounded Benchmark for Radiometrically Consistent RGB-to-Stokes Estimation](https://arxiv.org/abs/2610.08346)

**<font color=#1a73e8>作者：</font>** Beibei Lin, Tingting Chen, Xin Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Polarization imaging provides physical cues beyond intensity imaging but typically requires specialized hardware. Recent methods infer polarization from RGB-like inputs, yet predict only normalized Stokes components or relative descriptors, from which the radiometric scale needed for full Stokes reconstruction has been divided out. We introduce PolarScale, a benchmark that makes this scale an explicit prediction and evaluation target. Built on existing trichromatic full-Stokes measurements, PolarScale takes the per-scene normalized total-intensity image $s_0$ (a scene-referred linear image, not a consumer sRGB photograph) and asks models to predict normalized Stokes components, AoLP/DoLP/DoCP, and a per-scene scale. Because the scale is divided out of the input, it is not physically identifiable; PolarScale therefore evaluates dataset-conditioned semantic scale estimation against a constant-scale control, together with angular, self-consistency, and physical-bound metrics. Across seven restoration-based and generative backbones and three prediction strategies, the strongest restoration models estimate the scale with 3.6-4.3% mean relative error versus 5.7% for the constant control and violate physical bounds on fewer than 0.25% of pixels, whereas two generative baselines collapse to a near-zero scale; explicit descriptor supervision improves descriptor accuracy (23.66 vs. 18.88 dB PSNR for MAE). Predicted full-Stokes representations improve diffuse/specular separation, material segmentation, and glare classification, although in diffuse/specular separation the learned scale performs only on par with the constant control.

---


### 266. [Uncertainty Quantification Is Indispensable for Reliable Connectome-Based Graph Learning: A Narrative Review and Case Study](https://arxiv.org/abs/2610.08353)

**<font color=#1a73e8>作者：</font>** Mansooreh Pakravan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While graph neural networks (GNNs) have shown substantial promise in connectome-based diagnostic classification, deterministic models inevitably suppress pipeline-induced noise and model ambiguities, yielding overconfident predictions. Although uncertainty quantification (UQ) is widely adopted in voxel-level segmentation, its role in connectomic graph learning remains largely unaddressed. This paper presents a comprehensive narrative review of UQ frameworks tailored to connectome graph learning alongside an empirical case study demonstrating the perils of uncalibrated predictions. We delineate sources of aleatoric and epistemic uncertainty across neuroimaging pipelines and review prominent UQ paradigms, from Bayesian approximations and ensemble methods to evidential learning and conformal prediction. In our case study, a temporal Graph Attention Network (GAT) trained on dynamic functional connectivity (dFC) matrices from the SUDMEX CONN dataset achieves 80.0% diagnostic accuracy (F1 = 0.794) for Cocaine Use Disorder. However, a post-hoc uncertainty audit via Monte Carlo dropout reveals severe overconfidence (ECE = 0.127), with misclassified subjects assigned prediction confidences up to 95%. This empirical divergence between discrimination and calibration underscores the confidence paradox in deep connectomics. Our findings establish that rigorous UQ, calibration, and selective prediction mechanisms are indispensable for deploying trustworthy graph-based biomarkers in clinical neuroscience.

---


### 267. [Sensor Geometry as a Flow-Matching Prior for Multi-Channel Brain Signals](https://arxiv.org/abs/2610.08355)

**<font color=#1a73e8>作者：</font>** Jaedong Hwang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow-matching models start from an isotropic Gaussian source, the standard choice when the correlation structure of the data is unknown in advance. For multi-channel brain recordings, however, part of this structure is known in advance. Electrodes sit at fixed positions on the head, and volume conduction through the skull and scalp makes nearby electrodes co-vary in a way that is shared across subjects. Existing EEG generative models nonetheless leave the network to learn this from scratch. We put this structure into the source instead. From the sensor coordinates alone, we build a k-nearest-neighbor graph and take a graph-Matérn function of its Laplacian as the source covariance, so the flow starts from spatially coherent patterns rather than channel-independent noise. The change adds no learned parameters, works with any coupling and any drift network, and uses the same three hyperparameters on every dataset. Across eight EEG datasets and four flow-matching methods, the graph-Matérn source lowers the spectral discrepancy between generated and real signals in the five clinical bands (PSD-KL) on most datasets. PSD-KL falls by 12% to 17% in geometric mean over datasets depending on the method and by up to 40% on PhysioNet-MI, the densest montage. We show that the improvement stems from the spatial eigenvectors of the local graph of sensor positions, since randomizing the eigenvectors while preserving the eigenvalue spectrum eliminates the gain. Furthermore, a prior fitted directly to the empirical data covariance performs worse than isotropic noise. The same construction applies unchanged to MEG, intracranial EEG with patient-specific grids, and a traffic-sensor network, lowering PSD-KL for every method on each. this https URL

---


### 268. [Test-Time Adaptation of Quantized ViTs via Single-Pass Quantizer-Aligned Recalibration](https://arxiv.org/abs/2610.08358)

**<font color=#1a73e8>作者：</font>** Hyeongheon Cha, Young D. Kwon, Sung-Ju Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-training quantization is a standard route to fitting vision transformers (ViTs) into edge compute and memory budgets, yet quantized models become especially brittle under distribution shift. Test-time adaptation (TTA) addresses such shifts without labels, but most existing approaches are poorly aligned with the constraints of quantized inference. Prevailing TTA methods recover accuracy through backpropagation, while backprop-free methods often still incur overhead from extra forward passes or parameter updates, and lightweight feature- or logit-level methods recover only part of the loss. Across these approaches, a quantization-specific failure mode that amplifies the drop is not directly targeted: under shift, activations occupy frozen quantizers' calibrated ranges differently, distorting their code distribution. We propose Quantizer-Aligned Recalibration (QuAR), a single-pass TTA method tailored to quantized ViTs that neither backpropagates nor updates any model parameters. QuAR recalibrates activations at the input to a frozen quantizer, mapping the test stream's running per-channel statistics back toward the source calibration. On ImageNet-C with ViT-B, QuAR achieves the highest mean accuracy among state-of-the-art backprop-free TTA methods at 3-, 4-, 6- and 8-bit weight/activation precision, outperforming the strongest baseline by 2.28 points at 8 bits and 4.00 at 3 bits, with 46% lower latency and a memory overhead of only 0.17 MB (0.01% of peak inference memory). Analysis and diagnostics trace the gain to a reduced per-channel mismatch at these quantizers, which restores the code distribution the baselines leave unchanged or distort further. A single fixed configuration remains ahead across continual streams, non-i.i.d. label shift, seven out-of-distribution suites, and three other backbones.

---


### 269. [Explainable Failure Prediction and Prevention in Maritime](https://arxiv.org/abs/2610.08363)

**<font color=#1a73e8>作者：</font>** Dionisis Kalogeropoulos, Georgia Sovatzidi, Panagiotis G. Kalozoumis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Maritime systems operate in highly dynamic environments where unexpected equipment failures can compromise safety, reliability, and operational efficiency. Recent advances in artificial intelligence (AI), machine learning, digital twins, and predictive maintenance enable proactive failure prediction and prevention. However, ensuring trustworthy and explainable decision-making remains a major challenge in safety-critical maritime applications. This chapter reviews key AI technologies required for explainable failure prediction and prevention in maritime systems and presents a conceptual architecture capable of supporting autonomous or human-in-the-loop corrective actions. This architecture integrates data acquisition, time-series forecasting, anomaly detection, risk assessment, decision-making, and explainable AI into a closed-loop framework. With reference to the architectural components, a review and discussion of relevant maritime studies is performed, outlining their methods, advantages, and limitations. Furthermore, it highlights current challenges, including uncertainty and robustness, model generalization, explainability, limited availability of maritime datasets, and operational deployment, and identifies future research directions toward trustworthy AI-assisted maritime decision-making.

---


### 270. [Evolutionary One-Step Generators: Fast and Diverse Sampling for Discrete Design](https://arxiv.org/abs/2610.08367)

**<font color=#1a73e8>作者：</font>** Marcus Vukojevic, Erik Nielsen, Veronica Lachi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Several discrete design tasks, such as molecular discovery, require diverse collections of useful candidates at low computational cost. High validity alone does not guarantee a useful candidate library: repeatedly generating the same valid structures leaves few distinct alternatives. Training for both feasibility and diversity is challenging because many relevant criteria can only be evaluated after hard decoding. To address this challenge, we propose EGO (Evolutionary Generators with One-step inference), a framework for training compact generators directly on discrete outputs. The method combines distribution matching with structural constraints and optional diversity or history-dependent rewards, using antithetic low-rank evolution strategies without requiring criterion-specific differentiable surrogates. Once trained, the generator produces the entire graph in a single neural-network evaluation. On molecular generation benchmarks, our compact generator achieves over $50\times$ the valid-and-unique yield per estimated dense operation compared to recent one-step flow-map baselines while retaining high chemical validity. In scaffold completion, EGO achieves an observed $44.3\times$ speedup over MoLeR in generation to SMILES and produces approximately $10\times$ as many filter-passing proposals within matched time budgets for generation and screening. Beyond chemistry, EGO produces $1.54\times$ as many distinct held-out elite architectures as relaxed gradient training on NAS-Bench-101. The low generation cost may enable real-time candidate generation across discrete design tasks, supporting interactive exploration of constrained design spaces and rapid construction of candidate sets for downstream evaluation.

---


### 271. [Accelerating the Development of PLGA In Situ Forming Depots Through AI-Driven Multi-Objective Optimization](https://arxiv.org/abs/2610.08368)

**<font color=#1a73e8>作者：</font>** Pauric Bannigan, Siddarth Chandrasekaran, Brigitte A. G. Lamers 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Developing long-acting injectable formulations requires the simultaneous optimization of drug loading, release kinetics, viscosity, injectability, stability and other objectives. To navigate this multidimensional space, Corbion and Intrepid combined Corbion's diverse PURASORB bioresorbable polymer library with Intrepid Labs' proprietary AI algorithm (ANDROMEDA 1) to develop in situ forming depots for a therapeutic peptide. Over approximately 15 weeks, 181 unique formulations spanning drug loadings of 6-12% w/w were prepared and characterized through broad design-space mapping and targeted multi-objective optimization. Four lead candidate formulations were identified at 6%, 9%, and 12% w/w drug loading. Each met the predefined viscosity and injectability criteria while providing distinct 30-day in vitro release profiles. The study evaluated polymers spanning a broad range of molecular weights, including commercially available PURASORB grades and new polymers under development by Corbion to expand its polymer toolbox. ANDROMEDA 1 identified that polymers with intermediate molecular weights provided a favorable balance between sustained release and solution viscosity. Together, these findings demonstrate how integrated polymer expertise and AI-driven optimization can rapidly identify differentiated formulation candidates, focus the development space, and establish a strong data-driven foundation for further optimization and in vivo evaluation.

---


### 272. [UniCounting: Instance-Aware Proposal Consolidation for Image-Query-Free Multi-Category Counting](https://arxiv.org/abs/2610.08379)

**<font color=#1a73e8>作者：</font>** Jinshi Liu, Pan Liu, Lei He 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual counting is commonly formulated as counting a single specified target, with a model receiving an image-specific exemplar, text query, or target category and returning a single count. We instead study fixed-vocabulary image-query-free multi-category counting. A global vocabulary is fixed for each run, and, given only an RGB image, the model predicts a complete category--count vector without being told which categories appear. We present UniCounting, which casts counting as instance-aware structural inference over an over-complete proposal set. Generic segmenters produce duplicate masks, partial views, and proposals from neighboring instances; semantic scores can name them but cannot determine which denote the same object. Frozen SAM~2.1 generates masks, while frozen DINOv2 and OpenCLIP provide relation and category features. A 3,267-parameter category-shared relation head predicts same-instance affinities from instance-mask-derived supervision. Sparse graph construction, representative selection, labeling, and background-margin admission then convert each admitted component into one count with replayable group evidence. Only the relation head is trained, without count or density-map targets. On COCO clean500, UniCounting obtains lower point-estimate vector $\ell_1$ error and absent-class false mass than calibrated OWLv2-All80, with comparable micro presence F1. Under a matched decoder, the learned relation reduces both errors relative to mask containment, mask IoU, CLIP, and DINO, while revealing a fragmentation--merge trade-off. We also report transfer diagnostics on OmniCount-sub, FSC-147, and CARPK.

---


### 273. [Decision-Focused Learning in MDPs: An Occupancy Measure Approach](https://arxiv.org/abs/2610.08384)

**<font color=#1a73e8>作者：</font>** Zihao Zhao, Ashwath K. Karunakaram, Ali Eshragh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we consider decision-focused learning (DFL) for a Markov decision process (MDP), where existing methods differentiate through the KKT conditions of the Bellman equation and require solving a linear system over all state-action pairs, limiting its scalability. We address this by reformulating the MDP as an occupancy measure-based linear program (LP), whose feasible region is induced by predicted dynamics, and we derive a closed-form gradient by identifying the active constraints in the feasible polyhedron via the pivoting algorithm. This occupancy measure-based LP layer raises two challenges: (1) LP's solution gradient is discontinuous when active constraints change, and (2) the LP backward cost still scales with the state size, which is costly for large or continuous state spaces. We address the challenges with an augmented Lagrangian surrogate and smooth the boundary jumps by random row sketching of the constraints, and a learnable soft state-aggregation layer and its function-approximation generalization that scales the LP to large finite and continuous-state MDPs. Across multiple tasks, our methods reach lower regret than KKT-based DFL and two-stage baselines with significantly lower computation cost. The source code for all experiments is available at this https URL.

---


### 274. [Living Dashboards: Automatically Self-Updating Visualization Dashboards](https://arxiv.org/abs/2610.08393)

**<font color=#1a73e8>作者：</font>** Mingyu An, Heyon Jeon, Sungbok Shin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visualization dashboards are widely used interactive tools, but a disconnect exists between the dynamic data they display and their static structure. End-users cannot modify the dashboard to answer new questions. We introduce Living Dashboards, whose views are born, wither, revive, and die in response to how they are used. Rather than requiring manual reconfiguration, a living dashboard observes interaction and natural-language queries to autonomously wither neglected views and revive those used again. More consequential decisions, such as adding or retiring views, are deferred to the user. We formalize the concept as a four-dimensional design space and implement it in Living Dashboard, a web-based prototype. We evaluate it in an exploratory between-subjects study (N = 12) against an AI-supported baseline on analytical tasks. Living Dashboard participants answered more tasks correctly, reported lower workload, and rated the system higher on usability, though the two conditions differed in more than adaptive behavior alone.

---


### 275. [Atom-JEPA: Joint-Embedding Predictive Architecture for 3D Atomistic Systems](https://arxiv.org/abs/2610.08400)

**<font color=#1a73e8>作者：</font>** Kasper Helverskov Petersen, Rasmus Hannibal Tirsgaard, François R J Cornet 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale self-supervised pretraining has reshaped modern machine learning, substantially advancing the ability of language and vision models to generalize across downstream tasks. While deep learning has driven considerable progress in modeling atomistic systems in recent years, self-supervised pretraining in this domain has not yet achieved comparable downstream generalization. To address this, we introduce Atom-JEPA, a self-supervised pretraining framework that learns latent representations from unlabeled 3D structures through complementary atom-level and substructure-level objectives inspired by joint-embedding predictive architectures. We pretrain Atom-JEPA on large-scale molecular and crystalline datasets and evaluate its transfer performance by fine-tuning on a diverse set of downstream property prediction tasks. Atom-JEPA achieves state-of-the-art performance on molecular ADMET and quantum-chemical property prediction tasks, and is highly competitive in predicting the physical properties of crystalline materials. These results demonstrate the potential of latent-space predictive pretraining to support broad downstream generalization from structural data alone. Code and pretrained model checkpoints are publicly available at this https URL

---


### 276. [Decoy and disclosure radii of invariant shape descriptors](https://arxiv.org/abs/2610.08410)

**<font color=#1a73e8>作者：</font>** Tanush Shaska, Lubjana Beshaj  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A recognizer that compares rotation-invariant descriptors sees a surface only up to the fiber of the descriptor. We measure this fiber by its radius in the orbit distance from the enrolled surface. A large radius admits decoys, that is, distant shapes that pass the matcher. A small radius discloses the enrolled shape to anyone who captures the stored value. For star-shaped surfaces truncated to spherical harmonics of degree at most $L$, with $n$ coefficients, a descriptor of generic rank $r$ has generic fibers of dimension $n-3-r$ modulo rotations. The standard pool of band powers, even bispectra, and three invariants of the degree-three band therefore admits decoy families of dimension $5$, $13$, $20$ at $L=4,6,8$. Its rank first reaches $n-3$ at $L=16$, and a mirror decoy remains at every $L$. The odd bispectra remove the mirror decoy generically for $L \geq 4$. Yet at fixed mean radius the same pool determines the enclosed volume exactly, and it does not determine whether a surface meets a clearance requirement. We certify two cases by exact and interval arithmetic. At $L=6$ a decoy matches all $32$ invariants to relative precision $2 \cdot 10^{-18}$ at orbit distance at least $0.87$ times the norm of the enrolled tuple. For the radar shape model of asteroid (101955) Bennu, the pool recovers the modeled volume, misses the handedness, and leaves the keep-out radius uncertain by more than $7 \, \mathrm{m}$.

---


### 277. [Ariadne's Thread of LipSync: Unraveling Forgeries via Inconsistency between Lip Motions and Head Poses](https://arxiv.org/abs/2610.08417)

**<font color=#1a73e8>作者：</font>** Tianyi She, Jiawei Liu, Weifeng Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in LipSync generation technology have led to the creation of highly realistic videos, posing severe societal risks. However, existing defense strategies struggle against LipSync forgeries, as advanced LipSync generation methods not only achieve better lip synchronization but also eliminate visual artifacts. An important reason is that they overlook an inherent biological coupling between lip movements and head poses in natural speech videos. In this paper, we propose LipDA, a novel framework for joint LipSync Detection and Attribution, which takes advantage of the inconsistency between head and lip. For detection, the framework learns to quantify this discrepancy by contrasting lip and pose features from authentic versus forged videos. For attribution, our method is designed to capture the unique temporal dynamics and audio-visual synchronization patterns that act as the fingerprint of models, enabling source tracing. We conduct extensive experiments on two challenging LipSync datasets as well as our own proposed large-scale and multi-generator dataset. LipDA achieves over 97\% AUC in detection and 97.5\% accuracy in model attribution, significantly outperforming existing methods. Code and the proposed LipSync-A dataset are available at this https URL.

---


### 278. [From the Drosophila Visual Connectome to General-Purpose Computer Vision](https://arxiv.org/abs/2610.08418)

**<font color=#1a73e8>作者：</font>** Zongyu Li, Akito Yamauchi, Huaizhi Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Biological connectomes encode structured solutions to visual computation that may provide reusable inductive biases for artificial vision. We develop ConnectomeX around FlyVision, a trainable architecture that preserves parallel ON/OFF processing, recurrent computation and population-level graph interaction while scaling model capacity across tasks. FlyVision reached 99.34% accuracy on MNIST with 80,608 parameters and 78.03% on CIFAR-10 with 81,408 parameters. On ImageNet-1K, FlyVision Base and Large reached 60.79% and 66.25% top-1 accuracy with 1.8 and 3.7 million parameters, while a Large local-k7 model with a learned low-frequency branch reached 66.53%, compared with 69.25% for ResNet18 with 11.7 million parameters. On a 22-class skin-disease benchmark, FlyVision Large achieved 63.78% accuracy and 95.28% macro-AUROC with 2.99 million parameters. In four-class chest radiography, ImageNet-pretrained FlyVision Base and Large reached 92.60% and 92.76% accuracy with 1.33 and 2.97 million parameters, compared with 91.56% for ImageNet-pretrained ResNet18 with 11.18 million. BrainAGE extends FlyVision to volumetric T1-weighted MRI by applying a shared ImageNet-pretrained FlyVision Large encoder to 24 sagittal, coronal and axial slices per scan and combining slice-level age estimates by confidence-modulated Gaussian voting. On 433 held-out scans, three-axis fusion achieved a mean absolute error of 5.98 years and R^2 = 0.868. Across the 224x224 classification tasks, the best FlyVision configuration remained within three percentage points of ResNet18 on ImageNet-1K and skin-disease classification and exceeded it on chest radiography with substantially fewer parameters. These results show that a conserved connectome-informed computation can scale from compact recognition to large-scale natural and biomedical vision.

---


### 279. [Deformable CT-US Registration via Anatomy-Aware Implicit Neural Representations](https://arxiv.org/abs/2610.08419)

**<font color=#1a73e8>作者：</font>** Agnieszka Lach, Magdalena Wysocki, Feng Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Slice-to-volume registration between ultrasound (US) and preoperative computed tomography (CT) imaging would enhance many minimally invasive interventions, for example by locating soft tissue structures intra-operatively that are discernible in CT. While optical tracking enables initial rigid registration, contact from the probe induces soft tissue deformations that inhibit accurate alignment. In this work, we introduce a deformable CT-ultrasound registration framework that incorporates anatomical priors derived from CT to improve registration under deformation. Rigid registration is first established using a robot-assisted optical tracking system, after which a deformable transformation is estimated using a sinusoidal implicit neural representation (SIREN) optimized per frame. Tissue stiffness is approximated from CT-based HU values and used as spatially varying regularization, suppressing deformation in rigid structures such as bone while allowing more flexibility in soft tissue. Two additional constraints capture the physics of probe contact: a contact-zone displacement prior that drives the displacement field to compress tissue below the probe face, and a fan-geometry regularization term based on beam direction and convex transducer field of view. Model parameters are optimized with a normalized gradient field (NGF). The proposed approach improves alignment over rigid initialisation by 17% and outperforms classical deformable baselines while maintaining near-zero topological folding.

---


### 280. [Symmetry-Aware Feature Learning: A Polynomial Separation for Multi-Index Models](https://arxiv.org/abs/2610.08420)

**<font color=#1a73e8>作者：</font>** Jivan Waber, Vanessa Piccolo, Yatin Dandi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We establish a polynomial sample complexity separation between symmetry-aware and symmetry-agnostic feature learning. We study growing-rank multi-index models with high-dimensional Gaussian covariates in $\mathbb{R}^d$ and $r=\Theta(d^\delta)$ teacher directions forming a cyclic symmetry orbit, where $0<\delta<1/2$. We compare three ways of exploiting this structure: architectural weight sharing, data augmentation over the full symmetry group, and learning without access to the symmetry. In particular, we analyze a symmetry-tied convolutional network, an untied network, and the same untied network trained with full-group data augmentation, using spherical online SGD with correlation loss. For a class of polynomial links with information exponent $p\ge3$, we prove matching sample complexity bounds up to logarithmic factors: the tied and augmented learners achieve weak directional recovery in $\widetilde{\Theta}(d^{p-1})$ samples, whereas the symmetry-agnostic learner requires $\widetilde{\Theta}(rd^{p-1})$. For the pure quadratic Hermite link, the same separation holds for weak recovery of the teacher subspace, with sample complexities $\widetilde{\Theta}(d)$ and $\widetilde{\Theta}(rd)$, respectively. Thus, full-group data augmentation matches the sample efficiency of architectural weight sharing, and both provide a polynomial advantage over training without symmetry. For $p\ge3$, the proof reveals a two-stage mechanism: fluctuations at initialization select one direction in the teacher orbit, after which localized growth amplifies its overlap to the weak recovery scale while competing overlaps remain near their initialization scale.

---


### 281. [HuC-VideoMAE: Human-Centric Video Masked Autoencoding from synthetic data](https://arxiv.org/abs/2610.08433)

**<font color=#1a73e8>作者：</font>** Ricardo Pizarro, Roberto Valle, José M. Buenaposada 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern action recognition models rely on video transformers pretrained on massive collections of web-crawled videos, such as Kinetics-700. However, the use of such data raises ethical concerns, as subjects' consent is typically not obtained. Recent high-quality synthetic video datasets generated from motion-capture data, such as BEDLAM2.0, offer a promising ethical alternative. In this work, we investigate self-supervised pretraining of video transformers on synthetic human-motion datasets. We first show that directly applying the standard VideoMAE masking strategy leads to substantially worse performance than pretraining on Kinetics. To address this limitation, we propose a human-centric masking scheme that leverages body keypoints and person bounding box regions. Our approach encourages the model to focus on the structure and dynamics of human motion during pretraining. Experiments on NTU RGB+D and Toyota-Smarthome demonstrate that our method significantly outperforms standard VideoMAE pretraining on synthetic data, closing 49% of the gap to Kinetics pretraining on NTU RGB+D cross-view-subject without using a single real frame during pretraining. To promote the use of ethical action recognition models, we will publicly release our pretrained models.

---


### 282. [Climbing the Design Ladder: Sequential Knowledge Distillation for Early-Stage Circuit Timing Prediction](https://arxiv.org/abs/2610.08457)

**<font color=#1a73e8>作者：</font>** Reza Moravej, Fahad Rahman Amik, Zhanguang Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Integrated circuit design involves multiple design stages: logic synthesis, floorplanning, placement, and routing, with each stage taking hours to weeks to complete. Discovering timing violations late in this flow forces costly iterations back to earlier stages, wasting computational resources and delaying product launches. While predicting post-routing timing from early-stage data could prevent these failures, existing machine learning approaches struggle with the massive abstraction gap between post-synthesis logical descriptions and post-routing physical layouts. We propose STEP-KD (Sequential Timing Evaluation via Progressive Knowledge Distillation), which leverages intermediate design stages as ``stepping stones'' for progressive knowledge transfer rather than attempting direct prediction. STEP-KD trains teacher models at the post-routing, post-placement, and post-floorplan stages, then sequentially distills their knowledge to a post-synthesis student model through representation alignment. Experiments on diverse circuits demonstrate that STEP-KD reduces timing prediction error compared to direct distillation and supervised baselines, and in most settings compared to the industry-standard Static Timing Analysis (STA) tool. STEP-KD reduces the weighted mean absolute percentage error of Total Negative Slack prediction to 19.78\%, compared with 74.84\% for STA. Our proposed method is step forward to identify timing problems earlier, avoiding expensive late-stage redesigns.

---


### 283. [Federated Bayesian Surveillance of Mechanical Thrombectomy Adverse Events: A Population Risk Layer for Surgical Digital Twins](https://arxiv.org/abs/2610.08464)

**<font color=#1a73e8>作者：</font>** Damini Rijhwani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Learned surgical simulators and world models can roll out plausible procedural futures, but they carry no grounded estimate of how often interventional devices actually harm patients. We propose treating population-scale adverse-event surveillance as a distinct belief layer of the surgical digital twin, and we evaluate a federated Bayesian protocol for learning it under formal privacy guarantees. Each site holds per-class Gamma-Poisson posteriors over adverse-event rates and exchanges only Rényi-differentially-private natural-parameter updates. We benchmark on the complete FDA MAUDE cohort for thrombus-retrieval catheters (product code NRY): 8,617 reports, of which 6,491 are classified by transparent keyword rules into five thrombectomy complication classes and partitioned across $K=8$ manufacturer sites. At a matched privacy budget of $(\\varepsilon \\approx 2.09, \\delta = 10^{-5})$, the conjugate protocol attains a held-out Poisson score of -5.78 per test event versus -26.58 for FedAvg with differential privacy. The non-private federated model also outperforms centralized pooling (+3.19 vs +2.93), evidence that manufacturer-specific complication profiles are real and that federation preserves them. Because MAUDE lacks procedure denominators, outputs are relative rate orderings rather than absolute risks, and we report all privacy-utility operating points.

---


### 284. [The Now and Then: Integrating Current and Historical Data in Small Multiple Time Series Visualization](https://arxiv.org/abs/2610.08473)

**<font color=#1a73e8>作者：</font>** Sydney K. Purdue, Enrico Bertini, Melanie Tory  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Small multiple time series visualizations are often used for real-time data monitoring tasks in high-impact domains such as healthcare and manufacturing. Effective design is critical because users rely on these visualizations to monitor data from many entities, such as patients or machines, often while distracted. Users may need to rapidly appraise current values for each entity, monitoring for those that go outside an acceptable range, while also watching temporal trends. However, no design guidelines currently exist for visually emphasizing current values in historical time series represented by small multiples. Via an iterative design process informed by a review of related literature and theory on visual channels and emphasis, we present a design space for glanceable time series small multiple displays. We evaluate this space through two online empirical studies, testing against non-threshold and threshold rapid appraisal tasks. Our results provide insights into merging current value and historical data visualizations for rapid appraisal tasks in time series monitoring. For non-threshold tasks, we found that size encodings on the current value, spatially integrated into the line chart, may provide a good compromise, with 28% response time improvement for tasks involving finding large current values and minimal interference with trend lookup tasks. More generally, integrated designs outperformed separated designs (in which the current value representation is spatially separated from the historical trend line). For threshold tasks, color threshold encodings significantly outperformed shaded band encodings.
All supplemental materials are available at this https URL.

---


### 285. [Learning PDE solution operators with variable initial conditions via Latent Dynamics Networks](https://arxiv.org/abs/2610.08475)

**<font color=#1a73e8>作者：</font>** Stefano Maria Pizzamiglio, Stefano Pagani, Francesco Regazzoni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many-query scenarios, data-driven surrogate models provide an efficient alternative to high-fidelity solvers for simulating physical systems governed by Partial Differential Equations (PDEs). In this context, the Latent Dynamics Network (LDNet) has recently demonstrated remarkable performance in predicting the response of spatio-temporal systems, combining Neural Ordinary Differential Equations with nonlinear dimensionality reduction. However, the original formulation assumes a fixed initial condition, limiting its applicability to many real-world applications where a system evolves from varying starting states. In this work, we overcome this limitation while keeping the end-to-end training procedure of the original LDNet and its encoder-free nature, which preserves its intrinsic independence from spatial resolution and grid topology. We infer the initial latent state directly from a small set of early-time observations, treating latent-state initialization as an adaptation problem, and investigate two strategies: an auto-decoding formulation and a meta-learning approach in which the initial latent state acts as a task-specific context variable. We demonstrate the accuracy of the proposed methods across diverse physical phenomena, spanning advection-diffusion, fluid dynamics, and solid mechanics. Meta-learning markedly accelerates latent-state inference and induces smoother, better-conditioned optimization landscapes, and spontaneously organizes the latent space into a structured representation that reflects physically meaningful features of the underlying dynamics. The coordinate-based decoder enables training from spatially subsampled data while recovering high-resolution solution fields at inference. The resulting approach provides an efficient and resolution-independent surrogate modeling framework for many-query simulations of time-dependent PDEs with varying initial conditions.

---


### 286. [MetaLearnNCA: Few-Shot Offline Meta-Learning via Interacting Neural Cellular Automata](https://arxiv.org/abs/2610.08479)

**<font color=#1a73e8>作者：</font>** Etienne Guichard, Stefano Nichele  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Few-shot meta-learning traditionally formulates task adaptation either as analytical gradient descent through unrolled computational graphs or as metric-based distance comparisons over flattened 1D fea- ture vectors, which either incur costly test-time backpropagation or discard native 2D spatial geometry. In this work, we propose METALEARNNCA, a decentralized framework that achieves few-shot adapta- tion through the dynamical interaction of coupled Neural Cellular Automata (NCAs) without computing analytical gradients during inference. MetaLearnNCA decomposes task adaptation into an Active- NCA, which executes task inference conditioned on a continuous 2D spatial memory grid termed the spatial program, and a learned Meta-NCA, which acts as a decentralized cellular optimizer by diffusing spatial error residuals across local neighborhoods to dynamically update this program. METALEARN- NCA is competitive against canonical meta-learners in-distribution (96.12% on Omniglot) with Out-Of- Distribution transfer gains on MNIST, KMNIST, and Fashion-MNIST transfer across 10 independent testing seeds across 1-, 5-, and 10-shot regimes (e.g., surpassing Prototypical Networks by +10.54% on 10-shot MNIST and a +3.87% gain on 10-shot Fashion-MNIST over FOMAML). Our results establish that robust, gradient-free learning-to-learn can emerge from decentralized cellular dynamics on non-von Neumann substrates.

---


### 287. [Cylindrical Geodesic Flow Matching for Quasiperiodic Physiological Signal Transformation](https://arxiv.org/abs/2610.08510)

**<font color=#1a73e8>作者：</font>** Onur Selim Kilic, Afra Nawar, Cem Okan Yaldiz 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Paired translation between quasiperiodic physiological waveforms (i.e., recovering a target oscillatory signal from the source) is central to the interpretation of cardiovascular signals derived from wearables placed at different body locations. This source-to-target mapping in these problems carries inherent geometric structure: the phase wraps around the cycle and must be treated as a circular variable, the amplitude remains strictly positive, and the beat-to-beat alignment can drift unpredictably across cycles and subjects. While deep neural networks have been used for phase estimation and complex-valued signal modeling, prior work does not explicitly learn phase transport between paired signals. Consequently, neither endpoint-supervised regression nor the standard affine path used in flow matching accounts for this phase--amplitude structure. We introduce \emph{cylindrical geodesic flow matching} for paired cardiovascular waveform translation. We show that the standard affine path used in flow matching distorts intermediate amplitude and instantaneous frequency when interpolating between quasiperiodic signals; replacing it with a closed-form geodesic on the phase--amplitude cylinder eliminates these artifacts and converts each training pair into dense, geometry-consistent velocity supervision. On zero-shot photoplethysmography and limited-support seismocardiography adaptation benchmarks, our method consistently outperforms interpolation baselines and matches or exceeds direct supervised prediction, reducing Hilbert Transform, $L_2$, and Dynamic Time Warping distance by up to ${\sim}15\%$ over the strongest competing baseline. These results suggest that bridge geometry is a critical inductive bias for flow matching on oscillatory signal translation.

---


### 288. [2D Spatial Reasoning with Adaptive Neural Cellular Automata](https://arxiv.org/abs/2610.08518)

**<font color=#1a73e8>作者：</font>** Martin Spitznagel, Janis Keuper  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many modern learning approaches are still struggling with spatial reasoning tasks, i.e. they lack the ability to utilize geometric information of perceived entities and their spatial relation to each other to solve problems. We introduce a novel Adaptive Neural Cellular Automata (aNCA) architecture which uses deformable convolutions to dynamically adapt the perceptive field and iteratively reason over 2D spatial relations on grid-like data structures (e.g. images). Empirical results on public benchmarks show state of the art comprehensible results with high generalization abilities for solving image based puzzles like Sudoku or finding the shortest path in a maze.

---


### 289. [PHBA: Prefix-State Hybrid Block Attention](https://arxiv.org/abs/2610.08527)

**<font color=#1a73e8>作者：</font>** Ruijie Li, Jiaxi Hu, Shiyu Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid architectures combining linear sequence models with softmax attention provide an effective balance between efficient long-context modeling and precise token retrieval. Existing designs such as Native Hybrid Attention (NHA) combine compressed long-term states with sliding-window attention, but their exact attention is restricted to a fixed local window. In this work, we introduce Prefix-State Hybrid Block Attention (PHBA), which replaces local sliding-window attention with top-k block-sparse retrieval and couples each retrieved block with a compact prefix state summarizing its preceding context. The prefix states are constructed by a gated linear recurrence at block boundaries and retrieved together with the corresponding token blocks, allowing the model to combine precise long-range evidence with compressed historical context within a unified layer. We further develop a hardware-aware Triton implementation that streams routed token blocks and prefix states without materializing large intermediate tensors. Experiments show that PHBA improves long-context and retrieval performance over strong linear and hybrid baselines while retaining efficient training and inference.

---


### 290. [MedCORE: Criteria-Grounded Clinical Reasoning for Interpretable Medical Image Diagnosis](https://arxiv.org/abs/2610.08528)

**<font color=#1a73e8>作者：</font>** Asim Khan, Samee Ullah Khan, Dwarikanath Mahapatra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinical diagnosis is inherently a structured reasoning process, yet existing deep learning models often bypass this structure by mapping image features directly to disease labels without explicitly interrogating the morphological and textural criteria that clinicians systematically evaluate. This limits diagnostic transparency and may compromise safe clinical deployment. We present MedCORE (Medical Criteria-Oriented Reasoning and Evidence), a structured diagnostic framework that operationalizes clinical reasoning within a vision-language architecture. For each input image, MedCORE decomposes the diagnostic process into clinically defined criteria, spatially localizes each criterion to diagnostically relevant image regions, encodes evidence through multi-scale representations that capture macro-structural and micro-textural pathological characteristics, and refines criterion representations using a Graph Attention Network that explicitly models inter-criteria dependencies. Criterion representations are further aligned with clinical text descriptors, reinforced through class-wise visual prototypes, and aggregated using uncertainty-calibrated weighting that proportionally discounts low-confidence diagnostic evidence. MedCORE is validated across three clinically heterogeneous imaging modalities, including dermoscopic lesion classification on ISIC 2018, breast ultrasound lesion characterization on BUSI, and diabetic retinopathy grading on IDRiD. Quantitatively, MedCORE achieves 89.2% accuracy, 85.7% macro-F1, and 96.4% AUC on ISIC 2018; 96.1% accuracy, 95.2% macro-F1, and 98.4% AUC on BUSI; and 84.3% accuracy, 80.2% macro-F1, and 92.8% AUC on IDRiD. These results demonstrate consistent improvements over strong CNN, transformer, biomedical vision-language, concept-based, and prototype-based baselines.

---


### 291. [Beyond Perturbation Magnitude: Direction-Dependent Responses in Multimodal Geometric Representations](https://arxiv.org/abs/2610.08533)

**<font color=#1a73e8>作者：</font>** Yongsheng Luo, Wengan He, Yu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometric alignment scores based on Gram determinants provide a compact way to model higher-order consistency among modalities, yet how such scores respond to modality degradation is poorly understood. This paper asks whether the response of a multimodal geometric score is determined primarily by the magnitude of the perturbation-induced displacement. Using frozen cohorts from MSR-VTT (N=878) and DiDeMo (N=980), we apply controlled video blur and audio noise and analyze the response in the relational geometry on which the score is defined. Displacement magnitude explains at most 15% of the out-of-sample variance in the absolute response, and magnitude-matched pairs respond systematically differently, so scalar magnitude does not organize the response. The closed-form first-order expansion of the Gramian volume yields the Directional Geometric Response (DGR): the projection of the displacement onto the local volume gradient, which jointly captures the clean operating point, displacement magnitude, and displacement direction. The absolute first-order DGR term explains the observed response with out-of-sample R^2 of 0.838-0.969, matched-magnitude ranking accuracies of 0.864-0.963, and response-sign accuracies of 0.909-0.989, whereas the tested direction-free alternatives remain weak or unstable under the corresponding evaluation protocols. A pre-specified gain-normalization candidate, V/(g_V+eps), fails its predictability and clean-order gates. DGR uses the observed degraded-state displacement and is therefore an explanatory quantity, not a deployment-time predictor: geometric response depends on where the representation operates, how far degradation moves the relational geometry, and in which direction it moves.

---


### 292. [FlowCF: Sparse Counterfactual Explanations for Mixed-Type Tabular Data using Flow Matching](https://arxiv.org/abs/2610.08537)

**<font color=#1a73e8>作者：</font>** Emmanouil Panagiotou, Eirini Ntoutsi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In the field of Explainable AI (XAI), counterfactual (CF) explanations interpret a model's decision by suggesting the changes to the input that would lead to a more favourable outcome. To be useful in practice, such an explanation should change few features and change them as little as possible, properties known as sparsity and proximity. We observe that existing methods remain limited in this respect, especially for numerical features, whether they are model-agnostic and amortised, or gradient-based with full access to the model. In this paper, we propose FlowCF, a model-agnostic generative method that frames CF generation as sparse transport from the factual to the target class. We solve this transport with flow matching, which we extend to mixed feature types with a novel mixed flow operator, and exploit the resulting geometry to optimise for sparsity through a gating network that minimises the number of features the transport changes. Extensive experiments on six benchmark datasets demonstrate that FlowCF produces the best numerical sparsity and proximity, changing 29% of the numerical features where the best baseline changes 89%, at 70% smaller displacement, while remaining comparable on the other desiderata.

---


### 293. [From Shared Demand Patterns to Local Uncertainty: Probabilistic Load Forecasting by Mixing Compact Adaptations](https://arxiv.org/abs/2610.08538)

**<font color=#1a73e8>作者：</font>** Haoran Li, Zhe Cheng, Yang Weng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic load forecasting has been widely studied for power-system operation and planning, but customer- and transformer-level forecasting introduces a distinct scalability challenge. At these levels, load uncertainty is strongly affected by customer behavior, weather, and mixed load composition, making it difficult for a single shared model to capture heterogeneous patterns. Using separate probabilistic models can improve local accuracy, but becomes costly to train, store, update, and validate at scale. To address this challenge, we develop a scalable customer-aware forecasting framework that learns common demand behavior through a shared model while adapting only a compact subset of parameters. Rather than using an independent model for each load or assigning each load to a specialized model, the proposed design learns a small bank of low-dimensional adaptation components and allows each load to combine them according to its forecasting characteristics. This preserves shared knowledge across customers while providing sufficient flexibility for heterogeneous and mixed load compositions. Experiments on 590 load profiles from the SMART-DS dataset show consistent improvements in deterministic accuracy and probabilistic quality over statistical, neural-network, Transformer-based, and pretrained time-series baselines, while retaining low storage and inference costs.

---


### 294. [AnyBottle: A Recipe to Only Keep the Concepts You Really Need](https://arxiv.org/abs/2610.08552)

**<font color=#1a73e8>作者：</font>** Wolfgang Stammer, Sukrut Rao, Hevra Petekkaya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Concept bottleneck models (CBMs) make predictions inspectable and intervenable by routing them through human-interpretable concepts, but originally required concept annotations. Annotation-free variants remove this requirement, but typically use large concept vocabularies, static at both training and inference, producing bottlenecks larger than any task or prediction needs and harder to inspect. We propose AnyBottle, a single recipe for building compact, task-specific CBMs. AnyBottle assumes only a frozen backbone and an unsupervised concept pool, such as a sparse autoencoder. A black-box teacher trained on the same backbone then guides selection: each round adds the concept that best explains the bottleneck's current failures, with candidates restricted to regions of teacher/student disagreement. Trained with nested dropout over this selection order, the final bottleneck predicts accurately from any concept prefix, so inference spends fewer concepts on inputs it is confident about early and more on hard ones. Since no stage is modality-specific, a new domain and task requires swapping only the backbone and concept pool. Across six vision and two text datasets and two teacher paradigms, AnyBottle yields bottlenecks with fewer concepts and higher concept consistency than annotation-free baselines, while staying close to the black-box reference. Overall, AnyBottle shows that going annotation-free need not mean going large: a small, discovered vocabulary can be as expressive as a much larger, fixed one.

---


### 295. [DeltaTTT: Layerwise Optimization for Nonlinear Recurrent Memory](https://arxiv.org/abs/2610.08553)

**<font color=#1a73e8>作者：</font>** Yining Li, Dongchen Han, Jie Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sequential test-time training adapts a memory network through successive updates, each computing an inner-loop gradient based on the network's previous state. Intuitively, this state dependence should allow each update to account for what the memory has already learned and better incorporate new information. However, we find that this expected advantage does not consistently materialize in nonlinear memories: a fixed-base parallel TTT baseline outperforms its serial counterpart. Our exploratory experiments point to a key underlying difficulty: nonlinear memories can be harder to optimize than linear ones within a single pass over the sequence. To alleviate this optimization difficulty, we introduce DeltaTTT, which replaces joint inner-loop optimization of a two-layer memory network with layerwise learning. Each layer is assigned a local prediction target and updated through a state-dependent delta rule. This formulation retains a nonlinear readout while enabling chunkwise parallel computation. Experiments on DeltaNet and LaCT backbones show improvements in language modeling and retrieval over their recurrent baselines.

---


### 296. [Systemization of Knowledge (SoK): Human-Centered AI Safety for Youth](https://arxiv.org/abs/2610.08554)

**<font color=#1a73e8>作者：</font>** Pratyasha Saha, Yaman Yu, Yang Wang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> While HCI increasingly examines AI-safety for youth, the literature lacks a comprehensive view of what risks have been identified, how they are addressed, and whether proposed protections work in-practice. We systematically reviewed 100 empirical HCI studies involving children and youth interacting with or exposed to AI across schools, homes, care settings, and public services. Using the YAIR taxonomy for risks and the MIT Mitigation Taxonomy for countermeasures, we map which risks have been identified, whether each risk is addressed by countermeasure(s), and whether each countermeasure for that risk is implemented and even evaluated. The risk-countermeasure mapping shows that most risks are matched only with proposed/ideated countermeasures; few countermeasures have been implemented, and fewer still evaluated; and existing evaluations often measure technical performance rather than protection from harm. We identify where coverage is absent, where safeguards remain untested, and propose concrete directions for HCI research to strengthen youth AI-safety.

---


### 297. [Singular Value Decomposition: A Geometric Rediscovery, Where Proofs Become Algorithms](https://arxiv.org/abs/2610.08565)

**<font color=#1a73e8>作者：</font>** Paul Agron  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This article is a geometric rediscovery of the singular value decomposition, with a further claim: the construction it builds is the machinery behind much of machine learning. The same argument that answers an idle question about ellipses is the algorithm behind principal component analysis, kernel methods, and PageRank, and it is not only the results that transfer but the proofs themselves, run as procedures.
The usual introduction states $A = U\Sigma V^T$ and justifies it via the spectral theorem applied to $A^T A$. This is correct but unilluminating, since it assumes a powerful theorem to reach a result that is, in the end, about ellipses. Part I reverses the order. A linear map sends the unit circle to an ellipse; one asks which input directions map to its axes, and finds, example after example, that they are perpendicular. In the plane this can be watched: rotate a frame, track how far its images are from perpendicular, and a sign change forces a frame where they are exactly perpendicular, which is also where the map stretches hardest. Maximizing the stretch and recursing generalizes this to n dimensions, with singular values falling out in order, and the construction proves the spectral theorem rather than assuming it.
Part II puts each construction to work: maximize-and-recurse becomes the power method and PageRank; the lemma locating the maximizer becomes the stopping rule of gradient descent; the duality between $A^T A$ and $A A^T$ becomes the transport at the heart of kernel PCA. Each connection is stated with its boundary, saying what the decomposition supplies and where another idea takes over. Prerequisites are the standard sophomore sequence, and the worked examples are small enough to check by hand.

---


### 298. [Less Is More: A Leakage-Controlled Study of Dermoscopic Preprocessing for Joint Skin Lesion Classification and Segmentation with YOLO26](https://arxiv.org/abs/2610.08570)

**<font color=#1a73e8>作者：</font>** Truong Viet Vu, Nguyen Chi Hai, Nguyen Phuc Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Handcrafted preprocessing is widely employed in automated dermoscopic analysis to suppress imaging artifacts and enhance lesion visibility. Nevertheless, its actual contribution to modern real-time models remains unclear, particularly when evaluation protocols do not adequately control correlations among images of the same lesion. This study presents a leakage-controlled, lesion-disjoint evaluation of dermoscopic preprocessing and augmentation for joint multi-class lesion classification and instance segmentation using a fixed nano-scale YOLO26 segmentation model (YOLO26n-seg). From HAM10000 (10,015 images), quality control yields 10,013 valid image-mask pairs from 7,468 unique lesions, partitioned into mutually exclusive sets by lesion identity. With the architecture, resolution, training budget, and evaluation protocol held fixed, we compare minimally processed images plus online augmentation against offline class balancing, DullRazor-CLAHE preprocessing, and raw-processed hybrid views, over three random seeds. On the lesion-disjoint test set, the raw baseline achieves a mask mAP$_{50:95}$ of $0.5636 \pm 0.0234$, a Dice score of $0.9356 \pm 0.0024$, and a macro-F1 score of $0.6917 \pm 0.0202$. Offline augmentation does not improve the mean performance, while the combined and hybrid strategies reduce both class-aware segmentation and classification accuracy. At only 2.69 million parameters, the model runs at approximately 50 frames per second. Under a leakage-controlled, lesion-disjoint protocol with all non-input factors held fixed, minimally processed dermoscopic images combined with standard online augmentation deliver a better accuracy-efficiency trade-off than increasingly complex deterministic preprocessing, which yields no consistent joint benefit across three seeds on HAM10000.

---


### 299. [Sparse2comm: Towards Robust Cooperative 3D Object Detection](https://arxiv.org/abs/2610.08573)

**<font color=#1a73e8>作者：</font>** Lei Yang, Boqi Li, Chunmian Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cooperative perception improves autonomous driving by sharing complementary observations among vehicles and roadside infrastructure for 3D object detection. However, practical deployment is constrained by limited bandwidth and unreliable cooperation, where packet loss, transmission delay, and spatial misalignment jointly degrade the cooperative feature stream. Existing methods often reduce communication cost or compensate for one degradation type, leaving coupled disturbances insufficiently addressed. To address this problem, we propose Sparse2comm, a bandwidth-efficient and robust cooperative 3D object detection framework that treats unreliable cooperation as progressive restoration over degraded cooperative features. Sparse Feature Encoding first encodes communication as randomly mask-sampled foreground features transmitted by collaborating agents, from which the ego vehicle reconstructs dense semantic representations. This sparse-to-dense mechanism learns to infer missing object-centric content from sparse observations, enabling ultra-low-bandwidth communication and packet-loss recovery within the same representation. On the semantically restored features, Latency-Aware Alignment predicts motion flow to compensate delayed messages, and Self-Calibrating Fusion estimates residual spatial offsets in a self-supervised manner before adaptive cross-agent fusion. Sparse2comm therefore restores semantic completeness, temporal consistency, and spatial alignment in an ordered pipeline. Extensive experiments on DAIR-V2X, OpenV2V, and V2V4Real show that Sparse2comm maintains competitive clean accuracy and consistently improves robustness under individual and mixed real-world degradations. Compared with the selective feature communication baseline Where2comm, Sparse2comm improves mixed-setting AP@0.5/AP@0.7 by +20.15/+11.79, +12.66/+11.07, and +15.36/+12.61 on the three datasets, respectively.

---


### 300. [FedDermaSeg: Federated Learning for Dermatological Image Segmentation](https://arxiv.org/abs/2610.08574)

**<font color=#1a73e8>作者：</font>** Anabik Pal, Ganesh Patidar, Bikash Santra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Skin cancer is a major global health concern, and early detection and accurate lesion delineation are important for effective diagnosis and treatment planning. Automated skin lesion analysis can assist dermatologists, with lesion segmentation serving as a fundamental step in computer-aided diagnostic systems. Conventional deep learning-based segmentation models typically rely on centralized training, where images and their corresponding segmentation masks are collected on a central server. Such data aggregation raises privacy concerns in medical applications and requires substantial centralized computational resources. To address these limitations, we investigate the feasibility of federated learning for privacy-preserving skin lesion segmentation. The training and validation sets of the ISIC 2018 Skin Lesion Segmentation Challenge dataset are used to simulate a distributed learning environment and develop a federated segmentation model. The resulting model is evaluated on the ISIC 2018 test set and the PH2 dataset to assess its performance and generalizability. Experimental results demonstrate that the federated model achieves performance comparable to centralized training while consistently improving upon the locally trained models. These findings demonstrate the potential of federated learning for collaborative skin lesion segmentation without requiring centralized aggregation of medical images.

---


> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-335](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
