# 📦 其他研究 | 2026年09月02日

> 本类共 **485** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-485](./part-10.md)

---

### 51. [Curvature Cryptanalysis of Smooth Transformer Feed-Forward Networks](https://arxiv.org/abs/2608.28843)

**<font color=#1a73e8>作者：</font>** Munawar Hasan, Apostol Vassilev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that smooth two-layer feed-forward networks (FFNs) expose an additional structural model extraction channel under a chosen-input raw-output oracle at the FFN branch; consider transformer FFN branches with GELU or SiLU activations under chosen-input raw-output access, without access to parameters, gradients, or internal activations; exploit a second-order leakage channel in which projected input Hessians form different mixtures of the same hidden symmetric rank-one factors induced by the FFN input weights. We formalize resulting Hessian collection as a partially symmetric decomposition to establish conditions for local identifiability and stability to exploit vector-output stencil reuse to reduce the structural query cost by a factor of 16. On independently trained CIFAR-10 vision transformers, only 16 projected Hessians, corresponding to 8193 black-box queries, recover the hidden FFN directions with average absolute cosine alignment above 0.94, with 95.1 % of GELU and 91.9 % of SiLU directions exceeding 0.90 alignment. Recovery remains high across independently trained models, repeated extraction runs, and all transformer blocks. The recovered structure supports functional extraction too. Keeping the recovered directions fixed and fitting only the remaining FFN parameters yields high-fidelity substitutes with more than 93 % top-1 agreement, while test accuracy remains within 0.90% and 0.62% of the GELU and SiLU targets. Output rounding and Gaussian noise substantially reduce recovery under a fixed attack configuration, but adapting the finite-difference step restores average alignment to 0.9603 and 0.9398. This is an end-to-end path from black-box second-order observations to hidden FFN-structure recovery and functional replacement. Under the stated oracle model, smooth FFN curvature exposes internal parameter geometry that behavioral fidelity alone cannot reveal.

---


### 52. [Toward Postural State Classification in Immersive VR with Multimodal Data and Explainability Analysis](https://arxiv.org/abs/2608.28844)

**<font color=#1a73e8>作者：</font>** Nipa Anjum, Md Irfan Pavel, Robert Gonzalez Jr 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Ensuring a safe virtual reality (VR) experience requires systems that can predict and respond when users lose their balance. Although prior work has examined fall prediction and motion sickness, many approaches are regression-based and postural state classification remains less explored. This study compares machine learning (ML) and deep learning (DL) models for classifying postural states in VR under visual perturbations. We used a multimodal dataset containing kinematic, electromyographic (EMG), and electrodermal activity (EDA) signals. The data were prepared for a binary task to distinguish balanced from imbalanced postural states, and participant-wise downsampling addressed class imbalance. All models were evaluated with Leave-One-Participant-Out (LOPO) cross-validation to test generalization to unseen participants. Among the models, the Mamba-inspired CNN (MI-CNN) achieved the highest accuracy of 96.76%. SHapley Additive exPlanations (SHAP) analysis improved interpretability and identified the most influential classification factors. The SHAP results showed that kinematic features were dominant, indicating that body-motion patterns are informative for detecting imbalance in VR. We also evaluated MI-CNN using only the top two-thirds of features ranked by SHAP importance. Despite a 33% reduction in input dimensionality, the model maintained performance, achieving 0.957 accuracy and 0.957 F1-score, with about a 1% decrease compared with the full-feature model. These findings suggest that multimodal sensing, temporal deep learning, and explainable AI can support reliable classification of balance-related instability in VR. Accurate recognition of imbalanced postural states may raise awareness of fall risk and guide safer, adaptive VR systems that respond to instability while improving user safety and experience. Code is available at: this https URL.

---


### 53. [Equivariant Sheaf Neural Networks: Learning Geometric Transport on Graphs](https://arxiv.org/abs/2608.28853)

**<font color=#1a73e8>作者：</font>** Alessio Borgi, Mario Severino, Fabrizio Silvestri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equivariant graph neural networks provide a principled way to model geometric systems, but efficient first-order architectures remain limited in how vector information can be transformed as it moves across a graph. We introduce \textsc{ESNN}, an Equivariant Sheaf Neural Network that enriches this interaction by learning directed, matrix-valued transport between neighboring vector features while preserving exact Euclidean equivariance. Rather than increasing the order of the representation, ESNN keeps scalar and vector features first-order and places the additional geometric flexibility in the edge transport itself. We characterize this transport theoretically, showing that when relative displacement is the only covariant geometric input, every linear $O(n)$-equivariant map decomposes into independent radial and tangential components, while learned covariant features enable richer feature-conditioned transformations. We also introduce controlled symmetry relaxation for systems with a preferred ambient direction, which may be prescribed or inferred from data while recovering full $E(n)$-equivariance when the directional pathway is inactive. Across particle dynamics, mesh-based simulation, point-cloud classification, and molecular property prediction, ESNN improves dynamics prediction, recovers the gravity axis when symmetry is broken, yields substantial gains on selected mesh tasks and long-horizon rollouts, and remains robust to unseen rotations. These results show that learning how geometric information is transported across edges offers a complementary route to expressive equivariant message passing without requiring higher-order representations.

---


### 54. [MWIR-4-Plastic: The Identification of Complex End-of-Life Industrial Plastic using Mid-wave Infrared Hyperspectral Imaging and Machine Learning](https://arxiv.org/abs/2608.28874)

**<font color=#1a73e8>作者：</font>** Elias Arbash, Andréa de Lima Ribeiro, Filipa Simões 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The automated sorting of shredded black plastics from end-of-life (EOF) industrial waste presents a significant challenge in recycling facilities, primarily due to the limitations of current sensing and analytical approaches. Existing studies predominantly rely on single-point contact-based mid-infrared spectroscopy or laboratory hyperspectral imaging (HSI) setups, which fail to provide the spatially resolved analysis necessary for fast, bulk processing. Moreover, available datasets are laboratory-controlled and focus on intact rather than shredded plastics, hindering further recycling refinement. Black industrial plastics, in particular, are underrepresented, while most classification pipelines depend on manual region selection and rule-based spectral matching, neglecting spatial information and modern deep learning (DL) methods. To address these gaps, we introduce the first publicly available HSI dataset of shredded black plastics from EOF vehicle, comprising four industrial polymers across 13 co-registered RGB, VNIR, SWIR, and MWIR scenes and their segmentation pipeline. We developed a multi-modal spectral-spatial framework that integrates foreground isolation, pixel-wise classification, and object-level majority voting. By adapting advanced hyperspectral transformers from earth observation and incorporating chemometric band selection, we achieve accurate classification of complex black plastics. The study establishes the first comprehensive benchmark using nine processing methods, including chemometric, machine learning, and DL architectures. To ensure reproducibility, the complete dataset and methodologies are publicly released, establishing a benchmark for a hyperspectral object-analysis pipeline in industrial inspection.

---


### 55. [Enhancing Web Application Firewalls with BERT-GNN for SQL Injection Detection](https://arxiv.org/abs/2608.28882)

**<font color=#1a73e8>作者：</font>** Lilliane Linnet Musoke, Atta Badii, Ahmed Ashlam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Detecting sophisticated SQL Injection (SQLi) attacks remains among the most critical challenges in web applications security. This research study has resulted in an optimised hybrid BERT-GNN pipeline with improved detection accuracy and robustness while reducing false-positive and false-negative rates. SQL queries are tokenised and encoded into contextual BERT embeddings, which then initialise the node features of a Graph Neural Network (GNN) trained to classify each query, with the architecture tuned by Optuna over accuracy, precision, recall, and F1-score. The proposed model achieved 99.67% accuracy, with 99.71% precision, 99.39% recall, and 99.55% F1-score on the attack class. A sensitivity analysis, performed by perturbing graph inputs, further assessed the model robustness and yielded a low mean sensitivity score of 0.0037, indicating stable predictions under such perturbations. The results have demonstrated the potential of a novel hybrid model that couples BERT contextual understanding with the GNN structural modelling to detect sophisticated SQLi attack vectors. For open validation, the dataset, test sets and models are made available at this https URL.

---


### 56. [Moving the Mean Toward the Known Good, Not Beyond It: What Inference-Time Interventions and Weight Consolidation Buy in Open-Ended Generation](https://arxiv.org/abs/2608.28886)

**<font color=#1a73e8>作者：</font>** Roberto I. Ono Filho  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> What does a generation loop gain from learning on its own verified successes? In cycles of generate, verify, select and LoRA-consolidate on online bin packing, training on value-filtered candidates shifts what the model writes on held-out variants toward value (-1.7 points of excess, p=0.008; -3.1 against a random-consolidation control, p=0.004) while the best observed candidate converges to the classic heuristic's level and no further. A confirmation battery replicates the whole procedure three times, with fresh seeds and a never-consulted held-out set read exactly once: the mean was nearly identical in all three lineages (-2.0, -1.8, -1.9), and after aggregating within held-out variant all seven evaluable variants favored consolidation (p=0.008). The best observed candidate moved to the classic heuristic's level, exactly (0.021028 in all three lineages, for attract and for the random control alike), and never beyond it. A matched SFT-only control shows the supervised anchor, not repulsion from bad candidates, does the concentrating (96% of candidates land exactly at the classic heuristic's level). The tails cut both ways: consolidation lowers the per-candidate rate of better-than-classic candidates (10% to 3.9%) while its larger production yields more such candidates absolutely (5 against 1, on few events). As motivation we report the inference-time ledger that led here: a model-written schematic recap buys judged document integration and nothing buys development; a verifier written into the stream is imitated, 16.4 fabricated verdict lines per notebook. Mean quality among valid candidates can be bought and replicated; the observed best goes to the classic and, so far, never beyond it.

---


### 57. [Enhancing Web Application Firewalls with Machine Learning for SQL Injection Detection](https://arxiv.org/abs/2608.28889)

**<font color=#1a73e8>作者：</font>** Lilliane Linnet Musoke, Atta Badii, Ahmed Ashlam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Detecting SQL Injection (SQLi) attacks ranks among the most critical challenges in web application security. This research conducted a systematic literature review to identify the research gaps in this domain and responsively designed and optimised a DistilBERT-Stacked Ensemble pipeline to improve detection efficiency and robustness while reducing false-positive and false-negative rates. Comprehensive pre-processing and tokenisation were performed, DistilBERT embeddings were extracted, and machine-learning and ensemble classifiers were trained and ranked on accuracy, precision, recall and F1-score. The three best performers (Logistic Regression, XGBoost and SVM) were combined through a neural meta-learner to form a stacked ensemble. The ensemble was hardened with adversarial examples generated by the Fast Gradient Sign Method (FGSM) and tuned with Optuna. The optimised ensemble achieved 99.81% across all reported metrics, closely comparable to the strongest single model (DistilBERT SVM, 99.82%). On the evaluation platform used in this study (Section 3.8), the ensemble classified the full test set in 0.0136s against 1.896s for DistilBERT-SVM, an approximately 140-fold reduction in measured inference latency, while retaining 99.77% accuracy under a single-step FGSM attack. The contribution is the design and validation of a SQLi detector performing with state-of-the-art accuracy at real-time speed and with demonstrated robustness to a single-step FGSM attack, rather than a marginal gain in accuracy. Sensitivity analysis further confirmed the stability of the model. These findings highlight the value of adversarial training and stacked meta-learning in building robust Web Application Firewalls (WAFs) for SQLi detection. For open validation, the dataset, test sets and models are made available at this https URL.

---


### 58. [Pixel-wise Geo-registration of Drone and Satellite Images](https://arxiv.org/abs/2608.28891)

**<font color=#1a73e8>作者：</font>** Qingyang Liu, David G Shatwell, Parth Parag Kulkarni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel-level cross-view geo-registration aims to align a query image (e.g., drone) to a geo-referenced satellite map so that every query pixel can be mapped to real-world GPS coordinates. Despite strong progress in cross-view geo-localization, existing benchmarks largely provide only GPS labels, limiting evaluation to a single coordinate per image and leaving dense geodetic alignment underexplored. We introduce SkyReg, a dataset and standardized benchmark for pixel-level drone-to-satellite geo-registration, providing dense per-pixel geo-location supervision across diverse settings (orthographic and perspective), scene types (urban, landmark-centric, suburban/rural), and camera configurations. Using SkyReg, we evaluate a broad set of baselines spanning retrieval, feature matching, homography-based alignment, and feed-forward 3D reconstruction. Finally, cross-view pairs from SkyReg, we train a geometry-aware reconstruction pipeline that achieves state-of-the-art results,improving performance by a significant margin.

---


### 59. [ReconSplat: Generalizable 3D Scene Reconstruction Beyond Observed Views](https://arxiv.org/abs/2608.28895)

**<font color=#1a73e8>作者：</font>** Giuseppe Stracquadanio, Kevin Raj, Julia Grabinski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce ReconSplat, a feed-forward model for 3D scene reconstruction that aims to address the longstanding trade-off between plausible view generation for unobserved regions and geometric consistency, providing both geometrically aligned novel views and sharp depth estimates. Our approach builds on 3D Gaussian splatting (3DGS) as an intermediate differentiable scene representation and integrates it with a multi-view latent diffusion model (MV-LDM) trained to act simultaneously as a refiner and an inpainter for appearance and scene geometry. We enforce geometric consistency by guiding the diffusion process with variational 3D latent features for appearance and geometry, encoded by the feed-forward 3DGS representation and rasterized to 2D latent space. ReconSplat produces both photorealistic novel views and accurate depth maps on real-world benchmarks, RealEstate10K and DL3DV-10K, outperforming existing methods in challenging extrapolation setups. Notably, ReconSplat allows the extrapolation of unseen and challenging viewpoints jointly with coherent and precise scene geometry.

---


### 60. [Conservative Hybrid Graph Networks for Process Systems with Learned Routing](https://arxiv.org/abs/2608.28896)

**<font color=#1a73e8>作者：</font>** Paolo Guida  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial process networks do not maintain a single effective topology while operating: streams are throttled or bypassed, and units move between idle, transition, and active regimes. Models of such systems are typically trained on measured state trajectories while the operating mechanisms that generated them remain latent, and an unconstrained graph network can fit such a trajectory without assigning stable physical meaning to the recovered routing. We address both problems with the Conservative Hybrid Graph Network (CHGN), which learns routing, regime assignment, and removal rates as data-driven surrogates and inserts them into a fixed transport equation, so that the mass balance holds by construction for any predicted routing. CHGN trained on networks of 10-20 nodes transfers zero-shot to unseen graphs of 25-40 nodes without retraining, reaching an RMSE of 2.1e-3 against 6e-2 to 9e-2 for GNN baselines under the same protocol, with a gate MAE of 7.9e-3 and regime accuracy of 94.3% (1.2e-2 and 96.4% respectively on the fixed training topology). On a fluid-mixing pilot plant, CHGN improves on a persistence baseline for held-out physical faults but does not predict manual interventions, for which the governing valve actions are unobserved. The model therefore transfers across process topologies without retraining and exposes the latent mechanisms governing plant behaviour to inspection.

---


### 61. [Off-Policy Evaluation for Semantic ID Recommenders: Does the Model's Own Code Hierarchy Help?](https://arxiv.org/abs/2608.28905)

**<font color=#1a73e8>作者：</font>** Artem Betlei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative recommenders increasingly emit semantic IDs (SIDs): each item is a short sequence of hierarchical discrete codes from a residual quantizer, decoded autoregressively. Before spending scarce A/B-test, a team may decide offline which decoder or reranking variants are worth testing - a job for off-policy evaluation (OPE). We ask a simple question: can the model's own SID tree serve as the action abstraction for that OPE? Our answer has three parts. (i) Under the near-argmax logging real recommenders use, per-item OPE is hopeless - as item-level effective sample size is usually small on production logs - but marginalizing items to code-prefix clusters restores estimable support and cuts error. (ii) This gain is thanks to coarsening, not to the hierarchy specifically; but the SID tree is what makes coarsening feasible in a generative system - each cluster's mass is exactly and cheaply returned by the decoder, whereas flat clustering requires enumerating item/leaf masses that a code-only decoder does not directly expose. (iii) Resolution depth is the operative knob - coarser under scarce support - and a conditional bias bound links the coarsening bias to the quantizer's worst-case reconstruction residual and the target-logging divergence.

---


### 62. [Coarse to Fine: Iterative Adversarial Neural Cellular Automata for Medical Image Synthesis](https://arxiv.org/abs/2608.28909)

**<font color=#1a73e8>作者：</font>** Anh Thi Luu, Nick Lemke, Anirban Mukhopadhyay  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale, publicly available datasets have driven advances in deep learning, but privacy and legal restrictions often limit data sharing in medical imaging. Synthetic data generation offers a privacy-friendly alternative to enable the training of high-performance models on health data. While most state-of-the-art generative models produce high-quality images, they remain computationally expensive, which limits their applicability on resource-constrained hardware. We propose StyleGANCA, the first lightweight general-purpose NCA-based generative adversarial network. The architecture integrates a StyleGAN-inspired mapping network and adaptive style modulation into a multi-scale NCA synthesis process, enabling latent-controlled image generation through iterative local interactions. We evaluate StyleGANCA on BloodMNIST and PathMNIST against adversarial, variational, diffusion, and NCA-based baselines. Experimental results demonstrate that StyleGANCA achieves competitive image quality with substantially fewer parameters than baseline architectures, achieving the best FID and KID scores on PathMNIST with only 617k parameters. Furthermore, downstream experiments show that the generated images preserve class-specific information and effectively support the training of multi-class classifiers. Our code is publicly available at: this https URL

---


### 63. [Learning-Theoretic Foundation for General Coded Computing: The Straggler Setting](https://arxiv.org/abs/2608.28910)

**<font color=#1a73e8>作者：</font>** Parsa Moradi, Behrooz Tahmasebi, Mohammad Ali Maddah-Ali  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coded computing has emerged as a powerful paradigm for mitigating the impact of straggling workers in distributed computing systems. However, existing coded-computing schemes are predominantly designed for the exact recovery of highly structured computations, such as polynomial evaluation and matrix multiplication, and typically rely on strict recovery thresholds. These assumptions significantly limit their applicability to modern machine-learning workloads, particularly deep neural networks (DNNs), whose computations generally lack rigid algebraic structure and, in many applications, require only accurate approximations rather than exact recovery.
To address this gap, we revisit coded computing from a learning-theoretic perspective and introduce General Coded Computing (GCC). Rather than adopting existing algebraic tools, GCC formulates coded computing through a natural end-to-end mean-squared error loss that directly measures the discrepancy between the desired computations and their recovered estimates. By deriving suitable upper bounds and restricting the encoder and decoder to a reproducing kernel Hilbert space (RKHS) with mild smoothness constraints, we show that both the encoder and decoder admit specific representations as linear combinations of RKHS kernel functions. This representation allows the corresponding coefficients to be computed efficiently. Moreover, this framework enables us to establish theoretical performance guarantees for GCC under two complementary straggler regimes. In the worst-case setting with $N$ worker nodes, and at most $S$ stragglers, we show that the end-to-end loss decays at least at rate $O(S^3N^{-3})$ for standard configurations. We then study a probabilistic setting in which each worker independently straggles with probability $p$. We prove that the expected loss can still converge at rate $O(\log_{1/p}^3(N)N^{-3})$.

---


### 64. [mmIR: Frequency-Space Inverse Rendering for 3D Millimeter-Wave Radar ADC Synthesis](https://arxiv.org/abs/2608.28913)

**<font color=#1a73e8>作者：</font>** Adnan Armouti, Yixuan Gao, Rajalakshmi Nandakumar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution 3D radar data is scarce. Commodity mmWave sensors use small antenna arrays that limit angular resolution to several degrees, and existing datasets provide only 2D range-azimuth maps or sparse point clouds rather than raw analog-to-digital converter (ADC) signals. Hardware scaling is expensive, synthetic-aperture scanning is impractical at fleet scale, and learned synthesis methods are bottlenecked by the very data shortage they aim to address. We present mmIR, an open-source differentiable frequency-modulated continuous-wave (FMCW) radar inverse renderer that fits a physics-based forward model to real captures and re-renders from dense virtual apertures to synthesize high-resolution 3D radar data. Because radar resolution is too coarse to recover geometry directly, mmIR performs LiDAR-assisted inverse rendering: using LiDAR-derived meshes as a geometric scaffold, mmIR optimizes per-vertex International Telecommunication Union (ITU) physics materials, vertex normals, and antenna beam patterns through end-to-end automatic differentiation of a phase-coherent multiple-input multiple-output (MIMO) forward model with multi-bounce propagation, polarization, and free-space diffraction. On seven outdoor and six indoor ColoRadar scenes, mmIR achieves 0.914 mean Pearson correlation on range-azimuth maps versus 0.307 for Sionna-RT. Scenes trained on a cascaded imaging radar transfer to a co-located single-chip radar without re-training (0.554 correlation), and dense virtual arrays (100x100 elements) produce single-frame 3D occupancy validated against LiDAR. Project page: this https URL

---


### 65. [VoiceCodeBench: Evaluating Exact Structured-Token Recovery in Automatic Speech Recognition](https://arxiv.org/abs/2608.28916)

**<font color=#1a73e8>作者：</font>** Tyler Baumgartner, Brandon Tai, Lisa Kaelin-Martin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) systems are commonly evaluated with word error rate (WER), yet many voice workflows depend on exact written values for identifiers, paths, and measured quantities. A transcript can appear fluent and achieve low WER while corrupting a value that a downstream system must parse, store, or execute.
We introduce VoiceCodeBench, a benchmark for evaluating exact structured-token recovery in English ASR. It contains 300 human-recorded workplace segments spanning eight workflow domains and 1,482 audited target entities across 26 entity types, each with a canonical written form recoverable from the audio. Under a raw-audio-only protocol, systems receive audio bytes without additional context or metadata. Alongside WER, we evaluate Canonical Token/Entity Match (CTEM), Task Success Rate (TSR), and per-type exact recovery.
Across 12 baseline ASR systems, lower WER generally corresponded to better structured-token recovery but did not fully determine it: Spearman correlations were -0.73 for both WER versus CTEM and WER versus TSR. The strongest baseline by TSR reached only 68.7%, leaving nearly one third of recordings with at least one unrecovered workflow-critical value. These results show that entity-sensitive metrics are needed to assess whether ASR output preserves exact values that production systems must parse, route, store, compare, or execute.

---


### 66. [Identity by Design, Demographics by Accident: Demographic Leakage and Suppression in Behavioral Biometric Embeddings](https://arxiv.org/abs/2608.28921)

**<font color=#1a73e8>作者：</font>** Iyadh Khan, Patrick Nilackshan, Mohamed Aathif 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Behavioral biometric authentication (BBA) systems use deep learning models to transform biometric signals, such as eye movements, voice, keystroke/touchstroke dynamics, and gait, into identity embeddings for user authentication. While designed to encode identity, these embeddings may inadvertently reveal sensitive demographic attributes, including gender, age, and height. Consequently, an adversary with access to the authentication model can infer demographic information from biometric signals, including those of users unseen during training or enrollment. In this paper, we present the first systematic audit of demographic leakage in BBA systems, evaluating 11 models across 9 datasets spanning four biometric modalities. We further benchmark four post-hoc suppression methods-Incremental Variable Elimination (IVE), Hilbert-Schmidt Independence Criterion (HSIC), Adversarial Encoder-Decoder (AED), and Protected Attribute Suppression System (PASS) to assess their ability to mitigate demographic leakage while preserving authentication utility. Our analysis reveals substantial variation in leakage and suppressibility across modalities, model architectures, and learning objectives. While voice embeddings exhibit high leakage that can be effectively suppressed, keystroke/touchstroke embeddings exhibit lower leakage but are considerably more difficult to sanitize. These findings highlight a fundamental privacy risk in behavioral biometric authentication and provide insights into the factors governing demographic information suppressibility.

---


### 67. [RankShift: In-Database Detection and Explanation of Categorical Shifts](https://arxiv.org/abs/2608.28922)

**<font color=#1a73e8>作者：</font>** Omair Shafi Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A login service can receive its usual number of failed sign-ins while one source grows from 2% to 30% of them. The same pattern appears in system logs when a rare event template becomes common while the message rate stays stable. These events change which categories are active without changing how many events occur. RankShift detects such changes inside the analytical database that stores the data. It compares each window's category shares with a benign reference using a Pearson score whose terms identify the categories responsible for the change. The same query returns the score, calibrated alert, and largest increasing contributions. We evaluate RankShift on HDFS, BGL, and Thunderbird. It matches the count-vector autoencoder within 0.001 AUROC on HDFS (0.999 versus 1.000) and leads on Thunderbird (0.983 versus 0.949). In a controlled fixed-volume experiment, RankShift detects rare-category shifts that are invisible to event-count monitoring, reaching 0.787 AUROC compared with 0.771 for the autoencoder. Across all three corpora, observed false-alarm rates track the requested operating levels. RankShift requires no model training or inference service, and the autoencoders deployed state is 137x larger.

---


### 68. [ActiveAugment: Online Active Learning for Augmentation Selection in Deep Learning](https://arxiv.org/abs/2608.28923)

**<font color=#1a73e8>作者：</font>** Noah Videcrantz, Mostafa Mehdipour Ghazi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data augmentation is a cornerstone of deep learning pipelines, yet existing strategies treat it as a static, model-agnostic preprocessing step, either relying on expensive dataset-specific policy search or applying transformations uniformly at random, regardless of what the model has already learned. We introduce ActiveAugment, a unified framework that treats augmentation selection as an online active learning problem. For each training minibatch, ActiveAugment generates a pool of candidate augmented views and scores each candidate using a combination of the model's predictive uncertainty and the feature discrepancy induced by the augmentation. The augmentation under which the current model is most fragile is selected per sample, and the model is then trained with a joint supervised classification and supervised contrastive objective that enforces intra-class invariance to the selected augmentations while maintaining inter-class separation. We evaluate ActiveAugment on eight benchmark datasets spanning natural and medical imaging, using CNN and transformer architectures across three training regimes (training from scratch, full fine-tuning, and linear probing), and comparing eight active selection strategies for augmentation scoring. ActiveAugment outperforms AutoAugment, RandAugment, and TrivialAugment under controlled augmentation shifts across all domains and budgets, with the most pronounced gains at low labelling budgets. On medical imaging datasets, where data is scarce and domain shift relative to natural-image pretrained models is large, ActiveAugment achieves higher test F1 than all baselines, demonstrating strong cross-domain adaptability. Our analysis reveals that the augmentation selection policy evolves meaningfully during training and that strategy choice has a direct impact on generalisation. Code is available at: this https URL.

---


### 69. [Leveraging Turn-taking Dynamics for Intent Recognition in Multi-party Conversations](https://arxiv.org/abs/2608.28926)

**<font color=#1a73e8>作者：</font>** Galo Castillo-López, Alexis Lombard, Gaël de Chalendar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose a multi-task learning approach for multi-party dialogue intent recognition that leverages an auxiliary task that models turn-taking dynamics. Specifically, we introduce turn-transition entropy, a self-supervised target computed from the sequence of speaker transitions, which quantifies the predictability of interaction patterns. Experiments on multiple pre-trained models demonstrate that incorporating this auxiliary task improves intent recognition performance, outperforming existing approaches which ignore multi-party interaction dynamics. We find that our proposed continuous target can be learned as a single-task objective, suggesting that it is an actual signal carrying useful information.

---


### 70. [Membership is Ownership: A Robust Ownership Verification Framework for Diffusion Models](https://arxiv.org/abs/2608.28929)

**<font color=#1a73e8>作者：</font>** Feng Jiang, Zuobin Xiong, An Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large-scale diffusion models have fueled numerous profitable downstream applications for AI-related businesses, including visual editing and content creation. Meanwhile, due to the huge amount of resource consumption (e.g., computation and high-quality data) during training, such diffusion models are deemed valuable intellectual property (IP) for tech companies like OpenAI and Google. Yet, the IP assets are vulnerable to various unauthorized uses by adversaries seeking to steal models for customized, usually commercial applications. Some existing approaches have explored IP protection for AI models; however, they mostly face structural limitations in common --- using a training-time watermarking by injecting artifacts in the model, which can impose a measurable utility cost and can be weakened by post-hoc fine-tuning. To address these challenges, this work investigates IP protection (i.e., model ownership verification) for diffusion models in a realistic commercial scenario with minimal model utility loss. Specifically, the proposed method builds a framework for model ownership verification, termed ``{Membership is Ownership} (MiO)'', based on a population-level hypothesis test on a private member evidence dataset. MiO verifies ownership using two criteria: model attribution through membership inference and model separation from public references. Both are tested at $p<10^{-6}$. We evaluate MiO on DDIM and Stable Diffusion models without modifying the owner model or its sampling pipeline, and report ROC-AUC and true-positive rates at fixed nominal false-positive targets. Furthermore, MiO stays stable under different post-theft fine-tuning and weight perturbation in adversarial scenarios, reflecting better robustness compared to the watermarking methods.

---


### 71. [NBS: No Bias Stereo](https://arxiv.org/abs/2608.28933)

**<font color=#1a73e8>作者：</font>** Vage Taamazyan, Zhuowen Shen, Stefan Hinterstoisser 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stereo reconstruction is one of the last remaining Computer Vision tasks where all state-of-the-art methods employ a heavy architectural inductive bias. Even though it has been demonstrated that the task can be solved using general-purpose methods, it is widely believed that inductive biases in stereo are strictly necessary for both high-quality results and computational efficiency. We challenge this paradigm. In this paper, we demonstrate that both state-of-the-art accuracy and superior runtime efficiency are achievable with a model completely devoid of architectural inductive biases, relying instead on a simple, end-to-end Vision Transformer. By training on massive synthetic datasets, we show that pure data-driven learning can surpass explicitly engineered geometry. This work proves that explicit inductive biases are no longer a prerequisite for stereo matching, ultimately unlocking true scaling laws for continuous improvement in 3D reconstruction.

---


### 72. [Revisiting the Provable-Auditable Privacy Gap of DP-SGD](https://arxiv.org/abs/2608.28934)

**<font color=#1a73e8>作者：</font>** Saloni Modi, Srivi Balaji, Yusong Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Differential privacy (DP) has traditionally been used to provide theoretical upper bounds on an algorithm's stability to changing its training data. In modern private machine learning applications, achieving strong tradeoffs between utility and theoretical privacy is challenging, and thus one may optimistically hope that existing theoretical privacy analyses are loose. Recent work on privacy auditing has adopted a dual viewpoint, instead lower bounding the true privacy of an algorithm by constructing empirical distinguishing events. The auditing literature has thus far yielded a pessimistic outlook on the looseness of theoretical privacy bounds for DP-SGD, the de facto private training method in modern ML, as nearly-matching empirical lower bounds have been achieved under various threat models [NHSBTJCT23, AC24, CBP25].
In this work, we propose the empirical privacy lower bound of an algorithm as a concrete metric to optimize for, complementary to the theoretical upper bound. We give a lightweight defense framework that generically augments optimization methods in the ML pipeline to have significantly-improved empirical privacy on standard benchmarks. Moreover, we show that our framework comes at no theoretical privacy cost when augmenting DP-SGD, unlike previously-proposed defenses against membership inference attacks. We evaluate our defense against a broad range of audit constructions, models, and datasets to demonstrate its flexibility.

---


### 73. [From the Loss Landscape to Diverse Feature Learning in Neural Networks](https://arxiv.org/abs/2608.28948)

**<font color=#1a73e8>作者：</font>** David Aram Yunis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Over the course of the last decade, neural networks have grown from an academic curiosity to moving the markets of nations. Despite this explosion in both research and deployment, relatively little is understood about how they achieve the solutions they do. This is both scientifically relevant, and pressing for society. When neural networks make decisions across self-driving, construction, law, hiring and health, there have been and will continue to be unintended consequences.
However, attempting to generalize the failures of the largest and most important production systems makes for a very difficult task. Yet signs of these failures exist at all scales of neural networks, so we should be able to study a much more tractable setting. All neural networks must undergo an optimization process, called training, to be useful. To a great degree, understanding neural networks is understanding their optimization: through what process and exposure to which data did they arrive at their results. Yet our knowledge on this topic as a field is quite imprecise. In particular, a curious phenomenon called mode connectivity, the ability to connect neural networks in the loss surface, defies explanation entirely.
This dissertation elucidates, explains and exploits this special structure in the loss landscape...

---


### 74. [Continuity-Free Near-Minimax Leading-Order Regret for CVaR-UCBVI](https://arxiv.org/abs/2608.28960)

**<font color=#1a73e8>作者：</font>** Yuanlong Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> For finite-horizon tabular CVaR reinforcement learning, prior work proves a $\widetilde{O}(\tau^{-1}\sqrt{SAK})$ leading regret bound for arbitrary normalized return laws and the sharper $\widetilde{O}(\sqrt{SAK/\tau})$ rate under a density lower bound. We show that the same Bernstein CVaR-UCBVI algorithm attains the sharper rate without continuity assumptions. The key is a selected-budget self-bound: the conditional variance of the episode shortfall is at most $\tau$ plus the value-estimation width. Substitution into the original Bernstein decomposition yields, with high probability, $\widetilde{O}(\sqrt{SAK/\tau}+(SAHK^{1/4}+S^2AH)/\tau)$ regret for arbitrary normalized return laws, including atomic, mixed, and continuous laws. The $\tau^{-1/2}$ leading term matches the expected-regret minimax lower bound up to logarithmic factors. Thus Bernstein CVaR-UCBVI is minimax-optimal over the full return-law class in the leading-order regime; the lower-order terms retain their $\tau^{-1}$ dependence.

---


### 75. [From Location Phrases to Geographic Entities: Task-Adapted Retrieval for People Search](https://arxiv.org/abs/2608.28965)

**<font color=#1a73e8>作者：</font>** Yanbo Li, Chujie Zheng, Jiahao Xu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> People search must map free-form location phrases to geographic entities used as structured retrieval filters. Lexical standardizers handle canonical names well but are brittle to aliases, misspellings, metropolitan expressions, and same-name ambiguity. We formulate this task as graded, set-valued entity retrieval over a fixed ontology. We identify three coupled design requirements: distinguishing identity-preserving variation from knowledge-dependent aliases, controlling false negatives among valid same-name entities, and separating stable transformations from mutable entity knowledge. We realize them in a prompt-asymmetric bi-encoder with calibrated alias support, bounded ambiguity-aware negatives, and editable entity documents that support localized updates without retraining.
Across a fixed production-derived development benchmark and a public GeoNames transfer task, task adaptation improves substantially over frozen encoders and standard token baselines. Controlled development ablations show that specialized supervision contributes beyond standard task fine-tuning and encoder scaling. On GeoNames, the adapted model improves known-target Recall@1 throughout zero-to-moderate character overlap, while character n-grams retain a small aggregate Target Recall@5 advantage. In a blinded human comparison on a stratified production challenge set, our model raises relevant P@1 from 28.0% to 46.0% (p=0.012). Fixed-query endpoint estimates improve on non-canonical queries and remain close to control on frequent queries; a randomized live experiment detects no engagement regression. These results support task-adapted geographic entity retrieval as a practical replacement for the incumbent taxonomy-based standardizer, with the largest relevance gains on non-canonical queries.

---


### 76. [From Analytics to Tumor Boards: An Evidence-Linked Multi-Agent Workflow for Oncology Feature Extraction](https://arxiv.org/abs/2608.28974)

**<font color=#1a73e8>作者：</font>** Daniel Kang, Michelle Hu, Soorya Ram Shimgekar 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinically relevant oncology information is distributed across heterogeneous, longitudinal documentation, creating substantial abstraction burden and requiring accurate attribution across specimens, tumors, biomarkers, and time points, while manual cancer-registry abstraction can require 27.2 minutes per case, highlighting the need for scalable methods that preserve clinical context while converting documentation into structured data. We evaluate the Nimblemind Multi-Agent System (nMAS), a configurable oncology information-extraction workflow which extracts clinically relevant structured fields from fragmented oncology documentation. The extraction task uses a clinician-informed schema of 328 attributes spanning report metadata, diagnosis, staging, and cancer-type-specific information. nMAS separates clinician-defined field specifications from model execution and combines complexity-aware extraction, report-level consolidation, and source-grounded validation. The retrospective evaluation included 230 de-identified oncology documents from 40 patients and 418 clinician-reviewed document-field pairs containing 1,126 non-empty reference values. Evaluation focused on fields identified by clinicians as present in the source documents rather than exhaustively annotating all 328 schema fields. nMAS achieved a rank-weighted value-level precision of 82.6%, recall of 87.5%, and F1 of 85.0%, compared with an F1 of 66.4% for an independently implemented UMA-style MiniMax M2.5 comparator. These findings support the feasibility of using a configurable, source-grounded extraction workflow to convert fragmented oncology documentation into reusable structured data.

---


### 77. [The Role of Network Topology and Opponent Information in Shaping Cooperation in Multi-Agent Reinforcement Learning Systems](https://arxiv.org/abs/2608.28977)

**<font color=#1a73e8>作者：</font>** Seongho Son, Stephen Hailes, Mirco Musolesi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Several works have investigated the influence of graph topology on cooperation among artificial agents, while the majority of the literature has focused on modelling agents' adaptation through strategy imitation, which relies solely on the cumulative payoffs of others. This paper investigates scenarios in which each agent learns to play the two-player Iterated Prisoner's Dilemma (IPD) using deep reinforcement learning. Each agent is represented as a node in a graph, where its neighbours constitute the pool of opponents with whom it can interact. During each IPD episode, agents are provided with different types of information about their opponent, consisting of action history and opponent identity. Experimental results across different graph topologies show that the number of neighbours per node and the average path length are the main factors affecting the emergence of cooperation. We also show that, while partner selection fosters mutual cooperation by limiting the diversity of the opponent pool, providing agents with the identity of their opponent hinders the proliferation of cooperative strategies.

---


### 78. [AREAs-Lab: An Interactive Environment for AI-driven Requirement Elicitation for AI Systems](https://arxiv.org/abs/2608.28979)

**<font color=#1a73e8>作者：</font>** Pengshan Cai, Zihao Zhang, Ting Jin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Building effective AI systems increasingly depends on writing high-quality task requirements, yet users often struggle to articulate the constraints, preferences, and edge cases that determine success. This problem is especially acute in AI development, where behavior is shaped not only by human expectations but also by data characteristics. We present AREAs-Lab, an interactive environment for AI-driven Requirement Elicitation for AI systems. In AREAs-Lab, an assistant iteratively refines an initially incomplete requirement by analyzing the underlying dataset and asking targeted clarification questions to uncover the user's latent intent. To study this setting systematically, we construct a synthetic benchmark grounded in 16 public datasets spanning diverse domains and task types. Each benchmark instance includes a user profile, a complete reference requirement, and an intentionally underspecified version that serves as the assistant's starting point. We further introduce an automated evaluation pipeline based on an AI-simulated user that reveals hidden information only when appropriately prompted, enabling scalable and reproducible assessment of interactive elicitation quality. AREAs-Lab provides a controlled testbed for studying how AI assistants can transform vague user goals into actionable requirements for AI systems.

---


### 79. [V2TATC: A Joint Voice-Trajectory Embedding Framework and Dataset for Air Traffic Controller Situational Awareness](https://arxiv.org/abs/2608.28981)

**<font color=#1a73e8>作者：</font>** Louis Brusset, Mathurin Petit, Jordan Kam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As air traffic volumes in the National Airspace System continue to expand, in particular in the low altitude airspaces, the need for scalable decision support tools used by air traffic controllers will also require more development. This article introduces Voice-to-Trajectory for Air Traffic Control, a joint voice communication-flight trajectory data embedding framework, that can be a component of situational awareness in congested airspaces, and assist the development of tools for ATC as they reason in real-time over Automatic Dependent Surveillance-Broadcast trajectories, or the intent expressed by pilots in natural language. We show that these data modalities are not independent and represent a common physical referent: an aircraft flying through the airspace. V2TATC maps a voice instruction and the trajectory of the addressed aircraft to nearby points in a single latent space that can be queried in both directions. It combines a self-supervised trajectory encoder, a frozen large-scale speech encoder, a contrastive joint embedding, and a bijective lifting via normalizing flows. We demonstrate V2TATC's effectiveness on the San Francisco Bay Area, for its concentration of major airports, and its mix of commercial and general aviation low altitude traffic. Lastly, we release a novel paired voice-trajectory dataset, and report experiments on cross-modal retrieval, ablations, and latent-space analysis.

---


### 80. [FractureFields: Contact-Aware Binary Multi-Field Transfer for Fractured 3D Gaussian Simulation](https://arxiv.org/abs/2608.28982)

**<font color=#1a73e8>作者：</font>** Jianchen Wang, Runyang Qu, Fei Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physics-integrated 3D Gaussian representations make it possible to simulate image-reconstructed assets directly as particles, but current Gaussia-MPM pipelines keep a single Eulerian velocity field even after fracture. When disconnected fragments share interpolation support, they still write to and read from the same grid nodes, producing cross-fragment momentum leakage that appears as residual adhesion and non-physical stretching. We present FractureFields, a topology-adaptive transfer for fractured 3D Gaussian objects. After a structural event assigns persistent fragment identities, FractureFields builds fragment-specific mass and momentum fields in a single P2G pass, advances each field independently, and performs a field-aware G2P update so particles only sample their own fragment's grid state. To handle re-contact, we add a momentum-conserving contact projection that applies equal and opposite normal impulses only when two fragment fields are approaching, preserving free separation otherwise. Experiments on reconstructed scenes and a controlled re-contact benchmark show that fragment-conditioned routing eliminates realized cross-fragment mixing by construction, while contact projection reduces interpenetration during collision without reintroducing residual coupling. Overall, we argue that post-fracture simulation should treat structural disconnection as a change in local dynamical state, not merely a change in constitutive stress.

---


### 81. [CARVY-FL: Client Anticlustering for Robust Voting in Provably Secure Federated Learning](https://arxiv.org/abs/2608.28992)

**<font color=#1a73e8>作者：</font>** Masaki Nakada, Honoka Anada, Tatsuya Kaneko 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables collaborative training without directly sharing raw data, but remains vulnerable to malicious clients. Voting-based FL improves robustness by partitioning clients into groups, training one model per group, and aggregating predictions by plurality voting. However, under class-disjoint non-IID data, distribution-oblivious grouping can yield highly variable certified accuracy (CA). We propose CARVY-FL, which estimates client distribution types from one-epoch model updates and uses anticlustering to increase within-group distributional diversity. Under a fixed grouping, CARVY-FL retains the voting-based CA guarantee while increasing vote margins. Experiments on MNIST and Fashion-MNIST show higher CA than FLCert. Under BadNets with model replacement, CARVY-FL improves the AUC of 100-ASR by 11.1% and 14.9%, respectively.

---


### 82. [Verification abundance, adjudication scarcity: what happens to mathematical knowledge when proof checking becomes free](https://arxiv.org/abs/2608.28997)

**<font color=#1a73e8>作者：</font>** Maher Kallel, Mohamed El Louadi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In May 2026 an OpenAI model produced a counterexample to the Erdős unit distance conjecture. Five mathematicians published a human-verified version the same day, and the result entered the literature within weeks. In August 2026 the same laboratory published ten mathematical and theoretical computer science results, each accompanied by a machine-checkable Lean 4 certificate with no unproved steps. Four weeks later, one remained the subject of an unresolved dispute over whether its formalization meant what it claimed.
We argue that this difference is structural. We distinguish three layers of verification: derivational validity, which a kernel checks; representational fidelity, whether the formal statement means the intended question; and epistemic significance. Only the first is mechanizable. Making it effectively free therefore does not eliminate verification work but shifts the burden to layers dependent on scarce expert attention.
Measurements of the August corpus illustrate the shift. The kernel-checked proofs total 20.6 MB, while the statements requiring human audit total 55.6 KB, a ratio of 379 to 1. Yet those statements contain 218 bespoke definitions rather than relying on community-vetted ones. The audit surface is therefore small in volume but irreducibly expert. We argue that machine checking produces verification abundance while leaving adjudication scarce. We propose a six-category taxonomy of representational mismatch, a disclosure schema for machine-generated mathematical claims, and implications for software, cryptography, and regulated decision systems.

---


### 83. [Effective Graph and Rank-based Contextual Embeddings for Textual and Multimedia Data](https://arxiv.org/abs/2608.29001)

**<font color=#1a73e8>作者：</font>** Thiago César Castilho Almeida, Gustavo Rosseto Letício, Lucas Pascotti Valem 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In a data-driven world, efficiently organizing and mapping relationships between objects is crucial. Graphs are powerful tools for modeling these connections, being widely used in social networks, telecommunications, and biology. However, graph-based methods often face high computational costs, particularly in memory and space usage. To address this, graph embedding techniques, also referred to as Network Representation Learning, encode graph information into lower-dimensional representations while preserving structural aspects. Traditional methods, however, lack interpretable dimensions. RaDE (Rank Diffusion Embedding) introduces a new approach using rank-based information, with a key step being the selection of a representative subset of nodes to provide interpretability for its dimensions and improve retrieval tasks. Despite its potential, RaDE's original proposal did not fully explore the effectiveness of representative subset selection across different classes or evaluate embeddings in tasks like classification and clustering. Inspired by RaDE, this work introduces GRaCE (Graph and Rank-based Contextual Embeddings), a fully unsupervised framework that generates interpretable embeddings by leveraging robust rank-based measures for representative subset selection and node embedding. GRaCE surpasses RaDE and Original Features across diverse datasets, including textual and image collections, excelling in retrieval, classification, and clustering tasks, considering state-of-the-art Transformer models as feature descriptors and Graph Convolutional Networks models in classification tasks.

---


### 84. [RoSe-SLAM: Robust Semantic-Aware Gaussian Splatting SLAM from Dynamic Monocular Videos](https://arxiv.org/abs/2608.29003)

**<font color=#1a73e8>作者：</font>** Wenting Wang, Jiaxin Guo, Wenzhen Dong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In dynamic and unstructured environments, conventional SLAM systems generally suffer from significant accuracy degeneration due to their static assumptions. In this work, we propose Robust Semantic-aware Gaussian Splatting SLAM (RoSe-SLAM), to address the dynamic challenge by a holistic semantic scene understanding from uncalibrated monocular inputs, achieving accurate camera tracking and high-quality geometry reconstruction. Unlike conventional semantic SLAM using handcrafted semantic labels, our RoSe-SLAM exploits the semantic feature from 2D foundation model to enhance the dynamic tracking and mapping performance. By distilling the rich semantic features to our Gaussian fields, our method effectively identifies dynamic distractors and achieves semantic-aware multi-view consistency, significantly enhancing the geometric reconstruction and scene inpainting. Specifically, we propose a spatial-temporal motion mask generation module, enabling both long-term motion monitoring and short-term transient dynamics capturing, achieving robust and effective disentanglement of dynamic objects and static backgrounds. During global bundle adjustment, we propose an occlusion-aware keyframe selection mechanism to prioritize the occlusion as metric to pick the keyframes, and a multi-view semantic consistency module to improve the mapping quality in dynamic environments. By combining geometric motion cues with semantic priors, our system dynamically filters unreliable observations and reconstructs accurate static scene geometry. Extensive experiments conducted on benchmark datasets including dynamic TUM, Bonn and Wild-Mocap datasets, demonstrate that our method achieves superior performance in both trajectory estimation and static scene mapping, outperforming existing dynamic RGB SLAM baselines in long-term dynamic indoor environments.

---


### 85. [Context-Aware Interpretable Representations for Retrieval and Graph Convolutional Network Classification](https://arxiv.org/abs/2608.29004)

**<font color=#1a73e8>作者：</font>** Thiago César Castilho Almeida, Gustavo Rosseto Letício, Vinicius Atsushi Sato Kawai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The advances in visual information modeling and representation during the last decades are remarkable, mainly supported by Convolutional Neural Networks, Transformer-based, and Foundation Models. Despite this progress, critical challenges regarding the nature of similarity assessment and model transparency have been neglected. A primary concern is the Geometric Gap, where traditional pairwise measures fail to capture the intrinsic geometry of the dataset manifold. Furthermore, the Interpretability Gap persists, as representations often lack alignment with human cognition. Therefore, how to provide interpretability to representations while maintaining low dimensionality and high effectiveness in downstream tasks remains an open challenge. In this paper, we propose a novel unsupervised framework that integrates Manifold Learning strategies with Rank-based Interpretable Graph Embeddings. Our approach effectively bridges these gaps by first characterizing the contextual information of the dataset through manifold analysis and subsequently generating sparse, self-explainable embeddings. The proposed approach employs a flexible formulation, allowing different Manifold Learning and Representation Learning strategies. Extensive experimental evaluation across diverse datasets and features demonstrates that our Context-Aware representations not only provide intrinsic interpretability and dimensionality reduction but also maintain or enhance effectiveness in downstream tasks, specifically in image retrieval and semi-supervised classification using Graph Convolutional Networks (GCNs).

---


### 86. [Multi-Step Forecasting of Grape Berry Temperature based on LSTM Model with Feed-Forward Attention](https://arxiv.org/abs/2608.29008)

**<font color=#1a73e8>作者：</font>** Srikanth Gorthi, L. G. Divyanth, Dattatray Bhalekar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate forecasting of grape berry temperature (Tb) is essential for enabling timely heat stress management in vineyards. In this study, a feed-forward attention mechanism integrated with a Long Short-Term Memory network (FAM-LSTM) was developed and evaluated for multi-step, high-resolution Tb prediction. Models were trained using environmental data from 2023 and 2024 at Prosser, WA, USA, and validated on 2025 summer data. FAM-LSTM was benchmarked against LSTM, GRU, RNN, and Random Forest (RF) across horizons ranging from 15 minutes to 72 hours (288 time steps). Two input scenarios were evaluated: nearest open-field weather station observations and in-vineyard microclimate measurements. FAM-LSTM consistently outperformed all benchmark models across all horizons and input scenarios. Incorporating in-vineyard microclimate data significantly improved forecasting accuracy at longer horizons. Using open-field data, FAM-LSTM achieved MAE and RMSE ranges of 0.58 to 1.70 deg C and 0.65 to 2.07 deg C, respectively. In-vineyard observations further improved performance, with MAE and RMSE in the ranges of 0.51 to 1.55 deg C and 0.71 to 1.87 deg C. Error analysis showed prediction uncertainty was highest during peak daytime periods (11:00 to 18:00) and increased progressively with forecast horizon. Overall, the FAM-LSTM framework offers robust Tb forecasting to support precision heat stress management in vineyards.

---


### 87. [How Mental Health Self-Disclosure Becomes Visible: Evidence from Eight Conditions on Reddit](https://arxiv.org/abs/2608.29010)

**<font color=#1a73e8>作者：</font>** Renkai Ma, Lingyao Li, Shanting Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People share mental health diagnoses on social media, yet how such language becomes visible around their self-disclosure, and whether community engagement tracks it, remain unexamined across conditions. We analyze 89,605 Reddit posts from 739 users across eight conditions, removing each user's diagnosis disclosure and aligning their surrounding posts to that anchor. Within the pre-disclosure year, language-visible burden was highest in the month before disclosure for six conditions, earlier for post-traumatic stress disorder and furthest from it for borderline personality disorder, and remained visible afterward rather than resolving. The theme Seeking Clinical Explanations showed the largest early-to-late difference before disclosure in five conditions, yet engagement rarely tracked what users wrote: only 9 of 360 language--engagement correlations survived correction. Disclosure is therefore a waypoint in an unevenly visible process, and we offer implications for community practice and platform design where engagement metrics do not reflect clinical need.

---


### 88. [Frequency Selective Neural Networks as a Foundation Architecture for Time Series Learning](https://arxiv.org/abs/2608.29012)

**<font color=#1a73e8>作者：</font>** Hui Huang, Ye Sun, Shiyan Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time-series data across physical and biological domains are fundamentally driven by complex, non-stationary oscillatory modes. While deep learning models, such as Convolutional Neural Networks (CNNs), Recurrent Neural Networks, and Transformers, have dominated sequential analysis, they remain fundamentally "spectral-blind". By mapping continuous physical waves into unconstrained spatial or discrete token spaces, these architectures suffer from severe spectral entanglement, acting as opaque black boxes that decouple predictive accuracy from physical reality. In this paper, we introduce the Frequency Selective Neural Network (FSNN), pioneering a foundation architecture guaranteeing physical interpretability without sacrificing expressive power of deep learning. FSNN addresses spectral entanglement by explicitly embedding the rigorous mathematics of advanced signal processing into its neural topology. Through a fully differentiable Wiener-like filter bank optimized via complex-domain backpropagation, FSNN autonomously discovers and isolates the precise physical modes of a given task. Extensive evaluations demonstrate that FSNN establishes state-of-the-art predictive performance, achieving $77.0\%$ average accuracy on the standard 10 multivariate UEA datasets and leading across all major metrics on the highly imbalanced PTB-XL clinical ECG benchmark. Crucially, in contrast to yielding abstract feature maps, FSNN converges directly on physically meaningful frequency bands, such as isolating the cardiac QRS complex, providing a highly scalable, interpretable paradigm for robust pattern recognition in complex temporal domains. Our code is available at: this https URL.

---


### 89. [Disentangling Representation using Attributes-based Gaussian Estimation for Medical Sound Diagnosis](https://arxiv.org/abs/2608.29026)

**<font color=#1a73e8>作者：</font>** Ke Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep learning has a powerful capability of feature extraction. However, the lack of fairness and interpretability in deep neural networks poses limitations to their adoption in the medical domain. This paper proposes a disentangled representation learning (DisenRL) framework, named the Attributes-based Gaussian Estimation for Disentangled Representation (AGEDR), which incorporates Attribute Mapping Embedding (AME) modules designed to map attributes into vectors and align them with a subset of the latent vectors in a Variational AutoEncoder (VAE). This part of the latent vector will be disentangled from the remaining latent vectors by minimizing mutual information. A classifier is then trained using the mean parameters of the latent vectors from the VAE. Extensive experiments demonstrate that AGEDR outperforms both conventional classification models and existing disentangled representation learning methods. The ablation experiments also indicate the disentangling capability and fairness of AGEDR. The source code is publicly available at this https URL.

---


### 90. [Explainable Multi-Loss Distillation Framework for Efficient and Interpretable Shrimp Disease Text Classification](https://arxiv.org/abs/2608.29027)

**<font color=#1a73e8>作者：</font>** Anh Nguyen Quynh, Khang Nguyen Quoc, Luyl-Da Quach  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Shrimp disease classification has become an urgent issue due to its significant impact on the import-export output of producing countries, particularly Vietnam. Most existing studies focus on image-based classification, which typically operates at the late stage of disease manifestation. Therefore, text-based classification has the potential to enable early and timely disease detection. To address this limitation, we introduce the SALT (Shrimp disease text Analysis with multi-Loss disTillation) framework, which incorporates explainability analysis using Local Interpretable Model-agnostic Explanations (LIME) and SHapley Additive exPlanations (SHAP) to evaluate model predictions and interpret the learned linguistic features. Experimental results demonstrate that SALT achieves competitive performance across multiple distillation objectives, outperforming supervised baselines while providing a favorable trade-off between predictive performance and computational efficiency. Moreover, it exhibits strong explainability, accurately identifying key linguistic features and semantic patterns relevant to disease descriptions. These findings highlight the potential of knowledge distillation-based text classification for future applications in early shrimp disease diagnosis and related research directions.

---


### 91. [Flow-JEPA: Flow Matching for Robust Latent Dynamics in JEPA World Models](https://arxiv.org/abs/2608.29029)

**<font color=#1a73e8>作者：</font>** Yanchen Huo, Ziying Song, Yadan Luo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Joint-Embedding Predictive Architectures (JEPAs) have shown strong potential for learning compact predictive representations, and LeWorldModel (LeWM) extends this paradigm to reconstruction-free latent world modeling from pixels. However, its deterministic autoregressive predictor generates future states through repeated one-step transitions, which can accumulate errors and remain sensitive to task-irrelevant visual perturbations. In this work, we propose Flow-JEPA (F-JEPA), a conditional flow matching dynamics model that jointly generates a sequence of future latent states conditioned on the current observation and actions. A Gaussian distribution serves as the flow source, exposing the vector field to perturbed latent trajectories as it learns to transport them toward clean future representations. This formulation retains the reconstruction-free JEPA framework while replacing point-wise transition regression with stochastic trajectory-level prediction. F-JEPA raises mean success from $86\%$ to $92\%$ under clean observations and from $67\%$ to $86\%$ under noisy conditions, suggesting that conditional flow matching provides a promising alternative to deterministic autoregressive dynamics in JEPA world models.

---


### 92. [sRGB Real Noise Modeling via Noise-Aware Sampling with Normalizing Flows](https://arxiv.org/abs/2608.29038)

**<font color=#1a73e8>作者：</font>** Dongjin Kim, Donggoo Jung, Sungyong Baik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Noise poses a widespread challenge in signal processing, particularly when it comes to denoising images. Although convolutional neural networks (CNNs) have exhibited remarkable success in this field, they are predicated upon the belief that noise follows established distributions, which restricts their practicality when dealing with real-world noise. To overcome this limitation, several efforts have been taken to collect noisy image datasets from the real world. Generative methods, employing techniques such as generative adversarial networks (GANs) and normalizing flows (NFs), have emerged as a solution for generating realistic noisy images. Recent works model noise using camera metadata, however requiring metadata even for sampling phase. In contrast, in this work, we aim to estimate the underlying camera settings, enabling us to improve noise modeling and generate diverse noise distributions. To this end, we introduce a new NF framework that allows us to both classify noise based on camera settings and generate various noisy images. Through experimental results, our model demonstrates exceptional noise quality and leads in denoising performance on benchmark datasets.

---


### 93. [Sharing Roughness with Hand-Outline Visualization to Reduce Sensory Asymmetry in VR Collaboration](https://arxiv.org/abs/2608.29040)

**<font color=#1a73e8>作者：</font>** Minju Baeck, Yoonseok Shin, Hyunjin Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In collaborative VR, asymmetric access to haptic hardware creates a critical information gap: tactile evidence remains private to the haptic user, hindering the shared understanding needed for joint decision-making. While prior work has explored crossmodal sensory cues in virtual environments, it remains unclear how such cues should be designed for asymmetric collaboration, where collaborators receive information through different modalities. In our setting, the haptic user feels roughness through fingertip vibration, whereas the non-haptic user relies on vision alone. To reduce this asymmetry, we propose externalizing an object's tactile state through a glanceable hand-outline visual proxy. Specifically, we examine whether abstract visual roughness cues based on line shape and motion can encode three discrete roughness levels for both haptic and non-haptic users. Two preliminary studies establish a shared visual semantics by identifying visually distinguishable cues for non-haptic users and validating their visuo-haptic correspondence for haptic users. In a main study of a collaborative sorting task, showing this visualization on both users' hands significantly reduced completion time relative to a no-visualization baseline. Moreover, NU-side cue visibility was associated with higher confidence and perceived contribution for the non-haptic user. These findings show that hand-anchored abstract visual cues provide a lightweight means of externalizing object tactile state, reducing information asymmetry without compromising social presence.

---


### 94. [Di$^2$CycleSB: Towards High-Quality Unsupervised Nighttime Visibility Enhancement via Schrödinger Bridge Transformer](https://arxiv.org/abs/2608.29043)

**<font color=#1a73e8>作者：</font>** Hanting Li, Xin Sun, Wei Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Light-effect contamination poses a significant challenge to nighttime visibility enhancement. Most methods suppress light effects by estimating and decomposing them through prior-driven regularization, yet they are often limited by hand-crafted priors and ill-posed nature of decomposition. This work proposes Di$^2$CycleSB, a unsupervised Cycle Schrödinger Bridge Transformer framework guided by dynamic integral image priors, for high-quality unsupervised nighttime visibility enhancement. Specifically, a novel light-effect estimator is introduced to parameterize Gaussian-like adaptive priors by aggregating dynamic integral image representations for non-uniform glow estimation. Then, we propose a prior-informed Generator that exploits light-effect representations to guide long-range dependency modeling within our specific Transformer blocks. We formulate light-effect suppression as a Schrödinger bridge problem and construct forward and backward bridges with cycle consistency constraints to achieve visually pleasing enhancement. Extensive experiments on real-world datasets demonstrate the remarkable effectiveness of our Di$^2$CycleSB in enhancing nighttime visibility. In particular, it achieves effective end-to-end light-effect suppression without any regularization constraints and image decomposition. The code and models are available at this https URL.

---


### 95. [NVE: A Separability and Coverage-Aware Internal Validation Metric for Biclustering](https://arxiv.org/abs/2608.29045)

**<font color=#1a73e8>作者：</font>** Paritosh Tiwari, I Navin Kumar, James C. Bezdek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Biclustering, or co-clustering, aims to discover coherent submatrices by grouping rows and columns of a data matrix simultaneously. This local two-dimensional structure makes validation more difficult than in ordinary clustering, where internal indices usually rely on compactness and separation in a single shared feature space. Existing popular internal biclustering measures such as Mean Squared Residue (MSR), and Virtual Error (VE) mainly evaluate within-bicluster coherence. Although useful, these measures do not directly assess whether the extracted biclusters are mutually distinct or whether they explain a meaningful portion of the data matrix. This paper investigates Normalised Virtual Error (NVE), an internal validation metric that extends VE using a super-bicluster normalization strategy. By comparing the VE of each bicluster with the VE obtained after merging it with other biclusters, NVE introduces a relative notion of separability and redundancy. We also study a coverage-adjusted variant, NVE\textsubscript{cov}, which penalizes solutions that obtain low error by selecting only very small submatrices. Through controlled synthetic benchmarks and yeast gene-expression datasets, we examine whether NVE and NVE\textsubscript{cov} provide information beyond standard coherence-based metrics. The results show that NVE is sensitive to redundant and poorly separated biclusters, while NVE\textsubscript{cov} changes solution rankings when low-error biclusters cover only a negligible part of the matrix. These findings suggest that NVE-based measures are useful complementary criteria for internal co-clustering validation, especially when coherence, separability, and coverage must be considered jointly.

---


### 96. [DReSG: Diffusion Residuals for Stylized Gaussian Splatting](https://arxiv.org/abs/2608.29048)

**<font color=#1a73e8>作者：</font>** Zhongliang Liu, Wenjie Liu, Yang Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference-guided stylization of scenes represented by 3D Gaussian Splatting (3DGS) is important for efficient and controllable 3D content creation. Existing VGG-feature-based 3D stylization methods provide stable rendered-view optimization, but often under-represent expressive reference style cues; diffusion models offer stronger image priors, yet direct per-view or score-based diffusion guidance can lead to view drift, local artifacts, and hard-to-control appearance updates. We present DReSG, a 3D-grounded residual-feedback framework for stylized Gaussian splatting. DReSG represents attention-guided diffusion proposals as residual targets relative to the current render, and progressively absorbs these residuals into a shared Gaussian scene through multi-view Gaussian feedback. To make this feedback stable and controllable, DReSG modulates residual strength during target construction and combines coverage-aware view selection with conflict-filtered color updates during multi-view fitting. Extensive experiments demonstrate that DReSG achieves competitive reference-guided stylization while better preserving scene structure and cross-view stability. Our project page is available at this https URL.

---


### 97. [Let Prompts Bridge Defense Knowledge: Transferable Graph Purification via Vulnerability-Aware GPL](https://arxiv.org/abs/2608.29054)

**<font color=#1a73e8>作者：</font>** Shuomin Xue, Jingyuan Li, Ju Jia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) have emerged as a cornerstone for representing complex relational dependencies in diverse multimedia tasks, particularly in cross-platform user interest modeling and cross-modal semantic alignment. In the real world, a practical defense against graph adversarial perturbations is needed. However, we observe that the prevailing adversarial purification methods are essentially domain-restricted defenses, which leads to the following shortcomings: (1) single-domain data provides insufficient structural and semantic diversity for learning robust purification criteria; (2) training of domain-specific defense strategies from scratch consumes substantial computational cost. To address the above limitations, we propose a transferable graph purification scheme, named ProGAP, to bridge adversarial defense knowledge via vulnerability-aware graph prompt learning. Firstly, to capture universal adversarial patterns, a perturbation-capture edge detector is pretrained on data-rich graphs by jointly modeling topological and semantic information. Subsequently, to achieve more knowledge transfer w.r.t. robustness, vulnerability-aware prompts are designed that inject targeted purification guidance into biased nodes, during which the pretrained detector adapts to distribution shifts in downstream graphs without parameter-laborious updates. Experimental results demonstrate that compared with state-of-the-art baselines, our ProGAP achieves 1%-9% improvement, and reduces the time consumption by up to 2.2x. The code for ProGAP is available at this https URL.

---


### 98. [Sparse Koopman Autoencoders Identify Local Dynamical Regimes in Multibasin Systems](https://arxiv.org/abs/2608.29057)

**<font color=#1a73e8>作者：</font>** Aidan Li, Uday Kiran Reddy Tadipatri, Mahan Fathi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Koopman autoencoders (KAEs) seek a higher-dimensional latent representation in which nonlinear dynamics evolve linearly. However, many interesting systems have multiple basins of attraction, and both theoretical and empirical work has shown these multibasin systems cannot generally admit a single finite-dimensional global Koopman embedding under standard assumptions. We posit that encoders with a sparsity-inducing objective encouraging few active latent coefficients will provide latent supports as an inspectable basin-modeling principle for Koopman autoencoders. We use these encoders producing sparse latents in training Sparse Koopman Autoencoders (SKAEs) without basin labels or other regime annotations, and treat the learned latent supports as model-produced regime variables after training. Across a range of procedurally generated multibasin systems and chaotic flows, we show that SKAEs have superior forecasting performance compared to dense-latent KAEs. We also perform a mechanistic study that shows latent supports produced by SKAEs are both essential for the quality of the representation and useful for identifying basins on held-out basin interior states, whereas dense-latent KAEs collapse to an uninformative single family. These results identify sparse latents and their corresponding supports as label-free, interpretable regime variables for Koopman learning in nonlinear systems with multiple local dynamical laws.

---


### 99. [PathBridger: Subgoal Bridges for Offline Goal-Conditioned Reinforcement Learning](https://arxiv.org/abs/2608.29061)

**<font color=#1a73e8>作者：</font>** Soohyun Choi, Seonvin Cho, Songnam Hong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline goal-conditioned reinforcement learning (GCRL) aims to learn policies for reaching diverse goals entirely from fixed trajectory data. Long-horizon offline GCRL remains challenging because sparse goal-reaching signals must be propagated over many steps, while execution errors cannot be corrected through additional environment interaction. Existing methods address these challenges by improving long-range value estimation or reducing the effective decision horizon through subgoals, options, and action chunks. In several hierarchical methods, however, a selected subgoal specifies where to go, while the intervening state-space path remains implicit in an endpoint-conditioned low-level policy. To address this interface, we propose PathBridger, a hierarchical offline GCRL method that explicitly connects subgoal selection to short-horizon execution. PathBridger constructs a state-space bridge toward the selected intermediate endpoint and decodes it into a short executable action chunk using an inverse dynamics model. Experiments across the evaluated OGBench tasks demonstrate strong aggregate performance, with particularly large gains on the multi-object Cube manipulation tasks. Code: this https URL

---


### 100. [Nested Convex-Body Chasing for Online Optimization with Evolving Feasible Sets](https://arxiv.org/abs/2608.29074)

**<font color=#1a73e8>作者：</font>** Dhruv Sarkar, Aprameyo Chakrabartty  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study online optimization with nested shrinking feasible regions in two settings: convex optimization with nested evolving feasible sets (CONES) and adversarial constrained online convex optimization (COCO). Our algorithms separate loss control from geometric movement: constrained minimizers and cumulative-loss tests preserve regret guarantees, while a deterministic resettable nested convex-body chaser limits movement.
For CONES with a $G$-Lipschitz, $\mu$-strongly convex objective on a diameter-$D$ domain, we chase intersections of the current feasible set with adaptive objective sublevel sets. Using the Euclidean chasing ratio $O(\sqrt{d\log(1+d)})$, we obtain nonpositive regret at every prefix and movement $O(\sqrt{d\log(1+d)\,GD\log(eT)/\mu})$. The bound adapts to the increase in the constrained optimum value. In dimension two, with all other parameters fixed, every randomized algorithm with terminal expected regret $O(T^\beta)$, $\beta<1$, suffers $\Omega(\sqrt{\log T})$ expected movement on some deterministic nested sequence, proving optimal horizon dependence. Under linear growth away from the constrained minimizer set, Steiner-point tracking yields movement independent of $T$.
For general convex COCO, one-step-delayed chasing with regularized-leader resets gives regret $O(G_fD\sqrt{d\log(1+d)T})$ and cumulative constraint violation $O(G_gD\sqrt{d\log(1+d)T})$. For strongly convex losses, both are $O(d\log(1+d)\log(eT))$ when other parameters are fixed. These reductions replace the $O(d^{d/2})$ projection-path factor in prior analyses by the polynomial dimension dependence of Euclidean nested convex-body chasing.

---


> [!TIP]
> 当前位于：**51-100**（第 2/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-485](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
