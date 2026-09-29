# 📦 其他研究 | 2026年09月30日

> 本类共 **908** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

---

### 51. [Fusion Under Component Failure: Negative Results and Failure Modes in Ensemble AI-Generated Image Detection](https://arxiv.org/abs/2609.31749)

**<font color=#1a73e8>作者：</font>** Suraj Singh, Tushar Verma, Pragyan Singh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We built an ordinary stacking ensemble for AI-generated image detection -- three open detectors producing five scores, fused by a gradient-boosted meta-learner that treats a detector's failure as missing data -- deployed it, and then evaluated it against three controls it should have faced first. This paper reports what the controls found, including where they overturned our own earlier conclusions.
Fusion is worth its cost only when refitted on the target domain. The shipped meta-learner, fitted on a separate corpus, does not beat its best single member on 2000 StyleGAN faces (AUC 0.9896 vs 0.9961; McNemar p = 1.000). But a stacker refitted in-domain beats that member plus a post-hoc calibrator (Delta-AUC = +0.0025, [+0.0014, +0.0038]; p = 3.4e-4). An earlier draft claimed the calibrated single detector won outright; that comparison mixed regimes and we correct it here.
One corpus is not an evaluation. On 80 screenshots every model's AUC interval contains 0.5. We can say nothing stronger: the difference between the ensemble's drop and its best member's is [-0.185, +0.115].
Abstention is real, correlated, and mishandled. With four of five detectors silent and the survivor reporting "real", the system returns P(AI) = 0.9985, because an all-NaN input scores 0.9995 in a learner never fitted with missingness. The three AIDE checkpoints fail together, sharing one preprocessing path. A quorum rule requiring two distinct architectures prevents both failures with no retraining.
We also find Corpus A carries a class-conditional JPEG bias severe enough to separate the classes from the header alone, which limits every in-domain number we report. Code, harness, hash-identified artifacts and all corrections are released.

---


### 52. [Dimension-Specific Imbalance and an Adaptive Hybrid Label Strategy for Multi-Task Affective State Recognition in Classroom Video](https://arxiv.org/abs/2609.31750)

**<font color=#1a73e8>作者：</font>** Xiangqian Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recognition of student affective states from classroom video is constrained by a class imbalance problem whose true nature is, we argue, under-analyzed. We show that on DAiSEE -- the de facto benchmark for this task -- class imbalance is fundamentally a dimension-specific phenomenon: raw imbalance ratios reach as high as approximately 79:1 (Frustration), and the structure of imbalance -- not only its magnitude -- varies across dimensions, so uniform algorithmic treatments (aggressive class reweighting, focal loss, uniform binary simplification) fail in dimension-dependent ways. We propose the Adaptive Hybrid Label Strategy (AHLS), which assigns four-level classification to dimensions with manageable imbalance and binary classification to severely long-tailed dimensions, coupled with a null-class placeholder mechanism that stabilizes multi-task optimization by compressing the maximum effective inverse-frequency weight ratio from as high as ~79$\times$ to at most ~8.5$\times$ across the four dimensions. Validated on a lightweight FERShuffleNetV2 + LTCN architecture (0.39 M parameters, 0.07 G FLOPs), the strategy attains the highest mean Macro-F1 of 47.70% across all four affective dimensions among 11 compared methods, including five state-of-the-art deep models (up to 167$\times$ larger) and five traditional machine-learning baselines. A cross-model behavioral analysis on DAiSEE indicates that, in this setting, classification strategy may influence minority-state recognition more strongly than further backbone scaling alone. We also report evidence of an annotation-density limitation of DAiSEE on minority affective states, which suggests that benchmark design may bound future progress as much as algorithmic refinement. Index Terms Affective computing, classroom video analysis, class imbalance, multi-task learning, lightweight deep learning, DAiSEE, engagement recognition.

---


### 53. [Calibration-Free Surface Normals Estimation in Vision-Based Tactile Sensing using Universal Photometric Stereo](https://arxiv.org/abs/2609.31754)

**<font color=#1a73e8>作者：</font>** Zdravko Dugonjic, Stefanie Speidel, Roberto Calandra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-based tactile sensors are a popular solution for capturing rich contact surface geometry. However, to obtain high-detail contact surface normals and depth, it is necessary to calibrate the sensor by physically pressing a probe with known geometry against the sensor elastomer and mapping tactile images onto the ground truth probe's shape. This approach does not scale across different tactile sensors, and the calibration effort can be complex depending on the sensor shape and optical system. Instead, we propose a calibration-free procedure for the estimation of contact surface normals using Universal Photometric Stereo neural networks. In a series of real-world experiments, we evaluate our approach on 3 sensors with different optical systems, demonstrating that universal methods are a suitable approach for estimating surface normals at the contact patch from tactile images, thereby alleviating the need for tactile sensor calibration. Controlled experiments with a metal ball show that universal methods match the calibrated method, with a mean angular error of $6.56^{\Large\circ}$. We show that the proposed framework recovers high-frequency surface details of objects with natural textures, achieving an overall mean angular error of $10.66^{\Large\circ}$. Universal method robustly recovers the contact surface normals captured with dome-shaped Digit 360, achieving a low angular discrepancy of $10.18^{\Large\circ}$ relative to the calibrated baseline. This experiment demonstrates that with sufficient illumination settings surface normals could be estimated using a model trained solely on synthetic data. By providing a unified representation of contact surfaces across different vision-based tactile sensor designs, Universal Photometric Stereo neural networks lay the foundation for transferable tactile perception across sensors.

---


### 54. [Gauge-Equivariant Attention for Rotation-Stable $360^\circ$ Scene Understanding](https://arxiv.org/abs/2609.31755)

**<font color=#1a73e8>作者：</font>** Tianjian Zhou, Yishan Li, Jie Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Panoramic $360^\circ$ scene understanding increasingly relies on icosphere transformers, but a state-of-the-art spherical model loses more than half of its segmentation accuracy when the camera rotates by $90^\circ$, and controlled ablations identify gauge dependence in its relative-position bias as a major contributor. We propose gauge-equivariant relative position encoding (GE-RPE): a parameter-free Reynolds average of the bias over a finite cyclic subgroup $C_n\!\subset\!\mathrm{SO}(2)$ of gauge rotations. Plugged into a SphereUFormer backbone the change is invisible at deployment---zero added parameters and $1.5$--$4.4\%$ forward latency---and the matched three-seed GE-RPE model records a $1.3\%$ drop; the published SphereUFormer checkpoint records $53\%$ under the same stress protocol but a different training recipe. Once the gauge defect is removed and a teacher-token permutation $\pi_R$ aligns the SSL views to the rotated student frame, iBOT$+$MAE pretraining stops being a liability and becomes a clean low-label lever: the full framework EquiSSL (GE-RPE $+$ $\pi_R$ $+$ iBOT$+$MAE) tightens the drop to $0.8\%$ at $68.30\%$ val mIoU and lifts $1\%$-label fine-tuning by $+2.39$ mIoU on the $N{=}373$ test split (and by $+4.10$ on the smaller $N{=}40$ val split); the same fix carries over to monocular depth and to zero-shot Structured3D segmentation. The construction is provably $C_n$-invariant and $\mathcal{O}(n^{-2})$-close to the continuous $\mathrm{SO}(2)$ average, making the resulting model a usable $360^\circ$ visual-computing primitive across panoramic relighting, immersive video, and cross-dataset transfer. Code is available at this https URL.

---


### 55. [3dgs-sc: a controlled static screen-content benchmark for 3d gaussian splatting](https://arxiv.org/abs/2609.31756)

**<font color=#1a73e8>作者：</font>** Shicheng Cai, Hao Zhang, Dong Dai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Does high image fidelity imply readable screen content in 3D Gaussian Splatting (3DGS)? We introduce 3DGS-SC, a controlled static screen-content dataset and benchmark for examining this mismatch. Ten procedural scenes provide fixed multi-view splits, exact cameras, screen masks, text boxes, and transcripts. The protocol separates whole-image fidelity, screen-region fidelity, OCR readability, and edge preservation. In the reported five-method comparison, LightGaussian exceeds Mip-Splatting in screen PSNR by only 0.08 dB, yet trails it in OCR accuracy by 12.7 percentage points. Across all ten method pairs, screen-PSNR and OCR orderings disagree in seven cases. These aggregate results expose a method-selection failure of fidelity-only evaluation. Complementing prior text-aware 3DGS research, 3DGS-SC targets controlled monitor interfaces and exact annotations; scene-wise robustness and acquisition effects remain open validation questions.

---


### 56. [SMARtCARE: Privacy-Preserving Agentic AI Systems for Bounded-Autonomy Clinical Decision Support](https://arxiv.org/abs/2609.31763)

**<font color=#1a73e8>作者：</font>** Srini Ramaswamy, Deveeshree Nayak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context clinical AI systems can miss relevant patient history when prior admissions fall outside the active reasoning context. In ICU monitoring, this can cause early vital-sign drift to appear nonspecific even when it resembles a prior deterioration pattern. SMARtCARE addresses this gap through a four-state clinical decision-support architecture: Stable, Meta-cognitive, Assisted, and Regulated (Revoked). Rather than automatically retrieving prior records, SMARtCARE uses a lossy six-channel fingerprint of the patient's prior trajectory. When current drift matches that fingerprint and the prior record is absent from context, the system raises a Meta-cognitive escalation for clinician review; full retrieval occurs only through clinician action in the Assisted state. A patient-identity guard is designed to enforce correct attribution across data loading, logging, and audit layers. Evaluation combines a synthetic Monte Carlo study that validates the state-transition logic and estimator stability, not clinical performance, with real-data runs on both the MIMIC-III and MIMIC-IV Clinical Database Demos. On MIMIC-III, one prior-pattern recurrence was identified among 14 two-admission patients; on MIMIC-IV, the same pipeline produced no fingerprint matches among 9 two-admission patients, which illustrates a key limitation of a fixed canonical pattern library. Across both runs all logged decisions were fully traceable and correctly attributed. The results support SMARtCARE as a traceable, privacy-aware mechanism for surfacing middle-context risk; they are not a clinical efficacy claim.

---


### 57. [HGPTrans: Hierarchical Graph-Pooling Transolver for Automotive Aerodynamic Drag Coefficient Prediction](https://arxiv.org/abs/2609.31765)

**<font color=#1a73e8>作者：</font>** Bo Liu, Qiuli Luo, Lianrui Nie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate and rapid prediction of the aerodynamic drag coefficient ($C_D$) is essential for vehicle design, particularly during early-stage styling iterations where a large number of candidate geometries must be evaluated. Although computational fluid dynamics (CFD) provides reliable aerodynamic estimates, its high computational cost, typically requiring hours to days for a single configuration, limits its use in large-scale design exploration. This paper proposes HGPTrans, a hierarchical graph-pooling network with Transolver-based attention, to directly predict $C_D$ from vehicle surface meshes. Motivated by the fact that vehicle aerodynamics depends on both local geometric features and long-range interactions among spatially distant surface regions, HGPTrans integrates three complementary components. Graph isomorphism convolutions encode discriminative local geometry, physics-aware slice attention captures global interactions with linear computational complexity, and information-redundancy-aware hierarchical pooling progressively removes redundant nodes while preserving informative geometric structures. The model is trained and evaluated on the large-scale DrivAerNet and DrivAerNet++ datasets, where it achieves the lowest mean absolute error and mean squared error among the evaluated baselines. Its generalization capability is further assessed through transfer learning on a real-vehicle dataset containing both sedans and SUVs, achieving relative $L_1$ errors of 1.56% (sedans) and 2.12% (SUVs) with an inference time of approximately $0.293$ s per vehicle. This corresponds to an acceleration of several orders of magnitude relative to high-fidelity CFD while keeping the predicted drag coefficients within a few percent of the CFD reference. Ablation studies confirm each component's contribution and reveal the effects of depth and pooling ratio.

---


### 58. [UNMATCH: Selective Unbalanced Token-Patch Matching for Forensic Image-Claim Verification](https://arxiv.org/abs/2609.31766)

**<font color=#1a73e8>作者：</font>** Xinjin Li, Lian Lian, Yuanzhe Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contextual image misuse pairs an image with a misleading claim. We study image-claim correspondence in fact-checked pairs containing out-of-context reuse, visual manipulation, or both. Existing pair-based detectors often compress the two modalities into a global compatibility score or learn a highly flexible interaction module, which can obscure a decisive local mismatch. We introduce directional multiscale coverage, a compact representation that summarizes local image-claim affinity in both directions and at three spatial scales. At each scale, each direction is summarized by its mean, lower quartile, and two thresholded support ratios; the signed difference between directional means completes a nine-dimensional scale descriptor. Concatenating the three scales yields a compact local representation for a lightweight global-local classifier. Under leakage-aware three-fold, three-seed evaluation on the Snopes subset of the Fauxtography benchmark, UNMATCH achieves 69.82 Macro-F1 and 71.05 balanced accuracy, exceeding the MCOT adaptation by 2.60 and 2.16 points. A matched-reassigned intervention shows that breaking the observed pairing lowers coverage and increases both discrepancy and false-pair probability.

---


### 59. [Panoptic Scene Program Diffusion Transformer](https://arxiv.org/abs/2609.31780)

**<font color=#1a73e8>作者：</font>** Chika Maduabuchi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern text-to-image models produce high-fidelity images but still struggle with compositional prompts that require instance identity, attribute ownership, counting, spatial ordering, and role-sensitive relations. We introduce Panoptic Scene Program Diffusion Transformer (PSP-DiT), a diffusion-transformer architecture that treats a panoptic scene program as a first-class latent variable rather than an external control signal or post-hoc parse. PSP-DiT jointly denoises image latents and scene-program latents through coupled transformer streams, while panoptic grounding and cycle-consistency objectives tie object instances, attributes, relations, and counts to visual support in the generated image. Under matched training and inference settings, PSP-DiT improves over a strong flat-text baseline across GenEval 2, SANEval-Simple, PSG-Score, and DetailMaster, with the largest gains on counting, attribute binding, role-sensitive relations, and long structured prompts. The method preserves image quality, adds modest inference overhead, and remains robust to imperfect scene programs.

---


### 60. [Working with AI: A Design Framework for Human-AI Collaboration](https://arxiv.org/abs/2609.31793)

**<font color=#1a73e8>作者：</font>** Yuqian Lu, Regina Lee, Rui Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI), particularly GenAI, is becoming an increasingly important part of modern work. In industrial settings, AI can support decision-making, automate routine activities, assist humans, and improve productivity. However, successful AI adoption depends on more than what the technology can do. It also depends on how people experience and work with it. This raises an important question: how should human-AI collaboration be designed so that it works well for both people and organisations? This white paper addresses that question by presenting a practical framework for designing human-AI collaboration. The framework considers the human, the AI system, the task, the organisation, and the wider societal environment. It explains what effective collaboration looks like, what conditions influence it, what requirements should be met, and what design decisions organisations should consider. The report also includes a human-AI collaborative assembly system with cobot use case to demonstrate how the framework can be applied in practice. The use case shows how design requirements can be translated into specific collaboration features and evaluated through a case study. The aim of this white paper is to provide a clear and practical guide for designing human-AI collaboration that is effective, human-centred, and responsible.

---


### 61. [Rate-Adaptive One-Step Diffusion Compression for AIGC Images](https://arxiv.org/abs/2609.31795)

**<font color=#1a73e8>作者：</font>** Nitiz Khanal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We describe our entry to the LoViF 2026 AIGC Image Compression Challenge, a benchmark for ultra-low-bitrate coding of AI-generated images under a strict global rate budget of 0.025 bits per pixel (BPP). Generated imagery poses a distinct challenge for compression: it frequently contains rendered typography, synthetic edges, repeated motifs, UI-like layout, and stylized micro-texture that conventional distortion-oriented codecs erase at this rate, while unconstrained generative decoders can restore plausible-looking detail that no longer matches the source geometry or symbols. We treat this as a rate-perception allocation problem. Our system fine-tunes four rate-specialized checkpoints of the AEIC one-step diffusion codec, generates per-image candidates from all four, including one latent refined through encoder-side test-time optimization (TTO) with periodic entropy-conditioning refresh, entropy-codes every candidate with practical rANS coding, and selects exactly one bitstream per image with an exact multiple-choice knapsack solved over true coded file sizes. A fixed, zero-additional-bit residual restoration network is applied at decode time. Every submitted bitstream is independently decodable by the shipped decoder, which uses no source image or external side information. We report the full pipeline, an ablation history spanning 77 logged experiments, and a set of negative results, including why PSNR could not be pushed to parity with rate-distortion-oriented competitors under this architecture, useful to future participants. This is a challenge report: our entry scored 31.527739 (PSNR 27.02 dB, MS-SSIM 0.9176, LPIPS 0.0778, DISTS 0.0390 at 0.02495 BPP), the second-best DISTS on the leaderboard, ranking 5th on the final test-phase leaderboard announced August 4, 2026.

---


### 62. [Relational Compression: A Framework for Relational Fidelity in Constrained Representations](https://arxiv.org/abs/2609.31816)

**<font color=#1a73e8>作者：</font>** Yaniv Shulman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> What should a compressed representation preserve when the information of interest lies in relationships among elements rather than in the elements themselves? We formulate relational compression in the classical source-description-reconstruction sense, but with relational structure itself as the fidelity-bearing content. Each instance specifies the source relation, retained description, reconstructed or evaluated relation, fidelity criterion, and constrained resource. We use this interface to situate selected methods from graph summarization, spectral sparsification, similarity-preserving representation, and relational distillation within a common formulation while keeping their different reconstruction and resource assumptions explicit. We develop finite-codeword collision as one concrete realization. Same-codeword probability yields a relational geometry linking pair-specific alignment and separation to aggregate Rényi-2 occupancy and the spherical geometry of categorical assignments, with exact objective correspondences to squared-Euclidean centroid reconstruction and normalized graph association and cut. Graph and image studies illustrate complementary routes within the finite-codeword family: graph- and teacher-defined relational requirements act directly on equality or collision, while reconstruction acts through a joint decoder. Together, these results illustrate how distinct relational requirements can be formulated and tested within a common constrained-representation framework.

---


### 63. [Averaged Mirror Descent and Dual Gradient Methods: Convergent Algorithms for Entropic Gromov-Wasserstein Problem](https://arxiv.org/abs/2609.31848)

**<font color=#1a73e8>作者：</font>** Joanna Mark, Gabriel Rioux, Riccardo Passegger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Gromov-Wasserstein (GW) distance measures the discrepancy between metric measure (mm) spaces and identifies optimal alignments between them based solely on their intrinsic structure. Since it identifies isomorphic mm spaces, it provides a natural notion of distance for heterogeneous datasets which may admit isomorphic representations. In order to accelerate computation of GW distances, many practitioners employ entropic regularization to obtain an Entropic GW (EGW) problem. The most popular EGW solver is the Mirror Descent (MD) algorithm, which reduces EGW computations to an iterative process where an entropic optimal transport (EOT) problem is solved at each iteration. Despite its widespread use, the convergence of MD for this problem has only been established for restricted classes of costs. On the other hand, a recently proposed dual gradient method is available for general costs, but requires a choice of step size which depends on the regularization parameter. To address these two issues, we introduce Averaged Mirror Descent (AMD), which averages consecutive MD steps, and prove its convergence for arbitrary costs. Then, we establish that the dual gradient method with a fixed step size also converges for arbitrary costs at the cost of a more complicated iteration. In both cases, we also account for inexact iterations which are inescapable in practice. We compare the empirical performance of these methods across various settings and, in particular, show that AMD and the dual gradient method both converge on an example where classical MD fails.

---


### 64. [Metro-WM: Long-Horizon Latent Planning with Realisable Sub-Goals](https://arxiv.org/abs/2609.31868)

**<font color=#1a73e8>作者：</font>** Royson Lee, Fady Rezk, Titouan Parcollet 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model-predictive control with Joint-Embedding Predictive Architectures (JEPAs) provides a strong zero-shot goal-reaching planner, but it is only effective over short planning horizons. Hierarchical extensions attempt to bridge this gap by learning a macro planner to predict intermediate latent sub-goals to guide the micro planner. In this work, we demonstrate that unconstrained latent sub-goal prediction is fundamentally flawed. A rigorous evaluation reveals that a leading state-of-the-art macro planner routinely emits physically unrealisable sub-goals. To resolve this, we introduce Metro-WM, a hierarchical framework that issues sub-goals by retrieving genuine states from prior experience rather than generating ungrounded latent vectors. Specifically, Metro-WM constructs a graph whose vertices are observed frames from offline expert demonstrations or random-action trajectories, allowing frames from different episodes to be connected and stitched into routes to the goal. Planning over the full graph also makes the system highly robust to execution errors: if the micro planner drifts off course, Metro-WM instantly finds a new optimal path from the current state. Our experiments show that Metro-WM achieves superior long-horizon success rates of up to 37.33 percentage points over the next best hierarchical approach while being up to 10.9 times faster, requiring both 13-56 times less offline compute and fewer tuned hyperparameters. Additional analysis reveals that Metro-WM finds shorter paths than the offline demonstrations, outperforms an oracle relying on the query's own demonstration, and maintains robust performance under extremely sparse dataset conditions.

---


### 65. [Deep Reinforcement Learning for Equity Trading: Benchmarking Actor-Critic Methods with Forward Retraining](https://arxiv.org/abs/2609.31870)

**<font color=#1a73e8>作者：</font>** Bicheng Wang, Xinyi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Consistently profitable trading is difficult because equity markets are noisy, non-stationary, and only partially predictable from historical data. We benchmark five deep reinforcement learning (DRL) actor-critic methods: A2C, PPO, DDPG, TD3, and SAC, that learn trading actions end-to-end from market states, and compare them with a supervised price-forecasting baseline. Using daily data for 20 large-capitalization S&P 500 stocks from 2000 to 2020, enriched with trend-following technical indicators and log min-max scaling, we train on 2000-2018 and backtest on 2019-2020. Each agent is evaluated both when trained once and under forward retraining, in which it is retrained on all data available before each successive test window. DDPG achieves the highest annual return (55.5%), Sharpe ratio (1.38), and alpha (0.22), but also the highest market beta (1.24). TD3 and SAC offer a better risk-return balance, with Sharpe ratios of 1.37 and 1.33 and maximum drawdowns of about 25%. Forward retraining improves A2C, PPO, and SAC, leaves TD3 essentially unchanged, and reduces DDPG's annual return from 55.5% to 29.8%, consistent with TD3's greater robustness to hyperparameters. The forecasting baseline has the smallest maximum drawdown (9.6%) and the lowest beta (0.31), underscoring a trade-off between the higher returns of end-to-end DRL and the lower risk of forecast-driven strategies.

---


### 66. [TokenScanner: Detecting Backdoors and Discovering Triggers in Text-to-Image LoRAs via Full Vocabulary Scanning](https://arxiv.org/abs/2609.31878)

**<font color=#1a73e8>作者：</font>** Boliang Liu, Jing Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LoRAs are widely studied for adapting base text-to-image diffusion models. However, a backdoored LoRA can hide a backdoor: it behaves normally in most cases, but produces attacker-specified content (the backdoor target) when a hidden backdoor trigger appears in the input prompt. Detecting such backdoors before using an untrusted LoRA is important for the safety of LoRA adaptation. We present TokenScanner, a model-level vocabulary scanner for backdoor detection within a LoRA fine-tuned text-to-image diffusion model, aiming to discover the malicious trigger for trustworthy LoRA adaptation. The key observation is that backdoor trigger tokens that appear in a larger proportion of training prompts tend to induce more prominent token-specific LoRA responses than those induced by unrelated tokens. TokenScanner therefore scans the tokenizer vocabulary and measures token-wise LoRA responses in the U-Net and the text encoder. It uses these responses to detect backdoored LoRAs and rank candidate trigger tokens for subsequent testing of backdoor activation. Experiments on seven backdoor settings, comprising 840 backdoored LoRAs and 840 real-world benign test LoRAs, show that TokenScanner achieves 95.96% AUC and 96.55% TPR at an FPR of 10.95%. It also achieves 89.40% Hit@1 and 99.40% Hit@5 for trigger discovery across all seven settings.

---


### 67. [DOHF: Online Diffusion Fine-tuning with Doob's $h$-transform Guidance](https://arxiv.org/abs/2609.31882)

**<font color=#1a73e8>作者：</font>** Zhengyi Guo, Jiayuan Sheng, Wenpin Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward-based diffusion fine-tuning faces practical challenges when desirable outcomes are rare or conditioning corrections are costly to estimate. In this work, we propose Diffusion Online $h$-guidance Fine-tuning (DOHF), which turns Doob's $h$-transform into a practical online training algorithm. DOHF assigns optimality weights to generated samples, estimates the normalized local correction $\nabla\log h$ under the current rollout policy, and distills it directly into the generative model. Theoretically, we characterize the population-optimal DiffusionNFT update as well as the various classfier free guidance methods through a unified $h$-transform perspective. Methodologically, our framework accommodates black-box and non-differentiable rewards without additional network evaluations. We further show improved alignments under three empirical scenarios. Our work demonstrates how adapting probabilistic conditioning through inexpensive estimation and iterative distillation can improve generative learning across statistical sampling and visual generation.

---


### 68. [FARE: Deep Reinforcement Learning For Fair Exposure Constrained Uncertainty Aware Financial Content Personalization](https://arxiv.org/abs/2609.31890)

**<font color=#1a73e8>作者：</font>** Arundeep Chinta, Lucas Vinh Tran, Jay Katukuri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Content personalization systems in financial services must ensure fair exposure across diverse offerings-a requirement driven by contractual obligations and the need to prevent "rich-get-richer" dynamics where content with high click-through rate (CTR) dominates while other relevant products receive minimal visibility. Share of Voice (SOV) constraints, which guarantee each content category a target fraction of top-position exposure, address this by promoting product diversity and balanced user discovery. While re-ranking layers atop CTR models are common in practice, we propose two key novelties: (1) framing SOV-constrained ranking as a deep reinforcement learning problem analogous to constrained trade execution in algorithmic finance, and (2) explicitly incorporating CTR prediction uncertainty into the agent's state space and policy design-enabling larger ranking adjustments for high-uncertainty predictions where deviation from CTR-optimal ordering is less costly. We introduce FARE (Fair Ranking Executor), a modular uncertainty-aware execution layer that translates any black-box CTR model's predictions into SOV-fair rankings without retraining the underlying model. Our uncertainty-weighted proportional control policy (FARE-PC) and learned neural policies (FARE-ES, FARE-PPO) demonstrate that uncertainty-aware approaches can substantially reduce SOV deviation from fairness targets while minimizing engagement loss, with gradient-free evolution strategies outperforming policy gradient methods on synthetic data and the ordering reversing on KuaiRand-Pure.

---


### 69. [CyberWorld: World Models for Sample-Efficient Autonomous Cyber Defense](https://arxiv.org/abs/2609.31893)

**<font color=#1a73e8>作者：</font>** Ryozo Masukawa, Sanggeon Yun, Raheeb Hassan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning has become a prominent approach to autonomous cyber defense. Existing methods are predominantly model-free and consequently require extensive environment interaction. World models provide an alternative by learning predictive dynamics and optimizing policies through imagined trajectories, yielding substantial gains in sample efficiency in robotics and embodied control. Extending this paradigm to cybersecurity raises a fundamental question: what should constitute the "world" in a cyber world model? We introduce CyberWorld, a Dreamer-style world modeling framework that learns latent cyber dynamics from vector, graph, textual, and multimodal representations of the defended network. Across all four scoreable CyberWheel attack strategies, the graph-based CyberWorld variant exceeds a strategy-agnostic control after 3.6k-15.8k environment steps, compared with millions of steps required by model-free PPO. Across representation choices, graph structure provides greater robustness under topology-dependent attacks, while simpler representations remain competitive in overall performance. Among successful runs, the number of episodes required to reach the control remains approximately constant as network size increases from 15 to 100 hosts. These results establish learned cyber dynamics as a sample-efficient and scalable basis for autonomous defense, and identify world representation as a central design axis for robustness and scalability.

---


### 70. [Auditing Quality Filters for Long-Tail Human Data Curation](https://arxiv.org/abs/2609.31896)

**<font color=#1a73e8>作者：</font>** Rishav Agarwal, Nirshal Chandra Sekar, Anirudh Vemula  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robots on construction sites must detect workers who are kneeling or bending, which we call low poses. These workers can be lost from training datasets during automatic labeling. We study a pipeline that detects people, estimates their body joints using NLF, and groups similar poses. Low poses account for only about 2 percent of the retained examples. This low share may partly reflect the pipeline's quality filter, which rejects examples with low detection confidence or uncertain joint estimates. We examine this filtering using four alternative pose clues: bounding-box shape, vertical body span, pose grouping aligned to the scene's vertical direction, and image appearance. All four suggest that low poses are rejected by the filter more often. Separately, controlled simulated scenes show that a person detector fine-tuned on a public construction dataset misses more workers in these poses even when we correct their bounding box height is matched to that of standing workers. These findings suggest that low poses are scarce and hard to find, and we cannot rely on bounding boxes or poses for long-tail human data curation.

---


### 71. [Context-dependent agent evaluation with orthogonal equilibrium learning](https://arxiv.org/abs/2609.31897)

**<font color=#1a73e8>作者：</font>** Haorui Ma, Zehua Zang, Jiangmeng Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many applications require to evaluate agents under contextual information (e.g., a prompt, task, or user group). We study how to perform such context-dependent agent evaluation from offline feedback. Existing score-based models for this purpose (e.g., Bradley-Terry) impose a transitive preference ordering, which fails to reflect collective preferences when human judgements are heterogeneous. Inspired by social choice theory, we frame evaluation as a contextual game between two players, each selecting a distribution over agents as the strategy to receive greater collective preference than the other. Then, the support of the Nash equilibrium defines a context-specific set of winners. However, learning context-specific equilibria from offline logs is difficult because each context reveals human feedback on only a subset of agents, and, hence, a naive plug-in estimator can therefore be biased. To address these challenges, we propose NashEval, a general framework for robust contextual equilibrium learning. NashEval first constructs debiased estimates of the contextual payoff matrix that characterizes the game. NashEval then learns the context-to-equilibrium mapping with a tailored orthogonal loss, which avoids the need to solve a separate game for each context. We show theoretically that errors in estimating the nuisance functions underlying the payoff matrix affect the risk of the learned equilibrium (i.e., exploitability) only through higher-order terms. Across various experiments, NashEval improves robustness of equilibrium learning and consistently identifies the set of top-performing agents across contexts.

---


### 72. [PredRA: Fast Medical Image Translation by Deterministic Component Extraction and Controlled Stochastic Refinement](https://arxiv.org/abs/2609.31912)

**<font color=#1a73e8>作者：</font>** Jianhai Zhang, Pattarawut Charatpangoon, Donghao Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Strongly paired medical image translation contains a substantial component that can be predicted directly from the source. The current reality is that pure deterministic prediction can smooth away fine detail, while generative models can recover detail but may also introduce unnecessary or potentially harmful variation. We propose PredRA, a fast framework that uses the deterministic prediction as a stable reference and further extracts additional deterministic components from the residual during generative refinement, thereby improving fidelity while maintaining perceptual quality. The goal is simple: we view the entire residual-based generative process as an optimization problem and derive a practical solution that recovers useful residual detail through controlled refinement while keeping the prediction close to the paired target. Mechanism studies further show that useful residual information follows structured patterns, but its usefulness is difficult to estimate reliably at the voxel level. We therefore globally control how much of the residual refinement is added to the deterministic prediction, thereby reducing the accumulation of unnecessary uncertainty. PredRA therefore combines deterministic component extraction with controlled stochastic refinement for fast, fidelity-preserving, and perceptually strong medical image translation. We validate the approach across multiple real-world datasets, showing that controlled refinement improves fidelity to the paired target compared with full residual refinement while retaining much of the perceptual benefit of generative modeling. PredRA achieves competitive or superior performance to substantially larger state-of-the-art models with 1.4-11.9x fewer total parameters and 3.1-26.2x fewer trainable parameters, while its 32-step flow sampler requires 31.25x fewer sampling steps than the matched 1000-step DDPM.

---


### 73. [Facial classification Using Hybrid Quantum Machine Learning](https://arxiv.org/abs/2609.31915)

**<font color=#1a73e8>作者：</font>** Roshan Babu Bandlapalli, Srinivas V Katakam, Jitendra Chougala 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hybrid quantum methods have received limited study for resource-constrained facial biometrics. We present a hybrid quantum-classical facial recognition pipeline designed to run on standard computing hardware. Images undergo gamma correction, contrast enhancement, and principal component analysis before their features are encoded into an eight-qubit variational quantum classifier. Classical image matching then performs recognition. In experiments with 50,000 images, comprising 25,000 faces from CelebA and 25,000 non-face images from CIFAR-10, the method outperformed the reported CPU-trained FaceNet baseline in accuracy and training efficiency. The pipeline was also evaluated on GPU and quantum hardware. In an attendance monitoring deployment at Mahindra University in collaboration with Lloyds Technology Centre, CPU inference took 0.2 to 0.5 seconds per person, and the system remained robust to the use of spectacles. These findings support the feasibility of deploying hybrid quantum methods for facial recognition on existing CPU hardware.

---


### 74. [ROTE: Benchmarking Neural Memorization on Complexity-Controlled Symbolic Sequences](https://arxiv.org/abs/2609.31918)

**<font color=#1a73e8>作者：</font>** Xinye Chen, Stefan Güttel, Mohammad Mozaffari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce ROTE (RollOut Testing of Exact memorization), a benchmarking protocol for evaluating symbolic memorization of neural architectures. We study memorization and the extension of symbolic rules in neural sequence models by using sequences whose complexity is regulated by Lempel--Ziv--Welch (LZW) compression. Under ROTE, each architecture is trained as the same finite-context conditional predictor and is evaluated using teacher-forced one-step prediction as well as closed-loop rollout on the withheld symbols. Following a shared prediction-and-rollout evaluation routine, the benchmark evaluates gated recurrent, minimal recurrent, attention-based, and hybrid recurrent-attention models with their native computational characteristics preserved. Beyond standard predictive metrics, the benchmark reports normalized string distances, training time, memory usage, and parameter count across an LZW-complexity sweep. The study establishes a connection between the complexity of algorithmic sequences and the memorization capacity of neural architectures, revealing the trade-offs involving memorization quality, rollout stability, and computational expense. Our software and reproducible experimental code can be obtained from this https URL.

---


### 75. [Cache-Aware Conv3D Lowering Across Embedded World-Model Decoders](https://arxiv.org/abs/2609.31938)

**<font color=#1a73e8>作者：</font>** Jiaming Zhang, Wu Yang, Shuai Tao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative world models can provide visual rollouts for embodied planning, yet their feasibility on edge devices depends not only on the learned model but also on how the execution runtime represents its operations. We introduce a cache-aware lowering that expresses supported causal Conv3D calls as batched spatial Conv2D operations while preserving pretrained weights, temporal-cache semantics, convolution parameters, bias placement, and output layout. Across the complete Cosmos3-Edge image-to-video pipeline on a 64-GB NVIDIA Jetson AGX Orin, the proposed route accelerates VAE decoding by approximately $7\times$ and reduces complete-generation latency by more than $2\times$, while repeated decoder evaluations maintain complete fast-path coverage without fallbacks. The unchanged lowering also improves Cosmos3-Nano and transfers to LingBot-World's architecturally distinct Wan2.1 VAE. A clean-device comparison against fully specialized TensorRT shows that TensorRT provides a further $1.36\times$ steady-state improvement, but requires substantially greater per-module and per-runtime-state AOT specialization. Same-latent BF16 and FP32 evaluations characterize the finite-precision differences introduced by the alternative execution order. Together, these results position cache-aware lowering as a lightweight runtime optimization that recovers most of the available decoder acceleration without modifying the learned models themselves.

---


### 76. [Simple Extensions of Single-Objective Acquisition Functions and Hedge Strategies for Multi-Objective Bayesian Optimization](https://arxiv.org/abs/2609.31940)

**<font color=#1a73e8>作者：</font>** Haris Moazam Sheikh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-objective Bayesian optimization (MOBO) is commonly approached through specialized acquisition functions or scalarization schemes designed to explicitly account for trade-offs among non-preferential objectives. In this work, we show that such complexity might be unnecessary. We propose a framework that extends standard single-objective acquisition functions directly to the multi-objective setting through a hypervolume-based transformation. We further extend hedge strategies for acquisition functions, which are typically used only in single-objective optimization, to the multi-objective regime. Our approach requires minimal modification to existing Bayesian optimization pipelines and avoids the need for bespoke multi-objective formulations. We demonstrate how a broad class of commonly used single-objective acquisition functions and hedge strategies can be adapted in a principled manner to handle multiple objectives, while preserving their intuitive interpretation and computational efficiency. Empirically, we evaluate the proposed methods across a range of synthetic and real-world multi-objective benchmarks. Despite their simplicity, our extensions consistently match or outperform more complex state-of-the-art MOBO methods in terms of optimization performance and sample efficiency. These results suggest that effective multi-objective Bayesian optimization can be achieved by reusing and carefully extending well-established single-objective acquisition strategies, offering a simpler and more flexible alternative to existing approaches.

---


### 77. [Transformer MLP Gate Thresholds Are Couplings to a Carried Reference Direction](https://arxiv.org/abs/2609.31956)

**<font color=#1a73e8>作者：</font>** Olli Tuomi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The corpus-mean direction of a transformer's residual stream is a component shared across all inputs, and is commonly removed by mean-centering before representational analysis. We present evidence that it is a functional component: the reference against which the MLP gate population sets its operating point. In Phi-2, an exact decomposition of resting gate pre-activations shows that at mid-stack layers the resting inhibition of >99.9% of gates is carried by the coupling $w \cdot b_L$ to the carried mean direction, at 48-56$\times$ the explicit bias parameter, and the coupling is direction-specific: a random direction at matched norm orders the population's firing rates at Spearman $\rho \leq 0.09$ where the reference reaches 0.95. (That 0.95 is near-tautological on its own; the paper derives its null.) Causally, removing the stream's projection on the reference multiplies above-threshold firing by about 9$\times$, dose-monotonically, at 23-59$\times$ a norm-matched control; a random-initialised twin is flat, and replacement tests show that the direction carries the function and the magnitude does not. A direction-matched control makes the same point: noise injected along the reference costs 8-42$\times$ the same energy along a random direction. The decomposition replicates on four further families spanning both gate types (GELU with an explicit gate bias, bias-free SwiGLU), and the dose-response on two of them. Across an eight-model scan the mechanism is present in every GELU and SiLU family and absent only in OPT, where an opposing LayerNorm bias cancels the carried reference. Gate thresholds are implemented as couplings to a constant the network builds for the distribution it is reading, with the bias parameters contributing little; how much of that constant is carried in the stream and how much in parameters depends on the architecture.

---


### 78. [Hardware-Rooted PUF Fingerprinting for Device-Level Traceability in Knowledge Distillation](https://arxiv.org/abs/2609.31968)

**<font color=#1a73e8>作者：</font>** Ning Lyu, Yuntao Liu, Yonghong Bai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) enables model transfer across heterogeneous platforms and deployment environments, yet it exposes proprietary models to distillation-based theft, where an adversary extracts intellectual property (IP) by training a student model on teacher outputs. Current defenses, such as software watermarking or hardware-based access control, either fail to survive the distillation process or lack the granularity to identify the specific device responsible for a leak. Aiming to provide post-theft accountability and traceability, we propose a novel fingerprinting framework that superimposes device-specific Physical Unclonable Function (PUF) signatures onto teacher logits during distillation. By utilizing signatures derived from Ring Oscillator (RO) PUFs measured on a Xilinx Zynq-7020 FPGA, we ensure that any student model trained via KD inherits a unique, hardware-linked identity. Our framework is architecture-agnostic, enabling reliable identity inheritance across heterogeneous structures, including Convolutional Neural Networks, Vision Transformers, and encoders. To ensure robust attribution, we implement a two-stage recovery pipeline consisting of a neural decoder and Hamming-distance refinement, maintaining high detection accuracy even under noisy conditions. Furthermore, we introduce a multi-level logit encoding scheme to support large-scale device deployment. Experimental results demonstrate that the embedded fingerprints are resilient against common post-distillation modifications. These results establish a practical system-level approach for enabling hardware-linked model traceability in distributed AI deployment environments.

---


### 79. [Double-Edged Sword of Mediated Visibility: How Visual Framing Undermines Congresswomen's Perceived Competence](https://arxiv.org/abs/2609.31970)

**<font color=#1a73e8>作者：</font>** Bryce J. Dietrich, Hyein Ko, Myriam Shiran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Women's presence in Congress has stalled below 30%. That institutional underrepresentation is mirrored by their limited visibility on televised news, where visual presentation can shape perceived competence and authority. Yet research tells us more about whether congresswomen appear than how they are visually framed. Facial recognition analysis of 695,464 image-text segments from CNN and Fox News (2011-2021) reveals that congresswomen appear disproportionately in split-screen rather than solo shots. Two pre-registered experiments with 6,220 participants show that, in static frames, split-screen framing reduces congresswomen's perceived political competence, but not congressmen's. In dynamic videos, the competence penalty disappears; instead, outraged language reduces a congresswoman's perceived warmth roughly three times as much as a congressman's. Suggestive evidence (p = .057) indicates that women viewers report greater external political efficacy after watching a congresswoman appear alone. We conclude that visual framing shapes both congresswomen's mediated visibility and their perceived capabilities.

---


### 80. [Attributing Sensor Deviations to Degradation, Weather, or Attack in Oilfield Digital Twins: A Simulation Study of Probabilistic Attribution and Cost-Based Decisions](https://arxiv.org/abs/2609.31973)

**<font color=#1a73e8>作者：</font>** Mustafa S. Aljumaily, Nawar S. Alseelawi, Hayder Kareem Abed  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When an oilfield digital twin disagrees with its instruments, the operator must decide whether the cause is hardware degradation, harsh-weather effects, or malicious data manipulation. Existing digital-twin work appears to treat these causes separately: sensor-validation architectures target faults, and attack-focused twins have been evaluated on water-sector testbeds. We study joint cause attribution on a simulated four-well wellpad with 15 coupled instruments, legitimate operating transients, and weather. A physics-informed twin, identified from normal data only, produces analytical-redundancy residuals; windowed features feed a gradient-boosted classifier whose posterior drives an alarm gate with a fixed false-alarm rate and a cost-based decision rule that may defer to an analyst. On three independently generated sites, the classifier reaches macro-F1 of 0.818 on windows where the injected deviation is observable (0.723 when latent post-onset windows are included at the primary site). The physics twin accounts for essentially all of this: removing the data-driven twin changes macro-F1 by less than 0.01, whereas removing all twins drops it to about 0.58. Attacks are detected quickly (median 1.7 h) but attributed correctly at alarm time only 42% of the time, rising to 73% six hours later. A cost-aware policy that defers ambiguous cases had the lowest expected cost among all policies in every one of 144 cost and prior settings tested, sometimes by a small margin; the result depends on illustrative costs and on analysts resolving deferred cases. A twin-aware attacker was detected in 45% of episodes yet almost never attributed to attack. These results are conditional on the simulator's generative assumptions and have not been validated on field data.

---


### 81. [Model Casting and Low-Parameter Gating: Towards More Sparsely Activated FFNs](https://arxiv.org/abs/2609.31975)

**<font color=#1a73e8>作者：</font>** Maria Lomeli, Antoine Groudiev, Matthijs Douze 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces model casting, a mid-training recipe that drastically sparsifies the activations within the Feed-Forward Network (FFN) layer. With this strategy, at inference time, we first compute the output of the gating matrix and, thanks to its high sparsity, we avoid computations with the two other matrices, reducing the FLOP count by up to 3x. While this theoretical speedup is an upper bound, model casting translates into significant speedups both on CPU and GPU.
We then introduce LoPA Gating, a new FFN design that increases the maximum theoretical speedup. It is a low-FLOPs parameterization of the gating matrix that overcomes the 3x cap by allocating fewer FLOPs and parameters to the gating matrix, compared to the two other FFN matrices that are sparsely activated.
We consider two cases: (i) we cast a pre-trained model with a sparsity inducing activation; (ii) we train with LoPA from scratch. In all settings, we significantly outperform existing pruning solutions and regular RELU-fication. For instance, at matched quality, we achieve a 3.2x FLOP speedup with LoPA Casting, against 1.6x at best for competing methods top-p and TEAL. Using dedicated kernels, we achieve an actual 3.31x speed-up on GPU at 90% sparsity, past the 3x ceiling of standard gating; RELU-fication, meanwhile, plateaus below 80% sparsity.

---


### 82. [Toward Embedding-Based Psychometrics: Structural Modeling of Assessment-Item Semantics With Contextual Scores](https://arxiv.org/abs/2609.31976)

**<font color=#1a73e8>作者：</font>** Jinsong Chen, Shi-Ting Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Contextual scores represent assessment items through their similarities to reference words in an external corpus. We examine the semantic structure of scores for 40 TIMSS mathematics scored units using a partially specified two-step factor procedure. A search across factor counts identifies a persistent seven-group structure under the featured construction. Subsequent comparisons consistently favor a general dimension alongside group associations, although individual group memberships remain sensitive to some specification choices. Item examples distinguish recurring, cross-domain, sensitive, and imposed associations. Simpler and unrestricted references clarify the contribution and limits of the anchored representation: it improves on a single factor but does not achieve the lowest working Bayesian information criterion (BIC). A separate response benchmark compares three initial Q constructions and their Hull-PVAF revisions under higher-order and saturated attribute distributions. Among these diagnostic models, BIC favors the official content framework and the Akaike information criterion (AIC) favors its direct four-factor augmentation, but a matched unidimensional two-parameter logistic model has lower AIC and BIC than all twelve conditions. These findings support a conditional semantic representation while limiting direct diagnostic interpretation. We discuss learned text-assisted response calibration as a prospective application requiring a larger calibrated item bank and independent evaluation.

---


### 83. [Evasion Attacks on Cost-Utility-Based Adversarial Training for Online AutoML in IoT Networks](https://arxiv.org/abs/2609.31981)

**<font color=#1a73e8>作者：</font>** Chukwunonso Henry Nwokoye, Wajiha Zaheer, Khalil El-Khatib 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As Internet of Things (IoT) networks increasingly depend on machine learning for anomaly, malware, intrusion detection, and network monitoring, such systems have become attractive targets for evasion attacks. Evasion attacks pose a major security risk because an adversary intentionally modifies input data to mislead a trained model into producing incorrect predictions while evading detection. This study evaluates the impact of black-box evasion attacks on a cost-utility-based adversarial training defense strategy in an Online AutoML context for IoT networks. Specifically, evasion attacks were applied to online learners, including Hoeffding Tree (HT), Leveraging Bagging (LB), Streaming Random Patches (SRP), Hoeffding Adaptive Tree (HAT), and Adaptive Random Forest (ARF). By developing naive and adversarially trained (AT) versions of these online learners, we generated clean and adversarial accuracies for each model. The results show that the AT versions of LB and SRP performed best, achieving the highest adversarial accuracy (0.985) and high clean accuracy (0.993) at the highest cost budget of 1.00, with a maximum accuracy reduction of only 0.8%. Finally, drift detection was conducted using the Early Drift Detection Method (EDDM).

---


### 84. [Understanding the Subspace Stabilization of the Hessian and Gradient Covariance Matrix](https://arxiv.org/abs/2609.31983)

**<font color=#1a73e8>作者：</font>** Fangshuo Liao, Anastasios Kyrillidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The phenomenon of the top subspace stabilization of the Hessian matrix is an surprising and critical aspect in study of the second-order information of neural network training. Prior work argues that the top subspace of the Hessian stabilizes by measuring the overlap between the top subspaces of the step-wise Hessian, and explains this stabilization with diminishing parameter change in the late phase of training. In this paper, we define a new instability metric for the subspace evolution, and use it to detect subspace stabilization that is independent of the magnitude of parameter change. In the meantime, we observe that the gradient covariance matrix has a similar property of its top subspace to the Hessian. By using a between-class and within-class decomposition of the gradient covariance matrix, we identify an explicit form that gives a near-perfect approximation of the top-$(C-1)$ subspace of the Hessian and the gradient covariance matrix. In the gradient flow set-up, we show that the slow evolution of the idenfied approximation is due to the separation between the outlier and the bulk eigenvalues of the Hessian matrix, thus providing an explanation to the phenomenon of the top subspace stabilization of the Hessian matrix.

---


### 85. [Something to Talk About: Social Media as a Lens on Healthcare Ransomware Events](https://arxiv.org/abs/2609.31984)

**<font color=#1a73e8>作者：</font>** Seoyoung Kweon, Paul Chung, Isabel Straw 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In the modern era, ransomware attacks on critical healthcare organizations---like hospitals and insurers---are frequent, with impacts ranging from leaked private health information all the way to serious disruptions of urgent, time-sensitive clinical operations. Unfortunately, legal and economic incentives make it uncommon for hospitals to share basic information about these attacks, their scope, and the downstream impacts to patient care. In this paper, we explore the use of public social media posts---authored both by hospitals and by individuals---to garner more detailed insights about these attacks and their effects. We collect 1,628 Facebook and Reddit posts from 2018--2024, design and evaluate techniques to match post data to 212 ground-truth ransomware attacks, and conduct quantitative and qualitative analyses that explore the impacts such attacks have on critical hospital infrastructure, patient care, and providers. We conclude by discussing the promise and limitations of leveraging social data to study the impact of ransomware attacks and highlight areas of future research.

---


### 86. [Does Vision-Language Pretraining Granularity Matter? A Controlled Evaluation of Vision-Language Objectives Across Chest X-Ray Interpretation Tasks](https://arxiv.org/abs/2609.31985)

**<font color=#1a73e8>作者：</font>** Denis Musinguzi, Andrew Katumba, Prasenjit Mitra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language pretraining objectives differ in the spatial granularity of their supervision, yet the implications of this distribution for chest X-ray interpretation remain underexplored. We present a controlled study that isolates the pretraining objective: holding the encoder and pretraining data fixed, we train nine objectives spanning global and local contrastive learning, captioning, and their combinations, and evaluate across five chest X-ray tasks of increasing spatial granularity. We find that (i) pretraining granularity aligns with task granularity at the extremes, with local objectives leading on abnormality detection and global objectives on classification; (ii) local objectives are surprisingly competitive on global-level generation and question answering tasks; (iii) the merits of captioning and contrastive learning reverse across granularity levels; and (iv) among combinations, mixing captioning and contrastive supervision is strongest on classification and in distribution generation, while pairing two captioning objectives generalizes best on zero-shot report generation. These results show that no single objective is universally optimal, and that the interaction of objective type, granularity, and task governs downstream performance.

---


### 87. [Lagrangian and Hamiltonian Neural Networks With a Dissipative System](https://arxiv.org/abs/2609.31988)

**<font color=#1a73e8>作者：</font>** V. Rayamajhi, J. Singal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate the applicability of Lagrangian and Hamiltonian Neural Network models to a dissipative system that has explicit time dependence in its Lagrangian, Hamiltonian, and total energy. To do so we consider these neural network models for simulated systems of a harmonic one-dimensional, one-component oscillator with damping, as well as without damping for comparison. We find that both the Lagrangian and Hamiltonian approaches are able to predict the empirical physical behavior of the damped oscillator systems and to effectively ``learn'' to varying degrees the underlying Lagrangians and Hamiltonians, as has previously been shown to be the case with undamped oscillator systems. These investigations elucidate important properties of Lagrangian and Hamiltonian mechanics, including properties that are not manifest when considering systems without explicit time dependence.

---


### 88. [Mechanistic Interpretability Reveals Shared Causal Subspaces in Brain-to-Speech Decoders](https://arxiv.org/abs/2609.31992)

**<font color=#1a73e8>作者：</font>** Maryam Maghsoudi, Ayushi Mishra, Sanghamitra Dutta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decoding covert speech, such as mimed or imagined, from brain activity is harder than decoding vocalized speech. Cross-modal transfer, where information from one speech form helps decode another, is a promising remedy; yet how a decoder internally represents and processes brain activity from different speech forms remains unclear. In this work, we ask: which internal neurons of a decoder carry cross-modal information, and are these neurons shared across different speech forms? To answer these questions, we leverage mechanistic interpretability, using recordings of the same sentences in vocalized, mimed, and imagined input pairs for activation patching. We insert the decoder's internal activity for a sentence in one condition into its processing of the same sentence in another and measure the change in decoding accuracy. We find that no single neuron drives this benefit; instead, it arises from small groups of neurons, with vocalized speech as the most useful source. These groups are largely condition-specific in the early stage of the decoder but overlap in the later stage. These findings point toward more data-efficient covert speech decoders through training objectives that encourage shared later-stage representations learned mainly from vocalized data.

---


### 89. [Can Circuit Alignment Predict OOD Generalization?](https://arxiv.org/abs/2609.31996)

**<font color=#1a73e8>作者：</font>** Ayan Banerjee, Abhra Chaudhuri, Josep Llados 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can out-of-distribution (OOD) generalization be predicted from a trained model's weights alone, without any target-domain data? Existing representational similarity metrics (CKA, SVCCA, RSA) compare activations rather than forecast generalization. We show they are provably insensitive to structural rerouting in the computational graph, the very change distribution shift induces. We close this gap with the Circuit Alignment Score (CAS), which compares class-specific circuits across domains via graph kernels, decomposed into same-class coherence and cross-class confusion. Casting CAS as a Lebesgue integral over the domain distribution, we prove its Monte Carlo estimate recovers the ground-truth ranking of learners by OOD accuracy, with pairwise inversion error vanishing at rate $O(1/M)$, where $M$ is the number of sampled domains. Across $48$ learners on PACS, CAS attains $0.88$ rank correlation with OOD accuracy, versus $0.58$ (CKA), $0.23$ (SVCCA), and $0.14$ (RSA), with similar trends on other benchmarks and even against data-dependent methods, making it the first provably consistent predictor of distributional robustness requiring neither target-domain data nor labels. The code is available at: this https URL

---


### 90. [Type-Balanced Federated Learning for Visual Analog Meter Reading](https://arxiv.org/abs/2609.31998)

**<font color=#1a73e8>作者：</font>** Weida Zhao, Logan Bellamy, Yazhou Tu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Analog dial meters are widely deployed in industrial applications and utility sites, where environments and meter types vary and inspection data may be sensitive. Currently, automatic meter readers must be individually developed and deployed for each environment and meter type in practice. Deep learning could handle this variability but requires diverse labeled data that are costly to collect and update. In practice, meter images are distributed across independent sites, each with limited labels, while raw images often cannot be pooled because of ownership, governance, or privacy constraints. To address these challenges, we present a federated framework for visual analog meter reading that enables multiple sites to collaboratively train a reading model without sharing their raw images. Our framework consists of a four-stage pipeline: (1) dial localization, (2) thin-structure segmentation trained federatively across clients, (3) polar unwrapping, and (4) tick-counting decoding for final reading. To enable systematic evaluation of this setting, we release MeterFL, a 1,382-image mask-annotated dataset organized into deployment-motivated pseudo-clients derived from visual attributes via deterministic rules, with dHash near-duplicate control between the segmentation train and test splits. We evaluate both segmentation quality and end-to-end reading accuracy. MeterFL is publicly available at this https URL.

---


### 91. [VC Dimension and Expressivity of Real-Valued Transformers](https://arxiv.org/abs/2609.31999)

**<font color=#1a73e8>作者：</font>** Gavin Dooley, Andy Yang, Yijia Jessica Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Whereas previous results on abilities and limitations of transformers have restricted the definition of transformers in various ways, here we study softmax-attention, multi-layer transformers operating on real values, with very few additional assumptions. Applying results from real geometry, we obtain upper bounds on the VC dimension and split VC dimension of such transformers ($O(n^4)$ and $O(n^6)$, respectively, where $n$ is the input length). Conversely, we also construct specific transformers witnessing lower bounds on these quantities ($\Omega(n)$ in each case). These results have some notable consequences. For example, within the class of symmetric (permutation-invariant) functions, we show that transformers can uniformly express all functions over an alphabet of one symbol and non-uniformly express all functions over an alphabet of two symbols, but cannot (even non-uniformly) express some functions over an alphabet of six symbols. We also prove limitations on how many bits of a real number a transformer can access.

---


### 92. [What Does the Rank Buy? A Spectral and Distributional Analysis of Low-Rank Adaptation](https://arxiv.org/abs/2609.32002)

**<font color=#1a73e8>作者：</font>** Babak Barazandeh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rank $r$ in LoRA is widely treated as a capacity control: a smaller rank is assumed to yield a simpler model that generalizes better. We show that, under hard per-factor norm budgets---the idealization of the weight decay and norm control used in practice---this intuition breaks down. The reason is structural: under such budgets, the updates LoRA can reach are exactly the matrices of rank at most $r$ inside a nuclear-norm ball, and every complexity and displacement functional we analyze is maximized over this set by a rank-one update---so the rank cap never binds. The consequences follow directly. The linear-readout model class we study is identical for every $r \ge 1$, its Rademacher complexity carries no dependence on $r$, and the distance the adaptation can move the source distribution obeys a rank-independent upper bound that we show is sharp. If rank does not control capacity, where does it act? We identify two places. Statistically, replacing the per-factor budgets with a joint budget on the product restores a data-dependent, rank-sensitive complexity bound---though the gain appears only for well-spread feature distributions, and the worst case remains rank-free. Spectrally, rank sets the price of adaptation: canceling the leading singular directions of the pretrained weight requires both sufficient rank and sufficient budget. We bound the smallest rank achieving a desired source--target alignment, with upper and lower bounds that match under two-sided spectral decay. Together, these results recast rank as governing which updates are reachable and what cancellation costs---not how much capacity the model has.

---


### 93. [Is invariance all you need for algorithmic fairness? Removing demographic information can create new bias](https://arxiv.org/abs/2609.32004)

**<font color=#1a73e8>作者：</font>** Aditya Parikh, Eike Petersen, Stella Frank 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Encoded demographic information in internal model representations is a commonly assumed risk factor for algorithmic bias, with demographic representation invariance often being touted as the ideal state. However, while demographic shortcut learning is a genuine threat, some degree of encoding is necessary when demographics correlate with target labels. Here, we show, mathematically and empirically, that enforcing demographic invariance can actually hamper bias mitigation and even create new biases. We distinguish marginal from class-conditional representation invariance, and show that they imply the standard group fairness notions of demographic parity and equalized odds, respectively. We evaluate the effects on predictive performance and fairness of enforcing both invariance types, both theoretically and empirically across five tabular and two chest X-ray imaging datasets. Our findings support our mathematical argument that demographic representation invariance is neither desirable nor sufficient for fairness.

---


### 94. [Human Activity Recognition via Ultra-Wideband Data: A Framework for Dimensionality Reduction, Pattern Discovery, and Predictive Modeling](https://arxiv.org/abs/2609.32008)

**<font color=#1a73e8>作者：</font>** Nahid Sahel Gozin, Reza Sedaghat, Prathap Siddavaatam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in sensor technology have enabled more effective human activity recognition (HAR), particularly in real-time systems with limited computational resources. However, Ultra-Wideband (UWB) radar data remain challenging due to high dimensionality, noise, complexity, and nonlinear characteristics. This research proposes a framework to efficiently reduce data size, uncover significant patterns, and classify six activity types (Standff, Liedown, Noactivity, Sit, Stand, and Walk) from UWB signals with high accuracy. Two novel dimensionality reduction techniques are introduced in this paper. The first, Clustered Polynomial Expansion with Incremental PCA (CPE-IPCA), combines clustering and polynomial feature expansion with Incremental PCA, preserving 100% of the variance in only 50 components. The second, Post-PCA Standardization Approach (PPSA), standardizes data after PCA and retains 99.1% of the variance in 80 components, achieving superior compression and computational efficiency compared to conventional nonlinear methods. Frequent patterns are identified using Apriori and FP-Growth, which are then classified with Random Forest and a Vector Space Model (VSM). The framework achieves 100% accuracy with Random Forest on CPE-IPCA and 99% on PPSA, while VSM attains 100% precision, recall, and F1 on PPSA and near-perfect performance on CPE-IPCA (precision 1.00, recall 0.98-1.00, F1 0.99-1.00), demonstrating a fast, interpretable, and robust HAR system suitable for healthcare, assisted living, and smart environments.

---


### 95. [TriO: Tri-Modal Unsupervised Occupancy World Model for Anything Perception](https://arxiv.org/abs/2609.32013)

**<font color=#1a73e8>作者：</font>** Quinlan Sykora, Sourav Biswas, Christopher Diehl 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present TriO, a multi-modal unsupervised world model that predicts 4D occupancy, obstacle segmentation, flow and LiDAR. In contrast to prior work, TriO utilizes three distinct sensor modalities (camera, LiDAR, and RADAR) as both inputs and sources of self-supervision, eliminating the need for additional human annotations. Thanks to its novel supervision, the model is able to segment any occupancy from the drivable surface, overcoming the limitations of existing open-set methods in handling long-tail objects. TriO achieves state-of-the-art results in multiple 3D and 4D tasks, including occupancy, flow, and LiDAR prediction, as well as zero-shot road obstacle segmentation across multiple datasets such as Argoverse 2, and Spotting the Unexpected.

---


### 96. [Compact Shielded CSV: Post-Quantum, Private, Lightweight Client-Side Validation Blockchain](https://arxiv.org/abs/2609.32015)

**<font color=#1a73e8>作者：</font>** Dragos I. Ilie, Uri Lee, Iain D. Stewart 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We propose Compact Shielded CSV, a private client-side validation blockchain for peer-to-peer payments designed for the postquantum era. Upgrading existing blockchains to quantum-resistant cryptography substantially increases on-chain overhead. By keeping all large cryptographic artifacts off-chain, Compact Shielded CSV keeps a minimal on-chain footprint independent of the size of the underlying cryptographic proofs and signatures. For a single input transaction, the onchain footprint is just 3 hashes (3x32 bytes): a nullifier, a degriefer, and a commitment to the transaction. We introduce the degriefer - a novel mechanism that enforces ownership and prevents double-spending using only hash commitments, eliminating the need for on-chain signatures entirely. These properties make Compact Shielded CSV a promising foundation for private, scalable, post-quantum digital payments.

---


### 97. [Representation Learning for Exact Preimages](https://arxiv.org/abs/2609.32018)

**<font color=#1a73e8>作者：</font>** Konstantin Hess, Stefan Feuerriegel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern neural predictors can model highly nonlinear maps, but many scientific and engineering tasks require reasoning in the opposite direction: given a performance or safety level, the goal is to characterize the preimage, that is, the complete set of inputs which meet the desired target level and optimize over that set. For expressive neural predictors, however, such preimages typically have no explicit representation and are expensive to recover or optimize over. This creates a fundamental three-way challenge between expressive forward prediction, accurate preimage approximation, and tractable optimization over the preimage for downstream tasks. We introduce TRIO (tractable representations for preimage learning and inverse optimization), a framework for learning representations that make these objectives compatible by construction. Our key contribution is a preimage factorization: the forward model remains expressive through nonlinear radial transformations (including neural networks), while, under inversion, each transformation reduces to a single scalar radius, which yields simple geometric level sets. This yields an explicit geometric representation that is reusable for downstream optimization over the preimage, and, for linear objectives, we show that this admits a closed-form global solution. We finally prove a universal approximation theorem which shows that TRIO can approximate any continuous forward map and its entire family of potentially disconnected, nonconvex preimages arbitrarily well. Hence, TRIO combines expressive forward modeling, exact preimage recovery, and tractable global downstream optimization over preimages by design.

---


### 98. [Decentralized Master-Mind: Joint Action Refinement through Iterative Intent Denoising in Multi-Agent Pathfinding](https://arxiv.org/abs/2609.32019)

**<font color=#1a73e8>作者：</font>** Valeriy Vyaltsev, Anton Andreychuk, Taisia Zlotnikova 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decentralized multi-agent path finding (MAPF) with communication requires agents to reach individual goals without collisions under partial observability. Learnable policies trained on expert data provide an effective approach to this problem. However, when several coordinated joint actions are valid in the same context, independently sampling from per-agent distributions can recombine locally valid choices into incompatible joint actions. This failure can arise from the final sampling mechanism even when the per-agent action distributions are learned correctly. DMM (Decentralized Master-Mind) addresses this by replacing one-shot action sampling with discrete, iterative refinement of action intents across communication rounds, inspired by denoising in diffusion models. Agents initialize random action intents and refine them through local communication, coupling their choices before commitment. DMM is pretrained with imitation learning on expert MAPF solutions and further optimized with MICPO, a critic-free group-relative reinforcement-learning method designed for multi-agent, multi-round action refinement. DMM generally achieves higher success rates and lower solution costs than the evaluated learnable baselines. On 1,600 MovingAI tasks, DMM fine-tuned with MICPO solves 1,598, the highest coverage among the evaluated methods, while achieving solution costs close to those of the strongest baselines. DMM also scales to over one million simultaneously acting agents in obstacle-rich environments. These results show that round-level intent refinement can improve joint-action coordination while preserving decentralized execution.

---


### 99. [Depth Any Seen: Which Surfaces and How Far?](https://arxiv.org/abs/2609.32027)

**<font color=#1a73e8>作者：</font>** Xiaohao Xu, Xiaonan Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When several surfaces are visible along a ray, recovering visible 3D structure from one image requires jointly estimating their presence and metric depth. Depth Any Seen represents these surfaces as image-conditioned multi-Bernoulli depth sets, whose components each contribute one depth or remain absent. Its auxiliary-free Exact Multi-Bernoulli objective (ExactMB) learns depth and presence by marginalizing one-to-one assignments to complete, distinct targets. Our analysis shows that matching expected count can leave component-surface assignment unresolved. We extend real and synthetic layered-depth benchmarks to evaluate depth accuracy, recovered support, and overprediction. Compared to depth stacking, ExactMB reduces overprediction by a relative 88.2% on LD-Real and 80.5% on MD-3K while retaining most ordinal accuracy, with comparable conditional metric-depth error on LD-Syn. Further ablation studies show that ordered assignment improves depth-accurate recall and precision over marginalization, whereas the count-regularized configuration achieves higher deeper-rank precision than ordered assignment at lower recall. Our code will be publicly released.

---


### 100. [Reasoning Concentrates Errors, and Self-Consistency Never Notices](https://arxiv.org/abs/2609.32035)

**<font color=#1a73e8>作者：</font>** Asaad Althoubi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-consistency assumes that independent samples disagree when a model is unsure, so agreement is evidence of correctness. Holding weights fixed and toggling only a reasoning mode, over five benchmarks and 74,944 samples, we show that reasoning concentrates a model's errors: the probability that two independently drawn wrong answers coincide rises in all ten dataset-scale comparisons (p = 0.00098), and in nine of nine after restricting both arms to the problems each gets wrong. Where the answer space is unbounded, reasoning cuts the distinct answers produced to 0.43-0.65 of the non-reasoning count; where it is bounded, both arms hold an identical option set and reasoning concentrates mass on it instead, which no positional prior can explain at fixed weights. The aggregate cost is smaller than the mechanism predicts, because reasoning also shrinks the set of problems where answer diversity can decide anything, in ten of ten cells and by 2.7x; normalized for available headroom, both arms convert a quarter of it in domain. Confidence weighting does not recover what is left. Across 280 method-dataset-model combinations on eight models and five benchmarks, not one beats plain majority voting after correction; weighted voting agrees with it on 98.5% of problem-method pairs and is right 56.3% of the time on the rest; and a signal's direction can invert within fixed weights, with answer log-probability predicting correctness when reasoning is off and error when it is on. A learned six-signal combination gains nothing out of domain. Confidence signals should be evaluated on decisions, not on discrimination.

---


> [!TIP]
> 当前位于：**51-100**（第 2/19 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-908](./part-19.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
