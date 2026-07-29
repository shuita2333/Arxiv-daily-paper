# 📦 其他研究 | 2026年07月30日

> 本类共 **229** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-229](./part-05.md)

---

### 151. [OrthKD: Extracting Generalized Clinical Knowledge from Heterogeneous Teachers for Lightweight Deployment](https://arxiv.org/abs/2607.25545)

**<font color=#1a73e8>作者：</font>** Yi Xu, Cheng Chen, Mufan Cao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying diabetic retinopathy (DR) screening models in primary care requires edge-efficient systems that remain accurate, safe, and reliable under domain shift. Multi-teacher knowledge distillation (KD) is a natural compression strategy, but existing approaches largely assume that all teachers provide equally trustworthy supervision. In our setting, this assumption fails: a strong CNN teacher (EfficientNet-B3, 0.876 QWK) and a weaker Transformer teacher (Swin-Base, 0.830 QWK) are complementary, yet the Transformer's logits can still mislead the student. We therefore propose OrthKD, a selective-trust distillation framework that transfers full supervision from the strong CNN, uses feature-only distillation from the weak ViT, and enforces orthogonality between teacher-specific student projections to encourage complementary rather than redundant evidence. This design preserves local lesion precision, injects global structural context, and improves robustness to distribution shift. On 132,049 retinal images, a 5.4M-parameter MobileNetV3 student reaches 0.885 QWK on EyePACS and improves zero-shot Messidor-2 performance from 0.507 to 0.728 QWK, while also achieving strong referral AUC and calibration. These results show that selectively distilling heterogeneous teachers can enable practical DR screening on resource-constrained devices.

---


### 152. [From Training to Deployment: Post-Hoc Causal Feature Identification via Sensitivity Ratios](https://arxiv.org/abs/2607.25546)

**<font color=#1a73e8>作者：</font>** Athanasios Vlontzos, Giorgos Papanastasiou, Bernhard Kainz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Given a model that is already trained, which features does it rely on causally versus spuriously? Existing methods require access to the training procedure and cannot answer this post-hoc. We introduce the \textbf{Normalised Sensitivity Ratio~(NSR)}, a post-hoc, model-agnostic diagnostic for this question under a structured-shift regime: environments differ primarily in the mean of spurious features while the causal mechanism and causal marginals remain stable, as in multi-site clinical data or multi-batch genomics. Within this regime, causal features induce constant model sensitivity across environments while spurious features track shift. NSR formalises this as the squared coefficient of variation of per-environment sensitivity. Under a linear structural causal model (SCM) with $K\ge3$ non-degenerate environments, NSR achieves exact identification (Theorem~1). We fully characterise failure: weak shifts ($O(\varepsilon^4)$ collapse), degenerate geometry, and proxy attenuation ($O((1-\alpha)^4)$), giving practitioners quantitative criteria for assessing whether the regime holds. Finite-sample rates are $O_p(n^{-1})$ under the null and $O_p(n^{-1/2})$ under the alternative. Experiments confirm all theoretical predictions on synthetic data (area under the ROC curve [AUROC] $= 1.000$ under conditions satisfying the regime), show consistent rankings across five model families (Kendall $\tau\ge0.529$), and recover six of eight causal features on bike-sharing data (Precision@7 $= 0.75$) without modifying any trained model.

---


### 153. [Agent Skills Matter: Inferring Proprietary Skills from Execution Trajectories](https://arxiv.org/abs/2607.25560)

**<font color=#1a73e8>作者：</font>** Jianing Geng, Ruiqi He, Zekun Fei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills package reusable procedures that improve downstream performance. Their lightweight, portable form enables marketplace monetization and private deployment behind cloud-hosted agent interfaces, giving providers incentives to keep high-value skills proprietary. Yet hiding the artifacts does not conceal their behavioral effects, which remain observable in execution trajectories and form a behavioral side channel. We define this exposure as Skill Leakage: reconstructing proprietary skills from trajectories elicited by benign queries, without reference answers or success labels. We introduce SigLeak, a black-box framework that exploits recurring skill signatures in agent behavior. It constructs diverse, decision-rich diagnostic tasks, contrasts matched skill-enabled and skill-disabled trajectories, and iteratively refines a reconstructed skill from the isolated patterns. Across five scenarios, three model families, and three agent frameworks, SigLeak outperforms or matches three baselines in nearly every setting. It raises the success rate by 6.88 percentage points over the skill-disabled reference on average and achieves the highest overall SkillSim, our metric for coarse- and fine-grained semantic similarity. These results show that benign execution trajectories can expose proprietary procedural knowledge. The code is available at this https URL.

---


### 154. [Few-Shot Open-Vocabulary Remote Sensing Segmentation via Textual Inversion](https://arxiv.org/abs/2607.25563)

**<font color=#1a73e8>作者：</font>** Junhyuk Heo, Junghwan Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary segmentation labels arbitrary categories from a text query without per-class training, yet on remote sensing imagery it underperforms on categories it handles reliably elsewhere. We find that much of this gap traces to the text query rather than to the segmentation model. Because these models are not specialized for overhead imagery, the class name that serves as the query is often a weak address into the vision-language embedding space. We show that a better name repairs part of the gap, while the remaining failures call for an address that the tested natural-language rephrasings do not provide. We recover that address from a few examples through textual inversion on a frozen model, keeping inference text only. On a representative benchmark this raises the mean intersection over union on the affected categories from 3.9 to 39.4, and across eight remote sensing datasets it improves over few-shot methods that instead inject visual prompts at inference.

---


### 155. [The LAIA Dataset: Labelled Attention for Intelligent Automobiles](https://arxiv.org/abs/2607.25570)

**<font color=#1a73e8>作者：</font>** A. Contreras, D. Porres, R. Abad 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The development of autonomous vehicles (AVs) usually relies heavily on data-driven artificial intelligence (AI) models that require large volumes of sensor data with ground-truth annotations. While modular architectures are widely used, end-to-end driving paradigms offer a promising alternative by directly mapping sensor inputs to control actions. However, their adoption is limited by challenges in interpretability and explainability. To address this, we present LAIA (Labelled Attention for Intelligent Automobiles), a novel synthetic dataset designed to enrich end-to-end driving research with human attention data. Collected using the CARLA simulator in closed-loop environments, LAIA comprises over 15 hours of driving from 44 participants across carefully crafted scenarios designed to evoke natural responses. Each sequence includes RGB images under six weather conditions, semantic and instance segmentation, depth, optical flow, CAN bus signals, and synchronized eye-tracking data. LAIA enables applications including training attention-aware end-to-end AI drivers, predicting driver behavior, developing methods to detect anomalous driver-attention patterns, and improving model explainability. In this work, we use LAIA to compare human attention with the perceptual attention emerging in our end-to-end driving models, thereby providing insight into their behavior.

---


### 156. [Matrix-Free Photoacoustic Image Reconstruction via Sensor-Token Self-Attention](https://arxiv.org/abs/2607.25576)

**<font color=#1a73e8>作者：</font>** Mary John, Shibili Said, Imad Barhumi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Photoacoustic tomography (PAT) combines the optical absorption contrast of biological tissue with the spatial resolution of ultrasound, yet recovering the initial pressure distribution from sparse-view sensor measurements remains an ill-posed inverse problem. Iterative compressive-sensing solvers and unrolled deep networks both retain a dependence on the system matrix at inference, which leaves real-time clinical reconstruction computationally expensive. This paper proposes the Sensor Attention Network (SAN), a Transformer-based architecture that treats the full time series of each sensor as a token and maps raw measurements directly to the reconstructed image without invoking the system matrix at inference. For training and benchmarking, an analytical k-space H-matrix is constructed and validated against the k-Wave pseudo-spectral solver under matched geometry, achieving a mean per-sensor Pearson correlation of 0.919 +/- 0.049, with k-space apodization and Gaussian temporal damping acting synergistically to reduce the energy-normalized mismatch by 49%. Trained with a vessel-weighted loss on 488 augmented samples and evaluated on 46 held-out samples against ISTA, split-Bregman total variation (SBTV), and learned ISTA (LISTA), SAN attains the highest mean SSIM (0.522) and PSNR (22.09 dB) and the lowest NMSE (0.233). Paired t-tests and Wilcoxon signed-rank tests confirm the superiority of SAN over LISTA on PSNR, NMSE, and Pearson correlation at p < 1e-8, and over ISTA and SBTV on all fidelity metrics. By bypassing the H-matrix at inference, SAN reduces reconstruction time by at least an order of magnitude, supporting real-time PAT reconstruction.

---


### 157. [How Small Can You Go? A Controlled Study of LoRA Rank, Target Modules, and Quantization Trade-offs for Text-to-SQL on a 60M-Parameter Model](https://arxiv.org/abs/2607.25583)

**<font color=#1a73e8>作者：</font>** Mahendra Singh Rathor, Anagheem Azzam  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning (PEFT) and low-bit quantization are now standard tools for adapting language models under tight compute budgets, yet their interaction is most often studied on billion-parameter models where the design space is expensive to explore. We ask a complementary question: on a specific, fully reproducible 60M-parameter encoder-decoder model (T5-small) and a single-table text-to-SQL benchmark (WikiSQL), how much task accuracy does each efficiency knob actually cost? We run a controlled, single-variable study over (i) LoRA rank r in {2, 4, 8, 16, 32}, (ii) the set of adapted modules, and (iii) numerical precision. We report task accuracy alongside system-level metrics including trainable parameters, peak training memory, inference latency, and throughput, and frame adaptation as a constrained trade-off rather than an accuracy-only objective. Our results show that LoRA with r=16 recovers within 11.6 percentage points of full fine-tuning accuracy (59.6% vs. 71.2% exact-match) while training fewer than 1% of parameters and consuming 31% less peak GPU memory. Within this setting, rank beyond r=16 yields no measurable accuracy gain. QLoRA with INT8 and NF4 quantization achieves comparable accuracy (52.8% and 53.2%) at dramatically lower memory cost (0.60 GB each), demonstrating a compelling trade-off for memory-constrained deployments. All code, configurations, and logs are released for full reproducibility.

---


### 158. [A Density-Matrix Framework for Electronic-Structure Analysis of Functional-Group and Salt Effects in Lithium-Metal Electrolytes](https://arxiv.org/abs/2607.25597)

**<font color=#1a73e8>作者：</font>** Mingkang Liu, Huize Yu, Yanbin Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The reactivity of lithium-metal electrolytes arises from the interplay of molecular functional groups, Li$^+$ solvation, and salt-anion participation. This interplay operates through the redistribution of electron density across donor, anion, and cation centers, which is most directly read out from the electronic structure resolved in space. Quantum-chemical calculations deliver such readouts faithfully, yet become computationally demanding across this multidimensional design space, and machine-learning electronic-structure models seldom cover chemically diverse solvation shells or electrolyte-relevant readouts. Here, we present a density-matrix-centered AI platform (EMolStudio) for electronic-structure prediction and analysis. Its workflow integrates molecular functionalization, explicit Li$^+$ first-shell assembly, density-matrix prediction with idempotency projection, and readouts of frontier orbitals, electrostatic potential, Li$^+$-donor bond order, and electron localization. We apply EMolStudio to 163,655 functionalized molecules and 22,500 explicit Li$^+$ first-shell clusters across four lithium salts. We find that 1) at the molecular scale, functionalization distinguishes CO$_2$Me, CN, F/CF$_3$, and sulfonyl groups by chemically distinct changes in frontier levels, electrostatic potential, and Li$^+$-donor contact, consistent with $\pi^*$-acceptor, inductive, and polarization contributions, with sublinear accumulation at higher degrees of functionalization; 2) in explicit solvation shells, anion identity reshapes frontier-orbital localization: LiTDI anchors the HOMO on the anion across the entire library, whereas LiDFOB pairs an anion-hosted HOMO with strongly functional-group-dependent LUMO hosting. EMolStudio thereby translates functional-group and salt choices into electronic-structure hypotheses relevant to lithium-bond formation, desolvation, and interphase reactions.

---


### 159. [Computational Extraction of Legal Causes via al-Sabr wa al-Taqsim: A Set-Theoretic Formalization for Closed Fiqh Chapters](https://arxiv.org/abs/2607.25605)

**<font color=#1a73e8>作者：</font>** Elnaser Abdelwahab  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents a set-theoretic formalization of the classical usuli method of al-Sabr wa al-Taqsim (Examination and Division) for extracting legal causes ('ilal) within closed chapters of jurisprudence. A computational algorithm is introduced that extracts minimal operational rules from a truth table of juristic verdicts. The principal result is that, given a complete truth table for a closed chapter, the algorithm computes the minimal structural generators of the ruling and eliminates all logically redundant attributes. The resulting structures constitute admissible candidate causes for subsequent juristic evaluation. The framework is conditional upon the availability of a finite school-relative concept vocabulary and a complete ruling table for the chapter under investigation.

---


### 160. [Physics-Informed Broad Learning System: An Efficient Backpropagation-Free Framework for Solving Partial Differential Equations](https://arxiv.org/abs/2607.25608)

**<font color=#1a73e8>作者：</font>** Pinki Khatun, M. Sajid, Abhinav Jha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-informed neural networks (PINNs) have emerged as a powerful paradigm for solving partial differential equations (PDEs) by embedding governing physical laws into deep neural networks. However, their reliance on computationally expensive gradient-based optimization and deep architectures often results in slow training, high computational cost, and limited scalability. In this work, we propose a novel physics-informed broad learning system (PI-BLS), the first physics-informed learning framework based on broad RdNNs. The proposed formulation embeds the governing differential operator and the associated initial and boundary constraints directly into a linear output-layer optimization problem, thereby replacing nonlinear gradient-based training with a deterministic least-squares solution obtained via the pseudoinverse. Consequently, the entire learning process is reduced to a single linear optimization stage while preserving the underlying physical constraints. As a result, PI-BLS offers an efficient learning paradigm for a physics-informed learning framework for solving PDEs that eliminates iterative backpropagation while preserving the underlying physical constraints. Experimental results on representative forward PDE benchmarks demonstrate that PI-BLS achieves competitive and often superior performance with reduced training time and model parameters compared with conventional PINNs.

---


### 161. [Contrastive Representation Learning of Longitudinal Disease Trajectories on Temporal Graphs](https://arxiv.org/abs/2607.25609)

**<font color=#1a73e8>作者：</font>** Bastian Pfeifer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding disease trajectories from longitudinal clinical data remains challenging due to complex temporal dynamics and heterogeneous patient cohorts. Here, we present a contrastive representation learning framework that models multivariate disease trajectories as temporal graphs and learns representations using contrastive graph neural networks. Nodes represent patient observations over time, while edges capture temporal continuity and structural similarity between trajectories. Structure-aware random walks guide contrastive learning to generate embeddings that preserve temporal context and trajectory topology. The resulting representations enable robust clustering of patients with similar disease progression patterns and reveal latent structure in longitudinal data.

---


### 162. [Multi-Sensor Alignment for Weather Simulations](https://arxiv.org/abs/2607.25612)

**<font color=#1a73e8>作者：</font>** Samsad Alam, Devyani Lambhate, Aditya Mohan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Perception tasks for autonomous vehicles need to work satisfactorily in adverse weather conditions. Due to lack of real-world weather datasets, weather simulations are a promising alternative. To ensure simulations closely mirror real-world weather data, it's crucial that they represent the same weather characteristics, including severity and particle positioning, across different sensors. To achieve this, we propose the Reference Dataset Alignment Method (ReDAM) for weather intensity alignment in fog and Unified-weather-edit (inspired by Weather-edit[1]) for particle positioning alignment in rain and snow. We validate both alignment methods using statistical and geometrical tests, respectively. We find that 3D detection models for non-aligned versions tend to be overly optimistic as compared to aligned versions. We also show the aligned-multi-sensor simulation's effectiveness for achieving robustness for 3D object detection task by finetuning existing sensor fusion models on it.

---


### 163. [Beyond Facial Consistency: Personalized Person Image Generation with Holistic Identity Preservation](https://arxiv.org/abs/2607.25622)

**<font color=#1a73e8>作者：</font>** Yuxuan Xiao, Shanshan Zhang, Jian Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalized person image generation requires preserving subject identity across both local facial details and broader appearance cues. Existing methods typically emphasize only one level of identity information, leading to an inherent trade-off between facial fidelity and overall appearance consistency. To address this, we first propose a simple dual-branch baseline that unifies global appearance control and local facial control within a shared generation framework. This simple combination of different branches yields promising results, but suffers from instability in practice due to uncoordinated branch contributions. To this end, we propose Dynamic Balancing Scaling (DBS), a fine-tuning strategy for improving face and appearance identity coordination. DBS consists of two components: adaptive temporal gating, which dynamically modulates branch contributions along the denoising trajectory, and region-aware optimization, which improves the coordination of facial, appearance, and global supervision. Together, these designs alleviate persistent face-branch over-dominance and encourage more effective appearance-aware guidance. We also introduce Pexels-100, a benchmark for evaluating holistic identity consistency in personalized person generation. Experiments show that DBS achieves a better trade-off between facial fidelity and appearance consistency than existing open-source baselines, while providing a controllable basic framework for holistic identity modeling.

---


### 164. [Quotient Dynamics, Effective Curvature, and Implicit Bias in Positive Quadratic Networks](https://arxiv.org/abs/2607.25624)

**<font color=#1a73e8>作者：</font>** Pengcheng Cheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Positive quadratic networks admit the low-rank representation f_U(x)=x^top UU^top x, where Uinmathbb{R}^{dtimes r} is identifiable only up to right orthogonal multiplication, representing a rank-r PSD matrix Q=UU^top. We study how this quotient structure governs training dynamics, curvature, recovery, and interpolation bias. On the full-column-rank stratum, we identify mathbb{R}^{dtimes r}_*/O(r) with the rank-r PSD manifold. For smooth objectives L(U)=ell(UU^top), the Euclidean factor gradient is horizontal. Thus, factor gradient flow projects exactly to quotient Riemannian gradient flow, while finite-step gradient descent induces an exact congruence recursion for the predictor. For quadratic regression, we derive the effective Hessian at interpolators as the empirical measurement Gram form restricted to the tangent space relative to the quotient metric. Under Gaussian rank-one measurements, we compute population curvature, prove uniform deviation bounds for the empirical normal operator, construct a spectral initializer, and establish local exponential convergence for gradient flow and linear convergence for small-step descent. Recovery guarantees are explicit but conservative due to reliance on full-space second-moment control. In underdetermined commuting regimes, factor gradient flow becomes an exact entropy mirror flow in joint spectral coordinates. Strictly positive initializations converge to Bregman projections onto the interpolation set. With isotropic initialization q(0)=varepsilon^2mathbf{1}, predictors approach the minimum-trace solution set as varepsilondownarrow0, resolving nonuniqueness via weighted entropy within the invariant joint spectral algebra. Finite-step descent selects interpolants differing from continuous-time Bregman projections by O(eta). Numerical experiments verify these quotient identities, curvature predictions, recovery behaviors, and selection laws.

---


### 165. [AIriskEval-edu Demo: Auditing of Pedagogical Risks in Educational Explanations](https://arxiv.org/abs/2607.25634)

**<font color=#1a73e8>作者：</font>** Javier Irigoyen, Roberto Daza, Francisco Jurado 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present AIriskEval-edu Demo, a platform that audits the pedagogical quality of instructional explanations and provides explainable audit results. The platform evaluates an explanation against a rubric covering five dimensions of pedagogical risk: factual accuracy, depth and completeness, focus and relevance, student-level appropriateness, and ideological bias. For each dimension, it returns a binary decision and a confidence score. Detected risks also include a natural-language rationale and, except for Depth and Completeness, a localized evidence span. The platform integrates GPT-5.5 through an external API and a self-hosted Llama 3.1 8B evaluator that runs on consumer-grade GPUs. The local evaluator is fine-tuned on AIriskEval-edu, a dataset of K-12 instructional explanations with risk and explainability annotations. The platform operates in two modes: in AI mode, both evaluators assess stored explanations generated under six simulated teacher profiles, each representing a distinct pedagogical behavior and potential risk; in human mode, the local evaluator audits user-written explanations in real time. The local evaluator outperforms GPT-5.5 on most reported metrics, offering educational institutions a practical way to keep audited content within their own infrastructure.

---


### 166. [Using Data-Derived Priors to Guide CNN Architecture Design for NIR Chemometrics](https://arxiv.org/abs/2607.25636)

**<font color=#1a73e8>作者：</font>** Dário Passos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Convolutional neural networks (CNN) for near-infrared (NIR) chemometrics are often designed using generic architectural rules, although spectral datasets differ in sampling, smoothness, redundancy, and sample size. We tested whether these properties can provide empirical priors for CNN design. Across 25 NIR regression tasks, we computed descriptors of dataset size, spectral length and spacing, entropy, intrinsic rank, autocorrelation, and wavelet-scale structure. Two interpretable 1D-CNN scaffolds (a minimal single-convolution model and an extended shallow model with optional branching, dilation, etc) were optimized using five-fold cross-validated Bayesian hyperparameter optimization (HPO). Relationships extracted from near-optimal trials were converted into warm-start heuristics and evaluated directly and through leave-one-dataset-out (LODO) validation. The clearest relationships involved convolutional receptive fields. In the minimal CNN, the preferred kernel fraction decreased with spectral entropy and intrinsic rank, increased with the wavelet energy-support fraction, and the learning rate tended to decrease with training-set size. Direct and LODO heuristics were competitive with HPO, with median test-RMSE ratios of 0.953 and 1.017, respectively. The extended CNN showed similar but less transferable structure across branch usage, dilation, dropout, filter counts, and receptive-field choices. Ten stochastic refits showed seed sensitivity comparable to that of HPO-selected configurations. In a separate experiment, joint preprocessing and CNN HPO outperformed standardized-spectra HPO in 19 of 25 tasks, although gains were dataset-dependent. These results show that spectral descriptors can provide practical CNN design priors, guiding shallow NIR models toward plausible hyperparameter regions before target-specific tuning

---


### 167. [OmniPhys: Knowledge-Graph-Driven Benchmarking and Collective Optimization for Physical Commonsense in Text-to-Image Generation](https://arxiv.org/abs/2607.25641)

**<font color=#1a73e8>作者：</font>** Yajing Xu, Yarong Lan, Jiaoyan Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While text-to-image models exhibit remarkable visual fidelity, they frequently violate fundamental physical commonsense. Existing benchmarks often rely on coarse-grained descriptions, failing to diagnose the mastery of specific physical principles. Moreover, the high stochasticity of generative processes causes current prompt optimization methods to suffer from gradient hallucinations, where optimizers are misled by transient visual artifacts rather than systemic flaws. To address these challenges, we introduce OmniPhys, a rigorous benchmark of 1,551 samples grounded in a Physical Knowledge Graph. By aligning PhET simulations with standard curricula, OmniPhys operationalizes a knowledge-to-scenario pipeline that performs diagnostic stress tests via a dual-path verification protocol. We further propose OmniPrompt, an iterative framework that treats physical alignment as a discrete optimization problem. For each query, OmniPrompt aggregates K stochastic images into a per-query feedback buffer. Across training, it further merges feedback from batches of B queries before each meta-policy update, filtering seed and query-local noise. Evaluations across 12 representative text-to-image models reveal universal physical bottlenecks. Results demonstrate that OmniPrompt significantly enhances physical consistency across diverse backbones, proving the transferability and efficacy of our evolved meta-policies. The code and data are available at this https URL

---


### 168. [Engine-Equal, Human-Unequal: A Reproducible Outcome Skew in Engine-Assessed Equal Chess Positions](https://arxiv.org/abs/2607.25655)

**<font color=#1a73e8>作者：</font>** Jesung Park  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Among chess opening positions that a strong engine judges essentially equal (Stockfish 18 evaluation within 10 centipawns of zero, depth-stable) and that humans actually reach on Lichess (October 2025; 1,661 positions, 16.1M occurrences), human results are not balanced. Positions carry outcome skews, each the gap between its games' actual results and what the players' ratings predict, whose directions are stable properties of the naturally-reached position: some positions favour White, others Black. These skews reproduce across three re-partitions -- disjoint player-account sets (primary), time, and disjoint rating bands -- and on an out-of-sample month eight months later. On the primary split, each position's skew is measured once in each account group, and the replication slope asks how well one measurement predicts the other after removing rating and opening-family effects: one means undiminished carry-over; zero, no linear relation. We find 0.69 (family-clustered 95% CI [0.65, 0.74]), rising to 0.94 on the most-popular, best-measured positions. The slope's value depends on the position mix. Existence is the invariant claim: it survives every tighter evaluation band, search depth, calibration, and popularity cutoff we test, and replicates within blitz and rapid separately. The typical skew is small (median $|\delta| \approx 0.018$, about two percentage points of White score), yet it reproduces, position by position, across disjoint accounts. At these positions the disfavoured side also thinks longer. Even where the evaluation is most confident, it is not a sufficient statistic for human outcomes. The result is observational, and the causal question is left to a pre-registered randomised companion study.

---


### 169. [OrchBench: Evaluating Multi-Agent Orchestration Plans in Isolation via Deterministic Simulation](https://arxiv.org/abs/2607.25656)

**<font color=#1a73e8>作者：</font>** Zhenzhen Ren, Jiyan He, Xinpeng Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Complex tasks often decompose into parallelizable yet interdependent subtasks, making orchestration critical to the performance of multi-agent systems (MAS). Existing evaluations typically rely on end-to-end execution, which conflates orchestration-plan quality with worker capabilities, tool reliability, and environmental noise. Moreover, the time and token costs of real execution grow rapidly with workflow scale, making systematic evaluation expensive. We present OrchBench, a simulation-based benchmark for evaluating multi-agent orchestration plans in isolation. Starting from real-world tasks, OrchBench constructs directed acyclic graphs (DAGs) that encode task dependencies, with controlled sizes and degrees of parallelism. Given a DAG, a per-agent context limit, and an agent budget, the evaluated planner assigns subtasks to agents and specifies cross-agent information transfers and their retention ratios. A deterministic simulator evaluates the resulting plan without invoking worker agents and returns interpretable measures of result quality, makespan, and token cost. The simulated scores produced by OrchBench correlate strongly with quality scores from Claude Code executions, achieving a Pearson correlation of \(r=0.816\), while requiring only \(1.3\%\) of the tokens and \(10.3\%\) of the wall-clock time. Across diverse planners and workflow scales, we find that preserving task-critical information is more important than simply increasing the number of agents, and the benefits of parallelism diminish as coordination failures accumulate. These results establish OrchBench as an efficient and interpretable benchmark for comparing and diagnosing multi-agent orchestration plans.

---


### 170. [CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization](https://arxiv.org/abs/2607.25659)

**<font color=#1a73e8>作者：</font>** Bo-Wen Zhang, Junwei He, Wen Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rubric-based reinforcement learning enriches language model training by evaluating model outputs against explicit criteria. Yet in GRPO-style pipelines, these structured judgments are reduced to a scalar response-level reward and converted into a response-level advantage, which is broadcast uniformly to all generated tokens. This leaves no explicit mechanism for allocating credit within a response, even when different criteria are grounded in different spans, formatting decisions, or semantic choices. We propose CoRT, a token-level credit weighting method for rubric-conditioned GRPO. Instead of training an auxiliary token scoring model, CoRT uses counterfactual replay to rescore the same sampled response under the original rubric-conditioned prompt and a matched criteria-free prompt. The resulting tokenwise log-likelihood contrasts serve as a proxy for dependence on the rubric context. CoRT maps these contrasts to bounded, response-normalized weights and uses them to redistribute the signed GRPO advantage across tokens, without introducing an auxiliary scorer or changing the response-level reward. Experiments across instruction-tuned models and reward granularities show that CoRT improves over matched response-level GRPO in the vast majority of comparisons, with an average gain of 4.4 percentage points. The method remains competitive with learned token-level credit baselines while avoiding a separate relevance-learning stage. These results suggest that policy-internal counterfactual likelihood contrasts provide an effective training signal for within-response credit allocation while retaining the simplicity and stability of GRPO.

---


### 171. [Localized Adaptation Reveals Distinct Learning Signatures in Transformers](https://arxiv.org/abs/2607.25663)

**<font color=#1a73e8>作者：</font>** Rebecca Ramnauth, Brian Scassellati  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transformer adaptation is typically distributed across model depth, even when the intended change is narrow. We investigate how adaptation site shapes what a model learns, how well that learning generalizes, and how selectively it is applied. We introduce a controlled benchmark spanning five objectives (lexical binding, factual association, behavioral policy learning, causal mapping, and procedural reasoning) and define each objective's "adaptation geometry" as its profile of acquisition, transfer, and boundedness under full-stack and early-, middle-, or late-layer LoRA. The objectives exhibit distinct geometries. Lexical binding favors early-layer adaptation for acquisition and boundedness but requires broader updates for transfer; factual association favors later layers among localized adapters; behavioral learning separates late-layer action acquisition from middle-layer policy gating; and causal and procedural transfer benefit most from middle- or full-stack adaptation. These patterns largely persist under parameter-matched controls, and most corresponding directional contrasts replicate across five model families. These findings establish adaptation site as a key design variable for controlling what models learn, generalize, and leave unchanged.

---


### 172. [Contextual Deconvolution for Variance-Stable Demand Sensing: Kernel-Modulated Operators in Promotional Retail](https://arxiv.org/abs/2607.25664)

**<font color=#1a73e8>作者：</font>** Mohammad Forouhesh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning demand forecasts optimize statistical accuracy yet leave excess operational volatility that inflates safety stock and amplifies the Bullwhip effect. We introduce \textbf{Contextual Deconvolution} (CD), a two-stage estimator that reframes demand sensing as a convex decomposition: a kernel-modulated banded operator separates transient promotion-driven shocks from a smooth structural baseline, and hierarchical partial pooling enables catalog-scale deployment without per-SKU training. The operator is data-derived, not imposed---it reduces to the identity wherever the promotional response is impulsive (most of M5, all of Favorita) and contributes only where genuine multi-day carryover exists, so the gains rest on the structural decomposition itself. Evaluating strictly out-of-sample on 30,490 M5 SKUs and 2,845 Favorita items, with calendar-aware baselines given CD's identical future calendar, we anchor the contribution on a full inventory-cost accounting: CD lowers safety stock, holding cost, and order variance but under-provisions event spikes, reducing total cost only when holding costs exceed $\sim$20\% of stockout costs (95\% CI $[17\%,25\%]$); otherwise it is an operational-stability and inventory-capital layer, not an expected-cost minimizer. Its accuracy contribution is reliability rather than central tendency: across eleven baselines, CD attains the lowest cross-sectional dispersion of per-SKU error and mis-forecasts by more than 200\% on 0.8\% of SKUs versus 9.9--20.6\% for every baseline, ranking first on both in all four M5 draws. Because the Variance Ratio and std-based safety stock are minimized by any sufficiently smooth forecast, we treat them as diagnostics, not objectives. A supporting analysis shows the learned demand operators are non-normal, yet CD's compact parametric kernel matches their operational performance interpretably.

---


### 173. [A Physics-Informed Neural Operator for Thermal Ranking of Low-Cost Wall Materials in Hot-Dry Climates](https://arxiv.org/abs/2607.25668)

**<font color=#1a73e8>作者：</font>** Muhammad Akbar Khan, Fahim Raees, Ubaida Fatima  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Identifying cost-effective indigenous building materials that minimise heat penetration through walls is critical for indoor thermal comfort in low-income rural housing in hot-dry climates, where summer temperatures routinely exceed 45 C. We present a two-stage computational framework for thermal ranking of five low-cost indigenous wall materials: mud brick, clay-straw adobe, lime-stabilised bamboo panel, fired clay brick, and lime-mud composite. First, a validated Crank-Nicolson finite difference method (FDM) solves the one-dimensional transient heat equation with Robin boundary conditions under diurnal solar and outdoor air-temperature forcing, generating 1500 periodic-day solutions across a nine-dimensional parameter space by Latin Hypercube sampling. Second, a Physics-Informed Neural Operator (PINO) with a Fourier Neural Operator (FNO) backbone learns the parameter-to-solution operator mu -> T(x,t), enforcing both data fidelity and PDE consistency. The trained PINO attains a relative L2 field error of 5.14e-4 and a 0.201 K mean absolute error on the peak inner surface temperature, preserving the FDM material ranking exactly; PINO trained on 150 FDM samples matches a data-only FNO trained on twice as many, so the physics loss is most valuable when data are scarce. The periodic-day formulation also yields the ISO 13786 time lag and decrement factor, reproduced to within 0.99 h and 0.010. At nominal hot-dry summer conditions, clay-straw adobe achieves the best cost-performance index among widely available materials. A climate sweep, confirmed by FDM spot checks, reveals a regime boundary: under sub-ambient outdoor conditions the ranking inverts to conductive fired clay brick, delineating heat-exclusion and heat-rejection regimes. The framework supports evidence-based material selection for post-flood reconstruction in hot-dry regions.

---


### 174. [SignDeepSC: A Semantic Signature-based Approach for Robust Semantic Communication](https://arxiv.org/abs/2607.25676)

**<font color=#1a73e8>作者：</font>** Khalil Alhaj, Razane Tajeddine, Hadi Sarieddeen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Semantic communication systems such as deep semantic communication (DeepSC) offer high efficiency but are vulnerable to adversarial attacks on their underlying neural networks. We address a physical-layer man-in-the-middle (MitM) threat in which an adversary injects perturbations into the transmitted signal to distort its meaning. We propose SignDeepSC, an architectural defense that achieves adversarial robustness without requiring explicit adversarial example generation during training. The approach is built on a perceiver-inspired semantic signature, a compact vector summary of the source features transmitted over a separate low-rate auxiliary channel. This signature is used by a self-repairing decoder that leverages cross-attention to correct distortions and can additionally drive a scrambler that shuffles the feature layout. We evaluate SignDeepSC over Rayleigh fading and additive white Gaussian noise channels under both single-step fast gradient sign method (FGSM) and iterative projected gradient descent (PGD) attacks. Under PGD ($\epsilon = 0.7$), at 12~dB signal-to-noise ratio with Rayleigh fading, SignDeepSC achieves a bilingual evaluation understudy (BLEU-4) score of 0.237 and bidirectional encoder representations from transformers (BERT) sentence similarity of 0.646, outperforming all baselines without degrading clean-channel performance, when the signature channel is well protected.

---


### 175. [Cognivia: A Cognitive Behavioral Therapy Copilot for Evidence-Based Mental Healthcare](https://arxiv.org/abs/2607.25681)

**<font color=#1a73e8>作者：</font>** Qi Chen, Siria Xiyueyao Luo, Jian Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cognitive distortion amplifies negative emotions and contributes to mental health disorders. Cognitive Behavioral Therapy (CBT) is an effective way to address cognitive distortions, but its large-scale application is limited by the shortage of professional therapists. Although large language models (LLMs) have recently been explored for mental health applications, existing methods still suffer from limited domain specificity, overly flattering responses, and the absence of well-defined annotations for cognitive distortions. This paper proposes Cognivia, an evidence-based artificial intelligence therapist that integrates automatic cognitive distortion identification and rational response generation. Our framework is built on authoritative CBT texts widely regarded as core paradigms and standard references. It is further augmented with mental health question-answer (Q and A) data, and employs multi-stage prompting and structured generation strategies under the supervision of behavioral science experts. Then we fine-tune a lightweight LLM on this augmented CBT dataset to obtain Cognivia. In addition, we propose the first hierarchical quality evaluation framework for assessing LLM-generated rational responses, developed through collaboration between AI researchers and behavioral science experts. Cognivia is evaluated using lexical metrics, LLM-based Judges with two complementary criteria, and human evaluation by 10 behavioral science experts. It consistently outperforms the baseline methods in cognitive distortion recognition and rational response generation, demonstrating its effectiveness. Our code is available at this https URL.

---


### 176. [From Deterministic to Generative Deep Learning for Urban Air Quality Reconstruction from Sparse Observations](https://arxiv.org/abs/2607.25687)

**<font color=#1a73e8>作者：</font>** Abhishek A.Sabnis, Mihai Mitrea, Lya Lugon 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Full-field reconstruction of air pollution is essential for evaluating pollution exposure and supporting public health decision-making. However, the complex interactions among pollutants, hard-to-predict weather patterns, and limited monitoring station coverage make this a complex task. We apply deep learning techniques to provide fast and accurate reconstructions from sparse observations of four key pollutants: NO2, O3, PM2.5 and PM10. Models are trained on full-field simulation data and evaluated on real-world observations collected from 9 to 28 monitoring stations in the city of Paris. We introduce a diffusion-based generative framework for multi-pollutant reconstruction and benchmark its performance against deterministic deep learning models. Despite noisy observations and strong spatial variability, the models achieve high structural similarity on simulated validation data and produce realistic spatial patterns on real-world observations, as indicated by power-spectrum analysis. We introduce data augmentation methods that enable transfer to real-world observations without retraining, allowing the models to generalise beyond the training period. These findings highlight the potential of ML models for reliable real-world deployment in air pollution reconstruction tasks.

---


### 177. [Optimization with Dynamic Constraint Learning (DCL)](https://arxiv.org/abs/2607.25719)

**<font color=#1a73e8>作者：</font>** Ezgi Oztekin, Figen Oztoprak, S. Ilker Birbil  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose Dynamic Constraint Learning (DCL), a data-driven framework for constrained optimization when constraint functions are unknown and cannot be queried during optimization. At each iteration, the method learns a local surrogate from nearby data and solves a subproblem within a data-supported trust region. Compared with offline global constraint learning, the approach uses local surrogates that adapt to the data distribution during optimization and can achieve solution quality comparable to that of global models while using simpler local models and smaller optimization subproblems. We demonstrate the performance of DCL on a synthetic test problem and two case studies from the literature.

---


### 178. [A systematic evaluation of machine learning classifiers for event-by-event background rejection in LAFOV PET scanners](https://arxiv.org/abs/2607.25732)

**<font color=#1a73e8>作者：</font>** Konrad Klimaszewski, Michał Obara, Mateusz Bala 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The introduction of LAFOV PET scanners brings significant sensitivity gains but also a substantial increase in the background rate from accidental coincidences, phantom-scattered and detector-scattered photons. While machine learning methods have been applied to background reduction in PET imaging, they target specific background components in post-processing rather than event-by-event classification on the raw data. In this work, we formulate coincidence classification as a supervised multi-class problem and evaluate XGBoost, AdaBoost and Neural Network classifiers as pre-reconstruction filters, using Monte Carlo simulations of the Siemens Biograph Vision Quadra scanner with NEMA IEC and anthropomorphic XCAT phantoms. We investigate two feature sets: a 4-feature representation based on the Attenuation Factor, photon time difference, energy sum, and energy difference, and an extended 6-feature set that incorporates topology-based variables. A systematic robustness study via cross-phantom inference reveals that the 4-feature models generalise significantly better across different phantom geometries, with XGBoost suffering an accuracy loss of only 0.04 compared to 0.13 for the 6-feature variant. Our best models achieve accuracies of up to 0.74 and 0.69 for the NEMA IEC and XCAT phantoms, respectively, outperforming traditional geometry-based cuts. However, we show that this compact feature set not only provides limited suppression of in-phantom scattered coincidences, but it also can lead to non-trivial spatial patterns. With scattered coincidences being the dominant background component in clinical conditions, this suggests that while the method serves as an effective and geometry-agnostic replacement for traditional cut-based selection, meaningful further gains in image quality will require either larger input representations or dedicated treatment of the phantom-scattered component.

---


### 179. [A Structuration Approach to Theorizing Cybersecurity Practice: The STARC Model](https://arxiv.org/abs/2607.25734)

**<font color=#1a73e8>作者：</font>** Md Aktaruzzaman, Atif Ahmad, Sean Maynard  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The problem: Cybersecurity practice runs simultaneously across analysts, teams, organizations, sectors, and regulators, co-evolves with adversaries, and increasingly blends human and algorithmic decision-making. The theories applied to it operate at single organizational levels and cannot explain why organizations with broadly similar controls differ sharply in resilience.
This paper: We develop STARC (Structuration Theory Adaptation for Resilient Cybersecurity), a framework for locating where cybersecurity practice succeeds or fails structurally. It extends Giddens' Structuration Theory with three innovations, Multi-Level Adversarial Agency, Threat-Adaptive Structuration, and Material-Agential Structural Properties, across five structure-agency triads.
Evidence base: STARC is illustrated through re-analysis of three financial organizations, an Australian, an Indonesian, and a Malaysian bank, across 20 interviews from SOC analysts to senior executives, selected as diverse insourced and outsourced configurations rather than as a comparison of equivalents.
Cybersecurity contribution: STARC offers a structural account of why differently resourced and outsourced organizations differ in resilience, and a vocabulary for diagnosing incident-response breakdown across levels, tempos, and the human-algorithm authority boundary that single-level frameworks leave invisible.
Theory and outputs: It extends Structuration Theory to adversarial, multi-level, and hybrid human-algorithmic contexts, and yields seven testable propositions linking structuration to resilience, offered for future testing.

---


### 180. [Image Quality Dependent Degradation for AI Systems](https://arxiv.org/abs/2607.25736)

**<font color=#1a73e8>作者：</font>** Yannick Kees, Elena Hoemann, Frank Köster 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perception is one of the primary applications where neural networks outperform conventional algorithms. One example is AI systems for automated driving, which can detect pedestrians based on image data and avoid them accordingly. A substantial challenge with these AI systems is that their output depends heavily on the quality of the input images. For example, if an image is of inferior quality due to heavy contamination, such as noise or darkness, accurate predictions are hardly feasible. Additionally, various types of errors can occur, each with varying relevance to the trustworthiness of the underlying AI system. In particular, it may be more critical not to detect an existing person than to detect a person where there is none. Therefore, we want to show that we can still avoid the most critical errors in situations of inferior image quality. To achieve this, we aim to establish a fail-degraded system by lowering the network's confidence threshold based on the estimated image quality, enabling it to detect objects more cautiously in uncertain situations. Additionally, we present a novel method for estimating the quality of incoming images by comparing them to the training data using normalizing flows. We will also conduct experiments applying our method to state-of-the-art object detection. In summary, we will present a design strategy for AI-based systems in automated driving that can deal with poor-quality input data without resorting to fallback solutions. Such measures enhance trust in AI-based systems and lead to an increased provision of the AI component.

---


### 181. [Loss Invariance Determines What Concept Layers Encode: Volume Grounding in Echocardiography](https://arxiv.org/abs/2607.25748)

**<font color=#1a73e8>作者：</font>** Hyunkyung Han, Min Jung Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Objective: Concept bottleneck models route prediction through interpretable intermediate variables, and their validity is normally judged by how accurately those variables are predicted. We ask whether that judgement is sufficient, using left ventricular volumes as the concepts underlying ejection fraction estimation from echocardiographic video.
Methods: A video transformer encoder was trained on a publicly available echocardiography dataset. End-systolic and end-diastolic volumes formed a concept layer from which ejection fraction was computed analytically, with no residual path to the output. We compared training under an ejection fraction objective alone against training with additional supervision of the volumes in millilitres, and evaluated both on 1276 held-out studies.
Results: The concept bottleneck did not increase ejection fraction error relative to direct regression, at 6.89 against 7.13 mean absolute error. Without volume supervision, however, the spread of predicted volumes collapsed to 0.1 millilitres against reference spreads of 35.7 and 45.7 millilitres, while correlation was partly preserved. We show that this follows from an invariance property of the objective: ejection fraction is a ratio and is unchanged when both volumes are rescaled, so the loss determines the concept layer only up to scale. Supervision in absolute units reduced volume error from 89.8 to 25.8 millilitres at a cost of 0.4 in ejection fraction error.
Conclusion: Concept accuracy alone can conceal a concept layer that carries no physical scale.
Significance: Interpretable intermediate variables in clinical models should be validated against the invariance structure of the training objective, not only against prediction accuracy.

---


### 182. [Detecting CSAM Text-to-Image LoRAs From Weights](https://arxiv.org/abs/2607.25750)

**<font color=#1a73e8>作者：</font>** David Demitri Africa, Cate Heine, Nadine Staes-Polet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) fine-tuning has made it cheap and easy to customize open-weight image generation models for specific tasks, including the production of child sexual abuse material (CSAM). Existing moderation relies on metadata or generated outputs, but metadata can be deceptive and generating outputs may itself be unacceptable or illegal. We show that a safer signal lives in the weights. The top-left singular vectors of a LoRA's updates form a compact, inference-free fingerprint ($u_1$) of its strongest learned change. Using human-subject age as a benign proxy for CSAM, we find that $u_1$ identifies what a LoRA was trained on, generalizes across base models, and abstains on unrelated benign content. The signal is robust to additive weight noise, rescaling, and precision reduction. These results indicate that harmful LoRAs could be screened directly from their weights without relying on metadata or generating harmful outputs.

---


### 183. [An Embarrassingly Simple Rule-based Visiting Circulation Approach to Trip Destination Prediction](https://arxiv.org/abs/2607.25751)

**<font color=#1a73e8>作者：</font>** Eng-Shen Tu, Yong-Han Chen, En-Chao Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose the Rule-based Visiting Circulation (RVC) model in tackling the challenge in the IEEE Big Data Cup 2022: Trip Destination Prediction. Given trips containing travel information, personal attributes, origin zones, and their features in the training metropolitan areas, the task is to predict the destination of every trip in a targeted metropolitan area whose destinations are not given at all at the training stage. We highlight the challenges in this destination prediction task -- having no knowledge of the destinations in the targeted metropolitan area. We provide insights from the datasets, in which revisiting behaviors and the relationships between origins and destinations play a crucial role in individuals' trips. Hence, we design a simple but comprehensive method, rule-based visiting circulation, which directly utilizes the origin information and individuals' trip behaviors to determine the destinations in the targeted metropolitan area, i.e., requiring no learning from the four training areas. Experimental results on both offline evaluation and leaderboard submission consistently exhibit the proposed RVC can significantly outperform supervised learning methods and other heuristics. The RVC method eventually brings us to second place in the competition leaderboard.

---


### 184. [WorkSurface-Bench: Benchmarking Enterprise Agents on Multi-Surface Knowledge Routing](https://arxiv.org/abs/2607.25765)

**<font color=#1a73e8>作者：</font>** Hao Liang, Meiyi Qiang, Sizhe Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Enterprise agents often need to integrate heterogeneous knowledge sources: documents for narrative facts, tables for computation, and dependency graphs for file relationships. Existing benchmarks typically evaluate retrieval or tool use without distinguishing whether an agent first selects the appropriate knowledge sources. We introduce WorkSurface-Bench, a benchmark for evaluating this capability as surface routing. It contains 1,151 atomic tasks derived from persona-scoped Workspace-Bench-Lite workspaces, spanning document, table, graph, and cross-surface questions. Its reference answers are auditable: table answers are reproduced through executed DuckDB queries, document answers are grounded in verified text spans, and graph answers are traced to source dependency annotations. We evaluate four model backbones across six controlled agent settings, yielding 27,624 protocol-error-free trajectories. Under gold-constrained tool access, agents achieve 98.7-99.8 Route F1, while Answer remains only 56.1-75.3 percent, showing that correct surface selection is necessary but insufficient for task completion. Matched interventions further show that surface hints improve Answer for three of four models, whereas removing irrelevant tools primarily improves routing and efficiency. In an independent three-annotator audit, all 200 sampled tasks pass all six quality criteria by majority vote, with 192 receiving unanimous judgments on every criterion. We release the dataset, construction pipeline, scoring code, and agent harness at this https URL.

---


### 185. [A Unified Benchmark and Modality-Adaptive Network for Day-and-Night Drone-View Geo-Localization](https://arxiv.org/abs/2607.25778)

**<font color=#1a73e8>作者：</font>** Songtianhao Xu, Zhongwei Chen, Zhao-Xu Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most existing drone-view geo-localization (DVGL) benchmarks contain drone imagery captured under a single illumination condition and lack geographically aligned visible drone images, infrared drone images, and satellite images from the same locations. To evaluate the generalization capability of DVGL methods under challenging illumination conditions, some methods train models on a visible benchmark and test them on an independent infrared benchmark. This protocol essentially constitutes transfer between datasets, which makes it difficult to systematically evaluate DVGL across daytime and nighttime conditions within a unified benchmark. To address this limitation, we construct IRCHN,a real-world DVGL benchmark designed for localization across different illumination conditions. IRCHN contains 26,460 images collected from 8,820 geographic locations across four representative scene categories, including farmland, coastline, forest, and urban areas. Each location provides one visible drone image, one infrared drone image, and one corresponding satellite image, which enables unified evaluation of DVGL methods across different illumination conditions and sensing modalities. We further propose the Modality-Adaptive State-Space Transport Relation Network (MASTR-Net), a DVGL framework tailored to localization under varying illumination conditions. MASTR-Net integrates modality-adaptive feature enhancement, bidirectional selective state-space relation modeling, and soft optimal transport relation alignment to jointly reduce modality gaps and view-induced structural discrepancies. Extensive experiments demonstrate that MASTR-Net outperforms existing state-of-the-art methods on IRCHN for localization under varying illumination conditions and achieves competitive performance on two infrared benchmarks, IR-VL328 and CVGL-RGBT. Code: this https URL

---


### 186. [GeoMFD: Continual Drone-View Geo-Localization with Geometry-Aware Adapter and Margin-Field Distillation](https://arxiv.org/abs/2607.25788)

**<font color=#1a73e8>作者：</font>** Zhongwei Chen, Hai-jun Rong, Tao Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing drone-view geo-localization (DVGL) methods are mainly developed under a static training paradigm, where models are optimized for fixed environments with all training data available in advance. However, this paradigm is difficult to extend to real-world deployment, where drones may encounter diverse environments and require multiple environment-specific models, resulting in additional storage and model-selection costs. Directly adapting a single model to new environments also risks distorting previously learned cross-view embedding geometry and causing forgetting. To address these challenges, we formalize the continual drone-view geo-localization (C-DVGL) setting and propose GeoMFD, a geometry-aware continual adaptation method for DVGL. GeoMFD combines a cold-start bootstrapping strategy (CBS), a geometry-aware adapter (Geo-Adapter), and margin-field distillation (MFD) to balance adaptation and cross-view geometry preservation. CBS initializes a stable embedding space, Geo-Adapter enables environment adaptation through controlled residual corrections, and MFD preserves similarity margins between positive pairs and hard negatives to alleviate cross-view geometry forgetting. Extensive experiments demonstrate that GeoMFD effectively mitigates forgetting and achieves competitive performance with environment-specific DVGL methods using a single continuously updated model.

---


### 187. [Towards Faithful Sentimental Image Captioning via Evidence-Aware Multi-Agent Reasoning](https://arxiv.org/abs/2607.25789)

**<font color=#1a73e8>作者：</font>** Tiecheng Cai, Zexian Yang, Chao Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sentimental Image Captioning (SIC) requires balancing emotional expression with visual fidelity. Existing methods often struggle with this trade-off, leading to hallucinations due to insufficient local grounding and the lack of sentimental verification mechanisms. To address these limitations, we propose SEA-Cap, a Sentiment-Evidence-Aware Multi-Agent System for faithful and evidence-grounded sentimental image captioning. SEA-Cap incorporates a Sentiment Evidence Miner that extracts structured, local affective cues to shift sentiment control from global attributes to verifiable object-level evidence. Leveraging this evidence, our framework orchestrates a collaborative workflow where a Generator, Hallucination Checker, and Arbitrator iteratively refine captions via a shared blackboard. By explicitly auditing generated content against mined visual evidence, SEA-Cap ensures both sentiment accuracy and factual consistency. Extensive experiments on two benchmark datasets demonstrate that SEA-Cap effectively mitigates hallucinations and achieves state-of-the-art performance.

---


### 188. [SpectONet: A Physics-Guided Spectral Deep Operator Network for Euler-Bernoulli Beam Dynamics](https://arxiv.org/abs/2607.25790)

**<font color=#1a73e8>作者：</font>** Shivani Saini, Ramesh Kumar Vats, Arup Kumar Sahoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a novel physics-guided spectral deep operator network, termed SpectONet, for solving Euler-Bernoulli beam (EBB) vibration problems. The proposed framework integrates the operator-learning capability of DeepONet with physics-informed constraints and Chebyshev-Gauss-Lobatto (CGL) sensor placement. Unlike conventional DeepONet frameworks, which commonly employ uniformly distributed sensors, SpectONet uses nonuniform spectral sensor locations with a higher concentration of points near the domain boundaries. This sampling strategy improves the finite-dimensional representation of boundary-sensitive structural responses while requiring only a limited number of branch-network inputs. The governing beam equation, together with the associated initial and boundary conditions, incorporated into the training objective to promote physically consistent and generalizable predictions. Numerical experiments on three synthetic EBB vibration problems and a real-world bridge vibration dataset demonstrate the effectiveness of the proposed framework. Comparisons with strong baselines such as, Vanilla DeepONet, PI-DeepONet, PINN, and CNN-UNet show that SpectONet consistently achieves lower prediction errors across all considered evaluation metrics. In particular, SpectONet achieves at least \(64\%\) improvement over the considered baseline models across the three synthetic problems and at least \(37\%\) for the real-world problems. These results demonstrate that SpectONet provides an accurate, computationally efficient, and physically consistent operator-learning framework for structural vibration analysis.

---


### 189. [FLASH: Efficient Impact Fall Detection with Unified Hypergraph State-Space Model](https://arxiv.org/abs/2607.25791)

**<font color=#1a73e8>作者：</font>** Tresor Y. Koffi, Youssef Mourchid, Yohan Dupuis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Falls represent a critical public health challenge, and accurate detection of the impact moment when an individual hits the ground is crucial for timely intervention. Existing skeleton-based methods rely on graph neural networks modeling only pairwise joint connections, failing to capture multi-joint coordination characteristic of fall impacts, while transformer-based temporal models suffer from quadratic complexity limiting real-time deployment. We propose FLASH, a novel framework integrating single-matrix hypergraph representations with Mamba's selective state-space models through adaptive feedback mechanisms for efficient impact detection. Our approach constructs biomechanically-grounded hyperedges to model functional joint coordination while leveraging Mamba's linear-time complexity to capture temporal dynamics. Experiments on UP-Fall and UMAFall datasets demonstrate that FLASH achieves state-of-the-art accuracy with real-time inference capability and strong zero-shot cross-dataset generalization, while significantly reducing computational cost compared to dual-representation and transformer-based methods. The model provides interpretable feedback through learned attention patterns aligned with biomechanical principles. Code is available at this https URL.

---


### 190. [Explicit Layer Modeling for Video Object Insertion and Layer Decomposition](https://arxiv.org/abs/2607.25802)

**<font color=#1a73e8>作者：</font>** Kyujin Han, Seungjoo Shin, Sunghyun Cho  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most video editing systems still lack explicit layered video representations, limiting their ability to perform realistic compositing, object reuse, and consistent manipulation. This limitation is especially pronounced in video object insertion and video layer decomposition, where existing methods rely on implicit inference or per-scene optimization due to the absence of explicit foreground-layer supervision. We introduce TriLayer, a large-scale triplet video dataset containing aligned composite, background, and foreground videos, where the foreground layers include both object appearance and associated visual effects. This explicit supervision enables models to learn layered video representations directly rather than inferring them implicitly. Building on this dataset, we propose DBL-Diffusion, a dual-branch diffusion framework that jointly models RGB composites and RGBA foreground layers through shared denoising and cross-branch interaction. We instantiate the framework in two tasks: DBL-Insert for layered object insertion, which generates explicit RGBA layers for realistic compositing and flexible post-editing, and DBL-Decompose for video layer decomposition, which recovers foreground and background layers using triplet supervision. Experiments demonstrate that explicit layer modeling substantially improves both insertion fidelity and decomposition quality.

---


### 191. [Freq-RemoteVAR: Next-Frequency Autoregressive Modeling for Remote Sensing Change Detection](https://arxiv.org/abs/2607.25815)

**<font color=#1a73e8>作者：</font>** Luqi Gong, Rui Xu, Yue Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing change detection aims to identify land-cover changes from bi-temporal images. Most existing methods follow a one-shot dense prediction paradigm, directly regressing a change mask from fused features. However, such approaches overlook the intrinsic frequency characteristics of change patterns. We propose Freq-RemoteVAR, a frequency autoregressive framework that reformulates change detection as a structured generation problem in the frequency domain. Instead of predicting the change mask in a single step, we introduce a next-frequency prediction paradigm, where change information is progressively generated from coarse to fine. We design a frequency-aware mask tokenization strategy that decomposes change supervision into multi-frequency token targets via Fourier transformation and quantization. We develop a Frequency VAR Transformer, which performs causal autoregressive modeling over frequency tokens. The model starts from learned mask queries and progressively predicts frequency-level tokens conditioned on previously generated tokens and bi-temporal image features, effectively capturing long-range dependencies across frequency scales. We introduce Scale-Aligned RoPE Cross Attention (SRCA) module, which aligns frequency-domain mask queries with spatial-domain bi-temporal features under a unified coordinate system, enhancing spatial-frequency consistency during generation. We propose a Change-quality Control module that adaptively modulates the generation process through dynamic normalization, attention biasing, and spatial offset adjustment, thereby suppressing pseudo-change responses and improving robustness. Extensive experiments on CDD, GZ-CD, and LEVIR-CD demonstrate that Freq-RemoteVAR consistently outperforms existing methods, particularly in challenging scenarios with complex appearance variations and noisy disturbances.

---


### 192. [CHILL-Harness: Counterfactual Harness Learning for Efficient Reasoning in Long-Horizon Agents](https://arxiv.org/abs/2607.25825)

**<font color=#1a73e8>作者：</font>** Jiarun Fu, Lizhong Ding, Sida Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agent harnesses have become the operational infrastructure of modern large language model agents, coordinating context, tools, verification, and execution control to translate latent model capability into reliable long-horizon behavior. However, reliable long-horizon behavior requires harness control to adapt to task demands, execution environments, and evolving execution states, whereas current harnesses predominantly rely on hand-crafted or globally fixed policies; this mismatch manifests as unnecessary computational overhead and, in adverse cases, reduced task success. To address this limitation, we formulate the task of enabling adaptive orchestration in harness systems as a causal learning problem and propose Counterfactual Harness Intervention Learning for Long-Horizon Agents (CHILL-Harness). CHILL-Harness intervenes at the orchestration layer to enable advantage-guided workflow adaptation, thereby improving reasoning and execution efficiency while preserving task performance. Specifically, we develop causal intervention effect learning as the effect-estimation component of CHILL-Harness to estimate intervention-relative workflow advantage from confidence-weighted execution evidence and identify advantageous workflow adaptations. We further introduce advantage-realizing causal orchestration as its realization component to adaptively allocate counterfactual reasoning and realize only workflow adjustments supported by sufficient expected advantage. Finally, we incorporate a success-preserving objective and advantage-margin authorization constraints into CHILL-Harness to promote reliable adaptation. Extensive experiments on heterogeneous long-horizon tasks spanning information seeking, software engineering, and terminal interaction show that CHILL-Harness consistently preserves or improves task success while substantially reducing token consumption and execution time.

---


### 193. [Prototype Adaptation for Zero-Shot sEMG Movement Classification](https://arxiv.org/abs/2607.25826)

**<font color=#1a73e8>作者：</font>** Rui Liu, Benjamin Paassen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Surface electromyography (sEMG) enables the control of prostheses, allowing upper-limb amputees to re-gain some hand function. Most current research focuses on recognizing basic movements for prosthesis control. However, in most daily activities, such as opening a door, combined movements are essential. However, collecting training data for all possible combined movements is time-consuming and requires re-training of the model for any new combination. We propose two novel recognition approaches, Compositional Prototype Interpolation (CPI) and Synthetic Adaptation for Prototypes (SAP), that enable zero-shot learning of combined, novel and unseen movements in Prototype Networks after training only with basic movements. Our methods rest on a linear interpolation assumption in the embedding space, which we study by inspecting the geometry of combined motions in signal and embedding space. In experiments on the NearLab and NinaPro DB3 data sets as well as our newly recorded BasCom dataset, our proposed SAP outperforms prior zero-shot learning methods with accuracy improvements on combined movements of more than 20%. This advantage is maintained in online inference experiments in a user study.

---


### 194. [Beyond Static Costs: Learning-Dynamics Aware Loss Functions for Long-Tailed Classification](https://arxiv.org/abs/2607.25830)

**<font color=#1a73e8>作者：</font>** Varad Shinde, Nikhil Kumar Shrey, Magesh Rajasekaran 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models in computer vision face significant challenges when trained on long-tailed datasets, where a few majority classes dominate while many minority classes are severely underrepresented. Such imbalances frequently arise in real-world scenarios such as rare species recognition, manufacturing fault detection, and medical image understanding, leading to biased models that underperform on tail classes. Existing reweighting methods typically rely on static class frequencies to penalize the model, ignoring the dynamic nature of how effectively a network actually learns a class over time. We address this by introducing a novel Learning-Dynamics Aware Loss (LDAL) function that shifts the focus from static sample counts to dynamic learning progress. LDAL framework adjusts class weights continuously by leveraging: (i) the strength of learned feature representations (semantic scale), (ii) the intrinsic learning difficulty of each class, measured via the Shannon entropy of its predictions, and (iii) an inter-epoch regularizer term that tracks prediction shifts between consecutive epochs to stabilize training and avoid local minima. LDAL is purely a objective function which incurs negligible computational overhead while adapting to the feature learning of the model. Experimental results on multiple benchmark datasets demonstrate that our approach significantly surpasses state-of-the-art reweighting loss functions, providing an optimal trade-off between accuracy and generalizability. The source code is available at this https URL

---


### 195. [Distributed Constraint Optimization via Online Learning and Iterative Pricing with Application to Large-Scale Satellite Scheduling](https://arxiv.org/abs/2607.25835)

**<font color=#1a73e8>作者：</font>** Itai Zilberstein, Pranav Rajbhandari, Steve Chien 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Distributed constraint optimization problems (DCOPs) provide a popular framework for distributed decision making under limited communication, but many real-world instances are too large to solve monolithically. We address this challenge from two complementary directions. We revisit the connection between DCOPs and potential games, and adapt modern online learning algorithms for equilibrium finding to DCOPs. We show that these algorithms are competitive with representative incomplete DCOP algorithms. We then turn to decomposition frameworks for large-scale DCOPs, motivated by large-scale decentralized satellite scheduling. We propose a new framework that separates a DCOP into two interacting subproblems: a high-level meta-DCOP for task allocation, and independent local optimization problems for scheduling. To couple the two levels, we develop a novel iterative pricing method that updates the meta-level utilities using feedback from the local optimizers. Combining our online learning methods with our iterative pricing framework, we obtain near-optimal performance on real-world decentralized satellite scheduling problem instances, fulfilling over 99% of observation requests compared with 87% for state-of-the-art baselines.

---


### 196. [Adversarial Deepfake Generation and an Investigation of Purification-Based Adversarial Detection](https://arxiv.org/abs/2607.25842)

**<font color=#1a73e8>作者：</font>** Junghyun Kim, Seunghyun Kim, Jiyoung Woo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper describes the participation of team "Go To Germany" in the ImageCLEF 2026 Deepfake Detection and Generation Task. For the image generation task, we employ FLUX.1-dev with PuLID for identity-preserving face synthesis, combined with a multi-model PGD adversarial attack targeting 12 detectors simultaneously (DiffJPEG-in-loop, MI/DI/EoT, adaptive weighting, two-stage warm-start). Our approach achieved 90% evasion against organizer detectors and 57.6% against participant detectors, with a final generation score of 0.4170. For the image detection task, we combine two complementary detectors - SigLIP+DINOv2 for AI-generated images and GenD-DINOv3 for face manipulations - in a max-probability ensemble, achieving 99.4% accuracy on baseline deepfakes but suffering from high false-positive rates on real images, resulting in a final detection score of 0.6986. Beyond the official submission, we conducted a self-initiated investigation of purification-based adversarial detection, comparing three families of detection signals across six detectors that share a CLIP ViT-L/14 backbone. We find that raw $|\Delta \text{logit}|$ under median-3 purification, applied through the EFFORT detector, separates adversarial inputs from clean inputs with AUROC 0.81-0.98 across four adversarial source types - a finding that refutes the simple backbone-preservation hypothesis and exposes a sharp JPEG-quality cliff at Q70 where the signal collapses.

---


### 197. [AngelSpec: Towards Real-World High Performance Inference with Speculative Decoding](https://arxiv.org/abs/2607.25852)

**<font color=#1a73e8>作者：</font>** Hong Liu, Rui Cen, Junhan Shi 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model inference without changing the target distribution, but no single drafting structure performs best across real-world workloads. Autoregressive multi-token prediction (MTP) is a lightweight, stable proposal mechanism, whereas block-parallel diffusion amortizes drafting latency over much longer candidate sequences; the better choice depends strongly on the output distribution. We present AngelSpec, a unified training framework for MTP and block-parallel speculative decoding that addresses this heterogeneity at three levels. At the training level, rather than fitting one universal drafter to a uniform data mixture, we co-specialize structure and data: the MTP drafter is trained on diverse conversational data for high-entropy open-ended chat, and the block-diffusion drafter on code and mathematics data for longer predictable continuations. At the architecture level, we propose DFly, a block-diffusion framework combining a hybrid target-conditioning backbone with a predecessor-conditioned autoregressive head, improving target-feature utilization and intra-block dependency modeling while keeping generation parallel. At the inference level, both acceptance length and verification cost vary with domain, request, online load, and hardware, so DFly treats verification as a shared batch-level resource: it reallocates compute toward high-confidence prefixes across requests and combines expected utility with a profiled cost model to adapt verification depth online. Across the Hy3 series, DFly raises the average accepted length on Hy3-A21B by roughly 30% and attains the highest average throughput at every tested concurrency from 4 to 64, a 1.98-2.40x speedup over autoregressive decoding and 10.5-11.8% higher throughput than DFlash. We release AngelSpec to support training and extending these methods.

---


### 198. [Shieldstral](https://arxiv.org/abs/2607.25857)

**<font color=#1a73e8>作者：</font>** Antonia Calvi, Avinash Sooriyarachchi, Giada Pistilli 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Shieldstral, a 3B-parameter policy-adaptive multimodal safety classifier that matches or outperforms models nearly 7$\times$ its size on text safety benchmarks and sets a new state of the art on multimodal safety classification. Shieldstral formulates content moderation as a binary question-answering task. This simple formulation unifies diverse moderation tasks into a single yes/no problem, enabling heterogeneous safety datasets with divergent taxonomies to be consolidated under one training framework. We present the data construction recipe, covering curation and generation of approximately 54.1M samples and a fine-grained evaluation set to evaluate policy adaptability. Together, these enable a small adaptive model to match or outperform much larger models.

---


### 199. [Open-Ended CT Volume Segmentation with Weak Supervision from Language](https://arxiv.org/abs/2607.25860)

**<font color=#1a73e8>作者：</font>** Sanjay Subramanian, Junwei Yu, Zirui Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce a method for training a text-conditioned segmentation model for CT scans, which combines voxel-level supervision with coarse but scalable slice-level supervision from reports. We extract, from a large database of scan-report pairs, descriptions of findings with indices of slices where those findings occur. We then finetune a general-purpose 2D image segmentation model, SAM3, with standard segmentation losses from strongly labeled data and with a slice-level classification loss from the extracted weak supervision. Our results on the ReXGroundingCT dataset illustrate that this strategy improves the segmentation dice score: from an 8% relative gain when there are 1000 fully labeled volumes to 22% when there are 250 fully labeled volumes.

---


### 200. [DRIFT: Direct-Recursive Intervention-Conditioned Forecasting of ICU Physiological Trajectories](https://arxiv.org/abs/2607.25864)

**<font color=#1a73e8>作者：</font>** Weixin Liu, Juming Xiong, Congning Ni 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many time-series forecasts depend not only on prior observations but also on actions specified during the forecast period. In intensive care units (ICUs), future vital signs and laboratory values are influenced by treatments such as vasopressors. However, models that predict the full future sequence all at once make little use of these treatments, whereas autoregressive models can accumulate errors. We introduce DRIFT, a hybrid framework in which a direct model produces the primary forecast and a recursive, action-conditioned model contributes constrained corrections. We evaluate DRIFT on 6,046 admissions from MIMIC-IV and 8,345 admissions from eICU-CRD. Averaged across the 8-, 24-, and 48-hour forecast endpoints, DRIFT reduces mean absolute error for mean arterial pressure (MAP) by 0.673% relative to an action-conditioned Temporal Fusion Transformer (TFT-action) on MIMIC-IV and achieves the lowest corresponding error among the compared models on eICU-CRD. Although the overall accuracy improvement is modest, a MIMIC-IV audit restricted to windows in which the supplied treatment sequence was altered showed that DRIFT achieved lower observed-target MAP error than TFT-action at 8 and 24 hours. Treatment-sequence alteration increased DRIFT's MAP error by 0.21-0.26 mmHg more than it increased TFT-action's error, with prediction changes occurring primarily after the supplied paths diverged. In a separate robustness experiment, the MAP advantage persisted under three shared checkpoint-selection rules emphasizing overall endpoint error, MAP error, or both equally.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-229](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
